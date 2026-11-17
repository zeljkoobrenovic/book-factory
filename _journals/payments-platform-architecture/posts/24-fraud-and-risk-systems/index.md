---
title: "Deciding in Milliseconds: Fraud and Risk Systems"
date: 2026-11-17
author: Željko Obrenović
excerpt: "How does a provider decide, during an authorization, whether a payment is fraud? It cannot know: it estimates the chance of a later fraud dispute, blocks above a threshold before the bank is asked, and learns weeks afterwards whether it was right, so the threshold is a price the merchant sets and pays."
permalink: payment-fraud-and-risk
timetoread: 28 min read
---

> **IN THIS CHAPTER, YOU WILL:** Learn where a provider's fraud decision sits, what its score estimates, why the evidence arrives weeks late, and how to price a block threshold.

> **KEY POINTS:**
>
> * **A risk score is a forecast of a dispute, not a finding of fraud.** Stripe and Adyen both decide before the cardholder's bank sees the payment and again after it answers. Adyen's documentation defines its risk level as the likelihood of "a fraudulent dispute", an event that has not happened yet.
> * **The evidence arrives weeks later, or never.** Stripe's 2026 figures show 41% of fraud disputes reported by day 14 and 86% by day 60, and a blocked payment never gets an outcome at all. No rule or model change can be judged on its first two weeks. Adyen lets a few payments through whatever their risk to keep measuring, and Stripe documents a similar device.
> * **The threshold is a price, and card testing is outside it.** The merchant pays for fraud it accepts and for good customers it refuses, so it has to set the threshold from its own margins. Card testing leaves no dispute to learn from and has to be stopped before authorization, by limits on the endpoint.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-payment-systems-go-wrong.html):**
>
> * **The Open Till** — a public booking page that can start a payment without a login or a limit is what bots use to test stolen cards.
> * **The Borrowed Blueprint** — a default threshold or a vendor's network-wide false-positive figure is taken as right for a business whose margins it was never set for.
> * **The Phantom Payment** — a payment the provider blocked, or passed with "unknown risk", is recorded as if the bank had judged it.

<br>
At 03:14 on a Saturday a €1 payment arrives at a studio's booking page. The card number is real, the expiry date is right and the three-digit code matches. Nothing was stolen from the studio, its platform or its payment provider; the number was taken somewhere else, months ago. Stripe's documentation (n.d., accessed November 2026) defines the problem: "A payment is considered fraudulent when the cardholder didn't authorize it. Most fraudulent payments are made using stolen cards or card numbers." The European Banking Authority and the European Central Bank report that theft of card details made up "more than 56% of the total value" of fraud on online card payments in 2024. The vault and the network token of the last two chapters protect a stored card; they do nothing here. **The only person who knows this payment is fraud is the cardholder**, who is asleep and will find out from a bank statement some weeks from now.

So a provider does not detect fraud during an authorization (the real-time request to the cardholder's bank, the **issuer**, to approve a payment). It **estimates how likely the payment is to be disputed as fraud later**, and blocks it above a threshold before the issuer is asked. It learns weeks afterwards whether it was right, and only for the payments it let through. The threshold is therefore **a price with two costs**, fraud accepted and good customers refused, and both fall on the merchant.

**Where we are in the payment's journey.** When Mila Janssen buys her €120.00 class pass at 19:42 on Tuesday 9 March 2027, the risk decision sits between Larkfield's request to Adyen and the authorization request to her bank ([[payment-authorization]]). She pays from her phone's wallet, which checked her fingerprint, and nothing is blocked. The payment this chapter is mostly about looks like the one that set up her €49.00 membership on 12 January: a card number typed into a web page.

The chapter starts at Larkfield, the fictional studio-software platform this book follows, with the Card-Testing Weekend. It then covers the kinds of fraud and how the evidence for each arrives, where the decision sits in the authorization path, and how the models learn from disputes that come late. Next come the threshold as a price, card testing, and risk in the merchant being paid. The comparison of Stripe and Adyen follows, then what Larkfield changed, and the ways a risk system fails.

## Setting the Scene at Larkfield: The Card-Testing Weekend

On the weekend of 8–9 August 2026 bots sent **61,000 one-euro payments**, each with a different stolen card number, through the public booking widget of one Larkfield studio. The widget sold €1 trial drop-ins to guests who had no account, so anyone could start a payment from it. Of the 61,000 attempts, about 38,400 were blocked by the provider before they reached a bank, 19,700 were declined by the issuers and 2,900 were approved *(the split is an illustrative assumption; the total is Larkfield's)*.

The result was a bill without a theft. Larkfield stored none of those card numbers and lost no data. It refunded the 2,900 approved payments at once, because each one left alone could have come back as a dispute with a fee of €15.00 *(illustrative)*. With provider fees on the attempts and the refunds, the weekend cost Larkfield **€4,100** *(about €2,900 in refunds and €1,200 in fees; the split is an assumption)*. An engineer switched off the studio's online payments to stop the attack, and the studio could not sell online for **31 hours**.

In February 2027 Femke de Graaf, Head of Payments Engineering, reviews the weekend with Jonas Weber, who leads risk and compliance. Three questions remain. What does the provider's risk system decide, and when? Why did a system built to catch fraud not treat 61,000 stolen cards as fraud? And who chooses how strict it is?

## Five Kinds of Fraud, and How the Evidence for Each Arrives

The payment system learns of card fraud in one way: the cardholder tells the issuer, and the issuer files a **dispute** (a chargeback: the bank takes the money back from the merchant; see [[refunds-reversals-and-disputes]]). The loss lands on the merchant. Stripe's documentation says that when such a dispute is decided for the cardholder "the business suffers a loss equal to the amount of the payment, and the cost of any goods or services already provided. The business is also subject to a dispute fee." Fraud is also an online problem. In the EBA and ECB report for 2024 the card fraud rate by value was 0.091% for remote payments against 0.007% for payments with the card present, "13 times higher in value". Fraud is rare, then, and concentrated where a number can be typed in.

"Fraud" covers five different things, and for a system builder the useful difference is how the evidence arrives. The quoted definitions are Stripe's (it files the last one under "marketplace fraud"); account takeover is absent from both companies' risk-product documentation, so its row follows Adyen's payment-fraud guide (2025): "when fraudsters get access to shoppers’ accounts". Fraud between the users of a marketplace (fake listings, scams) is a separate subject, covered in [[fraud-prevention]].

| Kind | What happens | How the evidence arrives | Who carries the loss by default |
| --- | --- | --- | --- |
| **Stolen-card fraud** | Someone pays with a card number that is not theirs | A dispute, weeks later | The merchant |
| **Card testing** | "testing a card (or multiple cards) on one site to see if it's still valid before using it on another site" | No evidence per payment; most attempts are declined and few are ever disputed | The tested merchant pays fees; a later merchant takes the fraud |
| **Account takeover** | A criminal logs in as a real customer and pays with the stored card | A dispute or a complaint from the customer | The merchant |
| **Friendly fraud** | "a legitimate cardholder makes a purchase, but then disputes it at a later date" | The same dispute as real fraud | The merchant, unless it wins the dispute |
| **Merchant fraud** | "a fraudulent business takes payments without providing the services or goods" | Many disputes against one account | The platform or the provider, if the seller's funds are gone |

Only the first row produces clean evidence tied to one payment, and it comes late. That has two consequences. A single verdict on a payment hides at least three prediction problems: a late dispute, an attack with no per-payment evidence, and a property of an account *(my reading, not a vendor's)*. And because fraud is rare, the commonest error is a **false positive**: a legitimate payment refused. Take the same report's remote rate by number of payments, 0.068%: about 7 payments in every 10,000. A detector that is wrong about only 1% of legitimate payments refuses about 100 good payments in those 10,000, some fifteen for every fraudulent one it could catch *(my arithmetic)*.

## Where the Decision Sits: Before the Issuer, and Again After

The first decision is made before the card network (Visa or Mastercard, which carries the request between the banks) and the issuer see the payment. Stripe's documentation (n.d., accessed November 2026) shows the record of a payment blocked for risk: `"network_status": "not_sent_to_network"`, `"type": "blocked"`, `"reason": "highest_risk_level"`. Adyen's documentation (n.d., accessed November 2026) describes the same placement and gives the reason: "Pre-authorization: the risk rule conditions are assessed before the payment is authorized. This saves issuer and scheme fees compared to blocking after authorization." ("Scheme" is Adyen's word for a card network.) A blocked payment is one the bank was never asked about, which is why [[authorization-optimization]] kept it out of the issuer's decline count.

<!-- illustration-placeholder
{
  "id": "24-two-decision-points",
  "status": "pending",
  "asset": "assets/images/24-fraud-and-risk-systems/24-two-decision-points.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph on the first decision before the network",
  "visual_goal": "Show that the risk decision is made twice: once before the bank is asked, with a block that never reaches the bank, and once after the bank answers, when more signals exist.",
  "prompt": "Create a left-to-right flow diagram with four generic boxes in a row: a shop labeled \"Merchant\", a payment company building labeled \"Provider\", a hub labeled \"Card network\", and a bank building labeled \"Issuer\". A thick blue arrow labeled \"Request\" runs from the merchant to the provider. Inside the provider box draw two round gates. The first gate, on the left, is labeled \"Decision 1\"; an orange arrow labeled \"Blocked\" drops down out of it and ends at a small stop sign, never reaching the network. A blue arrow continues from the first gate through the card network to the issuer. A green arrow labeled \"Answer\" returns from the issuer through the network to the second gate, on the right inside the provider box, labeled \"Decision 2\". From the second gate one green arrow labeled \"Allow\" goes back to the merchant and one teal arrow goes down to a desk with a person, labeled \"Review\". A dashed bracket under the stop sign reads \"Bank never asked\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Flow from merchant to provider, card network and issuer with two decision gates inside the provider, one before the network and one after the issuer's answer.",
  "caption": "The risk decision is made twice: before the bank is asked, where a block never reaches the bank, and again after the bank answers."
}
-->

A second decision follows the issuer's answer, because some signals exist only then. Adyen's documentation says that in post-authorization rules "the risk evaluation can take extra signals into account that are only available after authorization. For example authentication results, CVC/CVV codes, or AVS responses" (the issuer's check of the three-digit security code and of the billing address). Stripe documents built-in rules that "block certain payments that the card issuer approved". Review by a person comes later still. Stripe: "Payments placed into review are typically already successfully processed, unless you capture authorized payments later" (capture is the separate instruction that takes the money an authorization has reserved). Adyen, if capture is delayed for review, gives "up to seven calendar days to reject a transaction". By then the cardholder's money is already reserved.

Both decisions use a **risk score**: the provider's estimate of how likely this payment is to end in a fraud dispute. Adyen's documentation says so in those terms. Its fraud-risk rule, a premium feature of its risk engine, assigns a level "ranging from **Very Low** to **Very High**", which "indicates the likelihood that a transaction will result in a fraudulent dispute", and "By default, the block threshold for this rule is set to high risk and above." Stripe's product, Radar, attaches "a risk score that ranges from 0–99": "By default, a score of 65 or above indicates elevated risk, while a score of 75 or above indicates high risk." Radar blocks the highest level by default and allows elevated-risk payments, which go to a review queue on plans that have one. As of November 2026 the number itself is returned only on the Plus and Pro plans, the upper two of Radar's four. Two cautions apply. Stripe's page on risk settings calls this score "the probability that a payment results in a fraudulent dispute or early fraud warning" (an early fraud warning is an issuer's notice that a cardholder has reported fraud), but neither company documents how a score or a level maps to a percentage, so I read a score of 65 as a rank and not as a 65% chance *(my reading)*. And the same page says Radar "is deprecating" the block rule built on this score in favor of "risk settings, which use separate models to block payments", with separate scores from 0 to 99 for fraudulent disputes, early fraud warnings and fraudulent payments.

The estimate has to fit inside the payment call. Stripe's 2023 engineering post said Radar "makes this decision, accurately, in less than 100 milliseconds" **(Evidence age: 3.6 years; the current system may differ.)** Its 2024 post on the system that serves model inputs adds that "the time required to retrieve features directly impacts the overall payment API latency", and its October 2026 post says only that the model "scores payments in milliseconds". Adyen publishes no figure for the whole risk decision. A January 2025 Adyen engineering post gives its model-serving service "a p50 of 20 ms and p99 of 100 ms" per request; a transaction passes "between 2 and 5" such endpoints.

| Requirement | Stripe | Adyen |
| --- | --- | --- |
| How fast | "less than 100 milliseconds" (2023) | 20 ms median, 100 ms at the 99th percentile, per model endpoint (2025); whole decision not published |
| How consistent | A retry of the same payment gets the same treatment under a partly rolled-out rule (documentation) | Not documented |
| How available | Not documented | Not documented |
| On failure | "an error might cause risk evaluation to fail. If this happens, Stripe reports the payment as having unknown risk"; the documented example is authorized | Not documented |

> **INFERENCE, NOT DOCUMENTED:** A step that runs inside every card payment needs a hard time limit and a decided behavior when the limit passes. Stripe's documented "unknown risk" outcome on an authorized payment suggests that on an error it lets the payment through. Whether the same holds for a slow evaluation, and what Adyen does in either case, is not in the public record.

The inputs to the estimate are called **fraud signals**, and most of their value comes from the provider seeing many merchants. Stripe's 2026 post: "a credit card that is new and untrusted to one business might have years of history elsewhere on Stripe that proves it's OK or an IP address may link activity across several cards and accounts." Adyen's documentation says its models "can detect recent fraud on a shopper's email address or recognize a good shopper because of a recent in-person payment on a card on the Adyen platform". Other signals are collected in the browser. Adyen "collects data about how shoppers interact with and use the payment form", and Stripe's card-testing guidance marks "Advanced fraud detection", the device and activity signals its JavaScript library gathers in the browser, as "Highest impact" among the data a merchant can send to its card-testing models. So the way you collect card data ([[tokenization-vaulting-and-pci]]) also decides how much the fraud model can see.

## Learning Weeks Later: Labels, Delay and the Payments Nobody Sees

A model learns from **labels**: the after-the-fact record that a given payment was fraud. For card fraud the label is the dispute, and it is slow. Stripe's October 2026 engineering post: "For a payment made with a stolen card, it could take weeks for the cardholder to notice and report it to their bank. When Stripe receives the fraudulent dispute, we gain a fraud label for a payment we scored weeks earlier." The description of its chart puts numbers on the wait: the share of fraud disputes reported reaches "41% by day 14, 66% by day 30, and 86% by day 60 after the payment". Two weeks after any change, more than half of the evidence about it does not exist yet.

<!-- illustration-placeholder
{
  "id": "24-label-arrival-curve",
  "status": "pending",
  "asset": "assets/images/24-fraud-and-risk-systems/24-label-arrival-curve.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that gives the 41%, 66% and 86% figures",
  "visual_goal": "Show that fraud reports arrive slowly, so a verdict given two weeks after a change sees less than half of the evidence.",
  "prompt": "Create a simple chart-style illustration. A horizontal axis is labeled \"Days after payment\" with three tick marks labeled \"14\", \"30\" and \"60\". A smooth rising teal curve starts at the bottom left and flattens toward the top right. Three round markers sit on the curve above the ticks, labeled \"41%\", \"66%\" and \"86%\". Above day 14 stands a small figure of an analyst holding a clipboard next to an orange flag labeled \"Verdict too early\". The area above the curve at day 14 is shaded light orange and labeled \"Not reported yet\". Above day 60 a green flag is labeled \"Judge here\". Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Rising curve of fraud reports over time with markers at 41%, 66% and 86% for days 14, 30 and 60.",
  "caption": "Fraud disputes arrive slowly: 41% by day 14, 66% by day 30 and 86% by day 60, so a verdict at two weeks sees less than half of them."
}
-->

That delay can reverse a verdict. The same post describes a larger version of Radar's model that "looked better in offline tests and in early results of a production experiment. But, as more fraud reports arrived, its measured performance fell below the earlier model's, and we had to roll back". The cause was the delay itself: training on recent payments without sampling had added "more fraudulent examples labeled as legitimate, about 20 times more", because their disputes had not arrived. If a company with Stripe's volume of data misjudged a change on early results, a merchant judging a new rule after two weeks has less to go on.

Worse, a blocked payment never gets a label, because nobody finds out what it would have been. The remedy is a **holdout**: a small share of payments let through whatever their score, so that their outcomes can be seen. Adyen documents one and calls it control traffic: "A very small percentage of all transactions is randomly selected to be part of control traffic. Control traffic transactions are settled regardless of their risk evaluation." (Settled here means processed and paid like any other payment.) Adyen limits the cost by excluding, among others, "Transactions with an amount of EUR 2000 or higher". Stripe's documentation has one sentence: "For a small subset of payments, Stripe modifies the reported risk score so we can measure the performance of our models and obtain data for subsequent model development." It does not say that payments which would have been blocked are let through. A Stripe manager's 2018 talk (InfoQ transcript) described letting "a small fraction of them go through uniformly at random" **(Evidence age: 8 years.)** That Radar does this today is my inference. A fraud system without a holdout cannot count the good customers it refuses.

Together the two gaps make a **feedback loop**: the system's own decisions determine which outcomes it will later see. Merchants are part of the loop. On Stripe, refunding a payment with the reason `fraudulent` adds its card fingerprint (Stripe's identifier for a card number) and email address to the default block lists, and the documentation says "Our AI models respond to feedback you share with us". That is a faster label than a dispute. The labels are also noisy, since friendly fraud arrives through the same dispute as a stolen card *(my judgement)*.

How much is known about the model inside this loop differs sharply between the two companies. Stripe's 2023 post traced Radar from "relatively simple ML models (e.g., logistic regression)" through an ensemble of a tree-based model (XGBoost) and a deep neural network to, "in mid-2022", "a pure DNN-only model" **(Evidence age: 3.6 years; the 2026 post links back to this one and describes a neural-network architecture.)** The 2026 post names the transaction-fraud model Shield, gives "roughly 800 million transactions in its training set", and says a new training configuration "improved recall by over 8%" in a controlled comparison (recall is the share of fraud caught). The version trained on more data "grew to roughly 30 million parameters, three times its previous size"; that is the version the post says was rolled back, and it does not give the size of the model now in production. It speaks of "regular retraining" and gives no interval; a 2019 Stripe engineering post said Radar's models were trained and deployed "on a daily cadence" **(Evidence age: 7 years.)** For Adyen's fraud-risk model the documentation says only that the premium features offer "Machine learning powered fraud detection using global transaction data". An August 2024 Adyen engineering post adds that the fraud models are "currently based on tree-based ensembling models", retrained "on a default weekly cadence" **(Evidence age: 2 years.)**

## The Threshold Is a Price: Refused Customers against Fraud Losses

Wherever the threshold sits, it trades two errors: fraud allowed, and good customers refused. The merchant pays for both. A refused customer is a lost sale. For accepted fraud, Stripe's documentation is plain: "you're ultimately responsible for payments you choose to accept, including those that are later disputed or found to be fraudulent." The provider makes the estimate; the loss stays with you. Stripe's 2023 post said "Radar incorrectly blocks just 0.1%" of legitimate payments **(Evidence age: 3.6 years.)** That is a vendor's network average, not your rate.

<!-- illustration-placeholder
{
  "id": "24-threshold-as-price",
  "status": "pending",
  "asset": "assets/images/24-fraud-and-risk-systems/24-threshold-as-price.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that says the threshold trades two errors",
  "visual_goal": "Show the block threshold as one dial with two costs: moving it one way refuses more good customers, moving it the other way accepts more fraud, and the merchant pays for both.",
  "prompt": "Create a conceptual illustration centered on a wide horizontal slider with a round orange knob near the middle, labeled \"Threshold\". At the left end of the slider is a group of friendly generic customers turned away from a closed shop door, with a growing stack of euro coins beside them labeled \"Refused customers\". At the right end is a masked generic figure walking out with a shopping bag, with another stack of euro coins labeled \"Accepted fraud\". Two curved arrows show that sliding the knob left makes the left stack taller and sliding it right makes the right stack taller. Below the slider, in the center, a shopkeeper holds a single bill labeled \"Merchant pays\" with two thin lines connecting the bill to both stacks. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "A slider labeled Threshold between a stack of costs from refused customers and a stack of costs from accepted fraud, both connected to a bill the merchant pays.",
  "caption": "One dial, two costs: a stricter threshold refuses more good customers, a looser one accepts more fraud, and the merchant pays for both."
}
-->

The trade can be priced. Block a payment only when its chance of fraud times the cost of a fraud case is greater than its chance of being legitimate times the cost of refusing a good customer. The break-even chance is the cost of a refused customer divided by the sum of the two costs. Take a €200 item that cost the retailer €160, with a €15 dispute fee *(illustrative)*. A fraud case loses €175 and a refused customer loses the €40 margin, so the break-even is 40 ÷ (40 + 175) = 19%. Adyen's documentation says the same in words: "The optimal blocking threshold ... depends on your business model and the difference in cost between a fraud case and a false decline." It recommends a low or medium threshold to thin-margin retailers and a high or very high one to sellers of digital goods, for whom "the cost of a false decline (potential loss of lifetime value) mostly outweighs the cost of a fraud case". The right threshold depends on your margins. The model does not know them.

A merchant can act on that price in four ways, each with more control and more cost.

| Configuration | What you control | What it costs you | When it is right |
| --- | --- | --- | --- |
| **Provider default** | Nothing: Stripe blocks its highest level, Adyen's premium tier blocks at High and above | A threshold set for nobody in particular | Low volume and no one to own fraud |
| **Your own threshold** | The cut-off: Radar's risk settings (Plus and Pro plans), Adyen's blocking threshold per risk profile | You must know your two costs | Margins far from average, in either direction |
| **Model plus rules and lists** | Conditions on what only you know (product, customer history), and lists of values to allow or block | Upkeep, and every allow rule overrides the model | You hold information the provider cannot see |
| **Plus manual review** | A person's decision on the uncertain middle | Staff time and delay; on Adyen up to seven days before capture | Orders large enough to repay a look |

Rules deserve the most care. A rule is your own condition evaluated on every payment, and its action is allow, block or, between the two, review by a person or a request for **3-D Secure** (asking the issuer to check who is paying). Stripe's example of that last action is `Request 3D Secure if :risk_level: != 'normal' and :amount_in_usd: > 25`. Rules are explainable and they are yours, but apart from the provider's risk level they work on your own data. Their danger is the allow rule. Stripe: "Implement any allow rules minimally, because they override the Stripe default rules, along with any other custom rules that match the same criteria." Adyen: "**Allow** rules have the highest priority within a risk profile." One broad allow rule switches the model off for everything it matches. Stripe caps an account at "200 transaction rules and 100 account rules".

Test every change to a threshold or rule before and during rollout. Both providers document the tools. Stripe's rule tester "runs a simulation on the last 6 months of charges", and its traffic allocation applies a custom rule to a chosen percentage of matching payments; at 0% the rule is evaluated without acting, and "Radar assigns all attempts for the same transaction to the same allocation bucket, so each retry receives the same outcome as the original attempt." Adyen's premium tier lets you backtest custom rules and run experiments that "A/B test two risk profiles against each other" on "real transactions". A backtest and a control group are the only places a merchant can see what a rule refuses. And the verdict waits until the labels are in.

## Card Testing: Fraud That Leaves No Label

**Card testing** uses a merchant's checkout to find out which stolen or guessed card numbers work. Adyen's engineering post of October 2026 separates two forms: "verification, where bots iterate through lists of stolen credentials using low-amount transactions to identify active cards; and enumeration, where scripts systematically guess missing fields, such as CVVs or expiry dates, within specific BIN ranges" (a BIN is the first digits of a card number, which identify the issuing bank). The merchant is the tool and not the target. A validated card is worth money: Visa's release of May 2024, on its own data for fiscal year 2023, says "Thirty three percent of enumerated accounts experienced fraud within five days", and puts enumeration at "$1.1B annually in fraud losses".

A model trained on disputes is slow to see this, because no single attempt carries evidence. The Adyen post: "Unlike chargeback fraud ... card testing offers no explicit transaction-level signal." Attackers also hide from simple counters: "Rotational attacks: Fraudsters continuously rotate details—such as IP addresses—to stay well below baseline velocity thresholds." The evidence is in the shape of traffic over minutes. Adyen describes computing features over "subslices" of traffic, such as one range of card numbers at one merchant. A feature language is compiled to Apache Spark for training and to Apache Kafka and Flink for live scoring; "Flink writes these streaming metrics to an Apache Cassandra feature store, where the risk engine fetches the latest subslice values to make real-time block/allow decisions before sending transactions to the issuer." It is the only substantial description of one of its fraud models that I found from Adyen.

<!-- illustration-placeholder
{
  "id": "24-card-testing-traffic-shape",
  "status": "pending",
  "asset": "assets/images/24-fraud-and-risk-systems/24-card-testing-traffic-shape.jpeg",
  "aspect_ratio": "16:9",
  "placement": "after the paragraph that says the evidence of card testing is in the shape of traffic",
  "visual_goal": "Show that each card-testing payment looks ordinary on its own, while the same payments seen together as one slice of traffic over a few minutes are obviously an attack.",
  "prompt": "Create a two-panel conceptual illustration. The left panel is labeled \"One payment\" and shows a magnifying glass over a single small payment card with a tag reading \"€1\" and a green check mark beside it, looking harmless. The right panel is labeled \"One slice, ten minutes\" and shows a bar chart of payment counts over time: several low, even teal bars on the left, then a sudden tall cluster of orange bars on the right, with many tiny identical payment cards tagged \"€1\" raining onto the tall bars from a small generic robot figure. A dashed line across the chart is labeled \"Normal level\". A thick arrow labeled \"Same payments\" leads from the left panel to the right panel. Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people.",
  "alt": "Left: one harmless-looking one-euro payment under a magnifying glass. Right: a traffic chart where a sudden cluster of one-euro payments rises far above the normal level.",
  "caption": "Each €1 attempt looks ordinary on its own; the attack is visible only in the shape of one slice of traffic over minutes."
}
-->

It is tempting to let the issuers decline the attempts. But declined attempts still cost the merchant. Stripe's documentation lists the effects: extra fees, and "A high decline rate might damage the reputation of your business with card issuers and card networks, which makes all of your transactions appear riskier". The networks count them too. Visa's Acquirer Monitoring Program fact sheet (2025) defines an enumeration ratio as "[Count of Enumerated Authorization Transactions (Approved + Declined)] ÷ [Count of Authorization Transactions (Approved+ Declined)]", with thresholds of 2,000 basis points (20%) and 300,000 enumerated transactions in a month, and says the program "requires acquirers to take proactive steps to prevent merchants from exceeding enumeration thresholds". An acquirer is the licensed party that connects a merchant to the network ([[acquiring-and-network-connectivity]]). A decline at the issuer comes too late.

So card testing has to be stopped before authorization, in two layers. The first is yours: limits in front of any endpoint that can start a payment. Stripe warns that "simple firewall rules or filters based on a single heuristic such as IP addresses are usually not sufficient" and recommends CAPTCHA, a login before the payment form, and rate limits. The second is the provider's blocking before the network. Stripe includes card-testing prevention in every Radar plan. Adyen's "Machine learning: bot attack risk" rule, in its basic tier, "detects and blocks transactions that come in at an unusually fast rate with suspicious payment properties ... This rule mostly prevents large scale attacks". Both publish results. Stripe (May 2025): "While attacks are up industry-wide, they are down 80% on Stripe." Adyen (October 2026): "increasing blocked card testing attacks by 28% on average, with zero impact on legitimate shoppers". These are vendor claims with no baseline, period or method, and they cannot be compared.

## Risk Beyond the Payment: When the Merchant Is the Risk

The same structure, an estimate now and the facts later, applies to the business being paid. A provider pays a merchant days after a sale, while customers can dispute for months. If the merchant has vanished by then, the provider is left with the loss. This is its **credit exposure** to that account. Stripe's October 2026 engineering post on risk assessment lists the questions it asks: "Is the business trustworthy? ... Has this business become suddenly popular, or is it under attack? Should we adjust a business' credit reserves?" (a reserve is part of a merchant's sales held back). To platforms Stripe exposes an account risk score that "correlates to the probability that an account would cause losses to your platform". Adyen documents a held amount it calls the deposit: "Adyen calculates the deposit requirement for your account daily, based on variables such as your processing volume and the number of chargebacks and refunds". If exposure exceeds coverage "by more than **EUR10,000**, then Adyen automatically withholds funds from your next payout".

Adyen's deposit page describes the calculation in outline: exposure (orders paid but not yet delivered, plus chargebacks and refunds predicted from "the past 180 days of data") is set against coverage (the merchant's balances and funds or instruments held by Adyen), and the risk Adyen accepts for a merchant is "determined on a case-by-case basis". It gives no numbers behind those terms. Stripe's support site names the factors behind a reserve ("industry conditions, payment activity, dispute rate, refund rate, and financial stability") and gives no formula or amounts. Each company lists the businesses it prohibits; neither publishes the credit criteria or models by which it accepts a merchant. What a platform needs to know is who is left with a seller's loss. Stripe's documentation says "responsibility for your connected accounts' negative balances can belong to your platform or to Stripe". Under Larkfield's terms a studio carries a lost dispute, and if its balance cannot cover it, the loss falls on Larkfield. [[payment-compliance-and-regulation]] picks up what a provider must know about the businesses it pays, and [[platform-payment-models]] who carries their losses.

## Stripe and Adyen: Where They Differ

The table sets side by side facts already cited in this chapter, all from documentation accessed in November 2026 unless a year is given. The last column is my inference.

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Decision before the network | A risk block is recorded as `not_sent_to_network`; built-in rules can also block after the issuer approves | Risk rules run pre-authorization or post-authorization; blocking before "saves issuer and scheme fees" | No material difference in placement; Adyen states the timing as a property of each rule |
| Exposed score and default block | 0–99; elevated from 65, high from 75; highest level blocked; the number only on Plus and Pro plans; the block rule on this score is being deprecated in favor of risk settings | Five levels, Very Low to Very High; default block at "high risk and above" (premium) | Stripe offers a finer dial; neither documents how a score or level maps to a percentage |
| Holdout | Score modified for "a small subset of payments" | "Control traffic", settled regardless of risk; excludes EUR 2000 and above | Probably the same device (for Stripe that is my reading of one sentence); Adyen documents its limits |
| Testing a change | Simulation on the last 6 months of charges; per-rule traffic allocation, including 0% | Backtest of custom rules; live A/B experiment between two risk profiles (premium) | Stripe tests rule by rule, Adyen profile against profile |
| Card-testing control | In every Radar plan; merchant guidance published | Bot-attack rule in the basic tier, no configuration; engineering description (October 2026) | Stripe tells you what to add yourself; Adyen tells you how its model works |
| Published model detail | Lineage to a neural-network-only model (2023); Shield's training-set size and the label delay (October 2026) | Bot-attack feature pipeline (October 2026); fraud-risk model: tree-based ensembles, weekly retraining by default (2024) | The models cannot be compared, only what each chose to publish |
| Published latency | "less than 100 milliseconds" (2023) | 20 ms median per model endpoint (2025); whole decision not published | The figures measure different things |

On Stripe, read the outcome of every payment (level, reason, whether it was sent to the network), and use the rule tester and traffic allocation before a rule acts. On Adyen, decide for each rule whether it should run before or after authorization, check which features need the premium tier, and use control traffic and experiments to measure.

The blanks in the table are gaps in the public record, not differences in practice. As of 17 November 2026 I found nothing in either company's documentation, help center, site or engineering posts on:

- Adyen's fraud-risk model beyond its family and weekly retraining: its size and training data.
- Merchant underwriting at either company: credit criteria and models, and the amounts behind Stripe's named reserve factors and Adyen's deposit calculation.
- The size of the Shield model now in production: the 30 million parameters belong to a version that was rolled back.
- How often Radar is retrained now: daily in 2019; the 2026 post says "regular retraining" and no more.
- A latency figure for Adyen's whole risk decision.
- What either system does when the evaluation is slow.
- How the payments foundation model Stripe announced in May 2025, which it says it uses against card testing, relates to Shield, which its October 2026 engineering post describes without mentioning it.

## In Practice at Larkfield: Closing the Open Till and Pricing Two Thresholds

Larkfield's answer to the weekend was not a stricter fraud model. It put three limits in front of the public booking widget. A guest who pays without logging in must pass a CAPTCHA. The payment service, through which decision K1 of the Keel program sends every money-moving call, caps payment attempts per studio at a multiple of that studio's busiest recorded hour. And an alert fires when a studio's declined and blocked attempts in ten minutes exceed its usual hourly total. The providers' own blocking before the network stays on. These are the two layers of the previous section, placed where Larkfield owns the endpoint.

Then Femke prices the threshold, per product. A studio's class seat costs almost nothing extra to provide, so a fraud case costs the studio the €15.00 dispute fee *(illustrative)* and little else. A refused customer costs far more for some products than others. Assume a new member stays eight months, worth 8 × €49 = €392 *(assumption)*. For a first membership payment the break-even is 392 ÷ (392 + 15) = **96%**. For a €16 guest drop-in it is 16 ÷ (16 + 15) = **52%**. One studio and one model need two thresholds, because a refused member costs more than twenty times a refused guest. The arithmetic has a limit, which the last section returns to: card networks cap dispute rates whatever a dispute costs you.

In March 2027 Jonas proposes a rule for the studios on Stripe, `Block if :risk_level: = 'elevated'`, and points to a two-week trial on a few studios in which disputes fell. (On Stripe Connect, Stripe's product for platforms, whose Radar rules apply to a payment, the platform's or the studio's connected account's, depends on the charge type; see [[platform-payment-models]].) Femke asks for the two things that result cannot show. Most disputes on those payments have not been filed yet, and nobody has counted the good members the rule refused. So the rule runs at 0% traffic allocation, where Stripe evaluates it without acting, and goes through the simulation on six months of charges. Any verdict is set for sixty days after rollout, when Stripe's curve says about 86% of fraud disputes are in. On the Adyen studios the threshold stays at the default, and control traffic supplies the comparison.

## When It Goes Wrong

The rarest failure is documented: the evaluation itself does not run. Stripe's documentation says "In unusual cases, an error might cause risk evaluation to fail. If this happens, Stripe reports the payment as having unknown risk", and the example outcome carries `"reason": "unknown_risk_level"` with `"type": "authorized"`. The payment went through unjudged. Count those outcomes and review them; do not read the absence of a block as a pass. Adyen documents no equivalent state, so on Adyen there is nothing to count.

The second failure you configure yourself. A broad allow rule or a stale entry on an allow list turns the model off for whatever it matches. Stripe's documentation warns that "Allowlists can allow fraudsters to operate without restrictions and bypass controls", and limits entries on its default fingerprint allow lists to "a maximum lifespan of 30 days". A related fault is a rule that answers a retry differently from the first attempt, which Stripe's pinning of retries to one allocation bucket prevents. Review allow rules and lists on a calendar, with an owner.

The commonest failure raises no error. A threshold or rule that refuses good customers shows up only as sales that did not happen. The detectors are the ones this chapter has named: the holdout or control group, and the count of payments each rule blocked. The opposite mistake surfaces months later. Visa's monitoring program counts fraud reports and disputes against settled transactions, and its fact sheet says the "Excessive Merchant threshold reduced to >=150bps" (1.5%) in the EU, the US, Canada and Asia-Pacific on 1 April 2026. Watch the dispute rate by the month the payments were made, and read a month only after sixty days.

## What to Take Away

**Established.**

- Both providers decide before the card network sees a payment and again after the issuer answers; a risk block never reaches the bank (Stripe and Adyen documentation, accessed November 2026).
- The score estimates a later fraud dispute. It is not a finding, and neither company documents how a score or level maps to a percentage.
- Labels are late and incomplete: 41% of fraud disputes by day 14 and 86% by day 60 (Stripe, October 2026), and none for blocked payments, which is why Adyen documents a holdout and Stripe appears to run one.
- The merchant is responsible for what it accepts (Stripe documentation), and card testing is counted against it even when the attempts are declined (Visa fact sheet, 2025).

**Depends on context.**

- Where to set the threshold: high when a refused customer costs much more than a fraud case (memberships, digital goods), low when goods are costly and margins thin.
- Whether rules and manual review repay their cost: only if you know something the provider cannot see, or orders are large enough for a person to look.
- Which limits an endpoint needs: a logged-in checkout needs less than a public form that can start a payment.
- Whether you can test a change: a small merchant cannot measure a rule's effect and should stay close to the defaults.

**The author's synthesis.**

- Every risk decision is made before its evidence exists. A risk product moves the decision to the provider and leaves the price with me, so I own the threshold, the control-group measurement and the endpoint limits myself.
- I date every verdict on a model or rule sixty days out. The €1 payment at 03:14 could not be known to be fraud by anyone in its path; what could be known was the shape of the traffic around it, and the control that mattered was a limit on the endpoint.

## Questions to Ask

1. For each product we sell, what does a refused good customer cost and what does a fraud case cost, and what break-even chance of fraud follows?
2. Which threshold is in force on each provider today, who set it, and was it ever changed from the default?
3. How many payments did each rule block last month, and how do we estimate how many of them were good customers?
4. Does our provider keep a holdout or control group, and can we see its results?
5. When we change a rule or threshold, on what date do we judge it, and is that at least sixty days after rollout?
6. Which of our endpoints can start a payment without a login, and what limit sits in front of each?
7. Which allow rules and allow-list entries exist, who owns them, and when were they last reviewed?
8. What does our integration record when the provider blocks a payment or returns an unknown risk level?

Between allow and block a risk rule has a third course, "request 3-D Secure", and on every payment allowed without it the merchant carries the fraud loss. [[three-d-secure-and-sca]] takes up what that request is: handing the question of who is paying to the issuer, and the conditions under which the issuer then takes the loss as well.

## Sources and Evidence

*Company, product and investor sources*

- [Transaction risk prevention](https://docs.stripe.com/radar/transaction-risk-prevention), Stripe documentation, n.d., accessed 2026-11 — blocked-payment outcome, score range and thresholds, the holdout, unknown risk, merchant feedback, responsibility for accepted payments.
- [Fraud prevention rules](https://docs.stripe.com/radar/rules), Stripe documentation, n.d., accessed 2026-11 — built-in rules, rule actions and precedence, rule limits, the six-month simulation, traffic allocation.
- [Risk setting and risk controls](https://docs.stripe.com/radar/risk-settings), Stripe documentation, n.d., accessed 2026-11 — the risk score described as a probability, the deprecation of the block rule built on it, the separate scores.
- [Review payments](https://docs.stripe.com/radar/transaction-reviews), Stripe documentation, n.d., accessed 2026-11 — review happens after processing.
- [Lists](https://docs.stripe.com/radar/lists), Stripe documentation, n.d., accessed 2026-11 — allow and block lists, the 30-day limit on entries in the default fingerprint allow lists.
- [How Radar works](https://docs.stripe.com/radar/how-radar-works), Stripe documentation, n.d., accessed 2026-11 — the four plans and which features each includes.
- [Protect yourself from card testing](https://docs.stripe.com/disputes/prevention/card-testing), Stripe documentation, n.d., accessed 2026-11 — consequences, symptoms, recommended controls, signal impact.
- [Advanced fraud detection](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection), Stripe documentation, n.d., accessed 2026-11 — the device and activity signals Stripe's JavaScript library collects.
- [Common types of online fraud](https://docs.stripe.com/disputes/prevention/fraud-types), Stripe documentation, n.d., accessed 2026-11 — definitions of fraud, card testing, friendly fraud and marketplace fraud.
- [Account fraud prevention](https://docs.stripe.com/radar/account-fraud-prevention), Stripe documentation, n.d., accessed 2026-11 — account risk score for platforms.
- [Use Radar with Connect](https://docs.stripe.com/connect/radar), Stripe documentation, n.d., accessed 2026-11 — which account's Radar rules apply to direct and transferred charges.
- [Risk and liability management with Connect](https://docs.stripe.com/connect/risk-management), Stripe documentation, n.d., accessed 2026-11 — who is responsible for connected accounts' negative balances.
- [How we built it: Stripe Radar](https://stripe.dev/blog/how-we-built-it-stripe-radar), Ryan Drapeau, Stripe, 2023-03-29 — model lineage, "less than 100 milliseconds", the 0.1% figure (evidence age: 3.6 years).
- [Shepherd: How Stripe adapted Chronon to scale ML feature development](https://stripe.dev/blog/shepherd-how-stripe-adapted-chronon-to-scale-ml-feature-development), Ben Mears, Stripe, 2024-04-15 — feature retrieval as part of payment latency.
- [Scaling Radar: Fighting fraud with agent-assisted machine learning](https://stripe.dev/blog/scaling-radar-fighting-fraud-with-agent-assisted-machine-learning), Ryan Drapeau and Sai Samant, Stripe, 2026-10-19 — the label-delay curve, the rollback of the larger model, Shield's training set, network signals.
- [Fine-tuning LLMs for risk assessment](https://stripe.dev/blog/training-llms-for-risk-assessment), Hangzhi Guo and others, Stripe, 2026-10-09 — the list of risk decisions about businesses.
- [Counterfactual Evaluation of Machine Learning Models](https://www.infoq.com/presentations/stripe-ml-models-fraud), Michael Manapat, Stripe, talk at QCon.ai, transcript published 2018-05-10 — letting through a random fraction of blocked payments (evidence age: 8 years).
- [Railyard: how we rapidly train machine learning models with Kubernetes](https://stripe.com/blog/railyard-training-models), Rob Story, Stripe, 2019-05-07 — daily retraining of Radar's models (evidence age: 7 years).
- [Reserves: Frequently asked questions](https://support.stripe.com/questions/reserves-frequently-asked-questions), Stripe support, n.d., accessed 2026-11 — reserve factors.
- [Prohibited and Restricted Businesses](https://stripe.com/legal/restricted-businesses), Stripe, last updated 2026-09-22 — businesses Stripe refuses.
- [Using AI to optimize payments performance with the Payments Intelligence Suite](https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite), Stripe, 2025-05-15 — the card-testing claim and the foundation-model announcement (vendor claim).
- [Risk management](https://docs.adyen.com/risk-management), Adyen documentation, n.d., accessed 2026-11 — basic and premium tiers, cross-channel signal.
- [Configure your risk profile](https://docs.adyen.com/risk-management/configure-your-risk-profile), Adyen documentation, n.d., accessed 2026-11 — pre- and post-authorization rules, actions, precedence of allow rules.
- [Machine learning rules](https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules), Adyen documentation, n.d., accessed 2026-11 — risk levels, default threshold, threshold guidance, the bot-attack rule.
- [Control traffic](https://docs.adyen.com/risk-management/control-traffic), Adyen documentation, n.d., accessed 2026-11 — the holdout and its exclusions.
- [Case management](https://docs.adyen.com/risk-management/case-management), Adyen documentation, n.d., accessed 2026-11 — the seven-day review window.
- [Run A/B test experiments](https://docs.adyen.com/risk-management/run-ab-test-experiments), Adyen documentation, n.d., accessed 2026-11 — live experiments between two risk profiles.
- [Data collection to detect fraud](https://docs.adyen.com/risk-management/fraud-data-collection), Adyen documentation, n.d., accessed 2026-11 — client-side collection of interaction data.
- [Deposit](https://docs.adyen.com/account/balances/deposit), Adyen documentation, n.d., accessed 2026-11 — daily deposit requirement, the outline of the exposure and coverage calculation, the EUR 10,000 exposure rule.
- [How Adyen does AI](https://www.adyen.com/knowledge-hub/how-adyen-does-ai), Andreu Mora, Adyen, 2024-08-16 — tree-based fraud models, weekly retraining (evidence age: 2 years).
- [The AI behind Uplift](https://www.adyen.com/knowledge-hub/the-ai-behind-uplift), Andreu Mora, Adyen, 2025-01-17 — model-serving latency.
- [Payment fraud: What is it and how to protect your business](https://www.adyen.com/knowledge-hub/payment-fraud), Adyen, 2025-12-08 — account takeover defined.
- [Prohibited and Restricted Products and Services](https://www.adyen.com/legal/list-restricted-prohibited), Adyen, last updated 2025-11-13 — businesses Adyen refuses.
- [Catching card testing at scale with real-time features](https://www.adyen.com/knowledge-hub/catching-card-testing-at-scale), Jaap Stefels, Adyen, 2026-10-04 — verification and enumeration, absence of labels, subslice features, the streaming pipeline, the 28% claim.

*Standards, regulation and official documentation*

- [2025 Report on payment fraud](https://www.ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf), European Banking Authority and European Central Bank (EBA/REP/2025/40), 2025-12 — EEA card fraud rates for 2024, remote against non-remote, share from theft of card details.
- [Visa Acquirer Monitoring Program Overview](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf), Visa fact sheet, 2025 — enumeration ratio and thresholds, the 150 basis-point merchant threshold from 1 April 2026.
- [Visa Announces Generative AI-Powered Fraud Solution to Combat Account Attacks](https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20661.html), Visa press release, 2024-05-07 — enumeration losses and the five-day figure (Visa's own data for fiscal year 2023).

*Research and practitioner sources*

- None.

Larkfield is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
