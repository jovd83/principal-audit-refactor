# Contributing

Thanks for improving `principal-audit-refactor`.

## Ground Rules

- Keep `SKILL.md` concise and operational.
- Move detailed contracts or explanatory material into `references/`.
- Keep reusable output skeletons in `assets/`.
- Keep examples and forward-test evidence in `examples/`.
- Preserve the approval gate between audit and refactor.
- Do not add speculative architecture or cross-agent infrastructure unless the repository explicitly grows into that scope.

## Development Workflow

1. Make your change in the smallest useful slice.
2. Update documentation or examples if behavior changes.
3. Run the repository validator:

```bash
python scripts/validate_skill.py
```

4. If you changed core behavior, refresh the forward-test evidence in `examples/forward-tests/`.
5. Update `CHANGELOG.md`.

## Review Expectations

Pull requests should explain:
- what changed,
- why it improves the skill,
- whether prompts, contracts, or examples were updated,
- how the change was validated.

## Scope Discipline

This repository is a skill package, not a framework. Favor clarity, explicit contracts, and maintainability over added surface area.
