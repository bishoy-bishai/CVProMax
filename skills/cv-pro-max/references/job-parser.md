# Job Description Parser

The Job Parser converts an unstructured job description into a normalized requirement model.

## Extraction order

1. Role identity
2. Seniority
3. Location and work model
4. Responsibilities
5. Must-have requirements
6. Preferred requirements
7. Technical stack
8. Domain requirements
9. Leadership/collaboration signals
10. Keywords
11. Application constraints
12. Unknowns

## Requirement extraction

For every requirement capture:

| Field | Description |
|---|---|
| ID | Stable local identifier |
| Text | Original wording |
| Normalized | Short normalized requirement |
| Type | Technical / Domain / Responsibility / Leadership / Education / Soft skill |
| Priority | Must / Preferred / Signal |
| Evidence needed | What would prove it |
| Notes | Ambiguity or interpretation |

## Must-have detection

Treat a requirement as Must only when:
- the JD explicitly says required, must-have, minimum, or equivalent;
- the wording clearly makes it a hiring prerequisite.

Do not turn every bullet under "Requirements" into an equally hard blocker.

## Responsibility extraction

Responsibilities are not automatically skills.

Example:

"Own frontend architecture decisions."

This is primarily an ownership/architecture requirement.

"Experience with React."

This is a technical skill requirement.

## Signal extraction

Signals are recurring patterns that indicate what the employer values.

Examples:
- repeated references to collaboration;
- emphasis on ownership;
- repeated mention of experimentation;
- repeated mention of design systems.

Signals influence positioning but must not be treated as mandatory unless explicitly required.

## Keyword extraction

Extract:
- exact tools;
- frameworks;
- domain terms;
- role titles;
- recurring concepts;
- methodologies.

Then classify each against candidate evidence:
- exact supported;
- truthful synonym;
- related;
- unsupported.

## Ambiguity handling

If wording is ambiguous, preserve the original wording and mark the normalized interpretation as INFERENCE.

Never silently reinterpret an ambiguous requirement as a fact.
