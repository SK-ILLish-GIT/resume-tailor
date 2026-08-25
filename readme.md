# Resume Tailor

Tailor your LaTeX CV for each job application directly from Cursor chat.

## Quick Start

```bash
make install-deps
make docker-build
```

## Tailor for a Job

1. Invoke `/tailor-resume` (or paste a JD and say "tailor my resume for this")
2. Paste the job description
3. Agent automatically creates and uploads everything:
   - `resume.yaml` — tailored variant
   - `email-template.yaml` — tailored coldMail email
   - `jd-analysis.md` — keyword audit, gaps, interview prep
   - `Sk_Sahil_Parvez_CV.pdf` — ready to submit
   - MongoDB — variant + resume + template in coldMail

Requires `.env` with MongoDB credentials (see `.env.example`).

## Update Master CV

Use `/update-resume` or edit `master/resume.yaml` directly.

## Preview Master PDF

```bash
make build-master   # preview canonical CV PDF
make publish-variant SLUG=popclub-sde1-backend-2026-08-25  # email + PDF + MongoDB
```

## Project Structure

```
master/resume.yaml              # Canonical CV data
master/email-template.yaml      # coldMail email format (no resume facts)
docs/tailoring-playbook.md      # ATS rules
docs/email-template-playbook.md # Email template rules
templates/                      # LaTeX Jinja2 templates
scripts/render.py               # YAML → LaTeX
scripts/build.sh                # Docker PDF build
scripts/build_email_template.py # Assemble email-template.yaml
scripts/upload_to_mongo.py      # Upload variant + template to coldMail MongoDB
.agents/skills/tailor-resume/   # JD tailoring skill
.agents/skills/update-resume/   # Master CV maintenance skill
output/{slug}/                  # Per-job tailored variants
```

## Requirements

- Docker Desktop
- Python 3.10+ with PyYAML and Jinja2
