# Email Template Tailoring Playbook

Loaded by `/tailor-resume` on every run alongside `docs/tailoring-playbook.md`.

## Source of Truth

| File | Role |
|------|------|
| `master/email-template.yaml` | **Format only** — section order, HTML skeleton, coldMail tokens |
| `master/resume.yaml` | **All facts** for About Me and signature |
| `output/{slug}/resume.yaml` | Tailored resume — proof for impact bullets |
| `output/{slug}/email-overrides.yaml` | Optional JD-specific `why_reaching_out` + `impact_bullets` |

Never store resume facts in `master/email-template.yaml`.

## coldMail Tokens (NEVER change)

`{{name}}`, `{{company}}`, `{{email}}`, `{{jobLink}}` — substituted at compose in coldMail.

## Job Link Section

| Job URL in user message? | Action |
|--------------------------|--------|
| **Yes** | `has_job_link: true`; include link block with `{{jobLink}}` |
| **No** | `has_job_link: false`; omit link section entirely |

## Structure

1. **About Me** — from `resume.yaml` via `build_about_me()`
2. **Why I'm Reaching Out** — 1–2 short sentences tailored per JD (keep compact)
3. **How I Can Impact {{company}}** — 3–4 impact bullets with proof from tailored resume
4. **Closing + Signature** — format from master; signature from `resume.yaml`

### Why section rule

Keep `why_reaching_out` to **one short paragraph** (1–2 sentences). Bio details belong in About Me, not here.

### Impact bullet formula

```
<strong>[Impact for them]</strong> — [Proof from experience/project bullet + metric]
```

No separate Experience / Projects sections.

## Build command

```bash
make build-email-template SLUG={slug}
```

Writes `output/{slug}/email-template.yaml`. Use `output/{slug}/email-overrides.yaml` for JD-specific copy.

## Upload

Runs automatically at the end of every `/tailor-resume` run via `make publish-variant SLUG={slug}`.

Manual:

```bash
make upload-variant SLUG={slug}
```

Uploads resume + `email-template.yaml` to coldMail `templates` collection when present.
