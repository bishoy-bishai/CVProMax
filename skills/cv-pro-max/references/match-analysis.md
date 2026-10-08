# Match Analysis

Match Analysis explains how the candidate's evidence maps to a specific role.

## Requirement record

For each important requirement capture:

| Field | Meaning |
|---|---|
| Requirement | Exact or normalized JD requirement |
| Priority | Must / Preferred / Signal |
| Status | MATCH / ADJACENT / GAP / UNKNOWN |
| Candidate Evidence | Concrete supporting experience |
| Evidence Source | CV / project / answer / verified source |
| Confidence | High / Medium / Low |
| Positioning | How to represent it truthfully |
| Question | Missing information, if any |

## Status rules

### MATCH
Use only when the candidate has direct, credible evidence.

### ADJACENT
Use when the candidate has related experience but the requirement is not equivalent.

### GAP
Use when available evidence indicates the candidate does not have the requirement.

### UNKNOWN
Use when the profile is insufficient to decide.

Never turn UNKNOWN into MATCH because the candidate is senior.

## Requirement hierarchy

Prioritize:
1. Explicit must-haves
2. Core responsibilities
3. Repeated technical requirements
4. Seniority/ownership requirements
5. Preferred skills
6. Generic soft skills

## Match summary

A good summary answers:
- What makes the candidate credible for this role?
- What are the strongest differentiators?
- Which requirements are weak?
- Which unknowns should be resolved?
- What should change in the CV?

## Scoring

The score is a positioning aid, not a hiring probability.

Default weights:
- must-have technical: 30%
- relevant experience/domain: 25%
- responsibilities/ownership: 20%
- seniority/leadership: 10%
- preferred requirements: 10%
- education/certification: 5%

Evidence strength:
- 1.0 direct
- 0.7 adjacent
- 0.3 weak
- 0.0 gap
- N/A unknown

Always show the evidence behind a score.

## Example

Requirement: Design systems

Status: MATCH

Evidence: Candidate built and maintained reusable shared UI components and a design system.

Positioning: Put design-system ownership in the recent experience section and mention reusable component architecture.

Requirement: FinTech

Status: ADJACENT

Evidence: Candidate has relevant financial-product exposure but no verified direct FinTech role.

Positioning: Use the transferable product/technical experience without claiming FinTech expertise.


## 6. Deterministic Scoring Procedure

Create one row per scored dimension.

| Dimension | Weight | Score | Evidence |
|---|---:|---:|---|
| Must-have technical | 30 | 0–1 | Requirement rows |
| Relevant experience/domain | 25 | 0–1 | Experience evidence |
| Responsibilities/ownership | 20 | 0–1 | Ownership evidence |
| Seniority/leadership | 10 | 0–1 | Scope evidence |
| Preferred requirements | 10 | 0–1 | Requirement rows |
| Education/certification | 5 | 0–1 | Verified records |

Calculate:

Weighted Match = Σ(dimension score × weight).

Unknown handling:
- UNKNOWN is not silently converted to zero when evidence is genuinely unavailable.
- Report the score as provisional when one or more high-weight dimensions contain material UNKNOWN evidence.
- If a numeric decision aid is requested despite unknowns, calculate an observed-evidence score and separately report unknown coverage.

Status-to-score defaults:
- MATCH = 1.0
- ADJACENT = 0.7
- WEAK = 0.3
- GAP = 0.0
- UNKNOWN = N/A

Requirement weighting:
- Explicit must-have: highest priority.
- Repeated technical requirement: next.
- Core responsibility: next.
- Preferred: lower.
- Generic soft skill: lowest.

## 7. Coverage Metrics

Report:
- Must-have coverage = direct MATCH must-haves / total must-haves.
- Evidence coverage = requirements with MATCH or ADJACENT evidence / scored requirements.
- Unknown rate = UNKNOWN requirements / total requirements.
- High-risk gaps = must-haves classified GAP.
- High-risk unknowns = must-haves classified UNKNOWN.

Do not present these metrics as hiring probability.

## 8. Decision Rules

Recommend:
- Strong fit: no high-risk must-have gaps and most must-haves are MATCH.
- Plausible fit: core role is credible but has material ADJACENT or UNKNOWN requirements.
- Stretch fit: multiple core requirements are ADJACENT/GAP but transferable evidence is credible.
- Weak fit: one or more critical must-haves are unsupported or contradicted.

The final recommendation must explain which requirements drove it.
