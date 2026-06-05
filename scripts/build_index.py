#!/usr/bin/env python3
"""Regenerate index.json from all skills in the skills/ directory."""

import os, json, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
OUT_PATH = os.path.join(ROOT, "index.json")

skills = []

for category in ["gemini", "scientific", "claude"]:
    cat_dir = os.path.join(SKILLS_DIR, category)
    if not os.path.isdir(cat_dir):
        continue

    entries = sorted(os.listdir(cat_dir))
    for entry in entries:
        entry_path = os.path.join(cat_dir, entry)

        # Subfolder with SKILL.md (gemini, scientific)
        skill_md = os.path.join(entry_path, "SKILL.md")
        if os.path.isdir(entry_path) and os.path.isfile(skill_md):
            with open(skill_md) as f:
                content = f.read()
            desc = ""
            m = re.search(r'^description:\s*(.+?)$', content, re.MULTILINE)
            if m:
                desc = m.group(1).strip()
            skills.append({
                "name": entry,
                "category": category,
                "description": desc,
                "path": f"skills/{category}/{entry}/SKILL.md"
            })

        # Flat .md file (claude)
        elif os.path.isfile(entry_path) and entry.endswith(".md"):
            skill_name = entry[:-3]
            with open(entry_path) as f:
                content = f.read()
            desc = ""
            m = re.search(r"description:\s*'?(.+?)'?\s*$", content, re.MULTILINE)
            if m:
                desc = m.group(1).strip()
            skills.append({
                "name": skill_name,
                "category": category,
                "description": desc,
                "path": f"skills/{category}/{entry}"
            })

index = {"version": "1.0.0", "total": len(skills), "skills": skills}
with open(OUT_PATH, "w") as f:
    json.dump(index, f, indent=2)

print(f"index.json written — {len(skills)} skills")
for cat in ["gemini", "scientific", "claude"]:
    count = sum(1 for s in skills if s["category"] == cat)
    print(f"  {cat}: {count}")
