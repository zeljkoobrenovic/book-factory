---
title: "Discovery, Delivery and Empowered Teams"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What may a product team decide for itself, and how does that fit with a vision set at the top? Leaders decide the problems, their order and the measure of success; the team decides the solution and answers for the outcome, and it needs customers and data within reach to do so."
permalink: discovery-delivery-and-empowered-teams
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn which product decisions belong to leaders and which to the team, and what a team needs before it can use its share.

> **KEY POINTS:**
>
> * **Leaders own the problem space; the team owns the solution space.** Leaders decide which customers and problems matter, in what order, and what counts as success. The team decides what to build and which experiment to run first, and answers for the outcome.
> * **A vision set at the top fits with that.** It bounds the problems worth solving and leaves the solutions open. The two schools of product management divide decisions the same way; only their one-sided readings conflict.
> * **The handing over is empty without discovery and its supplies.** A team needs the context, access to customers and data. Discovery is the team's own work, and product operations keeps it supplied.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Feature Factory** — the chapter shows how it survives under the word "empowered", and what has to be handed over to end it.
> * **The Escalation Ladder** — the worked example hands to a team a routine solution decision that was still made by the chief product officer.

<br>

In 2025 Priya Nambiar became chief product officer of Corvane, the fictional company this book follows, and told its product teams that they were now **empowered**. Two quarters later one team was still building a list of features that came from sales. Another had spent a quarter on a problem that nobody had chosen. If you have heard a leader announce that teams are empowered and then watched little change, or watched a team drift, you have seen both results. Both have one cause. The announcement said what would stop. It did not say **which decisions were now the team's** and which stayed with the leaders.

This chapter draws that line. A product team decides the solution: what to build, how it should work and in what order to try things. It answers for the outcome. Leaders decide which problems matter, the order of those problems and how success is measured. A vision set at the top fits with this, because the vision bounds the problem space and leaves the solution space open. The arrangement works only when the team has the context, the customers and the data it needs to find solutions. The chapter starts with Corvane's two teams, then defines the two spaces and sorts common decisions between them. Three patterns follow: the handover, discovery and delivery in one team, and product operations. After that come the two ways the idea fails, the apparent quarrel between its two main sources, one Corvane team for which the line was written down, and what AI changes.

## Setting the Scene: Two Teams Called Empowered

Here is the situation in full. In 2024, when it had 180 people, Corvane shipped forty-one features, each promised to a named customer, and its renewal rate fell. During 2025 the company grew from eleven product teams toward about thirty, on its way to about 500 people, 260 of them in product and tech. Priya Nambiar, its first product manager and now its CPO, replaced the list of promised features with a roadmap of outcomes ([[roadmaps-and-horizons]]). Every team's goal now named a measure it was meant to move. At the same meeting she told the teams that they were empowered. Apart from a few promises already under contract, nobody would hand them feature lists again. She did not say what a team now decided.

For the Customer Portal team, little changed. Its goal named a measure, as every team's did. But each month the sales director still sent the team's product manager the requests of the three largest accounts. The product manager turned them into the backlog, the list of work the team would build next, and filed each request under the goal. The team's plan for the quarter read as three features, with dates that came from sales. The engineers and the designer decided how to build each feature and nothing else. Every decision about what to build was still made outside the team, and the team was called empowered.

The Reporting team had the opposite experience. Its goal named a measure too, one that reports could do little to move, and nobody said which problem, for which customer, the team was meant to solve. The team chose its own problem and spent a quarter rebuilding its report builder. At the quarter's outcome review the measure had not moved, nobody could say what the rebuilding had been for, and no leader had asked in between. Both teams lacked the same thing: a stated line between what the leaders decide and what the team decides.

## Two Spaces: The Problem and the Solution

The line needs a few terms, and the first is the word in the announcement. In *Empowered*, Marty Cagan and Chris Jones use **empowered product team** for a team that is given a problem to solve and answers for the outcome, the change in what customers can do or in a business result. They set it against the **feature team**, which is given features to build and answers for delivering them. My record of the book is [[team-objectives]]. The team in both cases is a product manager, a designer and engineers. How those three divide decisions among themselves is the subject of [[the-product-engineering-design-triad]], and this chapter treats them as one unit.

A team that is given a problem needs to know where the problem ends and the solution begins, so I divide product decisions into two spaces. The **problem space** holds four decisions: which customers to serve, which of their problems matter, in what order to take those problems, and how success is measured. The **solution space** holds three: what to build, how it should work, and in what order to try things. Leaders own the first space and the team owns the second. The line between them is a **decision right** as [[the-organization-as-a-system]] defined it: the agreed answer to who may make a named kind of decision, whose input they must take, and where the decision is written down. It is one of that chapter's four levers of organization design, applied here to product work.

The previous three chapters lead up to this line, and the drawing below puts them in one chain. On the team's side it shows two kinds of work that a later section defines: discovery, which is finding the solution, and delivery, which is building it.

---begin mermaid---
flowchart LR
    V["Leaders: vision, the customer's future journey"] --> S["Leaders: strategy, the problems in order"]
    S --> R["Leaders: roadmap, an outcome and its measure"]
    R -->|"the line: problem, measure, context"| D["Team: discovery"]
    D -->|"what is worth building"| L["Team: delivery"]
    L -->|"what was learned"| D
    L --> O["Measured outcome"]
    O -->|"leaders judge the result"| S
---end mermaid---

**Figure 1:** *A vision set at the top bounds the problem space; each step toward the team says less about the solution, until the team holds a problem, a measure and the context, and the measured result returns to the leaders.*

The line sits where it does because each side decides where it has the information. The team talks to customers and knows what the technology can do, so it sees solutions the leaders cannot. The leaders see across teams and across years, which no single team can, so they see which problem matters most now. Melissa Perri makes the same division in *Escaping the Build Trap*, drawing on Stephen Bungay's *The Art of Action*. When results disappoint, she writes, organizations respond with more detailed instructions, and they should instead let each level define how it will achieve the intent of the level above.

Sorted by the line, eight common decisions fall to the leaders, to the team or to both. The fourth and the seventh rows are the hard ones, and the two paragraphs after the table explain them.

| Decision | Who decides | Why |
| --- | --- | --- |
| Which customer segment to serve | Leaders | Problem space; it takes the view across the market and the company |
| Which problems matter this year | Leaders | Problem space |
| The order of this year's outcomes | Leaders | Problem space; a choice across teams and time |
| The measure of success for an outcome | Leaders, with the team | Leaders say what counts as success; the team proposes the target it will answer for |
| What to build: for example, a warning or a hard block | Team | Solution space |
| Which experiment to run first | Team | Solution space |
| Whether to build or buy a component | Team, inside engineering guardrails | Solution space, bounded by rules set once for all teams |
| When to drop a solution and try another | Team, reported to the leaders | Solution space; the leaders judge the result |

The measure of success has two owners, and each owns a different part. Leaders say what counts as success for the outcome, because the measure is part of stating the problem: "planners trust the schedule" means little until someone says how that is counted. The team then proposes the target it will answer for. In *Empowered* the key results, the numbers by which an objective is judged, are proposed by the team that has to reach them, and leaders negotiate when a proposal does not meet the business need. The reason is accountability. A team can be held to a number it proposed. A number dictated to it is the leaders' guess.

Build or buy has one owner and a boundary set elsewhere. Whether to build a component or buy one is a choice among solutions, so it is the team's. The team makes it inside **guardrails**: rules that engineering sets once for all teams, such as a list of approved vendors or a review of where customer data goes. A guardrail narrows every team's solution space equally and leaves the choice inside it to the team. That is different from a leader choosing this team's solution for this problem. How guardrails are set belongs to [[engineering-strategy]] and [[architecture-governance]].

## Pattern: Hand Over a Problem, a Measure and the Context

The first pattern is the act by which a leader uses the line. It is done in writing, on a page both sides can point to, and it has three parts. The leader hands over the **problem**, stated as an outcome for a named customer. The leader hands over the **measure** of success. And the leader hands over the **context** a team needs to decide well: the vision, the strategy, the reason this problem comes before the others, and the constraints. *Empowered* insists on the third part: a problem without the strategic context is not a real assignment. My record of the book's strategy chapters adds a test ([[empowered-product-strategy]]): ask the team to explain why its objective matters. A team that cannot has received an order formatted as an objective.

After the handover the leader stays close to progress and away from the solution. Cagan and Jones describe weekly attention to where the team is, what blocks it and which other teams it depends on, and they separate this from both micromanagement and absence. The leader removes obstacles, judges the result against the measure, and does not design. Perri gives the team's side of the bargain: "If you keep things transparent, you will have more freedom to become autonomous." A team that shows its progress in terms of the outcome gives its leaders no reason to reach for the solution.

A handover of this kind is the default, and two conditions move the line: a team's skill and a date that truly cannot move. The table gives three settings, the default in the middle and one for each condition, with what each costs. Leaders naming the solution is what Cagan calls a high-integrity commitment: a promise of a date or a deliverable, investigated before it is made and kept rare. Leaders coaching a team toward a solution is his remedy for a team that cannot yet discover by itself ([[coaching]]).

| Setting | What you gain | What you lose | Fits when |
| --- | --- | --- | --- |
| Leaders name the solution | A date or a deliverable that can be promised | The team's knowledge of the customer; its accountability for the outcome | A contract or a regulation fixes the date, and the solution was investigated first |
| Leaders hand over a problem, a measure and the context | Solutions the leaders could not have seen; a team that answers for the result | Predictability about what will ship | The team has the skill and the access to discover |
| Leaders hand over the problem and coach the team toward a solution | A team that learns to decide | Leader time, and speed | The team is new, or new to discovery, and the period is stated |

The users of this pattern are the product team and the leader who hands over. It has worked when any member of the team can say, without preparation, what problem the team is solving, how success will be measured and what the team may decide. A quicker measure, my own: count how many items on the team's board arrived from outside as a named feature.

## Pattern: Discovery and Delivery in One Team

A team that has been handed a problem and no solution has to find the solution, and that is a kind of work with its own name. **Discovery** is finding out which solution is worth building before paying to build it. **Delivery** is building that solution so that it runs reliably for every customer. The two words in this sense are Cagan's, from his earlier book *Inspired*, which I cite for this widely known distinction as a supplement to the notes this chapter rests on. In *Empowered* he lists four risks to settle before committing to a solution: whether customers will value it, whether they can use it, whether it can be built, and whether the business can support it. Perri describes the same work as turning known unknowns, the assumptions you know you have to test, into facts.

Discovery and delivery are two kinds of work done continuously by the same team. They are not two phases, and they are not two teams. What a person learns by watching a planner use the product does not survive being written up and handed to someone else, and engineers who take part in discovery see solutions that nobody else knows are possible. *Build What Matters*, by Ben Foster and Rajesh Nerlikar, makes the timing explicit. Research that only tests an initiative already chosen is reactive, they argue, and customer research belongs at every stage, including the decision about what to build at all.

This pattern is for the product team, and it needs two things from its leaders: protected time and permission for small experiments. My working rule, drawn from *Build What Matters* and kept in [[right-processes]], is at least four hours of customer research a week for each product manager, whether or not a project asks for it. [[working-small]] covers the tempo of small experiments. The pattern has worked when the team drops ideas before building them and can show which shipped changes moved the measure.

## Pattern: Product Operations as the Support System

Discovery needs customers and data, and both move out of a team's reach as a company grows. Foster and Nerlikar describe how. A sales team is added, then a customer success team, and these become the voice of the customer. Product managers end up in what the authors call a game of telephone with the people they build for. Perri and Denise Tilles report the same thing in *Product Operations*: sales and customer success often act as gatekeepers to clients. Data moves away in the same way, into other departments' systems. A problem handed to a team that can reach neither customers nor data cannot be solved by that team.

The function that restores the supply is **product operations**. Perri and Tilles define it plainly: "At its core, product operations is an enablement function." It has three parts: business data read next to product data, customer and market insight that a team can find and add to, and a shared process of templates and cadences. What product operations takes off product managers is the assembling: pulling the numbers, recruiting customers to talk to, reinventing a planning format. It makes none of their decisions, and the authors say directly that it does not replace skill in product managers.

The users of product operations are product managers and their teams, with the leaders who read outcomes as a second group. I judge it by one measure: how long a team takes to get from a question to the data, or to a conversation with a customer. It fails by becoming what Perri and Tilles call "process people", who standardize everything. One practitioner they quote runs operations like a product whose unused services are retired, which is the right test. At Corvane's earlier sizes I would make this a part-time duty of one product manager before making it a team; that is my recommendation, not the book's.

## Anti-Patterns: The Feature Team Called Empowered and the Team Left Alone

Used without the line, the word "empowered" produces the two teams of the opening. The first is **The Feature Factory** under a new name: a feature team that is called empowered. The Feature Factory is one of this book's twelve failure patterns, a team that receives a list of features decided elsewhere and keeps only the decision of how. You can recognize it by three signs. Its objectives are deliverables with dates, or have a list of deliverables filed under them. The dates and targets arrive from outside the team. And its product manager is what Perri calls the waiter, an order taker who asks stakeholders and customers what they want and turns the answers into a list. With no goal to weigh requests against, she observes, the most important requester wins. Corvane's Customer Portal team showed all three signs: three features filed under its goal, dates from sales, and a product manager who passed the list on. The largest accounts won.

The second failure is the reverse: leaders who decide nothing. A team left alone has been abandoned, not empowered. It has freedom over solutions, and no stated problem and no context to use the freedom for. A measure with no problem attached, which is what the Reporting team had, is not an outcome handed over. My record of *Empowered* calls this management by absence: no progress reviews, no obstacles removed, and the word empowerment to cover it. Corvane's Reporting team was the case. The arrangement has two sides, the leaders' direction and the team's freedom to choose the solution. The feature team keeps the direction and loses the freedom. The team left alone keeps the freedom and loses the direction.

## Where the Sources Disagree: Vision From the Top or Solutions From the Edge

Each of those two sides has a school behind it, and the two schools appear to disagree about where product direction comes from. *Build What Matters* describes vision-led product management. Leaders write the vision and then make a top-down allocation of capacity, and the authors state the principle bluntly: "This should be obvious, but big decisions need to come before small ones." *Empowered* argues from the other end. The best solutions come from the people closest to the customers and the technology, so teams must be given problems and trusted with the answers.

Read closely, neither book holds the position its title suggests. Cagan asks leaders for a product vision and a strategy, and has them decide which team works on which problem; the bottom-up view is not his. Foster and Nerlikar list "delegate decision-making" among the things a product culture needs. They want product managers in front of customers, and they say of the mock-ups that illustrate a vision: "Remember, these are not deliverables that you will hand to engineering." The real quarrel is between two readings, and each drops one side. The **bottom-up reading of empowerment** holds that any direction from the top turns teams into feature teams. The opposite instinct of managers holds that teams cannot be trusted with solutions that matter.

This book's resolution follows the two books and not the two readings. Leaders own the problem space, the order of problems and the measure of success, with the team proposing its own target. Teams own the solution space and the order of their experiments. The line is written down, so that neither side has to guess. One difference of degree remains: how concrete the vision should be. A vision that describes the customer's future journey ([[vision-and-product-strategy]]) may sketch what the customer will see. The more of that sketch a team is required to build as drawn, the more of the solution space the vision has taken. How much it should take depends on how well that future journey is known.

## Worked Example: Double-Booking at Corvane

One Corvane team shows the line written down. In 2026, with the company still at about 500 people, the Scheduling team was handed an outcome from the middle horizon of the roadmap: planners no longer keep a second schedule in a spreadsheet. The team owns the rule engine, the service that decides which jobs may overlap. Priya Nambiar and the director of the team's product group recorded who decided what on one page. Its last row is a decision that had not moved since 2022, and the example comes back to it.

| Decision | Who decided | What was decided |
| --- | --- | --- |
| Whose problem | Priya Nambiar and the group's director | Planners at existing customers |
| Which problem, and its place in the order | The same two | The second schedule that planners keep outside the product; first of the group's three outcomes for 2026 |
| Measure of success | The leaders named it; the team proposed the target | Share of planners who keep a second schedule, by quarterly survey: from 60% to under 30% in two quarters, with the time to book a job not rising |
| What to build | Scheduling team | Left open |
| Order of experiments | Scheduling team | Left open |
| The scheduling rules themselves | Priya Nambiar, as since 2022 | Not yet handed over |

The team then did its discovery. The product manager, the designer and two engineers sat with planners at five customers over three weeks. The visits were arranged by Corvane's first product operations hire and no longer went through account managers. The leaders had expected the team to build an import for the spreadsheets. The team found out what the spreadsheets were for: the product blocked a second job for a technician inside the travel time after the first. Planners squeezed emergency call-outs into exactly that gap, on purpose, and phoned the next customer to say the technician would be late. The product refused those jobs, so planners kept them in a spreadsheet. The team proposed to replace the block with a warning that shows which later jobs are affected and offers to move them. It tried the warning first as a prototype with three planners, then with one customer's office.

Replacing the block meant changing a scheduling rule, and that decision was not yet the team's. In 2022 Corvane had about 45 engineers, and three teams each implemented the scheduling rules in their own application. Priya Nambiar, then the product manager who worked with all of them, began deciding the rules herself, with the three teams consulted. The block was one of her decisions. At that size the arrangement fitted. By 2025 she was the CPO of about 500 people, and every rule question still waited for her. The decision right had become **The Escalation Ladder**: a routine decision made two levels above the work. She handed it to the Scheduling team, with the Dispatch and Technician App teams consulted and the decisions still recorded. She kept only the rule changes that alter what the product promises a customer.

With the rule in its own hands, the team released the warning, and the result fell short of the target. After two quarters the share of planners keeping a second schedule had fallen from 60% to 35%, against a target of under 30%. The time to book a job had not changed. The team reported the gap to Priya Nambiar and the director, with the experiment it would run next. The leaders judged the result and left the next step to the team.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The Scheduling team's case is set in 2026, when its engineers already had coding agents, so it is fair to ask whether cheaper building moves the line. **Emerging.** As of November 2026, in the teams I have observed, a team with coding agents can put several working prototypes in front of customers in the time one used to take. For a team that already does discovery, that makes discovery cheaper. This is my observation. I know of no published measurement of the effect, so this chapter makes no Proven claim.

An organization that has not drawn the line gets something different from the same tools. **Speculative.** If building costs less, a feature team ships more features that nobody examined, and ships them faster. The Customer Portal team with agents would have delivered the sales list sooner. The scarce work is then at the two ends of Figure 1: choosing the problem, and verifying that the outcome moved. On that reasoning the line matters more when building is cheap. The claim would be confirmed where teams report shipping more while their outcome measures stay flat, and [[where-the-constraint-moves]] weighs the published evidence.

## What to Take Away

**Established.** What the sources agree on:

- Teams given problems to solve, with the context to decide, find better solutions than teams given features (Cagan and Jones, *Empowered*; Perri, *Escaping the Build Trap*).
- Leaders owe the vision, the strategy and the choice of problems (*Empowered*; Foster and Nerlikar, *Build What Matters*).
- Customer research belongs before the decision about what to build, and the team that builds should do it (*Build What Matters*; *Empowered*).
- Product operations enables decisions and makes none (Perri and Tilles, *Product Operations*).

**Depends on context.** What changes with the situation:

- Where the line is set depends on the team's skill and on commitments that cannot move. A new team is coached; a fixed date is a rare, investigated exception.
- How concrete the vision is depends on how well the customer's future journey is known.
- Whether product operations is a team or a part-time duty depends on size.

**The author's synthesis.** What is this book's own position:

- The two spaces, and the line between them as a decision right, are my arrangement of these sources.
- The handover in three parts, a problem, a measure and the context, is my summary of what *Empowered* asks of leaders.
- That the vision-led and the empowered schools conflict only in their one-sided readings is my reading of both books.

## Checklist

The line, the handover, discovery and product operations are one arrangement seen from four sides. The line says who decides. The handover carries the leaders' decisions to the team. Discovery is how the team makes its own, and product operations keeps discovery supplied. Take one team and one roadmap of your own, and run these eight checks.

- [ ] List the decisions made about the team's work last quarter, and mark who made each.
- [ ] For each one, say whether it was in the problem space or the solution space, and whether the right side made it.
- [ ] Ask three members of the team separately what problem the team is solving and how success is measured.
- [ ] Check that the team proposed its own target, and that a leader accepted or negotiated it.
- [ ] Count the items on the team's board that arrived as a named feature from outside the team.
- [ ] Ask when each member of the team last watched a customer use the product.
- [ ] Time how long the team takes to get from a question to the data, or to a customer.
- [ ] On the roadmap, mark each item as an outcome or a solution; for each solution, name the outcome it serves or remove it.

The last check closes Part III as well as this chapter. Outcome, vision, roadmap and empowered team are one chain. Each link says less about the solution and more about the reason, until the team is left with a problem, a measure and the freedom to solve it. Corvane's two teams of 2025 each held one end of that chain: the Customer Portal team had solutions and no problem of its own, and the Reporting team had freedom and no problem at all. The forty-one features of 2024 can be read as plainly: they were output with no outcome above it, forty-one solutions chosen outside the teams that built them. The argument between top-down and bottom-up product work dissolves once each level knows which space it owns. Engineering has a model of the same shape. Where the product model has a vision, a strategy, a roadmap and empowered teams, the engineering model has a strategy, governance, platforms, quality practices and migrations, and it also settles each decision at the level that has the information. Part IV sets it out, beginning with [[part-4]].

## Sources and Evidence

**Books**

- *Empowered: Ordinary People, Extraordinary Products*, Marty Cagan with Chris Jones, 2020. Empowered product teams and feature teams; strategic context; team objectives and key results proposed by the team; active management; the four risks; coaching; high-integrity commitments. Used through the author's records [[team-objectives]], [[empowered-product-strategy]], [[coaching]] and [[team-topology]].
- *Inspired: How to Create Tech Products Customers Love*, Marty Cagan, second edition, 2017. Cited only for the widely known terms discovery and delivery; it supplements the author's notes.
- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. Vision-led product management; top-down allocation; research before the decision to build; the separation of product managers from customers; delegated decisions; vision mock-ups as concepts. The author's records: [[right-processes]] and [[right-team]].
- *Escaping the Build Trap*, Melissa Perri, 2018. The waiter archetype; known unknowns and discovery; building to learn; each level defining how it achieves the intent of the level above (after Stephen Bungay, *The Art of Action*, 2011, as Perri cites it); transparency and autonomy.
- *Product Operations: How Successful Companies Build Better Products at Scale*, Melissa Perri and Denise Tilles, 2023. Product operations as an enablement function; its three parts; what it does not do; gatekeepers; the "process people" warning.

**Practitioner sources**

- "TBM 435: 20 Unfiltered Operating Takes", John Cutler, *The Beautiful Mess*, August 2026, through the author's record [[working-small]]. Working in small experiments.
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
