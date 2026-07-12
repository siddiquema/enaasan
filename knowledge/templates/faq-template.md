# FAQ Template

For a collection of question/answer pairs on one theme. The live site's `faq.html` (32 questions, 7 categories) is the existing worked reference for this type, though it predates this formal template.

Copy the block from `metadata-template.md` above this line, with `document_id` using type `FAQ`.

---

# [FAQ Collection Title]

[One or two sentences: what range of questions this collection covers, and for whom.]

## Category: [First category name]

**Q: [Question, phrased exactly as a reader would ask it — see `docs/website-update-spec.md` §7/§15's preference for question-form phrasing]**

A: [Direct answer first, reasoning after. Follow `branding/writing-style.md`'s "lead with the answer" rule. Length target: roughly 60–120 words per answer — long enough to be genuinely useful, short enough to stay scannable, consistent with the existing FAQ's answer length.]

**Q: [Next question in this category]**

A: [Answer.]

## Category: [Next category name]

[Repeat the pattern.]

## Notes for FAQPage schema

[If this FAQ collection will be published to the website with `FAQPage` structured data (as `faq.html` already does), the question text here should match the schema's `Question.name` and the answer text should match `acceptedAnswer.text` exactly — see `docs/website-update-spec.md` §3 and the existing FAQPage JSON-LD block in `faq.html` for the pattern. This section is a reminder to keep the two in sync if this content is ever published that way; it does not itself generate schema.]
