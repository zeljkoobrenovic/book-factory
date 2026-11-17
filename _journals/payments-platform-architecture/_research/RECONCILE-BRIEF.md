# Reconcile Brief — bring the specs and pages into line after verification

Every chapter of **SETTLED** has been verified against its sources. Verifiers corrected the prose but were not allowed to edit the journal spec, so some journal-spec entries (and the copies of them in page specs) still state things the verification disproved; and some corrections made on one page have not yet reached other pages that repeat the same statement. Your job is to close those gaps for the parts assigned to you. You change wording to make it true; you do not change arguments.

REPO = `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (run scripts from there). ROOT = `REPO/_journals/payments-platform-architecture/`.

## Read first

1. `ROOT/_research/consistency-issues.md` — every ruling (1–45 and any later ones). These are the settled corrections.
2. `ROOT/_research/reconcile-notes.md` — the coordinator's running list of known pending items (some already done; check before changing).
3. For each page in your scope: its verification file `ROOT/_research/verification/<folder>.md`, especially the sections "For the author", "Journal-spec …", "For other pages" and "Ledger conflicts". Then the page's current `index.md` and `spec.json`, and its entry in the journal spec.
4. `ROOT/_research/scenario-ledger.md` (the `[editor]` line at the end wins over chapter lines).

## How the journal spec is edited

`ROOT/journal-spec.json` is GENERATED. Edit only the fragment for your part in `ROOT/_research/journal-spec-parts/<part-id>.json`, then run `python3 _journals/payments-platform-architecture/_research/tools/assemble_journal_spec.py`. A page spec's `intent.outcome`, acceptance criteria, `thesis` (question, claim, disputed_by, so_what, how_why) and `role` must equal its journal entry word for word, so after changing an entry apply the same change to `ROOT/posts/<folder>/spec.json`. For a single text replacement in one post's entry and its page spec together you can use `python3 _journals/payments-platform-architecture/_research/tools/fix_entry.py <post-id> "<old>" "<new>"` (it reassembles and validates). Part-intro specs copy the part's thesis and supporting claims: keep them equal too.

## What to do, per page in your scope

A. **Journal entry versus verified page.** Find every sentence in the entry (question, know/believe/can_do, acceptance criteria incl. probes and expected answers, thesis fields, role, transition_in) that the verification file or a ruling shows to be false or overstated, and correct it with the smallest change that makes it true. Typical cases: a "not public"/"nothing published" that turned out to be published; a date, name or number corrected by a verifier; an unscoped claim that a ruling scopes (for example ruling 29); a status that changed. Re-sync the page spec.
B. **Part-level fields.** Do the same for your parts' own fields (intent, thesis `how_why`/`so_what`, supporting claims, opening, closing, transition_in). **Do not change a part thesis `claim`**: the author approved those ten sentences. If a part claim contains a clause that verification made false or too strong, do not edit it; report the clause, the evidence and your suggested rewording.
C. **Chapter-level thesis claims** may be corrected when a clause is false (chapters 39 and 32 were such cases). Keep the claim a specific, disputable answer to its question, say what is established and where the public record stops, and after rewriting give ONLY the new thesis object to a fresh agent with the four rubric questions (does the claim answer the question; could a reasonable reader hold `disputed_by`; free of vague evaluative words; are `so_what` and `how_why` more than restatements). Report old and new claims.
D. **Page spec body.** Where a verifier changed prose inside a unit, make sure that unit's `controlling_idea` and `evidence` in `spec.json` still describe it truthfully. Do not add, drop, merge or reorder sections or paragraphs. Add one changelog entry dated 2026-11-17 to each spec you change.
E. **Cross-page sweep within your scope.** Using the rulings and the "For other pages" notes, grep your pages' `index.md` for statements that a ruling corrects but that this page still carries in its old form (the verification of that page may have predated the ruling), and fix them. Recurring ones: Adyen "publishes nothing" on acquiring countries (27), report timing (32), load testing / peak freeze / headroom (42), failover and regions (45), negative-balance period and loss-bearing pilot (41), tax (38), merchant of record (chapter 32), a recovery figure (37), terminal rollout (chapter 11); Stripe "has no" Click to Pay page (35), scheduler description (34), conversion figure (40), periodic re-verification (36), second root-cause analysis (43), first-attempt least-cost routing in Australia (31); "no endpoint returns a payment" unscoped (29); merchant of record "takes the liability" (chapter 32); "partner banks" for Stripe's named acquirers (27); Visa rule citations (44); Georgia bank and Bridge status (33); the Silent Webhook weekday (20); "eight incidents in 2026" (24); "nightly" for the Keel reconciliation job (28); documentation pages dated from "last modified" metadata (30); publication dates that differ from the displayed date (25).
F. **Format leftovers.** Hand-offs and part references use `[[part-N]]`/`[[permalink]]`; no external URLs in running text (ruling 22); `timetoread` equals the `check_draft.py structure` word count ÷ 230; the page stays within the `max_words` of its spec (trim connective sentences if a correction adds words; never cut evidence).
G. **Illustration placeholders.** Where a correction makes a placeholder's caption, alt text or prompt false (for example a figure that draws "place unknown" pins for data that is now known, or one that shows liability moving to a merchant of record), correct the placeholder's JSON so the figure will be true when generated. Keep the JSON valid.

## Limits

- Edit only: the fragment files of your parts, and `index.md` / `spec.json` of the pages in your scope. Do not edit the ledger, the style guide, the rulings or other parts' files; put anything outside your scope under "For other scopes" in your report.
- Do not re-verify claims against the web unless a correction needs it; the verification files are the evidence. If you find a NEW doubt, fetch the source and note it.
- Never put the user's name, email or any personal identifier in a request.

## Finish

- `python3 _wiring/validate_spec.py payments-platform-architecture` prints `ok` for the journal spec and every page spec.
- For each page you edited: `python3 _wiring/check_draft.py structure <post-dir>` passes; `python3 .claude/skills/article-illustrator/scripts/extract_illustration_placeholders.py <index.md>` parses.
- Build: `python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient parallel-build error can be ignored if a rerun passes).
- Write your log to `ROOT/_research/reconcile-<scope>.md`: per page, each journal-entry field changed (old → new, one line), each cross-page fix, each placeholder fix; then the part-claim clauses you could not change, with evidence and suggested wording.

## Report back

Under 300 words: pages touched; chapter thesis claims rewritten (old → new, one line each); part-claim clauses the author must decide (clause, evidence, suggested wording); validation result; anything for other scopes.
