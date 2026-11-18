# Revision after draft check, round 1 — 37-payment-reliability

Date: 2026-11-17. Report judged: round 1, 29 failed results (1 blocker, 25 major, 3 minor). One line per failed result. Words: 6,496 before, 6,824 after; `max_words` raised 5%, 6,500 to 6,825. `timetoread` 28 to 30. Apart from the corrections listed under "Content", no fact, number, date, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## AC-3 (blocker) and evidence_is_explained

- AC-3, Australian 100% has no definition: fixed. The Adyen paragraph (p11) now says what the figure is (Adyen Australia Pty Ltd's quarterly disclosure as a member of the Reserve Bank of Australia's settlement system, ruling 46h), its date (third quarter of 2026; page n.d., accessed 17 November 2026), the regulator's definition (share of planned time without a significant outage; maintenance and outages caused by a cardholder's bank excluded) and what it does not measure (requests answered, what became of the rest). Table cell "Definition as published" now gives the definition in short. Spec p11 and its evidence aligned.
- evidence_is_explained, the Australian figure only in the table: fixed by the same paragraph.

## transition_expresses_declared_relationship

- p10 does not name Stripe: fixed; opens "Stripe's figures come first."
- Conclusion opens on a label: fixed; "What the chapter has shown, from the figures to the recoveries, sorts by how settled it is." in the same unit as **Established.**

## flow_is_followable (major)

- "the first thing that gives way": fixed; the intro now restates the part opening's claim (the record of each payment must not give way) and says the chapter asks what gives way when part of the path fails and what is left to repair.
- "the record" as if defined: fixed in the same sentence ("the record of each payment"). Spec p01 aligned.
- Mila's evening never told: fixed; p04 says the drill later in the chapter scripts such an evening, and In Practice picks Mila up (her €120.00 pass would move under K8; her €49 stored-card membership would wait; ledger, chapter 10 line). Spec p04, p34 aligned.
- Provider switch, K8 and Keel unglossed: fixed at first use in the scene; "The switch plays a small part" now "The provider switch of K8". Spec p06 aligned.
- 99.9%-per-quarter row before any quarterly figure: fixed; p09 says the first row is the quarterly figure in Adyen's contract, discussed below.
- "No row of the table" points at a later table: fixed; "sorted in the table below; no row can be ranked against another".
- Australian figure never discussed: fixed (see AC-3).
- Stripe not named in p10: fixed (see transitions).
- "131 minutes a quarter and 26 seconds a month apart": fixed; "the contract tolerates about 131 minutes of downtime a quarter; the status page's figure, about 26 seconds in 30 days."
- October 2026 count then 2025 entry: fixed; split into two sentences, "An older entry, of 20 October 2025, says ...".
- Failover paragraph a digression (spec): moved p20 after p21 (the inference box) within the section, as both readers proposed; p20 now opens "Beyond the two accounts behind that reading, the public record thins out"; the next section opens "Your own payment path needs the same decision, what may give way". Spec order, transitions and section flow aligned.
- "Adyen's accounting queue is the queue": fixed; "Each design has a public instance; for queueing it is Adyen's accounting queue." Spec p24 aligned.
- The four documents never listed: fixed; p26 names them. Spec p26 aligned.
- Where They Differ brings in new facts: fixed; the opening sentence now announces the three facts the table adds (support-plan response time, billing-usage failover, Adyen's 2023 SLO post). Spec p32 aligned.
- K8 switch's stacked restrictions: fixed; "The K8 switch is narrow. It applies only at the 50 largest studios ... and there it moves only online card payments that bring their own credential".
- 20 hours / 6 days unexplained: fixed; "the time Larkfield allows a resend (20 hours on Stripe, 6 days on Adyen, within how long each provider keeps a key)" (ledger, chapter 18 line). Spec p37 aligned.
- "adds a second provider to the first two": fixed; "The third failure brings in the second provider."
- "Platform balances" new in the takeaways: fixed; "Stored cards, and studios that are each on one provider, tie most of Larkfield's payments to that provider" (body's own reason).

## flow_is_followable (minor)

- "mirror of the provider's status": fixed; "Larkfield's copy of the studio's verification status at the provider".
- "plans to contain such bursts": fixed; "Stripe's 2019 commitment shows a provider containing such bursts on its side; on yours the remedy is pacing".
- "the latter" in the Adyen quotation: fixed; "in its words “the latter” is the edge".

## known_before_new

- "The books" and "non-critical requests" in the thesis paragraph: fixed; glossed in place. Spec p03 aligned.
- "The edge" and "the outer edge": fixed; the edge glossed at first use (the outer layer of servers that receives every payment request); "the outer edge of your own system, where it calls the provider" in p25. Spec p25 aligned.

## no_weak_conclusion_pattern

- New idea and new example in the takeaways: fixed; platform balances replaced (above); the €16.00 drop-in replaced by "a payment below the bound you set" (the table's own rule).

## Content

- Australian disclosure's definition added from the source page (fetched 17 November 2026 to confirm it); source entry unchanged.
- Mila's pass and membership under K8 from the ledger (chapter 10 line).

## Not changed

- No failure judged wrong. Trims to stay within length: connective phrases only (e.g. "The achieved figures are scattered", "Where Adyen lets the books lag", one duplicate gloss of "issuer").
