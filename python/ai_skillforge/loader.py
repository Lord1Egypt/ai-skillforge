import json
import os
from typing import Optional

_SKILLS_ROOT = os.path.join(os.path.dirname(__file__), "skills")
_INDEX_PATH = os.path.join(os.path.dirname(__file__), "index.json")

_index: Optional[dict] = None


def _get_index() -> dict:
    global _index
    if _index is None:
        with open(_INDEX_PATH, encoding="utf-8") as f:
            _index = json.load(f)
    return _index


class Skill:
    def __init__(self, meta: dict, content: str):
        self.name = meta["name"]
        self.category = meta["category"]
        self.description = meta["description"]
        self.path = meta["path"]
        self.prompt = content

    def __repr__(self):
        return f"<Skill name={self.name!r} category={self.category!r}>"

    def __str__(self):
        return self.prompt


def load(name: str, category: str = None) -> Skill:
    """
    Load a skill by name. Reads from disk only when called.

    Args:
        name: Skill name (e.g. "exploratory-data-analysis")
        category: Optional — "gemini", "scientific", or "claude"

    Returns:
        Skill object with .prompt, .name, .category, .description

    Example:
        skill = load("scientific-brainstorming")
        print(skill.prompt)
    """
    index = _get_index()
    matches = [
        s for s in index["skills"]
        if s["name"] == name and (category is None or s["category"] == category)
    ]
    if not matches:
        raise ValueError(
            f"Skill '{name}' not found. Use search('{name}') to find similar skills."
        )
    if len(matches) > 1 and category is None:
        cats = [m["category"] for m in matches]
        raise ValueError(
            f"Skill '{name}' exists in multiple categories: {cats}. "
            f"Specify category=, e.g. load('{name}', category='{cats[0]}')"
        )
    meta = matches[0]
    skill_path = os.path.join(_SKILLS_ROOT, *meta["path"].split("skills/", 1)[1].split("/"))
    with open(skill_path, encoding="utf-8") as f:
        content = f.read()
    return Skill(meta, content)


def search(query: str, category: str = None, limit: int = 10) -> list:
    """
    Search skills by name or description keyword.

    Args:
        query: Search term
        category: Optional filter — "gemini", "scientific", or "claude"
        limit: Max results (default 10)

    Returns:
        List of dicts with name, category, description

    Example:
        results = search("data analysis")
        for r in results:
            print(r["name"], r["category"])
    """
    index = _get_index()
    q = query.lower()
    results = [
        s for s in index["skills"]
        if (q in s["name"].lower() or q in s["description"].lower())
        and (category is None or s["category"] == category)
    ]
    return [{"name": r["name"], "category": r["category"], "description": r["description"]}
            for r in results[:limit]]


def list_skills(category: str = None) -> list:
    """
    List all skills, optionally filtered by category.

    Args:
        category: Optional — "gemini", "scientific", or "claude"

    Returns:
        List of dicts with name, category, description

    Example:
        skills = list_skills(category="scientific")
        print(len(skills))
    """
    index = _get_index()
    skills = index["skills"]
    if category:
        skills = [s for s in skills if s["category"] == category]
    return [{"name": s["name"], "category": s["category"], "description": s["description"]}
            for s in skills]


def categories() -> dict:
    """
    Return skill counts per category.

    Returns:
        Dict with category names and counts

    Example:
        print(categories())
        # {"gemini": 538, "scientific": 148, "claude": 340, "total": 1026}
    """
    index = _get_index()
    counts = {}
    for s in index["skills"]:
        counts[s["category"]] = counts.get(s["category"], 0) + 1
    counts["total"] = index["total"]
    return counts
