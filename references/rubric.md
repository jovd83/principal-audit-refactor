# Principal Engineer Audit Rubric

Use this rubric after stack discovery. Apply the categories in a technology-aware way, but keep the severity model stable across stacks.

## Severity Model

Use one severity per finding:
- Critical: creates an immediate security, data-integrity, correctness, or availability risk.
- High: materially weakens maintainability, safety, or delivery speed and should be prioritized early.
- Medium: real engineering debt that should be addressed, but does not justify stopping the release by itself.
- Low: useful polish or hygiene improvement; include only when it clarifies a broader pattern.

Prefer fewer well-supported findings over many repetitive ones.

## 1. Architecture And Boundaries

Look for:
- boundary violations between UI, orchestration, domain, and persistence,
- leaky abstractions that expose low-level details in high-level modules,
- oversized files or classes mixing unrelated responsibilities,
- missing seams for extension, substitution, or testing,
- cyclic dependencies or unclear ownership between modules.

Evidence examples:
- raw SQL or transport concerns inside presentation code,
- request parsing and rendering mixed in the same function,
- a service object that also owns logging, validation, caching, and formatting.

## 2. Data, Security, And Type Safety

Look for:
- missing validation at trust boundaries,
- unsafe dynamic typing or unchecked casts,
- insecure defaults, secret exposure, or sensitive logging,
- injection risk, serialization hazards, or unsafe file handling,
- data-shape drift between layers.

Evidence examples:
- `any`, `dynamic`, `interface{}`, unchecked JSON blobs,
- string-concatenated SQL or shell commands,
- API handlers that trust raw request bodies.

## 3. Reliability And Operability

Look for:
- swallowed exceptions or generic fallback errors,
- inconsistent error-handling patterns,
- hidden global state or time-dependent logic that resists testing,
- missing retries, cancellation, idempotency, or cleanup where those concerns matter,
- poor observability that makes diagnosis slow or speculative.

Evidence examples:
- empty `catch` blocks,
- a module that mutates global state during request handling,
- business logic coupled directly to system time or environment variables.

## 4. Code Hygiene And Sustainability

Look for:
- magic values and duplicated logic,
- dead code, unused dependencies, or heavyweight dependencies with trivial usage,
- misleading names, weak module boundaries, or comment noise,
- functions with multiple unrelated side effects,
- patterns that slow safe modification.

Evidence examples:
- copy-pasted validation branches,
- large helper files with no coherent responsibility,
- comments that restate the code while the real design intent remains undocumented.

## 5. Configuration And Delivery Readiness

Look for:
- environment-specific values hardcoded into source,
- missing dependency lockfiles or reproducibility gaps,
- absent or misleading setup instructions,
- CI or test coverage blind spots that raise delivery risk,
- runtime assumptions that are not encoded in configuration.

Evidence examples:
- production URLs in source files,
- undocumented required env vars,
- missing build or validation instructions for a non-trivial stack.

## Scoring Guidance

Start at `100` and deduct:
- `10` per Critical finding
- `5` per High finding
- `2` per Medium finding
- `1` per Low finding when included

Floor at `0`. Treat the score as an executive shorthand, not the whole audit.

## Reporting Rules

- Attach each finding to a concrete file path or architectural area.
- Explain the engineering risk, not just the smell name.
- Recommend the smallest change that materially improves the system.
- If multiple files share one pattern, describe the pattern once and link the representative files.
- Distinguish verified facts from inference when tooling coverage is incomplete.
