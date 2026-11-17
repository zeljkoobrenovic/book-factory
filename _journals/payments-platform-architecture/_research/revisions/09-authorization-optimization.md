# Revision after draft check, round 1 — 09-authorization-optimization

Date: 2026-11-24. Report judged: spec `399abeb3efade3f0`, draft `ed044a9e3412d4b7` (24 failed results: 16 major or blocker, 8 minor). One line per failed result. Words: 6,127 before, 6,586 after; `max_words` raised 1.5% (6,500 to 6,600). `timetoread` 26 to 29. Apart from the editor-authorized corrections listed at the end, no fact, number, date, quotation, hedge, figure, caption, callout or `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- p22 (retry policy, then what the vendors publish about results): fixed in the draft. The sentence on unpublished recovery rates, with the 4% and the 55%, left p22 and its figures went to p33, where the spec assigns them.

## evidence_is_explained

- p40, test-plan table: fixed. The lead-in now says each row applies one of the six rules, with the size from the rule of thumb.

## transition_expresses_declared_relationship

- When It Goes Wrong: fixed. The section opens "A test like Larkfield's is optimization going to plan; in production it goes wrong in three ways."

## flow_is_followable (major)

- p02, "The remote system here": fixed. The spec's bridge sentence now precedes it.
- p14, 82.3% against the scene's 82.0%: fixed ("The 82.3% is Adyen's rate per attempt; the scene's 82.0% was Stripe's").
- p34, "the third design" before the table: fixed. The paragraph names the three designs before the rule, and the sentence reads "Adyen provides for the third design, the merchant's own schedule".
- p36, cells "cited earlier" that were not: fixed by citing both earlier. p23 quotes Stripe's "Excessive retry prevention" (same documentation page as decline prevention, fetched 24 November 2026); p24 quotes Adyen's refusal reason 46.
- p37, the Checkout API clause: fixed. It is now its own sentence, tied to the attempt records ("Those records depend on webhooks: …").
- p33 after the six rules (spec): repaired in spec and prose. p33 now precedes p32; both transitions and the section's flow rationale were rewritten. The Mastercard sentence stays in the unit, now introduced as a gap on the network side.

## flow_is_followable (minor)

- p07, "They are this chapter's sections" (spec): fixed in prose and spec ("the subjects of the next four sections").
- p40, test-plan row against K5, and the date of the test: no action; settling it needs a fact the ledger does not give. For the editor.
- Position of "Stripe and Adyen: Where They Differ" (spec): house format; transition strengthened (last sentence of p34 and first sentence of p36).
- Visa table, "within the limit": no action; one reader, and the fix cost words the page does not have.
- p45, blended pricing first met in the take-aways: no action; one reader.

## known_before_new

- 3-D Secure in the counting section: glossed at first use; the later gloss removed. The opening sentence no longer counts "three sources of failure".
- "Acquiring": glossed in p12, before the table that first uses it; p20's duplicate gloss removed.
- Penalty fee behind a block: p08 now says "to avoid a fee the card network would charge for the attempt"; p15 no longer redefines the blocked payment with a different reason.
- Keel and its numbered decisions: glossed in p05 from the ledger ("Keel, the 2027 program to steady Larkfield's payments estate").
- Tom Hendriks: role added from the ledger ("the senior engineer who built Larkfield's payment service").
- "Larkfield's own five states": the five states are named, from the ledger.
- "Authenticate module": glossed ("the Uplift module for cardholder authentication").
- "the ledger's method mix" (minor): reworded ("Larkfield's mix of payment methods"), and "across both providers" added.
- MAC (minor): attached to "Merchant Advice Code"; "could not be read" now says "for this chapter".

## conclusion_calls_back_to_introduction

- Fixed. The first synthesis bullet returns to the member refused with code 05, in the words of the spec's callback.

## AC-3 (blocker), editor-authorized content corrections

- Stripe's "55%": moved to p33 and quoted from Stripe's Billing product page (n.d., accessed November 2026): "Businesses using Stripe recover 55% of failed payments on average", with its scope (the preceding sentence names Smart Retries, the card account updater and cancellation surveys together; not a Smart Retries figure; ruling 37c). Wording confirmed by fetch on 24 November 2026. Sources entry added, as in chapter 29.
- Adyen's "4%": quoted in p33 from the guide of 16 June 2026: "Pinterest saw a 4% improvement in recovery rate on retried transactions, with expectation of reaching 10% over time"; one customer, no baseline (ruling 37b). Confirmed by fetch. Sources entry added, as in chapter 29.
- Adyen's "11% and 12%": quoted from the press release of 22 September 2026: "an 11% increase in payment conversion" at Too Good To Go (the customer's words: "11% relative increase during the pilot") and "an 12% increase in payment conversion on the eligible traffic" at Just Eat Takeaway.com; labeled testimonials for one module with no baseline or method (ruling 31d). Confirmed by fetch. Existing Sources entry reworded to say so.
- Spec p33 evidence corrected: it still listed "any figure after Adyen's pilot of 60" as not found, against the verified page.
- No figure was removed as unsupported.

## For the editor

1. p40, "A schedule driven by decline category and Mastercard advice code, against the current fixed schedule": one reader could not square it with K5 ("retries on a schedule tied to decline codes") or date the test against Mila's April renewal. Recommend one ledger line saying the test is how the K5 schedule was chosen, and its month.
2. `max_words` is now 6,600, over the style guide's 6,500. Recommend accepting, or cutting original prose, which a reviser may not do.
