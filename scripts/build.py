"""build.py -- merge verified research files into the tracker and render the site.

Inputs:
  data/positions.json   the tracker's own list (status and notes live here, never overwritten by a merge)
  data/countries.json   country scores (visa, work after PhD, economy)
  --merge FILE...       new research JSON files (lists of position objects) to fold in

Outputs:
  index.html            one self-contained page (data embedded, works from disk and on GitHub Pages)
  README.md             the same data as Markdown tables, readable on github.com in a private repo

usage: python scripts/build.py [--merge a.json b.json ...]
"""
import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POS = ROOT / "data" / "positions.json"
COUNTRIES = ROOT / "data" / "countries.json"
TEMPLATE = ROOT / "scripts" / "template.html"
STATUSES = ["new", "shortlist", "emailed", "applied", "interview", "offer", "rejected", "skip", "expired"]
KEEP = ("status", "notes", "added", "history")


def slug(p):
    base = f"{p.get('institution', '')}-{p.get('pi', '')}-{p.get('title', '')}"
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")[:90]


def load(path, default):
    return json.loads(path.read_text(encoding="utf8")) if path.exists() else default


def merge(existing, new_items, today):
    by_id = {p["id"]: p for p in existing}
    added = updated = 0
    for raw in new_items:
        p = dict(raw)
        p["id"] = p.get("id") or slug(p)
        if p["id"] in by_id:
            old = by_id[p["id"]]
            for k in KEEP:
                if k in old:
                    p[k] = old[k]
            by_id[p["id"]] = {**old, **p}
            updated += 1
        else:
            p.setdefault("status", "new")
            p.setdefault("notes", "")
            p.setdefault("added", today)
            by_id[p["id"]] = p
            added += 1
    return list(by_id.values()), added, updated


def mark_expired(items, today):
    for p in items:
        d = str(p.get("deadline", ""))
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) and d < today and p.get("status") in ("new", "shortlist"):
            p["status"] = "expired"
    return items


def sort_key(p):
    d = str(p.get("deadline", ""))
    dated = re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) is not None
    return (p.get("status") in ("expired", "skip", "rejected"), not dated, d, -float(p.get("fit_1_10") or 0))


def md_escape(s):
    return str(s or "").replace("|", "/").replace("\n", " ")


def readme(items, countries, today):
    adverts = [p for p in items if p.get("type") == "advert"]
    cold = [p for p in items if p.get("type") == "cold-email"]
    out = [f"# PhD tracker\n\nLast updated {today}. Open `index.html` for the full view with filters.\n"]
    if countries:
        out.append("## Countries\n\n| Rank | Country | Visa from Iran | Work after PhD | Economy | Note |\n|---|---|---|---|---|---|")
        for c in sorted(countries, key=lambda c: c.get("rank", 99)):
            out.append(f"| {c.get('rank', '')} | {c['country']} | {c.get('visa', '')} | {c.get('work', '')} | {c.get('economy', '')} | {md_escape(c.get('note'))} |")
        out.append("")
    out.append("## Open positions\n\n| Deadline | Fit | Status | Country | Institution | PI | Position |\n|---|---|---|---|---|---|---|")
    for p in sorted(adverts, key=sort_key):
        out.append(f"| {p.get('deadline', '')} | {p.get('fit_1_10', '')} | {p.get('status', '')} | {p.get('country', '')} | "
                   f"{md_escape(p.get('institution'))} | {md_escape(p.get('pi'))} | [{md_escape(p.get('title'))}]({p.get('apply_url', '')}) |")
    out.append("\n## Cold-email targets\n\n| Fit | Status | Country | Institution | PI | Topic |\n|---|---|---|---|---|---|")
    for p in sorted(cold, key=lambda p: -float(p.get("fit_1_10") or 0)):
        out.append(f"| {p.get('fit_1_10', '')} | {p.get('status', '')} | {p.get('country', '')} | {md_escape(p.get('institution'))} | "
                   f"[{md_escape(p.get('pi'))}]({p.get('pi_url', '')}) | {md_escape(p.get('topic'))} |")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--merge", nargs="*", default=[])
    args = ap.parse_args()
    today = dt.date.today().isoformat()
    items = load(POS, [])
    for f in args.merge:
        new = json.loads(Path(f).read_text(encoding="utf8"))
        items, a, u = merge(items, new, today)
        print(f"{f}: {a} added, {u} updated")
    items = mark_expired(items, today)
    for p in items:
        if p.get("status") not in STATUSES:
            sys.exit(f"bad status {p.get('status')!r} in {p['id']}")
    items.sort(key=sort_key)
    POS.write_text(json.dumps(items, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
    countries = load(COUNTRIES, [])
    payload = json.dumps({"positions": items, "countries": countries, "updated": today, "statuses": STATUSES}, ensure_ascii=False)
    page = TEMPLATE.read_text(encoding="utf8").replace("/*DATA*/null", payload.replace("</", "<\\/"))
    (ROOT / "index.html").write_text(page, encoding="utf8")
    (ROOT / "README.md").write_text(readme(items, countries, today), encoding="utf8")
    print(f"{len(items)} entries, {sum(p.get('type') == 'advert' for p in items)} adverts, wrote index.html and README.md")


if __name__ == "__main__":
    main()
