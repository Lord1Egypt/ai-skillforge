"""
skillforge-agent — Lazy-loading AI skills toolkit
1,026 skills across Claude, Gemini, and Scientific categories.
"""

from .loader import load, search, list_skills, categories

__version__ = "1.0.0"
__all__ = ["load", "search", "list_skills", "categories"]
