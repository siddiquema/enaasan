# EOS-002: Object Model

**Status:** Approved — part of the Enaasan Knowledge Standard v1.0  
**Version:** 1.1  
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
- A clear purpose (why it exists)
- An intended outcome (what result should it produce)
- An audience (who is it for)
- Metadata (title, owner, status, version, language, etc.)
- A lifecycle (draft → review → published → archived)
- Relationships (it connects to other objects)
- Integrity attributes (evidence level, review status, accuracy)

Objects are NOT:
- Database records (those are representation-layer details)
- API endpoints (those are application-layer details)
- Website pages (pages are composed of objects, not objects themselves)
- Files or documents (a document might contain multiple objects)

An object is **conceptual**. It represents a "thing worth tracking" because it will be published, reused, searched, or consumed by AI.

**Example:** "BPS Career Guide" is an object (a Publication). The website page showing it is an application. The PDF generated from it is another application. The database record storing it is a representation. But the object itself is the conceptual thing: "organized knowledge about careers in Business Process Services with the purpose of helping students understand BPS careers and the outcome that they can make an informed decision about pursuing BPS."

---

## OBJECT CLASSIFICATION

### The 10 First-Class Objects (Frozen)

EnaasanOS includes exactly 10 first-class objects organized into 4 layers:

| Layer | Objects | Purpose |
|-------|---------|---------|
| **Knowledge** | Publication, Knowledge Card, Learning Path | The actual content and how it's organized |
| **Domain** | Career, Skill | The entities that students and educators care about |
| **Planning** | Initiative, Task, Decision | How we organize work and make choices |
| **Measurement** | Metric, Release | How we track progress and release changes |

**Architectural Constraint:** These 10 objects are frozen. No new object types will be added unless an Architecture Decision Record (ADR) explicitly justifies it. Instead of creating new types, use Object Categories (see below).

### Object Categories (Not New Types)

Instead of creating new object types, different **categories** of the same object type provide specialization:

**Knowledge Card Categories:**

Each Knowledge Card is a specific type chosen for its reusability and publication value:

| Category | Purpose | Example |
|----------|---------|---------|
| **Definition** | Explains what something is (technical term, concept, entity) | "What is BPS?", "What is a stream?" |
| **Mental Model** | Explains how something works (system, process, relationship) | "How do career choices affect your future?", "Why do some careers require specific streams?" |
| **Checklist** | Guides action (decision criteria, evaluation steps) | "Checklist: Is BPS right for you?", "Steps to choose your stream" |
| **FAQ** | Answers common question (user confusion points) | "Can I switch streams after 12th?", "What if I don't like my first choice?" |
| **Framework** | Provides structure for thinking (decision model, analysis method) | "Career Decision Framework", "Skills Assessment Model" |
| **Reflection** | Prompts self-discovery (questions, journal prompts) | "Reflect: What are your values?", "What does success mean to you?" |
| **Example** | Shows concrete instance (real career, real person, real scenario) | "Example: A day in the life of a BPS professional", "Success story: Maya's BPS journey" |

**Publication Categories:**

Each Publication is composed of Knowledge Cards and serves a specific purpose:

| Category | Purpose | Example |
|----------|---------|---------|
| **Guide** | Comprehensive, authoritative explanation of a topic | "BPS Career Guide", "Career FAQ" |
| **Workbook** | Interactive, action-oriented content for self-directed learning | "90-Day Career Clarity Plan" |
| **Playbook** | Step-by-step instructions for a specific process | "How to Choose Your Stream" |
| **Career Profile** | In-depth profile of a specific career | "Data Scientist Profile" |
| **Reference** | Quick lookup, organized by topic | "Salary Ranges by Career" (future) |
| **Toolkit** | Collection of templates, resources, checklists | "Student Career Toolkit" (future) |

**Advantage of Categories over New Types:**
- Keeps the model lean (10 objects, not 20+)
- Allows specialization (a "Checklist" card is different from a "Definition" card)
- Makes metadata more specific (a Checklist has different integrity requirements than a Definition)
- Improves search and AI consumption ("Show me all Checklist cards related to career decision")
- Scales forward (new categories can be added without changing the core model)

**Constraint:** Categories are labels, not separate objects. A "Definition" card is still a Knowledge Card. A "Guide" publication is still a Publication. They inherit all object properties and can be specialized through metadata.

---

## KNOWLEDGE OBJECTS

These objects represent the actual content and how it's structured.

### OBJECT 1: Knowledge Card

**Definition**

**A Knowledge Card is the smallest independently reusable unit of knowledge.**

It is the atomic unit of content in EnaasanOS. It cannot be meaningfully divided without losing independent value or reusability.

**Purpose & Outcome**

A Knowledge Card exists to:
- Teach one concept, answer one question, or guide one decision
- Be reused in multiple contexts (Publications, Learning Paths, search results, AI systems)
- Maintain a single source of truth (when the concept changes, it changes everywhere)

The outcome of a Knowledge Card is that **the reader understands one thing well** (concept, decision criteria, process step, etc.).

**Who It's For**

- Students (primary audience)
- Parents and teachers (secondary)
- Search engines and AI systems (tertiary)

**Description**

A Knowledge Card is:
- Focused on one topic (concept, question, decision point, example)
- Self-contained (can be understood in isolation)
- Reusable (designed to appear in multiple Publications and Paths)
- Publishable (can be rendered in any format: web, PDF, mobile, API, chat)
- Categorized (Definition, Mental Model, Checklist, FAQ, Framework, Reflection, Example)

**When to Use**

Use a Knowledge Card when you want to:
- Define a single concept ("What is BPS?")
- Answer a single question ("Why is PCM chosen for engineering?")
- Explain a single process or decision ("How do I choose my stream?")
- Provide a single example or story ("What does a day in BPS look like?")
- Create reusable content (the same "Stream Definition" card appears in 5 publications)

**When NOT to Use**

Do NOT use a Knowledge Card if:
- The content spans multiple concepts (combine into a Publication instead)
- The content is only ever used in one place, in one format, never reused (optimize for that specific context instead)
- The content is too small to stand alone independently (e.g., a single word; that's metadata, not a card)
- The content is too large to be consumed in one sitting (e.g., 5,000 words; that's a Publication, not a Card)

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

**Definition**

**A Publication is a coherent collection of Knowledge Cards designed to be published and consumed as a complete unit.**

It is the primary vehicle for multi-format publishing (web, PDF, DOCX, mobile, API, AI knowledge bases).

**Purpose & Outcome**

A Publication exists to:
- Organize related Knowledge Cards into a cohesive guide, reference, or resource
- Enable multi-format publishing (one source, many outputs)
- Provide a complete learning or reference experience on a topic

The outcome of a Publication is that **the reader has a comprehensive understanding of a topic** and can apply that understanding to make decisions or take actions.

**Who It's For**

- Students seeking in-depth information on a topic
- Parents and teachers seeking credible guidance
- Systems consuming structured knowledge (search engines, AI, recommendation engines)

**Description**

A Publication is:
- Composed of 3+ Knowledge Cards (minimum; cards are the building blocks)
- Structured with clear sections and flow (not just a list)
- Publishable to multiple formats without content duplication
- Meaningful as a complete unit (a career guide, not a fragment)
- Categorized (Guide, Workbook, Playbook, Career Profile, Reference, Toolkit)

**When to Use**

Use a Publication when:
- You have 3+ related Knowledge Cards that form a coherent topic
- The content is meant to be published as a unit (e.g., "BPS Career Guide", "Career FAQ")
- You want to enable multi-format output and reuse (web, PDF, Word, API, mobile)

**When NOT to Use**

Do NOT use a Publication if:
- You only have 1-2 cards (publish those cards directly; no publication needed)
- The content doesn't hold together coherently (split into multiple publications)
- The content is purely for navigation/structuring (use a Learning Path instead)

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

**Definition**

**A Learning Path is a curated sequence of Publications and Knowledge Cards designed to guide a learner toward a specific outcome.**

It orchestrates existing content in a specific order to maximize learning or decision-making effectiveness.

**Purpose & Outcome**

A Learning Path exists to:
- Guide learners through a sequence (not just list related content)
- Support specific learning goals (career clarity, skill development, decision-making)
- Adapt to different audiences or paces (beginner vs. advanced)

The outcome of a Learning Path is that **the learner has achieved the path's goal** (e.g., "chosen a career", "understood stream options", "developed a skill").

**Who It's For**

- Students at specific stages (10th-graders, 12th-graders, graduates)
- Parents seeking to guide their children
- Teachers seeking curriculum structure

**Description**

A Learning Path is:
- Sequential (order matters; content is consumed in a specific sequence)
- Goal-oriented (leads to a specific outcome, not just exploration)
- Composed of existing objects (reuses Publications and Cards; doesn't create new content)
- Adaptable (variations for different audiences or paces)

**When to Use**

Use a Learning Path when:
- You want to guide a specific audience from Point A to Point B
- The sequence is intentional (not arbitrary; rearranging would reduce effectiveness)
- You're combining existing content in a new way
- You want to support multiple paces or styles ("Fast Track", "Comprehensive", "For Parents")

**When NOT to Use**

Do NOT use a Learning Path if:
- You're just listing related content (that's a search result, not a path)
- The sequence doesn't matter (use a Publication instead)
- The content is unrelated (each step should build on previous ones)

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

**Definition**

**A Career is a specific, distinct career option that a student might pursue.**

It is a domain object representing a real career path with entry requirements, growth opportunities, and outcomes.

**Purpose & Outcome**

A Career object exists to:
- Describe a specific career path (entry, skills, salary, growth)
- Help students evaluate career fit
- Support career discovery and decision-making

The outcome of a Career is that **a student understands the career's requirements, opportunities, and fit for their situation** and can make an informed decision about whether to pursue it.

**Who It's For**

- Students exploring career options
- Parents wanting to understand career contexts
- Career counselors and educators
- Search engines and AI recommendation systems

**Description**

A Career is:
- Specific and distinct (e.g., "BPS", "Data Scientist", not "Technology" which is too broad)
- Owned by a subject matter expert (someone who works in or deeply knows the career)
- Described in multiple dimensions (entry paths, skills, salary, growth, challenges)
- Publishable as a Career Profile publication
- Localized (versions in multiple languages)

**When to Use**

Use a Career object when:
- You're describing a specific, named career path
- The career is distinct enough to have a LinkedIn profile or unique job description
- The career has characteristics distinct from similar careers
- Students will search for or filter by this career

**When NOT to Use**

Do NOT use a Career object if:
- The term is too broad (e.g., "IT" — split into "Software Engineer", "Data Scientist", "Network Administrator")
- You're describing a skill (use Skill instead)
- You're describing an industry or field (use a Publication instead)
- You're describing education (e.g., "B.Tech" — that's a path; the career is what you do with it)

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

**Definition**

**A Skill is a specific, teachable capability or competency that a person can develop.**

It is a domain object representing learnable, measurable competencies required by or relevant to careers.

**Purpose & Outcome**

A Skill object exists to:
- Define a specific capability or competency
- Show which careers require or value this skill
- Support learning path design (how to develop this skill)
- Enable skill-based career discovery ("what careers use this skill?")

The outcome of a Skill is that **a student understands what the skill is, why it matters, and how to develop it**.

**Who It's For**

- Students wanting to develop specific capabilities
- Careers that require certain skills
- Career counselors building learning plans
- AI systems that recommend careers based on interests/skills

**Description**

A Skill is:
- Named and specific (e.g., "Communication", "Data Analysis", not "Technical Skills")
- Independently valuable (useful in multiple careers, promotable)
- Teachable (can be developed through practice, training, experience)
- Measurable (can assess whether someone has acquired it)
- Reusable (same skill appears in multiple career profiles)

**When to Use**

Use a Skill object when:
- You're defining a specific, teachable competency
- The skill is relevant to multiple careers (promotes reuse)
- The skill has a learning path or development process
- Students will search for or filter by this skill

**When NOT to Use**

Do NOT use a Skill object if:
- You're describing a personality trait (e.g., "ambitious", "creative" — those are traits, not skills)
- You're describing education (e.g., "B.Tech" — that's a qualification, not a skill)
- You're describing an industry or field (e.g., "IT" — that's a domain)
- The skill is too vague to teach or assess (e.g., "business sense")

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

**Definition**

**An Initiative is a strategic goal or program that coordinates multiple tasks toward a measurable outcome.**

It represents "what we're trying to accomplish" at a high level and owns the knowledge assets that serve that goal.

**Purpose & Outcome**

An Initiative exists to:
- Organize work around a strategic goal
- Coordinate multiple tasks toward a single outcome
- Measure progress and success
- Own the knowledge assets (Publications, Cards) that result from the work

The outcome of an Initiative is that **a specific strategic goal is achieved** (e.g., "50 careers documented and published").

**Who It's For**

- Leadership (strategic planning and oversight)
- Teams (coordinating work)
- Metrics systems (tracking progress)

**Description**

An Initiative is:
- Strategic (connected to Enaasan's mission; matters long-term)
- Long-term (measured in quarters to years)
- Measurable (success defined by outcomes, not just completion)
- Owned by a leader (clear accountability)
- Tracked by metrics (progress is visible and measurable)

**When to Use**

Use an Initiative when:
- You want to represent a major strategic goal (e.g., "Expand career coverage to 50 careers")
- Multiple tasks will contribute to the same goal
- Success is measured by outcomes (knowledge published, coverage achieved, etc.)

**When NOT to Use**

Do NOT use an Initiative if:
- You're tracking a single task (use Task instead)
- The scope is too small (e.g., "Review one career guide" — that's a task)
- The goal is purely operational (daily maintenance work)

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

**Definition**

**A Task is a unit of work that contributes to an Initiative.**

It represents "what needs to be done" to advance toward the initiative's outcome.

**Purpose & Outcome**

A Task exists to:
- Break down an Initiative into actionable work
- Assign ownership for specific deliverables
- Track progress toward the Initiative's goal

The outcome of a Task is that **a specific deliverable is complete and integrated** (e.g., "BPS Career Guide published and linked").

**Who It's For**

- Team members (assignees)
- Initiative owners (tracking progress)
- Project management systems (task tracking)

**Description**

A Task is:
- Specific (can be clearly described, no ambiguity)
- Measurable (clear definition of "done")
- Assignable (one person owns it; they have the authority to complete it)
- Time-bounded (has a target completion date)
- Outcome-focused (results in a deliverable or decision)

**When to Use**

Use a Task when:
- You have a specific unit of work to track
- The work takes 1-2 weeks to complete (roughly)
- The work produces a deliverable (Publication, Card, etc.) or decision
- You need to assign ownership and track completion

**When NOT to Use**

Do NOT use a Task if:
- It's too small (a subtask within a larger task)
- It's ongoing operational work without a clear end (that's maintenance, not a task)
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

**Definition**

**A Decision is a documented choice between multiple valid options that affects strategic direction or implementation approach.**

It records "what we decided and why" at strategic choice points.

**Purpose & Outcome**

A Decision exists to:
- Record strategic choices (so future teams understand the reasoning)
- Make choices explicit (not implicit or forgotten)
- Enable reversal if circumstances change (with full context)

The outcome of a Decision is that **a choice is made, documented, and communicated** so the entire team understands the direction and reasoning.

**Who It's For**

- Leadership (making strategic choices)
- Architecture and design teams (designing systems)
- Future teams (understanding past reasoning)
- Auditors (understanding how choices were made)

**Description**

A Decision is:
- Strategic (affects multiple initiatives, long-term direction, or architecture)
- Documented (reasoning is recorded; not just the choice)
- Significant (reversing it would be expensive or require significant rework)
- Dated (made at a specific point in time)
- Reversible (can be changed if circumstances warrant, with full impact analysis)

**When to Use**

Use a Decision when:
- You're choosing between 2+ valid options
- The choice affects architecture, scope, or methodology
- You want to preserve reasoning for future teams
- Reversing the decision would require significant effort

**When NOT to Use**

Do NOT use a Decision if:
- There's only one valid option (not a decision; just an implementation)
- The choice is trivial (doesn't affect anything significant)
- The choice is already determined by policy or external constraint (document the constraint, not the "decision")

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

**Definition**

**A Metric is a measurable outcome that tracks progress toward an Initiative's goal.**

It quantifies success and informs decisions about whether to continue, change direction, or scale the initiative.

**Purpose & Outcome**

A Metric exists to:
- Define how we measure Initiative success
- Track progress toward goals
- Enable decision-making (continue? pivot? scale?)
- Make success visible and transparent

The outcome of a Metric is that **progress is measurable and decisions are data-informed**.

**Who It's For**

- Leadership (tracking progress, making decisions)
- Initiative owners (monitoring their initiative)
- Teams (understanding what success looks like)
- Systems (dashboards, reports, alerts)

**Description**

A Metric is:
- Specific (defined with no ambiguity; anyone should interpret it the same way)
- Measurable (can be counted, tested, or calculated)
- Time-bound (measured at specific intervals: daily, weekly, monthly, etc.)
- Actionable (results actually inform decisions or changes)

**When to Use**

Use a Metric when:
- An Initiative needs success definition and progress tracking
- The measurement is recurring (not one-time)
- Multiple people need to track and communicate about it
- The metric will influence decisions (resource allocation, direction changes, etc.)

**When NOT to Use**

Do NOT use a Metric if:
- It's a one-time measurement (measure it once, don't track it)
- It's purely informational (no decision impact)
- It's purely operational (internal team tracking, no strategic relevance)

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

**Definition**

**A Release is a versioned, coordinated collection of changes to the knowledge system.**

It groups related Publications, Cards, and improvements that go live together and marks a significant point in the system's evolution.

**Purpose & Outcome**

A Release exists to:
- Coordinate multiple changes (Publications, Cards, fixes) into coherent units
- Communicate "what's new" to users and teams
- Enable rollback if issues are discovered
- Mark significant milestones in the system's evolution

The outcome of a Release is that **users and systems have a clear, versioned snapshot of the knowledge at a point in time**.

**Who It's For**

- Users (seeing "what's new" in release notes)
- Systems (rolling back to previous versions if needed)
- Teams (coordinating deployments)
- Metrics systems (tracking adoption of new content)

**Description**

A Release is:
- Versioned (e.g., v1.0, v1.1, v2.0; follows semantic versioning or similar)
- Coordinated (groups related changes; multiple changes released together)
- Documented (release notes explain what changed and why)
- Reproducible (can be deployed identically multiple times)

**When to Use**

Use a Release when:
- You want to group related Publications, Cards, or improvements
- Multiple changes should go live together (not individually)
- You want a clear version number for reference
- You want to communicate changes to users via release notes
- You want the ability to rollback to a previous state if needed

**When NOT to Use**

Do NOT use a Release if:
- You're tracking every single small change (that's object versioning, not release versioning)
- A single card or publication update is isolated and doesn't need coordination
- Changes are so frequent that releases would be meaningless (might need more frequent release cadence instead)

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

### Purpose and Outcome (Universal)

Every object in EnaasanOS SHALL have an explicit **Purpose** and **Outcome**.

**Purpose:** Why does this object exist? What problem does it solve? What value does it create?

**Outcome:** What should happen as a result of this object existing and being consumed?

**Why these matter:**
- Purpose keeps the model grounded in reality (why are we building this?)
- Outcome makes success measurable (how do we know if this object is working?)
- Together, they enable AI systems to understand context (not just structure)
- Together, they guide reuse decisions (should this object appear in multiple places?)

**Examples:**

| Object | Purpose | Outcome |
|--------|---------|---------|
| Career (BPS) | Help students understand BPS as a career option | Student can decide whether BPS aligns with their goals |
| Skill (Communication) | Define a core skill needed by many careers | Student knows what communication means and can develop it |
| Knowledge Card (Stream Decision) | Help students understand stream options | Student can choose between PCM, PCB, Commerce based on their interests |
| Learning Path (Career Clarity) | Guide students through complete career decision-making | Student has chosen a career path and knows next steps |
| Initiative (Expand Careers) | Document careers systematically | 50+ career guides published with consistent quality |
| Task (Write BPS Guide) | Create comprehensive BPS career guide | BPS career guide is published and integrated |
| Metric (Career Coverage) | Track progress toward career documentation goal | Leadership can see we're on track or need to adjust pace |

**Note:** These are introduced here in EOS-002. Specific metadata fields for Purpose and Outcome will be defined in EOS-003 (Universal Metadata Contract).

---

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
| 1.1 | 2026-07-12 | Major revision: Freeze 10 object types; introduce Object Categories (Knowledge Card types, Publication types); refine Knowledge Card definition to "smallest independently reusable unit"; restructure all object definitions to answer What/Why/Who/When/What Outcome; introduce Purpose and Outcome as universal concepts; focus model on publishing/reuse/search/AI value | Chief Knowledge Architect |
| 1.0 | 2026-07-12 | Initial specification: 10 first-class objects with lifecycle, integrity attributes, evidence classification | Chief Knowledge Architect |

