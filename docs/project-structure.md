# enaasan.online — Project Structure & GitHub Architecture

Snapshot of the repo layout and GitHub setup as of 2026-07-12. This is a point-in-time reference — re-generate rather than hand-edit when the structure changes significantly.

---

## 1. Local folder structure

```
enaasan_fresh/
├── index.html                  Homepage
├── about.html                  About / transparency / contact
├── streams.html                Stream Explorer (after 10th)
├── after10.html                Earning after 10th (vocational/diploma/ITI)
├── after12.html                After 12th (entrance exams, degrees)
├── careers.html                Career Compass
├── bps.html                    BPS / KPO careers (differentiated content)
├── guide.html                  Guidance Hub (incl. parent myths section)
├── state-exams.html            State-wise entrance exams (5 states × 6 stages)
├── faq.html                    Career FAQ — 32 Q&As, 7 categories, FAQPage schema
├── 90-day-plan.html            Landing page for the 90-Day Career Clarity Plan PDF
├── privacy.html                Privacy Policy
├── terms.html                  Terms & Disclaimer
├── theme-preview.html          [untracked] local prototype for issue #53 (theme switcher)
│
├── assets/
│   ├── enaasan-90-day-career-clarity-plan.pdf   Downloadable resource (WS-02 / #68)
│   └── og-image.jpg            Open Graph share image
│
├── css/
│   └── lang-styles.css         Language-pill styling (shared across pages)
│
├── js/
│   └── i18n.js                 i18n engine — detect → localStorage → fetch locale JSON → swap data-i18n text
│
├── locales/
│   ├── en.json                 694 keys — English (source of truth)
│   ├── ta.json                 694 keys — Tamil
│   ├── te.json                 694 keys — Telugu
│   └── hi.json                 694 keys — Hindi
│
├── docs/
│   ├── README.md                    Index of the docs folder
│   ├── project-structure.md         This file
│   ├── website-update-spec.md       Source spec for issues WS-01..WS-21 (growth label)
│   ├── claude-code-handover.md       Handover notes for Claude Code sessions
│   ├── bug-tracker.md                Open issues and fix log (informal, predates GitHub Issues use)
│   └── decisions.md                  Architecture/design decisions log
│
├── .github/
│   └── workflows/
│       └── indexnow.yml        Pings IndexNow (Bing) with changed pages on every push to main
│
├── .claude/
│   └── launch.json             Dev server config for the Browser preview tool (python -m http.server 3333)
│
├── sitemap.xml                 13 URLs, standard sitemaps.org 0.9 format
├── robots.txt                  Explicit allow for GPTBot, OAI-SearchBot, Bingbot, Google-Extended, PerplexityBot, ClaudeBot
├── CNAME                       enaasan.online (custom domain for GitHub Pages)
├── BingSiteAuth.xml            Bing Webmaster Tools domain verification
├── 89dcc8ed321f4c9e961c398bd5bf5e72.txt   IndexNow key file (must live at domain root)
├── .gitattributes              Forces binary handling for PDFs/images/fonts (prevents CRLF corruption)
├── .gitignore                  OS junk, logs, node_modules
├── TIME_LOG.md                 Per-session time tracking (Claude Code sessions only, from 2026-07-05)
└── README.md                   Top-level project summary (folder table is stage-plan-oriented, slightly stale — see note below)
```

### Legacy / orphaned files (tracked in git, not referenced by any page)

These exist at the repo root as duplicates of the real, in-use files and are **not linked from any HTML page** — dead weight left over from an early setup pass on 2026-07-05, never cleaned up:

| File | Live equivalent actually used |
|---|---|
| `i18n.js` | `js/i18n.js` |
| `lang-styles.css` | `css/lang-styles.css` |
| `i18n/en.json`, `i18n/hi.json`, `i18n/ta.json`, `i18n/te.json` | `locales/*.json` |
| `enaasan-fixes.patch` | — (stray patch file, no longer applicable) |

Not deleted as part of writing this doc — flagging for a future cleanup pass rather than acting unilaterally on files that might be intentionally kept.

### Untracked local-only files (not in git)

| File | Why it's local-only |
|---|---|
| `.claude/` | Claude Code session config (launch.json, settings.local.json) |
| `favicon-screenshot.png` | Working screenshot from favicon iteration, never committed |
| `setup-enaasan-issues.ps1` | One-off script used to bulk-create the original 40 GitHub issues |
| `theme-preview.html` | Prototype for issue #53 (theme switcher), not shipped |

---

## 2. i18n architecture

- **Convention:** every translatable element carries `data-i18n="key.name"`. `js/i18n.js` fetches the matching `locales/<lang>.json` and sets `el.textContent = messages[key]`.
- **Pinned architecture rule (GitHub issue #1):** never put `data-i18n` on an element with child HTML — the engine uses `textContent`, which wipes nested tags. Always grep for existing usage before editing a page's i18n keys.
- **Languages:** English (default/source of truth), Tamil, Telugu, Hindi — all four locale files are kept at identical key counts (694 as of the FAQ page addition).
- **Detection order:** `localStorage` preference → `navigator.language` → fallback to English.
- **Long-form article content** (per `docs/website-update-spec.md` §17) is planned to use separate `/te/` page routes instead of the data-i18n key system — a decision still open (issue WS-17 / #81).

---

## 3. GitHub repository architecture

**Repo:** [siddiquema/enaasan](https://github.com/siddiquema/enaasan) · **Branch:** `main` only, no protection rules · **Pages source:** `main` branch, `/` root path, custom domain `enaasan.online`, HTTPS enforced.

### Labels (23)

| Category | Labels |
|---|---|
| GitHub defaults | `bug`, `documentation`, `duplicate`, `enhancement`, `good first issue`, `help wanted`, `invalid`, `question`, `wontfix` |
| Workflow status | `execute-now` (ready, no decisions needed), `needs-decision` (blocked on a choice), `stage-2` (deferred post-feedback) |
| Topic | `design`, `ux`, `copy`, `content`, `i18n`, `performance`, `security`, `strategic`, `feedback` |
| Initiative-specific | `geo` (GEO/AEO — Bing index, IndexNow, schema, answer capsules), `growth` (student-acquisition spec, WS-01..WS-21) |

### Milestones (9)

| Milestone | Status |
|---|---|
| Sprint 1 - Core fixes | empty (0/0) |
| Saturday decision session | empty (0/0) |
| Sprint 2 - Post-decision execution | empty (0/0) |
| Stage 2 - After young-user feedback | empty (0/0) |
| Launch | empty (0/0) |
| WS Phase 1 - Pre-promotion | 8 open, 1 closed |
| WS Phase 2 - Navigation and content | 5 open |
| WS Phase 3 - Readiness and participation | 5 open |
| WS Phase 4 - Advanced features | 2 open |

The first five milestones are early/unused scaffolding from initial repo setup. The four `WS Phase` milestones are the active ones, mapping directly to the four phases in `docs/website-update-spec.md`.

### Issues

**60 open, 27 closed** (as of 2026-07-12). Numbering is not sequential by topic — issues were filed in several batches over time:

| Range | Batch |
|---|---|
| #1–#41 | Original site-feedback backlog (architecture rule, homepage/design decisions, KM/PS reviewer feedback, stage-2 content gaps) |
| #43–#55 | Continued feedback batch + state-exams link verification |
| #56–#66 | GEO/AEO backlog (`geo` label) — Bing indexing, IndexNow, FAQPage schema, answer capsules, career-decision-traps section |
| #67–#87 | Website update spec (`growth` label) — WS-01 through WS-21, mapped to the four WS Phase milestones |

### GitHub Actions

**`.github/workflows/indexnow.yml`** — on every push to `main`, diffs the commit range for changed `.html` files and POSTs them to the IndexNow API (`api.indexnow.org`) using the key file at the domain root. Also runnable manually via `workflow_dispatch` with an explicit space-separated URL list. Purpose: get changed pages into Bing's index quickly, since AI answer engines (ChatGPT, Copilot) lean on Bing's index more than Google's.

---

## 4. External services referenced in the codebase

| Service | Where it's wired in |
|---|---|
| Google Analytics 4 (`G-D4QMDFL8XF`) | `gtag.js` snippet in every page `<head>` |
| Google Search Console | via sitemap.xml submission (external, not in-repo) |
| Bing Webmaster Tools | `BingSiteAuth.xml` (verification) + IndexNow key file + GitHub Action |
| Google Fonts | Syne, DM Sans, DM Mono — preconnected in every page |
| WhatsApp / LinkedIn share links | inline `wa.me` and share-intent URLs on faq.html, 90-day-plan.html, and others |

No backend, no database, no build step — the whole site is static HTML/CSS/vanilla JS served directly by GitHub Pages. Several open issues (WS-01 subscriber capture, WS-16 question submission form) are blocked specifically because they need a third-party form/email service that doesn't exist yet, since there's no server to hold that logic.

---

## 5. Known documentation drift

- **Root `README.md`** describes a folder table (`css/style.css`, `js/nav.js`, `js/analytics.js`, `data/*.json`) that does not match what actually exists today — those specific files were never created; only `css/lang-styles.css` and `js/i18n.js` exist. The Stage 1/2/3 plan in that file (`auth/`, `api/` folders) is aspirational/future, not yet built.
- **`docs/bug-tracker.md`** predates the move to tracking everything as GitHub Issues — check GitHub Issues first for current bug status, not this file.
