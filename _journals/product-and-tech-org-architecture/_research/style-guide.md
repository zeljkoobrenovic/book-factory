# Style Guide — Architecting Product & Tech Organizations

Read this, `../PLAN.md`, `../journal-spec.json` (your page's entry and its neighbours'), `scenario-ledger.md` and the page's `spec.json` before writing. The spec is the contract: write its units in its order.

## Voice and audience

- Two readers at once. An **executive** (CTO, CPO, VP, Director) must be able to act on the page. An **individual contributor** must be able to follow the reasoning. Write the decision for the first and the explanation for the second.
- The reader knows how software teams work. The reader does **not** know organization-design vocabulary. Define each such term in one plain clause the first time it appears in a chapter, and link the chapter that owns it.
- Problem before model. Open with what goes wrong and what it costs, then the concept.
- Direct, concrete, plain. Short sentences. One idea per paragraph. A worked example beats an abstraction. Use "you" for the reader.
- First person ("I") is the author's judgement, used in trade-offs, take-aways and recommendations. Never claim specific real employers, real incidents or inside knowledge of a company.
- Opinionated, and honest about "it depends": say what it depends on.
- American spelling. No marketing language, no motivational writing, no management clichés ("empower", "unlock", "world-class", "move the needle", "north star" as decoration, "at the end of the day").

## Evidence discipline (non-negotiable)

Every statement is one of six kinds, and the wording makes the kind clear:

1. **Source** — a book or paper, named with its concept ("Larson's four team states, in *An Elegant Puzzle*"). Paraphrase; quote at most a sentence. Cite the edition year under Sources and Evidence.
2. **Research finding** — a study or survey, with year and what it measured. Fetch and read it before citing.
3. **Documented practice** — what a named company has published about itself, with the year. Never infer a real company's internals.
4. **Author's experience** — marked as such, without naming employers.
5. **Recommendation** — the author's view, with its reasoning and the conditions under which it does not hold.
6. **Illustration** — Corvane, or any invented number. Say "Corvane, the fictional company this book follows" the first time in each chapter. Ledger numbers are illustrations.

No invented statistics, quotations or case studies. Where the evidence runs out, say so. Rules of thumb from a source are presented as that author's rule of thumb, not as a law.

**AI claims carry one of three labels**, in bold at the start of the claim: **Proven** (measured and published; cite it), **Emerging** (practised by some organizations and reported; say by whom or mark as the author's observation), **Speculative** (reasoning about what may follow; say what would confirm it). Date anything that can change: "as of November 2026".

## Page format

Front matter:

```yaml
---
title: "<title from journal-spec.json>"
date: 2026-11-19
author: Željko Obrenović
excerpt: "<two sentences: the question and the answer in plain language>"
permalink: <id from journal-spec.json>
timetoread: <N> min read
---
```

Use typographic quotes inside front-matter values, never `\"`.

Then, in this order, with these exact labels:

```markdown
> **IN THIS CHAPTER, YOU WILL:** <one sentence, at most about 25 words>

> **KEY POINTS:**
>
> * **<Bold lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.

<br>
<Lead paragraphs.>
```

Exactly three KEY POINTS. Two or three failure patterns. Part intros open with KEY POINTS only and end with `## Chapters in this part`.

Body, named by content and in roughly this order (the spec fixes the actual sections):

1. **The problem**, shown at Corvane.
2. **Principles** — the model, with its terms defined.
3. **Patterns** — what to do. Each pattern names its **user** (who it is for) and its **outcome measure** (how you would know it worked), because the book applies product thinking to organization design as well as system design.
4. **Anti-patterns** — how it fails, using the failure-pattern names.
5. **Trade-offs** — a comparison table; when each choice is right.
6. **Where the Sources Disagree** — only when they do; state the tension and the book's resolution.
7. **What AI Changes Here** — exact heading, Parts I–X; labeled claims.
8. **A worked example** at Corvane, with ledger numbers.
9. **What to Take Away** — three tiers, exact labels: **Established.** / **Depends on context.** / **The author's synthesis.**
10. **Checklist** or decision framework — exact heading `## Checklist`, 6–10 items as `- [ ]` task-list lines the reader can run.
11. A closing paragraph that hands off to the next page with a `[[link]]`.
12. `## Sources and Evidence` — grouped *Books*, *Research and reports*, *Practitioner sources*; each entry: title, author, year, one clause on what it supports. End with: "Corvane is fictional; recommendations and labeled assumptions are the author's judgement."

Length: 3,500–5,000 words for chapters, measured from front matter to the start of Sources and Evidence; part intros up to about 1,200.

## Diagrams and tables

Mermaid for org structures, interaction modes and decision flows, fenced exactly as:

```
---begin mermaid---
flowchart LR
    A["Team A"] -->|"request"| B["Platform"]
---end mermaid---
```

Every node label in double quotes; edge labels quoted; under about 14 nodes; no `classDef`; no `end` as a node id. Follow each diagram with `**Figure N:** *<caption that states the point in one sentence>*`. One to three diagrams per chapter. Use tables for comparisons, trade-offs and "what it says / what it does not say".

## Cross-links

Link chapters with `[[permalink]]`, using only ids from `journal-spec.json`. Cross-link the author's related records where they give working detail the book does not repeat (for example `[[conways-law]]` and `[[organizational-design]]` in `grounded-engineering-executive`, the `org-design` records, `grounded-product-management`). Check each resolves in the build; never invent a permalink.

## Failure patterns (provisional names, fixed by the failure-patterns page)

| Family | Patterns |
| --- | --- |
| Boundaries | The Org Chart as Architecture · The Overloaded Team · The Reorg as Strategy |
| Interfaces | The Review Bottleneck · The Platform Nobody Asked For · The Unowned Interface |
| Decision rights | The Feature Factory · The Escalation Ladder · The Consensus Stall |
| Incentives | The Output Scoreboard · The Ladder as Checklist · The Hero Culture |
