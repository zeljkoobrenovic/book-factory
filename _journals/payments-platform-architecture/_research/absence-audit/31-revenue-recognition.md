# Absence audit — 31-revenue-recognition

Audit of 17 November 2026. Corpora fetched in this session with a generic user agent: `docs.adyen.com/llms-full.txt` (68 MB, full text), `docs.adyen.com/sitemap.xml`, `docs.adyen.com/llms.txt`, `www.adyen.com/sitemap-en.xml`, `help.adyen.com/sitemap.xml`, `docs.stripe.com/sitemap.xml`, `docs.stripe.com/llms.txt`, `support.stripe.com/sitemap.xml`; web searches restricted to the providers' domains (stripe.com, docs.stripe.com, support.stripe.com, stripe.dev; adyen.com, docs.adyen.com, help.adyen.com, medium.com); pages named below read directly.

| Statement | Where searched | Result | Change |
| --- | --- | --- | --- |
| Inference block: Stripe's pages "do not call the product a subledger" | stripe.com product page (English edition served for the Netherlands), Stripe docs sitemap (all Revenue Recognition pages grepped), customer story, web search | overturned | Product page heading "A centralised revenue subledger"; report column "Stripe subledger account" (activity breakdown); a customer story says "source of truth and subledger for revenue". Block rewritten; spec unit updated; two sources added |
| Same block: "they do not say it is the book of record" | same | holds | Scope stated |
| "Neither the documentation index nor the pages read explain what a revenue contract is" | Stripe docs sitemap (no revenue-contract page), all Revenue Recognition .md pages (two mention revenue contracts without defining them), web search | holds | Sitemap and web search named; source note updated |
| "They do not describe estimating a price that varies" | verification row 37 (38 pages read) | already wide | none |
| Adyen: "I found no counterpart"; table "Not public" x3; take-away; Sources notes | verification rows 47 to 49 (docs index, help-center sitemap, adyen.com sitemap) plus docs full text ("revenue recognition" 0 hits) and web search | holds | Prose, table cell and source note name the full text and adyen.com |
| "No Adyen documentation of a revenue-recognition product or of Orb's reporting as part of Adyen's platform" | same | holds | none |
