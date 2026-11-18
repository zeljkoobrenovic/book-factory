# Revision after draft check, round 1 — 05-payment-economics

Date: 2026-11-17. Report judged: spec `20286b4050d1d0a7`, draft `a553c6302953f1eb` (22 failed results: 17 major, 5 minor). One line per failed result. Words: 6,437 before, 6,823 after; `max_words` raised 5% (6,500 to 6,825). `timetoread` 27 to 30. Apart from the editor-authorized additions listed at the end, no fact, number, date, quotation, hedge, figure, caption, callout, source entry or existing `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- p15 (US debit cap, then the routing rule), spec: repaired. Split in spec and prose: p15 keeps the cap; new p52 holds the two-network routing rule. No sentence lost.
- p24 (which model suits whom, then the rule for comparing quotes), spec: repaired. Split: p24 keeps the recommendation and its limit; new p53 holds "never compare a blended rate with a markup", with one connecting sentence ("The first is a total and the second is one of its three parts").

## evidence_is_explained

- p15, $0.23 against $0.51: fixed. The sentence now ends "without the cap, the issuer receives on average more than twice as much" (the spec's "shows").

## transition_expresses_declared_relationship

- Questions to Ask (p50): fixed. A lead-in before the list carries over the take-aways.

## flow_is_followable (major)

- p03, a second €120 pass with nothing to tell it from Bram's: fixed. The paragraph says Bram's pass was the opening one and Mila's is a different payment, the one the book follows.
- p14, Stripe's Article 9 inference before blended pricing and Stripe's prices (spec): repaired inside the section. p17 (Stripe's four card prices) moved up to follow p13, so the inference block now follows both the prices and Article 9; p17 says each price is "a single rate for every card of its kind". The block's wording is unchanged and it stays with p14.
- p16, US litigation as a detour with two strands mixed: fixed. The debit strand is marked ("Take debit first"); the credit strand opens by saying there is no cap to strike down and that the open matter is a settlement over credit interchange, before the filing's dates.
- p17, "however" with nothing to contrast, Stripe's tiers a section early (spec): repaired by the same move. p17 now follows p13 (the capped cards and the exemptions), so the contrast holds; section order of units is p12, p13, p17, p14, p15, p52, p16; the section's flow rationale was rewritten.
- p25, failure-costs table before its terms (spec): repaired. The table moved to the end of the section (now evidence of p29) after the four paragraphs that explain its terms; p25 announces the order and the closing table and keeps the date convention.
- p38, list of unpublished prices in the section on what a provider builds (spec): not moved. It needs the chargeback fee from the failure-costs section and the next section's transition picks it up, and the report names no section where both readers would put it. Reworded instead: it opens on where the record on what the providers build stops, leads with the unpublished computation of network costs, and the roadmap (p04) now announces "where the public record stops".
- p30, nested net-revenue quotation: fixed. The paragraph says Adyen's definition deducts other costs, quotes it, says the two deducted costs are not interchange and scheme fees, and ends the labeled reading on what that makes net revenue.
- p33, 21%, 8% and 18% without the linking step: fixed. One sentence says what the one customer did to volume growth and that revenue grew with the others' volume; the reading is still labeled as the author's.
- p42, "the acquirer, by inference": fixed. One sentence gives the reason from the ledger and ruling 27 (Adyen publishes where it acquires, not which entity acquires in each country) and points to the next chapter.
- p44, "That answers Priya" (spec): fixed in the draft and recorded in the spec's p44. The sentence now answers her second question (forecasting) by name and says the first (why nearly two-thirds goes out) cannot be answered from one payment: €0.61 of €2.53 is about a quarter, and the two-thirds is the 2026 total over every method and both providers. The ledger gives no breakdown, so none is invented.
- p45, "the one payment in the ledger": fixed. Bram de Wit's pass is named as the payment from the chapter's opening.
- p46, "his bank" without antecedent: fixed ("Bram de Wit's bank").

## flow_is_followable (minor)

- p06, a February scene reading Mila's March payment (spec): fixed. "A payment such as the one Mila will make in March, a €120 pass on a Dutch debit card"; spec wording aligned.
- p03, "illustrative €0.61" unexplained: fixed. One sentence says every Larkfield figure is an assumption made for teaching.
- p39, the "blended rates" cell not stated earlier: fixed. p21 now states the fact with its source and date (see additions).
- p42, €0.11 against the published $0.13: fixed. The parenthesis says the page gives $0.13 and that €0.11 is the fixed fee of Larkfield's assumed rate.

## known_before_new

- "Extended authorization" (major): fixed. Glossed at first use in p27 from p35 ("approvals held open beyond the standard window, for up to 30 days"); the table that used it earlier now comes after.
- "Merchant service charge" (minor): fixed. Glossed in p14 as the regulation's name for the previous section's merchant discount rate.

## Cheap fix from a passed result

- AC-3 note: the Adyen 2025 growth figures now carry their date inline (12 February 2026, as in Sources).

## Editor-authorized additions (content, each against the page's own sources)

- p21: Adyen's platform documentation (n.d., accessed November 2026) defines a fee type as "The transaction fee due to Adyen under blended rates" (verification row 67; Sources entry "Transaction fees"). It was only in the comparison table.
- p42: a new `[[acquiring-and-network-connectivity]]` link for the acquirer-of-record point (ledger line `01-journey-of-a-payment`; ruling 27).

## Judged wrong

- None.

## For the editor

- None. No failure required a change of claim, a moved section, or a change to intent, thesis, role or acceptance criteria.

## Checks

- `python3 _wiring/validate_spec.py payments-platform-architecture 05-payment-economics`: ok.
- `python3 _wiring/check_draft.py structure …/05-payment-economics`: pass, 6,823 words.
- No readers run, no `check-report.json` written, no build run.
