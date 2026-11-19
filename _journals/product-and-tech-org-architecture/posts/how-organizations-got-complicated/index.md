---
title: "How Organizations Got Complicated: From Three People at One Table to a Thousand"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Why is a product and tech organization so complicated, when it starts as a few people who simply talk to each other? Because each structure, from the manager to the metric, was added to relieve something real that had run out, each brought a new wait with it, and almost none was ever removed."
permalink: how-organizations-got-complicated
timetoread: 17 min read
---

> **KEY POINTS:**
>
> * **Three people at one table need no structure.** One hears the customer, one builds, one checks, and all three heard the same sentence. Nobody waits for anybody.
> * **Each structure was added when something ran out, and each put someone new between the idea and the shipped change.** The manager, the product manager, the split into teams, the platform team, the managers of managers, the plan, the career ladder and the metric each relieved a real limit. Almost none was removed.
> * **The failures that follow are the price of those reasonable additions.** A line at a manager's desk, a rule that falls between two teams, a number that people serve in place of the work: the next page names twelve such cases.

<br>

Three people sit at one table and build a product. In the morning one of them says that a customer wants to export the schedule as a file. Another builds the export after lunch. The third tries it, finds a wrong date, sees it fixed, and it ships before dinner. Now picture the same request in an organization of a thousand. It needs a place on a roadmap, a team that owns that part of the product, a release that another team runs, a review by someone who did not write it, and a number on a dashboard that says whether it helped. It ships in a month, if it ships. Both scenes are illustrations, and you have probably worked in both.

Between the table and the thousand lie eight structures: the manager, the product manager, the split into teams, the platform team, the managers of managers, the plan, the career ladder and the metric. **Each was added because something real had run out, each put a new person or a new wait between the idea and the shipped change, and almost none was removed.** This is a simplified account. It follows one generic organization as it grows, in the order of the ideas, and it is not the history of any company or of the industry. Real organizations add these structures in other orders and at other sizes, and the sizes given here are rough illustrations of common practice. The few dates are the years in which a source put an idea in writing. Their sources are listed at the end, and the chapters carry the detail.

The walk has nine steps: three people at one table; the manager; the product manager; the split into teams; the platform team; the managers of managers; the plan; the ladder and the metric; and today, shown at the fictional company this book follows. Each step says what stopped working, what was added and what the book calls it, what it made possible, and what it cost. The figure below draws the result as a stack. Each step then ends by answering one question: **who decides, who knows and who checks, and what does each of them wait for?**

---begin mermaid---
flowchart BT
    A["Three people at one table: say it, build it, check it"]
    B["The manager"]
    C["The product manager"]
    D["The split into teams"]
    E["The platform team"]
    F["The managers of managers"]
    G["The plan"]
    H["The ladder and the metric"]
    I["Today: all of them at once, and software that writes"]
    A --> B --> C --> D --> E --> F --> G --> H --> I
---end mermaid---
**Figure 1:** *Nine steps, one stack: each structure was added on top of the ones before and none was taken out, so a change made today passes through all of them.*

## Three People at One Table: Nothing to Wait For

Start at the table, an illustration of the simplest organization there is. Three people are building one product. One of them comes back from a customer and says what the customer asked for. They talk for ten minutes about whether it is worth doing. One of them builds it, another tries it out, and it ships the same day.

Nothing is written down and nobody has a title. The [[introduction]] named three things that run out in an organization, and at the table none of them is scarce. Each person can hold the whole product in mind, which the book calls **attention**. Each decision is made by people who heard everything there was to hear, which it calls **judgment**. And anyone can look at anyone's work and tell whether it is right, which it calls **verification**. [[the-organization-as-a-system]] defines the three properly.

Even the table is not quite simple. Suppose one of the three spends a week at a customer's office. While she is away, the other two decide to change how the schedule is stored. She learns that the customer plans in weeks, not days, and nobody at the table knows it yet. On Thursday a release goes out, and nobody compares it with what the customer said. After one week's absence it already matters who decided, who knew and who checked.

So the table works under three conditions. Everyone hears everything. Each person knows the whole product. Anyone can check anything. **Each step that follows begins where growth breaks one of these conditions**: too much said in too many places for everyone to hear it, too much product for one head, too many people and too much work for anyone to check.

**Who decides, who knows, who checks?** All three, all three, all three. **What do they wait for?** Nothing, except in the week when one of them is away.

## The Manager: Someone Whose Work Is the Team

Picture the same company at about ten people, as an illustration of common practice. They still fit in one room. But one of the founders settles every question: what comes first this week, who is hired, what someone is paid, what to do about two people who cannot work together. She used to settle such things over lunch. Now there is a line at her desk, and her judgment is the thing everyone waits for.

So one person is given a new kind of work: the team itself. That person is a manager. The manager does not build the product. The manager sees that the people who build it know what comes first, have what they need and are treated fairly. With the role comes an agreement about who may decide what. The book calls such an agreement a **decision right** ([[decision-rights-and-decision-records]]).

Both sides gain. The people on the team get an answer the same day, and someone who has time to listen to them. The founder gets her attention back for customers and for the product.

The price is that the person who decides is no longer one of the people who do the work. The manager hears about the work in a weekly conversation and decides from what was said there. A question raised on Tuesday can wait for Friday's meeting. For the first time, deciding and knowing sit in different heads.

**Who decides, who knows, who checks?** The manager decides what comes first. The people doing the work know it. They still check one another. **What do they wait for?** The manager's time.

## The Product Manager: Someone Who Speaks for the Customer

The manager settles what comes first inside the team. What customers want is a different question, and it is the next one nobody has time for. At about twenty people the company gains customers faster than its builders can visit them. Requests now arrive from sales, from support and from the founders, all at once and often in conflict. Typically the engineers have not spoken to a customer in months. Nobody has the time to find out which requests matter, so the loudest one wins. What has run out is judgment about what is worth building.

So one person is given that work: to know the customers and to decide what is built next. That person is a **product manager**, who typically works with the engineers and a designer as a group of three roles ([[the-product-engineering-design-triad]]). The engineers decide how a thing is built. The product manager decides which thing.

Both sides gain. Customers get someone who listens before anything is built. The builders get one ordered answer in place of five competing requests, and can finish what they start.

The price is a hand-off. The person who knows why a feature matters is no longer the person who builds it, and the reason can get lost on the way. What reaches the team is then a list of features, and the team is judged by how much of the list it ships. A shipped feature is an output and a customer who is better off is an outcome, and the two are not the same ([[outcomes-over-output]]). Ben Foster and Rajesh Nerlikar's *Build What Matters* (2020) lists this among ten dysfunctions of product management and calls it the Feature Factory: “an assembly line of features”.

**Who decides, who knows, who checks?** The product manager decides what is built, and the engineers decide how. One knows the customer and the others know the code. The engineers check that it works. Often nobody checks that the customer is better off. **What do they wait for?** Each other: the engineers for the next decision, the product manager for the next release.

## The Split into Teams: More Than One Conversation

At about thirty people, nobody can follow every conversation or know every part of the product. The arithmetic is against them. Three people make three pairs who might need to talk. Twelve make 66. Thirty make 435. What has run out is attention. Frederick Brooks made the same point about growing teams in *The Mythical Man-Month*, whose original preface dates from 1975; his book is not among this book's main sources and is cited only for that widely known point.

So the group is split into teams, and each team is given a part of the product to own: the web application, the mobile app, the connections to customers' systems. Each team gets its own manager and its own product manager. A part is the right size when the people on the team can understand it well enough to change it safely. The amount a team can hold in mind in this way is what the book calls its **cognitive load** ([[cognitive-load-and-team-boundaries]]), a term it takes from Matthew Skelton and Manuel Pais's *Team Topologies* (2019). A team given more than it can hold in mind is overloaded, however many people it has.

Both sides gain. Inside a team it is the table again: a handful of people who know their part and hear everything that concerns it. The company can now grow by adding teams, without asking anyone to understand everything.

The price is the line between teams. A rule that concerns two teams, such as how a discount is calculated, now has to cross that line. An agreed way for work or knowledge to cross is what the book calls an **interface** ([[interaction-modes-and-team-apis]]). Where there is none, each team builds its own version of the rule, and the product comes out in the shape of the teams. Melvin Conway described this in 1968: organizations that design systems, he wrote, produce designs that copy their own communication structures ([[conways-law-and-the-inverse-conway-maneuver]]).

**Who decides, who knows, who checks?** Each team decides inside its own part, and nobody decides what crosses the line. Each team knows its part, and nobody knows the whole. Each checks its own work, one colleague reviewing another's change before it ships, and nobody checks the joints. **What do they wait for?** Another team.

## The Platform Team: Build It Once for Everyone

With a dozen teams, typically each one has set up its own way to release software, to watch it run and to store its data. The same work has been done a dozen times, a little differently each time. Every team spends part of its attention on things that are not its part of the product, and a fault fixed in one team stays unfixed in the other eleven.

So one team is given the things all the others need, and builds them once. The book calls it a **platform team** ([[team-types]], [[platforms-and-developer-experience]]). *Team Topologies* names it as one of four types of team, and says that what such a team knows is best offered as self-service: something the other teams can use by themselves, without asking.

Both sides gain. The product teams get back the attention they spent on plumbing. The company gets one way of releasing and one place to fix a fault for everyone.

The price is a team that every other team depends on. When its help comes as a request to be handled, with the platform team running and checking each launch, and not as a service a team can use alone, every launch joins the same line. A platform team's customers also work down the corridor and are easy not to ask, so it can spend a year building something none of them wanted.

**Who decides, who knows, who checks?** The platform team decides the shared tools. The product teams know what they need from them. The platform team often checks each launch. **What do they wait for?** Their place in the platform team's line.

## Managers of Managers: Decisions Climb

With fifteen or twenty teams, the person at the top has as many managers reporting to her as the first manager once had engineers. Each of them needs what the engineers needed: an answer, and someone with time to listen. The line at her desk is back, one level higher.

So the teams are gathered into groups, and each group gets a manager whose reports are themselves managers, often called a director. Two words describe the result. The number of people one manager supports is that manager's **span**. Each level between the work and the top is a **layer** ([[spans-layers-and-managers-of-managers]]). Will Larson's rule of thumb in *An Elegant Puzzle* (2019) is that a manager should support six to eight engineers, and a manager of managers four to six managers. It is one author's rule, not a law.

Both sides gain. Every manager again has someone with time for them. The person at the top can hold four groups in mind where she could not hold twenty teams.

The price is distance. A question between two groups goes up to the person both report to, and the answer comes down again. That person knows the work only from summaries, so decisions are made far from what is known. And once the organization is drawn as a chart of boxes, the chart is easily taken for the organization itself, and redrawing it is the tool nearest to hand when results are slow or poor, whether or not the boxes were the problem.

**Who decides, who knows, who checks?** Whoever sits above both sides decides. The people at the bottom know, and the top knows a summary. Managers check managers, by report. **What do they wait for?** The question to go up and the answer to come down.

## The Plan: Agreeing Once a Quarter

With several groups, one group's most important project commonly needs work from two others, and each of those has a most important project of its own. Nobody below the top can settle whose comes first, and the top cannot settle every such case one by one. What has run out is judgment across groups: no one has both the knowledge and the standing to choose.

So the priorities are written down for everyone at once and fixed for a period, usually a quarter or a year, together with the people and money each one gets. The book calls the document, and the routine that produces it, the **plan** ([[planning]]). The regular meetings that keep it current are the subject of [[operating-cadence]].

Both sides gain. A team can count on the help it was promised, because the other team's quarter was planned with it. The leaders can tell customers and the board what is coming and what it will cost.

The price is time. A plan knows only what was known when it was written. Something learned in week three waits for the next round. And the round itself needs every group to agree, so it can take weeks, and one group that will not agree can hold up all the others.

**Who decides, who knows, who checks?** The planning round decides, once a quarter, from what was known that day. The teams know what has changed since. Progress is checked against the plan, not against the customer. **What do they wait for?** The next round.

## The Ladder and the Metric: Judging Work You Cannot See

By now several layers and a plan stand between the top and the work. So at several hundred people, those who decide on pay, promotion and funding have never seen most of the work they judge. Commonly two managers reward the same work differently, and nobody at the top can say whether one team is doing better than another. What has run out is verification: knowing, from a distance, whether people and teams are doing good work.

Two things are added, and each stands in for watching. For people, the company writes down what is expected at each level of seniority, which the book calls a **career ladder** ([[career-ladders-and-leveling]]). For teams, it picks a few numbers to follow, which the book calls **metrics** ([[measuring-engineering]]). One widely used set, for the performance of software delivery, comes from *Accelerate* (2018) by Nicole Forsgren, Jez Humble and Gene Kim, and is commonly called the DORA metrics.

Both sides gain. People learn what it takes to move up, and are judged by one standard whoever their manager is. Leaders can see from a distance whether a team is getting faster or slower, and can ask why.

The price is that a description is not the work, and neither is a number. People do the things the ladder lists, because those are what a promotion case can show. Teams move the number that is counted. And a visible rescue at midnight is easier to write down than the quiet work that prevented one, so the rescue is what gets rewarded.

**Who decides, who knows, who checks?** A committee decides, from a written case and a dashboard. The people nearest the work still know it. The number checks only what it counts. **What do they wait for?** The next promotion round.

## Today: Every Structure at Once, and Software That Writes

None of the eight structures was taken away when the next one arrived. Few are removed even when the limit they answered is no longer the one that holds the work back. Each still relieves someone, each is now somebody's job, and no one in particular is responsible for taking it out. This is my own reading of common practice, not a measured result.

What the present adds is software that writes. Claims about AI carry a label in this book, as the [[introduction]] explains. **Emerging** (the author's observation, as of November 2026): where teams use coding agents, a change that a person used to write by hand is drafted in minutes, while deciding whether it is right, and whether it was worth making, takes as long as before. [[where-the-constraint-moves]] and [[agentic-delivery]] treat this in full.

Corvane, the fictional company this book follows, shows all of it together ([[corvane-at-five-sizes]]). In the book's story Corvane has 1,100 people in 2028, 520 of them in product and tech. Every structure of this walk is in place: managers and product managers, product teams and a platform team, directors, a yearly and a quarterly plan, a career ladder and delivery metrics. Coding agents work in every team. Between January 2027 and January 2028 the number of changes merged each week rose 2.4 times, and the number of people able to review them did not rise. The median wait for a colleague to review a change went from 5 hours to 31. These figures are illustrations.

**Who decides, who knows, who checks?** Everyone named so far, each for a part. **What do they wait for?** Each of the waits named so far, and at Corvane most of all for a person to check what software wrote in minutes.

## What the Steps Add Up To

Here are the nine steps side by side. The last column uses the names the next page gives to these failures, in bold, and plain words where it has none. The names are explained there, not here.

| Step | What it made possible | What it added | New party or wait | What can now go wrong |
| --- | --- | --- | --- | --- |
| Three people at one table | A change said, built and checked in a day | Nothing | None | It works only while everyone hears everything |
| Manager | An answer the same day; the founder's attention back | The manager; the decision right | A person who decides without doing the work | Decisions made second-hand; a line at the manager's desk |
| Product manager | Customers are heard; builders get one ordered answer | The product manager | A hand-off between why and what | **The Feature Factory** |
| Split into teams | Each part understood by someone; growth by adding teams | Teams; cognitive load; the interface | Another team | **The Unowned Interface**, **The Overloaded Team** |
| Platform team | Shared things built once | The platform team | One team's line for everyone | **The Platform Nobody Asked For** |
| Managers of managers | Every manager supported; the top can hold the whole in mind | Span and layer | Levels between the work and the decision | **The Escalation Ladder**, **The Org Chart as Architecture**, **The Reorg as Strategy** |
| Plan | Teams can count on each other; leaders can make promises | The plan | The planning round | **The Consensus Stall** |
| Ladder and metric | One standard for people; teams visible from a distance | The career ladder; metrics | A committee, a dashboard and the promotion round | **The Ladder as Checklist**, **The Output Scoreboard**, **The Hero Culture** |
| Today | A thousand people build one product; changes drafted in minutes | Software that writes | Coding agents; the wait for a reviewer | **The Review Bottleneck** |

Count what now stands behind the request that three people shipped before dinner. There are eight structures, and they brought seven waits, because the ladder and the metric share one: for a manager's time, a product manager's decision, another team, the platform team's line, an answer from above, the next planning round and the next promotion round. Today adds no new wait, but it lengthens one that has been there since the split into teams: the wait for a colleague to review a change. **Every step moved deciding, knowing and checking a little further apart.** At the table they were the same three people. The answer to “who decides, who knows and who checks, and what do they wait for?” grew from “all of us, and nothing” to a chain in which each link waits for another.

It is tempting to read the result as bureaucracy: structures that pile up because managers build empires, and that a determined leader could strip away without loss. I think the walk shows the opposite. **Each structure answers a limit that comes back the day the structure is removed.** Take away the manager and the line at the founder's desk returns. Take away the plan and the groups' priorities collide again. But limits move, and a structure built around a limit that has moved is the one to change. A review step sized for changes written by hand is an example. So before you remove a structure, or copy one from another company, ask two questions. What was it added for? Does that need still exist here?

The next page names the costs. [[where-product-and-tech-organizations-go-wrong]] describes twelve recurring failure patterns, and after this walk none of them should come as a surprise: each is the price of one of these reasonable additions, and each is tied to something a leader can design.

## Sources and Evidence

The walk describes common practice in one generic organization; it is not a record of events, and the sizes at which the steps are placed are illustrations. Each date below was read on its source's page on 19 November 2026 and is the year a source put an idea in writing, not the year a practice began. The page claims no “first” for any structure.

Set in order, the dates show that the observations about teams are more than fifty years old, while the names this book uses for platform teams, spans and delivery metrics were all published within the last ten years.

| Year | What its source dates to that year | Step |
| --- | --- | --- |
| 1968 | Conway's paper on how organizations shape the systems they design | Split into teams |
| 1975 | The original preface of Brooks's *The Mythical Man-Month* | Split into teams |
| 2018 | *Accelerate* and the delivery metrics commonly called the DORA metrics | Ladder and metric |
| 2019 | *Team Topologies*: cognitive load and the platform team | Split into teams; platform team |
| 2019 | *An Elegant Puzzle*: Larson's rules of thumb for spans | Managers of managers |
| 2020 | *Build What Matters*: the Feature Factory | Product manager |

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. The rules of thumb for how many engineers a manager supports and how many managers a manager of managers supports. Year from the Open Library record.
- *Team Topologies*, Matthew Skelton and Manuel Pais, 2019. Cognitive load as the limit on what a team can own; the platform team as one of four team types, offered as self-service. Year from the book's own page at teamtopologies.com.
- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. The Feature Factory among ten dysfunctions of product management. Year from the Open Library record.
- *Accelerate*, Nicole Forsgren, Jez Humble and Gene Kim, 2018. Named only as the source of the delivery metrics commonly called the DORA metrics. Date from the publisher's page (IT Revolution).
- *The Mythical Man-Month*, Frederick P. Brooks. Not on the author's bookshelf; cited only for the widely known point that the effort of communication grows with the size of a team. The year 1975 is from the publisher's page for the anniversary edition (Addison-Wesley, 1995), whose preface refers to “the 1975 Preface”. The counts of pairs in the text are arithmetic, not a quotation.

**Research and reports**

- “How Do Committees Invent?”, Melvin E. Conway, *Datamation*, April 1968, as reproduced on the author's own site (melconway.com). The observation that designs copy the communication structures of the organizations that produce them; paraphrased.

**Practitioner sources**

- The statement about coding agents in the last step is the author's observation as of November 2026 and is labeled Emerging. The statement that structures are seldom removed is the author's reading of common practice.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
