"""Cache supplied illustration URLs locally, preserving downloaded bytes."""
from pathlib import Path
import json,urllib.request,concurrent.futures,hashlib
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'docs/data/datasets.json';items=json.loads(p.read_text())
urls=list(dict.fromkeys(im['source'] for d in items for im in d['images']))
def fetch(url):
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=30) as r:
   data=r.read();typ=r.headers.get('Content-Type','')
  ext='png' if data[:8]==b'\x89PNG\r\n\x1a\n' else 'jpg' if data[:2]==b'\xff\xd8' else 'gif' if data[:3]==b'GIF' else 'webp' if data[:4]==b'RIFF' else None
  if not ext: raise ValueError('Not an image: '+typ)
  rel='assets/images/'+hashlib.sha256(url.encode()).hexdigest()[:16]+'.'+ext
  (ROOT/'docs'/rel).write_bytes(data)
  return url,rel
 except Exception as e: print('Image failed',urls.index(url),type(e).__name__);return url,url
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: mapping=dict(pool.map(fetch,urls))
for d in items:
 for im in d['images']: im['src']=mapping[im['source']]
p.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
print('Cached',sum(not p.startswith('http') for p in mapping.values()),'/',len(urls),'unique illustrations')
