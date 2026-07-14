# GOV-001: Research and Intellectual Property Policy

**Status:** Approved v1.0  
**Effective:** 2026-07-14  
**Owner:** Founder / Chief Knowledge Architect  
**Supersedes:** Verbal directives; first formalized record

---

## Purpose

Enaasan's long-term reputation depends on trust and originality. This policy ensures that every Knowledge Card, Publication, Guide, and educational artifact is:

1. **Evidence-grounded** — claims are verified against authoritative sources
2. **Original** — written in Enaasan's voice, not derived from existing publications
3. **IP-compliant** — respects copyright, attribution, and licensing
4. **Legally defensible** — could withstand editorial review, academic scrutiny, copyright review, and legal due diligence

This policy is not a constraint on knowledge creation; it is a foundation for sustainable, trusted knowledge work.

---

## Research Principles

### Verification is Mandatory

Every load-bearing claim in a published Knowledge Card or Publication SHALL be:

- **Supported by an authoritative source** — peer-reviewed research, government publications, official statistics, academic papers, or recognized institutional data
- **Verified against the original publication** — not quoted from secondary sources; the primary source is read and confirmed
- **Traceable** — the source is named and linked in `evidence_notes` and the card's references section
- **Current** — sources are checked for updates; if stronger, more recent sources exist, they replace weaker ones

### If Evidence Cannot Be Verified

- **Remove the claim.** Do not weaken the standard by allowing unverified claims into published work.
- **Rewrite the card.** If the core claim cannot be verified, the card's entire argument may need restructuring.
- **Document the uncertainty.** If a claim is probable but unverifiable, it does not belong in load-bearing content; it may belong in a `voice` publication (dated, transparent about its non-authoritative status) or in the `uncertainty` field as "we believe this but have not verified it."

### Illustration and Modeling are Distinct from Evidence

- **Illustrative content** (worked examples, composite scenarios) must be labeled as such in both metadata (`evidence: anecdotal`) and body text ("these are composite illustrations constructed from real salary bands, not case studies")
- **Modeling** (inferred tables, calculated ranges) must be labeled as "modeled" in the body, not presented as "based on analysis of"
- **Neither illustrative nor modeled content is load-bearing.** The card's evidence rating is determined by its load-bearing claims alone.

---

## Intellectual Property & Copyright

### Original Voice is Required

Every Knowledge Card, Publication, Guide, and educational artifact SHALL be written in **Enaasan's original voice**:

- **Use sources to understand deeply.** Read widely; understand the subject thoroughly.
- **Write originally.** Compose new sentences that express the learning in Enaasan's voice and pedagogy.
- **Do not paraphrase closely.** Rewriting a paragraph with different words but the same structure and argument is still plagiarism.
- **Do not reproduce structure.** A guide that follows the same outline and reasoning as an existing publication, even with different words, is derivative work.

### Quotation is Minimal and Attributed

- **Quotations are rare.** Use them only when the original author's exact wording is necessary — e.g., a memorable definition, a precise statistical finding that cannot be better expressed, or a direct claim that needs to be attributed.
- **Quotations are brief.** Never more than a few sentences. Long quotations should be reconsidered as "do we need the author's exact words, or can we express this more briefly in our own voice?"
- **Quotations are attributed.** Every quotation includes a clear, immediate attribution: source, author, date, and optionally a page number.
- **Quotations are marked.** Use quotation marks or block formatting so the reader knows which text is quoted vs. original.

### Attribution Standards

Every Knowledge Card or Publication that draws from published research SHALL include:

- **Evidence Notes**: named sources ("NASSCOM BPS Report 2024-25," "Glassdoor salary data analysis 500+ roles," "25+ recruiter interviews")
- **References section**: full citations of sources, with links where available
- **Canonical source comments**: for embedded content, `<!-- canonical: <object-id> -->` markers ensuring the reader can trace every claim

### Licensing and Media Assets

- **Images, graphics, icons, datasets:** Confirm the license before use. Do not include copyrighted assets unless the license explicitly permits their use for educational or commercial purposes.
- **When in doubt, exclude it.** If licensing status is uncertain, do not include the asset. Document the exclusion and the licensing uncertainty instead.
- **Default license for Enaasan content:** All Knowledge Cards and Publications are licensed under the terms stated in the `license` metadata field (default: free to read, download, and share for personal and educational use; not for resale or republication).

---

## Editorial Review Gate

The review process includes an **IP check**:

1. **Reviewer reads the card** for original voice and originality of expression
2. **Reviewer spot-checks sources** — particularly load-bearing claims — against originals
3. **Reviewer verifies attributions** — every source named in `evidence_notes` and references is real and correctly cited
4. **Reviewer checks for quotations** — confirms they are minimal, attributed, and necessary
5. **Reviewer confirms licenses** — all media assets have been checked; licensing status is clear or asset is excluded

A card does not pass review if:
- It reproduces or closely paraphrases existing work
- Its claims are unverified
- Its sources are misattributed or incorrect
- Its quotations are too long or improperly attributed
- It includes unlicensed media

---

## The Long-Term Standard

Assume that every Enaasan Knowledge Card, Publication, and Guide may eventually:

- Become part of a published book
- Be translated into multiple languages
- Be used in academic curricula
- Be cited in policy or business contexts
- Be reviewed by external editors, academics, or legal counsel

Write every artifact to that standard:

- **Editorial review worthy** — original, clearly sourced, properly attributed
- **Academically defensible** — claims are supported; reasoning is transparent; uncertainty is disclosed
- **Copyright-clean** — no infringement, proper attribution, clear licensing
- **Legally robust** — no claims that could expose Enaasan to liability; clear disclaimer where needed

**If there is any doubt about copyright, attribution, licensing, or permissible use, choose the more conservative approach and document the issue.**

---

## Consequences of IP Violations

IP violations are treated seriously:

- **First-time minor violation** (e.g., inadequate attribution) → education + correction
- **Repeated violations or serious breaches** (e.g., substantial plagiarism, unlicensed media) → removal from publication + investigation
- **Deliberate copyright infringement** → disqualification from contributing; potential legal escalation

Enaasan's reputation depends on trust. IP violations undermine that trust and may expose the organization to legal risk.

---

## Questions & Clarity

**Q: What if a source's exact phrasing is the best way to express the idea?**  
A: Still paraphrase. The source's wording is copyrighted; your paraphrase is not. If the source's wording is truly irreplaceable, quote it briefly and attribute it.

**Q: Can I adapt an existing guide's structure if I rewrite every sentence?**  
A: No. Structure is also intellectual property. If the outline, argument flow, and reasoning sequence are identical, it's derivative work even if words differ.

**Q: What about common knowledge or facts?**  
A: Facts are not copyrighted. "The population of India is 1.4 billion" can be stated without quotation or attribution. But the *analysis* of that fact, the *interpretation*, the *contextualization* — these are creative work and may be copyrighted. Attribute when in doubt.

**Q: How do I verify a source if I can't access it directly?**  
A: Do not cite it. Find a source you can access. If the claim is important but unverifiable, remove it or move it to the uncertainty field.

**Q: What if a source is behind a paywall?**  
A: Cite it and note that it is paywalled. If the claim is load-bearing and you cannot verify it, remove it or rewrite the card to rest on accessible sources.

---

## Document History

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0 | 2026-07-14 | Initial policy: verification mandatory, original voice required, quotation minimal, attribution clear, licensing checked, long-term standard applied, consequences defined | Founder / Chief Knowledge Architect |
