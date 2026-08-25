"""Email template helpers — format from master/email-template.yaml, content from resume.yaml."""

from __future__ import annotations

import html
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MASTER_TEMPLATE = ROOT / "master" / "email-template.yaml"
JOB_LINK_PLACEHOLDER = "{{JOB_LINK_SECTION}}"

COLDMAIL_TOKENS = ("{{name}}", "{{company}}", "{{email}}", "{{jobLink}}")

TAILOR_PLACEHOLDERS = (
    "{{ABOUT_ME}}",
    "{{WHY_REACHING_OUT}}",
    "{{IMPACT_INTRO}}",
    "{{IMPACT_BULLETS}}",
    "{{CLOSING}}",
    "{{SIGNATURE}}",
)


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_master_template(path: Path | None = None) -> dict:
    return load_yaml(path or MASTER_TEMPLATE)


def extract_job_url(text: str) -> str | None:
    match = re.search(r"https?://[^\s<>\"')\]]+", text)
    return match.group(0).rstrip(".,;") if match else None


def current_experience(resume: dict) -> dict | None:
    items = resume.get("experience") or []
    return items[0] if items else None


def education_line(resume: dict) -> str:
    edu = (resume.get("education") or [{}])[0]
    institution = edu.get("institution") or "IIIT Allahabad"
    degree = edu.get("degree") or "B.Tech in IT"
    dates = (edu.get("dates") or "").replace("--", "–")
    short = "IIIT Allahabad" if "Allahabad" in institution else institution
    return f"{degree} from {short} ({dates})"


def _display_name(raw: str) -> str:
    if raw.isupper():
        return " ".join(raw.title().split())
    return raw


def build_about_me(resume: dict) -> str:
    header = resume.get("header") or {}
    name = _display_name(header.get("name") or "Sk Sahil Parvez")
    edu = education_line(resume)
    exp = current_experience(resume)
    if exp:
        title = exp.get("title") or "SDE"
        company = exp.get("company") or "my current company"
        role_line = f"Currently, I work as {title} at {company}."
    else:
        role_line = "I'm actively seeking software engineering roles."
    return f"<p>\n  I'm {name}, a {edu}. {role_line}\n</p>"


def format_why_reaching_out(html_block: str) -> str:
    """Keep why section to one compact paragraph."""
    text = html_block.strip()
    match = re.match(r"^<p>\s*(.*?)\s*</p>$", text, re.DOTALL | re.IGNORECASE)
    inner = match.group(1).strip() if match else text
    return f"<p>\n  {inner}\n</p>"


def build_signature(resume: dict) -> str:
    header = resume.get("header") or {}
    name = _display_name(header.get("name") or "Sk Sahil Parvez")
    phone = header.get("phone") or ""
    email = header.get("email") or ""
    linkedin = (header.get("linkedin") or {}).get("url") or ""
    portfolio = (header.get("portfolio") or {}).get("url") or ""
    portfolio_label = (header.get("portfolio") or {}).get("label") or portfolio
    exp = current_experience(resume)
    phone_fmt = f"+91 {phone}" if phone and not str(phone).startswith("+") else phone

    parts = [
        "<p>",
        "  Best regards,<br>",
        f"  <strong>{html.escape(name)}</strong><br>",
    ]
    if exp:
        line = f"{exp.get('title', 'SDE')}, {exp.get('company', '')}"
        parts.append(f"  {html.escape(line)}<br>")
    if phone_fmt:
        parts.append(f"  Phone: {html.escape(str(phone_fmt))}<br>")
    if email:
        parts.append(f'  Email: <a href="mailto:{html.escape(email)}">{html.escape(email)}</a><br>')
    if linkedin:
        parts.append(f'  LinkedIn: <a href="{html.escape(linkedin)}">LinkedIn</a><br>')
    if portfolio:
        parts.append(
            f'  Portfolio: <a href="{html.escape(portfolio)}">{html.escape(portfolio_label)}</a>'
        )
    parts.append("</p>")
    return "\n".join(parts)


def build_subject(template: dict, resume: dict, *, role_suffix: str | None = None) -> str:
    pattern = template.get("subject_template") or template.get("subject") or ""
    exp = current_experience(resume)
    employer = exp.get("company") if exp else "Highspot"
    subject = pattern.replace("{current_employer}", employer)
    if role_suffix:
        subject = f"{subject} | {role_suffix}"
    return subject


def default_why_reaching_out() -> str:
    return format_why_reaching_out(
        "Interested in opportunities at <strong>{{company}}</strong> and happy to discuss relevant roles."
    )


def format_impact_bullets(items: list[str]) -> str:
    if not items:
        return "<ul></ul>"
    lines = ["<ul>"] + [f"  <li>{item}</li>" for item in items] + ["</ul>"]
    return "\n".join(lines)


def resolve_job_link_section(master: dict, has_job_link: bool) -> str:
    if not has_job_link:
        return ""
    section = (master.get("job_link_section") or "").strip()
    return f"\n{section}\n" if section else ""


def assemble_body(
    master: dict,
    *,
    about_me: str,
    why_reaching_out: str,
    impact_intro: str,
    impact_bullets_html: str,
    closing: str,
    signature: str,
    has_job_link: bool,
) -> str:
    body = master.get("body") or ""
    job_link = resolve_job_link_section(master, has_job_link)
    replacements = {
        "{{ABOUT_ME}}": about_me,
        "{{WHY_REACHING_OUT}}": why_reaching_out,
        "{{IMPACT_INTRO}}": impact_intro.strip(),
        "{{IMPACT_BULLETS}}": impact_bullets_html,
        "{{CLOSING}}": closing.strip(),
        "{{SIGNATURE}}": signature,
        JOB_LINK_PLACEHOLDER: job_link,
    }
    for key, value in replacements.items():
        body = body.replace(key, value)
    return body


def validate_output(subject: str, body: str, *, has_job_link: bool) -> list[str]:
    missing: list[str] = []
    combined = f"{subject}\n{body}"
    for token in ("{{name}}", "{{company}}"):
        if token not in combined:
            missing.append(token)
    if has_job_link and "{{jobLink}}" not in body:
        missing.append("{{jobLink}}")
    for ph in (JOB_LINK_PLACEHOLDER, *TAILOR_PLACEHOLDERS):
        if ph in body:
            missing.append(f"unresolved {ph}")
    return missing


def sanitize_tag(text: str) -> str:
    cleaned = re.sub(r"[^\w\s-]", "", text.strip().lower())
    cleaned = re.sub(r"\s+", "-", cleaned)
    return re.sub(r"-+", "-", cleaned).strip("-")[:48]


def build_template_tags(company: str, role_title: str, resume_tags: list[str]) -> list[str]:
    tags: set[str] = set()
    if company:
        tags.add(sanitize_tag(company))
    for part in re.split(r"[\s/–-]+", role_title or ""):
        part = sanitize_tag(part)
        if len(part) > 2:
            tags.add(part)
    tags.update(resume_tags[:12])
    return sorted(tags)
