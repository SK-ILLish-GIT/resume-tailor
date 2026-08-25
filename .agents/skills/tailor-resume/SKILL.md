---
name: tailor-resume
description: Tailor resume for a job description — parse JD, create per-job YAML variant, email template, PDF, and upload to coldMail MongoDB. Fully automatic, no approval gate. Use when user pastes a JD, says tailor resume, or invokes /tailor-resume.
---

# Tailor Resume for Job Description

Automatically tailor `master/resume.yaml` for a pasted job description and produce **resume YAML + email template + PDF + MongoDB upload** — all in one run.

## When to Use

- User invokes `/tailor-resume`
- User pastes a JD and asks to tailor, update, or customize their CV/resume
- User says "apply to this role" with a job description

## Prerequisites

- Docker running locally
- Python deps installed: `make install-deps`
- Docker image built once: `make docker-build`
- `.env` at repo root with `MONGODB_URI`, `MONGODB_DB`, `MONGODB_USER_ID` (see `.env.example`)

## Workflow (Fully Automatic — No Approval Gate)

Execute **all steps** without pausing for user approval. Never ask "should I upload?" — always upload.

**Deliverables every run:**
1. `output/{slug}/resume.yaml`
2. `output/{slug}/email-overrides.yaml` + `email-template.yaml`
3. `output/{slug}/Sk_Sahil_Parvez_CV.pdf`
4. MongoDB upload (variant + resume PDF + email template)

### 1. Load Context

Read these files completely:

- `master/resume.yaml` — canonical source (do NOT edit)
- `docs/projects-catalog.yaml` — GitHub-sourced project metadata for picking the best 2 projects
- `docs/tailoring-playbook.md` — tailoring rules
- `docs/email-template-playbook.md` — coldMail email template rules
- `docs/jd-analysis-template.md` — audit report structure
- `master/email-template.yaml` — email format skeleton (do NOT edit during tailoring)

### 2. Parse the Job Description

From the user's pasted JD text, extract:

- Company name
- Role title
- Required and nice-to-have skills
- Seniority level
- Role focus (frontend, backend, platform, AI, etc.)
- Domain keywords

### 3. Create Output Slug and Directory

Format: `{company}-{role-keywords}-{YYYY-MM-DD}` (lowercase, hyphens)

Example: `stripe-backend-sde-2026-08-24`

Create: `output/{slug}/`

### 4. Copy and Tailor YAML

1. Deep-copy `master/resume.yaml` → `output/{slug}/resume.yaml`
2. Tailor **only** the copy, following `docs/tailoring-playbook.md`:

| Section | Action |
|---------|--------|
| `summary` | Aggressively rewrite for JD focus |
| `experience[].bullets` | Select, reorder, aggressively rewrite; respect bullet caps |
| `projects` | **GameVault always #1** (`include: true`); pick 1 more by JD match; set `include: false` on others; rewrite bullets |
| `skills` | Reorder categories and keywords |
| `education` | **Do not change** |
| `certifications` | **Do not change** |
| `header` | **Do not change** |

**Rules:**
- Never fabricate experience or skills
- Never add missing JD keywords to the CV
- Preserve all dates, companies, titles, metrics
- Use bullet `tags` and `priority` for selection scoring

### 5. Write Full Audit Report

Write `output/{slug}/jd-analysis.md` using the template structure:

- Keyword coverage (matched, missing, percentage)
- Tailoring decisions with rationale
- Page length status (soft 1-page — warn if overflow, do not auto-trim; drop Fractal.ai before going below 2 projects)
- Gap analysis with interview talking points
- ATS tips for this role

Also save the raw JD text to `output/{slug}/job-description.txt` (required for MongoDB upload).

If the user pasted a job URL in their message, save it to `output/{slug}/job-link.txt`.

### 6. Build Email Template

Write `output/{slug}/email-overrides.yaml` with JD-specific copy:

- `why_reaching_out` — **1–2 short sentences** tailored to the role (keep compact; bio stays in About Me)
- `impact_bullets` — 3–4 bullets using the formula in `docs/email-template-playbook.md`
- `has_job_link: true/false` — set true only when a job URL was provided
- `role_suffix` — optional short role label for subject (e.g. `Backend SDE`)
- `tags` — search tags for coldMail

Rules:
- **Do NOT change coldMail tokens:** `{{name}}`, `{{company}}`, `{{email}}`, `{{jobLink}}`
- All factual content from `output/{slug}/resume.yaml` — never fabricate
- Omit job link section entirely when no URL was provided

### 7. Build PDF, Email, and Upload (always run all three)

If Docker image missing, run `make docker-build` first.

```bash
make publish-variant SLUG={slug}
```

This runs in order:
1. `build-email-template` → `output/{slug}/email-template.yaml`
2. `build-variant` → `output/{slug}/Sk_Sahil_Parvez_CV.pdf`
3. `upload-variant` → coldMail MongoDB (`resume_variants`, `resumes`, `templates`)

Writes to ColdMail collections:
- `resume_variants` — yaml, jdAnalysis, jobDescription, coverage, slug, templateId
- `resumes` — PDF binary as `Sk_Sahil_Parvez_CV.pdf` with tags + `tailoredFor` metadata
- `templates` — email subject/body from `email-template.yaml`

Does **not** sync `master/resume.yaml` to `resume_master`.

If MongoDB upload fails (missing `.env`, network, etc.), report the error clearly but still return all local artifact paths.

### 8. Report to User

Return:

- PDF path: `output/{slug}/Sk_Sahil_Parvez_CV.pdf`
- Email template path: `output/{slug}/email-template.yaml`
- Audit path: `output/{slug}/jd-analysis.md`
- MongoDB IDs: `resume_variants.id`, `resumes.id`, `templates.id` (from upload output)
- 3–5 bullet summary of key changes
- Overflow warning if applicable
- Top gaps and suggested interview talking points

## Example

**User:** `/tailor-resume` + pasted Stripe backend JD

**Agent actions:**
1. Creates `output/stripe-backend-sde-2026-08-24/`
2. Tailors YAML emphasizing Node.js, distributed systems, observability
3. Writes `email-overrides.yaml` + builds email template
4. Writes full `jd-analysis.md`
5. Runs `make publish-variant SLUG=stripe-backend-sde-2026-08-24` (PDF + MongoDB upload)
6. Returns PDF path, email template path, MongoDB IDs, and audit highlights

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Docker not running | Ask user to start Docker Desktop |
| `make build-variant` fails | Check `output/{slug}/build/main.log` for LaTeX errors |
| `make upload-variant` fails | Check `.env` has `MONGODB_URI` + `MONGODB_USER_ID`; local artifacts still valid |
| JD missing company name | Infer from text or use `unknown-company` in slug |
| YAML validation fails | Run `make validate SLUG={slug}` |
