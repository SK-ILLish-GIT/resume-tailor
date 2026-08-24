# Resume Tailoring Playbook

Loaded by `/tailor-resume` on every run. Customize these rules over time.

## Hard Constraints (Never Violate)

- Never change dates, company names, job titles, or education details
- Never fabricate skills, projects, or experience not in `master/resume.yaml`
- Never add missing JD requirements to the CV — report gaps in `jd-analysis.md` only
- Education and certifications sections are **fully static** — copy verbatim from master
- Preserve all quantified metrics (percentages, team counts, instance counts) unless rephrasing

## JD Analysis Checklist

Before tailoring, extract from the pasted JD:

1. **Company name** and **role title** (for output folder slug)
2. **Required skills** — must-have technologies and domains
3. **Nice-to-have skills** — preferred but not mandatory
4. **Seniority signals** — intern, junior, mid, senior, staff, years of experience
5. **Role focus** — frontend, backend, fullstack, platform, infra, data, AI/ML
6. **Domain keywords** — industry terms (fintech, observability, distributed systems, etc.)
7. **Action verbs** used in the JD — mirror where truthful

## ATS Keyword Rules

- Mirror **exact terminology** from the JD (if JD says "React.js", use "React.js" not "React")
- Place top matched keywords in **summary** (first 2 sentences) and **skills** section
- Repeat critical keywords naturally across summary, experience bullets, and skills — avoid stuffing
- Use standard section headings: SUMMARY, WORK EXPERIENCE, PROJECTS, TECHNICAL SKILLS, EDUCATION, ACHIEVEMENTS
- Avoid tables with merged cells beyond the skills table; avoid images and graphics
- Prefer common tech spellings ATS expects: Node.js, GraphQL, CI/CD, OpenTelemetry, PostgreSQL

## Aggressive Rewrite Formula

Each bullet should follow:

```
[Strong action verb] + [JD-aligned lead phrase] + [technologies/methods] + [quantified outcome]
```

**Preferred action verbs:** Built, Architected, Delivered, Implemented, Designed, Developed, Integrated, Instrumented, Optimized, Led, Shipped, Automated

**Rewrite strategy (aggressive):**
- Lead with the JD's highest-priority keyword that the bullet genuinely supports
- Reframe the same work from the JD's perspective (e.g. "platform" JD → emphasize deployment/scaling language)
- Swap synonyms to match JD terms (e.g. "microservices" ↔ "distributed services" per JD wording)
- Keep all numbers and facts intact — rewrite framing, not substance
- **Prefer quantified bullets** when selecting/reordering — bullets with metrics beat vague ones at equal JD match

## Quantification Rules

Every bullet should include a **number, scale, or scope** when one exists in master or project catalog:

| Good (quantified) | Weak (vague) |
|---|---|
| 20+ AWS EC2 instances | large-scale cloud deployment |
| 5 teams and 50+ engineers | many teams adopted it |
| 10-service Docker Compose stack | containerized platform |
| 50+ test cases | comprehensive test suite |
| 6 Grafana dashboards | full observability |

**Where to find numbers:** master bullets, `docs/projects-catalog.yaml` highlights (service counts, retry limits, node scale), repo READMEs.

**Never fabricate** percentages, latency improvements, or user counts you cannot verify.

**Priority when trimming:** drop unquantified bullets before quantified ones at similar JD relevance.

**Summary:** include at least one scale metric in sentence 2 (e.g. 20+ instances, 10 services, 50+ engineers).

**Example rewrite:**

- Before: "Built OtelForge, a platform to deploy and manage OpenTelemetry Collectors across 20+ AWS EC2 instances."
- JD focus: observability platform, SRE, infrastructure
- After: "Architected OtelForge, an observability platform deploying and managing OpenTelemetry Collectors across 20+ AWS EC2 instances for enterprise telemetry pipelines."

## Bullet Selection Rules

Score each bullet by tag overlap with JD keywords. Select by score × (1/priority).

| Role | Max bullets |
|------|-------------|
| Current role (Highspot) | 4 |
| Recent role (Zscaler) | 3–4 |
| Older role (Fractal.ai) | 2 |

- Drop lowest-scoring bullets first when space is tight
- Reorder remaining bullets: highest JD relevance first

## Summary Rules

- 2–3 sentences, single paragraph
- First sentence: lead with role identity + top 3 matched JD keywords
- Second sentence: strongest quantified achievement aligned to JD
- Third sentence (optional): supporting tech stack match
- Aggressively mirror JD language while staying truthful

## Skills Reordering (ATS)

- Use **standard ATS category labels**: `Programming Languages`, `Cloud & Infrastructure`, `Observability`, `Databases`, `Backend & APIs`, `Core CS` (avoid creative names)
- Lead each row with **exact JD spellings** first (e.g. JD says "Go" → list `Go, Golang` not only Golang)
- Split into **6 compact rows** — ATS parsers scan comma-separated keywords, not paragraphs
- Group all databases in one row with `SQL, NoSQL` alongside named stores (PostgreSQL, MongoDB, etc.)
- Pull keywords only from `master/resume.yaml` skills — reorder and alias for JD terms, never invent
- Repeat top JD keywords across summary + skills + bullets naturally; do not keyword-stuff
- Mirror JD terminology: `CI/CD`, `OpenTelemetry`, `Node.js`, `REST APIs`, `Distributed Systems`
- Drop low-match keywords (e.g. Next.js, MCP) when space or relevance requires

## Project Selection

- **GameVault is always project #1** — `include: true`, listed first in `projects[]`
- **Pick exactly 1 more project** as #2 by scoring OtelForge, File Organizer, PriceTracker against the JD (use `docs/projects-catalog.yaml`)
- Set `include: false` on the other two projects
- Cross-reference catalog `highlights` when rewriting bullets (do not fabricate)
- Platform/infra/observability/cloud-native JD → **GameVault + OtelForge**
- Frontend/fullstack JD → **GameVault + PriceTracker**
- Automation/scripting JD → **GameVault + File Organizer**
- Backend/product JD → **GameVault + OtelForge** (or PriceTracker if product/web focus)
- Max 3–4 bullets per included project; trim lowest-scoring project bullets first

## Page Length Policy (Soft 1-Page)

- Target 1 page; do not auto-trim content
- If likely overflow, set status to `OVERFLOW` in jd-analysis.md
- List ranked cut suggestions (lowest JD-match bullets/projects first)
- User decides cuts in follow-up chat
- **Space priority when trimming:** never go below 2 projects — drop **Fractal.ai experience first** (entire role), then trim bullets within included projects, then other experience bullets

## Gap Policy

When JD requires something not in the bullet pool:

1. List under **Missing** in keyword coverage — do NOT add to CV
2. Under **Gap Analysis & Interview Prep**, suggest:
   - Adjacent experience that partially covers the gap
   - A honest talking point for interviews
   - Whether it's worth learning before applying

**Example:**

- Missing: Kubernetes
- Adjacent: Docker Compose 10-service stack in GameVault
- Talking point: "I've operated multi-container Docker deployments with service discovery and observability; K8s is the next step for orchestration at scale."

## Role-Type Heuristics

| JD focus | Lead with | Emphasize |
|----------|-----------|-----------|
| Frontend / Fullstack | React, GraphQL, Next.js bullets | UI delivery, data views, API integration |
| Backend / API | Node.js, Express, GraphQL, databases | Service design, data pipelines, SQL |
| Platform / Infra / SRE | OtelForge, GameVault observability | OpenTelemetry, AWS, CI/CD, Docker, automation |
| AI / ML Engineering | CodePilot, AI orchestration | SDLC skills, personas, governance, AI workflows |
| Testing / QA | pytest framework, Codecept.js | Test automation, CI/CD integration |

## Output Slug Convention

Auto-detect from JD: `{company}-{role-keywords}-{YYYY-MM-DD}`

Examples:
- `stripe-backend-sde-2026-08-24`
- `google-swe-l3-2026-08-24`

Use lowercase, hyphens, no spaces. User may rename folder after generation.
