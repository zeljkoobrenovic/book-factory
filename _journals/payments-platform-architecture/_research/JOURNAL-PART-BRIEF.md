# Journal-Part Brief — one part of `journal-spec.json`

You are writing **one part** of the journal outcome spec for **SETTLED: Architecting Payments and Revenue Infrastructure**, before any prose exists. Several agents write different parts in parallel, each to its own fragment file; an assembly script joins them into `journal-spec.json`.

REPO = `/Users/zeljkoobrenovic/PycharmProjects/book-factory`
ROOT = `REPO/_journals/payments-platform-architecture/`

## Read first (in this order)

1. `REPO/.claude/skills/journal-spec/SKILL.md` — the contract rules for a journal spec (outcome not coverage; a thesis is a disputable answer to a stated question; children add up to the parent; transitions choose the relationship first).
2. `REPO/_wiring/outcome-specs/journal-spec.schema.json`, `common.schema.json` and `RULES.md` — the fields, enums and the rule behind each.
3. In `REPO/_wiring/outcome-specs/examples/commerce-platform-architecture.journal-spec.json`: the `preface`, `part-1`, `part-9` (journeys), `part-11` (cases) and `reference` parts as worked examples of a part at `detail: "full"` with its posts at `full`. Use `python3 -c` with `json` to print just those parts; the file is large.
4. `ROOT/_research/journal-spec-parts/top.json` — the journal level: the confirmed thesis, its supporting claims **J1–J10**, the flow and the non-goals.
5. `ROOT/PLAN.md` — your part's chapter contracts (folder, permalink, title, question, coverage, Larkfield thread, terms owned) and the contracts of the parts before and after yours.
6. `ROOT/_research/style-guide.md` (audience, evidence discipline, failure-pattern names, page format) and `ROOT/_research/scenario-ledger.md` (Larkfield: cast, figures, incidents, Keel decisions, the recurring payment).
7. The research briefs your chapters name in PLAN.md (`ROOT/_research/brief-*.md`). **Read them before writing any thesis about Stripe or Adyen.** A thesis, `how_why` or acceptance criterion may state as fact only what a brief tags VERIFIED or WIDELY REPORTED; where the briefs say the public record is silent, the thesis must not depend on the missing fact.

## What to write

One JSON object: your part, conforming to the schema's `part` definition at `detail: "full"`, with **every post of the part at `detail: "full"`**, saved as `ROOT/_research/journal-spec-parts/<part-id>.json` (`preface.json`, `part-1.json` … `part-10.json`, `reference.json`).

- `id` and `title`: exactly as given in your task (the title equals the section title in `ROOT/config.yaml`).
- `intent` (outcome: know / believe / can_do; acceptance criteria: the two standard ones — children cover the part thesis, hand-offs express declared relationships — plus one or two cold-reader criteria with `probe` and `expected` that test a reader outcome on a case the part does not contain).
- `thesis`: `question`, `claim`, `disputed_by`, `so_what`, `how_why`, and `supporting_claims` with ids `P<n>-1`, `P<n>-2`, … (`PF-1`… for the preface, `PR-1`… for reference). Three to six claims; together they must establish the part's claim.
- `role`: `contribution` and `supports` — the journal claims (J1–J10) this part argues for. Your task names the primary one. The preface and reference may support none or a few; say what they contribute.
- `flow`: the pattern that orders the chapters and, in `rationale`, what would break for the reader if they were reordered.
- `opening` (carried by the part intro page; a `hook` that is an actual scenario from the Larkfield ledger or a dated public fact, never a description of one; `bridge`; `roadmap`) and `closing` (carried by the part's last argued chapter: `synthesis` that says something no single chapter says, `so_what`, `callback` to the opening hook, `takeaway`).
- `transition_in` (all parts except the preface): the relationship to the previous part, what it carries over, what it introduces. Your task gives the neighbouring parts' claims.
- `posts`: in `config.yaml` order. For each: `id` (the permalink from PLAN.md; the part intro's id is `part-<n>`), `folder`, `title` (exactly as PLAN.md; a part intro's title equals the part title), `kind` (`part_intro`, `chapter`, `walkthrough` for Part IX journeys, `case` for chapters 46, 47 and 49, `front_matter` for the three preface pages, `reference` for the four reference pages), `detail: "full"`, `question`, `intent` (outcome and 2–4 acceptance criteria, at least one `cold_reader` criterion with `probe` and `expected` for every chapter), `thesis` (all five fields; no `supporting_claims` at post level — those belong to the post spec), `role` (`contribution`; `supports` naming your part's claim ids; part intros and reference pages may have an empty list), `transition_in` (every post after the first in the part), and `post_spec`: `"posts/<folder>/spec.json"`.

## Rules that matter most here

- **Outcome, not coverage.** `can_do` and acceptance criteria state what a reader can do afterwards, on a case the chapter does not contain. "The chapter covers idempotency keys" is not a criterion; "given a retry scenario, the reader says what key to send and what the provider does on the second request" is.
- **A thesis is a specific, disputable answer.** The `claim` answers the `question`; `disputed_by` names a view a reasonable engineer actually holds; no vague evaluative words ("important", "robust", "complex", "key"); `so_what` and `how_why` add something the claim does not say. A chapter's question is the "Q:" in its PLAN contract; you may sharpen its wording, not change its subject.
- **Evidence-bound theses.** This book's worst possible defect is an unsourced or invented claim about how Stripe or Adyen works. Where a chapter's subject is thinly documented (PLAN marks several as "expected to be short"; the briefs' "Open questions / not verifiable" sections tell you which), write the thesis about what *can* be established, and say in `how_why` that the public record stops there. Never write a thesis that needs undocumented internals to be true.
- **Every chapter's thesis must leave room for the required "Stripe and Adyen: Where They Differ" section** (Parts I–VIII): where the briefs show a documented difference, the thesis or `how_why` should name it with its year; where they show none, do not manufacture one.
- **Children add up.** Every `P<n>-k` claim is supported by at least one chapter; every chapter (`chapter`, `walkthrough`, `case`) supports at least one claim.
- **Transitions.** Choose the relationship from the enum first, then write `carries_over` and `introduces`. Read your part's transitions side by side: if most are `sequence` or `additional_support`, the order is a list and you should rethink it or say why in `flow.rationale`. You may propose a different chapter order inside your part if the argument needs it; if you do, keep the folder numbers, say so in your report, and note that `config.yaml` must follow.
- **Larkfield.** Hooks, callbacks and probes may use ledger facts (names, amounts, dates, incidents, K1–K8) exactly as written. Do not invent new canonical facts here.
- **Plain language.** American spelling; no marketing words; define nothing in the spec that the chapter will define, but do not use an undefined payments term in a `probe` without a clause explaining it.
- Leave everything `draft`-neutral: the part object has no `status` field; do not edit `top.json`, `config.yaml`, `PLAN.md` or any other file.

## Check before you finish

1. Your file parses: `python3 -c "import json;json.load(open('<your file>'))"`.
2. Validate it inside a temporary assembled spec: run `python3 ROOT/_research/tools/assemble_journal_spec.py --only <part-id> --check`. It builds a scratch journal spec from `top.json` plus your part and prints the schema errors that concern your part (errors about other parts being absent are expected and filtered). Fix every error it prints.
3. **Thesis rubric.** For your part thesis and each chapter thesis, start a fresh agent (Agent tool, not a fork) that is given **only that thesis object** and answers four questions with a reason each: does the claim answer the question; could a reasonable reader hold `disputed_by` instead; is the claim free of vague evaluative words; are `so_what` and `how_why` more than restatements of the claim. You may batch several thesis objects into one agent call (up to six per call) as long as the agent sees nothing else. Revise any thesis that fails and note which.
4. Re-read your part's theses against the briefs once more: every factual statement about a real company or regulation traceable to a tagged brief claim.

## Report back

Under 250 words: file written; the part thesis in one sentence; the chapter theses that failed the rubric and how they changed; any chapter whose thesis you had to narrow because the evidence is thin; any proposed reordering; anything in PLAN.md you found contradicted by the briefs.
