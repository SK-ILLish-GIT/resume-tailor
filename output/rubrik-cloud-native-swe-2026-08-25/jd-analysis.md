# JD Analysis — Rubrik / Software Engineer — Cloud Native Protection / 2026-08-25

## Keyword Coverage

### Matched
| Keyword | Where it appears |
|---------|------------------|
| Distributed systems | Summary, Zscaler, GameVault, skills (Concepts) |
| Cloud / cloud-native | Summary, Zscaler (AWS), GameVault, experience bullets |
| Python | Summary, Zscaler, skills (Languages) |
| Golang / Go | Summary, Zscaler, skills (Languages) |
| C++ | Skills (Languages) |
| AWS | Summary, Zscaler (OtelForge), skills |
| Docker | Summary, GameVault, skills (DevOps) |
| Microservices / microservice architecture | Summary, GameVault bullets |
| OpenTelemetry / observability | Summary, Zscaler, GameVault |
| CI/CD | Summary, Zscaler (GitLab), skills |
| Design, develop, test, deploy, maintain | Zscaler pytest bullet, Highspot delivery bullets |
| SDLC | Highspot CodePilot bullet, Fractal testing bullet |
| Problem-solving (DSA) | Certifications — CodeChef, Codeforces, LeetCode |
| Collaboration / cross-functional | Highspot, Fractal bullets |
| Data security / PII handling | Zscaler PII masking bullet (adjacent to cloud data protection) |
| Bachelor's CS/related | Education — B.Tech IT, IIIT Allahabad |
| Software engineering principles | OOP, Distributed Systems in skills |

### Missing (NOT added to CV)
- Java, Scala (explicitly named in JD languages)
- Azure, GCP (only AWS in master)
- Kubernetes (Docker Compose only — adjacent experience exists)
- 2+ years formal experience (candidate has ~8 months full-time SDE + internships)
- Cloud data protection / cyber resilience domain keywords (Rubrik-specific)
- Design patterns (as explicit skill phrase)

**Coverage:** ~72%

## Tailoring Decisions

### Summary
Rewrote to lead with **cloud-native distributed systems**, **Python**, **Golang**, **AWS**, **Docker**, and **OpenTelemetry** — directly mirroring Rubrik's Cloud Native Protection stack. Emphasized design/deploy/maintain lifecycle and SDLC practices. Removed React/GraphQL-heavy frontend framing.

### Experience

**Highspot (3 bullets kept, reordered & rewritten):**
- **Led with:** CodePilot — SDLC skills, governance, engineering practices across 5 teams
- **Rewrote:** GraphQL scorecard → scalable platform feature delivery
- **Rewrote:** Feature flag tool → distributed platform tooling (kept, reframed from React focus)
- **Dropped:** React chart blueprint bullet (low cloud/infra match)

**Zscaler (4 bullets kept — highest JD overlap):**
- **Kept/rewrote:** OtelForge → cloud platform on AWS EC2 for distributed production systems
- **Kept/rewrote:** Golang + RabbitMQ → distributed cloud infrastructure workers
- **Kept/rewrote:** OpenTelemetry + PII masking → secure data handling (adjacent to cloud data protection)
- **Kept/rewrote:** pytest + GitLab CI/CD → design, test, deploy, maintain software releases

**Fractal.ai:** Dropped entirely to make room for GameVault + OtelForge (2-project minimum policy; Fractal is first cut for space)

### Projects
- **#1 (always):** GameVault — 3 bullets (Docker microservices, Nginx/API gateway + data stores, MELT observability)
- **#2 (JD match):** OtelForge — 3 bullets (OTel pipelines, RabbitMQ/Go orchestration, TLS/multi-signal telemetry)
- **Excluded:** File Organizer, PriceTracker (`include: false`)
- **Space:** Dropped Fractal.ai experience entirely; trimmed Zscaler to 3 bullets and GameVault from 4→3

### Skills
- Reordered: **Languages** (Golang, Python, C++ lead)
- **DevOps & Observability** — Docker, OTel, Prometheus, Grafana, Loki, Tempo, RabbitMQ (aligned to GameVault + OtelForge)
- **Backend & Microservices** — Node.js, Express, Nginx, microservices (GameVault stack)
- **Cloud & Databases** — AWS, PostgreSQL, MongoDB, Redis

## Page Length

**Status:** fits 1 page

Tailoring dropped 1 Highspot bullet (React charts) and excluded PriceTracker. Four Zscaler + four GameVault bullets may be tight — monitor overflow; likely fits given prior Popclub variant fit comfortably.

## Gap Analysis & Interview Prep

**Missing: 2+ years experience**
- Adjacent: 8 months full-time SDE at Highspot + 6-month Zscaler internship + Fractal internship; graduated June 2025
- Talking point: "I have production experience across two companies including building a cloud observability platform at Zscaler and currently shipping platform features at Highspot. My internship-to-full-time progression and competitive programming background (1600+ DSA problems) compensate for tenure with depth of technical delivery."

**Missing: Kubernetes**
- Adjacent: 10-service Docker Compose stack + 8-container observability overlay in GameVault; OtelForge managing 20+ AWS EC2 instances
- Talking point: "I've built and operated multi-container Docker deployments with service discovery, API gateways, and full observability stacks. Kubernetes is the natural next step for orchestration at scale — my foundation in containerized microservices maps directly."

**Missing: Java / Scala**
- Adjacent: Strong Golang and Python production experience; C++ in skills
- Talking point: "My systems work is primarily in Go and Python — both widely used at Rubrik-scale infrastructure companies. Language is an implementation detail; my strength is distributed systems design and cloud deployment patterns."

**Missing: Azure / GCP**
- Adjacent: AWS EC2 deployment and management at scale (OtelForge, 20+ instances)
- Talking point: "I've deployed and managed production workloads on AWS. Cloud primitives — compute, networking, IAM, monitoring — transfer across providers; I've operated at the infrastructure layer where the concepts are provider-agnostic."

**Missing: Cloud data protection domain**
- Adjacent: PII masking in OpenTelemetry pipelines at Zscaler; secure data handling in distributed logs/traces
- Talking point: "At Zscaler I built telemetry infrastructure with PII redaction for secure log and trace handling — directly relevant to protecting sensitive cloud data. Rubrik's mission to secure cloud data at scale aligns with the security-conscious platform work I've done."

## ATS Tips

- Rubrik Cloud Native Protection is a **platform/infra** role — your OtelForge + GameVault observability stack is the strongest differentiator; ensure these are discussed prominently in cover letter
- Mirror JD verbs in interviews: **design, develop, test, deploy, maintain, improve**
- `#LI-PM2` suggests LinkedIn sourcing — optimize LinkedIn headline to include "Cloud / Distributed Systems / Golang / AWS"
- Rubrik values **self-starters who manage themselves** — CodePilot (built independently, adopted by 5 teams) and GameVault (personal project, 10-service stack) demonstrate initiative
- Apply with cover letter connecting Zscaler security telemetry + PII work to cloud data protection mission
