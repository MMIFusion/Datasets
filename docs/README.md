# 网站与内容维护

[项目首页](../README.md) · [在线网站](https://mmifusion.github.io/Datasets/) · [完整目录](CATALOG.md) · [贡献说明](CONTRIBUTING.md)

## 目录结构

```text
docs/
├── README.md                 本目录说明
├── index.html                网站入口与页面文案
├── CATALOG.md                完整数据集目录，由脚本生成
├── CONTRIBUTING.md           资源补充与勘误说明
├── data/datasets.json        网站与完整目录共用的数据
├── assets/                   样式、交互脚本、图标及原图
├── scripts/                  内容维护工具
├── source/original.html      原始 HTML 存档
├── .nojekyll                 静态文件发布标记
└── .gitignore                本目录的忽略规则
```

GitHub Pages 从 `main` 分支的 `/docs` 发布，首页为 `index.html`。这里的 README 是维护文档，不替代网站首页。网站运行不执行 Python 脚本，也不读取原始 HTML。

## 日常更新

以下命令均在仓库根目录运行。

1. 编辑 `docs/data/datasets.json`。保留已有条目的 `id`，避免分享链接失效。
2. 如有新配图，将图片放入 `docs/assets/images/`，并在数据中保留来源链接。
3. 运行 `python3 docs/scripts/build_catalog.py`，同步生成 `docs/CATALOG.md`。
4. 本地预览检查后提交并推送，Pages 自动重新发布。

```sh
python3 -m http.server 8765 --directory docs
```

访问 `http://localhost:8765`。修改外观用 `docs/assets/style.css`，修改搜索、筛选与详情交互用 `docs/assets/app.js`。

## 工具与原稿

- `scripts/build_catalog.py`：读取 JSON 生成 Markdown 目录，仅依赖 Python 标准库。
- `scripts/import_source.py`：从 `source/original.html` 重新提取数据，需要 `beautifulsoup4`。会覆盖 JSON，不用于常规增量更新。
- `scripts/cache_images.py`：根据 JSON 中的原始图片 URL 下载图片，更新本地路径，保留下载字节，不裁剪或改色。需要网络。
- `source/original.html`：最初提供的完整 HTML，保留原文及文末推荐，用于核对和追溯；不会随 JSON 修改自动同步。

脚本通过自身路径定位 `docs/`，也可从其他工作目录调用。
