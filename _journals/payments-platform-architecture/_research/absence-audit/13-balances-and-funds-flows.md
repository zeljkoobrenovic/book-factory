# Absence audit — 13 balances-and-funds-flows

Audit of 17 November 2026. Earlier search (verification pass): partly wide (six pages, `llms.txt`, a support FAQ, one site-limited search); legal terms not searched. "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 3 hold, 0 overturned, 3 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Stripe does not say whether its schedule waits for the network (excerpt, key points, introduction) | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed (text left) | Front matter and key points are journal-spec-locked wording; unchanged. See the paragraph below the table |
| No public source says whether `available_on` waits for network settlement | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed | Services terms (28 Sep 2026): a payout can be delayed by 'a delay or failure of a Financial Provider to settle a Transaction to Stripe'; Stripe may reverse if 'the Payment Method Provider invalidates the Transaction'. Whether availability otherwise waits remains unstated. Sentence added; source added |
| INFERENCE: for Stripe's standard payouts who carries either risk is not public | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed | Rewritten: terms let Stripe delay or reverse; the normal-case timing gap is not public |
| No public source says how a balance transaction is derived from Ledger (INFERENCE) | stripe.dev posts, docs, web search | holds | none |
| `payment_reversal`: the list does not say which methods it covers or whether it applies after a payout | docs.stripe.com balance transaction types and reporting categories; support.stripe.com | holds | none |
| Table: pre-funded amount taken back / tie to network settlement: Not public for standard payouts | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed | Second cell now names the terms clause; first cell holds |

Locked sentences now imprecise (not edited): intent and thesis say that for Stripe's standard payouts the question is simply 'not public' / the documentation 'does not say'. The documentation still does not say; the services terms give the delay and reversal rights quoted above.
