# Writer Brief — one page: outcome spec, then article

You are writing one page of **SETTLED: Architecting Payments and Revenue Infrastructure**, a technically accurate architecture book for **engineers and architects who are new to payments**, anchored on Stripe and Adyen. The author's instruction: **quality over speed; every factual claim about a company's architecture needs a source; documented facts are kept apart from labeled inferences; evidence older than about three years is flagged; no padding — where little is public, write a short page that says so.**

REPO = `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (run every script from there)
ROOT = `REPO/_journals/payments-platform-architecture/`

You do two things in order: write the page's outcome spec (`spec.json`), then write the article (`index.md`) from it.

## Read first (in this order)

1. `ROOT/_research/style-guide.md` — audience and voice, evidence discipline, the required "Stripe and Adyen: Where They Differ" section, the three take-away tiers, page format, figure placeholders, failure-pattern names, valid permalinks. Follow it exactly.
2. `ROOT/PLAN.md` — your chapter contract; skim the neighbours' contracts so you do not re-teach what they own.
3. `ROOT/journal-spec.json` — your page's entry (intent, thesis, role, transition_in) and the entries of the previous and next pages in reading order, plus your part's thesis. Print them with a few lines of Python; do not read the whole file.
4. `ROOT/_research/scenario-ledger.md` — the canonical Larkfield facts, including every line under "Additions by chapter".
5. `ROOT/_research/consistency-issues.md` — numbered cross-chapter rulings (which chapter owns an idea two chapters touch, corrections to PLAN.md and the ledger found during research). Apply every ruling that names your page; a ruling wins over your PLAN contract.
5a. The research briefs named in your contract (`ROOT/_research/brief-*.md`). Read the relevant parts in full, including their "Open questions / not verifiable" and "Research limitation" sections.
6. Model chapter for format and density: `REPO/_journals/commerce-platform-architecture/posts/12-payments/index.md` (first 150 lines and the Sources section). Its reader is a newcomer to software; yours is an engineer, so go deeper technically.
7. If pages already exist in `ROOT/posts/`, skim the ones your contract links to, so terminology and examples stay consistent.

## Step 1 — the outcome spec (`ROOT/posts/<folder>/spec.json`)

Follow `REPO/.claude/skills/spec-creator/SKILL.md` (read it, with `REPO/_wiring/outcome-specs/post-spec.schema.json`, `RULES.md` and the example it names). Specifics for this book:

- **Source material** is your PLAN contract plus the research briefs. That is the "INPUT" the skill asks for.
- Copy `intent.outcome`, the acceptance criteria, the thesis and `role` from your `journal-spec.json` entry unchanged.
- Sections follow the style guide's body order, **named by content**. The required section "Stripe and Adyen: Where They Differ" (Parts I–VIII), "What to Take Away" (the conclusion) and the style guide's other fixed elements must be in the spec so the article can contain them. The callouts, the "Where we are in the payment's journey" paragraph and the roadmap paragraph are part of the introduction. "Questions to Ask" is a list unit in the conclusion or a short final section, as the example spec does it; "Sources and Evidence" is apparatus and is not specified.
- **Evidence must exist.** Every `evidence` item names a specific tagged claim from a brief (give the URL and date in `what`) or a ledger fact. Do not plan a paragraph around evidence you do not have. If the briefs show the public record is thin for part of your contract, plan fewer paragraphs and add a paragraph whose controlling idea is where the evidence stops.
- **Size the spec to the evidence.** Typical chapter: 6–9 sections, 35–50 paragraphs. A chapter marked "expected to be short" in PLAN: 4–6 sections, 15–25 paragraphs.
- Validate: `python3 _wiring/validate_spec.py payments-platform-architecture <folder>`. Fix every error.
- Flow rubric: `python3 _wiring/validate_spec.py --flow _journals/payments-platform-architecture/posts/<folder>/spec.json`, give that output and nothing else to a fresh agent, and ask the four questions in the skill. On "unsound", fix the order and rerun.
- **Acceptance.** The author delegated acceptance on 17 November 2026: when the spec validates and the flow rubric returns "sound" or "sound with notes", set `"status": "accepted"` and add the changelog entry `{"date": "2026-11-17", "change": "Accepted under the author's delegation of 17 November 2026: validates and passed the flow rubric (<verdict>)."}`. If you could not get there, leave it `draft`, do **not** write the article, and report why.

## Step 2 — the article (`ROOT/posts/<folder>/index.md`)

Follow `REPO/.claude/skills/detailed-article/SKILL.md`, section "Writing from `spec.json`": write unit by unit in spec order; do not add, drop, merge or reorder units. If you find you must, stop, fix the spec first (re-validate), then continue. The style guide governs format: front matter, exact callout labels, the required sections, the Sources and Evidence format, illustration placeholders (3–4, staged only; do not run the image generator).

**Facts.** The briefs are your primary factual base.

- State as fact only what a brief tags VERIFIED or WIDELY REPORTED, or what you verify yourself by fetching the page in this session (WebFetch, or `curl -sL --max-time 40 -A "Mozilla/5.0 (research-bot)" <url>`; `docs.stripe.com` and `docs.adyen.com` pages usually have a `.md` variant). Cite with the publication date, or "n.d., accessed November 2026" for documentation.
- A brief's ASSUMPTION/JUDGEMENT becomes, in the article, either the author's labeled judgement or an `> **INFERENCE, NOT DOCUMENTED:**` block. Never promote it to fact.
- Quotes must be exact. Copy them from the brief only where the brief quotes; otherwise fetch the page.
- **Before you finish, re-fetch the 6–10 most load-bearing sources of your page** (the ones behind the "Where They Differ" table and the key points) and confirm each still says what you wrote. Fix or hedge anything that does not match. List in your report which URLs you re-fetched and any you could not reach.
- Never cite a research brief, a Productscape file or a sibling book's research brief. Sibling book chapters are cited with `[[permalink]]`.
- Never put the user's email address, name or any personal identifier in HTTP headers, User-Agent strings, query strings or request bodies.

**Length.** Use the word count that `python3 _wiring/check_draft.py structure <post-dir>` reports (prose and tables; it leaves out the illustration-placeholder JSON, which a plain `wc -w` would wrongly include). Aim 4,000–5,500; never over 6,500; short chapters 2,000–3,000. Set `timetoread` to that count ÷ 230.

**If the Agent tool refuses with a concurrent-subagent limit** when you start the flow-rubric reader: do not write the article. Finish and validate the spec, leave it `draft`, and report that the flow rubric is pending; the coordinator will run it and resume you.

## Larkfield

Use the ledger exactly. Append genuinely new canonical facts (ones another chapter might rely on) to "Additions by chapter" in `scenario-ledger.md`: one small append edit, prefixed with your folder name; re-read the file's tail immediately before you edit; never rewrite others' lines.

## Files you may write

`ROOT/posts/<folder>/spec.json`, `ROOT/posts/<folder>/index.md`, and the one append to the ledger. Nothing else: not `config.yaml`, `journal-spec.json`, other pages, or files outside ROOT. Private scratch goes in `/private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-book-factory/69f0aeef-1582-4169-8062-d2abd585a792/scratchpad/writer-<folder>/`.

If your journal-spec entry is wrong (the thesis cannot be supported by the evidence, the transition does not hold), do not edit it and do not write around it: stop and report what is wrong and what you would change.

## Verify before you finish

1. `python3 _wiring/validate_spec.py payments-platform-architecture <folder>` passes.
2. `python3 _wiring/check_draft.py structure _journals/payments-platform-architecture/posts/<folder>` — sections and unit counts must match the spec; fix the draft where they do not.
3. `python3 .claude/skills/article-illustrator/scripts/extract_illustration_placeholders.py _journals/payments-platform-architecture/posts/<folder>/index.md` parses every placeholder.
4. Build: `python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head`. "missing post" warnings for pages other writers have not finished are fine. A transient error from a parallel build can be ignored if a rerun passes.
5. Render check: `python3.11 _journals/payments-platform-architecture/_research/tools/render_check.py <permalink>` must print `OK`. `unresolved=[[x]]` is acceptable only if `x` is a valid permalink of this book whose page is not written yet. `XJ:` entries (links into another journal outside the allowed list) must be fixed. Exception: keep `[[introduction]]`, `[[toolkit]]`, `[[glossary]]`, `[[bibliography]]`, `[[domain-coverage]]` and `[[part-1]]` … `[[part-10]]` as `[[…]]` links even if they show as `XJ:` now; those permalinks also exist in other books and resolve in-journal once this book's page is written. Do not replace them with hard-coded `.html` links.
6. Re-read the article once as two reviewers: a payments engineer from Stripe or Adyen looking for anything wrong, unsourced or outdated about their company; and an engineer new to payments looking for an undefined term, a section that buries the problem, or a "Where They Differ" row that says nothing.

## Report back

Under 200 words: files written; spec status and flow verdict; word count; the three key points; the rows of the "Where They Differ" table in one line each; facts you added to the ledger; URLs re-fetched and any that failed; every claim you hedged or could not verify; anything a reviewer should check.
