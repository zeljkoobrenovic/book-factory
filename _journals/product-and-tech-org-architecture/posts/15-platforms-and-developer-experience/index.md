---
title: "Platforms and Developer Experience"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Once a platform team is justified, how is the platform funded, run and judged? As a product whose users are the product teams: funded against the load it takes off them, started thin, adopted by choice, and judged by how long those teams wait and how much they have to know to ship."
permalink: platforms-and-developer-experience
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn how to fund, run and judge an internal platform as a product, and what developer experience measures.

> **KEY POINTS:**
>
> * **A platform is a product, and its users are teams.** Its value exists only in their work, so adoption by choice is evidence of that value, and a mandate hides the evidence.
> * **Developer experience is the outcome measure.** It is how long product teams wait and how much they have to know to ship, read from adoption by choice together with the adopters' lead time and friction.
> * **Fund load removed, start thin, let users shape the roadmap.** Each new roadmap item names the teams, their load and how it was measured. Low adoption is a product failure to investigate.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Platform Nobody Asked For** — the chapter starts every platform product from a load that teams have reported or that was measured.
> * **The Output Scoreboard** — a platform team that reports features shipped cannot say whether any team waits less.

<br>

At the half-year review in mid-2026, Lena Brandt, Director of Platform at Corvane, reported that her team had shipped all nine items on its roadmap. Corvane is the fictional company this book follows, and that year it had about 500 people, thirty teams and a platform team of eight. Dario Vance, the VP Engineering, asked one question: how many teams release through the release path, the platform team's main product? Nobody in the room knew. A count made that week gave eleven, the same eleven as a year earlier. If you have funded a platform team that delivers its whole plan and cannot tell you what that did for other teams, you know this review. A platform has users, and **whether it works shows only in their work**.

This chapter argues that a platform should be funded, run and judged by what it does for those users. When a platform team is justified is the question of [[team-types]]; this chapter starts once the answer is yes. From there, the platform is **funded against the measured load it removes** from **stream-aligned teams**, the teams that each own one flow of user value from end to end. It is run as a product whose users are those teams: its roadmap is shaped by their problems, and it starts as the thinnest thing that removes a load teams have reported or measured. It earns adoption by being the easier path and does not rely on a mandate. Its outcome measure is **developer experience**: how long product teams wait and how much they have to know to ship. The chapter starts with Corvane's review, says what it means to treat a platform as a product, and defines developer experience and its measures. Three patterns follow: funding against measured load, the thinnest viable platform, and a roadmap shaped by users' problems. The chapter then names how platforms fail and where a mandate still belongs, works through Corvane's review, and ends with what AI changes.

## Setting the Scene: Nine Items Shipped, Eleven Teams On

The review had two descriptions of the same half-year in front of it. The first column below comes from the platform team's report, and the second from Dario Vance's count and a look at the meeting invitations. The **release path** is the set of automated readiness checks and release tooling that a product team runs on its own change. The platform team built it in 2024, when Corvane had eleven product teams, and all eleven joined it, as [[the-organization-as-a-product]] tells.

| What the report said | What the count showed |
| --- | --- |
| Nine of nine roadmap items shipped, among them faster readiness checks and a release dashboard | Eleven of thirty teams release through the release path |
| The release path is available to all teams | The teams formed in 2025 and 2026 release in three other ways |
| The roadmap is reviewed every quarter with team leads | The review invites the leads of the eleven teams of 2024 and nobody else |

Nothing in the report was false. It looked the way it did because it counted what the platform team had produced, and nobody had asked the team for anything else. This book calls that failure **The Output Scoreboard**: an organization counts what was built and does not ask what changed for a user. Here the users were Corvane's own teams. A remedy was within easy reach, to require the path, and Corvane had stopped short of it. After a failed release in May, the release path had been named the one standard for deploying under the company's new engineering strategy: the default for new services, with the platform team to move the other teams onto it; [[engineering-strategy]] and [[quality-and-reliability]] tell that story. A requirement is how the common alternative to this chapter works. In the **infrastructure-team model**, a central team builds and operates shared systems to its own roadmap, and teams are required to use them. Vance's point at the review was that a requirement would answer a different question. In time it would make the number thirty, and it would tell nobody why nineteen teams had stayed away.

## A Platform Is a Product Whose Users Are Teams

What Corvane's report lacked was its users, and the stance that puts them first starts from a definition. The previous chapter described a **paved path**: a ready-made, supported way of doing a common task, which nudges teams toward a choice by making it the easy one. A platform is the paved path made into a product. It has users, the stream-aligned teams. It has a team that owns it, and it has a roadmap. As the introduction said, [[team-types]] decides whether an organization should have a platform team at all: it should when several teams repeat the same mechanics and can be given them as **self-service**, which means without filing a request and waiting for a person. I do not repeat that argument here. The phrase **platform as a product** comes from Camille Fournier and Ian Nowland's *Platform Engineering*, where the internal platform has identified customers, the application teams. I cite that book, and Gregor Hohpe's *Platform Strategy*, through my own working records of them, such as [[platform-as-a-product]].

One consequence of the product stance decides how a platform is judged. A platform delivers nothing to a customer. Its value exists only in its users' work: a release that did not wait, a service set up without learning how the hosting works. Teams adopt what makes their work easier and route around what does not. A platform therefore earns adoption by being **the easier path**: using it costs a team less waiting and less to know than doing without it. So whether teams choose the platform is honest evidence of its value. I call this **adoption by choice**: a team uses the platform although it could do otherwise. A mandate removes the evidence and leaves the platform as it was. Fournier and Nowland give the warning directly: mandatory usage is not to be read as proof of success, and voluntary adoption has to be told apart from mandated adoption. This is why Vance's count was the right first question.

The infrastructure-team model does without that evidence, and it still has a case. Shared systems need one owner, and consistency across teams does pay. Where the model goes wrong is in how it gets consistency, and the two models part in four places:

| | Infrastructure team | Platform as a product |
| --- | --- | --- |
| The roadmap comes from | The team's own view of what is needed | Problems its users have reported or that were measured |
| Teams reach it by | Requirement, often through a ticket | Choice, as self-service |
| Success is reported as | Systems built and uptime | Adoption by choice and what changed for the adopters |
| Low adoption means | Teams are not complying | The product has a fault to find |

## Developer Experience: The Outcome Measure

The last two rows of the table speak of what changes for the users, and that has a name. **Developer experience**, in this book's sense, is how long a product team waits and how much it has to know to ship a change. The two halves are the two costs that earlier chapters measured. Waiting is where lead time goes, as [[flow-and-the-constraint]] showed. What a team has to know is its cognitive load, the total it has to hold in mind, which [[cognitive-load-and-team-boundaries]] treats as the limit on what one team can own. The definition is mine, and it is narrower than common usage, in which developer experience covers everything from tools to culture to how satisfied developers are. I keep it narrow because a platform team can move these two quantities and can be held to them. Together they are the **load** a platform exists to remove, and the rest of the chapter uses the word in that sense.

Neither quantity can be read from one number. Five measures show them, and each tells a platform team something different. In the table, **lead time** is the time from starting work on a change to its release, and **friction** is my word for the steps where a team was stuck or had to learn how the platform works inside.

| Measure | What it tells the platform team | How it is collected |
| --- | --- | --- |
| Adoption by choice: the share of teams using a product they could avoid | Whether teams find it the easier path | Counted from usage, for each product |
| Time to a first release for a new team or a new service | How steep the way in is | Timed, or watched with an engineer new to the platform |
| Adopters' lead time for a change | Whether the teams that use it wait less | From the delivery tooling |
| Share of uses that need no request to the platform team | Whether it is self-service in fact | Counted from requests and questions |
| Reported friction | What a team still has to know | A short regular survey, and watching teams work |

The selection is mine, but this way of measuring is not. Two research papers support it, and they supplement my own sources here. *The SPACE of Developer Productivity*, by Nicole Forsgren, Margaret-Anne Storey and colleagues (2021), holds that productivity cannot be measured by a single metric or dimension and is more than a developer's activity. *DevEx: What Actually Drives Productivity*, by Abi Noda, Storey, Forsgren and Michaela Greiler (2023), proposes measuring developer experience by combining feedback from developers with data about the engineering systems they use. I rely only on the two papers' abstracts. The practical form is in my record [[devex-evaluation]], taken from the *Platform Engineer's Handbook*: a developer who does not know the platform takes a real application through the whole journey, and the platform team writes down every step that needed help.

The first measure in the table needs a caution, and the caution comes from the source that argues hardest for platforms as products. In my record [[platform-success]], Fournier and Nowland warn that adoption figures alone prove nothing, because a mandated migration inflates them. Hohpe adds, in [[growing-platforms]], that existing users are a biased sample. I read both as a limit on adoption and not as a reason to drop it. Adoption by choice shows that teams prefer the platform. The adopters' lead time and reported friction show whether it helps them. Read the three together, and ask the teams that stayed away.

## Pattern: Fund the Platform Against Measured Load

With a measure in hand, funding has something to be decided by. A platform is an investment in other teams' attention: the company pays platform engineers so that product engineers have less to wait for and less to know. The case for the investment is therefore a **load statement**. It says which teams carry a load today, how much, how that was measured, and what the platform would cost to remove it. An example of the form, with numbers that Corvane finds later in this chapter: nineteen teams each spend about twelve engineer-days a quarter keeping their own deployment scripts working. Fournier and Nowland give the test behind it, which I summarize in [[what-is-platform-engineering]]: a small platform team must make a much larger engineering organization more productive. Writing that test down item by item, as a load statement for each new thing on the roadmap, is my extension.

**The pattern.** Fund each new platform item against a written load statement. Its users are the leader who approves the budget and the teams the statement names. It worked if the named load, measured the same way a quarter or two after the item shipped, has fallen by more than the item cost. The pattern does not fit three cases. Security and compliance work returns lower risk and not lower load, and it is argued as risk. Operating and supporting what already exists is a standing cost, and it is funded as that. And in a company of four teams, measuring costs more than the shared script it would justify; [[team-types]] gives three teams with the same need as my rule of thumb for when a platform is worth considering.

## Pattern: Start with the Thinnest Viable Platform

A load worth funding still leaves open how much to build. The answer in *Team Topologies* is the **thinnest viable platform**: the smallest set of interfaces, documentation and tools that speeds up the stream-aligned teams. The reason Matthew Skelton and Manuel Pais give, as I record it in [[four-fundamental-team-topologies]], is that platforms tend to grow and to start dictating to the teams they serve. Hohpe puts the same thought as a question to ask before building anything, in [[organizing-for-platforms]]: would the thinnest viable platform do? I add one condition: teams have reported the load it removes, or someone has measured it. A thin platform for a load nobody has is still **The Platform Nobody Asked For**, this book's name for a platform built ahead of any team's stated need.

Thin also means selective. Three questions decide whether a piece of work belongs in the platform or stays with the product teams, and Figure 1 puts them in order. The first, whether several teams carry the load, repeats the rule of thumb of three teams. The second is Fournier and Nowland's centralization test: one implementation must serve many teams without extensive tailoring for each. The third is self-service, which keeps a platform from becoming a queue. At Corvane the release path runs the readiness checks for every team, and what a team's own check asserts about its own service stays with that team.

---begin mermaid---
flowchart TD
    Q1["Have several teams reported or shown this load?"] -->|"no"| A1["Stays with the team"]
    Q1 -->|"yes"| Q2["Does one implementation fit them without tailoring for each?"]
    Q2 -->|"no"| A2["Stays with the teams; share an example or a guide"]
    Q2 -->|"yes"| Q3["Can teams use it without asking the platform team?"]
    Q3 -->|"no"| A3["Not yet: it would be a queue"]
    Q3 -->|"yes"| A4["Platform: build the thinnest version with one team that has the load"]
---end mermaid---
**Figure 1:** *A piece of work belongs in the platform only if several teams carry it, one implementation fits them and they can use it without asking.*

**The pattern.** Build the thinnest version with one team that has the load, and widen it only when it is used. Its user is that first team. It worked if the team keeps using the thin version after the platform engineers have left, and if a second team takes it up without their help. Corvane's release path began this way in 2024, at 180 people and eleven product teams. It was built with one team, Scheduling, in one quarter, and it was a set of automated readiness checks and release tooling and nothing more. Scheduling ran it alone from the seventh week, and the other ten teams joined over the next two quarters; [[the-organization-as-a-product]] and [[interaction-modes-and-team-apis]] tell that story. The pattern does not fit a load that cannot be removed in pieces, such as a move to a new hosting provider that every service has to make.

## Pattern: A Roadmap Shaped by Users' Problems

After the first version, something has to decide the next ones. A platform team finds its users' problems the way a product team does, through **discovery**: the work of finding out, before building, which problem is worth solving, as [[discovery-delivery-and-empowered-teams]] describes it. For a platform, Fournier and Nowland's advice is to watch how teams really work, including the workarounds they have built, and to separate a team's problem from the solution it proposes. A request such as "add this flag" is a clue to a problem and not an order. A platform team that builds each request as specified, for whoever asks loudest, becomes what they call a **feature shop**. Hohpe's point about biased samples applies here too, and it is the one Corvane's platform team had missed: the teams that stayed away have to be asked.

Four planning habits carry what discovery finds into the roadmap:

- **Write each item as a team's problem.** An item names the teams, their problem and the measure that should move. This extends the load statement to the whole roadmap and is my addition.
- **Review the roadmap with users and non-users.** A platform team's **team API**, the page that says what it owns and promises and which [[interaction-modes-and-team-apis]] describes, should promise a quarterly roadmap review with team leads. The invitation has to include leads of teams that do not use the platform.
- **Sort requests by impact and fit.** Hohpe's triage, in my record [[growing-platforms]], weighs each request by its impact on the business and its fit with the roadmap, and a refusal comes with its reason.
- **Count the work of getting teams on.** For Fournier and Nowland, migration and adoption are project work inside the plan. The platform team carries the cost of moving teams and does not leave it to them.

**The pattern.** Let the users' problems, found by discovery, set the roadmap. Its users are the platform lead who plans and the teams who are asked, adopters or not. It worked if every roadmap item can name the teams and the measure behind it, and if the measure moved after the item shipped. The pattern has a limit. Teams cannot be asked what a security review or the hosting provider will require next year, so that part of the roadmap comes from the platform team and is labeled as such.

## Anti-Patterns and the Place of a Mandate

A platform fails in four ways, and each leaves out something this chapter has set up. In the order of the table, those are a load that teams reported, adoption as evidence, a roadmap built from shared problems, and the measure. The platform team's own reports show none of the four, but each has a sign you can see from outside the team. Two are failure patterns of this book. The other two come from Fournier and Nowland, who also name the **shadow platform**: a team's own replacement for something the platform offers.

| Anti-pattern | What you see | What to do |
| --- | --- | --- |
| **The Platform Nobody Asked For** | Its builders cannot name the teams they spoke to; teams keep their own scripts beside it | Go back to a reported load and a thin version with one team |
| **Adoption by mandate** | Usage is high and so are the workarounds; somewhere a shadow platform appears | Measure friction and lead time; treat the shadow platform as a finding about an unmet need |
| **The feature shop** | A backlog of single-team requests that only the platform team can do | Find the problem that several teams share |
| **The Output Scoreboard** at the platform team | Reviews list features shipped | Report adoption by choice and the adopters' lead time |

The second row does not make a mandate always wrong. [[architecture-governance]] reserves the mandate for divergence that creates a risk a team cannot carry, such as legal exposure or a security weakness, and a platform is often how such a mandate is carried out. A platform that teams are required to use is then judged by its users' friction and lead time alone. The trade-off is plain. Earning adoption is slower, and for a time it leaves several ways of working alive, a cost that [[migrations-and-technical-debt]] takes up. Mandating is fast, and it blinds the platform team to its own faults.

## Worked Example: Corvane's Platform Review of 2026

Corvane had not mandated its release path: its strategy made the path the default, which a team may leave by writing a decision record and operating its own way. So the platform team had to do the work that a mandate lets a platform team skip. In the weeks after the half-year review of mid-2026, Lena Brandt and two platform engineers took the five measures for the release path for the first time. They interviewed the leads of six teams that were off the path, and they watched an engineer from one of those teams try to join it.

| Measure | Release path, mid-2026 |
| --- | --- |
| Adoption by choice | 11 of 30 teams |
| Time to a first release of a new service | On the path: about three weeks of the team's work, after waiting about two months for a platform engineer. With a copied script: two days |
| Adopters' median lead time | Under 7 days; for teams off the path, 11 days |
| Uses without a request | Releasing on the path: all. Joining the path: none |
| Reported friction | 4 of the 11 steps to join needed a platform engineer |

The table gave one finding. For a team already on it, the release path was the easier path: those teams released without asking anyone, and they waited less than the others. For a new team it was the harder one. The reason was an offer made in 2024, when the platform team's team API promised each joining team a platform engineer for up to six weeks. That offer was designed for eleven teams. In 2025 and 2026 Corvane formed nineteen more, and eight platform engineers could not staff it. A new team that had to release in its first weeks copied a script from a neighbor or wrote one. The six leads estimated what keeping such scripts working cost them: about twelve engineer-days a quarter in each team, or about 230 across the nineteen. So the low adoption had a cause that the platform team could remove, and nobody had looked for it while the roadmap was being reported as shipped.

The fix was thin. In the third quarter of 2026 two platform engineers worked for six weeks with two of the newer teams and built a service template and one setup command, which together put a new service on the release path with working defaults. The steps that needed a platform engineer went from four to none, and a first release of a new service on the path took under two days. Moving a team's existing services took longer, about six weeks in which the team shipped little. By the end of 2026 seven of the nineteen newer teams were on the release path, which made eighteen of thirty. The platform team moved these seven first because their releases failed most, so the count is not adoption by choice. For them the platform team reads the other measures.

The plan for 2027 was decided by the same evidence. Lena Brandt's draft roadmap held three items and a request for four more engineers, and Dario Vance asked for the load statement behind each item. The second item was an old request. In 2024 Brandt had asked for a second platform team to build test environments, and Vance had answered "not yet", as [[team-types]] tells. The table gives the three items and his decisions. The four engineers were not approved, and no second platform team was formed.

| Item | Load statement | Decision |
| --- | --- | --- |
| Move the remaining twelve teams onto the release path, each by an agreed date | About twelve engineer-days a quarter in each of the twelve teams; a median lead time of 11 days against under 7 | First, within the team of eight |
| Self-service test environments | Seven of the eleven teams of 2024 kept their own scripts for setting up a test environment, and the newer teams copied them | A thin version with two teams in the first half of 2027, reviewed after one quarter |
| A developer portal | No team had reported a problem it would remove | Not built; asked again when a team reports one |

The half-year review and the decisions that followed left one lasting change and one piece of unfinished work. From 2027 the platform team's quarterly report leads with the measures and not with items shipped. For the release path, now the standard that teams are moved onto, those are the adopters' lead time, the time to a first release and friction. Adoption by choice is reported for products that teams can still avoid, beginning with test environments. The unfinished work is the twelve teams. Moving them is a migration, and [[migrations-and-technical-debt]] shows how one is finished.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, coding agents are becoming users of internal platforms alongside people. This is my observation and not a measured result: teams that work with agents point them at the platform's templates and checks, because a paved path with documented interfaces and safe defaults is something an agent can follow and be held to. My record [[ai-augmented-platform-engineering]], drawn from the *Platform Engineer's Handbook*, gives the principle for agents that act on a platform: guardrails are enforced in code, because a prompt is a request and not a control. The measures of this chapter apply to the new user unchanged.

Agents also make it cheaper to avoid the platform. **Speculative.** If an agent can write a team's own deployment script in minutes, the platform no longer wins by saving the effort of building one. "The easier path" has so far been a comparison with that effort. What remains is verification, knowing that a change is correct, which [[flow-and-the-constraint]] names as a capacity that runs out. A shared path with checks lowers that cost, and thirty private scripts raise it. A platform would then earn adoption by making changes verifiable more than by convenience. The claim would be confirmed where teams that use agents report staying on a shared path, or returning to it, for its checks. [[ai-platform-governance-and-risk]] and [[agentic-delivery]] take the question further.

## What to Take Away

**Established.** What the sources agree on:

- An internal platform is a product with customers, the application teams, and mandatory usage is not proof that it succeeds (Fournier and Nowland, *Platform Engineering*).
- A platform should start as the thinnest viable one and grow only as its users need (Skelton and Pais, *Team Topologies*; Hohpe, *Platform Strategy*).
- Developer productivity cannot be read from a single measure, and counted data is paired with what developers report (the SPACE and DevEx papers).

**Depends on context.** What changes with the situation:

- Whether a mandate is right. It is right where divergence creates a risk a team cannot carry, and then adoption no longer tells you anything.
- How much to measure. A company of four teams needs a conversation and not five measures.
- How long several ways of working may live side by side while adoption is earned. That depends on what the divergence costs.

**The author's synthesis.** What is this book's own position:

- Developer experience defined narrowly, as how long teams wait and how much they have to know to ship.
- The load statement as the unit of funding, one for each new roadmap item.
- Adoption by choice read together with the adopters' lead time and friction, and the three questions for what belongs in a platform.

## Checklist

Funding, running and judging a platform are one question asked three times: what does a named set of teams no longer have to wait for or know? The load statement asks it before the work, the thin version with one team asks it during the work, and adoption by choice with the adopters' lead time asks it afterwards. A platform team that can answer needs no mandate, and a mandate does not help one that cannot. So judge your platform by its users' outcomes and not by its output, starting with these checks:

- [ ] For each platform product, count the teams that use it by choice and the teams that could and do not.
- [ ] Time a new team's first use, or watch an engineer new to the platform try it, and note every step that needed help.
- [ ] Compare the lead time of teams on the platform with that of teams off it.
- [ ] Ask three teams that stayed away why, and treat each answer as a finding about the product.
- [ ] Write a load statement for every new roadmap item: which teams, how much load, measured how.
- [ ] Put each proposed platform feature through the three questions of Figure 1.
- [ ] Invite leads of teams that do not use the platform to the roadmap review.
- [ ] Change the platform team's report so that it leads with adoption by choice and the adopters' lead time.

Dario Vance asked how many teams used the release path, and nobody at Corvane had counted. You can now say what the report lacked: its users. Nine items shipped said what the platform team had done, and the count began to say what the platform had done for the teams. A platform judged in this way carries the shared mechanics of building and releasing software, and carries them once. It does not make any team's software correct, and it does not keep that software running at night. The next chapter turns to what teams do every day on top of the platform to keep what they ship correct and running: [[quality-and-reliability]].

## Sources and Evidence

**Books**

- *Platform Engineering: A Guide for Technical, Product, and People Leaders*, Camille Fournier and Ian Nowland, 2024. The platform as an internal product with customers; mandatory usage is not proof of success; the feature shop and shadow platforms; the test of leverage; adoption figures that a mandate inflates; migration as the platform team's work. Cited through the author's records.
- *Platform Strategy: Innovation Through Harmonization*, Gregor Hohpe, 2024. Asking whether a platform is needed; adoption as the measure of growth; triage of requests; existing users as a biased sample. Cited through the author's records.
- *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, Matthew Skelton and Manuel Pais, 2019. The thinnest viable platform. Cited through the author's records.

**Research and reports**

- "The SPACE of Developer Productivity: There's more to it than you think", Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck and Jenna Butler, *ACM Queue*, 2021. Productivity cannot be measured by a single metric or dimension. Supplements the author's sources; cited from its abstract.
- "DevEx: What Actually Drives Productivity", Abi Noda, Margaret-Anne Storey, Nicole Forsgren and Michaela Greiler, *ACM Queue*, 2023. Measuring developer experience by combining developers' feedback with data from engineering systems. Supplements the author's sources; cited from its abstract.

**Practitioner sources**

- The author's working records of *Platform Engineering*: [[what-is-platform-engineering]], [[four-pillars]], [[getting-started]], [[platform-as-a-product]], [[managing-stakeholders]] and [[platform-success]].
- The author's working records of *Platform Strategy*: [[organizing-for-platforms]] and [[growing-platforms]].
- The author's records of the *Team Topologies* material and of the platform operating model: [[four-fundamental-team-topologies]], [[next-gen-operating-model]] and [[platform-and-devops-operating-model]].
- The author's records drawn from the *Platform Engineer's Handbook*: [[devex-evaluation]] and [[ai-augmented-platform-engineering]].
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
