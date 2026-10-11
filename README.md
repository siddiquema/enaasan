# enaasan.online

Career guidance platform for Indian students.

## Folder Structure

| Folder | Purpose |
|---|---|
| assets/ | Logo, favicon, og-image, hero images |
| css/ | style.css, lang-styles.css, mobile.css |
| js/ | i18n.js, nav.js, analytics.js |
| locales/ | en.json, ta.json, te.json, hi.json |
| data/ | careers.json, exams.json, streams.json (Stage 2) |
| docs/ | bug-tracker, roadmap, decisions log |

## Translation checks

Pages are translated by `js/i18n.js`, which swaps the text of every element with
`data-i18n="key"` using `locales/<lang>.json` (en, ta, te, hi). The `i18n/` folder
and root `i18n.js` are legacy copies that no page loads — edit `locales/` only.

When you add or change English text that has a `data-i18n` key:

1. Update the English in the page **and** in `locales/en.json`.
2. Add or update the same key in `locales/ta.json`, `te.json` and `hi.json`.
   If no translation is ready, copy the English as a placeholder — it shows up in
   the audit as "same as English" for the reviewer.
3. Run the check before committing:

```bash
python3 scripts/i18n-check.py check --base origin/main   # what CI runs
python3 scripts/i18n-check.py audit                      # refresh translation-audit.md
```

The **Translation check** GitHub Action runs on every pull request and push to
`main` that touches pages or locale files:

- **Fails** if a page uses a key that is missing from `en.json`, or a key in
  `en.json` is missing from ta/te/hi.
- **Warns** if English text changed without Tamil/Telugu/Hindi being updated, or
  a page's English no longer matches `en.json`. Add `--strict` to fail on warnings.

Older known issues are listed in `scripts/i18n-baseline.json` so they don't block
every PR. When you fix some, run `python3 scripts/i18n-check.py baseline` to shrink it.

Reviewers: Telugu — Vijaya · Hindi — Shafi · Tamil — TBD. Never overwrite a
reviewed translation with a machine translation.

## Deployment
- Live: https://enaasan.online
- Host: GitHub Pages
- Repo: siddiquema/enaasan

## Stage Plan
- Stage 1: Free public layer (current)
- Stage 2: Login layer (auth/)
- Stage 3: Paid AI/coaching layer (api/)
