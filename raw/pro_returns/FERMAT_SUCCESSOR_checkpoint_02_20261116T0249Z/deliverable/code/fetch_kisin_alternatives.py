from pathlib import Path
import urllib.request, concurrent.futures, hashlib, json
base=Path(__file__).resolve().parents[2]/'work'/'primary'
urls=[
('kisin_author.dvi','https://www.math.harvard.edu/~kisin/dvifiles/serre2.dvi'),
('kisin_author.pdf','https://people.math.harvard.edu/~kisin/dvifiles/serre2.pdf'),
('kisin_published.pdf','https://link.springer.com/content/pdf/10.1007/s00222-009-0207-5.pdf'),
]
def fetch(item):
 name,url=item
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(request,timeout=20) as response:
   data=response.read(20_000_000)
  kind='PDF' if data.startswith(b'%PDF') else ('DVI' if data.startswith(b'\xf7') else 'other')
  if kind in ('PDF','DVI'): (base/name).write_bytes(data)
  return dict(name=name,url=url,status=kind,size=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e:return dict(name=name,url=url,status='failed',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for out in pool.map(fetch,urls):print(json.dumps(out),flush=True)
