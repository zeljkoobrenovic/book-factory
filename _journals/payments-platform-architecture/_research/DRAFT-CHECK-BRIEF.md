# Draft-Check Brief — final check of each page against its spec

You coordinate the draft check of a few pages of **SETTLED: Architecting Payments and Revenue Infrastructure**. Repository: `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (run scripts from there). ROOT = `_journals/payments-platform-architecture/`. The pages are written, verified against their sources, illustrated and final in content. This is the last step of the outcome pipeline: readers who did not write a page judge whether it does what its `spec.json` says, and the result is written to `posts/<folder>/check-report.json`.

## Read first

1. `.claude/skills/draft-check/SKILL.md` — follow it exactly. It defines the readers, what each may see, the judge, `check_draft.py` (`structure`, `units`, `finalize`, `status`) and what PASS, REVISE and ESCALATE mean.
2. `_wiring/outcome-specs/RULES.md` ("Check catalogue") and `_wiring/outcome-specs/PIPELINE.md` (step 5).

## Rules for this run

- **Pages one at a time**, in the order given. Finish a page (PASS, or ESCALATE reported) before starting the next.
- **Concurrency:** many coordinators run at once and the session limit is tight. Start **at most three reader agents at a time** for your page; wait for them before starting more. If an agent cannot be started because of a concurrency limit, wait a minute and retry; never skip a reader, and never play a reader yourself. A check that could not be run is recorded as not run.
- **Readers are fresh agents** (not forks) and see only what the skill says. Do not tell a reader what you expect. Give each its input as file paths in your scratch directory `<system temp scratch>/draft-check/<folder>/`.
- **Revisions (REVISE):** rewrite only the units named in failed results, each from its own spec entry. In addition, for this book: a revision must not change any fact, number, date, quotation, attribution, hedge, "Not public" statement, source entry, figure, caption or `[[link]]`. These were verified against sources; a draft-check revision changes how something is said or where a transition sits, never what is claimed. Keep within the spec's `max_words`. If a failure can only be fixed by changing a claim or the unit structure, treat it as a fault of the spec and escalate it. At most two revision rounds, with fresh readers each round, as the skill says.
- **Never edit `spec.json`**, the journal spec, the ledger or other pages.
- **Minor findings** (uncorroborated open-ended ones): fix only those that are cheap and plainly right, under the same no-fact-change rule; then the report must be finalized after the last edit, because any edit makes a report stale. End every page with `python3 _wiring/check_draft.py status <post-dir>` showing a current report.
- After the last page: `python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient error from a parallel build can be ignored if a rerun passes).

## Report back

Under 250 words. Per page: final verdict (PASS / ESCALATE), rounds used, units revised (count and what kind of failure), and for an ESCALATE each remaining failure with its quote, whether the draft or the spec looks at fault and why, and the three options for the author (revise by hand, change the spec, waive). Then: minor findings left unfixed that the author may care about (one line each), and any reader that could not be run.
