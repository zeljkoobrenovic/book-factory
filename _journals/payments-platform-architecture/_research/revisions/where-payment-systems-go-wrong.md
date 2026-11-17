# Revision log — where-payment-systems-go-wrong (draft check round 1, ESCALATE)

Revised 2026-11-24. One line per failed result. No fact, number, date, quotation, hedge, source, figure, caption or `[[link]]` changed.

## Major

- one_controlling_idea_per_paragraph, Introduction ¶2 (p02; spec fault): agreed. Split in spec and prose: p02 keeps the first-day origin and no-blame point; new unit p129 holds "The patterns also chain…" (sentence unchanged). `thesis_statement.placement` now names p02 and p129.
- one_controlling_idea_per_paragraph, Sixteen Patterns ¶12 (p15; spec fault): agreed. Split in spec and prose at "Where the confirmed record lives also differs by provider"; new unit p130 carries the Stripe/Adyen evidence, p15 keeps the cause. Sentences unchanged. Kept in place (not moved to the remedy), since a move was not needed to fix the failure.
- evidence_is_explained, ¶105 (p108): fixed in draft. Added the sentence the spec's `shows` states ("Both proposals borrowed an answer to a problem Larkfield had not measured") and pointed the per-account limit to The First of the Month, where it is told.
- flow_is_followable, ¶63 (p66, the K8 switch): fixed in draft. One clause says what the rehearsed switch is, in the words of The Single Rail entry.
- flow_is_followable, ¶103 (p106, evidence-age note mid-sentence): fixed in draft. The note, unchanged, moved to directly after the sentence it qualifies.
- flow_is_followable, ¶105 (p108, "the same Black Friday figure"): fixed in draft. Reworded so the figure is cited by him against the wave, and "the same" is replaced by "of this entry's opening quote".
- flow_is_followable, Chains ¶2 (Version Cliff, Open Till, Accidental Bank links name no money-truth pattern): fixed in draft by one sentence in the lead paragraph (p118) saying that a few links end in wrong money that none of the five names covers. NOT fixed by assigning each link a money-truth pattern: that would be a new claim. For the editor if the mapping is wanted.
- flow_is_followable, Chains ¶3 (p120, Vault Hostage; judged spec fault): fixed in draft only. A connecting clause ("and so it joins the scale chain at the Single Rail") ties the link to the frame; the spec's p120 already says the Vault Hostage feeds the Single Rail, so no spec change was needed. Figure 3's caption untouched.
- flow_is_followable, Chains ¶5 (p122, "keeps both providers and adds no orchestration product"): fixed in draft. The clause is now its own sentence, introduced by "None of these is a new provider".
- flow_is_followable, Using the Patterns ¶1 (p123, referent of "It"): fixed in draft ("The failure shows…").
- known_before_new, ¶14 (Silent Webhook named before told): fixed in draft with a one-clause gloss of the incident.
- known_before_new, ¶21 (Unexplained €0.4 Million named before told): fixed in draft with a one-clause gloss (the difference between Larkfield's books and its providers' balances). The sum of the two figures was not added (it would be a new number).
- known_before_new, ¶63 (K4 and the exit sheet): fixed in draft. K4 glossed in one clause from the scenario ledger (card numbers never touch Larkfield; provider tokens only), which also says why the exit sheet sits under it.
- known_before_new, ¶22 (K3 never stated): fixed in draft. K3 glossed at first use from the ledger ("every movement gets a ledger entry").
- known_before_new, table (reserves; spec fault): repaired in spec and prose. Gloss moved up from p05 into p04, before the table; p04's controlling idea says the table's terms are glossed first.
- known_before_new, table (chargeback; spec fault): same repair, gloss in p04 in the entry's own words; the entry gloss stays.
- known_before_new, table (payout; spec fault): same repair.
- known_before_new, table (token; spec fault): same repair.
- known_before_new, table (acquirer; spec fault): same repair.
- known_before_new, ¶2 (disputes in p05; draft fault): fixed by the dispute gloss in p04, which precedes p05.

## Minor

- flow, ¶8 (p11, retry after a timeout versus the next scheduled attempt): not changed. One reader only; explaining the retry schedule here would add content the ledger places under K1 and dunning, and the other reader found it fine.
- flow, ¶14 (p17, three nested definitions): fixed. The SEPA Direct Debit definition is now its own sentence before the main clause.
- flow, ¶21 (p24, "Whose money pays this?"): not changed. One reader only; the quote and its tense are a ledger scene, and the answer is the remedy unit that follows (a written rule for who funds a refund after payout).
- flow, Chains ¶4 (p121, "its refused requests"): fixed ("the peak's refused requests").
- flow, Using the Patterns ¶2 (p124, opening customer and the Silent Webhook): fixed with a comparison ("like the members turned away on the morning of the Silent Webhook"); the page does not claim they are the same event.
- Judge's note on p32 (spec says the reconciliation runs "when that provider's reports are ready"; p31's draft says "nightly"): not changed. Changing either is a change of a claim (consistency ruling 28). For the editor.

## Spec changes

- p02 split, new p129; p15 split, new p130 (evidence moved with it); p04 controlling idea extended with the table-term glosses; section flow note records the extra unit; `max_words` 6500 -> 6825 (5%), because the glosses and clauses add about 240 words and the page has no connective text of that size to trim; changelog entry dated 2026-11-24.

## Checks

- `validate_spec.py payments-platform-architecture where-payment-systems-go-wrong`: ok.
- `check_draft.py structure`: pass, 6,736 words (limit 6,825).

## Round 2 (items selected by the coordinator; prose only, spec unchanged)

- K8 forward reference in The Vault Hostage (p66): the switch is now stated plainly in its own sentence before it is used; the exit sheet and K4 have separate sentences.
- "the Black Friday figure of this entry's opening quote" (p108): his argument (152,000 a minute against about 1,000) and why her answer follows (load for all customers together, as the entry's mechanism says) are stated in place.
- Custom connected accounts (p87): added the sentence the spec's evidence `shows` states (the provider announced the change; nobody at Larkfield owned the deadline). Existing gloss kept.
- Stripe's embedded onboarding component (p88): one clause, from platform-onboarding-and-verification.
- Signpost sentence in the chains lead (p118): kept, now names the three links (Version Cliff, Open Till, Accidental Bank) and says the five money-truth names do not cover them.
- "a Black-Box Balance seen from the seller's side" (p120): the missing step added (a platform that does not mirror the requirement cannot say why the money is held).
- "rail" (p91): one clause in The Single Rail's first unit.
- "One writer" (p11): one clause, from K1.
- "five payments terms" (p04): now six, and the sentence says the table and the paragraph after it.
- "bank redirect" (p60): one clause, with iDEAL as the example.
- Trimmed to stay within max_words: the connective opening of the hand-off paragraph and a few words elsewhere; no evidence removed.
- `timetoread` 28 -> 30 (6,824 words / 230).
- Not addressed, by the coordinator's selection: p04 glossary as a unit of its own; Borrowed Blueprint's family; time order in p24; "noticed as this pattern" in p17; K numbering; Card in the Log's two subjects; "capturable" and "reversals"; "drop-in".
- Checks: validate_spec ok; structure pass, 6,824 words (limit 6,825).
