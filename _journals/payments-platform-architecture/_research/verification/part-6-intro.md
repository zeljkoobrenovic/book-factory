# Verification — part-6-intro (permalink `part-6`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–45 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source. All six chapters of the part (27–32) had a verification file when this page was finished.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | KEY POINT 3: the public record puts the invoice inside Stripe's platform and, on Adyen, with the merchant | 27; ruling 6 | corrected to match | Chapter 27 calls "with the merchant" an inference from absence. Now: "Stripe documents it inside its platform; Adyen documents none, which leaves it with the merchant" |
| 2 | Stripe documents subscriptions, invoices, usage meters, tax calculation and revenue recognition on one platform | 27, 28, 30, 31 | agrees | — |
| 3 | Adyen documents a stored card charged with a recurring flag | 27 | agrees | — |
| 4 | Adyen documents retries of refused payments (Auto Rescue) | 29 (row 66) | agrees | — |
| 5 | Adyen documents automatic card updates | 29 (Account Updater, Real Time Account Updater) | agrees | — |
| 6 | Adyen closed its acquisition of the billing company Orb on 1 July 2026 | 27; 30 (row 40); ruling 21 | agrees | No quotation and no knowledge-hub date is used, so ruling 21 has nothing to correct |
| 7 | "no integrated product is documented yet" | 27; 31 (rows 49, 52); ruling 39(b) | corrected to match | Narrowed to "Adyen documents no integrated billing product yet" (Orb's own pages document Adyen as a gateway) |
| 8 | For invoicing, tax and revenue recognition no Adyen product was found; an absence, not a statement by Adyen | 27, 30 (row 37), 31 (rows 47–49); ruling 38 | corrected to match | Now "tax calculation" and "no first-party Adyen product" |
| 9 | On merchant of record Adyen says it does not act as one | 32 | agrees | Chapter 32's finding, already in the page |
| 10 | Merchant of record glossed as the model in which "the provider is the legal seller" (lead, twice) | 32 (rows 4, 42, 100) | corrected to match | Stripe's terms name its entity merchant of record and "not the seller of record". Now "sells in its own name" |
| 11 | Ch. 27: a billing engine is a scheduler, a price calculator and a subscription state machine whose output is the invoice | 27 | agrees | — |
| 12 | Ch. 27: Stripe keeps that engine in its platform | 27 | agrees | — |
| 13 | Ch. 27: in Adyen's documentation "Subscription" is a flag on a payment the merchant starts | 27 | agrees | — |
| 14 | Ch. 28: three time rules before the first invoice | 28 | agrees | — |
| 15 | Ch. 28: Stripe's meters can accept an event and never bill it | 28 | agrees | — |
| 16 | Ch. 29: a finalized invoice is frozen and collected as one debt (dunning) | 29 | agrees | — |
| 17 | Ch. 29: Stripe's Smart Retries retry an invoice Stripe holds | 29; ruling 37(c) | agrees | No recovery figure is given |
| 18 | Ch. 29: Adyen's Auto Rescue retries a payment, tied to the billing cycle by a merchant reference | 29, 27; ruling 37(b) | agrees | The page makes no statement on Auto Rescue figures |
| 19 | Ch. 30: a provider can calculate; calculating is one of four steps; the liability for all four stays with the seller | 30 | agrees | — |
| 20 | Ch. 30: Stripe Tax returns zero where the seller has recorded no registration | 30 (row 21) | agrees | — |
| 21 | Ch. 30: "No Adyen tax product was found" | 30 (rows 37, 45–47); ruling 38 | corrected to match | "No first-party Adyen tax engine was found" |
| 22 | Ch. 31: each line gets a service period; its amount is deferred and released | 31 | agrees | — |
| 23 | Ch. 31: Stripe documents a recognition ledger over its own invoices | 31 (row 25) | agrees | — |
| 24 | Ch. 31: none was found for Adyen | 31 (rows 47–49); ruling 39(b) | agrees | Reads as "no recognition ledger", which is the chapter's scoped finding |
| 25 | Ch. 31: billing should stop where contracts stop matching invoices | 31 | agrees | The chapter's judgement |
| 26 | Ch. 32's question: "what changes when the provider is the legal seller" | 32 (current excerpt and journal-spec question) | corrected to match | "…is the merchant of record" |
| 27 | Ch. 32: a merchant of record "resells your product and takes the tax, fraud and dispute liability" | 32 (rows 4, 18, 103) | corrected to match | Now "sells your product in its own name and takes over the indirect tax and the handling of fraud and disputes"; a parallel edit of 17:16 added that Stripe "leaves the cost of disputes with you" |
| 28 | Ch. 32: an operating model that a platform cannot use | 32 | agrees | — |
| 29 | Ch. 32: Managed Payments costs 3.5% on top of payment fees | 32 | agrees | — |
| 30 | Ch. 32: it excludes platform accounts | 32 | agrees | — |
| 31 | Ch. 32: Adyen states that it is not a merchant of record | 32 | agrees | — |
| 32 | Ruling 34 (Stripe's scheduling service is partly on record) | 27 | agrees | The page says nothing about how Stripe schedules renewals |

Counts: 32 statements checked: 25 agree, 7 corrected to match, 0 no longer in the chapter and removed.

## Re-check after chapter verification

Nothing. Chapter 32's verification file appeared during the pass and was applied (rows 9, 10, 26, 27).

## Other checks

- **KEY POINTS:** three; the first two match the chapters; the third was reworded (row 1).
- **Chapter paragraphs:** each names the chapter's question and its Larkfield case: Femke's inventory of two engines (27), Studio Noord's 1,240 and 1,324 messages (28), Mila's renewal of 1 and 4 April 2027 (29), two invoices with €0.00 (30), Ironworks Climbing's €1,890 and €144.99 (31), the chief executive's question answered no, twice (32).
- **Larkfield (one correction):** the lead said only that failure emails went to members who had done nothing wrong. Ruling 37(a) asks for both steps: the lead now says the job marked the 7,900 renewals failed with no card charged, and an email job that could not tell a decline from a card never charged sent failure notices. Checked and agreeing with the ledger: 1 October 2026, 7,900; 1 November 2026, new idempotency key, 1,840 members, €71,300, 212 disputes; €1,890 on 1 February 2027 and €144.99; Femke de Graaf's title; 1,240 and 1,324 in March 2027; Mila's €49.00, 1 and 4 April 2027; May 2027.
- **Links:** all six `[[permalink]]` targets are in the style guide's list; no external URL in the text. The range "Parts I to V" is plain text, as ranges are in the other intros; the page has no `[[part-5]]` link.
- **Length and format:** 1,198 words by `check_draft.py structure` (limit 1,200; it was 1,196, so the additions were paid for with small cuts inside units); `timetoread` 5 min (1,198 ÷ 230); unit count and order unchanged. `spec.json`: p01, p05 and p10 fields brought into line, changelog entry added.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build clean for this journal; render check OK.

## Concurrent edits

Another pass edited this page's `spec.json` (17:14) and its merchant-of-record paragraph (17:16) while this one ran, to reconcile them with chapter 32. The two sets of edits agree and both are in the file.

## Ledger conflicts

None found.

## For other pages

- `journal-spec.json`, Part VI opening bridge: it mentions the subscription "that renewed without them noticing"; the page keeps that sentence in a shorter form.
