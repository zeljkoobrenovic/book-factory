# Verification — how-payments-got-complicated

Verified on 17 November 2026. Every external source was fetched in this session and the passage read. Word count after the pass: 4,158 (spec maximum 4,200); `timetoread` 18 min is correct.

Source keys: **VH** Visa history timeline, `https://corporate.visa.com/en/about-visa.html` (the page's old address `usa.visa.com/about-visa/our_business/history-of-visa.html` redirects here by two 301s); **DC** `https://www.dinersclub.com/about-us/history/`; **V10K** Visa Form 10-K for fiscal 2026 on SEC EDGAR (fetched with the required User-Agent; directory listing dated 2026-11-05); **VR** Visa Core Rules and Visa Product and Service Rules PDF, edition of 24 October 2026; **ISO** Stripe's ISO 8583 explainer; **AD** `https://www.adyen.com/about`; **SL** Stripe annual letter 2023 (landing page plus the PDF it links); **FRH** Federal Reserve History, "Check Payments"; **TCH** The Clearing House, "Our History"; **PCI** PCI SSC "About Us"; **PSD2** Directive (EU) 2015/2366 via the CELEX resource (`Accept: application/xhtml+xml`).

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Fed essay (2023): banks exchanged checks locally "through institutions known as clearinghouses" | FRH | confirmed | Quote matches. Published September 28, 2023 |
| 2 | The Clearing House "dates itself to 1853"; described as "the New York banks' association" | TCH | corrected | The page says "a banking association and payments company that is owned by the largest commercial banks and dates back to 1853"; it does not call itself a New York association. Text and source entry now use the page's own description |
| 3 | Fed essay: "a check wound its way through a series of banks" in several cities | FRH | hedged | Quote matches, but the essay says the correspondent process "sometimes resulted" in this and that historians debate how common it was. Added "at times" |
| 4 | The check put "days" between goods and money | none (generalization) | hedged | Now "commonly days" |
| 5 | Banks commonly exchange checks in batches (clearing) and pay the difference (settlement) | definition; marked "commonly" | confirmed | Already marked as common practice; scoped to the United States by the next sentence |
| 6 | Diners Club's history page dates its charge card to 1950 | DC | confirmed | Page: "1950 — We became the world's first multipurpose charge card". The page makes no "first" claim of its own from this. Page title is "History and Legacy", corrected in Sources |
| 7 | Visa's history page dates BankAmericard to 1958, "the first card with a “revolving credit” feature" | VH | confirmed | Quote matches; attributed to Visa. Source URL had moved: replaced with the final address |
| 8 | The 1958 program took the name Visa in 1976 | VH | confirmed | "1976 — BankAmericard becomes Visa" |
| 9 | Visa's annual report for fiscal 2026 calls customer, issuer, shop and acquirer the "four-party" model | V10K | confirmed | "among consumers, issuing and acquiring financial institutions and sellers in a structure we call the “four-party” model"; character for character |
| 10 | "Visa is not a financial institution." | V10K | confirmed | Character for character (appears three times in the filing) |
| 11 | 10-K date 2026-11-05 | EDGAR directory listing | confirmed | — |
| 12 | Stripe's explainer (updated 2026): ISO 8583 "published in 1987" | ISO | confirmed | "Published in 1987, this international standard…"; "Last updated 18 September 2026" |
| 13 | ISO 8583 "defines the structure of messages between acquirers and card issuers" | ISO | confirmed | Quote matches |
| 14 | The authorization "travels as" an ISO 8583 message | ISO | hedged | Stripe says the standard "still operates across many major card networks", not all. Now "commonly travels as" |
| 15 | The card company "pays the shop and collects from the customer afterwards"; the shop is paid "for certain" / "close to certain" | none (generalization about what a card company guarantees) | hedged | Now "in the usual arrangement"; "fee for the card company's promise"; "no longer depends on the customer if the shop kept to the rules". The section title (a spec title) is unchanged |
| 16 | "No single bank could sign every shop … What it took was … a card network" | none (a claim about why networks formed) | hedged | Rewritten without the necessity claim: "One bank can sign up only so many shops and customers. A card network is a way for banks to accept each other's cards." |
| 17 | The issuer answers within seconds; money follows "a day or more later"; banks settle in daily totals | chapters 1–3 (industry practice; daily net settlement verified there against VR) | confirmed | Consistent with chapter 1's timeline table and the introduction |
| 18 | Interchange: part of the shop's fee passed to the issuer | definition (chapter 5) | confirmed | — |
| 19 | Visa's rules (Product and Service Rules, edition of 24 October 2026) give the cardholder's bank 120 days for most disputes | VR, dispute condition time-limit tables | confirmed | "120 calendar days from the Transaction Processing Date" is the limit in most conditions, including card-absent fraud. Citation form follows ruling 44; wording agrees with chapter 4 ("120 days from processing for most disputes") |
| 20 | "about 120 days before the payment is beyond dispute" (closing) | VR; chapter 4 | hedged | Chapter 4 gives up to 540 days for services delivered later, and a class pass is such a service. Now "before the usual time limit for a dispute has passed" |
| 21 | A card-not-present payment the cardholder denies is "commonly the shop's loss" | industry practice; marked "commonly" | confirmed | Already hedged in both places ("commonly", "Mostly the shop"). Not a Visa quotation; the rules make the acquirer liable and the pass-through to the shop is contract practice |
| 22 | PCI council "founded in 2006 by five card brands" | PCI | confirmed | "The Council was founded in 2006 by American Express, Discover, JCB International, MasterCard and Visa Inc." |
| 23 | A directive of 2015: authentication built on "two or more elements" | PSD2 Art. 4(30) | confirmed | "an authentication based on the use of two or more elements categorised as knowledge…, possession… and inherence". Added "still in force in November 2026" in the text as the evidence-age mark (11 years); Article 97 added to the source entry |
| 24 | PSD2 requires it "for online payments, with exemptions" | PSD2 Art. 97, 98 | confirmed | Art. 97(1)(b) covers electronic payments the payer initiates; exemptions are mandated by Art. 98. A simplification, declared as such by the page |
| 25 | Adyen's company page gives 2006 as founding year | AD | confirmed | "We were founded in Amsterdam in 2006." |
| 26 | Stripe's annual letter for 2023: Stripe "launched in 2011" | SL (PDF) | confirmed | "when Stripe launched in 2011"; PDF dated March 13, 2024. The sentence is in the PDF, not on the landing page; source entry says so |
| 27 | A small online shop can begin "without arranging anything with a bank itself" | none (generalization) | hedged | Now "can often begin" |
| 28 | "Over a counter that cannot happen" (paying twice) | true only of cash | hedged | Now "With a coin on a counter that cannot happen", which matches the spec's AC-2 |
| 29 | "so the shop does not keep it" (the stored card number) | none (generalization) | hedged | Now "commonly does not keep it" |
| 30 | "Such a seller has neither the time nor the standing…" | illustration | hedged | Now "commonly has neither" |
| 31 | Visa's rules define a payment facilitator: "An entity that contracts with an Acquirer to deposit Transactions, receive settlement from, or contract with an Acquirer on behalf of a Sponsored Merchant" | VR Glossary, ID# 0028921 | confirmed | Character for character |
| 32 | A platform "more often" builds on a provider | none (frequency comparison) | hedged | Now "commonly" |
| 33 | Under PSD2 a licensed payment company has to keep such funds "apart and protected" | PSD2 Art. 10(1) | corrected | Art. 10 offers two ways: (a) not commingled, deposited separately and insulated, or (b) covered by insurance or a guarantee. Added "or insure them" |
| 34 | "every payment system since has kept one" (a ledger) | none (universal claim) | hedged | Now "every payment system in this book keeps one" |
| 35 | "None was ever retired" | the page's thesis (journal spec) | confirmed as argument, clarified | Literally false of the paper check in some countries. One clause added to the simplification paragraph: "retired" is meant of what each step introduced. See "For the author" |
| 36 | Sixteen pattern names in the closing table | style guide | confirmed | All sixteen, exact spelling, each once |
| 37 | Every URL in Sources resolves | all eleven | confirmed | Ten return 200 at the listed address; the Visa history address redirected and was replaced |
| 38 | Every `[[permalink]]` is valid and points to the owning chapter | style guide list; PLAN "Owns" | confirmed | Added one link for "card network" and the four-party model to `journey-of-a-payment`, which owns both. `acquirer` is owned by chapters 1 and 6; the page links chapter 6 |

Counts: 38 checked — 24 confirmed, 2 corrected, 12 hedged, 0 unsupported, 0 unreachable.

## Larkfield consistency

Checked against the ledger and chapter 1: 19:42 on Tuesday 9 March 2027 (a Tuesday), €120, fee €2.53, €117.47, payout Thursday 11 March (a Thursday), dispute "until about 7 July", Studio Noord on Adyen, wallet payment. Seven parties equals the seven rows of chapter 1's cast table (Adyen counted once as acquirer and provider). Five promises "by her bank, the studio, the acquirer, the network and the provider" equals the promise column of chapter 1's six-step table (the dispute window makes none). "Four installments" (promised, moved, paid out, final) agrees with the Today step. All agree.

## Ledger conflicts

None.

## field-evolution skill: breaches found

- **Length.** The skill says 2,500–3,500 words; the page is 4,158 under the spec's maximum of 4,200, raised by the author's revision. Not changed.
- **Gain before cost, paying at a distance.** The chargeback paragraph states a cost (the shop's loss) before the gain paragraph. It sits in "what was added"; fixing it would reorder units, so it is left for the author.
- **One new term per paragraph.** The check paragraph introduces clearing and settlement together; the network paragraph introduces acquirer and the four-party model together. Left.
- **"Layers".** Not used in the prose; "stack" appears once, next to the figure, as the skill allows.
- **"First" claims and motives.** The only "first" is Visa's own, quoted and attributed. No motive is attributed after the edit to claim 16.
- **Illustrations labeled; simplification declared; Larkfield only at the last step** (the lead recalls Mila's tap from the introduction as today's case, not in the past). No breach.

## Not verified, and what was done

- Mastercard's history pages and ISO's catalogue page were not retried; the page states neither as a source and gives no date from them.
- The Fed essay (2023-09-28) is just over three years old. It is a history essay; the source entry now carries "evidence age: 3 years" and the text gives the year. No in-text bold mark was added.
- Diners Club's and Visa's dates are the companies' own accounts; the page attributes them so.

## For other pages

- `introduction`: its table of "five promises" lists authorization, capture, clearing and settlement (merged), payout and the dispute window. Chapter 1's table gives the five promises as issuer, merchant, acquirer, network and provider, and says the dispute window makes none. This page follows chapter 1. The two lists should be aligned.

## For the author

- "None was ever retired" is the page's thesis and is stated five times. It is true of what each step introduced and not of every instrument everywhere (the paper check). I added one clarifying clause and changed nothing else.
- The section title "The Card: Someone Else Guarantees the Shop Is Paid" still says "guarantees"; the body is now hedged. Changing the title needs a spec and `config`-level title change.
