#!/usr/bin/env python3
"""Generate README.md from data/papers.yaml and data/categories.yaml.

Usage: python scripts/build_readme.py [--check]
  --check  exit 1 if README.md is out of date (used in CI)
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
HEADER = ROOT / "templates" / "readme_header.md"
FOOTER = ROOT / "templates" / "readme_footer.md"


def load():
    cats = yaml.safe_load((ROOT / "data" / "categories.yaml").read_text())["categories"]
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())["papers"] or []
    return cats, papers


def links(p):
    out = []
    if p.get("arxiv"):
        out.append(f"[arXiv]({p['arxiv']})")
    if p.get("code"):
        out.append(f"[Code]({p['code']})")
    if p.get("project"):
        out.append(f"[Project]({p['project']})")
    return " ".join(out) or "-"


def esc(s):
    return str(s).replace("|", "\\|")


def render(cats, papers):
    lines = [HEADER.read_text().rstrip(), ""]
    lines.append(f"**{len(papers)} papers** · last updated {max((str(p.get('added', '')) for p in papers), default='-')}")
    lines.append("")
    lines.append("## Contents")
    for c in cats:
        n = sum(1 for p in papers if p["category"] == c["id"])
        anchor = c["title"].lower().replace(" ", "-").replace("&", "").replace("/", "")
        lines.append(f"- [{c['title']}](#{anchor}) ({n})")
    lines.append("")

    for c in cats:
        items = [p for p in papers if p["category"] == c["id"]]
        lines.append(f"## {c['title']}")
        lines.append("")
        lines.append(f"_{c['description']}_")
        lines.append("")
        if not items:
            lines.append("_No papers yet — PRs welcome!_")
            lines.append("")
            continue
        items.sort(key=lambda p: (-int(p["year"]), str(p["title"]).lower()))
        lines.append("| Year | Venue | Title | Links | Tags |")
        lines.append("|---|---|---|---|---|")
        for p in items:
            title = esc(p["title"])
            if p.get("short") and p["short"].lower() not in p["title"].lower():
                title = f"**{esc(p['short'])}**: {title}"
            tags = " ".join(f"`{t}`" for t in p.get("tags", []))
            lines.append(f"| {p['year']} | {esc(p['venue'])} | {title} | {links(p)} | {tags} |")
        lines.append("")

    lines.append(FOOTER.read_text().rstrip())
    lines.append("")
    return "\n".join(lines)


def main():
    cats, papers = load()
    out = render(cats, papers)
    readme = ROOT / "README.md"
    if "--check" in sys.argv:
        if not readme.exists() or readme.read_text() != out:
            print("README.md is out of date. Run: python scripts/build_readme.py")
            sys.exit(1)
        print("README.md is up to date.")
        return
    readme.write_text(out)
    print(f"Wrote README.md ({len(papers)} papers)")


if __name__ == "__main__":
    main()
