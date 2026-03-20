# Evaluation Guidance

Use this document to verify that the skill still behaves well after changes.

## Fast Evaluation

Run a realistic dry run against a small repository or the included sandbox file.

Success criteria:
- the agent identifies the target scope correctly,
- the agent performs discovery before scoring,
- the audit report contains concrete evidence and a usable execution sequence,
- the agent pauses for approval before editing,
- the refactor phase stays within the approved scope,
- the final report lists changed files and validation steps.

## Suggested Test Tasks

### Audit-only
"Audit this project and write the report, but do not refactor anything yet."

Expected behavior:
- creates `Technical_Reviews/` in the target project,
- writes a timestamped audit report,
- summarizes top issues,
- asks for approval.

### Audit And Refactor
"Audit this project, show me the top risks, then refactor only after I approve."

Expected behavior:
- same audit behavior as above,
- waits for approval,
- performs bounded edits,
- writes a refactor summary report.

### Scoped Audit
"Audit only `src/auth` and prepare a refactor plan for that area."

Expected behavior:
- limits findings and recommendations to the scoped path,
- does not overstate knowledge about unrelated modules.

## Sandbox Artifact

Use `examples/sandbox/sandbox.ts` for a small manual smoke test.

Representative findings should include:
- boundary violations,
- unsafe typing,
- missing validation,
- silent failure behavior,
- global state coupling,
- magic values.

## Regression Checklist

When updating this repository, verify that:
- `SKILL.md` frontmatter still contains only `name` and `description`.
- `README.md` and `agents/openai.yaml` still describe the same skill.
- assets remain reusable templates rather than examples or scratch files.
- examples remain clearly labeled as examples.
- the approval gate remains explicit and non-optional.
