---
title: "The Organization as a System That Can Be Architected"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What does it mean to treat an organization as a system that can be architected like any other, and what can a leader actually design? Four elements describe it, four levers change it, and three conditions decide whether the change works."
permalink: the-organization-as-a-system
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to describe an organization by four elements and to name the four levers a redesign has on it.

> **KEY POINTS:**
>
> * **An organization is a system, and it can be architected like one.** Teams are its components, contracts and rituals are its interfaces, work, information and decisions are its flows, and attention, judgment and verification are the capacities that run out.
> * **Behavior follows that structure.** People do what is sensible given the goals, resources and constraints their place gives them, so replacing a person changes little when the place stays the same.
> * **A redesign has four levers and three conditions.** It can move boundaries, interfaces, decision rights and incentives. It cannot set skill, trust or strategy, and it has to fit them.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Org Chart as Architecture** — the chapter shows what a reporting line does not change.
> * **The Unowned Interface** — the opening case is a rule that had to cross between teams and had no agreed way to do so.
> * **The Reorg as Strategy** — the four levers say in advance what a reorganization will leave untouched.

<br>

In 2021 the planners and the technicians of Corvane's customers saw different schedules for three weeks. Corvane is the fictional company this book follows, and its Web and Mobile teams had each built the rule for overlapping jobs, each in its own way. The review found a **communication failure**, and the lead of the Mobile team was replaced. Eight months later his successor's team and the Integrations team disagreed about the status of a job in exactly the same way. If you have seen a problem pinned on a person, the person moved, and the problem come back, you have seen what Corvane saw. When a failure outlives the person blamed for it, **something that stayed in place produced it**.

Naming what stayed in place is what an architect does for any system. This chapter argues that an organization is a system and can be architected like other systems. It has the same four kinds of element: teams as components, contracts and rituals as interfaces, work, information and decisions as flows, and attention, judgment and verification as capacities that run out. It also argues that a redesign can change only four things about that system, which I call **the four levers**: boundaries, interfaces, decision rights and incentives. Skill, trust and strategy are conditions the design has to fit. The chapter starts with Corvane's two incidents, describes the organization by its four elements, explains why behavior follows structure, and then names the four levers and three conditions. After that it turns the vocabulary into a procedure for reading a complaint about people, shows the common misuses, states where the metaphor stops, reads Corvane's case again and ends with what AI does and does not change.

## Setting the Scene: The Same Failure, Twice

Here are the two incidents in full. Corvane makes scheduling software for field-service companies, and [[corvane-at-five-sizes]] follows it through five sizes. In 2021 it had 50 people, 28 of them in product and tech, in four teams under two engineering managers. Web built the office application planners use. Mobile built the technicians' app. Integrations connected customers' billing and stock systems. Core ran the shared services underneath. Each team built its own part of the product and built it well.

Because each team built its own part, both Web and Mobile implemented the rule for overlapping jobs. The office application let a planner book a second job for a technician inside the travel-time window after the first. The mobile app rejected that second job. For three weeks planners and technicians worked from different schedules, and each team's code was correct by that team's reading of the rule. Corvane came to call the incident the Two Calendars.

The review that followed named a communication failure: Mobile had not told Web what it was building. Corvane replaced the Mobile lead. Eight months later, in 2022, Mobile and Integrations diverged on the rules for job status. A job marked complete on the phone stayed open in customers' billing exports for eleven days. The remedy had been applied, and the failure came back with a different person in the role.

Between the two incidents the people changed and the structure did not. The teams were the same, what each owned was the same, and the ways they learned of each other's work were the same. Whatever caused the failure was therefore in the structure, and the review had no words for looking there.

## Four Elements: Components, Interfaces, Flows, Capacities

Those words exist, and architects already use them. In *Thinking in Systems*, Donella Meadows defines a system as a set of elements, interconnected and organized to achieve something: elements, interconnections and a purpose. An architect describing software works with the same ideas under other names. The elements are **components**. The interconnections are two things: the **interfaces** between components, and what **flows** across them. That makes three kinds of thing. The architect adds a fourth: the **capacities** that limit the whole. The purpose, what the system is for, is the subject of the next chapter.

Each of the four has a direct counterpart in an organization, and the table can be filled in for any company. Its last row names three capacities, attention, judgment and verification, which are defined a few paragraphs below.

| Element | In software | In an organization | At Corvane in 2021 |
| --- | --- | --- | --- |
| Components | Services or modules | Teams | Web, Mobile, Integrations, Core |
| Interfaces | APIs and contracts | Agreed contracts, rituals and documents between teams | None for scheduling rules |
| Flows | Requests and data | Work, information and decisions | Rule changes traveled by chance |
| Capacities | CPU, memory, latency budgets | Attention, judgment, verification | Attention: nobody could keep the whole product in mind |

The first row says the component is the team and not the person. A person owns things too, but a person leaves, goes on holiday and changes roles. The team is the smallest unit that can own something for longer than one person stays, which is why the chapters on boundaries and team types ([[cognitive-load-and-team-boundaries]], [[team-types]]) treat the team as the unit of design.

Components are connected by interfaces. An interface is any agreed way in which one team's work or knowledge reaches another: an API, a review meeting, a published schema, a channel where changes are announced. Meadows writes that "the greatest complexities arise exactly at boundaries", by which she means the places where the parts of a system meet, which in this book's terms are its interfaces, and that missing information flows are among the most common causes of a system's malfunction. Both observations say to look at the interfaces first and at the components second.

Three things move across those interfaces: work, information and decisions. Work is the one everybody tracks, in tickets and boards. Information is tracked less. Decisions are the flow that descriptions of organizations most often leave out, although every piece of work waits for someone to decide what it should be, whether it is ready and what comes next.

The fourth element is the limit the system runs under. Meadows observes that any growing system runs into a constraint sooner or later, and that growth itself changes what the constraint is. In an organization I count three **capacities** that run out. **Attention** is how much a team can hold in mind well enough to change it safely. **Judgment** is deciding with the relevant information at hand. **Verification** is knowing that what was built is correct and was worth building. This chapter only names them. [[flow-and-the-constraint]] treats each in full, with how it runs out and how to tell which one is limiting you.

Drawn with its interfaces and flows, Corvane in 2021 shows a gap its org chart did not. The org chart had four boxes under two managers. The drawing below has the same four boxes and adds the connections, including the two that were missing.

---begin mermaid---
flowchart LR
    C["Core"] -->|"service API"| W["Web"]
    C -->|"service API"| M["Mobile"]
    C -->|"service API"| I["Integrations"]
    W -.-|"scheduling rules: no interface"| M
    M -.-|"job status rules: no interface"| I
---end mermaid---

**Figure 1:** *Corvane's four teams in 2021: every team had an agreed interface to Core, and no interface carried a rule change between the three teams that each implemented the rules.*

## Why Replacing People Changes So Little

A description in these four elements is useful because it predicts behavior, and it answers the puzzle Corvane's review could not. Meadows states the general rule: "A system generally goes on being itself, changing only slowly if at all, even with complete substitutions of its elements—as long as its interconnections and purposes remain intact." She adds that changing the interconnections can change a system dramatically. Corvane substituted one person and kept every interconnection, and the system went on being itself.

In an organization the reason is simple to state. In *Six Simple Rules*, Yves Morieux and Peter Tollman argue that every behavior at work is a rational solution to a problem, given three things: the **goals** a person is trying to reach, the **resources** that help and the **constraints** that hinder. Their conclusion is that changing behavior works better through changing that context than through trying to change people's mind-sets. A new person in the same context faces the same problem and finds the same solution.

Read that way, both Mobile leads did the sensible thing. Their goal was the mobile roadmap, and that was what they were asked about every week. They had no resource for learning that another team was changing a rule: no channel, no document, no meeting where it would come up. And the effort of finding out would have fallen on them alone, with no benefit to their own goal. Morieux and Tollman call the price a person pays for cooperating an **adjustment cost**, and they count it among the constraints. Both leads avoided a cost that the structure put entirely on them.

None of this says that people are interchangeable. People differ in skill and experience, and a stronger lead might have noticed the gap sooner. But the structure sets the range within which those differences show. Meadows calls the limit **bounded rationality**: people make reasonable decisions on the information they have, and they lack information about distant parts of the system. A more able lead still decides without the information the structure never sends.

## What a Redesign Can Change: Four Levers and Three Conditions

Behavior follows context, and a person's context is the structure as seen from that person's place in it. That leaves the question of which parts of the structure a leader can change. A redesign changes four directly, and I call them the four levers. The elements say what is there; the levers say what can be changed, and each lever acts on one part of the description. Boundaries decide what the components are, and with that what each team's goals cover. Interfaces and decision rights shape the flows: interfaces carry work and information, decision rights carry decisions, and for the people who depend on them both are resources when they exist and constraints when they do not. Incentives decide which goals count. The capacities are not a lever: no redesign creates attention, judgment or verification, it only decides where they are spent. Each lever also answers a question that anyone in the organization can either answer or fail to answer.

| Lever | What it sets | The question it answers | Treated in depth in |
| --- | --- | --- | --- |
| Boundary | Who owns what | Whose is this? | Parts I and II |
| Interface | How work and knowledge cross between teams | How do they find out? | Part II |
| Decision right | Who may decide which kind of question | Who says yes? | Part VI |
| Incentive | What the organization visibly rewards | What gets you promoted here? | Part VII |

A **boundary**, as this book uses the word, is the line that says which team owns a thing: a service, a customer journey, a rule. Meadows's boundaries, quoted earlier, are the places where parts meet, which here are interfaces; a boundary in this book is the ownership line itself. It is a lever because moving it changes what each side has to understand. When Corvane's scheduling rule belonged to nobody, every team that touched it had to understand it, and none of them did completely.

An **interface** becomes a lever when it has an owner. Two engineers who talk every Thursday are an interface of a kind, agreed between the two of them only, and it leaves the company with either of them. An interface a leader can design has a form (a schema, a meeting, a document), an owner, and consumers who know it exists. [[interaction-modes-and-team-apis]] covers the forms.

A **decision right** is the agreed answer to three questions about a named kind of decision: who may make it, whose input they must take, and where the decision is written down. This working definition is enough for the next four parts. The methods for allocating decision rights and recording decisions come in [[decision-rights-and-decision-records]].

An **incentive** is whatever the organization visibly rewards: promotion, recognition, headcount, a leader's attention. Pay is only one form of it. Incentives defeat the other three levers when they point elsewhere. Meadows describes the trap of seeking the wrong goal: a system whose indicators confuse effort with result will produce effort. A team told to cooperate and promoted for shipping its own roadmap will ship its own roadmap. [[career-ladders-and-leveling]] treats the systems that set incentives.

Against those four stand three things that matter as much and that a redesign cannot set: **skill**, **trust** and **strategy**. A reorganization takes effect on a date. The skill to run a service, the trust between two teams and a strategy the company believes in take quarters or years, and they are built by other means, which Parts III, IV, VII and IX cover. So the design has to be fitted to them as they are today. A boundary that needs a skill the team lacks, or an interface that needs trust two teams do not have, will fail, and predictably.

## Pattern: Read a Complaint About People as a Design Problem

With levers and conditions defined, the vocabulary becomes a procedure, and it has three steps. First, state the behavior without a motive: what happens, not why someone is the kind of person who does it. Second, ask what makes that behavior the sensible thing to do, in terms of goals, resources and constraints. Third, name the lever that sets that context. The steps follow the first of Morieux and Tollman's six rules, which they call "understand what your people do". The questions they give for analyzing a work context make a good interview guide: whom do you depend on, and when they act, do they take the effect on you into account?

Common complaints map to levers in a repeatable way. The table restates four that most leaders have heard, and says where to look for each.

| Complaint as stated | Behavior without motive | Lever | What to look at |
| --- | --- | --- | --- |
| "They never tell us what they change" | Changes reach consumers after release | Interface | Whether any agreed channel exists, and who owns it |
| "They escalate everything" | Decisions travel two levels up | Decision right | Which decisions the team is permitted to make |
| "They only care about their own roadmap" | Cross-team work is deprioritized | Incentive | What the last three promotions rewarded |
| "That team is a bottleneck" | Requests queue at one team | Boundary | What the team owns that others need daily |

Some complaints do not resolve to a lever. The channel exists and is ignored, or the decision right is clear and nobody uses it. In those cases a condition is missing: the skill to use the interface, the trust to rely on it, or a strategy that says what the decision is for. A redesign will not supply any of them, and it helps to know that before announcing one.

## Anti-Patterns: Moving Boxes and Adding Functions

What is commonly done instead of the procedure is to move the boxes. **The Org Chart as Architecture** changes reporting lines and leaves interfaces, decision rights and incentives as they were. A reporting line changes who writes someone's review. It changes nothing about how a rule change reaches another team. Its repeated form, **The Reorg as Strategy**, redraws the chart each time results disappoint. Replacing the person, as Corvane did, is the same error on a smaller scale: it treats a problem of context as a problem of character. Morieux and Tollman are blunt about that move. Explaining what people do by an irrational mind-set, they write, says more about the limits of the analysis than about the people.

The second misuse adds boxes. Morieux and Tollman describe an organization that behaves like a machine with one routine: each time a new performance requirement appears, the machine adds a dedicated function to handle it. Quality becomes a requirement, so there is a quality department. Teams do not coordinate, so there is a coordinator. Each addition looks like action and each makes the organization more complicated, while the context that made cooperation a poor choice for everyone involved stays the same.

## Where the Sources Disagree: How Far the Metaphor Goes

Structure can be misused, and two of this chapter's own sources go further. They do not disagree with each other. They disagree with the idea this chapter rests on, and warn about how far the design of an organization can go. Morieux and Tollman reject what they call the hard approach: the belief that structures, processes and systems have a direct and predictable effect on performance, so that picking the right ones yields the results. They also advise leaders to "resist the pressure to clarify roles, decision rights, and processes" beyond a threshold, because too much clarity lets people comply with their own box and avoid cooperating. Meadows makes the same warning from the systems side: self-organizing systems with feedback are inherently unpredictable, every model of them falls short, and they can be understood and redesigned without ever being controlled.

Treating an organization as a system to be architected borrows from software, and to that extent it is a metaphor. I take both warnings as limits on it, and the book's resolution is this. A software component has no interests and no memory. A team has both, so a boundary or a decision right is an offer that people respond to, not an instruction they execute. The four levers set people's context and do not specify their actions. The right amount of structure is therefore the least that makes cooperation the sensible choice: explicit and narrow where the work is separable and the interface is stable, with deliberately overlapping responsibilities where the work is interdependent and still changing.

| Choice | What you gain | What you lose | Fits when |
| --- | --- | --- | --- |
| Explicit and narrow | Speed, no duplicated work, clear accountability | Cooperation across the line, initiative at the edges | The work is separable and the interface is stable |
| Deliberate overlap | People notice and cover the gaps | Some duplicated effort, more negotiation | The work is interdependent and changing |

## Worked Example: The Two Calendars, Read Again

The model can now be applied to the case the chapter opened with. Read through the four levers, Corvane's repeated failure was an **Unowned Interface** with three other gaps behind it. Each lever had a gap in 2021, and each got a specific change later in 2022, after the second incident.

| Lever | In 2021 | Change in 2022 |
| --- | --- | --- |
| Boundary | Scheduling and job-status rules owned by no team; each application implemented them | Both sets of rules moved into Core as one rule engine |
| Interface | None for rule changes | Rule changes published as a versioned schema and reviewed in a weekly rules session owned by Core |
| Decision right | Nobody decided what the rule was | Priya Nambiar, the product manager, decides scheduling and job-status rules, with Web, Mobile and Integrations consulted; decisions are recorded |
| Incentive | Teams praised for shipping their own roadmap | A shared objective on schedule consistency across the three applications |

The fix also depended on three conditions that the redesign did not create. Core had the skill to build the rule engine, because Samir Haddad, who worked in Core, already understood both the scheduling engine and the mobile sync. The three teams whose applications use the rules (Web, Mobile and Integrations) trusted Priya Nambiar enough to accept her decision, because she had worked with all three since 2020. And the company's strategy made consistent schedules worth the cost, because schedule inconsistency was the most frequent reason customers escalated. Without any one of the three, the same four changes would have produced a rule engine nobody could build, a decision nobody accepted or an objective nobody believed.

As a result, no third incident of this kind followed. The cost was real, though. Core took on the rule engine with the six engineers it already had, it now owned more than it could comfortably understand, and its lead time for other work rose. The boundary change, moving the rules into Core, relieved three teams and loaded a fourth. How much one team can own is the subject of [[cognitive-load-and-team-boundaries]].

## What AI Changes Here

Corvane's case is from 2021, so it is fair to ask whether the model still applies when agents do part of the work. The elements and the levers describe ownership, connection, flow and limit, and by definition none of these depends on who or what produces an artifact. What AI does change has to be shown by evidence. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The labels under What to Take Away at the end of each chapter are a separate set, for everything else. **Emerging.** As of November 2026, in the teams I have observed using coding agents, the agents take part in the flow of work without becoming components: they produce changes, and they do not own outcomes, carry on-call or hold a decision right. A person or a team remains the owner of every change an agent produces. This is my observation, not a measured result.

That placement has a possible consequence for the fourth element, the capacities. **Speculative.** If implementation takes less of a team's attention, the scarce capacity moves toward judgment and verification: deciding what is worth building, and knowing that what was built is right. That is the argument of Part XI, and I label it speculative here because this chapter gives no evidence for it. The published evidence for and against is weighed in [[where-the-constraint-moves]]. The claim would be confirmed where teams report that review and decision queues, and no longer build time, set their pace.

## What to Take Away

**Established.** What the sources agree on:

- Systems keep their behavior when their elements are replaced and change when their interconnections change (Meadows, *Thinking in Systems*).
- Behavior in organizations is a rational response to goals, resources and constraints, so it is changed through the context (Morieux and Tollman, *Six Simple Rules*).
- A growing system meets a constraint, and growth changes which one (Meadows).

**Depends on context.** What changes with the situation:

- How explicit to make a boundary or a decision right depends on how separable and how stable the work is, as the section on where the sources disagree set out. Separable, stable work takes narrow, explicit lines; interdependent, changing work needs overlap.
- Whether a redesign is the right tool depends on the three conditions. If skill, trust or strategy is what is missing, build that first.

**The author's synthesis.** What is this book's own position:

- The four levers and three conditions are my arrangement of those sources, chosen because each lever maps to a question people in the organization can answer.
- That attention, judgment and verification are the capacities to design for is the book's thesis. This chapter names them; [[flow-and-the-constraint]] defines them in full, and the parts after it argue for them.

## Checklist

Taken together, the description and the levers are one tool used in two directions: the four elements say what is there, and the four levers say what can be changed. A problem located in an element points to the lever that moves it, or to a condition no lever reaches. Take one recurring complaint in your organization and run these eight checks on it before you change a person, a reporting line or a headcount.

- [ ] State the behavior without a motive: what happens, how often, between which teams.
- [ ] Ask what makes it sensible: the goals, resources and constraints of the people involved.
- [ ] Boundary: can everyone involved say which team owns the thing in question?
- [ ] Interface: is there an agreed, owned way for the work or knowledge to cross, and do its consumers know it?
- [ ] Decision right: is it written down who decides this kind of question and whose input they need?
- [ ] Incentive: what did the last three promotions or public recognitions in this area reward?
- [ ] Conditions: do the teams have the skill, the trust and the strategy that your intended change assumes?
- [ ] Say in advance what your change will leave untouched, and whether the behavior depends on that.

Corvane's review could not say what had stayed in place between its two incidents. You can now: an unowned rule, a missing interface, an unassigned decision and an incentive that rewarded each team's own roadmap. The four levers say what can be changed. They leave two questions open: for whom the organization is designed, and how the work of changing it should be done. The next chapter answers both by treating the organization as a product, with users and with outcomes it owes them: [[the-organization-as-a-product]].

## Sources and Evidence

**Books**

- *Thinking in Systems: A Primer*, Donella H. Meadows, edited by Diana Wright, 2008. The definition of a system; persistence when elements are substituted; boundaries and missing information flows; constraints and growth; bounded rationality; seeking the wrong goal; the limits of control.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. Behavior as a rational solution in a context of goals, resources and constraints; adjustment costs; the hard approach; a dedicated function per requirement; the warning against over-clarifying roles, decision rights and processes.
- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. Systems thinking as a management tool; used in depth in [[flow-and-the-constraint]].

**Practitioner sources**

- The author's working checklists on organizational design and systems thinking: [[organizational-design]] and [[systems-and-tools]].
- The statement about coding agents under "What AI Changes Here" is the author's observation as of November 2026 and is labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
