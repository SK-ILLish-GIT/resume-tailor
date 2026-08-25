# JD Analysis — LG Ad Solutions / Software Engineer I / 2026-08-25

## Keyword Coverage

### Matched

| Keyword | Where |
|---------|-------|
| Python | summary, Zscaler experience, skills |
| Go / Golang | summary, Zscaler experience, OtelForge project, skills |
| JavaScript | summary, Fractal experience, skills |
| C++ | skills |
| Data structures & algorithms | skills (Core CS), certifications (1600+ DSA problems) |
| MySQL | Fractal experience, skills |
| Redis | GameVault project, skills |
| MongoDB | Highspot tech stack, GameVault project, skills |
| AWS | summary, Zscaler experience, skills |
| CI/CD | summary, Zscaler experience, skills |
| Distributed systems | summary, Zscaler, GameVault, OtelForge, skills |
| Scalable / performant systems | summary, GameVault project bullets |
| React.js | Highspot experience, GameVault, OtelForge, skills |
| Testing | Zscaler (pytest 50+ cases), Fractal (Codecept.js) |
| Cloud-native | summary, OtelForge project |
| Data pipelines | summary (telemetry/measurement pipelines), Zscaler OTel collection |
| Measurement systems | summary, Highspot scorecard, GameVault observability |
| SQL / NoSQL | Highspot (GraphQL+SQL), skills |
| Git / collaborative workflows | CI/CD integration implies Git workflows |
| Bachelor's CS degree | education (B.Tech IT, IIIT Allahabad) |

### Missing (NOT added to CV)

| Keyword | Notes |
|---------|-------|
| Scala | Not in master resume |
| HDFS | Not in master resume |
| Spark | Not in master resume |
| Databricks | Not in master resume |
| Kubernetes | Not in master resume |

**Coverage:** 18/23 core keywords ≈ **78%** (excluding "eagerness to learn" framing for Spark/K8s)

## Tailoring Decisions

### Summary

Rewrote to lead with **Software Engineer + scalable distributed systems + Python/Go/JavaScript** — the JD's top language and systems requirements. Second sentence anchors quantified scale (20+ AWS EC2, 10-service stack) and database breadth (PostgreSQL, MongoDB, Redis, MySQL). Third sentence mirrors JD language around **CI/CD, well-tested code, and measurement/data pipelines** without claiming ad-tech domain experience.

### Experience

**Highspot (4 bullets kept, reordered):**
- Promoted GraphQL+SQL scorecard to #1 — aligns with measurement/analytics and database familiarity
- Moved React.js blueprint visualizations to #2 — hits preferred ReactJS exposure
- Kept CodePilot for team scale (50+ engineers) and operational excellence framing
- Kept feature flags last — still demonstrates GraphQL/React but lower JD relevance

**Zscaler (4 bullets kept, aggressively rewritten):**
- Reframed OtelForge as **scalable platform + measurement/telemetry pipelines** (ad measurement adjacency)
- Emphasized **async Go workers + RabbitMQ** for distributed system components
- Reframed OTel sampling as **telemetry data collection** with PII handling
- Highlighted **pytest + GitLab CI/CD + 50+ test cases** for JD's testing/CI/CD requirements

**Fractal.ai (2 bullets kept, reordered):**
- Led with MySQL/Node.js project work — database requirement
- Kept test automation bullet — clean code/testing best practices

### Projects

**Included:** GameVault (#1, always) + OtelForge (#2)
- GameVault scores highest on distributed systems, scalable architecture, Redis/MongoDB/PostgreSQL, React.js, and measurement/observability
- OtelForge adds Go, AWS-adjacent cloud deployment, RabbitMQ async workers, PostgreSQL, Docker, cloud-native platform work
- OtelForge beats PriceTracker (React/MongoDB but weaker on distributed systems) and File Organizer (scripting-only) for this backend/platform JD

**Excluded:** File Organizer, PriceTracker (`include: false`)

**Bullet rewrites:**
- GameVault lead bullet now uses JD terms "scalable, performant" and "distributed system operations"
- Measurement language added to observability bullet (maps to ad measurement systems)
- OtelForge lead bullet uses "cloud-native platform" per preferred qualifications

### Skills

Reordered into 6 standard ATS rows per playbook:
1. **Programming Languages** — Python, Go first (JD order), then JavaScript, C++
2. **Cloud & Infrastructure** — AWS, Docker, CI/CD, Distributed Systems
3. **Databases** — all four JD-mentioned stores where applicable (MySQL, Redis, MongoDB) plus PostgreSQL
4. **Backend & APIs** — Node.js, GraphQL, REST, React.js
5. **Observability** — relevant for measurement/telemetry angle
6. **Core CS** — Data Structures, Algorithms explicit for JD requirement

Dropped: Next.js, MCP, AI Orchestration (low JD match, space optimization)

## Page Length

**Status:** OVERFLOW — likely 1.1–1.2 pages with 4 Highspot + 4 Zscaler + 2 Fractal + 8 project bullets + certifications

### Suggested Cuts (if overflow)

1. Drop Highspot feature flag bullet (lowest JD match among experience)
2. Drop OtelForge security/JWT bullet (least relevant to ad serving JD)
3. Drop Fractal.ai entire role (playbook: drop before going below 2 projects)
4. Trim GameVault observability bullet to 3 project bullets total
5. Drop Highspot CodePilot bullet if still tight

## Gap Analysis & Interview Prep

- **Missing: Scala**
  - Adjacent experience: Strong Python, Go, JavaScript, C++ — polyglot backend engineer
  - Talking point: "I haven't used Scala in production, but I'm comfortable picking up JVM-family languages — my competitive programming background (CodeChef 4-star, Codeforces Specialist) gives me strong fundamentals for functional/OOP paradigms Scala uses."

- **Missing: Spark / Databricks**
  - Adjacent experience: Built telemetry data collection pipelines with OpenTelemetry; async job processing with RabbitMQ; batch deployment across 50+ nodes
  - Talking point: "I've worked on data collection and batch processing at scale with OTel pipelines and message-queue workers. Spark would be the distributed compute layer I'd apply those pipeline patterns to — I'm actively interested in learning it for large-scale ad measurement workloads."

- **Missing: Kubernetes**
  - Adjacent experience: 10-service Docker Compose stack (GameVault), cloud-native OtelForge deployment, 20+ AWS EC2 instance management
  - Talking point: "I've built and operated multi-container Docker deployments with service discovery and observability overlays. Kubernetes is the natural next step for orchestrating those patterns at LG Ad Solutions' scale."

- **Missing: HDFS**
  - Adjacent experience: PostgreSQL, MongoDB, Redis multi-store architecture; AWS S3 in skills
  - Talking point: "My experience spans relational, document, and in-memory stores plus cloud object storage. HDFS would extend that to distributed file storage for big data pipelines — I'd connect it to the Spark learning path."

- **Domain gap: Ad serving / CTV advertising**
  - Adjacent experience: High-throughput backend services, measurement/analytics (scorecard, telemetry), targeting-adjacent feature flag dependency mapping
  - Talking point: "While I haven't worked in ad tech specifically, I've built measurement systems, analytics data views, and high-throughput distributed backends — the same engineering fundamentals LG Ad Solutions applies to ad serving latency and measurement accuracy."

## ATS Tips

- Apply via the LG Ad Solutions careers portal; paste this PDF — avoid column layouts (already handled by LaTeX template)
- Lead with **Python, Go, distributed systems, AWS, CI/CD** in any cover letter or application text fields
- Mention **eagerness to learn Spark and Kubernetes** in cover letter — JD explicitly welcomes learners
- Bangalore location aligns with Zscaler intern experience (Bangalore) — worth noting in cover letter
- Competitive programming credentials (1600+ DSA, LeetCode Knight) directly address "strong understanding of data structures and algorithms"
- If asked about big data: frame GameVault + OtelForge as **distributed systems portfolio**, OTel work as **measurement pipeline** experience
