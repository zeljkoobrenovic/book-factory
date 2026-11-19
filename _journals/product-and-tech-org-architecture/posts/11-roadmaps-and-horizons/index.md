---
title: "Roadmaps and Horizons"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What should a roadmap commit to, and how far ahead can it honestly look? It should commit to outcomes in an order and to a stated share of capacity, and it can name solutions and dates only as far ahead as the organization takes to learn whether a solution worked."
permalink: roadmaps-and-horizons
timetoread: 20 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn what a roadmap can commit to, how to balance it, and how far ahead it can name a solution and a date.

> **KEY POINTS:**
>
> * **A roadmap commits to outcomes in an order, and to a share of capacity.** The share is divided among innovation, iteration and operation, and it is decided before any item is ranked.
> * **Solutions and dates reach one learning cycle ahead.** Beyond the time the organization takes to learn whether a solution worked, a roadmap can honestly name outcomes, and further out only problems.
> * **One roadmap, with stated horizons, for every audience.** Customers, sales and the board get dates for the near horizon and direction beyond it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Feature Factory** — a roadmap of features with a requester and a date beside each is the factory's order book.
> * **The Output Scoreboard** — a roadmap judged by the share of dates kept counts delivery and says nothing about what changed for customers.

<br>

In 2024 Corvane, the fictional company this book follows, had 180 people and a roadmap of forty-one features. Each feature was promised to a customer by name, and each had a date. Corvane shipped all forty-one, thirty-eight of them by the promised date. Over the same year its **renewal rate fell**.

If you have defended a roadmap to sales, to a customer or to a board, you have been asked for features with dates a year out, and you have probably given them. The question of this chapter is what a roadmap can commit to without becoming false. My answer is that a roadmap should commit to **outcomes in an order** and to a **stated share of capacity**, and that it can name solutions and dates only one **learning cycle** ahead, which is the time the organization takes to find out whether a solution worked. The chapter starts with Corvane's roadmap and what it left unstated. It then says what a roadmap is for, how to balance it, and how the learning cycle gives it three horizons. After that it says what each horizon promises to each audience, answers the objection that customers and boards want dates, rewrites Corvane's roadmap, and ends with what AI changes.

## Setting the Scene: A Roadmap Delivered in Full

Corvane's 2024 roadmap was a list. Each row held a feature, the customer it was promised to and a date. Rows were added by sales or by account management during a deal or a renewal conversation, some of them a year before the date they carried. Four of the forty-one rows show the form.

| Feature | Promised to | Date |
| --- | --- | --- |
| Bulk job import from spreadsheets | A lift-maintenance company | March |
| Custom billing export format | A heating installer | June |
| Technician skills matrix | A telecom installer | September |
| Planner dashboard, version 2 | Three large customers | December |

By its own measure the roadmap was a success, and the falling renewal rate says that its own measure was the wrong one. The fault was in what the list stated. Nothing on it said what would change for a customer once a feature shipped. Nothing on it said how Corvane's capacity was divided among kinds of work. And nothing explained how a date set a year ahead could be known when it was written down. The next three sections take these three gaps in turn.

## What a Roadmap Is For

The first gap is about what an item on a roadmap should state, and that follows from what a roadmap is for. In *Build What Matters*, Ben Foster and Rajesh Nerlikar give it one job: a roadmap connects the near-term product changes to the mid-term strategic milestones and the long-term vision. It lets teams such as marketing and sales plan around the direction of the product, and it communicates the order of priorities. On that definition a roadmap holds the strategy of [[vision-and-product-strategy]] laid out in time. Its content is intended outcomes, in an order.

Corvane's roadmap had a different origin, and the difference has a name. In *Escaping the Build Trap*, Melissa Perri describes the sales-led company: "The product roadmap and direction were driven by what was promised to customers, without aligning back to the overall strategy." A roadmap assembled this way is a list of contracts. It is also the working document of the failure pattern this book calls **the Feature Factory**, in which a team receives features to build, each decided by whoever asked for it.

The remedy is to state each item as an **outcome**, and the feature becomes one candidate solution to it. Two terms need separating here, because the rest of the chapter uses both. A **problem** is what the customer cannot do today. An outcome is that problem solved to a measured degree: it adds the measure by which the problem will count as solved. The outcomes on a roadmap are narrower than the one key customer outcome of [[outcomes-over-output]]: each is a result of about the size of that chapter's drivers. That chapter gives the full method; the table applies it to three of Corvane's rows.

| As a feature | As an outcome | A measure |
| --- | --- | --- |
| Bulk job import from spreadsheets | A new customer's planners schedule their first real week soon after signing | Days from signing to the first week scheduled in Corvane |
| Custom billing export format | A completed job reaches the customer's invoice without anyone retyping it | Share of completed jobs invoiced without manual correction |
| Technician skills matrix | No job is assigned to a technician who is not qualified for it | Jobs reassigned for a missing qualification |

## Pattern: The Balanced Roadmap

Outcomes fill the first gap. The second was that nothing said how capacity is divided among kinds of work. Foster and Nerlikar sort all product development into three categories: innovation, which advances toward the vision; iteration, which improves what exists; and operation, which keeps the product and the business running. The first three columns of the table are theirs, and the fourth places Corvane's work of 2024.

| Category | What it is | Fed by | At Corvane in 2024 |
| --- | --- | --- | --- |
| Innovation | Progress against strategic milestones toward the vision | Vision and strategic planning | Nothing on the roadmap |
| Iteration | Better results from what is already built: minor improvements, new features, one-off requests, tests | Customer feedback and requests | The skills matrix, the custom export |
| Operation | Maintaining the product and running the business: architecture, performance, security, bug fixes, uptime | Bugs, internal tools, technical improvements | Release tooling, which was on no roadmap |

The pattern built on these categories is the **balanced roadmap**. Decide the share of capacity for each category top-down, before ranking any item, and then rank items only within their category. Foster and Nerlikar give "60 percent of our investment toward innovation, 30 percent toward iteration, and 10 percent toward operation" as an example of such a decision. The figures are their example and not a rule. The users of the pattern are the product leader and the executives who agree the split. Its outcome measure is whether the share actually spent each quarter matches the share stated.

Without a stated share, urgent and customer-specific work takes the whole roadmap. The cause is that items of different kinds cannot be compared. A step toward the vision, a customer's request and a security fix have no common scale, which the authors call comparing "apples to oranges to grapes". So each comparison is won by the item with the loudest sponsor, and they note that stakeholders with influence can have an outsized pull on priorities. At Corvane every row had a customer and a date behind it. Work on release tooling had neither, so the roadmap had no place for it.

The right share is not fixed. In my own working notes on the [[balanced-roadmap]] I tune it to the product's stage: a new product is mostly innovation, and a scaling one needs more operation. The share is revisited as the stage changes. The operation share in particular is reserved in advance. Foster and Nerlikar recommend setting a percentage aside for it and ranking technical debt, security holes and bugs against each other inside it, so that operation is not whatever is left. How the share is set inside budgeting and annual planning belongs to [[planning]], in Part VI.

## How Far Ahead: The Learning Cycle and Three Horizons

The third gap was how a date set a year ahead could be known, and the answer begins with an asymmetry. What an organization knows about a solution falls quickly with distance in time, while what it knows about the customer's problem holds. A solution depends on what the last release taught, on the technology, and on what customers do with the current product, and all of these change within months. The problem is different: a planner whose plan breaks when a technician calls in sick has the same problem next year. Both of this chapter's sources, *Build What Matters* and *Escaping the Build Trap*, treat needs as the stable part. Foster and Nerlikar ask, when setting a vision: "How do we build the right products based on the customer needs that are unlikely to change?" Perri gives strategy four levels, from vision down to solution options, and notes that each is on a different time horizon. Neither draws a limit from this.

To draw one, a unit is needed. I define a **learning cycle** as the time an organization takes from deciding to try a solution to knowing whether it moved the outcome. It is the sum of three parts: building and releasing the solution, reaching enough customers with it, and waiting for the measure to move and be read. You can estimate yours by adding the three for a typical item on your roadmap. An organization that builds and releases such an item in four weeks, whose customers take it up within two, and whose measure needs two more, has a learning cycle of about two months.

My position, which the sources do not state, is this: **a roadmap can honestly name solutions and dates only within one learning cycle.** The reason is in the definition. After one cycle the organization knows whether the first solution worked, and that result should decide what the next solution is. A solution written down today for the second cycle is chosen before the result that should choose it exists. It can be right only by luck or by ignoring the result.

The limit gives a roadmap three **horizons**, and what an item states gets less precise with each. The examples are from the roadmap Corvane wrote in 2025, shown in full later in the chapter.

| Horizon | Reaches | An item states | Example |
| --- | --- | --- | --- |
| Near | One learning cycle | The outcome, the solution and a date | "A customer whose appointment is moved hears it from Corvane first; a message with the new time, released in week 8 of the quarter" |
| Middle | The next two or three cycles | The outcome, its measure and its place in the order; no solution and no date | "When a technician is sick, the product proposes a repaired plan and the planner decides; measured by the share of proposals accepted unchanged" |
| Far | From there to the horizon of the vision | The problem, and roughly where it comes in the order | "A planner still builds each week's plan by hand" |

Items do not stay in their horizon. As cycles complete, each one moves from far to near and gains precision on the way, and each measured result changes what waits behind it.

---begin mermaid---
flowchart LR
    V["Vision and strategy"] --> F["Far: a problem"]
    F --> M["Middle: an outcome with a measure"]
    M --> N["Near: a solution with a date"]
    N --> R["Result measured"]
    R -->|"reorders and restates"| M
---end mermaid---

**Figure 1:** *An item enters the roadmap as a problem, becomes an outcome with a measure, and gets a solution and a date only when it enters the near horizon; each measured result reorders what waits behind it.*

A short near horizon does not mean a short roadmap. The limit shortens what a roadmap promises as solutions, and it does not shorten how far the roadmap looks. Looking only one cycle ahead is a failure of its own, which *Build What Matters* lists among its product dysfunctions as the Roller Coaster, a product pulled through fast twists and turns. The authors' diagnosis is that it "comes from setting a time horizon that is too short." Their rules of thumb are a three-year horizon for the vision by default, and a reassessment of roadmap and vision at each third or quarter of the horizon. The far horizon is where that long view lives, stated as problems.

Something can still be committed a year or more ahead. A roadmap carries three things, a share of capacity, an order of outcomes and solutions with dates, and they are three kinds of statement. The share of capacity is a decision. "A quarter of our capacity goes to operation this year" can be kept whatever the cycles teach, so it can be committed a year ahead. The order of outcomes is a judgement. It rests on the strategy and holds until a result contradicts it. A solution with a date is a prediction about what will have been learned, and it holds for one cycle. This reading is my synthesis of the balance and the limit.

## Pattern: One Roadmap with Stated Horizons

The horizons say what an item states, and the second pattern says what that amounts to as a promise. Publish one roadmap to every audience, with each horizon labeled by what it promises. The product leader publishes it, and its users are the people who read it: sales, customers and the board. The outcome measures are two: the share of near-horizon dates kept, and the number of dated promises that exist beyond the near horizon, which should be zero. These two measure only whether the roadmap keeps its one promise of delivery. Whether the work was worth doing is judged by each item's own outcome measure, and a roadmap judged by dates alone is the Output Scoreboard again.

| Horizon | What is promised | What a customer or a salesperson can do with it | What a board can do with it |
| --- | --- | --- | --- |
| Near | This solution, on this date | Plan a rollout and train staff | Check delivery against dates |
| Middle | This outcome, in this order, judged by this measure | Know what comes next, and argue about the order | Check that the order follows the strategy |
| Far | This problem is on the list | Know the direction of the product | Check the direction against the vision |

*Build What Matters* advises something different, and the difference should be visible. Its authors warn against letting salespeople share the internal roadmap to close deals, because customers who have seen it will hold the company to it, and the product manager loses the room to change course. I agree with the danger and differ on the remedy. The danger comes from features and dates in the far part of the document. A roadmap whose middle items are outcomes and whose far items are problems contains no feature to be held to, so it can be shown. My recommendation fails where the near-horizon dates are not kept, since those are the one thing the roadmap promises as delivery.

## The Objection: Customers and Boards Want Dates

The strongest objection to such a roadmap comes from the people it is shown to. Sales, customers and boards hold that a roadmap is a commitment to deliver named features on dates, and that anything less is evasion. The need behind the objection is real. A customer signing a three-year contract, a salesperson closing a deal and a board approving a budget each have plans of their own that depend on the product, and they have to plan on something.

A date for a named feature beyond the learning cycle does not give them that. Such a date can be kept in only one way: by fixing the solution before the evidence arrives and building it regardless. Corvane did exactly this. It kept thirty-eight of forty-one dates, and the customers who received the features renewed less. A kept date is not evidence that the promise was worth making. What the objectors need is something true to plan on. The roadmap gives them the order of outcomes, the share of capacity, the near-horizon dates, and the record of near dates kept so far.

Some requesters will still demand a date beyond the near horizon. There are three honest answers: direction only, a fixed date with open scope, and a priced exception, which is a named feature on a date that someone senior pays for out of a limited allowance. Which is right depends on where the date comes from. The priced exception has a precedent in *Build What Matters*, which recounts a company that gave its head of sales a limited number of tokens for one-off requests. By that account most such requests stopped reaching product management, because a request now cost the person who made it.

| Answer | What is given | Right when | Cost |
| --- | --- | --- | --- |
| Direction only | The outcome and its place in the order | The date is a wish | Some deals are harder to close |
| Fixed date, open scope | The date and the outcome to be reached by it; the solution stays open | The world sets the date: a regulation, the end of a contract, the customer's own launch | Scope is cut to keep the date |
| Priced exception | A named feature on a date | One customer's need justifies it, and someone senior spends a limited allowance on it | Capacity leaves the iteration share, visibly |

Most requests are not demands for a date at all, and the share and the horizons give a general way of answering them. Foster and Nerlikar call the ability to say no a hallmark of a product-driven company, and they describe the alternative as "playing product management Tetris", fitting every request in so that nobody has to be refused. Their practice is to keep an idea bank for suggestions that are not on the roadmap, and to be open about what did not make it and why. With a stated share, the answer has a form. The request is recorded, it competes inside the iteration share, and if it loses, the requester is told what it lost to.

## Worked Example: Corvane's Roadmap, Rewritten

Corvane's roadmap can now be rewritten with both patterns. In mid-2025 the company was growing toward 500 people, and Priya Nambiar, its first product manager and by then its CPO, did the rewriting. She began by classifying the roadmap of 2024. All forty-one rows were iteration: each was a request from a customer. No row was innovation. Operation work, such as the release tooling Corvane's engineers built that year, had been done outside the roadmap. Nobody had chosen this balance.

She then estimated Corvane's learning cycle. A solution of the size of a typical roadmap item took about six weeks to build and release. Customers needed about three weeks to switch a new function on for their planners. The measure needed four more weeks to move and be read. Six, three and four make thirteen weeks, so Corvane's near horizon was one quarter.

The roadmap she wrote stated a share first: 40 percent of capacity to innovation, 35 to iteration and 25 to operation. It then laid seven items over three horizons, following the order of Corvane's strategy.

| Horizon | Category | The item as stated | What Corvane promises |
| --- | --- | --- | --- |
| Near: third quarter of 2025 | Innovation | A customer whose appointment is moved hears it from Corvane before calling the office. A message with the new time and a link to accept it or ask for another, released in week 8 of the quarter. Measure: share of appointment changes that reach the customer from Corvane first; about a third today, target two thirds by the end of the cycle | The solution and the date |
| Near | Iteration | The features written into customer contracts in 2024 whose contract dates fall in this quarter | The solution and the date, promised by contract before the roadmap changed |
| Near | Operation | A completed job reaches the customer's billing system the same day. The nightly export's retry rebuilt, week 5 of the quarter | The solution and the date |
| Middle: to mid-2026 | Innovation | When a technician is sick, the product proposes a repaired plan and the planner decides. Measure: share of proposals accepted unchanged | The outcome and its place in the order |
| Middle | Iteration | Planners stop keeping a second schedule in a spreadsheet. Measure: share of planners who still keep one | The outcome and its place in the order |
| Far: to 2028 | Innovation | A planner still builds each week's plan by hand | Direction |
| Far | Operation | Each large customer's billing and stock integration is built separately | Direction |

The first cycle kept its date and missed its target. The message shipped in week 8 of the quarter. Four weeks later, the share of appointment changes that reached the customer from Corvane before the customer called had risen from about a third to just over half, short of the target of two thirds. The other changes had a common cause: a planner agreed them with a technician by phone and entered them only in the evening, too late for any message. So the second solution let the technician record the change on the phone. A feature list written in advance would have carried "notifications, version 2" with a date. The solution that the first cycle pointed to could not have been named before the cycle ran.

The change had costs, and it left two things open. Sales lost a list it could sell from. New dated features were granted only as priced exceptions: the head of sales was given three for the rest of 2025 and used two. The first open matter is the renewal rate. It is read once a year, and it cannot separate the effect of the roadmap from the other changes of 2025, so I claim no effect on it. The second is that the roadmap named outcomes without settling who chooses the solutions.

## What AI Changes Here

Corvane set its near horizon at one quarter in 2025, and that length may not hold when agents do part of the building. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, in the teams I have observed, coding agents shorten the time it takes to build a first version of a solution. This is my observation and not a measured result. Building is only one of the three parts of a learning cycle. The time customers take to adopt a solution, and the time the measure takes to move, are customers' time, and agents do not shorten them. So the cycle shortens by less than the building does.

If the cycle does shorten, the horizons shift with it. **Speculative.** A shorter learning cycle means the near horizon covers less calendar time, so less of a year's roadmap can be stated as solutions with dates. In exchange more cycles fit into the year, more is learned in the same stretch of the roadmap, and outcomes are reached or dropped sooner. The horizons are then better counted in cycles than in quarters. This follows from the limit argued above. It would be confirmed where organizations report more solution attempts per outcome in a quarter, together with a shorter dated part of their roadmaps.

The same speed can be spent the other way. **Speculative.** Cheaper building makes the dated feature list cheaper to keep. When a requested feature costs days, building it looks cheaper than refusing it, so the Feature Factory becomes more tempting and not less. This would be confirmed where organizations that use agents ship more customer-requested features per quarter with no change in their outcome measures.

## What to Take Away

**Established.** What the sources say:

- A roadmap connects near-term product changes to strategic milestones and the vision, and lets other teams plan (Foster and Nerlikar, *Build What Matters*).
- Product development divides into innovation, iteration and operation, and the share for each is decided top-down before items are ranked (Foster and Nerlikar).
- A roadmap driven by what was promised to customers, with no tie to the strategy, is the mark of a sales-led company (Perri, *Escaping the Build Trap*).

**Depends on context.** What changes with the situation:

- The share depends on the product's stage; 60, 30 and 10 is one book's example.
- The length of the near horizon depends on your learning cycle, which you estimate from your own build, adoption and measurement times.
- The answer to a demanded date depends on where the date comes from: a wish, the world, or one customer worth an exception.

**The author's synthesis.** What is this book's own position:

- The limit of one learning cycle on solutions and dates, and the three horizons that follow from it, are mine. The sources give the outcome orientation and the balance, and not this limit.
- A share is a decision, an order of outcomes is a judgement and a dated solution is a prediction. A roadmap is honest when each is committed only as far ahead as its kind allows, and it can then be planned on by customers, sales and a board.

## Checklist

The checklist turns the chapter into eight steps. Take your current roadmap and work through them in order.

- [ ] Classify every item as innovation, iteration or operation, and add up the share each category has today.
- [ ] Decide the share you want for each category, with the executives who must defend it, before ranking anything.
- [ ] Estimate your learning cycle: time to build and release, time for customers to take it up, time for the measure to move and be read.
- [ ] Keep solutions and dates only on items inside one learning cycle.
- [ ] Restate each item in the next two or three cycles as an outcome with a measure and a place in the order.
- [ ] Restate everything beyond that as a problem.
- [ ] Label each horizon with what it promises, and show the same roadmap to sales, customers and the board.
- [ ] For each remaining dated promise beyond the near horizon, decide whether the date comes from the world or is a priced exception, and who paid for it.

Corvane shipped forty-one promised features and its renewal rate fell. You can now say what that roadmap committed to: solutions and dates up to a year out, with no outcome and no stated share. A roadmap of outcomes removes that fault and opens a question of its own, which is who turns each outcome into a solution. The next chapter answers it by dividing decisions between leaders and teams, and by describing what a team needs in order to make the decisions that fall to it: [[discovery-delivery-and-empowered-teams]].

## Sources and Evidence

**Books**

- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. The purpose of a roadmap; innovation, iteration and operation; top-down allocation; the Roller Coaster; the three-year default horizon and the reassessment rule; saying no and the idea bank; the warning about sharing the internal roadmap; the account of sales tokens.
- *Escaping the Build Trap*, Melissa Perri, 2018. The sales-led roadmap driven by promises to customers; four levels of strategy on different time horizons.

**Practitioner sources**

- The author's record [[balanced-roadmap]], with its working checklist, and the author's Roadmapping Guide template: allocation before ranking, and tuning the share to the product's stage.
- The limit of one learning cycle, the three horizons and the statements under "What AI Changes Here" are the author's position and observation as of November 2026, and are labeled as such. No measured result on AI and roadmap horizons is cited.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
