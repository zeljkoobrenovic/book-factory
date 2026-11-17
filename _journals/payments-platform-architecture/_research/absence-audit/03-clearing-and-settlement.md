# Absence audit — 03 clearing-and-settlement

Audit of 17 November 2026. Earlier search (verification pass): narrow (pages cited, `llms.txt`, one site-limited search). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 7 hold, 0 overturned, 2 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Stripe does not say whether a capture can be rejected later at the network (prose, table row 1) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | holds | none; found only late failures for bank debits and the Charges capture reference already cited |
| Which interchange rate a record earns is not public | usa.visa.com public documents; Visa rules | narrowed | Visa publishes 'Visa USA Interchange Reimbursement Fees' (24 Oct 2026) with US rates by program; the rate qualification guide is not public. Sentence and spec evidence rewritten; source added |
| Network settlement cut-off times and cycles per day are not public (prose, timeline table) | Visa rules; visa.com, usa.visa.com, corporate.visa.com by web search | holds | scope words added |
| Mastercard rule documents could not be read | mastercard.us chargeback guide PDF retried 17 Nov 2026: HTTP 403 | holds | none |
| Stripe documents nothing equivalent to pre-financing for standard payouts; does not say whether availability waits for network funds (prose, table row 5, take-away) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed | Stripe's services terms (last modified 28 Sep 2026): settlement funds are transferred on the payout schedule 'unless a Payout Delay occurs', and a Payout Delay includes 'a delay or failure of a Financial Provider to settle a Transaction to Stripe'. No pre-financing statement. Paragraph, table cell, take-away and spec updated; source added |
| INFERENCE: Stripe does not say it carries a timing gap | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | holds | none |
| Table 'settled', network row, Stripe: Not public | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | holds | none (no merchant-facing network-settlement event found) |
| On Stripe the capture failure path is not public (table last column) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | holds | none |
| Timeline: clearing and settlement timing not public | as cut-off times | holds | none |

Locked fields: AC-3 and thesis.how_why say Stripe 'documents nothing equivalent' / 'states nothing of the kind' for standard payouts. Still true of pre-financing, so not reported as false; the terms clause is new context.
