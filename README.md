<div align="center">

# MMIF Datasets

<a href="https://mmifusion.github.io/Datasets/"><img src="docs/assets/website-button-charcoal.svg" alt="访问数据集网站" width="196" height="40"></a>
&nbsp;&nbsp;
<a href="https://mp.weixin.qq.com/s/ygUEl8rsOwjVFrlY5kdRDw"><img src="docs/assets/wechat-button-forest.svg" alt="微信公众号原文" width="196" height="40"></a>

### 图像融合与多模态感知数据集导航

A curated collection of datasets and benchmarks for image fusion and multimodal perception.

**[浏览网站 ↗](https://mmifusion.github.io/Datasets/) · [完整目录](docs/CATALOG.md) · [补充与勘误](https://github.com/MMIFusion/Datasets/issues) · [论文库](https://github.com/MMIFusion/ImageFusion)**

111 项资源 · 6 大方向 · 16 组任务

作者：汐萌、囗〇 ｜ 公众号「多模态信息融合」

</div>

## 资源范围

<div align="center">
<table align="center">
  <thead>
    <tr><th align="center">研究方向</th><th align="center">资源数</th></tr>
  </thead>
  <tbody>
    <tr><td align="center">红外与可见光及相关多模态</td><td align="center">88</td></tr>
    <tr><td align="center">多聚焦图像融合</td><td align="center">6</td></tr>
    <tr><td align="center">多曝光图像融合</td><td align="center">4</td></tr>
    <tr><td align="center">遥感与光谱图像</td><td align="center">7</td></tr>
    <tr><td align="center">医学与显微图像</td><td align="center">2</td></tr>
    <tr><td align="center">其他模态与任务</td><td align="center">4</td></tr>
  </tbody>
</table>
</div>

部分资源同时适用于多项任务，按主要用途归类。收录包括原创数据、衍生版本、评测基准和资源集合，不能理解为 111 个独立采集、均可直接下载的数据集。具体信息、开放状态、训练测试划分与许可，以原论文和官方说明为准。本项目提供资源索引，不托管数据集本体。

## 通过 Issue 补充数据集或勘误

1. 登录 GitHub，在网站和 [已有 Issues](https://github.com/MMIFusion/Datasets/issues) 中搜索数据集名称，确认是否已收录或有人提交。
2. 点击 [新建 Issue](https://github.com/MMIFusion/Datasets/issues/new)，按下方格式填写标题与正文。
3. 将示例图拖入正文，等待上传完成，保留生成的图片链接，并注明图片来源。
4. 点击 **Submit new issue** 提交。维护者核对后将条目、插图与目录同步到仓库及网站；需要补充材料时会在原 Issue 中回复。

### 新增数据集

标题使用 `[新增数据集] 数据集名称`，正文可直接复制以下模板。

```markdown
### 数据集名称
名称及简称：

### 分类与任务
所属分类（六选一）：红外与可见光及相关多模态 / 多聚焦图像融合 / 多曝光图像融合 / 遥感与光谱图像 / 医学与显微图像 / 其他模态与任务
输入模态：
适用任务：
资源类型：原创采集 / 衍生版本 / 评测基准 / 资源集合

### 团队与发表信息
发表团队及机构：
论文名称：
期刊或会议及年份（未发表请写预印本或未发表）：
发表状态依据链接：

### 资源链接
论文链接：
官方项目 / 代码仓库：
下载链接：
开放状态：可直接下载 / 需申请 / 尚未公开 / 待确认
使用许可或条件（附官方说明链接）：

### 数据集介绍
请介绍研究用途、数据来源、规模、模态、任务、标注及主要特点。
不确定的信息请标注“待确认”。

### 示例图
在这里拖入图片，或粘贴公开可访问的原图链接。
图片来源（论文图号或官方页面）：

### 其他说明（选填）
```

### 现有条目勘误

标题使用 `[勘误] 数据集名称 — 修改内容`，正文可直接复制以下模板。

```markdown
### 数据集名称及条目链接

### 当前信息 / 遇到的问题

### 建议修改为

### 支持依据
原论文、官方仓库或下载页面链接：

### 图片（选填）
如需更换插图，请上传图片并注明来源。
```

不适用的项目可写“无”。更多维护方式见 [贡献说明](docs/CONTRIBUTING.md)。

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

作者：汐萌、囗〇。

第三方数据集、论文与示例图片遵循各自原始许可，详见 [第三方版权说明](docs/COPYRIGHT.md)。欢迎通过 Issue 或 Pull Request 补充资源和勘误，详见 [贡献说明](docs/CONTRIBUTING.md)。
