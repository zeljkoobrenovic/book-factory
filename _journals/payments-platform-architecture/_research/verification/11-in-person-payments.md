# Verification — 11-in-person-payments (`in-person-payments`)

Verification pass of 17 November 2026. Every source listed on the page was fetched in this session: Adyen pages as `.md`, Stripe pages as `.md` in the variant the page cites, the Visa rules PDF, Adyen's Annual Report 2025 and Q3 2026 Business Update PDFs (both converted with pdftotext), and the EMVCo, PCI SSC, Apple, Adyen press and Stripe newsroom pages as HTML. Each quotation was compared with the fetched text by script after normalizing typographic quotes and markdown marks, and the passage around it was read.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | EMVCo quote: chip 'uses advanced cryptography to generate a one-time security code (cryptogram) ... cannot be reused' | https://www.emvco.com/emv-technologies/emv-contact-chip/ | confirmed | No edit |
| 2 | Chip works by contact and contactless, including phone wallets | https://www.emvco.com/emv-technologies/emv-contact-chip/ | confirmed | Page lists EMV Contact Chip and EMV Contactless Chip ('contactless chip cards and NFC enabled mobile devices') |
| 3 | EMVCo: '97% of card-based transactions' are chip, 'as of late 2025' | https://www.emvco.com/about-us/worldwide-emv-deployment-statistics/ | hedged | Quote exact, but the page measures card-present transactions over twelve months, reported as of Q4 2025; sentence now says so |
| 4 | EMVCo 'does not mandate or enforce EMV compliance' | https://www.emvco.com/about-us/overview-of-emvco/ | confirmed | No edit |
| 5 | EMV is named after Europay, Mastercard and Visa | (none on the pages fetched) | not checked | Common expansion of the acronym; neither EMVCo page fetched spells it out. Left as a term gloss |
| 6 | Visa rules edition is 24 October 2026 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Title page of the PDF |
| 7 | Visa: 'Dispute Condition 10.1: EMV Liability Shift Counterfeit Fraud' exists and is an issuer dispute | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Section 11.8.2.1, Table 11-9 |
| 8 | Visa quote: 'was completed with a Counterfeit Card in a Card-Present Environment' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 9 | Visa quote: 'The Cardholder denies authorization' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | The rule continues 'of or participation in the Transaction'; the quoted words are contiguous |
| 10 | Visa quote: 'The Card is a Chip Card' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 11 | Visa quote: 'The Transaction did not take place at a Chip-Reading Device' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | The rule adds '(terminal entry capability code was not 5)' |
| 12 | Visa quote: 'was Chip-initiated and, if ... authorized Online, the Acquirer did not transmit the Full-Chip Data to Visa in the Authorization Request' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 13 | Visa quote: 'was approved offline, and the Acquirer did not transmit the Full-Chip Data to Visa in the Clearing Record' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 14 | Participation varies by Visa region (Table 11-1) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Section 11.1.2, Table 11-1 |
| 15 | Table 11-9 entry last updated October 2023 (source entry) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | 'Edition: Oct 2026 / Last Updated: Oct 2023' |
| 16 | Mastercard's public rules could not be read (access error) | https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf | confirmed | HTTP 403 again in this session (ruling 17); the page already says Mastercard is unverified |
| 17 | PCI PTS is 'the card industry's standard for the tamper-resistant device that accepts a PIN' | https://www.pcisecuritystandards.org/standards/pts-point-of-interaction-poi/ | hedged | No source was listed and 'tamper-resistant' is not on the PCI page; replaced with the council's own words and added the source. PCI and PIN are now expanded |
| 18 | Adyen catalog labels each model 'PCI PTS 5' or 'PCI PTS 6'; last modified April 2026 | https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals | confirmed | last_modified 2026-04-15; source title corrected to 'Terminals' |
| 19 | Adyen: 'PCI PTS 5 payment terminals will no longer be available for order starting April 30, 2026' | https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals | confirmed | No edit |
| 20 | Adyen (2023): terminals 'can be centrally managed, and will automatically update themselves with the latest Adyen software' | https://docs.adyen.com/point-of-sale | confirmed | last_modified 2023-12-08 |
| 21 | Stripe S700: 'The reader restarts every day at midnight for PCI compliance' | https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710 | confirmed | No edit |
| 22 | Both encrypt by default with their own E2EE and offer validated P2PE as an option | https://docs.adyen.com/development-resources/e2ee-p2pe-comparison ; https://docs.stripe.com/terminal/overview | confirmed | Adyen: 'By default ... E2EE', 'you can opt-in to use Adyen's P2PE'. Stripe: 'encrypted using end-to-end encryption (E2EE) by default'; P2PE for 'certain industries' |
| 23 | PCI SSC: P2PE protects data 'from the point where a merchant accepts the payment card to the secure point of decryption' | https://www.pcisecuritystandards.org/standards/point-to-point-encryption-p2pe/ | confirmed | No edit |
| 24 | Adyen (2025): default needs only 'the SAQ B-IP' | https://docs.adyen.com/development-resources/e2ee-p2pe-comparison | confirmed | last_modified 2025-09-10 |
| 25 | Adyen: E2EE 'does not have the PCI P2PE-validated "stamp"' | https://docs.adyen.com/development-resources/e2ee-p2pe-comparison | confirmed | No edit |
| 26 | Stripe: 'Stripe P2PE is an optional, paid feature' | https://docs.stripe.com/terminal/overview | confirmed | Page is now titled 'How Terminal works'; source entry renamed |
| 27 | Stripe: Terminal-only merchants 'can validate using SAQ C' | https://stripe.com/guides/pci-compliance | confirmed | The URL redirects by locale (Dutch from this network); the English page (en-nl) has the sentence. Source title corrected to the page's title |
| 28 | Apple: an app must 'integrate with a supported payment service provider (PSP) who processes the payments ... and provides the certified terminal configurations ...' | https://developer.apple.com/tap-to-pay/ | confirmed | No edit |
| 29 | MPoC is a PCI standard for payment acceptance on COTS devices | https://www.pcisecuritystandards.org/standards/mobile-payments-on-cots-mpoc/ | confirmed | No edit |
| 30 | MPoC 'covers such software feature by feature'; Adyen: 'offline acceptance in its Android software' is in limited availability 'because it is not yet PCI MPoC certified' | https://docs.adyen.com/point-of-sale/offline-payment | hedged | PCI does not describe certification as feature by feature, and Adyen's sentence is about store and forward with the Mobile SDK for Android; both reworded |
| 31 | No Stripe or Adyen source describes how a software update is staged across a fleet | https://docs.adyen.com/point-of-sale/release-updating | corrected | Wrong for Adyen: 'Update to a new release' (last modified 2025-10-08) says releases come 'every four weeks', 'We roll out releases gradually and monitor the performance', and manual updates run in batches. Paragraph rewritten, source added. Stripe's S700 page says only that the reader 'receives updates automatically from Stripe when not in use' |
| 32 | No Stripe or Adyen source describes terminal key loading and rotation, or failure rates | https://docs.adyen.com/llms.txt ; https://docs.stripe.com/llms.txt | hedged | Index search for key injection, key rotation, DUKPT, HSM and failure rate found no terminal page; absence scoped to 'the pages I read' (neither company's P2PE instruction manual was read) |
| 33 | Adyen exposes device management through its Management API (2021 page) | https://docs.adyen.com/point-of-sale/automating-terminal-management | confirmed | last_modified 2021-04-21; source title corrected |
| 34 | Stripe: 'Dashboard tools for ordering and managing readers' | https://docs.stripe.com/terminal/overview | confirmed | No edit |
| 35 | Adyen (2023): 'Our Terminal API is based on the nexo Retailer Protocol' | https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api | confirmed | last_modified 2023-07-11 |
| 36 | nexo Retailer Protocol is an industry specification for till-to-terminal messages | (none) | not checked | Term gloss; nexo-standards.org was not fetched |
| 37 | Adyen: ServiceID 'Must be unique within the last 48 hours for the terminal' | https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api | confirmed | No edit |
| 38 | Adyen local: 'you make an API request directly to the IP address of the terminal' | https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture | confirmed | last_modified 2023-12-06 |
| 39 | Adyen local: 'you need to add Adyen's certificate to your POS app, and encrypt your messages' | https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture | confirmed | No edit |
| 40 | Adyen cloud: 'you send your Terminal API requests to an endpoint on the Adyen payments platform. This request is forwarded to the terminal' | https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture | confirmed | No edit |
| 41 | Adyen: cloud 'is easier to implement but does not support all use cases'; local 'can be more robust but requires an additional effort' | https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture | confirmed | No edit |
| 42 | Adyen local needs a fixed terminal address (four-shapes table) | https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture | confirmed | 'DHCP reservation ... or manually configure static IP addresses' |
| 43 | Stripe SDK integration: the SDK runs in the POS app and talks to the reader | https://docs.stripe.com/terminal/payments/setup-integration | confirmed | iOS variant: 'Install the SDK in your app' |
| 44 | Stripe server-driven: the Stripe API 'Receives requests and forwards them to a smart reader' | https://docs.stripe.com/terminal/payments/setup-integration | confirmed | Server-driven variant |
| 45 | Stripe: 'Server-driven integration doesn't support' collecting card payments while offline | https://docs.stripe.com/terminal/payments/setup-integration | confirmed | No edit |
| 46 | On Stripe the counter payment is a PaymentIntent in both shapes | https://docs.stripe.com/terminal/features/refunds ; https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | Both variants create and confirm a PaymentIntent |
| 47 | Four-shapes table: Adyen local can accept offline payments if enabled; cloud offline 'not very useful' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | The architecture page is blunter: 'A cloud integration does not support offline EMV or Store-and-forward transactions'. Left as quoted |
| 48 | Four-shapes table: Stripe SDK can store payments if enabled; server-driven cannot | https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | Offline mode is enabled per Location through a Configuration |
| 49 | Adyen offline page last modified May 2026 | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | last_modified 2026-05-04 |
| 50 | Adyen quote on offline EMV ('verifies that the PIN ... depends on how the issuer configured the card.') | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 51 | Adyen: 'Most debit cards do not support this type of payment.' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 52 | Adyen: store and forward 'approves payments without any verification' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 53 | Adyen: 'You are fully liable for the risk of failed captures, chargebacks, and disputes ...' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 54 | Stripe: 'You, as the user, assume all decline and tamper-related risks associated with an offline transaction' | https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | Smart readers, iOS variant |
| 55 | Stripe documents store-and-forward only (no offline approval by the card) | https://docs.stripe.com/terminal/features/operate-offline/overview | confirmed | All three reader variants describe storing and forwarding only: 'authorization is only attempted after connectivity is restored' |
| 56 | Adyen: later authorization rates '95% in some industries to several percentage points higher' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | Vendor statement, labeled as such on the page |
| 57 | Adyen limits: floor limit, 'Store-and-forward max. amount', 'Max. payments' per terminal, chosen by the merchant | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | The merchant gives the limits to Adyen's Support Team, which sets them |
| 58 | Adyen: 'you need to set a transaction floor limit before your integration can make offline payments' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 59 | Stripe: 'the Stripe-enforced offline maximum of 10,000 USD or equivalent in your operating currency' | https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | No edit |
| 60 | Stripe lets the integration add stricter limits | https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | 'Managing risk': REQUIRE_ONLINE with the stored count and amount |
| 61 | Stripe, EEA: 'customers are required to insert their card and enter a PIN' | https://docs.stripe.com/terminal/features/operate-offline/overview | confirmed | Footnote 2 of the payment methods table |
| 62 | Adyen: 'Store-and-forward offline payments do not work in the event of an outage of the Adyen payments platform' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | Quoted twice on the page; both match |
| 63 | Adyen: with cloud communications 'it is not very useful to enable offline payments' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 64 | Stripe smart reader: 'you must have previously connected to the same reader using a valid connection token within the last 24 hours, on the same local network' | https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | No edit |
| 65 | Stripe: reader whose 'software hasn't been updated in 30 days or more' must go online first | https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments | confirmed | No edit |
| 66 | Adyen's page does not say why store and forward fails in a platform outage (inference block) | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | The page gives no reason; the block stays labeled as inference |
| 67 | Adyen offline response: 'misses the PSP reference. Only contains the tender reference' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 68 | PSP reference is generated by the platform, tender reference by the terminal | https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api | confirmed | No edit |
| 69 | Adyen: 'failed store-and-forward payments that are eligible will be automatically retried for one calendar month' | https://docs.adyen.com/point-of-sale/offline-payment | hedged | True only with Auto Rescue, which the merchant asks Adyen to enable; sentence now says so |
| 70 | Stripe: 'the SDK or smart reader automatically forwards any stored payments'; the outcome returns as an event | https://docs.stripe.com/terminal/features/operate-offline/overview | confirmed | Forwarding event notification; webhooks for PaymentIntent events |
| 71 | Adyen (2021): 'With Adyen's single payments platform you have a unified view on all your customers' | https://docs.adyen.com/unified-commerce | confirmed | last_modified 2021-07-12; page title 'Omnichannel' |
| 72 | Stripe: 'Manage online and in-person payments in a single Stripe account' | https://docs.stripe.com/terminal/overview | confirmed | No edit |
| 73 | Adyen card alias (2023): 'You can use this to identify the shopper based on their card, but not to make payments' | https://docs.adyen.com/point-of-sale/card-acquisition | confirmed | last_modified 2023-02-23 |
| 74 | Adyen: 'If you tokenize the shopper's payment details ... at the point of sale, you can use that token in a later online payment' | https://docs.adyen.com/point-of-sale/recurring-payments | confirmed | The file's last_modified is 2026-11-17 12:56:38, the same second as the refund page; see note 3 |
| 75 | At Adyen a wallet needs its own identifier (PaymentAccountReference) | https://docs.adyen.com/point-of-sale/card-acquisition | confirmed | 'If the shopper used an NFC wallet, you can use this instead of the alias' |
| 76 | Stripe fingerprint 'uniquely identifies a particular card number' on card and card_present | https://docs.stripe.com/terminal/features/saving-payment-details/overview | confirmed | No edit |
| 77 | Stripe: 'Cards from mobile wallets (for example, Apple Pay or Google Pay) don't share a fingerprint with cards used online.' | https://docs.stripe.com/terminal/features/saving-payment-details/overview | confirmed | No edit |
| 78 | Stripe: card read in person is not reusable; 'in most cases, Stripe can create a reusable generated_card PaymentMethod' | https://docs.stripe.com/terminal/features/saving-payment-details/overview | confirmed | No edit |
| 79 | Adyen refunds: referenced (tied to the original by its identifier) and unreferenced (any amount to any card presented) | https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment | confirmed | No edit |
| 80 | Adyen table row 'Omnichannel refunds': 'Supported, using the PSP reference' / 'Not supported'; last modified November 2026 | https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment | confirmed | Row matches. Date is the file's last_modified (2026-11-17); see note 3 |
| 81 | Stripe refund is a server call 'passing in the PaymentIntent ID or the charge ID', 'whichever channel created the payment' | https://docs.stripe.com/terminal/features/refunds | hedged | Quote exact. 'Whichever channel' is not on the page; replaced by 'through the same Refunds API as for an online payment', which the page links |
| 82 | At Stripe the terminal takes almost no part in refunds | https://docs.stripe.com/terminal/features/refunds | corrected | The page now also offers refunds from the Terminal iOS or Android SDK (`confirmRefund`, no card needed) in private preview; added with its status |
| 83 | Stripe: 'In-person refunds are only available on Interac'; Interac is Canadian | https://docs.stripe.com/terminal/features/refunds | confirmed | 'For Interac transactions in Canada' |
| 84 | Adyen: 'The PSP reference and tender reference can be found in your Customer Area, and in reports generated by Adyen' | https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api | confirmed | No edit |
| 85 | Stripe recommends 'reconciling payments on your back end after a day's activity' (and the longer form in When It Goes Wrong) | https://docs.stripe.com/terminal/features/refunds | confirmed | Both quotations match |
| 86 | Neither page shows a combined settlement report | https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api ; https://docs.stripe.com/terminal/features/refunds | confirmed | True of the pages cited; Adyen's in-person landing page says point-of-sale payments run 'on the same platform as online payments' and links settlement reconciliation, without a report layout. The page's wording ('the documentation I read') already limits the claim |
| 87 | Adyen announced 'its first in-house designed terminals' on 18 August 2022 | https://www.adyen.com/press-and-media/adyen-advances-in-person-payments-with-the-launch-of-in-house-designed-terminal-range | confirmed | Displayed date August 18th, 2022 |
| 88 | Adyen Annual Report 2025: 'point-of-sale volumes' of '€310.9 billion, comprising 22% of total processed volume, up from 18% in 2024' | https://investors.adyen.com/financials/2025 | confirmed | Read in the report PDF linked from that page; signed March 5, 2026 |
| 89 | Adyen Q3 2026: 'The number of transacting terminals across the platform reached 878k' | https://investors.adyen.com/financials/q3-2026-10c88s | confirmed | Read in the PDF linked from that page. Source date made exact: 2026-10-28 |
| 90 | 'Transacting' is not defined | https://investors.adyen.com/financials/q3-2026-10c88s | confirmed | No definition in the update |
| 91 | Stripe announced Terminal on 17 September 2018 as 'a programmable point of sale for in-person payments' | https://stripe.com/newsroom/news/stripe-launches-terminal | confirmed | Source title corrected to the release's headline |
| 92 | Stripe publishes no Terminal volume, reader count or in-person share (table: 'Not public') | https://stripe.com/newsroom/news/stripe-2025-update ; https://stripe.com/terminal ; https://docs.stripe.com/llms.txt | confirmed | None on the 2025 update release, the Terminal product page or the documentation index. The annual letter's full text was not read; the sentence says 'I found no' |
| 93 | Table: Stripe drives the device by SDK or server-driven API; Adyen by Terminal API 'based on the nexo Retailer Protocol', local or cloud | (rows above) | confirmed | No edit |
| 94 | Table: Stripe record is a PaymentIntent; Adyen's has a tender reference and a PSP reference | (rows above) | confirmed | No edit |
| 95 | Table: recognizing a card (fingerprint, generated_card; alias, wallet value, token) | (rows above) | confirmed | No edit |
| 96 | Table: Adyen offline 'local communications only' | https://docs.adyen.com/point-of-sale/offline-payment | corrected | Adyen also supports offline on standalone terminals and through its Mobile SDK; cell now reads 'in a Terminal API integration, local communications only' |
| 97 | Table: Stripe 'Server-side refund for every channel' | https://docs.stripe.com/terminal/features/refunds | corrected | Cell now names the Refunds API and the SDK refund in private preview |
| 98 | Table: Adyen referenced refund at the terminal; omnichannel refunds 'Supported, using the PSP reference' | https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment | confirmed | No edit |
| 99 | Table: encryption row for both | (rows above) | confirmed | No edit |
| 100 | After the table: 'the same things are not public: terminal key management, how fleet updates are staged, and failure rates' | https://docs.adyen.com/point-of-sale/release-updating | corrected | Adyen documents staging; sentence rewritten |
| 101 | Adyen (2025): refunding an ecommerce payment at a terminal needs 'the PSP reference, the date, and the currency of the original payment' | https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/referenced | confirmed | last_modified 2025-01-22 |
| 102 | Adyen, for its mobile SDK: 'check the transaction status before you start the transaction again' | https://docs.adyen.com/point-of-sale/offline-payment | confirmed | No edit |
| 103 | Evidence ages: Terminal API 2023 (3 years), card acquisition 2023 (3), Omnichannel 2021 (5), terminal management 2021 (5), press release 2022 (4), Stripe launch 2018 (8) | (rows above) | confirmed | All flagged in the text and in the source entries |
| 104 | What to Take Away, Established: three bullets restating the EMVCo, Visa and offline facts | (rows above) | confirmed | No edit |

**Counts:** 104 claims: 91 confirmed, 5 corrected, 6 hedged, 0 unsupported, 0 unreachable, 2 not checked.

## Not verified, and what was done

1. **EMV as 'Europay, Mastercard and Visa'** and **nexo as a till-to-terminal industry specification** (rows 5 and 36) are term glosses with no source on the page; neither was checked against a source in this session. They are left in place as definitions.
2. **Mastercard's rules** returned HTTP 403 again. The page already limits its liability-shift claim to Visa and says so (ruling 17).
3. **Two Adyen dates are doubtful.** `refund-payment.md` and `recurring-payments.md` both carry `last_modified: 2026-11-17T12:56:38+01:00`, the same second on the day of this pass, which looks like a regeneration time and not an edit. The page and its source entries cite them as last modified November 2026, which is what the files say; the content of both was confirmed. If the author prefers, cite both as 'n.d., accessed November 2026'.
4. **Absences.** 'Not public' for Stripe's in-person scale and for terminal key management and failure rates at both companies rests on searches of both documentation indexes (`llms.txt`), Stripe's 2025 update release and its Terminal product page. Stripe's annual letter in full and both companies' P2PE instruction manuals were not read.
5. **Stripe's PCI guide** redirects by locale; the quotation was confirmed on the English page (`/en-nl/`). The source entry keeps the locale-free URL.

## Links

All 33 URLs under Sources and Evidence returned HTTP 200 (two new entries included: Adyen 'Update to a new release' and PCI SSC 'PTS Point of Interaction'). `stripe.com/guides/...` and `stripe.com/newsroom/...` redirect to a locale path; the locale-free URLs are kept. All `[[permalink]]` links are in the style guide's valid list and the render check reports none unresolved. No external URL appears in the running text (ruling 22).

## Sources section

- Removed: 'Adyen publishes H2 2025 financial results' (not cited in the text; the annual report carries the figure).
- Added: Adyen 'Update to a new release'; PCI SSC 'PTS Point of Interaction (POI)'.
- Titles corrected to the pages' own: 'Terminals', 'Automate the management of your terminals', 'How Terminal works', 'What is PCI DSS compliance?', 'Stripe announces Stripe Terminal, a programmable point of sale for in-person payments'. Q3 2026 update dated 2026-10-28.

## Format and rulings

- Ruling 8 (gloss of 'liability shift', link to `three-d-secure-and-sca`), 14 (Mila's pass paid from a phone wallet) and 17 (Mastercard) hold. A one-clause gloss was added for 3-D Secure and for 'settlement report'; PCI and PIN are expanded on first use.
- `timetoread` changed from 26 to 27 (6,096 words by `check_draft.py structure`, ÷ 230 = 26.5).
- `validate_spec.py` and `check_draft.py structure` pass; render check OK. No unit was added, dropped, merged or reordered.

## Larkfield consistency

Checked against the ledger: 2,100 studios, €210 million in 3.8 million payments (about €55 each, 18.75% of €1.12 billion), 1,140 split studios, Adyen terminals since 2024, 1.4% + €0.10, cloud communications and no offline (ledger line for chapter 11), €120 × 25 = €3,000 *(assumption)*, member id as the shared identifier, K3 and K8, Mila's €120.00 pass of 9 March 2027 and €84.00 refund of 18 March 2027, Femke de Graaf joining in January 2027. No contradiction found. The page names no weekday for a dated event.

## Ledger conflicts

None.

## For the author to decide

- **The journal spec still carries the corrected claim.** Acceptance criterion AC-4 ('the chapter says that neither company publishes its terminal key management or fleet update design') and `thesis.how_why` ('neither publishes key management, fleet updates or failure rates') are copied from `journal-spec.json`, which this pass may not edit, and `validate_spec.py` rejects a post spec that alters them. The article now says that Adyen documents how it stages fleet software updates and Stripe does not on the pages read. In the post spec, one supporting claim, the controlling idea and evidence of p15 and the evidence of the integrator-advice paragraph were reworded to match. The journal spec's two sentences need the same change.
- Whether to cite the two Adyen pages of note 3 as 'n.d.'.

## For other pages

- Any page that says neither Stripe nor Adyen documents terminal fleet updates (the brief `brief-acquiring-methods-and-terminals.md` lists 'estate software update mechanics' as not public at either) should be checked against Adyen's 'Update to a new release'.
- Any page that says Stripe Terminal refunds are server-side only: the SDK `confirmRefund` method is in private preview as of November 2026.
