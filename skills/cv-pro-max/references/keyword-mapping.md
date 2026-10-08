# Keyword Mapping

## Purpose
Map Job Description terminology to truthful candidate evidence. Keyword optimization is a semantic mapping problem, not keyword stuffing.

## Mapping Classes
| Class | Meaning | CV Usage |
|---|---|---|
| EXACT | Same term is supported | Use naturally |
| SYNONYM | Standard equivalent is supported | Use the clearest term |
| RELATED | Nearby concept but not equivalent | Do not present as exact |
| UNSUPPORTED | No evidence | Do not use |

## Mapping Record
Each important keyword should have: keyword, JD context, requirement_id, class, evidence_ids, proposed wording, confidence, and decision.

## Rules
1. Prefer the exact JD term when genuinely evidenced.
2. Prefer standard industry terminology over awkward paraphrases.
3. Never introduce a technology because it appears in the JD.
4. Never convert a related framework into an exact framework.
5. Do not repeat a keyword merely to increase frequency.
6. A keyword without evidence is an exclusion candidate.
7. If eligibility depends on unknown evidence, route it to the Question Engine.

## Example
JD: Experience with React Query and TypeScript.

If both are explicitly evidenced, both are EXACT.
If only React and TypeScript are evidenced, React Query is UNSUPPORTED and must not be added.
If TanStack Query is explicitly evidenced, treat it as SYNONYM only when the source clearly establishes the equivalence.

## Keyword Coverage Report
Return high-priority keywords covered, exact evidence, synonymous evidence, related terms, unsupported terms, and unknown terms.

Distinguish not mentioned from not possessed.