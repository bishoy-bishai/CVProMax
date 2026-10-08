# Question Engine

The Question Engine is the main anti-fabrication and information-gain mechanism.

## Goal

Ask the smallest number of questions that can materially improve the application.

## Question lifecycle

1. Parse the Job Description.
2. Identify high-value requirements.
3. Map each requirement to candidate evidence.
4. Mark unsupported or ambiguous requirements as UNKNOWN.
5. Identify missing evidence that could change positioning.
6. Rank candidate questions.
7. Ask a small batch.
8. Incorporate answers into the Career Profile and Evidence Ledger.
9. Re-run matching.
10. Stop when additional questions have low expected value.

## Priority model

Score a candidate question from 1–5 on:

- Relevance: how important is the related requirement?
- Evidence impact: could the answer change MATCH/ADJACENT/GAP/UNKNOWN?
- Reusability: could the answer strengthen several bullets, letters, or interview stories?
- Credibility impact: would it replace a vague claim with concrete evidence?

A simple priority score is:

Question Value = Relevance × Evidence Impact × Reusability

Use credibility impact as a tie-breaker.

## Question classes

### Requirement evidence
"Have you used React Native professionally? If yes, where and what did you personally own?"

### Impact evidence
"You mentioned reducing duplicated UI work. What changed afterward, and do you have a verified metric?"

### Scope evidence
"How many engineers or teams consumed the component library?"

### Seniority evidence
"Were you responsible for the technical direction, implementation, reviews, or all three?"

### Domain evidence
"Which part of the product involved payments, identity, banking, telecom, or another relevant domain?"

### Motivation evidence
"What specifically attracted you to this role?"

Only ask motivation questions when the answer will materially improve the application.

## Batch policy

Default: 3–7 questions.

Ask fewer when:
- the CV is already strong;
- only one unknown blocks the application;
- the user asks for a quick draft.

Ask more only when:
- the user requests a deep profile interview;
- building a reusable Career Profile for future applications.

## Good vs bad questions

Good:
"At Selfapy you mentioned A/B testing. What did you personally own, and what verified result did the experiment produce?"

Why: it can improve ownership, impact, and experimentation evidence.

Bad:
"What was your favorite part of the project?"

Why: low information value unless the target role explicitly asks for motivation.

## Answer handling

When the user answers:
- record the answer as FACT if it is first-party candidate evidence;
- preserve exact numbers;
- do not embellish;
- update the relevant achievement/evidence record;
- re-run affected requirement matches.

If the answer is still vague, ask one focused follow-up rather than inventing detail.

## Stop conditions

Stop asking when:
- all material must-haves have a defensible status;
- high-value achievements have enough evidence;
- remaining UNKNOWN items are low impact;
- the user asks to proceed;
- further questions would mainly polish wording rather than change substance.
