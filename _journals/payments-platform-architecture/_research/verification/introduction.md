# Verification — introduction

Verification pass of 17 November 2026. Every external source in the page's Sources section was fetched in this session with `curl` (User-Agent "Mozilla/5.0 (research-bot)") and read as text; the Adyen Annual Report 2025, the Stripe annual letter 2025 and the Visa rules were read as PDFs converted with `pdftotext`. All 13 original URLs returned HTTP 200. `stripe.com/annual-updates/2025` and `stripe.com/legal/acquirer-disclosure` redirect to a country edition from this network (`/nl/`, `/en-nl/`); the unprefixed URLs are kept. Quotations were matched against the fetched text after normalizing typographic quotes.

Because the page describes the book, a second table checks its statements about the book against `config.yaml`, the style guide, the journal spec, the chapters and `_research/verification/`.

## A. Claims about companies, standards and sources

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen Annual Report 2025: it chose to "develop and operate the essential layers of the financial stack ourselves" | https://investors.adyen.com/financials/2025 (PDF from the page's download button) | confirmed | Report: "we would develop and operate the essential layers of the financial stack ourselves. That decision set us on a long-term path" |
| 2 | 84% of 2025 volume was full-stack | same PDF | confirmed | "Of processed volumes, 84% were full-stack volumes, up from 83% in 2024." The report does not define the term (chapter 47 says so), so the page now puts “full-stack” in quotation marks as Adyen's word |
| 3 | Annual report signed 5 March 2026; audited | same PDF | confirmed | "March 5, 2026"; auditor's report present |
| 4 | On 1 July 2026 Adyen closed two acquisitions | https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates | confirmed | "Both transactions officially closed on July 1, 2026" (Talon.One, Orb) |
| 5 | Stripe's acquirer disclosure names a Stripe company as acquirer in the EEA | https://stripe.com/legal/acquirer-disclosure | confirmed | "European Economic Area Payment Method Acquirer is Stripe Technology Europe, Ltd." |
| 6 | The disclosure lists a bank of Stripe's own among its US acquirers | same | confirmed | "Stripe MALPB, 505 N Angier Avenue NE, Atlanta" is the last entry under United States ("Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers"). That it is a limited-purpose bank rests on ruling 33(a), not re-fetched here |
| 7 | Stripe idempotency post is from 2017 | https://stripe.com/blog/idempotency | confirmed | Displayed "February 22, 2017", Brandur Leach |
| 8 | Stripe rate-limiting post is from 2017 | https://stripe.com/blog/rate-limiters | confirmed | "March 30, 2017", Paul Tarjan |
| 9 | Stripe API versioning post is from 2017 | https://stripe.com/blog/api-versioning | confirmed | "August 5, 2017", Brandur Leach |
| 10 | Adyen's account of its accounting system is from 2021 | https://www.adyen.com/knowledge-hub/design-to-duty-adyen-architecture-part2 | confirmed | Displayed "August 23rd, 2021", "By Willem Pino, Tech Lead, Adyen" |
| 11 | Evidence age 9 years (2017 posts), 5 years (2021 post) | arithmetic | confirmed | — |
| 12 | Stripe's API reference "still describes keys that can be removed once they are at least 24 hours old", as confirmation of the 2017 post | https://docs.stripe.com/api/idempotent_requests ; https://stripe.com/blog/idempotency | corrected | The reference says "For API v1, you can remove keys from the system automatically after they’re at least 24 hours old." But the 2017 post gives no retention period (read in full: no "24 hours"), so "still" claimed a confirmation that does not exist. Now: the reference "still describes the 2017 post's idempotency key, and says keys can be removed once at least 24 hours old". Spec p17 evidence and the two source entries reworded |
| 13 | "That confirms the interface, not how keys are stored today" | journal-spec entry (AC-4, corrected today) | confirmed | Reworded to "how Stripe stores keys today", to agree with the corrected entry, which limits the absence to Stripe |
| 14 | Adyen documentation: "We periodically load test this system with merchants who hold transactions and then release the transactions in bulk." | https://docs.adyen.com/industries/peak-season | confirmed | Character for character. Citation completed to "(n.d., accessed November 2026)" (ruling 30) |
| 15 | Stripe engineering post of May 2024: "a scheduling service that looks for database records meeting certain criteria" | https://stripe.dev/blog/test-clocks-how-we-made-it-easier-to-test-stripe-billing-integrations | confirmed | Dated 2024.5.09, Ji Huang; the passage concerns subscriptions whose billing periods have just ended |
| 16 | Adyen is listed and files audited accounts | Annual Report PDF; press release ("AMS: ADYEN") | confirmed | — |
| 17 | Processed volume €1,394.3 billion | Annual Report PDF | confirmed | "Processed volume for 2025 was €1,394.3 billion" |
| 18 | Net revenue €2,364.2 million | Annual Report PDF | confirmed | "Net revenue for 2025 was €2,364.2 million" |
| 19 | Stripe letter for 2025: "$1.9 trillion in total volume" | https://stripe.com/annual-updates/2025 (desktop PDF linked from it) | confirmed | "businesses running on Stripe generated $1.9 trillion in total volume, up 34% from 2024". The landing page itself says only "generated $1.9 trillion"; the quotation is in the PDF, and the source entry now says so |
| 20 | Letter dated 24 February 2026, Patrick and John Collison | same PDF | confirmed | "February 24, 2026" |
| 21 | "a measure it does not define" | same PDF | confirmed | No definition of "total volume" in the letter |
| 22 | "Stripe has never published revenue" | same PDF; chapter 46 verification row 66 | hedged | The source on this page is one letter; "never" was checked in chapter 46 against four letters and the newsroom only. The 2025 letter also gives a revenue run rate for one product group ("Revenue suite … annual run rate of $1 billion"). Now: "no letter gives the company's revenue" |
| 23 | "The two volume figures count different things" | both documents | hedged | Stripe's measure is undefined, so the difference cannot be shown. Now "may count different things" |
| 24 | Neither has published how its webhook sender is built | chapter 20 and its verification; web search on stripe.com, docs.stripe.com, stripe.dev, adyen.com, docs.adyen.com | confirmed (absence) | Search in this session found only receiver-side documentation. A dated search result, as the page itself says |
| 25 | Neither has published a design for its card vault | chapter 22 and its verification | not checked independently | Taken from the owning chapter as verified; wording equals chapter 22 ("neither publishes a design") |
| 26 | Neither has published the topology and timing of a failover between data centers or regions | https://docs.adyen.com/industries/peak-season ; ruling 45; chapter 37 | confirmed | Adyen: load balancers "also manage the failover to the other data centers", no topology or timing. Stripe side taken from chapter 37 (not found for payments) |
| 27 | Sample row 1: Stripe API v1 at least 24 hours; Adyen 7 to 14 days after first submission | https://docs.stripe.com/api/idempotent_requests ; https://docs.adyen.com/development-resources/api-idempotency ; https://docs.stripe.com/api-v2-overview | corrected | Facts confirmed ("valid for a period of 7 to 14 days after first submission"). The row had been altered from chapter 18: the aspect was renamed, "API v2: 30 days" was dropped and the last cell said "outside Stripe's guarantee", which is wrong for API v2 (30 days: "occur within 30 days of each other"). Row restored to chapter 18's text; API v2 overview added to Sources |
| 28 | Sample row 2: Adyen key store unavailable | https://docs.adyen.com/development-resources/api-idempotency | corrected | Confirmed: "HTTP 503 – Service Unavailable status with the error code 703", then "Pause processing and retry the requests later" or "Fall back to non-idempotent processing". Cell restored to chapter 18's "503 with code 703; pause, or resend without the key" |
| 29 | Sample row 2: Stripe "Not public" | chapter 18 verification row 76; web search on stripe.com, docs.stripe.com, support.stripe.com, stripe.dev | confirmed (absence) | Nothing found on Stripe's behavior when its own key store is unavailable |
| 30 | Dispute window about 120 days (table, figure caption) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Edition of 24 October 2026: "120 calendar days from the Transaction Processing Date" in the dispute conditions read (11 occurrences) |
| 31 | The providers' documentation indexes do not list every page | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | confirmed, sentence corrected | Stripe's index has no "standalone selling" entry (ruling 39a holds). But Adyen's index does list the peak-season page, and the Stripe scheduler post is on stripe.dev, so neither example on the page was missed because of an index. "The first searches had relied on the … indexes" became "The first searches were too narrow, and the … indexes do not list every page" |
| 32 | A draft said Adyen had published nothing on load testing | `_research/verification/40-payment-peak-load.md` row 26; ruling 42 | confirmed | "I found no Adyen description of load testing" was corrected there |
| 33 | A draft said nothing was public about how Stripe schedules renewals | `_research/verification/27-subscriptions-and-billing-engines.md` rows 30, 45, 57; ruling 34 | confirmed | "None describes how renewals are scheduled" was corrected there |
| 34 | The most common error corrected was an over-confident "Not public" | all 60 files in `_research/verification/` | confirmed, approximately | Keyword count over 345 rows marked corrected: about 85 concern a statement of absence (in 38 files), about 55 a quotation or wording, about 31 a date, about 24 a link or format; the remaining 140 are mixed (numbers, names, statuses). Absence is the largest single kind, at about a quarter. The count is by keyword, not by reading every row |

## B. Statements about the book

| # | Statement | Checked against | Status | What changed |
| --- | --- | --- | --- | --- |
| B1 | Four preface pages, named | `config.yaml` | confirmed | — |
| B2 | Ten parts; chapter ranges 1–5, 6–11, 12–16, 17–21, 22–26, 27–32, 33–36, 37–41, 42–45, 46–50 and their subjects | `config.yaml`, journal spec | confirmed | Chapter 26 is given as "verification"; its subject is compliance (verification and monitoring). Left |
| B3 | Part questions | journal-spec part theses | confirmed | Shortened forms of the part questions |
| B4 | Four reference pages | `config.yaml` | confirmed | The pages are not written yet |
| B5 | Sixteen pattern names in four families, with the family glosses | style guide; patterns page | confirmed | Names exact; 5 + 3 + 4 + 4 |
| B6 | A failure is "started at one of the other twelve" | style guide table | corrected | Sixteen less five money-truth patterns is eleven. Now "eleven"; spec p11 too |
| B7 | Six kinds of statement; evidence-age flag; three tiers | style guide | confirmed | — |
| B8 | Chapter anatomy of Parts I–VIII; Parts IX and X | style guide; journal spec | confirmed | — |
| B9 | Routes table: each row's chapters cover the decision | chapter titles, rulings 2, 4, 5, 7 | confirmed | All permalinks are in the valid list |
| B10 | Toolkit has sixteen cards, including the idempotency key card and the reconciliation card | journal-spec entry `toolkit` | confirmed | The payment state card is no longer named (cut for length) |
| B11 | "Five promises" table | chapter 1 (owner), how-payments-got-complicated | corrected | The table had five rows and counted the dispute window as a promise by the bank, and merged clearing and settlement. Chapter 1: five promises in turn by the issuer, the merchant, the acquirer, the network and the provider, and a dispute window that is no promise. Table now has six rows in chapter 1's wording; lead sentence names the five parties; spec p06 reworded (same unit) |
| B12 | Agreement with the journal-spec entry corrected today (data-center layout, failover, key storage) | journal-spec entry | confirmed | The article states the failover wording of `how_why` exactly; it does not state the layout sentence; key storage reworded (row 13) |
| B13 | "Neither company reviewed it." | coordinator's instruction | not checked | Restored on instruction; an author's statement that no source can confirm |

## C. Larkfield

Checked against the ledger: Tuesday 9 March 2027 at 19:42, €120.00, Studio Noord on Adyen, fee €2.53, €117.47, payout Thursday 11 March, about 7 July 2027 (120 days); Rotterdam; 6,200 studios, €1.12 billion, 31.4 million payments, 44% and 56%; the studio is the seller and Larkfield never holds member funds; eight incidents "between the 2025 year-end close and November 2026" (ruling 24); the Double Charge of 1 November 2026 with 1,840 members; Femke de Graaf from January 2027; Keel K1 to K8. Weekdays agree with dates. No contradiction found.

## Ledger conflicts

None.

## Could not verify, and what was done

- **Card vault absence (row 25)** was not searched again; it stands on chapter 22's verification.
- **"Neither company reviewed it" (B13)** is the author's statement.
- **The share of corrections that were absences (row 34)** is a keyword count. The sentence was kept because absence is the largest single kind on that count; it is a plurality, about a quarter, not a majority.
- **Stripe MALPB as "a bank of Stripe's own"** rests on ruling 33(a) (Georgia regulator's bulletin), not re-fetched here.

## Format notes

- One external link remains in the running text: `[my work](https://obren.io)`, the author's own site, as in the introductions of the sibling books. It attributes no fact, so ruling 22 was not applied; the author may decide otherwise.
- "ERP" replaced by "the accounting system" (unexpanded acronym).
- Word count 3,500 (the maximum); `timetoread` 15 min is correct.
- Render check: the only entries are links to pages that do not exist yet (`part-10`, `domain-coverage`, `toolkit`, `glossary`, `bibliography`), which resolve to other journals' pages of the same name until they are written. Expected.

## For other pages

- `where-payment-systems-go-wrong` (key point 3 and the chains section), its `spec.json` (six places) and `journal-spec.json` (one place) say "one of the other twelve"; it is eleven.
- `journal-spec.json`, introduction entry, `know[4]`: "or at all (Stripe names no cloud region)" is stronger than chapter 39, which says Stripe names no AWS region but names data centers in the United States and India for login and identity data.
- `18-idempotency-and-retries` verification row 76 rests the Stripe "Not public" cell on the documentation index alone (ruling 39a asks for more); a web search in this session found nothing either, so the cell stands.
