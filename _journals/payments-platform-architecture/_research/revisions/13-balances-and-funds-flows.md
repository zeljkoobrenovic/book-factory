# Revision after draft check, round 1 — 13-balances-and-funds-flows

Date: 2026-11-24. Report judged: round 1, 17 failed results (12 major, 4 minor, 1 waived). One line per failed result. Words (structure count): 5,924 before, 6,274 after (`max_words` 6,500, unchanged). `timetoread` 25 to 27.

## one_controlling_idea_per_paragraph

- Adyen ¶3 (p19), adjustments and fees: fixed in spec and prose. Split into p19 (adjustments booked as they occur; the batch mixes one day's sales with other days' debits) and new p19a (fees reach the merchant twice), with a transition_in.

## evidence_is_explained

- Introduction ¶2 (p02), Adyen quotation and Stripe fact: fixed. A sentence before the pair asks whether "available" means the network has paid; a sentence after it says what the pair shows (one provider states the assumption, the other does not).

## transition_expresses_declared_relationship

- Where They Differ ¶1 (p38): fixed; house format, transition strengthened. The opening names the entry model that maps both providers by function and presents the six differences as what that mapping has to absorb, saying why the comparison comes here.

## known_before_new

- `created` used as known (p21): fixed. `created` (when the entry was booked) added to the Stripe field list in p14 (spec evidence updated).
- "negative refund allowance" (p20): fixed. Glossed with Adyen's own definition from the Balances page (a cited source).
- Buffer and `DepositCorrection` in the table before they are explained (p28): fixed. The lead-in now says the holds and the merchant's buffer are explained after the table.
- "settlement delay" meaning the scheme's delay (p22, minor): fixed with a parenthetical gloss.

## flow_is_followable (major)

- IN THIS CHAPTER "three balances" read as pending/available/reserved: fixed (content point). The callout names the three figures: the studio's share, Larkfield's fee and the processing cost.
- Introduction ¶2, quotation answers a question not yet asked: fixed with the same sentence as the evidence fix above.
- 1,140 studios vs Studio Noord: fixed against the ledger (Studio Noord on Adyen since 2024; the 1,140 are NL/DE studios onboarded before 2024, Stripe online and Adyen terminals). Prose now says Studio Noord saw one total and the 1,140 saw two.
- "The two statements" in the pre-funding paragraph: fixed. Now names them: the annual report's wording against the two statements in the terms and the documentation. Hedge unchanged.
- "Six kinds" vs heading (p28, fault unclear): fixed in prose and spec controlling idea. The lead-in says fees and holds are rows, and that negative balances and currency, the heading's other two subjects, are not rows and follow the holds.
- `SettledReversed`, `CaptureFailed` vs `SettledReversed`, `RefundNotCleared` (spec fault): corrected against the sources. The settlement details report defines `SettledReversed` as the debit that reverses a Settled entry when Adyen has not received the funds within 30 days (the case in the row, "a pre-funded amount taken back"); `RefundNotCleared` is a credit reversing an uncleared refund; `CaptureFailed` is a separate journal type ("Capturing funds has failed"). The table row now gives `SettledReversed` only; p24 adds one sentence saying which of the two quoted entries is which; spec p24 and p28 evidence updated to match. The quotation from the upgrade page is unchanged.
- €412,000 rounding rule without set-up (p33): fixed. The sentence now says what the case shows (a recomputed conversion drifts) and recalls what the €412,000 was (Larkfield's figure against its providers' balances at end of 2025, per the ledger).
- Position of "Stripe and Adyen: Where They Differ" (waived): house format; transition strengthened (see above).

## flow_is_followable (minor)

- Stripe "settlement" quoted before its meaning is given (p13): fixed with a one-line parenthetical pointing to the definition.
- Adyen for Platforms vocabulary (p21): fixed. One sentence says Studio Noord is on the platform model and the rest of the chapter uses its words (balance account, settlement delay).
- Fees announced in the heading, only a table row in the section (spec): fixed in prose without moving units. The p28 lead-in says fees were explained with each provider above.

## Content corrections (author's change 4)

- Table row "A pre-funded amount taken back": `CaptureFailed` removed, per Adyen's settlement details report (n.d., accessed November 2026).
- Scene ¶1–2: Studio Noord "on Adyen since 2024"; the 1,140 dated "before 2024" and placed in NL/DE, per the ledger.
