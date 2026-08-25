# JD Analysis — Rappi Turbo / Fullstack Engineer / 2026-08-25

## Keyword Coverage

### Matched

| Keyword | Where |
|---------|-------|
| Full-stack / backend-heavy | summary, Fractal, GameVault bullets |
| Python | summary, Zscaler experience, skills |
| Go / Golang | summary, Zscaler, OtelForge, skills |
| Node.js | summary, Highspot, Fractal, GameVault, skills |
| REST APIs | GameVault, Fractal, OtelForge, skills |
| Microservices | summary, GameVault, skills |
| PostgreSQL | GameVault, OtelForge, skills |
| MongoDB | Highspot tech stack, GameVault, skills |
| Redis / caching | GameVault (caching strategies), skills |
| Docker | GameVault, OtelForge, skills |
| AWS | Zscaler, OtelForge, skills |
| AI agents / agentic workflows | Highspot CodePilot (multi-step skills, personas, guardrails) |
| Tool-using agents | CodePilot (15+ reusable SDLC skills, governance) |
| Guardrails / authorization / validation | CodePilot, OtelForge bullets |
| Human-in-the-loop | OtelForge (rerun-failed controls, rollback) |
| Multi-step workflows | CodePilot, OtelForge batch workflows |
| Batch processing pipelines | Zscaler, OtelForge (RabbitMQ batch events) |
| Real-time pipelines | OtelForge (live job output), GameVault (real-time dashboard) |
| High-volume data processing | Highspot (2000+ flags), Zscaler telemetry pipelines |
| Data-intensive platforms | summary, Highspot scorecard (15 data views) |
| React / dashboards | Highspot, GameVault planning dashboard bullets |
| CI/CD | Zscaler GitLab CI/CD, skills |
| Observability / tracing decisions | GameVault, Zscaler (LLM eval adjacency) |
| Distributed systems | Zscaler, GameVault, OtelForge, skills |
| Bachelor's CS/IT degree | education (B.Tech IT, IIIT Allahabad) |
| 0-2 years experience | ~1 yr FT + internships — within range |
| Analytical thinking | certifications (1600+ DSA, competitive programming) |

### Missing (NOT added to CV)

| Keyword | Notes |
|---------|-------|
| Django | Not in master resume |
| Kotlin / Java | Not in master resume |
| LangGraph / CrewAI | Not in master resume (AI Orchestration/MCP adjacent) |
| RAG / vector stores (pgvector, Pinecone) | Not in master resume |
| GCP | AWS only |
| Supply chain / logistics / quick commerce domain | Not in master resume |
| Optimization algorithms / forecasting | Not in master resume |

**Coverage:** 28/35 core keywords ≈ **80%**

## Tailoring Decisions

### Summary

Rewrote to lead with **backend-heavy full-stack + scalable APIs + data-intensive platforms + Python/Go/Node.js** — exact JD stack and role identity. Second sentence anchors **CodePilot (AI agent workflows, 50+ engineers)** — the JD's single hardest qualification to meet. Third sentence hits **PostgreSQL/MongoDB/Redis + batch and real-time pipelines** for supply chain planning platform adjacency.

### Experience

**Highspot (4 bullets kept, aggressively rewritten):**
- **CodePilot** reframed as **production AI agent orchestrator** with multi-step skills, tool-using agents, governance guardrails, validation/authorization — direct mirror of JD's entire AI agents section
- **GraphQL+SQL scorecard** reframed as **planning/analytics data views** on data-intensive operational dashboards
- **Feature flags** reframed as **large-scale dataset processing** (2000+ entities)
- **React charts** reframed as **planning dashboards** — good-to-have frontend match

**Zscaler (4 bullets kept, rewritten):**
- OtelForge as **high-volume data pipeline platform** on AWS
- RabbitMQ as **batch + real-time decision pipelines**
- OTel collection as **high-volume data processing and transformation**
- pytest CI/CD for **observability and code quality**

**Fractal.ai (2 bullets kept):**
- Node.js + MySQL REST APIs — relational backend
- Full-stack test coverage

### Projects

**Included:** GameVault (#1, always) + OtelForge (#2)
- GameVault: microservices REST APIs, PostgreSQL data models, Redis caching, React dashboard, observability for tracing regressions
- OtelForge: batch workflows, PostgreSQL state, guardrails/authorization, human-in-the-loop controls, AWS Docker deployment
- PriceTracker has thin LLM usage (Gemini descriptions) — CodePilot in experience is the stronger agentic story; OtelForge wins on batch/platform scale

**Excluded:** File Organizer, PriceTracker (`include: false`)

### Skills

Reordered into 6 ATS rows with **AI Orchestration and MCP retained**:
1. **Programming Languages** — Python, Go, Node.js first (JD order)
2. **Cloud & Infrastructure** — Docker, AWS, Microservices
3. **Databases** — PostgreSQL, MongoDB, Redis explicit
4. **Backend & APIs** — REST APIs, GraphQL
5. **AI & Observability** — AI Orchestration, MCP (agent stack), OpenTelemetry (LLM eval adjacency)
6. **Core CS** — Data Structures, Algorithms

## Page Length

**Status:** OVERFLOW — likely 1.1–1.2 pages

### Suggested Cuts (if overflow)

1. Drop Highspot feature flag bullet (2000+ scale already implied elsewhere)
2. Drop GameVault observability bullet (covered in Zscaler)
3. Drop Fractal.ai entire role
4. Trim OtelForge Docker/AWS bullet to 3 project bullets

## Gap Analysis & Interview Prep

- **Missing: RAG / vector stores / LangGraph / CrewAI**
  - Adjacent experience: CodePilot multi-step agent orchestration with 15+ skills and context management; MCP in skills
  - Talking point: "CodePilot orchestrates multi-step agent workflows with specialized personas and governance guardrails — the same architectural patterns LangGraph uses for stateful agent graphs. RAG with pgvector would extend my agents with supply chain SOPs and supplier context at decision time."

- **Missing: Django**
  - Adjacent experience: Python production code (Zscaler OTel pipelines, pytest), Node.js/Express REST APIs, Go Fiber REST API
  - Talking point: "My Python backend work is in data pipelines and test automation; my REST API experience spans Express, Fiber, and GraphQL. Django's ORM and admin patterns map directly to the PostgreSQL data models I've built in GameVault and OtelForge."

- **Missing: Supply chain / quick commerce domain**
  - Adjacent experience: Planning dashboards (scorecard, GameVault), batch replenishment-like workflows (OtelForge batch deploy + rollback), inventory-state management (PostgreSQL + Redis caching in GameVault)
  - Talking point: "OtelForge's batch workflow engine — pre/post verification, rollback, human-in-the-loop escalation — mirrors supply chain replenishment decision pipelines. GameVault's Redis-cached leaderboard is structurally similar to inventory position caching for high-throughput planning queries."

- **Missing: Optimization algorithms**
  - Adjacent experience: 1600+ DSA problems, competitive programming (CodeChef 4★, Codeforces Specialist)
  - Talking point: "Strong algorithmic foundation from competitive programming. I'd partner with Rappi's data science team on optimization modules while owning the platform infrastructure that runs them at scale."

- **Strong differentiator: CodePilot**
  - JD requires "at least one agentic or LLM-powered application beyond a thin API wrapper" — CodePilot with 15+ skills, 3 personas, guardrails, and 50+ engineer adoption is the standout qualification match

## ATS Tips

- Role asks 0-2 years — your ~1 yr FT + internships is ideal; don't oversell seniority
- Lead cover letter with **CodePilot agent story + OtelForge batch pipeline story** — together they map to both halves of the JD (AI agents + supply chain platform infrastructure)
- Mention willingness to relocate to Mumbai (hybrid)
- PriceTracker Gemini AI is a secondary LLM project if asked — but CodePilot is primary
- System design prep: OtelForge batch workflow architecture as a planning pipeline design; GameVault caching layer as inventory query optimization story
