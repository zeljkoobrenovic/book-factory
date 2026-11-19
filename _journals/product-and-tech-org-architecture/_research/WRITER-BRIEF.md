# Writer Brief — one page of *Architecting Product & Tech Organizations*, end to end

You take **one page** of the book from its entry in the journal spec to a checked, built draft. The author has put the book in **auto mode**: you do not stop for approval. You decide, record what you decided, and report.

Repository root: `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (REPO). Journal root: `REPO/_journals/product-and-tech-org-architecture` (ROOT). Your page folder: `ROOT/posts/<folder>` (given in your task).

## Read first, in this order

1. `ROOT/_research/style-guide.md` — voice, evidence rules, AI labels, page format. Follow it exactly.
2. `ROOT/journal-spec.json` — your page's entry (intent, acceptance criteria, thesis, role, transition_in), its part, and the entries of the page before and after yours.
3. `ROOT/_research/scenario-ledger.md` — Corvane's facts, including every line of the append log. Your examples must agree with it.
4. `ROOT/PLAN.md` — the entry for your chapter: anchor, sources, gaps.
5. The two finished chapters, as models of density, voice and format: `ROOT/posts/01-the-organization-as-a-system/index.md` and `spec.json`; `ROOT/posts/02-the-organization-as-a-product/index.md`.
6. The skills, which define the pipeline: `REPO/.claude/skills/spec-creator/SKILL.md`, `detailed-article/SKILL.md`, `draft-check/SKILL.md`; and `REPO/_wiring/outcome-specs/post-spec.schema.json`.

## Sources (do not invent evidence)

- The author's Kindle notes: `ROOT/_input/bookshelf/docs/notes/*.pdf`. Extract with `pdftotext -layout <pdf> <your scratch dir>/<name>.txt` and read the parts you need. Quote at most one sentence at a time, verbatim from the notes; otherwise paraphrase and name the book and the concept.
- The author's own summaries of these sources, which you may use and should cross-link: `REPO/_journals/grounded-engineering-executive`, `grounded-engineering-management`, `grounded-product-management`, `grounded-platforms`, `grounded-people-management-tools`, `org-design`, `tech-strategy`, `ai-dev-strategy` (each `posts/<slug>/index.md`). Link with `[[permalink]]` and check after the build that the link resolved to the journal you meant.
- The checklists: `ROOT/_input/checklists/data/data.json`.
- A source named in PLAN.md as a **gap** (not on the author's bookshelf) may be used only for what you can verify: fetch and read it, or cite only the widely known claim and say in the text that it supplements the author's sources. No invented statistics, quotations or company cases. Company-internal folders elsewhere on this machine are off limits.
- Applying a source to something it does not address is marked as the author's extension.

## Pipeline

1. **Spec.** Write `spec.json` following the spec-creator skill: copy intent, acceptance criteria, thesis and role from the journal spec unchanged; add your own supporting claims, sections, paragraphs, introduction, conclusion, record keeping. `conclusion.hand_off` must equal the next page's `transition_in` in the journal spec. Validate: `python3 _wiring/validate_spec.py product-and-tech-org-architecture <folder>` (run from REPO).
2. **Flow rubric**, once: print the order with `python3 _wiring/validate_spec.py --flow <spec file>`, give that output and nothing else to one fresh agent, apply its notes, re-validate. Do not run it a second time.
3. **Accept.** Set `status: "accepted"` and add a decision-log line: "Accepted in auto mode by the author's standing instruction of 2026-11-19; not individually reviewed." List in `open_questions` anything the author should look at.
4. **Draft** `index.md` unit by unit from the spec (detailed-article skill). Then `python3 _wiring/check_draft.py structure <post dir>` until sections, unit counts and forms match and the length is within the cap.
5. **Check**, following the draft-check skill, with **at most two rounds** (the author's rule). Round 1: reverse outliner, cold intro reader, one cold reader per cold_reader criterion, two flow readers, then a judge; `finalize --round 1`. Revise the named units. Round 2 with fresh readers; `finalize --round 2`. If round 2 is not a pass: revise the named units once more and stop. **Do not record waivers yourself.** A waiver is the author's to grant, in the author's own words; leave the round-2 report as it is (it will read REVISE and be stale against the revised draft) and list each remaining finding in your report so the author can waive it or ask for another round. (The author decided on 2026-11-19 to waive such findings by rule; the lead session records the waivers after reading your report. You still do not record them.) **Also:** a failure whose fault is the spec's argument or order (not a wording slip) is not waived silently: fix the spec if the fix is local and obvious, record it in the spec's decision log and changelog, and name it first in your report.
6. **Build**: `python3 _wiring/build.py 2>&1 | grep -E "product-and-tech|Traceback"`. "missing post" warnings for pages not yet written are expected. Confirm `docs/product-and-tech-org-architecture/<permalink>.html` exists.
7. **Ledger.** Append any new Corvane fact your page introduces as one line at the end of `scenario-ledger.md`, dated, with your chapter named. Append only; re-read the file's tail immediately before appending, because other writers work in parallel. Never contradict an existing line.

**Concurrency.** Other writers run at the same time and the session allows a limited number of agents at once. Start your readers two or three at a time, not all together. If a launch is refused because of a concurrency limit, that is not a reason to skip the reader or the round: do other work or wait a few minutes (for example re-read your draft against the lessons below), then start that reader again; keep trying at intervals until it runs. Never judge your own draft in its place.

Give each reader exactly what the draft-check skill says and no more. Tell flow readers to rate each point (a) left unsure or went back to another section, or (b) resolved by re-reading the same sentence or paragraph; tell the judge that only points both readers rate (a) are flow failures, and give it the house-format note below.

**House-format note for readers and judges:** the opening blockquote callouts are page format, not spec paragraphs; the Checklist heading, its list and the closing hand-off paragraph fall inside the conclusion by design; unresolved `[[links]]` to pages not yet written are expected; the book's introduction explains the evidence labels, the AI labels and Corvane.

## How the draft checker counts units (get this right the first time)

- The introduction's units are the prose paragraphs before the first `##`. The three callouts are **not** units; do not list them in `introduction.paragraphs`.
- One spec paragraph = one prose block with no blank line inside it. A table, a mermaid figure with its caption, or a blockquote attaches to the paragraph **before** it, so a `"form": "table"` or `"figure"` paragraph is a lead-in sentence followed by the table or figure.
- A list directly after a paragraph merges with it into one unit of form `list`. So a `prose` paragraph must not be followed directly by a list, and a `list` paragraph is a lead-in line plus its list.
- The conclusion starts at `## What to Take Away` and runs to `## Sources and Evidence`. It has five units: three lists (Established / Depends on context / The author's synthesis), the checklist (lead-in plus `- [ ]` items under `## Checklist`), and one closing prose paragraph that contains the `[[next-page-permalink]]` link.
- Section headings in the draft equal the spec's `heading` values exactly.

## Lessons from chapters 1 and 2 (each cost a check round)

- **Define before use**, including inside tables: if a table row uses a term defined later, say so in the lead-in.
- **One sense per term.** If a source uses a word differently from the book (Meadows's "boundary"), say so where the book's sense is defined.
- **Give every Corvane example its year and company size**, and introduce each person with their role the first time in the chapter. Do not tell the opening scene twice in the same words.
- **The lead's roadmap sentence must list the sections in their actual order.** Re-read it after any reordering.
- **Do not add a claim the spec does not ask for.** Extra interpretive sentences added during revision caused new failures twice.
- **Do not judge a worked example before showing it**; table first, then what it shows.
- **Name which thing a pronoun or "that" refers to** when two candidates are near.
- **Announce the AI label scheme** in the first sentence of "What AI Changes Here": "Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative."
- **A section that the chapter's argument does not use is in the wrong chapter.** If the flow rubric or both flow readers say a section stands between a question and its answer, cut it to a paragraph and say where the full treatment is.
- **Every pattern names its user and its outcome measure** (the book applies product thinking as well as system design).
- **Do not use `sed`-style global replacements on prose**; make each edit an exact, unique string replacement and check it applied once.
- Each chapter stands alone: say "Corvane, the fictional company this book follows" once, early.
- **One worked example, one lens.** Chapter 3 needed three rounds because it carried two senses of one term, two conditions, two anti-patterns, three trade-off choices and three Corvane cases, and then tried to classify the cases by the trade-off choices. Check each case against the chapter's one main idea and nothing else. When a chapter is within 300 words of its cap, cut a secondary thread instead of compressing sentences.
- Aim for the target, not the cap: the first chapters all landed within 250 words of 5,000.

## Part introductions (kind `part_intro`)

A part introduction is short and has its own shape. Model: `REPO/_journals/commerce-platform-architecture/posts/part-1-intro/index.md` and its `spec.json`.

- It performs the part's `opening` from the journal spec (hook, bridge, roadmap) and states the part's thesis; use the part's thesis and supporting claims as the post spec's thesis, and say in the spec that they are the part's.
- Page format: KEY POINTS callout only (three bullets), no IN THIS CHAPTER and no FAILURE PATTERNS callout; lead paragraphs; two to four short sections; no "What AI Changes Here", no "What to Take Away" tiers, no Checklist; it ends with `## Chapters in this part`, a list with one line per chapter as `[[permalink]]` plus the question it answers; no Sources section unless a source is cited.
- Its `conclusion.hand_off` points to the first chapter of the part with that chapter's `transition_in` from the journal spec. Decide what the conclusion's units are, write the spec to match exactly, and set the conclusion heading to the heading you actually use (for example `Chapters in this part`).
- 800–1,200 words; set the spec's length cap to 1,400. One check round is usually enough for a page this short; the two-round limit still applies.

## Scope

Write only in your own page folder, plus one append to the ledger. Do not edit `journal-spec.json`, `config.yaml`, `PLAN.md`, the style guide, this brief or other pages. If your page cannot be written without a change to the journal spec, make the best local choice, and put the needed change first in your report.

## Report back (under 250 words)

Files written; word count; verdict and round of the final check report with counts of pass, fail and waived; the waived findings in one line each; any spec-level problem and what you did; facts appended to the ledger; cross-links that did not resolve as intended; anything the author must decide.

## Privacy

Never put the author's name, email or project names into web requests.
