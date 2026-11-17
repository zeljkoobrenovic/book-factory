# Verification — domain-coverage

Verified 17 November 2026 by an editor who did not write the page. The page states no fact about a company and cites no external source, so nothing was fetched from the web. It was checked against (a) the planning model's own files, re-counted by script, (b) `config.yaml`, and (c) the chapters as written.

How the chapters were read: for every capability graded **Section** or **Mention**, and for every "where it stands" and "why" cell, the named chapter was searched and the passage read. For capabilities graded **Chapter**, the check was the chapter's title, `config.yaml` description and section headings; those chapters were not re-read in full.

Totals: **96 claims checked: 92 confirmed, 4 corrected, 0 hedged, 0 removed, 0 unreachable.**

## Counts re-made from the model

| # | Claim | Counted | Status |
| --- | --- | --- | --- |
| 1 | 29 capability bricks | 29 | confirmed |
| 2 | Four groups: 7, 7, 8, 7 | Merchant Payments 7; Revenue Automation 7; Platform Money Movement 8; Shared Financial Foundations 7 | confirmed |
| 3 | Sub-groups 4, 2, 1 / 3, 3, 1 / 3, 4, 1 / 4, 2, 1, with the names given | same | confirmed |
| 4 | 7 product offerings | 7 | confirmed |
| 5 | 5 customer roles in 4 groups | 5 in 4 | confirmed |
| 6 | 48 logical records | 48 (9 + 5 + 11 + 9 + 10 + 4) | confirmed |
| 7 | 6 stress scenarios | 6 | confirmed |
| 8 | Comparison list of 10 companies | 10 | confirmed |
| 9 | Last reviewed 15 November 2026 | model files carry 2026-11-15 | confirmed |
| 10 | Quotation "does not attempt to describe … universal legal rights" | model's domain description, character for character | confirmed |
| 11 | Quotation "are inferred from the modeled jobs" | same file | confirmed |
| 12 | Quotation "authoring choices, not a published vendor roadmap"; no values or targets without a measurement source | same file | confirmed |
| 13 | The model has its own fictional class-booking example | model tutorial | confirmed |
| 14 | Tally 20 chapter, 6 section, 3 mention, 0 not covered; first table 14 rows, second 15 | recounted from the two tables: 10 + 10 chapter, 2 + 4 section, 2 + 1 mention | confirmed |
| 15 | All 29 keys and names "as the model names it" | 28 match; `rpts` is "Reporting, Sigma, and Data Export" in the model | corrected: name restored |

## Grades, capability by capability

| # | Capability | Grade | Checked in | Status | Note |
| --- | --- | --- | --- | --- | --- |
| 16 | `chck` Hosted Checkout | Mention | 22 "Four Ways to Collect a Card" (the redirect is one of four); 08 names Adyen's payment session; 32 names Checkout as a hosted page | confirmed | |
| 17 | `elem` Payment Elements | Section | 22, two sections: how the number reaches the provider; the page around the fields | confirmed | |
| 18 | `pmlk` Payment Links | Mention | 32 ("Checkout and Payment Links, Stripe's hosted payment pages"); 29 (Adyen's optional payment link after a failed rescue) | confirmed | |
| 19 | `pmtd` Payment Method Orchestration | Chapter | 07; 50 stablecoin section | confirmed | |
| 20 | `auth` Authorization Optimization | Chapter | 09, 02, 08 (25, 23, 03) | confirmed | |
| 21 | `term` Terminal and Reader Operations | Chapter | 11 | confirmed | |
| 22 | `rout` Processor Routing | Chapter | 10 (18) | confirmed | |
| 23 | `subs` | Chapter | 27 (43) | confirmed | |
| 24 | `usag` | Chapter | 28 | confirmed | |
| 25 | `invo` | Chapter | 29 (43) | confirmed | |
| 26 | `taxx` | Chapter | 30 (32) | confirmed | |
| 27 | `revn` | Chapter | 31 | confirmed | |
| 28 | `rpts` | Section | 15 "What Customers Get: Reports Itemized by Payout and by Batch", including the data offered as tables | confirmed | |
| 29 | `morc` | Chapter | 32 | confirmed | |
| 30 | `acct` | Chapter | 33, 34 | confirmed | |
| 31 | `kycb` | Chapter | 34, 26 | confirmed | |
| 32 | `iden` Identity Verification | Mention | 34 and 26: identity documents as one requirement | confirmed | |
| 33 | `split` | Chapter | 35 (44) | confirmed | |
| 34 | `pyot` | Chapter | 14 (35) | confirmed | |
| 35 | `issu` | Section | 36 "Card Issuing From the Issuer's Side" | confirmed | |
| 36 | `capm` | Section | 36 "Keep, Spend, Advance" and the availability table's financing row | confirmed | |
| 37 | `tres` | Section | 36; 16; 13 (currency in "What Leaves a Balance Without a Payout") | confirmed | |
| 38 | `rada` | Chapter | 24 | confirmed | |
| 39 | `disp` | Chapter | 04, 45 | confirmed | |
| 40 | `ledg` | Chapter | 12, 13 | confirmed | |
| 41 | `reca` | Chapter | 15 | confirmed | |
| 42 | `webh` | Chapter | 20 | confirmed | |
| 43 | `devx` | Chapter | 21, 17 | confirmed | |
| 44 | `mand` | Section | 50 "Agents That Pay: Who Authorized the Purchase" | confirmed | |

## "Covers briefly" table (where it stands, why)

| # | Row | Status | Note |
| --- | --- | --- | --- |
| 45–47 | Hosted checkout, payment links, identity verification | confirmed | |
| 48–50 | Embedded payment fields, reporting and data export, issued cards | confirmed | |
| 51 | Financing offers, "why" | corrected | Said "Little is public beyond eligibility and repayment terms; the chapter is short and says so". Chapter 36 does not discuss eligibility and nowhere says it is short or that the record is thin. Now: it teaches who lends, how an advance is repaid and where it is offered, not how an offer is priced or underwritten |
| 52 | Financial accounts and business liquidity | confirmed | |
| 53 | Delegated authority, "why" | corrected | Said the chapter "teaches only what was released". Chapter 50 describes announced and preview items with a label each; what it limits to released things is its advice on what to build. Reworded to say that |

## "Left out" table

| # | Part left out | Checked | Status |
| --- | --- | --- | --- |
| 54 | Posting into an ERP's general ledger and approving the close → RECONCILED | 15 and 31 both hand off to `[[payments-to-ledger]]`; permalinks exist in the finance journal | confirmed |
| 55 | Accounting standards → `[[accounting-for-architects]]` | 31 links it; "How an Invoice Line Becomes a Schedule" | confirmed |
| 56 | Cart, offer and order facts → `[[commerce-payments]]` | the brick's own description places cart facts in the merchant's commerce systems | confirmed |
| 57 | Agent-commerce protocols → `[[ai-and-agentic-commerce]]`, `[[agent-identity-and-least-privilege]]` | 50: "covers the protocols; this section covers only the payment" | confirmed |
| 58 | Tax law by country and filing → no chapter | 30 "Four Places the Calculation Can Live"; it describes what the provider's product files, not how to file | confirmed |
| 59 | A company's own treasury → no chapter | no chapter in `config.yaml` | confirmed |
| 60 | Dashboard users and operator roles → no chapter | 21 headings: credentials, test environments, request limits | confirmed |

## The ten subjects

| # | Subject | Status |
| --- | --- | --- |
| 61–70 | Each of the ten rows: every chapter named exists in `config.yaml` and has that subject; the ten match the spec's record of the author's list | confirmed |
| 71 | "A section titled 'Stripe and Adyen: Where They Differ' in every chapter of Parts I to VIII" | confirmed: present in all 41 chapters 01–41, absent from 42–50 |

The author's original list itself is recorded only in this page's `spec.json`; `_input/` is empty and PLAN.md does not hold it. The table was checked against the spec's wording.

## What the book added, scenarios, roles

| # | Claim | Status | Note |
| --- | --- | --- | --- |
| 72–82 | Eleven "model has / book adds" rows | confirmed | Model side checked in the brick descriptions, records and tutorial (four dated milestones; one €80 booking walkthrough; "payment authentication" and "credential lifecycle" inside `auth`; idempotency inside `rout`; one brick `devx` for API, credentials and dashboard). Book side checked against `config.yaml`; sixteen failure patterns per the style guide |
| 83–88 | Six stress scenarios and nearest chapters | confirmed | Scenario names are paraphrased (the model says "delegated corporate budgets", "beneficiary-verification") |
| 89–93 | Five roles, responsibilities, Larkfield seats, starting chapters | corrected (one entry for the five names) | The column is headed "Role in the model" but the names were paraphrased ("Growth commerce lead"). Restored to the model's names: Growth Commerce GM, SaaS Revenue Operations Lead, Platform Payments GM, Platform Seller and Payout Recipient, Treasury and Finance Controller. Seats and titles match the ledger's cast |
| 94 | Opening paragraphs: four reference pages in `config.yaml` order; sixteen cards in the toolkit; six steps of the page | confirmed | |
| 95 | The page does not cite the model for any fact about a company | confirmed | The model appears in Sources as "not a source for any fact in this book"; the only quotations are the model's statements about itself |
| 96 | No local file path, no external URL | confirmed | |

## Format and rulings

- Front matter complete; one IN THIS SECTION sentence; exactly three KEY POINTS; Sources in the three groups with the closing line. `timetoread` 15 = 3,482 ÷ 230.
- 182 `[[permalink]]` links, 67 distinct, all valid: 60 of this book and 7 allowed sibling links, each of which exists as a permalink in its journal.
- No banned word; American spelling.
- `validate_spec.py` ok; `check_draft.py structure` pass (17 units aligned); build ok; render check OK.
- Spec changed only in its changelog.

## Could not verify

- Nothing was unreachable. The twenty "Chapter" grades rest on titles, descriptions and headings, as said above.

## Ledger conflicts

- None.

## For the author to decide

1. **The model is listed under Sources and Evidence**, with the words "not a source for any fact in this book". PLAN.md says the model "is never cited as a source in a published page" and the style guide says never to cite a Productscape file. The entry describes the page's subject and is not a citation for a fact, so it was left; the author may prefer to move it out of the Sources list.
2. **Two brick names contain a provider's product name** ("Payment Elements", and now "Reporting, Sigma, and Data Export"). They are the model's names and the page says rows are named as the model names them. If the author prefers the neutral wording, the sentence "named as the model names it" should change instead.
3. The model's stress scenario for currency redenomination has no nearest chapter; the page says "None". No action unless the author wants one.
