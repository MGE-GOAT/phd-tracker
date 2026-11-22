# PhD Visa/Work/Economy Policy Research — Iranian Applicant (as of 2026-11-22)

**Verification note:** The shared WebSearch budget was exhausted during this task (consumed by parallel sub-teams). Rumour-task findings below come from direct page fetches today (2026-11-22) by sub-agents, forwarded through the team lead. The 21-country table largely carries forward a same-day verified sweep from 2026-08-13 (session 64968889-7b3d-41d1-986f-e7a6d3b098ed), supplemented by domain knowledge where no fresh fetch was possible this session. Every row below is flagged **[verified 2026-11]**, **[carried from 2026-08, not re-checked]**, or **[unverified, domain knowledge only]**. Treat the latter two as needing a follow-up fetch before acting.

---

## TASK 1 — The rumour: "Iranian students won't need an English test, they can take it after arriving"

### Verdict: **FALSE as a general rule.** No primary source supports deferring the test until after arrival. The real picture is narrower and different: (a) one generic visa-info page makes an unsupported blanket claim, (b) a handful of specific universities grant *temporary alternative-test* accommodations (not a deferral), and (c) the underlying problem is real — most standardized English tests have become hard to sit *inside Iran*, not that they've become optional.

**Evidence, each with exact quote, URL, and date seen (2026-11-22 unless noted):**

1. **Mastersportal Iran→Finland page** — `https://www.mastersportal.com/visa-info/110-9/students-from-iran-to-finland.html` (HTTP 200).
   Quote: *"Iranian students won't have to prove they speak English well enough to study in an international university in Finland."*
   This sentence sits in the page's **residence-permit** section, not the admissions section, and never mentions PhD study specifically. No real date on the page beyond a generic "2007–2026" copyright footer. **Confirmed templated boilerplate**: the India→Finland URL on the same site returns the *identical* sentence, including the word "Iranian" in the templated text — i.e., the page did not actually tailor the claim to Iran. This is not a usable source for an admissions policy; it looks like an auto-generated visa-info page with a copy-paste bug.

2. **University of Waterloo** — one admissions page states: *"Due to the recent restrictions in Iran, the University of Waterloo is temporarily accepting"* the Oxford ELLT as an alternative English-proficiency test. No visible date, footer says 2026. This is a real, specific, named accommodation — but it is a **substitute test taken before enrollment**, not a deferral to "after arriving." Other Waterloo admissions pages checked were JS-rendered shells or 404s, so the exact scope (which programs, grad vs. undergrad, PhD included or not) could not be confirmed from the fetched pages.

3. **Iran International, 30 Aug 2026** (`https://www.iranintl.com/en/202608308422`): *"IELTS, which now appears to be one of the few remaining major options for Iranian applicants."* — implies most *other* tests had already become hard to access in Iran by August, while IELTS was still relatively available.

4. **RFE/RL, 10 Nov 2026** (`https://www.rferl.org/a/iran-english-test-abroad-sanctions/33893817.html`): *"International language tests have all but vanished from Iran over the past year."* (Note: this single successful fetch is the only rferl.org access that succeeded; later attempts at the same domain were refused by the fetch tool, so this is a one-source quote, not independently cross-checked today.)

5. **ETS Iran testing-update page** (`https://www.ets.org/iran-testing-update.html`) — **could not be read**; the fetch failed with a header-overflow error both times it was tried. Its content remains unverified either way.

6. **IELTS.org** — the test-centre finder (`ielts.org/test-centres`) lists "Iran, Islamic Republic of" in its country dropdown, but actual open centres were not visible from a direct fetch. IELTS news pages (checked through 2026-10-01) contain **no mention of Iran** at all — no suspension notice, no accommodation notice.

7. **Duolingo English Test, Oxford ELLT (ELLT Global), LanguageCert, PTE** — centre-finder/country-list pages for all four either rendered as JavaScript shells, 404'd, or had their target domain refused by the fetch tool. **Status of each in Iran is UNVERIFIED from today's online sources.**

8. **Wikipedia** (IELTS page, Education in Iran page) — neither page mentions a 2026 IELTS suspension in Iran.

9. **Times Higher Education** article titled something like "English language test ban Iran unfair and counterproductive" appears to exist (found via its headline) but its domain refused the fetch tool, so its content is unread/unverified.

### What this actually means for the applicant
- There is **no evidence of a blanket policy** letting Iranian applicants skip the English requirement and test after arrival. Treat the rumour as false.
- There **is** a real, narrower phenomenon: access to test centres *inside Iran* has become unreliable for several of the major tests over the past year (RFE/RL, Iran International), prompting **individual universities** (Waterloo is the one confirmed case here) to grant **named alternative tests** (e.g., Oxford ELLT) as a substitute — still taken before enrollment, not deferred.
- Because the exact current status of IELTS/TOEFL/Duolingo/PTE/LanguageCert/Oxford ELLT access from inside Iran could not be independently confirmed from the available online sources today, **the applicant should verify locally in Tehran** (test-centre booking sites, British Council Tehran, or Swiss/EU-embassy-adjacent testing agents) before assuming any test is or isn't sittable — this is explicitly flagged as **unverified** rather than resolved.
- Practical fallback path if local testing is unreliable: look for specific universities (follow Waterloo's lead) offering alternate tests, online/home tests not requiring a physical Iran test centre (if any such option survives further verification), or conditional admission with a later-dated test requirement **confirmed in the official letter**, not assumed from a rumour.

---

## TASK 2 — Country assessment (1–10 scores: A=visa from Iran, B=work rights after PhD, C=economy; overall = A-weighted average, A×1.5)

| Rank | Country | A (visa) | B (work) | C (economy) | Status flag |
|---|---|---|---|---|---|
| 1 | Belgium | 8 | 7 | 7 | carried 2026-08 |
| 2 | Finland | 8 | 7 | 6 | carried 2026-08 |
| 3 | Switzerland | 6 | 7 | 9 | unverified, domain knowledge |
| 4 | Norway | 6 | 8 | 8 | unverified, domain knowledge |
| 5 | Austria | 7 | 7 | 7 | carried 2026-08 |
| 6 | Luxembourg | 5 | 7 | 9 | unverified, domain knowledge |
| 7 | United Kingdom | 6 | 6 | 7 | carried 2026-08 |
| 8 | Sweden | 6 | 6 | 7 | carried 2026-08 |
| 9 | Germany | 4 | 8 | 8 | carried 2026-08 |
| 10 | Poland | 7 | 5 | 5 | carried 2026-08 |
| 11 | Canada | 3 | 7 | 8 | carried 2026-08 |
| 12 | Italy | 6 | 5 | 5 | unverified, domain knowledge |
| 13 | Spain | 6 | 5 | 5 | unverified, domain knowledge |
| 14 | Netherlands | 2 | 8 | 8 | carried 2026-08 |
| 15 | Denmark | 2 | 7 | 8 | carried 2026-08 |
| 16 | Hungary | 6 | 4 | 4 | unverified, domain knowledge |
| 17 | Australia | 1 | 7 | 8 | carried 2026-08 |
| 18 | Ireland | 2 | 6 | 7 | carried 2026-08 |
| 19 | Estonia | 3 | 5 | 5 | carried 2026-08 (Baltic citizenship-renunciation issue) |
| 20 | Czechia | 2 | 5 | 5 | carried 2026-08 |
| 21 | Portugal | 2 | 4 | 4 | carried 2026-08 |

### What changed since the August 2026 sweep
- **Nothing in this table has been actively re-verified for Nov 2026** — the shared WebSearch budget was consumed by other sub-teams before country-specific re-checks could run, and direct-fetch attempts at migration-agency/embassy pages were not completed for this deliverable. The ranking above is the August 2026 verified baseline, carried forward, plus best-effort estimates for countries not covered in August (Switzerland, Norway, Luxembourg, Italy, Spain, Hungary) marked "unverified, domain knowledge."
- **Known as of August 2026** (unconfirmed whether still true): Germany's Tehran visa section frozen, §16b/§18d waitlists opened 15 Jul 2026, queued by registration date; Belgium/Finland/Austria/Poland open and filing from Tehran; Czechia's Tehran section closed 19 Jul 2026; Netherlands MVV suspended; France's embassy evacuated; Denmark not fileable from Iran plus PET screening; Canada 1–4 year security screening; Australia sealed.
- **Action needed before relying on this table**: re-fetch each target country's migration-agency and Tehran-embassy page directly (not via search) to confirm whether these August-2026 statuses still hold in November 2026 — this file should be treated as a draft pending that follow-up, not a final answer.

### Sensitive/dual-use flag
The applicant's profile (embedded ML, edge AI, biomedical signal processing) sits close to categories some countries screen heavily for Iranian nationals in sensitive/dual-use technology — most notably the **UK's ATAS** requirement (many CS/EE/biomedical-engineering subjects require an Academic Technology Approval Scheme certificate for Iranian nationals, and denial is an opaque risk) and the **Netherlands' knowledge-security screening** for sensitive technology fields. This was not independently re-verified today; treat it as a known risk to re-check per target program, not a settled fact.
