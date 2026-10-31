<div align="center">

# Datasets

[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-访问数据集网站-337c79?style=for-the-badge&logo=github)](https://mmifusion.github.io/Datasets/)

### 图像融合与多模态感知数据集导航

A curated collection of datasets and benchmarks for image fusion and multimodal perception.

**[浏览网站 ↗](https://mmifusion.github.io/Datasets/) · [完整目录](docs/CATALOG.md) · [补充与勘误](https://github.com/MMIFusion/Datasets/issues) · [论文库](https://github.com/MMIFusion/ImageFusion)**

110 项资源 · 6 大方向 · 15 组任务

作者：汐萌、方圆 ｜ 公众号「多模态信息融合」

</div>

## 资源范围

| 研究方向 | 资源数 |
| --- | ---: |
| 红外与可见光及相关多模态 | 88 |
| 多聚焦图像融合 | 6 |
| 多曝光图像融合 | 4 |
| 遥感与光谱图像 | 6 |
| 医学与显微图像 | 2 |
| 其他模态与任务 | 4 |

部分资源同时适用于多项任务，按主要用途归类。收录包括原创数据、衍生版本、评测基准和资源集合，不能理解为 110 个独立采集、均可直接下载的数据集。具体信息、开放状态、训练测试划分与许可，以原论文和官方说明为准。本项目提供资源索引，不托管数据集本体。

## 网站

以学术项目主页的简洁排版组织内容，支持全文搜索、六大方向筛选、细分任务筛选、名称与年份排序、完整介绍弹窗、原图查看和独立条目链接。兼容桌面与手机。无需框架或构建依赖，GitHub Pages 从 `main` 分支的 `/docs` 发布。

## 本地预览

```sh
python3 -m http.server 8765 --directory docs
```

在浏览器访问 `http://localhost:8765`。页面通过 HTTP 读取 JSON，请使用本地服务预览。

## 内容维护

项目内容统一放在 `docs/`，包括网站、资源目录、原始材料与维护脚本。详见 [目录结构与维护说明](docs/README.md)。

更新 `docs/data/datasets.json` 后，在仓库根目录运行：

```sh
python3 docs/scripts/build_catalog.py
```

首次发布：仓库 Settings → Pages → Deploy from a branch → `main` → `/docs` → Save。

## License

本项目原创代码与配套原创文档采用 [MIT License](LICENSE)。

Copyright (c) 2026 公众号「多模态信息融合」。

作者：汐萌、方圆。

第三方数据集、论文与示例图片遵循各自原始许可，详见 [第三方版权说明](docs/COPYRIGHT.md)。欢迎通过 Issue 或 Pull Request 补充资源和勘误，详见 [贡献说明](docs/CONTRIBUTING.md)。
