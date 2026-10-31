"""Generate the GitHub-readable catalogue from the website's single data source."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'data/datasets.json').read_text())
lines=['# 图像融合与多模态感知数据集目录','','原创：公众号@多模态信息融合','','[可搜索的网页导航](https://mmifusion.github.io/Datasets/) · [项目介绍](../README.md)','','收录包含数据集、衍生版本、评测基准与资源集合；开放状态及使用许可以原始资源为准。','']
category=None
for d in items:
 if d['category']!=category:
  category=d['category'];lines+=['## '+category,'']
 lines += ['### '+d['title'],'',f"**标签：** {d.get('tagsOriginal',d['task'])}",'',f"**发表团队：** {d['team']}",'',f"**论文题目：** {d['paper']}",'',f"**发表：** {d['publication']}",'']
 for label,note in d['linkNotes'].items():lines += [f'**{label}：** {note}','']
 lines += [d['description'],'']
 for im in d['images']:lines += [f"![{d['name']} 原始示例图]({im['src']})",'']
 lines += [f"[在网页中查看](https://mmifusion.github.io/Datasets/#dataset={d['id']})",'','---','']
(ROOT/'CATALOG.md').write_text('\n'.join(lines))
print('Generated CATALOG.md:',len(items),'entries')
