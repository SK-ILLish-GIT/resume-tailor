#!/usr/bin/env python3
"""One-time helper: document resume YAML schema and validate structure."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOP_LEVEL = {
    "header",
    "summary",
    "education",
    "experience",
    "projects",
    "skills",
    "certifications",
}


def validate_resume(data: dict) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_TOP_LEVEL - set(data.keys())
    if missing:
        errors.append(f"Missing top-level keys: {', '.join(sorted(missing))}")

    for idx, job in enumerate(data.get("experience", [])):
        for field in ("company", "title", "dates", "location", "tech_stack", "bullets"):
            if field not in job:
                errors.append(f"experience[{idx}] missing '{field}'")
        for bidx, bullet in enumerate(job.get("bullets", [])):
            if "text" not in bullet:
                errors.append(f"experience[{idx}].bullets[{bidx}] missing 'text'")

    for idx, project in enumerate(data.get("projects", [])):
        for field in ("name", "github_url", "github_label", "dates", "tech_stack", "bullets"):
            if field not in project:
                errors.append(f"projects[{idx}] missing '{field}'")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate resume YAML schema")
    parser.add_argument(
        "--yaml",
        type=Path,
        default=ROOT / "master" / "resume.yaml",
    )
    args = parser.parse_args()
    with args.yaml.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    errors = validate_resume(data)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        sys.exit(1)
    print(f"Valid: {args.yaml}")


if __name__ == "__main__":
    main()
