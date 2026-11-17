# Revision after draft check, round 1 — 06-acquiring-and-network-connectivity

Date: 2026-11-24. Report judged: spec `8822bc85ad1bc19f`, draft `b0f417a5a50b6b5c` (25 failed results: 2 blockers, 19 major, 4 minor). One line per failed result. Words: 5,993 before, 6,595 after; `max_words` raised 2.3% (6,500 to 6,650). `timetoread` 25 to 29. Apart from the editor-authorized corrections listed at the end, no fact, number, date, quotation, hedge, figure, caption, source entry or existing `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- p30 (where Adyen's route stops, then what Adyen publishes about entities and memberships), spec: repaired. Split in spec and prose: p30 keeps the 84%, the banking partners and pass-through payout, followed by the inference block; new p52 holds what Adyen publishes (14 acquiring connections, entities for some markets) and what it does not (entity per country, memberships by network and country). No sentence lost.

## evidence_is_explained

- p30, pass-through payout in Africa, Brazil and India: fixed. The term is glossed from chapter 3 and the sentence says what the fact shows (the other payout models are not available there; the page does not name the acquirer), with the reading labeled as the author's.

## transition_expresses_declared_relationship

- Section "What the Acquirer of Record Changes": fixed. The opening carries over the acquirer of record as a legal fact separate from the wire and says what it changes, before "Start with what 'domestic' means".

## flow_is_followable (major)

- Adyen before Stripe (spec): repaired without reordering. The Adyen section opens with the reason (the simpler case first, one company on one route; Stripe combines the first two routes and resolves the opening puzzle); the spec's flow rationale and the section's `transition_in` say the same.
- "Two Words" in the scene heading against "Two words carry the chapter": fixed. The scene and the roadmap name the two words ("local acquiring"); the definition paragraph now says "Two words of that definition matter most here".
- p11, "Those two activities" and "the table" before it appears: fixed. The paragraph names the two activities, and the pointer to the table is its last sentence.
- p18, the step from the two rules to "local acquiring": fixed. Three sentences join the definition and the jurisdiction rule before the term.
- p24, "I read two of the six": fixed. The paragraph says the disclosure names six US acquirers (set out in the Stripe section) and which two sets of terms were read and where each is described.
- p24, nested conditional on the Cross River terms: fixed. Two sentences; the condition has its own subject. "Registered with a network" is the terms' wording and is left unexplained because the source does not explain it.
- p30, "runs the other way": fixed by the split; p52 opens by saying what the reverse is.
- p38, Adyen's 2021 naming of Visa and Mastercard referred to as if shown: fixed. The sentence says it is not quoted in this chapter and where it stands (the US branch release of 14 June 2021; verification row 80).
- p39, 1,140 studios as a new fact, merged table row: fixed. The lead says the fact comes from Larkfield's own records (ledger); the merged row is split into a Netherlands and Germany row and a Belgium row, as the spec lists them.
- p44, "Keel" and "decision K8": fixed. Tied to where the book introduces them (`[[meet-larkfield]]`).
- p46, "The Single Rail in its acquirer form" (fault unclear): fixed. The sentence now gives the explanation (every payment from the new country depends on the one acquirer the business already had). The first failure is named as The Single Rail in the opening callout's sense and the second as The Accidental Bank, so both announced patterns are tied to a failure; spec evidence for p44 to p46 records this.
- p04, the answer and a caveat about the license page before the question: fixed. The answer is stated for Mila's payment with a dated source and one clause of reason.

## flow_is_followable (minor)

- Scene: "local acquiring" raised and not signaled: fixed. The roadmap and the opening of the local-acquiring section say where the two words get their meaning.
- Figure 2 caption against the text: fixed in the text (captions are untouched). p18 ends by saying the license matters through the outlets it permits; p40 says why the change of acquirer left the status unchanged.
- p33, Stripe still a payment facilitator under its own bank: fixed. One sentence says what changes is whose the member bank is.

## known_before_new

- "Payment facilitator" and "limited-purpose bank" in the hook (major): fixed. One parenthesis after the quotation, from the body's definitions.
- "Full-stack" (major): fixed. Glossed at first use in p30, with the reading still labeled by the block below it.
- "Pass-through payout" (major): fixed. Glossed in p30; "payout model" in p37 is spelled out.
- "Payment Aggregator", "Independent Sales Organization" (minor): fixed. One sentence in the table's lead says a named institution other than Stripe is the acquirer under both.

## conclusion_calls_back_to_introduction

- Fixed. The "Established" list opens by returning to the two Stripe statements of 2020 and 2026 and why both are true.

## AC-3 (blocker)

- "a member of the Networks": fixed. Each set of terms carries its date inline (EEA entity: terms n.d., accessed November 2026; US limited-purpose bank: terms last updated 28 May 2026), as in Sources.
- "my reading of Adyen's license page" in the introduction: fixed. The page is dated at first use (n.d., accessed November 2026).

## Cheap fix from a passed result

- Synthesis: the second half of the declared synthesis (public claims attach to the provider) is now stated in the author's first bullet.

## Editor-authorized corrections (content, each against Sources, the verification file, the rulings or the ledger)

- Introduction ¶4: "Adyen names no acquiring entity per country" became "Adyen publishes no complete list of acquiring entities per country", the wording of rulings 46(j) and 47(j) and of the page's own inventory table.
- Uplift table: the spec's evidence for p20 now lists the Twilio row and its source (verification rows 31 and 32); the page was already correct.
- In-practice table: the merged Stripe row split in two; counts unchanged (1,140 and 650).
- New links: `[[clearing-and-settlement]]` (pass-through payout) and `[[meet-larkfield]]` (Keel).

## Judged wrong

- None.

## For the editor

- None. No failure required a change of claim, a moved section, or a change to intent, thesis, role or acceptance criteria.

## Checks

- `python3 _wiring/validate_spec.py payments-platform-architecture 06-acquiring-and-network-connectivity`: ok.
- `python3 _wiring/check_draft.py structure …/06-acquiring-and-network-connectivity`: pass, 6,595 words.
- No readers run, no `check-report.json` written, no build run.
