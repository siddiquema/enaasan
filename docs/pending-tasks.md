# Pending Tasks — Snapshot as of 2026-07-12

**60 open issues** on [siddiquema/enaasan](https://github.com/siddiquema/enaasan/issues) plus a handful of non-issue pending items. Grouped by what each is waiting on. Point-in-time snapshot — regenerate rather than hand-edit.

---

## 1. Waiting on you (small, unblocks other work)

| Item | What's needed |
|---|---|
| **Workbook editorial review** | ENA-GRAD-001 (The First 90 Days workbook, 59-page PDF in `knowledge/output/pdf/`) is `In Review` — read and sign off to flip it to Published |
| #60 GEO-05 | One click: Bing Webmaster Tools → Sitemaps → submit `https://enaasan.online/sitemap.xml` (format already verified) |
| **Author details decision** | Four placement options proposed (About-page founder card + per-guide byline recommended); need your go + LinkedIn URL + photo yes/no. Unblocks #71 WS-05 |
| #9 C-05 Security headers | Pick a direction: Cloudflare free tier in front (recommended) / move hosting / accept limitation |
| #53 + #46 Theme/palette | Palette decision; prototype exists in local `theme-preview.html` |

## 2. Execute-now (no decisions needed, ready to build)

| Issue | Task |
|---|---|
| [#85](https://github.com/siddiquema/enaasan/issues/85) WS-21 | Cross-site design system components + article metadata scheme — foundation for most WS work |
| [#74](https://github.com/siddiquema/enaasan/issues/74) WS-08 | GA4 event tracking (`share_click`, `cta_click`, scroll depth…) + UTM convention doc |
| [#73](https://github.com/siddiquema/enaasan/issues/73) WS-07 | Guidance disclaimer, cookie consent for GA4, privacy-policy review |
| [#72](https://github.com/siddiquema/enaasan/issues/72) WS-06 | Sources + verification notices on high-stakes pages |
| [#71](https://github.com/siddiquema/enaasan/issues/71) WS-05 | Author box + last-reviewed dates + report-an-issue links *(content ready; waits on author decision above)* |
| [#70](https://github.com/siddiquema/enaasan/issues/70) WS-04 | Share bar (WhatsApp/Copy Link/LinkedIn) site-wide + shareable QR card |
| [#69](https://github.com/siddiquema/enaasan/issues/69) WS-03 | Article-level primary CTAs with click tracking (spec copy provided) |
| [#59](https://github.com/siddiquema/enaasan/issues/59) GEO-04 | FAQPage schema on bps/after12/streams — mechanical, but waits on #61 capsule text |
| [#55](https://github.com/siddiquema/enaasan/issues/55) | Research + verify 8 placeholder exam links on state-exams.html (needs web research, no decisions) |

## 3. Decision queue (planning-session material)

- [#67](https://github.com/siddiquema/enaasan/issues/67) **WS-01 Subscriber capture** — static site needs a form/email provider; same decision unblocks [#87](https://github.com/siddiquema/enaasan/issues/87) WS-16 (question form)
- [#61](https://github.com/siddiquema/enaasan/issues/61) **GEO-06 Answer capsules** — copy session; unblocks #59 and #62; pairs with [#80](https://github.com/siddiquema/enaasan/issues/80) WS-15 quick-answer blocks
- [#66](https://github.com/siddiquema/enaasan/issues/66) **Career decision traps** — trap list + copy session; direction settled (standalone articles + homepage teaser, syndication-ready)
- [#75](https://github.com/siddiquema/enaasan/issues/75) **WS-09 Start Here pathway** — consolidates #18 (guided quiz) + #20 (where-to-start)
- [#76](https://github.com/siddiquema/enaasan/issues/76) **WS-10 Topic hubs** — URL-structure decision (`/after10` routes vs upgrading existing `.html` pages) — decide before content multiplies
- [#81](https://github.com/siddiquema/enaasan/issues/81) **WS-17 Telugu long-form** — per-article `/te/` pages vs extending data-i18n
- [#62](https://github.com/siddiquema/enaasan/issues/62) GEO-07 question-form headings · [#63](https://github.com/siddiquema/enaasan/issues/63) GEO-08 backlink outreach targets · [#64](https://github.com/siddiquema/enaasan/issues/64) GEO-09 AI-citation tracking log format

### Older design/copy decision cluster (from the first feedback round)

[#16](https://github.com/siddiquema/enaasan/issues/16) tagline · [#17](https://github.com/siddiquema/enaasan/issues/17) top nav · [#18](https://github.com/siddiquema/enaasan/issues/18) guided quiz · [#19](https://github.com/siddiquema/enaasan/issues/19) brand misread · [#20](https://github.com/siddiquema/enaasan/issues/20) where-to-start · [#22](https://github.com/siddiquema/enaasan/issues/22) aspirational copy · [#23](https://github.com/siddiquema/enaasan/issues/23) hero image · [#25](https://github.com/siddiquema/enaasan/issues/25) background visuals · [#27](https://github.com/siddiquema/enaasan/issues/27) visual roadmaps — several are effectively folded into WS-09/WS-10; worth a cleanup pass to close duplicates when those build.

## 4. Content builds (unblocked, session-sized each)

- **Knowledge Series pipeline now exists** — natural next publications: Career Profiles for the 5 BPS/KPO roles (`knowledge/publications/careers/`), the After-12th checklist (spec's alternate resource), comparison pages
- [#77](https://github.com/siddiquema/enaasan/issues/77) WS-12 — 8 comparison pages (B.Com vs BBA, PCM vs PCB, CA vs CS vs CMA…)
- [#78](https://github.com/siddiquema/enaasan/issues/78) WS-13 — glossary (15 terms; workbook's 24-term glossary is seed material)
- [#86](https://github.com/siddiquema/enaasan/issues/86) WS-11 — related-content blocks (needs WS-21 metadata scheme first)
- [#50](https://github.com/siddiquema/enaasan/issues/50) PS-01 course eligibility · [#45](https://github.com/siddiquema/enaasan/issues/45) KM-05 career data · [#44](https://github.com/siddiquema/enaasan/issues/44) KM-04 parent section (→ WS-10 `/parents` hub) · [#43](https://github.com/siddiquema/enaasan/issues/43) KM-03 + [#39](https://github.com/siddiquema/enaasan/issues/39) + [#82](https://github.com/siddiquema/enaasan/issues/82) WS-18 student stories (consolidate when built) · [#41](https://github.com/siddiquema/enaasan/issues/41) KM-01 quiz (→ WS-09/WS-19)
- [#79](https://github.com/siddiquema/enaasan/issues/79) WS-14 — systematic mobile UX pass (best after Phase-1 components land)

## 5. Stage-2 career coverage (deferred until after young-user feedback)

[#29](https://github.com/siddiquema/enaasan/issues/29) sports · [#30](https://github.com/siddiquema/enaasan/issues/30) teacher training · [#33](https://github.com/siddiquema/enaasan/issues/33) polytechnic/ITI · [#34](https://github.com/siddiquema/enaasan/issues/34) supply chain · [#35](https://github.com/siddiquema/enaasan/issues/35) online education · [#36](https://github.com/siddiquema/enaasan/issues/36) gig/creator · [#37](https://github.com/siddiquema/enaasan/issues/37) manufacturing/semis · [#38](https://github.com/siddiquema/enaasan/issues/38) climate/space · [#32](https://github.com/siddiquema/enaasan/issues/32) font-size widget

## 6. Deferred / future phases

- [#12](https://github.com/siddiquema/enaasan/issues/12) homepage conversion path + [#52](https://github.com/siddiquema/enaasan/issues/52) gamified registration — wait on login layer
- [#83](https://github.com/siddiquema/enaasan/issues/83) WS-19 recommendation quiz + [#84](https://github.com/siddiquema/enaasan/issues/84) WS-20 AI mentor — WS Phase 4, build-later by design
- [#54](https://github.com/siddiquema/enaasan/issues/54) govt jobs & banking exams section · [#31](https://github.com/siddiquema/enaasan/issues/31) location-based recommendations (needs backend)

## 7. Pinned

- [#1](https://github.com/siddiquema/enaasan/issues/1) **Architecture rule** — never put `data-i18n` on an element with child HTML; grep before editing.

---

## Non-issue pending items (local housekeeping)

- **Uncommitted:** `docs/project-structure.md` (new) and `docs/README.md` (index update) — written, never committed
- **TIME_LOG.md** — session row from 2026-07-12 00:15 still open; close out at end of session
- **Untracked local files** — `theme-preview.html` (the #53 prototype), `favicon-screenshot.png`, `setup-enaasan-issues.ps1` — keep, commit, or delete: your call
- **v1.1 PDF rebrand request** — you asked to rebrand `enaasan-90-day-career-clarity-plan-v1.1.pdf` (Downloads) with a print-friendly cover, then interrupted the task. The new workbook honours that rule, but the *compact site PDF*'s dark cover is still live at `assets/enaasan-90-day-career-clarity-plan.pdf` — decide whether to regenerate it with the light cover

## Milestone progress

| Milestone | Open | Closed |
|---|---|---|
| WS Phase 1 — Pre-promotion | 8 | 1 (WS-02 ✔) |
| WS Phase 2 — Navigation and content | 5 | 0 |
| WS Phase 3 — Readiness and participation | 5 | 0 |
| WS Phase 4 — Advanced features | 2 | 0 |
