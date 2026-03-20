# Audit And Report Contract

Use this contract when writing audit artifacts to the target repository.

## File Location

Write audit reports to:

```text
<target-project>/Technical_Reviews/Audit_YYYY-MM-DD_HH-mm.md
```

Create `Technical_Reviews/` if it does not already exist.

## Required Sections

### Title
Use:

```text
# Refactoring Roadmap: <project-or-scope-name>
```

### Metadata
Include:
- timestamp,
- target path,
- execution mode: full repository or scoped path,
- detected stack,
- deterministic checks attempted and their status.

### Executive Summary
Provide:
- maintainability score,
- a short state-of-the-union summary,
- the top 3 risks in descending priority.

### Architecture Snapshot
Describe:
- entry points,
- main layers or subsystems,
- hot files or hot paths,
- important constraints or unknowns.

### Findings Table
Use a consistent table with these columns:

| Location | Severity | Smell Detected | Risk | Recommended Fix |
| :--- | :--- | :--- | :--- | :--- |

Rules:
- `Location` should use a file path, subsystem, or both.
- `Smell Detected` should name the issue category clearly.
- `Risk` should explain why the issue matters operationally.
- `Recommended Fix` should be actionable and scoped.

### Refactor Sequence
List the proposed execution order. Prefer a short numbered list ordered by dependency and risk.

### Open Questions Or Blockers
Capture ambiguity, missing tooling, or areas that need user confirmation before mutation.

## Writing Rules

- Keep the report evidence-based and specific.
- Prefer concrete engineering language over rhetorical phrasing.
- Do not describe the entire codebase when only a scoped path was audited.
- If deterministic checks failed to run, record the failure and continue with manual review.
- If the repository is not under git, mention that the audit was performed without version-control safety.
