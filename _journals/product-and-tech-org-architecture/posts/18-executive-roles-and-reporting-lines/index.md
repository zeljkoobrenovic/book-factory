---
title: "Executive Roles and Reporting Lines"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Which executive roles does a product and tech organization need, and who should report to whom? It needs someone accountable for what is built, someone accountable for how it is built and run, and a stated place where the two are joined. The common configurations differ in where they put that place."
permalink: executive-roles-and-reporting-lines
timetoread: 16 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to choose an executive configuration for a company, say what it gives up, and decide where design, data and security report.

> **KEY POINTS:**
>
> * **The top holds two accountabilities and a join.** Someone answers for what is built, someone for how it is built and run, and some decisions need both. Where those decisions are made has to be stated.
> * **Three configurations put the join in three places.** A CTO and a CPO as peers fit where balance matters more than speed, one combined executive where speed matters more, and a CTO with a VP Engineering where technical direction and running the organization are the hardest to join.
> * **Peers work when the executive team is their first team.** The practice is a written list of the decisions they make together. Design, data and security report where their decisions most often need joining.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Unowned Interface** — the line between two executives is an interface, and when nobody states it the teams below build the same plan twice.
> * **The Escalation Ladder** — when one executive joins everything, routine decisions wait for that one person.
> * **The Consensus Stall** — peers who put their functions first negotiate every shared decision and reopen the settled ones.

<br>

In 2025 Corvane, the fictional company this book follows, appointed its first chief product officer. Corvane makes scheduling software for field-service companies and was growing toward 500 people that year. Tomas Rell, co-founder and chief technology officer (CTO), and Priya Nambiar, promoted that year from product manager to chief product officer (CPO), each drew the organization they needed and brought the drawing to Ines Okafor, co-founder and CEO. The two drawings showed the same teams. For eleven of those teams they named a different leader.

You may have seen executive roles settled by who was available and who had to be kept, and a reorganization argued as a contest between charts. A chart cannot answer the question underneath: which decisions must be made together at the top, and where. This chapter's claim is that a product and tech organization needs, at the top, **someone accountable for what is built**, **someone accountable for how it is built and run**, and **a place where those two are joined**. Three common arrangements put that place differently, and each fits a condition: a CTO and a CPO as peers where balance matters more than speed, one combined executive where speed matters more, and a CTO with a VP Engineering where the hardest joining is inside engineering. The chapter starts with the two drawings. It then says what the top must hold and what each executive role is for, describes the three configurations, and gives two patterns: choose the configuration from the hardest join, and make the executive team the first team. It ends with where design, data and security report and with what AI changes.

## Setting the Scene: Two Drawings of One Organization

Each drawing was reasonable. The eleven teams were the product teams that already existed; the teams still to be formed were empty boxes in both drawings. Tomas Rell made his drawing with Dario Vance, the VP Engineering since 2023. It put each of the eleven teams under its engineering manager, the managers under engineering directors, and the directors under Dario Vance, with a product manager assigned to each team. Priya Nambiar's drawing put each team under its product manager and the product managers under a product lead for each group, with engineers staffed to the teams. Tomas Rell answered for how the product was built and run, so he drew a line from himself to every engineer. Priya Nambiar answered for what was built, so she drew a line from herself to every team's plan.

A third drawing could not have settled it, because "leading a team" stood for decisions nobody had listed. Who sets a team's plan for the quarter? Who hires for the team? Who says a feature is ready? Each drawing answered all of these at once, with one line, and the two answered them differently. The disagreement was also no longer on paper only. In three of the eleven teams, the engineering manager and the product manager had each been told by their own executive that they set the team's plan for the next quarter.

## What the Top of the Organization Must Hold

What the drawings left unstated can be stated. In my framing, the top of a product and tech organization must hold three things. Someone is accountable for **what is built**: whose problem the product solves, which problem and in what order. Someone is accountable for **how it is built and run**: the technology, the people who build it and the running product. And there is a place for **joined decisions**, by which this chapter means decisions that cannot be made well with the knowledge of one side alone. How much capacity goes to new product and how much to keeping the product running is one. Whether a promise to a customer can be kept by its date is another. Which teams exist and what each owns is a third.

Six executive roles recur. Three carry the two accountabilities: the CPO, the CTO and the VP Engineering. The other three, the heads of design, data and security, hold decisions that cut across both, and each gets a section later in the chapter. The table gives all six in one line each.

| Role | Is for | A decision it makes |
| --- | --- | --- |
| CPO, chief product officer | What is built | Which outcome a product group works on this year |
| CTO, chief technology officer | How it is built and run: the technical direction, and often the engineering organization too | Which technical choices are made once for all teams |
| VP Engineering | Running the engineering organization: managers, hiring, delivery | How many engineers each group gets |
| Head of design | Whether people can use what is built | The standard a screen must meet before release |
| Head of data | The data the company decides with and builds on | What a measure means across teams |
| Head of security | Stating risk, and the controls against it | Which risks are brought to the CEO to accept |

The table makes each role look fixed, but a title does not fix the job. The CTO's line already holds two jobs, and Will Larson's definition holds the same two: in *The Engineering Executive's Primer* the engineering executive is the functional leader for engineering, responsible for both technical execution and people management. The two jobs can sit in one person or in two. In one company the CTO runs the whole engineering organization. In another the CTO sets the technical direction and a VP Engineering runs the organization. The title does not say which, so read a role by the decisions it makes and not by its name.

## Three Configurations and What Each Trades

With the accountabilities and the roles named, the common arrangements can be compared. This chapter calls an arrangement of executive roles a **configuration**, and three are common. The first two are alternatives: they join product and engineering between two peers or inside one executive. The third is a division of the engineering side, and it combines with either of the first two.

---begin mermaid---
flowchart TB
    subgraph P["CTO and CPO as peers"]
        P1["CEO"] --> P2["CPO"]
        P1 --> P3["CTO"]
        P2 ---|"joined by agreement"| P3
    end
    subgraph C["One combined executive"]
        C1["CEO"] --> C2["CPTO: joined in one head"]
        C2 --> C3["Head of Product"]
        C2 --> C4["Head of Engineering"]
    end
    subgraph V["CTO with a VP Engineering"]
        V1["CEO"] --> V2["CTO: technical direction"]
        V2 ---|"second join"| V3["VP Engineering: runs the organization"]
        V4["Product: a peer, or under the CTO"] ---|"join with product, unchanged"| V2
    end
---end mermaid---

**Figure 1:** *The first two configurations put the join of product and engineering between two peers or inside one executive; the third adds a second join, inside engineering, to either of them.*

In the first diagram a CTO and a CPO are peers, and they join product and engineering by negotiation. Neither can overrule the other, so every joined decision is argued by one person who answers for each side. Both accountabilities stay at full strength. The cost is the time the argument takes, and a CEO who must decide when the two cannot. The CEO is part of this configuration: without one willing to settle a disagreement, the join has no place to go.

The second diagram is the opposite. One combined executive, often titled chief product and technology officer (CPTO), joins product and engineering in one head. A joined decision takes as long as that person takes to think. The configuration is fast, and it is lopsided, because the executive came from one of the two disciplines and gives it the better attention. It also has a limit. Corvane in 2019, at 12 people, had this configuration in practice: Tomas Rell decided product and technology alone, quickly and consistently, until every pricing, design and release decision waited for him. Corvane calls that time the Founder Queue.

The third diagram is not a third way of joining product with engineering. It divides the engineering side and leaves the join with product where it was, between peers or in one head. A CTO keeps the technical direction and a VP Engineering runs the organization, so each job has a full-time owner. The division creates a second join. Whether to pause feature work for a migration, for example, needs both the direction and the organization's capacity, and the two people have to agree on it. This configuration adds a join and removes none.

Each configuration moves the difficulty to a different place, and none removes it. Which one fits therefore depends on which joining is hardest for the company. A company can be in the third row and in one of the first two at once. The mapping in the table is my position and not a source's claim.

| Configuration | Where product and engineering are joined | Fits when | Gives up |
| --- | --- | --- | --- |
| CTO and CPO as peers | Between the two, by agreement, with the CEO behind them | Balance matters more than speed: a mistake toward either side is expensive | Speed, and a single point of joining |
| One combined executive | In one head | Speed matters more than balance: a small company, or one product changing fast | Balance, and the executive's time as the company grows |
| CTO with a VP Engineering | Where it was before: with a product peer, or in the CTO | The hardest joining is between technical direction and running the organization | A single voice for engineering; the second join must be written down |

## Pattern: Choose the Configuration from the Hardest Join

To find which condition a company is in, start from its decisions. The user of this pattern is whoever designs the top: a CEO, the founders or a board. The pattern worked if joined decisions take less time from being raised to being made, and fewer are reopened or made by one side alone. The procedure has four steps:

1. List the joined decisions of the last two quarters.
2. For each, write who made it, how long it waited and whether it was reopened.
3. Group the decisions by what had to meet: product with engineering, or, inside engineering, technical direction with running the organization. The group with the longest waits and the most reversals is the **hardest join**.
4. Choose the configuration that puts a person, or a written agreement between two people, on that join. If the hardest join is inside engineering, that is a CTO with a VP Engineering. If it is product with engineering, the table above decides between the other two: peers where a mistake toward either side is expensive, one combined executive where speed matters more.

Corvane's top went through all three configurations between 2019 and 2025, each at a different size.

| Years and size | Configuration | Hardest join at the time | What happened |
| --- | --- | --- | --- |
| 2019, 12 people | One combined executive in practice: Tomas Rell decides product and technology | None at first, then all of them | The Founder Queue |
| 2020–2022, 50 people | Still combined: Priya Nambiar, the first product manager, and those hired after her report to Tomas Rell | Product with engineering, inside one busy head | Product decisions wait for the CTO; in 2022 one kind, the scheduling rules, is handed to Priya Nambiar to decide |
| 2023–2024, 180 people | CTO with a VP Engineering: Dario Vance runs the organization and Tomas Rell keeps the technical direction; eleven product managers still report to the CTO | Technical direction with running an organization that doubled | Engineering gets its second executive; product has none, and sales fills the roadmap with forty-one promised features |
| 2025–2026, 500 people | CTO and CPO as peers, with the VP Engineering under the CTO | Product with engineering, now between two people | The two drawings |

The table shows each change answering the hardest join of its time and exposing the next one. The handing over of the scheduling rules in 2022 was a first sign that one head could no longer join everything. The table also shows one change that came late. In the 2023–2024 row engineering had been divided, but product was still joined to it in the old way, inside a CTO whose attention was on technology. That is the lopsidedness of the combined executive, at 180 people: with eleven product managers and nobody at the top answering for what was built, sales filled the roadmap with forty-one promised features. *Build What Matters*, by Ben Foster and Rajesh Nerlikar, gives a rule of thumb for the product side, which I summarize in my record [[right-team]]: the first product hire is a senior product manager, and a product executive follows when there are several product managers and a founder ready to hand over strategy. Corvane had eleven product managers in 2024 and no product executive.

The opposing practice shapes roles around the people available, on the grounds that the right people matter more than the chart. People do constrain the choice: Corvane could not have had peers in 2020, with one product manager. But a role made to keep or fit a person adds a join that somebody must carry, so I treat it as a cost to be stated. You can recognize such a role by removing the name and asking which decisions the role joins. *Build What Matters* names the commonest role of this kind the Throne Room: the founder or CEO who cannot let go of product decisions. Corvane had a different case of a role made to keep a person. After 2023 Tomas Rell was a founder who kept his title while Dario Vance ran engineering, with nothing written about the split. In 2025 they wrote it. Tomas Rell holds the technical side of company-level decisions, such as building or buying and acquisitions, and is consulted on the engineering strategy of [[engineering-strategy]]. Dario Vance holds everything inside engineering.

## Pattern: Make the Executive Team the First Team

A configuration with two or three executives has joins between people, and those hold only under one principle. An executive's **first team** is the executive team they sit in, and not the function they lead. The phrase is usually credited to Patrick Lencioni. My notes on his *Five Dysfunctions of a Team* hold the idea without the phrase: the fifth dysfunction, inattention to results, is members putting their own needs or their departments' needs above the collective goals of the team. Larson uses the phrase itself. In *An Elegant Puzzle* he tells managers to "make your peers your first team", and in the *Primer* he calls the weekly leadership meeting the forum for forging an executive's direct reports into a first team of their own. Applying it to a CTO and a CPO as members of the CEO's team is the plain reading of Lencioni and my extension of Larson's wording.

Peers need the principle because of what happens without it. Larson observes that when executives focus on their function and not on the executive team's shared success, allocating expenses becomes a zero-sum game. Every joined decision then becomes a contest over whose function wins. The damage also grows on the way down. Lencioni writes: "Like a vortex, small gaps between executives high up in an organization become major discrepancies by the time they reach employees below." At Corvane, the undefined phrase "leading a team" between two executives became three teams with two plans each.

The practice that makes the principle concrete starts from two pieces of advice in Larson's *Primer*. Its users are the two peers. The first piece is his advice on onboarding a peer executive, which in my working version reads: each writes down, alone, what they expect of the other's role, and the two compare the documents. Turning every difference into a line in a list of decisions, with who decides and who must be heard first, is my extension. The second piece is **structured escalation**, a process Larson credits to LinkedIn: agree to resolve a disagreement within five days, and if you cannot, escalate together with one shared document and commit to the answer. My working versions are the records [[onboarding-peer-executives]] and [[working-with-your-ceo-peers-and-engineering]]. The practice worked if disagreements reach the CEO from both executives at once, and settled decisions stay settled.

Corvane did this in 2025. Ines Okafor asked Tomas Rell and Priya Nambiar for a list of decisions in place of a third drawing, and the list fits on one page.

| Decision | Who decides | Who must be heard first |
| --- | --- | --- |
| Which outcomes each product group works on, and their order | CPO | CTO and VP Engineering, on what each would cost |
| How it is built, the technical standards, who is hired and how engineers are managed | VP Engineering, within the CTO's technical direction | CPO, on what the product needs next |
| The share of capacity for new product, for improving the existing product and for keeping it running | CPO and CTO together | The engineering directors of the product groups |
| Which teams exist, what each owns and who is the engineering director of each product group | CPO and CTO together | VP Engineering and the people affected |
| What a team does this quarter | The team's product manager and engineering manager together, within the outcome the team was given | The team's designer |
| A disagreement between the two executives | Both go to the CEO within five working days, with one page | Nobody |

The page settled what the drawings could not. Each of the eleven teams kept both an engineering manager and a product manager, and the two now shared one named decision, the team's quarter. The chart that followed kept two lines: engineering managers to the engineering directors and the VP Engineering, product managers to the CPO. In the quarter before the page, nine disagreements between product and engineering had reached Ines Okafor, each brought by one side. In the two quarters after it, four did, each brought by both with one page. The cost was time. The joint rows are negotiations, and in 2026 Corvane's quarterly planning took nine of the quarter's thirteen weeks. I read that in part as the price of joining by agreement; [[planning]] treats it in full.

## Where Design Reports

The CTO and the CPO were placed by asking where their decisions have to be joined. The same question gives a rule for the three other heads: a function reports where its decisions most often need to be joined with others. Design comes first of the three because its decisions meet product decisions most directly. A head of design is accountable for whether people can use what is built. The role reports either to the CPO or to the CEO as a third peer. Under the CPO, design decisions meet product decisions every day in one line, and the cost is that design can come to serve the roadmap. As a peer, usability has a voice equal to the other two, and the cost is a three-way negotiation at the top. This comparison is my judgment. Put the line where most of design's decisions are joined, and say what the other line would have given.

My sources add little here, and I say so plainly. *Build What Matters*, as my record [[right-team]] summarizes it, says only that design should become a function of its own as soon as the company can afford it, that designers should not report to individual product managers, and that design and product work as peers. A book on the subject exists, *Org Design for Design Orgs* by Peter Merholz and Kristin Skinner; it is not on my bookshelf. I have read only a 2016 interview in which Merholz describes its "centralized partnership", where all designers report through one design leader and work in teams that partner with product teams, and says the most senior designer should be no more than two levels from the CEO. At Corvane, Noor Achterberg, Head of Design from 2025, reports to Priya Nambiar. The stated cost is that design has no voice of its own in the executive team.

## Where Data Reports

Data is placed by the same rule, and it is harder to place because a head of data may hold three jobs. The first is the data platform: the pipelines and stores every team uses. The second is analysis for decisions. The third is data built into the product. Each joins with a different part of the organization. Under engineering, the platform is run like other shared services, and the cost is that analysis becomes a ticket queue for product. Under product, analysts sit with the decisions they inform, and the cost is a platform nobody engineers properly. A data executive of its own fits, in my judgment, only where data is what the company sells or a regulator requires the role, and it costs one more peer at the top.

My sources do not treat the data executive at all. Larson's chapter on the leadership team, as my record [[gelling-your-engineering-leadership-team]] summarizes it, names data only as one of the domains to check for when assembling that team. Everything else in this section is my judgment. Corvane in 2026 has no head of data. Its product analysts report into Priya Nambiar's organization, and the pipelines belong to the platform team under Lena Brandt, the Director of Platform. The cost is that no one person decides what a measure such as jobs completed on the first visit means in both places.

## Where Security Reports

Security follows the same rule with one difference: its head sometimes has to disagree with the executive it reports to. A head of security is accountable for stating risk and for the controls against it. Inside engineering, under the CTO or the VP Engineering, security decisions are joined with engineering decisions every day, and the cost is that the head of security reports to the person who may want a risk accepted. Outside engineering, under the CEO or a legal or operations executive, security is independent, and the cost is distance: a function that reviews from outside becomes a queue. This book calls that failure pattern the Review Bottleneck: finished work waits longer for approval than it took to make. In my judgment either line works if it has a direct path to the CEO for a risk that only the CEO can accept.

My sources mention security only in passing. Larson's *Primer* lists security engineering among the specialized roles inside engineering, counts security among the concerns that belong to the whole company, and gives "who's responsible for security at the company" as a question to ask before an acquisition. None of this says where the head of security should report. At Corvane a security lead has reported to Dario Vance since 2025. The two have a standing agreement: a risk that Dario Vance would accept and the security lead would not goes to Ines Okafor from both of them.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. AI adds joined decisions to the six roles' work. **Emerging.** As of November 2026, the organizations I have observed face a set of decisions that need product, engineering and security together: which coding agents and model providers to use, what data may leave the company, and what the product may do with a model. Where nobody at the top holds that join, each team decides for itself. Corvane's later story, told in Part XI, illustrates the result: by 2027 fourteen of its teams have each chosen their own agent, provider and conventions, and its security function cannot say what data leaves the company. This is my observation and not a measured result.

Whether these decisions call for a new role is open. **Speculative.** By the test of the first pattern, which asks what decisions a role joins once the name is removed, a head of AI is warranted only where there is a join that no existing role can make; a role created for a topic is a role built around something other than a decision. This would be confirmed if companies that appoint a head of AI can name decisions that the role joins and others could not. AI may also change which configuration fits: if agents shorten the distance between deciding what to build and building it, the speed of one combined executive may be worth more. That would be confirmed if combined product and technology executives become more common among companies that build mostly with agents.

## What to Take Away

**Established.** What the sources agree on:

- Executives who put their function before the executive team turn shared decisions into contests (Larson, *The Engineering Executive's Primer*; Lencioni's fifth dysfunction).
- Small gaps between executives become large ones for the people below them (Lencioni, *The Five Dysfunctions of a Team*).
- The engineering executive's role holds two jobs, technical execution and people management (Larson).

**Depends on context.** What changes with the situation:

- Which configuration fits. It depends on the hardest join, and the hardest join changes with size: Corvane used all three configurations in seven years.
- Where design, data and security report. It depends on which of their decisions are joined most often, and for data on which of its three jobs matters most.
- When product needs its own executive. *Build What Matters* gives a rule of thumb: several product managers, and a founder ready to hand over strategy.

**The author's synthesis.** What is this book's own position:

- The top holds two accountabilities and a join, and the three configurations are three places to put that join. The mapping of configurations to conditions is mine.
- What failed at Corvane each time was a join nobody had written down, and not the configuration: between Tomas Rell and everyone in 2019, between product and a busy CTO in 2024, between two peers in 2025.
- Design, data and security report where their decisions are most often joined, and a role made for a person is a cost to be stated, in decisions.

## Checklist

The checklist turns the two patterns and the reporting rule into eight questions about the top of an organization. One way to start is to list the decisions of the last two quarters that needed both product and engineering, and to mark where each waited.

- [ ] Accountabilities: can you name the one person accountable for what is built and the one accountable for how it is built and run?
- [ ] Joined decisions: have you listed the decisions of the last two quarters that needed both, with how long each waited?
- [ ] Hardest join: what had to meet in the decisions that waited longest or were reopened, product with engineering or technical direction with running the organization?
- [ ] Configuration: does your configuration put a person or a written agreement on that join, and can you say what it gives up?
- [ ] The page: have the peer executives written who decides what, who must be heard first and what they decide together?
- [ ] Escalation: do disagreements reach the CEO from both executives together, within an agreed number of days?
- [ ] Persons: for each executive role, which decisions does it join once the name is removed?
- [ ] Design, data, security: for each, where are its decisions joined most often, and what does the chosen line cost?

Corvane's two drawings asked who leads a team, and the answer that worked was a list of who decides what. The last line of that list reaches below the executives: a team's product manager and engineering manager decide the quarter together, after hearing the designer. The joining of what is built with how it is built does not stop at the top. The next chapter follows it, with design, through every level down to the team: [[the-product-engineering-design-triad]].

## Sources and Evidence

**Books**

- *The Engineering Executive's Primer*, Will Larson, 2024. The definition of the engineering executive; executives focused on their function and zero-sum allocation; the leadership team as a "first team"; onboarding a peer executive; structured escalation, which Larson credits to LinkedIn; the passing mentions of security.
- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. "Make your peers your first team", addressed to managers.
- *The Five Dysfunctions of a Team*, Patrick Lencioni, 2002. Inattention to results; small gaps between executives growing below them. The phrase "first team" is usually credited to Lencioni and is not in the author's notes on this book.
- *The Four Obsessions of an Extraordinary Executive*, Patrick Lencioni, 2000. A cohesive leadership team as the first discipline; background to the first-team pattern.
- *Build What Matters*, Ben Foster and Rajesh Nerlikar, 2020. The Throne Room; through the author's record, when a product executive is needed and design as a peer function.
- *Org Design for Design Orgs*, Peter Merholz and Kristin Skinner, 2016. Not read; named as the book on the design organization. It supplements the author's sources.

**Practitioner sources**

- "Getting the most from your design team", Mary Treseler's interview with Peter Merholz, O'Reilly, 2016. The centralized partnership and the two-levels remark; read for this chapter.
- The author's records in Grounded Engineering Executive: [Working with Your CEO, Peers, and Engineering](../grounded-engineering-executive/working-with-your-ceo-peers-and-engineering.html), [Onboarding Peer Executives](../grounded-engineering-executive/onboarding-peer-executives.html) and [Gelling Your Engineering Leadership Team](../grounded-engineering-executive/gelling-your-engineering-leadership-team.html); and in Grounded Product Management: [The Right Team](../grounded-product-management/right-team.html).
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
