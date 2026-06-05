#!/usr/bin/env python3
"""Command-line interface for ai-skillforge."""

import argparse
import sys
from .loader import load, search, list_skills, categories


def main():
    parser = argparse.ArgumentParser(
        prog="skillforge",
        description="ai-skillforge — 1,026 lazy-loading AI skills"
    )
    sub = parser.add_subparsers(dest="command")

    # skillforge load <name>
    p_load = sub.add_parser("load", help="Load and print a skill")
    p_load.add_argument("name")
    p_load.add_argument("--category", "-c", default=None)

    # skillforge search <query>
    p_search = sub.add_parser("search", help="Search skills")
    p_search.add_argument("query")
    p_search.add_argument("--category", "-c", default=None)
    p_search.add_argument("--limit", "-n", type=int, default=10)

    # skillforge list
    p_list = sub.add_parser("list", help="List all skills")
    p_list.add_argument("--category", "-c", default=None)

    # skillforge stats
    sub.add_parser("stats", help="Show skill counts per category")

    args = parser.parse_args()

    if args.command == "load":
        try:
            skill = load(args.name, args.category)
            print(f"# {skill.name} [{skill.category}]\n")
            print(skill.prompt)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "search":
        results = search(args.query, args.category, args.limit)
        if not results:
            print(f"No skills found for '{args.query}'")
        for r in results:
            print(f"[{r['category']:12}] {r['name']}")
            if r["description"]:
                print(f"              {r['description'][:80]}...")
            print()

    elif args.command == "list":
        skills = list_skills(args.category)
        for s in skills:
            print(f"[{s['category']:12}] {s['name']}")

    elif args.command == "stats":
        stats = categories()
        for k, v in stats.items():
            print(f"  {k:<15} {v}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
