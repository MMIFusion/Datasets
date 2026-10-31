"""Import the supplied HTML without rewriting its research content."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,re
ROOT=Path(__file__).resolve().parents[1]
soup=BeautifulSoup((ROOT/'source/original.html').read_text(),'html.parser')
heads=[x for x in soup.find_all('section') if 'rgb(39, 63, 85)' in x.get('style','')]
categories=['红外与可见光及相关多模态','多聚焦图像融合','多曝光图像融合','遥感与光谱图像','医学与显微图像','其他模态与任务']
items=[]
for i,h in enumerate(heads):
 nodes=[]
 for n in h.next_elements:
  if i+1<len(heads) and n is heads[i+1]: break
  if getattr(n,'name',None) and n.get_text(' ',strip=True)=='往期推荐': break
  if getattr(n,'name',None) in ('p','blockquote','img') and not h in n.parents:
   if n.name=='p' and n.find_parent('blockquote'): continue
   nodes.append(n)
 title=h.get_text(' ',strip=True)
 fields={}; pending=None; descriptions=[]; images=[]
 for n in nodes:
  if n.name=='blockquote': descriptions.append(n.get_text(' ',strip=True));pending=None;continue
  for img in ([n] if n.name=='img' else []):
   url=img.get('src') or img.get('data-src'); images.append({'source':url,'src':url})
  t=n.get_text(' ',strip=True)
  m=re.match(r'^(标签|发表团队|论文题目|发表|论文链接|下载链接|官方链接|三方下载)[：:]\s*(.*)$',t)
  if m:
   pending=m[1];fields[pending]=m[2]
  elif pending and t: fields[pending]=(fields[pending]+' '+t).strip()
 cat=0 if i<88 else 1 if i<94 else 2 if i<98 else 3 if i<104 else 4 if i<106 else 5
 # Category boundaries are determined from the actual source headings.
 for prev in h.find_all_previous(['p','section']):
  tx=prev.get_text(' ',strip=True)
  match=re.fullmatch(r'[一二三四五六]、(.+)',tx)
  if match and match[1] in categories: cat=categories.index(match[1]);break
 name=re.split(r'数据集|（|\(',title)[0].strip()
 slug=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-') or f'resource-{i+1}'
 if any(x['id']==slug for x in items): slug+=f'-{i+1}'
 links=[]
 for key in ['论文链接','下载链接','官方链接','三方下载']:
  for u in re.findall(r'https?://[^\s<>，；）]+',fields.get(key,'')):
   links.append({'label':{'论文链接':'论文','下载链接':'数据 / 项目','官方链接':'官方资源','三方下载':'三方下载'}[key],'url':u})
 body=' '.join(descriptions)
 status='见原文说明'
 if '待发布' in title: status='待发布'
 elif '待确认' in title or '开放状态待确认' in body: status='开放状态待确认'
 elif '需申请' in title:status='需申请'
 items.append(dict(id=slug,name=name,title=title,category=categories[cat],categoryIndex=cat,task=re.split(r'\s*[｜|【]\s*| Gorund_Truth',fields.get('标签',''))[0].strip(),tagsOriginal=fields.get('标签',''),team=fields.get('发表团队',''),paper=fields.get('论文题目',''),publication=fields.get('发表',''),description='\n\n'.join(descriptions),links=links,linkNotes={k:fields[k] for k in ['论文链接','下载链接','官方链接','三方下载'] if k in fields},images=images,status=status))
for d in items:
 for im in d['images']:
  import hashlib
  cached=list((ROOT/'assets/images').glob(hashlib.sha256(im['source'].encode()).hexdigest()[:16]+'.*'))
  if cached: im['src']=cached[0].relative_to(ROOT).as_posix()
assert len(items)==110,len(items)
assert len({x['id'] for x in items})==110
assert all(x['description'] for x in items)
(ROOT/'data/datasets.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print('Imported',len(items),'resources;',sum(len(x['images']) for x in items),'images')
from collections import Counter
print(Counter(x['category'] for x in items))
