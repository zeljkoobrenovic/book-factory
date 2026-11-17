# 08-payment-state-machines — revision after draft check round 1 (2026-11-24)

One line per failed result. Words: 5,507 before, 5,975 after (`max_words` 6,500, unchanged). `timetoread` 24 → 26 min. Callouts, figures, captions, links and Sources untouched; the only content correction is the one the editor authorized (marked EDITOR).

- one_controlling_idea_per_paragraph, p38 (spec): repaired. Split in spec and prose into p38 (legal transitions as a table) and new p38b (identity makes a message safe to apply twice, with the duplicate-event evidence); each opens by naming its guarantee. No sentence lost.
- evidence_is_explained, requirements table (p20): fixed. A sentence before the table says what it sets side by side (the response fast and partial, the outcome authoritative and possibly days later).
- transition, Silent Webhook paragraph (p08): fixed. Opens "The record was also wrong about payments it could describe."
- transition, opening of "Why a Yes-or-No Charge Stopped Working": fixed. Two sentences pick up Femke's question and say the history explains what the record is for.
- transition, two-questions paragraph (p14): fixed. Opens on the three failures and says they come down to two questions.
- transition, SetupIntent (p27): fixed. Opens "The PaymentIntent's machine has a sibling that reuses it."
- transition, opening of "Where They Differ": fixed. Opens on the contrast between designs a consumer chooses and differences it does not.
- flow_is_followable, position of "Where They Differ" (spec): house format; transition strengthened. The paragraph before it ends by saying the guarantees and designs give something to measure the providers against; the opening says the last column is read against them.
- flow_is_followable, second payment by Mila / "recurring payment": fixed. "The payment this book follows through every chapter is a different purchase of Mila's, her class pass".
- flow_is_followable, the two questions never put as questions: fixed. "must the customer act, and is the payment finalized only later?"
- flow_is_followable, first Adyen paragraph p28 placed before the definitions it uses (spec): NOT moved, for the editor (the move proposed is five places, beyond a local reorder). Eased in the draft: result code, modifications, `/sessions` and edge layer each glossed in a clause.
- flow_is_followable, "Succeeded | … | Nothing" (spec; EDITOR): fixed. Cell now: "No party closes it, and it is not final: a refund, a dispute or a late capture failure can follow, each a separate record"; p17's evidence in the spec changed to match.
- flow_is_followable, "Seven aspects separate what each company documents…": fixed in draft and in p41's controlling idea (the table gives, per aspect, what each documents and what the difference suggests).
- flow_is_followable, 12 January in the past tense: fixed. Marked as a replay through the redesigned record, in the present tense.
- flow_is_followable, "the payment returns to `authorized`": fixed. The paragraph now takes a payment that, unlike Mila's pass, was captured by a separate request.
- flow_is_followable (minor), `refunded` kept beside "two amounts and not a state": fixed. A clause says the word promises only that at least one refund is confirmed (the mapping table's wording).
- flow_is_followable (minor), the SEPA Direct Debit never worked in the In Practice section (spec, one reader): not repaired, for the editor. It needs a new unit with new scenario content.
- flow_is_followable (minor), where a refused or expired payment ends (`closed_reason`) (unclear, one reader): not changed, for the editor. Saying more than the page does would add a claim about the record's design.
- known_before_new, capture, dispute, `authorized` in the introduction and scene: fixed. Capture and dispute glossed in the introduction, `authorized` in the list of five states.
- known_before_new, 3-D Secure in the history section: fixed. One-clause gloss with a pointer to the next section.
- known_before_new, "the gap between the instant answer and the slow truth" (unclear): fixed. Now "this book's gap …", as chapter 7 words it.
- known_before_new, "edge layer": fixed. Glossed from the cited post, re-read for this revision ("Every API call to our systems goes through our edge services first"): "the set of services every API call reaches first".
- known_before_new, "Keel decision K2" (unclear): fixed. "K2, one of the numbered decisions of the Keel program".
- known_before_new, "card offers": fixed. Glossed from the cited webhook-types page, re-read for this revision ("The offer has expired, for example, because the shopper abandoned the session").
- known_before_new (minor), `pspReference`: fixed. Glossed at first use with a pointer down.
- known_before_new (minor), "inbox table": fixed. "in which each event is stored as it arrives".
- conclusion_synthesizes_and_answers_so_what: fixed. The spec's so-what is now the last two clauses of the first synthesis bullet.
