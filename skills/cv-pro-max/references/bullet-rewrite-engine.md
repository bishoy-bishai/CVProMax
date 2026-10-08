# Bullet Rewrite Engine

## Purpose
Turn raw career evidence into concise, role-relevant CV bullets without changing facts.

## Atomic Fact Extraction
Before rewriting, extract: action, object, ownership, context, technology/method, collaborators, scope, result, metric, timeframe, and evidence source. Anything absent becomes UNKNOWN.

## Rewrite Patterns
### Action-first
Action + object + context + result.

### Technical
Action + technology/method + problem/context + result.

### Ownership
Owned/led/coordinated + verified scope + outcome. Use led only when leadership is explicitly evidenced.

### Collaboration
Collaborated with + verified functions/teams + concrete contribution. Do not convert collaboration into management.

## Transformation Rules
Replace vague actions with the actual evidenced action. Replace filler adjectives with concrete nouns and verbs.

Never replace an unknown result with an invented result, collaboration with leadership, exposure with expertise, or an adjacent technology with an exact technology.

## Before/After Test
For every rewritten bullet ask: Is every factual noun supported? Is ownership unchanged? Is scope unchanged? Is technology supported? Is outcome supported? Did relevance improve? Did any adjective imply a stronger claim than the evidence?
If any answer fails, revise or mark the bullet for review.

## Quality Heuristic
Prefer bullets that make at least two of these clear: action, ownership, technical context, business/product context, outcome.

## Evidence Footer
Internally retain: 
Bullet → evidence_ids → requirement_ids
Do not expose internal IDs in the final CV unless the user asks for an audit.