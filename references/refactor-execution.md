# Refactor Execution Rules

Use this reference after the user approves the audit report.

## Core Principle

Refactor in bounded, reviewable increments that map back to audit findings. Do not turn the audit into a justification for uncontrolled rewriting.

## Execution Order

1. Resolve Critical and High issues that affect correctness, security, or integrity.
2. Restore or strengthen boundaries before performing cosmetic cleanup.
3. Remove duplication and naming debt after structural risks are under control.
4. Apply optional polish only if it does not distract from the approved scope.

## Change Strategy

Prefer these patterns:
- extract and isolate mixed concerns,
- replace unsafe types with explicit models or validation,
- centralize configuration and constants,
- convert hidden global state into explicit dependencies,
- add focused tests around newly isolated behavior when the repository supports testing.

Avoid these anti-patterns:
- rewriting an entire subsystem without evidence it is necessary,
- changing public behavior incidentally while pursuing style cleanup,
- inventing abstractions that the codebase does not need,
- introducing a new framework or major dependency unless the user asked for it,
- emitting chat-only full-file dumps when in-place repository edits are available.

## Large File Handling

When a file is tangled or oversized:
- identify the stable seams first,
- extract one bounded responsibility at a time,
- update imports and references immediately,
- keep the original file as a thinner coordinator,
- validate after each meaningful extraction.

## Validation Expectations

After edits, run the best available verification in this order when applicable:
1. targeted tests for the changed area,
2. typecheck or compilation,
3. lint or static analysis,
4. a minimal runtime or smoke validation.

If no automated verification is available, explain what was checked manually.

## Refactor Report Contract

Write the execution summary to:

```text
<target-project>/Technical_Reviews/Refactored_YYYY-MM-DD_HH-mm.md
```

Include:
- the audit report path used as input,
- files changed,
- findings resolved,
- deferred items and why they were deferred,
- validation performed,
- residual risks worth keeping visible.
