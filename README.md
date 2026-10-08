# CVProMax

> **Career Evidence → Job Match → Application → Interview**

CVProMax is an evidence-first job application skill for AI agents. It helps a candidate build a reusable career profile, compare it against a real job description, ask high-value questions, tailor a CV, write a focused cover letter, research the company, and prepare for interviews.

The defining rule is:

**Never make the candidate look stronger than the evidence allows.**

## What CVProMax does

### 1. Build a Career Profile

Instead of treating every CV as a new document, CVProMax keeps reusable evidence:

- experience
- achievements
- projects
- technical skills
- domains
- leadership
- verified metrics
- preferences
- evidence gaps

### 2. Parse the Job

A job description is normalized into:

- must-haves
- preferred requirements
- responsibilities
- technology
- domain
- seniority
- keywords
- signals
- unknowns

### 3. Match Evidence

Every important requirement becomes:

- **MATCH** — direct evidence
- **ADJACENT** — related evidence
- **GAP** — no supporting evidence
- **UNKNOWN** — insufficient information

This prevents the common "90% match" nonsense where an AI quietly invents experience.

### 4. Ask Better Questions

The Question Engine identifies the few missing facts that can materially improve the application.

Example:

> At Selfapy you mentioned A/B testing. What did you personally own, and what verified result did the experiment produce?

One answer can improve the CV, cover letter, match analysis, and interview preparation.

### 5. Tailor the CV

CVProMax changes:

- relevance
- ordering
- wording
- truthful terminology
- summary
- skills emphasis
- bullet selection

It does not add skills simply because they appear in the JD.

#
## CV Optimizer Engine

The CV mode uses a controlled optimization pipeline:

**JD Requirements → Evidence Mapping → Relevance Decisions → Keyword Mapping → Bullet Rewriting → Tailored CV → Truth/ATS Validation → Change Log**

Every material rewrite can be traced back to candidate evidence and the job requirement it is meant to address.

The optimizer explicitly distinguishes:

- **PROMOTE** — strong, relevant evidence
- **KEEP** — useful supporting evidence
- **COMPRESS** — true but lower-value detail
- **OMIT** — unnecessary for the target role
- **ASK** — valuable evidence that is still unknown

It also distinguishes **EXACT**, **SYNONYM**, **RELATED**, and **UNSUPPORTED** JD terminology, so ATS optimization never becomes keyword invention.

## 6. Write the Cover Letter

The letter connects:

**role need + candidate evidence + verified company context**

It avoids generic "I am passionate about your mission" copy.

### 7. Research the Company

When requested, research can cover:

- company facts
- role details
- salary evidence
- employee sentiment
- reported interview process
- candidate implications

Sources are separated by reliability. Unknown information stays unknown.

### 8. Prepare for Interviews

Preparation is derived from the actual role and the candidate's evidence:

- technical questions
- experience questions
- behavioral questions
- gap questions
- STAR stories
- likely follow-ups

## Core workflow

**DISCOVER → QUESTION → RESEARCH → MATCH → TAILOR → VALIDATE → PACKAGE**

## Truth model

Every material claim is classified internally as:

- FACT
- VERIFIED
- INFERENCE
- HYPOTHESIS
- UNKNOWN

The skill never upgrades uncertainty into fact.

## ATS philosophy

ATS-first means:

- standard headings
- clear chronology
- truthful job terminology
- machine-readable structure
- relevant keyword coverage

It does **not** mean keyword stuffing, hidden text, or deceptive formatting.

## Modes

- **Profile** — build/update the reusable Career Profile
- **Apply** — complete application workflow
- **CV** — tailor the CV to one job
- **Cover Letter** — write a focused letter
- **Research** — investigate a company/role
- **Interview** — prepare for interviews
- **Audit** — validate an application

See [skills/cv-pro-max/SKILL.md](skills/cv-pro-max/SKILL.md) for the complete operating instructions.

## Repository layout

- `skills/cv-pro-max/SKILL.md` — core behavior
- `skills/cv-pro-max/references/` — domain rules and quality gates
- `skills/cv-pro-max/templates/` — reusable application artifacts
- `skills/cv-pro-max/commands/` — explicit command
- `skills/cv-pro-max/cursor-rule/` — Cursor adapter
- `skills/cv-pro-max/codex-prompt/` — Codex adapter
- `tests/` — behavior checks
- `validation/` — repository validation

## Philosophy

A CV is not the product.

**Evidence is the product.**

The CV, cover letter, interview stories, and application decisions are different views of the same verified career evidence.

## License

MIT


## Installation

CVProMax is a markdown-based Agent Skill. It has no runtime, server, or package dependency.

### Agent Skills CLI

```bash
npx skills add bishoy-bishai/CVProMax --skill cv-pro-max
```

### Claude Code plugin

CVProMax ships as a Claude Code plugin:

```bash
claude plugin marketplace add bishoy-bishai/CVProMax
claude plugin install cv-pro-max@cv-pro-max-marketplace
```

Validate a local checkout:

```bash
git clone https://github.com/bishoy-bishai/CVProMax.git
cd CVProMax
claude plugin validate . --strict
```

### Manual installation

Clone the repo:

```bash
git clone https://github.com/bishoy-bishai/CVProMax.git ~/tools/CVProMax
CPVM=~/tools/CVProMax
```

Claude Code, project-scoped:

```bash
mkdir -p .claude/skills .claude/commands
cp -r "$CPVM/skills/cv-pro-max" .claude/skills/cv-pro-max
cp "$CPVM/skills/cv-pro-max/commands/cv-pro-max.md" .claude/commands/
```

Cursor:

```bash
mkdir -p .cursor/rules/cv-pro-max .cursor/commands
cp "$CPVM/skills/cv-pro-max/cursor-rule/cv-pro-max.mdc" .cursor/rules/
cp -r "$CPVM/skills/cv-pro-max/SKILL.md" "$CPVM/skills/cv-pro-max/references" "$CPVM/skills/cv-pro-max/templates" .cursor/rules/cv-pro-max/
cp "$CPVM/skills/cv-pro-max/cursor-rule/commands/cv-pro-max.md" .cursor/commands/
```

Codex CLI:

```bash
mkdir -p ~/.codex/prompts
cp "$CPVM/skills/cv-pro-max/codex-prompt/cv-pro-max.md" ~/.codex/prompts/
```

Other Agent-Skills-compatible clients: copy `skills/cv-pro-max/SKILL.md`, `references/`, and `templates/` into the client's skill/instruction directory. Copy the command file too if the client supports slash commands.

## Usage

After installation, use the explicit commands where supported, or describe the task in natural language.

| Command | Purpose |
|---|---|
| `/cv-pro-max profile` | Build or update the reusable Career Profile |
| `/cv-pro-max apply` | Run the full application workflow |
| `/cv-pro-max cv` | Match and tailor a CV for one job |
| `/cv-pro-max cover-letter` | Write an evidence-backed cover letter |
| `/cv-pro-max research` | Research a company and role |
| `/cv-pro-max interview` | Prepare role-specific interview questions and stories |
| `/cv-pro-max audit` | Audit truth, ATS, relevance, and consistency |

### Example prompts

```text
Build my Career Profile from this CV. Ask only questions that materially improve the evidence.

Tailor my CV for this job. Compare every important requirement against my evidence. Do not invent anything. Show what changed and what remains unknown.

Research this company before I apply. Separate verified facts, salary evidence, employee sentiment, reported interview information, and unknowns.

Write a cover letter using only evidence already established in my Career Profile.

Prepare me for the interview and map every story back to evidence in my Career Profile.
```

### Recommended workflow

1. `/cv-pro-max profile` — build the source-of-truth Career Profile.
2. `/cv-pro-max cv` — paste or attach a target Job Description and tailor the CV.
3. `/cv-pro-max cover-letter` — generate the evidence-backed letter.
4. `/cv-pro-max interview` — prepare questions and STAR stories.
5. `/cv-pro-max audit` — run the final consistency and truth check.

The CV pipeline is:

Job Description → Evidence Mapping → Match → Positioning → Keyword Mapping → Bullet Rewriting → Tailored CV → Validation → Change Log
