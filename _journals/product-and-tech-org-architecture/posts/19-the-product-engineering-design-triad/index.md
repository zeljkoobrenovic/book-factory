---
title: "The Product–Engineering–Design Triad"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How should product, engineering and design share decisions at each level? As three roles that each answer for one risk: whether the thing is worth building, whether it can be built and run, and whether people can use it, with each deciding in its own area after asking the other two."
permalink: the-product-engineering-design-triad
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn who decides what among product, engineering and design in a team, a group and the executive team, and how to recognize the three ways the arrangement fails.

> **KEY POINTS:**
>
> * **Three risks, one accountable role each.** Product answers for whether the thing is worth building, engineering for whether it can be built and run, design for whether people can use it. Each decides in its own area after asking the other two.
> * **The triad is a decision right, repeated at every level.** It exists in the team, in the group of teams and among the executives. A weekly meeting of the three is only where it is exercised, and a level with one of the three missing is incomplete.
> * **It fails in three recognizable forms.** Product gives orders, engineering only vetoes, or design is brought in to decorate. In each, a role is present and its judgment is not.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Feature Factory** — the chapter shows it from inside the team, where the product manager passes on a solution and the other two roles receive it as a specification.
> * **The Escalation Ladder** — a group with no product or design lead sends its cross-team questions up to the executives; the worked example brings them back down.

<br>

In September 2024 the Dispatch team at Corvane, the fictional company this book follows, shipped a technician skills matrix on the date promised to a customer. A product manager, eight engineers and a designer had worked on it. Nobody had asked any of them whether it was worth building, whether its most important part could be built, or whether a planner could use it. You may know a team like this one: the product manager writes the tickets, the engineers estimate them, and the designer is asked at the end to make the result look good. All three roles are present, and none of the three questions is answered by the person who could answer it.

This chapter says how the three should share decisions. They work as a **triad**: product answers for whether the thing is worth building, engineering for whether it can be built and run, and design for whether people can use it. Each decides in its own area after asking the other two, and the same arrangement repeats in the team, in the group of teams and among the executives. It fails in three recognizable ways: product gives orders, engineering only vetoes, or design is brought in to decorate. The chapter starts with the skills matrix. It then defines the three risks and their roles, shows the triad at three levels, and gives two patterns: setting it up in a team and setting it up in a group. After that come the three failure forms, the view that one role should own the product, one Corvane group that set its triad up, and what AI changes.

## Setting the Scene: One Feature, Three Roles

Here is the feature in full. In 2024 Corvane had 180 people and eleven product teams, and its roadmap was a list of forty-one features, each promised to a customer by name. Sales and account managers added the rows. One row read: technician skills matrix, for a telecom installer, September. It went to the Dispatch team, which had eight engineers, an engineering manager, a product manager of its own and a designer it shared with the Scheduling team. The decision to build was made before the team saw it.

Each role then did its work in turn. The product manager turned the account manager's notes into 23 tickets. They described two things: a grid of technicians against skills, kept up to date by a planner, and a dispatch board that offers a planner only the technicians who have the skill a job needs. The engineers estimated the tickets, and the engineering manager's estimate ran to November. In one meeting the dispatch-board part, which needed a change to the logic that assigns jobs, was cut to keep September. The designer was shown the built grid three weeks before release. She changed labels, spacing and colors.

The feature shipped in September. By the end of 2024 it was one of 26 features that only the customer who had asked for them used. At the telecom installer, planners filled in the grid and went on assigning jobs from memory, because the board did not use what they had entered. The date was met and the feature failed, on a question nobody in the team had been asked to judge: whether a grid without the board was worth building.

## Three Risks, Three Accountable Roles

What nobody judged has a name in the product literature. Marty Cagan, in his article "The Four Big Risks", lists four risks that a product idea carries. **Value risk** is whether customers will buy the thing or users will choose to use it. **Usability risk** is whether users can figure out how to use it. **Feasibility risk** is whether the engineers can build it with the time, skills and technology they have. **Business viability risk** is whether the solution also works for the rest of the business: its sales channel, its contracts, its costs. This book takes the first and the last together as one question, whether the thing is worth building, because Cagan gives both to one role, as the next paragraph shows. To feasibility it adds "and run", since a team also operates what it builds; that addition is mine.

Each risk gets one accountable role, and the three roles together are the triad. In the same article the product manager is responsible for the value and viability risks, the product designer for usability, and the lead engineer for feasibility. So in a team the triad is the **product manager**, the **engineering lead** and the **designer**. By engineering lead I mean whoever answers for feasibility in that team, a tech lead in some companies and an engineering manager in others. The word triad is common usage, not Cagan's term; my record [[right-team]] uses it too.

Being accountable for a risk means deciding in its area, after asking the other two. The table gives, for each member, the risk, what the member decides, and what it must ask first. The assignment of risks is Cagan's; the last two columns are my arrangement of it.

| Member | Risk | Decides | Must ask first |
| --- | --- | --- | --- |
| Product manager | Is it worth building? (value and viability) | Which problem inside the team's outcome comes next; whether a solution is worth building; when to drop it | Engineering: what would it cost, and what has become possible? Design: what did users do when they tried it? |
| Engineering lead | Can it be built and run? (feasibility) | How it is built; whether it can be built with the time and skills at hand; whether it is ready to run | Product: which part matters most to the customer? Design: which parts of the flow cannot change without breaking it for the user? |
| Designer | Can people use it? (usability) | How it works for the user: the flow, the words, the screens | Product: who is the user, and what must they get done? Engineering: what is cheap, what is costly, and what does the technology allow? |

The decisions are divided this way because each risk takes different knowledge to judge. The product manager knows the customers and the business. The engineers know what the technology allows and what it costs to run. The designer has watched users try the thing. One person deciding all three risks therefore decides two of them without the information. The 23 tickets at Dispatch show it. One document fixed what was valuable, what was feasible and how the screen would work. Only the first of the three was the product manager's to judge, and she had taken even that from an account manager's notes. My record [[product-engineering-partnership]] puts the cost in one line: a perspective that arrives only at the end has already weakened the decision.

Three separate judgments still make one decision. A solution goes ahead only when each of the three has judged its own risk acceptable. A member who says no owes the other two the condition under which the answer would be yes: "not by September with the board, but by September if the board filters on one skill only." The condition attached to a no is my own rule. Accountability stays single, because each risk has exactly one judge. The decision is shared, because it needs all three judgments.

The triad is therefore a **decision right**, and not a meeting. [[the-organization-as-a-system]] defined a decision right as the agreed answer to who may make a named kind of decision, whose input they must take, and where the decision is written down. The triad is three such answers held together. Many teams also hold a weekly meeting of the three; my own catalogue of team rituals has one, the Product Triad Sync, sixty minutes a week with resolved decisions and explicit ownership as its outputs. The meeting is where the right is exercised. A team can hold it every week while the product manager still writes all the tickets.

The book has already drawn one decision right for product work, and the two fit together. [[discovery-delivery-and-empowered-teams]] drew a line between levels: leaders decide which customers and problems matter, their order and the measure of success, and the team decides the solution and answers for the outcome. That chapter treated the team's three roles as one unit, and the triad divides the team's side of the line among them. That chapter's line runs between levels and the triad's lines run between functions at one level, so the two divisions cross and do not compete. Above the team, the same three functions divide the leaders' side, which is the next section.

## The Same Triad at Three Levels

The three risks do not stop at the team. Wherever product decisions are made, somebody has to judge whether the thing is worth doing, whether it can be built and run, and whether people can use it. So the triad repeats at the level of a **group**, several teams that work on one part of the product under one director, and at the executive level. Each function also keeps its own line from level to level, which the figure shows as a column.

---begin mermaid---
flowchart TB
    subgraph EX["Executive level"]
        direction LR
        P1["Head of product: worth building?"] --- E1["Head of engineering: can be built and run?"] --- D1["Head of design: can people use it?"]
    end
    subgraph GR["Group level"]
        direction LR
        P2["Group product lead"] --- E2["Engineering director"] --- D2["Group design lead"]
    end
    subgraph TM["Team level"]
        direction LR
        P3["Product manager"] --- E3["Engineering lead"] --- D3["Designer"]
    end
    P1 --> P2
    P2 --> P3
    E1 --> E2
    E2 --> E3
    D1 --> D2
    D2 --> D3
---end mermaid---

**Figure 1:** *The triad is a grid: decisions are shared along each row, by three roles with one risk each, and each function's own line runs down a column.*

What changes from level to level is the thing decided. The table reads from the top down, the direction in which problems are handed over.

| Level | Product answers for | Engineering answers for | Design answers for | What the three decide together |
| --- | --- | --- | --- | --- |
| Executive | Which outcomes are worth the company's capacity | Whether the organization and its technology can deliver and run them | Whether the product as a whole can be used and holds together | The outcomes and their order, the shares of capacity, which teams exist |
| Group | How the group's outcome is divided into problems for its teams | Which team builds what, and in what sequence | How a task that crosses the group's teams works for the user | The group's plan; solutions that cross teams |
| Team | Whether a solution is worth building | Whether it can be built and run | Whether people can use it | The solution |

My sources support the two upper rows only in part. *Empowered*, by Marty Cagan and Chris Jones, has the leaders of product, design and engineering shape together which teams exist and what each owns; I keep that in [[team-topology]]. Will Larson, in *The Engineering Executive's Primer*, names Product and Design among the functions best placed for strategic partnership with Engineering. Neither book assigns the three risks at group or executive level. That step is my extension of Cagan's team-level assignment.

The grid also gives a test: a level with one of the three missing is an incomplete structure. The missing risk does not go away. Either one of the other two judges it without the knowledge, or the question travels up to the level that has all three. A product group drawn in the engineering line is the usual case. It has a director and no product or design lead, and the group pattern below shows where its questions go. A team can be incomplete in the same way, with only part of a designer: [[team-size-and-composition]] counted seven designers for eleven teams at Corvane in 2024.

## Pattern: Appoint the Three Together and Name Each Risk

The first pattern puts the triad in place in one team. It has four steps and one agreement; the first step matters because a product manager who arrives months before the other two writes the plan they inherit.

1. **Appoint the three at the same time,** or at least announce them as three. *Build What Matters*, by Ben Foster and Rajesh Nerlikar, makes design a peer of product management and not its assistant, and *Empowered* wants the designer inside the team and not requested from a pool.
2. **Tell each one which risk is theirs,** in those words.
3. **Have them fill in the table** of who decides and who is asked first, for their own team, and keep it where the team can see it.
4. **Have all three take part in discovery,** the work of finding out which solution is worth building, before any solution is fixed.

The agreement is the pattern's last part. The table will not settle every disagreement, so the three agree beforehand how to escalate. Larson describes a structured escalation that he credits to LinkedIn. The two sides agree to resolve the disagreement within five days. If they cannot, they escalate together, with one shared document, and commit to the direction they are given. Larson writes about peer executives. Using the rule for a team's triad, with the three going together to their three managers, is my extension. It keeps a disagreement from being won by whoever reaches a manager first.

The users of this pattern are the team's three leads and the managers who appoint them. It has worked when each of the three, asked separately about a question that is open this week, names the same person as the one who decides it. A slower measure: the number of pieces of work in a quarter that were cut, redesigned or rebuilt after building began should fall.

## Pattern: Set Up the Triad at Group Level

One level up, the same setup usually starts from less, because one or two of the three do not exist yet. A group of teams is typically created inside one function's reporting line, most often engineering's. It appears when one manager has too many teams, so the new role is a manager of managers in that function: a director. Product managers and designers go on reporting to their own heads. This is my observation, not a finding from a source. The result is a level with one of the three, and the two missing risks go two different ways. Product questions that cross the group's teams climb to the head of product, and design questions that cross them are answered team by team.

Completing the level takes five steps:

1. **List the decisions of the last quarter that crossed the group's teams,** and who made each. The list shows whether the group has enough of them to need the two roles.
2. **Name a product lead and a design lead for the group.** In a small group these are part-time duties of a senior product manager and a senior designer. They are decision roles and need not be reporting lines.
3. **Appoint them with the director as three,** each told which risk is theirs for the group.
4. **Write who decides each kind of listed decision,** and who must be asked first.
5. **Agree the joint escalation** to the three executives.

The users are the heads of product, engineering and design, who make the appointments, and the group's teams, whose questions get answered. The pattern has worked when cross-team questions are settled inside the group and reach an executive only as joint escalations. Count the product and design questions from the group's teams that reach an executive in a quarter, and how long each waited.

## Anti-Patterns: Order-Giver, Veto, Decoration

Three roles can be present without the arrangement, and the triad then fails in three forms. The first is product as order-giver, which is **The Feature Factory** seen from inside the team. The Feature Factory, named by *Build What Matters*, is one of this book's twelve failure patterns: a team that receives a list of features decided elsewhere and keeps only the decision of how. Inside the team it has two versions. In one the product manager passes on a solution chosen by someone else, and in the other chooses it alone. My record [[right-team]] calls them the backlog clerk and the mini-CEO. The Dispatch product manager of 2024 was the first: 23 tickets from an account manager's notes.

Engineering as veto follows from an order. Engineers who first see a solution when it is specified can answer only with an estimate or a refusal. What they know about what is possible never reaches the decision. My record [[product-engineering-partnership]] calls the result technical veto theatre: engineering rejects ideas late because feasibility was not discussed early. At Corvane the engineers' one decision was to cut the dispatch-board part to keep the date. It was the part the planners needed, and nobody had asked for a cheaper way to keep it.

Design as decoration is the designer consulted after the flow is fixed. It can follow from an order too, and one staffing choice makes it likely even without one: treating design as a shared service that teams call on by request. *Empowered* warns that design run as an internal service starves discovery, and *Build What Matters* adds that designers who report to individual product managers produce design that serves the roadmap. Corvane in 2024 had seven designers for eleven teams, and four of them each worked for two teams. The Dispatch designer was one of the four. She saw the grid three weeks before release because those were her days with the team.

Side by side, each form is a member doing a job in place of judging its risk. The table gives the sign of each, the risk left unjudged and the correction, and the three corrections are one: the three find the solution together, from a stated problem, before the solution is fixed.

| Form | What you see | Risk left unjudged | Correction |
| --- | --- | --- | --- |
| Product as order-giver | The product manager writes detailed tickets from requests; the other two first see a finished specification | Value and viability, since the request stands in for the judgment; then the other two | The product manager brings a problem and a measure, not a solution |
| Engineering as veto | Engineers are asked only for an estimate; they answer with yes, no or a later date | Feasibility in its useful sense: what the technology would make possible | Engineers take part in discovery, and a no carries its condition |
| Design as decoration | The designer is brought in when the flow is built and asked to make it look good | Usability | The designer watches users with the problem and tests the flow before it is built |

## Where the Sources Disagree: One Owner or Three

The first of those forms, product as order-giver, has a respectable view behind it. The single-owner view says that one role, usually the product manager, should own the product while the others execute, because shared accountability is no accountability: when three people share a decision, each can point at the other two. Both of my main sources give this view some ground. Cagan writes: "The Product Manager is responsible for the value and viability risks, and overall accountable for the product's outcomes." My record of *Build What Matters* says the same, that one person holds real accountability for product outcomes.

The triad keeps what is right in that view and refuses its conclusion. The product manager answers for the outcome. That does not make the product manager the judge of feasibility or usability. The same article that gives the product manager the outcome gives usability to the designer and feasibility to the lead engineer, and my record adds that one accountable person does not mean the product manager decides alone. Each risk still has exactly one judge, so nobody can point at the other two. The skills matrix shows what the single-owner arrangement produces: one specification fixed all three risks, and its author could have judged at most one of them.

## Worked Example: A Group Triad at Corvane

One Corvane group shows the second pattern. By the start of 2026 Corvane had about 500 people and about thirty teams in four product groups. The group that holds the Scheduling, Dispatch and Technician App teams had eight teams and an engineering director. It had nobody at its level for product or for design. Its eight product managers reported to Priya Nambiar, the chief product officer. Its five designers reported to Noor Achterberg, the Head of Design, who in turn reported to Priya Nambiar. In the first quarter of 2026, fourteen product questions from the group's teams waited for Priya Nambiar, for a median of nine working days. Design questions that crossed teams were answered by each team for itself: a moved job was shown in three different ways on the dispatch board, on the planner's calendar and on the technician's phone.

In the second quarter the two heads completed the level. They began with the list of the first quarter's cross-team questions, which showed that the group had enough of them to need both roles. Priya Nambiar then named as the group's product lead the product manager who had taken over the Dispatch team in 2025, and Noor Achterberg named a senior designer as its design lead. They were appointed with the director on the same day, each told which risk was theirs for the group. The three wrote one page.

| Decision | Who decides | Who must be asked first |
| --- | --- | --- |
| Which problems the group's teams take, and in what order, inside the outcomes the CPO hands the group | Group product lead | Director: what each costs. Design lead: where it sits in the planner's and the technician's day |
| Which team builds what, and the sequence across teams, within Corvane's engineering strategy | Director | Product lead: what is needed first. Design lead: what the flow needs |
| How a task that crosses the group's three applications works for the user | Group design lead | Product lead: what the customer must get done. Director: what each option costs |
| Whether a solution that crosses teams goes ahead | Each of the three, for its own risk; a no carries its condition | The triads of the teams involved |
| A disagreement not settled in five working days | The three go together, with one page, to Priya Nambiar, Noor Achterberg and Dario Vance, the VP Engineering | Nobody |

The first decision under the page was the proposed repair of a sick technician's day: when a technician calls in sick, the product proposes a new plan and the planner decides. A full proposal needs three kinds of data: technicians' skills, customers' time windows and the parts each technician has on hand. The director judged feasibility and said no to parts in the first version, with the condition: the form of the parts data was still to be fixed by Corvane's platform director, and parts could join once it was. The design lead decided that a proposed change would look the same on the board, the calendar and the phone. With both answers in hand, the product lead judged a version without parts worth trying with two customers. This chapter records no result of that trial.

Two quarters later the group's questions were being settled inside the group. In the fourth quarter of 2026 three questions from its teams reached Priya Nambiar, where fourteen had in the first, and each came from all three leads with one page. A moved job was shown one way in the three applications. The cost was real. The Dispatch team had no product manager of its own for a quarter, until a replacement was hired. The design lead, who had worked full time in the Scheduling team, kept two days a week there. The three leads spent about half a day a week together. At the end of 2026 Corvane's other three groups still had only a director.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The group triad of 2026 worked in teams that already had coding agents, so it is fair to ask whether those tools change who holds the three roles. **Emerging.** As of November 2026, in the teams I have observed, a product manager or a designer with a coding agent can build a working prototype, and an engineer can produce a passable screen. Each role now does part of the others' work. This is my observation. I know of no published measurement of how it changes the division of decisions, so this chapter makes no Proven claim.

Doing part of another role's work is not the same as judging its risk. **Speculative.** If fewer people come to hold the three roles, the three risks do not merge with them. A person who holds two roles judges two risks and needs the knowledge for both. The order-giver form also becomes easier, because whoever can build alone can skip asking. On that reasoning the three accountabilities outlast the job titles. The claim would be confirmed where teams that merge roles report more work changed or withdrawn after release for reasons of usability or of running it. [[team-shape-and-roles-with-ai]] weighs the evidence.

## What to Take Away

**Established.** What the sources agree on:

- A product idea carries four risks, and each has a responsible role: value and viability for the product manager, usability for the designer, feasibility for the lead engineer (Cagan, "The Four Big Risks").
- Product, design and engineering find the solution together, and design belongs in the team as a peer (*Empowered*; *Build What Matters*).
- Peers who disagree escalate together, with one document (Larson, *The Engineering Executive's Primer*).

**Depends on context.** What changes with the situation:

- Who the engineering member is, a tech lead or an engineering manager, depends on who answers for feasibility in your teams.
- Whether a group's product lead and design lead are full roles or part-time duties depends on how many decisions cross its teams.
- How much of a designer a team needs depends on how often its decisions need one ([[team-size-and-composition]]); where design reports is a question for [[executive-roles-and-reporting-lines]].

**The author's synthesis.** What is this book's own position:

- The triad as a decision right, three answers to who decides, who is asked and where it is written, is my reading of these sources.
- The three risks applied at group and executive level, and "and run" added to feasibility, are my extensions of Cagan.
- The rule that a no carries its condition, and the three named failure forms, are mine.

## Checklist

Take one team and one group of your own, and run these eight checks.

- [ ] Name the three people in the team's triad and the risk each answers for; ask them whether they would give the same answer.
- [ ] Take one recent piece of work and write down who judged each of the three risks, and when.
- [ ] Ask when the engineers and the designer first saw that work: as a problem, or as a specification.
- [ ] Find the last time engineering said no, and check whether the no came with a condition.
- [ ] Ask the designer when they last watched a user before a flow was built.
- [ ] For one group of teams, name its product lead, its engineering lead and its design lead; mark any that is missing.
- [ ] Count the product and design questions from that group that reached an executive last quarter, and how long each waited.
- [ ] Ask each triad how it would escalate a disagreement, and whether it has ever done so together.

The risks, the levels, the patterns and the failure forms are one idea: a product decision needs three judgments, each made by the one role that has the knowledge, wherever such decisions are made. The patterns put a judge in each place, and the failure forms are what a place looks like when a role is present and its judgment is not. Corvane's skills matrix of 2024 had three roles and none of the three judgments. The product manager's tickets, the engineers' cut and the designer's polish were the three failure forms in one feature. A leader who sees that appoints the three together at every level, tells each which risk is theirs, and reads a level with one of the three missing as an incomplete structure, not a saving. Because the triad must exist at each level, the number of levels matters: every level added is three more roles to fill and one more step for a problem on its way down. How many levels an organization needs, and how many people each manager should lead, is the subject of [[spans-layers-and-managers-of-managers]].

## Sources and Evidence

**Books**

- *Empowered: Ordinary People, Extraordinary Products*, Marty Cagan with Chris Jones, 2020. Designers inside the team and not in a service pool; product, design and engineering leaders shaping the team topology together. Used through the author's records [[team-topology]], [[coaching]] and [[staffing]].
- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. Design as a peer of product management; designers not reporting to individual product managers; the Feature Factory; one person accountable for product outcomes. The author's Kindle notes and the record [[right-team]].
- *The Engineering Executive's Primer*, Will Larson, 2024. Product and Design as peer functions of Engineering; the structured, joint escalation credited to LinkedIn. The author's Kindle notes and the record [[working-with-your-ceo-peers-and-engineering]].

**Practitioner sources**

- "The Four Big Risks", Marty Cagan, Silicon Valley Product Group, 4 December 2017 (svpg.com/four-big-risks; read for this chapter in November 2026). The four risks and their definitions; the role responsible for each; the product manager's overall accountability for outcomes.
- The author's record [[product-engineering-partnership]]. Role boundaries and decision rights between product, design and engineering; technical veto theatre.
- The author's catalogue of team rituals, entry "Product Triad Sync". The weekly meeting of the three, with its participants and outputs.
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
