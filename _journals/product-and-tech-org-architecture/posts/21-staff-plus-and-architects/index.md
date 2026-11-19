---
title: "Staff-Plus and Architects: The Technical Leadership Track"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What do senior technical leaders own that managers do not? They own the technical decisions that cross the reporting line, and the track works when each role has a written scope, a way to be engaged and a measure of the decisions it improved."
permalink: staff-plus-and-architects
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to write what a staff or principal engineer or an architect is accountable for, tell their decisions from a manager's, and recognize four ways the track fails.

> **KEY POINTS:**
>
> * **The technical track holds what the reporting line cannot.** That is technical direction that crosses teams, the quality of the decisions teams make for themselves, and the connection between what executives intend and what the code can do.
> * **Each role needs one written page.** It states the scope, whose authority the role borrows, what it decides and advises on, how teams engage it and how it is judged. Without the page, seniority is a title.
> * **Judge the role by the decisions it improved.** It fails as an ivory tower when it decides without the teams, as an honorific when it decides nothing, and as a hero or a gate when the person becomes the constraint.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Hero Culture** — a staff engineer who alone holds what a team should hold is this pattern with a title, and the chapter makes handing that knowledge over part of the role.
> * **The Review Bottleneck** — a senior engineer whose approval teams wait for is a gate, and the chapter has the role engaged through advice.

<br>

In the autumn of 2026 Corvane, the fictional company this book follows, had nine engineers with a staff or principal title. Corvane makes scheduling software for field-service companies and had about 500 people then, in about thirty teams. Dario Vance, the VP Engineering, asked the four directors of the product groups and Lena Brandt, the Director of Platform, for one sentence on each of the nine: which decisions that cross teams does this person own or advise on? For two engineers the sentences agreed at once. For four, the sentence named a single team. For two, nobody could write one. And for the ninth, Samir Haddad, the staff engineer Corvane could least afford to lose, **three leaders wrote three different sentences**.

You probably know both kinds of engineer: the one whose title everyone respects and whose job nobody can state, and the one on whom everything depends. The previous chapter derived the management line of managers, directors and executives, which follows the reporting structure. This chapter is about the leadership that cuts across that line. My claim is that senior technical leaders, meaning staff and principal engineers and architects, **own what the management line is not placed to decide**: technical direction that crosses teams, the quality of the decisions teams make for themselves, and the connection between what executives intend and what the code can do. The track works when each role has a written scope and accountability. It fails as an ivory tower when the role decides without the teams, and as an honorific when it decides nothing. The chapter starts with Corvane's nine titles and with what the management line cannot decide. Two descriptions of the people who hold that work follow: Will Larson's four archetypes and Gregor Hohpe's architect who rides the elevator. Then come the pattern, a one-page role charter, four ways the track fails, the page Corvane wrote for Samir Haddad, and what AI changes.

## Setting the Scene: Nine Titles and One Engineer With Three Jobs

The titles were a year old. Corvane introduced its career ladder in 2025, and nine engineers were placed above senior: seven staff and two principal. The ladder's line for staff said that the engineer "has impact beyond their own team". It did not say which teams, or impact on what. The nine sentences that Dario Vance collected a year later showed how each engineer and each leader had filled that in. Two engineers had a scope that their director and their teams described in the same way. Four led the technical work of one team. Two had no scope anyone could state. One was a principal engineer who had been promoted in 2025 after an outside offer and who worked on his own team's hardest tickets. The other was a staff engineer who had written a target architecture for his product group; its teams had not been asked about it and did not follow it. The ninth was Samir Haddad. A group director wrote that he was the person to call about the rule engine. Dario Vance wrote that he chaired the architecture forum. Lena Brandt wrote that he had written the diagnosis for the engineering strategy with her.

The first of those sentences goes back five years. Haddad joined Corvane in 2019. In 2021, when the company had 50 people and four teams, he was the only engineer who understood both the scheduling engine and the mobile sync, the part that carries a technician's jobs to the phone and back. Any change that touched both waited for him. In 2022 Corvane moved the scheduling rules, which teams had built separately, into one rule engine, and his knowledge of both sides made that design possible. Afterwards, at about 45 engineers, he was the only person who could safely change the engine's overlap logic. The knowledge that joined the teams' systems was also a single point of failure, because it sat in one head and in no role. It stayed there until 2025, when Vance asked him to assess the two teams that then shared the rule engine. After the change that followed, four engineers could change rules that only one could before.

The other two sentences were added in 2025 and 2026. In 2025 Vance set up the architecture forum, a meeting of senior engineers that had to approve any design that added a technology or changed an interface between teams, and asked Haddad to chair it. In the first half of 2026 a design waited a median of 23 days for its hearing. That year he also wrote one of the two diagnoses on which Corvane's engineering strategy was built. With the rule engine, that made three jobs of cross-team work. Each had come as a request from one leader, none was stated as his role, and one of them had made him a queue.

## What the Management Line Cannot Decide

Why does such work exist at all? Because of where managers are placed. To **join** decisions is to make them in one place, so that each takes account of the other, and the previous chapters derived the management line from that idea: a manager joins the decisions of the teams that report to them. A technical decision often crosses teams that report to different managers. The first manager placed to join it may sit two or three levels up, too far from the code to judge it. This book calls the roles that hold such decisions the **technical leadership track**, and the people on it **staff-plus**: staff and principal engineers, and architects. The levels and promotion to them belong to [[career-ladders-and-leveling]]; the question here is what the roles are for. The figure shows the two directions for three of Corvane's teams in 2026.

---begin mermaid---
flowchart TB
    VP["VP Engineering"] --> D1["Director, product group A"]
    VP --> D2["Director, product group B"]
    D1 --> M1["Manager, Scheduling"]
    D1 --> M2["Manager, Dispatch"]
    D2 --> M3["Manager, Technician App"]
    M1 --> T1["Scheduling team"]
    M2 --> T2["Dispatch team"]
    M3 --> T3["Technician App team"]
    S["Staff engineer: the scheduling domain"] -.->|"advises"| T1
    S -.->|"advises"| T2
    S -.->|"advises"| T3
    VP -.->|"lends authority"| S
---end mermaid---

**Figure 1:** *The management line runs down the reporting structure, and a staff-plus scope runs across it, here across three teams under two directors.*

Three kinds of work fall outside the line. The table names each, with the reason no manager is placed to hold it and a case from Corvane.

| What the track holds | Why the line is not placed to hold it | At Corvane |
| --- | --- | --- |
| Technical direction that crosses teams | The first manager the teams have in common is too far from the code | The 2022 rule engine, one design for rules that teams had built separately |
| The quality of the decisions teams make for themselves | Good advice needs working knowledge of several teams' systems; a manager knows one team's people and results | Written advice on a team's design before it is built |
| The connection between what executives intend and what the code can do | Executives decide without knowing what the code allows, and teams build without knowing the intent | The 2026 finding that messaging between services had to be unified before a product milestone could be reached |

The strongest objection to a separate track is this: technical direction belongs to engineering managers, senior engineers are their strongest individual contributors, and a second line of leadership only blurs who is accountable. The fear is justified wherever the track is unwritten, and Corvane's nine titles are that case. But the remedy fails on placement. A manager's reach is set by who reports to them, and a technical decision's reach is set by the systems it touches. An engineering manager who set the direction for the rule engine, the dispatch board and the mobile sync would need a say over two teams that report elsewhere. The blur comes from roles that are unstated. A second track does not cause it.

Written down, the division is plain. The management line decides who works on what, with which priorities, and how people are judged and developed. The technical track decides or advises on technical choices that reach beyond one team. The table is my synthesis, and my working record [[staff-plus-technical-leadership]] draws the same boundaries.

| Decision | Management line | Technical track |
| --- | --- | --- |
| Who is on a team, and who is hired | Decides | Advises on the skills the work needs |
| A team's priorities for the quarter | Decides, with product | States technical constraints and risks before the plan is fixed |
| A technical choice inside one team | Not involved | Advises if asked; the team decides |
| A technical choice that crosses teams in the role's scope | Hears what it costs | Decides after advice, or advises the named decider |
| The technical direction of a group or an area | Funds it and holds teams to it | Writes it and keeps it current |

## Larson's Four Archetypes

Will Larson's *Staff Engineer* describes the people who hold this work as four **archetypes**, recurring shapes of the staff role that differ mainly in scope. One of them he calls the Architect; that is his name for one archetype, and the next section gives the wider sense in which this book uses the word. Larson attaches sizes to the archetypes, which I report as his rules of thumb and observations: an organization needs roughly one tech lead for every eight engineers; an area merits an architect only if it is both complex and enduringly central to the company; and the architect and the right hand appeared, in the companies he describes, at about one hundred and one thousand engineers.

| Archetype | What it does, in Larson's description | Scope |
| --- | --- | --- |
| Tech Lead | Guides the approach and execution of a team, in close partnership with one manager | One team or a cluster of teams |
| Architect | Is responsible for the direction, quality and approach within a critical area | One technical area, across teams |
| Solver | Digs into arbitrarily complex problems and finds a path forward | One problem at a time, wherever leadership points |
| Right Hand | Extends an executive's attention, borrowing their scope and authority | The executive's organization |

What do people in these four shapes do? Larson's answer is that they keep doing what made them successful senior engineers, but as auxiliary tasks. The core becomes five things: setting and editing technical direction, providing sponsorship and mentorship to other engineers, injecting engineering context into organizational decisions, exploration, and what Tanya Reilly calls being glue, the mostly invisible work that keeps people and projects connected. The list maps onto the three kinds of work in the first table of this chapter, and the mapping is mine. Setting direction is the first kind. Sponsorship, mentorship and glue raise the quality of what others decide, which is the second. Injecting engineering context is the third, and Larson says when it counts: "while it's still possible to change the outcome."

None of this work comes with authority over the teams it touches, because a staff engineer manages nobody. So where does the weight of the role come from? Larson answers for the right hand, who borrows an executive's scope and authority: "borrowing authority comes with the obligation of remaining deeply aligned with that leader's approach, beliefs, and values." I extend the point to all four archetypes, which the passages I rely on do not do: a tech lead borrows from the team's manager, an architect or a solver from the leader who needs the area to hold or the problem solved. I call that leader the role's **backer**: the manager or executive whose authority the role borrows and who answers for what it does. Larson's word sponsorship means something else, what a staff engineer gives to other engineers, so I use a different word. A staff-plus role without a backer has technical credibility and nothing else to stand on.

## The Architect Rides the Elevator

Larson sorts the roles by scope, and Gregor Hohpe, in *The Software Architect Elevator*, describes one of them by its movement. Picture the organization as a tall building: strategy is set in the penthouse, the code is written in the engine room, and most people stay on their own floor. The worst case, Hohpe writes, is that the people who hold the relevant information are not the ones who decide, while the ones who decide lack the information. His architect rides the elevator between the floors and carries what the engine room knows up and what the penthouse intends down. In his words, "it's the architect's job to translate technical options into meaningful choices for the business." This is the third kind of work, the connection between intent and code, described as a job.

My own book *Grounded Architecture* takes the same line with an image Hohpe also uses: the **superglue** architect, who holds architecture, technical detail, business needs and people together. It starts from the limit of expertise: "Technical strength is necessary for architects, but it is rarely sufficient." The value comes from translation, alignment and judgment more than from formal authority. The word architect needs one sense here, because the sources use it in two. For Larson the Architect is one archetype of four, the one with a technical area. For Hohpe and for *Grounded Architecture* an architect is whoever does the connecting, and titles vary between organizations. In this book an **architect** is anyone on the track whose scope is a technical area or the whole technical landscape, whatever the title says. Both books attach one condition, and the failures later in this chapter turn on it: the connector stays grounded in the code. *Grounded Architecture* says that "real influence starts with real experience."

## Pattern: The Role Charter

The principle and the two sources together say what has to be written for each role. I recommend one page per staff-plus engineer, and I call it a **role charter**. The name and the form are mine. My record [[staff-and-principal-engineers]], which follows Gergely Orosz's *The Software Engineer's Guidebook*, asks for the substance: a staff-plus engineer clarifies the scope and the level at which they operate. The page has three users: the teams in the scope, the backer, and the engineer. It has seven lines.

| Line | What it states |
| --- | --- |
| Scope | The teams, systems or area the role covers |
| Backer | The manager or executive whose authority the role borrows |
| Decides | The cross-team technical decisions the role makes, after advice |
| Advises on | The decisions of others on which the role must be asked |
| Engaged by | How to ask, and how fast an answer comes |
| Judged by | Two or three measures of decisions improved |
| Not this role's | The neighboring decisions that belong to managers, teams or other owners |

Scope is the first line to settle, because the other six depend on it, and it is a trade-off. The table gives four scopes, with the backer each implies, the condition each fits and what each risks. The pairing with Larson's archetypes is mine; a solver's scope is a problem with an end, under whoever assigned it. At Corvane's 500 people I would give most staff-plus roles a group or an area, and a company of 50 rarely needs more than the first row.

| Scope | Backer | Fits when | Risk |
| --- | --- | --- | --- |
| One team (Larson's tech lead) | The team's engineering manager | The team's technical work needs one lead | Senior work under a staff title |
| One group of teams | The group's director | The teams share systems and their choices collide | A deputy for everything |
| One technical area across groups (Larson's architect) | The VP Engineering, or the area's owner | The area is complex and central for years | Distance from every team's code |
| The whole company (Larson's right hand) | The CTO | One executive cannot attend to all of it | The ivory tower |

Inside the scope, the next two lines separate what the role decides from what it advises on, and the first of them should be short. A staff-plus role decides only what crosses teams in its scope and what no team or manager is placed to decide. In practice that is two things: the written technical direction of the scope, and a cross-team choice that the teams could not settle among themselves. Everything else goes on the "advises on" line, where the team or a named decider decides. A "decides" line that grows from year to year is the sign of a gate forming.

How teams reach the person is the fifth line, and my answer is the **advice process** that [[architecture-governance]] sets out as the default for technical decisions. A team that faces a decision asks the people it affects and the people with expertise. It writes their advice into its decision record, the short page that holds a decision and its reasons, and then it decides. The staff-plus engineer is the person with expertise whom the charter obliges the team to ask. Three things follow for the role. It is asked early, while the outcome can still change. Its advice is written where others can read it ([[advice-in-public]]). And it does not sign off. To be worth asking, the engineer stays in the code, and Hohpe is direct about it: "Staying grounded in reality and receiving feedback on decisions from real project implementations is vital for architects."

The sixth line says how the role is judged, and I judge it by **the decisions it improved**. Hohpe measures an architect on three legs: skill, impact, meaning benefit to the business, and leadership, which includes growing other architects. Larson makes the same point: "You're far more likely to change your company's long-term trajectory by growing the engineers around you than through personal heroics." From these I take three measures, and the choice is mine. The first is the share of cross-team decision records in the scope that name the role's advice and say what it changed. The second is how much repeated advice has become something teams no longer need to ask for: a template, an automated check, a written direction. The third is the number of parts in the scope that only one engineer can change, which should fall. The charter itself has worked when any team in the scope can say what the role is for and how to reach it.

## Anti-Patterns: The Ivory Tower, the Honorific, the Hero and the Gate

Each failure of the track is a line of the charter left empty or misused. The **ivory-tower architect** has no working "engaged by" line: the role decides without the teams. Direction is written at a distance from the code and handed down. Orosz lists the ivory tower among his architect archetypes, which *Grounded Architecture* surveys in an appendix. Hohpe gives the warning sign in terms of his three legs: "leadership without (prior) impact lacks foundation and might be a warning signal that an architect has become an ivory tower resident with a weak link to reality." Such direction is wrong in ways only the teams can see, so they work around it. Corvane's staff engineer with the target architecture nobody followed is the case.

The **honorific** is the opposite failure: the role decides nothing, because the scope and backer lines are empty. The title was given to reward a strong engineer or to keep one. The holder goes on doing excellent senior work, usually the team's hardest tickets. Corvane's principal engineer, promoted after an outside offer, is the case. The remedy is a scope, or an honest conversation about the level, and the second belongs to [[career-ladders-and-leveling]].

The last two failures are harder to see, because the role is doing real cross-team work, but through one person's hands. The **hero** holds knowledge or work that a team should hold. This is **The Hero Culture**, this book's name for an organization that thanks the people who rescue it and so keeps needing rescue. Hohpe warns the architect that getting smarter alone "can lead to a single point of failure (you!)". Samir Haddad in 2021 was a hero in this sense, through no fault of his own. The **gate** approves what teams should decide. This is **The Review Bottleneck**, a hand-over between teams built as an approval queue, and the forum Haddad chaired was one. In both, the person has become the constraint the role exists to remove. The hero shows in the count of parts that only one engineer can change. The gate shows in a "decides" line that has swallowed the "advises on" line, and in teams that wait.

## Worked Example: Samir Haddad's Page

Corvane wrote its charters late in 2026, after its engineering strategy ([[engineering-strategy]]) had changed the architecture forum from approving designs to advising on them. Dario Vance began with Samir Haddad and wrote the page with him. Two things help in reading it. A shared area, in Corvane's strategy, is a kind of technical choice that other teams must live with, such as deploying or messaging, and the Director of Platform decides those after advice. And when the page was written, two parts of the mobile sync could still be changed safely by one engineer only.

| Line | Samir Haddad's charter |
| --- | --- |
| Scope | The scheduling domain: the rule engine and its schema (Scheduling team), the dispatch board's use of them (Dispatch team) and the mobile sync (Technician App team). Three teams under two directors |
| Backer | Dario Vance, VP Engineering |
| Decides | The technical direction of the domain, a page revised twice a year. A technical change that crosses the three teams, when they cannot agree, after their written advice |
| Advises on | Every decision record that changes the rule schema or the sync. Choices in a shared area that touch the domain, which Lena Brandt decides |
| Engaged by | A question in the decision record, answered in writing within three working days. The weekly forum, which he convenes and which advises. Each quarter he works in the code of one of the three teams |
| Judged by | Records in the domain that name his advice and say what it changed. Parts of the domain that only one engineer can change |
| Not his | Who works on what, priorities, hiring and performance: the managers, with product. The scheduling rules themselves: the Scheduling team. Choices in a shared area: the Director of Platform |

The other eight pages followed the count from the opening. The four engineers who led one team's technical work got a page that named the team, with its engineering manager as backer. The two engineers with an agreed scope had it written down as it stood. The author of the target architecture withdrew the document and took the open decision records of his group's teams as his work, starting from their questions. The principal engineer was given the technical direction of his own product group, with its director as backer. All nine pages were published where every team could find them.

Two quarters later Vance read the measures on Haddad's page. Fourteen decision records had touched the scheduling domain. Eleven named his advice, and six said what the advice had changed. The two parts of the mobile sync that only one engineer could change had become none. The forum met weekly and approved nothing. There were costs. Haddad wrote less code in his first quarter under the page than in any quarter before, and two of the nine pages needed hard conversations. What the page changed is that three sentences became one, and that the three teams, and no longer only the VP, could say what Corvane's most senior engineer was for.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The two claims here ask what changes for the track when coding agents write much of the code. **Emerging.** As of November 2026, staff-plus engineers in teams I have observed put their technical direction into the files, templates and automated checks that coding agents work from. Written direction then reaches code that no person was briefed on, which makes the written part of a charter's "decides" line worth more than it was. This is my observation; I know of no published measurement of it, so the chapter makes no Proven claim.

**Speculative.** If agents multiply the number of code changes, a senior engineer who reviews every change becomes the gate at a larger scale. This book's Corvane story for 2027 and 2028, at 1,100 people, is the illustration: two senior engineers review everything while agents open three times as many changes, and the median wait for a review goes from 5 hours to 31. On this reasoning the judgment of staff-plus engineers is better spent on what gets checked automatically, and on the decisions an agent cannot make: which problem is worth solving, and what a choice costs the other teams. The claim would be confirmed where review waits grow with the volume of changes and fall again once senior review is replaced by written checks. [[where-the-constraint-moves]] weighs the published evidence.

## What to Take Away

**Established.** What the sources agree on:

- Staff engineers come in four shapes that differ by scope, and their core work is direction, growing others and bringing engineering context to decisions (Larson, *Staff Engineer*).
- An architect's value is in connecting levels while staying grounded in implementation (Hohpe, *The Software Architect Elevator*; *Grounded Architecture*).
- Growing other engineers counts for more than personal heroics (Larson; Hohpe).

**Depends on context.** What changes with the situation:

- Which archetypes you need depends on size; in Larson's observation the architect and the right hand appear late.
- What scope a role should have depends on how far technical choices cross teams and groups.
- Whether "architect" is a separate title depends on your organization. The role exists either way.

**The author's synthesis.** What is this book's own position:

- The three kinds of work that the management line leaves unowned are my framing.
- The role charter and its backer are my recommendation, with borrowed authority extended from Larson's right hand to every archetype.
- Judging the role by decisions improved is my choice of measure.

## Checklist

A staff-plus role is a leadership role of the same kind as a manager's: it joins decisions. It is placed across the reporting line where a manager is placed along it, and because no org chart shows that placement, a page has to. Run these eight checks on your own organization.

- [ ] List every engineer above senior, and write one sentence for each: which cross-team decisions do they own or advise on?
- [ ] Ask two other leaders for the same sentence, and compare the answers.
- [ ] For each role, name the backer whose authority it borrows.
- [ ] Write the seven lines of the charter for the role you understand least.
- [ ] Mark each decision on it as "decides" or "advises on", and check it against the decisions of the managers nearby.
- [ ] Count the parts in each scope that only one engineer can change.
- [ ] Find the last five cross-team decision records in a scope, and count those that name the role's advice.
- [ ] Ask one team in each scope what the role is for and how to reach it.

Corvane's three sentences for one engineer became one page, and with this chapter Part V is complete. Its four chapters gave four answers to one question, where decisions must be joined: at the top, in the executive roles; across functions, in the triad of product, engineering and design; down the line, in spans and layers; and across teams, in the technical track. The part opened with Corvane's CTO and its CPO each drawing the organization and disagreeing about who led eleven of the teams. The two drawings disagreed because nobody had said which decisions the CTO and the CPO make together. It is the same gap, one level up, as nine titles that nobody could explain. So do for every leadership role and every layer what the charter does for a staff engineer: write the decisions it joins that no one else can, and question a role or a layer whose list is empty. Part V has given you leaders and the levels at which decisions recur. Part VI goes into the mechanisms by which those decisions are made, recorded and turned into plans: [[part-6]].

## Sources and Evidence

**Books**

- *Staff Engineer: Leadership beyond the management track*, Will Larson, 2021. The four archetypes; what staff engineers do; the rules of thumb on tech leads and on when the architect and the right hand appear; borrowed authority; growing others over personal heroics.
- *The Software Architect Elevator*, Gregor Hohpe, 2020. The architect who connects the levels of an organization; staying grounded in implementation; the three legs of skill, impact and leadership; the ivory tower as a warning sign; the architect as a single point of failure.
- *Grounded Architecture: Redefining IT Architecture Practice*, Željko Obrenović, the author's online book at grounded-architecture.io, accessed November 2026. The superglue architect; the career tracks of architects and their engineering foundation; the survey of architect archetypes. Pages read: "Thinking Like an Architect: Architects as Superglue", "Navigating Career Paths in Architecture" and "Architect Archetypes".
- *The Staff Engineer's Path*, Tanya Reilly, 2022, and *The Software Engineer's Guidebook*, Gergely Orosz, 2023. Used only through Larson's citation of Reilly's term glue and through the author's records below.

**Practitioner sources**

- The author's working records: [[staff-and-principal-engineers]], [[pragmatic-tech-lead]] and [[engineering-career-paths]], which follow Orosz, and [[staff-plus-technical-leadership]] and [[advice-in-public]].
- The role charter, the backer, the three kinds of work and the three measures are the author's. The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
