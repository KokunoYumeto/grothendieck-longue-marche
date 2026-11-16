from pathlib import Path
import urllib.request,concurrent.futures,hashlib,json
base=Path(__file__).resolve().parents[2]/'work'/'primary'
base.mkdir(parents=True,exist_ok=True)
urls={
'mazur_1977.pdf':'https://www.numdam.org/item/PMIHES_1977__47__33_0.pdf',
'kisin_serre2.dvi':'https://people.math.harvard.edu/~kisin/dvifiles/serre2.dvi',
'serre_1972.pdf':'https://wstein.org/sage_summer/bsd_comp/Serre-properties_galoisiennes_des_points_dordre_fini_des_courbes_elliptiques.pdf',
}
def get(k,u):
 try:
  with urllib.request.urlopen(u,timeout=15) as f: b=f.read(30_000_000)
  if k.endswith('.pdf') and not b.startswith(b'%PDF'): return dict(file=k,url=u,status='not PDF',size=len(b))
  (base/k).write_bytes(b)
  return dict(file=k,url=u,status='downloaded',size=len(b),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e: return dict(file=k,url=u,status='failed',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 fs=[ex.submit(get,k,u) for k,u in urls.items()]
 for f in concurrent.futures.as_completed(fs): print(json.dumps(f.result()),flush=True)
