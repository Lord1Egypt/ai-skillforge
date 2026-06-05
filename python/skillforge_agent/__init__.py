"""
skillforge-agent — Lazy-loading AI skills toolkit
539 skills across Claude, Gemini, and Scientific categories.
"""

from .loader import load, search, list_skills, categories

__version__ = "1.0.1"
__all__ = ["load", "search", "list_skills", "categories"]
