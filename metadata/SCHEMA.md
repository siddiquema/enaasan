# Publication Metadata Schema

**Version:** 1.0  
**Last Updated:** 2026-07-17  
**Status:** Frozen (part of Knowledge Standard v1.0)

---

## Overview

Every publication on Enaasan must include a metadata JSON file that describes:
- What the publication teaches
- Who it's for
- Questions it answers
- How it connects to other content

**Storage:** `/metadata/publications/[publication-name].json`

---

## Field Definitions

### Core Fields (Required)

#### `id` (string)
Unique identifier for this publication. Format: `type-number-slug`

Examples:
- `guide-001-first-job`
- `hub-001-communication`
- `card-003-comm-salary`

**Rules:**
- Lowercase
- Use hyphens to separate words
- No spaces or special characters
- Must be unique across all publications
- Never change (stability over time)

---

#### `title` (string)
Full title of the publication as it appears to students.

Examples:
- "How to Get Your First Job"
- "The Five Communication Competencies"
- "Am I Ready? Communication Readiness Checklist"

**Rules:**
- Human-readable, friendly
- 3-60 characters
- Specific (not generic like "Career Guide")
- Answer-oriented when possible

---

#### `url` (string)
Full path where the publication lives on the website.

Examples:
- `/skills/first-job/`
- `/skills/communication/definition/`
- `/career-exploration/01-who-are-you.html`

**Rules:**
- Starts with `/`
- Matches actual URL on site
- Include trailing slash for directories
- Include `.html` for files
- Must be accessible and live (or coming-soon)

---

#### `description` (string)
One or two sentences that explain what the student will learn/understand.

Examples:
- "Learn how employers think when hiring fresh graduates. Understand what companies actually look for beyond grades and qualifications."
- "Discover your strengths, interests, values, and working style to make career decisions that actually fit."

**Rules:**
- Clear and concrete
- Focus on what student LEARNS, not what document IS
- 50-150 characters
- Written for student audience (not search engines)
- No jargon

---

#### `target_audience` (string)
Who this publication is designed for.

Examples:
- "College students and fresh graduates"
- "College graduates exploring career options"
- "College students preparing for careers"

**Rules:**
- Describe the person, not the degree
- Include education level + career stage
- Be specific (not just "everyone")

---

#### `duration` (string)
How long it takes to complete this publication.

Examples:
- "15 minutes"
- "45 minutes"
- "90 minutes (5 cards)"

**Rules:**
- Include unit (minutes, hours)
- Be realistic (test it)
- For hubs with multiple cards, show total + breakdown
- Format: "X minutes" or "X hour(s)"

---

#### `keywords` (array of strings)
Words a student might search for to find this.

Example:
```json
[
  "job",
  "first job",
  "graduate",
  "career",
  "hiring",
  "employability",
  "interview"
]
```

**Rules:**
- Lowercase
- 5-20 keywords per publication
- Include variations (job, first job, career)
- Include synonyms (salary, compensation, earnings)
- Include related concepts
- No stop words (a, the, and)

---

#### `questions_it_answers` (array of strings)
Actual questions a student might ask that this publication answers.

Example:
```json
[
  "How do I get my first job?",
  "What do employers look for?",
  "How do companies hire graduates?",
  "What matters more than grades?"
]
```

**Rules:**
- 2-6 questions per publication
- Written as actual student questions
- Start with question words (How, What, Why, When)
- End with question mark
- Specific to this publication
- Cover main use cases for search

---

#### `related_publications` (array of strings)
IDs of other publications students might find useful.

Example:
```json
[
  "guide-002-who-are-you",
  "guide-003-discover-careers",
  "guide-004-skills-required"
]
```

**Rules:**
- Reference by ID, not title
- Include publications 2-5 related items
- Use for contextual discovery
- Include guides that came before or after
- Update when relationships change

---

#### `next_publication` (string)
ID of the recommended next publication in sequence.

Example:
```json
"next_publication": "guide-002-who-are-you"
```

**Rules:**
- Single ID (string, not array)
- Must be a published or coming-soon publication
- Represents the natural next step for a student
- For series, should be the next item in series
- For standalone, link to thematically related guide

---

#### `tags` (array of strings)
Labels that categorize this publication.

Example:
```json
[
  "career",
  "first-job",
  "employability",
  "job-search"
]
```

**Rules:**
- 2-5 tags per publication
- Lowercase, hyphenated
- Broad category words
- Must be consistent across publications
- Use existing tags when possible
- Add new tags only when necessary

---

#### `status` (string)
Whether this publication is live or planned.

Values:
- `"published"` — Live on the website
- `"coming-soon"` — Announced but not yet live
- `"draft"` — Internal, not shown in search

**Rules:**
- Only published or coming-soon shown in search
- Draft status for internal work only
- Change status when publication goes live
- Coming-soon can appear in search with "Coming Soon" badge

---

### Optional Fields

#### `published_date` (string)
Date the publication went live.

Format: `"YYYY-MM-DD"` (ISO 8601)

Example:
```json
"published_date": "2026-07-17"
```

**Rules:**
- ISO format only
- Date the guide was published, not updated
- Null for coming-soon items
- Helps track content age

---

#### `part_of_series` (string)
Name of the series this publication belongs to.

Example:
```json
"part_of_series": "career-exploration"
```

**Rules:**
- Identify the series slug
- Must match series name consistently
- Helps group related content
- Optional for standalone guides

---

#### `series_order` (number)
Position in the series (0-indexed or 1-indexed).

Example:
```json
"series_order": 1
```

**Rules:**
- Number indicating position
- 0 or 1 to start (be consistent)
- Used for navigation ordering
- Must be unique within series

---

#### `is_hub` (boolean)
Whether this is a hub page containing multiple cards.

Example:
```json
"is_hub": true
```

**Rules:**
- `true` only for hub/collection pages
- `false` or omit for individual guides
- Hubs typically have `contains_cards` field

---

#### `contains_cards` (array of strings)
IDs of cards contained in this hub.

Example:
```json
"contains_cards": [
  "card-001-comm-definition",
  "card-002-comm-framework",
  "card-003-comm-salary"
]
```

**Rules:**
- Only for hub publications
- List IDs in order
- Must match actual card IDs in metadata
- Update when cards are added/removed

---

#### `part_of_hub` (string)
ID of the hub this card belongs to.

Example:
```json
"part_of_hub": "hub-001-communication"
```

**Rules:**
- Only for card publications
- Reference the hub ID
- Used to navigate back to hub
- Must match a real hub ID

---

#### `card_order` (number)
Position within the hub (1-indexed).

Example:
```json
"card_order": 1
```

**Rules:**
- 1 to start
- Sequential within hub
- Used for card navigation

---

## Complete Example

```json
{
  "id": "guide-003-discover-careers",
  "title": "Use AI to Discover Careers That Suit You",
  "url": "/skills/first-job/explore-careers/",
  "description": "Discover 3-5 careers worth exploring using AI tools. Understand what professionals do, shortlist options, and create a Career Exploration Sheet.",
  "target_audience": "College graduates exploring career options",
  "duration": "45 minutes",
  "keywords": [
    "career",
    "careers",
    "career exploration",
    "career discovery",
    "job roles",
    "career options",
    "AI",
    "ChatGPT"
  ],
  "questions_it_answers": [
    "What careers should I explore?",
    "How do I discover the right career for me?",
    "What do professionals actually do in different roles?",
    "How can I narrow down my career options?",
    "What careers are growing?"
  ],
  "related_publications": [
    "guide-002-who-are-you",
    "guide-004-skills-required",
    "guide-001-first-job"
  ],
  "next_publication": "guide-004-skills-required",
  "tags": [
    "career",
    "career-exploration",
    "ai",
    "job-discovery"
  ],
  "status": "published",
  "published_date": "2026-07-16",
  "part_of_series": "career-exploration",
  "series_order": 2
}
```

---

## Validation Rules

### Type Checking
- `id`: string
- `title`: string
- `url`: string starting with `/`
- `description`: string
- `target_audience`: string
- `duration`: string
- `keywords`: array of strings (lowercase)
- `questions_it_answers`: array of strings (end with `?`)
- `related_publications`: array of strings (valid IDs)
- `next_publication`: string or null
- `tags`: array of strings (lowercase, hyphenated)
- `status`: string from approved list
- `published_date`: string (ISO 8601) or null
- `series_order`: number >= 0
- `is_hub`: boolean
- `card_order`: number > 0

### Business Rules
1. Every published publication must have a `next_publication`
2. Coming-soon publications can have null `next_publication`
3. All referenced IDs in `related_publications` must exist
4. `next_publication` ID must exist
5. Hub pages must have `is_hub: true` and `contains_cards`
6. Cards must have `part_of_hub` field
7. `part_of_series` must be consistent across series items
8. Series order must be sequential within each series

---

## Maintenance Guidelines

### When Creating New Publication
1. Choose unique ID
2. Fill all required fields
3. Research and write `keywords` and `questions_it_answers`
4. Link `related_publications`
5. Set `next_publication`
6. Validate JSON (use JSONLint)
7. Add to `_index.json`

### When Updating Publication
1. Update fields that changed
2. Update `related_publications` if links changed
3. DO NOT change `id` or `url`
4. Update `published_date` only for first publication
5. Revalidate JSON

### When Retiring Publication
1. Change `status` to `"draft"`
2. Update `related_publications` in other guides
3. Update `next_publication` in preceding guides
4. Keep metadata file for reference

---

## Future Considerations

This schema is frozen for Knowledge Standard v1.0 but may be extended in future versions to support:
- Difficulty levels (beginner, intermediate, advanced)
- Prerequisite publications
- Time to complete variations (if content length varies)
- Content versioning
- Multiple language support metadata

Any schema changes require architectural review and explicit approval.

---

*Metadata Schema v1.0 — Stable and frozen as part of Enaasan Knowledge Standard.*
