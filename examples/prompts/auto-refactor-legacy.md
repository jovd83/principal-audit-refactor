# Legacy Refactor Prompt

This document preserves the original refactor prompt as a historical example.

It is intentionally non-normative. Use `SKILL.md` and `references/refactor-execution.md` for the maintained workflow.

## Legacy Prompt

```text
Read the latest technical review report.

Act as a Senior Principal Engineer and Architect. Resolve as many roadmap items as possible in a single pass while prioritizing correctness, readability, and current best practices.

1. Categorize findings into:
- critical or safety issues,
- architectural or structural issues,
- clean-code issues.

2. Refactor by file rather than by isolated finding.

3. Apply DRY and SOLID principles, strengthen typing, and keep comments minimal.

4. Produce a change log followed by the full final version of each changed file.
```
