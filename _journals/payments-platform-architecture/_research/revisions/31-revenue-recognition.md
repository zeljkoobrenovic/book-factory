# Revision log — 31-revenue-recognition (draft check round 1, ESCALATE)

Revised 2026-11-17. One line per failed result. No fact, number, date, quotation, hedge, source, figure, caption or `[[link]]` changed, except the content corrections listed below.

## Major

- evidence_is_explained, five-steps table third column (p08): fixed in draft. One sentence reads the column: a billing system holds lines, amounts and periods, but the contract is often outside it, and the split of the price across promises is judgement it holds only when each line is one promise.
- transition, where-to-stop opener (p23): fixed in draft. Opens on the provider asymmetry ("Because one provider documents a schedule and the other none, where the schedule is kept is a choice the business makes for itself").
- transition, where-they-differ lead (p27): house format; transition strengthened. The lead carries over the designs and the export and says why the comparison comes before Larkfield chooses.
- transition, in-practice opener (p29): fixed in draft. Picks up the comparison ("Larkfield bills on Stripe and takes payments on both providers, so that comparison decides where its schedule can live").
- flow, where-they-differ position: waived in the report (house format); handled by the lead sentence above.
- flow, Mila paragraph between thesis and roadmap (p03; spec fault, both readers): spec repair, local order inside the introduction. p03 now follows the roadmap (p04), so the thesis leads straight into the plan; transitions of p03, p04 and the scene updated. Content unchanged except the gloss below.
- known_before_new, "earned" and the two kinds of revenue in p03 (spec fault): fixed with one clause ("earned, in the accountant's sense of counting as revenue"); the paragraph already names both kinds in plain words.
- flow, "third of this part's failures of time" (p02): fixed in draft. The first two are named from the part introduction (October's delayed renewals, November's doubled ones).
- flow, FASB research aside (p08, both readers): shortened in place to the point it supports ("The steps below are quoted from the IFRS Foundation's summary; I did not read the text of ASC 606 itself"). The 403 and the archived copy stay in the Sources entry, so nothing is lost.
- flow and known_before_new, Orb quoted before introduced (p11, both readers): fixed in draft at first use ("Orb, a billing company that Adyen has owned since 1 July 2026", as in KEY POINTS and p22).
- flow, "Both vendors" (p15, both readers): fixed ("Both Stripe's and Orb's products").
- flow, revenue-contracts parenthetical (p20, both readers): fixed in draft; one sentence now says what was not found and where, with "which do not list every page" in place of the parenthetical example (the example stays in the Sources entry for the standalone selling price page).
- flow, €5.18 × 28 ≠ €144.99 (both readers): fixed in draft ("€5.18, rounded; the table multiplies the unrounded rate, so 28 days give €144.99"). Ledger: €1,890 / 365 × 28 = €144.99.
- flow and known_before_new, Keel and K7 (both readers): fixed in draft ("decision K7 of Keel, Larkfield's 2027 program to repair its payments estate", from the ledger).
- flow and no_weak_conclusion_pattern, €157.50 first in the conclusion (both readers, judge): fixed in the body. p10 now says "two of twelve equal months of €157.50" beside €315.00 (€1,890 / 12); the conclusion is unchanged.
- flow, "turn out" in the synthesis (p39, both readers): fixed ("Read together, this chapter and the two before it treat one invoice line three ways"), so it claims a reading across the part, not a result of this chapter.

## Minor

- flow, why Connect matters (p17): fixed, one clause ("which matters for Larkfield's own fees later in this chapter").
- flow, what "available" refers to (p17): fixed ("this support is available for destination charges to all users of the product, and for other charge types on request").
- flow, subledger first defined in the inference box (p19): not changed. The word is Stripe's own and the callout is where the chapter reads it; moving the definition out would split the labeled inference from its evidence.
- flow, who owned the integration when (p05): fixed ("is still owned by the growth team at that close"; p06 keeps the May 2027 handover).
- flow, "contracts equal invoices" undefined until the designs section: fixed with a one-clause gloss in p02 ("where an invoice line no longer stands for one promise to the customer").
- flow, the Adyen search account (p21; spec fault): not changed. The spec requires the search to be shown so the reader can repeat it.
- flow, export table repeats the four-input table (p26): fixed; p26 names what the export adds (each dated adjustment and, for usage, the date of use).
- flow, SMS overage row before usage is explained (p07; spec fault): not changed. p07's sentence already states that the messages are sent in March and invoiced in April, which is all the row needs; the general rule stays in the mechanism section.

## Spec changes

- Introduction order p01, p02, p04, p03, with transitions updated; scene carry-over updated; controlling ideas of p02, p03, p08, p10, p11, p26, p29, p31 extended to match the prose; `max_words` 5500 -> 5775 (5%), because the glosses and transitions add about 200 words and no connective text of that size could be cut without evidence; changelog entry dated 2026-11-17.

## Checks

- `validate_spec.py payments-platform-architecture 31-revenue-recognition`: ok.
- `check_draft.py structure`: pass, 5,602 words (limit 5,775).
- `timetoread` 23 -> 24 (5,602 / 230).
