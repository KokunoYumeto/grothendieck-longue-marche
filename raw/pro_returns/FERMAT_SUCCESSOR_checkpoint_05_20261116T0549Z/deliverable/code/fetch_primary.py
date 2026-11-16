from pathlib import Path
import urllib.request,concurrent.futures,hashlib,json
base=Path(__file__).resolve().parents[2]/'work'/'primary'
base.mkdir(parents=True,exist_ok=True)
urls={
'herfort_ribes_1985.pdf':'https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0358/LOG_0014.pdf',
'rubin_1987.pdf':'https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0089/LOG_0029.pdf',
'porowski_2026.pdf':'https://arxiv.org/pdf/2607.27746',
}
def get(k,u):
 try:
  with urllib.request.urlopen(u,timeout=12) as f: b=f.read(20_000_000)
  if not b.startswith(b'%PDF'): return dict(file=k,url=u,status='not PDF',size=len(b))
  (base/k).write_bytes(b)
  return dict(file=k,url=u,status='downloaded',size=len(b),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e: return dict(file=k,url=u,status='failed',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for x in ex.map(lambda kv:get(*kv), urls.items()): print(json.dumps(x))
