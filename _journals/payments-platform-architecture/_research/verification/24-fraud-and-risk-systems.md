# Verification — 24-fraud-and-risk-systems (`payment-fraud-and-risk`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Adyen documentation through the `.md` variants; the EBA/ECB report and the Visa fact sheet as PDFs converted with `pdftotext`; the stripe.dev, stripe.com, adyen.com and visa.com pages as HTML with tags stripped). Quotations were compared as strings after normalizing typographic quotes, markdown emphasis and white space; for each one I also read the surrounding passage. The page's writer skipped the final re-read, so the page was also read for undefined terms and for vendor claims stated as fact.

Short source names: **S-RISK** = docs.stripe.com/radar/transaction-risk-prevention (the old `/radar/risk-evaluation` redirects here); **S-SET** = docs.stripe.com/radar/risk-settings; **S-RULES** = docs.stripe.com/radar/rules; **S-REV** = docs.stripe.com/radar/transaction-reviews (old `/radar/reviews` redirects here); **S-LISTS** = docs.stripe.com/radar/lists; **S-HOW** = docs.stripe.com/radar/how-radar-works; **S-CT** = docs.stripe.com/disputes/prevention/card-testing; **S-AFD** = docs.stripe.com/disputes/prevention/advanced-fraud-detection; **S-TYPES** = docs.stripe.com/disputes/prevention/fraud-types; **S-ACCT** = docs.stripe.com/radar/account-fraud-prevention; **S-CR** = docs.stripe.com/connect/radar; **S-CRISK** = docs.stripe.com/connect/risk-management; **S-2023** = stripe.dev/blog/how-we-built-it-stripe-radar; **S-2024** = stripe.dev/blog/shepherd-how-stripe-adapted-chronon-to-scale-ml-feature-development; **S-2026** = stripe.dev/blog/scaling-radar-fighting-fraud-with-agent-assisted-machine-learning; **S-LLM** = stripe.dev/blog/training-llms-for-risk-assessment; **S-PIS** = stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite; **A-RISK** = docs.adyen.com/risk-management; **A-PROF** = docs.adyen.com/risk-management/configure-your-risk-profile; **A-ML** = …/configure-your-risk-profile/machine-learning-rules; **A-CTRL** = docs.adyen.com/risk-management/control-traffic; **A-CASE** = docs.adyen.com/risk-management/case-management; **A-AB** = docs.adyen.com/risk-management/run-ab-test-experiments; **A-FDC** = docs.adyen.com/risk-management/fraud-data-collection; **A-DEP** = docs.adyen.com/account/balances/deposit; **A-BLOG** = adyen.com/knowledge-hub/catching-card-testing-at-scale; **ECB** = EBA/ECB 2025 Report on payment fraud (ecb.europa.eu PDF); **VAMP** = Visa Acquirer Monitoring Program fact sheet 2025 (corporate.visa.com PDF); **V-PR** = Visa press release of 7 May 2024 (usa.visa.com).

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe: "A payment is considered fraudulent when the cardholder didn't authorize it. Most fraudulent payments are made using stolen cards or card numbers." | S-TYPES | confirmed | — |
| 2 | EBA/ECB: theft of card details "more than 56% of the total value" of fraud on remote card payments in 2024 | ECB (section 3, text under Chart 7) | confirmed | Source says "in remotely initiated fraudulent card transactions" (around 65% by volume) |
| 3 | Stripe: after a fraud dispute "the business suffers a loss equal to the amount of the payment … also subject to a dispute fee." | S-TYPES | hedged | The source sentence starts "If the dispute is resolved in favor of the cardholder". Page said "after a fraud dispute"; now "when such a dispute is decided for the cardholder" |
| 4 | EBA/ECB 2024: card fraud rate by value 0.091% remote against 0.007% non-remote, "13 times higher in value" | ECB (p. 18) | confirmed | — |
| 5 | Stripe's definition of card testing: "testing a card (or multiple cards) on one site …" | S-TYPES | confirmed | — |
| 6 | Stripe's definition of friendly fraud | S-TYPES | confirmed | — |
| 7 | Stripe's definition used for "merchant fraud": "a fraudulent business takes payments without providing the services or goods" | S-TYPES | confirmed | Stripe's heading for it is "Marketplace fraud"; the page now says so |
| 8 | Account takeover is not defined in either company's documentation that was read | docs.stripe.com/llms.txt, docs.adyen.com/llms.txt, and every page above | confirmed | "takeover" has 0 hits in both indexes and in all fetched pages |
| 9 | Author's arithmetic: a 1% false-positive rate refuses "about ten good payments for every fraudulent one" at "9 euros in every 10,000" | ECB (p. 18) | corrected | The sentence divided a count of payments by a rate measured in value. Now uses the report's rate by number of payments (0.068%, about 7 in 10,000): about 100 good payments refused, some fifteen per fraudulent one |
| 10 | Stripe blocked outcome: `not_sent_to_network`, `blocked`, `highest_risk_level` | S-RISK | confirmed | — |
| 11 | Adyen: "Pre-authorization: … This saves issuer and scheme fees compared to blocking after authorization." | A-PROF | confirmed | Gloss added: "scheme" is Adyen's word for a card network |
| 12 | Adyen: post-authorization rules "can take extra signals into account … authentication results, CVC/CVV codes, or AVS responses" | A-PROF | confirmed | — |
| 13 | Stripe: built-in rules "block certain payments that the card issuer approved" | S-RULES | confirmed | Source: "You can enable Radar's built-in rules to …" |
| 14 | Stripe: "Payments placed into review are typically already successfully processed, unless you capture authorized payments later." | S-REV | confirmed | "capture" defined in one clause (was undefined) |
| 15 | Adyen: with capture delay for case management, "up to seven calendar days to reject a transaction"; the payment is already authorized | A-CASE | confirmed | — |
| 16 | Adyen: level "ranging from Very Low to Very High", "indicates the likelihood that a transaction will result in a fraudulent dispute", default block "high risk and above"; premium only | A-ML | confirmed | Page now says at first use that the rule is a premium feature. The page names five levels (Very Low, Low, Medium, High, Very High) without the word "five" |
| 17 | Stripe: "a risk score that ranges from 0–99"; 65 elevated, 75 high | S-RISK | confirmed | — |
| 18 | Radar blocks the highest level by default and allows elevated-risk payments | S-RISK, S-RULES, S-SET | corrected | True as defaults, but S-RULES marks the rule `if :risk_level: = 'highest'` "(Deprecated)" and S-SET says "Radar is deprecating the high risk block rule that uses risk score … you must use risk settings, which use separate models to block payments". Added, with the three newer scores (fraudulent dispute, early fraud warning, fraudulent payment). Also added that elevated payments go to a review queue on plans that have one |
| 19 | The score number is returned only on Radar Plus and Pro | S-HOW (row "Risk scores") | confirmed | Page now says Radar has four plans |
| 20 | "Neither company documents the payment score as a probability, so a score of 65 is a rank" | S-SET | corrected | S-SET: "This risk score is the probability that a payment results in a fraudulent dispute or early fraud warning." The page now quotes this, says neither company documents how a score or level maps to a percentage, and labels "rank, not 65%" as the author's reading. Same change in the comparison table and in "Established" |
| 21 | Stripe 2023: Radar "makes this decision, accurately, in less than 100 milliseconds"; evidence age 3.6 years | S-2023 (dated 2023.3.29) | confirmed | 29 March 2023 to 17 November 2026 = 3.6 years |
| 22 | Stripe 2024: "the time required to retrieve features directly impacts the overall payment API latency" | S-2024 (2024.4.15, Ben Mears) | confirmed | — |
| 23 | Stripe October 2026: the model "scores payments in milliseconds" | S-2026 (2026.10.19, Ryan Drapeau, Sai Samant) | confirmed | — |
| 24 | Adyen publishes no latency figure for the risk decision | A-* pages, plus configure-risk-settings, custom-rules, post-auth-rules, risk-lists, handle-risk-rule-notifications, skip-risk-rules, uplift, A-BLOG | confirmed (by search) | Only hit: a recommendation to run risk in the same data region "to reduce latency while running ShopperDNA risk checks". No figure |
| 25 | Stripe: retries get "the same allocation bucket, so each retry receives the same outcome" | S-RULES | confirmed | — |
| 26 | Stripe: "an error might cause risk evaluation to fail … unknown risk"; the example is `unknown_risk_level` with `authorized` | S-RISK | confirmed | — |
| 27 | Requirements table "Not documented" cells (Adyen consistency under retries; availability, both; Adyen behavior on failure) and the inference block | pages listed in row 24; Stripe radar, rules/reference, testing, optimize-risk-factors | confirmed (by search) | Searched for timeout, unavailable, fallback, fail, availability, uptime; nothing found |
| 28 | Stripe 2026: "a credit card that is new and untrusted to one business might have years of history elsewhere on Stripe …" | S-2026 | confirmed | — |
| 29 | Adyen: models "can detect recent fraud on a shopper's email address or recognize a good shopper because of a recent in-person payment on a card on the Adyen platform" | A-RISK | confirmed | — |
| 30 | Adyen "collects data about how shoppers interact with and use the payment form" | A-FDC | confirmed | — |
| 31 | Stripe marks the browser data gathered by its JavaScript as "Highest impact" among what a merchant can supply | S-CT, S-AFD | hedged | S-CT lists "Advanced fraud detection (Highest impact)" among information that affects "Stripe card testing models", not the fraud model in general. That advanced fraud detection is device and activity data collected by Stripe.js is on S-AFD, which was not in Sources. Sentence narrowed; S-AFD added to Sources |
| 32 | Stripe 2026: "For a payment made with a stolen card, it could take weeks … a fraud label for a payment we scored weeks earlier." | S-2026 | confirmed | — |
| 33 | "41% by day 14, 66% by day 30, and 86% by day 60 after the payment" | S-2026 | confirmed | The words are the chart's text description (image alt text), not the body. Page now says "the description of its chart" |
| 34 | Stripe 2026: the larger model "looked better in offline tests … and we had to roll back" | S-2026 | confirmed | Full sentence ends "to a model trained with the earlier sampling strategy" |
| 35 | Removing sampling added "more fraudulent examples labeled as legitimate, about 20 times more" | S-2026 | confirmed | — |
| 36 | "If the company with the most data misjudged a change" | none | unsupported | No source ranks Stripe's data against others'. Reworded to "a company with Stripe's volume of data" |
| 37 | "Both providers let a small share of risky payments through on purpose, as a holdout" (Stripe: "modifies the reported risk score so we can measure the performance of our models") | S-RISK, A-CTRL | hedged | Adyen says so directly. Stripe's sentence does not say blocked payments are let through; that it is a holdout is an inference. Relabeled in the paragraph, KEY POINTS, the comparison table and "Established" |
| 38 | Adyen control traffic: "A very small percentage of all transactions is randomly selected … settled regardless of their risk evaluation"; excludes "Transactions with an amount of EUR 2000 or higher" | A-CTRL | confirmed | There are five exclusions; page now says "among others". "Settled" glossed |
| 39 | Stripe: refund with reason `fraudulent` adds card fingerprint and email to the default block lists; "Our AI models respond to feedback you share with us" | S-RISK, S-LISTS | confirmed | "card fingerprint" glossed |
| 40 | Stripe 2023: from "relatively simple ML models (e.g., logistic regression)" through XGBoost plus a deep neural network to, "in mid-2022", "a pure DNN-only model" | S-2023 | confirmed | — |
| 41 | "the 2026 post confirms the architecture" | S-2026 | hedged | The 2026 post links to the 2023 one ("how we initially built it") and mentions "Shield's ResNeXt architecture"; it does not restate "DNN-only". Flag now reads "the 2026 post links back to this one and describes a neural-network architecture" |
| 42 | Shield "grew to roughly 30 million parameters, three times its previous size" | S-2026 | corrected | In the source the 30 million parameters belong to the version trained on the larger dataset, and the next sentences say that version was rolled back. The page presented the figure as Shield's size. Now says which version it is and that the production model's size is not stated; same fix in the comparison table and the list of gaps |
| 43 | Shield had "roughly 800 million transactions in its training set" | S-2026 | confirmed | It is the downsampled set before the scaling work |
| 44 | "the year's changes 'improved recall by over 8%'" | S-2026 | corrected | Source: "In a controlled comparison, the new configuration improved recall by over 8%". No year is given. Now "a new training configuration … in a controlled comparison" |
| 45 | Stripe speaks of "regular retraining" and gives no interval | S-2026 and Stripe documentation pages searched for "retrain" | confirmed | — |
| 46 | Adyen premium: "Machine learning powered fraud detection using global transaction data" | A-RISK | confirmed | — |
| 47 | Stripe: "you're ultimately responsible for payments you choose to accept …" | S-RISK | confirmed | — |
| 48 | Stripe 2023: "Radar incorrectly blocks just 0.1%" of legitimate payments | S-2023 | confirmed | — |
| 49 | Adyen: "The optimal blocking threshold … depends on your business model and the difference in cost between a fraud case and a false decline"; "the cost of a false decline (potential loss of lifetime value) mostly outweighs the cost of a fraud case" | A-ML | confirmed | — |
| 50 | Adyen recommends "a low or medium threshold to thin-margin retailers and a high one to sellers of digital goods" | A-ML | corrected | Source: "a High or Very High threshold". Now "a high or very high one" |
| 51 | Design table: Radar risk settings on Plus and Pro; Adyen blocking threshold per risk profile; Adyen review up to seven days | S-HOW (row "Risk preferences"), A-ML, A-CASE | confirmed | — |
| 52 | Rule actions (allow, block, review, request 3-D Secure); Stripe's example rule | S-RISK, S-RULES, A-PROF | confirmed | — |
| 53 | Stripe: "Implement any allow rules minimally, because they override the Stripe default rules …" | S-RULES | confirmed | — |
| 54 | Adyen: "Allow rules have the highest priority within a risk profile." | A-PROF | confirmed | — |
| 55 | Stripe: "200 transaction rules and 100 account rules" | S-RULES | confirmed | — |
| 56 | Rules "see only your own data" | S-RULES | hedged | Stripe rules can use Stripe's own `:risk_level:` and scores. Now "apart from the provider's risk level they work on your own data" |
| 57 | Stripe's rule tester "runs a simulation on the last 6 months of charges" | S-RULES | confirmed | — |
| 58 | Traffic allocation applies a custom rule to a percentage; at 0% the rule is evaluated without acting | S-RULES | confirmed | "available only for custom transaction rules" |
| 59 | Adyen premium: backtest custom rules; experiments "A/B test two risk profiles against each other" on "real transactions" | A-RISK, A-AB, custom-rules page | confirmed | — |
| 60 | Adyen post of October 2026: "verification, where bots iterate … and enumeration, where scripts systematically guess …" | A-BLOG (Jaap Stefels, displayed date "October 4th, 2026") | confirmed | — |
| 61 | Visa, May 2024: "Thirty three percent of enumerated accounts experienced fraud within five days"; "$1.1B annually in fraud losses" | V-PR (5/07/2024) | confirmed | Footnotes give the data as VAAI fiscal 2023; page and source entry now say "for fiscal year 2023" |
| 62 | Adyen: "Unlike chargeback fraud … card testing offers no explicit transaction-level signal." | A-BLOG | confirmed | — |
| 63 | Adyen: "Rotational attacks: Fraudsters continuously rotate details—such as IP addresses—…" | A-BLOG | confirmed | — |
| 64 | Adyen: subslices; a feature language compiled to Spark, Kafka and Flink; "Flink writes these streaming metrics to an Apache Cassandra feature store …" | A-BLOG | confirmed | — |
| 65 | "This is the one substantial description of a fraud model Adyen has published." | not checkable as an absolute | hedged | Now "the only substantial description of one of its fraud models that I found from Adyen". I did not survey the whole Adyen knowledge hub |
| 66 | Stripe: "A high decline rate might damage the reputation of your business with card issuers and card networks …"; extra fees | S-CT | confirmed | — |
| 67 | Visa: enumeration ratio definition; 2,000 basis points and 300,000 transactions; "requires acquirers to take proactive steps …" | VAMP | confirmed | Monitoring is monthly, as the page says |
| 68 | Stripe: "simple firewall rules or filters based on a single heuristic … are usually not sufficient"; recommends CAPTCHA, login before the payment form, rate limits | S-CT | confirmed | — |
| 69 | Card-testing prevention is in every Radar plan | S-HOW | confirmed | Supported on Lite, Standard, Plus and Pro |
| 70 | Adyen: "Machine learning: bot attack risk" is in basic and premium, has no configuration, "mostly prevents large scale attacks" | A-ML | confirmed | — |
| 71 | Stripe, May 2025: "While attacks are up industry-wide, they are down 80% on Stripe." | S-PIS (May 15, 2025) | confirmed | Vendor claim, labeled as such on the page |
| 72 | Adyen, October 2026: "increasing blocked card testing attacks by 28% on average, with zero impact on legitimate shoppers" | A-BLOG | confirmed | Vendor claim, labeled as such on the page |
| 73 | Stripe October 2026 post lists "Is the business trustworthy? … Should we adjust a business' credit reserves?" | S-LLM (2026.10.09) | confirmed | The post is about fine-tuning language models for risk assessment; "post on reviewing businesses" changed to "engineering post on risk assessment" |
| 74 | Stripe's account risk score "estimates the probability" of loss | S-ACCT | hedged | Source: "The score correlates to the probability that an account would cause losses to your platform." Quote lengthened to include "correlates to" |
| 75 | Adyen deposit: calculated daily from processing volume, chargebacks and refunds; withholds when exposure exceeds coverage "by more than EUR10,000" | A-DEP | confirmed | — |
| 76 | "No criteria, no models, no formulas for a reserve or a deposit" are public; listed again under gaps | A-DEP; docs.stripe.com/llms.txt, S-ACCT | corrected | A-DEP documents the deposit calculation in outline: fulfillment, chargeback and refund exposure (prediction "based on the past 180 days of data") against processing and securities coverage, with accepted risk "determined on a case-by-case basis". The page now says so and limits "not public" to the amounts, Stripe's reserve rules and both companies' acceptance criteria. For Stripe I found no documentation page on how Stripe sets a reserve (`/reserves` is 404; the index has no such page) |
| 77 | Stripe: "responsibility for your connected accounts' negative balances can belong to your platform or to Stripe" | S-CRISK | confirmed | — |
| 78 | On Connect, whose Radar rules apply depends on the charge type | S-CR | confirmed | Direct charges: the collecting account's; transferred charges: the platform's. "Stripe Connect" and "connected account" glossed |
| 79 | Stripe: "Allowlists can allow fraudsters to operate without restrictions and bypass controls"; entries on its default card-fingerprint allow list last at most 30 days | S-LISTS | hedged | Source: "entries on default fingerprint allowlists" (card, ACH and SEPA fingerprints). Wording widened |
| 80 | Visa: ratio of fraud and disputes to settled transactions; "Excessive Merchant threshold reduced to >=150bps" in AP, Canada, EU and US on 1 April 2026 | VAMP (footnote 5) | confirmed | The ratio covers card-not-present transactions and has a minimum monthly count of 1,500, which the page does not mention |
| 81 | Stripe announced a payments foundation model in May 2025; the October 2026 post describes Shield without mentioning it | S-PIS, S-2026 | confirmed | "foundation" does not occur in S-2026 |
| 82 | Adyen: each custom rule is set to run before or after authorization | custom-rules page | confirmed | "For each rule, you configure if the rule should run before or after authorization" |
| 83 | "Where They Differ" table, all Stripe and Adyen cells | rows 10–20, 37–38, 42, 57–59, 69–70, 21, 24 | confirmed after the corrections in rows 18, 20, 37, 42 | "Not public" cells (Adyen latency, Adyen fraud-risk model) checked against the Adyen index and pages in row 24 |
| 84 | Publication dates and authors of the five dated Stripe and Adyen posts and the Visa release | each page | confirmed | Displayed dates used (ruling 25) |
| 85 | All 29 URLs in Sources resolve (27 original, 2 added) | each URL | confirmed | All return 200. Two redirect and were replaced with the final URL: `/radar/risk-evaluation` → `/radar/transaction-risk-prevention`; `/radar/reviews` → `/radar/transaction-reviews` |

**Counts:** 85 checked: 69 confirmed, 7 corrected (9, 18, 20, 42, 44, 50, 76), 8 hedged (3, 31, 37, 41, 56, 65, 74, 79), 1 unsupported and reworded (36), 0 unreachable.

## Could not verify, and what I did

- **Absolute negatives.** "Not public" and "not documented" statements (rows 24, 27, 45, 65, 76) are confirmed only against the provider documentation indexes and the pages listed. They are worded on the page as what the author found, with the date.
- **Stripe's holdout** (row 37). The documentation supports only that the reported score is modified for a small subset to measure the models. Kept as a labeled inference.
- **Whether the rollback reverted Shield's size** (row 42). The post says the team rolled back "to a model trained with the earlier sampling strategy" and does not state the production model's size. The page now says exactly that.
- **Stripe's reserve policy** (row 76). I searched Stripe's documentation only, not its support site or legal terms.

## Sources section changes

- Titles updated to what the pages now display: "Transaction risk prevention" (was "Risk evaluation"), "Fraud prevention rules" (was "Rules"), "Review payments" (was "Reviews"), "Protect yourself from card testing" (was "Card testing"), "Common types of online fraud" (was "Types of fraud"), "Risk and liability management with Connect", "Data collection to detect fraud".
- Added, because the text now relies on them: "Risk setting and risk controls" (S-SET) and "Advanced fraud detection" (S-AFD).
- Every entry is used in the text; no entry removed. No source is older than three years except S-2023, which is flagged at each use and in its entry.

## Rulings and format

- Ruling 22: no external URL in the running text (only the failure-patterns callout link).
- Rulings 14 and 23: Mila's pass is a wallet payment; no page text calls the Stripe studios Express accounts.
- Terms defined that were used undefined: card network, scheme, capture, settled, card fingerprint, early fraud warning, Stripe Connect and connected account, Adyen's premium features, Radar's four plans.
- `timetoread` changed from 26 to 28 (structure word count 6,345 ÷ 230 = 27.6). The page was 5,885 words before the pass; it is under the 6,500 limit by the structure count.
- No unit added, dropped, merged or reordered. Evidence text in `spec.json` was aligned with the corrections in six places and a changelog entry added.

## Larkfield consistency

Checked against the ledger: 8–9 August 2026 is a Saturday and Sunday; 61,000 = 38,400 + 19,700 + 2,900; €4,100 = €2,900 + €1,200; 31 hours; Tuesday 9 March 2027 19:42; membership set-up 12 January 2027; €15.00 dispute fee; 392 ÷ 407 = 96%; 16 ÷ 31 = 52%; 40 ÷ 215 = 19%; Jonas's rule at 0% allocation and the sixty-day verdict; the three limits on the widget; destination charges, so the platform's Radar rules apply (S-CR). No contradictions.

## Ledger conflicts

None.

## For other pages

- **journal-spec.json (part 5, this chapter's role claim)** says Stripe and Adyen "document the same decision points, holdouts and kinds of control". For Stripe the holdout is an inference from one sentence (row 37). The post spec copies the claim and I left it unchanged.
- **Any page that cites Radar's risk score or default block** (chapter 9 glosses "risk block"; chapter 25 uses Radar's request-3-D-Secure rules): Stripe marks the `:risk_level: = 'highest'` block rule as deprecated in favor of risk settings with separate fraudulent-dispute, early-fraud-warning and fraudulent-payment scores (S-SET, S-RULES, accessed November 2026).
- **Any page that cites `docs.stripe.com/radar/risk-evaluation` or `/radar/reviews`**: both now redirect (see row 85).
- **Chapter 35 or 33, if they say Adyen's deposit calculation is not public**: A-DEP documents its components (row 76).
