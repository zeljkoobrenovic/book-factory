---
title: "Glossary: Plain-Language Definitions and a Stripe–Adyen Crosswalk"
date: 2026-11-17
author: Željko Obrenović
excerpt: "What does each payments, banking and billing term in the book mean, and what do Stripe and Adyen each call it? One plain definition per term with its owning chapter, grouped by part; a crosswalk of the two providers' vocabularies with a note wherever they do not match; Larkfield's fictional names; and an alphabetical index."
permalink: glossary
timetoread: __TTR__ min read
---

> **IN THIS SECTION, YOU WILL:** Look up any term the book uses, read its definition beside the terms it is confused with, and translate it between Stripe's and Adyen's vocabularies.

> **KEY POINTS:**
>
> * **One term, one meaning, one owning chapter.** Each row gives a definition of one or two sentences in the book's own neutral wording and links to the chapter that owns the term. The definitions follow those chapters; when a chapter and this page disagree, one of them needs correcting.
> * **Translate by definition, not by spelling.** Stripe and Adyen often use different words for one thing (application fee and commission), the same word for different things (reserve, transfer, available, chargeback), and sometimes divide a concept differently: one connected account at Stripe is a legal entity, an account holder, a balance account and a transfer instrument at Adyen.
> * **Every entry is dated.** Provider terms are as read in the two companies' documentation in November 2026, legal entries summarize a rule and defer to its source, and “no counterpart found” is a search result, not a statement by the provider. Larkfield and its names are fiction.

<br>

At Stripe a **reserve** is money the provider holds back from a merchant against refunds and chargebacks. At Adyen the reserve is a buffer the merchant sets for itself, and the provider's hold is called a deposit ([[balances-and-funds-flows]]). The two companies often use different words for one concept, sometimes the same word for two, and sometimes divide a concept differently, so a reader moving between their documentation has to translate **by definition, not by spelling**. This page therefore gives each term one definition in the book's own neutral wording and one owning chapter, and sets beside it, in a crosswalk, the word each provider uses and a note where the two do not match. For some terms, such as the unit that represents a seller on a platform, no one-to-one translation exists.

The page has four parts, in this order. First come the definitions, grouped by the book's parts, each with a link to the chapter that owns the term. Then comes the Stripe–Adyen vocabulary crosswalk, one table per area. After it are the names of Larkfield, the fictional studio-software platform this book follows, and last an alphabetical index of everything. The material is the chapters' own definitions and the two providers' documentation as read in November 2026. The previous page, [[toolkit]], uses terms such as idempotency key, clearing account, payout return and PCI scope without defining them; they are defined here.

## How to Use This Glossary

Browse by the book's parts, or jump to the **[alphabetical index](#g-index)** for a term, an alias, an abbreviation or a provider's own word. To translate between the two providers, go to the **[crosswalk](#g-crosswalk)**: its tables are grouped by area, and the index marks every provider term with its company.

The **__NROWS__ definition rows** are short teaching definitions, and the **__XROWS__ crosswalk rows** each name one concept in both vocabularies. The last column links to the chapter that owns the term (the first link) and to others that use it; the fuller explanation, the worked example and the dated sources are there. Terms separated by a slash are defined together to show how they differ, and acronyms are expanded in the row.

Three kinds of entry need care. **Larkfield is fictional**, and its names and figures illustrate the definitions ([[meet-larkfield]]). **Legal and standards entries** summarize a rule as of November 2026; consult the cited source for the requirement itself. And **a provider's term** is the word its documentation used when the chapter was written: both companies rename things, so check the current page before a word from this table goes into a column name, a contract or a design decision.

