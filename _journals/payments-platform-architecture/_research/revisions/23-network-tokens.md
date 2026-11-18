# Revision log — 23-network-tokens (draft check round 1, ESCALATE)

Revised 2026-11-17 (single revision; no second check). One line per failed result. No quotation, date, number, hedge, source entry, figure, caption or `[[link]]` changed, except the content correction listed below.

## Major

- evidence_is_explained, Doist figure (uplift ¶2): fixed. The sentence now says it is one customer's figure outside the four, credited to network tokens and the card account updater together (verification claim 57), "again a bundle, not the token". p27 aligned.
- transition, push section opening: fixed. Opens from "tokens now sit behind stored cards, wallets and network checkouts" and says why (the networks push for it): cause and effect.
- transition, Where They Differ opening (house format; transition strengthened): the opening now names the three designs and which each provider documents (both default to the first; Adyen documents the second as a mode, Stripe only mentions it), and says the differences follow the requestor. p33 aligned.
- transition, When It Goes Wrong opening: fixed. Contrasts Lotte's renewal and the rule written in time with four ways tokens go wrong. p38 aligned.
- flow, Mila/Lotte/unnamed member: spec repair (ledger canonical). Intro ¶3 now names Lotte Smit as the member of the opening and the chapter's case; Mila appears only for her €120 pass (intro ¶3, wallets ¶1). Hook "gym" -> "studio" (Studio Noord is a yoga studio). p03 controlling idea and evidence, hook, sources entry aligned; p37 evidence no longer cites Mila's membership.
- flow, "They order this chapter": made true. Scene ¶3 names which section answers each question (two-tokens: first two; mechanism: third; push: fourth). "The old kind" -> "a card number without a token" (also fixes the minor item). p07 aligned.
- flow, "we automatically swap that": the swap is paraphrased before the quotation (the stored card swapped for a network token on the way to the bank).
- flow, two EMVCo quotations in one sentence: split into two sentences, each saying which token it describes; acquirer gloss attached to the first.
- flow, AI-agents detail: moved to a closing parenthesis; the hedge ("in its guidance for AI agents") kept.
- flow, cryptogram sentence relying on the merchant-managed mode: mode flagged as "described below"; consequence for the case stated ("So in those examples a renewal like Lotte's carries none"). p14 aligned.
- flow, promises table lead-in and "these features": lead-in now says four promises reduce to two and the right column draws on the steps and the providers' caveats; cell reads "for the features its payments-optimization page describes". p17 aligned.
- flow, wallets section position: opening sentence says why it comes before the push (Mastercard's aim of ending manual card entry runs through Click to Pay); the push opening picks up wallets and network checkouts. p18 aligned.
- flow, "the framework": now "Visa's Secure Credential Framework".
- flow, Visa revenue claim mid-sentence: split; the nearest basis is introduced as belonging to a different claim in the same release.
- flow, feature-flag digression: compressed into a parenthesis on the field sentence; facts kept.
- flow, portability paragraph: sentences reordered inside the unit: restriction, then the one answer (Adyen's sharing service), then the silences. p32 aligned.
- flow, Larkfield's own fee: parenthesized as "Larkfield's own platform fee … came out as usual".
- flow, both providers: intro ¶4 now says each studio takes online payments through Stripe or Adyen; fee paragraph says "For its studios on Stripe". p04 aligned.
- flow, rehearsed switch / planned migration: K8 named; migration made conditional (content correction below).
- flow, evidence-age marker: glossed at first use ("Older evidence carries its age:"); *illustration* and *assumption* glossed at first use in In Practice.
- flow, failure patterns never named again: each failure that answers a callout pattern now names it (The Phantom Payment; The Borrowed Blueprint on the cost side; The Vault Hostage). p38, p40, p41 aligned.
- flow, hand-off read as part of the questions: hand-off now opens "One question is missing from that list, because no token answers it." p46 transition aligned.
- known_before_new, "card scheme": glossed at first use (provisioning quote) as Adyen's word for the card network.
- known_before_new, 3-D Secure: gloss moved up to its first use in the wallets section (removed from the push section).
- known_before_new, randomized holdout: glossed.
- known_before_new, K4/Keel: Keel glossed ("its 2027 program of eight fixed decisions for the payments estate"); K4's quoted scope kept.
- known_before_new, Authenticate: glossed as Adyen's cardholder-authentication module, part of Uplift (as chapters 9 and 25 describe it).
- conclusion_synthesizes_and_answers_so_what: synthesis (one change from four sides) and so-what (four costs of treating tokens as a switch) added to the author's synthesis list. p44 aligned.
- conclusion_calls_back_to_introduction: callback to Lotte's renewal added in the same bullet (network re-pointed, Adyen chose to send it, the stale 4417 left to Larkfield).

## Minor

- flow, Figure 1 caption (who holds the network token): caption untouched; p11 prose now says the requestor holds it and the network keeps it current.
- flow, account updater returning under other names: one sentence says updaters return in fee lines and in Stripe's bundle.
- flow, "from a discount" not established: now "Tokens are still cheaper to process, but…", after Adyen's quote.
- flow, India "vault excluded" vs Stripe quote: reworded ("the provider's own vault may no longer hold the card number, and tokenizing a card needs the customer's consent").
- flow, Spreedly "contrast case" / TR-TSP vs roles: "contrast case" removed; "an independent vault, one that is not a payment provider"; TR-TSP glossed as a requestor serving many merchants.
- flow, renewals and the fee: "so many renewals may be exempt" added after the bulletin quote.
- flow, "the standard": now "The EMV tokenization standard".
- flow, "Only the network token stays valid" vs table: p11 reworded (the provider token is unchanged but may point at a stale number). p11 aligned.
- flow, Guest Checkout sentence: the fee is named in the prose (Customer Performance Development Fund).
- flow, Femke's inventory: "the acquirer inventory she started in February".
- known_before_new, interchange: glossed at first prose use.
- known_before_new, basis points: KEY POINTS callout glossed "(0.06 percentage points)"; definition moved before the first quoted amount.
- known_before_new, customer-initiated: glossed.
- known_before_new, EMV: glossed (Europay, Mastercard, Visa; glossary).
- known_before_new, blended rate and pass-through: glossed in place.

## Content corrections

- "its planned migration of 1,140 studios from Stripe to Adyen does": no ledger line plans or dates that migration (verification file, final note; ledger lines 30–32 and chapter 48's decision to keep both providers). Now conditional: "moving the 1,140 Dutch and German studios still on Stripe for online payments to Adyen would"; "Larkfield will measure it" -> "to be measured on the first batch of studios moved". Spec p41 evidence aligned.
- Hook "gym membership" -> "studio membership" (Studio Noord is a yoga studio; ledger).

## For the editor

- None. All failures were judged right and fixed in the draft or by the spec repairs allowed.

## Spec changes

- Hook content; controlling ideas of p03, p04, p07, p11, p14, p17, p18, p27, p32, p33, p38, p40, p41, p44; evidence of p03, p27, p37, p41; transitions of p03 and p46; ledger source entry; `max_words` 6500 -> 6825 (5%); `revised` and changelog dated 2026-11-17. No unit added, moved or removed.

## Checks

- `validate_spec.py payments-platform-architecture 23-network-tokens`: ok.
- `check_draft.py structure`: pass, 6,821 words (limit 6,825). `timetoread` 27 -> 30.
