#!/usr/bin/env python3
"""Assemble output/{slug}/email-template.yaml from master format + tailored resume."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from email_template import (
    assemble_body,
    build_about_me,
    build_signature,
    build_subject,
    build_template_tags,
    default_why_reaching_out,
    format_impact_bullets,
    format_why_reaching_out,
    load_master_template,
    load_yaml,
    validate_output,
)
from pdf_names import parse_jd_analysis_header, parse_date_from_slug
from upload_to_mongo import collect_tags

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Build tailored email-template.yaml for a slug")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--has-job-link", action="store_true")
    parser.add_argument("--role-suffix", default=None)
    parser.add_argument(
        "--overrides",
        help="YAML with why_reaching_out, impact_bullets[], name, role_suffix, has_job_link",
    )
    args = parser.parse_args()

    out_dir = ROOT / "output" / args.slug
    resume_path = out_dir / "resume.yaml"
    analysis_path = out_dir / "jd-analysis.md"
    overrides_path = Path(args.overrides) if args.overrides else out_dir / "email-overrides.yaml"

    if not resume_path.exists():
        raise SystemExit(f"Missing {resume_path}")

    master = load_master_template()
    resume = load_yaml(resume_path)
    overrides: dict = {}
    if overrides_path.exists():
        overrides = load_yaml(overrides_path)

    company, role_title, _ = None, None, None
    if analysis_path.exists():
        company, role_title, _ = parse_jd_analysis_header(analysis_path.read_text(encoding="utf-8"))

    has_job_link = args.has_job_link or bool(overrides.get("has_job_link"))
    if (out_dir / "job-link.txt").exists():
        has_job_link = True

    why_raw = overrides.get("why_reaching_out") or default_why_reaching_out()
    why = format_why_reaching_out(why_raw) if overrides.get("why_reaching_out") else why_raw
    impact_items = overrides.get("impact_bullets") or []
    impact_html = format_impact_bullets(impact_items)
    role_suffix = args.role_suffix or overrides.get("role_suffix")
    template_name = overrides.get("name") or (f"{company} — {role_title}" if company and role_title else args.slug)

    subject = build_subject(master, resume, role_suffix=role_suffix)
    body = assemble_body(
        master,
        about_me=build_about_me(resume),
        why_reaching_out=why,
        impact_intro=master.get("impact_intro") or "",
        impact_bullets_html=impact_html,
        closing=master.get("closing") or "",
        signature=build_signature(resume),
        has_job_link=has_job_link,
    )

    missing = validate_output(subject, body, has_job_link=has_job_link)
    if missing:
        raise SystemExit(f"Template validation failed: {missing}")

    tags = overrides.get("tags") or build_template_tags(
        company or "", role_title or "", collect_tags(resume)
    )

    doc = {
        "name": template_name,
        "subject": subject,
        "body": body,
        "has_job_link": has_job_link,
        "variant_slug": args.slug,
        "tags": tags,
    }

    out_path = out_dir / "email-template.yaml"
    header = f"# Tailored email for {template_name}\n# coldMail tokens preserved: {{name}} {{company}} {{jobLink}}\n\n"
    with out_path.open("w", encoding="utf-8") as f:
        f.write(header)
        yaml.dump(doc, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
