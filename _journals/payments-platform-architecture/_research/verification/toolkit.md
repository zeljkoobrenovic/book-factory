# Verification — toolkit

Verified 17 November 2026 by an editor who did not write the page. The page quotes no external source, so nothing was fetched from the web: each card was checked against the chapter(s) it names **as they read now** (after rulings 12/29, 13, 26, 28 and 41–48), against `scenario-ledger.md` (the `[editor]` lines win) and against `consistency-issues.md`. "Source" below is the chapter folder and section, or the ledger line.

How the chapters were read: for each card, the chapter's "In Practice at Larkfield" and "Questions to Ask" sections were read in full, and every other number, provider behavior and name on the card was searched for in the chapter text. The chapters were not re-read end to end.

Totals: **101 claims checked: 88 confirmed, 13 corrected, 0 hedged, 0 removed, 0 unreachable.**

| # | Claim (short) | Source | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Larkfield introduction: 6,200 studios; Stripe 2017, Adyen 2024; a studio is on one provider; Keel K1–K8; four roles; Mila and Studio Noord on Adyen; Ironworks on Stripe | ledger: company, why two providers, Keel, cast | confirmed | |
| 2 | "Start with three cards, as payments-what-is-moving advises" (state, idempotency key, reconciliation) | 50, closing paragraph | confirmed | |
| 3 | Only the provider comparison card is called a card in its chapter | search of all chapters for the card names and for `[[toolkit]]`: only 48 presents a card; 50 names three toolkit cards in its closing | confirmed | |
| 4 | Six working records that stay in chapters (acquirer inventory, method-family table, version register, authentication loss table, period record, data-location page) | 06 Larkfield section; ledger lines 07, 19, 25, 27, 39 | confirmed | Checked against the ledger; only chapter 6 was opened |
| 5 | Tool 1 "Built from" line | 04 questions 5–7; 45 questions 3–6 | corrected | Said questions 3 and 4 of journey-dispute; the "record that is the truth" and "end state" fields are its questions 5 and 6. Now "3 to 6" |
| 6 | Deadline starts with the chargeback notification of Wednesday 24 February 2027; a lost one is found against Adyen's daily dispute report | 45, "24 February" section | confirmed | |
| 7 | Deadline Monday 5 April 2027: 40 days, as Adyen documents for Mastercard (accessed November 2026) | 04 and 45; weekday computed | confirmed | |
| 8 | Owner Jonas Weber; alert three days before the deadline | 45; ledger 45 (illustrative) | confirmed | |
| 9 | Evidence: logged-in session of 2 February, check-ins 4 and 11 February, joined by the member id | 04 Larkfield section; 45 | confirmed | |
| 10 | Policy: defend when evidence exists and the amount is worth a second fee; one submission on 3 March | 45, "3 March" section | confirmed | |
| 11 | Record: provider's record checked daily (K2); ledger entries only from report lines (K3) | 45; ruling 28 | confirmed | |
| 12 | End state: reversed 5 March, +€120.00 provisional; won 12 May 2027; fee €15.00 stays lost | ledger 45 | confirmed | |
| 13 | Tool 2 "Built from" line | 08 questions | corrected | Said "the eight questions"; the template uses questions 1, 3, 4, 5, 7 and 8 (not 2 and 6). Now names them |
| 14 | Five-state mapping table, Stripe and Adyen columns | 08 Larkfield table | confirmed | Identical cell for cell |
| 15 | `paid` is not settled; `waiting_on`, `closed_reason`, child rows; unknown status stored and raised | 08; ledger 08 | confirmed | |
| 16 | Review by Femke de Graaf with Tom Hendriks in late March 2027 | ledger 08 | confirmed | |
| 17 | Tool 3 "Built from" line | 10 questions | corrected | Said questions 1, 6 and 8; question 1 (which problem) is not a field, question 7 (who works disputes, refunds and reconciliation on the second provider) is the owner field. Now "6, 7 and 8" |
| 18 | Rule "the studio's provider" with a manual override; it never looks at the payment | 10 scene and Larkfield section | confirmed | |
| 19 | Switch moves own-credential online card payments of the 50 largest studios (verified at both); leaves stored-card renewals and the front desk (Adyen terminals only) | 10 Larkfield section; ledger 10, 11 | confirmed | |
| 20 | An unknown first attempt is never sent to the second provider | ledger 37 | confirmed | From the ledger line of chapter 37, not chapter 10 |
| 21 | Quarterly rehearsal with real payments to payout, refund and reconciliation | 10 Larkfield section | confirmed | |
| 22 | Mila's €120.00 pass would move; her €49.00 renewal stays at Adyen | 10 Larkfield section | confirmed | |
| 23 | Tool 4 "Built from" line (questions 1, 2 and 6) | 13 questions | confirmed | |
| 24 | €117.47 / €1.92 / €0.61 *(assumption)*, whose claim each is | 13 Larkfield table | confirmed | |
| 25 | Payable Thursday 11 March, two business days after Tuesday 9 March | 13; ledger 03 | confirmed | |
| 26 | Refund of Thursday 18 March, −€84.00, against €212.40 of later sales; next payout €84.00 smaller | 13; ledger 35; ruling 26 | confirmed | |
| 27 | Tool 5 "Built from" line | 14 questions | corrected | Said questions 1 to 7; the card uses 1 to 4 and 6 |
| 28 | States and signals: Adyen transfer webhook `booked`, Stripe `payout.paid`, later `payout.failed` | 14 Larkfield section | confirmed | |
| 29 | 10 business days *(assumption)*; sent Thursday 11 March, arrived Thursday 25 March 2027 | 14; ledger 14 | confirmed | |
| 30 | "Payouts in transit" returns to zero; webhooks move state, entries come from report lines | 14 | confirmed | |
| 31 | Owner of a return: "an item open more than five business days goes to Priya Raman's weekly review" | 15 Larkfield section; ledger 15 | corrected | The five-day rule is chapter 15's rule for unmatched reconciliation items, not a payout rule of chapter 14. Now "an unmatched item … (Tool 6)" |
| 32 | 412 returns, €386,000, 19 days; name check and hold after a change of bank details | 14; ledger | confirmed | |
| 33 | Tool 6 "Built from" line | 15 questions | corrected | Said questions 1 to 7; the card uses 1 to 3 and 5 |
| 34 | Stripe itemized payout report (payout ID and balance transaction ID per row); Adyen Balance Platform Accounting Report (split lines share the PSP reference) | 15 Larkfield section; ruling 32(c) | confirmed | |
| 35 | Ready signal, not a fixed hour | 15; ledger `[editor]` (1) | confirmed | |
| 36 | Matching keys: payout ID; merchant account plus batch number and the daily report per studio | ledger 15; 15 | confirmed | |
| 37 | Entry only from a report line, never from a webhook | ruling 28 | confirmed | |
| 38 | Open items with amount, age, owner; five business days to Priya Raman | 15 | confirmed | |
| 39 | Three open items (€16.00, €49.00, £0.03) *(assumptions)* and the three causes of the €0.4 million | 15 open-items table | confirmed | The card does not carry the 02:00 batch close; nothing to reconcile with `[editor]` (6) |
| 40 | Tool 7 "Built from" line | 18 questions | corrected | Said "the nine questions"; the card uses 1 to 6 |
| 41 | Key form and example `renewal:M-204817:2026-11:1` | 18; ledger 18; ruling 13 | confirmed | |
| 42 | The renewal job's HTTP layer generated a key per network call on 1 November 2026 | ledger 18 | confirmed | |
| 43 | Row written before the first send (key, fingerprint, time, `pending`) | 18 | confirmed | |
| 44 | Stripe API v1 at least 24 hours; Adyen 7 to 14 days after first submission; Larkfield 20 hours and 6 days; a 36-hour redelivery is refused on Stripe | 18 | confirmed | Wording and date match the chapter |
| 45 | After a timeout: backoff and jitter, resend the stored key | 18 Larkfield section | confirmed | |
| 46 | Stripe: payment object found by metadata; Adyen: no call in the Checkout API returns an online payment, so webhook then settlement report | 18; rulings 12 and 29 | confirmed | |
| 47 | 1,840 duplicates, €71,300; Mila's keys `:2027-04:1` and `:2027-04:2` | 18; ledger 43 | confirmed | |
| 48 | Refund key from the refund request's identity, so a second click repeats the first key | 18, "Choosing the Key" (refund request as a business event; second trigger for the same event) | confirmed | The "order and refund request" example is the toolkit's own; it follows the chapter's rule |
| 49 | Tool 8 "Built from" line | 20 questions | corrected | Said "the eight questions"; the contract uses 1, 2, 4, 5, 6 and 8 |
| 50 | Acknowledgement: Stripe any 2xx "quickly", no number published; Adyen 2xx within 10 seconds | 20 comparison table | confirmed | |
| 51 | Retries: Stripe up to three days, events readable for 30 days; Adyen up to 30 days from a per-endpoint queue | 20 | confirmed | |
| 52 | Truth: PaymentIntent re-read; on Adyen the stored message until the settlement report | 20 Larkfield section | confirmed | |
| 53 | Sweep every 15 minutes over renewals pending more than 30 minutes *(assumption)*; on Adyen waits for the report | 20 | confirmed | |
| 54 | Check-in screen shows "being checked" and lets the member in | 20 | confirmed | |
| 55 | The chapter names no owner of silence | 20 (question 8 only) | confirmed | |
| 56 | Monday 14 September 2026; about half an hour, not nine hours | 20; ruling 20 | confirmed | |
| 57 | Tool 9 "Built from" line | 22 questions | corrected | Said questions 1 to 5; question 5 (card numbers arriving elsewhere) is not on the card. Now "1 to 4" |
| 58 | Hosted card fields since 2017; SAQ A with both providers each January | 22; ledger 22 | confirmed | |
| 59 | Mila's card of 12 January 2027: encrypted in the browser, ciphertext across Larkfield's server | 22 Larkfield section | confirmed | |
| 60 | 17 scripts from 9 domains, 4 without owner; 3 scripts from 2 domains | 22 | confirmed | |
| 61 | Content security policy report-only for two weeks, then enforced; script line met by own controls | 22 | confirmed | |
| 62 | Jonas Weber signs; Tom Hendriks owns the inventory | 22 | confirmed | |
| 63 | Acronym PCI not expanded on first use | format rule | corrected | "PCI (Payment Card Industry) scope" |
| 64 | Tool 10 "Built from" line | 29 questions | corrected | Said questions 1 to 7; question 7 (a payment during a retry) is not on the card. Now "1 to 6" |
| 65 | Six-row policy table (days 3, 7, 12; day 14; day 30; direct debit rules) | 29 Larkfield table | confirmed | Identical cell for cell |
| 66 | Period record; Larkfield runs the only schedule; message trigger; 7,900 renewals of 1 October 2026 | 29; ruling 37(a) | confirmed | |
| 67 | "Soft" and "hard" decline are industry shorthand | 29; ruling 15 | confirmed | |
| 68 | Tool 11 "Built from" line | 33; 35; 36 | corrected | The exposure row also draws on chapters 35 (€64,000) and 36 (June 2027). Both are now linked in the cell |
| 69 | Five-row table, Adyen and Stripe columns (30 days, reserved compensation account) | 33 Larkfield table; ruling 41(a) | confirmed | Identical cell for cell |
| 70 | Stored per studio and provider: merchant, booking rule, loss bearer, whether it can change | 33 | confirmed | |
| 71 | €156 million inside the 120-day window; €64,000 for Studio Noord *(assumption)*; limit and owner per studio still to be set in June 2027 | 33; 35; ledger 36 | confirmed | |
| 72 | Tool 12 "Built from" line (verification record of 26; questions 1, 5, 6, 7 of 34) | 26 and 34 | confirmed | |
| 73 | Ironworks Climbing: one UK private limited company, three locations | 34 | confirmed | |
| 74 | Legacy Custom account; card payments, Bacs debit payments and transfers | ruling 40(c); ledger `[editor]` (2) | confirmed | See "For other pages" on chapter 34's wording |
| 75 | Requirement changed in May 2026, announced in advance; not named in the book | 26; ledger 26 | confirmed | |
| 76 | Payouts paused Monday 11 May to Wednesday 20 May 2026; ticket of Thursday 14 May | ledger 34; weekdays computed | confirmed | |
| 77 | Owner Jonas Weber; banner with reason, date and one button; alerts 14 and 3 days before *(assumption)* | 26; 34 | confirmed | |
| 78 | Daily re-read from the provider's API (K2); 230 studios | 26 | confirmed | |
| 79 | Tool 13 "Built from" line (questions 1, 2, 4, 5, 8) | 40 questions | confirmed | |
| 80 | About 357,000 renewals, €17.5 million, 38% | 40; ledger | confirmed | |
| 81 | Stripe: 25 requests a second to one endpoint; Adyen publishes no rate limit for payments | 21; 40; ruling 42(a) | corrected | The fact matched; the cell carried no date. Added "(both from documentation accessed November 2026)" |
| 82 | 18 hours from midnight; buckets of 10 and 5 a second *(assumptions)* | 40; ledger 21, 40 | confirmed | |
| 83 | Three lanes in strict order; "not attempted yet" sends no message and carries to the next morning | 40 | confirmed | |
| 84 | 200,000 renewals at 5 a second need 11.1 hours, 62% of the window | 40 | confirmed | |
| 85 | Tool 14: the one card its chapter calls a card | 48 opening section | confirmed | |
| 86 | Six-row Larkfield card (acquirer, price, state, payout, billing, platform model) | 48 Larkfield table | confirmed | Identical cell for cell |
| 87 | Three kinds of difference; definition of "Not public" | 48 | confirmed | |
| 88 | October 2027; keep both; four events of 2026; read again in the K7 slot | 48; ledger 48 | confirmed | |
| 89 | Tool 15 "Built from" line; "the chapters call it the exit sheet" | 22 question 7; 10 questions 2–4 | confirmed | Chapter 22 says "exit sheet"; chapter 10 says "exit answers" |
| 90 | Vault per provider, provider tokens only (K4); network tokens under each provider's identifier, treated as not portable; transfer planned in weeks | 10 exit table | confirmed | |
| 91 | 1,140 Dutch and German studios: export from Stripe's vault, import into Adyen's | 22 Larkfield section | confirmed | |
| 92 | No fee stated in the chapters; answers kept current by the quarterly rehearsal; Femke owns the sheets | 10; 22 | confirmed | |
| 93 | About 940,000 renewals a month against stored payment details | 22 | confirmed | |
| 94 | Tool 16: no chapter gives a form; built from 06 opening scene and 10 Larkfield section | 06; 10 | confirmed | |
| 95 | K8 wording | ledger Keel | confirmed | |
| 96 | Proposal of February 2027 by Daniel Osei; 115,000 payments, a tenth of a month's card traffic | 10 | confirmed | |
| 97 | "Cards it changes": Tools 3, 15 and 12 | toolkit's own linkage; 34 says the 50 studios hold two verification records | confirmed | A recommendation of the toolkit, not a chapter fact |
| 98 | 2024 record: two reasons; "local acquiring" recorded as "effect not measured" | 06 | confirmed | |
| 99 | "Seller last told" came from one batch email to unread mailboxes | 26 | confirmed | |
| 100 | Sources statement: the page quotes no external source; examples repeat the owning chapter | page | confirmed | No external URL on the page |
| 101 | All weekdays on the page (9, 11, 18, 25 March 2027; 24 February; 5 April; 12 May 2027; 14 September 2026; 11, 14, 20 May 2026) | computed | confirmed | |

## Format and rulings

- Front matter complete; one IN THIS SECTION sentence; exactly three KEY POINTS. `timetoread` 35 = 7,998 ÷ 230.
- 66 `[[permalink]]` links, 27 distinct, all in the style guide's valid list. No external URL, no local path, no banned word, American spelling.
- Word count after the pass: **7,998 of 8,000**. Every correction was made within the limit; two words remain.
- `validate_spec.py` ok; `check_draft.py structure` pass (106 units aligned); build ok; render check OK (0 failed, 0 unresolved).
- Spec changed only in its changelog.

## Could not verify

- Nothing was unreachable. Limits of the check are stated at the top: sections and targeted searches, not a full re-read of sixteen chapters.

## Ledger conflicts

- None for this page. The midnight sales-day close and the 02:00 batch close (`[editor]` 6) do not meet on the reconciliation card, which carries neither time.

## For the author to decide

1. **Tool 4 has no owner field.** The page says three fields are never left out (record, owner, date). The funds-flow template has a record and a date and no owner, and its "When and who" names nobody. Chapter 13 raises no owner either, so adding one is the author's call.
2. **The page has one illustration placeholder**, and the style guide says reference pages have none. Left untouched, as the brief requires.
3. **SAQ and PSP are used without expansion** (SAQ A is glossed as "the shortest form"). Two words remain under the limit, so expanding them needs a cut elsewhere.
4. Several "When and who" lines (who owns a card, when to refill it) are the toolkit's own recommendations. The Sources section says so for all cards; they are not marked one by one.

## For other pages

- `34-platform-onboarding-and-verification`, Larkfield section: "Larkfield requests three capabilities for it: `card_payments`, `bacs_debit_payments` … and payouts, which Stripe's Accounts v2 API requests automatically", then adds transfers. Ruling 40(c) and ledger `[editor]` (2) give card payments, Bacs debit payments and transfers for a legacy Custom account. The toolkit follows the ruling.
- `15-payment-reconciliation-and-reporting` has no `[[meet-larkfield]]` link (noticed while listing its links; not checked further).
