# enaasan.online — Claude Code Handover
*Prepared: 28 June 2026 — pick up from here in Claude Code*

---

## Why Claude Code

Claude Code works directly inside `J:\Project\enaasan\enaasan\` — reads, edits, saves files without zip uploads. You reload Live Server instantly after each change. Use this for all remaining front-end fixes.

---

## Project Overview

| Item | Detail |
|---|---|
| Live site | https://enaasan.online |
| GitHub repo | siddiquema/enaasan |
| Local repo | `J:\Project\enaasan\enaasan\` |
| Deployed via | GitHub Pages (main branch) |
| Local testing | VS Code + Live Server → http://127.0.0.1:5500 |
| Design system | Dark navy `--night: #0D1B2A` / Gold `--gold: #F0A500` |
| Translation keys | 599 per language (en, ta, te, hi) in `locales/` folder |
| i18n engine | `js/i18n.js` — uses `el.textContent` to swap text |

---

## Step 1 — Git Push First (do this before anything else)

All local fixes from the 28 June session are ready. Push to make the live site current:

```bash
cd J:\Project\enaasan\enaasan
git add .
git status
git commit -m "Fix i18n container bugs, card clickability, progress bar, nav overlap, arrow wrapping (B-01 to B-17)"
git push origin main
```

Wait 2–3 minutes → verify https://enaasan.online loads correctly with dark navy background.

---

## Step 2 — Fix B-14: after12.html exam cards not translated

**File:** `after12.html`

**Problem:** All exam content is in a JS `const EXAMS = { ... }` data object inside a `<script>` tag. Fields like `tagline`, `body`, `difficulty`, `seats`, `leads` are hardcoded English strings. The i18n engine only translates DOM elements with `data-i18n` — it never reaches JS variables.

**How to fix (Option A — add a translations map inside the script):**

1. Find `const EXAMS = {` in after12.html
2. Add a `const EXAM_TRANSLATIONS = { ta: {...}, te: {...}, hi: {...} }` object with translated versions of each exam's `tagline`, `body`, `difficulty`, `seats` fields
3. Add a helper function:
```javascript
function getLang() {
  return localStorage.getItem('enaasan_lang') || 'en';
}
```
4. In the card-building function (wherever `EXAMS[key]` fields are rendered into HTML), replace hardcoded field references with:
```javascript
const lang = getLang();
const t = (EXAM_TRANSLATIONS[lang] && EXAM_TRANSLATIONS[lang][key]) || EXAMS[key];
// then use t.tagline, t.body etc instead of exam.tagline, exam.body
```
5. Also listen for the `langchange` event to re-render open cards:
```javascript
document.addEventListener('langchange', function(e) {
  // re-render currently displayed exam detail if any is open
});
```

**Fields to translate per exam:** `tagline`, `body`, `difficulty` label (HIGH/VERY HIGH/MODERATE), `seats` text, items in `leads` array.

**Exam keys in EXAMS object:** jee_main, jee_advanced, eamcet, bitsat, neet, cuet, clat, nid, nift, ca_foundation, nda, kvs — check the file for the full list.

---

## Step 3 — Fix B-15: streams.html Step 3 path not translated

**File:** `streams.html`

**Problem:** Same as B-14. All stream path content is in `const STREAMS = { pcm: {...}, pcb: {...}, commerce: {...}, arts: {...}, vocational: {...} }`. The `nodes` array inside each stream contains `stage`, `title`, `desc`, `options`, `exams`, and `careers` — all English, all unreachable by i18n.

**How to fix (same Option A pattern):**

1. Add `const STREAMS_TA = { pcm: { heading: '...', sub: '...', nodes: [...] }, ... }` and equivalent for te, hi
2. Add helper to select correct translation:
```javascript
function getStreamData(key) {
  const lang = getLang();
  const maps = { ta: STREAMS_TA, te: STREAMS_TE, hi: STREAMS_HI };
  return (maps[lang] && maps[lang][key]) ? { ...STREAMS[key], ...maps[lang][key] } : STREAMS[key];
}
```
3. Replace `const s = STREAMS[key]` with `const s = getStreamData(key)` in `buildStreamsGrid()` and `buildPath()`
4. Listen for `langchange` to re-render if user is on Step 2 or Step 3

**Priority order for translation:** Start with `heading`, `sub`, `description` (most visible). Then `nodes[].title` and `nodes[].desc`. Options and career chips can follow.

**Note:** The Tamil, Telugu, Hindi translations for these fields need to be written. Coordinate with reviewers:
- Tamil: Family member (senior Tamil language teacher)
- Telugu: Vijaya (ex-colleague)  
- Hindi: Shafi (cousin, Delhi) — v2 review still pending

---

## Architecture Rule — Never Violate

> `data-i18n` must ONLY be placed on leaf-node text elements with no child HTML.
> `el.textContent` in i18n.js destroys all child nodes on language switch.
>
> ✅ `<span data-i18n="key">text only</span>`
> ❌ `<h1 data-i18n="key">text <span>child</span></h1>`

---

## What Was Already Fixed — Do Not Redo

| Bug | What was done |
|---|---|
| B-01 | streams.html progress bar padding fixed |
| B-02/03 | streams.html card click → auto-advance |
| B-07–13 | All data-i18n container violations fixed across index, about, bps, streams |
| B-16 | Progress bar labels now translated (599 keys in all locale files) |
| B-17 | after12.html nav overlap fixed |
| index.html | white-space: nowrap on .path-link |
| locales | home.hero.title trimmed to first line in all 4 JSONs |

---

## Folder Structure

```
enaasan/
├── index.html          ← homepage
├── streams.html        ← 3-step stream explorer (B-15 work here)
├── after12.html        ← exam + college guide (B-14 work here)
├── careers.html
├── bps.html
├── guide.html
├── about.html
├── css/lang-styles.css ← language switcher styles
├── js/i18n.js          ← translation engine (do not modify without care)
├── locales/
│   ├── en.json         ← 599 keys
│   ├── ta.json         ← 599 keys
│   ├── te.json         ← 599 keys
│   └── hi.json         ← 599 keys
└── docs/
    ├── bug-tracker.md
    └── claude-code-handover.md  ← this file
```

---

## Git Workflow

```bash
cd J:\Project\enaasan\enaasan
git add .
git status
git commit -m "describe what you fixed"
git push origin main
# Live site updates in 2-3 mins at https://enaasan.online
```

