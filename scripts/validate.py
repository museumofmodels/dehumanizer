#!/usr/bin/env python3
"""Dependency-free package checks; not a model-quality benchmark."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


required = [
    "SKILL.md", "README.md", "LICENSE", "CREDITS.md",
    "agents/openai.yaml", "tests/README.md", "tests/cases.json",
    "tests/fixtures/document.md",
]
for name in required:
    check((ROOT / name).is_file(), f"Missing required file: {name}")
if errors:
    sys.exit("\n".join(errors))

skill = (ROOT / "SKILL.md").read_text()
check(skill.startswith("---\n"), "SKILL.md must begin with YAML frontmatter")
parts = skill.split("---\n", 2)
front = parts[1] if len(parts) == 3 else ""
check(bool(front), "SKILL.md frontmatter must be closed")
check(re.search(r"^name: dehumanizer$", front, re.M), "Wrong skill name")
check(re.search(r"^description: .+", front, re.M), "Missing description")
check(re.search(r"^license: MIT$", front, re.M), "Missing MIT declaration")
check(re.search(r'^metadata:\n  version: "1\.0\.0"$', front, re.M), "Missing metadata.version")
check(len(skill.split()) < 1600, "Skill exceeds the intended small runtime budget")

license_text = (ROOT / "LICENSE").read_text()
for notice in [
    "Copyright (c) 2025 Siqi Chen",
    "Copyright (c) 2026 Museum of Models contributors",
    "The above copyright notice and this permission notice shall be included",
    'THE SOFTWARE IS PROVIDED "AS IS"',
]:
    check(notice in license_text, f"Missing license notice: {notice}")

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if re.match(r"[a-z]+://|#|mailto:", target):
            continue
        check((path.parent / target.split("#")[0]).is_file(),
              f"Broken local link in {path.relative_to(ROOT)}: {target}")

cases = json.loads((ROOT / "tests/cases.json").read_text())
ids = [case["id"] for case in cases]
check(len(ids) == len(set(ids)), "Duplicate behavioral case IDs")
for case in cases:
    label = case["id"]
    for field in ["request", "source", "must_preserve", "must_not", "specimen"]:
        check(bool(case.get(field)), f"{label}: missing {field}")
    output = case["specimen"]
    for literal in case.get("literal_invariants", []):
        check(literal in output, f"{label}: specimen changed literal {literal!r}")
    source_numbers = set(re.findall(r"\d+(?:\.\d+)?", case["source"]))
    output_numbers = set(re.findall(r"\d+(?:\.\d+)?", output))
    check(source_numbers == output_numbers, f"{label}: numeric literals differ")
    if "max_words" in case:
        check(len(output.split()) <= case["max_words"], f"{label}: specimen too long")
    if "exact_bullets" in case:
        check(len(re.findall(r"^- ", output, re.M)) == case["exact_bullets"],
              f"{label}: wrong number of bullets")

fixture = (ROOT / "tests/fixtures/document.md").read_text()
check(fixture.startswith("---\n"), "File-mode fixture is missing frontmatter")
check('"Do not retry the payment."' in fixture, "File-mode fixture is missing its exact quote")
check("```sh\nrelease --version 1.2 --dry-run\n```" in fixture, "File-mode fixture is missing its command")

if errors:
    sys.exit("\n".join(f"FAIL: {error}" for error in errors))
print(f"PASS: package, license notices, local links, and {len(cases)} curated example checks.")
print("Model behavior and humor still require the review described in tests/README.md.")
