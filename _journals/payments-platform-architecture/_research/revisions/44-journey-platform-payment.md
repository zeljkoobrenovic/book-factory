# Revision — 44-journey-platform-payment (2026-11-17)

Round-1 check report, one line per failed result.

- evidence_is_explained (shortfall table): a sentence before the table now says what it answers; the destination-charge row contradicted the prose. Corrected against chapter 35 and Stripe's charges page (verification rows 40, 43): the column is now "If the studio's balance is empty"; the destination-charge row gives the reversal error and the refund sent without it, with the 45-day pending rule kept and scoped to the platform's own balance. Spec p26 evidence updated.
- flow_is_followable (destination-charge row): fixed by the same correction.
- flow_is_followable ("Stripe thus…" displaced): the Adyen paragraph now opens by restating the Stripe side (order of collection, 180 days) before the contrast.
- flow_is_followable (bare-refund paragraph): split into Stripe default, then the Adyen pilot logic step by step, then a plain sentence: for a platform outside the pilot Adyen's pages do not say where a bare partial refund is booked (verification row 29; spec open question 4).
- flow_is_followable (ledger order, "the sixth row"): rows sorted by date (25 March last); counterfactual named as "the second 18 March row"; "the sixth row" is now "the refund row of 18 March". Spec p30 evidence updated.
- flow_is_followable (step 3 not marked): "**Step 2.**" opens the paragraph and "**Step 3**, the platform's fee," marks the `Commission` item.
- flow_is_followable (step-1 terms before gloss): the split is pointed forward and the liable balance account glossed at first use in step 1.
- flow_is_followable (70% circular): rewritten: the destination charge transfers the full €120.00, the fee comes back separately, the refund is 70% of the charge, so 70% of the transfer is reversed (author's arithmetic, ledger figures).
- flow_is_followable ("three times", minor): now "four times, three on Adyen and one on Stripe", matching the four cases listed.
- flow_is_followable (whose short balance in p24, minor): names the platform's balance on destination charges and the studio's on a direct charge.
- known_before_new ("blended rate"): glossed as one percentage plus a fixed amount whatever the card costs, against the pass-through price assumed on Adyen (ledger, chapter 05 addition), which also says why €0.87 differs from €0.61.

Words 6,123 (max 6,500). validate_spec and check_draft structure pass. timetoread 27.
