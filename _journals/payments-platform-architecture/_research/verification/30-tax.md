# Verification — 30-tax (`billing-and-payment-tax`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants, the European Commission, Belastingdienst, Cornell, Avalara, Vertex and Adyen legal and press pages as HTML, Orb documentation as markdown. All double-quoted strings taken from sources or naming source pages (50 after the edits) were matched mechanically against the fetched texts after normalizing quotes and markup; none failed. Each row is one claim or one group of claims resting on the same passage.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Standard VAT rates: Netherlands 21%, Germany 19%; table 'Last checked: 13/07/2026' | https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm | corrected | Facts confirmed in the rate table. The cited URL (…/business/taxation/vat/…) redirects; Sources now carries the final URL |
| 2 | Quote: 'each member country is responsible for setting its own rates' | same page | confirmed | The page carries both 'each member country' and 'each EU country' wordings; the quoted one is present |
| 3 | Europe says VAT, Canada and much of Asia-Pacific GST, the US sales tax | https://docs.stripe.com/tax/how-tax-works | confirmed | Stripe: 'Canada and most countries in the Asia Pacific region refer to it as goods and services tax' |
| 4 | Quote: 'The buyer pays the tax and the seller forwards it to the government' | https://docs.stripe.com/tax/how-tax-works | confirmed | — |
| 5 | Quote: 'Stripe Tax uses your business address, tax registrations, product tax codes, customers' locations, and customer status …' | https://docs.stripe.com/tax/how-tax-works | confirmed | — |
| 6 | Quote: 'Stripe calculates the tax at the published rate at the time of invoice finalization' | https://docs.stripe.com/tax/invoicing | confirmed | Page title is 'Automatically collect tax on invoices' (source entry retitled) |
| 7 | EU rules since 1 July 2021; 'a new EU-wide threshold of EUR 10 000' for distance sales of goods and TBE services | https://vat-one-stop-shop.ec.europa.eu/index_en | confirmed | — |
| 8 | Above the threshold the customer's country taxes the sale | same page | hedged | The Commission page states the rule for sales below the threshold; the sentence now quotes it ('may remain subject to VAT in the Member State where the taxable person is established') and keeps 'above it' as the consequence |
| 9 | Quote: 'register in one EU Member State'; One Stop Shop | same page | confirmed | — |
| 10 | Wayfair decided 21 June 2018; physical-presence rule overruled | https://www.law.cornell.edu/supremecourt/text/17-494 | confirmed | 'Decided June 21, 2018'; Quill and National Bellas Hess 'are overruled' |
| 11 | Quote: 'deliver more than $100,000 of goods or services into the State or engage in 200 or more separate transactions' | same page | confirmed | — |
| 12 | Evidence-age flag on Wayfair (8 years) | same page | confirmed | Flag present in text and in the source entry |
| 13 | Thresholds count all of a seller's sales into the territory (EU: total sales across the EU) | https://docs.stripe.com/tax/supported-countries/european-union | confirmed | Stripe: 'Your total sales across the EU are below 10,000 EUR in a calendar year'; South Dakota wording as quoted |
| 14 | Quote: the four steps ('1. Understand which locations … 4. File and remit the tax you collected') | https://docs.stripe.com/tax/how-tax-works | confirmed | — |
| 15 | Quote: 'Online marketplaces/platforms facilitating supplies of goods are, in certain circumstances, deemed for VAT purposes to have received and supplied the goods themselves' (ruling 16) | https://vat-one-stop-shop.ec.europa.eu/index_en | confirmed | Goods only, as ruling 16 says |
| 16 | ViDA package adopted on 11 March 2025 | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en | confirmed | — |
| 17 | Quote: 'From 1 July 2028: deemed supplier measure for short-term accommodation rental and passenger transport platforms (Member States can delay implementation until 1 January 2030)' (ruling 16) | same page | confirmed | Two service sectors only; the page's statement that a fitness platform is in neither category is labeled as the author's reading and agrees with ruling 16 |
| 18 | Stripe Tax calculates in Checkout, on invoices and through an API; quote 'when processing payments off-Stripe' | https://docs.stripe.com/tax/standalone-tax-api | corrected | The cited URL /tax/custom redirects to /tax/standalone-tax-api and the page is titled 'Standalone Tax APIs', not 'Stripe Tax API'; text and Sources changed |
| 19 | A calculation versus a tax transaction; reports and filing read transactions | https://docs.stripe.com/tax/off-stripe | confirmed | 'transaction is included in threshold monitoring … and is available for tax reporting and filing' |
| 20 | `requires_location_inputs`; quote 'Stripe can't calculate the taxes, can't finalize the invoice, and can't collect the payment' | https://docs.stripe.com/tax/subscriptions | confirmed | Page title is 'Collect taxes for recurring payments' (source entry retitled) |
| 21 | Quote: 'Stripe only calculates tax in jurisdictions where you have an active tax registration. Without a registration in the customer's location, the calculation returns zero tax' | https://docs.stripe.com/tax/standalone-tax-api | confirmed | — |
| 22 | Quote: 'The API returns the reason for a tax result in the taxability_reason field'; values reverse_charge, customer_exempt, zero_rated, not_collecting | https://docs.stripe.com/tax/zero-tax | confirmed | — |
| 23 | `not_collecting` called 'ambiguous': missing registration or non-taxable product code | same page | confirmed | — |
| 24 | Quotes: tax IDs decide B2B; Stripe Tax 'doesn't validate whether the provided tax identification number exists or is valid' | https://docs.stripe.com/tax/how-tax-works | confirmed | — |
| 25 | Stripe Billing validates EU VAT numbers against VIES; statuses include verified and unverified | https://docs.stripe.com/billing/customer/tax-ids | confirmed | Statuses: pending, verified, unverified, unavailable. A doubled comma in the sentence was removed |
| 26 | Quotes: reverse charge 'when the tax ID has the required number format, regardless of the government verification result'; 'you're responsible for determining how to handle an `unverified` tax ID' | same page | confirmed | — |
| 27 | Monitoring quotes: 'tracks your Stripe-processed sales (minus refunds) …'; 'We only monitor Stripe-processed sales or imported transactions'; application fees do not count; 'it's up to you to confirm …' | https://docs.stripe.com/tax/monitoring | confirmed | Four quotations, all exact |
| 28 | Imports of other channels' sales | https://docs.stripe.com/tax/imports | confirmed | — |
| 29 | Off-Stripe payment recorded through the Tax API 'is included in threshold monitoring by default in live mode' | https://docs.stripe.com/tax/off-stripe | confirmed | — |
| 30 | Quote: 'You must register with the tax authority in a location to collect taxes there'; Stripe starts registrations in US states and points to a partner elsewhere | https://docs.stripe.com/tax/how-tax-works | confirmed | US: 'where you're a remote seller'; elsewhere Taxually |
| 31 | Filing quotes: automated filing in the US and 'for selected registrations in Ireland and Canada'; 'non-Union OSS registrations in Ireland and simplified federal GST/HST registrations in Canada' | https://docs.stripe.com/tax/filing | confirmed | HST expanded in the text |
| 32 | Filing elsewhere through partners; global filing listed as a private preview | same page | confirmed | Heading 'Global filing with Stripe (Private preview)' |
| 33 | Non-Union OSS is a scheme for sellers based outside the EU | https://docs.stripe.com/tax/supported-countries/european-union | confirmed | Now quoted from the page, which makes this source entry used in the text |
| 34 | Quote: 'The first step for using Stripe Tax with Connect requires you to determine which entity has the obligation to collect and report taxes'; one setup per liable party | https://docs.stripe.com/tax/connect | confirmed | — |
| 35 | Quote: 'Stripe Tax returns a tax amount of `0.00` and sets the taxability reason to not_collecting' | https://docs.stripe.com/tax/tax-for-platforms | confirmed | — |
| 36 | Quote: 'Separate charges and transfers without `on_behalf_of` aren't included. This is because Stripe can't know who the liable party for the transfer is' | https://docs.stripe.com/tax/monitoring | confirmed | Applies once the platform chose to be liable, as the page says |
| 37 | No Adyen product calculates, collects or files tax on a merchant's sales (absence of evidence) | https://docs.adyen.com/llms.txt; https://docs.adyen.com/llms-full.txt; https://help.adyen.com/sitemap.xml; web search limited to adyen.com | confirmed | Searched in this session: the documentation index and the full text (68 MB) for tax, VAT, GST, nexus, registration threshold, filing, remit, tax engine, Avalara, Vertex, TaxJar, Anrok; the help-center sitemap for tax, VAT, GST; two web searches. No calculator, threshold monitor or filing service for a merchant's indirect tax was found. Tax-related pages that exist are listed in the notes below |
| 38 | Adyen quote: 'does not deduct sales tax or value-added tax (VAT) from your settlement batches'; tax on its own invoices in some US states and in France | https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice | corrected | Quote and facts confirmed, but the cited help-center URL now returns 301 to this documentation page; text says 'Adyen's documentation', Sources carries the new URL and notes the redirect |
| 39 | Adyen quote: 'Level 2/3 enhanced scheme data (ESD) helps you track the amount spent on corporate cards and the amount of sales tax' | https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3 | corrected | Quote confirmed. The page was dated 'last modified March 2023' with an evidence-age flag; ruling 30 forbids last-modified stamps as dates (this page stamped 2023 mentions 1 April 2026). Now 'n.d., accessed November 2026', flag removed in text, table and Sources |
| 40 | Adyen closed the Orb acquisition on 1 July 2026 | https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates | confirmed | 'Both transactions officially closed on July 1, 2026'. The release was not in Sources; added |
| 41 | How Orb handles tax 'was not verified' | https://docs.withorb.com/integrations-and-exports/tax | corrected | Orb's documentation is public: 'Orb connects to third-party tax providers to calculate tax on Orb invoices' (Anrok, Avalara, Numeral, Sphere, Stripe Tax, TaxJar). The sentence now states this; source added |
| 42 | Table, Adyen cell 'Calculating tax on a sale': Not public; merchant may send a computed tax amount | Level 2/3 page; documentation search | confirmed | '2023' removed from the cell (ruling 30) |
| 43 | Table, Adyen cell 'What a zero result says': Not public | documentation search | confirmed | Nothing found; there is no calculator whose result could be documented |
| 44 | Table, Adyen cell 'Threshold monitoring': Not public | documentation search | confirmed | No hit for nexus or registration thresholds other than Adyen's own US sales-tax nexus on its fees |
| 45 | Table, Adyen cell 'Registration and filing': Not public | https://docs.adyen.com/platforms/us-tax-forms | corrected | Still not public for tax on sales, but Adyen documents one tax filing: 'Adyen is required to file a 1099-K tax form with the Internal Revenue Service (IRS) for any US-based user to which Adyen pays out directly'. Added to the cell and the paragraph, labeled as an information return; source added |
| 46 | Table, Adyen cell 'Liable party on a platform': Not public | https://docs.adyen.com/platforms/online-payments/split-transactions | corrected | Adyen documents a split type `VAT`: 'Books the value-added tax (VAT) incurred on a payment to the specified `account`, allowing you to book this tax separately from the sale amount' (the platform sends the amount). Added to the cell and the paragraph; who is liable remains not public; source added |
| 47 | Table, Adyen cell 'Who owes the tax': Not public | https://www.adyen.com/legal/adyen-terms-and-conditions | corrected | Adyen's terms and conditions (last update 1 November 2023), clause 4.5: 'each party will be required to comply with its own tax obligations under Applicable Law' and 'Merchant indemnifies Adyen from any tax liabilities incurred by Adyen arising out of any Taxes due on any products and/or services sold by Merchant'. Cell now cites it; the last column ('No material difference') is unchanged; source added |
| 48 | Table, six Stripe cells | Stripe pages above | confirmed | Each repeats a fact confirmed in the rows above; 'You must file and remit the tax you collect' is on the filing page |
| 49 | Avalara quote: 'across your ERP, billing, purchasing and commerce systems' (vendor claim) | https://www.avalara.com/us/en/products/calculations.html | confirmed | ERP glossed |
| 50 | Vertex quote: 'tax rules and rates for 19,000 jurisdictions' (vendor claim) | https://www.vertexinc.com/solutions/products/vertex-indirect-tax-o-series | confirmed | — |
| 51 | Managed Payments lists 'Third-party tax integrations' as unsupported | https://docs.stripe.com/payments/managed-payments | confirmed | — |
| 52 | Dutch reduced rate of 9% assumed for a studio's classes | https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/sportbeoefening_waaronder_zwembaden_en_sauna/gelegenheid_geven_om_te_sporten/ | hedged | The Dutch tax authority: 'Het geven van gelegenheid om te sporten valt onder het 9%-tarief'; lessons combined with the accommodation also 9%; lessons without it 21%; nonprofit sports organizations exempt. The 9% reduced rate also appears in the Your Europe table. The page now cites the authority and keeps 9% as a labeled assumption, because whether a given studio's classes (yoga, for instance) qualify was not determined; source added |
| 53 | Quote: 'The Tax Transactions page only includes *transactions* and not *calculations*' | https://docs.stripe.com/tax/payment-intent | confirmed | Page title is 'Stripe Tax with PaymentIntents' (source entry retitled) |
| 54 | `invoice.finalization_failed` with `requires_location_inputs` (failure table) | https://docs.stripe.com/tax/subscriptions | confirmed | — |
| 55 | Off-Stripe guide requires a reversal per refund (failure table) | https://docs.stripe.com/tax/off-stripe | confirmed | 'When you issue a refund, you must create a reversal tax transaction' |
| 56 | An event reports a tax number's verification (Larkfield, Cologne) | https://docs.stripe.com/billing/customer/tax-ids | confirmed | `customer.tax_id.updated` |
| 57 | Recording a One Stop Shop registration makes Stripe charge the customer country's VAT (Larkfield, Leipzig) | https://docs.stripe.com/tax/supported-countries/european-union | confirmed | Union OSS section; German standard rate 19% from the Your Europe table |
| 58 | Stripe treats a customer without a tax number as a consumer | same as row 24 | confirmed | Follows from 'Stripe Tax uses customer tax identification numbers to determine whether a transaction is B2B'; the page leaves the legal question open |
| 59 | Sources: titles and URLs of four Stripe entries | https://docs.stripe.com/tax/ | corrected | 'Collect tax on invoices' → 'Automatically collect tax on invoices'; 'Collect tax on subscriptions' → 'Collect taxes for recurring payments'; 'Use the Tax API with PaymentIntents' → 'Stripe Tax with PaymentIntents'; 'European Union' → 'Tax in the European Union', which was listed but not used in the text and is now used |

**Counts:** 59 claims checked: 48 confirmed, 9 corrected, 2 hedged, 0 unsupported, 0 unreachable.

## The "Not public" cells on the Adyen side

Searched on 17 November 2026: `https://docs.adyen.com/llms.txt` (the documentation index) and `https://docs.adyen.com/llms-full.txt` (the full text) for tax, VAT, GST, nexus, threshold, filing, remit, tax engine, tax registration, Avalara, Vertex, TaxJar, Anrok; the help-center sitemap (`https://help.adyen.com/sitemap.xml`) for tax, VAT, GST (the help-center search page itself is client-rendered and returned 404 to a plain request); two web searches, one limited to adyen.com. Result per cell:

- Calculating tax on a sale: no calculator found. Kept "Not public" plus the documented merchant-sent amount.
- What a zero result says; threshold monitoring: nothing found. Kept "Not public".
- Registration and filing: nothing for indirect tax; Adyen documents filing US form 1099-K for platform sellers. Cell changed.
- Liable party on a platform: Adyen documents a `VAT` split type. Cell changed; who is liable stays not public.
- Who owes the tax: Adyen's terms and conditions, clause 4.5, answer it. Cell changed from "Not public" to the fact.

Other Adyen pages that mention tax and were read but not added to the chapter, because none computes or files a merchant's tax: line-item tax fields (`taxAmount`, `taxPercentage`) the merchant sends for Klarna and similar methods (`docs.adyen.com/payment-methods/klarna/invoice-lines`); Greek fiscal rules for terminals, where Adyen attaches the signature of the merchant's e-invoicing system to a transaction (`…/point-of-sale/basic-tapi-integration/make-a-payment/greece-tax`); tax-free shopping for travelers through a third-party provider (`…/point-of-sale/shopper-recognition/tax-free-shopping`); help-center articles on 1099-K forms. The only hit for "calculates the tax" in the full text is a plugin release note about open-invoice line items.

## Could not verify, and what was done

- Current US state economic-nexus thresholds: not checked (the page says so in its evidence-age note). No change.
- The legal text behind the deemed-supplier rule (Article 14a of the VAT Directive) and the ViDA directive itself were not fetched; the page cites the Commission's summary pages, which were read. No change.
- Whether a studio's classes (yoga, pilates) count as "giving the opportunity to do sport" under Dutch practice: not determined. The 9% stays a labeled assumption with the tax authority's page cited.
- Whether a business customer without a VAT number is taxed as a consumer: a question of law the page explicitly leaves open; only Stripe's documented behavior was checked.
- The publication date of Adyen's terms and conditions is the page's own "Last update 1 November 2023" (three years; at the threshold, so no evidence-age flag was added, the date is in the sentence).

## Rulings and format

- Ruling 22: 22 inline external links reduced to plain attributions; every URL is in Sources and Evidence.
- Ruling 30: the "last modified March 2023" date and evidence-age flag on Adyen's Level 2/3 page removed.
- Ruling 16: the deemed-supplier statements agree with it (goods since 2021, two service sectors from 2028, not fitness studios).
- Ruling 23: the page's reference to application fees on Connect agrees with destination charges with `on_behalf_of`.
- Terms glossed: HST, ERP, split, form 1099-K. `timetoread` set to 22 (4,995 words ÷ 230). Length is 5 words under the spec's maximum of 5,000 after trimming the additions.
- No unit added, dropped, merged or reordered. `spec.json`: evidence entries of p18, p19 and p23 and two open questions updated to match; changelog entry added.
- All 29 source URLs return 200 at the URL listed. All six `[[permalinks]]` are valid.

## Larkfield consistency

Checked against the ledger: Tuesday 9 March 2027 (weekday correct), 19:42, €120.00, €117.47, payout 11 March, refund €84.00 on 18 March, Studio Noord on Adyen, plans €89/€189/€349, Stripe Billing since 2018, hand-over in May 2027, Stripe Tax since 2023, 1,450 German studios, 180 assumed studios, revenue €46.0M = €24.5M + €19.8M + €1.7M (53%), Femke de Graaf and Priya Raman (roles, she/her). Arithmetic rechecked: €189 × 21% = €39.69; €89 × 19% = €16.91; 180 × €16.91 = €3,043.80; €120.00 ÷ 1.09 = €110.09 and €9.91; €84.00 × 9/109 = €6.94.

## Ledger conflicts

None found.

## For other pages

- Any page that cites `https://help.adyen.com/knowledge/finance/invoices/what-kind-of-tax-is-applied-to-my-invoice` should cite `https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice` (301 redirect as of 17 November 2026).
- `32-merchant-of-record` and `27-subscriptions-and-billing-engines`: if either says Adyen is silent on who bears tax on a merchant's sales, clause 4.5 of Adyen's terms and conditions is a public statement; if either says Orb's tax handling is unknown, Orb's documentation says it uses third-party tax providers.
- Any page citing `docs.stripe.com/tax/custom` as "Stripe Tax API": the page is now `docs.stripe.com/tax/standalone-tax-api`, titled "Standalone Tax APIs".
- `_research/brief-billing-and-revenue.md` section 4.4 calls Adyen's tax pages help-center content and says nothing was found beyond fees; the VAT split type, the 1099-K filing and the terms' clause 4.5 were missed there.
