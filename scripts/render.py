#!/usr/bin/env python3
"""Render resume.yaml into LaTeX build directory."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"


def latex_escape(value: str) -> str:
    if value is None:
        return ""
    text = str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    for char, escaped in replacements.items():
        text = text.replace(char, escaped)
    return text


def latex_inline(text: str) -> str:
    """Convert markdown-style **bold** to LaTeX \\textbf{}."""
    if not text:
        return ""

    parts: list[str] = []
    last = 0
    for match in re.finditer(r"\*\*(.+?)\*\*", text):
        parts.append(latex_escape(text[last : match.start()]))
        parts.append(r"\textbf{" + latex_escape(match.group(1)) + "}")
        last = match.end()
    parts.append(latex_escape(text[last:]))
    return "".join(parts)


def load_resume(yaml_path: Path) -> dict:
    with yaml_path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def render_resume(yaml_path: Path, build_dir: Path) -> None:
    data = load_resume(yaml_path)
    build_dir.mkdir(parents=True, exist_ok=True)
    sections_dir = build_dir / "sections"
    sections_dir.mkdir(exist_ok=True)

    preamble = TEMPLATES / "static" / "preamble.tex"
    preamble_text = preamble.read_text(encoding="utf-8") if preamble.exists() else ""

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(default=False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["latex_escape"] = latex_escape
    env.filters["latex_inline"] = latex_inline

    main_template = env.get_template("main.tex.j2")
    main_content = main_template.render(**data)
    (build_dir / "main.tex").write_text(
        preamble_text + "\n" + main_content,
        encoding="utf-8",
    )

    section_templates = [
        "header.tex.j2",
        "summary.tex.j2",
        "education.tex.j2",
        "experience.tex.j2",
        "projects.tex.j2",
        "skills.tex.j2",
        "coding.tex.j2",
        "certifications.tex.j2",
    ]
    for template_name in section_templates:
        template = env.get_template(f"sections/{template_name}")
        output_name = template_name.replace(".j2", "")
        (sections_dir / output_name).write_text(
            template.render(**data), encoding="utf-8"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Render resume YAML to LaTeX")
    parser.add_argument(
        "--yaml",
        type=Path,
        default=ROOT / "master" / "resume.yaml",
        help="Path to resume YAML file",
    )
    parser.add_argument(
        "--out",
        type=Path,
        required=True,
        help="Output build directory for generated LaTeX",
    )
    args = parser.parse_args()
    render_resume(args.yaml.resolve(), args.out.resolve())
    print(f"Rendered LaTeX to {args.out.resolve()}")


if __name__ == "__main__":
    main()
