# Verification — part-10-intro (`part-10`)

Date: 2026-11-17. Verifier did not write the page.

**Method.** A part introduction cites no external source, so no URL was fetched. Every statement about a company was compared with the five chapters of Part X as they read now (`46-case-stripe`, `47-case-adyen`, `48-the-bets-compared`, `49-contrast-cases`, `50-what-is-moving`), by searching each chapter for the claim and reading the passage. "Source" below is the chapter that makes the statement. The chapters were not read end to end in this pass; a claim is "confirmed" only where the matching passage was found and read.

Counts: 46 claims checked; 41 confirmed, 0 corrected, 4 hedged to the chapter's wording, 1 unsupported and reworded, 0 unreachable.

## Claims

| # | Claim (short) | Source (chapter) | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen press release of 9 April 2026, "Unlike many providers that rely on a patchwork…single platform" | 47 (lead), 50 (source entry) | confirmed | Quotation equals chapter 47's character for character |
| 2 | Fourteen days later (23 April 2026) Adyen announced the Talon.One purchase | 47 (table: announced 23 April 2026) | confirmed | 9 + 14 = 23 April |
| 3 | Talon.One is a loyalty platform; price €750 million | 47 (table), 48 | confirmed | — |
| 4 | Orb announced 11 June 2026; usage-billing platform; $335 million | 47 (table), 48 | confirmed | — |
| 5 | Both deals closed on 1 July 2026 | 47, 48, 50 | confirmed | — |
| 6 | "Stripe is not a bank", attributed to Stripe's treasury documentation | 46 (lead and regulated-layer section), 48 | confirmed | Same attribution as chapter 46 ("Its treasury documentation says") |
| 7 | In November 2026 Stripe's US acquirer list named five banks and "Stripe MALPB, 505 N Angier Avenue NE, Atlanta" | 46 (table and text), 48, 49 | confirmed | Chapter 49: "next to five banks" |
| 8 | Acquirer defined as the card-network member that submits a merchant's payments and receives the money | 46, 48 | confirmed | — |
| 9 | Stripe MALPB is a limited-purpose bank of Stripe's own, in business since 28 May 2026 | 46 (Georgia regulator's bulletin), 48, 49 | confirmed | — |
| 10 | Parts I–VIII end each chapter with a "Where They Differ" table | 48 ("forty-one tables") | confirmed | — |
| 11 | Part IX found the same payment recorded in two vocabularies | journal-spec `transition_in` of Part X | confirmed | Not re-read in Part IX's chapters |
| 12 | Reading holds for banking and hosting | 48 (take-away: "holds for banking and hosting") | confirmed | — |
| 13 | Reading fails for card acquiring in Europe and much of Asia-Pacific, where Stripe's own companies acquire | 46 (table, take-away), 48 | confirmed | — |
| 14 | Cannot be tested on Stripe's motives: none published | 46, 48 ("Stripe has published none") | confirmed | — |
| 15 | Stripe publishes no volume per named acquirer | 46 ("no share of volume per acquirer"), 48 | confirmed | — |
| 16 | Adyen built on an acquiring license and became a bank | 47 (history page, first period 2006–2012; banking license 2017) | confirmed | Page gives no date for the license, as the chapter requires |
| 17 | Stripe launched with an API and assembled the regulated layer afterward, per market | 46, 50 | confirmed | — |
| 18 | By 2026 each was moving toward the other's position | journal-spec part thesis; 48, 50 | confirmed | Stated as the part's thesis |
| 19 | Research cut-off 17 November 2026; every claim dated | 46, 47, 48, 49 | confirmed | — |
| 20 | Documented, widely reported, inference kept apart | 47 ("How to Read This Case") | confirmed | — |
| 21 | "Not public" means not found by that date, not proof of absence | 48 | confirmed | — |
| 22 | Stripe is private; volume and customer counts in letters nobody audits; never revenue | 46 | confirmed | — |
| 23 | Adyen is listed and files audited accounts | 47, 49 | confirmed | — |
| 24 | Each case ends with what the record could not establish | 46, 47 ("Where the Evidence Stops") | confirmed | — |
| 25 | Stripe: an API in 2011, a suite with several products bought, a regulated layer per market | 46 | confirmed | — |
| 26 | Stripe's European companies are e-money institutions and acquire there | 46 (table) | confirmed | Term now defined in one clause, from chapter 46's definition |
| 27 | In the United States Stripe works under six named acquirers | 46, 48 | confirmed | — |
| 28 | Stripe volume $1.9 trillion for 2025; never published revenue | 46 | confirmed | — |
| 29 | Four interface practices transfer; about 2,000 database shards do not | 46 | confirmed | — |
| 30 | Adyen: acquiring license first, banking license 2017, US 2021, UK 2023 | 47 (KEY POINTS) | confirmed | — |
| 31 | Adyen 2025, audited: €1,394.3 billion processed, €2,364.2 million net revenue | 47 (table), 46 | confirmed | — |
| 32 | 84% of 2025 volume was full-stack | 47, 48 | hedged | "full-stack" put in quotation marks as Adyen's own term; chapter 47 says Adyen does not define it and marks its meaning as an inference |
| 33 | Adyen names banking partners where it has no acquiring license | 47 (take-away: "its risk section names banking partners") | confirmed | — |
| 34 | Chapter 48 adds no new fact | 48 ("This chapter adds no new fact") | confirmed | — |
| 35 | Eight bets, two of kind: who holds the money (licensed bank against e-money institutions with partner banks) | 48 | confirmed | — |
| 36 | Second difference of kind: "Adyen's own data centers against Amazon Web Services" | 47, 48 | hedged | Now "infrastructure Adyen manages itself against Amazon Web Services". Chapters document "We manage our own infrastructure in several data centers" and name no operators; the annual report speaks of "data center partners". Matches the reworded part thesis ("runs on servers it manages itself"). Same wording corrected in `spec.json` |
| 37 | The other bets narrowed in 2025 and 2026 | 48 | confirmed | — |
| 38 | PayPal's filing: a network of 439 million accounts | 49 ("439 million active accounts") | hedged | "active" added |
| 39 | Checkout.com reports ten acquiring licenses | 49 | confirmed | — |
| 40 | Block rents most of its acquiring and owns a Utah bank that lends to its sellers | 49 ("a Utah industrial bank") | hedged | "industrial" added |
| 41 | "A provider holds the permissions its first customers required" is the author's inference; three cases cannot prove it | 49 | confirmed | — |
| 42 | Agents change who authorized, stablecoins what the money is held in, instant payments when it has moved | 50 | confirmed | — |
| 43 | Adyen's agent product released in limited availability | 50 (June 2026 release; product page now names no phase) | confirmed | Past tense "was released" matches the chapter |
| 44 | Stripe's stablecoin balances are in preview | 50 ("public preview" in the United States) | confirmed | — |
| 45 | The EU's new payment rules were agreed and not yet law | 50 | confirmed | — |
| 46 | Closing: "each company adding what the other began with" | none | unsupported | No chapter says this (Adyen's purchases are not what Stripe began with). Reworded to the part thesis: "each company moving toward the other's position" |

## KEY POINTS against the part thesis

- Bullet 1 states the reading under test: equals the thesis question.
- Bullet 2: "order of construction, not a division of territory", holds for banking and hosting, fails for card acquiring in Europe, untestable on motives, each moving toward the other by 2026. All in the thesis claim. The bullet omits "much of Asia-Pacific", which is weaker than the thesis, not stronger.
- Bullet 3: the evidence rule; equals the third "believe" outcome of the part.
- The page nowhere uses the superseded wordings: it does not date Adyen's acquiring license to its founding, does not say Adyen owns its data centers (after fix 36), and calls the five other US acquirers "banks", not "partner banks".

## Chapter titles, questions and order

Order and permalinks equal `config.yaml` (46, 47, 48, 49, 50); the page title equals the section title. Each bolded question is a shortened form of the chapter's question in `journal-spec.json`; none changes its sense. Render check: all six `[[…]]` links resolve.

## Larkfield

| Fact | Ledger | Status |
| --- | --- | --- |
| 44% of 2026 member payment volume on Stripe, 56% on Adyen | Ledger lines for Stripe and Adyen (44%, €493M; 56%, €627M) | agrees |
| Payments team of 11; small ledger; no license sought | Ledger 2026 figures (11 in the payments team); chapter 47 (ledger since 2025) | agrees |
| Chief executive asks which provider to keep | Sofie Vermeer, CEO; chapter 48 | agrees |
| New head of payments engineering sorts a folder of three proposals | Femke de Graaf, joined January 2027; ledger addition for chapter 50 | agrees |
| Larkfield named as fictional once | lead, second paragraph | present |

No ledger conflicts.

## Format

- Front matter complete; opener is KEY POINTS only, exactly three bullets, then `<br>`; two illustration placeholders (captions checked: "five banks and one of its own", "closed on 1 July", both in the chapters); `## Chapters in this part` in config order; ends "Begin with [[case-stripe]]."; one-line Sources and Evidence. No external URL in the text.
- Words: 1,196 by `check_draft.py structure` (limit 1,200); `timetoread: 5 min read` equals 1,196 ÷ 230.
- `validate_spec.py payments-platform-architecture part-10-intro`: ok (copied fields equal the journal entry). `check_draft.py structure`: passes. Build: no errors. `render_check.py part-10`: OK, nothing unresolved.
- Spec: one phrase corrected ("own data centers" → "infrastructure Adyen manages itself"); changelog entry added. No unit added, dropped or reordered.

## Not verified, and what was done

- Nothing was fetched from the web; the chapters' own verification files are the evidence for the underlying sources.
- Claim 11 (Part IX) was checked against the journal spec's transition, not against the Part IX chapters.
- The style guide's banned-word list was not located by search; only American spelling was spot-checked (no finding).
- "The sources are company documents": chapters 46 and 49 also rest on a regulator's bulletin, two SEC filings and named secondary sources. The next sentence of the page covers secondary sources, so the sentence was left; the author may prefer "mostly company documents".

## For other pages

- None found. Chapter 48 (October 2027) says Femke de Graaf "leads payments engineering" and chapter 50 that she started in January 2027; these agree.
