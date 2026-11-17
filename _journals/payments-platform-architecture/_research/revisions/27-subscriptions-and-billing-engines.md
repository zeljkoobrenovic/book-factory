# Revision after draft check, round 1 — 27-subscriptions-and-billing-engines

Date: 2026-11-24. Report judged: round 1, 23 failed results (16 major, 7 minor) and 1 waived. One line per failed result. Words (check_draft structure): 5,848 before, 6,393 after (spec `max_words` 6,500, unchanged). `timetoread` 25 to 28. Apart from the corrections listed under "Content", no fact, number, date, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## evidence_is_explained

- Adyen ¶2, Orb and Adyen quotes: fixed; sentence added saying both put the billing system above Adyen (Orb treats Adyen as a gateway; Adyen says seat-and-month billing is served today, partly by partners).
- Designs ¶1, Metronome: fixed; sentence added: the provider-run engine now has a second, acquired engine beside it for usage prices.
- Where They Differ ¶1: fixed; the lead-in now states the result (Stripe documents the first design; Adyen the payment step under the second or third, unchanged so far by Orb). Spec p34 aligned.

## transition_expresses_declared_relationship

- Clock-decisions opening: fixed; opens "None of Femke's three answers … exists until something decides it."
- p13 identity: fixed; "The fifth decision is identity, and it holds the result of the other four."
- Where They Differ lead-in (house format; transition strengthened): opens from the three designs and places the two companies among them.
- When It Goes Wrong opening: fixed; contrast sentence after the **Late.** label ("both engines working as designed; they fail in four ways").

## flow_is_followable (major)

- Where They Differ position: waived by the author (house format); lead-in strengthened as above.
- Scene table incidents unexplained: fixed; each incident glossed in the cell (from the ledger); row label now "2026 incident in the engine".
- Keel mid-clause: fixed; Keel introduced in its own sentence before the punchline, with K1 to K8.
- K1, K5, K2 as unseen labels: fixed; each named in words at first use (K1 one writer, one key; K5 Larkfield paces and rate-limits renewals, now in prose before the table; K2 the provider's record is the truth, the webhook the doorbell).
- 3.33 / 0 USD example: fixed; the steps are added from Stripe's prorations page (fetched 2026-11-24): 10 USD paid 1 April, upgrade 11 April without proration, downgrade 21 April with a third of the month left; both modes debit 3.33 USD; classic credits 6.67 USD (example invoice -3.34 USD); flexible credits 3.33 USD, total 0 USD.
- `past_due` on Larkfield's engine: fixed; "the state Larkfield's engine calls `past_due`, a name borrowed from Stripe's status list".
- Silent Webhook late and contradicting "failed twice": fixed (content); the scene now names it as a third membership incident that sat in the webhook receiver, not in the renewal job (ledger: Stripe webhook receiver, Monday 14 September 2026, ruling 20); the failure section refers back to it. Spec p06 aligned.
- Intro dates out of order: fixed; ¶3 opens "The book's examples run in 2027, the year after Larkfield's incidents" and gives Mila's membership (January) before her pass (March). Spec p03 aligned.
- Pacing as an unannounced sixth decision: fixed; announced as a scheduler requirement where the engine's requirements are set out (sentence and a "How paced" row in the reference-design table), and the 38% figure given context in prose before the Larkfield table. Spec p15 and p39 aligned.

## flow_is_followable (minor)

- "invoice … defines it shortly": fixed; glossed in place ("one statement of what is owed for one period").
- Identity not named in the Stripe section: fixed; scheduler paragraph opens with "The fifth decision, one invoice per period, is the scheduler's job".
- `ContAuth`: fixed; "a payment the merchant starts, with no shopper taking part, is marked by the value `ContAuth` in its shopper-interaction field". (Adyen's page does not define the term; the gloss is the sentence's own merchant-initiated meaning.)
- "[[part-6]] claimed" reads like a placeholder: fixed; "The introduction to this part ([[part-6]]) argued … this chapter takes that something apart."
- Yearly beside monthly volume: fixed; "about €2.04 million a month" added (24.5 / 12; ledger line of chapter 41).
- Disputes/direct-debit paragraph as a detour: fixed; opens "Once the invoice is handed over, its collection is an ordinary payment".
- Studio Noord as seller and buyer: fixed; "Studio Noord, which sells Mila her membership, is itself Larkfield's customer".

## known_before_new

- Subscription schedule and phase: fixed; glossed as Stripe's object for automating changes to a subscription over time, divided into phases each with its own prices, and distinguished from the renewal schedule.

## Content

- Silent Webhook vs "failed twice": sentences made to agree with the ledger (see above).
- Classic-mode example total -3.34 USD added from Stripe's prorations page (its example invoice `total: -334`).
- Monthly figure for studio subscription volume added (€2.04 million, ledger).

## Not changed

- No failure judged wrong. Nothing left for the editor.
