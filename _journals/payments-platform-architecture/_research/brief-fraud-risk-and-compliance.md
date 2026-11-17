# Research brief: Fraud, risk and compliance systems

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 24 (fraud and risk systems) and 26 (KYC, AML and regulation), and parts of 16, 34 and 45. The brief is anchored on Stripe and Adyen. Other companies and bodies (Visa, the ECB and EBA, UK Finance, FinCEN, the FCA) appear where they are the primary source for a fact or where a contrast clarifies a design choice.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated documentation and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (the kind is named), not from a primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the researcher's inference, including every statement about how Stripe, Adyen or any other company works internally beyond what it has published.

**Evidence age matters.** Stripe and Adyen documentation pages are living documents with no reliable publication date (Adyen's markdown pages carry a `last_modified` field that is plainly not the last edit date: the risk-management landing page says 2019 while describing Adyen Uplift, launched in 2025). Product names in this area changed during 2025 and 2026 on both sides. Sources published before November 2023 are flagged **(evidence age: N years)**.

**Research limitation.** What could not be fetched or verified in this session:

- **Stripe pages on stripe.com were served in Dutch** (geo-redirect to `/nl/`) for the restricted-businesses list and the machine-learning primer. The facts below were read in Dutch and are paraphrased in English; they are not exact English quotes and must not be printed in quotation marks. docs.stripe.com and stripe.dev pages were served in English and are quoted exactly.
- **Stripe's older Radar posts** (the 2016 launch post, the 2018 "Radar 2.0" post, and any post describing nightly or daily retraining) were not found on the current blog index and were not fetched. Statements about Radar before 2022 rest on the 2023 retrospective.
- **Stripe support pages** (`support.stripe.com`) render client-side; three were read through a summarising fetch tool, so their quotes are short and should be re-checked before print.
- **The FATF Recommendations** page and PDF returned HTTP 403. The FATF items are tagged ASSUMPTION/JUDGEMENT or sourced from EU law that cites FATF.
- **The Massachusetts Attorney General press release** about Stripe (the only official enforcement item found) returned HTTP 403; it is tagged WIDELY REPORTED from a search-result summary.
- **The Adyen 2025 Annual Report PDF** was not located; only the shareholder letter on the investor page and the press release were read. Adyen's risk-governance and regulatory-capital disclosures are therefore not covered.
- **DORA statements by Stripe and Adyen**: the URLs tried (`stripe.com/legal/dora`, a Stripe support article, `adyen.com/knowledge-hub/dora`) returned 404. Nothing is claimed about either company's DORA position.
- **The US Congressional Review Act repeal** of the CFPB's digital-payment-apps rule could not be confirmed on congress.gov (403) or the Federal Register; the CFPB's own rule page still lists the rule as final.
- **The European Payments Council's Verification of Payee scheme page** returned 403; Verification of Payee is sourced from the regulation itself.
- **PayPal and Block risk-engineering posts** were not fetched (search budget was spent on Stripe, Adyen and regulators). No contrast with them is claimed.
- **Nilson Report** figures were not accessed (paywalled) and are not used.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: Radar plan names and feature gating, preview features, Visa VAMP thresholds, PSD3/PSR adoption, AMLA milestones, FinCEN relief, UK safeguarding rules, MTMA state counts.

---

## PART 1: Fraud and risk systems (chapter 24; parts of chapters 16 and 45)

### 1.1 Fraud types, and who carries the loss

Stripe's documentation gives the working definition and a taxonomy a newcomer can use:

- "A payment is considered fraudulent when the cardholder didn't authorize it. Most fraudulent payments are made using stolen cards or card numbers." [VERIFIED: https://docs.stripe.com/disputes/prevention/fraud-types.md, n.d., accessed 2026-11]
- **Stolen-card fraud**: after the cardholder disputes, "the business suffers a loss equal to the amount of the payment, and the cost of any goods or services already provided. The business is also subject to a dispute fee." [VERIFIED: same page]
- **Card testing**: "the practice of testing a card (or multiple cards) on one site to see if it's still valid before using it on another site to make a fraudulent payment." Other names: "carding", "account testing", "enumeration", "card checking" [VERIFIED: same page; https://docs.stripe.com/disputes/prevention/card-testing.md, n.d., accessed 2026-11].
- **Friendly fraud**: "also known as 'first-party misuse' or 'first-party fraud'—occurs when a legitimate cardholder makes a purchase, but then disputes it at a later date", accidentally or deliberately [VERIFIED: fraud-types page].
- **Marketplace (merchant) fraud**: "a fraudulent business takes payments without providing the services or goods to customers"; "if the funds can't be recovered from the seller, responsibility for the disputed amount and fee is ultimately on the platform" [VERIFIED: same page].
- **Overpayment and alternative-refund scams**: variants of stolen-card fraud in which the criminal extracts money through a second channel; Stripe's rule: "Never refund payments using a different method than the one originally used." [VERIFIED: same page]
- **Account takeover** is not defined on Stripe's fraud-types page. Radar's current overview lists separate "customer abuse" products (multi-accounting, account sharing, free-trial abuse, bot abuse, account farming) rather than an account-takeover product [VERIFIED: https://docs.stripe.com/radar.md, n.d., accessed 2026-11]. Account takeover is described here from general industry knowledge: a criminal logs in as a real customer and spends with the stored card [ASSUMPTION/JUDGEMENT].

Stripe states the liability position plainly: "you're ultimately responsible for payments you choose to accept, including those that are later disputed or found to be fraudulent." [VERIFIED: https://docs.stripe.com/radar/risk-evaluation.md, n.d., accessed 2026-11]

Adyen's engineering blog splits card testing into two forms: "verification, where bots iterate through lists of stolen credentials using low-amount transactions to identify active cards; and enumeration, where scripts systematically guess missing fields, such as CVVs or expiry dates, within specific BIN ranges." [VERIFIED: https://www.adyen.com/knowledge-hub/catching-card-testing-at-scale, published 2026-10-04]

**Stripe vs Adyen.** Stripe publishes a merchant-facing fraud taxonomy. Adyen's documentation has no equivalent taxonomy page (searched the `docs.adyen.com/llms.txt` index for "fraud types", "card testing" and "account takeover": no dedicated page); its fraud vocabulary appears inside the Protect product pages and one engineering post.

**For readers new to payments.**
- *Card-not-present (CNP)*: a card payment where the card is not physically read, such as an online purchase; called "remote" in EU statistics and "remote purchase" in UK statistics.
- *Chargeback (dispute)*: the cardholder's bank reverses a payment and takes the money back from the merchant.
- *Early fraud warning*: a notice from a card issuer that a cardholder has reported fraud on a card, sent before or instead of a dispute.
- *Liability shift*: when a payment is authenticated with 3D Secure, the loss from a fraud dispute usually moves from the merchant to the issuer.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The five fraud types need different detectors because their labels arrive differently: stolen-card fraud is labelled by disputes weeks later, card testing has no transaction-level label at all (section 1.6), friendly fraud is labelled by the same dispute signal as real fraud and must be separated afterwards, and merchant fraud is a property of an account, not of a payment. A single "fraud score" hides at least three different prediction problems.

### 1.2 Published fraud statistics

**EU/EEA (EBA and ECB, 2025 report, data to 2024).**
- Total reported payment fraud across the EEA "amounted to EUR 4.2 billion in the year 2024", "a year-on-year increase of EUR 602 million or 17% from 2023 to 2024" [VERIFIED: https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf, published 2025-12 (EBA/REP/2025/40)].
- Fraudulent credit transfers: EUR 2.5 billion, fraud rate 0.001%. Fraudulent card transactions (cards issued in the EU/EEA): EUR 1.3 billion, fraud rate 0.033% [VERIFIED: same report].
- "Remote card payment fraud in value and volume terms accounted for around 83% of all card fraud in 2024, while remotely initiated payments' share of the total value and volume of overall card transactions were only around 28% and 18%, respectively." [VERIFIED: same report]
- "the annual fraud rate in 2024 was 13 times higher in value, and 22 times higher, in volume, for remote (0.091% in values; 0.068% in volumes) when compared to non-remote card payments (0.007% in values; 0.003% in volumes)." [VERIFIED: same report]
- Theft of card details accounted for "more than 56% of the total value" of remote card fraud in 2024 [VERIFIED: same report].
- "In 2024, around 29% of remote card payments without SCA were exempted under TRA" (transaction risk analysis) [VERIFIED: same report].

**United Kingdom (UK Finance Annual Fraud Report 2026, data for 2025).**
- "criminals stole £1.28 billion through payment fraud in 2025, an increase of four per cent" [VERIFIED: https://www.ukfinance.org.uk/policy-and-guidance/reports/annual-fraud-report-2026, published 2026-06].
- Unauthorised fraud losses £703.4 million (down 5%); authorised push payment losses £576.4 million (up 19%); 3.81 million confirmed unauthorised cases (up 11%) [VERIFIED: https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf, published 2026-06].
- Remote purchase (CNP) fraud: £423.5 million, up 3% in value with a 13% rise in cases [VERIFIED: same PDF].
- The industry "prevented a further £1.68 billion of unauthorised fraud – equivalent to 70p in every £1 of attempted fraud being stopped" [VERIFIED: same PDF].

**Provider and network figures (self-reported).**
- Stripe: fraud is "on the order of 1 out of every 1,000 payments" [VERIFIED: https://stripe.dev/blog/how-we-built-it-stripe-radar, published 2023-03-29] **(evidence age: 3.6 years)**; not restated in the 2026 post.
- Visa: enumeration attacks cause "$1.1B annually in fraud losses" and "Thirty three percent of enumerated accounts experienced fraud within five days" (Visa's own VAAI data, fiscal 2023) [VERIFIED: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20661.html, published 2024-05-07].

**Stripe vs Adyen.** Neither company publishes an aggregate fraud rate for its own volume in a form comparable to the official statistics. Stripe publishes selected performance claims (section 1.4); Adyen publishes one (section 1.6).

**For readers new to payments.**
- *Fraud rate*: fraudulent value (or count) divided by total value (or count) of payments; the EU figure for cards is about 3 euros in every 10,000.
- *Authorised push payment (APP) fraud*: the victim is tricked into sending a bank transfer themselves; it is not card fraud and has no chargeback.
- *SCA and TRA*: strong customer authentication is the EU's two-factor rule for electronic payments; transaction risk analysis is an exemption that lets a low-risk payment skip it.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Card fraud is rare (hundredths of a percent) and concentrated in remote payments, so a fraud model is a rare-event classifier whose errors on legitimate payments outnumber its catches unless thresholds are set with care. The EU and UK numbers are measured by issuers and banks; a provider's own dispute data sees only the part of fraud that becomes a dispute or an early fraud warning.

### 1.3 Where risk scoring sits in the authorization path

Both companies document a decision that happens **before** the payment is sent to the card network, and both document a second decision point **after** the issuer answers.

- Stripe: a payment Radar blocks is never sent to the issuer. The Charge outcome for a blocked high-risk payment shows `"network_status": "not_sent_to_network"`, `"type": "blocked"`, `"reason": "highest_risk_level"` [VERIFIED: https://docs.stripe.com/radar/risk-evaluation.md, n.d., accessed 2026-11].
- Stripe: Radar "evaluates risk and runs rules for three Stripe API objects: Charges, PaymentIntents and SetupIntents", with four actions: request 3DS, allow, block, review [VERIFIED: same page]. "Request 3DS rules … are evaluated before review, block, and allow rules." [VERIFIED: https://docs.stripe.com/radar/rules.md, n.d., accessed 2026-11]
- Stripe: review is post-authorization: "Payments placed into review are typically already successfully processed, unless you capture authorized payments later." [VERIFIED: https://docs.stripe.com/radar/reviews.md, n.d., accessed 2026-11]
- Stripe: built-in CVC and postal-code rules "block certain payments that the card issuer approved", which means they run on the issuer's response [VERIFIED: rules page].
- Adyen: "Risk rules can trigger before or after authorization: Pre-authorization: the risk rule conditions are assessed before the payment is authorized. This saves issuer and scheme fees compared to blocking after authorization. Post-authorization: … the risk evaluation can take extra signals into account that are only available after authorization. For example authentication results, CVC/CVV codes, or AVS responses." [VERIFIED: https://docs.adyen.com/risk-management/configure-your-risk-profile.md, n.d., accessed 2026-11]
- Adyen: "post-authorization rules have priority over pre-authorization rules … The only exception is when a transaction is blocked before it is authorized." [VERIFIED: same page]
- Adyen's engineering post confirms the order for the bot-attack model: the risk engine fetches feature values "to make real-time block/allow decisions before sending transactions to the issuer" [VERIFIED: https://www.adyen.com/knowledge-hub/catching-card-testing-at-scale, published 2026-10-04].

**Latency budgets, as published.**
- Stripe: Radar "makes this decision, accurately, in less than 100 milliseconds" [VERIFIED: https://stripe.dev/blog/how-we-built-it-stripe-radar, published 2023-03-29] **(evidence age: 3.6 years)**. The 2026 post says the model "scores payments in milliseconds" and that tripling the model's size did not increase "serving latency in our load tests or production scoring" [VERIFIED: https://stripe.dev/blog/scaling-radar-fighting-fraud-with-agent-assisted-machine-learning, published 2026-10-19]. The 100 ms figure is not restated.
- Stripe: feature retrieval is part of that budget: "the time required to retrieve features directly impacts the overall payment API latency" [VERIFIED: https://stripe.dev/blog/shepherd-how-stripe-adapted-chronon-to-scale-ml-feature-development, published 2024-04-15].
- Visa: the VAAI Score "Provides a real-time risk score in 20 milliseconds" [VERIFIED: Visa press release, published 2024-05-07].
- Adyen: **no latency figure published** for Protect (searched the risk-management docs and the 2026 engineering post).

| Decision point | Stripe (Radar) | Adyen (Protect) |
| --- | --- | --- |
| Before authorization | Block (not sent to network), request 3DS, allow | Pre-authorization rules: allow, block, review, "check for 3DS" |
| After authorization | CVC/postal-code rules, review queue | Post-authorization rules (AVS, CVC, liability shift), case management |
| Manual review window | Review of processed payments; refund or approve | "up to seven calendar days to reject a transaction" when capture delay for case management is enabled; otherwise auto-accepted [VERIFIED: https://docs.adyen.com/risk-management/case-management.md, n.d., accessed 2026-11] |

**For readers new to payments.**
- *Authorization*: the real-time request to the cardholder's bank to approve a payment.
- *Pre-authorization block*: the provider refuses the payment itself and the bank never sees it.
- *AVS and CVC checks*: the issuer's comparison of the billing address and the three-digit code with its records, returned with the authorization answer.
- *Capture*: the later step that actually takes the authorized money; holding capture gives time for manual review.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] The risk decision is a synchronous dependency of the payment API, so it needs a hard time limit and a defined behaviour when it fails. Stripe documents its failure mode: "an error might cause risk evaluation to fail. If this happens, Stripe reports the payment as having unknown risk", and the example outcome shows the payment authorized [VERIFIED: risk-evaluation page]: the documented behaviour is to fail open. Adyen documents no equivalent. Two decision points also mean two different feature sets: issuer responses can only be used after the money has been reserved, at which point a "block" becomes a cancellation that has already cost scheme fees.

### 1.4 Stripe Radar's machine learning, as published (dated)

**Sources and dates.** Three engineering posts and one guide describe Radar's models: "How we built it: Stripe Radar" (Ryan Drapeau, 29 March 2023), "Shepherd: How Stripe adapted Chronon to scale ML feature development" (Ben Mears, 15 April 2024), "Scaling Radar: Fighting fraud with agent-assisted machine learning" (Ryan Drapeau and Sai Samant, 19 October 2026), and the undated "primer on machine learning for fraud protection". A product post of 15 May 2025 announced the payments foundation model. A fifth post, "Fine-tuning LLMs for risk assessment" (9 October 2026), concerns merchant risk (section 1.8).

**Model architecture over time.**
- "We started with relatively simple ML models (e.g., logistic regression) and over time have advanced to more complex ones (e.g., deep neural networks)" [VERIFIED: stripe.dev/blog/how-we-built-it-stripe-radar, published 2023-03-29] **(evidence age: 3.6 years; confirmed and extended by the 2026 post)**.
- "Our most recent architecture evolution occurred in mid-2022 when we migrated from an ensemble 'Wide & Deep model,' composed of an XGBoost model and a deep neural network (DNN), to a pure DNN-only model." [VERIFIED: same post]
- Simply removing XGBoost "would have caused a 1.5% drop in recall"; the replacement is "a multi-branch DNN-only architecture inspired by ResNeXt" [VERIFIED: same post].
- "By removing the XGBoost component of the architecture, we reduced the time to train our model by over 85% (to less than two hours)." [VERIFIED: same post]
- The 2026 post names the transaction-fraud model: "Shield is one of those models and focuses on transaction fraud", and confirms "Shield's ResNeXt architecture contains parallel branches" [VERIFIED: stripe.dev/blog/scaling-radar-…, published 2026-10-19].
- Model size: "The model grew to roughly 30 million parameters, three times its previous size" [VERIFIED: same 2026 post].

**Scale and accuracy claims.**
- Radar "assesses more than 1,000 characteristics of a potential transaction" and "Out of the billions of legitimate payments made on Stripe, Radar incorrectly blocks just 0.1%." [VERIFIED: 2023 post] **(evidence age: 3.6 years)**. The current docs say the model "uses hundreds of risk factors about each payment" [VERIFIED: https://docs.stripe.com/radar/risk-evaluation.md, n.d., accessed 2026-11]. The two numbers ("more than 1,000 characteristics", "hundreds of risk factors") are both Stripe's and are not reconciled anywhere public.
- Training data: "roughly 800 million transactions in its training set"; the experiment without downsampling "expanded the training set from roughly 800 million to 11 billion transactions" over "a nine-month window" [VERIFIED: 2026 post]. In 2023 Stripe had reported "a 10x increase in training transaction data" with "a 100x version" in progress [VERIFIED: 2023 post].
- Training time at 11 billion examples: "shortening each epoch from 24 hours to 4.8 hours (an 80% reduction)", with peak training memory cut "from 1.3 TB to 500 GB" [VERIFIED: 2026 post].
- Result of the 2026 work: "the new configuration improved recall by over 8%, translating to an estimated tens of millions of dollars a year in additional fraud prevention for Stripe's merchants." [VERIFIED: 2026 post]
- Product-level claims (marketing, May 2025): Radar "reduce[d] dispute rates for Radar users by 17% last year, even as industry-wide ecommerce fraud increased 15%"; adaptive 3DS "Backed by a new multihead model and decisioning layer, early users have seen an over 30% reduction in fraud on eligible transactions" [VERIFIED: https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite, published 2025-05-15].

**The feedback loop and its delay (the most useful published passage for chapter 24).**
- "For a payment made with a stolen card, it could take weeks for the cardholder to notice and report it to their bank. When Stripe receives the fraudulent dispute, we gain a fraud label for a payment we scored weeks earlier." [VERIFIED: 2026 post]
- The post's chart caption gives the arrival curve of fraud labels: the cumulative share of fraudulent disputes reported reaches "41% by day 14, 66% by day 30, and 86% by day 60 after the payment" [VERIFIED: 2026 post, figure alt text].
- A larger model first "looked better in offline tests and in early results of a production experiment. But, as more fraud reports arrived, its measured performance fell below the earlier model's, and we had to roll back" [VERIFIED: 2026 post].
- Cause: removing downsampling "added more legitimate examples, as intended, but also more fraudulent examples labeled as legitimate, about 20 times more." [VERIFIED: 2026 post]
- Merchant feedback is a second label source: refunding with `reason: 'fraudulent'` "adds the email address and card fingerprint associated with the payment to the default … block lists", and "Our AI models respond to feedback you share with us" [VERIFIED: risk-evaluation page].
- Stripe deliberately lets some risky traffic through to measure itself: "For a small subset of payments, Stripe modifies the reported risk score so we can measure the performance of our models and obtain data for subsequent model development." [VERIFIED: risk-evaluation page]

**Retraining cadence.**
- "For each week of payment data, our training pipeline kept every known fraudulent payment and randomly selected a subset of the remaining payments. This downsampling lets regular retraining finish more quickly." [VERIFIED: 2026 post] The post says "regular retraining" and does not give an interval.
- Stripe's primer says (paraphrased from the Dutch-language page served) that tooling lets Stripe release models three times faster than before, and that retraining last month's model on more recent data with the same features and architecture can improve recall by up to half a percentage point per month [VERIFIED: https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection, n.d., accessed 2026-11; read in Dutch].
- A "daily" or "nightly" retraining claim circulates in secondary sources; **it was not found in any Stripe page fetched in this session** and should not be printed as Stripe's statement.

**Features and feature infrastructure.**
- Example of a feature: "the total number of charges processed by a business on Stripe over the last seven days" [VERIFIED: stripe.dev/blog/shepherd-…, published 2024-04-15].
- Shepherd is Stripe's feature platform, built on Airbnb's Chronon: "In 2022 we began a partnership with Airbnb to adapt and implement its platform, Chronon, as the foundation for Shepherd". The first Shepherd-built fraud model has "over 200 features" and blocks "tens of millions of dollars of additional fraud per year" [VERIFIED: same post].
- The two competing requirements: latency ("the time required to retrieve features during model inference") and feature freshness ("the time required to update the value of features") [VERIFIED: same post].
- Storage design: "we split it into two implementations: a lower-cost store optimized for bulk uploads that is write-once and read-many, and a higher-cost distributed memcache-based store that is optimized for write-many and read-many." [VERIFIED: same post]
- Shepherd "computes historical training features and serves their online equivalents from the same definitions" [VERIFIED: 2026 post].
- Feature discovery is partly manual: "Every week, the Radar team also meets to discuss new fraud trends that emerge from research into activity on the dark web." [VERIFIED: 2023 post] **(evidence age: 3.6 years)**

**Explanations.** "In 2020 we built our risk insights feature, which lets users see which features of a transaction contributed to a transaction being declined." Stripe calls explanation "another tradeoff we came to accept when deciding to use DNNs" [VERIFIED: 2023 post].

**Agents in the experiment loop (2026).** "We built Agentic MLE … a set of tools and instructions that lets AI agents operate in Stripe's existing ML infrastructure, carrying an experiment from an idea to a result"; "Engineers review hypotheses and results and decide what to deploy." In one fraud attack, "Humans helped prioritize 38 ideas, then agents implemented the changes, trained models, debugged failed runs, and evaluated the results." [VERIFIED: 2026 post]

**The payments foundation model (May 2025).**
- "Historically, we've built specialized AI models for individual tasks such as fraud detection, authorization, and dispute management. But now, we're going a step further … with our Payments Foundation Model—an industry first. It's trained on tens of billions of transactions, and it distills almost everything about each payment on Stripe down to a single, versatile embedding." [VERIFIED: stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite, published 2025-05-15]
- Card-testing claim: "While attacks are up industry-wide, they are down 80% on Stripe." For "novel attack types that fraudulent actors sprinkle across the volumes of the world's biggest companies": "By classifying sequences of embeddings, our detection rate for attacks on large users significantly increased—from 59% to 97%—overnight." [VERIFIED: same post]
- What is **not** published: the model's architecture, size, training objective, how embeddings are served in the authorization path, the baseline period for "down 80%", and the definition of "detection rate". The post is unsigned product marketing, not an engineering post. ⚠ The 2026 engineering post on Shield does not mention the foundation model, so the relation between the two is not public [ASSUMPTION/JUDGEMENT: the absence is observed; no inference about internal design is offered].

**Stripe vs Adyen (machine learning).**

| Topic | Stripe | Adyen |
| --- | --- | --- |
| Model family | Logistic regression → XGBoost + DNN ensemble → DNN-only (mid-2022), ResNeXt-inspired, ~30M parameters (2026) | Not published. Docs say only "machine learning" and "risk classification" |
| Training set size | ~800M sampled transactions; 11B in experiment (2026) | "billions of transactions" used to build training sets for the bot-attack model (2026 post) |
| Features | "hundreds of risk factors" (docs); "more than 1,000 characteristics" (2023 post); Shepherd/Chronon platform | "hundreds of features per transaction" for the bot-attack model; custom feature DSL compiled to Spark and Flink |
| Label delay | Quantified: 41% / 66% / 86% of fraud disputes by day 14 / 30 / 60 | Qualitative only: card testing "offers no explicit transaction-level signal" |
| Latency | "less than 100 milliseconds" (2023) | Nothing published |
| Retraining cadence | "regular retraining"; no interval | Nothing published |
| Foundation model | Announced May 2025; no engineering detail | Nothing equivalent announced under that name; marketing refers to "AI Risk Score" and "Dynamic identification" |

**For readers new to payments.**
- *Risk score*: a number the provider attaches to a payment that estimates how likely it is to be fraud.
- *Recall and false positive*: recall is the share of fraud that is caught; a false positive is a good payment that was blocked.
- *Label*: the after-the-fact fact ("this payment was fraud") a model learns from; for card fraud it usually arrives as a dispute.
- *Feature*: one input to the model, such as how many cards an IP address has used today.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- The label curve (86% at day 60) sets a floor on how fresh a trustworthy evaluation can be: any model comparison judged on the last two weeks is judged on fewer than half of the eventual labels. This is the strongest published argument for holding a new model in a long shadow or partial rollout.
- Blocking a payment destroys its label. Both companies publish their answer: Stripe alters the score for "a small subset of payments"; Adyen runs "control traffic" (section 1.5). A fraud system without such a holdout cannot measure its own false positives.
- Training/serving consistency is a named problem at both companies (Shepherd at Stripe; the feature DSL at Adyen). It is the design reason a feature store exists.

### 1.5 Scores, rules, lists and reviews: what customers can configure

**Stripe Radar.**
- Score and levels: "each payment also includes a risk score that ranges from 0–99 … By default, a score of 65 or above indicates elevated risk, while a score of 75 or above indicates high risk." High-risk payments "are blocked by default"; elevated-risk payments are allowed by default and can go to review [VERIFIED: https://docs.stripe.com/radar/risk-evaluation.md, n.d., accessed 2026-11].
- Rule language: `{attribute} {operator} {value}`, with attributes prefixed by `:` and merchant metadata in double colons (`::product_sku::`). Example from the docs: `Request 3D Secure if :risk_level: != 'normal' and :amount_in_usd: > 25` [VERIFIED: https://docs.stripe.com/radar/rules.md, n.d., accessed 2026-11].
- Limits and precedence: "You can create a maximum of 200 transaction rules and 100 account rules." "Implement any allow rules minimally, because they override the Stripe default rules, along with any other custom rules that match the same criteria." [VERIFIED: rules page]
- Safe rollout: rules are backtested on recent payments before enabling, and "traffic allocation" applies a rule to a percentage of matching payments: "Radar assigns all attempts for the same transaction to the same allocation bucket, so each retry receives the same outcome as the original attempt." [VERIFIED: rules page]
- Lists: default allow and block lists for card BIN, card country, card fingerprint, client IP, customer ID, email and email domain; custom lists on higher plans [VERIFIED: https://docs.stripe.com/radar/lists.md, n.d., accessed 2026-11].
- Risk settings: three presets ("Maximize protection", "Balance risk and revenue", "Maximize revenue") that set thresholds on separate controls for fraudulent disputes, early fraud warnings, adaptive 3DS and "dynamic risk thresholds", which "automatically blocks additional elevated and high-risk payments when your account is under fraud pressure" [VERIFIED: https://docs.stripe.com/radar/risk-settings.md, n.d., accessed 2026-11]. The risk controls "don't use these AI models. They use more specialized models that can balance the tradeoffs between authorization and fraud." [VERIFIED: risk-evaluation page]
- Subscriptions: "the Radar fraud models only score the initial payment of a recurring Stripe Billing subscription, but evaluate rules for all payments." [VERIFIED: risk-evaluation page]
- ⚠ **Plans were renamed.** The docs fetched on 17 November 2026 list four plans: Radar Lite, Radar Standard, Radar Plus and Radar Pro. Risk scores, custom rules, lists, manual reviews and adaptive 3DS are in Plus and Pro; dynamic risk thresholds and customer-abuse signals are Pro only [VERIFIED: https://docs.stripe.com/radar/how-radar-works.md, n.d., accessed 2026-11]. The name "Radar for Fraud Teams" survives only in one guide URL on the pages fetched; chapter writers should use the current plan names and say they changed.
- Radar outside Stripe: "Radar can evaluate payments from any processor in real time and return risk signals" through a Payment Evaluation API (access by request) [VERIFIED: https://docs.stripe.com/radar/multiprocessor.md, n.d., accessed 2026-11].
- With Connect: for direct charges "Stripe applies only the collecting account's Radar configuration and rules"; for destination charges "only the platform account's Radar configuration and rules" [VERIFIED: https://docs.stripe.com/connect/radar.md, n.d., accessed 2026-11].

**Adyen Protect.**
- "Each payment goes through a risk evaluation. The risk evaluation reaches a decision that results in an action to block, allow, or review the transaction. This outcome is based on the risk settings on your account, the risk profile, and the risk rules on that profile." [VERIFIED: https://docs.adyen.com/risk-management.md, n.d., accessed 2026-11]
- Two tiers: basic (bot-attack blocking, Adyen risk lists, Adyen post-authorization rules, Dynamic 3D Secure) and premium (adds "Machine learning powered fraud detection using global transaction data", custom rules with backtesting, experiments and case management) [VERIFIED: same page]. "Protect is part of Adyen Uplift." [VERIFIED: same page]
- Machine-learning rules: "Machine learning: bot attack risk" (basic and premium, no configuration) and "Machine learning: fraud risk" (premium). The fraud-risk rule assigns "a risk level ranging from **Very Low** to **Very High**"; "By default, the block threshold for this rule is set to high risk and above." The risk level "indicates the likelihood that a transaction will result in a fraudulent dispute." [VERIFIED: https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules.md, n.d., accessed 2026-11]
- Adyen's guidance on thresholds is explicitly economic: thin-margin retailers should set "a **Low** or **Medium** threshold" because "the cost of a fraud case … largely outweighs the cost of a false decline", while sellers of digital goods should set "**High** or **Very High**" because "the cost of a false decline (potential loss of lifetime value) mostly outweighs the cost of a fraud case" [VERIFIED: same page].
- Precedence: "**Allow** rules have the highest priority within a risk profile. This means that when an **Allow** rule is triggered, it will override any **Block** or **Review** rules." [VERIFIED: https://docs.adyen.com/risk-management/configure-your-risk-profile.md, n.d., accessed 2026-11]
- Scores in the API: "For any field that shows a fraud score, for example `accountScore` or `totalFraudScore`, the possible values are **-100**, **0**, **100** or **200**." [VERIFIED: https://docs.adyen.com/risk-management/handle-risk-rule-notifications.md, n.d., accessed 2026-11] The score is therefore a coded decision, not a continuous probability. The older RevenueProtect model, in which each triggered rule added points and a total of 100 blocked the payment, is not described on the current pages fetched; the four fixed values look like its residue [ASSUMPTION/JUDGEMENT].
- Risk lists include an "Adyen global referral list" of "card and bank account numbers that are reported by the schemes as stolen or fraudulent" [VERIFIED: https://docs.adyen.com/risk-management/configure-your-risk-profile/risk-lists.md, n.d., accessed 2026-11].
- Control traffic: "A very small percentage of all transactions is randomly selected to be part of control traffic. Control traffic transactions are settled regardless of their risk evaluation." Excluded: "Transactions with an amount of EUR 2000 or higher", repeatedly refused transactions, and those on block or trust lists [VERIFIED: https://docs.adyen.com/risk-management/control-traffic.md, n.d., accessed 2026-11].
- Shopper DNA: "a shopper network and identity analysis tool" that "links transactions in clusters to identify a profile of a shopper even as they change devices, networks, and identities"; "Transactions link to a shopper profile only when they share identical identifiers." The page says "We are in the process of rolling out changes to shopper DNA." [VERIFIED: https://docs.adyen.com/risk-management/shopper-dna.md, n.d., accessed 2026-11] ⚠
- "Dynamic identification" is Adyen's newer umbrella term: the 2025 shareholder letter says it "draws on trillions of interactions across online and in-store commerce to inform decisions in real time" [VERIFIED: https://investors.adyen.com/financials/2025, published 2026-03-05]. It has no page in the developer documentation (the `llms.txt` index has zero matches), so how it relates to shopper DNA is not public.
- Explanations: the risk results page shows "the most influential signals", for example "The number of days since this email address first appeared in Adyen global transaction data." [VERIFIED: machine-learning-rules page]
- Adyen also supports A/B experiments between two risk profiles [VERIFIED: https://docs.adyen.com/llms.txt entry "Run A/B test experiments", n.d., accessed 2026-11].

**Stripe vs Adyen (configuration).**

| Topic | Stripe Radar | Adyen Protect |
| --- | --- | --- |
| Exposed score | 0–99, thresholds 65 and 75 (Plus/Pro plans) | Five levels, Very Low to Very High; API scores are -100/0/100/200 |
| Default block | `highest` risk level blocked | "high risk and above" blocked (premium) |
| Rule actions | Request 3DS, allow, block, review | Allow, block, review, check for 3DS; each rule pre- or post-authorization |
| Rule limit | 200 transaction rules, 100 account rules | Not stated |
| Gradual rollout | Per-rule traffic allocation, backtesting | Backtesting; A/B experiments between profiles |
| Holdout | Score altered for "a small subset of payments" | "Control traffic", settled regardless of risk |
| Scope unit | Account (and platform vs connected account) | Risk profile assigned to merchant accounts; lists per company account by default |
| Entity graph | Not exposed as a tool; "related transactions" in risk insights | Shopper DNA force graph |

**For readers new to payments.**
- *Rule*: a merchant-written condition ("block if the card country differs from the IP country") evaluated on every payment.
- *Allow list / block list*: a set of values (emails, card fingerprints, IPs) that always pass or always fail.
- *Manual review*: a human looks at a flagged payment before the order is fulfilled or the money captured.
- *Backtest*: running a new rule against past payments to see what it would have blocked.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Both products are a model plus a rules engine plus lists plus a human queue, with an explicit precedence order in which "allow" wins. That precedence is a risk in itself: one over-broad allow rule disables the model for the traffic it matches, which is why both vendors warn about it. Rule evaluation needs the same idempotence as the payment (Stripe pins a retry to the same allocation bucket) or a customer retrying a declined payment gets a different answer.

### 1.6 Card testing and enumeration

**Stripe's guidance.**
- Why criminals prefer card setup to payments: "card validation and authorizations during card setup don't typically show up on cardholder statements." [VERIFIED: https://docs.stripe.com/disputes/prevention/card-testing.md, n.d., accessed 2026-11]
- Consequences listed: disputes, "Higher decline rates" ("A high decline rate might damage the reputation of your business with card issuers and card networks, which makes all of your transactions appear riskier"), additional authorization fees, infrastructure strain, and enrolment in card monitoring programmes [VERIFIED: same page].
- Symptoms: "A spike in failed or blocked payments", "A spike in requests with 402 errors", and "A spike in suspicious payments with low transaction amounts" [VERIFIED: same page].
- Stripe's own controls on its hosted surfaces: "rate limiters, AI models, CAPTCHA triggers, ongoing reviews"; "When we detect that you're under a card testing attack, we dynamically choose interventions to suppress the attack as much as possible." [VERIFIED: same page]
- "simple firewall rules or filters based on a single heuristic such as IP addresses are usually not sufficient"; merchant-side controls recommended: CAPTCHA, requiring login before the payment form, rate limits (for example on customers created per IP per day) [VERIFIED: same page].
- "While card testing controls are separate from Radar's protection against fraudulent disputes, they benefit from the same risk factors used by Radar." [VERIFIED: same page] Card-testing prevention is included in every Radar plan, including Lite [VERIFIED: how-radar-works page].

**Adyen's engineering description (the one substantial Adyen post on fraud ML found).**
- Author and date: Jaap Stefels, Machine Learning Scientist, 4 October 2026 [VERIFIED: https://www.adyen.com/knowledge-hub/catching-card-testing-at-scale, published 2026-10-04].
- The evasion problem: "Rotational attacks: Fraudsters continuously rotate details—such as IP addresses—to stay well below baseline velocity thresholds. Low-volume attacks: Fraudsters throttle their scripts, keeping transaction bursts too small to trigger rules at the individual merchant level." [VERIFIED: same post]
- The feature idea: move from shopper identifiers to "higher-level aggregated traffic dimensions, which we call subslices", for example "a BIN range at the merchant level", and monitor "the health and velocity of these subslices in real time" [VERIFIED: same post].
- Labels: "Unlike chargeback fraud … card testing offers no explicit transaction-level signal." Issuer decline codes such as "invalid CVC" "are not definitive proof of an attack". Adyen "proxy-label[s] traffic subslices where statistical patterns confirm fraud is happening" [VERIFIED: same post].
- Pipeline: "a custom Feature Domain-Specific Language (DSL)" compiled to "Offline Feature Generation (Apache Spark)" and "Online Streaming Inference (Apache Kafka + Apache Flink)"; "Flink writes these streaming metrics to an Apache Cassandra feature store, where the risk engine fetches the latest subslice values" [VERIFIED: same post].
- Monitoring in four layers: data source, feature computation, model prediction, decision output [VERIFIED: same post].
- Result: the system "scores millions of payments every day, increasing blocked card testing attacks by 28% on average, with zero impact on legitimate shoppers" [VERIFIED: same post]. The baseline, period and measurement method for "28%" and "zero impact" are not given.
- Product behaviour: the bot-attack rule "detects and blocks transactions that come in at an unusually fast rate with suspicious payment properties … This rule mostly prevents large scale attacks", and Adyen recommends custom velocity rules on top [VERIFIED: machine-learning-rules page].

**Visa's enumeration programme.**
- Visa Account Attack Intelligence (VAAI) Score, announced 7 May 2024, "uses generative AI components to identify and score enumeration attacks"; trained "on more than 15 billion VisaNet transactions"; produces "a two-digit risk score"; Visa claims it reduces "the false positive rate by 85% compared to other risk models" [VERIFIED: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20661.html, published 2024-05-07]. The score is offered to issuers; the press release says nothing about availability to acquirers or providers.
- Enumeration is a metric in the Visa Acquirer Monitoring Program: "VAMP Enumeration Ratio, defined as [Count of Enumerated Authorization Transactions (Approved + Declined)] ÷ [Count of Authorization Transactions (Approved+ Declined)], ≥ 2000 bps" together with "Enumerated Transactions (Approved + Declined), ≥ 300,000" in a month [VERIFIED: https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf, published 2025]. ⚠
- The same fact sheet: the VAMP ratio is "Count of [Fraud (TC40) + Disputes (TC15)] ÷ Count of Settled Transactions (TC05)"; an acquirer is "Above Standard if its VAMP ratio is ≥50bps and as Excessive if ≥70bps"; the Excessive Merchant threshold in AP, Canada, EU and US was ≥220 bps, "reduced to >=150bps … on 1 April 2026"; thresholds effective 1 June 2025, advisory period to 30 September 2025 [VERIFIED: same fact sheet]. ⚠
- Visa does not disclose which individual transactions it counts as enumerated [WIDELY REPORTED: https://www.sardine.ai/blog/new-visa-dispute-rules, 2025; vendor blog].

**Stripe vs Adyen (card testing).** Stripe publishes merchant guidance and one headline claim ("down 80% on Stripe", "59% to 97%") without method. Adyen publishes the method (subslice features, streaming pipeline, proxy labels) and one headline claim ("28%") with no merchant-facing guidance page. Stripe emphasises controls at the integration surface (CAPTCHA, rate limits on hosted checkout); Adyen emphasises a model in the risk engine. Neither says how it uses Visa's VAAI score, if at all.

**For readers new to payments.**
- *Enumeration*: guessing card numbers, expiry dates or CVCs in bulk and using a merchant's checkout to learn which guesses are valid.
- *BIN*: the first digits of a card number, identifying the issuing bank and product.
- *Velocity rule*: a rule that counts events in a time window, such as "more than three cards from one IP in an hour".
- *Monitoring programme*: a card network scheme that fines or restricts acquirers and merchants whose fraud, dispute or enumeration ratios pass a threshold.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Card testing is a traffic-shape problem, not a per-payment problem: each attempt looks ordinary and the signal is in aggregates over a slice of traffic in the last seconds or minutes. That is why it needs streaming features, and why a model trained on dispute labels does not catch it. Declined attempts still count against the merchant (Visa's ratio counts "Approved + Declined"), so the defence must stop the request before authorization; stopping it at the issuer is too late. For Larkfield's Card-Testing Weekend the published facts support this chain: attack on a card-setup or low-value endpoint → spike in declines and 402 responses → authorization fees and damaged issuer reputation → possible VAMP enumeration identification of the acquirer.

### 1.7 Signals and the network effect

- Stripe: "a credit card that is new and untrusted to one business might have years of history elsewhere on Stripe that proves it's OK or an IP address may link activity across several cards and accounts." [VERIFIED: stripe.dev/blog/scaling-radar-…, published 2026-10-19]
- Stripe: "To identify fraudulent transactions, we rely on the breadth of the Stripe network—our biggest strength." [VERIFIED: 2023 post] The primer says (paraphrased from Dutch) that most of Radar's features are aggregates computed across the Stripe network [VERIFIED: primer, read in Dutch].
- Stripe: signal quality depends on the integration. Data with "significant impact": advanced fraud detection (the browser signals collected by Stripe's JavaScript) "(Highest impact)", IP address, customer email, customer name, billing address [VERIFIED: card-testing page].
- Adyen: models "can detect recent fraud on a shopper's email address or recognize a good shopper because of a recent in-person payment on a card on the Adyen platform." [VERIFIED: https://docs.adyen.com/risk-management.md, n.d., accessed 2026-11] This is a documented cross-channel signal (in-store history informing online risk).
- Adyen: "Adyen collects data about how shoppers interact with and use the payment form. Protect then uses this data to detect fraudulent payment activity", collected automatically by Drop-in, Components and Hosted Checkout; the merchant must handle consent under privacy law [VERIFIED: https://docs.adyen.com/risk-management/fraud-data-collection.md, n.d., accessed 2026-11].
- Limits of the network: Stripe's Shield "learned from only a fraction of the available history" and the stated aim was to catch "fraud patterns specific to particular businesses, products, and countries without flagging legitimate payments that happened to look unusual" [VERIFIED: 2026 post]. A network model can be wrong for a merchant whose normal traffic is unusual.

**Stripe vs Adyen.** Both claim a network effect from seeing many merchants. Adyen's documented distinctive signal is unified online and in-person history on one platform; Stripe's is the breadth of online merchants and browser signals from Stripe.js. Neither publishes how much of its accuracy comes from cross-merchant data. [ASSUMPTION/JUDGEMENT for the comparison]

**For readers new to payments.**
- *Card fingerprint*: a provider's stable identifier for a card number, so the same card can be recognised without storing the number in the merchant's system.
- *Device and browser signals*: technical facts about the shopper's device collected by the provider's checkout script.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Cross-merchant features mean the fraud system is a shared, multi-tenant service whose inputs are personal data from many controllers; data-protection design (purpose limitation, consent for behavioural collection) is part of the architecture, as Adyen's page makes explicit. A merchant integrating by raw API loses the client-side signals and gets a weaker model: integration choice is a fraud control.

### 1.8 Merchant-side risk: underwriting, monitoring and reserves (chapter 24; parts of 34 and 45)

**Stripe.**
- Risk decisions listed by Stripe itself: "Is this transaction legitimate? Is the business trustworthy? Is this product set allowed by this financial partner? Has this business become suddenly popular, or is it under attack? Should we adjust a business' credit reserves?" and "we make thousands of risk decisions every single second" [VERIFIED: https://stripe.dev/blog/training-llms-for-risk-assessment, published 2026-10-09; authors Hangzhi Guo, Stathis Vafeias, Florian Hartl, Luvsandondov Lkhamsuren, Adrian Lam].
- Account-level models: "We calculate account-level risk using KYC information, transactions, geographic risk factors, and behavior patterns." [VERIFIED: https://docs.stripe.com/radar/rules.md, n.d., accessed 2026-11]
- For platforms, connected-account scores mean: "`highest` risk, or a score of 90 or higher, indicates a probability of over 90%", "`elevated` risk, or a score of 50-89, indicates a probability of 50% to 89%", where the probability is "that an account would cause losses to your platform"; "Account risk scores and levels update each time a new event occurs" [VERIFIED: https://docs.stripe.com/radar/account-fraud-prevention.md, n.d., accessed 2026-11].
- Separate signals: a "fraudulent merchant signal" built on "bank account information, business details, transaction activity, disputes, and relationships with other accounts", and a "merchant delinquency risk signal" for accounts "at risk of carrying a negative balance for more than 90 days" (early access) [VERIFIED: https://docs.stripe.com/radar/fraudulent-merchant.md and https://docs.stripe.com/radar/merchant-delinquency-risk.md, n.d., accessed 2026-11]. ⚠
- Human review and LLMs: on a selected fraud-review cohort, precision at the human reviewers' recall was 0.487 for zero-shot prompting, 0.706 for domain-guided prompting and 0.790 for human review; a fine-tuned "open-weight 4B-parameter LLM" achieved "approximately 24% higher average precision than domain-guided prompting". Stripe warns that "results on accounts selected for review should not be read as performance across all Stripe businesses." [VERIFIED: stripe.dev/blog/training-llms-for-risk-assessment, published 2026-10-09]
- Reserves on direct accounts: "A reserve is a temporary hold on a portion of a business's funds for a predetermined period of time"; "Stripe uses two different types of reserves: fixed and rolling"; "In some rare cases, a reserve may be required indefinitely" [VERIFIED: https://support.stripe.com/questions/reserves-frequently-asked-questions, n.d., accessed 2026-11; read through a summarising fetch]. No percentages or criteria are published.
- Reserves a platform sets on connected accounts: holds, fixed plans and rolling plans; "You can't reserve funds for longer than 180 days." The API is in preview (`2025-08-27.preview`) [VERIFIED: https://docs.stripe.com/connect/connected-account-reserves.md, n.d., accessed 2026-11]. ⚠
- Who carries merchant losses on a platform: "responsibility for your connected accounts' negative balances can belong to your platform or to Stripe"; if the platform is responsible and "a connected account's balance remains negative for 180 days, we transfer funds from the platform reserve to cover the negative amount." [VERIFIED: https://docs.stripe.com/connect/risk-management.md, n.d., accessed 2026-11]
- Managed Risk: "Stripe continuously monitors and mitigates credit and fraud risk", with "Screening at onboarding", "Ongoing risk monitoring and mitigation" and "Negative balance liability" taken by Stripe [VERIFIED: https://docs.stripe.com/connect/risk-management/managed-risk.md, n.d., accessed 2026-11].
- Risk interventions are exposed as requirements on the account with identifiers prefixed `interv_` and a resolution path of `challenge`, `form`, `notice`, `support` or `underwriting_case`; types include `credit_review`, `reserve_appeal`, `rejection_appeal`, `fulfillment_policy` and `url_inquiry` [VERIFIED: https://docs.stripe.com/connect/handling-api-verification.md?accounts-namespace=v1, n.d., accessed 2026-11].

**Adyen.**
- The **deposit**: "the amount withheld by Adyen to cover potential losses and liabilities due to payment processing." "Adyen calculates the deposit requirement for your account daily, based on variables such as your processing volume and the number of chargebacks and refunds." "Unlike the reserve, you cannot determine your own deposit amount." [VERIFIED: https://docs.adyen.com/account/balances/deposit.md, n.d., accessed 2026-11]
- Acceptance policy: restrictions are based on law, "Requirements of our payment partners (e.g. card networks)", "Level of assessed risk (e.g. chargebacks, fraud)" and "Reputational impact to Adyen and cost aspects associated with this" [VERIFIED: https://www.adyen.com/legal/list-restricted-prohibited, last update 2025-11-13].
- Ongoing monitoring is acknowledged but not described: "Verification deadlines may be adjusted based on ongoing account monitoring and subsequent verification checks." [VERIFIED: https://docs.adyen.com/marketplaces/verification-overview.md, n.d., accessed 2026-11]
- Card-issuing capabilities "can also have different levels: low, medium, or high. Levels increase the capability, but may also require more checks and increased monitoring." [VERIFIED: https://docs.adyen.com/marketplaces/verification-overview/capabilities.md, n.d., accessed 2026-11]
- **Nothing public found** on Adyen's merchant underwriting models, credit-exposure calculation beyond the deposit sentence above, or merchant-fraud detection (searched docs index for "underwriting", "merchant risk", "monitoring"; no dedicated page; the tech blog feed has no post on it).

**Stripe vs Adyen (merchant risk).**

| Topic | Stripe | Adyen |
| --- | --- | --- |
| Funds held against merchant risk | "Reserve": fixed or rolling, set by Stripe; platforms can set their own on connected accounts (max 180 days) | "Deposit": recalculated daily by Adyen from volume, chargebacks and refunds; a separate merchant-set "reserve" exists |
| Merchant risk score exposed | Yes, to platforms: account risk level and probability; fraudulent-merchant and delinquency signals | Not exposed in documentation found |
| Who bears connected-account losses | Configurable: platform or Stripe (Managed Risk) | Not covered here; see the platforms brief |
| Engineering publications | One post on LLMs for business risk review (Oct 2026) | None found |

**For readers new to payments.**
- *Underwriting*: the provider's assessment, at onboarding and afterwards, of how much loss a merchant could cause it.
- *Reserve (deposit)*: part of a merchant's sales held back by the provider to cover future refunds and chargebacks.
- *Negative balance*: a merchant account that owes the provider money, typically after refunds or disputes exceed its sales.
- *Credit exposure*: the amount the provider would lose if the merchant vanished today, because customers can still dispute payments already paid out.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] A provider extends credit to every merchant it pays out before the dispute window closes; merchant risk is therefore a balance-sheet control implemented in the ledger (a held balance type) and driven by a daily or event-driven recalculation. Adyen documents the daily recalculation; Stripe documents event-driven score updates. The intervention must be an API state the platform can read, not an email: Stripe's `interv_` requirements are the documented example.

---

## PART 2: Compliance as a system (chapter 26; parts of chapters 34 and 45)

### 2.1 The legal obligations in outline

**European Union.**
- The AML Regulation (EU) 2024/1624 "shall apply from 10 July 2027" (10 July 2029 for football clubs and agents) [VERIFIED: http://publications.europa.eu/resource/celex/32024R1624, published 2024-06-19]. Until then the national laws transposing Directive (EU) 2015/849 apply [ASSUMPTION/JUDGEMENT].
- Beneficial ownership: "direct or indirect ownership of 25 % or more of the shares or voting rights or other ownership interest in the corporate entity", with a possible lower threshold for high-risk categories "set at a maximum of 15 %" [VERIFIED: same regulation, Article 52].
- Sanctions inside due diligence: obliged entities must verify "whether the customer or the beneficial owners are subject to targeted financial sanctions", including whether sanctioned persons "control the legal entity or have more than 50 % of the proprietary rights" [VERIFIED: same regulation, Article 20(1)(d)]. For credit and financial institutions this verification "shall also be carried out upon any new designation" [VERIFIED: same regulation, Article 26(4)].
- Periodic update of customer information: at most every "1 year" for higher-risk customers and "5 years" for all others, and whenever "there is a change in the relevant circumstances of a customer" [VERIFIED: same regulation, Article 26(2)-(3)].
- "Suspicious transactions, including attempted transactions … should be reported to the FIU" [VERIFIED: same regulation, recital]; each obliged entity "shall have a compliance officer, to be appointed by the management body" [VERIFIED: same regulation, Article 11(2)].
- AMLA Regulation (EU) 2024/1620 "shall apply from 1 July 2025". AMLA "shall commence the first selection process by 1 July 2027"; in the first round it supervises directly at most "the 40 obliged entities or groups operating in the highest number of Member States" [VERIFIED: http://publications.europa.eu/resource/celex/32024R1620, published 2024-06-19]. AMLA's own timeline: operations began in summer 2025, "During 2028 — Start of direct supervision"; seat in Frankfurt am Main [VERIFIED: https://www.amla.europa.eu/about-amla_en, n.d., accessed 2026-11]. ⚠
- Direct supervision targets high-risk financial entities operating "in at least six Member States" [VERIFIED: AMLA Regulation, recital]. Whether Adyen or Stripe's EU entities will be selected is unknown until the list is published [ASSUMPTION/JUDGEMENT].

**United States.**
- FinCEN's Customer Due Diligence rule requires covered financial institutions (banks, broker-dealers, mutual funds, futures commission merchants) to "identify and verify the identity of any individual who owns 25 percent or more of a legal entity, and an individual who controls the legal entity" [VERIFIED: https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule, n.d., accessed 2026-11]. The rule dates from 2016 with compliance from May 2018 **(evidence age: 8 years; still in force, modified by the 2026 relief below)**.
- On 13 February 2026 FinCEN granted exceptive relief (FIN-2026-R001): institutions "may instead limit their identification and verification of the identities of beneficial owners" to "(1) when a legal entity customer first opens an account …; (2) any time thereafter when the covered financial institution has knowledge of facts that would reasonably call into question the reliability of beneficial ownership information previously obtained …; and (3) as needed based on a covered financial institution's risk-based procedures for conducting ongoing customer due diligence." [VERIFIED: https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf, published 2026-02-13] ⚠
- Beneficial ownership **reporting** to FinCEN under the Corporate Transparency Act no longer applies to US companies: an interim final rule published "March 26, 2025" removed the requirement for "U.S. companies and U.S. persons", and "On August 11, [FinCEN] issued a final rule making permanent the beneficial ownership information (BOI) reporting exemptions" [VERIFIED: https://www.fincen.gov/boi, n.d., accessed 2026-11]. The page does not print the year of the final rule (it is after March 2025, so August 2025 or August 2026); check the Federal Register before print [ASSUMPTION/JUDGEMENT]. Only foreign companies registered to do business in the US remain reporting companies [VERIFIED: same page].
- Consequence: in the US a provider cannot rely on a public beneficial-ownership register for domestic companies and must collect ownership from the customer [ASSUMPTION/JUDGEMENT].
- OFAC's 50 Percent Rule: an entity owned 50 percent or more in the aggregate by blocked persons is itself blocked; the rule "speaks only to ownership and not to control" [VERIFIED: https://ofac.treasury.gov/faqs/topic/1521, n.d., accessed 2026-11].

**FATF.** The EU and US rules implement the FATF Recommendations (customer due diligence, politically exposed persons, wire-transfer information, suspicious transaction reporting, beneficial ownership). The FATF site could not be fetched; the mapping of Recommendation numbers (10, 12, 16, 20, 24) is from general knowledge and must be checked against the FATF text [ASSUMPTION/JUDGEMENT]. The AML Regulation's recitals cite FATF standards on proliferation-financing sanctions risk [VERIFIED: Regulation (EU) 2024/1624, recital].

**For readers new to payments.**
- *KYC / KYB*: know your customer / know your business: collecting and verifying who a customer is before and while serving them.
- *Beneficial owner (UBO)*: the natural person who ultimately owns or controls a company, usually anyone with 25% or more.
- *Sanctions screening*: checking customers, owners and payment parties against government lists of people and entities one may not deal with.
- *PEP*: politically exposed person: someone with a prominent public function, who gets enhanced checks.
- *Suspicious activity (transaction) report*: a confidential report a regulated firm must file with the national financial intelligence unit.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Every one of these duties is continuous, not one-off: sanctions lists change daily, ownership changes, risk ratings expire after one or five years. The system of record for a customer therefore needs versioned identity data, a risk rating with an expiry, and a re-screening job triggered both by list updates and by customer-data updates. "Onboarding" is the first run of a loop.

### 2.2 How Stripe exposes compliance to customers

- Framing: "Every country has its own requirements that accounts must meet so that Stripe can pay out funds … These are typically known as Know Your Customer (KYC) requirements." Platforms "collect the required information from users and provide it to Stripe. … Stripe then attempts verification." [VERIFIED: https://docs.stripe.com/connect/identity-verification.md, n.d., accessed 2026-11]
- Stripe will not be a platform's compliance programme: "Don't rely on Stripe's verification to meet any independent legal KYC or verification requirements." [VERIFIED: same page]
- Requirements vary by "Country", "Capabilities", "Business type", "Business structure", "The service agreement type between Stripe and the connected account" and "The risk level" [VERIFIED: same page].
- Thresholds: "At certain variable thresholds—usually when a specified amount of time has passed or volume of charges have been made—you might need to collect and verify additional information. Stripe temporarily pauses charges or payouts if the information isn't provided or verified" [VERIFIED: same page].
- The `requirements` hash on the Account object is the contract: `currently_due` ("requirements that you must resolve by the `current_deadline` for the account to remain `active`"), `eventually_due`, `past_due` ("requirements that have disabled capabilities because they weren't resolved before the `current_deadline`"), `pending_verification`, `errors`, `disabled_reason`, `current_deadline` [VERIFIED: https://docs.stripe.com/connect/handling-api-verification.md?accounts-namespace=v1, n.d., accessed 2026-11].
- Consequence of a missed deadline: "Stripe typically disables payouts on the account if we don't receive the information by the `current_deadline`. … if payouts are already disabled and the account is unresponsive to our inquiries, Stripe might also disable the ability to process charges." [VERIFIED: same page]
- Up-front vs incremental onboarding: "Up-front onboarding collects the `eventually_due` requirements for the account, while incremental onboarding only collects the `currently_due` requirements." [VERIFIED: identity-verification page]
- Changing rules: "Stripe frequently updates KYC requirements, often due to changes implemented by financial regulators, card networks, and other financial institutions." Upcoming changes appear in `future_requirements`; "The `future_requirements.current_deadline` timestamp represents when entries in `future_requirements` will move to `requirements`." Hosted and embedded onboarding update automatically; "API-based flows require you to update them manually." [VERIFIED: https://docs.stripe.com/connect/handle-verification-updates.md?accounts-namespace=v1, n.d., accessed 2026-11]
- Sanctions and PEP checks surface as requirement types: `sanctions_review` ("We must verify that the business isn't involved with a sanctioned person or jurisdiction") and `pep_review` ("…a person of interest or politically exposed person"); also `legal_hold` ("Stripe is required to hold funds for a legal reason") [VERIFIED: handling-api-verification page].
- Beneficial owners: "individuals who either own 25% or more of a company or exercise significant control over it"; "The exact rules vary by country." [VERIFIED: https://support.stripe.com/questions/beneficial-owner-and-director-definitions, n.d., accessed 2026-11; read through a summarising fetch]
- Periodic checks: "We may also reach out periodically to confirm that information on your account is still accurate." [VERIFIED: https://support.stripe.com/questions/know-your-customer-obligations, n.d., accessed 2026-11; read through a summarising fetch] No interval is published.
- Who collects KYC on a platform depends on liability: where Stripe is responsible for negative balances, "Stripe is responsible for collecting KYC information from your connected accounts" [VERIFIED: https://docs.stripe.com/connect/risk-management.md, n.d., accessed 2026-11].
- Stripe Identity is a separate product a business can use on its own users: it verifies "government-issued ID documents from more than 120 countries" and matches "photo IDs with selfies" [VERIFIED: https://docs.stripe.com/identity.md, n.d., accessed 2026-11]. A platform can attach an Identity verification to a connected account's person, and "Verification completion automatically updates the account." [VERIFIED: handling-api-verification page]
- Prohibited and restricted businesses: the page (last updated 2026-09-22) has a prohibited list, a restricted list needing extra due diligence, and jurisdiction-specific lists for Brazil, Canada, India, Indonesia, Japan, Malaysia, Mexico, Singapore, Thailand, the UAE and the US. It states (paraphrased from the Dutch page served) that as a financial service provider Stripe must follow financial laws and the rules of its financial partners such as card networks and bank partners, so it cannot support some businesses even if it wanted to; for restricted categories Stripe may ask for licences or details of the business model and may refuse [VERIFIED: https://stripe.com/legal/restricted-businesses, last updated 2026-09-22; read in Dutch].
- **Not public**: Stripe's transaction-monitoring rules, sanctions-screening vendor or matching logic, suspicious-activity-report volumes, and re-verification intervals.

### 2.3 How Adyen exposes compliance to customers

- Framing: "As required by payment industry regulations, Adyen must verify the users in your marketplace before you can process payments, pay out their funds, and offer financial products to them. These verification checks are also called *Know Your Customer* (KYC) checks." [VERIFIED: https://docs.adyen.com/marketplaces/verification-overview.md, n.d., accessed 2026-11]
- Data model: the platform creates a **legal entity** ("contains information about your user, for example, the legal name, address, and tax information"), **transfer instruments** ("your user's verified bank account") and **supporting documents** through the Legal Entity Management API [VERIFIED: https://docs.adyen.com/marketplaces/account-structure-resources/legal-entity-management.md, n.d., accessed 2026-11].
- Capabilities: "Based on the results of the verification checks, Adyen decides if a user can perform any action on your marketplace. These actions are known as *capabilities*." Each capability has `requested`, `allowed` and `enabled` flags and a `verificationStatus` of `pending`, `valid`, `invalid` or `rejected`; `rejected` "is final and any errors cannot be resolved by updating data or uploading documents." [VERIFIED: https://docs.adyen.com/marketplaces/verification-overview/capabilities.md, n.d., accessed 2026-11]
- Four events trigger verification: requesting capabilities, a user changing their data, a user moving to a higher tier, and "Periodic data reviews required by Adyen" [VERIFIED: verification-overview page].
- Verification deadlines (Legal Entity Management API v3 and v4 only): a "30-day period" for payout-side capabilities such as `sendToTransferInstrument` and `issueBankAccount`, and a "60-day period" for `receivePayments`, `issueCard` and others; "a standard deadline could be shortened or removed in specific situations." "Users are allowed to continue using the capabilities while the deadline is active." [VERIFIED: same page] ⚠
- Staggered verification is the default: "only the minimum required verification data is collected from users before they start using your platform"; there are "four tiers" determined by "country, legal entity, and processed amount"; on moving up a tier "their payouts are temporarily disallowed until they complete additional verification checks." [VERIFIED: https://docs.adyen.com/marketplaces/verification-overview/verification-types.md, n.d., accessed 2026-11]
- Periodic reviews: "Adyen occasionally requires your users to review and confirm that their data is up-to-date." The webhook `balancePlatform.accountHolder.updated` carries `verificationStatus` "Set to `invalid`", `allowed` that "Remains set to `true`", the verification error "**3_10** and message 'Review of data is required'", a deadline, and the remediating action to call `/legalEntities/{id}/confirmDataReview` [VERIFIED: https://docs.adyen.com/marketplaces/verification-overview/data-review-process.md, n.d., accessed 2026-11]. A platform can also request a review proactively.
- Who is verified in an organisation: "UBOs through ownership" ("Individuals who directly or indirectly own 25% or more of the total shares, voting rights or other equity"), "UBOs through control" (at least one; "If such an individual cannot be identified, then members of senior management must be identified"), signatories (at least one) and, in some countries, directors [VERIFIED: https://docs.adyen.com/marketplaces/verification-requirements.md, n.d., accessed 2026-11].
- Onboarding options: "Hosted onboarding: Direct your users to a page hosted by Adyen, where Adyen manages the onboarding flow and user interface" (recommended) or "API-only onboarding" [VERIFIED: https://docs.adyen.com/marketplaces/onboard-users.md, n.d., accessed 2026-11].
- Risk appetite is stated: "Some individuals may exceed Adyen's risk tolerance and therefore cannot be accepted." [VERIFIED: verification-requirements page]
- Prohibited and restricted list: one table marking each product category "R" (restricted: "We will require additional documentation prior to onboarding") or "P" (prohibited), separately for "Merchant" and "Platform / Partner business" models; "Last update Nov 13 2025" [VERIFIED: https://www.adyen.com/legal/list-restricted-prohibited, last update 2025-11-13].
- Regulatory status: "Adyen N.V. is authorised as a credit Institution under the supervision of Dutch Central Bank (De Nederlandsche Bank)", with passporting across the EEA [VERIFIED: https://www.adyen.com/en_GB/licenses/europe, n.d., accessed 2026-11]. Adyen's marketing adds "full banking licenses in the US, UK, and EU" [VERIFIED: https://www.adyen.com/protect, n.d., accessed 2026-11].
- **Not public**: sanctions and PEP screening do not appear as named concepts in the verification pages fetched (searched for "sanction", "PEP", "screen": no matches in the overview, requirements and onboarding pages); transaction-monitoring rules, review intervals and report volumes are not published.

**Stripe vs Adyen (compliance exposure).**

| Topic | Stripe | Adyen |
| --- | --- | --- |
| Unit that is verified | Account (with Persons) | Legal entity (with associated entities), linked to an account holder |
| Unit that is switched on or off | Capability on the account | Capability on the account holder (`requested` / `allowed` / `enabled`) |
| What is outstanding | `requirements.currently_due`, `eventually_due`, `past_due`, `pending_verification`, `errors` | `verificationStatus`, `problems` with `verificationErrors`, `subErrors`, `remediatingActions` |
| Deadline | `current_deadline` (single earliest timestamp) | `verificationDeadlines` per capability; standard 30 or 60 days |
| Announced rule changes | `future_requirements` hash | Not found as an API construct; a legacy page announces a 2022 change |
| Progressive KYC | "Incremental" vs "up-front" onboarding | "Staggered" (default, four tiers) vs "upfront" |
| Periodic re-verification | "may also reach out periodically"; no API event documented | Documented process: error 3_10, `confirmDataReview`, proactive request |
| Sanctions/PEP visibility | Named requirement types `sanctions_review`, `pep_review` | Not named in docs found |
| Hosted collection | Connect Onboarding (hosted or embedded) | Hosted onboarding page |
| Identity product for the customer's own users | Stripe Identity | None found |

**For readers new to payments.**
- *Capability*: a named permission on an account (accept card payments, receive payouts) that the provider turns on only after the required checks pass.
- *Requirement*: one missing fact or document the provider needs, with a deadline.
- *Hosted onboarding*: the provider's own web pages collect the identity data, so the platform never handles the documents.
- *Restricted business*: a category the provider serves only after extra checks; a prohibited one it does not serve at all.

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Both providers model compliance as **state on an account that gates capabilities**, with deadlines, and deliver changes by webhook. A platform must therefore store this state, surface it to its sellers, and expect it to regress: an account that was fully enabled can become restricted months later without any action by the seller (a rule change, a periodic review, a sanctions hit). Larkfield's Frozen Studios follow directly from the documented mechanics: a requirement becomes due, the deadline passes, payouts are disabled first, charges later. The difference that matters to an integrator is that Adyen documents the periodic review as an API flow, while Stripe documents rule changes as an API structure (`future_requirements`).

### 2.4 Transaction monitoring and suspicious-activity reporting

Neither Stripe nor Adyen publishes how it monitors transactions for money laundering, what scenarios it runs, or how many reports it files; the law forbids telling a customer that a report was made (the AML Regulation: "Disclosing that a suspicion has been reported …" is restricted [VERIFIED: Regulation (EU) 2024/1624, recital]). What is public is the customer-facing effect: Stripe's `legal_hold` and `other_compliance_inquiry` requirement types, and Adyen's statement that deadlines change "based on ongoing account monitoring" (both cited above). Everything else in a chapter on transaction monitoring is reference-architecture judgement [ASSUMPTION/JUDGEMENT].

**Architecture implications.** [ASSUMPTION/JUDGEMENT] Fraud scoring and AML monitoring look alike (rules and models over transactions) but differ in timing and output: fraud decides in milliseconds and blocks; AML works after the fact over weeks of behaviour and produces a case for a human, a report to an authority, and sometimes a freeze. They should share data and not share a decision path.

---

## PART 3: The regulation calendar as of November 2026 (chapter 26; chapter 45)

| Item | Status on 17 November 2026 | Source |
| --- | --- | --- |
| **DORA**, Regulation (EU) 2022/2554 | "It shall apply from 17 January 2025." Covers payment institutions and e-money institutions; payment-related incident reporting moved from PSD2 to DORA | [VERIFIED: http://publications.europa.eu/resource/celex/32022R2554, published 2022-12-14] **(evidence age: 3.9 years; in application)** |
| DORA oversight of critical ICT third-party providers | On 18 November 2025 the three European Supervisory Authorities published "the list of designated critical ICT third-party providers (CTPPs)" after a criticality assessment of "systemic importance", role in "critical or important functions" and "substitutability" | [VERIFIED: https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital, published 2025-11-18] |
| **PSD3 and PSR** | Not yet adopted. Parliament's procedure file for the PSR (2023/0210(COD)) shows: committee approval of the agreed text 5 May 2026; "Council position published" 5 November 2026; second-reading referral 12 November 2026; "Indicative plenary sitting date, 2nd reading" 14 December 2026; status "Awaiting Parliament 2nd reading" ⚠ | [VERIFIED: https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210(COD), accessed 2026-11-17] |
| PSD3/PSR timeline after publication | Final compromise texts published by the Council 23 April 2026. Adyen's reading: publication in the Official Journal "expected by December 2026"; "General application is expected 21 months after entry into force (Verification of Payee provisions will apply 27 months after)" ⚠ | [VERIFIED: https://www.adyen.com/knowledge-hub/psd3, published 2026-10-12]; [WIDELY REPORTED: https://www.matheson.com/insights/psd3-and-psr-published-whats-changing-for-eu-payment-services/, 2026; law-firm briefing] |
| **Instant Payments Regulation**, (EU) 2024/886 | Euro-area PSPs: receive instant euro transfers "by 9 January 2025", send "by 9 October 2025". Non-euro Member States: receive by 9 January 2027, send by 9 July 2027. Payment and e-money institutions in the euro area: send and receive "by 9 April 2027" | [VERIFIED: http://publications.europa.eu/resource/celex/32024R0886, published 2024-03-19] |
| Instant payment mechanics | Payee's PSP must make funds available "within 10 seconds of the time of receipt of the payment order"; if no confirmation in 10 seconds the payer's PSP restores the payer's account | [VERIFIED: same regulation] |
| **Verification of Payee** | Payer's PSP "shall offer the payer a service ensuring verification of the payee", performed "immediately after the payer provides relevant information about the payee and before the payer is offered the possibility of authorising that credit transfer". Euro-area PSPs "shall comply with this Article by 9 October 2025"; non-euro by 9 July 2027 | [VERIFIED: same regulation] |
| Sanctions screening for instant payments | No per-transaction screening; instead PSPs verify their customer base "immediately after the entry into force of any new targeted financial restrictive measures … and at least once every calendar day". Euro-area compliance by 9 January 2025 | [VERIFIED: same regulation] |
| **EU AML package** | AMLR applies 10 July 2027; AMLA applies from 1 July 2025, first selection by 1 July 2027, direct supervision during 2028 ⚠ | [VERIFIED: sources in section 2.1] |
| **UK safeguarding reform** (FCA PS25/12) | Policy statement "First published: 07/08/2025". "The Supplementary Regime, and related amendments to the Approach Document, will come into force on 7 May 2026." Two stages: interim "Supplementary Regime" and an end-state "Post-Repeal Regime" replacing the regulations' safeguarding rules "with a 'CASS' style regime". The end-state date is not given on the page ⚠ | [VERIFIED: https://www.fca.org.uk/publications/policy-statements/ps25-12-changes-safeguarding-regime-payments-and-e-money-firms, published 2025-08-07] |
| "CASS 15" | The supplementary rules sit in a new chapter 15 of the FCA's Client Assets sourcebook, with daily reconciliation, monthly returns and annual safeguarding audits | [WIDELY REPORTED: law-firm and consultancy summaries, 2025; the detail was not read in the FCA Handbook in this session] |
| **US state money-transmitter law** | The Money Transmission Modernization Act is "a single set of nationwide standards, including net worth (capital), surety bond, and permissible investments (liquidity) requirements". "To date, thirty-one states have enacted the law in full or in part." Licensees in adopting states "collectively account for 99% of reported money transmission activity". CSBS notes "uneven adoption and interpretation" ⚠ | [VERIFIED: https://www.csbs.org/csbs-money-transmission-modernization-act-mtma, n.d., accessed 2026-11] |
| **US beneficial ownership** | CDD rule in force; relief FIN-2026-R001 of 13 February 2026; BOI reporting removed for US companies | [VERIFIED: sources in section 2.1] |
| **CFPB open-banking rule** (section 1033) | "On August 22, 2025, the CFPB released an Advance Notice of Proposed Rulemaking on Personal Financial Data Rights Reconsideration." Outcome not shown on the page (last modified 27 August 2025) ⚠ | [VERIFIED: https://www.consumerfinance.gov/personal-financial-data-rights/, accessed 2026-11] |
| **CFPB digital-payment-apps supervision rule** | CFPB page lists a final rule issued 21 November 2024, effective 9 January 2025. Reported as repealed by a Congressional Review Act resolution in 2025; the repeal could not be confirmed on an official page in this session ⚠ | [VERIFIED for the rule: https://www.consumerfinance.gov/rules-policy/final-rules/defining-larger-participants-of-a-market-for-general-use-digital-consumer-payment-applications/, published 2024-12-10]; repeal [ASSUMPTION/JUDGEMENT: recalled from 2025 trade press, not fetched] |
| **Visa VAMP** | Thresholds effective 1 June 2025; merchant Excessive threshold 150 bps from 1 April 2026 in AP, Canada, EU, US ⚠ | [VERIFIED: Visa fact sheet, section 1.6] |

**What PSD3/PSR change for fraud, per Adyen's summary (not the legal text).** "PSR introduces an automatic refund right for some cases of impersonation or spoofing fraud"; "Issuing banks can seek to recoup losses from acquirers, which increases the likelihood of chargebacks reaching businesses further down the chain"; the transaction-risk-analysis exemption "remains but its qualifying conditions could change"; EBA guidelines on the commercial agent exemption "may impact the availability of the commercial agent exemption for businesses that touch both buyer and seller funds." [VERIFIED: https://www.adyen.com/knowledge-hub/psd3, published 2026-10-12] These are a provider's interpretation of compromise texts not yet adopted; the final text was not read here [ASSUMPTION/JUDGEMENT for any reliance on it].

**Stripe vs Adyen (regulation).** Adyen publishes a dated explainer on PSD3/PSR (updated 12 October 2026) and states its licence position (credit institution under DNB). No Stripe page on PSD3, DORA or its EU licences was fetched successfully in this session, so no comparison of positions is offered. Adyen holding a banking licence and Stripe operating in the EU through payment or e-money institutions is a structural difference covered in the companies brief; it is not verified here [ASSUMPTION/JUDGEMENT].

**Enforcement and regulatory facts from official sources.**
- Stripe: the Massachusetts Attorney General announced that a "payment processor" would pay $120,000 in connection with a cryptocurrency scheme (PlexCoin), alleging inadequate risk monitoring; the official page returned 403 and the details come from a search summary [WIDELY REPORTED: https://www.mass.gov/news/payment-processor-to-pay-120000-in-connection-with-cryptocurrency-scheme, date not read; official press release seen only as a search result].
- Adyen: **no official enforcement action found** (one search covering DNB and Adyen returned nothing). This is a null result of a limited search, not proof of absence.
- No OFAC, FinCEN or FCA enforcement action naming Stripe or Adyen was found in the same search.

**For readers new to payments.**
- *DORA*: the EU's Digital Operational Resilience Act, which sets ICT risk, incident-reporting, testing and supplier rules for financial firms.
- *PSD3 / PSR*: the directive and regulation that will replace PSD2, the EU's payment services law.
- *Verification of Payee*: a check, before a bank transfer is approved, that the name the payer typed matches the account holder of the IBAN.
- *Safeguarding*: keeping customers' money separate from the firm's own so it survives the firm's failure.
- *Money transmitter licence*: the US state-by-state licence needed to hold or move money for others.

**Architecture implications.** [ASSUMPTION/JUDGEMENT]
- DORA turns resilience practices (incident classification and reporting, a register of ICT suppliers, exit plans, testing) into legal duties for payment institutions, and brings the largest cloud and software suppliers under direct EU oversight. A provider's cloud concentration is now a regulated risk, which links chapter 26 to the reliability chapters.
- The instant-payments rules replace per-transaction sanctions screening with a daily screen of the customer base, because a ten-second payment cannot wait for a manual sanctions review. That is a legal instruction to move a control from the payment path to the customer-state path: the same move the fraud chapter argues against for fraud and the compliance chapter argues for.
- Verification of Payee adds a synchronous pre-authorisation lookup between PSPs for every credit transfer; payout products that send bank transfers in bulk need a way to carry and handle its answers.
- The dates differ by institution type: a payment institution in the euro area has until 9 April 2027 for instant payments, a bank had to be ready in 2025. Which licence a provider holds decides which deadline applies to it.

---

## Key numbers

| Number | Definition | Source and date |
| --- | --- | --- |
| EUR 4.2 billion | Total value of reported payment fraud, EEA, 2024 (credit transfers, direct debits, cards from issuer side, cash withdrawals, e-money) | EBA/ECB report, Dec 2025 |
| EUR 1.3 billion; 0.033% | Value of fraudulent card transactions on EU/EEA-issued cards, 2024; fraud rate by value | EBA/ECB report, Dec 2025 |
| 83% | Share of card fraud (value and volume) in remote payments, EEA, 2024 | EBA/ECB report, Dec 2025 |
| 0.091% vs 0.007% | Card fraud rate by value, remote vs non-remote, EEA, 2024 | EBA/ECB report, Dec 2025 |
| £1.28 billion | Total payment fraud losses, UK, 2025 (unauthorised £703.4m + authorised £576.4m) | UK Finance, June 2026 |
| £423.5 million | UK remote purchase (CNP) card fraud losses, 2025 | UK Finance, June 2026 |
| 1 in 1,000 | Stripe's order-of-magnitude fraud prevalence among payments | Stripe blog, 29 Mar 2023 (3.6 years old) |
| < 100 ms | Time for Radar's decision | Stripe blog, 29 Mar 2023 (3.6 years old) |
| 0.1% | Share of legitimate payments Radar "incorrectly blocks" | Stripe blog, 29 Mar 2023 (3.6 years old) |
| mid-2022 | Radar's move from XGBoost + DNN ensemble to DNN-only | Stripe blog, 29 Mar 2023 |
| 800 million → 11 billion | Shield training-set size, sampled vs unsampled nine-month window | Stripe blog, 19 Oct 2026 |
| ~30 million | Parameters of the larger Shield model | Stripe blog, 19 Oct 2026 |
| 41% / 66% / 86% | Cumulative share of fraudulent disputes reported by day 14 / 30 / 60 after payment | Stripe blog, 19 Oct 2026 (chart) |
| > 8% | Recall improvement from the 2026 training changes | Stripe blog, 19 Oct 2026 |
| 59% → 97% | Stripe's "detection rate" for card-testing attacks on large users after the foundation model; definition not given | Stripe blog, 15 May 2025 |
| 80% | Stripe's stated fall in card-testing attacks on Stripe; baseline not given | Stripe blog, 15 May 2025 |
| 0–99; 65; 75 | Radar risk score range; default elevated and high thresholds | Stripe docs, accessed Nov 2026 |
| 200 / 100 | Maximum Radar transaction rules / account rules | Stripe docs, accessed Nov 2026 |
| 28% | Adyen's average increase in blocked card-testing attacks from subslice features; baseline not given | Adyen blog, 4 Oct 2026 |
| EUR 2,000 | Amount at or above which Adyen excludes a transaction from control traffic | Adyen docs, accessed Nov 2026 |
| 7 calendar days | Adyen case-management window to reject a reviewed transaction (with capture delay enabled) | Adyen docs, accessed Nov 2026 |
| 30 / 60 days | Adyen standard verification deadlines by capability | Adyen docs, accessed Nov 2026 |
| 180 days | Maximum reserve duration a Stripe platform can set; also the negative-balance period before platform reserve is used | Stripe docs, accessed Nov 2026 |
| 25% | Beneficial-ownership threshold (EU AMLR Art. 52; FinCEN CDD rule; Stripe and Adyen definitions) | EU 2024/1624; FinCEN; provider docs |
| 2,000 bps and 300,000 | Visa VAMP enumeration ratio and monthly enumerated-transaction count | Visa fact sheet, 2025 |
| 150 bps | Visa VAMP Excessive Merchant ratio (AP, Canada, EU, US) from 1 April 2026 | Visa fact sheet, 2025 |
| 20 ms; 15 billion | Visa VAAI Score response time; VisaNet transactions used to train it | Visa press release, 7 May 2024 |
| 17 Jan 2025 | DORA application date | Regulation (EU) 2022/2554 |
| 9 Oct 2025 / 9 Apr 2027 | Instant-payment sending and Verification of Payee for euro-area PSPs / deadline for euro-area payment and e-money institutions | Regulation (EU) 2024/886 |
| 10 July 2027 | Application date of the EU AML Regulation | Regulation (EU) 2024/1624 |
| 7 May 2026 | UK safeguarding Supplementary Regime in force | FCA PS25/12, 7 Aug 2025 |
| 31 | US states that have enacted the MTMA in full or in part | CSBS, accessed Nov 2026 |

## Open questions / not verifiable

1. **Radar's retraining interval.** Stripe says "regular retraining" on weekly data slices; no published interval. Any "daily retraining" statement is unsourced.
2. **How the payments foundation model is used in the authorization path**, and how it relates to the Shield model described in October 2026. Stripe has published results, not design.
3. **Definitions behind Stripe's card-testing numbers** ("down 80%", "59% to 97%") and Adyen's ("28% on average", "zero impact on legitimate shoppers"): baseline, period and metric are not given by either company.
4. **Adyen's fraud-risk model**: family, size, training data, latency and retraining cadence are unpublished. Only the bot-attack model's feature pipeline is described.
5. **Whether Radar's "more than 1,000 characteristics" (2023) and "hundreds of risk factors" (current docs) describe the same thing.**
6. **What Adyen's "Dynamic identification" is technically**, and whether it replaces shopper DNA. It appears in investor and marketing text only.
7. **Latency of Adyen Protect** and the behaviour of either system when the risk service is slow (Stripe documents fail-open on error; neither documents timeouts).
8. **Merchant underwriting at both companies**: criteria, models, reserve and deposit formulas. Stripe has published one research post on LLM-assisted review; Adyen nothing.
9. **Transaction monitoring, sanctions-screening implementation and suspicious-activity reporting** at both companies: not public, and partly not publishable by law.
10. **Re-verification intervals**: Stripe says "periodically", Adyen "occasionally". Neither publishes a schedule; the EU's one-year and five-year limits apply from July 2027.
11. **Whether either company (or its group) will be among the entities AMLA supervises directly** from 2028.
12. **PSD3/PSR final text and dates**: on 17 November 2026 the PSR awaited Parliament's second reading (indicative plenary 14 December 2026). Application dates depend on the publication date. Re-check before print.
13. **The year of FinCEN's final rule on BOI exemptions** ("On August 11", 2025 or 2026) and the status of the CFPB's section 1033 reconsideration and digital-payment-apps rule.
14. **The Stripe Massachusetts settlement**: date, exact allegations and terms need the official page (403 in this session).
15. **FATF Recommendation numbers and any 2025 change to the wire-transfer recommendation**: not fetched.
16. **Stripe's and Adyen's own DORA and PSD3 positions and Stripe's EU licence structure**: not verified here.
17. **Account takeover**: neither company's documentation fetched here defines it or describes a control for it.

## Source list

**Stripe**
- "How we built it: Stripe Radar", Ryan Drapeau, Stripe, 2023-03-29. https://stripe.dev/blog/how-we-built-it-stripe-radar — model history, 100 ms, 0.1%, XGBoost removal, risk insights.
- "Shepherd: How Stripe adapted Chronon to scale ML feature development", Ben Mears, Stripe, 2024-04-15. https://stripe.dev/blog/shepherd-how-stripe-adapted-chronon-to-scale-ml-feature-development — feature platform, latency vs freshness, dual key-value store.
- "Scaling Radar: Fighting fraud with agent-assisted machine learning", Ryan Drapeau and Sai Samant, Stripe, 2026-10-19. https://stripe.dev/blog/scaling-radar-fighting-fraud-with-agent-assisted-machine-learning — Shield, 11B training set, label delay curve, rollback, Agentic MLE.
- "Fine-tuning LLMs for risk assessment", Hangzhi Guo and others, Stripe, 2026-10-09. https://stripe.dev/blog/training-llms-for-risk-assessment — business risk decisions, human review precision.
- "Using AI to optimize payments performance with the Payments Intelligence Suite", Stripe, 2025-05-15. https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite — foundation model, card-testing claims, Radar product claims.
- "A primer on machine learning for fraud protection", Stripe guide, n.d. https://stripe.com/guides/primer-on-machine-learning-for-fraud-protection — precision/recall teaching material, release speed (read in Dutch).
- Stripe docs, n.d., accessed 2026-11: https://docs.stripe.com/radar.md (overview); /radar/how-radar-works.md (plans); /radar/risk-evaluation.md (scores, outcomes, feedback); /radar/rules.md (rules, limits, traffic allocation); /radar/lists.md; /radar/reviews.md; /radar/risk-settings.md (risk controls); /radar/multiprocessor.md; /radar/account-fraud-prevention.md; /radar/fraudulent-merchant.md; /radar/merchant-delinquency-risk.md; /connect/radar.md; /disputes/prevention/card-testing.md; /disputes/prevention/fraud-types.md.
- Stripe docs, n.d., accessed 2026-11: https://docs.stripe.com/connect/identity-verification.md; /connect/handling-api-verification.md?accounts-namespace=v1 (requirements hash, risk requirement types); /connect/handle-verification-updates.md?accounts-namespace=v1 (future requirements); /connect/risk-management.md; /connect/risk-management/managed-risk.md; /connect/connected-account-reserves.md; /identity.md.
- Stripe support, n.d.: https://support.stripe.com/questions/reserves-frequently-asked-questions; /questions/beneficial-owner-and-director-definitions; /questions/know-your-customer-obligations.
- "Prohibited and restricted businesses", Stripe, last updated 2026-09-22. https://stripe.com/legal/restricted-businesses (read in Dutch).

**Adyen**
- "Catching card testing at scale with real-time features", Jaap Stefels, Adyen, 2026-10-04. https://www.adyen.com/knowledge-hub/catching-card-testing-at-scale — subslices, proxy labels, Spark/Flink/Kafka/Cassandra, 28%.
- "PSD3 and PSR Explained", Adyen, updated 2026-10-12. https://www.adyen.com/knowledge-hub/psd3 — status and expected timeline, provider reading of fraud-liability changes.
- Adyen 2025 Annual Report page and shareholder letter, 2026-03-05. https://investors.adyen.com/financials/2025; press release https://www.adyen.com/press-and-media/adyen-publishes-2025-annual-report — Dynamic Identification, Uplift.
- Adyen docs, n.d., accessed 2026-11: https://docs.adyen.com/risk-management.md; /risk-management/configure-your-risk-profile.md; …/machine-learning-rules.md; …/custom-rules.md; …/post-auth-rules.md; …/risk-lists.md; /risk-management/control-traffic.md; /risk-management/shopper-dna.md; /risk-management/case-management.md; /risk-management/fraud-data-collection.md; /risk-management/handle-risk-rule-notifications.md; /uplift.md; /account/balances/deposit.md.
- Adyen docs, n.d., accessed 2026-11: https://docs.adyen.com/marketplaces/verification-overview.md; …/verification-overview/capabilities.md; …/verification-overview/data-review-process.md; …/verification-overview/verification-types.md; /marketplaces/verification-requirements.md; /marketplaces/onboard-users.md; /marketplaces/account-structure-resources/legal-entity-management.md.
- "Prohibited and Restricted Products and Services", Adyen, last update 2025-11-13. https://www.adyen.com/legal/list-restricted-prohibited.
- "DNB license to operate in EEA", Adyen, n.d. https://www.adyen.com/en_GB/licenses/europe; Protect product page https://www.adyen.com/protect.

**Networks and statistics**
- "Visa Announces Generative AI-Powered Fraud Solution to Combat Account Attacks", Visa, 2024-05-07. https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20661.html — VAAI Score.
- "Visa Acquirer Monitoring Program Overview" fact sheet, Visa, 2025. https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf — VAMP ratio, thresholds, enumeration criteria.
- "2025 Report on payment fraud" (EBA/REP/2025/40), EBA and ECB, 2025-12. https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf — EEA fraud values and rates for 2024.
- "Annual Fraud Report 2026", UK Finance, 2026-06. https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf — UK losses for 2025.

**Law and regulators**
- Regulation (EU) 2022/2554 (DORA), 2022-12-14. http://publications.europa.eu/resource/celex/32022R2554.
- Regulation (EU) 2024/886 (instant payments), 2024-03-19. http://publications.europa.eu/resource/celex/32024R0886.
- Regulation (EU) 2024/1624 (AML Regulation), 2024-06-19. http://publications.europa.eu/resource/celex/32024R1624.
- Regulation (EU) 2024/1620 (AMLA), 2024-06-19. http://publications.europa.eu/resource/celex/32024R1620.
- "About AMLA", AMLA, n.d. https://www.amla.europa.eu/about-amla_en — timeline.
- ESAs press release on designated critical ICT third-party providers, 2025-11-18. https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital.
- European Parliament Legislative Observatory, procedure 2023/0210(COD) (PSR), accessed 2026-11-17. https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210(COD).
- FCA PS25/12, "Changes to the safeguarding regime for payments and e-money firms", 2025-08-07. https://www.fca.org.uk/publications/policy-statements/ps25-12-changes-safeguarding-regime-payments-and-e-money-firms.
- FinCEN, "Information on Complying with the Customer Due Diligence (CDD) Final Rule", n.d. https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule.
- FinCEN Order FIN-2026-R001, 2026-02-13. https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf.
- FinCEN, "Beneficial Ownership Information Reporting", n.d. https://www.fincen.gov/boi.
- OFAC FAQ topic "Entities Owned by Blocked Persons (50% Rule)", n.d. https://ofac.treasury.gov/faqs/topic/1521.
- CSBS, "Money Transmission Modernization Act (MTMA)", n.d. https://www.csbs.org/csbs-money-transmission-modernization-act-mtma.
- CFPB, "Personal Financial Data Rights", last modified 2025-08-27. https://www.consumerfinance.gov/personal-financial-data-rights/; CFPB final rule on larger participants in digital consumer payment applications, 2024-12-10.

**Secondary**
- Matheson LLP, "PSD3 and PSR published: what's changing for EU payment services?", 2026-04-29. https://www.matheson.com/insights/psd3-and-psr-published-whats-changing-for-eu-payment-services/ — law-firm briefing on the compromise texts.
- Sardine, "New Visa dispute rules", 2025. https://www.sardine.ai/blog/new-visa-dispute-rules — vendor blog; Visa's non-disclosure of enumerated transactions.
- Massachusetts Attorney General press release (not fetched; 403). https://www.mass.gov/news/payment-processor-to-pay-120000-in-connection-with-cryptocurrency-scheme.
