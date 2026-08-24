"""Shared PDF filename logic for local builds and MongoDB uploads."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER_PDF_NAME = "Sk_Sahil_Parvez_CV.pdf"


def parse_jd_analysis_header(text: str) -> tuple[str | None, str | None, str | None]:
    match = re.search(
        r"^#\s*JD Analysis\s*—\s*(.+?)\s*/\s*(.+?)\s*/\s*(\d{4}-\d{2}-\d{2})",
        text,
        re.MULTILINE,
    )
    if not match:
        return None, None, None
    return match.group(1).strip(), match.group(2).strip(), match.group(3).strip()


def parse_date_from_slug(slug: str) -> str | None:
    match = re.search(r"(\d{4}-\d{2}-\d{2})$", slug)
    return match.group(1) if match else None


def sanitize_filename_part(text: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", text.strip())
    cleaned = re.sub(r"\s+", "_", cleaned)
    return re.sub(r"_+", "_", cleaned).strip("_")


def build_pdf_names(company: str, role_title: str, date: str) -> tuple[str, str]:
    company_part = sanitize_filename_part(company)
    role_part = sanitize_filename_part(role_title)
    stem = f"{company_part}_{role_part}_{date}"
    return f"{stem}.pdf", stem


def variant_pdf_name(out_dir: Path, slug: str) -> str:
    analysis_path = out_dir / "jd-analysis.md"
    if not analysis_path.exists():
        raise FileNotFoundError(
            f"Missing {analysis_path}. Run tailor-resume to create jd-analysis.md first."
        )
    analysis_text = analysis_path.read_text(encoding="utf-8")
    company, role_title, date = parse_jd_analysis_header(analysis_text)
    if not company or not role_title:
        raise ValueError(f"Could not parse company/role from {analysis_path} header")
    if not date:
        date = parse_date_from_slug(slug)
    if not date:
        raise ValueError(f"Could not parse date from {analysis_path} header or slug {slug}")
    filename, _ = build_pdf_names(company, role_title, date)
    return filename


def resolve_pdf_path(slug: str, root: Path | None = None) -> Path:
    root = root or ROOT
    if slug == "master":
        return root / "output" / "master" / MASTER_PDF_NAME
    out_dir = root / "output" / slug
    return out_dir / variant_pdf_name(out_dir, slug)
