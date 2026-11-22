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
CHART = {mode: ROOT / "docs" / f"papers_per_year_{mode}.svg" for mode in ("light", "dark")}
THEME = {  # reference palette: surface, bar, primary/secondary/muted ink, grid, baseline
    "light": dict(surface="#fcfcfb", bar="#2a78d6", ink="#0b0b0b", ink2="#52514e", muted="#898781", grid="#e1e0d9", axis="#c3c2b7"),
    "dark": dict(surface="#1a1a19", bar="#3987e5", ink="#f0efec", ink2="#c3c2b7", muted="#898781", grid="#2c2c2a", axis="#383835"),
}


def year_counts(papers):
    years = sorted({int(p["year"]) for p in papers})
    return [(y, sum(1 for p in papers if int(p["year"]) == y)) for y in range(years[0], years[-1] + 1)]


def chart_svg(counts, mode):
    t = THEME[mode]
    W, H, L, R, T, B = 640, 220, 34, 8, 24, 30
    pw, ph = W - L - R, H - T - B
    vmax = max(c for _, c in counts)
    step = 5 if vmax <= 30 else 10 if vmax <= 60 else 20
    top = -(-vmax // step) * step
    y = lambda v: T + ph - v / top * ph
    slot = pw / len(counts)
    bw = min(48, slot * 0.62)
    font = "font-family='ui-sans-serif,-apple-system,Segoe UI,Helvetica,Arial,sans-serif'"
    o = [f"<svg xmlns='http://www.w3.org/2000/svg' width='{W}' height='{H}' viewBox='0 0 {W} {H}' role='img' "
         f"aria-label='Papers per year: " + ", ".join(f"{yr}: {c}" for yr, c in counts) + "'>",
         f"<rect width='{W}' height='{H}' rx='8' fill='{t['surface']}'/>"]
    for v in range(0, top + 1, step):
        o.append(f"<line x1='{L}' x2='{W - R}' y1='{y(v):.1f}' y2='{y(v):.1f}' stroke='{t['grid'] if v else t['axis']}' stroke-width='1'/>")
        o.append(f"<text x='{L - 6}' y='{y(v) + 4:.1f}' text-anchor='end' font-size='11' fill='{t['muted']}' {font}>{v}</text>")
    for i, (yr, c) in enumerate(counts):
        cx = L + slot * (i + 0.5)
        x0, y0, h = cx - bw / 2, y(c), T + ph - y(c)
        r = min(4, h, bw / 2)
        if c:
            o.append(f"<path d='M{x0:.1f},{T + ph:.1f} V{y0 + r:.1f} Q{x0:.1f},{y0:.1f} {x0 + r:.1f},{y0:.1f} "
                     f"H{x0 + bw - r:.1f} Q{x0 + bw:.1f},{y0:.1f} {x0 + bw:.1f},{y0 + r:.1f} V{T + ph:.1f} Z' fill='{t['bar']}'>"
                     f"<title>{yr}: {c} papers</title></path>")
        o.append(f"<text x='{cx:.1f}' y='{y0 - 6:.1f}' text-anchor='middle' font-size='12' font-weight='600' fill='{t['ink2']}' {font}>{c}</text>")
        o.append(f"<text x='{cx:.1f}' y='{H - 10}' text-anchor='middle' font-size='12' fill='{t['muted']}' {font}>{yr}</text>")
    o.append("</svg>")
    return "\n".join(o) + "\n"


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
    lines.append(f"> 💻 = code available ({n_code}/{len(papers)})")
    lines.append("")
    lines.append("**Papers per year** (by publication year; the latest year is year-to-date)")
    lines.append("")
    lines.append("<picture>")
    lines.append('  <source media="(prefers-color-scheme: dark)" srcset="docs/papers_per_year_dark.svg">')
    lines.append('  <img alt="Papers per year: ' + ", ".join(f"{y}: {c}" for y, c in year_counts(papers)) +
                 '" src="docs/papers_per_year_light.svg" width="640">')
    lines.append("</picture>")
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
        lines.append("| Year | Venue | Title | Links |")
        lines.append("|---|---|---|---|")
        for p in items:
            title = esc(p["title"])
            if p.get("short") and p["short"].lower() not in p["title"].lower():
                title = f"**{esc(p['short'])}**: {title}"
            if p.get("code"):
                title = f"{title} 💻"
            lines.append(f"| {p['year']} | {esc(p['venue'])} | {title} | {links(p)} |")
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
        charts = [(CHART[m], chart_svg(year_counts(papers), m)) for m in CHART]
        stale = [f.name for f, txt in [(readme, out), (SITE_DATA, data)] + charts if not f.exists() or f.read_text() != txt]
        if stale:
            print(f"{', '.join(stale)} out of date. Run: python scripts/build_readme.py")
            sys.exit(1)
        print("README.md, docs/data.json and charts are up to date.")
        return
    readme.write_text(out)
    SITE_DATA.parent.mkdir(exist_ok=True)
    SITE_DATA.write_text(data)
    for m, f in CHART.items():
        f.write_text(chart_svg(year_counts(papers), m))
    print(f"Wrote README.md ({len(papers)} papers)")


if __name__ == "__main__":
    main()
