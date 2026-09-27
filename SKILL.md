---
name: vibexplain
description: Scans any codebase to generate an executive layman pitch, architecture breakdown, "Why this stack" defense matrix, investor Q&A flashcards, and a standalone interactive visual HTML dashboard (vibexplain.html) for vibe coders. Activate when the user asks to explain their project, prepare for technical questions, audit their vibe-coded app, or generate an architectural blueprint.
license: MIT
metadata:
  version: "1.0.0"
  author: The SurfBoard
---

# Vibexplain: The Founder Technical Defense System

Vibexplain turns vibe-coded applications into a rock-solid, technically defensible project blueprint. It bridges the gap between non-technical creators and senior engineers or investors.

When this skill is activated, you MUST follow this structured, 7-step analysis and generate two deliverables:
1. `VIBEXPLAIN.md`: A comprehensive markdown defense dossier and cheat sheet.
2. `vibexplain.html`: A standalone, zero-dependency, dark-mode interactive HTML blueprint.

---

## Execution Protocol

### Step 1: Codebase Reconnaissance
Perform an automated audit of the repository:
- **Project Type & Entry Points:** Inspect `package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or Dockerfiles.
- **Frontend & Styling:** Identify frameworks (Next.js, Vite, React, Vue, Flutter) and UI libraries (Tailwind, Shadcn, Material UI).
- **Backend & API Layer:** Identify server endpoints, serverless handlers, or route handlers (`app/api`, `pages/api`, FastAPI routes, Express controllers).
- **Database & State:** Locate database schemas (`schema.prisma`, `drizzle.schema.ts`, SQL migrations, Supabase/Firebase setups).
- **Security & Auth:** Check session management (NextAuth, Clerk, Supabase Auth, Firebase Auth, JWTs).
- **3rd-Party APIs:** Detect payment gateways (Stripe), AI models (OpenAI, Anthropic), analytics, and email services.

### Step 2: Layman Pitch Formulation (EL5)
Synthesize the project without technical buzzwords:
- **Problem:** The specific human/business pain this app solves.
- **Solution:** A clear, real-world analogy (e.g., "Think of this as Uber for Pet Care" or "Git for Prompts").
- **Moat / Secret Sauce:** Why this solution is fast, cheap, or uniquely effective.
- **60-Second Elevator Script:** A natural script the founder can memorize and recite word-for-word.

### Step 3: "Why This Stack?" Matrix (Trade-offs)
For every core technology identified in the project, explain:
- **Why the AI chose it:** The speed, DX, or architectural advantage.
- **The Trade-off / Limitation:** Cold starts, vendor lock-in, memory overhead, or scaling caps.
- **A Tough Technical Question:** A realistic question a senior engineer would ask about this choice.
- **The Defensible Answer:** The exact counter-argument showing technical maturity.

### Step 4: Map the Primary Data Journey
Identify the single most critical user journey in the app (e.g., "User creates an account and generates their first report"):
- Break down the request across 4 to 6 discrete steps:
  1. User input in UI (Browser)
  2. Edge Guard / Middleware / Schema Validation
  3. Database lookup / Atomic transaction
  4. External API call / Background worker
  5. UI response streaming / Optimistic update
- Extract actual short code snippets from the repo where possible.
- Draft a clean Mermaid sequence/flowchart diagram.

### Step 5: The "Investor & Senior Dev Grill" Matrix
Anticipate 4 to 6 difficult questions that interviewers, investors, or senior tech evaluators will ask:
1. Concurrency & High Traffic (What happens if 1,000 users hit this simultaneously?)
2. Security & Injection (How are SQL injection / XSS attacks prevented?)
3. Secrets & Client Exposure (Are API keys exposed in the frontend bundle?)
4. Database Scaling & N+1 Queries (How are joins and relation queries indexed?)
5. Data Loss & Failure Handling (What happens if a 3rd party API goes down mid-request?)
*Provide clear, assertive, and technically sound answers.*

### Step 6: AI Spaghetti & Landmines Audit
Scan the codebase for common vibe-coding pitfalls:
- Missing rate limits on public API endpoints (API bill explosion risk).
- Unindexed database foreign keys or search fields.
- Hardcoded secrets or client-exposed environment variables.
- Raw unvalidated user inputs (missing Zod, Joi, or Pydantic validation).
- Missing error boundary or silent try/catch blocks that swallow failures.
*List each landmine with Severity (HIGH, MEDIUM, LOW), the exact file path, impact, and a 1-line code fix.*

### Step 7: Deliver the Outputs

#### Deliverable A: Write `VIBEXPLAIN.md`
Use the structure from `templates/VIBEXPLAIN_TEMPLATE.md` to output the complete technical dossier in the project root.

#### Deliverable B: Generate `vibexplain.html`
1. Read the base template from `templates/blueprint.html`.
2. Construct a JSON payload matching the `vibexplain-data` structure:
   ```json
   {
     "projectName": "...",
     "projectTagline": "...",
     "oneLiner": "...",
     "filesCount": 0,
     "stackCount": 0,
     "timestamp": "...",
     "stats": {
       "securityScore": "XX%",
       "scaleFit": "XX%",
       "landminesCount": 0
     },
     "pitch": {
       "problem": "...",
       "solution": "...",
       "moat": "...",
       "elevatorScript": "..."
     },
     "nodes": [ ... ],
     "dataFlow": [ ... ],
     "flashcards": [ ... ],
     "landmines": [ ... ]
   }
   ```
3. Replace the contents of `<script id="vibexplain-data" type="application/json"> ... </script>` with this new JSON payload.
4. Save the completed file as `vibexplain.html` in the user's project root directory.

#### Final User Handoff
Present a concise summary to the user:
- Point them to `VIBEXPLAIN.md` for their technical cheat sheet.
- Direct them to open `vibexplain.html` directly in their web browser to explore the interactive visual blueprint.
- Highlight the single highest-severity landmine that needs immediate attention.
