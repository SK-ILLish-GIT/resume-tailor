---
name: tailor-resume
description: Tailor resume for a job description — parse JD, create per-job YAML variant, write full audit, build PDF via Docker. Use when user pastes a JD, says tailor resume, or invokes /tailor-resume.
---

# Tailor Resume for Job Description

Automatically tailor `master/resume.yaml` for a pasted job description and produce a PDF.

## When to Use

- User invokes `/tailor-resume`
- User pastes a JD and asks to tailor, update, or customize their CV/resume
- User says "apply to this role" with a job description

## Prerequisites

- Docker running locally
- Python deps installed: `make install-deps`
- Docker image built once: `make docker-build`

## Workflow (Fully Automatic — No Approval Gate)

Execute all steps without pausing for user approval.

### 1. Load Context

Read these files completely:

- `master/resume.yaml` — canonical source (do NOT edit)
- `docs/projects-catalog.yaml` — GitHub-sourced project metadata for picking the best 2 projects
- `docs/tailoring-playbook.md` — tailoring rules
- `docs/jd-analysis-template.md` — audit report structure

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

Also save the raw JD text to `output/{slug}/job-description.txt` (needed for optional MongoDB upload).

### 6. Build PDF

```bash
make build-variant SLUG={slug}
```

If Docker image missing, run `make docker-build` first.

### 7. Optional — Upload to MongoDB

Only when the user asks to **save to db**, **upload to mongodb**, or similar:

Prerequisites:
- `.env` at repo root with `MONGODB_URI`, `MONGODB_DB`, `MONGODB_USER_ID` (see `.env.example`)
- `make install-deps` includes pymongo

```bash
make upload-variant SLUG={slug}
```

Writes to ColdMail collections:
- `resume_variants` — yaml, jdAnalysis, jobDescription, coverage, slug
- `resumes` — PDF binary as `{Company}_{Role}_{Date}.pdf` with tags + `tailoredFor` metadata

Does **not** sync `master/resume.yaml` to `resume_master`.

### 8. Report to User

Return:

- PDF path: `output/{slug}/{Company}_{Role}_{Date}.pdf` (parsed from jd-analysis header)
- Audit path: `output/{slug}/jd-analysis.md`
- MongoDB upload status (if requested)
- 3–5 bullet summary of key changes
- Overflow warning if applicable
- Top gaps and suggested interview talking points

## Example

**User:** `/tailor-resume` + pasted Stripe backend JD

**Agent actions:**
1. Creates `output/stripe-backend-sde-2026-08-24/`
2. Tailors YAML emphasizing Node.js, distributed systems, observability
3. Writes full jd-analysis.md
4. Runs `make build-variant SLUG=stripe-backend-sde-2026-08-24`
5. Returns PDF path and audit highlights

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Docker not running | Ask user to start Docker Desktop |
| `make build-variant` fails | Check `output/{slug}/build/main.log` for LaTeX errors |
| JD missing company name | Infer from text or use `unknown-company` in slug |
| YAML validation fails | Run `make validate SLUG={slug}` |
