# Absence audit — 08 payment-state-machines

Audit of 17 November 2026. Earlier search (verification pass): narrow (documentation index and one web search). "Wide" below means: the provider's documentation (`.md` pages), help or support center, company site (legal, pricing, newsroom, knowledge hub or engineering blog) and web searches restricted to the provider's domains, all on 17 November 2026. Result: **holds**, **narrowed**, **overturned** or **already wide**.

Counts: 2 hold, 1 overturned in part, 0 narrowed, 0 already wide.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Adyen has published no design history comparable to Stripe's | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | holds | none |
| Why Adyen chose result codes and modifications is not on record (prose, INFERENCE block, table) | docs.adyen.com, help.adyen.com, adyen.com (pricing, legal terms, licenses, knowledge hub, press), medium.com/adyen; domain-restricted web searches | overturned in part | Adyen engineering post 'Design to Duty: How we make architecture decisions at Adyen' (July 2021): 'Instead of keeping the state in our edge layer, we decided to process modifications asynchronously, which keeps the edge layer stateless.' Reason for result codes and no retrievable payment still not found. Three places and spec evidence rewritten; source added |
| Adyen has not published its reasons (INFERENCE) | as above | holds for the retrievable object | rewritten to match |

Consistency ruling 29 says the reasons for 'result codes and asynchronous modifications' are not on record; the second half is now wrong.
