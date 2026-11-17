# Style Guide for Chapter Writers — SETTLED: Architecting Payments and Revenue Infrastructure

Read this, `../PLAN.md` (your chapter contract and the teaching discipline), `scenario-ledger.md` (the shared fictional facts) and the research briefs named in your contract **before writing**. The sibling book whose format this one follows is ORDERED (`_journals/commerce-platform-architecture/`; read `posts/12-payments/index.md` as the model chapter for format, evidence handling and density). The sibling that already covers payments from the finance side is RECONCILED (`_journals/finance-systems-architecture/`, chapters `20-payments-fundamentals`, `21-adyen`, `22-stripe`, `25-payments-to-ledger`): link to it, do not repeat it.

**This book differs from ORDERED in two ways.** Its reader is a software engineer or architect, so it goes deeper technically. And it is anchored on two real companies, so the evidence discipline carries more weight than anywhere else in the series: a wrong or unsourced sentence about how Stripe or Adyen works is the worst defect a page can have.

## Voice and audience

- The reader is an **engineer or architect who is new to payments**. Do **not** explain what an API, a database, a queue, a webhook endpoint, replication or a retry is. **Do** explain every payments, banking, card-network, regulatory, billing and accounting term the first time it appears in each chapter, in one plain sentence or clause, before using it (issuer, acquirer, interchange, BIN, clearing, presentment, settlement, chargeback, representment, 3-D Secure, SCA, network token, cryptogram, PayFac, sponsor bank, safeguarding, mandate, dunning, proration, merchant of record, deferred revenue). Expand every acronym on first use in each chapter. Link to the chapter that owns the term (PLAN "Owns").
- **The problem before the mechanism.** Every chapter opens with what goes wrong and who loses money or trust, before it names a component. Tie the problem to the book's central idea where it fits: the gap between the instant answer and the slow truth.
- **Direct and concrete.** Use "you" for the reader. Short sentences. One idea per paragraph. Prefer a worked example with numbers to an abstraction. Do not stack three new terms in one sentence.
- First person ("I", "my") is the author speaking as an architect who builds on payment providers: judgement and recommendations ("I would…", "The rule I use…"). Use it in the trade-offs, the take-aways and the Larkfield scene; keep the analysis impersonal. Never claim specific real employers, real incidents or inside knowledge of any company.
- **American spelling** (organization, authorization, behavior, canceled, program) except in proper names and quotations (Adyen writes "authorisation"; quote it as written). The word for a regulatory permission is spelled "licence" as a noun in EU and UK contexts when quoting, "license" otherwise; pick "license" in running prose and keep the chapter permalink `licences-and-safeguarding` as it is. Plain, declarative sentences. No marketing language ("seamless", "robust", "leverage", "cutting-edge", "game-changer", "unlock", "empower", "holistic", "best-in-class", "world-class", "frictionless" except as the 3-D Secure technical term, "delight", "revolutionize", "journey" as a buzzword — the book uses "journey" only for the payment's journey).
- Explain **what problem a system solves and why it is hard, how the mechanism works, which designs exist, what trade-offs they introduce, and how Stripe and Adyen each do it** — not feature lists. A paragraph that could appear unchanged in either company's marketing does not belong.

## Evidence discipline (non-negotiable)

Six kinds of statement; make the kind obvious from wording and source:

1. **Documented fact** — a company's public statement (engineering blog, documentation, API reference, conference talk, annual or shareholder letter, investor filing, press release), a standard, a network rule, a regulation, a date, a number. Attribute it in the sentence (who said it, in what kind of document, when) and list the source with its URL under Sources and Evidence; the running text carries no external URLs, as in ORDERED. **For company evidence, give the year in the sentence** ("Stripe's 2017 engineering post described…", "Adyen's H1 2026 results report…", "Stripe's documentation (n.d., accessed November 2026) says…"). Only use facts tagged VERIFIED or WIDELY REPORTED in the briefs, or that you verify yourself by fetching the page. Prefer short verbatim quotes in double quotes for the load-bearing claims.
2. **Industry practice** — what payment companies and integrators commonly do. Phrase as "commonly", "a typical design is"; no invented percentages.
3. **Reference-architecture inference** — how a system is plausibly built. When it concerns a real company, **label it** on its own line: `> **INFERENCE, NOT DOCUMENTED:** …`. Never present inferred internals of Stripe, Adyen or any real company as fact. Do not invent service names, table names, data-center locations, volumes, team structures or algorithms.
4. **Recommendation / judgement** — the author's view, with reasoning and the conditions under which it does not hold.
5. **Illustration** — Larkfield. Always fictional; say so the first time in each chapter ("Larkfield, the fictional studio-software platform this book follows").
6. **Assumption** — illustrative volumes, latencies, costs, fees and percentages that are not ledger facts and not documented: label them ("Assume…", "an illustrative figure of…", `*(assumption)*` in table cells).

**Evidence age.** Much of the best public material about Stripe's internals is old (idempotency and rate limiting 2017, API versioning 2017, online migrations 2017). When a source is older than about three years, say so where you use it: `**(Evidence age: N years; the current system may differ.)**`, and, where current documentation confirms or contradicts the old account, say which. Documentation pages are undated and change: cite them as "n.d., accessed November 2026".

**Source quality.** Prefer primary sources: Stripe and Adyen engineering blogs (stripe.com/blog/engineering, stripe.dev, adyen.com/knowledge-hub and its tech blog), official documentation and API references, conference talks by their engineers, Stripe's annual letters and newsroom, Adyen's annual reports, half-year results and shareholder letters, card-network rules and documentation (Visa, Mastercard, EMVCo), standards bodies (PCI SSC, ISO), regulators and official legal texts. Use secondary analysis only to fill gaps and **say so in the sentence** ("according to trade press…", "a secondary source") and in the source entry ("(secondary source)"). Never cite Wikipedia for a load-bearing claim, a Productscape file, a research brief, or a sibling book's research brief.

Vendor-specific behavior and time-sensitive facts carry a date: "as of November 2026", "Stripe API version 2026-09-30". Separate historical from current, announced from generally available, preview from released, acquired from integrated. Vendor performance claims (uplift percentages, fraud reduction) are the vendor's claims: attribute them and do not generalize. Company-reported volume is not revenue; never rank companies by figures that measure different things. Where the evidence runs out, **say so** ("No public source describes how…; what follows is a reference-architecture inference").

## Required section: "Stripe and Adyen: Where They Differ"

Every chapter in Parts I–VIII has an H2 with this exact title. It contains a table and a short reading of it:

```markdown
## Stripe and Adyen: Where They Differ

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| <aspect> | <documented fact, with year or "n.d., accessed November 2026"; or "Not public"> | <same> | <one clause, an inference labeled as such, or "No material difference in the public record"> |
```

Rules: 3–7 rows; every Stripe and Adyen cell is either a documented fact linked or cited in the chapter, or the words "Not public"; the last column is the author's reading and is introduced once, in the sentence before the table, as inference. After the table, two or three sentences on what an integrator should do differently on each. If the public record shows no real difference, write a three-line section that says so; do not manufacture one.

## Three tiers of take-away (required)

Every chapter (not part intros) ends its argument with:

```markdown
## What to Take Away

**Established.** <2–4 bullets: what the field agrees on, with the evidence or standard behind it.>

**Depends on context.** <2–4 bullets: recommendations that hold under stated conditions; say the condition and what changes it.>

**The author's synthesis.** <1–3 bullets: the author's own position, marked as such, with the reasoning in one clause.>
```

## Page format

Folder: `posts/NN-slug/` with `index.md` and `spec.json`. Front matter (no tags, no icon or logo until art is generated):

```yaml
---
title: "<Title from PLAN>"
date: 2026-11-17
author: Željko Obrenović
excerpt: "<2 sentences: the question and the answer in brief, in plain language>"
permalink: <permalink from PLAN>
timetoread: <N> min read
---
```

`timetoread` is the article's word count divided by 230, rounded. Never write `\"` inside a front-matter value: the build does not unescape it. Use typographic quotes (“ ”) inside titles and excerpts.

Then, in this order (exact labels):

```markdown
> **IN THIS CHAPTER, YOU WILL:** <exactly one sentence, at most about 25 words>

> **KEY POINTS:**
>
> * **<Bolded lead phrase.>** <One or two sentences.>
> * **<…>** <…>
> * **<…>** <…>

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **<Pattern name>** — <chapter-specific reason, one sentence>.
> * **<Pattern name>** — <…>

<br>
<Lead paragraphs: 2–4 short paragraphs that frame the problem; bold 1–3 key phrases.>

**Where we are in the payment's journey.** <One short paragraph: which step of Mila's class pass (the recurring payment in the ledger) this chapter covers, or, for chapters off the payment's path, how it bears on it.>

<A roadmap paragraph that names every section of the chapter in order.>
```

Exactly three KEY POINTS. Two or three failure patterns, chosen by strength of connection. Part intros open with KEY POINTS only (three tight bullets), then `<br>`, and end with a `## Chapters in this part` list.

Body (a guide, not a rigid template — **name sections by content**, not generic labels, but cover these in roughly this order):

1. **Setting the scene at Larkfield** — a concrete 2026–2027 situation from the ledger that poses the chapter's question (one section, early, short).
2. **The problem and why it is hard** — with the vocabulary introduced: parties, states, who holds the money and the risk.
3. **How the mechanism works** — components, messages, states, data ownership; a small requirements table (how fast, how consistent, how available, what happens on failure) where flows are discussed; at least one figure.
4. **The designs** — the two to four realistic ways to build it, each in a paragraph or two.
5. **Trade-offs** — a comparison table; when each design is right.
6. **Stripe and Adyen: Where They Differ** — required (above). Longer documented material about each company's implementation belongs in sections 3–4 with its dates; this section is the comparison.
7. **In practice at Larkfield** — a worked example with ledger numbers, on one or both providers.
8. **When it goes wrong** — duplicates, unknown outcomes, late or missing events, partial failures, provider outages: detection and recovery.
9. **What to Take Away** — the three tiers.
10. **Questions to Ask** — 6–10 numbered questions the reader can take into a design review or a provider evaluation.
11. A closing paragraph that hands off to the next page in reading order with a `[[link]]`.
12. `## Sources and Evidence` — three groups with italic labels on their own line: *Company, product and investor sources*, *Standards, regulation and official documentation*, *Research and practitioner sources*. Each entry is one bullet: `- [Title](URL), Publisher or author, publication date (or "n.d., accessed 2026-11") — one clause on what it supports.` Add "(secondary source)" or "(evidence age: N years)" where it applies. One URL per bullet where practical. If a group is empty write `- None.` End the section with the line: "Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement."

Case studies (Part X, chapters 46, 47, 49) follow ORDERED's case anatomy instead: `## How to Read This Case` (labels, research cut-off, unreachable sources), thematic sections in system or chronological order with dated quotes and `**(Evidence age: …)**` marks, each ending in an `> **INFERENCE, NOT DOCUMENTED:**` block where the author interprets, a "what transfers" table (`Lesson | Evidence | Transfers?`), `## Where the Evidence Stops` (5–7 bullets), then What to Take Away, Questions to Ask, hand-off, Sources.

JOURNEYS chapters (Part IX) are a narrative plus a step table (`Step | Party or system | Message or record | Promise made | What can fail here → chapter`) and one sequence-style figure; they have What to Take Away and Sources but no "Where They Differ" section (they show both providers inline).

**Length.** Aim for **4,000–5,500 words** (front matter to the start of "Sources and Evidence"); **never over 6,500**. JOURNEYS 4,000–5,500; case studies 4,500–6,000; part intros 800–1,200. **Do not pad.** Where the contract marks a chapter as expected to be short, or the briefs show little public evidence, 2,000–3,000 words is right, and the chapter must say where the evidence stops. Depth beats breadth: one well-worked example beats five mentions.

## Figures

**No mermaid.** Every figure is a generated illustration. Write each one as an `illustration-placeholder` block in the article-illustrator skill's format (`.claude/skills/article-illustrator/SKILL.md`, "Placeholder format"): asset path `assets/images/<folder>/<id>.jpeg`, id in kebab-case starting with the folder number, `aspect_ratio` "16:9", a `caption` that states the figure's point in one sentence using only numbers that appear in the chapter, and a `prompt` that gives 5–9 elements with positions, quoted 1–3 word labels and every arrow named. Writers stage placeholders only (status "pending") and do **not** run the generator; a later illustration pass generates, inspects and replaces them with `![alt](asset)` followed by `**Figure N:** *caption*`. Refer to figures in the text by what they show ("the figure below"), not by number, until they are numbered.

Write **3–4 placeholders per chapter**: one or two that carry structure (a message flow between parties, a state machine, a funds flow, a component layout) and one or two conceptual (a metaphor or before/after that makes the central point memorable). Part intros and preface pages: 1–2. Reference pages: none.

End every prompt with the book suffix:

"Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people."

Because figures may not show brand names, a figure that compares the two providers labels them "Provider A" and "Provider B" and the caption says which is which.

Use GitHub tables generously: parties and who holds the risk, state tables, message fields, design comparisons, requirement tables, the "Where They Differ" table, "What it promises / What it does not promise".

## Cross-links

Link chapters with `[[permalink]]` — the build turns them into titled links. Valid permalinks (this book): `introduction`, `how-payments-got-complicated`, `where-payment-systems-go-wrong`, `meet-larkfield`, `part-1` … `part-10`, `journey-of-a-payment`, `payment-authorization`, `clearing-and-settlement`, `refunds-reversals-and-disputes`, `payment-economics`, `acquiring-and-network-connectivity`, `local-payment-methods`, `payment-state-machines`, `authorization-optimization`, `payment-routing-and-orchestration`, `in-person-payments`, `payment-ledgers`, `balances-and-funds-flows`, `payouts-and-money-movement`, `payment-reconciliation-and-reporting`, `licences-and-safeguarding`, `payment-api-design`, `idempotency-and-retries`, `payment-api-versioning`, `payment-webhooks-and-events`, `payment-developer-platform`, `tokenization-vaulting-and-pci`, `network-tokens`, `payment-fraud-and-risk`, `three-d-secure-and-sca`, `payment-compliance-and-regulation`, `subscriptions-and-billing-engines`, `usage-metering-and-rating`, `invoicing-collections-and-dunning`, `billing-and-payment-tax`, `billing-revenue-recognition`, `merchant-of-record`, `platform-payment-models`, `platform-onboarding-and-verification`, `splits-balances-and-platform-payouts`, `embedded-finance`, `payment-reliability-and-availability`, `payment-data-stores-and-consistency`, `payment-multi-region-and-data-residency`, `payment-peak-load`, `payment-safe-change`, `journey-card-payment`, `journey-failed-renewal`, `journey-platform-payment`, `journey-dispute`, `case-stripe`, `case-adyen`, `stripe-and-adyen-bets-compared`, `payment-contrast-cases`, `payments-what-is-moving`, `domain-coverage`, `toolkit`, `glossary`, `bibliography`.

Allowed links to sibling books (for depth the reader can follow; do not re-teach them):

- RECONCILED (finance): `payments-fundamentals`, `adyen`, `stripe`, `payments-to-ledger`, `designing-financial-ledgers`, `traceability-and-reconciliation`, `case-uber-payments`, `accounting-for-architects`, `resilience-and-security`.
- ORDERED (commerce): `commerce-payments`, `tax-invoicing-and-ledger`, `events-consistency-and-reconciliation`, `api-contracts-and-versioning`, `commerce-security`, `ai-and-agentic-commerce`, `peak-load-and-reliability`.
- LISTED (marketplaces): `fraud-prevention`, `marketplace-regulation`.
- Architecting Agentic Systems: `side-effects-and-external-actions`, `agent-identity-and-least-privilege`.

Note that `[[stripe]]` and `[[adyen]]` are RECONCILED's finance-side chapters; this book's own company chapters are `[[case-stripe]]` and `[[case-adyen]]`. Link where it helps (typically 8–20 per chapter). Never invent a permalink: a typo can silently resolve to another journal's page.

## Failure patterns (the opening guide `where-payment-systems-go-wrong`)

Use these exact names:

| Pattern | Warning sign | Family |
| --- | --- | --- |
| **The Double Charge** | A timeout is retried as a new request, and the customer pays twice. | Money truth |
| **The Phantom Payment** | A system believes a payment succeeded, or failed, without the provider's confirmed record saying so. | Money truth |
| **The Orphaned Refund** | Refunds, reversals and chargebacks arrive weeks later and nobody can tie them to the original payment. | Money truth |
| **The Black-Box Balance** | Money sits in a provider balance that nobody can break down into payments, fees, refunds and reserves. | Money truth |
| **The Stranded Payout** | A payout is marked sent, never arrives or comes back, and no one owns the difference. | Money truth |
| **The Trusted Doorbell** | Webhooks are treated as complete, ordered and delivered once. | Integration |
| **The Version Cliff** | An integration is pinned to an old API version until an upgrade is forced, all at once. | Integration |
| **A Card by Any Other Name** | Every payment method is assumed to behave like a card: instant, capturable, refundable, disputable the same way. | Integration |
| **The Vault Hostage** | Stored cards exist only as one provider's tokens, so the business cannot move. | Trust |
| **The Card in the Log** | Card data reaches a system that was never meant to see it, and compliance scope grows silently. | Trust |
| **The Open Till** | An endpoint that can start a payment has no limit, so attackers use it to test stolen cards. | Trust |
| **The Frozen Seller** | Verification is treated as a one-time form; a requirement changes and payouts stop. | Trust |
| **The Single Rail** | Every payment depends on one provider, one acquirer or one region, and nobody has rehearsed the switch. | Platform and scale |
| **The First of the Month** | A peak everyone could predict (renewals, a sale, a launch) meets limits nobody tested. | Platform and scale |
| **The Borrowed Blueprint** | An architecture is copied from a provider a thousand times larger without its reasons. | Platform and scale |
| **The Accidental Bank** | A platform holds, moves or lends other people's money without knowing which license and liability that takes. | Platform and scale |

## Larkfield usage

- Use the cast, systems, figures and incidents in `scenario-ledger.md`. Reuse the recurring worked examples (Mila's class pass, Mila's membership renewal, the refund after payout, the €120 dispute, the annual plan, the first of the month) and the named incidents (the Double Charge, the Silent Webhook, the Payout That Bounced, the Version Cliff, the Card-Testing Weekend, the Renewal Wave, the Frozen Studios, the Unexplained €0.4 Million) when relevant; amounts and dates must match.
- Time: chapters are set in **2027** (Femke de Graaf's first year) unless the contract says otherwise. The Keel decisions (K1–K8) are canonical; chapters explain them, they do not change them.
- Larkfield uses Stripe and Adyen by name. Its own systems are named by role ("the payment service", "the payment record store", "the ledger", "the booking app", "the webhook receivers", "the reconciliation job", "the data warehouse", "the front-desk app"). What Larkfield experiences with a provider is illustration, never evidence about the provider: a provider behavior shown in a Larkfield scene must also be documented and cited in the chapter.
- You may add *local* details (a meeting, an interface, an illustrative metric) that do not contradict the ledger. Record genuinely new **canonical** facts other chapters might rely on by appending to "Additions by chapter" in `scenario-ledger.md` (append only; never rewrite others' lines).
- The cast's pronouns are in the ledger. For real people (authors, cited engineers and executives) use their names; use they/them if you do not know their pronouns.

## Spec file

Each page has an outcome spec `spec.json` next to `index.md`, written with the `spec-creator` skill against `_wiring/outcome-specs/post-spec.schema.json` and the journal spec, and validated with `python3 _wiring/validate_spec.py payments-platform-architecture <folder>`. The article is written from the accepted spec unit by unit (the `detailed-article` skill) and may not add, drop, merge or reorder units. The style guide's page format governs how units are rendered (callouts, exact labels, required sections).

## Quality bar — check before finishing

- An engineer new to payments can define every payments term the chapter uses from the chapter alone; every acronym is expanded on first use.
- Every company-specific claim is traceable to a dated source in the chapter's Sources and Evidence; no invented internals; inferences labeled; old evidence flagged; illustrative numbers labeled as assumptions or as Larkfield.
- The "Stripe and Adyen: Where They Differ" table is present (Parts I–VIII) and every cell is a cited fact, "Not public", or labeled inference.
- At least one Larkfield worked example with ledger numbers; at least one trade-off table; a "When it goes wrong" treatment; "What to Take Away" with the three tiers; Questions to Ask; Sources and Evidence in the exact format.
- 3–4 illustration placeholders with valid JSON.
- No paragraph that could appear unchanged in a vendor brochure. No padding: if the evidence is thin, the chapter is short and says so.
- Cross-links use only valid permalinks.
