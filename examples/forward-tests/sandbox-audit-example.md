# Refactoring Roadmap: sandbox.ts

## Metadata
- Timestamp: 2026-03-19 00:00
- Target Path: `examples/sandbox/sandbox.ts`
- Scope: scoped path
- Detected Stack: TypeScript, browser-aware UI logic, sqlite3 usage, no repository-level manifest inspected in this isolated example
- Deterministic Checks: no project-native checks were run because the sandbox artifact is a single example file rather than a full runnable project

## Executive Summary
- Maintainability Score: 69
- State Of The Union: The sandbox intentionally compresses multiple high-risk engineering failures into one class so the audit path can prove it can find real boundary, safety, and reliability issues without over-scoping the review. The highest-risk problems are unsafe query construction, missing validation at the trust boundary, and tightly coupled global state that makes the behavior difficult to reason about or test.
- Top Risks:
  1. SQL injection and unsafe data access inside presentation-oriented code.
  2. Silent failure and ghost-state behavior that can hide broken writes or partial results.
  3. Type erosion and global mutable state that block safe refactoring.

## Architecture Snapshot
- Entry Points: `UserDashboardManager.processUserDataAndRender`
- Core Layers: presentation, persistence, cache mutation, role checks, and time-based admin behavior are all mixed into one class
- Hot Files / Hot Paths: `examples/sandbox/sandbox.ts`
- Constraints / Unknowns: isolated example file, no surrounding project structure, no git context, no native test or lint commands available from a manifest

## Findings Table

| Location | Severity | Smell Detected | Risk | Recommended Fix |
| :--- | :--- | :--- | :--- | :--- |
| `examples/sandbox/sandbox.ts:30` | Critical | Injection-prone data access | SQL is assembled with string concatenation from untrusted input, creating a direct correctness and security risk. | Move persistence into a dedicated data boundary and use parameterized queries with validated inputs. |
| `examples/sandbox/sandbox.ts:27` | High | Validation gap at trust boundary | `reqBody` is trusted without shape or null checks, allowing malformed input to corrupt control flow and downstream queries. | Introduce an explicit request model and validate `id`, `items`, and `role` before any business logic runs. |
| `examples/sandbox/sandbox.ts:36` | High | N+1 query pattern with swallowed failures | Per-item database calls happen in a loop and the callback ignores errors, making performance and diagnosis both poor. | Batch the query where possible, await results explicitly, and surface failures through a consistent error path. |
| `examples/sandbox/sandbox.ts:15` | High | Type safety erosion | `any` is used for the database handle, cache, user, request body, and result containers, removing meaningful compiler protection. | Replace `any` with explicit interfaces, typed collections, and narrow conversions at boundaries only. |
| `examples/sandbox/sandbox.ts:46` | Medium | Ghost state and mixed rendering side effects | Cache mutation and DOM updates happen before the data flow is trustworthy, so UI and cached state can drift from reality. | Separate data retrieval, view-model creation, and rendering so state changes happen from verified results only. |
| `examples/sandbox/sandbox.ts:67` | Medium | Untestable time-coupled admin logic | `doAdminStuff` depends directly on system time and hidden side effects, which makes deterministic testing awkward. | Inject time and side-effect dependencies or move scheduled behavior behind a dedicated service seam. |
| `examples/sandbox/sandbox.ts:17` | Medium | Magic values and weak role handling | Role checks and generic error strings are hardcoded, which encourages brittle branching and poor diagnostics. | Replace string literals with named constants or enums and return structured error information. |

## Refactor Sequence
1. Define typed input and domain models, then validate the request boundary.
2. Extract database access into a dedicated function or repository and replace string-built SQL with parameterized calls.
3. Separate result assembly from DOM rendering and cache mutation.
4. Replace global mutable state and time-coupled behavior with injected dependencies.

## Open Questions Or Blockers
- This forward test intentionally stops after the audit artifact because the skill requires explicit approval before refactoring.
- A full refactor pass would benefit from a runnable test harness around the sandbox behavior.

## Validation Outcome
- The audit contract was satisfiable on the sandbox artifact.
- The approval gate remained intact: no mutation artifact was produced because no approval step was granted.
