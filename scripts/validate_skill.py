#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / 'SKILL.md',
    ROOT / 'README.md',
    ROOT / 'CHANGELOG.md',
    ROOT / 'LICENSE',
    ROOT / 'agents' / 'openai.yaml',
    ROOT / 'assets' / 'audit-report-template.md',
    ROOT / 'assets' / 'refactor-report-template.md',
    ROOT / 'references' / 'rubric.md',
    ROOT / 'references' / 'report-contract.md',
    ROOT / 'references' / 'refactor-execution.md',
    ROOT / 'references' / 'evaluation.md',
]


def fail(message: str) -> None:
    print(f'ERROR: {message}')
    sys.exit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not match:
        fail('SKILL.md is missing YAML frontmatter delimited by ---')

    data: dict[str, object] = {}
    current_section: str | None = None
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip():
            continue
        if raw_line.startswith('  '):
            if current_section is None:
                fail(f'Unexpected indented frontmatter line: {raw_line!r}')
            line = raw_line.strip()
            if ':' not in line:
                fail(f'Invalid frontmatter line: {raw_line!r}')
            key, value = line.split(':', 1)
            section = data.setdefault(current_section, {})
            if not isinstance(section, dict):
                fail(f'Frontmatter section {current_section!r} must be a mapping')
            section[key.strip()] = value.strip()
            continue

        line = raw_line.strip()
        if ':' not in line:
            fail(f'Invalid frontmatter line: {raw_line!r}')
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        if value:
            data[key] = value
            current_section = None
            continue

        data[key] = {}
        current_section = key
    return data


def parse_simple_yaml(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' not in line:
            fail(f'Invalid YAML line: {raw_line!r}')
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip()
    return data


def validate_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        fail(f'Missing required files: {", ".join(missing)}')


def validate_skill_frontmatter() -> None:
    skill_text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    frontmatter = parse_frontmatter(skill_text)
    allowed_keys = {'name', 'description', 'metadata'}
    if set(frontmatter) != allowed_keys:
        fail(f'SKILL.md frontmatter keys must be exactly {sorted(allowed_keys)}; found {sorted(frontmatter)}')
    for key in ('name', 'description'):
        if not frontmatter[key]:
            fail(f'SKILL.md frontmatter key {key!r} must not be empty')
    metadata = frontmatter['metadata']
    if not isinstance(metadata, dict):
        fail("SKILL.md frontmatter key 'metadata' must be a mapping")
    for key in ('author', 'version'):
        if key not in metadata or not metadata[key]:
            fail(f"SKILL.md frontmatter metadata field {key!r} must not be empty")


def validate_openai_metadata() -> None:
    data = parse_simple_yaml((ROOT / 'agents' / 'openai.yaml').read_text(encoding='utf-8'))
    for key in ('display_name', 'short_description', 'default_prompt'):
        if key not in data or not data[key]:
            fail(f'agents/openai.yaml missing required field {key!r}')


def validate_local_links() -> None:
    docs = [
        ROOT / 'SKILL.md',
        ROOT / 'README.md',
        ROOT / 'references' / 'evaluation.md',
        ROOT / 'references' / 'report-contract.md',
        ROOT / 'references' / 'refactor-execution.md',
    ]
    for doc in docs:
        text = doc.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if re.match(r'^[a-z]+://', target):
                continue
            if target.startswith('#'):
                continue
            resolved = (doc.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f'Link escapes repository root in {doc.relative_to(ROOT)}: {target}')
            if not resolved.exists():
                fail(f'Broken local link in {doc.relative_to(ROOT)}: {target}')


def main() -> None:
    validate_required_files()
    validate_skill_frontmatter()
    validate_openai_metadata()
    validate_local_links()
    print('Validation passed: skill structure, metadata, and local links look good.')


if __name__ == '__main__':
    main()
