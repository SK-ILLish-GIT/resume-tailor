# JD Analysis — Popclub / SDE-1 Backend / 2026-08-25

## Keyword Coverage

### Matched

| Keyword | Where |
|---------|-------|
| Python | summary, Zscaler, skills |
| Go / Golang | summary, Zscaler, OtelForge, skills |
| REST APIs | summary, Fractal, GameVault, OtelForge, skills |
| SQL | Highspot experience, GameVault, skills |
| NoSQL / MongoDB | Highspot tech stack, GameVault, skills |
| Data Structures & Algorithms | summary, certifications (1600+ problems), skills |
| OOP | skills (Core CS) |
| Git / version control | Zscaler (GitLab CI/CD + Git), skills |
| Scalable systems | summary, Zscaler, GameVault bullets |
| Production systems | summary, Highspot, Zscaler, Fractal bullets |
| Unit testing | Zscaler (pytest 50+), Fractal (Codecept.js), skills |
| AWS | summary, Zscaler, OtelForge, skills |
| Backend frameworks | OtelForge Go Fiber (Gin/Echo-adjacent), Express.js in GameVault |
| Product development | Fractal, GameVault, OtelForge project bullets |
| Clean/maintainable code | Zscaler pytest, Highspot CodePilot governance framing |
| Code reviews | Highspot bullet |
| Bug fixing / performance | Fractal testing bullet, Highspot performance bullet |
| Cross-functional collaboration | Highspot (5 teams, 50+ engineers) |
| 1–2 years experience | ~1 yr FT + internships — within range |
| Problem-solving | certifications (CodeChef 4★, Codeforces Specialist, LeetCode Knight) |

### Missing (NOT added to CV)

| Keyword | Notes |
|---------|-------|
| Java | Not in master resume |
| Gin / Echo / Django / FastAPI / Spring Boot (explicit) | Go Fiber and Express.js are adjacent frameworks |
| Fintech / payments / UPI domain | Not in master resume |

**Coverage:** 20/23 core keywords ≈ **87%**

## Tailoring Decisions

### Summary

Rewrote for **backend SDE-1** identity — Python, Go, Node.js, REST APIs, SQL/NoSQL, production systems, unit testing, AWS. Explicitly mentions **DSA fundamentals** since Popclub weights competitive programming heavily for junior hires and welcomes fresh grads with strong fundamentals.

### Experience

**Highspot (4 bullets, backend-reframed):**
- GraphQL+SQL scorecard led — backend data layer and query performance
- Feature flags reframed as **GraphQL backend APIs** at production scale (2000+)
- CodePilot reframed as **backend workflows + cross-functional collaboration** (de-emphasized AI)
- React chart bullet kept last with **code reviews and performance improvements** — hits JD responsibilities

**Zscaler (4 bullets):**
- Clean Python/Go production code on AWS — direct JD language
- Go RabbitMQ backend workers
- Python data module + bug/reliability framing
- pytest + **Git version control** explicit (was gap in prior variant)

**Fractal.ai (2 bullets):**
- Node.js + MySQL REST APIs — product development
- Unit/E2E testing + bug fixing — JD responsibilities

### Projects

**Included:** GameVault + OtelForge (catalog pairing: `popclub-backend-sde1: otelforge`)
- Trimmed to **3 bullets each** (vs 4) to reduce overflow for junior role — dropped observability-heavy bullets
- GameVault: REST APIs, Express backend, PostgreSQL/MongoDB/Redis, caching
- OtelForge: Go Fiber REST API (Gin/Echo adjacency), PostgreSQL, RabbitMQ, AWS, product lifecycle

**Excluded:** File Organizer, PriceTracker

### Skills

6 compact ATS rows tuned for junior backend:
1. **Programming Languages** — Python, Go first (JD order)
2. **Cloud & Infrastructure** — AWS, Docker, CI/CD, **Git**
3. **Databases** — PostgreSQL, MongoDB, MySQL, SQL, NoSQL
4. **Backend & APIs** — REST APIs, Express.js, GraphQL
5. **Testing & Quality** — pytest, Unit Testing (good-to-have explicit)
6. **Core CS** — Data Structures, Algorithms, OOP

Dropped: MCP, AI Orchestration (low match for backend SDE-1 fintech)

## Page Length

**Status:** fits 1 page (trimmed project bullets to 3 each; backend-focused framing)

### Suggested Cuts (if overflow)

1. Drop Highspot React chart bullet
2. Drop Zscaler PII/Python data module bullet
3. Drop Fractal.ai entire role
4. Trim GameVault JWT bullet

## Gap Analysis & Interview Prep

- **Missing: Java**
  - Adjacent: Production Python and Go backends
  - Talking point: "My backend experience is in Python and Go. Java's OOP and JVM patterns are familiar from CS coursework — I'd ramp quickly on Popclub's stack."

- **Missing: Gin / Django / FastAPI (explicit)**
  - Adjacent: Go Fiber REST API (OtelForge), Express.js (GameVault), Python pytest pipelines (Zscaler)
  - Talking point: "I've built production REST APIs in Go Fiber and Express.js — same MVC/middleware patterns as Gin and FastAPI."

- **Missing: Fintech / payments domain**
  - Adjacent: Production SaaS at Highspot, backend systems handling sensitive data (PII masking at Zscaler), product development (Fractal, GameVault)
  - Talking point: "I haven't built payment systems, but I've shipped production backend features in fast-paced product teams and handled sensitive data with care — the same reliability POP UPI requires."

- **Location advantage:** Zscaler intern was in **Bangalore**; role is **HSR Layout, Bengaluru** — mention in cover letter

- **SDE-2 Agentic opening:** If backend SDE-1 doesn't fit, CodePilot experience qualifies for their Agentic SDE-2 role

## ATS Tips

- Popclub is Razorpay-backed fintech — lead with **production backend + DSA creds** in cover letter
- SDE-1 bar is fundamentals-heavy — certifications section (LeetCode Knight, 1600+ DSA) is a major asset; ensure PDF renders it clearly
- Keep resume to 1 page for junior role — this variant is trimmed accordingly
- Mention willingness to work from HSR Layout (hybrid/on-site as applicable)
- Backend frameworks: say "Go Fiber (Gin-equivalent)" in interview if asked — don't add Gin to CV (not in master)
