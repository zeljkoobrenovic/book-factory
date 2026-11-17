# Research brief: Platforms, marketplaces and embedded finance (Stripe Connect, Adyen for Platforms, accounts, cards and capital)

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 33 (platform payment models), 34 (platform onboarding and verification), 35 (splits, balances and platform payouts), 36 (embedded finance), journey 44 (a platform payment split, paid out and refunded), and parts of 14 (payouts and money movement) and 26 (compliance as a system). The two anchors are Stripe Connect and Adyen for Platforms; other companies appear only as contrast.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Paraphrases stay close to the source and quoted text is quoted. Undated documentation and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press), not a primary document fetched in this session.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the researcher's inference, including every statement about how Stripe or Adyen works internally beyond what it has published, every mapping between the two vocabularies, and every "what this suggests".

**Evidence age matters.** Almost everything here comes from living documentation that carries no reliable publication date. Stripe's documentation pages are undated. Adyen's documentation pages carry a `last_modified` field in their markdown front matter, but it is not trustworthy as a content date: several pages that describe 2026 features show 2020–2022, and others show today's date. All Adyen documentation is therefore tagged "n.d., accessed 2026-11". Sources published before November 2023 are flagged **(evidence age: N years)**.

**Research limitation.**

- **Mastercard Rules** could not be fetched: the public PDF on mastercard.us returned "Access Denied" (HTTP 403) to both fetch methods. Mastercard's payment-facilitator threshold is supported only by a 2014 trade-press article. The Visa Core Rules (24 October 2026 edition) were downloaded and read, so the network-rule section rests on Visa.
- **Adyen pages that returned no markdown** (the site served its HTML shell): the dedicated pages for negative balances, verification deadlines, instant payouts, cross-border payouts and the classic-to-balance-platform migration under the URL names tried. The facts on deadlines and payout priorities below come from neighbouring pages that did render. No Adyen page describing a platform-level negative-balance procedure was found.
- **Adyen's licence position does not appear in the documentation pages fetched**; it is stated in the H1 2026 shareholder letter and a 2021 press release. The page `adyen.com/legal/licenses` returned 404.
- **Stripe's pricing page** was served in the Netherlands locale (euro prices). US-dollar list prices were not verified.
- **Stripe's partner banks** are named piecemeal across pages (Fifth Third Bank, Celtic Bank, Lead Bank); no single current list was found. Evolve Bank & Trust, often named in older secondary coverage, did not appear on any page fetched in this session.
- **Hyperwallet, Marqeta and Braintree Marketplace** were not verified; they are mentioned only as unverified contrast or omitted.
- Two documentation pages contained instructions addressed to automated readers (a Stripe note telling coding agents to ignore the legacy account-types page; an Adyen note about SDK version numbers). They concern code generation, not research, and were not acted on; the legacy page was read because its history is in scope.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: preview and pilot status, country lists, product names (Stripe's Treasury naming has changed at least twice), list prices, Accounts v2 limitations, verification deadlines, network thresholds.

---

## PART 1: Platform payment models (chapter 33)

### 1.1 The payment facilitator in network rules

A platform that takes payments for other businesses sits in a position the card networks define precisely. Visa's rules were read in full for this section.

- Visa's glossary defines a **Payment Facilitator** as "An entity that contracts with an Acquirer to deposit Transactions, receive settlement from, or contract with an Acquirer on behalf of a Sponsored Merchant", and a **Sponsored Merchant** as "An entity that contracts with a Payment Facilitator and, pursuant to that contract, is able to accept a Card to sell goods or services" [VERIFIED: https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf, published 2026-10-24].
- A **Marketplace** is "An entity that brings together Cardholders and retailers on an electronic commerce website or mobile application and processes Transactions and receives Settlement on behalf of those retailers" [VERIFIED: same document, glossary entry last updated October 2019].
- **Who is the merchant** (rule 5.3.2.2): an entity is a Merchant or Sponsored Merchant if it "is selling the goods or services to the Cardholder", "uses its name primarily to identify its Merchant Outlet to the Cardholder" and "provides recourse to the Cardholder in the event of a dispute"; otherwise it is classified as a Digital Wallet Operator, a Marketplace, a Payment Facilitator or a Ramp Provider. Visa "reserves the right to determine" the classification and may look at who "Owns or takes possession of the goods or services", "Books the sale as revenue" and "Provides customer service and handles returns" [VERIFIED: same document].
- **Sub-merchant threshold** (rule 5.3.1.4): "An Acquirer that contracts with a Payment Facilitator must enter into a direct Merchant Agreement with a Sponsored Merchant that exceeds USD 1 million in annual Transaction volume", before processing for a new sponsored merchant, or "within 2 years" after an existing one crosses the threshold. The payment facilitator "may continue to provide payment services (including settlement)" to that merchant. Exceptions exist: a relationship held for at least 2 years with the same acquirer plus regular reporting and acquirer oversight, or a listed set of merchant category codes (utilities, rent, healthcare, education and others) [VERIFIED: same document, rule last updated October 2025]. ⚠
- **Marketplace qualification** (rule 5.3.4.1): the marketplace's name must be displayed "more prominently than the name and brands of retailers"; it "Handles payments for sales and refunds on behalf of the retailers"; it "Is financially liable for Disputes"; and no retailer located outside the marketplace's jurisdiction may exceed both "USD 10 million in annual Visa volume through the Marketplace" and "10% of the Marketplace's annual Visa volume". Franchisees (without franchisor permission), travel agents, high-integrity-risk merchants and crowd-funding are not eligible [VERIFIED: same document, rule last updated April 2023].
- **Registration goes through the acquirer.** "A Member must register a Third Party Agent with Visa"; Visa's explainer states "Acquirers are responsible for the acts of both PFs and sponsored merchants" and that the payment facilitator "Signs a merchant acceptance contract with a sponsored merchant on behalf of an acquirer" and "Receives & distributes settlement of transaction proceeds from an acquirer" [VERIFIED: Visa rules as above; https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-payment-facilitator-model.pdf, © 2024].
- **Mastercard**: trade press reported in November 2014 that Mastercard raised its sub-merchant threshold from $100,000 to "$1 million in annual MasterCard volume", while "Visa, however, for now is sticking with its $100,000 threshold" **(evidence age: 12 years)** [WIDELY REPORTED: https://www.digitaltransactions.net/mastercard-sub-merchants-dont-need-to-own-accounts-until-volume-hits-1-million/, 2014, trade press]. The Visa figure in that article is superseded by the 2026 rule above; the current Mastercard figure was not verified in this session.

**For readers new to payments**

- **Acquirer**: the bank or licensed institution that connects a merchant to the card networks and receives the money for card sales.
- **Payment facilitator (PayFac)**: a company registered with the networks through an acquirer that signs up smaller merchants under its own arrangement and passes their money on.
- **Sponsored merchant (sub-merchant)**: a business that accepts cards through a payment facilitator instead of holding its own agreement with an acquirer.
- **Marketplace (network sense)**: a platform that is itself the visible seller-of-record to the cardholder and is liable for disputes, with its sellers behind it.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- The networks' test for "who is the merchant" is about what the cardholder sees and who gives recourse, not about how the API call is shaped. A platform's data model has to record, per payment, which legal entity was presented as the seller, because that decides the statement descriptor, dispute liability and the applicable rule set.
- Thresholds are per sponsored merchant per year, so a platform acting as a facilitator needs running annual volume per seller and a process for the day one seller crosses USD 1 million. Platforms that use a provider's platform product inherit that monitoring from the provider.

### 1.2 Why platforms use a provider's platform product instead

- Stripe's own guide lists what a registered payment facilitator must do: get acquirer sponsorship, "Obtain Level 1 PCI DSS certification", build merchant dashboards, payout and dispute systems, underwriting and monitoring, "Register as a payfac with each card network in each country", "Apply for money transmitter licenses (MTLs) in each state the payfac operates in, if required to support certain fund flows", and "Re-register as a payfac with card networks annually". Its cost table gives, as approximate minimums: acquirer sponsorship 3–6 months; PCI validation "US$50,000–US$500,000"; merchant management system "US$600,000+"; network registration "Initial fees paid to Visa (US$5,000) and Mastercard (US$5,000)"; money transmitter licences "US$450,000 minimum"; "US and international licences: US$1,000,000+" [VERIFIED: https://stripe.com/guides/payfacs, n.d., accessed 2026-11]. This is vendor marketing: the figures are Stripe's estimates in support of its own product, and the guide cites a 2018 industry report, so parts of it are probably **(evidence age: about 8 years)** [ASSUMPTION/JUDGEMENT].
- The same guide notes that after PSD2 in Europe "Platforms that control the flow of funds need to acquire an e-money license, which can take months and millions of euros to obtain" [VERIFIED: same page].
- Stripe states what it brings instead: its screening includes "Risk-based KYC and AML checks", "Sanctions screening", "MATCH (Member Alert To Control High-risk businesses) list checks" and "Money transmitter licenses (MTL) in the US and e-money (EMI) licenses in the EU" [VERIFIED: https://docs.stripe.com/connect/risk-management, n.d., accessed 2026-11]. For Connect payouts, the licensing is "Covered by Stripe's licensing" and "your platform isn't part of the payout funds flow" [VERIFIED: https://docs.stripe.com/connect/cross-border-payouts-to-recipients/compare-global-payouts, n.d., accessed 2026-11].
- Adyen treats a registered payment facilitator as one kind of platform customer. A platform onboards "as a payment facilitator" when "You are already registered with Visa or Mastercard as a payment facilitator", "You have individuals as your users who want to accept in-person payments", or "You have users with high-risk Merchant Category Codes (MCCs)". In the general platform setup, "your users have a contractual relationship with the payment methods, while you maintain a relationship with your users" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources/platform-structure, n.d., accessed 2026-11].
- "PayFac as a service" is an industry label, not a term either company uses in the pages fetched [ASSUMPTION/JUDGEMENT].

**Stripe vs Adyen**

| Aspect | Stripe (documented) | Adyen (documented) | What the difference suggests |
| --- | --- | --- | --- |
| Is the platform a registered payment facilitator? | Stripe positions Connect as the alternative to becoming one; Stripe holds the licences (2026) | Both paths documented: general platform (users contract for payment methods) and platform that is itself a registered payment facilitator (2026) | Adyen's documentation expects some large platforms to hold their own network registration; Stripe's does not discuss it [ASSUMPTION/JUDGEMENT] |
| Network-rule mechanics exposed to the platform | Merchant-of-record guidance and charge types (section 1.4) | "To comply with payment scheme regulations, you must have a balance platform and merchant account in each region" (section 1.5) | Both hide registration; Adyen's regional structure is visible in the data model [ASSUMPTION/JUDGEMENT] |

### 1.3 Stripe Connect: from account types to responsibilities

**History in dated steps.**

- Connect launched in 2012 for connecting to "regular Stripe accounts"; on 23 March 2015 Stripe added "managed accounts", which "allow you to customize all aspects of the experience for sellers—from what the setup flow looks like and payment schedules to who pays fees and when info is collected" **(evidence age: 11 years)** [VERIFIED: https://stripe.com/blog/the-new-connect, published 2015-03-23].
- On 25 May 2017 Stripe introduced "Express, the easiest way to onboard a new seller or recipient", together with one-to-many and many-to-many payments ("split charges and transfers"), holding funds ("limited to 90 days") and Account Debits **(evidence age: 9 years)** [VERIFIED: https://stripe.com/blog/connect-updates, published 2017-05-25]. The naming Standard / Express / Custom dates from this period; the renaming of "managed" to Custom and "standalone" to Standard was seen only in a search result, not on a fetched page [ASSUMPTION/JUDGEMENT].
- Today the account-types page is headed "Connected account types — Learn about connected account configurations that use legacy account types" and carries a "Deprecated feature" notice: "The information on this page applies only to platforms that already use legacy connected account types (Standard, Express, or Custom accounts)" [VERIFIED: https://docs.stripe.com/connect/accounts, n.d., accessed 2026-11].
- What the three types bundled: Standard = full Stripe Dashboard, Stripe onboarding, direct charges only, liability with the connected account for direct charges; Express = Express Dashboard, Stripe onboarding, platform liable; Custom = no dashboard, "almost completely invisible to the account holder", platform liable and responsible for collecting information. "After you create a connected account, you can't change its type" [VERIFIED: same page].

**Controller properties (Accounts v1).** The bundle was unpacked into four settings on the v1 Account: `controller.losses.payments` (`stripe` or `application`), `controller.fees.payer` (`account` or `application`, plus the legacy values `application_custom` and `application_express`), `controller.requirement_collection` (`stripe` or `application`) and `controller.stripe_dashboard.type` (`full`, `express`, `none`). "Each account type maps to a set of controller properties. We automatically set those properties on your existing connected accounts." "Migrating your integration to use controller properties is optional" [VERIFIED: https://docs.stripe.com/connect/migrate-to-controller-properties, n.d., accessed 2026-11].

**Accounts v2.**

- "There are two versions of Accounts: v2: Highly configurable and extendable support for payments to and by connected accounts, funds transfers, and other functionality; v1: Limited support for connected accounts and payments" [VERIFIED: https://docs.stripe.com/connect/accounts-v2, n.d., accessed 2026-11].
- A v2 Account carries **configurations**: `merchant` ("allows an Account to accept payments from customers", with `card_payments` and `stripe_balance.payouts`), `customer` ("lets your platform charge an Account as a customer. You can use it instead of a Customer object") and `recipient` ("allows an Account to receive funds transfers", with `stripe_balance.stripe_transfers`, "which is required to use indirect charges") [VERIFIED: same page].
- Identity is shared across configurations: "When you add a configuration to an existing Account to enable additional functionality, you don't have to re-collect requirements that they already provided" [VERIFIED: same page].
- **Responsibilities** are set once: "You must define `defaults.responsibilities` properties when you add the Merchant configuration to an account. You can't update their values later." `fees_collector` "Defines how Stripe collects payment fees for direct charges on the connected account. (For destination or separate charges, Stripe always collects fees from your platform.)"; `losses_collector` "Assigns responsibility for negative balances incurred by the connected account". Constraint: "If you set `losses_collector` to `application`, then you must also set `fees_collector` to `application`" [VERIFIED: https://docs.stripe.com/connect/accounts-v2/connected-account-configuration, n.d., accessed 2026-11].
- A third responsibility is derived: `requirements_collector` "is automatically calculated based on the `losses_collector` and `dashboard` values. You can't set it." The platform collects KYC only "when you set `defaults.responsibilities.losses_collector` to `application` and `dashboard` to `none`" [VERIFIED: same page].
- The `dashboard` property takes `express`, `full` or `none` [VERIFIED: same page].
- **Status and limitations as of November 2026** ⚠: the documentation's example request carries the header `Stripe-Version: 2026-10-28.preview`. "You must use Accounts v1" for OAuth-connected accounts, for the recipient service agreement, and "To request or manage the following capabilities: `treasury`, `card_issuing_*`", deprecated capabilities and "certain payment methods in public or private preview". "Stripe discourages indefinitely maintaining both Accounts API versions simultaneously." A v2 Account ID can be passed to v1 endpoints [VERIFIED: https://docs.stripe.com/connect/accounts-v2, n.d., accessed 2026-11]. The destination-charges guide adds: "You can't use the Accounts v2 API to manage payout settings. Use the Accounts v1 API", while the payout-schedule guide says to use the Balance Settings API "to manage payout settings for Accounts v2" [VERIFIED: https://docs.stripe.com/connect/destination-charges; https://docs.stripe.com/connect/manage-payout-schedule, n.d., accessed 2026-11]. The two statements conflict; the documentation appears to be mid-migration [ASSUMPTION/JUDGEMENT]. No page fetched states whether Accounts v2 is formally generally available.
- A Stripe solutions architect at Sessions 2026 described the same shift from account types ("what you have now is traits") and gave the design rule "liability gates your fund flows. So pick it first, not last" [VERIFIED: https://stripe.com/sessions/2026/splitting-the-check-architecting, published 2026 (Stripe Sessions 2026; exact day not shown)].

**For readers new to payments**

- **Connected account**: the record a platform creates at Stripe for each seller or recipient; Stripe defines it as "A person or business accepting payments or receiving payouts on a Connect platform".
- **Negative balance liability**: who pays when a seller's refunds and chargebacks exceed what the seller has in its balance and the seller cannot cover it.
- **Capability**: a named permission on an account (for example accepting card payments) that becomes active only when its verification requirements are met.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- The three legacy types were a product package; controller properties and v2 responsibilities expose the underlying independent decisions (who loses money, who pays fees, who collects KYC, which dashboard). A platform's own account table should store those decisions as separate fields, because they are immutable per account and a platform can end up with several combinations.
- Immutability of responsibilities means a change of commercial model (for example moving from Stripe-priced to platform-priced) is a migration to new accounts, not a setting.
- Embedded finance still pulls a platform back to v1 for some calls, so a v2-only integration is not yet possible for platforms that issue cards or offer accounts.

### 1.4 Stripe charge types and the merchant of record

- "Connect uses three types of charges in two general categories": **direct charges** ("payments made directly to a connected account") and **indirect charges** ("Payments made to your platform"), the latter being **destination charges** and **separate charges and transfers** [VERIFIED: https://docs.stripe.com/connect/charges, n.d., accessed 2026-11].

| | Direct charge | Destination charge | Separate charges and transfers |
| --- | --- | --- | --- |
| Where the charge is created | "on your connected account, so the payment appears in the connected account's balance" | "on your platform, so the payment appears in your platform's balance. A portion of the funds immediately transfers to the connected account's balance" | "on your platform's account first. Create a separate transfer to move funds" |
| Who pays Stripe fees | "You can choose whether to have Stripe debit fees directly from connected accounts or from your platform account" | "Stripe debits fees from your platform's balance" | "Your account balance is debited for the cost of the Stripe fees, refunds, and chargebacks" |
| Refunds and chargebacks | "reduce the connected account's balance" | "reduce your platform's balance" | platform balance |
| Typical use (Stripe's examples) | SaaS platforms; "Shopify", "Thinkific" | "a home rental marketplace or a ridesharing app" | "DoorDash"; one-to-many, many-to-one, charge before the seller is known |

All cells: [VERIFIED: https://docs.stripe.com/connect/charges, n.d., accessed 2026-11].

- **`on_behalf_of`** on an indirect charge makes "the connected account the business of record for the payment". Stripe then "Settles charges in the country of the specified account", "Uses the fee structure for the connected account's country" and "Uses the connected account's statement descriptor". "If `on_behalf_of` is omitted, the platform is the business of record for the payment" [VERIFIED: https://docs.stripe.com/connect/charges; https://docs.stripe.com/connect/destination-charges, n.d., accessed 2026-11]. The destination-charge guide calls this the **settlement merchant**: it "determines whose information is used to make the charge" [VERIFIED: https://docs.stripe.com/connect/destination-charges, n.d., accessed 2026-11].
- **Merchant of record comes first, charge type second.** "The MoR is the entity that the customer understands they're buying from." "Determine the MoR based on the business model... Don't base it on the charge type or payment configuration." Stripe ties this to network rules: "card network compliance rules require a brand's identity to be clear and consistent throughout the transaction", with "card-network scrutiny or enforcement, including fines" for misalignment. Valid combinations: platform as MoR → destination charges or separate charges and transfers **without** `on_behalf_of`; connected account as MoR → direct charges, or the indirect types **with** `on_behalf_of` [VERIFIED: https://docs.stripe.com/connect/merchant-of-record, n.d., accessed 2026-11].
- **Statement descriptors** follow the charge type: with the `transfers` capability alone, "your platform, not the connected account, processes charges. Therefore, a connected account's customers' bank statements display your platform's statement descriptor". Accounts with `card_payments` "must have a statement descriptor that's at least 5 characters in length" [VERIFIED: https://docs.stripe.com/connect/account-capabilities; https://docs.stripe.com/connect/statement-descriptors, n.d., accessed 2026-11].
- Region constraint: destination charges and separate charges and transfers "support cross-region funds flows between platforms and connected accounts only in certain regions. For other regions, the platform and connected account must be in the same region unless using `on_behalf_of`"; with direct charges "Funds always settle in the country of the connected account" [VERIFIED: https://docs.stripe.com/connect/charges, n.d., accessed 2026-11].

### 1.5 Adyen for Platforms and the balance platform

**Classic versus balance platform.** Adyen documents two generations. The "Classic integration" page says: "This page is for classic Adyen for Platforms integrations. If you are just starting your implementation, refer to our new integration guide instead", and describes onboarding "sub-merchants as account holders" [VERIFIED: https://docs.adyen.com/classic-platforms, n.d., accessed 2026-11]. The model chooser asks "Have you integrated Adyen for Platforms before Aug 1, 2022?" and then "Have you upgraded to the balance platform?" [VERIFIED: https://docs.adyen.com/adyen-for-platforms-model, n.d., accessed 2026-11]. The release notes for the balance platform start in October 2021 (Transfers API v2) and January 2022 (Configuration API v2, Balance Platform Customer Area) **(evidence age: 5 years)** [VERIFIED: https://docs.adyen.com/release-notes/platforms-and-financial-products, entries dated 2021-10-28 and 2022-01-24]. No end-of-life date for classic was found.

**Two models on the balance platform.**

| Feature | Marketplace | Platform |
| --- | --- | --- |
| Shopper interaction | "Directly with you" | "Directly with your user" |
| Online payments | yes | yes |
| In-person payments | no | yes |
| Payment facilitators | no | yes |
| Financial products (issuing, business accounts, financing) | yes | yes |

[VERIFIED: https://docs.adyen.com/adyen-for-platforms-model, n.d., accessed 2026-11]. A marketplace is where "Customers recognize that they are doing business directly with your marketplace"; a platform is "a commerce platform, ordering or point-of-sale solution, retail management system, or you are a payment facilitator" [VERIFIED: same page; https://docs.adyen.com/marketplaces/account-structure-resources/marketplace-structure, n.d., accessed 2026-11].

**Resources.**

- Payment side: "a **company account** and one or more **merchant accounts**"; "**Store**: ensures that the transactions you process for your users correspond to an accurate payer statement" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources, n.d., accessed 2026-11].
- "The balance platform is an accounting system that manages the flow of funds within your business. You must have a separate balance platform for each region in which you acquire payments" [VERIFIED: same page]. Acquiring regions for platforms: Australia, Canada, Europe/EEA, Hong Kong, New Zealand, Singapore, United Kingdom, United States [VERIFIED: https://docs.adyen.com/platforms, n.d., accessed 2026-11]. ⚠
- Per user: "**Account holder**: specifies what your user can do in your platform"; "**Balance account**: holds the funds of your user. All financial activities in your platform, such as paying out to a bank account, happen through balance accounts"; "**Payment instrument**: an Adyen-issued card or business account"; "**Grant account**: enables you to track the total amount of offers for business capital your users have accepted" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources, n.d., accessed 2026-11].
- Verification side (Legal Entity Management API): "**Legal entity**: contains information about your user, for example, the legal name, address, and tax information"; "**Transfer instrument**: your user's verified bank account where they can receive payouts"; "**Supporting document**"; "**Business line**: contains information about your user's line of business, including their industry and source of funds". "A business line can be associated with multiple stores, and a store can be associated with multiple business lines." Adyen uses the business line's `service`, `industryCode` and `salesChannels` "to determine which payment methods are eligible for your user's store" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources/legal-entity-management, n.d., accessed 2026-11].
- The platform's own side: "**Liable account holder**: represents your business in the balance platform. **Liable balance account**: the account where your business' funds are held. Funds can be deducted from this account if your users' balance accounts incur negative balances due to refunds and chargebacks. These resources are created by Adyen" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources, n.d., accessed 2026-11].
- Multiplicity in the worked example (a platform in two regions, users in NL, DE and US): one company account; one merchant account and one balance platform per acquiring region; a platform legal entity per region; per user "At least one account holder for each country your user operates in", "For each account holder, at least one balance account with a defined base currency", "For each balance account, a transfer instrument", "A legal entity in each country your user operates in", and stores tied to the region's merchant account [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources/platform-structure, n.d., accessed 2026-11].

**Stripe vs Adyen**

| Aspect | Stripe (documented, 2026) | Adyen (documented, 2026) | What the difference suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Unit that represents a seller | One Account object carrying identity, configurations, capabilities, requirements and (via balance) funds | Several resources: legal entity (who), account holder (what they may do), balance account (their money), transfer instrument (their bank), store and business line (how they sell) | Adyen separates identity from money from permissions in the API; Stripe exposes one object and is now splitting it internally into configurations |
| Who is merchant | Chosen per payment by charge type and `on_behalf_of` | Chosen by model (marketplace versus platform) and by store setup | On Stripe the same account can be used both ways; on Adyen it is closer to an account-structure decision |
| Regional structure | Platform and connected accounts each have a country; cross-region flows limited to named regions | "a separate balance platform for each region in which you acquire payments" | Adyen's regional licences and acquiring entities are visible as separate ledgers; Stripe's are mostly hidden behind account country |
| Platform's own money | Platform Stripe balance, plus `connect_reserved` | Liable balance account | Same role, different name; see 1.6 |
| Legacy generation | Standard / Express / Custom, v1 with controller properties | Classic integration (pre-August 2022) | Both companies rebuilt the platform model once and still run the old one |

### 1.6 Loss liability and negative balances

**Stripe.**

- "Your platform is always responsible for its own negative balances. However, responsibility for your connected accounts' negative balances can belong to your platform or to Stripe" [VERIFIED: https://docs.stripe.com/connect/risk-management, n.d., accessed 2026-11].
- "Direct charges occur on a connected account, so negative transactions for direct charges affect the connected account's balance... Indirect charges occur on the platform, so negative transactions for indirect charges affect the platform's balance." Hence: "If you use indirect charges, assign negative balance responsibility to your platform, not to Stripe. Assigning responsibility to Stripe doesn't absolve your platform of responsibility for its own balance" [VERIFIED: same page].
- Recovery order: "if a connected account's balance becomes negative, Stripe first attempts to offset the negative amount by collecting funds from the account's external account". If the platform is responsible, Stripe "holds funds in your platform account in reserve"; "if a connected account's balance remains negative for 180 days, we transfer funds from the platform reserve to cover the negative amount" [VERIFIED: same page]. The reserve is the platform's `connect_reserved` balance; movements appear as balance transactions of type `reserve_transaction`, and the 180-day sweep as `connect_collection_transfer` [VERIFIED: https://docs.stripe.com/connect/account-balances, n.d., accessed 2026-11].
- Automatic bank debits for negative balances need `debit_negative_balances` set to `true` and are supported for banks in Australia, Canada, SEPA countries including the UK, New Zealand and the United States; "Stripe can't correct a negative Stripe account balance using a debit card" [VERIFIED: same page].
- What follows from the choice: when Stripe is responsible, the platform "can't pause payments or payouts", "can't directly debit connected account balances", and "can't use Stripe Treasury or Issuing"; when the platform is responsible it "can't use Managed Risk" and "Stripe might hold reserves on your platform account" [VERIFIED: https://docs.stripe.com/connect/risk-management, n.d., accessed 2026-11].
- **Managed Risk**: "Stripe assumes liability for unrecoverable negative balances on connected accounts", with onboarding screening, ongoing monitoring and direct contact with accounts; it applies to accounts where losses responsibility is `stripe`. For destination charges it is "(Private preview)" ⚠ [VERIFIED: https://docs.stripe.com/connect/risk-management/managed-risk; https://docs.stripe.com/connect/charges, n.d., accessed 2026-11].
- Stripe's own example of the risk: "During the COVID pandemic, some hotels and short-term accommodation providers represented by connected accounts went out of business. As a result, customers who had pre-paid for future stays submitted chargebacks, which were covered by the platforms that processed those payments" [VERIFIED: https://docs.stripe.com/connect/risk-management, n.d., accessed 2026-11].

**Adyen.**

- By default the platform carries everything: "By default, all transaction amounts and fees are booked to your platform's liable balance account" unless split instructions or a split configuration profile say otherwise [VERIFIED: https://docs.adyen.com/platforms/automatic-split-configuration, n.d., accessed 2026-11].
- Chargebacks by default: "Adyen withdraws the disputed funds from your platform's liable balance account"; the platform "can change this behavior by booking the disputed amount to any of the balance accounts in your platform, or even splitting it" [VERIFIED: https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks, n.d., accessed 2026-11].
- User balance accounts can go negative, and the liable account stands behind them (quoted in 1.5). Tools to recover: top-ups "To cover negative balances resulting from refunds or chargebacks" by direct debit from the user's verified bank account, and internal transfers between balance accounts [VERIFIED: https://docs.adyen.com/platforms/top-up-balance-account; https://docs.adyen.com/platforms/internal-fund-transfers, n.d., accessed 2026-11]. The consent wording Adyen supplies for users includes "I agree that {name of your platform} can deduct funds from my bank account to cover negative balances on my balance account" [VERIFIED: https://docs.adyen.com/platforms/onboard-users/terms-of-service, n.d., accessed 2026-11].
- **Nothing public found** on an Adyen option equivalent to Stripe's `losses_collector: stripe` (the provider taking seller loss liability), on a waiting period before the liable account is debited, or on a reserve mechanism. Searched: the platforms and marketplaces documentation trees and the release notes [ASSUMPTION/JUDGEMENT on the absence].

**For readers new to payments**

- **Chargeback**: a forced reversal of a card payment by the cardholder's bank, which takes the money back from the merchant side and adds a fee.
- **Reserve**: money a provider holds back from a balance to cover expected reversals.
- **Liable (balance) account**: the platform's own account at the provider, which is debited when a seller's account cannot cover what it owes.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- On Stripe, liability is a per-account attribute fixed at creation and it constrains the charge type; on Adyen, as documented, liability is the platform's by default and is redistributed transaction by transaction through splits and chargeback logic. A platform on both providers needs one internal concept ("who bears this loss") with two very different implementations.
- Either way the platform should keep its own per-seller exposure figure (paid-out volume still inside the dispute window), because neither provider's balance tells it how much could still come back.

### 1.7 Pricing and platform revenue

- Stripe documents two commercial models for SaaS platforms. **Stripe-owned pricing**: connected accounts "Pay Stripe fees", "Assume liability for their negative balances" and "Process payments as direct charges"; "Stripe doesn't charge your platform in this model", and the platform earns from subscriptions, application fees and "revenue share from Stripe when your connected accounts meet product activation targets". **Buy rate**: "Your platform purchases and white labels payment processing"; connected accounts "Don't pay Stripe fees" and "Are liable to the platform, not Stripe, for their negative balances" [VERIFIED: https://docs.stripe.com/connect/saas, n.d., accessed 2026-11].
- Marketplaces: "As a marketplace, you're responsible for paying Stripe fees, which include payment fees... and Connect fees (such as per-account fees and payout fees)" [VERIFIED: https://docs.stripe.com/connect/marketplace, n.d., accessed 2026-11].
- List prices as served to the Netherlands ⚠: "Stripe handles pricing for your users" — "No fees for your platform"; "You handle pricing for your users" — "€2 per monthly active account" and "0.25% + €0.10 per payout", with funds routing at "0.25% of payout volume" [VERIFIED: https://stripe.com/en-nl/connect/pricing, n.d., accessed 2026-11].
- The **platform pricing tool** lets a platform "set pricing logic for the application fees you charge your connected accounts" without code, with pricing groups per connected account; it applies only when "Stripe charges fees on the payment to your platform rather than the connected account" and "The payment doesn't specify an application fee or transfer amount" [VERIFIED: https://docs.stripe.com/connect/platform-pricing-tools, n.d., accessed 2026-11].
- Application-fee arithmetic depends on the fee collector: "if the Stripe processing fee is 1.00 and your fee is an additional 1.50... If Stripe collects the fees, set the application fee to 1.50... If your platform collects the fees, set the application fee to 2.50 so it covers both fees" [VERIFIED: https://docs.stripe.com/connect/accounts-v2/connected-account-configuration, n.d., accessed 2026-11].
- Adyen: platform revenue is a **Commission** split (section 3.2); Adyen's own fees can be passed to users or kept by the platform through fee split types. **No public price list for Adyen for Platforms was found**; the get-started page routes to sales ("Contact us to register your interest") [VERIFIED: https://docs.adyen.com/platforms/get-started, n.d., accessed 2026-11].

### 1.8 Vocabulary crosswalk (the researcher's mapping)

Everything in this table is **[ASSUMPTION/JUDGEMENT]**: neither company publishes a mapping to the other. Each row pairs terms verified separately in the sections cited; the pairing is approximate and several rows are one-to-many.

| Question | Stripe term | Adyen term | Caveat |
| --- | --- | --- | --- |
| The platform's own account | Platform account | Company account + merchant account(s) + liable account holder | Adyen splits payment processing from funds |
| The platform's own money | Platform balance (`available`, `pending`, `connect_reserved`) | Liable balance account | No documented Adyen reserve bucket |
| A seller | Connected account (v2 Account with `merchant` or `recipient` configuration) | Legal entity + account holder + balance account | One Stripe object versus three or more Adyen resources |
| Who the seller is (KYC data) | `identity` on the Account, persons | Legal entity, associated entities, business line | |
| What the seller may do | Capabilities (`card_payments`, `stripe_transfers`, `stripe_balance.payouts`) | Capabilities (`receivePayments`, `receiveFromPlatformPayments`, `sendToTransferInstrument`, …) | Adyen adds a platform-controlled `enabled` flag |
| What is still missing | `requirements` (currently due, eventually due, past due) | Verification status, `problems`, `verificationDeadlines` | |
| The seller's bank account | External account | Transfer instrument | |
| The seller's money at the provider | Connected account balance | Balance account | An Adyen account holder can have several |
| How a payment is attributed | Charge type and `on_behalf_of` | Store, merchant account and `splits` | |
| The platform's cut | Application fee | `Commission` split | |
| Moving money platform ↔ seller | Transfer, transfer reversal, account debit | Internal funds transfer (Transfers API) | |
| Paying the seller out | Payout, payout schedule | Payout (external transfer), managed payout schedule, sweep | |
| Adding outside money | Top-up (platform only) | Top-up (user or liable account) | Different scope |
| Who bears seller losses | `losses_collector` / `controller.losses.payments` | Liable balance account plus chargeback and refund logic | No per-account switch documented at Adyen |
| Provider-hosted onboarding | Account Link to Stripe-hosted onboarding | Hosted onboarding link | |
| Embeddable UI | Connect embedded components (AccountSession) | Components (Onboarding, Transactions, Payouts, Reports, Disputes, Capital) | |
| Stored-value account for the seller | Financial account | Business account (a payment instrument) | |
| Card for the seller | Issuing card | Payment instrument (card) | |
| Financing | Capital financing offer | Capital grant offer, grant account | |

---

## PART 2: Onboarding and verification (chapters 34 and 26)

### 2.1 Capabilities and requirements as state

**Stripe.**

- "Capabilities represent functionality that you can request for your connected accounts... A capability must be active for a connected account to perform actions associated with that capability." "The capabilities you request for a connected account determine the information you're required to collect for it. To reduce onboarding effort, only request the capabilities that your accounts need" [VERIFIED: https://docs.stripe.com/connect/account-capabilities, n.d., accessed 2026-11].
- v1 `requirements` hash: `currently_due` ("requirements that you must resolve by the `current_deadline` for the account to remain active"), `eventually_due` (may be needed "depending on whether the corresponding thresholds are reached"), `past_due` ("requirements that have disabled capabilities because they weren't resolved before the `current_deadline`"), `pending_verification`, `errors`, `disabled_reason` [VERIFIED: https://docs.stripe.com/connect/handling-api-verification (Accounts v1 variant), n.d., accessed 2026-11].
- What happens at the deadline: "Stripe typically disables payouts on the account if we don't receive the information by the `current_deadline`. However, other consequences might apply in some situations. For example, if payouts are already disabled and the account is unresponsive to our inquiries, Stripe might also disable the ability to process charges" [VERIFIED: same page].
- Coupling: "If a connected account has both `card_payments` and `transfers`, and the `status` of either one is `inactive`, then both capabilities are disabled" [VERIFIED: https://docs.stripe.com/connect/account-capabilities, n.d., accessed 2026-11].
- v2 reshapes the same information into requirement entries with `minimum_deadline.status`, a `summary.minimum_deadline` ("The strictest status that applies to at least one open requirement. `past_due` is the strictest, followed by `currently_due`, then `eventually_due`"), `awaiting_action_from` and per-entry `errors`; entries can carry a `requested_reasons.code` of `future_requirements` [VERIFIED: https://docs.stripe.com/connect/handling-api-verification (Accounts v2 variant), n.d., accessed 2026-11].
- Risk reviews add requirements the API cannot satisfy: "Stripe risk reviews of a connected account can add extra requirements, which you can't provide using the API" [VERIFIED: same page].

**Adyen.**

- "Based on the results of the verification checks, Adyen decides if a user can perform any action on your platform. These actions are known as capabilities" [VERIFIED: https://docs.adyen.com/platforms/verification-overview, n.d., accessed 2026-11].
- Each capability has three settings: `requested`; `allowed` ("the verification is successful and the user is permitted to use the capability"); `enabled` ("allows you to manage your users' access to capabilities... Changing this setting does not trigger verification checks"). "The capability can only be used when it is both allowed and enabled" [VERIFIED: https://docs.adyen.com/platforms/verification-overview/capabilities, n.d., accessed 2026-11].
- Core capabilities: `receivePayments`, `receiveFromPlatformPayments` ("receive funds from split payments"), `receiveFromBalanceAccount`, `sendToBalanceAccount`, `sendToTransferInstrument` (payouts), `receiveFromTransferInstrument` (top-ups) [VERIFIED: same page].
- **Three triggers for verification**: requesting capabilities; "When users change their data"; and "Periodic data reviews required by Adyen", which the platform can also request proactively (not "more than one year prior to the user's next scheduled review") [VERIFIED: https://docs.adyen.com/platforms/verification-overview; https://docs.adyen.com/platforms/verification-overview/data-review-process, n.d., accessed 2026-11].
- **Deadlines**: "Adyen may set a deadline to give users extra time to resolve any verification issues before certain capabilities are disallowed... Users are allowed to continue using the capabilities while the deadline is active." Standard periods: **30 days** for `sendToBalanceAccount`, `sendToTransferInstrument`, `receiveFromTransferInstrument`, `issueBankAccount`, `sendToThirdParty`, `getGrantOffers`, `receiveGrants`; **60 days** for `receiveFromBalanceAccount`, `receiveFromPlatformPayments`, `receivePayments`, `issueCard`, `useCard`. "Verification deadlines are only available in v3 and v4 of the Legal Entity Management API" ⚠ [VERIFIED: https://docs.adyen.com/platforms/verification-overview, n.d., accessed 2026-11].
- A gap worth knowing: `balancePlatform.accountHolder.updated` webhooks "are only triggered for capability-related changes to the account holder. Data changes to the legal entity of the account holder do not trigger webhooks" [VERIFIED: same page].
- **Upfront versus staggered**: "As a platform, you should collect verification data from your users upfront because the capability to receive payments is automatically requested for them." "Only payment facilitators can use staggered verification", where "When a user processes a higher amount of funds than the limit of their current tier, they are moved to a higher tier" and "their payouts are temporarily disallowed until they complete additional verification checks". "There are four tiers" [VERIFIED: https://docs.adyen.com/platforms/verification-overview/verification-types, n.d., accessed 2026-11]. The tier amounts were not captured.

### 2.2 Hosted, embedded and API onboarding

**Stripe** offers three: Stripe-hosted, embedded and API. Hosted and embedded get "Immediate" automatic updates for new compliance requirements and support new countries "without integration changes"; API onboarding "Requires integration changes", and "You must plan on reviewing and updating onboarding requirements at least every 6 months" [VERIFIED: https://docs.stripe.com/connect/onboarding, n.d., accessed 2026-11].

- Hosted onboarding is reached through an **Account Link**: "You can only use each temporary Account Link URL once, because it grants access to the account holder's personal information... Don't email, text, or otherwise send account link URLs outside of your platform application" [VERIFIED: https://docs.stripe.com/connect/hosted-onboarding (Accounts v2 variant), n.d., accessed 2026-11].
- **Networked onboarding** "allows owners of multiple Stripe accounts to share certain types of business information between them"; supported in hosted and embedded, not API [VERIFIED: https://docs.stripe.com/connect/onboarding, n.d., accessed 2026-11].
- **Embedded components** work through an AccountSession: "Stripe uses an AccountSession to express your intent to delegate API access to your connected account"; it returns a client secret "that allows an embedded component to access a connected account's resources as if you were making the API calls for them" [VERIFIED: https://docs.stripe.com/connect/get-started-connect-embedded-components, n.d., accessed 2026-11]. The web catalogue lists 24 components, among them account onboarding, account management, notifications banner, payments, disputes, payouts, balances, instant payouts promotion, tax settings, Terminal hardware, financial account, Issuing cards, documents and reports; some are marked preview ⚠ [VERIFIED: https://docs.stripe.com/connect/supported-embedded-components, n.d., accessed 2026-11].
- Who collects KYC is derived, not chosen (section 1.3); Stripe warns: "Configure platform responsibility for requirements collection only if you're prepared to manage the operational complexity" [VERIFIED: https://docs.stripe.com/connect/accounts-v2/connected-account-configuration, n.d., accessed 2026-11].

**Adyen** offers hosted onboarding and API-only onboarding, plus components.

- "Hosted onboarding is our recommended solution." Two variants: **onboarding on invite** ("All actions are performed in your Customer Area"; "Adyen automatically creates all required resources": account holder, balance account, business line, legal entities, payment methods, stores) and **API-initiated** (the platform creates resources and a hosted onboarding link by API) [VERIFIED: https://docs.adyen.com/platforms/onboard-users, n.d., accessed 2026-11].
- Legal entity types: organization, individual, sole proprietorship, and trusts "(Only in Australia and New Zealand)"; the requirements tool also lists unincorporated partnership [VERIFIED: https://docs.adyen.com/platforms/onboard-users; https://docs.adyen.com/platforms/onboard-users/onboarding-steps, n.d., accessed 2026-11].
- "The payment methods and stores are created after the `receivePayments` capability is allowed" [VERIFIED: https://docs.adyen.com/platforms/onboard-users, n.d., accessed 2026-11].
- Onboarding components are "only compatible with the legal entities created with v3 or v4 of the Legal Entity Management API"; Adyen recommends them inside an API-only flow and notes they "only cover certain functionality" [VERIFIED: https://docs.adyen.com/platforms/onboard-users/components, n.d., accessed 2026-11].
- Recent changes show the hosted flow still evolving: on 4 May 2026, onboarding on invite gained the option to "automatically send the hosted onboarding link by email" [VERIFIED: https://docs.adyen.com/release-notes/platforms-and-financial-products, entry dated 2026-05-04]. Note the contrast with Stripe's instruction not to email onboarding links.

**Stripe vs Adyen**

| Aspect | Stripe (documented, 2026) | Adyen (documented, 2026) | What the difference suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Requirement model | Lists of field-level requirements with one deadline; v2 adds per-entry deadline status | Per-capability `allowed` flag, verification errors with remediating actions, per-capability deadlines | Stripe models "what is missing"; Adyen models "what you may do and until when" |
| Deadline lengths | Not published as standard periods; per-account `current_deadline` | Standard 30 or 60 days by capability | Adyen's are predictable enough to build reminders on; Stripe's must be read per account |
| What stops first | "typically disables payouts", charges later | The specific capability is disallowed | Similar practice |
| Volume thresholds | `eventually_due` tied to thresholds | Tiers only for payment facilitators (staggered); platforms verify upfront | Stripe lets small sellers start with less; Adyen's general platforms front-load |
| Platform-side kill switch | Pause payments or payouts only when the platform bears losses | `enabled` flag on any capability | Adyen gives the platform a control independent of liability |
| Periodic re-verification | "maintain compliance with any requirement updates"; `future_requirements` | Named "periodic data reviews" with a schedule the platform can pull forward | Adyen documents re-verification as a recurring event; Stripe as requirement updates |
| Onboarding delivery | Hosted, embedded, API | Hosted (invite or API-initiated), API-only, components | Equivalent menus |

**For readers new to payments**

- **KYC / KYB**: "know your customer" and "know your business" checks a regulated payment company must run on whoever it pays, including who ultimately owns the business.
- **UBO (ultimate beneficial owner)**: a person who ultimately owns or controls a business, whom the provider must identify.
- **Hosted onboarding**: a sign-up flow on the provider's pages, so the provider and not the platform collects the sensitive documents.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Verification is continuous state, not a sign-up step: both providers re-open requirements after data changes, rule changes and periodic reviews. The platform needs a per-seller state machine fed by webhooks, and Adyen's missing webhook for legal-entity data changes means polling or re-reading after every update.
- The seller's question "why are my payouts paused" is answerable only if the platform stores the requirement or verification error that caused it and surfaces the provider's remediation link or component.
- Onboarding conversion is the platform's metric, not the provider's: neither company's documentation publishes conversion figures for its hosted flows (none found).

---

## PART 3: Splits, balances and platform payouts (chapters 35 and 14, journey 44)

### 3.1 Stripe: fees, transfers and balances

- **Application fee on a destination charge**: "the full charge amount is immediately transferred from the platform to the `transfer_data[destination]` account after the charge is captured. The `application_fee_amount`... is then transferred back to the platform." Worked example: on a 10.00 USD charge with a 1.23 USD application fee and 0.59 USD Stripe fees, "The application fee amount minus the Stripe fees (1.23 USD - 0.59 USD = 0.64 USD) remains in your platform account's balance" [VERIFIED: https://docs.stripe.com/connect/destination-charges, n.d., accessed 2026-11]. The alternative is `transfer_data[amount]`, which sends only part of the charge [VERIFIED: same page].
- **Separate charges and transfers**: the charge and its transfers are linked by a `transfer_group` string, which "only identifies associated objects. It doesn't affect any standard functionality". "Transfer and charge amounts don't have to match. You can split a single charge between multiple transfers or include multiple charges in a single transfer" [VERIFIED: https://docs.stripe.com/connect/separate-charges-and-transfers, n.d., accessed 2026-11].
- **`source_transaction`** ties a transfer to a charge so that "the transfer request returns success regardless of your available balance if the related charge hasn't settled yet", and the transferred funds become available when the charge's do. "When a payment used as a `source_transaction` fails, funds from your platform's account balance are transferred to the connected account to cover the payment"; for asynchronous methods such as ACH, "avoid using `source_transaction`" [VERIFIED: same page].
- No automatic retry: "When you transfer funds between your platform's balance and a connected account's balance, Stripe doesn't automatically retry failures" [VERIFIED: https://docs.stripe.com/connect/account-balances, n.d., accessed 2026-11].
- **Balances**: every account has `pending` and `available`; funds become available "on a 2-day rolling basis. (This timing can vary by country and account.)" [VERIFIED: same page]. ⚠
- **Funds segregation** (private preview ⚠) lets a platform "allocate funds from separate charges and transfers to a holding state on your platform account"; allocated funds "don't appear in your platform balance, and you can only transfer them to a connected account", protecting them from platform payouts, unrelated refunds and Stripe fees [VERIFIED: https://docs.stripe.com/connect/funds-segregation, n.d., accessed 2026-11].
- **Account debits** let a platform that bears losses pull money from a connected account's balance (maximum 100,000 USD per debit; "requires getting legally binding consent"; same region or listed corridors) [VERIFIED: https://docs.stripe.com/connect/account-debits, n.d., accessed 2026-11].

**Refunds.**

| Charge type | Who is debited | If the balance is short |
| --- | --- | --- |
| Direct | "Stripe debits the refund amount from the connected account's balance" | Refund is `pending`; fails with `insufficient_funds` after 45 days |
| Destination | "Stripe debits your platform balance... You can reverse the transfers made to your connected accounts to recover your refund cost" | Same 45-day rule on the platform balance; a refund that also requests a transfer reversal errors if the connected account is short |
| Separate charges and transfers | Platform balance; reverse transfers separately | Same 45-day rule |

[VERIFIED: https://docs.stripe.com/connect/charges, n.d., accessed 2026-11]. On a destination charge, "by default the destination account keeps the funds that were transferred to it, leaving the platform account to cover the negative balance from the refund"; `reverse_transfer=true` pulls the funds back, and `refund_application_fee=true` returns the platform's fee [VERIFIED: https://docs.stripe.com/connect/destination-charges, n.d., accessed 2026-11].

**Disputes.**

| | Direct charges | Indirect charges |
| --- | --- | --- |
| Who responds | Connected account (via `Stripe-Account` header) | Platform |
| Balance debited for the amount | "Connected account's balance" | "Platform's balance, with or without `on_behalf_of`" |
| Dispute fee | Depends on fee configuration | Platform |

[VERIFIED: https://docs.stripe.com/connect/disputes, n.d., accessed 2026-11]. For indirect charges the platform recovers by transfer reversal, and Stripe advises timing: "If you challenge the dispute, wait for the dispute outcome before reversing the transfer". "Regardless of a dispute's outcome, Stripe doesn't automatically refund the application fee" [VERIFIED: same page]. Dispute-fee payer by configuration: `fees_collector` = `application` → platform; `stripe`, `application_custom`, `application_express` → connected account [VERIFIED: https://docs.stripe.com/connect/direct-charges-fee-payer-behavior, n.d., accessed 2026-11].

### 3.2 Adyen: split instructions

- Splits are instructions about booking: "you must define instructions about how to split the funds between your user's balance accounts and your platform's liable balance account" [VERIFIED: https://docs.adyen.com/platforms/online-payments/split-transactions, n.d., accessed 2026-11].
- **When**: at authorization (`/payments`, `/sessions`), on an amount update, at capture, and on refunds. "Splitting payments at capture is only possible for payment methods that support separate captures" [VERIFIED: same page].
- **Split types** (the `type` of each item in the `splits` array): `BalanceAccount` ("Books a part of the transaction to your user's balance account"), `Commission` ("Books your platform's commission to your liable balance account"), `Interchange`, `SchemeFee`, `AcquiringFees` (interchange plus scheme fees), `AdyenCommission` (Adyen's fee under blended rates), `AdyenMarkup` (Adyen's fee under Interchange++), `AdyenFees` (commission plus markup), `PaymentFee` ("the aggregated amount of all the transaction fees"), `VAT`, `Remainder` ("the amount left over after currency conversion"), `Surcharge`, `TopUp`. "If you do not specify an `account` in your split instructions, the split amount is booked to your liable balance account" [VERIFIED: same page].
- **Fees are not known at payment time**: "Transaction fees refer to the costs you incur on a transaction in your platform that are not known at the time of payment. They are calculated by Adyen after we receive the payment request. By default, these costs are deducted from your liable balance account." If no fee split is given, "Adyen automatically updates the request to include the PaymentFee split type, deducting all transaction fees from your platform's liable balance account." More granular fee types override aggregated ones [VERIFIED: https://docs.adyen.com/platforms/online-payments/transaction-fees, n.d., accessed 2026-11].
- Fees that cannot be passed per payment: "Processing costs: These fees are aggregated and also applicable to refused and cancelled payments", and tiered-pricing discounts [VERIFIED: same page].
- **Split configuration profiles** apply the logic automatically per store: a profile holds rules with conditions (currency, payment method, card region, funding source, shopper interaction, card usage type) and split logic (commission as "a fixed amount (specified in minor units), a percentage (specified in basis points), or both", transaction fees, refund, refund cost allocation, chargeback, chargeback cost allocation, remainder, surcharge, tip). "We recommend that you always include a catch-all rule... Without one, any transaction that doesn't match a specific rule will be booked to your liable balance account by default." Request-level instructions override the profile [VERIFIED: https://docs.adyen.com/platforms/automatic-split-configuration, n.d., accessed 2026-11].
- **Precedence** (documented as "in pilot phase and is not available for all platforms" ⚠): at authorization, request then profile; at capture, capture request, then authorization request, then profile; for refunds, request, profile, balance-platform default, and finally "If the refund covers the full amount of one full capture... we use the capture's split ratio. In all other cases, such as for refunds of partial captures, we book the full refund amount to your platform's liable balance account" [VERIFIED: https://docs.adyen.com/platforms/how-adyen-applies-split-instructions, n.d., accessed 2026-11].
- **Refund limits**: "Refunds can only be deducted from the balance accounts to which the payment was credited"; the outcome arrives asynchronously in a REFUND webhook [VERIFIED: https://docs.adyen.com/platforms/online-payments/split-transactions/split-refunds, n.d., accessed 2026-11].
- **Chargeback logic** is chosen before the chargeback exists, in a `platformChargebackLogic` object on the payment or capture: book to the liable account, to one user balance account, or by the payment's split ratio; a balance-platform default can be set through support. Chargeback, chargeback reversal and second chargeback each debit or credit accordingly [VERIFIED: https://docs.adyen.com/platforms/online-payments/split-transactions/split-chargebacks, n.d., accessed 2026-11].
- **A silent fallback**: "The API request validates only the format of the split instructions, **not** the balance accounts specified in the request... If the balance account does not exist, or it is linked to an account holder with a **closed** status, the full transaction and its fees are booked to your platform's liable balance account" [VERIFIED: same page; same wording on the split-refunds page].
- **Multi pay-in** is "currently in pilot phase" ⚠: it "consolidates all funds processed for your users within Adyen's infrastructure, making it possible for you to combine payments processed by Adyen with third-party acquired volume". Funds from a pay-in partner land in a "multi pay-in account" which "is legally held by Adyen solely for your user's benefit"; "To comply with financial regulations, you must allocate the funds you receive in your multi pay-in account to the balance accounts in your balance platform within 24 hours". It "does not support separate authorization and capture" [VERIFIED: https://docs.adyen.com/platforms/multi-pay-in, n.d., accessed 2026-11].

### 3.3 Payouts to sellers

**Stripe.**

- Schedule: `interval` is `manual`, `daily`, `weekly` or `monthly`; `delay_days` "reflects how long it takes for `on_behalf_of` charges (or direct charges performed on the connected account) to become available for payout" and can be overridden "to a number up to 31" on accounts where the platform owns liability; minimum balances can be set per currency [VERIFIED: https://docs.stripe.com/connect/manage-payout-schedule, n.d., accessed 2026-11].
- **Instant Payouts**: "available at any day or time, including weekends and holidays, and funds typically settle in the associated debit card or bank account within 30 minutes". Platform and connected account must be in supported countries (AE, AU, CA, DK, EU, GB, HK, MY, NO, NZ, SE, SG, US); eligible external accounts vary (debit card or supporting bank accounts in the US, GB, euro area, SE, DK, SG, AU; debit card only in CA, CZ, HU, NO, PL, RO, NZ, MY, AE). The platform can charge for them by application fee; the account must be on `manual` payouts ⚠ [VERIFIED: https://docs.stripe.com/connect/instant-payouts; https://docs.stripe.com/connect/manage-payout-schedule, n.d., accessed 2026-11].
- **Cross-border payouts**: "Platforms based in the US, UK, EEA, Canada, or Switzerland can transfer funds to connected accounts in any of those regions"; supported only for separate charges and transfers and destination charges without `on_behalf_of`, and top-ups and transfers; not for accounts under the recipient service agreement. "Stripe doesn't support self-serve cross-border payouts to countries outside the listed regions" [VERIFIED: https://docs.stripe.com/connect/cross-border-payouts, n.d., accessed 2026-11]. ⚠
- **Recipient service agreement**: "acknowledges that Stripe has no direct service relationship with the recipient"; such accounts "can't process payments or request the `card_payments` capability" and transfers to them "take an additional 24 hours to become available" [VERIFIED: https://docs.stripe.com/connect/service-agreement-types, n.d., accessed 2026-11].
- **Global Payouts** is the separate product for paying parties who are not connected accounts: "Send payouts to more than 160 markets", from a financial account, "best for businesses that already hold the licenses required to move money themselves". Stripe's comparison: with Global Payouts "If you manage your customers' funds, you might need a license such as an MTL" and "Payouts don't flow through a Stripe balance belonging to the recipient, so you're responsible for any desired tracking of recipient funds"; with Connect, licensing is "Covered by Stripe's licensing" [VERIFIED: https://docs.stripe.com/global-payouts; https://docs.stripe.com/connect/cross-border-payouts-to-recipients/compare-global-payouts, n.d., accessed 2026-11].
- **Top-ups** add bank money to the platform balance (bonuses, discounts funded by the platform, paying a seller before funds arrive). Availability ⚠: "General availability: USA, UK, Japan"; "Private preview: EU, Canada, Australia, New Zealand". Requirement: platform and connected account "in the same market" or the account has a recipient agreement. "adding funds doesn't automatically retry the failed action" [VERIFIED: https://docs.stripe.com/connect/top-ups, n.d., accessed 2026-11].

**Adyen.**

- **Sales day settlement**: "the funds are settled independently of the timelines of schemes and payment methods involved"; a sales day is by default midnight to midnight in the balance account's time zone; a batch settles "after its sales day ends and the configured settlement delay has passed. The date when the schemes or payment methods transfer the funds to Adyen does not affect this timing". Settlement is net of transaction costs, refunds and chargebacks. "The pass-through settlement model is deprecated and not available for new integrations" except for two payment methods [VERIFIED: https://docs.adyen.com/platforms/settle-funds, n.d., accessed 2026-11].
- **Managed payouts** (announced 20 May 2026): schedules configured with an Adyen contact; **Standard** ("funds arrive in your user's bank account two business days after capture") or **Accelerated** (one business day); frequency weekdays, weekly or monthly; minimum, maximum and retained amounts. Limits: "one managed payout schedule per currency on each balance account" and "only... local payouts (within the same country and currency)" ⚠ [VERIFIED: https://docs.adyen.com/platforms/managed-payouts, n.d., accessed 2026-11; date from https://docs.adyen.com/release-notes/platforms-and-financial-products, entry dated 2026-05-20].
- **Custom payouts**: a custom settlement delay, custom schedules, and on-demand payouts; "Scheduled custom and on-demand payouts are bank transfer requests that move funds from your user's balance account to their bank account" [VERIFIED: https://docs.adyen.com/platforms/custom-payouts, n.d., accessed 2026-11]. A custom schedule is a **sweep** created on the balance account (`POST /balanceAccounts/{id}/sweeps`) with `triggerAmount`, `targetAmount` (minimum balance to keep) or `sweepAmount` (fixed amount) [VERIFIED: https://docs.adyen.com/platforms/custom-payouts/scheduled-payouts, n.d., accessed 2026-11].
- **Priorities**: a payout can list priorities (examples shown: regular, instant, wire); "When you specify multiple priorities, Adyen first attempts the transfer using the first option in the list. If that route is unavailable, Adyen automatically retries the transfer using the next available priority". "While most banks can process **regular** transfers, some do not support **instant** transfers." Adyen "reviews the payout and performs internal checks" before approval [VERIFIED: https://docs.adyen.com/platforms/custom-payouts/on-demand-payouts, n.d., accessed 2026-11].
- **Internal transfers** move funds "between your liable balance account and the balance account of one of your users, two balance accounts of the same user, or the balance accounts of two different users", on a schedule or on demand [VERIFIED: https://docs.adyen.com/platforms/internal-fund-transfers, n.d., accessed 2026-11].
- **Top-ups**: scheduled (a "pull sweep" that triggers "a direct debit from a verified transfer instrument") or on demand ("a one-off payment funded by your user", booked with the `TopUp` split type); "If needed, you can also top up your liable balance account" [VERIFIED: https://docs.adyen.com/platforms/top-up-balance-account and its two sub-pages, n.d., accessed 2026-11].

**Stripe vs Adyen**

| Aspect | Stripe (documented, 2026) | Adyen (documented, 2026) | What the difference suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| How one payment is divided | By charge type: an application fee carved out, or transfers created afterwards | By a `splits` array of typed bookings at authorization or capture, or by a store's profile | Stripe's split is a set of money movements between balances; Adyen's is a set of ledger bookings declared with the payment |
| Who pays the processing fee | Follows `fees_collector` and charge type; fixed per account | Any balance account, per fee type, per payment | Adyen exposes interchange and scheme fee as separately bookable; Stripe exposes them only under IC+ pricing |
| Fee amount known when | Stripe fee is reported on the balance transaction | "not known at the time of payment" | Adyen's Interchange++ model means the split is by type, not amount |
| Refund after payout | Platform balance debited; transfer reversal to recover | Refund split; only from accounts that were credited; fallback to liable account | Both put the platform in the middle by default |
| Dispute placement | Follows charge type; reversal is a separate call after the fact | Declared up front in `platformChargebackLogic` | Adyen makes the decision at payment time, Stripe at dispute time |
| Wrong-account behaviour | Transfer fails with an error | Booked silently to the liable account | A real operational difference: Adyen needs reconciliation to detect it |
| Payout timing basis | Rolling availability per charge, `delay_days` | Sales-day batches with a settlement delay, independent of scheme timing | Adyen decouples seller payout from network settlement and so funds the gap itself |
| Instant payout | Debit card or bank, about 30 minutes, listed countries | `instant` priority where the bank route supports it | |
| Third-party pay-ins | Not found for Connect | Multi pay-in (pilot) | Adyen is opening its ledger to volume it did not acquire |

**For readers new to payments**

- **Split**: the instruction that divides one customer payment among the seller, the platform and the provider's fees.
- **Application fee / commission**: the part of a payment the platform keeps.
- **Transfer**: a movement between two balances inside the provider, as opposed to a **payout**, which leaves the provider for a bank account.
- **Top-up**: bank money added to a balance at the provider that did not come from a customer payment.
- **Interchange++**: pricing in which the card-issuer fee and the network fee are passed through at cost and the provider adds a markup, so the total fee is known only after the payment.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Journey 44 has the same four hard moments on both providers: the split, the payout, the refund after payout, and the dispute after payout. The platform's ledger needs an entry for each leg (customer charge, seller share, platform commission, provider fee, payout, refund, reversal), keyed so that a refund can find the transfers or splits it must unwind.
- On Stripe with separate charges and transfers, the platform owns the linkage (`transfer_group`, `source_transaction`); forgetting it lets automatic platform payouts spend money owed to sellers, which is the problem funds segregation addresses.
- On Adyen, the silent fallback to the liable account means "payment succeeded" does not imply "seller credited"; transfer webhooks or the accounting report must be reconciled per split.
- Because Adyen fees arrive after the payment, a platform that passes fees to sellers cannot show the seller's net at checkout time; it can only show it after the fee booking.

---

## PART 4: Embedded finance (chapter 36)

### 4.1 The licence position, as each company states it

- **Adyen** (own licences): "Our own licensed infrastructure grants direct access to payment networks, giving us control over funds and enabling us to scale advanced monetization and treasury products globally"; "We also capture post-transaction value through our embedded financial products, enabled by our banking licenses. By offering native business accounts, card issuing, and capital within a single integration..." [VERIFIED: Adyen H1 2026 Shareholder Letter, https://investors.adyen.com/financials/h1-2026-c2a1a, published 2026-08-13]. "Adyen is currently in the possession of a pan-European banking license, which was granted in 2017", and the US Federal Reserve approved its application for a US federal branch in San Francisco, then pending OCC approval **(evidence age: 5 years)** [VERIFIED: https://www.adyen.com/press-and-media/adyens-branch-license-application-approved-by-us-federal-reserve, published 2021-05-21]. In H1 2026 Adyen "obtained a Retail Payment Services license from the Central Bank of the UAE" [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13]. Its financial statements describe "Accounts, in the form of merchant-related funds held in business accounts, and Capital, in the form of loans and advances", with net interest income of EUR 8.6 million in H1 2026 (EUR 6.0 million in H1 2025), "which mainly relates to the Accounts product offering" [VERIFIED: H1 2026 Shareholder Letter as above]. The product documentation pages fetched do not mention the licence.
- **Stripe** (partner banks, own money-transmission and e-money licences): "Stripe is not a bank. Checking accounts are provided exclusively by Fifth Third Bank, National Association, Member FDIC" [VERIFIED: https://docs.stripe.com/treasury, n.d., accessed 2026-11]. "Treasury for platforms is provided in the US by Stripe Payments Company, licensed money transmitter, with funds held at Stripe's bank partners, Members FDIC. Card and other credit products are provided by Celtic Bank and serviced by Stripe, Inc. and its affiliate Stripe Servicing, Inc." [VERIFIED: https://docs.stripe.com/treasury/connect/legacy/v1/how-financial-accounts-for-platforms-works, n.d., accessed 2026-11]. For Issuing: "We partner with multiple trusted banks to provide an embedded finance infrastructure" [VERIFIED: https://docs.stripe.com/issuing/how-issuing-works, n.d., accessed 2026-11]. In Europe, "Stripe Technology Europe, Limited, an electronic money institution authorised and regulated by the Central Bank of Ireland" [VERIFIED: https://docs.stripe.com/capital/overview, n.d., accessed 2026-11].

### 4.2 Accounts

**Stripe.** ⚠ The naming and status of this product family are in motion.

- Direct product, "Treasury": "Financial accounts are the core components of Treasury. They receive your settled Stripe earnings, hold funds, and support capabilities such as physical or virtual cards, multi-currency management and conversion, and international outbound payments". Available in the United States and United Kingdom; Australia in private preview. Financial accounts can hold fiat (USD, EUR, GBP) and, for eligible businesses, "a stablecoin balance in OUSD or USDC" (public preview in the US) [VERIFIED: https://docs.stripe.com/treasury, n.d., accessed 2026-11].
- Two US account structures: a "Checking account" backed by a demand deposit account "opened directly with Stripe's banking partner", where "The bank identifies your business as the account holder in its records"; and a "Business account" backed by a for-benefit-of arrangement, where "The bank's records show that the account holds funds for the benefit of Stripe customers" and "Stripe records how much of the total balance belongs to your business and reconciles that record against the funds held at the bank". FDIC treatment differs: ordinary deposit insurance for the first, pass-through insurance (where permitted) for the second, "up to 250,000 USD per depositor" [VERIFIED: same page].
- **Treasury for platforms** (current version): "allows Connect platforms to offer financial services, such as funds separation and storage, bill pay, and cash flow management, to eligible connected accounts. Stripe partners with trusted banks". Availability: "public preview for platforms and connected accounts in the UK"; "private preview for platforms and connected accounts in the US, AU, and the EU" (the country list also shows CA). Access through sales. "Treasury for platforms is available only to platforms with B2B use cases. Stripe doesn't offer financial accounts to consumers" [VERIFIED: https://docs.stripe.com/treasury/connect; https://docs.stripe.com/treasury/connect/requirements, n.d., accessed 2026-11].
- **Legacy v1**: "The v1 version of Treasury for platforms is a legacy integration... Don't build a new v1 integration." It "is available only to platforms and connected accounts located in the United States" [VERIFIED: https://docs.stripe.com/financial-accounts/connect; https://docs.stripe.com/treasury/connect/legacy/v1/requirements, n.d., accessed 2026-11]. So in November 2026 the US platform product sits between a legacy version that is not for new builds and a new version that is in private preview [ASSUMPTION/JUDGEMENT on the reading; both facts verified].
- Preconditions from the Connect side: the platform must bear negative-balance liability (section 1.6), and the `treasury` capability must be managed through Accounts v1 (section 1.3).

**Adyen.**

- "With an Adyen business account, your users can make business-related fund transfers to third-party bank accounts", receive transfers from third parties, and "Receive payouts faster, because you can pay out directly to their Adyen business account" [VERIFIED: https://docs.adyen.com/platforms, n.d., accessed 2026-11].
- **Status, verified**: "This feature is in development phase. Some of the APIs, documentation, and processes may change as the feature evolves" ⚠ [VERIFIED: https://docs.adyen.com/business-accounts, n.d., accessed 2026-11]. It must be "enabled for your balance platform", and the platform must "Implement Adyen's Authentication SDK to comply with the PSD2 regulations" [VERIFIED: https://docs.adyen.com/business-accounts/get-started, n.d., accessed 2026-11].
- **Countries, two versions on Adyen's own pages** ⚠: the product page says "available to eligible legal entities operating throughout the United States, the United Kingdom, and the Eurozone (excluding specific Nordic territories)", listing 19 eurozone countries, mainland UK and the US [VERIFIED: https://docs.adyen.com/business-accounts, n.d., accessed 2026-11]; the verification-requirements page says "BE, DE, ES, FR, GB, NL and US" [VERIFIED: https://docs.adyen.com/platforms/verification-requirements, n.d., accessed 2026-11]. Writers should cite the product page and note the discrepancy.
- Additional verification: source of funds, FATCA/CRS classification, tax residence, possibly source of wealth, and "A live selfie photo and a photo id" for signatories; in the US, the Patriot Act customer identification disclosure and a Regulation GG certification [VERIFIED: https://docs.adyen.com/platforms/verification-requirements, n.d., accessed 2026-11]. Capabilities: `issueBankAccount`, `receiveFromThirdParty`, `sendToThirdParty` [VERIFIED: https://docs.adyen.com/platforms/verification-overview/capabilities, n.d., accessed 2026-11].

### 4.3 Card issuing

**Stripe Issuing.**

- "Commercial issuing is available in Canada, the United States, the United Kingdom, and supported countries in the European Economic Area. Consumer issuing is available in the US. Stablecoin-backed card programs... are also available in more than 60 countries" [VERIFIED: https://docs.stripe.com/issuing, n.d., accessed 2026-11]. Program status: commercial (available); consumer "(Private preview)", described as "bank-sponsored"; stablecoin "(Public preview)" ⚠ [VERIFIED: https://docs.stripe.com/issuing/how-issuing-works, n.d., accessed 2026-11].
- "Use local issuing in 24 countries"; "the Issuer (the financial institution providing cards) and the Stripe platform are in the same region as the connected account and cardholder"; cards are denominated in CAD, USD, EUR or GBP [VERIFIED: https://docs.stripe.com/issuing/global, n.d., accessed 2026-11]. Stripe's annual letter of February 2026 says "our Issuing product is available in only 22 countries some 7 years after launch" [VERIFIED: https://stripe.com/annual-updates/2025 (PDF), published 2026-02-24]; the two counts differ by nine months and two countries.
- **Real-time authorization**: "When a card is used to make a purchase, Stripe creates an `issuing_authorization.request` and sends it to your configured endpoint for your approval." "If Stripe doesn't receive your approve or decline response within 2 seconds, the Authorization is automatically approved or declined based on your timeout settings, or Autopilot settings, if configured." "If your Issuing balance has insufficient funds for the incoming authorization, the authorization will be denied and your webhook endpoint won't receive the `issuing_authorization.request` event" [VERIFIED: https://docs.stripe.com/issuing/controls/real-time-authorizations, n.d., accessed 2026-11].
- Funding: "An Issuing balance is a funding source attached to a connected account"; funded from the connected account's Stripe balance or by bank top-up; with Treasury, cards draw on a financial account [VERIFIED: https://docs.stripe.com/issuing/how-issuing-works, n.d., accessed 2026-11].
- `card_issuing_*` capabilities require Accounts v1 and platform loss liability (sections 1.3 and 1.6).

**Adyen Issuing.**

- "Create fully customizable virtual and physical cards from Mastercard and Visa"; "Use a single pool of funds for all card payments or maintain balances per card"; "currently supported in the European Economic Area, the United Kingdom, and the United States" [VERIFIED: https://docs.adyen.com/issuing, n.d., accessed 2026-11]. The cards are described as debit cards "for business purposes" for organizations and sole proprietorships [VERIFIED: https://docs.adyen.com/financial-products; https://docs.adyen.com/platforms/verification-requirements, n.d., accessed 2026-11].
- A card is a **payment instrument** on a balance account: "Creating a payment instrument issues a card. Each balance account can have one or more payment instruments" [VERIFIED: https://docs.adyen.com/issuing, n.d., accessed 2026-11].
- **Relayed authorisation**: "On each attempt, Adyen sends a webhook to your server. Your server has up to 2000 milliseconds to respond. If we do not receive a response within this timeframe, we apply your default fallback" (default approval or default refusal); HTTP 4xx or 5xx responses also trigger the fallback. Transaction rules can approve or decline automatically [VERIFIED: https://docs.adyen.com/issuing/authorisation; https://docs.adyen.com/issuing/authorisation/relayed-authorisation, n.d., accessed 2026-11].
- Capability levels gate riskier use, for example ATM withdrawals up to EUR 750 per card per day at "Medium" [VERIFIED: https://docs.adyen.com/platforms/verification-requirements, n.d., accessed 2026-11].
- In May 2026 Adyen-issued cards gained card-on-file network tokenization [VERIFIED: https://docs.adyen.com/release-notes/platforms-and-financial-products, entry dated 2026-05-29].

### 4.4 Financing

**Stripe Capital.**

- "Funding volume grew 45% from 2024 to 2025, with Stripe Capital supporting more than 81,000 businesses. (Many of these businesses had access to Stripe Capital funds directly through the vertical SaaS platform on which they run...)" [VERIFIED: https://stripe.com/annual-updates/2025 (PDF), published 2026-02-24].
- **Capital for platforms**: "Stripe and its financial partners manage eligibility, underwriting, pricing, funding, servicing, and collections." Available for connected accounts in AU, CA, DE, FR, GB, US ⚠. Mechanism: daily prequalification from payment activity; an offer of "a principal amount plus a flat fee, with no variable interest"; funds in "1–2 business days"; "Stripe withholds a fixed percentage of each transaction until the complete balance is repaid" [VERIFIED: https://docs.stripe.com/capital/how-capital-for-platforms-works, n.d., accessed 2026-11].
- Providers differ by country: in the US, flex loans and fixed-term loans from "Celtic Bank or Lead Bank", merchant cash advances from YouLend ("A purchase of future receivables, not a loan"), and a line of credit in private preview; in Australia and Canada, "Fundbox provides... a loan"; in Europe, financing "in cooperation with YouLend" with Stripe Technology Europe acting "as an intermediary and technology provider" [VERIFIED: same page; https://docs.stripe.com/capital/overview, n.d., accessed 2026-11].

**Adyen Capital.**

- "We assess risks upfront and proactively create offers for your users"; "Users repay daily based on a fixed percentage of their processed volume through Adyen"; "one transparent fixed fee — no interest and no hidden costs". Countries: Finland, France, Netherlands, Spain, Sweden, United Kingdom, Canada (excluding Saskatchewan), United States, Australia ⚠ [VERIFIED: https://docs.adyen.com/capital, n.d., accessed 2026-11]. "Available on an invite-only basis" [VERIFIED: https://docs.adyen.com/platforms/verification-requirements, n.d., accessed 2026-11].
- Minimum eligibility: "processed payments with Adyen for at least three consecutive months (90 days)" and "a processing volume of at least 1,000 EUR, GBP, USD, or AUD for a minimum of three consecutive months". The funding is a **grant** "disbursed to the user's balance account"; repayment is deducted "from the user's daily net captured volume", and "Adyen monitors progress against a minimum 30-day threshold". Since May 2026 offers come in repayment terms of "90, 180, or 360 days" [VERIFIED: https://docs.adyen.com/capital/how-capital-works; https://docs.adyen.com/release-notes/platforms-and-financial-products, entry dated 2026-05-04].
- The lender is Adyen: "present business financing offers from Adyen" [VERIFIED: https://docs.adyen.com/platforms, n.d., accessed 2026-11]; loans and advances sit on Adyen's balance sheet per its statements (section 4.1).

**Stripe vs Adyen**

| Product | Stripe (documented, November 2026) | Adyen (documented, November 2026) | What the difference suggests [ASSUMPTION/JUDGEMENT] |
| --- | --- | --- | --- |
| Licence | Not a bank; money transmitter (US), e-money institution (Ireland); deposits at Fifth Third Bank; cards and loans from Celtic Bank and Lead Bank; third-party lenders abroad | Own banking licences (EU 2017, US branch approved 2021); accounts and loans on its own balance sheet | Stripe assembles each product per country from partners; Adyen extends one licensed balance sheet |
| Accounts for platform users | Treasury for platforms: UK public preview; US, AU, EU private preview; legacy v1 US-only | Business accounts: "in development phase"; US, UK, eurozone | Neither is generally available everywhere in plain terms; both are sold through sales |
| Issuing | Commercial GA in CA, US, UK, EEA (24 countries); consumer private preview; stablecoin public preview | EEA, UK, US; business debit cards | Similar footprint; Stripe is adding consumer and stablecoin programs |
| Authorization decision window | 2 seconds, then configured default | 2000 milliseconds, then configured default | Same number; it is likely derived from network response limits |
| Financing | Six countries via partner lenders; loans and merchant cash advances | Nine countries, invite-only; Adyen is the lender | Stripe's partner model reaches product variety; Adyen's is one product |
| Dependency on platform setup | Platform must bear seller losses; v1 API for capabilities | Enabled per balance platform; extra capabilities and verification | In both, embedded finance raises the platform's own compliance duties |

**Contrast cases (brief).**

- **Shopify Balance** is built on Stripe's stack: "Shopify is a tech company, not a bank"; it partners "with Stripe Payments Company for money transmission services" "with funds held at Fifth Third Bank N.A., Member FDIC"; cards "are powered by Stripe and issued by Celtic Bank" [VERIFIED: https://help.shopify.com/en/manual/finance/shopify-balance, n.d., accessed 2026-11].
- **Mangopay** is the e-money-institution model: "Mangopay S.A. is an EMI under Luxembourg law, authorized by the CSSF"; users are a `PAYER` by default and become an `OWNER`; KYC level is `LIGHT` until verification makes it `REGULAR` [VERIFIED: https://docs.mangopay.com/guides/users/verification, n.d., accessed 2026-11].
- **PayPal** offers "multiparty payment processing solutions for marketplaces and platforms" with "Partner fees" that "enable partners to charge commissions or brokerage fees for each transaction", settled "once daily" [VERIFIED: https://developer.paypal.com/docs/multiparty/, n.d., accessed 2026-11]. Hyperwallet and Braintree Marketplace were not verified.
- **Unit** describes itself as "an enterprise-grade financial infrastructure platform" and says "As a program manager, you manage the relationship with your partner bank(s)" [VERIFIED: https://www.unit.co/docs/api/, n.d., accessed 2026-11], which puts the bank relationship on the customer, unlike Stripe or Adyen [ASSUMPTION/JUDGEMENT].

**For readers new to payments**

- **Banking-as-a-service**: a licensed bank's accounts, cards or loans offered through another company's software, with the bank in the background.
- **For-benefit-of (FBO) account**: one bank account held in the provider's name for many customers, with the provider's ledger recording who owns what.
- **Issuer**: the licensed institution that puts a card in someone's hands and approves or declines each use of it.
- **Merchant cash advance**: money advanced against future sales and repaid as a share of them; legally a purchase of receivables rather than a loan.

**Architecture implications** [ASSUMPTION/JUDGEMENT]

- Issuing turns the platform into a participant in the authorization path with a hard two-second budget on both providers. The endpoint needs its own availability target and a deliberate default for timeouts, because the default is applied whenever the platform is slow or down.
- A stored balance (financial account or business account) changes the seller record from "pay out everything" to "hold, spend and send", which adds statements, authentication for outgoing transfers (Adyen requires its SCA SDK) and fraud controls the platform must run.
- Availability is the binding constraint. A platform operating in several countries will find a different subset of accounts, cards and capital in each, at different release stages, on both providers; product plans should be made per country.

---

## PART 5: Architecture record and scale

### 5.1 What each company has published about how the platform product is built

- **Stripe**: no engineering-blog post describing Connect's internal architecture was found (searched: Stripe engineering blog and web search for Connect internals, ledger, connected-account architecture). The public record is the documentation, the 2015 and 2017 product posts, and the Sessions 2026 talk by a solutions architect, which is integration guidance, not internals. One historical sentence hints at intent: with many-to-many payments, platforms "use Connect to track every part of their payments flow in one place, and they don't have to manually build and manage a ledger" **(evidence age: 9 years)** [VERIFIED: https://stripe.com/blog/connect-updates, published 2017-05-25].
- **Adyen**: describes the balance platform in one line as "an accounting system that manages the flow of funds within your business" [VERIFIED: https://docs.adyen.com/platforms/account-structure-resources, n.d., accessed 2026-11]. No engineering post on its internals was fetched in this session; the ledger brief may hold more.
- Everything about internal data stores, services or consistency models for either platform product is **not public** as far as this session found [ASSUMPTION/JUDGEMENT].

### 5.2 Scale figures

- Stripe: "businesses running on Stripe generated $1.9 trillion in total volume, up 34% from 2024"; "more than 5 million businesses directly or via platforms" [VERIFIED: https://stripe.com/annual-updates/2025 (PDF), published 2026-02-24]. **The letter gives no Connect-specific volume or account count** (the PDF was searched for "Connect" and "platforms").
- Adyen, H1 2026: "Platforms: Net revenue reached €165.5 million, up 37% YoY (40% CC), driven by our expansion across vertical SaaS businesses, particularly in the financial services and food & beverage verticals. Processed volume rose 42% YoY to €135.0 billion. We now power 37 platform customers processing over €1 billion annually, up from 32 a year ago. Active business customers reached 293K, up 51% YoY", the last "Defined as all end-customers that meet the processed volume thresholds for capital grants" [VERIFIED: Adyen H1 2026 Shareholder Letter, https://investors.adyen.com/financials/h1-2026-c2a1a, published 2026-08-13]. Group totals for the same half: net revenue €1,302.9 million, processed volume €803.8 billion [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13]. Platforms was therefore about 13% of net revenue and 17% of processed volume [ASSUMPTION/JUDGEMENT: the researcher's arithmetic].

---

## Key numbers

| Number | Definition | Source and date |
| --- | --- | --- |
| USD 1 million | Annual transaction volume above which an acquirer must have a direct merchant agreement with a payment facilitator's sponsored merchant (Visa), subject to exceptions | Visa Core Rules, 24 October 2026, rule 5.3.1.4 ⚠ |
| USD 10 million and 10% | Limits on a foreign retailer's Visa volume through a marketplace (both must not be exceeded) | Visa Core Rules, 24 October 2026, rule 5.3.4.1 |
| 180 days | Time a connected account's balance may stay negative before Stripe moves platform reserve funds to cover it (platform-liable accounts) | docs.stripe.com/connect/risk-management, accessed 2026-11 |
| 45 days | Time a pending Connect refund waits for sufficient balance before failing | docs.stripe.com/connect/charges, accessed 2026-11 |
| 31 | Maximum `delay_days_override` for a connected account's payout delay | docs.stripe.com/connect/manage-payout-schedule, accessed 2026-11 |
| 30 minutes | Typical arrival time of a Stripe Instant Payout | docs.stripe.com/connect/instant-payouts, accessed 2026-11 |
| €2 / 0.25% + €0.10 | Stripe Connect list price when the platform handles pricing: per monthly active account / per payout (Netherlands locale) | stripe.com/en-nl/connect/pricing, accessed 2026-11 ⚠ |
| 30 and 60 days | Adyen standard verification deadlines by capability (payout-type capabilities 30; payment-receiving and card capabilities 60) | docs.adyen.com/platforms/verification-overview, accessed 2026-11 ⚠ |
| 24 hours | Time limit to allocate funds from an Adyen multi pay-in account to balance accounts | docs.adyen.com/platforms/multi-pay-in, accessed 2026-11 ⚠ |
| 2 business days / 1 business day | Adyen managed payout "Standard" / "Accelerated" arrival after capture | docs.adyen.com/platforms/managed-payouts, accessed 2026-11 |
| 2 seconds / 2000 ms | Issuing authorization decision window before the configured default applies (Stripe / Adyen) | docs.stripe.com/issuing/controls/real-time-authorizations; docs.adyen.com/issuing/authorisation, accessed 2026-11 |
| 24 (22) countries | Stripe local commercial issuing countries per documentation (per the February 2026 letter) | docs.stripe.com/issuing/global, accessed 2026-11; Stripe annual letter, 2026-02-24 ⚠ |
| 81,000+ businesses; +45% | Businesses supported by Stripe Capital; growth in funding volume 2024 to 2025 | Stripe annual letter, 2026-02-24 |
| 3 months and 1,000 | Adyen Capital minimum processing history and monthly volume (EUR, GBP, USD or AUD) | docs.adyen.com/capital/how-capital-works, accessed 2026-11 |
| €135.0 billion; €165.5 million | Adyen Platforms processed volume and net revenue, H1 2026 (+42%, +37% year on year) | Adyen H1 2026 Shareholder Letter, 2026-08-13 |
| 293K; 37 | Adyen platform "active business customers" (end-customers meeting capital-grant volume thresholds); platform customers processing over €1 billion a year | Adyen H1 2026 Shareholder Letter, 2026-08-13 |
| $1.9 trillion; 5 million+ | Stripe total volume 2025; businesses served "directly or via platforms" | Stripe annual letter, 2026-02-24 |

## Open questions / not verifiable

1. **Mastercard's current payment-facilitator and sub-merchant rules** (definitions, threshold, registration fee): the rulebook could not be fetched; only a 2014 article supports the $1 million figure.
2. **Whether Stripe Accounts v2 is formally generally available.** Documentation recommends it for new platforms while its examples use a `.preview` API version and several features still require v1.
3. **Connect's size**: Stripe publishes no Connect volume, platform count or connected-account count in its 2025 letter.
4. **Stripe's full list of partner banks by product and country**, and which bank stands behind UK and EU financial accounts.
5. **Whether Adyen offers any arrangement in which Adyen, not the platform, bears seller losses**, and how long a user's negative balance may stand before the liable account is debited. Nothing found.
6. **Adyen staggered-verification tier amounts** and the full list of payout priorities and their rails per country (the pages did not render as text).
7. **Adyen business-account country list**: two Adyen pages disagree.
8. **Adyen classic integration end-of-life**: no date found.
9. **Adyen for Platforms pricing**: no public price list.
10. **Internals of either platform product** (how balances, splits and transfers are stored and kept consistent): nothing published that this session found.
11. **Onboarding conversion rates** for hosted or embedded flows: neither company publishes figures.
12. **Exact date of the Standard / Express / Custom naming** and of the introduction of controller properties: not found on a dated page.
13. **US-dollar list prices** for Connect.

## Source list

**Card networks**

- Visa Core Rules and Visa Product and Service Rules, Visa, 24 October 2026 — https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf — definitions of payment facilitator, sponsored merchant, marketplace; USD 1 million threshold; marketplace qualification.
- "Visa's Payment Facilitator Model", Visa, © 2024 — https://usa.visa.com/dam/VCOM/global/support-legal/documents/visa-payment-facilitator-model.pdf — roles of acquirer, facilitator and sponsored merchant.
- "MasterCard: Sub-Merchants Don't Need to Own Accounts Until Volume Hits $1 Million", Digital Transactions, 21 November 2014 — https://www.digitaltransactions.net/mastercard-sub-merchants-dont-need-to-own-accounts-until-volume-hits-1-million/ — historical thresholds (secondary; 12 years old).

**Stripe**

- "The new Connect", Stripe blog, 23 March 2015 — https://stripe.com/blog/the-new-connect — Connect since 2012; managed accounts.
- "Improving Connect to enable more platforms", Stripe blog, 25 May 2017 — https://stripe.com/blog/connect-updates — Express; split charges and transfers; account debits.
- Stripe 2025 annual letter, Stripe, 24 February 2026 — https://stripe.com/annual-updates/2025 — total volume, businesses served, Issuing countries, Capital figures.
- "Splitting the check: Architecting multiparty payment flows", Stripe Sessions 2026 — https://stripe.com/sessions/2026/splitting-the-check-architecting — account "traits", liability first.
- "Introduction to payment facilitators" guide, Stripe, n.d. — https://stripe.com/guides/payfacs — obligations and cost estimates of becoming a facilitator.
- Connect pricing, Stripe, n.d. — https://stripe.com/en-nl/connect/pricing — the two pricing models and list prices (euro).
- Stripe documentation, n.d., accessed November 2026, all under https://docs.stripe.com/: `connect/accounts-v2` (v2 configurations, limitations); `connect/accounts-v2/connected-account-configuration` (responsibilities, dashboard, KYC collector, v1 map); `connect/accounts` (legacy types); `connect/migrate-to-controller-properties` (controller properties); `connect/charges` (charge types, refunds, disputes, `on_behalf_of`); `connect/destination-charges` (application fee flow, settlement merchant, refund flags); `connect/separate-charges-and-transfers` (`transfer_group`, `source_transaction`); `connect/merchant-of-record` (MoR rules); `connect/risk-management` and `connect/risk-management/managed-risk` (liability, 180 days, Managed Risk); `connect/account-balances` (balances, reserves, auto-debit); `connect/direct-charges-fee-payer-behavior` (fee payer, dispute fees); `connect/platform-pricing-tools`; `connect/saas`; `connect/marketplace`; `connect/disputes`; `connect/statement-descriptors`; `connect/account-capabilities`; `connect/handling-api-verification` (requirements, deadlines); `connect/onboarding`; `connect/hosted-onboarding` (Account Links); `connect/get-started-connect-embedded-components` and `connect/supported-embedded-components`; `connect/manage-payout-schedule`; `connect/instant-payouts`; `connect/cross-border-payouts`; `connect/cross-border-payouts-to-recipients/compare-global-payouts`; `global-payouts`; `connect/top-ups`; `connect/account-debits`; `connect/service-agreement-types`; `connect/funds-segregation`; `treasury`; `treasury/connect`; `treasury/connect/requirements`; `financial-accounts/connect` and `treasury/connect/legacy/v1/…` (legacy v1); `issuing`; `issuing/global`; `issuing/how-issuing-works`; `issuing/controls/real-time-authorizations`; `capital/overview`; `capital/how-capital-for-platforms-works`.

**Adyen**

- Adyen H1 2026 Shareholder Letter and interim financial statements, Adyen N.V., 13 August 2026 — https://investors.adyen.com/financials/h1-2026-c2a1a — Platforms segment figures, licence statements, Accounts and Capital in the financial statements.
- "Adyen publishes H1 2026 financial results", Adyen press release, 13 August 2026 — https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne — group figures, UAE licence.
- "Adyen's branch license application approved by US Federal Reserve", Adyen press release, 21 May 2021 — https://www.adyen.com/press-and-media/adyens-branch-license-application-approved-by-us-federal-reserve — EU banking licence 2017, US branch.
- Release notes, platforms and financial products, Adyen, entries 2021–2026 — https://docs.adyen.com/release-notes/platforms-and-financial-products — dates for balance platform APIs, managed payouts, hosted onboarding email, Capital terms.
- Adyen documentation, n.d., accessed November 2026, all under https://docs.adyen.com/: `adyen-for-platforms-model` (marketplace versus platform, classic cut-off date); `classic-platforms`; `platforms` (countries, acquiring regions, financial products); `platforms/get-started`; `platforms/account-structure-resources` (resources, liable account, one balance platform per region); `platforms/account-structure-resources/platform-structure` (payment facilitators, worked structure); `marketplaces/account-structure-resources/marketplace-structure`; `platforms/account-structure-resources/legal-entity-management`; `platforms/verification-overview` (triggers, deadlines); `platforms/verification-overview/capabilities`; `platforms/verification-overview/verification-types` (upfront, staggered, tiers); `platforms/verification-overview/data-review-process`; `platforms/verification-requirements` (financial-product requirements and availability); `platforms/onboard-users`; `platforms/onboard-users/onboarding-steps`; `platforms/onboard-users/components`; `platforms/onboard-users/terms-of-service`; `platforms/online-payments/split-transactions` (split types); `platforms/online-payments/transaction-fees`; `platforms/automatic-split-configuration`; `platforms/how-adyen-applies-split-instructions`; `platforms/online-payments/split-transactions/split-refunds`; `platforms/online-payments/split-transactions/split-chargebacks`; `platforms/multi-pay-in`; `platforms/settle-funds`; `platforms/managed-payouts`; `platforms/custom-payouts` with `/scheduled-payouts` and `/on-demand-payouts`; `platforms/internal-fund-transfers`; `platforms/top-up-balance-account` with its sub-pages; `financial-products`; `business-accounts` and `business-accounts/get-started`; `issuing`; `issuing/authorisation` and `issuing/authorisation/relayed-authorisation`; `capital` and `capital/how-capital-works`.

**Contrast**

- Shopify Balance help page, Shopify, n.d. — https://help.shopify.com/en/manual/finance/shopify-balance — Stripe, Fifth Third Bank and Celtic Bank disclosures.
- Mangopay user verification guide, Mangopay, n.d. — https://docs.mangopay.com/guides/users/verification — e-money institution model, user and KYC levels.
- PayPal multiparty documentation, PayPal, n.d. — https://developer.paypal.com/docs/multiparty/ — partner fees for platforms.
- Unit API documentation, Unit, n.d. — https://www.unit.co/docs/api/ — program-manager model.
