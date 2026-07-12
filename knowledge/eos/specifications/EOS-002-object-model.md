# EOS-002: Object Model

**Status:** Draft for Review  
**Version:** 1.0  
**Last Updated:** 2026-07-12  
**Owner:** Chief Knowledge Architect

---

## PURPOSE

Define the first-class objects that make up the EnaasanOS knowledge model.

For each object, clarify:
- What it represents and why it exists
- When to use it vs. when to use something else
- Its lifecycle and how it evolves over time
- How it relates to other objects
- What evidence standards it must meet
- What integrity attributes it carries

This specification remains technology-independent. It defines WHAT objects exist, not HOW they are stored.

---

## INTRODUCTION: OBJECTS AS FIRST-CLASS CITIZENS

In EnaasanOS, objects are the atomic units of the system. Everything is an object.

An object is a "thing" worthy of:
- An identifier (so it can be referenced)
- Metadata (title, owner, status, version, language, etc.)
- A lifecycle (draft → review → published → archived)
- Relationships (it connects to other objects)
- Integrity attributes (evidence level, review status, accuracy)

Objects are NOT:
- Database records (those are representation-layer details)
- API endpoints (those are application-layer details)
- Website pages (pages are composed of objects, not objects themselves)
- Files or documents (a document might contain multiple objects)

An object is **conceptual**. It represents a "thing worth tracking."

**Example:** "BPS Career Guide" is an object (a Publication). The website page showing it is an application. The PDF generated from it is another application. The database record storing it is a representation. But the object itself is the conceptual thing: "organized knowledge about careers in Business Process Services."

---

## OBJECT CLASSIFICATION

EnaasanOS includes 10 first-class objects organized into 4 categories:

| Category | Objects | Purpose |
|----------|---------|---------|
| **Knowledge** | Publication, Knowledge Card, Learning Path | The actual content and how it's organized |
| **Domain** | Career, Skill | The entities that students and educators care about |
| **Planning** | Initiative, Task, Decision | How we organize work and make choices |
| **Measurement** | Metric, Release | How we track progress and release changes |

---

## KNOWLEDGE OBJECTS

These objects represent the actual content and how it's structured.

### OBJECT 1: Knowledge Card

**Purpose**

A Knowledge Card is the atomic unit of knowledge in EnaasanOS. It represents a single, coherent concept that cannot be meaningfully divided further without losing coherence.

**Description**

A Knowledge Card is:
- Self-contained (can be understood independently)
- Focused (covers one concept, not multiple)
- Reusable (can appear in multiple Publications and Learning Paths)
- Language-specific (each language is a separate card or language variant)

**When to Use**

Use a Knowledge Card when:
- You have a single question or concept to explain (e.g., "What is BPS?", "Why is PCM chosen for engineering?")
- The content is atomic enough to be reused in multiple contexts (e.g., the definition of "Stream" can appear in multiple publications)
- You want to maintain consistency (e.g., "Career" definitions should be cards, so they update everywhere)

**When NOT to Use**

Do NOT use a Knowledge Card if:
- The content spans multiple concepts (combine into a Publication instead)
- The content is too small to stand alone (e.g., "B.A." vs. "Bachelor of Arts in Economics" — the latter is a card)
- The content is only relevant in one specific context and nowhere else (might still be a card, but owned by one publication)

**Real Examples from Enaasan**

1. **What is BPS (Business Process Services)?**
   - Current location: BPS career page
   - Could be reused: After-12 streams page, comparison pages, search results
   - Is atomic: Yes, one concept, self-contained

2. **PCM stream: Mathematics focus vs. Physics focus**
   - Current location: Scattered across multiple pages
   - Should be atomic: Yes, it's a specific micro-decision
   - Should be reused: Yes, every stream comparison page needs this

3. **Why do 90+ percent of BPS graduates stay in the field?**
   - Current location: BPS page
   - Is atomic: Yes, one data point and explanation
   - Reusable: Yes, in career-stickiness comparisons, retention articles

**Lifecycle**

Every Knowledge Card SHALL follow this lifecycle:

```
draft → review → published → archived/deprecated
         ↓ (rejected)
       draft
```

**States:**

- **draft:** Card is being written. Not visible. May be incomplete.
- **review:** Card is ready for review by subject matter expert or editor. Not visible to public.
- **published:** Card is live. Appears in publications and search results.
- **archived:** Card is no longer used. Replaced by a newer version or no longer relevant.
- **deprecated:** Card is still published but marked as "outdated; use X instead."

**Transitions:**

- `draft` → `review`: When author believes card is ready
- `review` → `published`: When reviewer approves
- `review` → `draft`: When reviewer requests changes
- `published` → `deprecated`: When card becomes outdated but still referenced
- `published` → `archived`: When card is no longer used anywhere
- `archived` → `published`: If we decide to resurface old content (rare)

**Integrity: Knowledge Card**

Every Knowledge Card SHALL include these integrity attributes:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| **Evidence Level** | Confidence in the accuracy of this card | "Official Data" (JEE exam dates), "Research" (salary ranges), "Opinion" (career advice) |
| **Last Reviewed** | When this card was last fact-checked | "2026-07-10" — if 12+ months old, flag for review |
| **Accuracy Confidence** | How confident we are in this card's accuracy | "High" (government data), "Medium" (survey data), "Low" (anecdotal) |
| **Review Cycle** | How often should this card be reviewed? | "annually" (exam dates), "quarterly" (salary data), "every 2 years" (career advice) |
| **Content Warnings** | Does this card need disclaimers? | "Subject to change" (exam patterns), "Incomplete data" (regional salary info) |

**Relationships**

A Knowledge Card:
- **is contained in** one or more Publications (a card appears in multiple pubs)
- **is composed of** zero or more Skills or Careers (a card can explain multiple concepts)
- **requires** zero or more other Cards (e.g., "Understanding PCM-vs-PCB" requires understanding "What is a stream?")
- **contradicts** zero or more other Cards (for consistency checking; ideally zero)

---

### OBJECT 2: Publication

**Purpose**

A Publication is a large, coherent piece of content composed of multiple Knowledge Cards. It is the primary unit for publishing and sharing.

**Description**

A Publication is:
- Composed of Knowledge Cards (not standalone text)
- Publishable to multiple formats (website page, PDF, DOCX, API response)
- Structured (has a table of contents, sections, hierarchy)
- Meaningful as a whole (a complete guide, not a fragment)

**When to Use**

Use a Publication when:
- You have enough related knowledge cards to form a coherent document (5+ cards minimum)
- The knowledge is meant to be published as a unit (e.g., "BPS Career Guide")
- You want to enable multi-format output (web, PDF, Word doc)

**When NOT to Use**

Do NOT use a Publication if:
- You only have 1-2 cards (might just be a card)
- The content doesn't hold together as a coherent unit (split into multiple publications)
- The content is purely structural (for that, use a Learning Path)

**Real Examples from Enaasan**

1. **BPS Career Guide**
   - Contains: What is BPS, Required streams, Skills needed, Salary ranges, Entry points, Growth paths, Student story
   - Publishable as: Career page on website, PDF guide, Google Doc template
   - Is atomic: Yes, a complete guide to one career

2. **Career FAQ (existing)**
   - Contains: 32 questions and answers across 7 categories
   - Publishable as: Interactive accordion on web, printable PDF, chatbot knowledge base
   - Is atomic: Yes, a complete reference

3. **90-Day Career Clarity Plan (existing)**
   - Contains: Introduction, monthly milestones, worksheets, resources, appendices
   - Publishable as: Downloadable PDF, email series, web page, printable workbook
   - Is atomic: Yes, a complete planning framework

**Lifecycle**

Every Publication SHALL follow this lifecycle:

```
draft → review → published → archived/deprecated
         ↓ (rejected)
       draft
```

Same states as Knowledge Card (draft, review, published, archived, deprecated).

**Integrity: Publication**

Every Publication SHALL include these integrity attributes:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| **Completeness** | Is this publication finished enough to publish? | "Complete" (all sections present), "Partial" (missing examples), "In Progress" (outline only) |
| **Coverage** | What percentage of the topic does this cover? | "Comprehensive" (covers all major subtopics), "Focused" (covers key aspects), "Intro" (basic overview only) |
| **Last Reviewed** | When was this publication fact-checked as a whole? | "2026-07-10" — distinct from card review dates |
| **Review Cycle** | How often should this be comprehensively reviewed? | "annually" (job market changes), "every 2 years" (career guides) |
| **Obsolescence Risk** | How likely is this to become outdated? | "Low" (foundational concepts), "Medium" (industry data), "High" (exam patterns) |

**Relationships**

A Publication:
- **contains** one or more Knowledge Cards (required; a pub with zero cards is not a publication)
- **is part of** zero or more Learning Paths (optional; a guide can stand alone)
- **supports** one or more Initiatives (e.g., "BPS Guide" supports the initiative "expand career coverage")
- **requires** zero or more Publications (e.g., "Advanced BPS" might require readers have read "Intro to Careers")

---

### OBJECT 3: Learning Path

**Purpose**

A Learning Path is a sequence of Publications and Knowledge Cards designed to lead a learner from a starting point to an outcome.

**Description**

A Learning Path is:
- Sequential (has an order; the first element comes before the second)
- Goal-oriented (leads somewhere; has a clear outcome)
- Composed of existing objects (doesn't create new content; reuses publications and cards)
- Personalization-ready (future paths can be variations: "Path for Engineers," "Path for Business Students")

**When to Use**

Use a Learning Path when:
- You want to guide a specific audience through a sequence (e.g., "First Steps for 10th-graders")
- You're combining existing content into a new journey (e.g., "Complete Career Clarity Blueprint" = 90-Day Plan + FAQ + Career Guides)
- You want to support different learning styles or paces (e.g., "Fast Track" vs. "Comprehensive")

**When NOT to Use**

Do NOT use a Learning Path if:
- You're just listing related content without sequence (use a Publication instead)
- The content is too small (1-2 cards; just link them)
- The sequence is arbitrary (e.g., "related articles" doesn't need a path; that's a search result)

**Real Examples from Enaasan**

1. **"Start Here" for 10th-graders**
   - Sequence: Intro → Streams Explained → Career Snapshot → Decision Framework → Next Steps
   - Composes: FAQ cards, introduction guide, career guide cards, decision guide
   - Outcome: Student understands basic career concepts

2. **"Career Clarity" learning journey**
   - Sequence: 90-Day Plan → Career Guides (3-5 of them) → Skills Deep Dive → Decision-Making
   - Composes: existing publications and cards
   - Outcome: Student has chosen a career path

3. **"Skill Mastery" path for a specific skill (future)**
   - Sequence: Skill intro → Use cases → Development steps → Resources → Practice → Next skills
   - Composes: skill definitions, career guides mentioning this skill, resource guides
   - Outcome: Student can apply the skill

**Lifecycle**

Learning Paths follow the same lifecycle as Publications:

```
draft → review → published → archived/deprecated
```

**Integrity: Learning Path**

Every Learning Path SHALL include these integrity attributes:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| **Sequencing Quality** | Is the sequence optimal for learning? | "Validated" (tested with users), "Logical" (makes sense), "Ad-hoc" (could be better) |
| **Completeness** | Does this path achieve its stated outcome? | "Complete" (all steps present), "Partial" (missing intermediate steps) |
| **Estimated Duration** | How long does it take to complete? | "2-3 hours", "1-2 weeks", "ongoing" |
| **Target Audience** | For whom is this path? | "10th-graders", "12th-graders", "parents", "teachers" |
| **Prerequisite Knowledge** | What should learners know before starting? | "Basic career concepts", "Completed stream choice" |

**Relationships**

A Learning Path:
- **composes** one or more Publications and/or Knowledge Cards (required)
- **targets** one or more audience segments (e.g., "10th-graders", "parents")
- **enables** one or more Initiatives (e.g., "First Steps" path enables the "Career Awareness" initiative)
- **requires** zero or more other Learning Paths (prerequisites; e.g., "Advanced Path" might require "Intro Path")

---

## DOMAIN OBJECTS

These objects represent the entities in the career guidance domain that students and educators care about.

### OBJECT 4: Career

**Purpose**

A Career object represents a specific career option that a student might choose. It contains information about what the career is, how to enter it, what skills it requires, and what the future looks like.

**Description**

A Career is:
- A specific, named option (e.g., "BPS," not "IT" which is too broad)
- Owned by a subject matter expert (e.g., someone who works in BPS or knows it well)
- Described in multiple dimensions (entry paths, skills, salary, growth, opportunities)
- Localized (can have versions in multiple languages)

**When to Use**

Use a Career object when:
- You're describing a specific, distinct career path
- The career is specific enough to have a LinkedIn profile or job description (e.g., "Data Scientist" not "Technology")
- The career has distinct characteristics from similar careers (entry requirements, skills, salary)

**When NOT to Use**

Do NOT use a Career object if:
- The term is too broad (e.g., "Technology" — split into specific roles like "Software Engineer", "Data Scientist")
- You're describing a skill or field (use Skill instead)
- You're describing education (e.g., "B.Tech" — describe the career path that uses it, like "Software Engineer")

**Real Examples from Enaasan**

1. **BPS (Business Process Services)**
   - Entry: 12+2, PCM or stream-neutral
   - Skills: Process knowledge, communication, customer focus
   - Salary: ₹2-5L entry, ₹5-15L mid-career
   - Growth: Process specialist → Team lead → Manager

2. **Data Scientist**
   - Entry: B.Tech/B.Sc in relevant field
   - Skills: Statistics, programming, domain knowledge
   - Salary: ₹5-10L entry, ₹10-20L+ senior
   - Growth: Specialist → Lead → Principal

**Lifecycle**

Careers follow this lifecycle:

```
draft → review → published → maintained → archived/deprecated
                    ↓ (annual review)
                maintained
```

Note: Published careers enter "maintained" state (not perpetually published). They're reviewed annually.

**States:**

- **draft:** Career guide is being written.
- **review:** Career guide is ready for SME review.
- **published:** Career is live (first publication).
- **maintained:** Career is published and actively maintained (annual review completed).
- **archived:** Career is no longer relevant or is being replaced.
- **deprecated:** Career is outdated but still published with a redirect to the replacement.

**Integrity: Career**

Every Career object SHALL include these integrity attributes:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| **Evidence Level** | How well-researched is this career? | "Primary Research" (interviewed 10+ professionals), "Secondary Research" (industry reports), "Expert Opinion" (SME judgment) |
| **Data Freshness** | When was the data (salary, demand, etc.) last updated? | "2026-Q2" (current), "2025-Q4" (6 months old) |
| **Geographic Scope** | Is this career data relevant to specific regions or all of India? | "National", "Metro cities", "Tier-1/2 cities", "Limited availability" |
| **Career Maturity** | How established and stable is this career? | "Established" (30+ years), "Growing" (5-10 years), "Emerging" (<5 years) |
| **Salary Currency** | In what currency are salary ranges stated? | "INR" (implied), "USD", "Notes if variable" |

**Relationships**

A Career object:
- **requires** one or more Skills (e.g., "BPS requires Process Knowledge and Communication")
- **requires** one or more Education Paths (e.g., "BPS requires 12+2; specific streams optional")
- **is described in** one or more Publications (e.g., "BPS Career Guide", "BPS in Career Comparison")
- **appears in** one or more Learning Paths (e.g., the career appears in a "Complete Career Guide" learning path)
- **relates to** zero or more other Careers (similar careers: "BPS", "Business Analyst"; competitive careers: "BPS" vs. "Engineering")

---

### OBJECT 5: Skill

**Purpose**

A Skill object represents a specific competency or capability that a person can develop. Skills are atomic; they cannot be subdivided.

**Description**

A Skill is:
- Named and specific (e.g., "Data Analysis," not "Technical Skills")
- Independently valuable (useful in multiple contexts)
- Learnable (can be developed through practice)
- Measurable (can assess whether someone has it)

**When to Use**

Use a Skill object when:
- You're describing a specific, teachable competency
- The skill is relevant to multiple careers (promotes reuse)
- The skill can be developed through explicit training or practice

**When NOT to Use**

Do NOT use a Skill object if:
- You're describing a trait or personality characteristic (e.g., "ambitious" — that's a trait, not a skill)
- You're describing education (e.g., "B.Tech" — that's an education path)
- You're describing a field (e.g., "Technology" — that's an industry)

**Real Examples from Enaasan**

1. **Communication (specifically: Technical Communication)**
   - Used in: BPS, Software Engineering, Management, Teaching
   - Teachable: Yes, through courses and practice
   - Measurable: Can assess via writing samples, presentations, feedback

2. **Process Analysis**
   - Used in: BPS, Operations, Management, Logistics
   - Teachable: Yes, requires specific frameworks and practice
   - Measurable: Can assess via case studies, certifications

3. **Statistical Thinking**
   - Used in: Data Science, Research, Business Intelligence, Quality Assurance
   - Teachable: Yes, through math and practical projects
   - Measurable: Can assess via tests, projects, portfolios

**Lifecycle**

Skills follow a similar lifecycle to Careers:

```
draft → review → published → maintained → archived/deprecated
```

**Integrity: Skill**

Every Skill object SHALL include these integrity attributes:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| **Skill Maturity** | How established is this skill in the market? | "Core" (essential in 10+ careers), "Specialized" (essential in 2-5 careers), "Emerging" (essential in <2 careers) |
| **Learning Path Clarity** | How clear is the path to learn this skill? | "Clear" (established courses exist), "Guided" (courses exist but not comprehensive), "Uncharted" (must learn through experience) |
| **Demand Level** | How in-demand is this skill in the job market? | "High" (shortage of skilled people), "Moderate" (available but valued), "Low" (supply exceeds demand) |
| **Skill Half-Life** | How quickly does this skill become outdated? | "Stable" (5+ years), "Moderate" (2-5 years), "Fast" (<2 years) |

**Relationships**

A Skill object:
- **is required by** one or more Careers (e.g., "Communication is required by BPS, Engineering, Teaching")
- **is described in** one or more Publications (e.g., "Data Analysis Deep Dive")
- **requires** zero or more other Skills (prerequisites; e.g., "Advanced Statistics requires Basic Mathematics")
- **enables** zero or more other Skills (related; learning this makes that easier)
- **is taught in** one or more Learning Paths

---

## PLANNING OBJECTS

These objects represent how we organize work and make strategic decisions.

### OBJECT 6: Initiative

**Purpose**

An Initiative is a strategic goal or program that drives work. It represents "what we're trying to accomplish" at a high level.

**Description**

An Initiative is:
- Strategic (matters for the business; connected to Enaasan's mission)
- Long-term (measured in quarters to years)
- Measurable (success is defined by outcomes, not activities)
- Owned by a leader (someone is accountable)

**When to Use**

Use an Initiative when:
- You want to represent a major strategic goal (e.g., "Expand career coverage to 50 careers")
- Multiple tasks or projects will contribute to the same goal
- Success is measured by business outcomes, not just completion

**When NOT to Use**

Do NOT use an Initiative if:
- You're tracking a single task (use Task instead)
- The scope is too small (e.g., "Fix typo on homepage" is a task, not an initiative)
- The goal is operational (daily work; not strategic)

**Real Examples from Enaasan**

1. **"Complete Career Coverage" Initiative**
   - Goal: Document 50+ careers across all major sectors
   - Success: 50 careers published, with consistent quality
   - Duration: 12-18 months
   - Owns: Career guide publications, BPS guides, engineering guides

2. **"Localization for Telugu" Initiative**
   - Goal: Translate core content to Telugu
   - Success: Top 20 publications available in Telugu
   - Duration: 6 months
   - Owns: Translation of publications, review process for Telugu accuracy

3. **"Personalized Learning Paths" Initiative**
   - Goal: Build custom learning paths for different student segments
   - Success: 5+ distinct paths, tested with 100+ students
   - Duration: 9 months (future initiative)

**Lifecycle**

Initiatives follow this lifecycle:

```
proposed → active → completed/archived
    ↓ (rejected)
  rejected
```

**States:**

- **proposed:** Initiative idea is documented but not approved.
- **active:** Initiative is approved and work is ongoing.
- **completed:** Initiative's goals are achieved; work is done.
- **archived:** Initiative was cancelled or no longer relevant.

**Relationships**

An Initiative:
- **owns** one or more Publications or Knowledge Cards (work that serves the initiative)
- **is supported by** one or more Tasks (specific work units)
- **is enabled by** one or more Decisions (strategic choices)
- **produces** one or more Metrics (measures of success)

---

### OBJECT 7: Task

**Purpose**

A Task is a unit of work that contributes to an Initiative. It represents "what needs to be done."

**Description**

A Task is:
- Specific (can be clearly described; not vague)
- Measurable (can determine if it's complete)
- Assignable (someone can own it)
- Time-bounded (has a target completion date)

**When to Use**

Use a Task when:
- You have a specific unit of work to track
- The work takes 1-2 weeks to complete (roughly)
- The work contributes to an Initiative
- You want to track completion

**When NOT to Use**

Do NOT use a Task if:
- It's too small (e.g., "Review one paragraph" — might be part of a larger task)
- It's ongoing operational work (not a discrete task)
- It's a strategic question (use Decision instead)

**Real Examples from Enaasan**

1. **"Write BPS Career Guide"**
   - Owner: Subject matter expert on BPS
   - Target: 2 weeks
   - Contributes to: "Complete Career Coverage" Initiative
   - Definition of Done: Career guide published, reviewed, linked

2. **"Translate FAQ to Telugu"**
   - Owner: Telugu translator
   - Target: 1 week
   - Contributes to: "Localization for Telugu" Initiative
   - Definition of Done: Translation complete, reviewed, published

**Lifecycle**

Tasks follow this lifecycle:

```
backlog → in-progress → review → completed → archived
             ↓ (blocked)
          blocked
```

**States:**

- **backlog:** Task is planned but not started.
- **in-progress:** Someone is actively working on it.
- **review:** Task is complete but awaiting review before closure.
- **completed:** Task is done and integrated.
- **blocked:** Task is waiting for something else; work is paused.
- **archived:** Task was cancelled and won't be completed.

**Relationships**

A Task:
- **contributes to** one Initiative (required; every task serves an initiative)
- **depends on** zero or more other Tasks (blockers)
- **produces** zero or more Publications, Knowledge Cards, or other objects
- **is tracked in** GitHub Issues (implementation detail, but noted here for clarity)

---

### OBJECT 8: Decision

**Purpose**

A Decision object represents a strategic choice point where we acknowledge that multiple valid options exist, and we're choosing one.

**Description**

A Decision is:
- Strategic (affects multiple initiatives or long-term direction)
- Documented (the reasoning is recorded, not just the choice)
- Reversible or expensive (if it were trivial, we wouldn't track it)
- Dated (made at a specific point in time)

**When to Use**

Use a Decision when:
- You're choosing between multiple valid approaches
- The choice affects how we build things (architecture, process, scope)
- You want to record the reasoning for future teams
- Reversing the decision would be expensive

**When NOT to Use**

Do NOT use a Decision if:
- There's only one valid option (not a decision, just an implementation)
- The choice is trivial (e.g., "use red or blue" — doesn't matter)
- The choice is already determined by policy or constraint

**Real Examples from Enaasan**

1. **"Should we localize all content or only priority content?"**
   - Options: (A) All content, all languages immediately; (B) Core content only; (C) Phased approach by language
   - Decision: Phased approach — Phase 1 is top 20 publications in EN/TA/TE/HI
   - Reasoning: Balances quality with speed; allows testing before full commitment
   - Affects: Localization roadmap, resource planning, content prioritization

2. **"Should career guides be Publications or Learning Paths?"**
   - Options: (A) Each career is a Publication; (B) All careers are compositions in a Learning Path; (C) Hybrid
   - Decision: Each career is a Publication; careers can be composed into Learning Paths
   - Reasoning: Promotes reuse; allows stand-alone career exploration; supports multi-format publishing
   - Affects: Object model (this specification), publishing workflow, localization strategy

**Lifecycle**

Decisions follow this lifecycle:

```
proposed → made → in-effect → reversed/updated
```

**States:**

- **proposed:** Decision is under discussion; not made yet.
- **made:** Decision is decided; reasoning is documented.
- **in-effect:** Decision is being implemented.
- **reversed:** Decision is overturned; a new decision replaces it.
- **updated:** Decision is modified based on new information.

**Relationships**

A Decision:
- **affects** one or more Initiatives (strategic consequences)
- **affects** one or more Tasks (implementation changes)
- **depends on** zero or more other Decisions (prerequisite decisions)
- **is documented in** EOS specifications or architectural documents

---

## MEASUREMENT OBJECTS

These objects represent how we track progress and coordinate releases.

### OBJECT 9: Metric

**Purpose**

A Metric object represents a measurable outcome that we use to track progress toward an Initiative's goal.

**Description**

A Metric is:
- Specific (defined clearly; no ambiguity)
- Measurable (can be counted, tested, or calculated)
- Time-bound (measured at specific intervals)
- Actionable (results lead to decisions or changes)

**When to Use**

Use a Metric when:
- An Initiative needs to measure success
- The measurement is ongoing or periodic
- Multiple people need to track the same thing
- The metric informs decisions (whether to continue, change direction, etc.)

**When NOT to Use**

Do NOT use a Metric if:
- It's a one-time measurement
- It's purely informational with no decision impact
- It's operational (internal to a team, doesn't affect strategy)

**Real Examples from Enaasan**

1. **"Career Coverage Percentage"**
   - Metric: (Number of careers with published guides) / (Target number of careers)
   - Target: 50 careers by Q4 2026
   - Measured: Monthly
   - Informs: Whether we're on track for the "Career Coverage" Initiative

2. **"Content Review Freshness"**
   - Metric: (Number of cards reviewed in last 12 months) / (Total cards) × 100%
   - Target: 80%+ of content reviewed annually
   - Measured: Quarterly
   - Informs: Which content needs review; whether review process is keeping up

3. **"Localization Progress"**
   - Metric: (Words translated and published in language X) / (Words in source language) × 100%
   - Target: 80% coverage in TA/TE/HI by Q2 2027
   - Measured: Monthly
   - Informs: Whether translation team is on pace; quality of translations

**Lifecycle**

Metrics don't have a traditional lifecycle; they're ongoing. But they have states:

- **active:** Currently being measured and tracked
- **paused:** Temporarily not being measured (e.g., because the initiative is on hold)
- **archived:** No longer relevant; replaced by a different metric

**Relationships**

A Metric:
- **measures** one Initiative's progress
- **is affected by** one or more Tasks (tasks affect the metric)
- **reports to** Leadership or stakeholders (metrics are communicated regularly)

---

### OBJECT 10: Release

**Purpose**

A Release object represents a versioned, coordinated collection of changes to the knowledge system. It groups related changes that go live together.

**Description**

A Release is:
- Versioned (e.g., v1.0, v1.1, v2.0)
- Coordinated (multiple changes released together)
- Documented (what changed, why, what's new)
- Reproducible (can be deployed multiple times identically)

**When to Use**

Use a Release when:
- You want to group related Publications, Knowledge Cards, or changes
- You want a clear version number to reference
- You want to communicate "what's new" to users
- You want to enable rollback if needed

**When NOT to Use**

Do NOT use a Release if:
- You're tracking every single small change (that's version history on individual objects)
- The change is isolated (single publication update might not need a release)

**Real Examples from Enaasan**

1. **v1.5 Release: "Complete BPS Coverage"**
   - Includes: BPS Career Guide, BPS Comparison Cards, BPS Skills deep-dive
   - Also includes: Bug fixes, localizations
   - Release notes: "Added comprehensive BPS career guide; added Bengali localization"
   - Released: 2026-07-15

2. **v2.0 Release: "Learning Paths Launch"**
   - Includes: New Learning Path objects, 5 initial paths, path UI on website
   - Also includes: Migrated career guides to path-friendly structure
   - Release notes: "Added personalized learning paths; career guides restructured"
   - Released: 2026-09-01

**Lifecycle**

Releases follow this lifecycle:

```
planned → in-development → testing → released → supported → end-of-life
```

**States:**

- **planned:** Release is scheduled; content is identified.
- **in-development:** Changes are being made; not yet testable.
- **testing:** Release is being tested; quality check in progress.
- **released:** Release is live; available to users.
- **supported:** Release is live and actively supported (bug fixes, patches).
- **end-of-life:** Release is no longer supported; users should upgrade.

**Relationships**

A Release:
- **contains** multiple Publications, Knowledge Cards, or Initiatives
- **is associated with** one or more Metrics (performance of this release)
- **follows** previous Release(s) in version sequence

---

## CROSS-CUTTING CONCEPTS

These concepts apply to all objects and deserve explicit mention.

### Knowledge Integrity

Every object in EnaasanOS SHALL maintain integrity attributes that describe the quality, accuracy, and maintenance status of the knowledge.

**Integrity includes:**

1. **Evidence Level** — How well-researched is this knowledge?
   - PRIMARY RESEARCH: Direct research, interviews, studies
   - SECONDARY RESEARCH: Peer-reviewed sources, published reports
   - EXPERT OPINION: Judgment of qualified experts
   - ANECDOTAL: Stories, user reports, observation
   - OPINION: Professional judgment without formal research

2. **Review Status** — Has this been fact-checked?
   - DRAFT: Not yet reviewed
   - UNDER REVIEW: Currently being checked
   - REVIEWED: Fact-checked and approved
   - FLAGGED: Issues identified during review
   - DISPUTED: Contradicted by other sources (requires documentation)

3. **Accuracy Confidence** — How sure are we?
   - HIGH: Multiple sources agree; official data; primary research
   - MEDIUM: Most sources agree; some uncertainty; secondary research
   - LOW: Limited sources; significant uncertainty; anecdotal; emerging field
   - UNKNOWN: Not yet assessed

4. **Freshness** — How up-to-date is this knowledge?
   - CURRENT: Reviewed or updated in the last 3 months
   - RECENT: Last updated 3-12 months ago
   - AGING: Last updated 1-2 years ago; review recommended
   - STALE: Last updated 2+ years ago; review urgent
   - UNKNOWN: Unknown when last updated

### Knowledge Lifecycle

Every object SHALL move through a knowledge lifecycle that ensures quality, timeliness, and relevance.

**Lifecycle stages:**

1. **Creation** — Object is created by owner
2. **Draft** — Object is being written; not ready for review
3. **Review** — Subject matter expert or editor reviews for accuracy, clarity, completeness
4. **Publication** — Object is live; visible to users
5. **Maintenance** — Object is periodically reviewed and updated to stay current
6. **Archival** — Object is no longer used; removed from active system (but history is preserved)

**Transitions:**

- Draft → Review: Initiated by owner when ready
- Review → Published: Initiated by reviewer when approved
- Review → Draft: Initiated by reviewer with feedback; owner revises
- Published → Maintenance: Automatic transition; starts review cycle
- Published → Deprecated: Object marked as "outdated; use X instead" but still visible with warning
- Published/Deprecated → Archived: When object is no longer used anywhere

**Review Cycles** depend on object type:

- **Exam data** (very time-sensitive): Reviewed every 6 months
- **Career guides** (moderately time-sensitive): Reviewed annually
- **Foundational concepts** (stable): Reviewed every 2 years
- **Philosophical content** (very stable): Reviewed every 3+ years

### Evidence Classification

For knowledge objects (Knowledge Cards, Publications, Careers, Skills), every major claim SHOULD be classified by evidence level.

**Evidence classification is:**
- Item-level (specific claims, not entire objects)
- Transparent (users can see evidence confidence)
- Updatable (evidence level can change as research improves)

**Example:** In a career guide, the claim "Average salary is ₹5L" is classified as "Secondary Research (2024 industry report)." Another claim "This career is growing" is classified as "Expert Opinion (based on recruiter interviews)."

**Advantage:** Users understand which information is rock-solid and which is informed judgment.

**Disadvantage:** Requires discipline; every significant claim needs evidence classification.

---

## RELATIONSHIPS AT A GLANCE

This table shows which objects relate to which (without detailing every relationship):

| Object | Relates To | Type |
|--------|-----------|------|
| **Knowledge Card** | Publications, Skills, Careers, other Cards | composition, prerequisites, contradiction |
| **Publication** | Knowledge Cards, Learning Paths, Initiatives, Skills, Careers | composition, support, contribution |
| **Learning Path** | Publications, Knowledge Cards, Careers, Initiatives, Audiences | composition, enablement, targeting |
| **Career** | Skills, Publications, Learning Paths, other Careers | requirements, description, relationships |
| **Skill** | Careers, Publications, Learning Paths, other Skills | requirements, teaching, prerequisites |
| **Initiative** | Publications, Tasks, Decisions, Metrics | ownership, support, direction, measurement |
| **Task** | Initiatives, Decisions, Publications, other Tasks | contribution, dependencies, production |
| **Decision** | Initiatives, Tasks, other Decisions | impact, prerequisites |
| **Metric** | Initiatives, Tasks | measurement, influence |
| **Release** | Publications, Knowledge Cards, Initiatives, Metrics | containment, association |

---

## OBJECT SUMMARY TABLE

For quick reference:

| Object | Type | Scope | Lifecycle | Integrity |
|--------|------|-------|-----------|-----------|
| **Knowledge Card** | Content | Atomic concept | draft→review→published→archived | Evidence level, review status, accuracy, freshness |
| **Publication** | Content | Large document | draft→review→published→archived | Completeness, coverage, obsolescence risk |
| **Learning Path** | Content | Sequence | draft→review→published→archived | Sequencing quality, target audience, duration |
| **Career** | Domain | Specific career | draft→review→published→maintained→archived | Evidence level, data freshness, geographic scope, maturity |
| **Skill** | Domain | Capability | draft→review→published→maintained→archived | Market maturity, learning clarity, demand, half-life |
| **Initiative** | Planning | Strategic goal | proposed→active→completed | (Goals define success; metrics track it) |
| **Task** | Planning | Work unit | backlog→in-progress→review→completed | (Definition of done defines success) |
| **Decision** | Planning | Strategic choice | proposed→made→in-effect→reversed | (Reasoning documents rationale) |
| **Metric** | Measurement | Outcome measure | active→paused→archived | (Measured periodically; informs decisions) |
| **Release** | Measurement | Version | planned→in-development→testing→released | (Release notes document changes) |

---

## QUESTIONS STILL OPEN (ANSWERED BY EOS-003 AND BEYOND)

These questions will be answered by subsequent specifications:

1. **Object Identification:** How are objects identified? (By name? By UUID? By URL slug?)

2. **Metadata Details:** What specific metadata fields does each object type require? (Answered in EOS-003)

3. **Relationship Directions:** Are relationships one-way or bidirectional? (Answered in EOS-004)

4. **Versioning Strategy:** Do we version all changes, only significant changes, or only releases? (Answered in EOS-003)

5. **Language Variants:** For multilingual content, is a translation a new object or a language variant of the same object? (Answered in EOS-003)

6. **Ownership Transfer:** What happens when an object's owner leaves the organization? (Answered in governance; likely EOS-005)

7. **Cardinality Constraints:** Can a card appear in infinite publications, or is there a practical limit? (Answered in EOS-004)

8. **Historical Retention:** How long do we keep archived objects? Forever or with retention limits? (Answered in governance)

9. **Conflict Resolution:** If two objects contradict each other, what's the resolution process? (Answered in review process; likely EOS-005)

10. **Machine Readability:** Should the model support tags, categories, and structured metadata for machine processing? (Answered in Phase 2: Representation Layer)

---

## DOCUMENT HISTORY

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0 | 2026-07-12 | Initial specification: 10 first-class objects with lifecycle, integrity attributes, evidence classification | Chief Knowledge Architect |

