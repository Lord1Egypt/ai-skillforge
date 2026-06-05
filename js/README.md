# skillforge-agent

> 539 lazy-loading AI skills for Claude, Gemini, and Scientific agents

[![PyPI version](https://img.shields.io/pypi/v/skillforge-agent?style=flat-square&color=blue)](https://pypi.org/project/skillforge-agent/)
[![npm version](https://img.shields.io/npm/v/skillforge-agent?style=flat-square&color=red)](https://www.npmjs.com/package/skillforge-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-539-brightgreen?style=flat-square)](index.json)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=flat-square)](https://pypi.org/project/skillforge-agent/)
[![Node](https://img.shields.io/badge/node-14%2B-green?style=flat-square)](https://www.npmjs.com/package/skillforge-agent)

</div>

---

## What is skillforge-agent?

**skillforge-agent** is a unified toolkit of 539 production-ready AI agent skills — merged from three specialized repositories into one clean package.

| Category | Count | Source |
|----------|-------|--------|
| Claude | 340 | Claude Code system prompts & agent prompts |
| Scientific | 148 | Research, science, engineering & analysis skills |
| Gemini | 51 | Gemini-exclusive agent skills |
| **Total** | **539** | |

### Zero token waste — skills load on demand

Skills are **not preloaded**. The index is tiny (~200 KB). Only the skill you ask for is read into memory — at the moment you call `load()`. No startup cost, no wasted tokens.

```
import time           # Your app starts instantly
load("eda")           # Only THIS skill is loaded, only when you need it
```

---

## Install

### Python

```bash
pip install skillforge-agent
```

### Node.js

```bash
npm install skillforge-agent
```

---

## Quick Start

### Python

```python
from skillforge_agent import load, search, list_skills, categories

# Load a skill — reads from disk only at this moment
skill = load("scientific-brainstorming")
print(skill.name)        # "scientific-brainstorming"
print(skill.category)    # "scientific"
print(skill.prompt)      # full skill content

# Use directly as a string
print(str(skill))

# Search skills
results = search("data analysis")
for r in results:
    print(r["name"], r["category"])

# List by category
gemini_skills = list_skills(category="gemini")

# See counts
print(categories())
# {"claude": 340, "scientific": 148, "gemini": 51, "total": 539}
```

### JavaScript / TypeScript

```js
const { load, search, listSkills, categories } = require('skillforge-agent')
// or: import { load, search, listSkills, categories } from 'skillforge-agent'

// Load a skill
const skill = load('exploratory-data-analysis')
console.log(skill.prompt)

// Search
const results = search('protein', 'scientific', 5)
results.forEach(r => console.log(r.name))

// Stats
console.log(categories())
// { claude: 340, scientific: 148, gemini: 51, total: 539 }
```

---

## CLI

```bash
# After pip install
skillforge stats
skillforge search "data analysis"
skillforge search "agent" --category gemini
skillforge list --category scientific
skillforge load scientific-brainstorming

# After npm install -g
npx skillforge stats
npx skillforge search "protein"
npx skillforge load exploratory-data-analysis
```

---

## Skill Categories

### Gemini (51 skills)
General-purpose agent skills covering accessibility, data analysis, cloud tools, frameworks, APIs, and more.

```python
skill = load("exploratory-data-analysis", category="gemini")
skill = load("accessibility-a11y")
```

### Scientific (148 skills)
Research and science-focused skills: protein structure, molecular dynamics, bioinformatics, brainstorming, and more.

```python
skill = load("scientific-brainstorming")
skill = load("molecular-dynamics")
skill = load("protein-structure-prediction")
```

### Claude (340 skills)
Claude Code system prompts, agent prompts, tool descriptions, and skill templates.

```python
skill = load("agent-prompt-explore", category="claude")
```

---

## API Reference

### `load(name, category=None)`
Load a skill by name. Returns a `Skill` object.

| Field | Type | Description |
|-------|------|-------------|
| `.name` | str | Skill name |
| `.category` | str | `gemini`, `scientific`, or `claude` |
| `.description` | str | One-line description |
| `.prompt` | str | Full skill content |

### `search(query, category=None, limit=10)`
Search skills by keyword. Returns a list of metadata dicts.

### `list_skills(category=None)`
List all skills. Returns a list of metadata dicts.

### `categories()`
Returns skill counts per category.

---

## Project Structure

```
ai-skillforge/
├── skills/
│   ├── claude/          # 340 Claude Code system prompts
│   ├── gemini/          # 51 unique Gemini agent skills
│   └── scientific/      # 148 scientific research skills
├── index.json           # Unified skill registry (lazy-loaded)
├── python/              # Python package source
│   └── ai_skillforge/
│       ├── __init__.py
│       ├── loader.py
│       └── cli.py
├── js/                  # Node.js package source
│   ├── src/
│   │   ├── index.js
│   │   └── index.d.ts
│   └── package.json
└── README.md
```

---

## Contributing

Pull requests welcome! To add a new skill, create a folder in the appropriate category:

```
skills/gemini/my-new-skill/SKILL.md
```

With frontmatter:

```markdown
---
name: my-new-skill
description: One-line description of what this skill does.
license: MIT license
metadata:
    skill-author: YourGitHub
---

# Skill Title
...
```

Then regenerate `index.json` by running:

```bash
python3 scripts/build_index.py
```

---

## License

MIT — Made with ❤️ by [Lord1Egypt](https://github.com/Lord1Egypt)
