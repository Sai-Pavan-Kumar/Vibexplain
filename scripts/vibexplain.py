#!/usr/bin/env python3
"""
Vibexplain CLI Scanner
Lightweight helper script to scan a repository and generate an inspection report.
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

IGNORE_DIRS = {
    'node_modules', '.git', '.next', 'dist', 'build', '__pycache__',
    '.venv', 'venv', 'env', '.idea', '.vscode', 'coverage', '.turbo'
}

def scan_repository(repo_path: str):
    root = Path(repo_path).resolve()
    if not root.exists():
        print(f"Error: Path {root} does not exist.")
        sys.exit(1)

    tech_stack = []
    file_count = 0
    package_json = root / "package.json"
    requirements_txt = root / "requirements.txt"
    pyproject_toml = root / "pyproject.toml"
    cargo_toml = root / "Cargo.toml"
    prisma_schema = root / "prisma" / "schema.prisma"

    # Analyze JS/TS Stack
    if package_json.exists():
        try:
            with open(package_json, 'r', encoding='utf-8') as f:
                pkg = json.load(f)
                deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
                
                if 'next' in deps: tech_stack.append("Next.js")
                if 'react' in deps: tech_stack.append("React")
                if 'tailwindcss' in deps: tech_stack.append("Tailwind CSS")
                if '@prisma/client' in deps or 'prisma' in deps: tech_stack.append("Prisma ORM")
                if '@supabase/supabase-js' in deps: tech_stack.append("Supabase")
                if 'firebase' in deps: tech_stack.append("Firebase")
                if 'next-auth' in deps or '@auth/core' in deps: tech_stack.append("NextAuth")
                if 'zod' in deps: tech_stack.append("Zod Validation")
                if 'ai' in deps: tech_stack.append("Vercel AI SDK")
                if 'openai' in deps: tech_stack.append("OpenAI API")
                if '@anthropic-ai/sdk' in deps: tech_stack.append("Anthropic API")
                if 'stripe' in deps: tech_stack.append("Stripe")
                if 'express' in deps: tech_stack.append("Express.js")
                if 'fastify' in deps: tech_stack.append("Fastify")
        except Exception as e:
            print(f"Warning: Could not read package.json: {e}")

    # Analyze Python Stack
    if requirements_txt.exists() or pyproject_toml.exists():
        tech_stack.append("Python")
        # Check requirements
        if requirements_txt.exists():
            try:
                content = requirements_txt.read_text(encoding='utf-8')
                if 'fastapi' in content.lower(): tech_stack.append("FastAPI")
                if 'django' in content.lower(): tech_stack.append("Django")
                if 'flask' in content.lower(): tech_stack.append("Flask")
                if 'sqlalchemy' in content.lower(): tech_stack.append("SQLAlchemy")
                if 'langchain' in content.lower(): tech_stack.append("LangChain")
            except Exception:
                pass

    if cargo_toml.exists():
        tech_stack.append("Rust / Cargo")

    # Count files
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        file_count += len(filenames)

    summary = {
        "projectName": root.name,
        "rootPath": str(root),
        "totalFiles": file_count,
        "detectedStack": list(dict.fromkeys(tech_stack)),
        "hasPrisma": prisma_schema.exists(),
    }
    return summary

def main():
    parser = argparse.ArgumentParser(description="Vibexplain Repository Scanner")
    parser.add_argument("path", nargs="?", default=".", help="Path to project directory")
    parser.add_argument("--json", action="store_true", help="Output summary as JSON")
    args = parser.parse_args()

    summary = scan_repository(args.path)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print("\n⚡ Vibexplain Codebase Reconnaissance")
        print("=" * 45)
        print(f"📁 Project:        {summary['projectName']}")
        print(f"📊 Total Files:    {summary['totalFiles']}")
        print(f"🛠️ Detected Stack: {', '.join(summary['detectedStack']) or 'Custom / Unrecognized'}")
        print("=" * 45)
        print("💡 Tip: Run Vibexplain inside Claude Code, Antigravity, or Cursor to generate full blueprints.\n")

if __name__ == "__main__":
    main()
