# CV Optimizer Engine

## Purpose
The CV Optimizer converts a reusable Career Profile into a role-specific CV without changing the underlying truth.

It is a controlled transformation pipeline:
Job Requirements → Evidence Mapping → Relevance Decisions → Positioning → Bullet Rewriting → Keyword Alignment → Validation → Change Log

The optimizer must preserve evidence provenance for every material claim.

## 1. Optimization Contract
The optimizer may change: wording, ordering, emphasis, section selection, bullet length, truthful terminology, summary positioning, and skills ordering.

The optimizer must not change: employment dates, employers, unsupported technologies, ownership level, metrics, scope, seniority, education, certifications, or domain experience.

## 2. Inputs
Required: Career Profile and normalized Job Description.
Preferred: Evidence Ledger, Achievement Bank, and Question Engine answers.
If required inputs are missing, invoke the Question Engine rather than filling gaps.

## 3. Evidence Mapping
Create one mapping record for every important requirement.

| Field | Meaning |
|---|---|
| requirement_id | Stable requirement identifier |
| requirement | Normalized JD requirement |
| priority | Must-have / preferred / signal |
| evidence_ids | Supporting Career Profile evidence |
| status | MATCH / ADJACENT / GAP / UNKNOWN |
| confidence | HIGH / MEDIUM / LOW |
| target_section | Where it should appear |
| target_claim | Truthful wording candidate could use |
| decision | PROMOTE / KEEP / COMPRESS / OMIT / ASK |

Evidence selection order: direct verified evidence; direct candidate evidence; closely related evidence; transferable evidence; no evidence.
Never use a lower-ranked evidence class to overwrite a stronger contradiction.

## 4. Relevance Decision Engine
For each experience bullet or achievement, assess requirement coverage, role similarity, technical relevance, ownership relevance, outcome strength, recency, and evidence confidence.

Classify each item:
- PROMOTE — high relevance and strong evidence.
- KEEP — useful supporting evidence.
- COMPRESS — true and useful but low-value for this role.
- OMIT — not useful for the target role or consumes scarce space.
- ASK — potentially valuable but evidence is incomplete.

Omission from the tailored CV is not deletion from the Career Profile.

## 5. Relevance Budget
Default priority:
1. Must-have requirements with direct evidence.
2. Core responsibilities with direct evidence.
3. Strong quantified achievements.
4. Relevant domain experience.
5. Preferred requirements.
6. Supporting technologies.
7. Older or weakly relevant detail.

Do not force every JD keyword into the CV.

## 6. Bullet Rewrite Algorithm
For every selected bullet: extract original facts; identify ownership; identify technical/context detail; identify outcome; identify relevant JD terminology; build a truthful sentence; remove filler; compare against original; record supporting evidence IDs.

Preferred structure: Action + what/context + method/technology + result.

Only add a result when the result is evidenced.

## 7. Keyword Alignment
For every important JD term classify it as EXACT, SYNONYM, RELATED, or UNSUPPORTED.

Use EXACT terminology when truthful and natural. Do not transform RELATED into EXACT. Do not add a keyword merely because it is ATS-friendly.

## 8. Summary Optimization
The summary should answer what the candidate is, strongest relevant experience, relevant technical/domain strengths, and differentiation.

Default length: 2–4 sentences. Every material claim must be traceable to evidence.

Avoid generic passion statements, unsupported years, fake specialization, company-specific flattery, and keyword lists disguised as prose.

## 9. Experience Selection
Preserve accurate employer/title/date. Select the highest-value evidence. Put strongest relevant bullets first. Compress repetitive bullets. Remove low-value detail only from the tailored artifact.

## 10. Skills Optimization
Skills are evidence labels, not wish lists. Use technologies explicitly evidenced by experience or projects. Prioritize truthful high-priority JD requirements.

## 11. Page and Density Control
If a page limit exists: remove redundant prose, compress low-relevance bullets, remove weak or duplicate skills, reduce older-role detail, then reduce summary length. Never remove a high-value requirement match solely for decorative whitespace.

## 12. Final CV Validation
### Evidence
Every material claim has evidence; metrics are unchanged; technologies are supported; ownership is not inflated.

### Match
Important requirements have a visible truthful status; strong matches are prominent; gaps are not disguised.

### ATS
Standard headings; clear dates and titles; natural JD terminology; no hidden keywords; no keyword stuffing; no parser-hostile structure.

### Human
Concise, specific, natural, non-repetitive, and free of generic AI phrasing.

## 13. Required Optimizer Output
Return:
1. Optimization verdict.
2. Requirement coverage table.
3. Key positioning decisions.
4. Tailored CV.
5. Change Log.
6. Unsupported or unknown requirements.
7. Validation report.

Never report a numeric ATS score unless an actual ATS/parser evaluation was performed.

## 14. Change Log Contract
Every material change records: change_id, section, original, revised, reason, evidence_ids, requirement_ids, risk, validation_status.

Risk: LOW = wording/order only; MEDIUM = meaningful reframing; HIGH = claim could materially change perceived scope and requires explicit evidence review.

## 15. Stop Conditions
Do not finalize when a high-impact claim has unresolved evidence, a requested requirement depends on unknown candidate information, the rewrite changes scope or ownership, or dates/titles conflict. Show the blocker and ask the smallest useful question.