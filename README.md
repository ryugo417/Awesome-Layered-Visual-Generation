# Awesome Layered Visual Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of papers on **layered representations for visual generation**: layered / transparent (RGBA) image generation, image & video layer decomposition, layer composition (shadows, reflections, harmonization), layer-aware editing, and layered graphic design.

> This list is updated on weekdays with the help of an AI agent and checked by a maintainer. Found a missing paper or a wrong link? Please [open an issue](../../issues/new?template=add_paper.yml) or send a PR.

<!-- AUTO-GENERATED from data/papers.yaml by scripts/build_readme.py. Do not edit README.md by hand. -->

**31 papers** · last updated 2026-11-22

## Contents
- [Layered Image Generation](#layered-image-generation) (10)
- [Image Layer Decomposition](#image-layer-decomposition) (3)
- [Layer Composition & Harmonization](#layer-composition--harmonization) (2)
- [Layer-aware Editing](#layer-aware-editing) (0)
- [Layered Video Generation & Decomposition](#layered-video-generation--decomposition) (11)
- [Graphic Design / Vector Layers](#graphic-design--vector-layers) (3)
- [Datasets & Benchmarks](#datasets--benchmarks) (2)
- [Surveys](#surveys) (0)

## Layered Image Generation

_Generating transparent (RGBA) images or multiple layers directly from text / conditions._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | CVPR 2026 Findings | TAUE: Training-free Noise Transplant and Cultivation Diffusion Model | [arXiv](https://arxiv.org/abs/2511.02580) [Code](https://github.com/IyatomiLab/TAUE) [Project](https://iyatomilab.github.io/TAUE) | `image` `training-free` `foreground` `background` |
| 2025 | CVPR 2025 | ART: Anonymous Region Transformer for Variable Multi-Layer Transparent Image Generation | [arXiv](https://arxiv.org/abs/2502.18364) | `image` `fine-tuned` `transparency` |
| 2025 | arXiv | LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge | [arXiv](https://arxiv.org/abs/2501.01197) | `image` `foreground` `background` |
| 2025 | arXiv | PSDiffusion: Harmonized Multi-Layer Image Generation via Layout and Appearance Alignment | [arXiv](https://arxiv.org/abs/2505.11468) | `image` `fine-tuned` `transparency` |
| 2025 | CVPR 2025 | TKG-DM: Training-free Chroma Key Content Generation Diffusion Model | [arXiv](https://arxiv.org/abs/2411.15580) [Code](https://github.com/ryugo417/TKG-DM) | `image` `training-free` `foreground` `background` |
| 2024 | ECCV 2024 Workshops (AI4VA) | Alfie: Democratising RGBA Image Generation With No $$$ | [arXiv](https://arxiv.org/abs/2408.14826) [Code](https://github.com/aimagelab/Alfie) | `image` `training-free` `transparency` |
| 2024 | ECCV 2024 | LayerDiff: Exploring Text-guided Multi-layered Composable Image Synthesis via Layer-Collaborative Diffusion Model | [arXiv](https://arxiv.org/abs/2403.11929) | `image` `fine-tuned` `foreground` `background` |
| 2024 | arXiv | LayerFusion: Harmonized Multi-Layer Text-to-Image Generation with Generative Priors | [arXiv](https://arxiv.org/abs/2412.04460) [Project](https://layerfusion.github.io) | `image` `training-free` `transparency` `foreground` `background` |
| 2024 | SIGGRAPH 2024 | **LayerDiffuse**: Transparent Image Layer Diffusion using Latent Transparency | [arXiv](https://arxiv.org/abs/2402.17113) [Code](https://github.com/lllyasviel/LayerDiffuse) | `image` `fine-tuned` `transparency` `foreground` `background` |
| 2023 | arXiv | Text2Layer: Layered Image Generation using Latent Diffusion Model | [arXiv](https://arxiv.org/abs/2307.09781) | `image` `fine-tuned` `foreground` `background` |

## Image Layer Decomposition

_Decomposing a flat RGB image into layers (foreground/background, instances, effects such as shadows and reflections)._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | CVPR 2026 | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition | [arXiv](https://arxiv.org/abs/2512.15603) [Code](https://github.com/QwenLM/Qwen-Image-Layered) | `image` `fine-tuned` `transparency` `text` |
| 2025 | CVPR 2025 | **LayerDecomp**: Generative Image Layer Decomposition with Visual Effects | [arXiv](https://arxiv.org/abs/2411.17864) [Project](https://rayjryang.github.io/LayerDecomp) | `image` `fine-tuned` `foreground` `background` `shadow` `reflection` |
| 2024 | CVPR 2024 | pix2gestalt: Amodal Segmentation by Synthesizing Wholes | [arXiv](https://arxiv.org/abs/2401.14398) [Code](https://github.com/cvlab-columbia/pix2gestalt) [Project](https://gestalt.cs.columbia.edu) | `image` `fine-tuned` `foreground` |

## Layer Composition & Harmonization

_Inserting / compositing objects or layers into scenes, including shadow, reflection and lighting synthesis._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2024 | ECCV 2024 | ObjectDrop: Bootstrapping Counterfactuals for Photorealistic Object Removal and Insertion | [arXiv](https://arxiv.org/abs/2403.18818) [Project](https://objectdrop.github.io) | `image` `fine-tuned` `shadow` `reflection` |
| 2023 | WACV 2024 | Collage Diffusion | [arXiv](https://arxiv.org/abs/2303.00262) [Project](https://vsanimator.github.io/collage_diffusion) | `image` |

## Layer-aware Editing

_Editing that operates on, or produces, layered representations._

_No papers yet — PRs welcome!_

## Layered Video Generation & Decomposition

_RGBA video generation, omnimatte-style video layer decomposition, layered video editing._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2025 | CVPR 2025 | Generative Omnimatte: Learning to Decompose Video into Layers | [arXiv](https://arxiv.org/abs/2411.16683) | `video` `fine-tuned` `shadow` `reflection` |
| 2025 | ICCV 2025 | LayerAnimate: Layer-level Control for Animation | [arXiv](https://arxiv.org/abs/2501.08295) [Project](https://layeranimate.github.io) | `video` `fine-tuned` `foreground` `background` |
| 2025 | SIGGRAPH 2025 | LayerFlow: A Unified Model for Layer-aware Video Generation | [arXiv](https://arxiv.org/abs/2506.04228) [Project](https://sihuiji.github.io/LayerFlow-Page) | `video` `fine-tuned` `transparency` `foreground` `background` |
| 2025 | SIGGRAPH Asia 2025 | OmnimatteZero: Fast Training-free Omnimatte with Pre-trained Video Diffusion Models | [arXiv](https://arxiv.org/abs/2503.18033) | `video` `training-free` `shadow` `reflection` |
| 2025 | CVPR 2025 | **TransPixar**: TransPixeler: Advancing Text-to-Video Generation with Transparency | [arXiv](https://arxiv.org/abs/2501.03006) [Code](https://github.com/wileewang/TransPixar) [Project](https://wileewang.github.io/TransPixar) | `video` `fine-tuned` `transparency` |
| 2025 | arXiv | **Wan-Alpha**: Video Generation with Stable Transparency via Shiftable RGB-A Distribution Learner | [arXiv](https://arxiv.org/abs/2509.24979) [Project](https://donghaotian123.github.io/Wan-Alpha) | `video` `fine-tuned` `transparency` |
| 2023 | SIGGRAPH 2023 (TOG) | FactorMatte: Redefining Video Matting for Re-Composition Tasks | [arXiv](https://arxiv.org/abs/2211.02145) [Project](https://factormatte.github.io) | `video` `shadow` `reflection` |
| 2023 | ICCV 2023 | OmnimatteRF: Robust Omnimatte with 3D Background Modeling | [arXiv](https://arxiv.org/abs/2309.07749) [Project](https://omnimatte-rf.github.io) | `video` `3d` `background` `shadow` |
| 2021 | SIGGRAPH Asia 2021 | Layered Neural Atlases for Consistent Video Editing | [arXiv](https://arxiv.org/abs/2109.11418) [Code](https://github.com/ykasten/layered-neural-atlases) [Project](https://layered-neural-atlases.github.io) | `video` |
| 2021 | CVPR 2021 | Omnimatte: Associating Objects and Their Effects in Video | [arXiv](https://arxiv.org/abs/2105.06993) | `video` `shadow` `reflection` |
| 2020 | SIGGRAPH Asia 2020 | Layered Neural Rendering for Retiming People in Video | [arXiv](https://arxiv.org/abs/2009.07833) [Code](https://github.com/google/retiming) | `video` `shadow` `reflection` |

## Graphic Design / Vector Layers

_Layered graphic design, posters, PSD/SVG-style layered outputs._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | arXiv | LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition | [arXiv](https://arxiv.org/abs/2603.17965) | `image` `transparency` `text` |
| 2025 | ICCV 2025 | LayerD: Decomposing Raster Graphic Designs into Layers | [arXiv](https://arxiv.org/abs/2509.25134) [Project](https://cyberagentailab.github.io/LayerD) | `image` `text` |
| 2025 | ICCV 2025 | LayerTracer: Cognitive-Aligned Layered SVG Synthesis via Diffusion Transformer | [arXiv](https://arxiv.org/abs/2502.01105) [Code](https://github.com/showlab/LayerTracer) | `image` `fine-tuned` |

## Datasets & Benchmarks

_Multi-layer datasets, benchmarks and evaluation protocols._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2025 | arXiv | PrismLayers: Open Data for High-Quality Multi-Layer Transparent Image Generative Models | [arXiv](https://arxiv.org/abs/2505.22523) [Project](https://prism-layers.github.io) | `image` `transparency` |
| 2024 | CVPR 2024 | MULAN: A Multi Layer Annotated Dataset for Controllable Text-to-Image Generation | [arXiv](https://arxiv.org/abs/2404.02790) [Project](https://mulan-dataset.github.io) | `image` `transparency` |

## Surveys

_Survey and overview papers._

_No papers yet — PRs welcome!_

## Contributing

Add an entry to [`data/papers.yaml`](data/papers.yaml), run `python scripts/validate.py && python scripts/build_readme.py`, and open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

If you find this list useful, please cite it via the "Cite this repository" button (see [CITATION.cff](CITATION.cff)).

## License

[CC0 1.0](LICENSE) — to the extent possible under law, the maintainers have waived all copyright and related rights to this list.
