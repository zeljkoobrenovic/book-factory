# Research brief: Card data, tokens and authentication (PCI scope, vaults, network tokens, 3-D Secure and SCA)

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 22 (tokenization, vaulting and PCI scope), 23 (network tokens), 25 (3-D Secure and SCA), and parts of 11 (the payment page and its scripts) and 50 (what is moving: PSD3/PSR, passkeys). Anchors are Stripe and Adyen; card networks, EMVCo, PCI SSC and EU legal texts supply the rules both companies build on.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated documentation and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (processor bulletin, trade press, consultancy, law firm), or a primary page seen only as a search-result excerpt. The kind of source is named.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including **every** statement about how Stripe, Adyen or a card network works internally beyond what it has published.

**Evidence age.** Stripe and Adyen documentation pages are living documents with no publication date; what they say in November 2026 may differ next quarter. Sources published before November 2023 are flagged **(evidence age: N years)** with a note on whether newer material confirms them.

**Research limitation.** What could not be fetched or verified in this session:

- **EMVCo specifications themselves** (Payment Tokenisation Technical Framework v2.3/v2.4; EMV 3-D Secure Protocol and Core Functions) sit behind a licence click-through and were not read. EMVCo's public technology pages, FAQs and press releases were read. Role definitions in the tokenisation framework and message names in the 3DS protocol (AReq/ARes, CReq/CRes, RReq/RRes) are therefore tagged ASSUMPTION/JUDGEMENT.
- **PCI SSC SAQ documents** (the v4.0.1 SAQ PDFs on `docs-prv.pcisecuritystandards.org`) returned a licence page, not the PDF. SAQ eligibility wording comes from PCI SSC's blog and FAQ 1588 and from the Stripe and Adyen PCI guides.
- **Mastercard and Visa developer documentation** (`developer.mastercard.com` MDES pages, `developer.visa.com` VTS pages, `mastercard.com` product pages) returned 403 or empty bodies. Mastercard is represented by one newsroom release (June 2024) and Visa by its product page and two press releases.
- **Network fee schedules** are not public. The Visa and Mastercard token-related fees in section 3.3 come from PayPal/Braintree's network-update bulletins and one consultancy (CMSPI), not from the networks.
- **Adyen's card-data export procedure**: a `help.adyen.com` article ("How can I prepare for token migration? [Export]") appears in search results but now redirects (HTTP 301) to the tokenization documentation, which does not describe an export. Only the search excerpt was seen.
- **Stripe's Click to Pay page** (`stripe.com/payment-method/click-to-pay`) exists in search results but rendered a generic payment-methods page; no Stripe statement on Click to Pay or on Visa/Mastercard payment passkeys was verified.
- **UK, India and Japan regulator texts**: the FCA page no longer carries its e-commerce SCA guidance; the Japanese Credit Card Security Guidelines are in Japanese and were not read; only one RBI circular (September 2021) was read. Dates for these markets lean on Stripe and Adyen documentation.
- **PSD3/PSR final texts** were not read. Status comes from the European Parliament Legislative Observatory (read); content comes from Adyen's knowledge-hub article of 12 October 2026 and a law-firm note.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: PSD3/PSR adoption dates, passkey pilots, Stripe Orchestration (private preview), Adyen risk-based exemptions (rolling out), network token fees, TRA limits, EMV 3DS 2.4 (draft), SAQ wording.

---

## PART 1: PCI DSS and how scope is determined (chapters 22 and 11)

### 1.1 The standard and its dates

- PCI DSS "provides a baseline of technical and operational requirements designed to protect payment account data" and applies to "Entities that store, process, or transmit cardholder data (CHD) and/or sensitive authentication data (SAD) or could impact the security of the cardholder data environment (CDE). This includes all entities involved in payment card processing – including merchants, processors, acquirers, issuers, and service providers" [VERIFIED: https://www.pcisecuritystandards.org/standards/pci-dss/, n.d., accessed 2026-11].
- **v4.0** was published in March 2022; **v4.0.1** was published on 11 June 2024 as "a limited revision"; "There are no additional or deleted requirements in this revision." "PCI DSS v4.0 will be retired on 31 December 2024. After that point, PCI DSS v4.0.1 will be the only active version" [VERIFIED: https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1, published 2024-06-11].
- v3.2.1 retired on 31 March 2024 (title of PCI SSC's own post, linked from the v4.0 resource hub) [VERIFIED: https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub, n.d., accessed 2026-11]. The exact day v4.0 was published (31 March 2022) is not on the pages read [ASSUMPTION/JUDGEMENT].
- The requirements that were "new" in v4.0 and best practice until then, including 6.4.3 and 11.6.1, became effective on **31 March 2025**; v4.0.1 "does not impact the effective date of these new requirements" [VERIFIED: same v4.0.1 post].
- The PCI SSC was formed in 2006 by Visa, Mastercard, American Express, Discover and JCB [VERIFIED: https://stripe.com/guides/pci-compliance, n.d., accessed 2026-11 (Stripe's summary; not checked against PCI SSC)].
- **Who enforces**: "PCI SSC does not define compliance requirements for any organization or set compliance validation responsibilities... Compliance validation requirements are set by brands, acquirers, payment facilitators, etc., which are often referred to as compliance enforcing entities" [VERIFIED: https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a, published 2025-01-30]. In practice the merchant's "compliance enforcing entity" is its provider: both Stripe and Adyen say which document they require (sections 1.5, 1.6).

### 1.2 Levels, SAQ types and the January 2025 SAQ A change

- **Merchant levels** as Stripe summarises them: Level 1 is more than 6 million Visa or Mastercard transactions (or 2.5 million American Express) a year and requires an annual Report on Compliance (RoC) by a Qualified Security Assessor (QSA) plus quarterly scans by an Approved Scanning Vendor; "Level 1 businesses can't use a Self-Assessment Questionnaire (SAQ)"; Levels 2–4 use an SAQ whose type depends on the integration [VERIFIED: https://stripe.com/guides/pci-compliance, n.d., accessed 2026-11]. Level thresholds are set by each card brand, not by PCI SSC [ASSUMPTION/JUDGEMENT].
- **Scale of the burden**, in Stripe's words: "you might be required to meet each of the 300+ security controls in PCI DSS. There are more than 1,800 pages of official documentation... and more than 300 pages just to understand which form(s) to use" [VERIFIED: same page].
- **SAQ A** "includes only those PCI DSS requirements applicable to merchants with account data functions completely outsourced to PCI DSS validated and compliant third parties, where the merchant retains only paper reports or receipts with account data. SAQ A merchants may be either e-commerce or mail/telephone-order merchants (card-not-present) and do not store, process, or transmit any account data in electronic form on their systems or premises" [VERIFIED: PCI SSC post of 2025-01-30, above].
- **The January 2025 change.** PCI SSC removed "PCI DSS Requirements 6.4.3 and 11.6.1 for payment page security, and Requirement 12.3.1 for a Targeted Risk Analysis to support Requirement 11.6.1" from SAQ A, and added an eligibility criterion for merchants to "confirm their site is not susceptible to attacks from scripts that could affect the merchant's e-commerce system(s)." The October 2024 SAQ A was retired on 31 March 2025, when the January 2025 version took effect. The modifications "do not remove or diminish the underlying requirements within PCI DSS" [VERIFIED: same post].
- **How a merchant meets the new criterion** (FAQ 1588): it "only applies to e-commerce merchants with a webpage that includes a TPSP's/payment processor's embedded payment page/form (for example, one or more inline frame(s) (iframes))" and "does not apply to e-commerce merchants with a webpage that redirects customers". The merchant confirms either by "Using techniques such as, but not limited to, those detailed in PCI DSS Requirements 6.4.3 and 11.6.1", or by "Obtaining confirmation from the merchant's PCI DSS compliant TPSP/payment processor... that, when implemented according to the TPSP's/payment processor's instructions, the TPSP's/payment processor's solution includes techniques that protect the merchant's payment page from script attacks" [VERIFIED: https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/how-does-an-e-commerce-merchant-meet-the-saq-a-eligibility-criteria-for-scripts/, n.d., accessed 2026-11].
- The other SAQ types named in the task, as the two providers apply them (PCI SSC's own definitions were not readable; see limitation):

| SAQ | Applies when (per the providers' guides) | Source |
| --- | --- | --- |
| A | All card entry is in a provider-hosted page or iframe; merchant never has unencrypted card data | Stripe guide; Adyen guide |
| A-EP | The merchant's own page hosts the form and passes card data to the provider from the browser (Stripe: legacy Stripe.js v2) | Stripe guide |
| B-IP | Standalone IP-connected approved terminals, no electronic card data storage (Adyen: default terminal integration with end-to-end encryption) | Adyen guide |
| P2PE | Terminals in a PCI-listed point-to-point encryption solution (Adyen: opt-in P2PE, plus its P2PE Instruction Manual) | Adyen guide |
| C | Payment application systems connected to the internet (Stripe: Terminal-only merchants) | Stripe guide |
| C-VT | Manual entry into a virtual terminal (Stripe: Dashboard manual card entry) | Stripe guide |
| D | Everything else, including sending raw card numbers to the provider's API | Both guides |

[VERIFIED for the right-hand mappings: https://stripe.com/guides/pci-compliance and https://docs.adyen.com/development-resources/pci-dss-compliance-guide.md, n.d., accessed 2026-11] [ASSUMPTION/JUDGEMENT for the generic one-line definitions of A-EP, B-IP, C and C-VT, which paraphrase PCI SSC documents not read in this session].

### 1.3 Requirements 6.4.3 and 11.6.1: scripts on the payment page

- **6.4.3** (as restated by Adyen): all payment page scripts loaded and executed in the consumer's browser are managed so that "A method is implemented to confirm that each script is authorized", "A method is implemented to assure the integrity of each script", and "An inventory of all scripts is maintained with written justification as to why each is necessary" [VERIFIED: https://docs.adyen.com/development-resources/pci-dss-compliance-guide/script-security.md, n.d., accessed 2026-11].
- **11.6.1** (as restated by Adyen): a change- and tamper-detection mechanism "alerts personnel about unauthorized modification (including indicators of compromise, changes, additions, and deletions) to the security impacting HTTP headers and the script contents of payment pages, as received by the consumer browser's Document Object Model (DOM)" [VERIFIED: same page].
- PCI SSC published an information supplement, "Payment Page Security and Preventing E-Skimming – Guidance for PCI DSS Requirements 6.4.3 and 11.6.1" [VERIFIED: https://blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming, n.d., accessed 2026-11].
- **Who still owes 6.4.3/11.6.1 after January 2025**: per Adyen, they "remain applicable to merchants that are required to submit PCI DSS Self-Assessment Questionnaire D (SAQ D) and merchants that are required to present an Attestation of Compliance (AoC) for onsite assessment" [VERIFIED: https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility.md, n.d., accessed 2026-11]. So a Level 1 merchant using only hosted fields still has to address them in its RoC [ASSUMPTION/JUDGEMENT].
- **3-D Secure scripts are exempt from 6.4.3**: "The 3D Secure script validation process is exempted from the scope of PCI DSS requirement 6.4.3, because the trust relationship with the 3D Secure service provider is established through due diligence, onboarding, and business agreements of the entities involved" [VERIFIED: Adyen script-security page, above].
- **Adyen's recommended controls**: a Content Security Policy for 6.4.3, and Subresource Integrity for its legacy client-side encryption library [VERIFIED: same page and PCI guide]. **Stripe's** integration security guide publishes the CSP directives for Checkout, Stripe.js, Connect embedded components and Link, and warns: "Including JavaScript from other sites makes your security dependent on theirs and poses a security risk. If they're ever compromised, an attacker could execute arbitrary code on your page... we recommend trying to minimize it" [VERIFIED: https://docs.stripe.com/security/guide.md, n.d., accessed 2026-11]. Stripe's PCI guide and security guide do not mention requirements 6.4.3 or 11.6.1 by number (searched both pages for "6.4.3", "11.6.1", "script") [VERIFIED: same pages].
- **The residual risk, in Adyen's words** (useful for chapter 11 and the Larkfield script inventory): with an iframe integration "attackers can create alternative content for the Drop-in or Components, or drop an iframe over the already existing iframe. In this scenario, the payment may still be completed, but a copy of the cardholder data is sent to the attacker" [VERIFIED: Adyen PCI guide].

### 1.4 PCI P2PE and in-person scope

- Adyen offers two terminal encryption modes. Default **E2EE**: "Adyen's end-to-end solution protects payment messages by encrypting them at the terminal and decrypting them at the platform before sending them for authorization"; merchant completes **SAQ B-IP**. Opt-in **P2PE**: a "PCI-approved P2PE payment solution" with separate encryption of the PAN and track data and "Compliance with the P2PE Instruction Manual"; merchant completes **SAQ P2PE** and "store staff will need to inspect the terminals regularly and keep an audit trail of these inspections". Adyen's own comparison: "While E2EE is secure, it does not have the PCI P2PE-validated 'stamp'" [VERIFIED: https://docs.adyen.com/development-resources/e2ee-p2pe-comparison.md, n.d., accessed 2026-11].
- Stripe: "If you exclusively collect card data through Stripe Terminal, you can validate using SAQ C" [VERIFIED: https://stripe.com/guides/pci-compliance]. Stripe Terminal "is certified to the EMVCo Level 1 and 2 standards" and to PA-DSS [VERIFIED: https://docs.stripe.com/security.md, n.d., accessed 2026-11]. **Nothing public found** on a PCI-listed P2PE solution for Stripe Terminal (searched the docs index `llms.txt` for "P2PE" and the Terminal overview for "encrypt").

### 1.5 Stripe: integration to SAQ, and its own attestation

- "A PCI-certified auditor evaluated Stripe and certified us to PCI Service Provider Level 1... This audit includes both the Stripe Card Data Vault (CDV) and the secure software development of our integration code" [VERIFIED: https://docs.stripe.com/security.md]. "Stripe is certified annually by an independent PCI Qualified Security Assessor (QSA)" [VERIFIED: https://docs.stripe.com/security/guide.md].

| Stripe integration | Stripe's stated requirement | Stripe's reasoning (quoted) |
| --- | --- | --- |
| Checkout or Elements | SAQ A | "host all card data collection inputs within an iframe served from Stripe's domain (not yours)" |
| Mobile SDK (official UI components, or Elements in a WebView) | SAQ A | "card numbers pass directly from your customers to Stripe"; SDK "development and change control complies with PCI DSS (requirements 6.3–6.5)" |
| Connect (card data collected only by the platform) | SAQ A | Stripe checks whether the platform provides the documentation |
| Stripe.js v2 (legacy, own form) | SAQ A-EP | "pass card data entered in a form hosted on your own site" |
| Terminal only | SAQ C | — |
| Dashboard manual entry | SAQ C-VT | "for exceptional circumstances only" |
| Direct API (raw card numbers to the API) | SAQ D | "your integration is directly handling that data" |

[VERIFIED: https://stripe.com/guides/pci-compliance, n.d., accessed 2026-11]

- Stripe adds a commercial lever: "Radar... is only available when using any of our methods for client-side tokenization" [VERIFIED: same page]. Stripe's docs index tells assistants that a user sending raw card numbers server-side "might be required to prove PCI compliance to gain access to such an option" [VERIFIED: https://docs.stripe.com/llms.txt, n.d., accessed 2026-11].
- Stripe automates the paperwork: "We analyze the user's integration method and dynamically inform them of which PCI validation form to use", with pre-filled SAQs in the Dashboard for Elements, Checkout, Terminal SDKs and mobile libraries [VERIFIED: https://docs.stripe.com/security.md].

### 1.6 Adyen: integration to SAQ, and its own attestation

- "Adyen is a PCI DSS Level 1 Service Provider, with PCI DSS compliance assessed by an independent Qualified Security Assessor (QSA) annually." Responsibility boundary: "Adyen is solely responsible for the security of cardholder data only as soon as Adyen receives the data through the relevant payment interface." Adyen is also "a qualified PCI Secure Software Lifecycle (SLC) software vendor for the development of payment pages and components" [VERIFIED: https://docs.adyen.com/development-resources/pci-dss-compliance-guide.md, n.d., accessed 2026-11].

| Adyen integration | Required document | Adyen's risk label and reasoning |
| --- | --- | --- |
| Drop-in / Components / plugins (Card Component in an iframe) | SAQ A | Low–Medium; "cardholder data is encrypted on your shopper's browser. You do not have access to decryption keys" |
| Hosted Checkout (redirect) | SAQ A | Low |
| Pay by Link | None required by Adyen ("you must be PCI DSS compliant at all times") | Low |
| Custom Card Component | SAQ A | — |
| API only (own form, raw card data sent over TLS 1.2) | SAQ D | High; "your system receives, transmits, and potentially stores and processes cardholder data" |
| Client-side encryption with a third-party JWE library | SAQ A | "once encrypted, you cannot decrypt the data" |
| Legacy client-side encryption (CSE) library | SAQ A, plus Subresource Integrity | "being phased out"; no new integrations |
| Mobile Drop-in / Components | SAQ A | Data "encrypted in the app, sent to your server, and then transmitted to Adyen" |
| Mobile API only | SAQ D | — |
| Terminals, default E2EE | SAQ B-IP | Low |
| Terminals, P2PE | SAQ P2PE + P2PE Instruction Manual | Low |

[VERIFIED: same Adyen PCI guide]

**Stripe vs Adyen**

| Topic | Stripe | Adyen | Difference the evidence supports |
| --- | --- | --- | --- |
| Level 1 service provider attestation | Yes; scope names the Card Data Vault and integration code | Yes; plus PCI Secure SLC vendor listing | Equivalent claims; Adyen names one extra PCI programme |
| Own-form card entry with SAQ A | Not offered; own form means A-EP (legacy) or D | Offered: card data encrypted in the browser (JWE or legacy CSE) passes through the merchant's server and Adyen still requires only SAQ A | **Real divergence.** Adyen accepts encrypted card data transiting merchant servers as SAQ A; Stripe's model keeps card data off merchant servers entirely |
| 6.4.3 / 11.6.1 guidance | CSP directives published; requirements not named | Dedicated script-security page; names the 3DS exemption | Adyen documents the requirement; Stripe documents the mechanism |
| Terminals | SAQ C | SAQ B-IP by default, SAQ P2PE optional | Adyen offers a PCI-listed P2PE option; none found for Stripe |
| SAQ automation | Dashboard wizard, pre-filled SAQs | Guide plus document request by Adyen | Stripe automates more [ASSUMPTION/JUDGEMENT: from the pages read, not a product comparison] |

**For readers new to payments**

- **Cardholder data environment (CDE)**: the people, processes and systems that store, process or transmit card numbers, plus anything that can affect their security; PCI DSS applies to all of it.
- **SAQ (self-assessment questionnaire)**: the form a smaller merchant fills in yearly to attest PCI DSS compliance; which form applies depends on how card data is collected.
- **Hosted field**: a card input rendered inside an iframe served by the payment provider, so the merchant's page never sees what is typed.
- **QSA / RoC / AoC**: the accredited auditor, the audit report, and the signed summary a company shares with partners.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Scope follows the data path. The integration decision (hosted page, iframe fields, encrypted own form, raw API) is a compliance decision first and a UX decision second; reversing it later means a different SAQ and possibly an auditor.
- "SAQ A" does not mean "no risk on my page". Since 2025 the merchant must attest that its page cannot be used to attack the embedded form, or rely on its provider's confirmation. A script inventory and a CSP are the cheap controls; the provider's iframe does not protect against an overlay injected by a third-party script.
- Adyen's client-side encryption shows a second design: card data may cross the merchant's servers if the merchant cannot decrypt it. It buys a fully custom form at the cost of a more complex argument to an assessor, and Adyen is retiring its own library for the web.

---

## PART 2: Vaulting and provider tokens (chapter 22)

### 2.1 What Stripe has published about its vault

Stripe's public statement is one section of its security page, "Dedicated card technology" [VERIFIED: https://docs.stripe.com/security.md, n.d., accessed 2026-11]:

- **Isolation**: "The Stripe infrastructure for storing, decrypting, and transmitting primary account numbers (PANs), such as credit card numbers, runs in a separate hosting infrastructure and doesn't share any credentials with the rest of our services, including our API and website."
- **Hosting and people**: "A dedicated team manages our CDV in an isolated Amazon Web Services (AWS) environment that's separate from the rest of the Stripe infrastructure. We restrict access to this separate environment to a small number of specially trained engineers and review access quarterly."
- **Encryption and keys**: "All card numbers are encrypted at rest with AES-256. Decryption keys are stored on separate machines."
- **Internal tokenization**: "We tokenize PANs internally, isolating raw numbers from the rest of our infrastructure. None of the Stripe internal servers and daemons can obtain plaintext card numbers, but they can request that cards are sent to a service provider on a static allowlist."
- **Other data**: "We treat other sensitive data, such as bank account information, similarly to how we tokenize PANs."
- Elsewhere on the page: "All Stripe internal server-to-server communication is encrypted using mutual transport layer security (mTLS)"; code changes "are recorded in an immutable, tamper-evident log."

**Not public** (searched `stripe.com/blog`, `stripe.dev`, and the web for "card data vault", vault engineering talks): no Stripe engineering post or talk on the vault's design was found. Service names, the key-management system, hardware security modules, key rotation, the number of regions, and how the "static allowlist" is enforced are not published. Stripe's marketing explainers ("What is a token vault?") describe vaults generically; one states "Stripe's Vault and Forward API stores tokens alongside native network tokenisation" [VERIFIED: https://stripe.com/resources/more/token-vault, n.d., accessed 2026-11]. A third-party "teardown" naming a "Vault 2.0" is not a Stripe source and should not be used [ASSUMPTION/JUDGEMENT].

### 2.2 What Adyen has published about its vault

- Adyen names the store: "we store payment details in the Adyen Vault"; "Reduce your PCI DSS scope by letting Adyen handle the sensitive payment data in the Adyen Vault" [VERIFIED: https://docs.adyen.com/online-payments/tokenization.md, n.d., accessed 2026-11].
- Security statement, in full: "We use client-side encryption (CSE) and end-to-end encryption to ensure that sensitive data is never exposed. All cryptographic keys are managed in a secure and compliant manner, so that you can focus on processing payments while Adyen handles the security requirements" [VERIFIED: same page].
- Vaults are regional: to use the Forward API, "Make sure that your live endpoint region matches your Adyen token vault storage region" [VERIFIED: https://docs.adyen.com/online-payments/tokenization/forward-payment-details.md, n.d., accessed 2026-11].
- Marketing: "Adyen's universal token vault stores details once, then lets you use them everywhere" [VERIFIED: https://www.adyen.com/uplift/tokenize, n.d., accessed 2026-11].
- One engineering article exists, but it is about **personal data in Adyen's data infrastructure, not the card vault**: incoming PII "passes through our Tokenization system, which encrypts the data with a key from the HSM-backed vault key manager"; "The encrypted data is stored inside the Data Vault"; tokens are UUIDs "generated using hardware entropy"; the design supports "multiple active tokenization services that operate concurrently" [VERIFIED: https://www.adyen.com/en_GB/knowledge-hub/securing-your-personal-data-via-tokenization, published 2019-10-01] **(evidence age: 7 years; no newer engineering source confirms or updates it; it shows an HSM-backed design pattern at Adyen in 2019, not the current card vault)**.

**Not public**: the Adyen Vault's isolation model, encryption algorithm, key hierarchy, HSM use for card data, and hosting. Adyen's docs do not make a statement comparable to Stripe's "AES-256 / separate machines / separate AWS environment" (searched the tokenization, PCI and security documentation pages; `adyen.com/security` and `adyen.com/platform/certifications` returned 404).

### 2.3 Token types each company exposes

**Stripe**

- **Token** (`tok_…`, Tokens API): "Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner." "You can't store or use tokens more than once. To store card or bank account information for later use, create Customer objects or External accounts." Token kinds: card, bank account, CVC update, PII, person, account [VERIFIED: https://docs.stripe.com/api/tokens.md, n.d., accessed 2026-11].
- **PaymentMethod** (`pm_…`): "contains reusable payment details, such as a card's expiration date or a billing address. It doesn't include transaction-specific information"; reusable once attached to a Customer; single-use methods "can't be attached to customers because they're consumed after a payment attempt" [VERIFIED: https://docs.stripe.com/payments/payment-methods.md, n.d., accessed 2026-11]. A card PaymentMethod carries a `fingerprint` that identifies the underlying card number without revealing it [VERIFIED: the field is present in the same page's example object] [ASSUMPTION/JUDGEMENT: its meaning is from the API reference, not re-read in this session].
- **ConfirmationToken**: "ConfirmationTokens help transport client side data collected by Stripe JS over to your server for confirming a PaymentIntent or SetupIntent. If the confirmation is successful, values present on the ConfirmationToken are written onto the Intent." It "holds a superset of the data found on a PaymentMethod, such as shipping information" [VERIFIED: https://docs.stripe.com/api/confirmation_tokens.md and https://docs.stripe.com/payments/payment-element/migration-ct.md, n.d., accessed 2026-11].
- **What a merchant may keep**: "the card type, the last four digits of the card, and the expiration date. This information isn't subject to PCI compliance... Additionally, you can store anything returned by our API" [VERIFIED: https://docs.stripe.com/security/guide.md].
- Token scope: Stripe tokens are "a nonsensitive string that can be used only by the business that collected the card" [VERIFIED: https://stripe.com/guides/understanding-benefits-of-network-tokens, n.d., accessed 2026-11].

**Adyen**

- **`storedPaymentMethodId` + `shopperReference`**: "you must store the token with a unique shopper reference... we use it to associate the token with the shopper." The token arrives asynchronously: "get the unique identifier and other information about the token from the `recurring.token.created` webhook" [VERIFIED: https://docs.adyen.com/online-payments/tokenization.md and https://docs.adyen.com/online-payments/tokenization/create-tokens.md, n.d., accessed 2026-11]. Adyen "uses a reference to the shopper rather than the payment details for tokenization" [VERIFIED: https://docs.adyen.com/development-resources/migrating-payment-data.md, page metadata last modified 2019-12-06] **(evidence age: 7 years; the current tokenization page confirms the shopper-reference model)**. `recurringDetailReference` is the older name for the same identifier in the Classic API [ASSUMPTION/JUDGEMENT: industry knowledge; the classic pages were listed but not read].
- **`recurringProcessingModel`** declares what the token is for (`CardOnFile`, `Subscription`, `UnscheduledCardOnFile`) [VERIFIED: create-tokens page, where all three values appear].
- **Scope**: "By default, shopper references and tokens can only be used with one merchant account... you can enable the Token Groups feature which shares shopper references and their associated tokens between your merchant accounts" [VERIFIED: tokenization page].
- **Across channels**: "If you tokenize the shopper's payment details when they make a payment at the point of sale, you can use that token in a later online payment." Use cases Adyen lists: subscriptions sold in store, hospitality no-shows, autonomous stores, omnichannel [VERIFIED: https://docs.adyen.com/point-of-sale/recurring-payments.md, n.d., accessed 2026-11].
- **Wallet limit**: "You cannot use a token stored with Adyen to make a one-click payment with Apple Pay, Google Pay, or Samsung Pay" [VERIFIED: tokenization page].

### 2.4 Token portability: import, export and forward

**Import (both document it)**

- Stripe: the previous processor "encrypts your data with the Stripe PGP key and uploads it" to "a dedicated SFTP server for each migration request"; Stripe returns a mapping file from old identifiers to new ones. "Processors can take anywhere from a few days to several months to produce a final export... After Stripe receives valid data, imports typically complete within 10 business days." "Processors differ in how they handle export requests—some charge a fee, and some require specific forms" [VERIFIED: https://docs.stripe.com/get-started/data-migrations/pan-import.md, n.d., accessed 2026-11].
- Adyen: "We do not charge for migrating payment data. Because of technical and compliance complexity, migrating payment data usually takes 10 days or more." Files are CSV, PGP-encrypted; Adyen recommends three stages (new sign-ups to Adyen first, then import, then switch old customers) [VERIFIED: https://docs.adyen.com/development-resources/migrating-payment-data.md, page metadata last modified 2019-12-06] **(evidence age: 7 years; still the live page)**.

**Export**

- Stripe: "We believe our customers own the sensitive data they entrust to Stripe. We make sure that you have access to this data—even if you're moving elsewhere." Conditions: "we can only transfer your card data to another PCI DSS Level 1-compliant payment processor"; Stripe requires the recipient's "current PCI Attestation of Compliance (AOC), or their listing on Visa's Global Registry of Service Providers" and a "PGP public encryption key, which must be 4096 bits or greater in length", hosted over HTTPS on a domain named in the AOC or registry listing. The export is "an encrypted JSON export file" with card numbers, expiry, names, addresses, emails and metadata. **Not exported**: "payment history, subscriptions, or other objects", and "any credentials saved through Link" [VERIFIED: https://docs.stripe.com/get-started/data-migrations/pan-export.md, n.d., accessed 2026-11]. CVCs are not in the sample export file [VERIFIED: same page's sample]; PCI DSS forbids storing them after authorization [ASSUMPTION/JUDGEMENT].
- Adyen: **no public export procedure found**. A help-centre article on token export is indexed by search engines (excerpt: export as CSV, delivered over SFTP that the receiving vault usually hosts, for a whole merchant account or a list of shopper references) but the URL now redirects to the tokenization docs [WIDELY REPORTED: https://help.adyen.com/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export, search excerpt of an Adyen help article, 2026].

**Forward (both now offer it)** ⚠

- **Stripe Vault and Forward API**: "allows you to tokenize and store card details in Stripe's PCI-compliant vault and route that data to supported processors or endpoints." Flow: the merchant creates a ForwardingRequest with the destination URL and a body with blank card fields; Stripe substitutes `card_number`, `card_expiry`, `card_cvc`, `cardholder_name`; "Stripe redacts identified PCI sensitive data and relays the response." Limits: "available only to businesses with a dedicated Stripe account team"; destinations come from a supported list (the page lists more than twenty processors, including Adyen's `/payments` and `/storedPaymentMethods`, Braintree, Checkout.com and Worldpay); Link credentials excluded; "CVCs expire automatically after a certain time period and also expire when used with the Vault and Forward API". Wallet device tokens can be forwarded through `network_token_number` / `network_token_cryptogram` fields. Stripe "only retains hashed and encrypted versions of destination endpoint API keys" [VERIFIED: https://docs.stripe.com/payments/vault-and-forward.md, n.d., accessed 2026-11].
- **Stripe Orchestration** (private preview): "Stripe manages the full processor integration on your behalf—routing, authentication, capture, refunds, and 3DS across multiple PSPs. Same Payment Intents API"; not supported: "non-card payments or Link, Capital, Connect, Terminal, or Organizations", disputes and settlement [VERIFIED: https://docs.stripe.com/payments/orchestration.md, n.d., accessed 2026-11].
- **Adyen Forward**: "You can forward payment details that you stored with Adyen to a PCI compliant third party, like a payment service provider (PSP). We support forwarding card details, and network tokens." Flow: POST `/forward` with placeholders; "Adyen replaces the placeholders with the payment details and makes a request to the third party API on your behalf". Requires Checkout API v70 or later and enablement by Support [VERIFIED: https://docs.adyen.com/online-payments/tokenization/forward-payment-details.md]. Adyen markets it as retaining "full routing control across your entire PSP setup without duplicate vaults" [VERIFIED: https://www.adyen.com/uplift/tokenize].

**Stripe vs Adyen**

| Topic | Stripe | Adyen | Difference |
| --- | --- | --- | --- |
| Vault internals published | One paragraph: separate AWS environment, no shared credentials, AES-256, keys on separate machines, internal tokenization, static allowlist | Names "Adyen Vault"; keys "managed in a secure and compliant manner"; regional storage | Stripe states more. Neither publishes a design |
| Engineering posts on the card vault | Nothing public found | Nothing on the card vault; one 2019 post on PII tokenization (HSM-backed) | Thin on both sides |
| Reusable token | PaymentMethod attached to a Customer | `storedPaymentMethodId` paired with the merchant's own `shopperReference` | Stripe holds the customer object; Adyen keys on the merchant's customer ID [ASSUMPTION/JUDGEMENT] |
| Token delivery | Synchronous API object | Webhook `recurring.token.created` | Adyen's is asynchronous by design |
| In-person to online reuse | Not researched in this brief | Documented (POS token reused online) | See brief `acquiring` for Stripe Terminal saved cards |
| Export | Documented, with recipient conditions and file format | No public procedure found | Stripe is explicit; Adyen's process is not public |
| Forward to other PSPs | Vault and Forward API (account-team gated); Orchestration in private preview | Forward API (Support-enabled); cards and network tokens | Both; Adyen also forwards network tokens |

**For readers new to payments**

- **PAN (primary account number)**: the card number printed on the card; the thing PCI DSS exists to protect.
- **Provider token**: an identifier a payment provider gives a merchant in place of a card number; it works only with that provider and usually only for that merchant.
- **Vault**: the isolated system that keeps the real card numbers and the mapping from tokens to them.
- **Token portability**: the ability to move stored cards from one provider to another, done provider-to-provider under PCI rules because the merchant never held the numbers.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- A provider token is a foreign key into someone else's database. Portability is a contractual and operational process (weeks, PGP files, an AOC check), not an API call; plan migrations in the three stages Adyen describes.
- The vault pattern is: smallest possible system that can see plaintext, no shared credentials, everything else works with references, and the only way plaintext leaves is to an allowlisted destination. Stripe's paragraph is the best public statement of that pattern; writers should quote it and say plainly that the rest is not public.
- Forwarding APIs turn a provider's vault into a shared service for multi-processor setups. The trade is dependence on that provider's uptime and on its list of supported destinations.

---

## PART 3: Network tokens (chapter 23)

### 3.1 EMV Payment Tokenisation: what EMVCo publishes

- "EMV Payment Tokenisation enhances in-store, e-commerce and remote payment security by removing the most valuable data to a fraudster, the primary account number (PAN), and replacing it with a unique alternative value, the EMV Payment Token. Importantly, an EMV Payment Token is constrained in how it can be used. For example, to a specific merchant, device or payment scenario" [VERIFIED: https://www.emvco.com/emv-technologies/payment-tokenisation/, n.d., accessed 2026-11].
- **How it differs from provider tokens**: "EMV Payment Tokenisation enables a payment token to be used in a payment transaction from point of purchase, to an acquirer and then passing across the payment networks through to payment authorisation by the card issuer... Other forms of tokenisation can happen at different points within the payment process. For example, within the merchant environment tokenisation can happen between the merchant and acquirer" [VERIFIED: same page, FAQ].
- **The specification**: "EMV Payment Tokenisation Specification – Technical Framework" **v2.4, published 9 July 2026** (v2.3 was published 19 October 2021); supported by "A Guide to Use Cases" [VERIFIED: same page]. ⚠ v2.4 is four months old; what changed from v2.3 was not read.
- **Registries**: EMVCo "manages and assigns TSP Codes worldwide to ensure that each TSP issuing EMV Payment Tokens is uniquely identifiable", and BIN Controller IDs so that institutions can "link an EMV Payment Token to a PAN using a payment account reference (PAR)". PAR "enables support for value added services such as fraud screening, anti-money laundering monitoring, some PAN-based loyalty systems" [VERIFIED: same page].
- EMVCo runs no testing programme for tokens: they "are not contained within one area of the payment ecosystem, but instead overlay the entire payment infrastructure" [VERIFIED: same page].
- **Roles and lifecycle** (framework not read; industry knowledge) [ASSUMPTION/JUDGEMENT]: a **token requestor** (merchant, PSP or wallet, registered with the token service provider and given a Token Requestor ID) asks a **token service provider** (TSP; in practice the card network, sometimes the issuer) to issue a token for a PAN; the issuer approves, possibly after identifying and verifying the cardholder; the TSP keeps the token-to-PAN mapping in its token vault and de-tokenises during authorization. **Domain restriction controls** bind a token to a requestor, channel or device. Each cardholder-initiated use carries a one-time **cryptogram** generated for that token and transaction. **Lifecycle management** means the TSP suspends, resumes, deletes or re-maps the token when the card is lost, reissued or closed, and notifies the requestor.
- Corroboration from sources read: Adyen's explainer says "A network token can be requested by a merchant, payment gateway, or payment processor. The requestor sends a PAN to the card scheme, which forwards the request to the issuer. The issuer approves the request, and the network issues the token. Tokens are domain-locked... card schemes issue a cryptogram each time a customer uses their saved card details to initiate a purchase. These cryptograms are effectively one-time-passwords that are contextual to the business, token, and purchase" [VERIFIED: https://www.adyen.com/knowledge-hub/network-tokenization, published 2024-09-04, modified 2026-09-14]. The RBI's 2021 circular permits "card issuers to offer card tokenisation services as Token Service Providers (TSPs)" [VERIFIED: https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12159&Mode=0, published 2021-09-07] (evidence age: 5 years; Stripe's current India page confirms the regime).

### 3.2 Visa Token Service and Mastercard MDES: facts and performance claims

- **Visa Token Service (VTS)** "is the foundational platform for global tokenization"; related services include the Visa Cloud Token Framework and a credential-enrichment service that "leverages VisaNet data to search for the latest confirmed expiry associated with the PAN" during provisioning [VERIFIED: https://usa.visa.com/products/visa-token-service.html, n.d., accessed 2026-11].
- **Visa's claims, exact wording** (press release, 4 June 2024): "Visa tokens have generated more than $40 billion in incremental ecommerce revenue for businesses globally and saved $650 million in fraud in the last year"; "issued more than 10 billion tokens since the technology's launch in 2014"; "Currently, 29% of all transactions processed by Visa use tokens"; "Tokenization technology has also caused a six-basis point increase in payment approval rates globally. Overall, tokenization can reduce the rate of fraud by up to 60%"; "over 8,000 issuers are enabled for tokenization"; "over 1.5 million eCommerce merchants transacted with Visa Tokens every day." Footnotes: revenue from "VisaNet CY2023 credit and debit global card-not-present (CNP) payment volume for tokenized and non-tokenized credentials"; fraud from "Risk Datamart CY2023" [VERIFIED: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20701.html, published 2024-06-04].
- **Source-quality note**: the release says "six-basis point" (0.06 percentage points). Secondary sources routinely cite a Visa figure of about 6% or "6 percentage points" for the same effect; CMSPI, for example, writes that Visa's token growth "has been associated with a 6% improvement in authorized rates" [WIDELY REPORTED: https://cmspi.com/april-2026-u-s-network-fee-updates-3-billion-estimated-cost-impact-for-merchants/, consultancy article, 2026]. The two differ by a factor of 100. Writers should quote the press release exactly and say the figure is a vendor comparison of tokenized against non-tokenized CNP volume, not a controlled experiment [ASSUMPTION/JUDGEMENT].
- **Mastercard** (press release, 11 June 2024): "Mastercard today announced its vision for 100% e-commerce tokenization in Europe by the end of the decade. This supports a global commitment to phase out manual card entry." "Introduced in 2014, Mastercard's tokenization service today secures 25% of all e-commerce transactions globally, with adoption accelerating 50% year-over-year." Three pillars: tokenization, Click to Pay "To eliminate manual card entry", and payment passkeys "to eliminate passwords and one-time codes" [VERIFIED: https://newsroom.mastercard.com/news/press/2024/june/mastercard-reimagines-online-checkout-commits-to-reaching-100-e-commerce-tokenization-by-2030-in-europe/, published 2024-06-11]. The 2030 goal is a stated vision for Europe, not a rule; the release gives no approval or fraud percentages.
- MDES (Mastercard Digital Enablement Service) is the name of Mastercard's tokenization platform [ASSUMPTION/JUDGEMENT: industry knowledge; Mastercard developer pages were not fetchable].
- **Provider-reported uplift**: Adyen: "We've seen an average uplift of 3% in authorization rates for businesses on our platform who use network tokenization" [VERIFIED: Adyen knowledge hub, 2024-09-04]. Stripe publishes no network-token-only figure; it claims "Increase acceptance rates by 3.8% on average with Authorisation Boost" (network tokens plus Adaptive Acceptance plus Card Account Updater) and that businesses on interchange-plus pricing "can also lower card processing costs by up to 3.3%" [VERIFIED: https://stripe.com/authorization-boost, n.d., accessed 2026-11]. Neither states a methodology [ASSUMPTION/JUDGEMENT].

### 3.3 Fees and mandates ⚠

The networks do not publish fee schedules. The following are from processor bulletins and one consultancy.

- **Visa Secure Credential Framework (Europe)**: "Effective 1 October 2023: Visa will introduce a new fee of 2.5bps (0.025%) per transaction for domestic and interregional ecommerce primary account number (PAN)-approved authorizations processed without Visa EMV Payment Tokens (network tokenization) or Visa Secure (3D Secure)", in "All European countries (except Turkey and France)"; exempted transactions (TRA, low value) pay it too unless tokenized or authenticated [WIDELY REPORTED: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23, processor bulletin, 2023] (evidence age: 3 years; the 2026 Braintree bulletin still refers to "the Secure Credential Framework fee").
- **Visa Digital Commerce Fee (US)**: from 1 October 2023, "0.75bps on all settled transactions with a min of $0.0075" on card-not-present transactions [WIDELY REPORTED: same bulletin, 2023]. From April 2026 it applies to authorized CNP transactions and bundles token and updater services (TAVV, Visa Account Updater, Visa Digital Credential Updater); Visa also introduces "a Card-Present Token Fee on authorized network-tokenized card-present transactions" [WIDELY REPORTED: CMSPI article above, 2026].
- **Mastercard (EU, UK/Ireland)**: revised "Customer Performance Development Fund" pricing from 1 January 2027, "four rate changes phased in over three years, aimed at driving tokenization and authentication"; current not-tokenized/not-authenticated card-on-file fee 5 bps in most of Europe; "In April 2028, Guest Checkout will be included in the non-token fee" [WIDELY REPORTED: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/fall/2026, processor bulletin, 2026].
- **Visa DCAP (Canada)**: from 24 October 2026, qualifying tokenized consumer-credit CNP transactions that share device ID, IP, email and billing address "qualify for an interchange incentive of 10bps. A new Enhanced Data Program fee of 5bps will also apply" [WIDELY REPORTED: same 2026 bulletin].
- **What Stripe says about fees**: "Some payments that use a network token qualify for reduced interchange rates. For example, Visa offers certain discounts on consumer card-not-present payments in some markets." "Mastercard levies a Credential Continuity Program (CCP) fee when attempting a payment using outdated card details." And the cost side: "Stripe doesn't reflect any fees that might occur as a result of network token use, such as the Visa Digital Credential Updater (VDCU) fee" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md, n.d., accessed 2026-11].
- **What Adyen says**: "Some schemes, like Visa, might charge a fee for the management of issued tokens. They still charge lower fees for processing tokens than for processing PANs" [VERIFIED: Adyen knowledge hub, 2024-09-04].
- **A legal mandate exists in India**: the RBI "mandates card on file (CoF) tokenization through the card networks"; "Businesses, Payment Aggregators (PAs), Payment Gateways (PGs), and acquiring banks can no longer store customer card information"; a token must be scoped "to a Merchant, Customer Card, and Token Requestor" and needs "explicit user consent and Additional Factor of Authentication" [VERIFIED: https://docs.stripe.com/india-network-tokenization.md, n.d., accessed 2026-11].

### 3.4 How Stripe and Adyen expose network tokens

**Stripe**

- Automatic, no integration: "Our optimised network token solution works out of the box for all merchants who use Stripe Payments. Stripe has built integrations with networks and will request tokens on your behalf" [VERIFIED: https://stripe.com/guides/understanding-benefits-of-network-tokens, n.d., accessed 2026-11]. The docs index instructs: "Stripe manages network token provisioning and uses for its network token solution; no separate network token integration is required" [VERIFIED: https://docs.stripe.com/llms.txt].
- Token or PAN, decided per payment: "Stripe also optimises for future transactions once a token is created, determining when to use a network token or the underlying PAN. We maintain PAN redundancy to retry failed network token transactions on the underlying PAN" [VERIFIED: same guide].
- Latency is acknowledged: "using a network token often requires a one-time cryptogram that needs to be fetched from networks. As a result, network tokens can be prone to high additional latency compared to using PANs. Stripe has optimised our infrastructure to minimise these latency impacts" [VERIFIED: same guide].
- Lifecycle: "if a customer lost their card, Stripe would get notified by the network and would update the token directly so it would continue to work" [VERIFIED: same guide].
- Availability: "US, Canada, Mexico, India, Australia, New Zealand, the EU, the UK, the UAE, Brazil, Malaysia, Hong Kong, Japan, the Philippines, Thailand and Singapore" [VERIFIED: same guide] ⚠.
- Packaging: network tokens are one of three features of **Authorization Boost**, with Adaptive Acceptance and Card Account Updater; the Dashboard estimates recovered volume per feature, attributing each recovered payment to "the one most likely responsible for approval". "Stripe doesn't guarantee any outcomes" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md].
- India is the exception: "Cards won't be automatically tokenized" without customer consent [VERIFIED: India page above].

**Adyen**

- Two modes. **Adyen-managed**: "This option does not require any additional integration. We collect and store network tokens from the card schemes. When you send a payment request, we automatically swap the card details from your payment request for the network token"; with a stored token, "we automatically swap that for a network token". **Merchant-managed**: "you can keep your existing network tokens and use them in the payment requests", sending the cryptogram as `mpiData.tokenAuthenticationVerificationValue` ("The network token authentication verification value (TAVV). This is the network token cryptogram") [VERIFIED: https://docs.adyen.com/online-payments/network-tokenization.md, n.d., accessed 2026-11].
- Limitation: "Network tokenization is only applicable for payments acquired by Adyen. It cannot be used with external acquirer connections" [VERIFIED: same page].
- Fallback is visible in the response: "If a payment attempt with a network token fails (`attempt1`), we automatically retry the payment. In the second attempt (`attempt2`), we do not swap the card details or the `storedPaymentMethodId` token for a network token"; the merchant can receive `retry.attemptN.networkTokenOffered` and the raw acquirer response per attempt [VERIFIED: same page]. For merchant-managed tokens there is a separate **PAN fallback** (the merchant supplies the PAN; "Not every refused payment leads to a retry with the PAN"; "You cannot use 3D Secure for transactions with network tokens that you manage yourself") [VERIFIED: https://docs.adyen.com/online-payments/network-tokenization/pan-fallback.md, n.d., accessed 2026-11].
- Routing: US network tokens co-badged with a debit network (Accel, Maestro USA, NYCE, PULSE, STAR) can be routed "over the network with the lowest costs and/or the best authorization rate" [VERIFIED: network-tokenization page].
- Observability: optional `networkToken.bin`, `networkToken.tokenSummary`, `latestCard.summary`, `latestCard.expiryDate` in responses [VERIFIED: same page].
- Enablement wording is inconsistent across Adyen's pages: the tokenization overview says "Adyen automatically requests network tokens for stored cards when possible, and no extra integration is required", while the network-tokenization page tells merchants to "ask our Support Team to enable payments with network tokens" [VERIFIED: both pages]. Whether network tokens are on by default for a new account is unclear [ASSUMPTION/JUDGEMENT].
- Related: Account Updater (batch and real time). Adyen has "been offering Real Time Account Updater with a number of global card networks since 2017" and was first to offer Visa's real-time updater in Europe [VERIFIED: https://www.adyen.com/press-and-media/adyen-first-to-launch-real-time-account-updater-with-visa-in-europe, published 2022-09-13] (evidence age: 4 years; the product is still documented).

### 3.5 Wallets as device tokens

- Google Pay returns either "cards on file on Google.com (`PAN_ONLY`) or a device token on an Android device authenticated with a 3-D Secure cryptogram (`CRYPTOGRAM_3DS`)"; for `PAN_ONLY` the merchant should "trigger 3D Secure (step-up authentication)" [VERIFIED: https://developers.google.com/pay/api/web/guides/tutorial, n.d., accessed 2026-11].
- "Apple Pay uses network tokenization, stores payment information securely in the shopper's Apple Pay eligible device, and confirms the payment through Touch ID or Face ID authentication." Liability shift applies for American Express, Discover, JCB, Mastercard and Visa; for Visa, globally from iOS 16.2, and only for European-issued cards on older versions [VERIFIED: https://docs.adyen.com/payment-methods/apple-pay.md, n.d., accessed 2026-11].
- Stripe treats wallet credentials as network tokens when forwarding: "Apple Pay DPANs: Use network token replacement fields (`network_token_number`, `network_token_cryptogram`, `network_token_expiry`, `network_token_electronic_commerce_indicator`)" [VERIFIED: https://docs.stripe.com/payments/vault-and-forward.md]. Stripe's Radar exposes `has_liability_shift`, which "might not always be the same as 3DS, for example Apple Pay in certain regions" [VERIFIED: https://docs.stripe.com/radar/rules.md, n.d., accessed 2026-11].
- A device token (DPAN) is an EMV payment token whose requestor is the wallet and whose domain is the device; a card-on-file network token has the merchant or PSP as requestor [ASSUMPTION/JUDGEMENT].

### 3.6 Click to Pay and payment passkeys, status November 2026 ⚠

- **Click to Pay** is the consumer brand for EMV Secure Remote Commerce. Adyen: "The card scheme is responsible for securely storing the cardholder data and issuing tokens"; supported in Web Drop-in/Components v5.39.0+ and Checkout API v69+; "Currently, Adyen's Click to Pay integration only supports recurring payments on Mastercard Click to Pay" [VERIFIED: https://docs.adyen.com/payment-methods/cards/click-to-pay.md, n.d., accessed 2026-11].
- **Visa Payment Passkey Service** was announced 15 May 2024: "Built on the latest Fast Identity Online (FIDO) standards, the Visa Payment Passkey Service confirms a consumer's identity and authorizes online payments with a quick scan of their biometrics"; "As its first deployment of passkeys, Visa is integrating Visa Payment Passkey Service into Click to Pay" [VERIFIED: https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20686.html, published 2024-05-15].
- **Adyen–Visa announcement** (29 October 2026): "today announced the roll out of Visa Payment Passkey (VPP) through Authenticate, a module within its AI-powered payment optimization suite, Adyen Uplift." "Adyen will initially offer Visa Payment Passkey through Authenticate in the UK, with further enhancements and a global expansion planned for 2027." Footnote: "After a cardholder's bank verifies them and they create a passkey with Visa Payment Passkey, they can authenticate future purchases by unlocking their device... Biometric data is never collected by or shared with Visa" [VERIFIED: https://www.adyen.com/press-and-media/adyen-visa-payment-passkey, published 2026-10-29]. The release does **not** claim Adyen is first; trade press reported Checkout.com rolling out at about the same time [WIDELY REPORTED: https://idtechwire.com/checkout-com-and-adyen-begin-rolling-out-visa-payment-passkey-to-merchants/, trade press headline, 2026].
- **Adyen's documentation is more cautious than its press**: "Scheme passkeys are currently in pilot phase, and only enabled for a specific group of merchants"; "Scheme passkey authentication is supported for Mastercard network tokenized transactions"; not supported for merchant-initiated recurring payments, nor "if the redirect URL opens in an iFrame"; the merchant "cannot enforce scheme passkey authentication"; success gives "a liability shift from your company to the issuer" [VERIFIED: https://docs.adyen.com/online-payments/authentication/scheme-passkeys.md, n.d., accessed 2026-11].
- **Google Secure Payment Authentication** at Adyen: "currently only enabled for a specific group of merchants"; the shopper authenticates "directly on your website, using the Google web front end. This avoids a redirect to the shopper's card issuer"; liability shift applies [VERIFIED: https://docs.adyen.com/online-payments/authentication/google-secure-payment-authentication.md, n.d., accessed 2026-11].
- **Stripe**: nothing verified on Click to Pay or on Visa/Mastercard payment passkeys (see limitation). Stripe's docs index has no page for either (searched `llms.txt` for "click to pay", "passkey"); Stripe's own checkout wallet is Link, covered in brief `stripe-api`.

**Stripe vs Adyen (network tokens)**

| Topic | Stripe | Adyen | Difference |
| --- | --- | --- | --- |
| Provisioning | Automatic for Stripe Payments; no API surface | Adyen-managed (automatic swap) or merchant-managed (bring your own tokens and cryptograms) | Adyen lets a merchant be its own token requestor; Stripe does not document that option |
| Token vs PAN choice | Stripe decides per payment; retries on PAN | Token first, automatic retry without token; per-attempt data returned | Adyen exposes the attempts; Stripe exposes estimates in a dashboard |
| Reported uplift | 3.8% average for the Authorization Boost bundle | 3% average for network tokenization | Not comparable: different bundles, no methodology |
| Fee transparency | Names CCP and VDCU fees; estimates savings for US/Canada domestic | General statement that tokens cost less to process | Stripe is more specific |
| Forwarding tokens to other PSPs | Wallet DPANs through network-token fields | Network tokens explicitly supported | — |
| Passkeys | Nothing verified | Visa Payment Passkey (UK, Oct 2026), Mastercard passkeys, Google SPA, all pilot or limited | Adyen has announced; Stripe has not, on the evidence found |

**For readers new to payments**

- **Network token**: a substitute card number issued by the card network for one merchant (or one device), which the network maps back to the real card during authorization.
- **Token requestor**: the party that asks the network for a token: a merchant, a payment provider or a wallet.
- **Token service provider (TSP)**: the party that issues tokens and keeps the token-to-card mapping; usually the card network.
- **Cryptogram**: a one-time value generated for a single token transaction, proving the request comes from the token's legitimate holder.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- A stored card now has up to three representations: the PAN in the provider's vault, the provider token the merchant holds, and the network token the provider holds. The provider chooses which to send per attempt; keep the provider token as the system-of-record key and never assume the credential used.
- Network tokens add a network call (the cryptogram) to the authorization path. Stripe says so; a design that batches renewals should expect it.
- Network tokens belong to the requestor. Tokens a PSP requested generally do not move with the merchant; the PANs do. Merchants who want token continuity across PSPs become their own token requestor (Adyen's merchant-managed mode) or use a forwarding vault.
- Fees are moving from "discount for tokens" toward "penalty for raw PANs", and in 2026 toward fees on tokens themselves. Cost models built on a token discount need a yearly review.

---

## PART 4: Authentication: SCA and 3-D Secure (chapter 25, part of 50)

### 4.1 PSD2 strong customer authentication: the legal text

- **Definition** (Directive (EU) 2015/2366, Article 4(30)): "'strong customer authentication' means an authentication based on the use of two or more elements categorised as knowledge (something only the user knows), possession (something only the user possesses) and inherence (something the user is) that are independent, in that the breach of one does not compromise the reliability of the others" [VERIFIED: http://publications.europa.eu/resource/celex/32015L2366, published 2015-11-25] (evidence age: 11 years; in force and unchanged on this point).
- **Article 97(1)**: a payment service provider applies SCA "where the payer: (a) accesses its payment account online; (b) initiates an electronic payment transaction; (c) carries out any action through a remote channel which may imply a risk of payment fraud or other abuses." **Article 97(2)** adds dynamic linking for remote payments: SCA "that includes elements which dynamically link the transaction to a specific amount and a specific payee" [VERIFIED: same text].
- **Liability, Article 74(2)**: "Where the payer's payment service provider does not require strong customer authentication, the payer shall not bear any financial losses unless the payer has acted fraudulently. Where the payee or the payment service provider of the payee fails to accept strong customer authentication, it shall refund the financial damage caused to the payer's payment service provider" [VERIFIED: same text]. This is the statutory root of "liability shift": whoever avoids SCA carries the loss.
- The RTS (Commission Delegated Regulation (EU) 2018/389) "shall apply from 14 September 2019" [VERIFIED: http://publications.europa.eu/resource/celex/32018R0389, published 2018-03-13] (evidence age: 8 years; in force). Card e-commerce enforcement was phased: Stripe treats EU cards saved before 31 December 2020 and UK cards saved before 14 September 2021 as eligible for "previous authorization agreements" [VERIFIED: https://docs.stripe.com/strong-customer-authentication.md, n.d., accessed 2026-11].
- **Merchant-initiated transactions** are not in the RTS as an exemption; they are treated as outside Article 97 because the payer does not initiate them. Stripe: such payments "technically fall outside the scope of SCA. In practice, marking a payment as MIT is similar to requesting an exemption; neither a customer challenge nor a liability shift occurs" [VERIFIED: https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions.md, n.d., accessed 2026-11]. Adyen: "Recurring transactions are merchant-initiated, and therefore considered out-of-scope" [VERIFIED: https://docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/sca-exemptions.md, n.d., accessed 2026-11].

### 4.2 RTS exemptions and their thresholds

| Exemption | Article | Conditions (quoted or paraphrased from the RTS) |
| --- | --- | --- |
| Contactless at point of sale | 11 | Individual amount "does not exceed EUR 50"; and cumulative amount since last SCA "does not exceed EUR 150" or consecutive transactions "does not exceed five" |
| Unattended transport and parking terminals | 12 | No thresholds |
| Trusted beneficiaries | 13 | Payee is on a list the payer created with SCA through its own bank |
| Recurring transactions | 14 | SCA when the payer "creates, amends, or initiates for the first time, a series of recurring transactions with the same amount and with the same payee"; none for subsequent ones |
| Low-value remote | 16 | Amount "does not exceed EUR 30"; and cumulative since last SCA "does not exceed EUR 100" or not more than "five consecutive individual remote electronic payment transactions" |
| Secure corporate payments | 17 | Dedicated processes "only made available to payers who are not consumers", accepted by the competent authority |
| Transaction risk analysis (TRA) | 18 | Provider's fraud rate at or below the reference rate for the band; amount within the band; real-time risk analysis finds no abnormal behaviour, device, malware, known fraud scenario, abnormal payer location or high-risk payee location |

TRA bands for remote card payments (Annex): fraud rate **0.13%** up to **EUR 100**, **0.06%** up to **EUR 250**, **0.01%** up to **EUR 500**. A provider must stop using a band when its rate exceeds the reference "for two consecutive quarters" (Article 20) [VERIFIED for the whole table: RTS text above].

- **Who may apply which**: the RTS addresses "payment service providers", so both the issuer and the acquirer side can invoke TRA and low value. Adyen: if the acquirer requests TRA and it is granted, "the chargeback liability stays with you"; if the issuer applies TRA unasked, "The chargeback liability shifts to the issuer" [VERIFIED: Adyen SCA exemptions page].
- **Scheme support differs**: at Adyen, American Express supports only the secure-corporate exemption; Cartes Bancaires supports low value and TRA but not secure corporate; Visa and Mastercard support all three [VERIFIED: same page].
- **France tightened exemptions outside 3DS**: from 10 March 2025 French issuers "soft decline all customer initiated authorization exemptions except those requested via EMV 3DS"; from 14 October 2024 exemptions limited "to EUR 100 per shopper per day" [VERIFIED: https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance.md, n.d., accessed 2026-11].

### 4.3 EMV 3-D Secure 2: components, flows and versions

- EMVCo: "EMV 3DS enables the exchange of data, or messages, between the merchant and the issuer to authenticate the consumer and approve the transaction. The data includes information about the transaction, payment method and device" [VERIFIED: https://www.emvco.com/emv-technologies/3-d-secure/, n.d., accessed 2026-11].
- **Components** as the providers describe them: the **3DS Server** on the merchant/PSP side, the card network's **Directory Server (DS)**, and the issuer's **Access Control Server (ACS)**. Stripe: "Stripe communicates with the card network's DS and the issuer's Access Control Server (ACS)" [VERIFIED: https://docs.stripe.com/payments/3d-secure/standalone-three-d-secure.md, n.d., accessed 2026-11]. Adyen: "the 3D Secure server fetches and stores URLs for scripts from an EMV 3DS Access Control Server (ACS), EMV 3DS Directory Server (DS)..." [VERIFIED: Adyen script-security page].
- **Message flow** (protocol specification not read) [ASSUMPTION/JUDGEMENT]: optional device fingerprinting (the "3DS method"); authentication request and response (AReq/ARes) from 3DS Server through the DS to the ACS; if the ACS wants a challenge, challenge request and response (CReq/CRes) between the cardholder's browser or app and the ACS; then a results request and response (RReq/RRes) back through the DS. The output is an authentication value (CAVV for Visa, AAV for Mastercard), an Electronic Commerce Indicator (ECI) and a DS transaction ID that go into the authorization message.
- Stripe's five steps for its standalone API match that shape: "Create... Fingerprint (optional)... Submit... Challenge (if required)... Retrieve the authentication outcome. On success, extract the cryptogram, ECI, and DS Transaction ID" [VERIFIED: Stripe standalone page].
- **Frictionless vs challenge**: "In a frictionless flow, the acquirer, issuer, and card scheme exchange all necessary information in the background through passive authentication using the shopper's device fingerprint. The transaction is completed without further shopper interaction." "In a challenge flow, the issuer requires additional shopper interaction, either through biometrics, two-factor authentication, or similar methods" [VERIFIED: https://docs.adyen.com/online-payments/3d-secure.md, n.d., accessed 2026-11]. The issuer decides: "Stripe can't guarantee your preference because the issuer determines the ultimate authentication flow" [VERIFIED: https://docs.stripe.com/payments/3d-secure/authentication-flow.md, n.d., accessed 2026-11].
- **Versions**:
  - 2.1.0 (2017) and 2.2.0 (2018) [ASSUMPTION/JUDGEMENT: industry knowledge; dates not re-verified].
  - **2.3.1** released 29 September 2022, "effective immediately and replaces EMV 3DS 2.3.0", adding data for Secure Payment Confirmation and out-of-band authentication [VERIFIED: https://emvco.com/wp-content/uploads/2022/11/EMV-3DS-2.3.1-press-release.pdf, published 2022-09-29] (evidence age: 4 years). **2.3.1.1** replaced it in May 2023 [VERIFIED: https://www.emvco.com/knowledge-hub/enhancing-the-emv-3-d-secure-specifications/, published 2023-05-19] (evidence age: 3.5 years).
  - **2.4.0.0 is in draft**: "EMV 3-D Secure Protocol and Core Functions Specification – DRAFT 2 – Comment period ends 8 January 2027", published 4 November 2026 [VERIFIED: EMVCo 3DS page] ⚠.
  - **2.1 was deprecated in 2024**: "July 01, 2024: Mastercard deprecates 3DS 2.1.0 and expects volumes to be fully migrated to 3DS 2.2.0"; "September 24, 2024: Visa deprecates 3DS 2.1.0" [VERIFIED: Adyen 3DS-for-regulation page].
  - Stripe "supports the 3DS protocol up to and including version 2.3.1" [VERIFIED: Stripe standalone page].
- **3DS1 sunset**: "Effective 15 October 2022, Visa will discontinue support of 3-D Secure 1.0.2 and related technology" [VERIFIED: https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-will-discontinue-support-of-3d-secure.pdf, published 2021-02-04] (evidence age: 5 years; Stripe's current docs confirm "Major card brands no longer support 3D Secure 1"). Mastercard's date was 18 October 2022 [WIDELY REPORTED: https://payabl.com/news/3-ds-1-is-being-discontinued-all-you-need-to-know, processor article, 2022]. South Asia was extended: Visa stopped 3DS1 for domestic transactions in India, Bangladesh, Nepal, Bhutan, Maldives and Sri Lanka on 16 November 2023, Mastercard in India and Bangladesh the same day; Bancontact on 30 June 2024 [VERIFIED: Adyen 3DS-for-regulation page].

### 4.4 Liability shift

- General rule (Adyen): "if a shopper successfully completes a 3D Secure 2 challenge authentication flow, the liability for fraudulent chargebacks shifts from you to the card issuer... In some regions, card schemes may grant liability shift after a successful frictionless flow." Both flows result in a liability shift under Adyen's Dynamic 3DS description [VERIFIED: Adyen 3DS-for-regulation page and https://docs.adyen.com/risk-management/dynamic-3d-secure.md, n.d., accessed 2026-11].
- Visa specifics from Adyen's table: liability shift applies to a 3DS2 transaction "regardless of whether the issuer supports 3D Secure 2" in the EU since 14 March 2020, APAC/MEA since 18 April 2020, the US since 31 August 2020; "For Visa transactions, the chargeback protection is valid for 90 days" [VERIFIED: same page] (the dated rows are 6 years old; the page is live).
- Mastercard specifics: no shift for "PSD2 SCA out-of-scope transactions that were not authenticated with 3D Secure 2" or where "merchant or acquirer requests for a PSD2 exemption and the issuer grants an exemption"; shift applies where the "issuing bank applies a PSD2 exemption without the merchant or acquirer requesting for it" [VERIFIED: same page].
- Stripe says the same in one line: "When the customer's bank approves an exemption request, liability shift for fraudulent transactions doesn't apply" [VERIFIED: Stripe exemptions page]. Liability shift covers fraud disputes only: "the liability for any fraud-related disputes for that payment typically shifts from the seller to the issuer" [VERIFIED: https://docs.stripe.com/radar/rules.md].

### 4.5 Data-only flows, standalone authentication and delegated authentication

- **Data-only (EMVCo: Data Share Only)**. Adyen: "you use the same 3D Secure 2 infrastructure, but only to share shopper data with Visa or Mastercard directly. The card schemes then handle the risk evaluation... shoppers will **not** be presented with a 3D Secure 2 challenge. This also means that there is no liability shift"; "available for Visa and Mastercard outside PSD2 SCA regulated markets" [VERIFIED: https://docs.adyen.com/online-payments/3d-secure/data-only.md, n.d., accessed 2026-11]. Stripe: "Data Only is an optimization available to Authorization Boost merchants"; "Stripe's AI model determines when a Data Only flow is likely to improve authorization outcomes and applies it automatically"; Mastercard's variant, Identity Check Insights, is offered by Stripe "in the EEA and UK only"; from API version `2026-09-30.endive` the charge shows `three_d_secure.result = data_share_only` [VERIFIED: https://docs.stripe.com/payments/3d-secure/data-only.md and the exemptions page, n.d., accessed 2026-11].
- **Visa DCAP** (Digital Commerce Authentication Program) rewards sending IP, device ID, billing address, email and phone with authentication; "In the United States and Canada, Visa has introduced specific interchange programs for transactions that qualify for DCAP, with additional benefits when DCAP is combined with network tokens" [VERIFIED: Stripe data-only page]. Adyen: DCAP "applies only to merchants in the United States and Canada" [VERIFIED: Adyen data-only page].
- **Standalone authentication** (authenticate here, authorize elsewhere). Stripe: "run EMV 3D Secure authentication independently from payment authorization... authenticate on Stripe while processing payments with any payment service provider"; supports 3RI (requestor-initiated) and non-payment authentication; Visa, Mastercard, American Express, Discover, Cartes Bancaires; all card countries "except Malaysia and Thailand" [VERIFIED: Stripe standalone page]. Adyen: "you make a payment request that specifies only authentication... you receive the 3D Secure 2 authentication data which you can use to authorize the payment with Adyen or another PSP"; Advanced flow only [VERIFIED: https://docs.adyen.com/online-payments/3d-secure/standalone-authentication.md, n.d., accessed 2026-11].
- **The reverse** (authenticate elsewhere, authorize here). Stripe "Import 3D Secure results" for travel aggregators and third-party 3DS providers, in a listed set of countries [VERIFIED: https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md, n.d., accessed 2026-11]. Adyen "Authorization-only: Use a third-party 3D Secure 2 provider, and perform the authorization request with Adyen" [VERIFIED: Adyen 3DS overview].
- **Delegated authentication** in the strict PSD2 sense (the issuer delegates SCA to a merchant or wallet) is not documented as a merchant-facing product by either company. What exists in 2026 is scheme-run delegation: scheme passkeys and Google SPA at Adyen (section 3.6), where the cardholder authenticates to the network or to Google instead of the issuer after a first issuer-verified step [ASSUMPTION/JUDGEMENT: classification is the analyst's]. Nothing public found for Stripe on delegated authentication for card acquiring (searched the 3DS documentation set).

### 4.6 Authentication mandates outside the EEA

| Market | Rule as documented | Source |
| --- | --- | --- |
| UK | SCA under "the Payment Services Regulations 2017"; Stripe's low-value and TRA amounts in GBP (25, 85, 220, 440) | Adyen 3DS overview; Stripe exemptions page [VERIFIED] |
| India | "banks are required to perform authentication on all domestic ecommerce transactions"; card-on-file must be network or issuer tokens | Adyen 3DS-for-regulation page; Stripe India page [VERIFIED] |
| Japan | "all online credit card payments in Japan will require Strong Customer Authentication (SCA) for credit cards processed over Japan acquiring connections, effective April 01, 2025" (Credit Card Security Guidelines 5.0); customer-initiated only; wallets excluded | https://docs.adyen.com/industries/markets/japan/credit-card-security-guidelines-compliance-guide.md [VERIFIED, n.d., accessed 2026-11]; Stripe: "by the end of March 2025" [VERIFIED: https://stripe.com/resources/more/3d-secure-mandatory-for-ecommerce-in-japan, n.d.] |
| Australia | AusPayNet CNP framework: SCA on all non-exempt CNP transactions after exceeding, "for two consecutive quarters", both "More than AUD 50,000 in fraud losses" and a "Fraud-to-sales ratio of 0.2% or above" | https://docs.adyen.com/online-payments/auspaynet-compliance-guide.md [VERIFIED, n.d., accessed 2026-11] |
| Malaysia | "issuing banks may require authentication on their BINs, otherwise, authorisation rates will be low" | Adyen 3DS-for-regulation page [VERIFIED] |
| Nigeria, South Africa, Singapore | Listed by Adyen as markets "with existing regulations that require 3D Secure implementation" | Same page [VERIFIED] |
| US, Canada | No mandate; data-only and DCAP incentives instead | Sections 4.5, 3.3 |

- The UK e-commerce SCA enforcement date (14 March 2022) is industry knowledge; the FCA's SCA page no longer states it, and its change log records "21/03/2022: Information changed removed applying SCA to e-commerce" [VERIFIED for the change-log line: https://www.fca.org.uk/firms/strong-customer-authentication, n.d., accessed 2026-11] [ASSUMPTION/JUDGEMENT for the date].
- In Japan, Adyen "can exempt **CardOnFile** transactions from strong customer authentication (SCA) based on our risk assessment powered by machine learning" [VERIFIED: Adyen Japan guide]. A newer version 6.0 of the guidelines (March 2025) is reported by other processors but was not verified [WIDELY REPORTED: search excerpt of a Checkout.com article, 2025].

### 4.7 PSD3 and the Payment Services Regulation: status on 17 November 2026 ⚠

- **Official status**: procedure 2023/0210(COD) (the Regulation, PSR) is at "Awaiting Parliament 2nd reading". Key events: proposal published 28 June 2023 (COM(2023)0367); Parliament first-reading decision 23 April 2024; "Approval in committee of the text agreed at early 2nd reading interinstitutional negotiations" 5 May 2026; "Council position published" 5 November 2026 (08543/1/2026); "Committee referral announced in Parliament, 2nd reading" 12 November 2026; "Indicative plenary sitting date, 2nd reading" **14 December 2026** [VERIFIED: https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210(COD), n.d., accessed 2026-11-17]. The Directive (PSD3), 2023/0209(COD), is at the same stage with the same dates (Council position 08535/1/2026) [VERIFIED: https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0209(COD), accessed 2026-11-17].
- **So, as of this brief, neither text is adopted, published in the Official Journal or in force.**
- The final compromise texts were published by the Council on 23 April 2026, after the provisional agreement announced in November 2025 [VERIFIED: https://www.algoodbody.com/insights-publications/psd-3-psr-final-compromise-texts-published, law-firm note, published 2026-04-24].
- **Expected timing** (Adyen, 12 October 2026): "Publication in the Official Journal is expected in December 2026, and the rules enter into force 20 days later. PSR applies 21 months after entry into force, with Verification of Payee applying at 27 months, and PSD3 must be transposed into national law on the same 21-month timeline. A December 2026 publication points to around late 2028 for general application" [VERIFIED: https://www.adyen.com/knowledge-hub/psd3, published 2026-10-12].
- **What changes for SCA** (Adyen's reading of the compromise text; the text itself was not read): "SCA isn't going anywhere... The only key difference is that two biometric checks can now fulfill the requirement as well as two separate categories. Merchant-initiated transactions for recurring billing also stay as they are." Exemptions: "The contactless exemption could rise from €50"; MOTO "will continue but regulation will be tightened"; "The transaction risk analysis exemption remains but its qualifying conditions could change." Detail waits for EBA technical standards in 2027–2028; "Whether a specific passkey flow qualifies as SCA will depend on the EBA's technical standards" [VERIFIED: same Adyen article].
- **What changes for fraud liability** (same source): an "automatic refund right for some cases of impersonation or spoofing fraud", with liability on the customer's bank; "Issuing banks can seek to recoup losses from acquirers"; "acquirers now face their own obligation to monitor transactions for fraud risk"; "Card schemes, technical service providers such as wallet providers, and payment gateways can also be held liable if they fail to apply SCA correctly"; PSPs get "a clearer legal basis to share specified fraud-related data with each other" [VERIFIED: same article].
- **Scheme fee transparency** (relevant to section 3.3): schemes must "unbundle, and disclose all fees charged to acquirers", give "at least six months' notice of any fee changes", and "maintain a single, public EU repository detailing their scheme rules and fee schedules"; a delegated regulation is "expected during 2027" [VERIFIED: same article].
- **Stripe**: nothing found on PSD3/PSR in the documentation set read; not searched on stripe.com beyond that (see brief `companies`).

### 4.8 Stripe: how authentication decisions are exposed

- **Default is automatic**: "Stripe triggers 3DS automatically if mandated by regulations such as Strong Customer Authentication in Europe, industry guidelines such as the Credit Card Security Guidelines in Japan, if requested by an issuer with a soft decline code, or if certain Stripe optimizations apply" [VERIFIED: https://docs.stripe.com/payments/3d-secure/authentication-flow.md].
- **Decision inputs, in order**: "Stripe assesses if the transaction supports and requires 3DS based on regulatory mandates, Radar rules, manual API requests, issuer soft declines, and other criteria." If not required, "Stripe attempts the charge... If requested by the issuer with a soft decline, we automatically reattempt and continue as if required" [VERIFIED: same page].
- **Exemptions are requested for the merchant**: "Stripe requests applicable SCA exemptions on your behalf." Low value under EUR 30 (GBP 25) with the EUR 100 (GBP 85) / five-transaction counters. TRA: "UK and Swiss merchants have access to TRA exemptions for qualifying low risk transactions up to 220 GBP. EEA merchants... up to 250 EUR"; the limit "depends on the Stripe overall fraud rates and your access to the Stripe authentication offerings" [VERIFIED: Stripe exemptions page] ⚠. A EUR 250 limit implies Stripe's reported fraud rate sits at or below the RTS's 0.06% band [ASSUMPTION/JUDGEMENT].
- **Radar rules** add requests on top: the built-in action is "Request 3D Secure", for example `Request 3D Secure if :risk_level: != 'normal' and :amount_in_usd: > 25`; attributes for follow-up rules are `is_3d_secure`, `is_3d_secure_authenticated` and `has_liability_shift`; custom 3DS rules need the paid Radar tier. "The default method to trigger 3DS is using Radar to dynamically request 3D Secure based on risk level and other requirements" [VERIFIED: https://docs.stripe.com/radar/rules.md and authentication-flow page].
- **API override**: `payment_method_options[card][request_three_d_secure]` set to `any` ("preference for a `frictionless` flow") or `challenge`. "Triggering 3DS manually is for advanced users integrating Stripe with their own fraud engine." "Stripe's mandatory authentication rules run automatically, regardless of whether or not you manually request 3DS" [VERIFIED: authentication-flow page].
- **Where the state lives**: the PaymentIntent moves to `requires_action`; Stripe.js shows the challenge "in a pop-up modal", or the merchant redirects or uses an iframe; mobile SDKs render native challenge screens [VERIFIED: same page and SCA readiness page].
- **Observability**: `authentication_flow` on `payment_method_details.card.three_d_secure`; the standalone API returns "the full 3DS protocol output, including the authentication result, Electronic Commerce Indicator (ECI), Directory Server (DS) Transaction ID, and the cryptogram" [VERIFIED: authentication-flow and standalone pages].

### 4.9 Adyen: how authentication decisions are exposed

- **Three named layers** [VERIFIED: https://docs.adyen.com/online-payments/authentication.md, n.d., accessed 2026-11]:
  - **Dynamic 3D Secure and risk-based authentication**: "Evaluates transaction risk to determine whether to request a challenge."
  - **Authentication Engine**: "Selects the most appropriate authentication method, such as 3D Secure 2, scheme passkey authentication, or Google Secure Payment Authentication (Google SPA). It considers device capabilities, risk signals, issuer data, real-time performance data, and local regulatory requirements."
  - **Adyen Uplift**: "Analyzes authorization rates and payment performance, then provides targeted recommendations."
- **Outcome by risk** (Adyen's table): low risk goes to "PSD2 exemption", "Frictionless 3D Secure 2" or "3D Secure 2 data-only"; high risk goes to "the challenge flow"; "Very high risk transactions are declined entirely" [VERIFIED: same page].
- **Compliance floor**: "we always authenticate transactions with 3D Secure if this is required by regulations such as PSD2... we do not trigger 3D Secure for out-of-scope transactions, or when the issuing bank does not enforce 3D Secure. For transactions within the scope of PSD2, we also handle requesting exemptions." "By default Adyen sends a request for the most suitable exemption type on your behalf", reported in `additionalData.scaExemptionRequested` [VERIFIED: Dynamic 3DS page; SCA exemptions page].
- **Merchant controls**: a default rule ("**Prefer not**" for new accounts, or "**Always**"); ordered Dynamic 3DS rules ("Rules are evaluated in order, from first to last. If a rule is triggered, the remaining rules are not evaluated"), at company or merchant-account level, optionally triggered by a custom risk rule with the "Check for 3DS" action; request-level overrides [VERIFIED: Dynamic 3DS page].
- **Overrides disable optimization**: sending `authenticationData.attemptAuthentication`, `threeDSRequestorChallengeInd`, `scaExemption` or `threeDSVersion` "overrides Adyen's authentication decisions, reducing our ability to optimize the authentication flow" [VERIFIED: authentication page].
- **Risk-based authentication** (needs Protect premium): "sends transactions that would have been blocked by the machine learning fraud risk rule to 3D Secure 2"; it "increases authentication costs, but leads to more settled transactions" [VERIFIED: Dynamic 3DS page].
- **Risk-based exemptions** ⚠: "From July 2026, Adyen is rolling out risk-based exemptions to select companies using Protect premium"; they are claimed to boost "authorization rates by up to ten percent"; inside PSD2 markets "Adyen uses the Transaction Risk Analysis (TRA) exemption to skip 3D Secure for low-risk transactions" [VERIFIED: same page].
- **Native vs redirect**: native runs "within your website or mobile app"; redirect sends shoppers "to the card issuer's site" and "might lead to lower conversion rates due to technical errors during the redirection". But the Authentication Engine's newer methods need redirect: for scheme passkeys and the optimized flow, "You must set the `nativeThreeDS` to **disabled**" (Sessions flow) or implement redirect 3DS2 (Advanced flow) [VERIFIED: Adyen 3DS overview; authentication page; scheme-passkeys page]. That reverses years of advice to prefer native 3DS2 [ASSUMPTION/JUDGEMENT].
- **Press framing** (22 September 2026): Authenticate "replaces those rules with three machine learning powered decisions on every transaction: whether authentication is needed, which method will perform best, and which data to share". The stated structural advantage: "unlike legacy 3D Secure (3DS) providers, Adyen operates as both the authentication provider and the acquirer. This position allows Authenticate's machine learning... to learn from final authorization outcomes down the funnel, rather than authentication results alone." Customer claims: Too Good To Go "an 11% increase in payment conversion"; Just Eat Takeaway.com "an 12% increase in payment conversion on the eligible traffic" [VERIFIED: https://www.adyen.com/press-and-media/adyen-launches-authenticate-upgrade, published 2026-09-22]. These are customer testimonials in a press release; no methodology [ASSUMPTION/JUDGEMENT].

**Stripe vs Adyen (authentication)**

| Topic | Stripe | Adyen | Difference |
| --- | --- | --- | --- |
| Default behaviour | Automatic 3DS when regulation, issuer soft decline or Stripe optimization requires it | Same floor; default rule "Prefer not" | Equivalent |
| Merchant rule surface | Radar rules (`Request 3D Secure if …`), part of the fraud product; custom rules on the paid tier | Dynamic 3DS rules, a separate ordered rule list, linkable to risk rules | Stripe folds authentication into fraud rules; Adyen keeps a dedicated rule set |
| Per-request override | `request_three_d_secure` = `any` or `challenge` | Several parameters; documented as reducing optimization | Adyen warns against overriding; Stripe calls it "for advanced users" |
| Exemptions | Requested automatically; TRA up to EUR 250 / GBP 220 published | Requested automatically; requested type returned per payment; TRA limit not published | Stripe publishes its TRA ceiling; Adyen exposes the per-transaction exemption |
| Method selection beyond 3DS | None documented | Authentication Engine picks 3DS, scheme passkeys or Google SPA | Adyen only, and in pilot |
| Data-only | Authorization Boost customers; model-applied | Outside PSD2 markets; engine-applied or forced by parameter | Stripe gates by product tier; Adyen by region |
| Standalone 3DS | Yes (3DS up to 2.3.1; 3RI; non-payment) | Yes (Advanced flow only) | Both sell authentication detached from acquiring |
| Stated design argument | — | Authentication provider and acquirer in one, so models train on authorization outcomes | Adyen makes the claim explicitly; Stripe is in the same structural position but does not argue it in the pages read [ASSUMPTION/JUDGEMENT] |

**For readers new to payments**

- **Strong customer authentication (SCA)**: a legal requirement in the EEA and UK that the payer prove identity with two independent factors out of knowledge, possession and inherence.
- **3-D Secure (3DS)**: the card networks' protocol by which the merchant's side sends transaction and device data to the card issuer, which either approves silently (frictionless) or asks the cardholder to confirm (challenge).
- **Exemption**: a legally defined case in which SCA may be skipped, such as a low amount or a low-risk transaction; the party that asks for it usually keeps the fraud liability.
- **Liability shift**: after a successful authentication, the cost of a fraud chargeback moves from the merchant to the card issuer.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Authentication makes payment a two-phase, user-interactive operation. Any API that hides it behind a single synchronous call is lying; both providers model it as a state (`requires_action`; an action returned to the client component) that the client must resolve.
- "Should we authenticate?" is an optimization with three terms: conversion lost to friction, fraud cost if liability stays with the merchant, and scheme fees for unauthenticated or untokenized traffic. Both providers now make that decision by model and expose rules only as constraints.
- The provider that both authenticates and acquires can train on authorization outcomes. A merchant splitting authentication and acquiring across vendors (standalone 3DS) gives that up and must carry ECI, cryptogram and DS transaction ID across the seam itself.
- Exemption capacity is a shared resource: the TRA ceiling depends on the provider's fraud rate across all its merchants, so one merchant's limit can move for reasons outside its control.
- Design for the regulation moving: PSR will not apply before late 2028 on current forecasts, but the EBA standards that decide whether passkeys count as SCA come in between.

---

## Key numbers

| Number | Definition | Source and date |
| --- | --- | --- |
| 31 March 2025 | Date PCI DSS v4.x future-dated requirements (incl. 6.4.3, 11.6.1) became effective; also the date the revised SAQ A took effect | PCI SSC blog, 2024-06-11 and 2025-01-30 |
| 11 June 2024 / 31 December 2024 | PCI DSS v4.0.1 published / v4.0 retired | PCI SSC blog, 2024-06-11 |
| 300+ controls; 1,800+ pages | Stripe's description of the PCI DSS burden when handling card data directly | Stripe PCI guide, n.d. |
| 6 million / 2.5 million | Annual Visa or Mastercard / American Express transactions above which a merchant is Level 1 | Stripe PCI guide, n.d. |
| AES-256 | Encryption of card numbers at rest in Stripe's vault | Stripe security page, n.d. |
| 4096 bits | Minimum PGP key length Stripe requires from a processor receiving exported cards | Stripe PAN export page, n.d. |
| 10 business days | Typical time for Stripe to complete an import after valid data arrives; Adyen: "10 days or more" | Stripe import page, n.d.; Adyen migration page (2019) |
| 10 billion+ tokens; 29% | Visa tokens issued since 2014; share of all Visa-processed transactions using tokens (April 2024) | Visa press release, 2024-06-04 |
| "six-basis point"; "up to 60%" | Visa's stated global approval-rate increase from tokenization; stated fraud-rate reduction | Same release |
| $40 billion; $650 million | Visa's stated incremental e-commerce revenue and fraud saved "in the last year" (CY2023 data, tokenized vs non-tokenized CNP) | Same release |
| 25%; 50% | Share of global e-commerce transactions secured by Mastercard tokenization; year-over-year adoption growth | Mastercard newsroom, 2024-06-11 |
| 2030 | Mastercard's target year for 100% e-commerce tokenization in Europe | Same release |
| 3% | Adyen's average authorization-rate uplift for businesses using network tokenization | Adyen knowledge hub, 2024-09-04 |
| 3.8%; 3.3% | Stripe's average acceptance increase with Authorization Boost (bundle); maximum processing-cost reduction on interchange-plus pricing | Stripe Authorization Boost page, n.d. |
| 2.5 bps | Visa Europe fee on e-commerce PAN authorizations without a network token or 3DS, from 1 October 2023 | Braintree bulletin, 2023 (secondary) |
| EUR 30 / EUR 100 / 5 | Low-value remote exemption: per-transaction cap, cumulative cap, consecutive-transaction cap | RTS 2018/389 Art. 16, published 2018-03-13 |
| EUR 50 / EUR 150 / 5 | Contactless exemption caps | RTS 2018/389 Art. 11 |
| 0.13% / 0.06% / 0.01% | Reference fraud rates for TRA on remote card payments up to EUR 100 / 250 / 500 | RTS 2018/389 Annex |
| EUR 250; GBP 220 | TRA exemption ceiling currently available to Stripe's EEA and UK/Swiss merchants | Stripe exemptions page, n.d. |
| 14 September 2019 | Date the SCA RTS applied | RTS 2018/389 Art. 38 |
| 15 October 2022 | Visa ended support for 3-D Secure 1.0.2 | Visa bulletin, 2021-02-04 |
| 2.3.1 | Highest EMV 3DS version Stripe states it supports; 2.4.0.0 in draft since 4 November 2026 | Stripe standalone page; EMVCo |
| 90 days | Validity of Visa chargeback protection after 3DS authentication | Adyen 3DS-for-regulation page, n.d. |
| AUD 50,000 and 0.2% | AusPayNet merchant fraud thresholds (both, two consecutive quarters) that trigger mandatory SCA | Adyen AusPayNet guide, n.d. |
| 1 April 2025 | Effective date of mandatory 3DS for online credit card payments in Japan | Adyen Japan guide, n.d. |
| 14 December 2026 | Indicative European Parliament plenary date for the second reading of PSR and PSD3 | EP Legislative Observatory, accessed 2026-11-17 |
| 21 months / 27 months | Application of PSR after entry into force / Verification of Payee | Adyen knowledge hub, 2026-10-12 |
| 11%; 12% | Conversion increases Adyen attributes to Authenticate at Too Good To Go and Just Eat Takeaway.com (eligible traffic) | Adyen press release, 2026-09-22 |

---

## Open questions / not verifiable

These are candidates for the book's "where the evidence stops" statements.

1. **Stripe's vault design.** Beyond one paragraph (separate AWS environment, no shared credentials, AES-256, keys on separate machines, internal tokenization, static allowlist of recipients), nothing is public: no key-management design, HSM statement, rotation policy, region count, or description of how internal services exchange tokens for plaintext.
2. **Adyen's vault design.** Adyen publishes less than Stripe: a name (Adyen Vault), regional storage, and "keys are managed in a secure and compliant manner". The only engineering article (2019) concerns PII in the data platform.
3. **Adyen's export process.** No public page describes how a merchant leaving Adyen gets card data transferred, or what Adyen requires of the recipient. A former help article is no longer served.
4. **Whether Adyen provisions network tokens by default.** Two Adyen pages disagree (automatic vs. ask Support).
5. **Visa's approval uplift.** The 2024 press release says "six-basis point"; common citations say roughly six percent. Visa's underlying methodology is not public; neither figure is a controlled comparison.
6. **Network token fees.** No network fee schedule was read. All fee figures are from a processor's bulletins and a consultancy; amounts vary by region and change twice a year.
7. **EMVCo role definitions and 3DS message flow** were not read from the specifications. v2.4 of the tokenisation framework (July 2026) may have changed terminology.
8. **Stripe and scheme passkeys / Click to Pay.** No Stripe statement verified. Whether the Payment Element supports Click to Pay or Visa/Mastercard passkeys in November 2026 is open.
9. **Delegated authentication.** Neither company documents issuer-delegated SCA as a merchant product; scheme passkeys are the nearest thing and are in pilot.
10. **TRA ceilings at Adyen** and the fraud rates behind either company's TRA use are not published.
11. **PSD3/PSR final wording** on SCA factors, exemption thresholds, acquirer monitoring duties and the liability of "technical service providers" was not read; the brief relies on Adyen's summary. Adoption is forecast, not done.
12. **Stripe Terminal and PCI P2PE**: no listing found; the brief `acquiring` should check the PCI SSC P2PE solutions list.
13. **UK e-commerce SCA date, India card-storage deadline, Japan guidelines 6.0**: not verified from regulators in this session.
14. **How many merchants** at either company run network tokens, standalone 3DS or forwarding: no adoption figures are public.

---

## Source list

**PCI SSC**

- "Just Published: PCI DSS v4.0.1", PCI SSC blog (Alicia Malone), 2024-06-11, https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 — version dates, effective date of future-dated requirements.
- "Important Updates Announced for Merchants Validating to Self-Assessment Questionnaire A", PCI SSC blog (Alicia Malone), 2025-01-30, https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a — SAQ A change, who sets validation requirements.
- FAQ 1588 "How does an e-commerce merchant meet the SAQ A eligibility criteria for scripts?", PCI SSC, n.d., https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/how-does-an-e-commerce-merchant-meet-the-saq-a-eligibility-criteria-for-scripts/ — iframe vs redirect, two ways to confirm.
- PCI DSS standard page, PCI SSC, n.d., https://www.pcisecuritystandards.org/standards/pci-dss/ — who the standard applies to.
- PCI DSS v4.0 Resource Hub, PCI SSC blog, n.d., https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub — v3.2.1 retirement date.
- "New Information Supplement: Payment Page Security and Preventing E-Skimming", PCI SSC blog, n.d., https://blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming — existence of the guidance.

**Stripe**

- "Security at Stripe", Stripe docs, n.d., https://docs.stripe.com/security.md — PCI Level 1, Card Data Vault isolation, AES-256, mTLS.
- "Integration security guide", Stripe docs, n.d., https://docs.stripe.com/security/guide.md — shared responsibility, storable data, CSP directives, third-party script warning.
- "PCI DSS compliance guide", Stripe, n.d., https://stripe.com/guides/pci-compliance — levels, SAQ per integration.
- Stripe docs index, n.d., https://docs.stripe.com/llms.txt — network token and raw-PAN guidance; absence of Click to Pay / passkey / P2PE pages.
- "Tokens" API reference, n.d., https://docs.stripe.com/api/tokens.md — single-use tokens.
- "Payment Methods" guide, n.d., https://docs.stripe.com/payments/payment-methods.md — reusable vs single-use.
- "Confirmation Tokens" API reference and "Migrate to Confirmation Tokens", n.d., https://docs.stripe.com/api/confirmation_tokens.md, https://docs.stripe.com/payments/payment-element/migration-ct.md — ConfirmationToken purpose.
- "Request a payment data export", n.d., https://docs.stripe.com/get-started/data-migrations/pan-export.md — export conditions and format.
- "Import payment data to Stripe", n.d., https://docs.stripe.com/get-started/data-migrations/pan-import.md — import process and timing.
- "Forward card details to third-party API endpoints", n.d., https://docs.stripe.com/payments/vault-and-forward.md — Vault and Forward API.
- "Orchestration", n.d., https://docs.stripe.com/payments/orchestration.md — private preview scope.
- "What is a token vault?", Stripe resources, n.d., https://stripe.com/resources/more/token-vault — one sentence on Vault and Forward with network tokenization.
- "Understanding the benefits of network tokens", Stripe guide, n.d., https://stripe.com/guides/understanding-benefits-of-network-tokens — automatic provisioning, PAN redundancy, latency, countries.
- "Payments optimization" (Authorization Boost), n.d., https://docs.stripe.com/payments/analytics/optimization.md — features, attribution method, fee notes.
- "Authorization Boost", Stripe product page, n.d., https://stripe.com/authorization-boost — 3.8% and 3.3% claims.
- "India network tokenization", n.d., https://docs.stripe.com/india-network-tokenization.md — RBI regime as Stripe applies it.
- "3D Secure authentication" overview, n.d., https://docs.stripe.com/payments/3d-secure.md — markets with mandates.
- "Authenticate with 3D Secure" (authentication flow), n.d., https://docs.stripe.com/payments/3d-secure/authentication-flow.md — triggers, API override, UI.
- "SCA exemptions", n.d., https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions.md — exemptions, TRA limits, MIT.
- "Data Only", n.d., https://docs.stripe.com/payments/3d-secure/data-only.md — Data Share Only, DCAP, API change of 2026-09-30.
- "Standalone 3DS", n.d., https://docs.stripe.com/payments/3d-secure/standalone-three-d-secure.md — standalone API, 3DS 2.3.1.
- "Import 3D Secure results", n.d., https://docs.stripe.com/payments/payment-intents/three-d-secure-import.md — external 3DS.
- "Radar rules", n.d., https://docs.stripe.com/radar/rules.md — Request 3D Secure rules and attributes.
- "Strong Customer Authentication readiness", n.d., https://docs.stripe.com/strong-customer-authentication.md — SCA dates, off-session handling.
- "3D Secure 2.0 mandatory for e-commerce sites in Japan", Stripe resources, n.d., https://stripe.com/resources/more/3d-secure-mandatory-for-ecommerce-in-japan — Japan deadline.

**Adyen**

- "PCI DSS compliance guide", Adyen docs, n.d. (metadata 2024-02-27), https://docs.adyen.com/development-resources/pci-dss-compliance-guide.md — Level 1, SAQ per integration, risk labels.
- "Self-Assessment Questionnaire A eligibility", n.d., https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility.md — SAQ A criteria and the 2025 change.
- "Script security for ecommerce", n.d., https://docs.adyen.com/development-resources/pci-dss-compliance-guide/script-security.md — 6.4.3, 11.6.1, 3DS exemption, CSP.
- "Adyen's E2EE and P2PE PCI security", n.d., https://docs.adyen.com/development-resources/e2ee-p2pe-comparison.md — terminal encryption options.
- "Tokenization", n.d., https://docs.adyen.com/online-payments/tokenization.md — Adyen Vault, shopper reference, Token Groups, security statement.
- "Create tokens", n.d., https://docs.adyen.com/online-payments/tokenization/create-tokens.md — webhook delivery, recurringProcessingModel.
- "Forward payment details", n.d., https://docs.adyen.com/online-payments/tokenization/forward-payment-details.md — Forward API, vault region.
- "Tokenization" (point of sale), n.d., https://docs.adyen.com/point-of-sale/recurring-payments.md — in-person tokens reused online.
- "Import data from another payment provider", metadata 2019-12-06, https://docs.adyen.com/development-resources/migrating-payment-data.md — import process.
- "Tokenize" product page, n.d., https://www.adyen.com/uplift/tokenize — "universal token vault", Forward positioning.
- "Securing your personal data via tokenization", Adyen (Sriram Kunjathur), 2019-10-01, https://www.adyen.com/en_GB/knowledge-hub/securing-your-personal-data-via-tokenization — HSM-backed PII tokenization.
- "Network tokenization", n.d., https://docs.adyen.com/online-payments/network-tokenization.md — two modes, fallback data, co-badged routing.
- "PAN fallback for network tokens", n.d., https://docs.adyen.com/online-payments/network-tokenization/pan-fallback.md — merchant-managed fallback.
- "Optimize card payments with network tokenization", Adyen knowledge hub, 2024-09-04, https://www.adyen.com/knowledge-hub/network-tokenization — requestor flow, 3% uplift, fees.
- "Adyen first to launch Real Time Account Updater with Visa in Europe", 2022-09-13, https://www.adyen.com/press-and-media/adyen-first-to-launch-real-time-account-updater-with-visa-in-europe — account updater history.
- "Apple Pay", n.d., https://docs.adyen.com/payment-methods/apple-pay.md — network tokenization and liability shift.
- "Click to Pay", n.d., https://docs.adyen.com/payment-methods/cards/click-to-pay.md — support and limits.
- "Authentication", n.d., https://docs.adyen.com/online-payments/authentication.md — three layers, risk table, overrides.
- "Scheme passkeys", n.d., https://docs.adyen.com/online-payments/authentication/scheme-passkeys.md — pilot status and limits.
- "Google Secure Payment Authentication", n.d., https://docs.adyen.com/online-payments/authentication/google-secure-payment-authentication.md — limited availability.
- "Dynamic 3D Secure", n.d., https://docs.adyen.com/risk-management/dynamic-3d-secure.md — rules, risk-based authentication and exemptions.
- "3D Secure 2 authentication", n.d., https://docs.adyen.com/online-payments/3d-secure.md — native vs redirect, flows.
- "3D Secure for regulation compliance", n.d., https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance.md — markets, dates, liability shift tables.
- "Data-only flow", n.d., https://docs.adyen.com/online-payments/3d-secure/data-only.md — data-only and DCAP.
- "Standalone authentication", n.d., https://docs.adyen.com/online-payments/3d-secure/standalone-authentication.md — authentication-only requests.
- "SCA exemptions", n.d., https://docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/sca-exemptions.md — exemptions, liability, scheme support.
- "Credit Card Security Guidelines" (Japan), n.d., https://docs.adyen.com/industries/markets/japan/credit-card-security-guidelines-compliance-guide.md — Japan mandate.
- "AusPayNet compliance guide", n.d., https://docs.adyen.com/online-payments/auspaynet-compliance-guide.md — Australian thresholds.
- "Adyen Launches First-to-Market Upgrade to Authenticate", 2026-09-22, https://www.adyen.com/press-and-media/adyen-launches-authenticate-upgrade — Authenticate decisions and claims.
- "Adyen Rolls Out Visa Payment Passkey", 2026-10-29, https://www.adyen.com/press-and-media/adyen-visa-payment-passkey — UK rollout, 2027 expansion.
- "PSD3 and PSR: what businesses need to know", Adyen knowledge hub, 2026-10-12, https://www.adyen.com/knowledge-hub/psd3 — PSD3/PSR content and timing.

**Standards bodies and networks**

- "EMV Payment Tokenisation", EMVCo, n.d., https://www.emvco.com/emv-technologies/payment-tokenisation/ — definition, v2.4 (2026-07-09), TSP and BIN Controller registries, PAR.
- "EMV 3-D Secure", EMVCo, n.d., https://www.emvco.com/emv-technologies/3-d-secure/ — definition, 2.4 draft (2026-11-04).
- "EMVCo Updates EMV 3DS Specifications…" (2.3.1 press release), EMVCo, 2022-09-29, https://emvco.com/wp-content/uploads/2022/11/EMV-3DS-2.3.1-press-release.pdf — 2.3.1 content and date.
- "Enhancing the EMV 3-D Secure Specifications", EMVCo, 2023-05-19, https://www.emvco.com/knowledge-hub/enhancing-the-emv-3-d-secure-specifications/ — 2.3.1.1.
- "Visa Token Service", Visa, n.d., https://usa.visa.com/products/visa-token-service.html — VTS description.
- "Visa Issues 10 Billionth Token…", Visa, 2024-06-04, https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20701.html — token statistics and claims.
- "Visa Reinvents the Card…", Visa, 2024-05-15, https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20686.html — Visa Payment Passkey Service.
- "Visa Will Discontinue Support of 3-D Secure 1.0.2", Visa Business News, 2021-02-04, https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-will-discontinue-support-of-3d-secure.pdf — 3DS1 sunset.
- "Mastercard reimagines online checkout; commits to reaching 100% e-commerce tokenization by 2030 in Europe", Mastercard, 2024-06-11, https://newsroom.mastercard.com/news/press/2024/june/mastercard-reimagines-online-checkout-commits-to-reaching-100-e-commerce-tokenization-by-2030-in-europe/ — 2030 vision, 25% share.
- Google Pay API web tutorial, Google, n.d., https://developers.google.com/pay/api/web/guides/tutorial — PAN_ONLY vs CRYPTOGRAM_3DS.

**Law and regulators**

- Directive (EU) 2015/2366 (PSD2), 2015-11-25, http://publications.europa.eu/resource/celex/32015L2366 — Articles 4(30), 74, 97.
- Commission Delegated Regulation (EU) 2018/389 (SCA RTS), 2018-03-13, http://publications.europa.eu/resource/celex/32018R0389 — Articles 11–18, 20, Annex, application date.
- European Parliament Legislative Observatory, procedures 2023/0210(COD) and 2023/0209(COD), accessed 2026-11-17, https://oeil.secure.europarl.europa.eu/oeil/en/procedure-file?reference=2023/0210(COD) — PSR/PSD3 status and dates.
- RBI circular "Tokenisation – Card Transactions: Permitting Card-on-File Tokenisation (CoFT) Services", 2021-09-07, https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12159&Mode=0 — issuers as TSPs, CoF tokenisation.
- FCA "Strong Customer Authentication", n.d., https://www.fca.org.uk/firms/strong-customer-authentication — change log only.

**Secondary**

- A&L Goodbody, "PSD 3 & PSR: final compromise texts published", 2026-04-24, https://www.algoodbody.com/insights-publications/psd-3-psr-final-compromise-texts-published — law-firm note on publication date.
- PayPal/Braintree network updates, Visa Fall 2023 and Fall 2026, https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23 and https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/fall/2026 — processor bulletins on token-related fees.
- CMSPI, "April 2026 U.S. Network Fee Updates", 2026, https://cmspi.com/april-2026-u-s-network-fee-updates-3-billion-estimated-cost-impact-for-merchants/ — consultancy estimate of fee changes; "6%" citation.
- payabl, "3DS 1 is being discontinued", 2022, https://payabl.com/news/3-ds-1-is-being-discontinued-all-you-need-to-know — Mastercard 3DS1 date (search excerpt).
- ID Tech Wire, "Checkout.com and Adyen Begin Rolling Out Visa Payment Passkey to Merchants", 2026, https://idtechwire.com/checkout-com-and-adyen-begin-rolling-out-visa-payment-passkey-to-merchants/ — headline only.
