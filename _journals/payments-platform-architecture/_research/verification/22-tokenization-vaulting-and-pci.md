# Verification — 22-tokenization-vaulting-and-pci

Verified 17 November 2026. Every source below was fetched in this session (curl with a generic research user agent, `.md` variants for `docs.stripe.com` and `docs.adyen.com`; `stripe.com/guides/*` served a localized copy, so the English `en-*` variant was read). Quotations were compared with the fetched text by script (whitespace, markdown and typographic quotes normalized) and the misses were read by hand.

Short source names: **S-SEC** docs.stripe.com/security · **S-PCI** stripe.com/guides/pci-compliance · **S-GUIDE** docs.stripe.com/security/guide · **S-TOK** docs.stripe.com/api/tokens · **S-PM** docs.stripe.com/payments/payment-methods · **S-CARD** docs.stripe.com/api/cards/object · **S-NT** stripe.com/guides/understanding-benefits-of-network-tokens · **S-CO** docs.stripe.com/payments/checkout · **S-RADAR** docs.stripe.com/radar/optimize-risk-factors · **S-IMP** docs.stripe.com/get-started/data-migrations/pan-import · **S-EXP** docs.stripe.com/get-started/data-migrations/pan-export · **S-VF** docs.stripe.com/payments/vault-and-forward · **A-PCI** docs.adyen.com/development-resources/pci-dss-compliance-guide · **A-SAQA** …/pci-dss-compliance-guide/saq-a-eligibility · **A-SCRIPT** …/pci-dss-compliance-guide/script-security · **A-CARD** docs.adyen.com/payment-methods/cards/web-component · **A-TOK** docs.adyen.com/online-payments/tokenization · **A-CREATE** …/tokenization/create-tokens · **A-FWD** …/tokenization/forward-payment-details · **A-IMP** docs.adyen.com/development-resources/migrating-payment-data · **A-KH** adyen.com/en_GB/knowledge-hub/securing-your-personal-data-via-tokenization · **P-DSS** pcisecuritystandards.org/standards/pci-dss/ · **P-401** blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1 · **P-SAQA** blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a · **P-FAQ** pcisecuritystandards.org/faqs/1588/ · **P-ESK** blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | SAQ A since 31 March 2025: quote "confirm their site is not susceptible to attacks from scripts…" (scene, key points) | P-SAQA | confirmed | Attribution added in the sentence (announcement of 30 January 2025) |
| 2 | PCI DSS applies to: quote "Entities that store, process, or transmit cardholder data (CHD)… (CDE)" | P-DSS | confirmed | — |
| 3 | PCI SSC formed by five card brands | S-PCI (Visa, Mastercard, American Express, Discover, JCB, 2006) | confirmed | Sourced through Stripe's summary, as the Sources entry says |
| 4 | v4.0.1 published 11 June 2024 | P-401 (posted 11 Jun 2024) | confirmed | — |
| 5 | v4.0.1 the only active version since 31 December 2024 | P-401 ("v4.0 will be retired on 31 December 2024") | confirmed | — |
| 6 | "might be required to meet each of the 300+ security controls in PCI DSS" | S-PCI | confirmed | — |
| 7 | "Compliance validation requirements are set by brands, acquirers, payment facilitators, etc." (30 January 2025) | P-SAQA (posted 30 Jan 2025) | confirmed | — |
| 8 | Level 1 = more than 6 million Visa or 6 million Mastercard transactions; yearly QSA-led Report on Compliance | S-PCI | confirmed | Stripe also lists 2.5 million American Express; not added |
| 9 | Smaller merchants file an SAQ that depends on the integration | S-PCI ("Level 2-4 users… different SAQ types depending on your payment integration method") | confirmed | — |
| 10 | Adyen: requirements "may differ from what other acquirers require" | A-PCI | confirmed | — |
| 11 | Adyen PCI guide dated "last modified February 2024" | A-PCI front matter | corrected | Ruling 30: now "n.d., accessed November 2026" in text, table and Sources |
| 12 | SAQ A is for "merchants with account data functions completely outsourced to PCI DSS validated and compliant third parties" | P-SAQA | confirmed | Sentence now names the council post |
| 13 | Council's SAQ documents not readable | docs-prv.pcisecuritystandards.org SAQ PDFs (HTTP 403 for SAQ A, A-EP, D) | confirmed | The page's "I could not read" still holds |
| 14 | Table: SAQ A when every card input is in a page or frame the provider serves (both guides) | S-PCI, A-PCI | confirmed | — |
| 15 | Table: SAQ A-EP for Stripe.js v2 own form | S-PCI | confirmed | — |
| 16 | Table: SAQ D for raw card numbers to the API (both guides) | S-PCI, A-PCI | confirmed | — |
| 17 | "Checkout and Stripe.js and Elements host all card data collection inputs within an iframe served from Stripe's domain (not yours)…" | S-PCI | confirmed | — |
| 18 | At Stripe the frame sends the number directly to Stripe | S-GUIDE ("transmit payment information directly to Stripe without it passing through your servers") | confirmed | — |
| 19 | Adyen: "the cardholder data is encrypted on your shopper's browser. You do not have access to decryption keys" | A-PCI | confirmed | — |
| 20 | Adyen: merchant server sends `encryptedCardNumber` to `/payments` | A-CARD (server-side request with API key) | confirmed | — |
| 21 | Adyen mobile: "encrypted in the app, sent to your server, and then transmitted to Adyen" | A-PCI | confirmed | Quote confirmed, then cut from the page for length; the web evidence (row 20) carries the point |
| 22 | Adyen asks SAQ A for Drop-in / Components | A-PCI | confirmed | — |
| 23 | Stripe token: "a nonsensitive string that can be used only by the business that collected the card" | S-NT | confirmed | — |
| 24 | "You can't store or use tokens more than once." | S-TOK | confirmed | Source now named in the sentence |
| 25 | PaymentMethod "contains reusable payment details"; attached to a Customer | S-PM | confirmed | Source now named; "It arrives in the API response" dropped (not stated on the cited page) |
| 26 | `fingerprint` "Uniquely identifies this particular card number"; same card across customers | S-CARD | confirmed | — |
| 27 | Adyen: "When you store a shopper's payment details, you must store the token with a unique shopper reference" | A-TOK | confirmed | — |
| 28 | Adyen token is `storedPaymentMethodId` | A-CREATE | confirmed | — |
| 29 | "The token does not arrive in the payment response" | A-CREATE | corrected | Source: "For some payment methods, the API response includes the token in `additionalData.tokenization.storedPaymentMethodId`… We recommend to always get the token from the recurring.token.created webhook." Text, comparison table, advice paragraph and spec p15 changed |
| 30 | "get the unique identifier and other information about the token from the recurring.token.created webhook" | A-CREATE | confirmed | Sentence now names the page |
| 31 | "By default, shopper references and tokens can only be used with one merchant account" | A-TOK | confirmed | — |
| 32 | Stripe: "the card type, the last four digits of the card, and the expiration date"; "This information isn't subject to PCI compliance" | S-GUIDE | confirmed | — |
| 33 | "Dedicated card technology"; separate hosting, no shared credentials (long quote) | S-SEC | confirmed | — |
| 34 | "A dedicated team manages our CDV in an isolated Amazon Web Services (AWS) environment… review access quarterly." | S-SEC | confirmed | — |
| 35 | CDV covered by the PCI Service Provider Level 1 audit | S-SEC ("This audit includes both the Stripe Card Data Vault (CDV) and…") | confirmed | — |
| 36 | "All card numbers are encrypted at rest with AES-256… static allowlist." | S-SEC | confirmed | — |
| 37 | Stripe's page does not name the allowlisted destinations | S-SEC | confirmed | — |
| 38 | Adyen: "we store payment details in the Adyen Vault" | A-TOK | confirmed | — |
| 39 | Adyen: "We use client-side encryption (CSE) and end-to-end encryption… secure and compliant manner" | A-TOK | confirmed | — |
| 40 | Adyen: "Make sure that your live endpoint region matches your Adyen token vault storage region." | A-FWD | confirmed | — |
| 41 | A-FWD dated "last modified June 2025" | A-FWD front matter | corrected | Ruling 30: now n.d. |
| 42 | Adyen assessed yearly as a Level 1 service provider | A-PCI | confirmed | — |
| 43 | No Adyen statement on separate infrastructure, credentials, algorithm, key location | docs.adyen.com/llms.txt (2,634 lines searched for vault, encryption, HSM, key, PCI, security), A-TOK, A-PCI, Adyen "Protecting sensitive data" page | confirmed | "Not public" holds as far as the index shows |
| 44 | Neither publishes key management, HSM, rotation or token-exchange design; no engineering article on either vault | S-SEC, docs.stripe.com/llms.txt, two web searches, Stripe resource pages "token-vault" and "card-vaulting-explained" (generic, no Stripe internals) | confirmed | Negative claim; searched, nothing found |
| 45 | Adyen article 1 October 2019, Sriram Kunjathur; quote "passes through our Tokenization system… HSM-backed vault key manager" | A-KH (page shows "October 1st, 2019") | confirmed | — |
| 46 | That article "describes a different system and proves nothing about the card vault" | A-KH | hedged | The article lists "credit card details" among the personal data it tokenizes. Now: it is about the data platform behind reports, does not say it is the store behind payment tokens, and the author does not read it as the card vault |
| 47 | Stripe Checkout: "via a redirect to a Stripe-hosted page" | S-CO | confirmed | — |
| 48 | Adyen Hosted Checkout asks SAQ A, risk "Low", "change the redirect from an Adyen-hosted payment page to a fraudulent payment website" | A-PCI | confirmed | — |
| 49 | FAQ 1588: criterion "does not apply to e-commerce merchants with a webpage that redirects customers" | P-FAQ | confirmed | URL replaced by the final address `/faqs/1588/` |
| 50 | FAQ 1588: applies to a webpage "that includes a TPSP's/payment processor's embedded payment page/form" | P-FAQ | confirmed | — |
| 51 | Stripe Elements / Checkout and mobile SDK: SAQ A | S-PCI | confirmed | — |
| 52 | Adyen mobile Drop-in / Components: SAQ A | A-PCI | confirmed | — |
| 53 | Adyen web Drop-in / Components risk "Low-Medium" | A-PCI | confirmed | — |
| 54 | Adyen JWE: "Cardholder data is encrypted on your shopper's browser using a third-party JWE library, sent to your server, and then transmitted to Adyen" | A-PCI | confirmed | — |
| 55 | Adyen JWE: "Medium", "you provide the payment form", "could still be scoped on the Self Assessment Questionnaire A (SAQ A)… cannot decrypt the data" | A-PCI | confirmed | — |
| 56 | Stripe lists no own-form equivalent; "Using Stripe.js v2… requires completing the SAQ A-EP annually" | S-PCI | confirmed | — |
| 57 | Stripe direct API: "When you pass card information directly to Stripe's API…"; SAQ D "the most demanding of the SAQs" | S-PCI | confirmed | — |
| 58 | Adyen API only: "High"; "your system receives, transmits, and potentially stores and processes cardholder data" | A-PCI (web tab; the mobile API-only tab says "Medium") | confirmed | — |
| 59 | "Radar… is only available when using any of our methods for client-side tokenization." | S-PCI | confirmed | Quote is exact |
| 60 | The raw API "gives up Radar" (text and take-away) | S-TOK, S-RADAR | hedged | Stripe's API reference says Radar "performs best with integrations that use client-side tokenization", and the risk-factors page lists direct API integrations with Radar Sessions. Text now gives both statements; the take-away says the raw API loses the signals Stripe's client libraries collect |
| 61 | Radar page: risk factors "automatically captured by Stripe.js and our SDKs" | S-RADAR | corrected | `docs.stripe.com/radar/integration` now redirects to `/radar/optimize-risk-factors`, titled "Risk factors recommendations"; URL, title and the description in the sentence updated |
| 62 | Overlay attack quote "attackers can create alternative content… a copy of the cardholder data is sent to the attacker." | A-PCI | confirmed | — |
| 63 | Council guidance uses the term e-skimming | P-ESK | corrected | Source entry said n.d.; the post is dated 10 March 2025. Date added in Sources and "of March 2025" in the sentence |
| 64 | "Including JavaScript from other sites makes your security dependent on theirs and poses a security risk." | S-GUIDE | confirmed | — |
| 65 | Requirements 6.4.3 and 11.6.1 took effect 31 March 2025 | P-SAQA, P-401 | confirmed | — |
| 66 | 6.4.3 as restated by Adyen (three quotes: authorized, integrity, inventory) | A-SCRIPT | confirmed | — |
| 67 | 11.6.1 asks for a mechanism that detects unauthorized changes to scripts and headers; "alerts personnel about unauthorized modification" | A-SCRIPT | confirmed | — |
| 68 | 30 January 2025: council removed both from SAQ A and added the eligibility line; "do not remove or diminish the underlying requirements within PCI DSS" | P-SAQA | confirmed | — |
| 69 | FAQ 1588 two routes: "Using techniques such as, but not limited to, those detailed in PCI DSS Requirements 6.4.3 and 11.6.1"; "includes techniques that protect the merchant's payment page from script attacks" | P-FAQ | confirmed | — |
| 70 | Adyen script page names both requirements and recommends a content security policy | A-SCRIPT | confirmed | Page named in the sentence |
| 71 | Adyen SAQ A eligibility page: requirements "remain applicable" to SAQ D and on-site merchants | A-SAQA | confirmed | "(n.d., accessed November 2026)" added |
| 72 | Stripe security guide publishes CSP directives | S-GUIDE | confirmed | — |
| 73 | Neither S-GUIDE nor S-PCI mentions 6.4.3 or 11.6.1 | S-GUIDE, S-PCI (searched both; also docs.stripe.com/llms.txt, no script-security page) | confirmed | — |
| 74 | Stripe import: "encrypts your data with the Stripe PGP key and uploads it"; mapping file returned | S-IMP | confirmed | — |
| 75 | "Processors can take anywhere from a few days to several months to produce a final export" | S-IMP | confirmed | — |
| 76 | Adyen import: "Because of technical and compliance complexity, migrating payment data usually takes 10 days or more." | A-IMP | confirmed | — |
| 77 | A-IMP "last modified in December 2019" with an evidence-age flag | A-IMP front matter | corrected | Ruling 30: stamp and the flag built on it removed; cited n.d. in text and Sources |
| 78 | Stripe export: "We believe our customers own the sensitive data they entrust to Stripe." | S-EXP | confirmed | — |
| 79 | "we can only transfer your card data to another PCI DSS Level 1-compliant payment processor"; proof asked | S-EXP (AOC or Visa registry listing, PGP key) | confirmed | — |
| 80 | "Stripe doesn't export your account's payment history, subscriptions, or other objects"; "We exclude any credentials saved through Link" | S-EXP | confirmed | — |
| 81 | Adyen card export: no documentation page; "Not public" in the table | docs.adyen.com/llms.txt (no export page; only import pages), A-TOK, managing-tokens page, help.adyen.com/sitemap.xml | confirmed | Still true. The help sitemap lists "how-to-prepare-for-token-migration-export", but the address returns 301 to the Tokenization docs page, which does not mention export. Sentence now says exactly this; a Sources entry was added for the help address |
| 82 | Stripe Vault and Forward: "available only to businesses with a dedicated Stripe account team"; placeholders replaced from the vault | S-VF | confirmed | — |
| 83 | Adyen: "We support forwarding card details, and network tokens"; enabled by support; placeholders | A-FWD | confirmed | — |
| 84 | Adyen: "dividing the migration into three stages"; "Switch all new tokenizations/sign-ups to Adyen…" | A-IMP | confirmed | — |
| 85 | "Whether network tokens travel is documented by neither company" | S-EXP, S-IMP, A-IMP, A-FWD | hedged | True of the pages read (S-EXP does not mention network tokens; Adyen has no export page). Now "Neither company's pages cited here say…" |
| 86 | Table row "Own form": Stripe not listed / SAQ A-EP; Adyen SAQ A, "Medium" | S-PCI, A-PCI | confirmed | "(2024)" replaced by "(n.d.)" |
| 87 | Table row "Reusable token" | S-PM, A-CREATE, A-TOK | corrected | "delivered by webhook" replaced by "Adyen recommends reading it from a webhook"; last column reworded |
| 88 | Table row "Published description of the vault" | S-SEC, A-TOK, A-FWD | confirmed | "Isolation: Not public" checked against the Adyen index |
| 89 | Table row "Script-security guidance" | S-GUIDE, S-PCI, A-SCRIPT | confirmed | — |
| 90 | Table row "Export of stored cards" | S-EXP; Adyen index and help sitemap | confirmed | — |
| 91 | Table row "Forwarding a stored card" | S-VF, A-FWD | confirmed | "(2025)" replaced by "(n.d.)" |
| 92 | Adyen recommends "Use a report-only CSP HTTP header" | A-SCRIPT | confirmed | Quote cut for length; the attribution stays |
| 93 | "the payment may still be completed" | A-PCI | confirmed | — |
| 94 | "New tokens may still be created with your current provider… request the tokens created in the interim." | A-IMP | confirmed | — |
| 95 | A-CREATE dated "last modified 2023-07-28" (Sources) | A-CREATE front matter | corrected | Ruling 30: n.d. |
| 96 | FAQ 1588 address | P-FAQ | corrected | Old address redirects; replaced by `https://www.pcisecuritystandards.org/faqs/1588/` in Sources and spec |

Counts: 96 claims; 84 confirmed, 9 corrected, 3 hedged, 0 unsupported, 0 unreachable.

## Could not verify, and what I did

- **The council's SAQ documents** (SAQ A, A-EP, D PDFs on `docs-prv.pcisecuritystandards.org`) return HTTP 403. The page already says the definitions of SAQ A-EP and SAQ D are given as the providers' guides apply them; left as is.
- **The Adyen help-center export article** (`help.adyen.com/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export`) is in the help sitemap and in search results (title "How can I prepare for token migration? [Export]"), but the server answers 301 to `docs.adyen.com/online-payments/tokenization`. A search-engine summary describes a formal letter, an SFTP transfer and a CSV format; I could not read the article, so none of that is on the page. No archived copy could be queried (the Wayback availability API returned an upstream 403).
- **Negative claims** (no vault design, no HSM statement, no engineering article, no Adyen export page) cannot be proven; they were checked against both documentation indexes, the pages cited and two web searches.
- **"Last modified" stamps**: A-SAQA's front matter carries today's build time, which confirms ruling 30's point that the stamps are not publication dates.

## Format and rulings

- Ruling 22: the body has no external URLs. Attribution (who, what document, year or n.d.) added where a sentence lacked it: the scene quote, the SAQ A definition, the Token/PaymentMethod/card-object sentence, Adyen's create-tokens, eligibility, import and forwarding pages.
- Ruling 30 applied (rows 11, 41, 77, 95) in the text, the comparison table, Sources and the spec's source strings.
- Length: the draft was at 6,468 of 6,500 words; the added attributions were paid for by cutting one corroborating quote (row 21), one short quote (row 92) and a few connective phrases. Now 6,494 words; `timetoread` stays 28 min. No unit added, dropped, merged or reordered.
- Sources: Radar entry retitled and re-addressed; e-skimming entry dated; one entry added (Adyen help-center address). Every entry is used in the text.

## Larkfield consistency

Checked against the ledger: 8–9 August 2026 (a Saturday and Sunday), 61,000 numbers, €1.12 billion, Tuesday 9 March 2027, 12 January 2027, €49.00, 17 scripts from 9 domains with 4 unowned, 3 scripts from 2 domains, two weeks report-only, Jonas signs in February 2027, 940,000 renewals, 1,140 studios, K4 and K8, the cast's roles. No contradiction found.

## Ledger conflicts

None.

## For other pages

- Any page that says Adyen's stored-card token "arrives only by webhook" should be checked against Adyen's "Create tokens" page (row 29).
- Any page that cites `docs.stripe.com/radar/integration` should use `docs.stripe.com/radar/optimize-risk-factors` ("Risk factors recommendations").
- Any page that says Stripe's Radar is unavailable for server-side card numbers should note that Stripe's own pages disagree in strength (row 60).

## For the author

- The Sources entry for the Adyen help-center address is a link that redirects by design (it documents the redirect). Remove it if the rule "every Sources URL returns its own page" should have no exception.
- The Adyen import page no longer carries an evidence-age flag, because ruling 30 disallows its 2019 stamp as a date. If you want the caution kept, it needs a different basis.
