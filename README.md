<div align="center">

<img src="vibexplain-logo.webp" alt="Vibexplain Logo" width="120" style="border-radius: 20px; margin-bottom: 12px;" />

# ⚡ Vibexplain
### The Founder Technical Defense System for Vibe Coders

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![Compatible With](https://img.shields.io/badge/Supports-Antigravity%20%7C%20Claude%20Code%20%7C%20Cursor-violet)](https://github.com)

**Turn vibe-coded projects into rock-solid, technically defensible architectural blueprints in 60 seconds.**

[Explore Live Demo Blueprint](examples/vibexplain_sample.html) • [View Sample Dossier](examples/VIBEXPLAIN_SAMPLE.md) • [Install Skill](#-installation--usage)

</div>

---

## 💡 The Problem

You spent the weekend vibe-coding a SaaS using **Cursor**, **Lovable**, **v0**, or **Claude Code**. The app works, looks great, and has early users. 

**Then comes the dread:**
- An angel investor asks: *"How does your auth architecture handle edge sessions?"*
- A senior dev friend asks: *"Why did your AI pick Prisma over Drizzle, and how do you handle serverless connection pooling?"*
- A potential enterprise client asks: *"Is your backend vulnerable to DDoS or SQL injection?"*

You freeze because you didn't write the code—your AI did.

**Vibexplain solves this.** Unlike generic AI summarizers that guess based on your project title, Vibexplain runs a **Ground-Truth Code Trace** from UI event handlers down to database queries. It produces an evidence-backed dossier and an Apple-grade interactive visual blueprint so you can defend your technical choices with bulletproof confidence.

---

## 🛡️ The Ground-Truth Engine (Zero Guesswork & Anti-Hallucination)

Generic AI tools hallucinate. They read a project name like *"BloodRadar"* or *"Eventime"*, assume it's *"Uber for X"*, and fabricate complex background queues that don't exist in your code.

Vibexplain is governed by **8 non-negotiable guardrails**:

1. **Forbid Analogies Before Code Tracing:** The Layman Pitch is strictly synthesized *last*. No assumptions based on project names or UI text.
2. **Sequential Flow Verification:** Checks actual execution timing. If two services execute in parallel in the same second without delays, it states that fact honestly.
3. **Architectural Discrepancy Detection:** Flags mismatches where schemas intend tiered stages, but the frontend blasts them simultaneously.
4. **Mandatory Line-Level Citations:** Every claim in the request flow must cite `file_path:line_number`. No citation = forbidden from claiming it happens.
5. **Live Code vs. Dead Stubs:** Distinguishes between reachable user flows and abandoned, unimported AI mock files.
6. **Persistence Reality Check:** Distinguishes real database commits from temporary in-memory state or local array mocks.
7. **Evidence-Backed Landmines Only:** Zero generic textbook warnings. Every vulnerability quotes an existing file and line in the repo.
8. **Inverted Execution Order:** Ground-truth facts are proven first; the elevator pitch is distilled last.

---

## 🚀 What Vibexplain Delivers

When invoked on any codebase, Vibexplain produces two zero-dependency artifacts right in your root directory:

### 1. 🗺️ `vibexplain.html` (Interactive Visual Blueprint)
A single, zero-dependency, dark-mode dashboard that runs locally in any browser:
- **Interactive Component Node Map:** Click each stack component (ORM, Auth, Framework) to see why your AI picked it, how it interacts, and real-world trade-offs.
- **Request Lifecycle Simulator:** An animated step-by-step player showing how data travels from user clicks to DB transactions and back.
- **Investor & Tech Grill 3D Flashcards:** Interactive flip cards featuring tough engineering interview/pitch questions with concise, defensible answers.
- **AI Landmine & Debt Radar:** Color-coded severity alerts highlighting missing rate limiters, unindexed DB tables, or unvalidated inputs.

### 2. 📄 `VIBEXPLAIN.md` (Executive Defense Dossier)
A complete Markdown reference cheat sheet containing:
- **The 60-Second Layman Pitch (EL5):** Natural, jargon-free problem/solution scripts to explain your app to non-tech founders or investors.
- **The "Why This Stack?" Matrix:** Engineering rationale and limitations for every tool in your project.
- **Mermaid Sequence Diagrams:** Copy-paste diagrams ready for slide decks and pitch documents.
- **Top 10 Technical Grill Questions:** Exact words to say when questioned by engineers.

---

## 📦 Installation & Usage

You can use Vibexplain across all major AI agent environments:

### Option A: Antigravity IDE / CLI
Clone or copy this repository into your personal skills directory:
```bash
git clone https://github.com/Sai-Pavan-Kumar/Vibexplain.git ~/.gemini/antigravity/skills/vibexplain
```
Inside any project in Antigravity, simply prompt:
> *"Run Vibexplain on my codebase and generate my architecture blueprint."*

### Option B: Claude Code
Copy the `vibexplain` folder to your project or global Claude directory:
```bash
cp -r vibexplain/ .claude/skills/vibexplain/
```
Then ask Claude Code:
> *"Use the vibexplain skill to analyze this repository."*

### Option C: Cursor / Windsurf
Add `SKILL.md` to your `.cursorrules` or ask Cursor Agent:
> *"Read SKILL.md in the vibexplain folder and generate VIBEXPLAIN.md and vibexplain.html for this project."*

### Option D: Standalone Python CLI
Run the lightweight scanner directly without any agent setup:
```bash
python scripts/vibexplain.py .
```

---

## 📸 Interactive Dashboard Preview

The generated `vibexplain.html` requires **no build tools, no `npm install`, and zero server setup**. Double-click it to inspect:

```
┌─────────────────────────────────────────────────────────────────┐
│ ⚡ Vibexplain | PromptStudio AI Blueprint      [Export PDF] [⭐]│
├─────────────────────────────────────────────────────────────────┤
│ [🗺️ Architecture]  [⚡ Data Journey]  [🃏 Grill-Me]  [⚠️ Landmines] │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────────┐     ┌───────────────┐     ┌───────────────┐  │
│  │ Next.js 15    │ ──> │ Prisma ORM    │ ──> │ PostgreSQL    │  │
│  │ (App Router)  │     │ (Type Safety) │     │ (ACID DB)     │  │
│  └───────────────┘     └───────────────┘     └───────────────┘  │
│                                                                 │
│  🃏 FLASHCARD: "What happens if 1,000 users click Run Test?"   │
│  [Tap to reveal confident defense answer]                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ How It Works Under the Hood

```
Your Repository
  ├── package.json / requirements.txt
  ├── API Routes & Schemas
  └── Database Models
            │
            ▼
    [Vibexplain Engine]
            │
            ├─► 1. Codebase Reconnaissance & Stack Detection
            ├─► 2. Layman Pitch Formulation (EL5)
            ├─► 3. Architectural Trade-Off Analysis
            ├─► 4. End-to-End Request Flow Mapping
            ├─► 5. Senior Tech / Investor Question Anticipation
            └─► 6. Landmine & Spaghetti Debt Audit
            │
            ▼
    Dual Deliverables
      ├── VIBEXPLAIN.md (Markdown Dossier)
      └── vibexplain.html (Standalone Interactive Dashboard)
```

---

## 🤝 Contributing

We love contributions! If you have ideas for:
- New stack detectors (Go, Elixir, Rust, Flutter, iOS)
- Additional investor grill questions
- UI enhancements to the dashboard template

Feel free to open an Issue or submit a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">
  <sub>Vibexplain built by The SurfBoard. Never get roasted in a tech meeting again.</sub>
</div>
