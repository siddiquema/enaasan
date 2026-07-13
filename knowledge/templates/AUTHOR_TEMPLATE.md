# Author Template — the only metadata you write

You are writing a Knowledge Card or Publication for Enaasan. Of the ~24 metadata fields the system tracks, **you write nine.** Everything else is assigned automatically or set by your reviewer — don't fill it in, don't worry about it.

Copy the block below to the top of your draft and replace every `TODO`. Guidance for each field follows. Budget: **5–10 minutes** once you've done it twice.

---

## Copy this

```yaml
---
title: "TODO"
description: "TODO — 1–2 sentences: what this is and who should care"
purpose: "TODO — the student decision or fear this serves"
outcome: "TODO — a capability the student gains: 'Student can …'"
stage: [TODO]        # any of: after10, after12, college, graduate, early-career
audience: [TODO]     # any of: student, parent, educator
evidence: TODO       # your honest proposal: primary-research | secondary-research | expert-opinion | anecdotal | opinion
evidence_notes: "TODO — name what this rests on"
uncertainty: "TODO — what you don't know, what varies, what the reader must verify"

# Optional — only if you already know them:
stakes: TODO         # high | medium | low — your proposal; the reviewer decides
volatile: TODO       # true if it contains salaries, fees, exam patterns, cutoffs, hiring trends
---
```

---

## How to fill each field

### `title`
Plain words, for the reader, and **honest** — the title may not promise more than the content delivers. If your examples are constructed, don't call them "real."

### `description` vs `purpose` — they are different
- **description** = *what it is*: "A framework of the five communication competencies employers assess, with a self-rating table."
- **purpose** = *the student moment it serves*: "Helps a student facing 'strong communication skills required' in a job posting understand what will actually be assessed."

If your purpose reads like a summary of the content, it's a description. Name the decision or the fear.

### `outcome` — phrase it as a capability, always
The outcome is what the student **can do** afterwards — never what they will decide. We inform decisions; we don't make them.

✅ "Student can compare B.Com and BBA using criteria that matter to their own situation."
✅ "Student can evaluate any 'soft skills matter' claim in rupee terms."
✅ "Student can locate their communication gaps and choose roles that match their current level."
❌ "Student chooses B.Com." — decision made for them; will be rejected at review.
❌ "Student understands communication." — too vague to check.

Best outcomes name a **transferable** capability: not just this answer, but the ability to judge the next question alone.

### `stage` and `audience`
List **everywhere** the content genuinely applies — multiple values are normal and good (that's how the same card serves several hubs without being rewritten). Don't stretch: a graduate-interview card doesn't serve `after10` just because a 15-year-old could theoretically read it.

### `evidence` — be honest; your reviewer will check
Rate by your **weakest important claim**, not your best source:

| Level | Means |
|---|---|
| `primary-research` | We gathered it ourselves (interviews, surveys we ran) |
| `secondary-research` | Published reports, official data, postings analysis |
| `expert-opinion` | Informed judgment — including *your own synthesis or framework* |
| `anecdotal` | Stories, individual reports, **illustrative composites** |
| `opinion` | A position we hold and argue for |

Two traps the pilot caught, so you don't repeat them:
- **Your own framework or grouping is `expert-opinion`**, even if it's built on real research. The synthesis is yours.
- **Constructed examples** ("Agent A vs Agent B") built on real salary data: if the example *is* the point of the card, rate `anecdotal`, say "illustrative composite" in `evidence_notes`, and label it in the body. If the example only illustrates a claim proven elsewhere, the real data's rating stands — but still disclose the composite.

### `evidence_notes`
Name the actual sources: "NASSCOM BPS report 2024-25; Glassdoor/AmbitionBox postings analysis; 25 practitioner interviews." Not "research shows."

### `uncertainty` — required thinking, with starters per card type
What don't you know? What varies by city, company, year? What must the reader verify themselves? Starting points:

- **Definition** → "This is one widely-used framing, not a universal standard; employers weight it differently."
- **Salary / fees / dates** → what varies, by roughly how much, and where to check live figures.
- **Checklist / self-assessment** → "Self-assessment is unreliable; thresholds are heuristics; get an outside view."
- **Example** → "Illustrative composite — no real outcome will match; read as direction, not forecast."
- **Framework / mental model** → where the model breaks down or doesn't apply.

Writing "nothing is uncertain" is almost never true and will block publication on high-stakes content.

### `stakes` and `volatile` (optional proposals)
- **stakes** = what it costs a student if this is wrong. `high`: can redirect years or money (eligibility, entry requirements). `medium`: shapes preferences (salary ranges, readiness guidance). `low`: error costs a re-read. Propose it if you have a view — the reviewer confirms either way.
- **volatile** = `true` if the content contains data that ages in months. This sets how often we're obliged to re-verify your card, automatically.

---

## What happens after you submit

1. Automatic: id, domain, category, language, dates, version, status, license get assigned.
2. Your reviewer confirms `stakes` and `evidence` (adversarially — that's their job, not distrust), checks your `outcome` phrasing and `uncertainty`, and sets the review date.
3. Your card starts at `maturity: seed` and earns its way up through reviews, real usage, and feedback. That's normal; everything starts there.

Questions the template doesn't answer: `knowledge/architecture/metadata-standard.md` has the full rules, and `knowledge/LEARNING_PHILOSOPHY.md` has the why.
