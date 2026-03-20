# Refactoring Roadmap: <project-or-scope-name>

## Metadata
- Timestamp: <YYYY-MM-DD HH:mm>
- Target Path: <absolute-or-repo-relative-path>
- Scope: <full repository | scoped path>
- Detected Stack: <languages, frameworks, package manager, runtime>
- Deterministic Checks: <command -> result>

## Executive Summary
- Maintainability Score: <0-100>
- State Of The Union: <two or three concise sentences>
- Top Risks:
  1. <highest priority risk>
  2. <second priority risk>
  3. <third priority risk>

## Architecture Snapshot
- Entry Points: <api handlers, cli, jobs, UI routes, services>
- Core Layers: <presentation, application, domain, data, infra>
- Hot Files / Hot Paths: <prioritized list>
- Constraints / Unknowns: <missing coverage, broken tooling, non-git repo, etc.>

## Findings Table

| Location | Severity | Smell Detected | Risk | Recommended Fix |
| :--- | :--- | :--- | :--- | :--- |
| `path/to/file.ext:line` | High | Boundary violation | Presentation code is directly coupled to persistence details, making testing and change isolation brittle. | Extract persistence logic behind a repository or service boundary and keep the caller focused on orchestration. |

## Refactor Sequence
1. <first execution step>
2. <second execution step>
3. <third execution step>

## Open Questions Or Blockers
- <question or blocker>
