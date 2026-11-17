# Absence Audit Brief — every "Not public" re-tested

The verification pass of **SETTLED** found that the commonest error in the book was an over-confident statement of absence: "Not public", "publishes nothing", "no page found", "does not say". Several were wrong because the first searches relied on the providers' `llms.txt` documentation indexes, which are incomplete (ruling 39). Your job: re-test every statement of absence on your assigned pages with a wide search, and correct those that are wrong.

REPO = `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (run scripts from there). ROOT = `REPO/_journals/payments-platform-architecture/`.

## Read first
`ROOT/_research/consistency-issues.md` (all rulings; many record an absence already overturned, and what the provider does publish), and for each assigned page its `ROOT/_research/verification/<folder>.md` (it records where the verifier searched).

## Per page
1. List every statement of absence about a real company, network or regulator: in the prose, in "Where They Differ" table cells, in "Where the Evidence Stops" lists, in take-aways, captions and the Sources notes. Grep for: not public, not found, none found, no … found, not published, publishes no, has published no, nothing public, not documented, does not say, does not state, not stated, no first-party, silent on. Skip Larkfield.
2. For each, decide whether the verification file shows a WIDE search already (documentation sitemap or site search, help center, company site and engineering blog, and a web search restricted to the provider's domains). If yes, mark it "already wide" and move on. If the search was narrow (index only) or not recorded, search now in all of: `docs.<provider>.com` (sitemap and `.md` pages), `support.stripe.com` / `help.adyen.com`, `stripe.com` (incl. `/blog/engineering`, `/newsroom`, `/guides`, `/sessions`), `adyen.com` (incl. `/knowledge-hub`, `/press-and-media`, `/infrastructure`, investor pages) and `medium.com/adyen`, and web searches restricted to those domains with two or three phrasings. Conference talks and podcasts by named employees count as first-party statements if you can read or hear a transcript; say which.
3. Classify: **holds** (wide search, nothing found: make sure the sentence says what was searched in a few words where the page's style does, e.g. "no first-party statement found in documentation, help center or engineering posts, November 2026"; do not lengthen sentences that already scope themselves); **overturned** (the provider does publish it: replace the absence with the fact, dated and attributed in the sentence, add the source to Sources and Evidence in the page's format; no external URL in running text); **narrowed** (part is published: say which part and what remains unpublished).
4. Keep the page within its spec's `max_words` (trim connective sentences, never evidence), keep units unchanged, update a unit's `controlling_idea`/`evidence` in `spec.json` if an overturned absence changes it, and add one changelog line dated 2026-11-17 to the spec. If an overturned absence makes a sentence of the page's journal-spec-locked fields (intent, acceptance criteria, thesis, role) false, do not edit those: report them.

## Limits
Edit only your pages' `index.md` and `spec.json`, and write `ROOT/_research/absence-audit/<folder>.md` (table: statement | where searched | result | change). Never put the user's name, email or any personal identifier in a request; use a generic User-Agent.

## Finish
`python3 _wiring/validate_spec.py payments-platform-architecture <folder>` ok; `python3 _wiring/check_draft.py structure <post-dir>` passes; build has no errors.

## Report back
Under 250 words: per page, counts (holds / overturned / narrowed / already wide); each overturned or narrowed statement in one line (was → now, source); locked journal-spec sentences now false; other pages that repeat an overturned absence.
