---
name: update-resume
description: Append new experience bullets or update master/resume.yaml via chat. Use when user wants to add work experience, projects, or skills to their canonical CV.
---

# Update Master Resume

Maintain the canonical `master/resume.yaml`. Never edit tailored variants in `output/`.

## When to Use

- User invokes `/update-resume`
- User says "add this bullet to Highspot", "add a new project", "update my skills"
- User completed new work and wants it in the master bullet pool

## Workflow

### 1. Load Master

Read `master/resume.yaml` completely.

### 2. Understand the Request

Identify:
- Target section (experience company, project, skills category)
- Content to add or modify
- Whether user provided tags (if not, generate from content)

### 3. Apply Changes

**Adding an experience bullet:**

```yaml
bullets:
  - text: "User-provided bullet text"
    tags: [auto, generated, from, content]
    priority: 2  # default 2; use 1 for highest importance
```

**Adding a project:** include all required fields per existing schema.

**Updating skills:** append keywords to the appropriate category; do not remove existing unless user asks.

### 4. Validate

```bash
python3 scripts/migrate_tex_to_yaml.py --yaml master/resume.yaml
```

### 5. Confirm

Tell the user:
- What was added/changed
- Tags assigned
- Reminder: run `make build-master` to preview master PDF
- Tailored variants in `output/` are not affected

## Hard Rules

- Only edit `master/resume.yaml`
- Never edit `output/*/resume.yaml` through this skill
- Never change education or certifications unless user explicitly requests
- Auto-generate sensible `tags` from bullet content (technologies, domains, verbs)
- Assign `priority: 1` for flagship achievements, `2` default, `3–4` for supporting bullets

## Example

**User:** `/update-resume` Add to Highspot: "Reduced API latency by 40% through GraphQL query optimization and Redis caching."

**Agent:**
1. Appends bullet to Highspot with tags: `[graphql, redis, performance, optimization, node]`
2. Sets priority: 1
3. Validates YAML
4. Confirms addition
