# Absence audit — 01 journey-of-a-payment

Audit of 17 November 2026. Earlier search (verification pass): medium (legal and license pages, both `llms.txt`). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 4 hold, 0 overturned, 2 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen US: acquirer of record per payment Not public | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Adyen: which locations use banking partners Not public; no public page names the acquiring entity | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Neither company publishes its class of network membership per country | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | narrowed | Stripe's STEL and MALPB acquirer terms call each 'a member of the Networks'; Adyen claims 'principal membership of Visa and Mastercard in major markets' (2026). No list by network and country. Sentence added; sources added |
| Neither publishes volume per acquirer; Adyen does not define 'full-stack' | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches; docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Stripe's payout page does not say whether a payout waits for the network's money | docs.stripe.com, support.stripe.com, stripe.com/legal (services agreement, services terms, pricing policy), stripe.com newsroom and guides, stripe.dev; domain-restricted web searches | narrowed | Services terms (28 Sep 2026) count a financial provider's failure to settle to Stripe as a payout delay. Clause added; source line updated |
| Mastercard's rules could not be read | retried: HTTP 403 | holds | none |

**Ruling 46(j), applied after the audit.** Key point, advice paragraph and cast paragraph now say Adyen names an acquiring entity for some markets only and publishes no complete list per country; license pages for Japan and Singapore added to Sources; article date corrected to 3 July 2026.
