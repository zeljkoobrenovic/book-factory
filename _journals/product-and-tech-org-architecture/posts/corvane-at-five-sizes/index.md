---
title: "Meet Corvane: One Company at Five Sizes"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Which company do the book's examples come from, and what happens to it as it grows? Corvane is a fictional maker of field-service scheduling software, followed from 12 to about 1,100 people in five stages, each with a structure that made sense when it was built and an incident that came when growth moved on without it."
permalink: corvane-at-five-sizes
timetoread: 14 min read
---

> **KEY POINTS:**
>
> * **Corvane is fictional.** It is an invented company that makes scheduling software for field-service firms. Every figure, name and incident on this page was made up for the book and is kept in one record, so no number here is data about a real company.
> * **Five stages, and each structure was a reasonable answer.** Corvane grows from 12 people to 50, 180, 500 and about 1,100. At each size its structure answers the problem in front of the company when it was built, and the incident of that stage comes where growth has since made something else scarce and the structure has stayed.
> * **Each incident is matched to a failure pattern.** The eight named incidents, from the Founder Queue to the Hiring Question, each get a date, a size and a pattern from the previous page: the one that best explains the incident or, for the Hiring Question, the one it risks. Use this page as the lookup when a chapter cites one.

<br>

The previous page named twelve ways in which a product and tech organization fails ([[where-product-and-tech-organizations-go-wrong]]). This page gives the one company in which the book shows those failures happening: Corvane. **Corvane is fictional.** It is not a disguised portrait of a real company. Every figure, name and incident here was invented for the book, and every number is an illustration, never a measurement. All of it is kept in one record, a ledger of Corvane's facts that is maintained alongside the book. Each chapter follows the ledger and may only add to it, and this page is the ledger in readable form. That is what lets a chapter refer to "the Launch Queue" or "Corvane at 500 people" in a phrase and mean the same thing as every other chapter.

Corvane is followed through five sizes, from 12 people to about 1,100. The page's claim is about what those five sizes have in common. **At each size the structure was a reasonable answer to the problem in front of the company when it was built.** Each named incident happened where growth had since made something else scarce and the structure had stayed as it was. None of the incidents needed a careless person. The page gives the company in five steps: the product, the five stages, the cast, the incidents matched to failure patterns, and a table of where the chapters use each stage and incident.

## Corvane and Its Product

Corvane was founded in Rotterdam in 2018. It sells scheduling and dispatch software to field-service companies: firms whose technicians install and repair heating systems, maintain lifts or install telecom lines at customers' sites. The product has three parts. Planners in the customer's office use a **web application** to assign jobs to technicians. Technicians use a **mobile app** to see their day, travel to each job and mark it done. **Integrations** pass finished jobs to the customer's billing system and parts used to its stock system. Customers pay per technician per month.

This product suits the book for one reason. A single scheduling rule has to hold in all three parts. A job assigned in the office must appear on the technician's phone, and a job finished on the phone must reach the billing system. If the teams that build the three parts understand a rule differently, nobody needs a report to find out. A planner and a technician look at two different schedules the same morning. At Corvane a gap between two teams becomes **a fault that a customer can see**, and that makes the organization's structure visible in a way it rarely is in real life.

## Five Stages, 2018 to 2028

Each stage below is read by asking which of three capacities was running short. The introduction named them, and they are the book's own terms. **Attention** is how much a team can hold in mind well enough to change it safely. **Judgment** is deciding with the relevant information at hand. **Verification** is knowing that what was built is right. A company always has a limited amount of each, and growth changes which one runs out first.

Corvane's ten years run from one team of 12 people in 2018 to two business units of about 1,100 people in 2028. They divide into five stages, and each stage ends in at least one incident that Corvane's people later gave a name.

---begin mermaid---
flowchart LR
    S1["1. One table<br/>2018–2019<br/>12 people<br/>The Founder Queue"] --> S2["2. First teams<br/>2020–2021<br/>50 people<br/>The Two Calendars<br/>The Second Calendar, 2022"]
    S2 --> S3["3. The hiring wave<br/>2022–2024<br/>180 people<br/>The Launch Queue"]
    S3 --> S4["4. Groups and plans<br/>2025–2026<br/>500 people<br/>The Nine-Week Plan<br/>The Tuesday Reorg"]
    S4 --> S5["5. Scale and AI<br/>2027–2028<br/>1,100 people<br/>The Review Wall<br/>The Hiring Question"]
---end mermaid---

**Figure 1:** *Corvane's five stages in order, each with its years, the size of the whole company and the incidents it is remembered for.*

The table gives the same five stages in full. "Product and tech" counts the engineers, product managers and designers, the part of the company this book is about. The last two columns are the ones later chapters cite most.

| Stage | Years | Whole company | Product and tech | Structure | What ran short | Named incidents |
| --- | --- | --- | --- | --- | --- | --- |
| 1. One table | 2018–2019 | 12 | 8 | One team, no managers; the two founders decide everything | Nothing at first; at the end, the founders' judgment | The Founder Queue |
| 2. First teams | 2020–2021 | 50 | 28 | Four teams; two engineering managers; the first product manager | Attention | The Two Calendars; the Second Calendar (2022) |
| 3. The hiring wave | 2022–2024 | 180 | 95 engineers, 11 product managers, 7 designers | Eleven product teams cut by headcount; one platform team of five; a VP Engineering | Verification, and the platform team's attention | The Launch Queue |
| 4. Groups and plans | 2025–2026 | 500 | 260 | Four product groups with directors; a CPO; annual and quarterly planning; a career ladder; an architecture forum | Judgment | The Nine-Week Plan; the Tuesday Reorg |
| 5. Scale and AI | 2027–2028 | about 1,100 | 520 | Two business units after an acquisition; coding agents in every team; an AI enablement team | Verification and judgment | The Review Wall; the Hiring Question |

**Stage 1, One table (2018–2019, 12 people).** Eight of the twelve work on the product, as one team with no managers. Ines Okafor, co-founder and CEO, sells and looks after the first customers. Tomas Rell, co-founder and CTO, builds. The two founders decide everything, and the decisions about the product fall to Tomas. The arrangement works because everyone sits within earshot: nobody has to be told what a customer said or what changed yesterday. It stops working at one point only. By 2019 every pricing, design and release decision waits for Tomas, and engineers start a second piece of work while the first waits for his answer. Corvane calls this **the Founder Queue**. Tomas decides well. There is one of him, and judgment has run out at his desk.

**Stage 2, First teams (2020–2021, 50 people).** Corvane's answer to the queue is to stop routing everything through the founders. The 28 people in product and tech form four teams, Web, Mobile, Integrations and Core, under the first two engineering managers. Priya Nambiar joins in 2020 as the first product manager and Noor Achterberg as the first designer. Decisions now get made where the work is. What nobody has any longer is the whole product in their head, so the shortage moves from judgment to attention. In 2021 Web and Mobile each build the rule for overlapping jobs, and for three weeks planners and technicians see different schedules: **the Two Calendars**. The review blames communication and the Mobile lead is replaced. Eight months later, in 2022, Mobile and Integrations diverge on job status in the same way, and a job marked complete on the phone stays open in customers' billing exports for eleven days: **the Second Calendar**. Only then does Corvane give the rules one home and one decider: they move into a single rule engine owned by the Core team, and Priya Nambiar decides what the rules are. The failure does not come back. The Second Calendar falls in the first year of the next stage, and it is told here because it is the same failure.

**Stage 3, The hiring wave (2022–2024, 180 people).** This is the stage the book's introduction opened with. By 2022 Corvane has 45 engineers and customers who ask for more than 45 can build. The answer looks obvious: hire. In eighteen months the engineers more than double, from 45 to 95. In 2023 they are divided evenly into eleven product teams of about eight, and the platform team, five engineers led by Lena Brandt since it was formed in 2022, handles releases for all of them. Dario Vance joins as VP Engineering that year, after the hiring plan is agreed. Two things about this stage have no name at Corvane, and later chapters use both. One is **the even split**: the eleven teams are cut by headcount, and nobody states what the new structure is meant to achieve. The other is **the forty-one features**: in one year Corvane ships forty-one features, each promised to a customer by name, and its renewal rate falls, so the added hands are busy and customers are no better served. Then comes the incident that has a name. The median lead time for a change, measured from starting work on it to its release, goes from 4 days to 19. About two of the 19 days go into writing the change. The rest is waiting: all eleven teams need the platform team for some launches, three need it for every launch, and at the peak 14 launch requests are open. This is **the Launch Queue** of 2024. Corvane had added people to the step that writes changes. The shortage was in the step that checks and releases them: verification had run out, and with it the attention of five platform engineers serving eleven teams. In 2024 Dario Vance tests a release path that one team can run without Platform, and three quarters later the company-wide median is under 7 days. One problem is left open. With the queue gone, the longest wait at Corvane is for someone to say that a feature is ready, and nobody has that decision.

**Stage 4, Groups and plans (2025–2026, 500 people).** The problem stage 3 left open is the one this stage sets out to solve: eleven teams, and nobody to decide what no single team can. Who says a feature is ready is one such question. Another is technical. By 2025 the eleven teams run four ways of deploying, three message brokers and two identity libraries, each a reasonable choice for the team that made it. Corvane's answer is a set of structures for deciding across teams. It forms four product groups, each under a director. Priya Nambiar becomes Chief Product Officer. Annual and quarterly planning, a career ladder and an architecture forum follow. The cost is distance. The people who now decide are two or three levels away from the information the decision needs, and judgment runs short again, this time because the people deciding lack the information, where in stage 1 the one person deciding lacked the time. Both incidents of the stage show it. A quarterly plan has to be agreed across the four groups before any of it is fixed, and that takes nine of the quarter's thirteen weeks: **the Nine-Week Plan**. And a reorganization is drawn up by people who do not know what each team runs. It is announced without a plan for moving that work, and two teams lose their on-call rotation: **the Tuesday Reorg**, named for the day of the announcement.

**Stage 5, Scale and AI (2027–2028, about 1,100 people).** Corvane acquires Routewise, a route-optimization company of 140 people, and becomes two business units. Coding agents are in use in every team, and an AI enablement team supports them. Writing a change becomes cheap. Checking one does not. From January 2027 to January 2028 the number of merged changes per week rises 2.4 times while review capacity stays flat, and the median wait for a review goes from 5 hours to 31: **the Review Wall**. The shortage is verification once more, as in stage 3, and it sits at a different step. The Review Wall then raises a question of judgment that no earlier stage had to ask. If writing is cheap and review is the limit, more engineers who write would only lengthen the wait. So the 2028 plan asks whether Corvane should hire engineers at all: **the Hiring Question**.

Read together, the five stages have one shape. Each structure answered the problem in front of Corvane when it was built. Teams and managers ended the queue at the founder. Hiring added hands when there was more to build than people to build it. Groups and plans gave eleven teams someone to decide across them. The last change, coding agents, was not an answer to anything at Corvane; it arrived from outside and made writing cheap. And each time, growth then made something else scarce, in a place the structure had not been built to watch: in the rules between teams, at the launch, in the distance between a decision and its facts, at the review. **Each structure was right for the problem it was built for and wrong once the shortage had moved.** The book's chapters explain why. On this page it is enough to see it happen at every size.

## The Cast

Seven people are named in the book. The table gives each one's role, with the year it began where that matters, and where the chapters most often meet them.

| Person | Role | Where the chapters meet them |
| --- | --- | --- |
| Ines Okafor | Co-founder and CEO | With Tomas Rell, decides everything in stage 1 |
| Tomas Rell | Co-founder and CTO | The Founder Queue, 2019 |
| Priya Nambiar | First product manager (2020); Chief Product Officer from 2025 | Decides what the scheduling rules are, from 2022 |
| Dario Vance | VP Engineering, joined 2023 | Leads the 2024 response to the Launch Queue |
| Lena Brandt | Leads the platform team from 2022; Director of Platform from 2025 | The platform team in the Launch Queue |
| Samir Haddad | Staff engineer, at Corvane since 2019 | In stage 2, the only engineer who understands both the engine that computes schedules and the code that keeps the mobile app in step with the office |
| Noor Achterberg | First designer (2020); Head of Design from 2025 | Design, from stage 2 onward |

The cast are roles. They are not culprits. Most of the seven are at Corvane through several stages, and the incidents happen around them all the same. Tomas Rell is there for the Founder Queue and for the Review Wall. Samir Haddad has been at Corvane since 2019, through every named incident. **No incident in this book is explained by one of them failing at the job.** One person does lose a job over an incident: the lead of the Mobile team, replaced after the Two Calendars in 2021. The book leaves him without a name on purpose, because his successor met the same failure eight months later. A change of person did not change the result.

Teams are also referred to by name, and the names tell you the stage. Web, Mobile, Integrations and Core are the four teams of stage 2. Core is dissolved when the eleven teams are formed in 2023, and its work is divided among them; the rule engine goes to the Scheduling and Dispatch teams. From stage 3 the eleven product teams are Scheduling, Dispatch, Technician App, Customer Portal, Billing Integrations, Stock Integrations, Reporting, Onboarding, Identity, Notifications and Growth, and the twelfth team is Platform. From stage 5 the chapters also mention the Routewise teams and AI Enablement.

## The Incidents and the Patterns Behind Them

The previous page sorted its twelve failure patterns into four families, one for each thing a leader can design directly. **Boundaries** are what each team owns. **Interfaces** are the agreed ways in which work and knowledge cross between teams. **Decision rights** say who may decide which kind of question. **Incentives** are what gets measured and rewarded. A pattern is a way of getting one of the four wrong. An incident is a dated event at Corvane. Most of the cases in the table below are one of those patterns with a date and a size. The last, the Hiring Question, is a decision still to be made.

The table matches ten of Corvane's cases to patterns: the eight named incidents and the two unnamed cases of stage 3, the even split and the forty-one features. Where a case shows more than one pattern, the table gives the one that best explains it.

| Case | Stage, year and size | What happened | Primary pattern | Family |
| --- | --- | --- | --- | --- |
| The Founder Queue | 1; 2019; 12 people | Every pricing, design and release decision waits for one founder | The Escalation Ladder | Decision rights |
| The Two Calendars | 2; 2021; 50 people | Two teams each build the rule for overlapping jobs; planners and technicians see different schedules for three weeks | The Unowned Interface | Interfaces |
| The Second Calendar | 2 into 3; 2022 | The same failure between two other teams, after the person blamed was replaced; finished jobs stay open in billing for eleven days | The Unowned Interface | Interfaces |
| The even split | 3; 2023 | Eleven product teams are formed by dividing people evenly, with no outcome stated | The Org Chart as Architecture | Boundaries |
| The forty-one features | 3; one year of the stage | Forty-one features ship, each promised to a named customer, and the renewal rate falls | The Feature Factory | Decision rights |
| The Launch Queue | 3; 2024; 180 people | Launches wait at a platform team of five; median lead time goes from 4 days to 19 | The Review Bottleneck, with the Overloaded Team behind it | Interfaces |
| The Nine-Week Plan | 4; 2025–2026; 500 people | Quarterly planning takes nine of the quarter's thirteen weeks | The Consensus Stall | Decision rights |
| The Tuesday Reorg | 4; 2025–2026; 500 people | A reorganization is announced without a migration plan; two teams lose their on-call rotation | The Reorg as Strategy | Boundaries |
| The Review Wall | 5; 2027–2028; about 1,100 people | Merged changes rise 2.4 times, review capacity stays flat, and the median review wait goes from 5 hours to 31 | The Review Bottleneck | Interfaces |
| The Hiring Question | 5; 2028; about 1,100 people | The 2028 plan asks whether to hire engineers at all | A decision, not a failure; the pattern it risks is the Output Scoreboard | Incentives |

Three things about this table need saying. First, one pattern per case is a simplification. The Launch Queue is filed under the Overloaded Team, because five engineers owned the release of eleven teams' work, and it is also a queue for checks, which is the Review Bottleneck. Later chapters name the second pattern where their argument needs it. Second, the cases touch all four families, and the incentives family only as a risk: the Hiring Question goes wrong if it is answered by counting merged changes. Third, three patterns have no case in the table: the Platform Nobody Asked For, the Ladder as Checklist and the Hero Culture. The last of these has a sign at Corvane without an incident, in Samir Haddad as the only engineer who understood two systems in stage 2. I have not invented incidents to fill the gaps.

## Where the Chapters Use Corvane

The last table runs the other way, from a place in the book to the stage and the cases it draws on. The first row is the introduction and the five rows after it are the chapters of Part I; these six describe pages already written. For Parts II to IV the row gives the scene the part opens with. For Parts V to XI the row gives the stage the part's subject belongs to, and the chapters there settle which cases they use.

| Where in the book | Stage | What it uses |
| --- | --- | --- |
| [Introduction](introduction.html) | 3 | The hiring wave, as the book's opening puzzle |
| [[the-organization-as-a-system]] | 2 | The Two Calendars and the Second Calendar; the 2022 fix |
| [[the-organization-as-a-product]] | 3 | The hiring wave as a reorganization with no stated outcome; the 2024 response |
| [[conways-law-and-the-inverse-conway-maneuver]] | 2 and 3 | The Two Calendars; the rule engine of 2022; the eleven teams of 2023 |
| [[cognitive-load-and-team-boundaries]] | 2 and 3 | The Core team in 2022; the eleven teams cut by headcount |
| [[flow-and-the-constraint]] | 1 to 3 | The Founder Queue; the Launch Queue, measured by its waits |
| Part II, teams and their interfaces | 3 | The platform team of five and the eleven teams it served |
| Part III, the product operating model | 3 | The forty-one features |
| Part IV, the engineering operating model | 4 | The 2025 landscape: four ways of deploying, three message brokers, two identity libraries |
| Part V, leadership | 3 and 4 | The VP Engineering of 2023; the CPO and the directors of 2025 |
| Part VI, decisions and planning | 1 and 4 | The Founder Queue; the Nine-Week Plan |
| Parts VII to IX, talent, health and culture | 3 to 5 | The career ladder of stage 4; the lead-time and review-wait figures |
| Part X, scaling and reorganizing | All five | The stages themselves; the Tuesday Reorg; the Routewise acquisition |
| Part XI, AI and the organization | 5 | The Review Wall; the Hiring Question |

Chapters cite Corvane by a fixed convention, so that a scene can be placed without turning back to this page. A scene gives the incident's name or the year, and the size of the company at the time. A person gets their role the first time they appear in a chapter. A chapter may add detail to the record: what was decided, what the fix was, what it cost. It may not change a fact that another chapter has used. That rule is why a figure on this page means the same thing wherever you meet it.

## What to Take Away

**Fixed.** What does not change between chapters:

- Corvane is fictional, and so is every person, figure and incident attached to it.
- The product, the five stages with their years and headcounts, the seven people and their roles, and the eight named incidents.
- The stated figures: lead time from 4 days to 19 in stage 3; five platform engineers for eleven teams; merged changes up 2.4 times and review wait from 5 hours to 31 in stage 5.

**Added by later chapters.** What is still to come:

- The detail each argument needs: what Corvane decided after an incident, what the change cost and how it was judged.
- Further cases for the three patterns that have none here, where a chapter needs one.
- The choice of cases in Parts V to XI, which the last table gives only by stage.

**How to use this page.** When a chapter cites Corvane:

- Place the incident by its stage in the first table, and read the size and the shortage from the same row.
- Read its pattern and family from the incident table, and expect the chapter to name a second pattern where it matters.
- Treat every Corvane number as an illustration. Evidence about real organizations is cited separately in each chapter, with its source.

Three pages of this preface work as one instrument: the introduction, the failure patterns and this page. The introduction's claim says what can be designed: boundaries, interfaces, decision rights and incentives, arranged around attention, judgment and verification. The patterns say how that design fails. Corvane gives each failure a date and a size. The hiring wave that the introduction opened with is no longer a puzzle standing alone. It is stage 3 of five, at 180 people. The book's chapter on scaling treats it as the stage between about 150 and 300 people. The stage before it explains where the teams came from, and the stage after it explains why the plans arrived.

You can now say in plain words what went wrong at Corvane at each size: a queue at a founder, a rule with two versions, a wait at the launch, a plan that took most of its quarter, a wall of reviews. Before going on, ask which of these your own organization has had, and at what size. What plain words do not yet give is the reason. Why did capable people, in a structure that had worked, produce each of these results? Part I answers with the vocabulary and the reasoning that explain why structure produces behavior: [Part I — FOUNDATIONS: The Organization as a System](part-1.html).

## Sources and Evidence

Corvane, Routewise and every person named on this page are fictional. Every figure is an illustration invented for the book and is not data about any company. The facts are kept in one record that all chapters follow.

- The twelve failure patterns and their four families: [[where-product-and-tech-organizations-go-wrong]].
- Attention, judgment and verification are named in the [introduction](introduction.html) and treated in full in [[flow-and-the-constraint]].
- The matching of incidents to patterns is the author's reading.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
