# Revision after draft check, round 1 — 33-platform-payment-models

Date: 2026-11-24. Report judged: round 1, 29 failed results (1 blocker, 18 major, 10 minor) and 1 waived. One line per failed result. Words: 6,500 before, 6,819 after; `max_words` raised 5% from 6,500 to 6,825 (glosses required by AC-3 and the readers; restatement trimmed elsewhere). `timetoread` 28 to 30. Apart from the corrections listed under "Content", no fact, number, date, quotation, hedge, figure, source entry or `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- Adyen ¶6 reserve-account sentence (major): fixed by subordination, not deletion (the fact is verified, row 68, and has its own source entry). The reserved compensation account is now defined as one of the platform's three liable accounts; the reserve account is a parenthetical "separate case" for transfer-caused negatives; the paragraph then runs default, recovery tools, exception. Spec p27 aligned.

## evidence_is_explained (blocker)

- "Use this logic if you want to make your user liable…" (designs ¶2): fixed. Added: "Adyen's 'user' is the seller, so the instruction puts the first step on the seller's balance account, with the platform's liable balance account still behind it." Spec p31 `shows` aligned.

## transition_expresses_declared_relationship

- Where They Differ ¶1 (major): house format; transition strengthened. Opens "The three models hold on either provider, but seven documented differences change how one is built".
- In Practice ¶5 "the same name" (major): fixed; Larkfield is named: "Larkfield stands behind Studio Noord and pays what the studio cannot." Spec p42 aligned.

## flow_is_followable (major)

- Provider split "by channel" vs "since 2024" (spec): fixed against the ledger. The scene now states the split by studio, the post-2024 studios on Adyen, and the 1,140 pre-2024 NL/DE studios on Stripe online with Adyen terminals; the Larkfield section already agreed. Spec p07 controlling idea and evidence aligned.
- p14 table provider column (spec): fixed by glossing every provider term of the last column in the paragraph before the table (charge type, `on_behalf_of`, responsibilities, model, store, split instructions); liable balance account defined in p13. Spec p13, p14 aligned.
- "Four classes" vs three rows: fixed; the paragraph says the table defines the two classes and the sponsored merchant, and names the other two classes (digital wallet operator, ramp provider; verification row 3). Spec p10 aligned.
- Refund aside in Stripe ¶5: fixed; the 180-day timeline sentence now closes the collection sequence and the 45-day refund rule follows as "a shorter one".
- Legacy-account detour (Stripe ¶7): fixed with a signpost: Larkfield's studios on Stripe are such accounts, and the box below applies the migration remedy to a change of commercial model.
- Reserved compensation account undefined: fixed (see one_controlling_idea).
- RECONCILED unexplained: fixed; "this book's companion on the finance side of payments".
- Crosswalk breaks two and three read as one: fixed; each break is named by what it is about (shape of a seller; where the assignment lives; who bears the loss by default). Spec p29 aligned.
- "Use this logic…" quotation vs "stands behind": fixed (see evidence_is_explained).
- Bram de Wit and "the ledger's two reversals": fixed; Bram re-identified with his 2 February pass at Studio Noord, both payments said to be on Adyen, "this chapter's two reversals", and "at the second step Larkfield pays on both". Spec p41 aligned.
- Figure 4 three steps vs the two-step rule (spec): fixed in caption and alt text (image not regenerated): the seller's bank account is described as part of recovering the first step. Spec figure description aligned.
- "Same name" at the payoff: fixed (see transitions).

## flow_is_followable (minor)

- Scene repeats the opening's questions: fixed; "the three questions this chapter opened with".
- Facilitator-cost detour: fixed; the paragraph now says up front that cost is why most platforms do not register.
- Losses-and-fees rule with no weight: fixed; "the combination that returns below as Stripe's buy rate model".
- "The same choice" lost its referent: fixed; "The loss assignment, `losses_collector`, fixes much more".
- "Platform model" not tied to the front desk: fixed; "such as a studio's front-desk terminal".
- Marketplace default distinguishes nothing: fixed; the sentence now says the marketplace model is the one where the default matches whom the customer deals with.
- "Three Ways" heading vs four-row table: fixed; the lead-in calls the facilitator a fourth route beside the three models; "Down the rows" replaces "In every row". Heading kept (spec title).
- "Both require it" / "the second model": fixed; both named.
- "One to two months" derivation: fixed in the inference column (more than 30 days, then the first day of the next month).
- Failure patterns not named in the body: partly fixed; the first failure is named as "the Orphaned Refund at its largest". The fourth is not tied to a pattern, because none of the three listed fits it without stretching.

## known_before_new and AC-3

- p14 table terms (spec, major): fixed (see flow).
- Reserved compensation account (major): fixed.
- AC-3 (spec, major): fixed; charge type glossed in KEY POINTS (callout gloss allowed by change 3) and before the p14 table; liable balance account defined in p13.

## flow_is_followable (waived)

- Where They Differ position: house format; transition strengthened (above).

## Content

- Provider split in the scene corrected to the ledger (by studio; 1,140 pre-2024 NL/DE studios on Stripe online with Adyen terminals).
- Figure 4 caption and alt text corrected to the two-step rule and to what the image shows.
- Spec p50 count corrected from nine to eight questions (the page has eight).

## Not changed

- No failure judged wrong.
