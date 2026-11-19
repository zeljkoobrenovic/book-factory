---
title: "Outcomes Over Output"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Why do organizations that ship a great deal still fail their customers? Because they measure themselves by what they ship. The alternative is a result the customer wants, stated in the customer’s terms, with a business result that follows from it."
permalink: outcomes-over-output
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to name the dysfunction of a product organization that counts what it ships, and to restate its goals as customer outcomes with a measure.

> **KEY POINTS:**
>
> * **A busy product organization can be moving its customers nowhere.** When shipping is what gets counted, shipping becomes the goal, and *Build What Matters* lists ten recurring ways in which that fails.
> * **Aim at a key customer outcome, then a key business outcome.** The first is the result the customer wants, in the customer's own terms. The second follows from it, and chasing it first extracts value that was never delivered.
> * **An outcome can be managed by, not only declared.** Rewrite each goal as an outcome with a measure, break the outcome into drivers that move within a quarter, and review shipped work against the driver it was meant to move.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Feature Factory** — a roadmap of requested features gives a team nothing to judge a feature by except its date.
> * **The Output Scoreboard** — an organization that praises what shipped gets more shipped, whatever it does for customers.

<br>

Corvane, the fictional company this book follows, sells scheduling and dispatch software to field-service companies, which pay per technician per month. In 2024, at 180 people, it shipped forty-one features. Each one had been promised to a customer by name, and thirty-eight shipped on the promised date. Over the same year the share of customers who renewed fell from 93 percent to 87.

You have probably delivered a roadmap in full, been thanked for it, and seen nothing change for the customers it was built for. This chapter is about that experience. Its claim is that organizations which ship a great deal still fail their customers when they **measure themselves by what they ship**, and that what they should aim at instead is a **key customer outcome**, the result the customer wants in the customer's own terms, paired with a **key business outcome** that follows from it. The chapter starts with Corvane's year, explains why output becomes the goal, and sets out the ten dysfunctions of product management that *Build What Matters* lists, with their three themes. It then defines the two outcomes and gives three patterns: rewrite the goal, break the outcome into drivers, and review shipped work. It follows Corvane through the next year, says where the sources disagree and how the remedy fails, and ends with what AI changes.

## Setting the Scene: Forty-One Features and a Falling Renewal Rate

Corvane's roadmap for 2024 was a list. Each row held a feature, the customer it had been promised to and a date. Rows were added by sales and account managers, during a deal or a renewal conversation, and the forty-one features of that year had been promised to twenty-three customers, most of them large. Each of the eleven product teams took its rows at the start of a quarter and built them. By the list's own measure the year went well: thirty-eight of the forty-one shipped by the promised date, and the teams were praised for it.

The customers answered differently. The renewal rate, the share of customers due for renewal who renewed, fell from 93 percent in 2023 to 87 percent in 2024. Six of the twenty-three customers who had been promised a feature, and had received it, did not renew. Inside Corvane the explanation was that customers needed more features and needed them faster, and the list for 2025 began to grow.

At the end of 2024 Priya Nambiar, Corvane's first product manager and by then the most senior of its eleven, counted something the roadmap had never recorded: which customers used each of the forty-one features.

| Who used the feature at the end of 2024 | Features |
| --- | --- |
| Only the customer that had asked for it | 26 |
| Two to ten customers | 11 |
| More than ten customers | 4 |

## Why Output Becomes the Goal

Nobody at Corvane had decided to build twenty-six features for one customer each, and two words are needed to say how it happened. For a product, **output** is what the organization ships: a feature, a release, an integration. An **outcome** is a change in what the customer gets done. Chapter 2, [[the-organization-as-a-product]], used the same two words for a change to the organization itself: there the users were teams, and the output was a finished reorganization. In this chapter the object is the product and the user is the customer, so the output is a shipped feature and the outcome is something the customer can now do.

Output replaces outcome as the goal because of what it is like as a measure. It is easy to count, and it is under the team's control: a team can promise a date and keep it by its own effort. Whether a customer's work changes depends on the customer and shows later. A weekly review asks for what can be answered that week, so it asks what shipped, and what is asked about every week becomes what people aim at. Nobody has to prefer output to outcome for this to happen. Melissa Perri names the end state in *Escaping the Build Trap*: "The build trap is when organizations become stuck measuring their success by outputs rather than outcomes." The name is hers; the account of how a measure turns into a goal is my reasoning.

At Corvane the trap took a particular form, the sales-led company. In *Build What Matters*, Ben Foster and Rajesh Nerlikar contrast two kinds of company. A product-driven company meets a customer's need with a solution that fits a wider market. A sales- or services-driven company builds for one customer at a time. They put the difference in one sentence: "While a sales- or services-driven company succeeds by saying yes to a specific customer, a product-driven company often succeeds by saying no." Perri describes the same condition: "Sales-led companies let their contracts define their product strategy." Each yes at Corvane was reasonable for the person who gave it. An account manager facing a renewal was offered a way to keep the customer, and nothing on the roadmap gave a reason to refuse.

## Ten Dysfunctions, Three Themes

The build trap and the sales-led company are two entries in a longer catalogue: Foster and Nerlikar list ten dysfunctions of product management, and as I read their list the build trap is its Hamster Wheel and the sales-led company its Feature Factory. In the table, the names and the short descriptions are theirs, taken from their self-assessment list. The sign to look for is mine, and so is the theme number in the last column, which the paragraph after the table explains.

| Dysfunction | Their description | A sign you can see | Theme |
| --- | --- | --- | --- |
| The Hamster Wheel | Output over outcomes | Reviews ask whether it shipped on time, and nothing else | 2 |
| The Counting House | Obsession with internal metrics | The dashboard shows revenue and active users, and nothing a customer would recognize | 1 |
| The Ivory Tower | Lack of customer research | Nobody on the team has talked to a customer this quarter | 1 |
| The Science Lab | Optimization to the exclusion of everything else | Many small tests, no new capability | 3 |
| The Feature Factory | An assembly line of features | The roadmap is a list of requests, each with a requester | 2 |
| The Business School | Overdependence on data and spreadsheets | Priorities come from a scoring model nobody believes | 1 |
| The Roller Coaster | Fast-paced twists and turns | Priorities change before anything can show a result | 3 |
| The Bridge to Nowhere | Overengineering for future unknowns | Work on needs no customer has yet | 1 |
| The Negotiating Table | Trying to keep everyone happy | Every stakeholder gets something each quarter | 2 |
| The Throne Room | Whipsaw decision-making from the person in charge | The plan changes after the founder visits a customer | 2 |

The authors reduce the ten to three themes. In the first, an internal focus draws attention away from delivering value to customers. In the second, the product team is so busy answering requests and complaints, which the authors call playing defense, or has so little authority, that no time is left for new ideas. In the third, a wish for short-term, directly measurable business results lets only superficial changes through. My notes on the book do not record which dysfunction the authors place under which theme, so the numbers in the table's last column are my assignment and not theirs. The themes are more useful than the names, because each points at a different repair: where attention goes, who has authority, and how far ahead results are expected.

The three themes say what kind of repair an organization needs. To pick the entry among the ten that fits one organization, ask two questions: **what decides what gets built**, and **what counts there as success**. If requests decide and shipping counts, it is the Feature Factory. If the date counts, whoever decided, it is the Hamster Wheel. If an internal number counts, it is the Counting House. If the person in charge decides, it is the Throne Room, and if whoever objects decides, the Negotiating Table. At Corvane a customer's request decided and the ship date counted: a Feature Factory run on a Hamster Wheel. The two failure patterns of this book that the chapter addresses are those two again. This book's Feature Factory is theirs, read as a question of who decides what gets built, and the Output Scoreboard is the Hamster Wheel turned into what the organization rewards.

## What to Aim At: A Key Customer Outcome, Then a Key Business Outcome

All ten dysfunctions aim at the wrong thing, and Foster and Nerlikar's remedy starts by naming the right one. A **key customer outcome** is the result the customer wants from the product, stated in the customer's own terms. They call it the "metric of progress", the way to know whether the product is delivering value. Priya Nambiar found Corvane's by asking one question of planners, the people who schedule the technicians, at customers that had left: what had they bought Corvane for? None of them named a feature. They wanted the technician to arrive in the time window promised to the end customer, the household or business being visited, and to finish the job on that visit. Corvane's key customer outcome became **jobs completed on the first visit, inside the promised window**. Its measure is the share of a customer's jobs that meet both conditions, which Corvane can compute from job data it already holds. At the end of 2024 the median customer stood at 71 percent.

The **key business outcome** is the one business result the leadership agrees to optimize for, and it comes second for a reason. Foster and Nerlikar sort product work into two kinds: work that delivers value to customers, and work that extracts value for the company from value already delivered, such as a price increase or a shorter free trial. Extraction has nothing to draw on unless delivery came first. In their words, "providing customer value is what creates the opportunity to produce sustainable financial outcomes for the company, not the other way around." They also say why companies reverse the order: a company's own results are easier to measure than the value its customers get, and many companies do not notice that there is a trade-off. Corvane's key business outcome is the renewal rate, and its own data showed the order. In 2024, customers with more than 80 percent of jobs done on the first visit inside the window renewed at 97 percent. Customers below 60 percent renewed at 72 percent.

Both outcomes need a measure, and not every number qualifies. A **vanity metric** is a number that measures the company's activity and can rise while no customer is better off. Three questions separate it from an outcome metric. They come from my working checklist on the key-outcomes chapter of *Build What Matters*, a list of questions I drew from the book for my own use, so the wording is mine and the ideas are the authors', and the Counting House is the authors' name for failing them.

| Question | A metric that passes | A metric that fails |
| --- | --- | --- |
| Whose result does it measure? | Jobs done on the first visit (the customer's) | Monthly active users (the company's) |
| Would it still matter if the product were redesigned? | Jobs done inside the promised window | Clicks on the schedule board |
| Would a customer pay, renew or switch for it? | Fewer second visits | Number of features adopted |

## Pattern: Rewrite the Goal as an Outcome

A key outcome for the company still leaves each team with a goal of its own, and the first pattern restates that goal. It is for the leader who sets a team's goal and for the team that receives it. Take the output goal and ask: so that who can do what? Repeat the question until the answer is in the customer's terms and no longer names the feature. Then write the goal in six parts: the customer, what that customer can do afterwards, one measure, its value today, a target and a date. The six-part form is mine, built on the authors' key outcome. You can tell that the pattern is working by the share of a quarter's team goals that have all six parts.

Three of the rows still open on Corvane's list, all due in 2025, show the rewrite. The left column is the row as it stood at the end of 2024, and the targets on the right are for the end of 2025.

| Output goal on the roadmap | The goal rewritten | Measure: value at the end of 2024 → target |
| --- | --- | --- |
| Bulk reassignment of jobs, for a telecom installer, by April 30 | Planners replan a disrupted day inside Corvane | Disrupted jobs reassigned in the product within 15 minutes: 34% → 70% |
| Stock connector, for a heating company, by June | Technicians arrive with the part they need | Jobs that need a second visit for a missing part: 14% → 7% |
| SMS notification to end customers, by the second quarter | Someone is at home when the technician arrives | Visits with nobody home: 9% → 5% |

None of the rewritten goals names a feature, and that changes what can be asked. Bulk reassignment may or may not be the best way to get a disrupted day replanned within fifteen minutes. Under the output goal that question could not come up, because the feature was the goal. Under the outcome goal the feature is one candidate among several, and it can be judged by what it does to the measure. Who chooses among the candidates is the subject of [[discovery-delivery-and-empowered-teams]].

## Pattern: Break the Outcome into Drivers

The strongest objection to goals like these is that outcomes are too slow and too indirect to manage by. It is right about the two numbers at the top. A renewal rate moves once a year, and sales, pricing and the market move it too. A team cannot be steered by a number that arrives after its work is done and that it shares with half the company. If the two key outcomes were the only alternative to counting features, counting features would be the practical choice.

The second pattern answers the objection, and it is for the product leaders who set team goals. An **outcome pyramid** puts the key outcome at the top and, below it, the **drivers** that produce it. A driver is a narrower result that a team's work can move within weeks, and its measure is a **leading indicator**: a number that moves before the outcome above it does. Each driver also names the business outcome expected to follow, so that no driver is pursued without a reason the company can state. The device is recorded in my checklist on the authors' key-outcomes chapter; in the book they speak of breaking the key customer outcome down into specific areas of value creation. The pattern's measure is the share of team goals and roadmap items that name the driver they are meant to move. Corvane's pyramid had three drivers, the three rewritten goals of the previous section, and each named the same business outcome, the renewal rate.

---begin mermaid---
flowchart BT
    D1["Driver: the plan survives the day (disrupted jobs replanned within 15 minutes)"] --> C["Key customer outcome: jobs done on the first visit, inside the promised window"]
    D2["Driver: the technician has the part (second visits for a missing part)"] --> C
    D3["Driver: someone is at home (visits with nobody home)"] --> C
    C --> B["Key business outcome: renewal rate"]
---end mermaid---

**Figure 1:** *Corvane's outcome pyramid: teams move the drivers within a quarter, the drivers move the key customer outcome, and the business outcome follows.*

The pyramid adds a level between output and the key outcomes, so there are four kinds of measure to compare. They differ in how soon they move, who controls them and what they can tell you. The driver moves nearly as soon as output does and says far more, which is why it is the level at which a team can be managed. The comparison is mine.

| Measure | How soon it moves | Who controls it | What it tells you |
| --- | --- | --- | --- |
| Output count (features shipped) | Days | The team | That work was done |
| Driver (leading indicator) | Weeks | Mostly the team | Whether the work changed what customers do |
| Key customer outcome | Quarters | The product organization | Whether customers get the result they came for |
| Key business outcome | A year | The whole company, and the market | Whether the result was worth paying for |

## Pattern: Review Shipped Work Against Its Outcome

A driver named in a goal says what shipped work was meant to move, and some shipped work will not move it. A shipped feature that moved nothing is a cost. This is my judgment and not a finding from a source. Every feature in a product has to be tested, supported and explained at every later release, and it makes the product harder to use for everyone it was not built for. An organization that counts features records the unused one as an achievement, while it goes on paying for it.

The third pattern, the **outcome review**, finds that cost and decides what to do about it. It is for the leader who reviews a team's work. Its date is set when the goal is set, usually one or two quarters after release. It asks two things: what the driver's measure was before and after, and who uses what was shipped. It ends in one of three decisions: keep the work, change it, or remove it. The review is my recommendation; my checklist on *Build What Matters* holds the idea as one line, to review whether shipped work created customer value. The pattern's measure is the share of shipped items reviewed on the date set, together with the number changed or removed as a result.

## Worked Example: Corvane's 2025, Planned by Outcome

Corvane ran its next year on the three patterns. For 2025, as the company began to grow from 180 toward 500 people, Priya Nambiar put the key customer outcome, the three drivers and a review date for each in place of the list as the teams' goals; the roadmap shown to customers kept its form of features with dates until the middle of the year. Each product team's goal named a driver. Seventeen further promises, made during 2024 with dates in 2025, were still open at the end of 2024. Corvane kept the five that were written into contracts. For the other twelve, the three rewritten rows among them, it went back to the customer and said which driver it would work on instead.

A year later Corvane had shipped fewer than half as many features. The table gives each measure at the end of 2024 and at the end of 2025, with its target. Two drivers and the key customer outcome moved toward their targets without reaching them, the renewal rate rose, and one driver stayed where it was.

| Measure | End of 2024 | End of 2025 | Target |
| --- | --- | --- | --- |
| Features shipped in the year | 41 | 19 | None |
| Disrupted jobs replanned within 15 minutes | 34% | 61% | 70% |
| Second visits for a missing part | 14% | 9% | 7% |
| Visits with nobody home | 9% | 8% | 5% |
| Jobs done on the first visit inside the window, median customer | 71% | 78% | 85% by the end of 2026 |
| Renewal rate | 87% | 91% | None set |

The row that stayed where it was turned out to be the most useful one. The SMS notification, which the Notifications team had kept as its first solution, shipped on time in the second quarter of 2025. Under the old list it would have been a kept promise and the end of the matter. At its outcome review, visits with nobody home had gone from 9 percent to 8. The Notifications team kept its goal and reopened the solution. The reviews also went back over 2024: nine of the twenty-six features used by one customer only were removed in 2025, with those customers' agreement.

The better year still left one question open at Corvane. It had chosen three drivers out of many. It had chosen them from one round of conversations with customers who had left, at the end of a bad year, and other conversations would have produced other drivers. Nothing in the pyramid said why these three, or in what order.

## Where the Sources Disagree: Which Outcome Leads

Corvane led with a customer outcome, and one of this chapter's two main sources starts from the other side. In the passages of *Escaping the Build Trap* that I marked, Perri begins with the business. "Product-led companies optimize for their business outcomes, align their product strategy to these goals", she writes, and every feature and initiative should result in an outcome tied back to business value. Foster and Nerlikar warn against that focus. They hold that most internal metrics are trailing indicators of a product's success, numbers that move only after the success or failure has happened, and should not be the primary concern of product management, and the Counting House is their name for a team that forgets it. My notes on Perri are partial, and she too asks how a product delivers value to its customers. The difference is in where each account starts.

The two accounts are answering different questions, which is why the pyramid can follow both. Perri's rule says what every piece of work must connect to, and it guards against customer outcomes that nobody will pay for. Foster and Nerlikar's order says what to aim at first, and it guards against extracting value that was never delivered. So the pyramid **aims at the customer outcome and accounts in the business outcome**: its drivers serve the first, and each names the second. The resolution is mine, and it has a condition. Where a customer outcome has no path to a business outcome, the work is a gift, and it should be chosen as one, knowingly.

## Anti-Patterns: The Relabeled Feature and the Counted Click

Even with the order of the two outcomes right, the practice fails in two common ways, and both keep the vocabulary. The first is the relabeled feature. "Launch the customer portal" moves to a column headed Outcomes, with a date as its only measure, and nothing else changes. The test is simple: a goal that would be met by shipping, whether or not any customer's work changed, is an output goal. In my experience a whole roadmap can be converted this way in an afternoon. The Feature Factory and the Output Scoreboard stay in place under a new name.

The second is the counted click: a vanity metric adopted as the key outcome. It is the Counting House again, now with the word outcome on it. Active users rise, the team is praised, and no customer is better off. The three questions for an outcome metric catch it. Pushed hard enough it turns into extraction, with the product tuned to raise the number at the customer's expense.

## What AI Changes Here

Both anti-patterns count output under another name, and AI makes output cheaper to produce. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, in the teams I have observed using coding agents, a feature takes less engineering time to build than it did. Engineering time was the cost that limited a feature factory: a promise to one customer displaced other work, and somebody had to say so. Where that cost falls, the promise is easier to make and the list grows faster. This is my observation, not a measured result. The chapter makes no Proven claim; Part XI weighs the published evidence.

**Speculative.** If building a feature is cheap, building is no longer the scarce step. Establishing whether the feature moved its driver is. The outcome review, and not delivery, would then set the pace of a product organization. This follows from the argument of [[where-the-constraint-moves]]. It would be confirmed where organizations using agents report that features shipped per quarter rise while their customer outcome measures stay flat, and where work waits longer for its outcome review than it took to build.

## What to Take Away

**Established.** What the sources agree on:

- Success in product work is measured by outcomes and not outputs (Perri, *Escaping the Build Trap*; Foster and Nerlikar, *Build What Matters*).
- Output-driven product organizations fail in recurring ways that can be named, ten of them in *Build What Matters*.
- Customer value creates the opportunity for business value, and not the reverse (Foster and Nerlikar).

**Depends on context.** What changes with the situation:

- How far a company can refuse work for a single customer depends on its market and its contracts. Corvane kept five promises because they were contractual, and a company with forty customers cannot say no the way a company with four thousand can.
- How soon a driver can show movement depends on how often customers use the product. Daily scheduling shows a change in weeks; an annual process does not.

**The author's synthesis.** What is this book's own position:

- Every dysfunction lets something other than the customer's result decide what gets built or count as success. The three patterns put that result back in three places: the goal, the plan and the review.
- The two diagnostic questions, the assignment of the ten dysfunctions to the three themes, the six-part goal and the outcome review with its three decisions are mine, built on the sources.

## Checklist

Take the list of what your organization shipped last quarter, and its goals for the next one, and ask eight questions.

- [ ] What decides what gets built here, and what counts as success? Name the dysfunction.
- [ ] Can the leadership state the key customer outcome in words a customer would use?
- [ ] Does its measure pass the three questions: the customer's result, still meaningful after a redesign, worth paying for?
- [ ] Is there one key business outcome, and can you say how it follows from the customer outcome?
- [ ] Does each team goal name a customer, what they can do afterwards, a measure, its value today, a target and a date?
- [ ] Does each goal and roadmap item name the driver it is meant to move?
- [ ] For each item shipped last quarter: which driver was it meant to move, and what did that measure do?
- [ ] Is there a dated outcome review for what ships next, and has any review ever ended in "remove"?

Corvane shipped forty-one features in 2024, and you can now say what they were: output with no outcome above it, twenty-six of them used by one customer each. Making outcomes the unit of progress changed what Corvane counted. It left open which outcomes to pursue and in what order, a problem that an outcome cannot solve for itself. The solution is a view of where the customer should end up: a vision of the customer's future, and a strategy that works backward from it. Both are the subject of [[vision-and-product-strategy]].

## Sources and Evidence

**Books**

- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. The ten dysfunctions of product management and their three themes; product-driven and sales- or services-driven companies; the key customer outcome and the key business outcome; delivering and extracting value; internal metrics as trailing indicators. The assignment of dysfunctions to themes and the signs in the table are the author's.
- *Escaping the Build Trap*, Melissa Perri, 2018. The build trap; sales-led companies; business value as what every initiative ties back to.

**Practitioner sources**

- The author's working checklists on *Build What Matters*, which hold the outcome pyramid, the questions for an outcome metric and the review of shipped work: [[dysfunctions]] and [[outcomes]].
- The statements about coding agents under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
