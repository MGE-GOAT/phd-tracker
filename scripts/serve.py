#!/usr/bin/env python3
"""Local tracker server. Serves the site on http://localhost:8765 and records every
"Open in Gmail" click and every "Mark as sent" tick into data/progress.json (current
state) and data/progress.log (history). Each change is committed and pushed to GitHub.
Nothing here holds a token. It listens on this computer only.

usage: python3 scripts/serve.py
"""
import datetime as dt
import functools
import http.server
import json
import os
import subprocess
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(os.environ.get("TRACKER_PORT", "8765"))
NOPUSH = os.environ.get("TRACKER_NOPUSH") == "1"
PROG = ROOT / "data" / "progress.json"
LOG = ROOT / "data" / "progress.log"
PUSH_URL = "ssh://git@ssh.github.com:443/MGE-GOAT/phd-tracker.git"
HOSTS = {f"localhost:{PORT}", f"127.0.0.1:{PORT}"}
ORIGINS = {f"http://{h}" for h in HOSTS}
KINDS = {"sent", "opened"}
lock = threading.Lock()
push_timer = None


def now():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan_steps():
    return {s["id"]: s for s in json.loads((ROOT / "data" / "plan.json").read_text(encoding="utf8"))["steps"]}


def load_progress():
    try:
        return json.loads(PROG.read_text(encoding="utf8"))
    except (OSError, ValueError):
        return {"sent": {}, "opened": {}, "updated": ""}


def record(kind, step_id, on):
    steps = plan_steps()
    step = steps[step_id]
    with lock:
        p = load_progress()
        bucket = p.setdefault(kind, {})
        if on:
            if kind == "sent":
                bucket.setdefault(step_id, now())
            else:
                bucket[step_id] = now()
        else:
            bucket.pop(step_id, None)
        p["updated"] = now()
        tmp = PROG.with_suffix(".tmp")
        tmp.write_text(json.dumps(p, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
        tmp.replace(PROG)
        entry = {"at": now(), "kind": kind, "on": bool(on), "id": step_id, "who": step.get("who"), "to": step.get("address")}
        with LOG.open("a", encoding="utf8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    schedule_push()


def push_now():
    if NOPUSH:
        return
    try:
        run = lambda *a: subprocess.run(a, cwd=ROOT, capture_output=True, text=True, timeout=150)
        run("git", "add", "data/progress.json", "data/progress.log")
        if run("git", "diff", "--cached", "--quiet").returncode == 0:
            return
        run("git", "commit", "-q", "-m", "Progress update")
        r = run("git", "push", PUSH_URL, "main")
        print("push:", "ok" if r.returncode == 0 else r.stderr.strip()[:200], flush=True)
    except Exception as e:  # keep the server alive whatever happens
        print("push failed:", e, flush=True)


def schedule_push():
    global push_timer
    if push_timer:
        push_timer.cancel()
    push_timer = threading.Timer(8.0, push_now)
    push_timer.daemon = True
    push_timer.start()


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass

    def _reject(self, code, msg):
        self.send_response(code)
        self.end_headers()
        self.wfile.write(msg.encode())

    def do_POST(self):
        if self.path != "/api/event":
            return self._reject(404, "not found")
        # Only this page may write. The custom header forces a CORS preflight, so other
        # websites open in your browser cannot post here, and the host check stops DNS tricks.
        if self.headers.get("Host") not in HOSTS or self.headers.get("Origin") not in ORIGINS or self.headers.get("X-Tracker") != "1":
            return self._reject(403, "forbidden")
        try:
            n = int(self.headers.get("Content-Length", "0"))
            if not 0 < n <= 2000:
                raise ValueError
            body = json.loads(self.rfile.read(n))
            kind, step_id, on = body["kind"], body["id"], bool(body.get("on", True))
            if kind not in KINDS or step_id not in plan_steps():
                raise ValueError
        except (ValueError, KeyError, TypeError):
            return self._reject(400, "bad request")
        record(kind, step_id, on)
        self.send_response(204)
        self.end_headers()


def main():
    handler = functools.partial(Handler, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler)
    print(f"Tracker running. Open http://localhost:{PORT}/  (Ctrl+C to stop)", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        push_now()


if __name__ == "__main__":
    main()
