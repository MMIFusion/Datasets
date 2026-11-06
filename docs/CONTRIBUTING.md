# 补充资源与勘误

欢迎通过 Issue 或 Pull Request 补充图像融合与相关多模态感知资源。

## Issue 提交步骤与模板

新增资源、补充插图、更新链接或纠正条目时，请按 [README 中的完整流程与填写模板](../README.md#通过-issue-补充数据集或勘误) 提交。

先搜索已有条目和 Issues，再点击 [新建 Issue](https://github.com/MMIFusion/Datasets/issues/new)。填写正文后，将插图拖入编辑框并等待上传完成，注明来源，再点击 **Submit new issue**。维护者核对后更新仓库及网站；后续材料可在同一 Issue 中补充。

## 内容要求与 Pull Request 维护

请提供全部论文作者（按原文署名顺序）、发表团队及机构、数据集名称、模态、适用任务、原论文或官方项目页、公开状态，以及需要修改的信息和支持依据。标明是原创采集、衍生版本、评测基准还是资源集合；没有证据时不推断发表状态或可下载状态。

在仓库根目录修改 `docs/data/datasets.json`，运行 `python3 docs/scripts/build_catalog.py` 同步完整目录。保留既有条目的 `id`，避免分享链接失效。新增图片请注明来源，不修改原图内容。

提交内容前请阅读 [版权与使用说明](COPYRIGHT.md)，并确认所提交文字、链接与图片的来源及使用权限。
