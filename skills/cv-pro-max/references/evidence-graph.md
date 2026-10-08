# Evidence Graph

The Evidence Graph is the internal model connecting candidate evidence to job requirements and generated application claims.

## Nodes

### Candidate Evidence
Examples:
- employment experience
- achievement
- project
- skill
- domain exposure
- leadership example
- metric
- education

### Job Requirement
Examples:
- React
- TypeScript
- design systems
- ownership
- fintech experience

### Application Claim
A sentence or bullet proposed for:
- CV
- cover letter
- interview answer

### Source
The origin of the evidence:
- candidate CV
- candidate answer
- project documentation
- official company page
- external research source

## Edges

Use these relationships:

- SUPPORTS — evidence directly supports requirement.
- PARTIALLY_SUPPORTS — evidence is relevant but incomplete.
- CONTRADICTS — evidence conflicts with the claim.
- DERIVED_FROM — claim was generated from evidence.
- VERIFIED_BY — external fact verified by source.
- NEEDS_EVIDENCE — requirement or claim lacks sufficient support.

## Example

Candidate Evidence:
"Built reusable shared UI components."

→ SUPPORTS →

Job Requirement:
"Experience building design systems."

Classification:
MATCH, if the candidate evidence clearly establishes design-system scope.

Otherwise:

Classification:
ADJACENT, because reusable components alone do not automatically prove ownership of a complete design system.

## Claim generation rule

Every material generated claim should be traceable:

Application Claim
→ DERIVED_FROM
→ Candidate Evidence
→ Source

If the chain cannot be established, do not present the claim as fact.

## Evidence graph workflow

1. Extract candidate evidence.
2. Normalize evidence into atomic records.
3. Extract job requirements.
4. Link evidence to requirements.
5. Classify relationship strength.
6. Identify missing evidence.
7. Ask Question Engine questions.
8. Recompute links after answers.
9. Generate application claims only from supported nodes.
10. Validate generated claims against the graph.

## Atomic evidence rule

Do not store a vague paragraph as one giant evidence node.

Split:

"Led the migration, created the component library, mentored engineers, and reduced duplication."

into separate evidence records when the source supports them:

- migration ownership
- component-library work
- mentoring
- duplication reduction

This makes matching and truth validation more precise.
