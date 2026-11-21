"""Exact root-text capture helpers; no image access or authority inference."""
from pathlib import Path
import hashlib,json,re,runpy,sys
sys.dont_write_bytecode=True
BASE=Path('/workspace/scratch/94548b74fbe0');OUT=BASE/'out/checks'
sha=lambda b:hashlib.sha256(b.encode() if isinstance(b,str) else b).hexdigest()
dump=lambda v:(json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode()
def save(name,value,raw=False):
 assert name.startswith('scan026_source_') and '/' not in name
 b=value if raw else dump(value);p=OUT/name
 if p.exists():assert p.read_bytes()==b,('immutable source output differs',name)
 else:p.write_bytes(b)
 return {'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b)}
def capture(label,requested):
 captures={};text={}
 for kind,suffix in [('decisions','json'),('journal','md')]:
  original=f'out/checks/scan026_root_{kind}.{suffix}'
  name=f'scan026_source_authority_{label}_root_{kind}.{suffix}';p=OUT/name
  if not p.exists():save(name,(BASE/original).read_bytes(),True)
  b=p.read_bytes();text[kind]=b.decode()
  captures[kind]={'path':'out/checks/'+name,'sha256':sha(b),'bytes':len(b),'original_root_path':original}
 D,J=text['decisions'],text['journal'];data=json.loads(D)
 current=json.loads((OUT/'scan026_root_decisions.json').read_bytes())
 selected={d['section']:d for d in data['decisions'] if d['section'] in requested}
 assert set(selected)==set(requested),(requested,list(selected))
 for s,d in selected.items():assert next(x for x in current['decisions'] if x['section']==s)==d
 heads=list(re.finditer(r'^## (\d\d) — .+$',J,re.M));sections={}
 for i,m in enumerate(heads):
  if m.group(1) in selected:sections[m.group(1)]=(m.start(),heads[i+1].start() if i+1<len(heads) else len(J))
 assert set(sections)==set(selected)
 for s,(a,b) in sections.items():assert selected[s]['body'] in J[a:b]
 decoder=json.JSONDecoder();at=D.index('[',D.index('"decisions"'))+1;i=0;spans={}
 while True:
  while D[at] in ' \r\n\t,':at+=1
  if D[at]==']':break
  value,end=decoder.raw_decode(D,at)
  if value['section'] in selected:spans[value['section']]=(i,at,end)
  at=end;i+=1
 helper=runpy.run_path(str(OUT/'scan026_source_splice.py'));exact=helper['exact']
 def ref(kind,a,b,pointer=None):
  c=captures[kind];r=exact(c['path'],text[kind],a,b)
  r.update(original_root_path=c['original_root_path'],original_root_sha256_at_capture=c['sha256'])
  if pointer is not None:r['original_json_pointer']=pointer
  return r
 auth={}
 for s in selected:
  i,a,b=spans[s];x,y=sections[s];auth[s]=[ref('decisions',a,b,f'/decisions/{i}'),ref('journal',x,y)]
 return captures,selected,auth,helper
