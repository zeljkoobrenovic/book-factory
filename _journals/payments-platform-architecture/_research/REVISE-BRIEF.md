# Revise Brief — acting on a draft-check report

A draft check of a page of **SETTLED** ended in ESCALATE in round 1: independent readers and a judge found failures, some at fault in the draft and some in the spec. The check stopped there, as its rules require. You are the reviser for that page. The author has delegated the acceptance of page specs to the coordinating editor, who authorizes the spec repairs described below; anything beyond them goes back to the editor.

Repository: `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (run scripts from there). ROOT = `_journals/payments-platform-architecture/`.

## Read first

1. `ROOT/posts/<folder>/check-report.json` in full: every failed result with its check, loci, quote, finding, fault and severity; also the minor findings.
2. The page's `index.md` and `spec.json` in full; `ROOT/_research/style-guide.md`; `_wiring/outcome-specs/RULES.md` (what each check means).

## The rule that outranks everything

The page's content was verified against its sources. **Do not change any fact, number, date, quotation, attribution, hedge, "Not public" statement, source entry, figure, caption or `[[link]]`, and do not weaken or strengthen any claim about a company.** You change how something is said, where a sentence sits inside its unit, how a unit opens, and how units are divided. If a failure can only be fixed by changing what is claimed, do not fix it: list it for the editor.

## What to do with each failed result

Decide first whether you agree. A judge can be wrong; if a failure misreads the page or the spec, do nothing and say why in your report (one line). Otherwise:

**Draft faults** (fix in `index.md` only):
- *Unglossed term* (`known_before_new`): add a gloss of one clause at first use, taken from the chapter that owns the term or the glossary (`ROOT/posts/glossary/index.md`); or move the existing gloss up to first use.
- *Evidence not explained* (`evidence_is_explained`): add the sentence that says what the table, figure, quotation or number shows, in the page's own terms.
- *Transition does not express the declared relationship*: rewrite the opening sentence of the unit so it carries over what the spec's `transition_in` names and expresses that relationship.
- *Unit does not state its controlling idea / summary mismatch*: rewrite the unit's first sentence so the unit says what the spec says it is about.
- *Weak introduction or conclusion pattern, callback, synthesis*: rewrite the named sentences.

**Spec faults you may repair** (edit `spec.json` AND `index.md` together, keeping them aligned):
- *A paragraph holds two controlling ideas*: split it into two units in the spec (give the new unit an id not yet used, a controlling idea, a function, the evidence that belongs to it and a `transition_in`), and split the prose paragraph at the same point. No sentence is lost or added beyond a connecting clause.
- *A controlling idea, count or wording in the spec disagrees with the verified page* (for example "six examples" where the page correctly lists seven; "the last two" where there are three): correct the spec's wording to match the page. The page's facts win.
- *A term is used before its gloss because the spec's unit order puts a table first*: add the gloss to the earlier unit in both spec and prose.
- *A local order problem inside one section* (a paragraph that plainly belongs one or two places earlier or later in the same section, by both flow readers or by the judge with a clear reason): move the unit in the spec and the paragraph in the prose, and fix the transitions on both sides.

**Spec faults you may NOT repair** (list them for the editor, with the quote and your recommendation):
- Moving, merging or removing a whole section; changing the order of sections.
- Anything touching `intent`, acceptance criteria, `thesis` or `role` (they are copied from the journal spec and locked).
- A failed acceptance criterion whose fix would change a claim.

## Limits and finish

- Stay within the spec's `max_words`; if repairs add words, trim connective sentences elsewhere (never evidence). If that is impossible, raise `max_words` by at most 5% and say so.
- Keep callouts, front matter (including `icon:` and `logo:` lines), figure lines, captions and Sources untouched.
- One front-matter line you DO update: `timetoread: N min read`, where N is the `check_draft.py structure` word count divided by 230, rounded to the nearest whole number. Do this last, after all other edits, because the check that follows is tied to the exact file.
- Add one changelog entry to `spec.json` dated 2026-11-24 summarizing the repairs.
- `python3 _wiring/validate_spec.py payments-platform-architecture <folder>` passes; `python3 _wiring/check_draft.py structure ROOT/posts/<folder>` passes.
- Do not run readers and do not write `check-report.json`: a separate session checks your revision with fresh readers.
- Write `ROOT/_research/revisions/<folder>.md`: one line per failed result (id or check, what you did, or why not).

## Report back

Under 200 words: failures fixed in the draft (count by kind); spec repairs made (each in one line); failures you judged wrong (count, with the two most significant); failures left for the editor (each with quote and recommendation); word count; checks run.

## Changes decided by the author on 24 November 2026 (these override the text above where they differ)

1. **This is the only revision the page gets.** No second check follows, so be thorough and careful: fix every failure you agree with, including the minor ones that are cheap and plainly right.
2. **Waiver, book-wide.** The position of the required house-format sections ("Stripe and Adyen: Where They Differ", "In Practice at Larkfield", "When It Goes Wrong", "What to Take Away", "Questions to Ask", "Sources and Evidence", the setting-the-scene section) is fixed. Never move one. Where a failure is about such a position, make the paragraph before the section and its opening sentence say why it comes there, and log it as "house format; transition strengthened".
3. **Callouts may now be touched for one purpose:** a term in the opening callouts (IN THIS CHAPTER, KEY POINTS, FAILURE PATTERNS) that a reader flagged as unexplained gets a gloss of a few words taken from the body. Keep exactly three KEY POINTS and the exact labels.
4. **Content inconsistencies found by the check** (a table cell that contradicts the prose, a count that does not match its list, a figure without source or date, a Larkfield sentence that contradicts the ledger, a date in a table that differs from the same source's date in the prose): correct them, each against the page's own Sources section, its verification file (`_research/verification/<folder>.md`), the rulings in `_research/consistency-issues.md` and the ledger (`[editor]` lines win; where the ledger is silent, state the condition and do not invent a fact). Documentation pages are cited "n.d., accessed November 2026" (ruling 30), not with a year taken from page metadata. Fetch a source only to confirm wording you must quote; never put the user's name, email or any personal identifier in a request. List every such correction in your report. If a claim cannot be supported, remove it and say so.
5. **Length:** stay within `max_words`; you may raise it by at most 5% but never above 6,900 for a chapter. Prefer trimming restatement.
6. **Do not run the build** (`_wiring/build.py`): parallel builds collide. Validate and run the structure check only.
7. **Spec faults about a paragraph that belongs in another section:** you may move a single paragraph unit to the section where both readers or the judge say it belongs, in spec and prose together, fixing the transitions on both sides, when the move loses nothing and the paragraph's content does not change. Whole sections still never move.
