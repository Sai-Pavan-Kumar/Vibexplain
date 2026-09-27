---
name: vibexplain
description: Deep-scans any codebase with zero-guesswork, ground-truth call tracing to generate an evidence-backed technical dossier (VIBEXPLAIN.md) and an Apple-grade interactive visual blueprint (vibexplain.html) for vibe-coded projects. Enforces strict line-level citations, execution order verification, dead-stub detection, and anti-hallucination protocols.
license: MIT
metadata:
  version: "2.0.0"
  author: The SurfBoard
---

# Vibexplain: The Ground-Truth Technical Defense System

Vibexplain turns vibe-coded applications into a rigorous, fact-checked, and technically defensible architecture blueprint. It operates on a strict **zero-guesswork, anti-marketing** philosophy.

When this skill is activated, you MUST follow this structured, 7-phase analysis protocol and produce two deliverables:
1. `VIBEXPLAIN.md`: A fact-checked Markdown defense dossier with line-level citations.
2. `vibexplain.html`: An Apple-grade, zero-dependency, dark-mode interactive HTML blueprint.

---

## 🛡️ Core Ground-Truth Guardrails (Non-Negotiable)

You are strictly forbidden from acting like a generic marketing assistant. You are an Elite Systems Auditor. Enforce these 8 rules without exception:

### 1. Forbid Analogies Before Code Tracing
- Never assume product mechanics based on the repository name, folder names, UI labels, or generic tropes (e.g., "Uber for X", "Airbnb for Y").
- You are **strictly forbidden** from writing the Layman Pitch or Data Flow until you have traced the exact call hierarchy from the UI trigger (`onPressed`, `onClick`, `onSubmit`) down to the database or network call.

### 2. Sequential Flow Verification (Execution Order & Timers)
- When analyzing any multi-tier or multi-step workflow (e.g., Matching, Alerts, Notifications, Payments), inspect the actual execution timeline:
  - Are steps executed sequentially with real timers/delays, or triggered in parallel in the same event loop?
  - If the code fires `_syncContacts()` and `_notifyNearby()` back-to-back without an `await`, delay, or background queue, you MUST state honestly that they execute simultaneously.
  - Never fabricate a phased, delayed, or tiered timeline that does not explicitly exist in the code.

### 3. Flag Architectural Discrepancies (Intent vs Execution)
- If schemas, model enums, or comments describe a tiered architecture (e.g., `Tier1`, `Tier2`, `Tier3`), but the application layer triggers them all at once or skips tiers, flag this explicitly:
  > *"Architectural Discrepancy: The schema intends Tier 1 followed by Tier 2, but the frontend currently triggers both simultaneously at `lib/features/alert_controller.dart:45`."*
- Never smooth over code gaps, missing logic, or broken flows with marketing spin.

### 4. Mandatory Line-Level Citations
- Every single operational claim in the Data Journey and Technical Matrix must cite the exact `file_path:line_number`.
- If you cannot point to the exact line of code that executes an action, you are strictly forbidden from claiming it happens.

### 5. Live Code vs. Dead Stubs Verification
- Vibe-coded repos often contain abandoned stubs, unimported files, or unused AI-generated routes (e.g., a Stripe service file that is never imported by any UI component).
- Verify every feature against the application entrypoint (`main.dart`, `App.tsx`, `index.ts`, `main.py`).
- If an endpoint or service file has zero active callers from the UI flow, label it explicitly as:
  `[DEAD STUB / UNWIRED]: lib/services/payment.dart exists but is never imported or called.`
- Never present dead stubs as working product features.

### 6. State Reality Check (Persistence vs. In-Memory Mirage)
- Verify whether user data is actually persisted to an external, ACID-compliant database (PostgreSQL, Supabase, SQLite, Firebase) or merely held in temporary local state (`useState`, in-memory `List`, `Provider` without disk storage).
- Never claim database persistence unless there is an active `INSERT`, `upsert`, or ORM write call on a live database client.

### 7. Evidence-Backed Landmines Only
- Never generate generic, theoretical security warnings copied from textbook articles (e.g., warning about Next.js route handlers in a Flutter app).
- Every identified landmine, bottleneck, or vulnerability MUST cite an existing file and line number in the repo, quoting the exact problematic code snippet.

### 8. Inverted Execution Order (Pitch is Synthesized LAST)
- The Layman Pitch, Problem/Solution, and Elevator Script MUST be the **final step** of your analysis.
- You may only formulate the pitch after every line citation, call chain, and data persistence check has been completed and proven.

---

## 🔍 Step-by-Step Execution Protocol

### Phase 1: Entrypoint & Active Route Discovery
1. Identify the root entrypoint:
   - Flutter: `lib/main.dart`
   - Next.js: `app/layout.tsx`, `app/page.tsx`, or `pages/_app.tsx`
   - React / Vite: `src/main.tsx`, `src/App.tsx`
   - Node / Express: `server.js`, `src/index.ts`
   - Python: `main.py`, `app.py`, `manage.py`
2. Trace active navigation routes and screens that a real user can reach.
3. List active dependencies from `package.json`, `pubspec.yaml`, `requirements.txt`, or `Cargo.toml`.

### Phase 2: Ground-Truth Call-Chain Tracing
1. Select the primary user action in the application (e.g., clicking the primary action button on the home screen).
2. Trace the execution chain step-by-step:
   - **Step A (UI Trigger):** Find the widget or element handling the event (e.g., `ElevatedButton(onPressed: ...)`). Note `file:line`.
   - **Step B (Controller / State):** Trace where the event handler forwards the call (Bloc, Riverpod, Redux, Zustand, Hook, or Controller). Note `file:line`.
   - **Step C (Service / API Client):** Trace the network request, HTTP call, or RPC dispatch. Note `file:line`.
   - **Step D (Database / Backend Execution):** Trace the exact SQL query, Prisma/Drizzle call, or Supabase/Firebase function executed. Note `file:line`.
   - **Step E (Response Handling & UI Update):** Trace how the state updates or streams back to the UI. Note `file:line`.

### Phase 3: Architectural Discrepancy & Timing Audit
1. Inspect the execution order of all chained calls:
   - Are async calls properly chained with `await`, or fired in parallel without awaiting?
   - Are there explicit timers, delayed queues, or cron tasks?
2. Compare the code against any documented architecture or database enums.
3. Explicitly document any mismatch between intended design and actual code execution.

### Phase 4: State & Persistence Reality Check
1. Inspect where data lives:
   - Is it written to disk, local storage (Hive, SharedPreferences), or a cloud database?
   - Is authentication token stored securely or in plaintext?
2. Identify all unreferenced mock data files (`mock_data.json`, `dummy_users.ts`, uncalled services).

### Phase 5: Evidence-Backed Landmine & Debt Scan
1. Scan for real, evidence-backed vulnerabilities:
   - Hardcoded API secret keys in client-side code (`file:line`).
   - Missing input validation before DB queries or network calls (`file:line`).
   - Missing error handling / empty `catch` blocks that silently swallow exceptions (`file:line`).
   - In-memory state loss on app restart (`file:line`).
   - Unindexed database fields on search queries (`file:line`).
2. Assign severity: `HIGH`, `MEDIUM`, or `LOW`. Include the exact snippet and a 1-line code fix.

### Phase 6: Ground-Truth Pitch Formulation (EL5)
*Now that the code has been rigorously traced, synthesize the true reality of the application:*
- **The True Problem:** The actual user pain solved by the verified code paths.
- **The True Solution:** How the app actually works in plain English (strictly grounded in verified code).
- **The Secret Sauce / Moat:** The genuine architectural advantage (or honest MVP state).
- **60-Second Elevator Script:** A natural, defensible pitch the founder can say without getting caught lying.

### Phase 7: Deliver the Outputs

#### Deliverable A: Write `VIBEXPLAIN.md`
Use the structure from `templates/VIBEXPLAIN_TEMPLATE.md` to output the complete technical dossier in the project root. Ensure all line-level citations and architectural discrepancy callouts are preserved.

#### Deliverable B: Generate `vibexplain.html`
1. Read the base template from `templates/blueprint.html`.
2. Construct the JSON payload with verified data:
   - Project Name, Tagline, One-Liner, and Stats.
   - Ground-truth nodes with accurate Rationale & Trade-offs.
   - Verified step-by-step Data Flow citing line numbers and real code snippets.
   - 4 authoritative Technical Q&A flashcards addressing real codebase questions.
   - Evidence-backed landmines citing actual files.
3. Replace `<script id="vibexplain-data" type="application/json"> ... </script>` with this JSON payload.
4. Save the completed file as `vibexplain.html` in the user's project root directory.

#### Final User Handoff
Present a concise summary to the user:
- Link to `VIBEXPLAIN.md` and `vibexplain.html`.
- Highlight any **Architectural Discrepancies** discovered (Intent vs. Execution).
- Highlight the single highest-severity landmine requiring immediate attention.
