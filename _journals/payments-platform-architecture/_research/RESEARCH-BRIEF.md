# Research Brief — SETTLED research briefs

You are preparing one verified research brief for **SETTLED: Architecting Payments and Revenue Infrastructure**, a book that explains to **engineers and architects who are new to payments** how payment and revenue infrastructure is actually built, anchored on **Stripe and Adyen**. It follows the evidence discipline of its sibling books (ORDERED, RECONCILED, LISTED, BOOKED). The author's instruction for this book: **prioritize quality over speed; every factual claim about a company's architecture needs a source; separate what companies have publicly documented from what is inferred; check dates and flag anything older than about three years; do not pad — where little is public, say so.**

ROOT = `/Users/zeljkoobrenovic/PycharmProjects/book-factory/_journals/payments-platform-architecture/`

## The book's frame

Read `ROOT/PLAN.md` ("Positioning", "Structure", "Teaching discipline" and the chapter contracts that name your brief) so you know which chapters your brief feeds and what each must cover. Every chapter in Parts I–VIII has a required section "Stripe and Adyen: Where They Differ", so **for every topic in your brief, find what Stripe has published, what Adyen has published, and state explicitly when one of them has published nothing**. Other companies (PayPal/Braintree, Checkout.com, Block/Square, Uber, Airbnb, Shopify, Paddle, Spreedly, Chargebee and others) belong in your brief only where a contrast clarifies an architectural choice.

The book's running example (Larkfield) is fictional; your brief is about **real, public, dated evidence**.

## Starting points you may read, with rules

- The Productscape domain model at `/Users/zeljkoobrenovic/PycharmProjects/productscape-workspace/productscape-examples/_config/product-domains/other/payments-and-revenue-infrastructure/` (`_domain/DOMAIN.md`, `REVIEW.md`, `customers/links.json`, `customers/insights.json`, `business/competition.json`, `product-bricks/product-bricks.json`). Use it for the domain map, terminology and source leads. It is **one source and a model, not evidence**: never tag a claim VERIFIED because the model says so; fetch the linked primary source.
- Sibling research briefs: `/Users/zeljkoobrenovic/PycharmProjects/book-factory/_journals/finance-systems-architecture/_research/brief-payments.md` (October 2026) and `/Users/zeljkoobrenovic/PycharmProjects/book-factory/_journals/commerce-platform-architecture/_research/brief-checkout-payments-tax.md` (November 2026). Use them to find sources quickly. Everything you carry over must be **re-verified in this session** by fetching the URL; tag it by what you found, not by the old tag.
- The reader reports in `/private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-book-factory/69f0aeef-1582-4169-8062-d2abd585a792/scratchpad/reads/finance-F3.md` list the Stripe and Adyen facts the sibling book RECONCILED already published (chapters 20, 21, 22, 25). The new book goes deeper than those; do not stop at what they cover.

## Format to match

Read the first 60 lines of `/Users/zeljkoobrenovic/PycharmProjects/book-factory/_journals/commerce-platform-architecture/_research/brief-checkout-payments-tax.md` and copy its conventions:

- Title `# Research brief: <topic>` and a "Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters …" line.
- A "How to read this brief" section with the three tags: **[VERIFIED: url, published YYYY-MM(-DD)]** (you fetched the page in this session and it supports the claim; date = publication date, or "n.d., accessed 2026-11" for undated documentation and product pages), **[WIDELY REPORTED: url, YYYY]** (reputable secondary source; say what kind), **[ASSUMPTION/JUDGEMENT]** (industry knowledge or inference; **every** statement about how Stripe, Adyen or any company works internally beyond what it has published).
- **Evidence-age warnings**: mark every source older than about three years (published before November 2023) with **(evidence age: N years)** and say whether newer material confirms, updates or contradicts it. ⚠ volatility flags for anything likely to change within 12 months (pricing, preview status, product names, thresholds, regulation in progress). An honest "Research limitation" paragraph naming what you could not fetch or verify.
- Numbered PARTs and sections that follow the chapters you feed; tables of contrasts where useful; **quote sparingly and accurately** — exact quotes in double quotes are valuable because chapter writers will reuse them.
- **Per section, a "Stripe vs Adyen" table or note**: what each has documented on this topic (with URL and date), "nothing public found" where that is the case (say what you searched), and the differences the evidence supports. Tag any interpretation ASSUMPTION/JUDGEMENT.
- **Per section, a short "For readers new to payments" note**: the two to four payments terms that must be defined, each in one plain sentence, so writers can lift the definitions.
- **Per section, a short "Architecture implications" note**: what the facts imply for system design, tagged ASSUMPTION/JUDGEMENT.
- End with: "Key numbers" table (each with source, date, and the exact definition of the metric), "Open questions / not verifiable" (be specific: these become the book's "where the evidence stops" statements), and "Source list" (title, publisher/author, publication date, URL, one line on what it supports).

## Research rules

- **Primary sources first**: Stripe engineering blog (`stripe.com/blog/engineering`, `stripe.dev/blog`), Stripe documentation and API reference (`docs.stripe.com`; append `.md` to most docs URLs for a clean markdown version), Stripe newsroom, annual letters and Sessions talks; Adyen documentation (`docs.adyen.com`; many pages have a `.md` variant), Adyen's tech blog and knowledge hub (`adyen.com/knowledge-hub`, `adyen.com/blog`, the Adyen Tech publication on Medium), Adyen investor relations (annual reports, half-year results, shareholder letters, capital markets day material); card networks and standards (Visa and Mastercard rules and developer documentation, EMVCo, PCI SSC, ISO 8583 and ISO 20022 descriptions, NACHA, the European Payments Council); regulators and legal texts (EUR-Lex via the Publications Office, EBA, ECB, DNB, FCA, the Federal Reserve, OCC, CFPB, RBI); investor filings (SEC EDGAR for PayPal, Block, Shopify, Global Payments); conference talks by named engineers (QCon, Strange Loop, InfoQ, re:Invent, company events) — cite the talk page and date; peer-reviewed or well-known practitioner publications.
- **Secondary analysis only to fill gaps**, tagged WIDELY REPORTED with the kind of source named. Wikipedia is acceptable only as a pointer to a primary source you then fetch.
- **Verify by fetching.** A claim is VERIFIED only if you fetched the page in this session and read the passage. Search results snippets do not count. Record the publication date you saw on the page. If a page you expected is gone, moved or blocked, say so in "Research limitation" and look for an archived or official alternative.
- Fetching tips: use the WebFetch tool where you have it, or `curl -sL --max-time 40 -A "Mozilla/5.0 (research-bot)" <url>` in Bash and read the text. Medium pages often return 403: fetch the RSS feed instead (`https://medium.com/feed/<publication>`). EUR-Lex blocks fetches; the EU Publications Office serves official texts: `http://publications.europa.eu/resource/celex/<CELEX>` with header `Accept: application/xhtml+xml` (curl). For SEC EDGAR use the User-Agent `research-bot admin@example.com`. Large PDFs (annual reports): download to your own scratch directory and extract text with `pdftotext` if available, or Python.
- The web-search quota is shared with eleven other researchers running in parallel; search efficiently, then fetch known URLs directly.
- **Never invent proprietary internals** (service names, data-center locations, database products, volumes, algorithms, team structures) of real companies. If something is only plausible, tag it ASSUMPTION/JUDGEMENT.
- **Never put the user's email address, name or any personal identifier** in HTTP headers, User-Agent strings, query strings or request bodies.
- Record every source with its publication date. Aim for **60–110 tagged claims** and **450–800 lines**. Depth and accuracy beat breadth. If a topic in your scope has little public information, say so in two lines and move on; do not fill the gap with generalities.
- Keep your private scratch files in `/private/tmp/claude-501/-Users-zeljkoobrenovic-PycharmProjects-book-factory/69f0aeef-1582-4169-8062-d2abd585a792/scratchpad/research-<your-brief-name>/`, never in the repository.

## Deliverable

Write only `ROOT/_research/brief-<your-topic>.md` (the name is given in your task). Do not edit any other file in the repository.

## Report back

Under 200 words: file written, line count, number of VERIFIED / WIDELY REPORTED / ASSUMPTION tags, the five most important findings for the book, where Stripe and Adyen differ most on your topic, and the biggest gaps you could not verify.
