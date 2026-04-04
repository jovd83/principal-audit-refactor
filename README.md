# Principal Audit & Refactor

[![Validate Skills](https://github.com/jovd83/principal-audit-refactor/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/jovd83/principal-audit-refactor/actions/workflows/validate-skills.yml)
[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](https://github.com/jovd83/principal-audit-refactor/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)


`principal-audit-refactor` is an Agent Skill for auditing a local codebase, producing an evidence-backed engineering review, and executing an approval-gated refactor plan.

It is designed for AI coding agents that need a disciplined way to upgrade prototype-quality repositories into safer, cleaner, more maintainable systems without skipping discovery, over-editing, or mixing audit and mutation into one uncontrolled pass.


## What This Skill Is Responsible For

This skill handles:
- repository and stack discovery,
- deterministic technical checks when reliable commands exist,
- severity-ranked audit reporting,
- a hard approval gate before mutation,
- bounded refactor execution tied back to audit findings,
- traceable audit and refactor artifacts written into the target project.

This skill does not provide:
- cross-project shared memory infrastructure,
- universal lint or build scripts for every stack,
- autonomous self-modifying behavior,
- speculative repo frameworks that are not needed by the target project.

## Why It Exists

Many audit prompts are strong on tone and weak on operating discipline. This repository packages the workflow into a reusable skill with:
- explicit safety rules,
- modular reference material,
- report contracts instead of vague narrative,
- a clear memory model,
- examples and evaluation guidance for maintainers.

## Installation

### CLI

```bash
npx skills add jovd83/principal-audit-refactor
```

The general install syntax is `npx skills add <owner>/<repo>` according to the public Agent Skills CLI documentation.

### Manual

Clone or copy this folder into a local skills directory supported by your agent tooling, for example:

```text
~/.agents/skills/
~/.cursor/skills/
```

## Repository Layout

```text
SKILL.md
README.md
CHANGELOG.md
SECURITY.md
LICENSE
.github/
  ISSUE_TEMPLATE/
  pull_request_template.md
  workflows/
    validate-skills.yml
agents/
  openai.yaml
assets/
  audit-report-template.md
  refactor-report-template.md
examples/
  forward-tests/
  prompts/
  sandbox/
references/
  evaluation.md
  refactor-execution.md
  report-contract.md
  rubric.md
scripts/
  validate_skill.py
```

## Workflow Summary

1. Establish the target scope.
2. Discover the stack, architecture, and deterministic validation options.
3. Evaluate the codebase with the rubric.
4. Write `Technical_Reviews/Audit_YYYY-MM-DD_HH-mm.md` in the target project.
5. Pause for approval.
6. Refactor only after approval.
7. Write `Technical_Reviews/Refactored_YYYY-MM-DD_HH-mm.md` in the target project.

## Memory Model

The skill uses three clearly separated memory layers:
- Runtime memory: active findings, tool outputs, and temporary reasoning for the current execution.
- Project-local persistent memory: audit and refactor reports written into the target repository.
- Shared memory: intentionally out of scope. If a broader memory system is needed, integrate an external shared-memory skill rather than extending this repository ad hoc.

## Optional Integrations

These are compatible ideas, not bundled implementations:
- shared-memory skills for promoting stable cross-project conventions,
- repository-specific lint/test scripts already present in the target project,
- CI workflows that consume the generated `Technical_Reviews/` artifacts.

## Examples

- `examples/prompts/technical-review-legacy.md`: the legacy prompt that inspired the audit phase.
- `examples/prompts/auto-refactor-legacy.md`: the legacy prompt that inspired the refactor phase.
- `examples/sandbox/sandbox.ts`: a deliberately flawed TypeScript file for trial runs.

## Evaluation And Maintenance

Use [references/evaluation.md](references/evaluation.md) to validate the skill against a sample repository or the included sandbox artifact.

Repository-level validation:

```bash
python scripts/validate_skill.py
```

GitHub Actions runs the same validator through the `Validate Skills` workflow on pushes, pull requests, and manual dispatch.

Forward-test evidence:
- `examples/forward-tests/sandbox-audit-example.md`: audit-only proof that the skill can evaluate the sandbox and stop correctly at the approval gate.

When updating the skill:
- keep `SKILL.md` concise and operational,
- move detailed contracts into `references/`,
- keep assets limited to reusable output templates,
- preserve the approval gate and mutation boundaries,
- update `agents/openai.yaml` if the public-facing wording changes.

## Publishing Notes

This repository is intended to be GitHub-ready and skill-installable:
- `SKILL.md` contains only standard activation metadata in frontmatter,
- `agents/openai.yaml` provides UI-facing metadata,
- references and assets are separated by role,
- examples are clearly marked as examples rather than core execution assets.
