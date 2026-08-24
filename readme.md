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
3. Agent creates `output/{company-role-date}/` with:
   - `resume.yaml` — tailored variant
   - `jd-analysis.md` — keyword audit, gaps, interview prep
   - `Sk_Sahil_Parvez_CV.pdf` — ready to submit

## Update Master CV

Use `/update-resume` or edit `master/resume.yaml` directly.

## Preview Master PDF

```bash
make build-master   # writes to output/master/Sk_Sahil_Parvez_CV.pdf (regenerated, gitignored)
```

## Project Structure

```
master/resume.yaml              # Canonical CV data
docs/tailoring-playbook.md      # ATS rules
templates/                      # LaTeX Jinja2 templates
scripts/render.py               # YAML → LaTeX
scripts/build.sh                # Docker PDF build
.agents/skills/tailor-resume/   # JD tailoring skill
.agents/skills/update-resume/   # Master CV maintenance skill
output/{slug}/                  # Per-job tailored variants
```

## Requirements

- Docker Desktop
- Python 3.10+ with PyYAML and Jinja2
