---
title: "Whose Tax, at What Rate: Tax Calculation in the Payment Path"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How does indirect tax get calculated, collected and reported when the payment provider is also the tax engine? The provider can do the arithmetic because its invoice holds the facts, but registering, counting thresholds, filing and the liability itself stay with the seller."
permalink: billing-and-payment-tax
timetoread: 22 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn what a tax calculation needs, which compliance steps a payment provider performs, and how to tell a correct zero from a missing one.

> **KEY POINTS:**
>
> * **A provider can calculate tax; it cannot owe it.** The checkout or invoice holds the facts a calculation needs: who sells, what is sold, where the customer is. Calculating is one of four steps, and the liability for all four stays with the seller.
> * **Stripe Tax is a calculator with partial sight.** As of November 2026 its documentation says it returns zero where the seller has recorded no registration, counts thresholds only on the sales it sees, and files itself only in the United States and for selected registrations in Ireland and Canada.
> * **The comparison is one-sided.** No public source was found that shows an Adyen product calculating, collecting or filing tax on a merchant's sales. On Adyen, and for any business on two providers, the calculation lives in your own system or a separate tax engine.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Black-Box Balance** — a seller's payout contains tax that is not its revenue, and nothing in the payment path says how much.
> * **The Accidental Bank** — a platform can be made liable for its sellers' tax by a rule it never checked, the same way it can become a holder of their money.

<br>
Three invoices for the same software plan each show a tax line of €0.00. On the first, the customer is a business in another country that must account for the tax itself. On the second, the seller never told the tax calculator that it is registered where the customer lives. On the third, somebody marked the product as non-taxable years ago. **The three zeros look identical on the page, and only the first means that the seller owes nothing.**

A payment provider can calculate tax at all because the checkout or invoice it runs already holds the facts the calculation needs: who sells, what is sold and where the customer is. But **calculating is one of four steps**, next to knowing where tax is due, registering there, and filing and paying, and the liability for all four stays with the seller. [[invoicing-collections-and-dunning]] said a finalized invoice is frozen for tax reasons; this chapter is about the tax line on it. The public record shows a tax product at Stripe and none at Adyen, so the comparison here is one product against what a merchant must bring itself.

**Where we are in the payment's journey.** Tax is not a step on the path of Mila Janssen's class pass, the payment this book follows at Larkfield, the fictional studio-software platform ([[meet-larkfield]]). It is decided before the path starts and reported after it ends. The €120.00 that Mila's bank approved on Tuesday 9 March 2027 at 19:42 already contained the tax, and Studio Noord, which received €117.47, owes that tax to the Dutch tax authority weeks later. Nothing in the authorization, the settlement or the payout says how much it is.

The chapter starts with three Larkfield invoices that show no tax. It then defines what indirect tax asks of a seller and goes through what Stripe Tax does, step by step. Next it sets Stripe beside Adyen, compares four places the calculation can live, works two Larkfield cases and ends with the ways tax in the payment path goes wrong.

## Setting the Scene at Larkfield: Three Invoices with No Tax

In May 2027 the payments team took over Larkfield's billing integration, the Stripe Billing setup that charges studios €89, €189 or €349 a month, from the growth team that had run it since 2018. Femke de Graaf, Larkfield's head of payments engineering, found Stripe Tax, Stripe's tax product, switched on since 2023. It had exactly one tax registration recorded, the Dutch one; a registration is a seller's enrollment with a tax authority, and the next section defines it. Nobody had reviewed the setting since.

Three invoices from that month, in the table below, show what that produced. The rates are the standard rates of value-added tax (VAT): 21% in the Netherlands and 19% in Germany (European Commission, Your Europe portal, table last checked 13 July 2026). The Cologne zero is a reverse charge, a rule under which a business that buys across a border accounts for the tax itself. The Leipzig zero exists because no registration covered Germany. Priya Raman, the finance controller, read the export and asked two questions: "Two zeros. Which one did we mean? And the dashboard says tax is on, so is this Stripe's job now?"

| Studio | Plan | Customer's VAT number | Tax on the invoice | Total |
| --- | --- | --- | --- | --- |
| Utrecht, Netherlands | €189.00 | On file | €39.69 (21%) | €228.69 |
| Cologne, Germany | €189.00 | On file | €0.00 | €189.00 |
| Leipzig, Germany | €89.00 | None | €0.00 | €89.00 |

## What Indirect Tax Asks of a Seller

Indirect tax is a tax on a sale that the seller collects from the buyer and passes on to a tax authority. Europe calls it VAT, Canada and much of the Asia-Pacific region call it goods and services tax (GST), and the United States calls it sales tax. Stripe's documentation (n.d., accessed November 2026) puts the mechanism in one sentence: "The buyer pays the tax and the seller forwards it to the government" (the page "How Stripe Tax works"). The seller is a collector for the state, which is why the seller answers for a wrong amount. The rate belongs to a place and a product category: "each member country is responsible for setting its own rates" (European Commission, same table).

A calculation therefore needs three facts and one piece of state. The facts are who sells and from where, what is sold, and where the customer is. The customer's status refines the third: a business that buys across a border usually accounts for the tax itself, the reverse charge of the Cologne invoice. The state is where the seller is registered. Stripe lists the same inputs: "Stripe Tax uses your business address, tax registrations, product tax codes, customers' locations, and customer status to determine the correct tax rates" (same page). A checkout or an invoice holds the facts at the moment the amount is fixed, and the tax must be on the invoice before it freezes: "Stripe calculates the tax at the published rate at the time of invoice finalization" (Stripe's page on collecting tax on invoices, n.d., accessed November 2026). That is why the calculation sits beside billing and checkout and not in the ledger, which only records the result.

| Input | Where a billing or checkout flow has it | If it is missing or wrong |
| --- | --- | --- |
| Seller's location | Account settings | The wrong country's rules |
| What is sold | A tax category on the product (Stripe calls it a product tax code) | The wrong rate, or tax on an exempt product |
| Customer's location, or where a service is performed | Billing address, shipping address or venue | No calculation, or the wrong jurisdiction |
| Customer's status | A tax number or an exemption flag on the customer | Tax charged to a business that should account for it itself, or the reverse |
| Seller's registrations | Nowhere, unless the seller enters them | A calculated zero |

A **tax registration** is the seller's enrollment with a tax authority, which allows and obliges it to collect that authority's tax. Whether a seller must register usually depends on a **threshold**, a volume of sales into the territory. In the European Union, the rules that apply since 1 July 2021 set "a new EU-wide threshold of EUR 10 000" for cross-border sales to consumers of goods and of telecommunications, broadcasting and electronic services. Below it such sales "may remain subject to VAT in the Member State where the taxable person is established"; above it the customer's country taxes them, and a seller can "register in one EU Member State" and declare them all through the One Stop Shop (OSS) (European Commission, One Stop Shop page, n.d., accessed November 2026). In the United States the Supreme Court, in *South Dakota v. Wayfair* on 21 June 2018, overruled the rule that only sellers with a physical presence in a state could be made to collect its sales tax; the South Dakota law before it covered sellers that "deliver more than $100,000 of goods or services into the State or engage in 200 or more separate transactions" a year (opinion of the Court, 2018). **(Evidence age: 8 years; the holding stands, and the states' current thresholds, which differ, were not verified here.)** A duty that follows from sales volume alone is called economic nexus. In both systems the threshold counts all of the seller's sales into the territory, through every channel.

Registration is the second of four steps. Stripe's documentation names them: "1. Understand which locations require you to collect tax. 2. Register for tax in those locations. 3. Calculate and collect tax. 4. File and remit the tax you collected" (How Stripe Tax works). To remit is to pay over what was collected. A calculation, however exact, is the third step, and the seller owes all four. The only way to hand over the tax itself is to let a provider sell in its own name as merchant of record, the supplier for indirect tax where local rules allow ([[merchant-of-record]]).

For a platform, though, the law itself can change who the seller is. A **deemed supplier** is a platform that VAT law treats as if it had bought and resold what its sellers sell, so that the platform owes the tax. In the EU, "Online marketplaces/platforms facilitating supplies of goods are, in certain circumstances, deemed for VAT purposes to have received and supplied the goods themselves" (European Commission, One Stop Shop page). The VAT in the Digital Age package, adopted on 11 March 2025, extends the idea to services: "From 1 July 2028: deemed supplier measure for short-term accommodation rental and passenger transport platforms (Member States can delay implementation until 1 January 2030)" (European Commission, page on VAT in the Digital Age, n.d., accessed November 2026). So who owes the tax is a property of each transaction that a platform must know, and the answer carries a date. My reading, which is not legal advice: a platform for fitness studios is in neither category on the face of these texts, and whether a national rule reaches it is a question for a tax adviser.

## How Stripe Tax Works, Step by Step

Stripe Tax calculates wherever Stripe already fixes an amount: in Checkout (Stripe's hosted payment page), on a subscription's invoice at finalization, and through an API for custom flows, including "when processing payments off-Stripe" (Stripe's page on its standalone Tax APIs, n.d., accessed November 2026). A calculation is a quote; a tax transaction records that the sale happened, and reports and filing read transactions. When an input is unusable, Stripe stops and does not guess. If a customer's address cannot be resolved, the invoice's tax status becomes `requires_location_inputs`, and then "Stripe can't calculate the taxes, can't finalize the invoice, and can't collect the payment" (Stripe's page on collecting taxes for recurring payments, n.d., accessed November 2026). A missing tax input is thus a billing failure: the renewal is not charged. The figure below places the calculation among the four steps.

<!-- illustration-placeholder
{
  "id": "30-four-step-cycle",
  "status": "pending",
  "asset": "assets/images/30-tax/30-four-step-cycle.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that says where Stripe Tax calculates",
  "visual_goal": "Show tax compliance as a cycle of four steps in which the provider performs the calculation and the seller holds the other three.",
  "prompt": "Structural cycle diagram with four round stations arranged clockwise on a ring. Top station: a map with a magnifying glass, labeled \"Know where\". Right station: a form with a stamp, labeled \"Register\". Bottom station: a calculator next to an invoice, labeled \"Calculate\". Left station: an envelope going to a government building, labeled \"File and pay\". Blue arrows run clockwise between the stations, each named: \"thresholds\" from Know where to Register, \"registrations\" from Register to Calculate, \"tax collected\" from Calculate to File and pay, \"sales totals\" from File and pay back to Know where. A person at a desk tagged \"Seller\" stands outside the ring with thin teal lines to the top, right and left stations. A generic office building tagged \"Provider\" stands below the ring with one thick orange line to the bottom station only. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A ring of four steps: know where, register, calculate, file and pay. A seller is linked to three of them and a provider to the calculation only.",
  "caption": "Calculating and collecting is one of four steps; the provider performs it, and knowing where tax is due, registering and filing stay in the seller's hands."
}
-->

A missing registration, by contrast, stops nothing. "Stripe only calculates tax in jurisdictions where you have an active tax registration. Without a registration in the customer's location, the calculation returns zero tax" (standalone Tax APIs page). That is the Leipzig invoice. The reason travels in a separate field: "The API returns the reason for a tax result in the taxability_reason field", with values such as `reverse_charge`, `customer_exempt`, `zero_rated` and `not_collecting` (Stripe's page on zero tax amounts and reverse charges, n.d., accessed November 2026). Even the reason needs reading: the page calls `not_collecting` "ambiguous", because it covers both a missing registration and a product the seller marked non-taxable. So the three zeros of the opening differ in a field that an export of amounts drops, and two of them share a value.

<!-- illustration-placeholder
{
  "id": "30-three-zeros",
  "status": "pending",
  "asset": "assets/images/30-tax/30-three-zeros.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on the zero result and its reason field",
  "visual_goal": "Show three invoices that look the same, each with a zero tax line, and a different cause standing behind each one.",
  "prompt": "Conceptual illustration with three identical paper invoices side by side in the foreground, each showing a few unlabeled gray lines and one highlighted line labeled \"Tax €0.00\". Behind each invoice a translucent tag rises like a shadow, connected to it by a thin dashed line. Behind the left invoice: a tag with two office buildings and an arrow between them, labeled \"Buyer accounts\", with a small green check mark. Behind the middle invoice: a tag with an empty form and a missing stamp, labeled \"Not registered\", with a small orange warning triangle. Behind the right invoice: a tag with a product box and a crossed-out percent sign, labeled \"Marked non-taxable\", with a small orange warning triangle. A person with a magnifying glass looks at the three invoices from the front and sees only the identical faces. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Three identical invoices each show tax of zero euros. Behind them stand three different causes: the buyer accounts for the tax, the seller is not registered, the product was marked non-taxable.",
  "caption": "Three invoices with the same zero tax line and three different causes; only the reason stored with the amount tells them apart."
}
-->

The reverse-charge zero has its own weakness: it rests on a tax number the customer typed. "Stripe Tax uses customer tax identification numbers to determine whether a transaction is B2B", business-to-business, and it "doesn't validate whether the provided tax identification number exists or is valid" (How Stripe Tax works). Stripe Billing does check EU VAT numbers against VIES, the European Commission's VAT number database, and reports a status such as `verified` or `unverified`. But the check does not gate the calculation: "Stripe Tax applies the reverse charge or zero rate according to applicable laws when the tax ID has the required number format, regardless of the government verification result", and "you're responsible for determining how to handle an `unverified` tax ID" (Stripe's page on customer tax IDs, n.d., accessed November 2026). By that description, a well-formed number that fails verification keeps producing a zero until the seller acts.

Next comes the step that reads those calculated transactions: knowing where tax is due. Stripe supports it with a monitor: "Stripe Tax tracks your Stripe-processed sales (minus refunds) based on each customer's location and compares these sales against local tax registration thresholds." The page states its limits: "We only monitor Stripe-processed sales or imported transactions", "Application fees that Connect platforms charge don't count toward the platform's tax registration thresholds", and "it's up to you to confirm whether registration is actually required in each jurisdiction" (the page "Monitor your obligations", n.d., accessed November 2026). A threshold counts all of a seller's sales; the monitor counts Stripe's. The documented remedy is to bring the rest in, by file import or by recording a payment taken elsewhere through the Tax API, which then "is included in threshold monitoring by default in live mode" (Stripe's pages on imports and on off-Stripe payments, n.d., accessed November 2026).

Registering and filing then remain mostly the seller's. "You must register with the tax authority in a location to collect taxes there" (How Stripe Tax works); Stripe can start a registration in US states and points to a partner elsewhere. As for filing, "Stripe Tax offers automated filing in the US, as well as automated filing for selected registrations in Ireland and Canada", namely "non-Union OSS registrations in Ireland and simplified federal GST/HST registrations in Canada" (the page "File and remit", n.d., accessed November 2026). HST is Canada's harmonized sales tax. Non-Union OSS is "for businesses based outside the EU selling services to individuals in the EU" (Stripe's page on tax in the European Union). Elsewhere filing goes through partners, and the page lists global filing as a private preview. By that list, **as of November 2026 a seller based in the EU files its own EU returns or uses a partner.**

On a platform, the question of the liable party comes before any calculation. Stripe's guide for Connect, its product for platforms, opens with it: "The first step for using Stripe Tax with Connect requires you to determine which entity has the obligation to collect and report taxes" (the page "Use Stripe Tax with Connect", n.d., accessed November 2026). It offers one setup in which the connected accounts (the platform's sellers) are liable and one in which the platform is, and the tooling follows the answer per charge. With sellers liable, each connected account needs its own settings and registrations, or the silent zero repeats: "Stripe Tax returns a tax amount of `0.00` and sets the taxability reason to not_collecting" (the page "Tax for software platforms", n.d., accessed November 2026). With the platform liable, some charges still cannot be counted: "Separate charges and transfers without `on_behalf_of` aren't included. This is because Stripe can't know who the liable party for the transfer is" (Monitor your obligations). [[platform-payment-models]] owns the charge types; the point here is that the funds flow has to carry the liable party.

## Stripe and Adyen: Where They Differ

For Adyen the evidence stops early. The research for this book searched Adyen's documentation (docs.adyen.com), its help center (help.adyen.com), its product pages and the open web on 17 November 2026, and found no product that calculates, collects or files tax on a merchant's sales. It found four things, the first three in Adyen's documentation (n.d., accessed November 2026). Adyen taxes its own fees: it "does not deduct sales tax or value-added tax (VAT) from your settlement batches" and shows the tax on its invoice to the merchant, in some US states and in France (the page "Payment processing invoice"). A merchant can send a tax amount it has already computed: "Level 2/3 enhanced scheme data (ESD) helps you track the amount spent on corporate cards and the amount of sales tax" (the page "Level 2/3 data"), and on a platform a split, the instruction that divides a payment between balances, can have the type `VAT`, which "Books the value-added tax (VAT) incurred on a payment to the specified `account`" (the page on splitting transactions). For platform sellers in the United States Adyen files form 1099-K, a report of a seller's payment volume and not a tax on sales (the page "Provide tax forms (US only)"). And Adyen's terms and conditions (last updated 1 November 2023) leave the tax with the merchant: "each party will be required to comply with its own tax obligations under Applicable Law". The missing calculator is absence of evidence in public pages, not a statement by Adyen. Orb, the billing company whose acquisition Adyen closed on 1 July 2026 (press release of that date), does not calculate tax either: "Orb connects to third-party tax providers to calculate tax on Orb invoices" (Orb documentation, n.d., accessed November 2026).

The table sets the two side by side; its last column is my reading, an inference from the public record. The cells repeat facts cited above (documentation, n.d., accessed November 2026, unless a year is given).

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Calculating tax on a sale | Stripe Tax: in Checkout, on invoices, and through an API that also covers payments taken elsewhere | Not public. Documented: the merchant may send a tax amount it computed (Level 2/3 data) | On Adyen the calculation is done in your system before the payment request is built |
| What a zero result says | Zero where no registration is recorded; the reason is in `taxability_reason` | Not public | Only the system that calculates can explain a zero; on Adyen that is your system |
| Threshold monitoring | Stripe-processed, imported or API-recorded sales only; the seller confirms the obligation | Not public | A monitor inside one provider undercounts for a business on two |
| Registration and filing | Starts registrations in US states; files in the US and for selected registrations in Ireland and Canada; partners elsewhere | Not public. Documented: files US form 1099-K for platform sellers | Steps two and four are mostly outside both providers |
| Liable party on a platform | The platform decides; monitoring follows the charge type | Not public. Documented: a `VAT` split books a tax amount the platform supplies | The liable party belongs in your own payment record on both |
| Who owes the tax | The seller: "You must file and remit the tax you collect" | The merchant: "each party will be required to comply with its own tax obligations" (terms and conditions, 2023) | No material difference in the public record |

On Stripe, treat the registration list and the reason behind every zero as your own data: keep the list in your records, compare it with what Stripe holds, and export `taxability_reason` with every invoice. On Adyen, decide before you integrate which system computes tax, compute it before the payment request is built, and send Adyen the gross amount.

## Four Places the Calculation Can Live

One provider has a calculator and the other has none on record, so a business on either or both has to choose where the calculation lives. The table below gives the four realistic places. They differ in what the calculator can see and in who maintains the rules. Built into one provider's flows, it sees that provider's sales. As that provider's API, or as an independent tax engine, it sees every channel the seller sends to it: Avalara describes its engine as working "across your ERP, billing, purchasing and commerce systems", and Vertex advertises "tax rules and rates for 19,000 jurisdictions" (the two vendors' product pages, n.d., accessed November 2026; vendor claims). (ERP: a company's finance and operations system.) As the seller's own rate table it sees everything and knows only the rules the seller wrote.

| Design | What it sees | Who maintains rates and rules | Fits when | Limits |
| --- | --- | --- | --- | --- |
| Provider's built-in tax (Stripe Tax in Checkout and on invoices) | That provider's sales | The provider | One provider carries all taxable sales | Thresholds undercount once a second channel exists |
| Provider's tax API for every channel (Stripe Tax API, with payments taken elsewhere recorded in it) | What you send | The provider | Two providers, one of them Stripe | Tax history and reports sit with one payment provider |
| Independent tax engine (for example Avalara AvaTax or Vertex O Series) | What you send | The engine's vendor | Several providers, an ERP, many jurisdictions or product categories | One more vendor and one more call in the checkout path |
| Your own rate table | Everything in your system | You | One country and few rates, or sellers who set their own rate | You must notice every rule change yourself |

<!-- illustration-placeholder
{
  "id": "30-partial-sight",
  "status": "pending",
  "asset": "assets/images/30-tax/30-partial-sight.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the table of four designs",
  "visual_goal": "Show that a threshold monitor inside one provider sees only that provider's share of a seller's sales, while the threshold counts all of them.",
  "prompt": "Structural diagram. Left: a small office building tagged \"Seller\". From it three horizontal streams of euro coins flow to the right, stacked one above the other: the top stream passes through a generic building labeled \"Provider A\", the middle stream passes through a generic building labeled \"Provider B\", the bottom stream passes through a paper invoice icon labeled \"Other invoices\". Above the top stream only, a monitor screen with a gauge is labeled \"Threshold monitor\" and a blue cone of light from it covers the top stream alone; the middle and bottom streams are in soft gray shade. Far right: the three streams pour into one tall glass container with a horizontal orange line across it labeled \"Threshold\"; the combined coins rise above the line, while a small ghost outline shows that the top stream alone would stay below it. A teal arrow labeled \"import\" curves from the two shaded streams up to the monitor. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A seller's sales flow in three streams through two providers and other invoices. A threshold monitor lights only the first stream, while all three together pass the threshold.",
  "caption": "A monitor built into Provider A (Stripe, in this chapter) counts only the sales Provider A processes, while a registration threshold counts all of the seller's sales; importing the rest is one of the two fixes."
}
-->

The rule I use: built-in tax while one provider carries all your taxable sales. From the day a second channel exists, either feed its sales into the first provider's tax product or move the calculation to an independent engine. These are the only two fixes for partial sight: bring the unseen sales to the calculator, or take the calculator out of the provider. I keep a rate table only where sellers set their own rates in one country, which is the case of a studio selling classes. Merchant of record is a different decision, because it changes who the seller is and takes the choice away: Stripe's Managed Payments lists "Third-party tax integrations" among the integrations it does not support (Stripe documentation, n.d., accessed November 2026).

## In Practice at Larkfield: Two Sellers, Two Calculations

On Mila's class pass the seller is Studio Noord, and Studio Noord owes the VAT. Larkfield is not the merchant of record and, on my reading above, not a deemed supplier. The €120.00 Mila paid is a tax-inclusive price. The Dutch tax authority (n.d., accessed November 2026) puts giving people the opportunity to do sport under the reduced rate of 9%, puts lessons given without the accommodation under 21% and exempts nonprofit sports organizations. Assume 9% applies here *(assumption: which treatment fits a studio's classes is the studio's question for its own adviser)*: the pass is €110.09 net and €9.91 VAT. The booking app computes that split from a rate the studio sets and sends the provider one number, €120.00. This is the fourth design, and it is the same on Adyen and on Stripe. The €117.47 paid out on 11 March includes €9.91 that is not the studio's revenue. When Mila is refunded €84.00 on 18 March, €6.94 of VAT goes back with it: a refund is a tax event too. In the payment record store every payment names the studio as the liable party.

On its own subscription, by contrast, Larkfield is the seller, and it uses the first design. The fix for Leipzig is one piece of state. Larkfield registers for the One Stop Shop in the Netherlands and records the registration in Stripe Tax, and the next €89.00 invoice carries 19% German VAT: €16.91, for a total of €105.91. Assume 180 of the 1,450 German studios have no VAT number and are on the €89 plan *(assumption)*: that is 180 × €16.91 = €3,043.80 a month that was never charged. Whether a business customer without a VAT number is taxed as a consumer is a question of law this chapter does not settle; Stripe's calculation treats it so, and in this fiction Priya's adviser agrees. For Cologne, Femke's team stores `taxability_reason` with every invoice line in the finance export and listens for the event that reports a tax number's verification. A person reviews any customer whose number comes back `unverified` before the next invoice.

There remains the first step, knowing where the next registration is due. Stripe's monitor sees the €24.5 million of subscriptions that Stripe bills, which is 53% of Larkfield's 2026 revenue of €46.0 million. It does not see the €19.8 million of payment fees: the part taken on Adyen never passes through Stripe, and Stripe's own page excludes the application fees a platform charges on Connect. Nor does it see the €1.7 million of other revenue, which is invoiced from the finance system *(assumption)*. Which of those sales are taxable, and where, is the adviser's question; the monitor never counted them. Priya's team now counts sales per territory from the ledger, which covers both providers, and imports into Stripe Tax what Stripe did not process.

## When It Goes Wrong

Six failures recur, and none is exotic. The table gives each with a detection that reads fields Stripe documents; the third is the undercount Larkfield has just met. The last row rests on one line of Stripe's documentation: "The Tax Transactions page only includes *transactions* and not *calculations*" (Stripe's page on Stripe Tax with PaymentIntents, n.d., accessed November 2026).

| Failure | What happens | How you detect it | Recovery |
| --- | --- | --- | --- |
| Silent zero | No registration is recorded; tax is zero and nothing fails | Count invoices with `not_collecting` per country each month | Record the registration; settle past periods with your adviser |
| Unverified tax number | A reverse charge rests on a number that failed, or never finished, verification | List customers whose verification status is not `verified` | Review the customer before the next invoice |
| Undercounted threshold | The monitor counts one provider's sales | Compare the monitor's totals with sales per territory from your ledger | Import the other sales, or count outside the provider |
| Blocked invoice | An unusable address stops finalization; the renewal is not collected | The `invoice.finalization_failed` event with `requires_location_inputs` | Ask the customer for an address; validate addresses when they are entered |
| Refund without reversal | In a custom flow the payment is refunded and the tax record is not | Compare refunds with reversal tax transactions | Create the reversal for each refund, as Stripe's off-Stripe guide requires |
| Calculation without a transaction | Tax was quoted and charged but never recorded | Compare payments with tax transactions | Create the missing transactions |

Only the blocked invoice raises an error at the moment of the charge. The other five produce an amount that is plausible and wrong, which is the shape of the failures in [[payment-reconciliation-and-reporting]]: a statement nobody compared with a second record. So the control is a periodic comparison with a named owner: tax collected per jurisdiction, against the invoices, against the list of registrations. At Larkfield nobody owned the tax setting for four years; since May 2027 Priya Raman owns the registration list and Femke's team owns the export.

## What to Take Away

**Established.**

- The seller owes indirect tax and all four steps: know where it is due, register, calculate and collect, file and remit. Stripe's documentation frames its own product this way.
- Registration follows thresholds counted over all of a seller's sales into a territory: one EU-wide €10,000 threshold for cross-border consumer sales since 1 July 2021, and sales-based nexus in US states since the *Wayfair* decision of 21 June 2018.
- Stripe documents that its calculation returns zero where no registration is recorded, and that its monitor counts only Stripe-processed or imported sales.
- No public source was found for an Adyen product that calculates, collects or files tax on a merchant's sales. That is absence of evidence.

**Depends on context.**

- Where the calculation lives depends on how many providers, jurisdictions and product categories you have: built-in tax fits one provider; a second channel calls for imports or an independent engine.
- Whether a platform owes its sellers' tax depends on its category and country, and the answer changes: the EU adds two service sectors from 1 July 2028.

**The author's synthesis.**

- A calculated tax can be exact and still wrong, because whether it should have run, for whom and on which sales are decided outside the calculation. So I store the reason with every tax amount, give the registration list an owner, and record the liable party on every platform transaction.
- The three zeros of the opening differ only in state the seller holds. "Tax is switched on" is where the responsibility starts.

## Questions to Ask

1. Where are we registered, and does the list in our provider match the list our finance team holds?
2. For last month's zero-tax invoices, which reason does each carry, and who reviewed the ones that are not reverse charges?
3. Which of our sales does the provider's threshold monitor not see, and how do they reach it?
4. What happens to a renewal when the customer's address cannot be used for tax?
5. Is a customer's tax number verified before it changes what we charge, and what do we do when verification fails?
6. On our platform, which party owes the tax on each kind of sale, and where is that recorded per transaction?
7. Has anyone checked whether our platform's category makes it a deemed supplier, and when was that last rechecked?
8. Does every refund in a custom flow create a tax reversal?

Tax reads the lines of an invoice and asks where the sale took place and who owes the tax. A second calculation reads the same lines and asks a different question: in which period does the amount count as revenue? As with tax, the provider can compute it only for what it sees. [[billing-revenue-recognition]] takes that up.

## Sources and Evidence

*Company, product and investor sources*

- [How Stripe Tax works](https://docs.stripe.com/tax/how-tax-works), Stripe documentation, n.d., accessed 2026-11 — the four steps, the inputs, tax numbers and B2B, registering (Stripe in US states, a partner elsewhere).
- [Standalone Tax APIs](https://docs.stripe.com/tax/standalone-tax-api), Stripe documentation, n.d., accessed 2026-11 — zero tax without an active registration; calculations and transactions for custom and off-Stripe flows.
- [Zero tax amounts and reverse charges](https://docs.stripe.com/tax/zero-tax), Stripe documentation, n.d., accessed 2026-11 — `taxability_reason` and the ambiguity of `not_collecting`.
- [Customer tax IDs](https://docs.stripe.com/billing/customer/tax-ids), Stripe documentation, n.d., accessed 2026-11 — VIES validation, verification statuses, reverse charge on number format.
- [Monitor your obligations](https://docs.stripe.com/tax/monitoring), Stripe documentation, n.d., accessed 2026-11 — what threshold monitoring counts and its exceptions, including Connect charge types and application fees (volatile).
- [Import transactions into Stripe Tax](https://docs.stripe.com/tax/imports), Stripe documentation, n.d., accessed 2026-11 — imports of sales from other channels.
- [Collect tax on off-Stripe payments](https://docs.stripe.com/tax/off-stripe), Stripe documentation, n.d., accessed 2026-11 — off-Stripe payments in monitoring; a reversal per refund.
- [Stripe Tax with PaymentIntents](https://docs.stripe.com/tax/payment-intent), Stripe documentation, n.d., accessed 2026-11 — calculations versus tax transactions.
- [File and remit](https://docs.stripe.com/tax/filing), Stripe documentation, n.d., accessed 2026-11 — the seller must file and remit; filing in the US, Ireland and Canada, partners, global filing in private preview (volatile).
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect), Stripe documentation, n.d., accessed 2026-11 — the liable entity as the first decision.
- [Tax for software platforms](https://docs.stripe.com/tax/tax-for-platforms), Stripe documentation, n.d., accessed 2026-11 — connected accounts' settings and the zero without a registration.
- [Automatically collect tax on invoices](https://docs.stripe.com/tax/invoicing), Stripe documentation, n.d., accessed 2026-11 — the rate at finalization.
- [Collect taxes for recurring payments](https://docs.stripe.com/tax/subscriptions), Stripe documentation, n.d., accessed 2026-11 — `requires_location_inputs` and the invoice that cannot finalize.
- [Tax in the European Union](https://docs.stripe.com/tax/supported-countries/european-union), Stripe documentation, n.d., accessed 2026-11 — the non-Union One Stop Shop scheme.
- [Managed Payments](https://docs.stripe.com/payments/managed-payments), Stripe documentation, n.d., accessed 2026-11 — third-party tax integrations not supported.
- [Payment processing invoice](https://docs.adyen.com/reporting/invoice-reconciliation/payment-processing-invoice), Adyen documentation, n.d., accessed 2026-11 — tax on Adyen's own fees (the help-center article "What kind of tax is applied to my invoice?" now redirects to this page).
- [Level 2/3 data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3), Adyen documentation, n.d., accessed 2026-11 — a tax amount sent by the merchant.
- [Split specific transactions between balance accounts](https://docs.adyen.com/platforms/online-payments/split-transactions), Adyen documentation, n.d., accessed 2026-11 — the `VAT` split type.
- [Provide tax forms (US only)](https://docs.adyen.com/platforms/us-tax-forms), Adyen documentation, n.d., accessed 2026-11 — Adyen files form 1099-K for US platform sellers.
- [Adyen Terms and Conditions](https://www.adyen.com/legal/adyen-terms-and-conditions), Adyen, last updated 2023-11-01 — clause 4.5: each party complies with its own tax obligations (the clause also has the merchant indemnify Adyen for taxes on what it sells).
- [Adyen Closes Talon.One and Orb Acquisitions; Announces Leadership Updates Across Product and Finance](https://www.adyen.com/press-and-media/adyen-closes-talonone-and-orb-acquisitions-announces-leadership-updates), Adyen press release, 2026-07-01 — closing date of the Orb acquisition.
- [Tax: Overview](https://docs.withorb.com/integrations-and-exports/tax), Orb documentation, n.d., accessed 2026-11 — Orb calculates tax through third-party tax providers.
- [Avalara AvaTax](https://www.avalara.com/us/en/products/calculations.html), Avalara, n.d., accessed 2026-11 — an independent tax engine across systems (vendor claim).
- [Vertex O Series](https://www.vertexinc.com/solutions/products/vertex-indirect-tax-o-series), Vertex, n.d., accessed 2026-11 — rules and rates for 19,000 jurisdictions (vendor claim).

*Standards, regulation and official documentation*

- [VAT e-Commerce: One Stop Shop](https://vat-one-stop-shop.ec.europa.eu/index_en), European Commission, n.d., accessed 2026-11 — rules from 1 July 2021, the EUR 10 000 threshold, the One Stop Shop, deemed supplier for goods.
- [VAT in the Digital Age (ViDA)](https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en), European Commission, n.d., accessed 2026-11 — adoption on 11 March 2025; deemed supplier for two service sectors from 1 July 2028.
- [VAT rules and rates](https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm), European Commission, Your Europe, table last checked 2026-07-13 — standard rates in the Netherlands and Germany; each country sets its own rates.
- [Btw-tarief gelegenheid geven om te sporten](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/sportbeoefening_waaronder_zwembaden_en_sauna/gelegenheid_geven_om_te_sporten/), Belastingdienst (Dutch Tax and Customs Administration), n.d., accessed 2026-11, in Dutch — the 9% rate for giving the opportunity to do sport, 21% for lessons given without the accommodation, the exemption for nonprofit sports organizations.
- [South Dakota v. Wayfair, Inc.](https://www.law.cornell.edu/supremecourt/text/17-494), Supreme Court of the United States, 2018-06-21, text at Cornell Legal Information Institute — the physical-presence rule overruled (evidence age: 8 years).

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
