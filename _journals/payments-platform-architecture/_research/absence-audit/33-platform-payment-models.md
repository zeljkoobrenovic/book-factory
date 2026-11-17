# Absence audit — 33-platform-payment-models

Audit of 17 November 2026. Corpora fetched in this session with a generic user agent: `docs.adyen.com/llms-full.txt` (68 MB, full text), `docs.adyen.com/sitemap.xml`, `docs.adyen.com/llms.txt`, `www.adyen.com/sitemap-en.xml`, `help.adyen.com/sitemap.xml`, `docs.stripe.com/sitemap.xml`, `docs.stripe.com/llms.txt`, `support.stripe.com/sitemap.xml`; web searches restricted to the providers' domains (stripe.com, docs.stripe.com, support.stripe.com, stripe.dev; adyen.com, docs.adyen.com, help.adyen.com, medium.com); pages named below read directly.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Inference block: "Stripe documents no procedure for moving existing accounts when a platform's commercial model changes" | docs.stripe.com/connect/configuration-migration-guide, accounts-v2/connected-account-configuration, migrate-to-controller-properties; web search | overturned | Stripe documents it: "you need to create new connected accounts with the desired account configuration and re-onboard your users", in phases. What stays inference: that this applies to a platform's own change of commercial model. Block, last failure paragraph, spec p46 and Sources updated |
| Inference block: per-payment chargeback instruction must be stored | reasoning, not an absence | holds | none |
| Table: Adyen price list for the platform product "Not public; only payment-method prices are" | adyen.com/pricing, docs fee-type pages, web search | holds | none |
