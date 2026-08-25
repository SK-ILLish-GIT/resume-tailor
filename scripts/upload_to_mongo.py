#!/usr/bin/env python3
"""Upload a tailored resume variant to ColdMail MongoDB."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import secrets
import string
from datetime import datetime, timezone
from pathlib import Path

import certifi
import yaml
from dotenv import load_dotenv
from pymongo import MongoClient

from pdf_names import (
    MASTER_PDF_NAME,
    build_pdf_names,
    parse_date_from_slug,
    parse_jd_analysis_header,
    resolve_pdf_path,
)

ROOT = Path(__file__).resolve().parent.parent
ID_ALPHABET = string.ascii_letters + string.digits + "_-"


def gen_id(length: int = 11) -> str:
    return "".join(secrets.choice(ID_ALPHABET) for _ in range(length))


def load_env() -> tuple[str, str, str]:
    load_dotenv(ROOT / ".env")
    uri = os.environ.get("MONGODB_URI")
    db_name = os.environ.get("MONGODB_DB", "coldmail")
    user_id = os.environ.get("MONGODB_USER_ID")
    missing = [k for k, v in [("MONGODB_URI", uri), ("MONGODB_USER_ID", user_id)] if not v]
    if missing:
        raise SystemExit(
            f"Missing env var(s): {', '.join(missing)}. "
            "Copy .env.example to .env and fill in values."
        )
    return uri, db_name, user_id


def parse_coverage_pct(text: str) -> int | None:
    match = re.search(r"\*\*Coverage:\*\*\s*~?(\d+)%", text)
    return int(match.group(1)) if match else None


def parse_page_status(text: str) -> str:
    if re.search(r"overflow|exceeds|over 1 page|>1 page", text, re.IGNORECASE):
        return "overflow"
    return "fits"


def collect_tags(yaml_data: dict) -> list[str]:
    tags: set[str] = set()
    for section in ("experience", "projects"):
        for item in yaml_data.get(section, []) or []:
            for bullet in item.get("bullets", []) or []:
                tags.update(bullet.get("tags") or [])
    for skill in yaml_data.get("skills", []) or []:
        keywords = skill.get("keywords") or ""
        for token in re.split(r",\s*", keywords):
            token = token.strip().lower()
            if token:
                tags.add(token)
    return sorted(tags)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_tags(input_tags: list[str] | None) -> list[str]:
    """Match coldMail server/src/utils/tags.js rules."""
    if not input_tags:
        return []
    seen: set[str] = set()
    out: list[str] = []
    for raw in input_tags:
        t = re.sub(r"\s+", "-", str(raw or "").strip().lower())[:24]
        if not t or not re.match(r"^[a-z0-9][a-z0-9+./_-]*$", t) or t in seen:
            continue
        seen.add(t)
        out.append(t)
        if len(out) >= 25:
            break
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload tailored resume to ColdMail MongoDB")
    parser.add_argument("--slug", required=True, help="Output folder slug, e.g. popclub-sde1-backend-2026-08-25")
    parser.add_argument(
        "--job-description-file",
        help="Path to raw JD text (defaults to output/{slug}/job-description.txt if present)",
    )
    args = parser.parse_args()

    out_dir = ROOT / "output" / args.slug
    yaml_path = out_dir / "resume.yaml"
    template_path = out_dir / "email-template.yaml"
    analysis_path = out_dir / "jd-analysis.md"
    default_jd_path = out_dir / "job-description.txt"

    try:
        pdf_path = resolve_pdf_path(args.slug, ROOT)
    except (FileNotFoundError, ValueError) as exc:
        raise SystemExit(str(exc)) from exc

    for path, label in [(yaml_path, "resume.yaml"), (analysis_path, "jd-analysis.md"), (pdf_path, "PDF")]:
        if not path.exists():
            raise SystemExit(f"Missing {label}: {path}")

    template_data = None
    if template_path.exists():
        with template_path.open(encoding="utf-8") as f:
            template_data = yaml.safe_load(f)

    uri, db_name, user_id = load_env()
    client = MongoClient(uri, tlsCAFile=certifi.where())
    db = client[db_name]

    with yaml_path.open(encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)

    analysis_text = analysis_path.read_text(encoding="utf-8")
    company, role_title, date = parse_jd_analysis_header(analysis_text)
    if not company or not role_title:
        raise SystemExit(f"Could not parse company/role from {analysis_path} header")
    if not date:
        date = parse_date_from_slug(args.slug)
    if not date:
        raise SystemExit(f"Could not parse date from {analysis_path} header or slug {args.slug}")

    jd_path = Path(args.job_description_file) if args.job_description_file else default_jd_path
    if jd_path.exists():
        job_description = jd_path.read_text(encoding="utf-8").strip()
    else:
        job_description = f"Tailored for {role_title} at {company} ({args.slug})"

    _, display_name = build_pdf_names(company, role_title, date)
    filename = MASTER_PDF_NAME
    coverage_pct = parse_coverage_pct(analysis_text)
    page_status = parse_page_status(analysis_text)
    tags = normalize_tags(collect_tags(yaml_data))
    pdf_bytes = pdf_path.read_bytes()
    now = utc_now_iso()
    jd_hash = hashlib.sha256(job_description.encode("utf-8")).hexdigest()[:12]
    jd_preview = job_description[:120].replace("\n", " ")

    existing_variant = db.resume_variants.find_one({"userId": user_id, "slug": args.slug})
    variant_id = existing_variant["id"] if existing_variant else gen_id()
    resume_id = existing_variant.get("resumeId") if existing_variant else gen_id()
    template_id = None
    if template_data:
        template_id = existing_variant.get("templateId") if existing_variant else gen_id()
        if existing_variant and not existing_variant.get("templateId"):
            template_id = gen_id()

    variant_doc = {
        "id": variant_id,
        "userId": user_id,
        "slug": args.slug,
        "company": company,
        "roleTitle": role_title,
        "jobDescription": job_description,
        "yaml": yaml_data,
        "jdAnalysis": analysis_text,
        "coveragePct": coverage_pct,
        "pageStatus": page_status,
        "status": "built",
        "resumeId": resume_id,
        "updatedAt": now,
    }
    if template_id:
        variant_doc["templateId"] = template_id
    if existing_variant:
        db.resume_variants.update_one({"_id": existing_variant["_id"]}, {"$set": variant_doc})
    else:
        variant_doc["createdAt"] = now
        db.resume_variants.insert_one(variant_doc)

    resume_doc = {
        "id": resume_id,
        "userId": user_id,
        "name": display_name,
        "filename": filename,
        "contentType": "application/pdf",
        "size": len(pdf_bytes),
        "tags": tags,
        "content": pdf_bytes,
        "tailoredFor": {
            "jdHash": jd_hash,
            "jdPreview": jd_preview,
            "role": role_title,
            "company": company,
            "sessionId": variant_id,
            "variantSlug": args.slug,
            "coveragePct": coverage_pct,
            "savedAt": now,
        },
        "createdAt": now,
    }

    existing_resume = db.resumes.find_one({"id": resume_id, "userId": user_id})
    if existing_resume:
        db.resumes.update_one(
            {"_id": existing_resume["_id"]},
            {"$set": {k: v for k, v in resume_doc.items() if k != "createdAt"}},
        )
    else:
        db.resumes.insert_one(resume_doc)

    print(f"Uploaded variant {args.slug} → resume_variants.id={variant_id}")
    print(f"Uploaded PDF {filename} → resumes.id={resume_id} (userId={user_id})")

    if template_data and template_id:
        template_name = template_data.get("name") or f"{company} — {role_title}"
        template_doc = {
            "id": template_id,
            "userId": user_id,
            "name": template_name,
            "subject": template_data.get("subject") or "",
            "body": template_data.get("body") or "",
            "tags": normalize_tags(template_data.get("tags") or tags),
            "updatedAt": now,
            "tailoredFor": {
                "jdHash": jd_hash,
                "jdPreview": jd_preview,
                "role": role_title,
                "company": company,
                "sessionId": variant_id,
                "savedAt": now,
                "variantSlug": args.slug,
                "resumeId": resume_id,
            },
        }
        existing_template = db.templates.find_one({"id": template_id, "userId": user_id})
        if existing_template:
            db.templates.update_one(
                {"_id": existing_template["_id"]},
                {"$set": {k: v for k, v in template_doc.items() if k != "createdAt"}},
            )
        else:
            template_doc["createdAt"] = now
            db.templates.insert_one(template_doc)
        print(f"Uploaded template → templates.id={template_id} (tags={len(template_doc['tags'])})")


if __name__ == "__main__":
    main()
