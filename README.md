# Awesome Layered Visual Generation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

🔎 **[Search & filter this list on the web](https://ryugo417.github.io/Awesome-Layered-Visual-Generation/)**

A curated list of papers on **layered representations for visual generation**: layered / transparent (RGBA) image generation, image & video layer decomposition, layer composition (shadows, reflections, harmonization), layer-aware editing, and layered graphic design.

> This list is updated on weekdays with the help of an AI agent and checked by a maintainer. Found a missing paper or a wrong link? Please [open an issue](../../issues/new?template=add_paper.yml) or send a PR.

<!-- AUTO-GENERATED from data/papers.yaml by scripts/build_readme.py. Do not edit README.md by hand. -->

**73 papers · 6 public datasets** · last updated 2026-11-22

## Contents
- [Layered Image Generation](#layered-image-generation) (17)
- [Image Layer Decomposition](#image-layer-decomposition) (18)
- [Layer Composition & Harmonization](#layer-composition--harmonization) (6)
- [Layer-aware Editing](#layer-aware-editing) (3)
- [Layered Video Generation & Decomposition](#layered-video-generation--decomposition) (14)
- [Graphic Design / Vector Layers](#graphic-design--vector-layers) (11)
- [Dataset & Benchmark Papers](#dataset--benchmark-papers) (4)
- [Surveys](#surveys) (0)
- [Datasets](#datasets) (6 public, 8 announced/unclear)

> 💻 = code available (46/73) · Papers per year — 2020: 1 · 2021: 2 · 2022: 1 · 2023: 7 · 2024: 12 · 2025: 24 · 2026: 26

## Layered Image Generation

_Generating transparent (RGBA) images or multiple layers directly from text / conditions._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | arXiv | **LASAGNA**: A Unified and Controllable Framework for Layered Image Generation with Visual Effects | [arXiv](https://arxiv.org/abs/2601.15507) [Project](https://rayjryang.github.io/LASAGNA-Page) | `image` `foreground` `background` `shadow` `reflection` |
| 2026 | CVPR 2026 Findings | LayerFusion: Harmonized Multi-Layer Text-to-Image Generation with Generative Priors | [arXiv](https://arxiv.org/abs/2412.04460) [Project](https://layerfusion.github.io) | `image` `training-free` `transparency` `foreground` `background` |
| 2026 | CVPR 2026 | MRT: Masked Region Transformer for Layered Image Generation and Editing at Scale | [arXiv](https://arxiv.org/abs/2605.27235) | `image` `transparency` |
| 2026 | WACV 2026 | PSDiffusion: Harmonized Multi-Layer Image Generation via Layout and Appearance Alignment 💻 | [arXiv](https://arxiv.org/abs/2505.11468) [Code](https://github.com/dingbang777/PSDiffusion) ![stars](https://img.shields.io/github/stars/dingbang777/PSDiffusion?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` `transparency` |
| 2026 | CVPR 2026 Findings | TAUE: Training-free Noise Transplant and Cultivation Diffusion Model 💻 | [arXiv](https://arxiv.org/abs/2511.02580) [Code](https://github.com/IyatomiLab/TAUE) ![stars](https://img.shields.io/github/stars/IyatomiLab/TAUE?style=flat&label=%E2%98%85&color=yellow) [Project](https://iyatomilab.github.io/TAUE) | `image` `training-free` `foreground` `background` |
| 2025 | arXiv | AlphaVAE: Unified End-to-End RGBA Image Reconstruction and Generation with Alpha-Aware Representation Learning 💻 | [arXiv](https://arxiv.org/abs/2507.09308) [Code](https://github.com/o0o0o00o0/AlphaVAE) ![stars](https://img.shields.io/github/stars/o0o0o00o0/AlphaVAE?style=flat&label=%E2%98%85&color=yellow) | `image` `transparency` |
| 2025 | CVPR 2025 | ART: Anonymous Region Transformer for Variable Multi-Layer Transparent Image Generation 💻 | [arXiv](https://arxiv.org/abs/2502.18364) [Code](https://github.com/microsoft/art-msra) ![stars](https://img.shields.io/github/stars/microsoft/art-msra?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` `transparency` |
| 2025 | ICCV 2025 | DreamLayer: Simultaneous Multi-Layer Generation via Diffusion Model | [arXiv](https://arxiv.org/abs/2503.12838) | `image` `transparency` |
| 2025 | ICCV 2025 | LaRender: Training-Free Occlusion Control in Image Generation via Latent Rendering 💻 | [arXiv](https://arxiv.org/abs/2508.07647) [Code](https://github.com/XiaohangZhan/LaRender) ![stars](https://img.shields.io/github/stars/XiaohangZhan/LaRender?style=flat&label=%E2%98%85&color=yellow) | `image` `training-free` |
| 2025 | arXiv | LayeringDiff: Layered Image Synthesis via Generation, then Disassembly with Generative Knowledge | [arXiv](https://arxiv.org/abs/2501.01197) | `image` `foreground` `background` |
| 2025 | arXiv | OmniAlpha: Aligning Transparency-Aware Generation via Multi-Task Unified Reinforcement Learning 💻 | [arXiv](https://arxiv.org/abs/2511.20211) [Code](https://github.com/Longin-Yu/OmniAlpha) ![stars](https://img.shields.io/github/stars/Longin-Yu/OmniAlpha?style=flat&label=%E2%98%85&color=yellow) | `image` `transparency` |
| 2025 | CVPR 2025 | TKG-DM: Training-free Chroma Key Content Generation Diffusion Model 💻 | [arXiv](https://arxiv.org/abs/2411.15580) [Code](https://github.com/ryugo417/TKG-DM) ![stars](https://img.shields.io/github/stars/ryugo417/TKG-DM?style=flat&label=%E2%98%85&color=yellow) | `image` `training-free` `foreground` `background` |
| 2024 | ECCV 2024 Workshops (AI4VA) | Alfie: Democratising RGBA Image Generation With No $$$ 💻 | [arXiv](https://arxiv.org/abs/2408.14826) [Code](https://github.com/aimagelab/Alfie) ![stars](https://img.shields.io/github/stars/aimagelab/Alfie?style=flat&label=%E2%98%85&color=yellow) | `image` `training-free` `transparency` |
| 2024 | NeurIPS 2024 | Generating Compositional Scenes via Text-to-image RGBA Instance Generation | [arXiv](https://arxiv.org/abs/2411.10913) | `image` `transparency` |
| 2024 | ECCV 2024 | LayerDiff: Exploring Text-guided Multi-layered Composable Image Synthesis via Layer-Collaborative Diffusion Model | [arXiv](https://arxiv.org/abs/2403.11929) | `image` `fine-tuned` `foreground` `background` |
| 2024 | SIGGRAPH 2024 | **LayerDiffuse**: Transparent Image Layer Diffusion using Latent Transparency 💻 | [arXiv](https://arxiv.org/abs/2402.17113) [Code](https://github.com/lllyasviel/LayerDiffuse) ![stars](https://img.shields.io/github/stars/lllyasviel/LayerDiffuse?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` `transparency` `foreground` `background` |
| 2023 | arXiv | Text2Layer: Layered Image Generation using Latent Diffusion Model | [arXiv](https://arxiv.org/abs/2307.09781) | `image` `fine-tuned` `foreground` `background` |

## Image Layer Decomposition

_Decomposing a flat RGB image into layers (foreground/background, instances, effects such as shadows and reflections)._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | CVPR 2026 | Cycle-Consistent Tuning for Layered Image Decomposition | [arXiv](https://arxiv.org/abs/2602.20989) | `image` |
| 2026 | CVPR 2026 | DiffDecompose: Layer-Wise Decomposition of Alpha-Composited Images via Diffusion Transformers 💻 | [arXiv](https://arxiv.org/abs/2505.21541) [Code](https://github.com/Wangzt1121/DiffDecompose) ![stars](https://img.shields.io/github/stars/Wangzt1121/DiffDecompose?style=flat&label=%E2%98%85&color=yellow) | `image` `transparency` |
| 2026 | CVPR 2026 | From Inpainting to Layer Decomposition: Repurposing Generative Inpainting Models for Image Layer Decomposition | [arXiv](https://arxiv.org/abs/2511.20996) | `image` `foreground` `background` |
| 2026 | arXiv | LiWi: Layering in the Wild | [arXiv](https://arxiv.org/abs/2605.14552) | `image` |
| 2026 | CVPR 2026 | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition 💻 | [arXiv](https://arxiv.org/abs/2512.15603) [Code](https://github.com/QwenLM/Qwen-Image-Layered) ![stars](https://img.shields.io/github/stars/QwenLM/Qwen-Image-Layered?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` `transparency` `text` |
| 2026 | ICLR 2026 | Referring Layer Decomposition | [arXiv](https://arxiv.org/abs/2602.19358) | `image` |
| 2026 | ICML 2026 | RevealLayer: Disentangling Hidden and Visible Layers via Occlusion-Aware Image Decomposition 💻 | [arXiv](https://arxiv.org/abs/2605.11818) [Code](https://github.com/360CVGroup/RevealLayer) ![stars](https://img.shields.io/github/stars/360CVGroup/RevealLayer?style=flat&label=%E2%98%85&color=yellow) | `image` `foreground` `background` |
| 2026 | arXiv | See-through: Single-image Layer Decomposition for Anime Characters 💻 | [arXiv](https://arxiv.org/abs/2602.03749) [Code](https://github.com/shitagaki-lab/see-through) ![stars](https://img.shields.io/github/stars/shitagaki-lab/see-through?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2026 | arXiv | Stable-Layers: Fine-Tuning Image Layer Decomposition Models with VLM-Scored Reinforcement Learning 💻 | [arXiv](https://arxiv.org/abs/2605.30257) [Code](https://github.com/Stability-AI/Stable-Layers) ![stars](https://img.shields.io/github/stars/Stability-AI/Stable-Layers?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` |
| 2026 | arXiv | Workflow-Aware Structured Layer Decomposition for Illustration Production 💻 | [arXiv](https://arxiv.org/abs/2603.14925) [Code](https://github.com/zty0304/Anime-layer-decomposition) ![stars](https://img.shields.io/github/stars/zty0304/Anime-layer-decomposition?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2025 | SIGGRAPH 2025 | AssetDropper: Asset Extraction via Diffusion Models with Reward-Driven Optimization 💻 | [arXiv](https://arxiv.org/abs/2506.07738) [Code](https://github.com/Lanjiong-Li/AssetDropper) ![stars](https://img.shields.io/github/stars/Lanjiong-Li/AssetDropper?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2025 | arXiv | Controllable Layer Decomposition for Reversible Multi-Layer Image Generation 💻 | [arXiv](https://arxiv.org/abs/2511.16249) [Code](https://github.com/monkek123King/CLD) ![stars](https://img.shields.io/github/stars/monkek123King/CLD?style=flat&label=%E2%98%85&color=yellow) | `image` `transparency` |
| 2025 | CVPR 2025 | **LayerDecomp**: Generative Image Layer Decomposition with Visual Effects 💻 | [arXiv](https://arxiv.org/abs/2411.17864) [Code](https://github.com/Rayjryang/LayerDecomp) ![stars](https://img.shields.io/github/stars/Rayjryang/LayerDecomp?style=flat&label=%E2%98%85&color=yellow) [Project](https://rayjryang.github.io/LayerDecomp) | `image` `fine-tuned` `foreground` `background` `shadow` `reflection` |
| 2024 | SIGGRAPH Asia 2024 (TOG) | Colorful Diffuse Intrinsic Image Decomposition in the Wild 💻 | [arXiv](https://arxiv.org/abs/2409.13690) [Code](https://github.com/compphoto/Intrinsic) ![stars](https://img.shields.io/github/stars/compphoto/Intrinsic?style=flat&label=%E2%98%85&color=yellow) | `image` `light` |
| 2024 | SIGGRAPH 2024 | Object-level Scene Deocclusion | [arXiv](https://arxiv.org/abs/2406.07706) | `image` `foreground` `background` |
| 2024 | CVPR 2024 | pix2gestalt: Amodal Segmentation by Synthesizing Wholes 💻 | [arXiv](https://arxiv.org/abs/2401.14398) [Code](https://github.com/cvlab-columbia/pix2gestalt) ![stars](https://img.shields.io/github/stars/cvlab-columbia/pix2gestalt?style=flat&label=%E2%98%85&color=yellow) [Project](https://gestalt.cs.columbia.edu) | `image` `fine-tuned` `foreground` |
| 2024 | SIGGRAPH 2024 | RGB↔X: Image Decomposition and Synthesis Using Material- and Lighting-aware Diffusion Models 💻 | [arXiv](https://arxiv.org/abs/2405.00666) [Code](https://github.com/zheng95z/rgbx) ![stars](https://img.shields.io/github/stars/zheng95z/rgbx?style=flat&label=%E2%98%85&color=yellow) | `image` `light` |
| 2023 | TOG 2023 | Intrinsic Image Decomposition via Ordinal Shading 💻 | [arXiv](https://arxiv.org/abs/2311.12792) [Code](https://github.com/compphoto/Intrinsic) ![stars](https://img.shields.io/github/stars/compphoto/Intrinsic?style=flat&label=%E2%98%85&color=yellow) | `image` `light` |

## Layer Composition & Harmonization

_Inserting / compositing objects or layers into scenes, including shadow, reflection and lighting synthesis._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2025 | ICLR 2025 | Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models | [arXiv](https://arxiv.org/abs/2411.07232) | `image` `training-free` `foreground` `shadow` |
| 2025 | arXiv | Controllable Shadow Generation with Single-Step Diffusion Models from Synthetic Data | [arXiv](https://arxiv.org/abs/2412.11972) [Project](https://gojasper.github.io/controllable-shadow-generation-project) | `image` `fine-tuned` `shadow` `light` |
| 2025 | ICLR 2025 | **IC-Light**: Scaling In-the-Wild Training for Diffusion-based Illumination Harmonization and Editing by Imposing Consistent Light Transport 💻 | [Code](https://github.com/lllyasviel/IC-Light) ![stars](https://img.shields.io/github/stars/lllyasviel/IC-Light?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` `light` `foreground` `background` |
| 2024 | ECCV 2024 | ObjectDrop: Bootstrapping Counterfactuals for Photorealistic Object Removal and Insertion | [arXiv](https://arxiv.org/abs/2403.18818) [Project](https://objectdrop.github.io) | `image` `fine-tuned` `shadow` `reflection` |
| 2023 | WACV 2024 | Collage Diffusion | [arXiv](https://arxiv.org/abs/2303.00262) [Project](https://vsanimator.github.io/collage_diffusion) | `image` |
| 2023 | CVPR 2023 | ObjectStitch: Generative Object Compositing | [arXiv](https://arxiv.org/abs/2212.00932) | `image` `fine-tuned` `foreground` `background` |

## Layer-aware Editing

_Editing that operates on, or produces, layered representations._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | AAAI 2026 | LayerEdit: Disentangled Multi-Object Editing via Conflict-Aware Multi-Layer Learning 💻 | [arXiv](https://arxiv.org/abs/2511.08251) [Code](https://github.com/fufy1024/LayerEdit) ![stars](https://img.shields.io/github/stars/fufy1024/LayerEdit?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2024 | CVPR 2024 | Move Anything with Layered Scene Diffusion | [arXiv](https://arxiv.org/abs/2404.07178) | `image` |
| 2022 | ECCV 2022 | Text2LIVE: Text-Driven Layered Image and Video Editing 💻 | [arXiv](https://arxiv.org/abs/2204.02491) [Code](https://github.com/omerbt/Text2LIVE) ![stars](https://img.shields.io/github/stars/omerbt/Text2LIVE?style=flat&label=%E2%98%85&color=yellow) | `image` `video` `transparency` |

## Layered Video Generation & Decomposition

_RGBA video generation, omnimatte-style video layer decomposition, layered video editing._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | ICML 2026 | LayerT2V: A Unified Multi-Layer Video Generation Framework 💻 | [arXiv](https://arxiv.org/abs/2508.04228) [Code](https://github.com/guangzhaoli/LayerT2V) ![stars](https://img.shields.io/github/stars/guangzhaoli/LayerT2V?style=flat&label=%E2%98%85&color=yellow) | `video` `foreground` `background` |
| 2026 | arXiv | Vera: A Layered Diffusion Model for Content-Preserving Video Editing | [arXiv](https://arxiv.org/abs/2606.23610) | `video` |
| 2026 | CVPR 2026 | **Wan-Alpha**: Video Generation with Stable Transparency via Shiftable RGB-A Distribution Learner 💻 | [arXiv](https://arxiv.org/abs/2509.24979) [Code](https://github.com/WeChatCV/Wan-Alpha) ![stars](https://img.shields.io/github/stars/WeChatCV/Wan-Alpha?style=flat&label=%E2%98%85&color=yellow) [Project](https://donghaotian123.github.io/Wan-Alpha) | `video` `fine-tuned` `transparency` |
| 2025 | CVPR 2025 | Generative Omnimatte: Learning to Decompose Video into Layers 💻 | [arXiv](https://arxiv.org/abs/2411.16683) [Code](https://github.com/gen-omnimatte/gen-omnimatte-public) ![stars](https://img.shields.io/github/stars/gen-omnimatte/gen-omnimatte-public?style=flat&label=%E2%98%85&color=yellow) | `video` `fine-tuned` `shadow` `reflection` |
| 2025 | ICCV 2025 | LayerAnimate: Layer-level Control for Animation 💻 | [arXiv](https://arxiv.org/abs/2501.08295) [Code](https://github.com/IamCreateAI/LayerAnimate) ![stars](https://img.shields.io/github/stars/IamCreateAI/LayerAnimate?style=flat&label=%E2%98%85&color=yellow) [Project](https://layeranimate.github.io) | `video` `fine-tuned` `foreground` `background` |
| 2025 | SIGGRAPH 2025 | LayerFlow: A Unified Model for Layer-aware Video Generation 💻 | [arXiv](https://arxiv.org/abs/2506.04228) [Code](https://github.com/SihuiJi/LayerFlow) ![stars](https://img.shields.io/github/stars/SihuiJi/LayerFlow?style=flat&label=%E2%98%85&color=yellow) [Project](https://sihuiji.github.io/LayerFlow-Page) | `video` `fine-tuned` `transparency` `foreground` `background` |
| 2025 | SIGGRAPH Asia 2025 | OmnimatteZero: Fast Training-free Omnimatte with Pre-trained Video Diffusion Models 💻 | [arXiv](https://arxiv.org/abs/2503.18033) [Code](https://github.com/dvirsamuel/OmnimatteZero) ![stars](https://img.shields.io/github/stars/dvirsamuel/OmnimatteZero?style=flat&label=%E2%98%85&color=yellow) | `video` `training-free` `shadow` `reflection` |
| 2025 | CVPR 2025 | **TransPixar**: TransPixeler: Advancing Text-to-Video Generation with Transparency 💻 | [arXiv](https://arxiv.org/abs/2501.03006) [Code](https://github.com/wileewang/TransPixar) ![stars](https://img.shields.io/github/stars/wileewang/TransPixar?style=flat&label=%E2%98%85&color=yellow) [Project](https://wileewang.github.io/TransPixar) | `video` `fine-tuned` `transparency` |
| 2023 | SIGGRAPH 2023 (TOG) | FactorMatte: Redefining Video Matting for Re-Composition Tasks 💻 | [arXiv](https://arxiv.org/abs/2211.02145) [Code](https://github.com/jaclyngu/FactorMatte) ![stars](https://img.shields.io/github/stars/jaclyngu/FactorMatte?style=flat&label=%E2%98%85&color=yellow) [Project](https://factormatte.github.io) | `video` `shadow` `reflection` |
| 2023 | ICCV 2023 | OmnimatteRF: Robust Omnimatte with 3D Background Modeling 💻 | [arXiv](https://arxiv.org/abs/2309.07749) [Code](https://github.com/facebookresearch/OmnimatteRF) ![stars](https://img.shields.io/github/stars/facebookresearch/OmnimatteRF?style=flat&label=%E2%98%85&color=yellow) [Project](https://omnimatte-rf.github.io) | `video` `3d` `background` `shadow` |
| 2023 | CVPR 2023 | Shape-aware Text-driven Layered Video Editing 💻 | [arXiv](https://arxiv.org/abs/2301.13173) [Code](https://github.com/text-video-edit/shape-aware-text-driven-layered-video-editing-release) ![stars](https://img.shields.io/github/stars/text-video-edit/shape-aware-text-driven-layered-video-editing-release?style=flat&label=%E2%98%85&color=yellow) | `video` |
| 2021 | SIGGRAPH Asia 2021 | Layered Neural Atlases for Consistent Video Editing 💻 | [arXiv](https://arxiv.org/abs/2109.11418) [Code](https://github.com/ykasten/layered-neural-atlases) ![stars](https://img.shields.io/github/stars/ykasten/layered-neural-atlases?style=flat&label=%E2%98%85&color=yellow) [Project](https://layered-neural-atlases.github.io) | `video` |
| 2021 | CVPR 2021 | Omnimatte: Associating Objects and Their Effects in Video 💻 | [arXiv](https://arxiv.org/abs/2105.06993) [Code](https://github.com/erikalu/omnimatte) ![stars](https://img.shields.io/github/stars/erikalu/omnimatte?style=flat&label=%E2%98%85&color=yellow) | `video` `shadow` `reflection` |
| 2020 | SIGGRAPH Asia 2020 | Layered Neural Rendering for Retiming People in Video 💻 | [arXiv](https://arxiv.org/abs/2009.07833) [Code](https://github.com/google/retiming) ![stars](https://img.shields.io/github/stars/google/retiming?style=flat&label=%E2%98%85&color=yellow) | `video` `shadow` `reflection` |

## Graphic Design / Vector Layers

_Layered graphic design, posters, PSD/SVG-style layered outputs._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2026 | arXiv | CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers | [arXiv](https://arxiv.org/abs/2604.19632) | `image` `text` |
| 2026 | arXiv | Does Synthetic Layered Design Data Benefit Layered Design Decomposition? 💻 | [arXiv](https://arxiv.org/abs/2605.15167) [Code](https://github.com/YangHaolin0526/SynLayers) ![stars](https://img.shields.io/github/stars/YangHaolin0526/SynLayers?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2026 | CVPR 2026 Workshops | LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition | [arXiv](https://arxiv.org/abs/2603.17965) | `image` `transparency` `text` |
| 2026 | CVPR 2026 | PSDesigner: Automated Graphic Design with a Human-Like Creative Workflow 💻 | [arXiv](https://arxiv.org/abs/2603.25738) [Code](https://github.com/FudanCVL/PSDesigner) ![stars](https://img.shields.io/github/stars/FudanCVL/PSDesigner?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2026 | CVPR 2026 | SemLayer: Semantic-aware Generative Segmentation and Layer Construction for Abstract Icons | [arXiv](https://arxiv.org/abs/2603.24039) | `image` |
| 2026 | AAAI 2026 | Step-by-step Layered Design Generation | [arXiv](https://arxiv.org/abs/2512.03335) | `image` |
| 2026 | CVPR 2026 | Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure | [arXiv](https://arxiv.org/abs/2512.14336) | `video` |
| 2025 | ICCV 2025 | LayerD: Decomposing Raster Graphic Designs into Layers 💻 | [arXiv](https://arxiv.org/abs/2509.25134) [Code](https://github.com/CyberAgentAILab/LayerD) ![stars](https://img.shields.io/github/stars/CyberAgentAILab/LayerD?style=flat&label=%E2%98%85&color=yellow) [Project](https://cyberagentailab.github.io/LayerD) | `image` `text` |
| 2025 | SIGGRAPH Asia 2025 | LayerPeeler: Autoregressive Peeling for Layer-wise Image Vectorization 💻 | [arXiv](https://arxiv.org/abs/2505.23740) [Code](https://github.com/kingnobro/LayerPeeler) ![stars](https://img.shields.io/github/stars/kingnobro/LayerPeeler?style=flat&label=%E2%98%85&color=yellow) | `image` |
| 2025 | ICCV 2025 | LayerTracer: Cognitive-Aligned Layered SVG Synthesis via Diffusion Transformer 💻 | [arXiv](https://arxiv.org/abs/2502.01105) [Code](https://github.com/showlab/LayerTracer) ![stars](https://img.shields.io/github/stars/showlab/LayerTracer?style=flat&label=%E2%98%85&color=yellow) | `image` `fine-tuned` |
| 2025 | arXiv | OmniPSD: Layered PSD Generation with Diffusion Transformer 💻 | [arXiv](https://arxiv.org/abs/2512.09247) [Code](https://github.com/showlab/OmniPSD) ![stars](https://img.shields.io/github/stars/showlab/OmniPSD?style=flat&label=%E2%98%85&color=yellow) | `image` `transparency` |

## Dataset & Benchmark Papers

_Multi-layer datasets, benchmarks and evaluation protocols._

| Year | Venue | Title | Links | Tags |
|---|---|---|---|---|
| 2025 | arXiv | PrismLayers: Open Data for High-Quality Multi-Layer Transparent Image Generative Models 💻 | [arXiv](https://arxiv.org/abs/2505.22523) [Code](https://github.com/redredsheep/PrismLayers) ![stars](https://img.shields.io/github/stars/redredsheep/PrismLayers?style=flat&label=%E2%98%85&color=yellow) [Project](https://prism-layers.github.io) | `image` `transparency` |
| 2025 | ICCV 2025 | Seeing and Seeing Through the Glass: Real and Synthetic Data for Multi-Layer Depth Estimation 💻 | [arXiv](https://arxiv.org/abs/2503.11633) [Code](https://github.com/princeton-vl/LayeredDepth) ![stars](https://img.shields.io/github/stars/princeton-vl/LayeredDepth?style=flat&label=%E2%98%85&color=yellow) | `image` `3d` `transparency` |
| 2024 | CVPR 2024 | MAGICK: A Large-scale Captioned Dataset from Matting Generated Images using Chroma Keying | [Project](https://ryanndagreat.github.io/MAGICK) | `image` `transparency` |
| 2024 | CVPR 2024 | MULAN: A Multi Layer Annotated Dataset for Controllable Text-to-Image Generation | [arXiv](https://arxiv.org/abs/2404.02790) [Project](https://mulan-dataset.github.io) | `image` `transparency` |

## Surveys

_Survey and overview papers._

_No papers yet — PRs welcome!_

## Datasets

_Layered datasets, including data released alongside method papers. Status is re-checked by the daily agent._

### Public (downloadable)

| Dataset | Paper | Modality | Content | Size | License | Link | Checked |
|---|---|---|---|---|---|---|---|
| **Crello** | [paper](https://arxiv.org/abs/2108.01249) | design | Graphic design templates with per-element layers (pre-rendered images / text boxes) and canvas metadata | 10K–100K documents | CDLA-Permissive-2.0 | [Download](https://huggingface.co/datasets/cyberagent/crello) | 2026-11-22 |
| **LayeredDepth** | [Seeing and Seeing Through the Glass: Real and Synthetic Data for Multi-Layer Depth Estimation](https://arxiv.org/abs/2503.11633) (ICCV 2025) | 3d | Multi-layer (through-glass) relative depth; real benchmark with human annotations + procedural synthetic set | 1,500 real images; 15,300 synthetic images | CC0 (images and validation annotations) | [Download](https://layereddepth.cs.princeton.edu) | 2026-11-22 |
| **MAGICK** | [MAGICK](https://ryanndagreat.github.io/MAGICK) (CVPR 2024) | image | Single-subject generated RGBA images (alpha via chroma keying) with captions | 140K+ images, 1024x1024 | - | [Download](https://huggingface.co/datasets/OneOverZero/MAGICK) | 2026-11-22 |
| **MuLAn** | [MuLAn](https://arxiv.org/abs/2404.02790) (CVPR 2024) | image | Natural images (COCO / LAION Aesthetics) decomposed into a background + instance RGBA layer stack with captions | 44K+ images, 100K+ instances | - | [Download](https://huggingface.co/datasets/mulan-dataset/v1.0) | 2026-11-22 |
| **PrismLayersPro** | [PrismLayers](https://arxiv.org/abs/2505.22523) (arXiv) | image | Synthetic multi-layer transparent images; up to 50 RGBA layers per sample, each with caption and bounding box, plus whole image and base layer | 20,046 samples (21 style categories) | Apache-2.0 | [Download](https://huggingface.co/datasets/creative-graphic-design/PrismLayersPro) | 2026-11-22 |
| **VidLayer** | [LayerT2V](https://arxiv.org/abs/2508.04228) (ICML 2026) | video | Raw video, background-only video, foreground video and foreground masks, with layer-level captions | ~50K samples (from 200K source clips) | - | [Download](https://huggingface.co/datasets/kr-cen/VidLayer) | 2026-11-22 |

### Announced (release promised, not downloadable yet)

| Dataset | Paper | Modality | Content | Size | License | Link | Checked |
|---|---|---|---|---|---|---|---|
| **AlphaBlend** | [DiffDecompose](https://arxiv.org/abs/2505.21541) (CVPR 2026) | image | Semi-transparent / transparent layer decomposition across six subtasks (flare, fog, glassware, X-ray, ...) | - | - | [Page](https://github.com/Wangzt1121/DiffDecompose) | 2026-11-22 |
| **LASAGNA-48K / LasagnaBench** | [LASAGNA](https://arxiv.org/abs/2601.15507) (arXiv) | image | Composite + clean background + foreground layer with visual effects (shadows, reflections) and captions | 48K triplets; 242-image human-decomposed benchmark | - | [Page](https://rayjryang.github.io/LASAGNA-Page) | 2026-11-22 |
| **LiWi-100k** | [LiWi](https://arxiv.org/abs/2605.14552) (arXiv) | image | In-the-wild photos decomposed into layers with shadows / lighting effects kept | 100K+ images | - | [Page](https://rassetmusty.github.io/LiWi) | 2026-11-22 |
| **RefLade** | [Referring Layer Decomposition](https://arxiv.org/abs/2602.19358) (ICLR 2026) | image | Image–RGBA layer–prompt triplets for prompt-conditioned layer decomposition | 430K images, 1.11M layers (incl. 100K curated, 10K test) | - | [Page](https://yaojie-shen.github.io/project/RLD) | 2026-11-22 |
| **RevealLayer-100K / RevealLayerBench** | [RevealLayer](https://arxiv.org/abs/2605.11818) (ICML 2026) | image | Natural images with background + per-object RGBA layers (visible and occluded parts) and boxes | 100K training tuples; 200-sample benchmark | - | [Page](https://360cvgroup.github.io/RevealLayer/) | 2026-11-22 |

### Status unclear

| Dataset | Paper | Modality | Content | Size | License | Link | Checked |
|---|---|---|---|---|---|---|---|
| **AlphaLayers** | [OmniAlpha](https://arxiv.org/abs/2511.20211) (arXiv) | image | Foreground / background / composite RGBA triplets with masks and captions | 1,000 triplets (512x512) | - | [Page](https://github.com/Longin-Yu/OmniAlpha) | 2026-11-22 |
| **Controllable Shadow Generation benchmark** | [Controllable Shadow Generation with Single-Step Diffusion Models from Synthetic Data](https://arxiv.org/abs/2412.11972) (arXiv) | image | Object images with shadow maps under varied light direction / softness / intensity | - | - | [Page](https://gojasper.github.io/controllable-shadow-generation-project) | 2026-11-22 |
| **SynLayers** | [Does Synthetic Layered Design Data Benefit Layered Design Decomposition?](https://arxiv.org/abs/2605.15167) (arXiv) | design | Fully synthetic layered graphic-design data (code and model are public; dataset link not found) | - | - | [Page](https://yanghaolin0526.github.io/SynLayers/) | 2026-11-22 |

## Contributing

Add an entry to [`data/papers.yaml`](data/papers.yaml), run `python scripts/validate.py && python scripts/build_readme.py`, and open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

If you find this list useful, please cite it via the "Cite this repository" button (see [CITATION.cff](CITATION.cff)).

## License

[CC0 1.0](LICENSE) — to the extent possible under law, the maintainers have waived all copyright and related rights to this list.
