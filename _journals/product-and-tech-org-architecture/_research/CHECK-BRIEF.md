# Check Brief — finishing the draft check of one page

You run the remaining check rounds on **one existing draft** and revise it. You did not write it. Repository root: `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (REPO). Journal root: `REPO/_journals/product-and-tech-org-architecture` (ROOT). Your task names the post folder and which rounds are owed.

## Read first

- `ROOT/_research/WRITER-BRIEF.md`: the sections "How the draft checker counts units", "Lessons from chapters 1 and 2", "Scope", and the house-format note.
- `REPO/.claude/skills/draft-check/SKILL.md`.
- The page's `spec.json` and `index.md`, and its `check-report.json` if one exists (it shows what an earlier round found).

## Each round

1. From REPO: `python3 _wiring/validate_spec.py product-and-tech-org-architecture <folder>` and `python3 _wiring/check_draft.py structure <post dir>`. Fix any structural mismatch in the draft first.
2. Put the inputs in a scratch directory of your own: `python3 _wiring/check_draft.py structure <post dir> > structure.json`, `… units <post dir> > units.json`, a copy of `index.md`, and the introduction alone (everything before the first `## `).
3. Start fresh readers as separate agents, each given only what the draft-check skill allows:
   - a reverse outliner (units only);
   - a cold introduction reader (introduction only);
   - one cold reader per `cold_reader` acceptance criterion (whole draft and the probe, nothing else);
   - two flow readers (whole draft). Ask each to rate every point (a) left unsure, had to supply an assumption, or went back to another section, or (b) resolved by re-reading the same sentence or paragraph.
4. Then one judge (spec, structure, outline, the readers' answers, the draft for tables and figures). Tell it that only points both flow readers rate (a) are flow failures, that a failure both readers trace to the order of sections is a spec fault, and give it the house-format note. It writes `results.json` in the `--results` format.
5. `python3 _wiring/check_draft.py finalize <post dir> --results <results.json> --round <n>`.

Start readers a few at a time. If an agent launch is refused because of a concurrency limit, wait and try that reader again later in your run; do not judge the draft yourself and do not skip a reader.

## After a round that is not a pass

Revise only the units named in failing results, with the smallest change that answers each finding. Prefer cutting a confusing sentence to explaining it. Do not add claims the spec does not ask for. Do not add, drop, merge or reorder units. If a finding's fault is the spec and the fix is local and obvious, fix the spec, and log it in the spec's decision log and changelog; otherwise leave the spec alone and report it. Re-run the structure check.

## When to stop

- The author's rule is **at most two rounds per page**. If round 1 already exists, run round 2 only. If no round exists, run round 1 and, if it is not a pass, revise and run round 2 with fresh readers.
- After the last round, if it is not a pass, revise the named units once and stop. **Do not record waivers**; the lead session does that under the author's rule.
- Build: `python3 _wiring/build.py 2>&1 | grep -E "product-and-tech|Traceback"`.

## Report (under 200 words)

The verdict and counts of each round you ran; each failing finding of the last round in one line, with whether both readers reported it and what you changed; any spec change; the final word count; anything the author must decide.
