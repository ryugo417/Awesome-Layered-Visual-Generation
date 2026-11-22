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
    ds_file = ROOT / "data" / "datasets.yaml"
    datasets = (yaml.safe_load(ds_file.read_text()) or {}).get("datasets") or [] if ds_file.exists() else []
    return cats, papers, datasets


STATUS_TITLE = {
    "public": "Public (downloadable)",
    "announced": "Announced (release promised, not downloadable yet)",
    "unknown": "Status unclear",
}


def paper_ref(ds, by_id):
    ref = str(ds.get("paper", ""))
    p = by_id.get(ref)
    if p:
        label = p.get("short") or p["title"]
        link = p.get("arxiv") or p.get("project") or ""
        return f"[{esc(label)}]({link}) ({esc(p['venue'])})" if link else f"{esc(label)} ({esc(p['venue'])})"
    if ref.startswith("http"):
        return f"[paper]({ref})"
    return "-"


def render_datasets(datasets, papers):
    if not datasets:
        return []
    by_id = {str(p["id"]): p for p in papers}
    lines = ["## Datasets", "",
             "_Layered datasets, including data released alongside method papers. Status is re-checked by the daily agent._", ""]
    for status in ["public", "announced", "unknown"]:
        items = [d for d in datasets if d.get("status") == status]
        if not items:
            continue
        lines.append(f"### {STATUS_TITLE[status]}")
        lines.append("")
        lines.append("| Dataset | Paper | Modality | Content | Size | License | Link | Checked |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for d in sorted(items, key=lambda d: d["name"].lower()):
            link = f"[{'Download' if status == 'public' else 'Page'}]({d['url']})" if d.get("url") else "-"
            lines.append(
                f"| **{esc(d['name'])}** | {paper_ref(d, by_id)} | {d.get('modality', '-')} | {esc(d.get('content', '-'))} "
                f"| {esc(d.get('size', '-'))} | {esc(d.get('license', '-'))} | {link} | {d.get('checked', '-')} |")
        lines.append("")
    return lines


import re
import json

GH = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+)")


def stars_badge(url):
    m = GH.match(url or "")
    if not m:
        return ""
    owner, repo = m.group(1), m.group(2).removesuffix(".git")
    return f" ![stars](https://img.shields.io/github/stars/{owner}/{repo}?style=flat&label=%E2%98%85&color=yellow)"


def links(p):
    out = []
    if p.get("arxiv"):
        out.append(f"[arXiv]({p['arxiv']})")
    if p.get("code"):
        out.append(f"[Code]({p['code']}){stars_badge(p['code'])}")
    if p.get("project"):
        out.append(f"[Project]({p['project']})")
    return " ".join(out) or "-"


def sort_key_recent(p):
    pid = str(p["id"])
    return (str(p.get("added", "")), pid if re.match(r"^\d{4}\.\d{4,5}$", pid) else "0")


def render_recent(papers, cats, n=10):
    cat_title = {c["id"]: c["title"] for c in cats}
    items = sorted(papers, key=sort_key_recent, reverse=True)[:n]
    lines = ["## Recently Added", "", "| Added | Title | Venue | Category |", "|---|---|---|---|"]
    for p in items:
        name = p.get("short") or p["title"]
        link = p.get("arxiv") or p.get("project") or p.get("code") or ""
        title = f"[{esc(name)}]({link})" if link else esc(name)
        lines.append(f"| {p.get('added', '-')} | {title} | {esc(p['venue'])} | {cat_title.get(p['category'], p['category'])} |")
    lines.append("")
    return lines


SITE_DATA = ROOT / "docs" / "data.json"


def site_data(cats, papers, datasets):
    clean = lambda d: {k: (str(v) if k in ("added", "checked") else v) for k, v in d.items() if k != "needs_check"}
    return (json.dumps({
        "categories": cats,
        "papers": [clean(p) for p in papers],
        "datasets": [clean(d) for d in datasets],
    }, ensure_ascii=False, indent=1) + "\n")


def esc(s):
    return str(s).replace("|", "\\|")


def render(cats, papers, datasets=()):
    lines = [HEADER.read_text().rstrip(), ""]
    n_pub = sum(1 for d in datasets if d.get("status") == "public")
    lines.append(f"**{len(papers)} papers · {n_pub} public datasets** · last updated "
                 f"{max([str(p.get('added', '')) for p in papers] + [str(d.get('checked', '')) for d in datasets], default='-')}")
    lines.append("")
    lines.append("## Contents")
    for c in cats:
        n = sum(1 for p in papers if p["category"] == c["id"])
        anchor = c["title"].lower().replace(" ", "-").replace("&", "").replace("/", "")
        lines.append(f"- [{c['title']}](#{anchor}) ({n})")
    if datasets:
        lines.append(f"- [Datasets](#datasets) ({n_pub} public, {len(datasets) - n_pub} announced/unclear)")
    lines.append("")
    n_code = sum(1 for p in papers if p.get("code"))
    years = sorted({int(p["year"]) for p in papers})
    per_year = " · ".join(f"{y}: {sum(1 for p in papers if int(p['year']) == y)}" for y in years)
    lines.append(f"> 💻 = code available ({n_code}/{len(papers)}) · Papers per year — {per_year}")
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
            if p.get("code"):
                title = f"{title} 💻"
            tags = " ".join(f"`{t}`" for t in p.get("tags", []))
            lines.append(f"| {p['year']} | {esc(p['venue'])} | {title} | {links(p)} | {tags} |")
        lines.append("")

    lines += render_datasets(datasets, papers)
    lines.append(FOOTER.read_text().rstrip())
    lines.append("")
    return "\n".join(lines)


def main():
    cats, papers, datasets = load()
    out = render(cats, papers, datasets)
    data = site_data(cats, papers, datasets)
    readme = ROOT / "README.md"
    if "--check" in sys.argv:
        stale = [f.name for f, txt in ((readme, out), (SITE_DATA, data)) if not f.exists() or f.read_text() != txt]
        if stale:
            print(f"{', '.join(stale)} out of date. Run: python scripts/build_readme.py")
            sys.exit(1)
        print("README.md and docs/data.json are up to date.")
        return
    readme.write_text(out)
    SITE_DATA.parent.mkdir(exist_ok=True)
    SITE_DATA.write_text(data)
    print(f"Wrote README.md ({len(papers)} papers)")


if __name__ == "__main__":
    main()
