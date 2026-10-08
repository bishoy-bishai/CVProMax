# ATS Validation

## Purpose
Validate ATS compatibility through observable document properties. Do not claim compatibility with a specific vendor parser unless that parser was actually tested.

## Structural Checks
Prefer standard headings, clear employer/title/date relationships, chronological ordering, plain text for critical information, conventional bullets, and consistent date formats.

Avoid critical information only in images, decorative shapes, untested multi-column layouts, unusual section names, excessive icons, essential information only in headers/footers, and hidden keywords.

## Content Checks
Verify truthful target terminology, visible must-have matches, accurate titles and dates, supported skills, no keyword stuffing, and no duplicate keyword blocks.

## ATS Evidence Levels
### Level A — Structural
Parser-friendly conventions are followed.

### Level B — Content
Relevant truthful terminology is represented.

### Level C — Tested
The document was actually parsed with a named ATS/parser and the result is available.

Only Level C permits claims about observed parser behavior.

## ATS Validation Output
Return structural status, content status, unsupported constructs, keyword coverage, unresolved risks, and test evidence if Level C.

Never output a fake ATS score.