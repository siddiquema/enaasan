# Ask Enaasan: Student-Centric Search System

**Philosophy:** Students search for answers, not pages.

---

## Overview

Ask Enaasan is a lightweight, metadata-driven search experience that helps students find the right guidance content by answering their questions.

**NOT** a traditional website search feature.

**Key Principle:**
> Students do not search for pages. Students search for answers to questions.

---

## System Architecture

### Metadata Layer
- **Location:** `/metadata/publications/`
- **Format:** JSON files (machine-readable, client-side queryable)
- **Structure:** One file per publication + central index (`_index.json`)
- **Fields:** title, url, description, target_audience, duration, keywords, questions_it_answers, tags, status, etc.

### Search Engine
- **File:** `/js/ask-enaasan.js`
- **Type:** Client-side (no backend required)
- **Capability:** Full-text search across metadata
- **Match types:** title, keywords, questions, description, tags
- **Scoring:** Relevance-based ranking

### UI Component
- **File:** `/components/ask-enaasan-search.html`
- **Type:** Reusable HTML/CSS/JS component
- **Placement:** Homepage, First-Job Guide, Guidance Hub
- **Interaction:** Real-time search with example chips

---

## Metadata Structure

Every publication must have a metadata JSON file in `/metadata/publications/`

### Required Fields

```json
{
  "id": "unique-id",
  "title": "Publication Title",
  "url": "/path/to/publication/",
  "description": "Brief description of what this guide teaches",
  "target_audience": "Who this is for",
  "duration": "15 minutes",
  "keywords": ["tag1", "tag2", "tag3"],
  "questions_it_answers": [
    "Question 1?",
    "Question 2?"
  ],
  "related_publications": ["id-001", "id-002"],
  "next_publication": "id-next",
  "tags": ["tag1", "tag2"],
  "status": "published"
}
```

### Optional Fields

```json
{
  "published_date": "2026-07-17",
  "part_of_series": "series-name",
  "series_order": 1,
  "is_hub": true,
  "contains_cards": ["card-001", "card-002"],
  "part_of_hub": "hub-id",
  "card_order": 1
}
```

### Status Values

- `"published"` — Live on website
- `"coming-soon"` — Not yet published (appears in search results with "Coming Soon" badge)
- `"draft"` — Not yet shown in search

---

## Search Behavior

### How Search Works

1. **User enters query** → "How do I improve my communication?"
2. **Search engine normalizes** → breaks into terms
3. **Matches against** → title, keywords, questions, description, tags
4. **Scores relevance** → higher score = better match
5. **Returns results** → sorted by relevance
6. **Displays** → title, description, duration, tags, status

### Relevance Scoring

| Match Type | Score |
|---|---|
| Exact title match | 100 |
| Title contains query | 50 |
| Keyword match | 8 |
| Question match | 7 |
| Tag match | 6 |
| Description contains | 3 |

**Result:** Only items with relevance > 0 are shown

### Examples

**Query:** "first job"
**Returns:** 
- How to Get Your First Job (100+ score)
- Communication Skills Guide (8+ score - has "job" keyword)

**Query:** "I don't know which career suits me"
**Returns:**
- Who Are You? Beyond Grades (matches question)
- Use AI to Discover Careers (matches question)

**Query:** "interview preparation"
**Returns:**
- Prepare for Interviews Using AI (coming-soon)
- How to Get Your First Job (partial match)

---

## Implementation Guide

### Adding Ask Enaasan to a Page

1. **Include JavaScript**
```html
<script src="/js/ask-enaasan.js"></script>
```

2. **Include Component**
```html
<!-- After including ask-enaasan.js -->
<div id="askEnaasanContainer"></div>

<script>
  // Load component
  fetch('/components/ask-enaasan-search.html')
    .then(r => r.text())
    .then(html => {
      document.getElementById('askEnaasanContainer').innerHTML = html;
    });
</script>
```

### Placement Recommendations

✅ **DO place on:**
- Homepage (primary entry point)
- First-Job guide (guide hub)
- Guidance Hub (central resource page)

❌ **DO NOT place on:**
- Every page (creates clutter)
- Individual guide pages (too late in journey)
- Navigation pages (purpose is different)

---

## Publishing Workflow Update

As of 2026-07-17, every publication must follow this complete workflow:

### Step 1: Create Content
- Write the guide (HTML page)
- Follow design system
- Test responsiveness

### Step 2: Create Metadata
- Create JSON file in `/metadata/publications/`
- Use unique ID
- Fill all required fields
- Link to related publications

### Step 3: Update Index
- Add entry to `/metadata/publications/_index.json`
- Verify file path is correct

### Step 4: Update Sitemap
- Add URL to `/sitemap.xml`
- Set appropriate priority (0.8 for guides)
- Set `lastmod` to today's date

### Step 5: Update Navigation
- Add links in related guides (previous/next)
- Update reuse-registry.md
- Add to Guidance Hub if applicable

### Step 6: Update Inventory
- Add to `/CONTENT_INVENTORY.md`
- Update statistics
- Update timeline

### Step 7: Commit & Deploy
- Stage all changes
- Commit with descriptive message
- Push to main branch

**IMPORTANT:** Publication is NOT complete until metadata exists.

---

## Search Index Maintenance

### When to Update Metadata

- **Any content change** → Update metadata + republish metadata files
- **URL change** → Update all metadata files + update in search index
- **Status change** → Update status field + rebuild index
- **New related content** → Update `related_publications` in all affected files

### Versioning

Metadata files don't have version numbers but track:
- `published_date` — When first published
- Commit history in git — What changed and when

### Index Refresh

The search index is loaded fresh on each page load:
1. Browser loads `/js/ask-enaasan.js`
2. Script loads `/metadata/publications/_index.json`
3. Script loads each publication JSON file
4. Search is ready to use

No manual cache clearing needed.

---

## Future Capabilities

Ask Enaasan is designed to support future enhancements:

### Phase 2 (Potential)
- **Smarter search:** Typo tolerance, synonym expansion
- **Question-based recommendations:** "People who searched X also found Y useful"
- **Learning path suggestions:** "Complete this first, then this"
- **AI-enhanced search:** Natural language understanding (optional LLM integration)

### Phase 3 (Potential)
- **Personalized guidance:** Based on degree, interests, career stage
- **Progress tracking:** Which guides student has read
- **Recommendation engine:** Suggests next steps based on history

**Current Phase:** Phase 1 (Lightweight, metadata-driven, client-side)

---

## Editorial Philosophy

### Why Metadata Matters

1. **Student-centric:** Metadata focuses on questions, not technology
2. **Separation of concerns:** Content (HTML) stays separate from indexing (JSON)
3. **Future-proof:** Easy to add new search methods without changing content
4. **Maintainable:** Single source of truth for publication info
5. **Discoverable:** Helps students find answers, not pages

### Principles

> Students do not care about website architecture. They care about answers to their questions.

- **Terminology:** Call it "Ask Enaasan," not "Search"
- **Framing:** "What would you like to know?" not "Search the website"
- **Results:** Show answers to questions, not just links
- **Philosophy:** Mentor guiding student, not search engine indexing pages

---

## Technical Details

### Performance
- **Search speed:** O(n) where n = number of publications (~150ms for 50+ publications)
- **Metadata load:** ~1 per file + index (lazy loaded on first interaction)
- **UI:** Lightweight CSS, no external dependencies

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Requires fetch API (all modern browsers)
- Graceful degradation if JS disabled

### Accessibility
- Semantic HTML
- ARIA labels on interactive elements
- Keyboard navigation (Tab, Enter)
- Color contrast meets WCAG AA

---

## Examples: Adding New Publications

### Example 1: Simple Guide

**File:** `/metadata/publications/guide-007-example.json`

```json
{
  "id": "guide-007-example",
  "title": "My New Guide",
  "url": "/skills/path/to/guide/",
  "description": "Short description",
  "target_audience": "Target audience",
  "duration": "30 minutes",
  "keywords": ["keyword1", "keyword2"],
  "questions_it_answers": [
    "Question 1?",
    "Question 2?"
  ],
  "related_publications": ["guide-001-first-job"],
  "next_publication": "guide-008-next",
  "tags": ["tag1"],
  "status": "published",
  "published_date": "2026-07-18"
}
```

### Example 2: Coming Soon

```json
{
  "id": "guide-006-interviews",
  "title": "Prepare for Interviews Using AI",
  "url": "/skills/first-job/interview-prep/",
  "description": "Master interview prep...",
  "target_audience": "College graduates interviewing",
  "duration": "45 minutes",
  "keywords": ["interview", "first job"],
  "questions_it_answers": [
    "How do I prepare for a job interview?",
    "What questions will I be asked?"
  ],
  "related_publications": ["guide-001-first-job"],
  "tags": ["interview", "career"],
  "status": "coming-soon",
  "published_date": null
}
```

---

## Troubleshooting

### Search returns no results
- Check query matches keywords, questions, title, or tags in metadata
- Verify metadata JSON is valid (use JSONLint)
- Check browser console for loading errors

### Metadata not loading
- Verify `/js/ask-enaasan.js` is loaded
- Check `/metadata/publications/_index.json` exists
- Check individual publication JSON files exist
- Look for 404 errors in Network tab

### Component not showing
- Verify component HTML file path is correct
- Check for JavaScript errors in console
- Ensure ask-enaasan.js loads before component

---

## Maintenance Checklist

- [ ] Metadata created for every new publication
- [ ] `_index.json` updated with new publication
- [ ] Sitemap.xml updated
- [ ] Navigation links updated
- [ ] Reuse registry updated
- [ ] CONTENT_INVENTORY.md updated
- [ ] All tests pass
- [ ] Metadata is valid JSON

---

*Ask Enaasan: Help students find answers, not pages.*
