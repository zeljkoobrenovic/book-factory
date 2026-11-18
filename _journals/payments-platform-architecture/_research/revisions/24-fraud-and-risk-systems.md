# Revision log — 24-fraud-and-risk-systems (draft check round 1, ESCALATE)

Revised 2026-11-17 (single revision; no second check). One line per failed result. No quotation, date, number, hedge, source entry, figure, caption or `[[link]]` changed; no fact added (the foundation model, K1 and the Connect point were already on the page and are only moved or glossed).

## Major

- one_controlling_idea_per_paragraph, Five Kinds ¶3: spec repair. Split into p10 (one verdict hides three prediction problems) and new p46 (rarity: the false positive), at "The second consequence comes from rarity". No sentence lost.
- evidence_is_explained, Adyen pipeline quotation: fixed. A sentence now says what it shows (the model judges a payment by the recent traffic of its slice, computed as it streams in, before the issuer is asked). p27 aligned.
- transition, Five Kinds opening: fixed. Picks up Femke's second question ("The second question starts with how the payment system learns of fraud at all.").
- transition, Threshold opening: fixed. Carries over the late and missing labels and answers Femke's third question (someone has to choose how strict it is). p21 aligned.
- transition, Card Testing opening: fixed. Contrast stated in prose ("The score, the threshold and the feedback loop all run on dispute labels. Card testing produces almost none"). p26 aligned.
- transition, In Practice ¶3 (Jonas's rule): fixed. Opens "Against that price set from costs came a rule argued from results." p37 aligned.
- transition, When It Goes Wrong opening (house format; transition strengthened): turns from Larkfield's working setup to three quiet failures. p38 aligned.
- flow and known_before_new, Mila and Larkfield before introduction (intro ¶3): the paragraph now introduces Larkfield and Mila first, then says her pass is not the chapter's kind of payment and names that kind (a typed card, as at her 12 January membership set-up and in the weekend's 61,000 attempts). Intro ¶4 no longer re-introduces Larkfield. p03 aligned.
- flow, "a property of an account": the three prediction problems are mapped to the table's rows in the sentence (merchant fraud named).
- flow, overloaded score paragraph: the probability-versus-rank caution now follows the definition; plan and deprecation details are grouped last as "Two Stripe details change what a merchant sees"; a closing sentence says what "the score" means in the rest of the chapter. p13 aligned.
- flow and known_before_new, traffic allocation in the requirements table: spec repair (gloss to the earlier unit). One sentence before the table defines it. p14 aligned.
- flow, "the two gaps": named in place (late labels; no labels for blocked payments).
- flow, Risk Beyond the Payment position: not moved (topical section, not house format; whole sections never move). Transitions strengthened: its opening ties it to card testing and to the fraud table's account row; the Where They Differ opening names "the account risk just described". Recommendation below.
- flow and known_before_new, K1/Keel: glossed ("Keel (Larkfield's 2027 program of eight fixed decisions for its payments)").
- flow, Connect parenthetical: shortened and moved to the end of the paragraph, after the proposal and its test.
- flow and known_before_new, payments foundation model: introduced in the body where Stripe's May 2025 claim is cited (same source), before the gap list. p29 aligned.
- known_before_new, risk profile: glossed before the configuration table. p23 aligned.
- known_before_new, account rules: clause added ("this chapter's rules are the transaction rules"); no definition invented.
- known_before_new, feature language and named infrastructure: "feature language" glossed; Spark/Kafka/Flink/Cassandra left as named systems (the reader is an engineer, style guide) with the new sentence saying what the pipeline does.

## Minor

- flow, probability vs rank in the pricing: one labeled sentence says the break-even chances set the direction per product, not a dial position, since neither provider maps its scale to a chance. p36 aligned.
- flow, model-lineage paragraph breaking the line (spec, one reader): not moved; it closes the learning section by design and the threshold section's new opening carries the line forward.
- flow, fraud-signals paragraph placement (spec, one reader): not moved; single reader, no clear reason to override the chronological order.
- flow, "only substantial description" vs the 2024 post: reworded "Beyond the 2024 post's model family and retraining interval, it is the only substantial description … that I found" (hedge kept).
- flow, "the last section returns to": now "When It Goes Wrong returns to".
- flow, scene question contradicted by its numbers: now "stop only part of an attack made entirely of stolen cards". p07 and section transition aligned.
- flow, first person in the synthesis: "leaves the price with the merchant, so as a merchant I would own…".
- flow, €15 cost step: "A fraud case takes the payment back, but the class seat it paid for cost almost nothing extra to provide, so the studio is out the €15.00 dispute fee".

## Content corrections

- None needed on the page. Spec only: p34 said "six things" not found; the page lists seven (Shield's production size included) — spec corrected. p20 said Adyen "has published nothing" about its fraud-risk model; the page cites its 2024 post (family, weekly retraining) — spec corrected. p10's evidence gave the value-based arithmetic (about ten per fraud) where the page uses the count-based rate (0.068%, about fifteen) — moved to p46 and corrected to the page.

## For the editor

- Risk Beyond the Payment, position ("The same structure, an estimate now and the facts later, applies to the business being paid."): recommendation: keep it where it is. The spec's reason holds (it changes the subject from payer to payee only after the payment argument is complete, and comes before the comparison so the underwriting gap is listed with the others), and the strengthened transitions now tie it to card testing, to the fraud table's account row and to the comparison table. If the editor wants it out of the Larkfield line, the only alternative is to fold its two paragraphs into the compliance and platform chapters it already hands off to, which is a structural change for the author.

## Spec changes

- p10 split (new p46); controlling ideas of p03, p07, p10, p13, p14, p20, p21, p23, p26, p27, p29, p30, p34, p35, p36, p37, p38, p43; `kinds` and `merchant-risk` transition_in; `kinds` flow rationale; `max_words` 6500 -> 6825 (5%); `revised` and changelog dated 2026-11-17.

## Checks

- `validate_spec.py payments-platform-architecture 24-fraud-and-risk-systems`: ok.
- `check_draft.py structure`: pass, 6,824 words (limit 6,825). `timetoread` 28 -> 30.
