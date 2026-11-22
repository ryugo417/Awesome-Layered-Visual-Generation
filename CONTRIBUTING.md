# Contributing

Thanks for helping! The list is generated from [`data/papers.yaml`](data/papers.yaml).

## Add a paper
1. Append an entry to `data/papers.yaml`:
   ```yaml
   - id: "2501.03006"            # arXiv ID (or a short unique slug)
     title: "Full paper title"
     short: MethodName           # optional
     authors: "First Author et al."
     year: 2025
     venue: "CVPR 2025"          # "arXiv" for preprints
     category: video             # see data/categories.yaml
     tags: [video, fine-tuned, transparency]
     arxiv: https://arxiv.org/abs/2501.03006
     code: https://github.com/...   # optional
     project: https://...           # optional
     added: 2026-11-22
   ```
2. Run `pip install pyyaml && python scripts/validate.py && python scripts/build_readme.py`.
3. Open a PR. (Or just [open an issue](../../issues/new?template=add_paper.yml) and we will add it.)

## Scope
In scope: anything that generates, decomposes, composes or edits **layers** (incl. RGBA / alpha) of images or videos, and datasets / benchmarks for that.
Out of scope: "layers" meaning neural-network layers; plain matting/segmentation without a layered generation or composition aspect.
