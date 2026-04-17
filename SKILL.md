---
name: principal-audit-refactor
description: Audit a local software project, produce a severity-ranked engineering review, and execute an approval-gated refactor plan. Use when Codex needs to assess prototype-quality or inconsistent codebases, run stack-aware checks, write timestamped audit artifacts, and then implement production-grade improvements with explicit safety boundaries, report contracts, and refactoring discipline.
metadata:
  dispatcher-layer: execution
  dispatcher-lifecycle: active
  author: jovd83
  version: "1.3.0"
  dispatcher-output-artifacts: audit_report, refactor_plan, refactor_summary
  dispatcher-risk: high
  dispatcher-writes-files: true
  dispatcher-input-artifacts: repository_context, audit_scope, codebase_metrics, approval_state
  dispatcher-capabilities: code-audit, refactor-planning, approval-gated-refactor
  dispatcher-stack-tags: analysis, refactor, engineering-review
  dispatcher-accepted-intents: audit_codebase, plan_refactor, execute_approved_refactor
  dispatcher-category: analysis
---
# Principal Audit & Refactor

Use this skill to turn an unstable or inconsistent repository into a better-structured, safer, more maintainable codebase without collapsing discovery, audit, and mutation into one uncontrolled pass.


## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `python scripts/dispatch_logger.py --skill <skill_name> --intent <intent> --reason <reason>`

## Operating Model

Work in two explicit modes:
1. Audit mode: inspect the target project, run safe deterministic checks, and write an audit report.
2. Refactor mode: only begin after the user explicitly approves the audit findings.

Keep the workflow grounded in the target repository, not the skill repository. Write generated reports into the target project's `Technical_Reviews/` directory.

## Safety Gates

Enforce these gates before mutating code:
- Confirm the target path the user wants audited. Default to the current working directory only when the intent is unambiguous.
- Detect whether the target is inside a git repository. If it is, inspect status before editing. If it is not, continue but explicitly note the lack of version-control safety.
- Do not require a perfectly clean tree to perform an audit. For refactoring, pause if unrelated changes create a real risk of overwriting user work.
- Never invent linter commands. Prefer project-native commands discovered from manifests, scripts, or tool configs. If no reliable deterministic check is available, say so and continue with manual review.
- Stop after writing the audit report and ask for approval. Do not begin implementation in the same phase unless the user has already authorized both audit and refactor work.
- Scope edits to the agreed target. Do not "boil the ocean" unless the user asked for a full-repository pass.

## Workflow

### 1. Establish Scope
- Identify the target repository or subpath.
- Determine whether the user wants an audit only or audit plus refactor.
- Treat audit plus refactor as a two-step workflow with a hard approval gate between them.

### 2. Discover the Environment
- Inspect manifests and build files such as `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `pom.xml`, `build.gradle`, `.csproj`, `Dockerfile`, and CI configs.
- Identify the main languages, frameworks, runtime, package manager, test stack, data layer, and entry points.
- Identify likely high-risk areas: core orchestration, auth, persistence, state management, heavy utility modules, or files already producing warnings.
- Prefer deterministic tooling when available: lint, typecheck, unit tests, static analysis, or build validation.

Read [references/rubric.md](references/rubric.md) once discovery is complete.

### 3. Produce the Audit
- Use [references/report-contract.md](references/report-contract.md) and [assets/audit-report-template.md](assets/audit-report-template.md).
- Write a timestamped audit file in `Technical_Reviews/` at the target project root.
- Include concrete file paths, severity, risk, and recommended action.
- Base severity on evidence from code inspection and any deterministic tool output you were able to run.
- If evidence is incomplete, state the limitation rather than over-claiming.

### 4. Pause for Approval
After saving the audit report:
- summarize the top risks,
- name the report path, and
- ask for explicit approval before editing code.

### 5. Execute the Refactor
Only after approval:
- Read [references/refactor-execution.md](references/refactor-execution.md).
- Refactor by file or bounded subsystem, not by isolated smell.
- Prefer in-place repository edits over chat-only "full file output" unless the user explicitly asks for copy-paste output.
- Preserve behavior unless the audit explicitly calls for a behavioral fix.
- Add or update tests when the repository already has a testing story and the change materially benefits from coverage.
- Write a timestamped execution summary using [assets/refactor-report-template.md](assets/refactor-report-template.md).

## Output Contracts

### Audit report
Must include:
- project name or scoped target,
- timestamp,
- detected stack,
- deterministic checks run and their outcomes,
- prioritized findings with severity,
- maintainability score with a clear scoring rule,
- recommended refactor sequence,
- explicit open questions or blocked areas.

### Refactor report
Must include:
- audit report reference,
- files changed,
- resolved findings,
- follow-up work intentionally left out of scope,
- validation performed after edits.

## Memory Model

Use memory deliberately:
- Runtime memory: current findings, tool output, and the active refactor plan for this run only.
- Project-local memory: persisted audit and refactor reports written into `Technical_Reviews/` in the target repository.
- Shared memory: out of scope for this skill. If cross-project reuse is needed, integrate with a separate shared-memory skill instead of storing shared memory here.

Do not automatically promote runtime observations into persistent artifacts unless they are useful to the user or needed for traceability.

## Failure Handling

If the workflow becomes unreliable, degrade gracefully:
- Missing repo metadata: continue with manual discovery and note the limitation.
- Missing or broken tooling: capture the failure, avoid guessing commands, continue with review.
- Large or tangled files: split work into bounded extractions before deeper cleanup.
- Unsafe ambiguity about intent or target path: pause and confirm before editing.
- Conflicts with user changes: stop and ask before overwriting.

## Gotchas

Watch out for these common friction points:
- **Root Ambiguity**: In monorepos, the skill might default to the root. Always clarify if the audit should be scoped to a specific package or directory.
- **Context Window Limits**: For very large repositories or files, the agent may not see the full context in a single pass. Consider splitting large audits into subsystems.
- **Generated Artifacts**: Ensure you are auditing source code and not generated files (e.g., `dist/`, `build/`, `node_modules/`).
- **Tooling Hallucination**: If native test/lint scripts are missing, strictly report the gap rather than inventing commands to simulate a "deterministic" check.
- **State Drift**: If the user makes manual edits after an audit but before a refactor, the audit results may become stale. Briefly re-verify critical files before mutating.

## Resource Map
- Rubric: [references/rubric.md](references/rubric.md)
- Report contract: [references/report-contract.md](references/report-contract.md)
- Refactor execution rules: [references/refactor-execution.md](references/refactor-execution.md)
- Evaluation guidance: [references/evaluation.md](references/evaluation.md)
- Audit template: [assets/audit-report-template.md](assets/audit-report-template.md)
- Refactor template: [assets/refactor-report-template.md](assets/refactor-report-template.md)
- Example prompts and sandbox: `examples/`
