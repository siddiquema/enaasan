# Translation Audit — enaasan.online

*Generated 2026-10-11 from commit `72f2c37` by `scripts/i18n-check.py audit`. Re-run the script to refresh; do not hand-edit the tables.*

> **Audit only.** No translation file was changed. Human-reviewed translations are untouched. Reviewers: Telugu — Vijaya, Hindi — Shafi, Tamil — TBD.

## 1. How translation works on this site

- **Engine:** `js/i18n.js` (loaded by 12 pages). On load it detects the language (saved choice → browser language → English). For Tamil, Telugu or Hindi it fetches `locales/<lang>.json` and replaces the `textContent` of every element with `data-i18n="key"`, plus `<title>` and `<meta name="description">`.
- **English source of truth:** the English written in each HTML page. `locales/en.json` is only applied when a visitor switches *back* to English, so it can silently drift from the page.
- **Live files:** `locales/en.json`, `ta.json`, `te.json`, `hi.json` (694 keys each).
- **Legacy files — not loaded by any page:** `i18n/*.json` (596 keys) and the root `i18n.js`. Some English fixes and Shafi's Hindi review were saved here (see §6). Decision 2026-10-11: leave both folders as they are; report only.
- **Rule (issue #1):** `data-i18n` only on leaf elements — `textContent` destroys child HTML.

**Stale-key signals** (git history of `locales/` has only 2 commits, so dates alone cannot show staleness; three signals are combined):

| Signal | Meaning |
|---|---|
| `page-text` | The English on the page no longer matches `locales/en.json` — English was edited in the HTML after the translation was made |
| `legacy-en` | `i18n/en.json` has a newer English value than `locales/en.json` |
| `git-date` | `git blame`: the English line in `locales/en.json` was changed after the translated line |

## 2. Summary — page × language

Counts are keys used on that page. **Missing** = no value in the live language file (or not even in `en.json`). **Stale** = translation exists but English has changed. **Same as EN** = value identical to English. **OK** = keys with none of these. **Hardcoded** = visible English text not routed through i18n (text nodes + translatable attributes + English strings in page scripts; approximate).

| Page | Keys | Tamil miss / stale / same / OK | Telugu miss / stale / same / OK | Hindi miss / stale / same / OK | Hardcoded |
|---|---:|---|---|---|---:|
| `90-day-plan.html` | 0 | — | — | — | 39 |
| `about.html` | 86 | 0 / 3 / 0 / 83 | 0 / 3 / 0 / 83 | 0 / 3 / 0 / 83 | 16 |
| `after10.html` | 14 | 0 / 0 / 0 / 14 | 0 / 0 / 0 / 14 | 0 / 0 / 0 / 14 | 220 |
| `after12.html` | 119 | 0 / 0 / 2 / 117 | 0 / 0 / 1 / 118 | 0 / 0 / 7 / 112 | 206 |
| `bps.html` | 131 | 0 / 24 / 8 / 99 | 0 / 24 / 0 / 107 | 0 / 24 / 13 / 94 | 228 |
| `career-exploration/01-who-are-you.html` | 0 | — | — | — | 123 |
| `careers.html` | 111 | 0 / 1 / 1 / 109 | 0 / 1 / 1 / 109 | 0 / 1 / 7 / 103 | 625 |
| `components/ask-enaasan-search.html` | 0 | — | — | — | 12 |
| `components/cookie-consent.html` | 0 | — | — | — | 5 |
| `components/guidance-disclaimer.html` | 0 | — | — | — | 6 |
| `faq.html` | 107 | 0 / 0 / 0 / 107 | 0 / 0 / 0 / 107 | 0 / 0 / 0 / 107 | 11 |
| `gig-work/index.html` | 0 | — | — | — | 215 |
| `guide.html` | 121 | 0 / 1 / 0 / 120 | 0 / 1 / 3 / 117 | 0 / 1 / 3 / 117 | 14 |
| `index.html` | 64 | 3 / 11 / 0 / 50 | 3 / 11 / 0 / 50 | 3 / 11 / 2 / 48 | 21 |
| `privacy.html` | 0 | — | — | — | 50 |
| `skills/communication/definition/index.html` | 0 | — | — | — | 54 |
| `skills/communication/examples/index.html` | 0 | — | — | — | 73 |
| `skills/communication/framework/index.html` | 0 | — | — | — | 78 |
| `skills/communication/index.html` | 0 | — | — | — | 47 |
| `skills/communication/readiness/index.html` | 0 | — | — | — | 58 |
| `skills/communication/salary-premium/index.html` | 0 | — | — | — | 76 |
| `skills/first-job/build-skills/index.html` | 0 | — | — | — | 156 |
| `skills/first-job/explore-careers/index.html` | 0 | — | — | — | 77 |
| `skills/first-job/index.html` | 59 | 44 / 0 / 0 / 15 | 44 / 0 / 0 / 15 | 44 / 0 / 0 / 15 | 15 |
| `state-exams.html` | 0 | — | — | — | 94 |
| `streams.html` | 39 | 0 / 1 / 0 / 38 | 0 / 1 / 0 / 38 | 0 / 1 / 0 / 38 | 149 |
| `terms.html` | 0 | — | — | — | 57 |
| `theme-preview.html` | 0 | — | — | — | 45 |
| **Total** | **851** | **47 / 41 / 11 / 752** | **47 / 41 / 5 / 758** | **47 / 41 / 32 / 731** | **2770** |

*Keys shared by several pages are counted on each page that uses them.*

## 3. Per language

### 3.1 Tamil (`ta`) — reviewer: TBD

- Missing: **47** · Stale: **41** · Same as English: **18** (of which 8 look like real untranslated text)

**Missing keys (47)**

| Key | Page(s) | In en.json? |
|---|---|---|
| `firstjob.closing.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.note` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.hero.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.hero.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.meta.description` | skills/first-job/index.html | **no** — add English first |
| `firstjob.nextsteps.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.page.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.note` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause1.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause2.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.question` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.cand1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.cand2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.label` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.setup` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.why` | skills/first-job/index.html | **no** — add English first |
| `firstjob.section.badge` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.title` | skills/first-job/index.html | **no** — add English first |
| `home.starthere.body` | index.html | **no** — add English first |
| `home.starthere.cta` | index.html | **no** — add English first |
| `home.starthere.title` | index.html | **no** — add English first |

**Stale keys (41)**

| Key | Signal | English now | Current translation |
|---|---|---|---|
| `about.hero.body` | page-text | Every year, millions of Indian students make one of the most conseque… | இந்தியாவில் தொழில் வழிகாட்டல் துண்டு துண்டாக உள்ளது — அல்லத… |
| `about.hero.title` | page-text | Built for the student | Enaasan ஏன் உருவானது |
| `about.page.title` | page-text, legacy-en | About Enaasan \| Helping Students Make Better Career and Learning Dec… | எங்களைப் பற்றி — enaasan |
| `bps.analytics.subtitle` | page-text | KPO — Analytics | தரவு பகுப்பாய்வு & ஆராய்ச்சி |
| `bps.analytics.title` | page-text | Data Analytics & Research | KPO — பகுப்பாய்வு |
| `bps.fa.subtitle` | page-text | F&A BPS | நிதி & கணக்கியல் செயல்பாடுகள் |
| `bps.fa.title` | page-text | Finance & Accounting Operations | நிதி & கணக்கியல் BPS |
| `bps.healthcare.subtitle` | page-text | KPO — Healthcare | சுகாதார BPS & மருத்துவ குறியீடு |
| `bps.healthcare.title` | page-text | Healthcare BPS & Medical Coding | KPO — சுகாதாரம் |
| `bps.hr.subtitle` | page-text | HR BPS | மனித வளங்கள் பகிர்ந்த சேவைகள் |
| `bps.hr.title` | page-text | Human Resources Shared Services | மனித வளங்கள் BPS |
| `bps.lpo.subtitle` | page-text | KPO — LPO | Legal Process Outsourcing |
| `bps.lpo.title` | page-text | Legal Process Outsourcing | KPO — சட்ட செயல்முறை மேலாண்மை |
| `bps.nonvoice.subtitle` | page-text | BPS — Non-Voice | பின்னிருக்கை அலுவலக & பரிவர்த்தனை செயலாக்கம் |
| `bps.nonvoice.title` | page-text | Back Office & Transaction Processing | BPS — குரல் அல்லாதது |
| `bps.roles.expand_hint` | page-text | Roles in depth | முழு திறன் தொகுப்பு, கருவிகள் மற்றும் முதலாளிகள் என்ன தேடுக… |
| `bps.roles.subtitle` | page-text | Click any role to expand the full skill set, tools, and what employer… | ஒவ்வொரு பங்கும் உண்மையில் என்ன உள்ளடக்கியது — என்ன தேவை |
| `bps.roles.title` | page-text | What each role actually involves — and what it takes | ஆழமான பங்கு விவரங்கள் |
| `bps.salary.disclaimer` | page-text | *Salary ranges are indicative estimates based on publicly reported da… | சம்பள வரம்புகள் Glassdoor, AmbitionBox, NASSCOM BPS அறிக்கை… |
| `bps.tech.subtitle` | page-text | Tech-enabled BPS | தொழில்நுட்பம் & AI-மேம்படுத்தப்பட்ட செயல்பாடுகள் |
| `bps.tech.title` | page-text | Technology & AI-augmented Operations | தொழில்நுட்பம் இயக்கும் BPS |
| `bps.terminology.bps` | page-text | BPO / BPS | BPO / BPS பரந்த வரம்பை உள்ளடக்குகிறது — குரல் அடிப்படையிலான… |
| `bps.terminology.honest` | page-text | The honest picture: | நேர்மையான படம்: BPS ஒரு மாற்று விருப்பம் அல்ல. இது தெளிவான … |
| `bps.terminology.kpo` | page-text | KPO | KPO என்பது அறிவு சார்ந்த நுண்ணிய பகுதி — சட்ட செயல்முறை மேல… |
| `bps.tips.title` | page-text | Navigating a BPS career — honestly. | யாரும் சொல்லாத விஷயங்கள் |
| `bps.voice.subtitle` | page-text | BPS — Voice | வாடிக்கையாளர் ஆதரவு & தொலைதொடர்பு செயல்பாடுகள் |
| `bps.voice.title` | page-text | Customer Support & Tele-operations | BPS — குரல் |
| `careers.org.intro` | page-text | Nobody explains the unwritten rules. | முதல் வேலையில் சேருவது குழப்பமானது. எழுதப்படாத விதிகளை யாரு… |
| `guide.meta.description` | page-text | A guide for parents, career counsellors, and placement coordinators h… | பெற்றோர், தொழில் ஆலோசகர்கள் மற்றும் வேலை வாய்ப்பு ஒருங்கிணை… |
| `home.card.after12.badge` | page-text, legacy-en | Grade 11–12 · Inter students | 🗺️ 11–12-ம் வகுப்பு · இன்டர் மாணவர்கள் |
| `home.card.after12.cta` | page-text | Plan after 12th | 12-க்கு பிறகு திட்டமிடுங்கள் → |
| `home.card.careers.badge` | page-text, legacy-en | College / Early career | 💼 கல்லூரி / ஆரம்ப தொழில் |
| `home.card.careers.cta` | page-text | See job skill maps | வேலை திறன் வரைபடங்களைப் பாருங்கள் → |
| `home.card.guide.badge` | page-text, legacy-en | Parents · Counsellors · Coordinators | 👨‍👩‍👧 பெற்றோர் · ஆலோசகர்கள் · ஒருங்கிணைப்பாளர்கள் |
| `home.card.guide.cta` | page-text | Go to guidance hub | வழிகாட்டல் மையத்திற்கு செல்லுங்கள் → |
| `home.card.streams.badge` | page-text, legacy-en | Grade 10 · Board exams done | 🎯 10-ம் வகுப்பு · பொதுத் தேர்வு முடிந்தது |
| `home.card.streams.cta` | page-text | Explore streams | பிரிவுகளை ஆய்வு செய்யுங்கள் → |
| `home.hero.title` | legacy-en | Whatever stage you are at — what comes next? | நீங்கள் எந்த நிலையில் இருந்தாலும் — |
| `home.stats.careers.num` | page-text, legacy-en | 40+ | 60+ |
| `home.stats.exams.num` | page-text, legacy-en | 40+ | 20+ |
| `streams.step2.compare` | page-text | Show me all stream paths side by side | 🗺️ அனைத்து பிரிவு பாதைகளையும் பக்கவாட்டில் காட்டுங்கள் |

**Same as English (18)** — review needed; acronyms and numbers are often fine

| Key | Value | Likely |
|---|---|---|
| `about.honest.subtitle` | A thinking tool. Not a counsellor. Not a coaching institute. | **untranslated** |
| `about.origin.section.title` | Built in Hyderabad, for students across India. | **untranslated** |
| `about.problem.section.title` | Career guidance in India is broken — or missing entirely. | **untranslated** |
| `about.promises.subtitle` | Four things enaasan commits to, always. | **untranslated** |
| `about.transparency.section.title` | How enaasan is built — and what that means for you. | **untranslated** |
| `after12.college.iit.title` | IITs / IIMs / IISc / AIIMS | acronym/number — probably OK |
| `after12.college.nit.title` | NITs / BITS / Top NLUs | acronym/number — probably OK |
| `bps.analytics.salary` | ₹3.5–12 LPA | acronym/number — probably OK |
| `bps.fa.salary` | ₹2.5–7 LPA | acronym/number — probably OK |
| `bps.healthcare.salary` | ₹2.5–8 LPA | acronym/number — probably OK |
| `bps.hr.salary` | ₹2.5–6 LPA | acronym/number — probably OK |
| `bps.lpo.salary` | ₹4–15 LPA | acronym/number — probably OK |
| `bps.lpo.subtitle` | Legal Process Outsourcing | **untranslated** |
| `bps.nonvoice.salary` | ₹1.8–3.5 LPA | acronym/number — probably OK |
| `bps.tech.salary` | ₹2.5–10 LPA | acronym/number — probably OK |
| `bps.voice.salary` | ₹1.8–4 LPA | acronym/number — probably OK |
| `careers.org.csuite.title` | C-Suite (CEO, CFO, CTO, COO…) | **untranslated** |
| `nav.brand` | enaasan | **untranslated** |

### 3.2 Telugu (`te`) — reviewer: Vijaya

- Missing: **47** · Stale: **41** · Same as English: **9** (of which 5 look like real untranslated text)

**Missing keys (47)**

| Key | Page(s) | In en.json? |
|---|---|---|
| `firstjob.closing.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.note` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.hero.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.hero.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.meta.description` | skills/first-job/index.html | **no** — add English first |
| `firstjob.nextsteps.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.page.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.note` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause1.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause2.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.question` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.cand1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.cand2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.label` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.setup` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.why` | skills/first-job/index.html | **no** — add English first |
| `firstjob.section.badge` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.title` | skills/first-job/index.html | **no** — add English first |
| `home.starthere.body` | index.html | **no** — add English first |
| `home.starthere.cta` | index.html | **no** — add English first |
| `home.starthere.title` | index.html | **no** — add English first |

**Stale keys (41)**

| Key | Signal | English now | Current translation |
|---|---|---|---|
| `about.hero.body` | page-text | Every year, millions of Indian students make one of the most conseque… | ప్రతి సంవత్సరం, లక్షలాది భారతీయ విద్యార్థులు వారి జీవితంలో … |
| `about.hero.title` | page-text | Built for the student | సరైన మార్గం చూపించే గైడ్ లేని విద్యార్థుల కోసం నిర్మించబడిం… |
| `about.page.title` | page-text, legacy-en | About Enaasan \| Helping Students Make Better Career and Learning Dec… | మా గురించి — enaasan |
| `bps.analytics.subtitle` | page-text | KPO — Analytics | డేటా అనలిటిక్స్ & రీసెర్చ్ |
| `bps.analytics.title` | page-text | Data Analytics & Research | KPO — అనలిటిక్స్ |
| `bps.fa.subtitle` | page-text | F&A BPS | ఫైనాన్స్ & అకౌంటింగ్ ఆపరేషన్స్ |
| `bps.fa.title` | page-text | Finance & Accounting Operations | F&A BPS |
| `bps.healthcare.subtitle` | page-text | KPO — Healthcare | హెల్త్‌కేర్ BPS & మెడికల్ కోడింగ్ |
| `bps.healthcare.title` | page-text | Healthcare BPS & Medical Coding | KPO — హెల్త్‌కేర్ |
| `bps.hr.subtitle` | page-text | HR BPS | హ్యూమన్ రిసోర్సెస్ షేర్డ్ సర్వీసెస్ |
| `bps.hr.title` | page-text | Human Resources Shared Services | HR BPS |
| `bps.lpo.subtitle` | page-text | KPO — LPO | లీగల్ ప్రాసెస్ అవుట్‌సోర్సింగ్ |
| `bps.lpo.title` | page-text | Legal Process Outsourcing | KPO — LPO |
| `bps.nonvoice.subtitle` | page-text | BPS — Non-Voice | బ్యాక్ ఆఫీస్ & ట్రాన్సాక్షన్ ప్రాసెసింగ్ |
| `bps.nonvoice.title` | page-text | Back Office & Transaction Processing | BPS — నాన్-వాయిస్ |
| `bps.roles.expand_hint` | page-text | Roles in depth | పూర్తి నైపుణ్యం సెట్, సాధనాలు, యజమానులు ఏమి చూస్తారో విస్తర… |
| `bps.roles.subtitle` | page-text | Click any role to expand the full skill set, tools, and what employer… | ప్రతి పాత్ర నిజంగా ఏమి ఇమిడి ఉంటుంది — మరియు దానికి ఏమి అవస… |
| `bps.roles.title` | page-text | What each role actually involves — and what it takes | పాత్రలు లోతుగా |
| `bps.salary.disclaimer` | page-text | *Salary ranges are indicative estimates based on publicly reported da… | జీతం పరిధులు Glassdoor, AmbitionBox, NASSCOM BPS నివేదికలు,… |
| `bps.tech.subtitle` | page-text | Tech-enabled BPS | టెక్నాలజీ & AI-ఆగ్మెంటెడ్ ఆపరేషన్స్ |
| `bps.tech.title` | page-text | Technology & AI-augmented Operations | టెక్-ఎనేబుల్డ్ BPS |
| `bps.terminology.bps` | page-text | BPO / BPS | BPO / BPS విస్తృత శ్రేణిని కవర్ చేస్తుంది — వాయిస్-ఆధారిత క… |
| `bps.terminology.honest` | page-text | The honest picture: | నిజమైన చిత్రం: BPS ఒక ప్రత్యామ్నాయం కాదు. ఇది స్పష్టమైన ప్ర… |
| `bps.terminology.kpo` | page-text | KPO | KPO జ్ఞాన-ఇంటెన్సివ్ చివర — లీగల్ ప్రాసెస్ అవుట్‌సోర్సింగ్,… |
| `bps.tips.title` | page-text | Navigating a BPS career — honestly. | ఎవరూ మీకు చెప్పనివి |
| `bps.voice.subtitle` | page-text | BPS — Voice | కస్టమర్ సపోర్ట్ & టెలి-ఆపరేషన్స్ |
| `bps.voice.title` | page-text | Customer Support & Tele-operations | BPS — వాయిస్ |
| `careers.org.intro` | page-text | Nobody explains the unwritten rules. | మీ మొదటి ఉద్యోగం గందరగోళంగా ఉంటుంది. ఎవరూ అలిఖిత నియమాలు వి… |
| `guide.meta.description` | page-text | A guide for parents, career counsellors, and placement coordinators h… | తల్లిదండ్రులు, కెరీర్ కౌన్సెలర్లు, ప్లేస్‌మెంట్ కోఆర్డినేటర… |
| `home.card.after12.badge` | page-text, legacy-en | Grade 11–12 · Inter students | 🗺️ గ్రేడ్ 11-12 · ఇంటర్ విద్యార్థులు |
| `home.card.after12.cta` | page-text | Plan after 12th | 12వ తర్వాత ప్లాన్ చేయండి → |
| `home.card.careers.badge` | page-text, legacy-en | College / Early career | 💼 కాలేజీ / ఆరంభ కెరీర్ |
| `home.card.careers.cta` | page-text | See job skill maps | జాబ్ నైపుణ్యం మ్యాప్‌లు చూడండి → |
| `home.card.guide.badge` | page-text, legacy-en | Parents · Counsellors · Coordinators | 👨‍👩‍👧 తల్లిదండ్రులు · కౌన్సెలర్లు · కోఆర్డినేటర్లు |
| `home.card.guide.cta` | page-text | Go to guidance hub | గైడెన్స్ హబ్‌కు వెళ్ళండి → |
| `home.card.streams.badge` | page-text, legacy-en | Grade 10 · Board exams done | 🎯 గ్రేడ్ 10 · బోర్డ్ పరీక్షలు పూర్తయ్యాయి |
| `home.card.streams.cta` | page-text | Explore streams | గ్రూప్‌లను అన్వేషించండి → |
| `home.hero.title` | legacy-en | Whatever stage you are at — what comes next? | మీరు ఏ దశలో ఉన్నా — |
| `home.stats.careers.num` | page-text, legacy-en | 40+ | 60+ |
| `home.stats.exams.num` | page-text, legacy-en | 40+ | 20+ |
| `streams.step2.compare` | page-text | Show me all stream paths side by side | 🗺️ అన్ని గ్రూప్ మార్గాలు పక్కపక్కన చూపించు |

**Same as English (9)** — review needed; acronyms and numbers are often fine

| Key | Value | Likely |
|---|---|---|
| `after12.college.iit.title` | IITs / IIMs / IISc / AIIMS | acronym/number — probably OK |
| `bps.fa.title` | F&A BPS | acronym/number — probably OK |
| `bps.hr.title` | HR BPS | acronym/number — probably OK |
| `bps.lpo.title` | KPO — LPO | acronym/number — probably OK |
| `careers.org.csuite.title` | C-Suite (CEO, CFO, CTO, COO…) | **untranslated** |
| `guide.share.linkedin` | in LinkedIn | **untranslated** |
| `guide.share.twitter` | 𝕏 X / Twitter | **untranslated** |
| `guide.share.whatsapp` | 💬 WhatsApp | **untranslated** |
| `nav.brand` | enaasan | **untranslated** |

### 3.3 Hindi (`hi`) — reviewer: Shafi

- Missing: **47** · Stale: **41** · Same as English: **42** (of which 29 look like real untranslated text)

**Missing keys (47)**

| Key | Page(s) | In en.json? |
|---|---|---|
| `firstjob.closing.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.body5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.note` | skills/first-job/index.html | **no** — add English first |
| `firstjob.closing.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.hero.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.hero.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.intro.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.meta.description` | skills/first-job/index.html | **no** — add English first |
| `firstjob.nextsteps.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.page.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.clarify3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.detail5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.note` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause1.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.pause2.body` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.question` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.cand1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.cand2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.scenario.label` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.setup` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.title` | skills/first-job/index.html | **no** — add English first |
| `firstjob.reflection.why` | skills/first-job/index.html | **no** — add English first |
| `firstjob.section.badge` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body1` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body2` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body3` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body4` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.body5` | skills/first-job/index.html | **no** — add English first |
| `firstjob.teaches.title` | skills/first-job/index.html | **no** — add English first |
| `home.starthere.body` | index.html | **no** — add English first |
| `home.starthere.cta` | index.html | **no** — add English first |
| `home.starthere.title` | index.html | **no** — add English first |

**Stale keys (41)**

| Key | Signal | English now | Current translation |
|---|---|---|---|
| `about.hero.body` | page-text | Every year, millions of Indian students make one of the most conseque… | हर साल, लाखों भारतीय छात्र अपने जीवन के सबसे महत्वपूर्ण फैस… |
| `about.hero.title` | page-text | Built for the student | उस छात्र के लिए बनाया जिसे कोई गाइड नहीं किया। |
| `about.page.title` | page-text, legacy-en | About Enaasan \| Helping Students Make Better Career and Learning Dec… | हमारे बारे में — enaasan |
| `bps.analytics.subtitle` | page-text | KPO — Analytics | Data Analytics & Research |
| `bps.analytics.title` | page-text | Data Analytics & Research | KPO — Analytics |
| `bps.fa.subtitle` | page-text | F&A BPS | Finance & Accounting Operations |
| `bps.fa.title` | page-text | Finance & Accounting Operations | F&A BPS |
| `bps.healthcare.subtitle` | page-text | KPO — Healthcare | Healthcare BPS और Medical Coding |
| `bps.healthcare.title` | page-text | Healthcare BPS & Medical Coding | KPO — Healthcare |
| `bps.hr.subtitle` | page-text | HR BPS | Human Resources Shared Services |
| `bps.hr.title` | page-text | Human Resources Shared Services | HR BPS |
| `bps.lpo.subtitle` | page-text | KPO — LPO | Legal Process Outsourcing |
| `bps.lpo.title` | page-text | Legal Process Outsourcing | KPO — LPO |
| `bps.nonvoice.subtitle` | page-text | BPS — Non-Voice | बैक ऑफिस और ट्रांजेक्शन प्रोसेसिंग |
| `bps.nonvoice.title` | page-text | Back Office & Transaction Processing | BPS — नॉन-वॉइस |
| `bps.roles.expand_hint` | page-text | Roles in depth | पूरा स्किल सेट, टूल्स और एम्पलॉयर क्या ढूंढते हैं देखने के … |
| `bps.roles.subtitle` | page-text | Click any role to expand the full skill set, tools, and what employer… | हर रोल में असल में क्या होता है — और क्या चाहिए |
| `bps.roles.title` | page-text | What each role actually involves — and what it takes | रोल्स गहराई से |
| `bps.salary.disclaimer` | page-text | *Salary ranges are indicative estimates based on publicly reported da… | सैलरी रेंज Glassdoor, AmbitionBox, NASSCOM BPS रिपोर्ट और L… |
| `bps.tech.subtitle` | page-text | Tech-enabled BPS | Technology और AI-augmented Operations |
| `bps.tech.title` | page-text | Technology & AI-augmented Operations | Tech-enabled BPS |
| `bps.terminology.bps` | page-text | BPO / BPS | BPO / BPS का दायरा बड़ा है — वॉइस-बेस्ड कस्टमर सपोर्ट से ले… |
| `bps.terminology.honest` | page-text | The honest picture: | सच्ची तस्वीर: BPS फॉलबैक नहीं है। यह स्पष्ट एंट्री पॉइंट, प… |
| `bps.terminology.kpo` | page-text | KPO | KPO ज्ञान-गहन छोर है — लीगल प्रोसेस आउटसोर्सिंग, फाइनेंशियल… |
| `bps.tips.title` | page-text | Navigating a BPS career — honestly. | वो बातें जो कोई नहीं बताता |
| `bps.voice.subtitle` | page-text | BPS — Voice | कस्टमर सपोर्ट और टेली-ऑपरेशंस |
| `bps.voice.title` | page-text | Customer Support & Tele-operations | BPS — वॉइस |
| `careers.org.intro` | page-text | Nobody explains the unwritten rules. | पहली नौकरी में शुरुआत भटकाने वाली होती है। कोई अलिखित नियम … |
| `guide.meta.description` | page-text | A guide for parents, career counsellors, and placement coordinators h… | माता-पिता, करियर काउंसलर और प्लेसमेंट कोऑर्डिनेटर के लिए सं… |
| `home.card.after12.badge` | page-text, legacy-en | Grade 11–12 · Inter students | 🗺️ ग्रेड 11–12 · इंटर के छात्र |
| `home.card.after12.cta` | page-text | Plan after 12th | 12वीं के बाद प्लान करें → |
| `home.card.careers.badge` | page-text, legacy-en | College / Early career | 💼 कॉलेज / अर्ली करियर |
| `home.card.careers.cta` | page-text | See job skill maps | जॉब स्किल मैप देखें → |
| `home.card.guide.badge` | page-text, legacy-en | Parents · Counsellors · Coordinators | 👨‍👩‍👧 माता-पिता · काउंसलर · कोऑर्डिनेटर |
| `home.card.guide.cta` | page-text | Go to guidance hub | गाइडेंस हब पर जाएं → |
| `home.card.streams.badge` | page-text, legacy-en | Grade 10 · Board exams done | 🎯 ग्रेड 10 · बोर्ड परीक्षा हो गई |
| `home.card.streams.cta` | page-text | Explore streams | स्ट्रीम एक्सप्लोर करें → |
| `home.hero.title` | legacy-en | Whatever stage you are at — what comes next? | आप जहाँ भी हों — |
| `home.stats.careers.num` | page-text, legacy-en | 40+ | 60+ |
| `home.stats.exams.num` | page-text, legacy-en | 40+ | 20+ |
| `streams.step2.compare` | page-text | Show me all stream paths side by side | 🗺️ सभी स्ट्रीम पाथ एक साथ दिखाएं |

**Same as English (42)** — review needed; acronyms and numbers are often fine

| Key | Value | Likely |
|---|---|---|
| `after12.college.iit.title` | IITs / IIMs / IISc / AIIMS | acronym/number — probably OK |
| `after12.college.nit.title` | NITs / BITS / Top NLUs | acronym/number — probably OK |
| `after12.filter.arts` | 🎭 Arts & Humanities | **untranslated** |
| `after12.filter.commerce` | 📈 Commerce | **untranslated** |
| `after12.filter.defence` | 🎖️ Defence | **untranslated** |
| `after12.filter.pcb` | 🧬 Science (PCB) | **untranslated** |
| `after12.filter.pcm` | ⚛️ Science (PCM) | **untranslated** |
| `bps.analytics.salary` | ₹3.5–12 LPA | acronym/number — probably OK |
| `bps.analytics.subtitle` | Data Analytics & Research | **untranslated** |
| `bps.analytics.title` | KPO — Analytics | **untranslated** |
| `bps.crossover.analytics.to` | → In-house Analytics, Strategy, Consulting | **untranslated** |
| `bps.crossover.fa.to` | → Corporate Finance, Controllership | **untranslated** |
| `bps.crossover.hr.to` | → HR Business Partner, HR Manager | **untranslated** |
| `bps.crossover.lpo.to` | → In-house Counsel, Law Firm, Compliance | **untranslated** |
| `bps.crossover.ops.to` | → Operations Management, General Management | **untranslated** |
| `bps.fa.salary` | ₹2.5–7 LPA | acronym/number — probably OK |
| `bps.fa.subtitle` | Finance & Accounting Operations | **untranslated** |
| `bps.fa.title` | F&A BPS | acronym/number — probably OK |
| `bps.healthcare.salary` | ₹2.5–8 LPA | acronym/number — probably OK |
| `bps.healthcare.title` | KPO — Healthcare | **untranslated** |
| `bps.hr.salary` | ₹2.5–6 LPA | acronym/number — probably OK |
| `bps.hr.subtitle` | Human Resources Shared Services | **untranslated** |
| `bps.hr.title` | HR BPS | acronym/number — probably OK |
| `bps.lpo.salary` | ₹4–15 LPA | acronym/number — probably OK |
| `bps.lpo.subtitle` | Legal Process Outsourcing | **untranslated** |
| `bps.lpo.title` | KPO — LPO | acronym/number — probably OK |
| `bps.nonvoice.salary` | ₹1.8–3.5 LPA | acronym/number — probably OK |
| `bps.tech.salary` | ₹2.5–10 LPA | acronym/number — probably OK |
| `bps.tech.title` | Tech-enabled BPS | **untranslated** |
| `bps.voice.salary` | ₹1.8–4 LPA | acronym/number — probably OK |
| `careers.dept.finance.title` | Finance | **untranslated** |
| `careers.dept.hr.title` | Human Resources (HR) | **untranslated** |
| `careers.dept.marketing.title` | Marketing | **untranslated** |
| `careers.dept.ops.title` | Operations | **untranslated** |
| `careers.dept.sales.title` | Sales & Business Development | **untranslated** |
| `careers.dept.tech.title` | Technology / IT | **untranslated** |
| `careers.org.csuite.title` | C-Suite (CEO, CFO, CTO, COO…) | **untranslated** |
| `guide.share.linkedin` | in LinkedIn | **untranslated** |
| `guide.share.twitter` | 𝕏 X / Twitter | **untranslated** |
| `guide.share.whatsapp` | 💬 WhatsApp | **untranslated** |
| `home.stats.india.label` | India-first | **untranslated** |
| `nav.brand` | enaasan | **untranslated** |

## 4. Hardcoded English (not routed through i18n)

These strings stay in English whatever language the visitor picks. Counts are approximate (heuristic: 2+ English words in a text node or attribute; 4+ words in a script string). Full list: [`translation-audit-hardcoded.md`](translation-audit-hardcoded.md).

| Page | Text nodes | Attributes | Script strings | Total | Uses i18n? |
|---|---:|---:|---:|---:|---|
| `90-day-plan.html` | 39 | 0 | 0 | 39 | **no** |
| `about.html` | 11 | 5 | 0 | 16 | yes |
| `after10.html` | 215 | 5 | 0 | 220 | yes |
| `after12.html` | 69 | 5 | 132 | 206 | yes |
| `bps.html` | 118 | 5 | 105 | 228 | yes |
| `career-exploration/01-who-are-you.html` | 123 | 0 | 0 | 123 | **no** |
| `careers.html` | 15 | 5 | 605 | 625 | yes |
| `components/ask-enaasan-search.html` | 9 | 1 | 2 | 12 | **no** |
| `components/cookie-consent.html` | 5 | 0 | 0 | 5 | **no** |
| `components/guidance-disclaimer.html` | 6 | 0 | 0 | 6 | **no** |
| `faq.html` | 5 | 6 | 0 | 11 | yes |
| `gig-work/index.html` | 210 | 5 | 0 | 215 | **no** |
| `guide.html` | 9 | 5 | 0 | 14 | yes |
| `index.html` | 16 | 5 | 0 | 21 | yes |
| `privacy.html` | 45 | 5 | 0 | 50 | **no** |
| `skills/communication/definition/index.html` | 50 | 4 | 0 | 54 | **no** |
| `skills/communication/examples/index.html` | 69 | 4 | 0 | 73 | **no** |
| `skills/communication/framework/index.html` | 74 | 4 | 0 | 78 | **no** |
| `skills/communication/index.html` | 43 | 4 | 0 | 47 | **no** |
| `skills/communication/readiness/index.html` | 54 | 4 | 0 | 58 | **no** |
| `skills/communication/salary-premium/index.html` | 72 | 4 | 0 | 76 | **no** |
| `skills/first-job/build-skills/index.html` | 152 | 4 | 0 | 156 | **no** |
| `skills/first-job/explore-careers/index.html` | 73 | 4 | 0 | 77 | **no** |
| `skills/first-job/index.html` | 10 | 5 | 0 | 15 | yes |
| `state-exams.html` | 17 | 0 | 77 | 94 | **no** |
| `streams.html` | 7 | 5 | 137 | 149 | yes |
| `terms.html` | 52 | 5 | 0 | 57 | **no** |
| `theme-preview.html` | 38 | 4 | 3 | 45 | **no** |

Script strings are mostly the data behind interactive cards (exam cards on `after12.html`, stream paths on `streams.html`, career profiles on `careers.html`) — known bugs B-14 / B-15.

## 5. Structural problems found

1. **Switching back to English shows old English.** `js/i18n.js` applies `locales/en.json` when a visitor switches back to English. 40 page elements differ from it, e.g. homepage stats revert to "60+ / 20+" and the About title reverts to the pre-SEO version.
2. **`skills/first-job/` cannot translate.** 44 of its keys are not in any language file, and its script requests `locales/<lang>.json` relative to `/skills/first-job/`, which does not exist — Tamil/Telugu/Hindi silently fall back to English.
3. **Legacy `i18n/` folder** holds edits that are not live (§6).
4. **20 keys in `en.json` are not used by any page:** `about.honest.subtitle`, `about.origin.section.title`, `about.problem.section.title`, `about.promises.subtitle`, `about.transparency.section.title`, `bps.tips.subtitle`, `guide.parents.myths.subtitle`, `home.ai.badge`, `home.ai.body`, `home.ai.notify.button`, `home.ai.notify.confirm`, `home.ai.notify.label`, `home.ai.section.title`, `home.ai.share.text`, `home.ai.subtitle`, `home.ai.title`, `home.share.linkedin`, `home.share.twitter`, `home.share.whatsapp`, `nav.brand`

## 6. Legacy folder `i18n/` — differences from the live files

Not loaded by the site. Listed so reviewed work is not lost.

| Language | Keys whose `i18n/` value differs from `locales/` |
|---|---:|
| English | 8 |
| Tamil | 8 |
| Telugu | 8 |
| Hindi | 31 |

Hindi: commit `1f7841e` (2026-07-02) "Apply Shafi's Hindi review decisions" changed 23 values in `i18n/hi.json` only — **reviewed Hindi that is not live.**

<details><summary>Hindi keys that differ (legacy vs live)</summary>

| Key | `i18n/hi.json` (legacy) | `locales/hi.json` (live) |
|---|---|---|
| `about.page.title` | हमारे बारे में \| छात्रों को बेहतर करियर और शिक्षा निर्णय ल… | हमारे बारे में — enaasan |
| `after12.timeline.step6.title` | परामर्श एवं सीट आवंटन | काउंसलिंग और सीट अलॉटमेंट |
| `after12.tip2.title` | साल का अंतराल एक वैध विकल्प है | गैप ईयर एक वैध विकल्प है |
| `bps.crossover.fa.body` | ट्रांसफर होने वाली स्किल: ERP सिस्टम, रिकन्सिलिएशन, फाइनेंश… | ट्रांसफर होने वाली स्किल: ERP सिस्टम, रिकन्सिलिएशन, फाइनेंश… |
| `bps.growth.subtitle` | BPS में व्यवस्थित ग्रोथ पाथ हैं। यहाँ है अलग-अलग ट्रैक में … | BPS में व्यवस्थित ग्रोथ पाथ हैं। यहाँ है अलग-अलग ट्रैक में … |
| `bps.terminology.honest` | सच्ची तस्वीर: BPS फॉलबैक नहीं है। यह स्पष्ट एंट्री पॉइंट, प… | सच्ची तस्वीर: BPS फॉलबैक नहीं है। यह स्पष्ट एंट्री पॉइंट, प… |
| `bps.tip2.body` | अंतरराष्ट्रीय प्रोसेस रोल (US/UK/Australia शिफ्ट टाइमिंग) ड… | अंतरराष्ट्रीय प्रोसेस रोल (US/UK/Australia शिफ्ट टाइमिंग) ड… |
| `bps.tip3.body` | BPS में बेहद ज्यादा कर्मचारी त्याग दर है। बहुत से लोग एक कं… | BPS में बेहद ज्यादा एट्रिशन है। बहुत से लोग एक कंपनी में ऊर… |
| `bps.tip3.title` | कर्मचारी त्याग दर का जाल — लोग क्यों अटके रहते हैं | एट्रिशन का जाल — लोग क्यों अटके रहते हैं |
| `careers.advice1.title` | दृश्यता गुणवत्ता जितनी ही मायने रखती है | विजिबिलिटी गुणवत्ता जितनी ही मायने रखती है |
| `careers.ai.new_roles.tip` | अपनी टीम का AI champion बनने के लिए आगे आएं। AI टूल्स को प्… | अपनी टीम का AI champion बनने के लिए आगे आएं। AI टूल्स को प्… |
| `careers.growth.subtitle` | कोई फील्ड चुनें — नौसिखिया से सीनियर लीडर तक का आम करियर लै… | कोई फील्ड चुनें — फ्रेशर से सीनियर लीडर तक का आम करियर लैडर… |
| `careers.org.manager.tip` | मैनेजर के रूप में आपकी सफलता आपकी टीम के आउटपुट से मापी जात… | मैनेजर के रूप में आपकी सफलता आपकी टीम के आउटपुट से मापी जात… |
| `careers.org.tl.tip` | यह वह ट्रांजिशन है जहाँ बहुत से लोग अटक जाते हैं — 'खुद करन… | यह वह ट्रांजिशन है जहाँ बहुत से लोग अटक जाते हैं — 'करने' स… |
| `guide.counsellors.change2.title` | NDA में अब महिला प्रत्याशी के लिए भी आवेदन खुले हैं। | NDA अब महिला उम्मीदवारों के लिए खुला है |
| `guide.parents.change6.body` | आज एक अच्छा नौसिखिया सॉफ्टवेयर इंजीनियर ₹6–15 LPA कमा सकता … | आज एक अच्छा सॉफ्टवेयर इंजीनियर फ्रेशर ₹6–15 LPA कमा सकता है… |
| `guide.parents.myth3.myth` | साल का अंतराल समय की बर्बादी है। | गैप ईयर समय की बर्बादी है। |
| `guide.parents.myth3.reality` | JEE और NEET के कई टॉप स्कोरर ड्रॉप ईयर छात्र हैं। तैयारी या… | JEE और NEET के कई टॉप स्कोरर ड्रॉप ईयर छात्र हैं। तैयारी या… |
| `guide.parents.myths.myth_label` | ❌ गलतफहमी | ❌ मिथक |
| `home.card.after12.badge` | ग्रेड 11–12 · इंटर के छात्र | 🗺️ ग्रेड 11–12 · इंटर के छात्र |
| `home.card.careers.badge` | कॉलेज / अर्ली करियर | 💼 कॉलेज / अर्ली करियर |
| `home.card.guide.badge` | माता-पिता · काउंसलर · कोऑर्डिनेटर | 👨‍👩‍👧 माता-पिता · काउंसलर · कोऑर्डिनेटर |
| `home.card.streams.badge` | ग्रेड 10 · बोर्ड परीक्षा हो गई | 🎯 ग्रेड 10 · बोर्ड परीक्षा हो गई |
| `home.hero.title` | आप जहाँ भी हों — आगे क्या? | आप जहाँ भी हों — |
| `home.how.step1.num` | कदम 01 | चरण 01 |
| `home.how.step2.num` | कदम 02 | चरण 02 |
| `home.how.step3.num` | कदम 03 | चरण 03 |
| `home.how.step3.title` | वे प्रश्न पूछें जिन्हें आप Google पर नहीं खोज सकते। | वो सवाल पूछें जो Google पर नहीं मिलते |
| `home.how.step4.num` | कदम 04 | चरण 04 |
| `home.stats.careers.num` | 40+ | 60+ |
| `home.stats.exams.num` | 40+ | 20+ |

</details>

## 7. Re-running and the guard

See README → "Translation checks". `python3 scripts/i18n-check.py audit` regenerates this file; `check` runs in GitHub Actions on every pull request that touches pages or locale files.
