# Visual Language

## Colour palette

Matches the live site's existing system exactly — this is not a new palette, it's the documented version of what already exists in every page's `:root` CSS block:

| Token | Hex | Use |
|---|---|---|
| Night | `#0D1B2A` | Primary dark background (screen contexts) |
| Ink | `#14273A` | Secondary dark surface (footers, panel backgrounds) |
| Card | `#192F44` | Card/section backgrounds on dark surfaces |
| Border | `#1E3A52` | Hairlines and dividers on dark surfaces |
| Gold | `#F0A500` | Primary accent — CTAs, links, emphasis |
| Glow | `#FFD166` | Hover/active state for gold elements |
| Chalk | `#F2EFE9` | Primary text on dark surfaces |
| Mist | `#A8C0D4` | Secondary/muted text on dark surfaces |
| Faint | `#4A6580` | Tertiary text, captions, footer copy |

## Typography

- **Syne** (600/700/800 weight) — headings, wordmark, anything that needs to feel confident and structural.
- **DM Sans** — body text, UI copy.
- **DM Mono** — eyebrows/labels (small uppercase tags like "CAREER FAQ," "WEEK 1 · DAYS 1–7"), never for body copy.

## Print-friendliness rule (this exists because of a real incident)

**Do not fill an entire first/cover page with a dark solid background on anything meant to be printed.** The screen-first dark navy/gold system above works well for web pages and PDFs read on-screen, but a full-bleed dark cover page uses a large amount of ink or toner when a student or parent prints it at home or at a shop — and enaasan's audience includes people for whom that cost is not trivial.

For printable documents (Workbooks, Checklists, anything explicitly meant to be printed and filled in by hand):

- Cover/first pages use a **light or white background** as the base.
- Dark navy and gold appear as **accents only** — a header band, a rule line, the logo lockup, a coloured heading — not as a full-page fill.
- Interior/worksheet pages stay white-background with dark text throughout (as the existing 90-Day Plan's interior pages already do) — this rule is specifically about full-bleed dark *cover* pages, which is where the ink cost is concentrated in a single sheet.
- Screen-only documents (a landing page, an on-site FAQ) are not bound by this rule — the dark theme is the site's normal, correct visual identity there. This rule applies specifically to the printed-cover-page case.

## Illustration style

Not yet established with real assets (see `assets/illustrations/README.md`) — reserved for future work. When defined, illustrations should be simple, warm, and avoid stock-photo-style generic imagery; consistent with the "personal guide, not corporate institution" brand value.

## Photography style

Not currently used anywhere on the site. If introduced, photography should feature real Indian contexts (not generic stock imagery of ambiguous origin) and avoid the "polished corporate stock photo" look that would contradict the brand's honest, unglossy voice.

## Document design principles

1. **Screen-first pages can be rich; printable pages must be economical.** See the print-friendliness rule above — it's the single most important visual rule in this file.
2. **One accent colour, used sparingly.** Gold is the signal for "this matters" (a CTA, an important note); overusing it dilutes that signal.
3. **Whitespace is a feature, not a gap to fill.** Dense, cramped pages contradict the calm tone described in `tone-of-voice.md`.
4. **Consistent iconography over decorative flourish.** A checkbox is a checkbox everywhere; a callout note uses the same visual treatment everywhere (see the "💡" verify-note pattern already used on `state-exams.html` and the "Honest note" boxes in the 90-Day Plan).
