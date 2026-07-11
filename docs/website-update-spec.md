# enaasan.online — Website Update Specification

## Purpose

Prepare enaasan.online for sustainable student acquisition through social content, WhatsApp sharing, search, and college/community distribution. The immediate objective is to improve conversion, trust, sharing, and measurement before expanding content volume.

## Guiding Principles

- Keep browsing frictionless: visitors must be able to explore without mandatory sign-up.
- Add optional, valuable conversion points after users receive guidance.
- Prioritise mobile users, especially students accessing links through Instagram, WhatsApp, and search.
- Make high-stakes guidance transparent: display author, review date, sources, and verification reminders.
- Build every article as a shareable, discoverable landing page—not just a reading page.
- Start with English; localise selected high-demand guides into Telugu after the core system is stable.

---

# Phase 1 — Must Complete Before Promotion

## 1. Optional Subscriber Capture

### Objective
Turn a portion of one-time visitors into an audience enaasan can reach again, while preserving the current no-compulsory-sign-up experience.

### Requirements

- Add an optional email or WhatsApp subscription component.
- Do **not** gate regular articles or core website navigation.
- Ask for only one contact method per form: email **or** WhatsApp number.
- Add clear consent copy: `No spam. Unsubscribe anytime.`
- Link to the Privacy Policy beside the form.
- Track form views, starts, submissions, and successful completions.

### Suggested placement

- End of every major guide/article.
- Homepage below the main pathway cards.
- Exit-intent or scroll-depth prompt only if it does not harm mobile usability.

### Suggested copy

**Heading:** Get practical career guidance, once a week

**Body:** Short, honest guidance for Indian students and families. No coaching sales pitch. No spam.

**CTA:** Get the Career Clarity Starter Pack

---

## 2. Flagship Downloadable Resource

### Objective
Provide a compelling reason to subscribe and a practical asset students can save and share.

### First resource recommendation

**Title:** After Graduation: A 90-Day Career Clarity Plan

### Alternative resource if the immediate audience becomes Class 12 students

**Title:** After 12th: The Indian Student’s Decision Checklist

### Requirements

- Create a short, visually clean, mobile-readable PDF.
- Include actionable worksheets/checklists, not just exported article text.
- Add enaasan branding, website URL, and a clear next-step CTA.
- Create a dedicated landing page for the resource.
- Use the same resource as the primary CTA in related social posts.
- Track PDF downloads and landing-page conversion rate.

### Suggested contents for the 90-day plan

- Week 1: clarify current situation and constraints
- Weeks 2–3: choose target roles/pathways
- Weeks 4–6: identify and close skill gaps
- Weeks 7–9: build portfolio, resume, and evidence of skills
- Weeks 10–12: job search, networking, applications, and interview practice
- A weekly tracker and a parent/family conversation checklist

---

## 3. Strong Article-Level Calls to Action

### Objective
Give each visitor a clear next step after consuming content.

### Requirements

- Add one primary CTA per article, based on the page topic.
- Avoid placing multiple competing CTAs in the same visual section.
- Use consistent button styles and accessible contrast.
- Add CTA click tracking.

### Suggested CTAs

- `Not sure where to begin? Find your starting point.`
- `Get the free 90-day career clarity plan.`
- `Explore what comes after Class 12.`
- `Build your college-to-career action plan.`
- `Send this guide to a parent or guardian.`

---

## 4. Share Infrastructure

### Objective
Make every useful page easy to forward to a specific student, friend, parent, teacher, or group.

### Requirements

- Add sharing controls to all major guides.
- Prioritise: WhatsApp, Copy Link, LinkedIn.
- Ensure all share buttons work well on mobile.
- Use the page title and a short, useful pre-filled share message where platform APIs allow it.
- Track share-button clicks by channel and page.

### Contextual share prompts

- `Know someone deciding after Class 12? Send them this guide.`
- `Share this with a final-year student who may need it.`
- `Want to discuss this at home? Send this guide to a parent or guardian.`

### Shareable visual card

Add a mobile-first vertical card near the end of major articles containing:

- One memorable insight or decision prompt
- Article/topic title
- enaasan logo and domain
- QR code pointing to the guide
- Short share prompt

This card should be reusable as a WhatsApp image, Instagram Story asset, or carousel slide.

---

## 5. Author, Review, and Trust Signals

### Objective
Build trust for career and education guidance, especially where students are making consequential decisions.

### Requirements

- Add an author box to every article.
- Display `Written and reviewed by Siddique Ahamed`.
- Include a concise, accurate credibility line based on relevant experience in learning, workforce readiness, L&D, and career guidance.
- Link to a founder/author page and optionally LinkedIn.
- Display `Last reviewed: <date>` on every substantive guide.
- Include `Report an issue` / `Suggest a correction` links on all major pages.

### Suggested author box copy

**Written and reviewed by Siddique Ahamed**

Learning and development professional with 23+ years of experience in corporate learning, workforce skills, and learning technology. enaasan provides practical, India-first guidance to help students make more informed decisions.

---

## 6. Sources and High-Stakes Content Notices

### Objective
Make claims about admissions, exams, eligibility, fees, cut-offs, rules, and timelines verifiable.

### Requirements

- Add a `Sources and official links` section to high-stakes pages.
- Link to primary/official sources wherever possible.
- Add an update notice: `Rules, dates, fees, eligibility and cut-offs can change. Verify important decisions with the relevant official authority.`
- Add source publication/update dates where available.
- Do not present volatile information as permanent fact.

---

## 7. Legal and Privacy Pages

### Create or update

- Privacy Policy
- Terms of Use
- Career and education guidance disclaimer
- Cookie notice/consent mechanism if analytics, marketing pixels, or non-essential cookies are used
- Contact page or clear contact method

### Disclaimer requirements

- Clarify that enaasan provides educational and informational guidance, not guarantees of admissions, employment, salary, or outcomes.
- State that users must verify time-sensitive information from official institutions and authorities.
- Clarify the role of AI assistance and human editorial responsibility, consistent with the site’s stated approach.

---

## 8. Analytics and Attribution

### Objective
Measure which topics, channels, and CTAs create useful student engagement.

### Required setup

- Google Analytics 4 or a privacy-conscious alternative such as Plausible.
- Google Search Console.
- Event tracking for:
  - Share-button clicks
  - CTA clicks
  - Form views and submissions
  - Resource downloads
  - Outbound clicks to official sources
  - Student-question submissions
  - Scroll depth on long guides

### UTM naming convention

Use consistent UTM parameters for every social, email, WhatsApp, partner, and campaign link.

Example:

```text
https://enaasan.online/graduate?utm_source=linkedin&utm_medium=organic&utm_campaign=after_graduation_90_day_plan
```

Suggested values:

- `utm_source`: linkedin, instagram, youtube, whatsapp, email, college_partner
- `utm_medium`: organic, carousel, reel, short, newsletter, qr, referral
- `utm_campaign`: descriptive_lowercase_campaign_name

---

# Phase 2 — Core Navigation and Content Experience

## 9. Start Here Guided Pathway

### Objective
Help visitors quickly find relevant guidance instead of guessing which page to open.

### Page/feature

Create a `Start Here` page or a lightweight guided decision flow.

### Questions

1. Where are you now?
   - Class 10
   - Class 11–12 / Intermediate
   - College student
   - Recent graduate
   - Parent, teacher, or counsellor
2. What do you need help with?
   - Stream selection
   - Course/college choice
   - Entrance exams
   - Career options
   - Skills and internships
   - Job readiness
   - Higher studies
3. What is your biggest concern today?

### Output

Show 3–5 recommended enaasan guides and one optional lead-magnet CTA.

### Requirements

- No sign-up required.
- Mobile-first UI.
- URL or local storage state should ideally preserve the result for return visits.
- Track selections and result-page clicks.

---

## 10. Topic Hub Pages

### Objective
Turn the current life-stage navigation into structured content hubs that improve usability, internal linking, search visibility, and social campaign targeting.

### Recommended hubs

| URL | Purpose |
|---|---|
| `/after10` | Stream decisions, vocational paths, myths, and next steps after Class 10 |
| `/after12` | Entrance routes, degree options, alternatives, cost, and career outcomes |
| `/college` | Skills, internships, portfolios, placements, and first-job preparation |
| `/graduates` | Job search, reskilling, higher studies, and the 90-day plan |
| `/parents` | Guidance for parents without pressure or misinformation |
| `/careers` | Career maps by industry, job role, route, skills, and realistic outcomes |

### Hub page requirements

- Clear introduction and who the page is for.
- Featured guides.
- Common questions.
- Decision map or visual framework.
- Links to related comparisons and next steps.
- One relevant optional subscriber/download CTA.
- Article cards with review dates where appropriate.

---

## 11. Related Content and Next-Step Blocks

### Objective
Prevent dead ends and guide readers from a single question to a complete decision journey.

### Requirements

- Add a `What to read next` block to every substantive article.
- Show 3 relevant links based on topic and student stage.
- Include at least one action-oriented next step.
- Avoid generic recommendations; make recommendations context-sensitive.

### Example: B.Com article

- Careers beyond CA
- B.Com vs BBA: which route suits whom?
- Skills to build during first year of college

---

## 12. Comparison and Decision Pages

### Objective
Create high-intent content that students and families frequently search for and share.

### Initial content backlog

- B.Com vs BBA: careers, cost, skills, and who each route suits
- PCM vs PCB: pathways, workload, and career options
- CA vs CS vs CMA: route, difficulty, time, cost, and outcomes
- JEE route vs state entrance route for engineering
- Degree college vs diploma: who should choose which?
- B.Tech vs BCA: realistic roles and career pathways
- Government college vs private college: a decision framework beyond rankings
- MBA immediately after graduation vs work experience first

### Standard comparison template

- Short answer
- Who each option suits
- Entry requirements
- Cost and time commitment
- Skills required
- Typical career paths
- Risks and misconceptions
- What to do next
- Sources and last-reviewed date

---

## 13. Glossary

### Objective
Explain confusing education and career terminology in simple, India-relevant language and strengthen internal linking.

### Initial terms

- CUET
- Credit system
- Lateral entry
- Internship
- Placement
- Portfolio
- NIRF
- Accreditation
- BPS
- KPO
- Apprenticeship
- Skill certificate
- Entrance exam
- Cut-off
- Eligibility

### Requirements

- Keep entries concise.
- Link each term to a deeper relevant guide.
- Add contextual glossary links in articles without over-linking.

---

# Phase 3 — Student Readiness and Audience Participation

## 14. Mobile-First UX Review

### Checklist

- Test every core page on common Android screen widths.
- Confirm readable body text, line height, and contrast.
- Ensure tables have a mobile alternative: stacked cards, horizontal scrolling with cues, or simplified comparison blocks.
- Use large, accessible tap targets.
- Optimise images, fonts, JavaScript, and layout shift for fast loading on mobile data.
- Ensure sticky CTA/share controls do not obscure text or navigation.
- Test navigation, forms, PDF downloads, and share actions in Chrome Android.

---

## 15. Quick Answer Blocks

### Objective
Help visitors from search and social get value quickly while retaining a route into deeper guidance.

### Add near the top of long guides

```text
Quick answer

Short answer: ...

This route may suit you if: ...

Be cautious if: ...

What to do next: ...
```

### Requirements

- Use plain language.
- Do not oversimplify or make guarantees.
- Link to the relevant deeper section or next page.

---

## 16. Student Question Submission

### Objective
Create a direct pipeline of real student needs that can guide future articles, social posts, videos, FAQs, and tools.

### Feature

A simple page/form with the prompt: `What are you confused about?`

### Fields

- Current stage: Class 10, Class 11–12, college, graduate, parent/teacher
- Topic: stream, course, entrance, career, skills, job, higher studies, other
- Question (required)
- Optional anonymous submission toggle
- Optional contact method only if the user wants a response

### Requirements

- Do not imply individual counselling or guaranteed replies unless operationally supported.
- Publish a clear privacy note.
- Add spam protection.
- Build an internal review workflow for submissions.
- Track topic frequency to inform the editorial calendar.

---

## 17. Telugu Localisation

### Objective
Build relevance and reach in Telangana and Andhra Pradesh without creating an unmaintainable translation burden.

### Phase approach

- Do not translate the entire website at once.
- Translate/localise only high-demand, high-stakes, high-traffic guides first.
- Use human review for accuracy, natural language, and cultural fit.

### Suggested first Telugu pages

- What to do after Intermediate
- Course-choice basics
- B.Com and BBA pathways
- Engineering routes
- Post-graduation job readiness plan

### Technical requirements

- Use clear language routes, e.g. `/te/after12`.
- Add language switchers that preserve the closest equivalent page.
- Implement correct `hreflang` metadata.
- Do not mix languages within the main article body unless intentionally designed.

---

## 18. Student Stories and Social Proof

### Objective
Demonstrate relevance through real situations while maintaining privacy and accuracy.

### Requirements

- Collect explicit consent before publishing identifiable stories.
- Support anonymous and pseudonymous submissions.
- Label stories clearly as personal experiences, not universal advice.
- Do not publish unverifiable outcomes or exaggerated claims.
- Use a standard format: situation, confusion, options considered, decision framework, next action.

---

# Phase 4 — Advanced Features (Build Later)

## 19. Personalised Recommendation Quiz

Build only after the topic hubs and recommendation logic are mature.

Requirements:

- Clear boundaries: guidance, not a definitive career prescription.
- Explain what inputs influence results.
- Give recommended reading paths, not a single “best career” output.
- Preserve privacy and minimise data collection.

## 20. Ask Enaasan AI Mentor

Build only after the site has a robust, maintained knowledge base and governance model.

Requirements:

- Ground responses in enaasan content and cited official sources.
- Display source links and content review dates.
- Use clear career/admissions disclaimers.
- Avoid high-confidence answers where facts are uncertain or volatile.
- Provide escalation paths to official sources or qualified counsellors for sensitive/high-stakes questions.
- Log anonymised failure cases and update the knowledge base regularly.

---

# Cross-Site Design System Requirements

## Reusable components to build

- Primary CTA module
- Optional subscription form
- Downloadable-resource card
- Article author/reviewer box
- Last-reviewed and source list module
- High-stakes verification notice
- WhatsApp/LinkedIn/copy-link sharing bar
- Shareable social/QR card
- Related-content block
- Quick-answer block
- Report-an-issue link/component
- Article card with audience label, update date, and topic tag

## Content metadata for every article

Store and render where relevant:

- Title
- Slug/URL
- Student stage/audience
- Topic/category
- Short summary
- Author/reviewer
- Published date
- Last-reviewed date
- Sources
- Main CTA
- Related articles
- Social share title/description/image

---

# Suggested Technical Tracking Events

Use consistent event names, adapting them to the chosen analytics platform.

| Event | Trigger | Useful properties |
|---|---|---|
| `cta_click` | Primary or secondary CTA clicked | page, cta_name, destination |
| `share_click` | Share control clicked | page, channel |
| `copy_link` | Copy-link action completed | page |
| `lead_form_view` | Subscription form becomes visible | page, placement |
| `lead_form_submit` | Subscription form submitted | page, contact_type |
| `resource_download` | PDF/resource download | resource_name, page |
| `outbound_official_click` | Official external source clicked | page, domain |
| `question_submit` | Student question form submitted | stage, topic, anonymous |
| `guided_path_complete` | Start Here flow completed | stage, concern, recommendation_set |
| `related_article_click` | Related content clicked | source_page, target_page |

---

# Acceptance Checklist for Phase 1

Do not begin broad social promotion until these are complete:

- [ ] Visitors can browse without creating an account or providing contact details.
- [ ] At least one optional subscription mechanism is live and privacy-compliant.
- [ ] One flagship downloadable resource has a landing page and tracking.
- [ ] WhatsApp, LinkedIn, and copy-link sharing work on major guides.
- [ ] Each major guide has one clear, relevant primary CTA.
- [ ] Each major guide has an author/reviewer box and last-reviewed date.
- [ ] High-stakes pages contain official sources and a verification notice.
- [ ] Privacy Policy, Terms, Disclaimer, and contact/correction route are live.
- [ ] Analytics and Search Console are configured.
- [ ] CTA, sharing, resource download, and form events are tracked.
- [ ] UTM naming convention is documented and ready for campaign use.
- [ ] Mobile testing has been completed for homepage, hub pages, top articles, forms, and sharing.

---

# Recommended Development Order

1. Legal/privacy pages and analytics foundation
2. Reusable CTA, subscription, share, author, source, and review-date components
3. Flagship resource and its landing page
4. Homepage CTA and article-level CTA placement
5. UTM/tracking implementation and validation
6. Start Here guided pathway
7. Topic hubs and related-content logic
8. Question-submission feature
9. Comparison-page templates and first articles
10. Telugu localisation of selected priority content
11. Advanced personalisation and AI features

---

# Definition of Done

A page is ready for promotion when it:

- Answers one clear student or parent question.
- Is readable and fast on a mobile phone.
- Includes a quick answer and an appropriate next step.
- Displays an author/reviewer and last-reviewed date.
- Includes sources and verification notes if information is time-sensitive or high-stakes.
- Has sharing controls and a contextual sharing prompt.
- Has one measurable CTA.
- Links to relevant enaasan resources rather than ending at a dead end.
- Has complete social metadata: title, description, and image.
