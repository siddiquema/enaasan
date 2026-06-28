# enaasan.online — Bug Tracker
*Last updated: 28 June 2026 — Session 2*

---

## ✅ Fixed — Session 28 June 2026

| # | Issue | File(s) | Fix Applied |
|---|---|---|---|
| B-01 | Progress bar clipped behind fixed nav | streams.html | Increased `.page` top padding 100px → 120px desktop, 140px → 150px mobile |
| B-02 | Step 1 interest tiles not clickable on mobile | streams.html | Added `goToStep2()` to all 4 tile `onclick` handlers |
| B-03 | Step 2 stream cards not clickable on mobile | streams.html | Changed `card.onclick` to call `selectStream()` then `goToStep3()` immediately |
| B-07 | Gold "what comes next?" accent destroyed on language switch | index.html + locales | Moved `data-i18n` off `<h1>` container onto inner `<span>`; accent span kept static; locale JSONs updated |
| B-08 | Hero eyebrow tagline span destroyed on language switch | index.html | Removed duplicate `data-i18n` from `<div>` container |
| B-09 | 4 card CTA arrows destroyed on language switch | index.html | Moved `data-i18n` off `<a>` containers onto inner text `<span>` |
| B-10 | Map button emoji destroyed on language switch | streams.html | Moved `data-i18n` off `<button>` onto inner text `<span>` |
| B-11 | 3 container elements destroyed on language switch | about.html | `data-i18n` moved to safe leaf nodes |
| B-12 | 2 container elements destroyed on language switch | bps.html | `data-i18n` removed from container div; strong simplified |
| B-13 | Card CTA arrow wrapping to new line on narrow cards | index.html | Added `white-space: nowrap` to `.path-link` |
| B-16 | Progress bar labels always in English | streams.html + locales | Added `data-i18n` to 3 label spans; added 3 translation keys to all 4 locale files (now 599 keys each) |
| B-17 | after12.html hero eyebrow clipped under fixed nav | after12.html | Increased `.page` top padding 100px → 120px desktop, 88px → 110px mobile |

---

## 🔴 Open — Requires Claude Code

| # | Issue | File | Type | Priority | Notes |
|---|---|---|---|---|---|
| B-14 | after12.html exam card content not translated | after12.html | Architecture — JS `EXAMS{}` object | P2 | All exam taglines, descriptions, seat counts, difficulty labels hardcoded in JS. Needs JS-level translation layer. See handover doc. |
| B-15 | streams.html Step 3 path content not translated | streams.html | Architecture — JS `STREAMS{}` object | P2 | Node titles, descriptions, options, career paths all in `STREAMS{}` JS object. Same fix pattern as B-14. See handover doc. |

---

## 🟡 Deferred — Stage 2

| # | Issue | Type |
|---|---|---|
| #26 | Stream descriptions rewrite | Content |
| #33 | BPS/KPO card addition on homepage | Content |
| Various | 25 open UX issues from 6-reviewer feedback round | UX/Content |
| SEO | Meta titles and descriptions — all 7 pages | SEO |
| Launch | LinkedIn launch post | Marketing |

---

## Architecture Rule (permanent)
> `data-i18n` must ONLY be placed on **leaf-node text elements** with no child HTML.
> `el.textContent` destroys all child nodes (`<span>`, `<br>`, `<strong>`, `<em>`) on language switch.
> Before adding any `data-i18n` — verify the element has zero child HTML tags.

