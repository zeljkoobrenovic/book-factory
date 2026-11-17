# Absence audit — 11 in-person-payments

Audit of 17 November 2026. Earlier search (verification pass): narrow (both `llms.txt`, one release, one product page). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 3 hold, 0 overturned, 2 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Stripe's in-person scale is Not public | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; 2025 annual letter page | holds | none |
| Neither describes how keys are loaded and rotated | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | narrowed | A Stripe guide article says Stripe handles key injection and decryption for Terminal readers; no procedure or rotation. Adyen: nothing beyond its P2PE terms. Sentence added; source added. P2PE instruction manuals still not read |
| Neither publishes how often terminals fail | as above | holds | none |
| How fleet updates are staged is documented by Adyen and not by Stripe | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed | Stripe documents automatic updates at midnight local time for smart readers and, for mobile readers, optional updates whose required date 'can vary across devices in the fleet'; no rollout policy. Two sentences and spec evidence rewritten; source added |
| Mastercard's rules could not be read; Adyen's page does not say why terminals refuse store-and-forward in a platform outage | retried: 403; the page | holds | none |

Locked AC-3 says 'Stripe documents no equivalent' to Adyen's four-weekly gradual rollout: still true of a rollout policy.
