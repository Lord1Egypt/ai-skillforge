# skillforge-agent — Session 2 Log
> Date: 2026-06-05 | Author: Lord1Egypt

---

## What We Did This Session

### 1. GitHub & Vercel Cleanup
- Deleted 1,353 old GitHub forks (kept newest 100 repos)
- Deleted 167 Vercel apps (kept 13 working apps)
- Script: /home/lordegypt/delete_forks.sh

### 2. Built & Published skillforge-agent

**Package:** `skillforge-agent` v1.0.5
- PyPI: https://pypi.org/project/skillforge-agent/
- npm: https://www.npmjs.com/package/skillforge-agent
- GitHub: https://github.com/Lord1Egypt/ai-skillforge

**Source repos merged:**
- `Lord1Egypt/claude-code-system-prompts` → 340 Claude prompts
- `Lord1Egypt/gemini-agent-toolkit` → 538 Gemini (deduped to 51 unique)
- `Lord1Egypt/scientific-agent-toolkit` → 148 scientific skills
- **Total: 539 unique skills**

**Tested working on Windows (PowerShell) + Linux.**

---

## Tokens & Credentials

### Token File Location
```
~/.skillforge_tokens
```
Load with: `source ~/.skillforge_tokens`

### PyPI
- Variable: `PYPI_TOKEN`
- Scope: Entire account
- Manage: https://pypi.org/manage/account/token/

### npm
- Variable: `NPM_TOKEN`
- npm username: `webpalms`
- Scope: All packages, Read+Write, Bypass 2FA
- **Expires: ~2026-09-03** (renew before this date)
- Manage: https://www.npmjs.com/settings/~/tokens
- Also in GitHub secret: `NPM_TOKEN` in Lord1Egypt/ai-skillforge

### PyPI Trusted Publisher
- Project: `skillforge-agent`
- Owner: `Lord1Egypt`
- Repo: `ai-skillforge`
- Workflow: `publish.yml`
- Environment: `pypi`

---

## How to Update skillforge-agent

Tell Claude: **"dear update skillforge from the source repos"**

Or manually:
```bash
bash /home/lordegypt/ai-skillforge/scripts/update.sh
```

---

## Tricks & Bugs Fixed

| Problem | Fix |
|---------|-----|
| `setuptools.backends.legacy:build` fails on CI | Use `setuptools.build_meta` |
| README outside python/ dir breaks build | Copy README.md into python/ folder |
| npm granular token 403 on new package | Select "All packages" scope, not specific |
| `ai-skillforge` taken on PyPI | Renamed to `agent-skillforge` |
| `agent-skillforge` taken on npm | Renamed to `skillforge-agent` |
| PyPI outage | Used twine with API token directly |
| README not showing on npm | Remove `<div>` HTML wrapper — start with `# heading` |
| Tokens hardcoded in public script | Store in `~/.skillforge_tokens`, load via `source` |
| Gemini is superset of other skills | Deduplicate: scientific > claude > gemini priority |
| Failed GitHub deployment showing | Mark inactive then DELETE via API |

---

## Next Project Plan — awesome-prompt-forge

### Idea
Build a second package merging:
1. `Lord1Egypt/awesome-ai-system-prompts` — 52 system prompts (ChatGPT, Claude, Cursor, v0, Manus, etc.)
2. HuggingFace datasets — curated prompts from public datasets

### Package name candidates
- `awesome-prompt-forge`
- `prompt-forge`
- `ai-prompt-hub`

### Goal
- Same lazy-loading pattern as skillforge-agent
- Published as `pip install awesome-prompt-forge`
- Published as `npm install awesome-prompt-forge`
- Categories: by AI tool (chatgpt/, claude/, cursor/, v0/, etc.)
- Pull from HuggingFace datasets API for extra prompts

### HuggingFace dataset ideas
- `fka/awesome-chatgpt-prompts` — 163 prompts
- `Falah/system_prompts_collection` — system prompts collection
- `MaziyarPanahi/WizardLM_evol_instruct_70k` — instruction prompts

### Plan when ready
1. Clone awesome-ai-system-prompts locally
2. Write HuggingFace downloader script (datasets library)
3. Organize by category/tool
4. Build lazy loader (same pattern as skillforge-agent)
5. Publish to PyPI + npm

---

*Session: 2026-06-05*
