#!/usr/bin/env python3
"""Validate data/papers.yaml: required fields, known categories/tags, unique ids, URL format.

Usage: python scripts/validate.py [--list-ids]
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["id", "title", "authors", "year", "venue", "category", "added"]


def main():
    cats = yaml.safe_load((ROOT / "data" / "categories.yaml").read_text())
    cat_ids = {c["id"] for c in cats["categories"]}
    known_tags = {t for group in cats["tags"].values() for t in group}
    papers = yaml.safe_load((ROOT / "data" / "papers.yaml").read_text())["papers"] or []

    if "--list-ids" in sys.argv:
        for p in papers:
            print(p["id"], "|", p["title"])
        return

    errors, warnings, seen = [], [], {}
    for i, p in enumerate(papers):
        where = f"#{i} ({p.get('id', '?')})"
        for k in REQUIRED:
            if not p.get(k):
                errors.append(f"{where}: missing '{k}'")
        pid = str(p.get("id"))
        if pid in seen:
            errors.append(f"{where}: duplicate id (also #{seen[pid]})")
        seen[pid] = i
        if p.get("category") not in cat_ids:
            errors.append(f"{where}: unknown category '{p.get('category')}'")
        for t in p.get("tags", []):
            if t not in known_tags:
                warnings.append(f"{where}: tag '{t}' not in categories.yaml")
        for k in ("arxiv", "code", "project"):
            if p.get(k) and not str(p[k]).startswith("https://"):
                errors.append(f"{where}: {k} must be an https URL")
        if p.get("arxiv") and re.match(r"^\d{4}\.\d{4,5}$", pid) and pid not in p["arxiv"]:
            errors.append(f"{where}: arxiv URL does not match id")
        if p.get("needs_check"):
            warnings.append(f"{where}: needs_check")

    titles = {}
    for p in papers:
        key = re.sub(r"[^a-z0-9]", "", str(p.get("title", "")).lower())
        if key in titles:
            errors.append(f"duplicate title: {p['title']}")
        titles[key] = 1

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(papers)} papers, {len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
