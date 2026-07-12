$repo = "siddiquema/enaasan"

Write-Host "Step 1: Creating labels..." -ForegroundColor Cyan
gh label create "execute-now" --color "0E8A16" --description "Ready to code, no decisions needed" --repo $repo --force
gh label create "needs-decision" --color "E4A820" --description "Blocked until a decision is made" --repo $repo --force
gh label create "stage-2" --color "0075CA" --description "Deferred until after young-user feedback round" --repo $repo --force
gh label create "design" --color "D93F0B" --description "Visual, layout, icons, typography" --repo $repo --force
gh label create "ux" --color "006B75" --description "Navigation, interaction, accessibility" --repo $repo --force
gh label create "copy" --color "5319E7" --description "Messaging, taglines, stream descriptions" --repo $repo --force
gh label create "content" --color "0052CC" --description "New pages, career tracks, exam info" --repo $repo --force
gh label create "i18n" --color "BFD4F2" --description "Translation and multilingual issues" --repo $repo --force
gh label create "performance" --color "E4E669" --description "Speed, image size, SEO, schema" --repo $repo --force
gh label create "security" --color "555555" --description "Headers, HTTPS, privacy" --repo $repo --force
gh label create "strategic" --color "C2E0C6" --description "Big decisions, scope, product vision" --repo $repo --force
Write-Host "Labels done." -ForegroundColor Green

Write-Host "Step 2: Creating milestones..." -ForegroundColor Cyan
gh api repos/$repo/milestones --method POST --field title="Sprint 1 - Core fixes" --field description="All execute-now items. Complete before Saturday decision session."
gh api repos/$repo/milestones --method POST --field title="Saturday decision session" --field description="13 decision-blocked items get unblocked here."
gh api repos/$repo/milestones --method POST --field title="Sprint 2 - Post-decision execution" --field description="Implement all items unblocked by the Saturday session."
gh api repos/$repo/milestones --method POST --field title="Stage 2 - After young-user feedback" --field description="Content expansion, new career tracks, backend features."
gh api repos/$repo/milestones --method POST --field title="Launch" --field description="LinkedIn launch post. Triggered after Sprint 1 and Saturday decisions are complete."
Write-Host "Milestones done." -ForegroundColor Green

Write-Host "Step 3: Creating architecture rule issue..." -ForegroundColor Cyan
$body = "ARCHITECTURE RULE - read before every edit.`n`ndata-i18n must ONLY be placed on leaf-node text elements with no child HTML.`n`nCORRECT: span data-i18n=key - text only`nWRONG: h1 data-i18n=key with child span inside it`n`ni18n.js uses el.textContent which destroys all child nodes.`n`nBugs already caused: button inside .step-nav wiped (See matching streams unclickable), span inside .nav-logo wiped (logo lost gold rendering).`n`nBefore every edit run: grep -n data-i18n filename.html and verify each result has no child HTML tags."
gh issue create --repo $repo --title "ARCHITECTURE RULE - never violate (pin this)" --label "bug" --body $body
Write-Host "Architecture rule issue done." -ForegroundColor Green

Write-Host "Step 4: Creating execute-now issues..." -ForegroundColor Cyan

gh issue create --repo $repo --title "#40 Nav overlay blocking content on inner pages mobile" --label "execute-now,bug,ux" --body "Fixed nav is 90-100px tall on mobile. Language pills wrap to 2nd row and block taps on interest tiles. Fix applied to streams.html - apply same media query fix to guide.html, about.html, bps.html, careers.html, after12.html in one pass one commit. CSS: @media max-width 560px - nav flex-direction column, .page padding-top 140px."

gh issue create --repo $repo --title "#42 Stream tile selection no visual feedback at point of tap" --label "execute-now,ux" --body "When a student taps an interest tile or stream card in streams.html there is no immediate visual confirmation. Add a selected state with border highlight and checkmark icon at moment of tap in Step 1 and Step 2."

gh issue create --repo $repo --title "#26 Stream Step 2 descriptions have no future-of-work signal" --label "execute-now,copy" --body "Step 2 stream descriptions are generic. Rewrite with fast-growing 2026 fields. PCM: add AI/ML, semiconductors, EVs, space tech. Commerce: add fintech, analytics, GCC sector. PCB: add pharma, biotech, public health. Arts: add UX/design, journalism, law, psychology. Optional: add GROWING IN pill row beneath subject pills."

gh issue create --repo $repo --title "#33 BPS KPO page has no homepage card - only discoverable via footer" --label "execute-now,ux,content" --body "bps.html is invisible on the homepage. Add a 5th homepage card on index.html matching the existing 4-card visual template linking to bps.html. Card title: BPS and KPO Careers."

gh issue create --repo $repo --title "#34 AI and Machine Learning has no visual differentiation in Career Compass" --label "execute-now,design" --body "careers.html lists AI and Machine Learning with no indication it is the fastest-growing sector. Add a Fastest growing badge to the AI and Machine Learning career card matching dark navy/gold design."

gh issue create --repo $repo --title "#16 No outbound links to official exam and government websites" --label "execute-now,content" --body "Add official outbound links across after12.html, streams.html, careers.html. Open in new tab with rel=noopener noreferrer. Include: nta.ac.in, cuet.samarth.ac.in, jeemain.nta.ac.in, neet.nta.nic.in, cbse.gov.in"

gh issue create --repo $repo --title "C-04 Language switcher returning to English unreliable on streams.html" --label "execute-now,bug,i18n" --body "After switching to Tamil, Telugu, or Hindi on streams.html, switching back to English does not re-render the JS-driven grid. Fire a custom langchange event in i18n.js after each language switch. In streams.html listen for that event and re-call buildStreamsGrid and buildPath."

gh issue create --repo $repo --title "C-05 Security headers file missing" --label "execute-now,security" --body "Create _headers file in repo root. Add: Strict-Transport-Security max-age=31536000 includeSubDomains, X-Content-Type-Options nosniff, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy geolocation=() microphone=() camera=(). GitHub Pages supports _headers natively."

gh issue create --repo $repo --title "C-06 Terms and Disclaimer page missing" --label "execute-now,content" --body "Create terms.html similar to privacy.html. Content: not a certified career counsellor, not affiliated with any institution, information is for guidance only. Link in footer of all 8 pages alongside Privacy Policy."

gh issue create --repo $repo --title "C-07 Hero section too tall on mobile - cards appear below the fold" --label "execute-now,ux" --body "On mobile the hero min-height pushes homepage cards too far down. Reduce hero min-height on index.html for mobile. Test on 360px and 390px screen widths."

gh issue create --repo $repo --title "C-08 No conversion path on homepage" --label "execute-now,ux" --body "No way for a visitor to stay connected after first visit. Add WhatsApp community link OR a Notify me when AI mentor launches prompt on index.html. No forced signup."

gh issue create --repo $repo --title "C-01a OG image too large and OG description too long" --label "execute-now,performance" --body "assets/og-image.png is 1.1MB. Run: pngquant --quality=65-85 assets/og-image.png to compress. og:description on index.html is 130 chars - trim to under 125 for mobile previews."

gh issue create --repo $repo --title "C-10 Schema.org structured data missing on all pages" --label "execute-now,performance" --body "Add schema.org JSON-LD to all 8 pages. index.html: EducationalOrganization and WebSite schema. guide.html: FAQPage schema. All inner pages: BreadcrumbList schema."

gh issue create --repo $repo --title "Sitemap - privacy.html missing from sitemap.xml" --label "execute-now,performance" --body "Add privacy.html to sitemap.xml. Resubmit sitemap in Google Search Console after pushing."

Write-Host "Execute-now issues done." -ForegroundColor Green
Write-Host "Step 5: Creating needs-decision issues..." -ForegroundColor Cyan

gh issue create --repo $repo --title "#1 No tagline or value proposition on first screen" --label "needs-decision,copy" --body "Decision needed: agree the tagline and value proposition line for the hero section. First-time visitors do not immediately understand what enaasan does. To unblock: add agreed line as a comment then relabel to execute-now."

gh issue create --repo $repo --title "#6 No top navigation with dropdown menu" --label "needs-decision,ux" --body "Decision needed: nav structure - which pages appear in dropdown, how it behaves on mobile, whether it replaces or supplements current footer nav. To unblock: agree structure, add as comment, relabel to execute-now."

gh issue create --repo $repo --title "#7 Find Your Path is passive - needs guided quiz" --label "needs-decision,ux" --body "Decision needed: quiz design - 3 to 5 questions, what they ask, how results map to stream and career recommendations. Currently the page just lists streams."

gh issue create --repo $repo --title "#17 Brand name Enaasan misread by multiple users" --label "needs-decision,copy,design" --body "Anvar read E naasan. Sheerin read En aasan. Decision needed: how to display brand name to aid correct pronunciation. Options: pronunciation note, adjusted typography, transliteration in Tamil script."

gh issue create --repo $repo --title "#18 First-time visitors do not know where to start" --label "needs-decision,ux" --body "Decision needed: onboarding flow - should there be a modal, hero CTA sequence, quiz, or chatbot prompt as the primary entry point for new visitors?"

gh issue create --repo $repo --title "#21 Low-income and post-Class 10 pathways entirely missing" --label "needs-decision,content" --body "Students who need to earn after Class 10 have no guidance. Flagged by Anvar via voice note. Decision needed: framing and placement. Tone is critical - must be empowering and dignified, not a fallback. Must not discourage students who can pursue higher education."

gh issue create --repo $repo --title "#25 Homepage opening copy is informational not aspirational" --label "needs-decision,copy" --body "Flagged by Harpreet: current copy tells students what the site does but does not pull them into their own future. Decision needed: full homepage copy rewrite direction - agree voice, tone, and emotional hooks before rewriting."

gh issue create --repo $repo --title "#3 No hero image - homepage feels text-heavy" --label "needs-decision,design" --body "Decision needed: image direction - illustration vs photo, subject matter (students, aspirational career imagery, abstract), licensing approach."

gh issue create --repo $repo --title "#22 Target Map Family icons do not match dark navy gold design" --label "needs-decision,design" --body "Decision needed: icon replacement style - Phosphor, Heroicons, Tabler, or custom SVG. Determines which library to standardise on sitewide."

gh issue create --repo $repo --title "#23 Background visuals not career-oriented" --label "needs-decision,design" --body "Decision needed: visual and decorative direction - what background elements fit a dark navy/gold Indian career guidance platform for students?"

gh issue create --repo $repo --title "#29 Sarkari Naukri and Government Jobs - no dedicated depth page" --label "needs-decision,content,strategic" --body "High search volume. SSC CGL, IBPS, State PSCs, UPSC have very different prep timelines. Currently not covered. Decision needed: scope and depth, dedicated page vs expanded careers.html section."

gh issue create --repo $repo --title "#36 No visual career roadmaps or comparison charts" --label "needs-decision,design" --body "Flagged by Kamalakar: site is too text-heavy. Decision needed: static SVG infographics, interactive flowcharts, or downloadable PDFs?"

gh issue create --repo $repo --title "#20 Site focuses on national exams - state-level exams missing" --label "needs-decision,content,strategic" --body "Decision needed: which states to cover, which state-level board exams and entrance exams to include. Primary markets: Telangana and Tamil Nadu."

Write-Host "Needs-decision issues done." -ForegroundColor Green
Write-Host "Step 6: Creating stage-2 issues..." -ForegroundColor Cyan

gh issue create --repo $repo --title "#8 Sports as a career - not covered anywhere" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#9 Teacher training - not covered anywhere" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#10 Location-based institute recommendations needs backend" --label "stage-2,content,ux" --body "Requires data sourcing and likely a backend. Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#11 Font size accessibility widget sitewide A A+ A++" --label "stage-2,ux" --body "Simple toggle for older parents and younger students. Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#19 Polytechnic Diplomas ITIs and short certificate courses missing" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#27 Supply Chain and Logistics missing from Career Compass" --label "stage-2,content" --body "Major and fast-growing Indian sector. Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#28 Distance and Online Education missing as pathway and career" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#30 Gig Economy Freelancing and Creator Economy missing" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#31 Manufacturing and Semiconductor Fabs no career track coverage" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#32 Climate Tech Green Energy Space Tech missing from Career Compass" --label "stage-2,content" --body "Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#37 No student stories or social proof" --label "stage-2,content" --body "Future content - real student journeys and testimonials. Deferred until after young-user feedback round."
gh issue create --repo $repo --title "#38 Multilingual rollout - Telugu and Hindi v2 review pending" --label "stage-2,i18n" --body "Tamil reviewed by family member. Telugu confirmed by Vijaya. Hindi v2 review pending with Shafi. All 4 language files at 599 keys each."

Write-Host "Stage-2 issues done." -ForegroundColor Green
Write-Host ""
Write-Host "All done! Issue count:" -ForegroundColor Cyan
gh issue list --repo $repo --state open --limit 100 | Measure-Object -Line
Write-Host "View at: https://github.com/siddiquema/enaasan/issues" -ForegroundColor Green
