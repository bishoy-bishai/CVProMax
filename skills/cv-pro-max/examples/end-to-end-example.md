# CVProMax End-to-End Example

> Synthetic example for regression testing. All candidate and company details below are fictional.

## Candidate Evidence
- Senior Frontend Engineer at ExampleCo, 2023–2026.
- Built customer-facing React and TypeScript workflows.
- Maintained a reusable shared UI component library.
- Collaborated with product and design.
- React Query is not present in the candidate evidence.
- No verified conversion metric is available.

## Job Description
- Senior Frontend Engineer.
- Must have React and TypeScript.
- Must have experience with design systems.
- Must have React Query.
- Preferred: Next.js.
- Responsibilities include collaboration with product and design.

## Expected Requirement Mapping

| Requirement | Status | Evidence |
|---|---|---|
| React | MATCH | React customer-facing workflows |
| TypeScript | MATCH | TypeScript customer-facing workflows |
| Design systems | MATCH | Reusable shared UI component library |
| React Query | UNKNOWN | No evidence either way |
| Next.js | UNKNOWN | No evidence either way |
| Product/design collaboration | MATCH | Explicit collaboration evidence |

## Expected Positioning
- Promote React, TypeScript, design-system, and collaboration evidence.
- Ask about React Query because it is a must-have and currently UNKNOWN.
- Do not claim React Query.
- Do not invent a conversion metric.
- Do not claim Next.js unless the candidate supplies evidence.

## Expected Keyword Mapping
- React → EXACT.
- TypeScript → EXACT.
- design systems → EXACT or truthful equivalent based on source wording.
- React Query → UNSUPPORTED until evidence is provided; operationally treated as UNKNOWN at requirement level.
- Next.js → UNSUPPORTED until evidence is provided.

## Expected CV Change Log
- Promote design-system ownership.
- Promote React/TypeScript work.
- Preserve collaboration wording without turning it into management.
- No invented metrics.
- Add an ASK item for React Query.

## Expected Validation
- Truth: PASS.
- ATS structure: PASS if standard headings and terminology are used.
- Relevance: PASS with React/design-system evidence promoted.
- Human: PASS if wording remains specific and concise.
- Consistency: PASS.
- Application readiness: BLOCKED only if the user requires a definitive answer on React Query before finalizing.