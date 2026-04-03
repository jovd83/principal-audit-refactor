# Changelog

All notable changes to `principal-audit-refactor` are documented here.

The format follows Keep a Changelog and uses semantic versioning where practical for a skill repository.

## [1.2.0] 2026-04-03

### Added
- "Gotchas" section to `SKILL.md` to highlight common friction points like monorepo roots, context window limits, and state drift.
- Version, License, and "Buy Me a Coffee" badges to `README.md`.

## [1.1.0] 2026-03-19

### Added
- `agents/openai.yaml` for UI-facing skill metadata.
- MIT `LICENSE` and GitHub community health files.
- Modular reference documents for the rubric, report contract, execution rules, and evaluation guidance.
- Separate audit and refactor report templates.
- `examples/` structure for legacy prompts and a sandbox artifact.
- Lightweight repository validation script and GitHub Actions workflow.
- Forward-test evidence for the sandbox audit flow.

### Changed
- Rewrote `SKILL.md` around explicit safety gates, approval boundaries, output contracts, and a scoped memory model.
- Rewrote `README.md` to be publishable, installation-friendly, and explicit about scope and architecture.
- Upgraded the rubric to use clearer severity guidance and more actionable review categories.
- Reframed repository assets so templates, references, and examples each have a distinct responsibility.

### Fixed
- Removed non-standard frontmatter fields from `SKILL.md`.
- Corrected inconsistent terminology around rubric dimensions, report behavior, and refactor execution.
- Replaced vague or unsafe instructions that encouraged invented tooling, uncontrolled edits, or copy-paste-only workflows.

## [1.0.0] - 2026-03-17

### Added
- Initial public release of the Principal Audit & Refactor skill.
