#!/bin/bash
# Sync skills from source repos and republish to PyPI + npm
# Usage: bash scripts/update.sh
# Requires: PYPI_TOKEN and NPM_TOKEN env vars set, or stored in ~/.skillforge_tokens

set -e
ROOT="/home/lordegypt/ai-skillforge"

# Load tokens from local file if not in env
if [ -f ~/.skillforge_tokens ]; then
  source ~/.skillforge_tokens
fi

if [ -z "$PYPI_TOKEN" ] || [ -z "$NPM_TOKEN" ]; then
  echo "Error: set PYPI_TOKEN and NPM_TOKEN env vars or create ~/.skillforge_tokens"
  exit 1
fi

echo "=== Pulling source repos ==="
git -C /home/lordegypt/claude-code-system-prompts pull
git -C /home/lordegypt/gemini-agent-toolkit pull
git -C /home/lordegypt/scientific-agent-toolkit pull

echo "=== Syncing skills ==="
cp -r /home/lordegypt/gemini-agent-toolkit/gemini-skills/. "$ROOT/skills/gemini/"
cp -r /home/lordegypt/scientific-agent-toolkit/scientific-skills/. "$ROOT/skills/scientific/"
cp -r /home/lordegypt/claude-code-system-prompts/system-prompts/. "$ROOT/skills/claude/"

echo "=== Rebuilding index ==="
python3 "$ROOT/scripts/build_index.py"

echo "=== Syncing into packages ==="
cp -r "$ROOT/skills/." "$ROOT/python/skillforge_agent/skills/"
cp "$ROOT/index.json" "$ROOT/python/skillforge_agent/index.json"
cp -r "$ROOT/skills/." "$ROOT/js/skills/"
cp "$ROOT/index.json" "$ROOT/js/index.json"
cp "$ROOT/README.md" "$ROOT/python/README.md"

echo "=== Bumping version ==="
CURRENT=$(grep '^version = ' "$ROOT/python/pyproject.toml" | cut -d'"' -f2)
NEW=$(python3 -c "v='$CURRENT'.split('.'); v[2]=str(int(v[2])+1); print('.'.join(v))")
echo "$CURRENT → $NEW"
sed -i "s/version = \"$CURRENT\"/version = \"$NEW\"/" "$ROOT/python/pyproject.toml"
sed -i "s/\"version\": \"$CURRENT\"/\"version\": \"$NEW\"/" "$ROOT/js/package.json"
sed -i "s/__version__ = \"$CURRENT\"/__version__ = \"$NEW\"/" "$ROOT/python/skillforge_agent/__init__.py"

echo "=== Publishing npm ==="
cd "$ROOT/js" && npm publish --//registry.npmjs.org/:_authToken=$NPM_TOKEN

echo "=== Building & publishing PyPI ==="
cd "$ROOT/python" && rm -rf dist/ && python -m build
TWINE_USERNAME=__token__ TWINE_PASSWORD=$PYPI_TOKEN twine upload dist/*

echo "=== Committing ==="
cd "$ROOT" && git add -A
git commit -m "v$NEW: sync skills from source repos"
git push

echo "Done! Published v$NEW"
