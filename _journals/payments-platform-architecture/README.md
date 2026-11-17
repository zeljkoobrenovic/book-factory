# SETTLED — Manuscript Workspace

**SETTLED: Architecting Payments and Revenue Infrastructure**

How payment and revenue infrastructure is actually built: how a payment is authorized, cleared, settled, recorded, paid out and disputed; how the APIs, ledgers, vaults, risk systems and billing engines behind it work; and where Stripe and Adyen made different architectural bets, and why. Written for engineers and architects who are new to payments.

## Layout

- `config.yaml` — reading order, **68 configured pages**. Public permalinks are stable.
  - Preface: 4 pages (introduction, how paying got this complicated, the failure patterns, the fictional company).
  - Parts I–X: each opens with an unnumbered part introduction; 50 chapters in folders `01`–`50` (Part IX is four end-to-end journeys; Part X holds the Stripe and Adyen cases, the comparison, the contrast cases and the outlook).
  - Reference: domain coverage, toolkit, glossary, bibliography.
- `PLAN.md` — positioning, structure, the teaching discipline and one contract per chapter.
- `journal-spec.json` — the outcome spec for the journal, its parts and its pages (thesis, role, flow, transitions). Authored before the prose.
- `posts/<folder>/index.md` + `spec.json` (+ `check-report.json`) — each page, the outcome spec it was written from and the report of the draft check (see "Outcome specs" in the repository `CLAUDE.md`).
- `_research/` — private working material, not published:
  - `style-guide.md` — audience and voice, format, evidence discipline, the required "Stripe and Adyen: Where They Differ" section, the three take-away tiers, figure rules, the sixteen failure-pattern names, valid permalinks.
  - `scenario-ledger.md` — canonical facts about **Larkfield**, the fictional running example. Pages must agree with it.
  - `RESEARCH-BRIEF.md`, `WRITER-BRIEF.md`, `REVIEWER-BRIEF.md` and other `*-BRIEF.md` files — instructions given to the AI research, writing, review and illustration sessions.
  - `brief-*.md` — verified research briefs. Claims are tagged VERIFIED / WIDELY REPORTED / ASSUMPTION with publication dates and evidence-age flags.
  - `tools/render_check.py` — loads built pages in Playwright and reports unresolved or disallowed cross-journal links.
  - `bib-tools/`, `glossary-tools/` — generators for the bibliography and the glossary.
  - Rebuild the glossary: edit `glossary-tools/rows.py` (definitions, Larkfield names) or `crosswalk.py` (Stripe–Adyen vocabulary), run `python3 _journals/payments-platform-architecture/_research/glossary-tools/assemble.py`, then `python3 _wiring/build.py` (`harvest.py` lists candidate terms, `kw.py` shows where the chapters use one).
- `_input/` — private inputs (empty at creation).

**Rebuilding the bibliography.** `posts/bibliography/index.md` is generated and is never edited by hand. After any page's "Sources and Evidence" section changes, run `sh _journals/payments-platform-architecture/_research/bib-tools/run.sh` from the repository root (standard library only; it runs `gen.py` → `classify.py` → `fix.py` → `render.py`), then `python3 _wiring/build.py`. R-numbers are stable through `bib-tools/ids.json`: existing sources keep their number, new ones take the next free number and a removed source retires its number, so never delete that file. Read the audit lines the run prints (`UNPARSED`, `no date`, `DATE CONFLICT`, `TITLE VARIANTS`, `SAME TITLE`, `AGE`) and fix what they name in the chapter's own Sources entry, or in `gen.py` (`SKIP`, `EQUIV`) and `fix.py` (`FIX`, `TITLE`, `META_URL`) when the chapter is right. `python3 _journals/payments-platform-architecture/_research/bib-tools/linkcheck.py` requests every cited URL once and writes `bib-tools/link-check.md` (use `--failed` to retry only failures, `--all` to recheck everything; decisions on failures are kept in `link-check-notes.json`).

## Provenance and neutrality

The book started from a Productscape domain model of payments and revenue infrastructure, used as a research map only and never cited as a source. Statements about Stripe, Adyen and other companies are documented facts with a source and a publication date; everything else is labeled as industry practice, inference, recommendation, illustration or assumption. Evidence older than about three years is flagged. Larkfield is fictional and is not a disguised version of any real company.

## Conventions

Same format as ORDERED (`_journals/commerce-platform-architecture`): opening callouts (IN THIS CHAPTER, YOU WILL / KEY POINTS / FAILURE PATTERNS), a fictional running example, tables of contrasts, generated figures, `[[permalink]]` cross-links, "What to Take Away" in three tiers, and a Sources and Evidence section per chapter. One deliberate difference, agreed with the author on 17 November 2026: ORDERED's "Across Scale Stages" section is replaced by a required **"Stripe and Adyen: Where They Differ"** section.
