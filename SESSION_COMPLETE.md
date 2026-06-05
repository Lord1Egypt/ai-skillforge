# skillforge-agent — Complete Build Log
> Date: 2026-06-05 | Author: Lord1Egypt

---

## Final Package Info

| | |
|---|---|
| Package name | `skillforge-agent` |
| PyPI | https://pypi.org/project/skillforge-agent/ |
| npm | https://www.npmjs.com/package/skillforge-agent |
| GitHub | https://github.com/Lord1Egypt/ai-skillforge |
| Version | 1.0.1 |
| Skills | 539 (Claude 340 + Scientific 148 + Gemini 51) |

## Install

```bash
pip install skillforge-agent
npm install skillforge-agent
```

## Usage — Python

```python
from skillforge_agent import load, search, list_skills, categories

print(categories())
# {'claude': 340, 'gemini': 51, 'scientific': 148, 'total': 539}

skill = load("scientific-brainstorming")
print(skill.prompt)

results = search("protein", limit=5)
```

## Usage — JavaScript

```js
const { load, search, listSkills, categories } = require('skillforge-agent')

console.log(categories())
const skill = load('scientific-brainstorming')
console.log(skill.prompt)
```

## CLI

```bash
skillforge stats
skillforge search "data analysis"
skillforge list --category scientific
skillforge load scientific-brainstorming
```

---

## Tokens & Credentials

### Location
All tokens stored in: `~/.skillforge_tokens` (never in git — in .gitignore)

```bash
source ~/.skillforge_tokens   # loads PYPI_TOKEN and NPM_TOKEN into env
```

### PyPI API Token
- File: `~/.skillforge_tokens`
- Variable: `PYPI_TOKEN`
- Scope: Entire account
- URL to manage: https://pypi.org/manage/account/token/

### npm Token
- File: `~/.skillforge_tokens`
- Variable: `NPM_TOKEN`
- npm username: `webpalms`
- Scope: All packages, Read and Write, Bypass 2FA enabled
- Expiry: 90 days from 2026-06-05 (renew ~2026-09-03)
- URL to manage: https://www.npmjs.com/settings/~/tokens

### PyPI Trusted Publisher (GitHub Actions)
- Project: `skillforge-agent`
- Owner: `Lord1Egypt`
- Repo: `ai-skillforge`
- Workflow: `publish.yml`
- Environment: `pypi`

### GitHub Actions Secrets
- `NPM_TOKEN` — set in Lord1Egypt/ai-skillforge repo settings

---

## How to Update (add new skills)

Just tell Claude: **"dear update skillforge from the source repos"**

Or run manually:
```bash
bash /home/lordegypt/ai-skillforge/scripts/update.sh
```

This will automatically:
1. Pull latest from all 3 source repos
2. Sync skills into the package
3. Rebuild index.json
4. Bump patch version
5. Publish to PyPI + npm
6. Push to GitHub

---

## Source Repos

| Repo | Skills | Local path |
|------|--------|------------|
| `Lord1Egypt/claude-code-system-prompts` | 340 Claude prompts | `/home/lordegypt/claude-code-system-prompts` |
| `Lord1Egypt/gemini-agent-toolkit` | 538 Gemini skills (deduped to 51 unique) | `/home/lordegypt/gemini-agent-toolkit` |
| `Lord1Egypt/scientific-agent-toolkit` | 148 scientific skills | `/home/lordegypt/scientific-agent-toolkit` |

---

## Project Structure

```
/home/lordegypt/ai-skillforge/
├── skills/
│   ├── claude/          # 340 Claude prompts (.md flat files)
│   ├── gemini/          # 51 unique Gemini skills (SKILL.md in subfolders)
│   └── scientific/      # 148 scientific skills (SKILL.md in subfolders)
├── index.json           # 539 deduplicated skills registry
├── python/
│   ├── skillforge_agent/
│   │   ├── __init__.py
│   │   ├── loader.py    # lazy load/search/list/categories
│   │   ├── cli.py       # skillforge CLI
│   │   ├── index.json   # bundled copy
│   │   └── skills/      # bundled copy
│   ├── pyproject.toml
│   ├── README.md
│   └── dist/            # built packages (gitignored)
├── js/
│   ├── src/
│   │   ├── index.js     # lazy loader
│   │   └── index.d.ts   # TypeScript types
│   ├── bin/cli.js        # skillforge CLI
│   ├── index.json        # bundled copy
│   ├── skills/           # bundled copy
│   └── package.json
├── scripts/
│   ├── build_index.py    # rebuild index.json
│   └── update.sh         # full sync + publish script
├── .github/workflows/
│   └── publish.yml       # GitHub Actions auto-publish on release
├── .gitignore            # includes .skillforge_tokens
├── LICENSE
├── README.md
└── SESSION_COMPLETE.md   # this file
```

---

## Tricks & Bugs Fixed During Build

| Problem | Fix |
|---------|-----|
| `setuptools.backends.legacy:build` fails on CI | Use `setuptools.build_meta` instead |
| README outside package dir fails build | Copy README.md into `python/` folder |
| npm granular token 403 on new package | Select "All packages" scope, not specific packages |
| `ai-skillforge` name taken on PyPI | Renamed to `agent-skillforge` |
| `agent-skillforge` name taken on npm | Renamed to `skillforge-agent` |
| PyPI outage during first publish | Waited, then used `twine upload` with API token directly |
| Trusted publisher "pending" fails (project exists) | Must match exact project name that doesn't exist yet |
| Gemini is superset of claude+scientific skills | Deduplicated: scientific > claude > gemini priority |
| Tokens hardcoded in update.sh committed to public repo | Move tokens to `~/.skillforge_tokens`, load via `source` |
| PyPI maintenance page shown | Status was wrong — used https://status.python.org to verify |

---

## Deduplication Logic

Gemini toolkit contains copies of claude and scientific skills.
Priority when same skill name exists in multiple categories:
1. `scientific` (highest — most specific)
2. `claude`
3. `gemini` (lowest — superset, only unique ones kept)

Result: 539 unique skills instead of 1,026 raw total.

---

## npm Account Info

- Username: `webpalms`
- Token expiry: ~2026-09-03 (90 days)
- When token expires: go to npmjs.com -> Access Tokens -> Generate new Granular token
  - Packages: Read and Write
  - Select packages: All packages
  - Bypass 2FA: enabled
  - Then update `~/.skillforge_tokens` and GitHub secret `NPM_TOKEN`

---

*Session: 2026-06-05 — Everything working on Windows + Linux*
