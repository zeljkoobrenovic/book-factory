---
title: "Team Size and Composition"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How large should a team be, and who should be in it? As large as its scope, its on-call rotation and its coordination require, which gives six to eight engineers only under stated assumptions, with the roles its decisions would otherwise wait for."
permalink: team-size-and-composition
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to derive a team's size from its scope, its on-call duty and its coordination cost, and to decide which roles belong inside it.

> **KEY POINTS:**
>
> * **A size is a result.** It lies between two floors, the people needed to understand what the team owns and to sustain its on-call rotation, and one ceiling, the size at which a team stops coordinating as one group.
> * **Six to eight has assumptions.** Will Larson's numbers are rules of thumb for teams that write and operate their own services; change the scope, the duty or the cost of producing a change and the number changes.
> * **Composition follows waiting.** Product, design and engineering sit in one team wherever a decision would otherwise wait for another team, and a team below a floor grows, sheds scope or merges.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Overloaded Team** — a team sized by budget or by history carries a duty its headcount cannot sustain.
> * **The Org Chart as Architecture** — when every team gets the same number, boundaries follow the headcount.
> * **The Hero Culture** — a team of two or three works only while particular people are available.

<br>

In 2024 every engineer on Corvane's platform team was on call two weeks in every five. To be **on call** is to be the person who must answer alerts from production at any hour. In August, with one colleague on holiday, it was every second week. Corvane is the fictional company this book follows, and it had 180 people that year. The platform team had five engineers, and nobody at Corvane could say why five. The eleven product teams had about eight engineers each, and the reason for that number was division: about ninety engineers, eleven teams. If your own team's size came from a budget line or from a number nobody has looked at since, you know both cases, and you have probably heard the right answer quoted as six to eight.

A size that was never derived cannot be defended when it is right or corrected when it is wrong. The two previous chapters settled what a team is for and how other teams reach it, which decides what it owns and how much of its time others consume. From that, this chapter derives how many people it needs, and which roles. **A team should be as large as three things require and no larger**: enough people to understand and change what it owns without depending on one of them, enough to sustain its on-call rotation, and few enough to coordinate without splitting into sub-teams. For teams that write and operate their own services, that gives Will Larson's six to eight engineers with one manager, and a different number when the scope, the on-call duty or the cost of producing a change is different. Composition follows the same logic: product, design and engineering sit together wherever a decision would otherwise wait for another team. The chapter starts with Corvane's two sizes, sets out the two floors and the ceiling, and gives a pattern for deriving a size and one for a team that is too small. It then turns to composition, to where the sources disagree, and to two habits that get sizing wrong. It sizes Corvane's platform team, says which input AI changes and, closing Part II, reads that team as a type, a mode and a size.

## Setting the Scene: Two Team Sizes Nobody Derived

The eight dates from Corvane's reorganization of 2023 ([[cognitive-load-and-team-boundaries]] tells that story), when about ninety of its engineers were divided evenly into eleven product teams. The five is older. The twelfth team was the platform team, led by Lena Brandt, which Corvane had formed in 2022 to take release and infrastructure work off the other teams. It had five engineers when it was formed, when Corvane had about 45 engineers in all. It still had five when the engineers it served had doubled, and nobody had looked at the number again.

What five meant showed in the team's weeks. The platform team operated the shared infrastructure and the release tooling around the clock, in a **two-tier rotation**: each week one engineer was the primary, who answered alerts first, and another was the secondary, who took over when the primary could not be reached. Two of the five were therefore on call in any week, and each engineer was on call two weeks in every five. In August 2024 one of them took three weeks of holiday, and the other four were on call every second week. The same five also checked and released launches for the eleven product teams, and at the peak that year fourteen launch requests waited for them ([[flow-and-the-constraint]] follows that queue).

The product teams' eight caused no such trouble. A product team also ran a two-tier rotation, for its own services, and with eight engineers each of them was on call two weeks in eight. So one of Corvane's two sizes worked and the other did not, and the company could explain neither. Both numbers had been inputs to the design, one from division and one from history, and neither came from asking what the team had to do. So what should a team's size be derived from?

## Two Floors and a Ceiling: What Sets a Team's Size

A team's size is the result of three requirements. Two of them are **floors**, numbers the team must not fall below: enough people to understand and change what it owns, and enough to sustain its on-call rotation. The third is a **ceiling**: few enough people that the team can coordinate as one group. The size lies between the higher of the two floors and the ceiling. Where it lies between them depends on a fourth quantity: how much work the scope demands, at the current **cost of producing a change**, the effort it takes to write, test and release one. The frame of two floors and a ceiling is mine; the numbers that fill it in are Will Larson's, from *An Elegant Puzzle*. The figure shows the derivation.

---begin mermaid---
flowchart LR
    S["Scope: what the team owns"] --> U["Understanding floor: every part can be changed by at least two people"]
    O["On-call duty: hours and tiers"] --> R["Rotation floor: enough trained people for every tier"]
    U --> F["The higher of the two floors"]
    R --> F
    C["Coordination inside the team"] --> X["Ceiling: the size at which sub-teams form"]
    F --> Z["Team size: between floor and ceiling"]
    W["Work the scope demands, at the current cost of producing a change"] --> Z
    X --> Z
    Z -->|"floor above ceiling"| T["Too much for one team: shed, share or split"]
---end mermaid---

**Figure 1:** *A team's size is derived from its scope, its on-call duty, its coordination cost and the work the scope demands, and a floor that comes out above the ceiling means the team owns too much.*

The first floor is understanding. [[cognitive-load-and-team-boundaries]] gave the test for ownership: a team owns a thing only when its members can change it and operate it without relying on one particular person. So every part the team owns needs at least two people who can change it safely, and the wider the scope, the higher the floor. There is also a minimum whatever the scope, which Larson puts at four: "Teams with fewer than four individuals are a sufficiently leaky abstraction that they function indistinguishably from individuals." His reason is that such a team cannot be planned as a unit: to reason about its delivery you have to know about each on-call shift, vacation and interruption. He has sponsored teams of one or two people and regretted it every time. Below about four a team has no redundancy, and one absence removes a skill.

The second floor is the on-call rotation, and for a team that operates its own services it is usually the higher of the two. Larson gives a number for the two-tier case: "My rule of thumb is that it takes eight engineers on a team to support a two-tier on-call rotation". He gives the number; the arithmetic that follows is mine. With two tiers and *n* engineers, each engineer is on call two weeks in every *n*. Eight gives one week in four, six one week in three, five two weeks in five. Where the duty stops being sustainable is a judgement, and mine is one week in three: six engineers is the least a two-tier rotation can run on, and Larson's eight leaves room for holidays and for his other rule, that only trained engineers can go on call.

The ceiling pushes the other way, and it comes from coordination. A team of *n* people contains *n*(*n*−1)/2 pairs: five people have 10 pairs, eight have 28 and twelve have 66. Two people in a pair have to keep each other informed, so the cost of coordinating grows much faster than the headcount. Past a certain size a team splits informally into sub-teams, and the dependence on a few people returns. The manager is the second reason for a ceiling. Larson's rule of thumb is that a manager supports six to eight engineers, with a reason for each end of the range. Managers who support more than eight or nine act as coaches and safety nets, too busy to invest in the team or its area. Managers who support fewer than four tend to become tech lead managers, who take on a share of the design and implementation work.

For a team that writes and operates its own services, the requirements meet in a narrow range: an understanding floor of at least four, a rotation floor of six at the least and eight to be safe, and a ceiling of about eight engineers with one manager. That is where Larson's best-known number comes from: "Teams should be six to eight during steady state." The table gives his rules of thumb with his reasons; the last column, what each assumes, is my reading.

| Larson's rule of thumb | His reason | What it assumes |
| --- | --- | --- |
| A manager supports six to eight engineers | Below four the manager becomes a tech lead manager; above eight or nine, a coach and safety net | A full-time people manager |
| Three to five engineers when the manager does hands-on technical work | The manager's time is divided | The manager is expected to write code or design |
| About eight engineers for a two-tier on-call rotation | His rule of thumb for sustaining the rotation | The team operates its own services around the clock, in two tiers, with trained engineers |
| Fewer than four people is not a team | It functions like individuals and cannot be planned as a unit | The team is meant to be planned as a unit |

The reasoning carries over to other teams, and the numbers do not. A team with no duty around the clock has only the understanding floor, and four or five people can be right for it. A team whose scope has more parts than eight people can cover two deep has a floor above its ceiling, and needs less scope, not twelve people. And between floor and ceiling, the scope a given number of engineers can carry depends on the cost of producing a change, which is the input AI moves and which a later section takes up. Six to eight is a result, and it holds where its assumptions hold.

## Pattern: Derive the Size from Scope and On-Call

The requirements become a pattern for any team. Its user is the manager of the team, together with the leader who approves its headcount. Its outcome measures are two numbers: the share of weeks each engineer is on call, and the number of parts of the scope that only one person can change safely. It has five steps.

1. List what the team owns and operates, part by part. Its type and its interaction modes ([[team-types]], [[interaction-modes-and-team-apis]]) say what belongs on the list.
2. For each part, count the people who can change it safely. The understanding floor is the smallest team in which every part has at least two, and it is never below four.
3. Write down the on-call duty, its hours and tiers, and set the rotation floor. For two tiers around the clock, start from Larson's eight.
4. Take the higher floor and compare it with the ceiling of about eight engineers with one full-time manager. Between the two, add engineers only for the work the scope demands at the current cost of producing a change.
5. If the floor is above the ceiling, or above what you can staff, change the scope or the duty. Record the assumptions next to the number.

Larson also says how a team gets to its size. New teams are grown, not assembled. He grows an existing team to eight to ten and lets it bud into two teams of four or five, so that each half starts with people who already work together and climbs back toward six to eight. The ten and the four are passing states, briefly above the ceiling and briefly at the understanding floor. He adds a prohibition: no empty teams, meaning teams created before they have their people.

## Pattern: Grow, Shed or Merge a Team That Is Too Small

The derivation will sometimes show a team below one of its floors, and then there are three remedies. This pattern's user is the leader responsible for that team. Its outcome measure is that the team passes both floors again by a date set with the remedy. Which remedy fits depends on which floor is broken and on who else could carry the work.

| Remedy | What it changes | What it costs | Fits when |
| --- | --- | --- | --- |
| Grow | Raises the team to its floor | Months of hiring and training before a new engineer counts on the rotation | Nobody else can understand or operate the scope, and the scope will stay |
| Shed or share scope and on-call | Lowers the floor: a service moves to another team, or two teams that know each other's systems share one rotation | The receiving team carries more and has to learn it | Part of the scope belongs elsewhere, or a neighboring team already understands the systems |
| Merge | Two teams below the floor become one team above it | One wider scope to understand; one team ends | The two scopes are adjacent, and neither team can reach its floor alone |

One remedy is missing from the table because it does not work: headcount that never reaches the team. Engineers hired into other teams do not understand this team's parts and do not carry its pager, so a company can grow by a hundred people while one team stays below its floor. A half-time share of an engineer from elsewhere fails for the same reason. Borrowing a person outright fails in another way. Larson observes that teams have high fixed costs, so that moving one person out can set a healthy team back. The loan repairs one team by damaging another. His alternative is the second row of the table: "I've found it most fruitful to move scope between teams, preserving the teams themselves." The scope moves and the people stay.

## Composition: The Roles a Decision Would Otherwise Wait For

Composition, meaning which roles are in the team, is derived the same way as size. Size asked how many people a team needs so that its work does not wait for one person; composition asks which roles it needs so that its decisions do not wait for another team. Besides how to build, a product team keeps deciding what to build next and how it should work for the user. If the role that makes one of those decisions sits outside the team, each decision becomes a request to another team and waits there. So the roles those decisions need, product management, design and engineering, belong inside the team. The product sources agree. In *Empowered*, Marty Cagan and Chris Jones put product managers, designers and engineers in one team and warn against treating design as an internal service. In *Build What Matters*, Ben Foster and Rajesh Nerlikar make design a peer of product management.

How much of a role a team needs depends on how often its decisions need that role, and the sign that it has too little is a particular kind of waiting, as the table shows. For the proportions, *Build What Matters* offers a starting ratio for one product team: "5 to 7 Developers (your base value) 1 Product Manager 0.5 UX Designer (variable depending on the nature of the product) 0.3 UI Designer (variable depending on the nature of the product) 1 or 2 Quality Assurance Engineers". The ratio says of itself that it varies with the product: like Larson's numbers, it is a rule of thumb with assumptions. Its quality assurance engineers are left to [[quality-and-reliability]], and the table adds data, which the ratio omits.

| Role | The decisions it brings | Sign that the team has too little of it | Full-time or shared |
| --- | --- | --- | --- |
| Engineering | How to build, change and operate the product | Nothing ships | The core of the team, sized by the derivation |
| Product management | Which problem comes next, and what counts as done | Engineers guess priorities or wait for an answer | One per team |
| Design | How it should work for the user | Screens wait for a designer, or ship without one | In the team where the user interface changes often; shared where it seldom does |
| Data, where needed | Whether a change produced its outcome | Nobody can say whether a release worked | In the team when its decisions rest on usage data it cannot read itself |

Corvane shows what a shared role costs. In 2024 its eleven product teams had 11 product managers and 7 designers. Every team had a product manager of its own. Three teams had a designer of their own, and the other four designers each worked for two teams. In those eight teams a decision about how a screen should work waited for the designer's days with the team. On the staffing plan each of the eight teams had half a designer. In its working week each of them had a queue.

## Where the Sources Disagree: Six to Eight of What, and Why Not Fewer

Read as answers to one question, how large a team should be, Larson's numbers and the *Build What Matters* ratio do not agree, and a third and better-known answer disagrees with both. Larson says six to eight engineers. The ratio adds up to about eight to eleven people. And the two-pizza rule, widely attributed to Amazon, says that a team should be small enough to be fed by two pizzas. I cite it only as the widely known rule; it is not among this book's sources. It is the usual support for the view that smaller teams are faster and should be kept as small as possible.

The three answers differ because they count different things and guard different bounds. Larson counts the engineers one manager supports, and his rules guard both floors and the ceiling. *Build What Matters* counts the whole product team around those engineers. The two-pizza rule names a maximum only: it guards the ceiling and is silent about the floors. My resolution uses each for what it counts. The floors and the ceiling in this chapter count engineers, as Larson does, and on that count the ratio's five to seven developers is close to his six to eight. The product manager and the designers come on top. And a rule that gives only a maximum is not advice about the minimum.

What the small-team view leaves out is what a team gives up as it shrinks. A smaller team gains cheaper coordination and gives up redundancy, so smaller is faster only where there is little to be redundant about: a narrow scope and no rotation to sustain. The table sets out the trade by size.

| Engineers | What the team gains | What it gives up | Right when |
| --- | --- | --- | --- |
| Two or three | Almost no coordination | All redundancy: one absence stops a skill or the rotation | A temporary group with an end date |
| Four or five | Little coordination; a hands-on manager | A two-tier rotation around the clock; room for a resignation | The scope is narrow with no such rotation, or the team has just budded |
| Six to eight | Two or more people for every part; a rotation it can sustain | Some coordination cost; a full-time manager | The team writes and operates its own services |

## Anti-Patterns: Sized by Budget, Small on Principle

Two habits ignore that trade. The first is **the size from the budget**: the engineers the plan can pay for are divided among the teams. Corvane's eleven teams of eight were sized this way. An even number is right only for the teams whose scope and duty happen to match it. The team with the heaviest duty ends up below its floor, as the platform team did with the five it kept from history, which is the failure pattern this book calls **The Overloaded Team**. And because the teams are cut to fit the number, their boundaries follow the headcount and not the work, which is **The Org Chart as Architecture**.

The second habit runs the other way: **small on principle**. Teams of two or three arise in two ways. A new initiative gets one because small teams are thought to be fast, or a reorganization leaves a remnant of three behind. Either way a temporary arrangement becomes a standing team whose members are the only people who know its systems, which this book calls **The Hero Culture**. Larson's verdict on the teams of one or two he sponsored was regret, every time.

## Worked Example: Sizing Corvane's Platform Team

The derivation can now be run on the platform team as it stood at the end of 2024, still with five engineers. That year Corvane had changed how launches worked: product teams now ran automated readiness checks on their own changes, and the hand check of every launch had left the platform team ([[the-organization-as-a-product]] tells that story). The table gives the inputs of the derivation: what the team still owned, who could change each part, and the duty.

| Part of the scope | Engineers who could change it safely | On-call duty |
| --- | --- | --- |
| The release path: readiness checks and deployment tooling | 3 of 5 | Two tiers, around the clock |
| Shared infrastructure: hosting, databases and monitoring | 3 of 5 | Two tiers, around the clock |
| The shared data model for customers and jobs | 2 of 5 | Working hours |

The floors and the ceiling then give the size. Every part had at least two people who could change it, so the understanding floor was met at five. The rotation floor was not: five is below the six a two-tier rotation needs at the least. Six would have left nothing for a holiday or for an engineer still in training, as August 2024 had shown, so the floor taken for this team was Larson's eight. The ceiling was also about eight engineers with one manager, and the work the scope demanded, with the launch checks gone, called for no more. So the size was eight. Five was wrong for one reason that could be named, the rotation, and it would have been right for a team with the same parts to own and no duty at night.

What remained was the choice of remedy. Scope had been shed once already, when the launch checks moved to the product teams, which left the rotation as it was. Shedding the rotation did not fit, because no product team understood the shared infrastructure well enough to be on call for it. Merging did not fit, because no other team had an adjacent scope. Dropping to one tier, a way of shedding duty, would have lowered the floor, and Lena Brandt rejected it: a missed alert on the release path would stop every team's releases. That left growing. In the plan for 2025 she proposed eight engineers, and Dario Vance, Corvane's VP Engineering, approved it. Three engineers joined in the first half of 2025, and each joined the rotation after about a quarter of training. By the end of 2025 each platform engineer was on call two weeks in eight, down from two in five.

The same derivation explains why a product team's eight worked. Take Scheduling, the product team that owns the rules for assigning jobs to technicians, as it stood in 2025: eight engineers, a two-tier rotation for its own services, and, since its boundaries were redrawn that year ([[cognitive-load-and-team-boundaries]]), no part that only one engineer could change. Both floors were met, and eight sat at the ceiling. The number that came from division was right for Scheduling by a coincidence of scope and duty. A derivation gives the reason, and the reason tells you when the number has to change.

## What AI Changes Here

Of the inputs to that derivation, AI changes one. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, in the teams I have observed, coding agents lower the cost of producing a change, while the agents are not on the rotation and the people still have to understand what they approve. This is my observation, not a measured result. That cost decided how many engineers a scope needed above the floors. The floors do not count hands that write code: one counts people who understand each part well enough to change it safely, the other trained people on a rotation. So the familiar six to eight does not simply fall when writing gets cheaper.

**Speculative.** What happens instead is not known, and two outcomes are possible. A team of six to eight may own a wider scope than before, until understanding or verification, and not hands, sets the limit. Or teams may settle nearer the floors, at four or five engineers, with shared rotations. The first would be confirmed where teams of unchanged size own more parts with none known to one person only, the second where stable teams of four or five sustain their on-call duty. [[team-shape-and-roles-with-ai]] makes the full argument. This chapter claims less: when the cost of producing a change moves, the size is derived again, with the same floors and ceiling.

## Closing Part II: One Team Read as a Type, a Mode and a Size

This chapter completes Part II, which asked of every team which type it is, in which mode it works with others and how large it should be. The part opened with Corvane's platform team of five, which was meant to help eleven product teams release faster and, within a year of those teams being formed, was the place where launches waited. Reading it takes two terms from the previous chapters. A **platform team** exists to take mechanics off the stream-aligned teams, the teams that deliver to users. **X-as-a-Service** is the mode in which one team uses what another provides without having to ask. The table reads the platform team of 2024 with each of the part's three chapters.

| Reading | What it should have been | What it was in 2024 | What the org chart showed |
| --- | --- | --- | --- |
| Type ([[team-types]]) | A platform team | A platform team | The name |
| Mode ([[interaction-modes-and-team-apis]]) | X-as-a-Service: product teams release without asking | A request for a launch: a collaboration nobody had chosen, which had become a queue | Nothing |
| Size (this chapter) | Eight for its rotation, or a smaller duty | Five | The number, without a reason |

The three readings are one decision made three times. What a team is for decides how other teams should reach it, and both decide how many people it needs. Corvane's platform team was the right type, in the wrong mode, with too few people for its scope, which included a rotation around the clock. The order of the repair shows the dependence. Only when the mode changed in 2024, and launches stopped being requests, did the team's scope hold still for long enough to be sized, and the size it then needed was set by its rotation and not by the queue. None of this was visible on the org chart, which showed a box named Platform with five names in it.

## What to Take Away

**Established.** What the sources agree on:

- Larson's rules of thumb, each with a reason: six to eight engineers per manager, about eight for a two-tier rotation, no teams below four, three to five with a hands-on manager (*An Elegant Puzzle*).
- The pairs in a team grow as *n*(*n*−1)/2, far faster than its headcount; new teams are grown out of working ones, and scope moves before people do (Larson).
- Product management, design and engineering belong in one team (*Empowered*; *Build What Matters*).

**Depends on context.** What changes with the situation:

- The number itself: it depends on the scope, the on-call duty and whether the manager does hands-on work.
- The remedy for a team that is too small: it depends on which floor is broken and who else could carry the work.
- The roles a team needs full-time: it depends on how often its decisions need each role.

**The author's synthesis.** What is this book's own position:

- The two floors and the ceiling, the arithmetic of on-call weeks and the one-week-in-three threshold are mine.
- Deriving composition from waiting, and reading one team as a type, a mode and a size, are this book's.

## Checklist

A team size is an answer with its working shown: floors from what the team owns and must sustain, a ceiling from what it can coordinate, roles from the decisions it makes. List your teams with a type, the mode of each of their main interactions and the reason for each team's size, and where the reason is missing, derive it.

- [ ] For each team, write down its type, the mode of each of its main interactions, and the reason for its size: a derivation, a budget or history?
- [ ] List what the team owns, part by part. Can at least two people change each part safely?
- [ ] Write down the on-call duty and how many weeks in ten each engineer is on call, holidays included.
- [ ] For a team below a floor: grow, shed or share scope and on-call, or merge?
- [ ] Do you have standing teams of two or three? Give each one an end date, a merger or a plan to grow.
- [ ] Which decisions about what to build, or how it should work, wait for a role outside the team?
- [ ] Record the assumptions next to each size, and derive it again when one of them moves.

In 2024 five platform engineers were on call two weeks in five, and nobody could say why the team had five. You can now say why five was wrong, why the product teams' eight was right, and what had to be settled first: the team's type and its mode. Part II leaves you with teams, their interfaces and their sizes. It has not yet said what those teams are asked to achieve, or who decides it. That comes next, in [[part-3]].

## Sources and Evidence

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. The sizing rules of thumb and their reasons: six to eight engineers per manager, tech lead managers and coaches, eight for a two-tier on-call rotation, fewer than four is not a team, three to five with a hands-on manager, growing and budding teams, moving scope before people, only trained engineers on call.
- *Build What Matters*, Ben Foster and Rajesh Nerlikar, 2020. The staffing ratio for one product team, and design as a peer of product management.
- *Empowered: Ordinary People, Extraordinary Products*, Marty Cagan with Chris Jones, 2020. Product managers, designers and engineers in one team; used through the author's summary.
- *Team Topologies*, Matthew Skelton and Manuel Pais, 2019. Team types, interaction modes and cognitive load, treated in [[team-types]], [[interaction-modes-and-team-apis]] and [[cognitive-load-and-team-boundaries]].

**Research and reports**

- None. The chapter cites no study; the arithmetic of pairs and of on-call weeks is the author's.

**Practitioner sources**

- The two-pizza rule, widely attributed to Amazon. Not among the author's sources; cited only as the widely known rule.
- The author's working summaries: [[organizational-design]] (Larson's sizing rules), [[right-team]] and [[team-topology]] (the product sources on composition), and [Team Size and Composition Guardrails](../org-design/team-size-and-composition.html) (size and composition guardrails).
- The statement about coding agents under "What AI Changes Here" is the author's observation as of November 2026 and is labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
