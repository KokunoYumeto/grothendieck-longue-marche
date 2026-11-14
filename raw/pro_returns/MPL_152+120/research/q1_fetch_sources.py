from pathlib import Path
import urllib.request, json, concurrent.futures, time
root=Path('research_sources/q1')
root.mkdir(parents=True,exist_ok=True)
d=json.loads((root/'repository_tree.json').read_text())
paths=[x['path'] for x in d['tree'] if x['type']=='blob' and x['path'].startswith('transcripts/') and x['path'].endswith('.fr.tex') and x['path'].split('/')[1] not in {'120','152'}]
print('Search-index files:',len(paths),flush=True)
def fetch(p):
 target=root/'index'/p
 if target.exists(): return (p,'exists')
 target.parent.mkdir(parents=True,exist_ok=True)
 try:
  data=urllib.request.urlopen('https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/'+p,timeout=45).read()
  target.write_bytes(data)
  return(p,'ok')
 except Exception as e: return(p,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
 results=list(ex.map(fetch,paths))
(root/'index_downloads.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print('Search-index downloaded:',sum(v in ['ok','exists'] for _,v in results),'errors:',sum(v not in ['ok','exists'] for _,v in results),flush=True)
def pdf(c):
 p=root/(str(c)+'.pdf')
 if p.exists(): return(c,'exists',p.stat().st_size)
 try:
  with urllib.request.urlopen('https://grothendieck.umontpellier.fr/'+str(c)+'.pdf',timeout=55) as r:
   data=r.read()
  assert data.startswith(b'%PDF'),data[:80]
  p.write_bytes(data)
  return(c,'ok',len(data))
 except Exception as e:return(c,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(pdf,[147,149,150,151]): print(r,flush=True)
