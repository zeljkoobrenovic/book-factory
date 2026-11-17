# Absence audit — 28-usage-metering-and-rating

Audit of 17 November 2026. Corpora fetched in this session with a generic user agent: `docs.adyen.com/llms-full.txt` (68 MB, full text), `docs.adyen.com/sitemap.xml`, `docs.adyen.com/llms.txt`, `www.adyen.com/sitemap-en.xml`, `help.adyen.com/sitemap.xml`, `docs.stripe.com/sitemap.xml`, `docs.stripe.com/llms.txt`, `support.stripe.com/sitemap.xml`; web searches restricted to the providers' domains (stripe.com, docs.stripe.com, support.stripe.com, stripe.dev; adyen.com, docs.adyen.com, help.adyen.com, medium.com); pages named below read directly.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Inference block: Stripe's 2025 post does not say whether raw meter events are retained | Stripe docs (meter configuration, recording usage, meter event summary reference); web search of Stripe domains | holds | Sentence now covers the documentation as well as the post |
| "The sources used here describe how Metronome connects to Stripe, not how it is built" | self-scoped to the sources used; Stripe docs Metronome pages | holds (self-scoped) | none |
| "No public source says whether Stripe's two engines, or Adyen's platform and Orb, will be merged, or when" | Stripe blog "Metronome + Stripe: Building the future of billing" (23 January 2026); Stripe Sessions 2026 "Product roadmap: Revenue" transcript; Adyen press release of 11 June 2026 and knowledge-hub articles | narrowed | Both state an intent to unify (Stripe: "we’ll build a unified roadmap for one monetization platform"; Adyen: convergence); no date, and nothing on whether meters and Metronome become one engine. Sentence, spec p32 and Sources updated |
| "The absence of an Adyen meter"; prose "no meter, usage or billing object in Adyen's documentation"; table "Not public: no meter or usage object found" | Adyen docs full text (metering 0 hits; usage-based 1 hit, a PayTo mandate example), docs sitemap, adyen.com sitemap, web search | holds | Table cell names index and full text |
| Table: "Not public for Adyen" for pipeline design, time rules, credit balance; "no Adyen product documented" for token billing | same | holds | none |
