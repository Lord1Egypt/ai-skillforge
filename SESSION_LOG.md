# ai-skillforge — Session Log
> Date: 2026-06-05 | Author: Lord1Egypt

---

## What We Did This Session

### 1. GitHub Cleanup
- Had 1,649 repos total (1,427 forks, 222 own)
- Sorted all by newest updated date
- Protected the top 100 newest repos (no deletions)
- Deleted **1,353 old forks** — 0 failures
- Script used: `/home/lordegypt/delete_forks.sh`
- Log: `/home/lordegypt/delete_forks.log`

### 2. Vercel Cleanup
- Had **180 apps** total (team: mkeshitaoutlookcoms-projects)
- Kept newest 40 first, then user manually chose additional ones to remove
- Final result: **13 apps kept** (all working)
- Vercel API used directly (token in `~/.local/share/com.vercel.cli/auth.json`)
- Team ID: `team_iHI1zyOayAcWwcEb3yjEbZ1P`

**Kept Vercel apps:**
| App | What |
|-----|------|
| mediadl-web | MediaDL web interface |
| devpulseweb | DevPulse web app |
| news-bot | Telegram News Bot |
| tg-calculator-bot | Telegram Calc Bot |
| tg-crypto-watch-bot | Telegram CryptoWatch Bot |
| tg-media-dl-bot | Telegram MediaDL Bot |
| tg-url-bot-deploy | Telegram URL Bot |
| duke-bot | Duke Bot |
| evm-codes | EVM codes tool (working) |
| polygon-faucet | Polygon faucet (working) |
| whitespider | Whitespider (working) |
| super-mario64-online | Mario64 (working) |
| mega-crypto-bot | Crypto bot (working) |

### 3. ai-skillforge Project Built

**Goal:** Merge 3 repos into one lazy-loading AI skills package.

**Source repos merged:**
- `Lord1Egypt/claude-code-system-prompts` → 340 Claude prompts
- `Lord1Egypt/gemini-agent-toolkit` → 538 Gemini skills
- `Lord1Egypt/scientific-agent-toolkit` → 148 scientific skills

**Deduplication:** Gemini is a superset — scientific and claude skills take priority.
- Final unique skills: **539** (Claude 340, Scientific 148, Gemini 51)

**Package name:** `ai-skillforge`
- pip: `pip install ai-skillforge`
- npm: `npm install ai-skillforge`
- GitHub: https://github.com/Lord1Egypt/ai-skillforge

**Files built:**
```
/home/lordegypt/ai-skillforge/
├── skills/
│   ├── claude/          340 prompts (.md files)
│   ├── gemini/          538 skills (SKILL.md in subfolders)
│   └── scientific/      148 skills (SKILL.md in subfolders)
├── index.json           539 skills — unified deduplicated registry
├── python/
│   ├── ai_skillforge/
│   │   ├── __init__.py
│   │   ├── loader.py    lazy load/search/list/categories
│   │   ├── cli.py       `skillforge` CLI
│   │   ├── index.json   (copy)
│   │   └── skills/      (copy for bundling)
│   └── pyproject.toml
├── js/
│   ├── src/
│   │   ├── index.js     lazy load/search/listSkills/categories
│   │   └── index.d.ts   TypeScript types
│   ├── bin/cli.js       `skillforge` CLI
│   ├── index.json       (copy)
│   ├── skills/          (copy for bundling)
│   └── package.json
├── scripts/
│   └── build_index.py   regenerate index.json when adding skills
├── LICENSE
├── README.md
├── .gitignore
└── SESSION_LOG.md       ← this file
```

**Key design — Lazy loading:**
- `index.json` loads only on first call (tiny, ~200KB)
- Individual skill files read from disk ONLY when `load("skill-name")` is called
- Zero startup cost, zero wasted tokens

**Python API:**
```python
from ai_skillforge import load, search, list_skills, categories
skill = load("scientific-brainstorming")
print(skill.prompt)
```

**JS API:**
```js
const { load, search, listSkills, categories } = require('ai-skillforge')
const skill = load('exploratory-data-analysis')
console.log(skill.prompt)
```

**CLI:**
```bash
skillforge stats
skillforge search "protein"
skillforge load scientific-brainstorming
skillforge list --category scientific
```

**Tested — all passing:**
- `categories()` returns correct counts
- `load()` returns correct skill with prompt content
- `search()` returns relevant results
- JS and Python both work
- CLI works for both

---

## What Is Left To Do

### Publish to PyPI
```bash
cd /home/lordegypt/ai-skillforge/python
python -m build
twine upload dist/*
```
Needs: PyPI account + API token → set up `~/.pypirc`

### Publish to npm
```bash
cd /home/lordegypt/ai-skillforge/js
npm login    # need npm account
npm publish
```
Needs: npm account login (`npm adduser` or `npm login`)

### Tools already installed
- `build` and `twine` installed via pip ✅
- `npm` v11.14 available ✅
- `node` v25.8.1 available ✅

---

## Vercel Auth (for future sessions)
- Token: in `~/.local/share/com.vercel.cli/auth.json`
- Team ID: `team_iHI1zyOayAcWwcEb3yjEbZ1P`
- API: `https://api.vercel.com/v9/projects?teamId=team_iHI1zyOayAcWwcEb3yjEbZ1P`

---

*Session ended: 2026-06-05*
