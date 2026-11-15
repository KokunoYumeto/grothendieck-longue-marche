#!/usr/bin/env python3
"""Record reproducible text-only context searches for each root research item."""
from pathlib import Path
import collections
import datetime as dt
import hashlib
import json
import re
import subprocess

root=Path(__file__).resolve().parents[1]
context=root.parent/'context'
draft=(root/'records/research_root_draft.md').read_text()
groups={
 'localization': r'localiz|localis|abelianiz|abélian|quasi-inv',
 'interval': r'interval|contractor|absorban|multiplicati',
 'resolution': r'projectiv|projectif|résolution|resolution|bicomplex',
 'coefficient': r'coefficient|injectiv|injectif|coflat|coplat',
 'totality': r'totalement|total aspher|totale asph|filtrant',
 'adjunction': r'adjoint|counit|unit.*map|finite type|type fini',
 'duality': r'dualit|duality|opposite|Pontryagin|IMPL.*I1',
 'binomial': r'binomial|Symbin|P\(a\+|P\(t\)',
 'material': r'Modelizing|SGA.?7|Intersections|xérograph|scratchwork|Kimchi|manuscrites',
 'diagonal': r'diagonal|coalgebra|additive envelope|additif|additive',
 'asphericity': r'asph|category of elements|catégorie des éléments|Theorem.?A|théorème.?A',
 'status': r'GALOIS|RESIDUE|TOTASPH|PRETOT|TOTEX|BISITE|PATHS|CATHOT',
}
assignments={
 'localization':[1,6,7,10,11,14,17,21,22,26,30,56,60,61,62,63,64],
 'interval':[2,3,4,8,18,23,29,30,31,32,33,34,35,38,41,42,43,70,71,72,73,74,81],
 'resolution':[4,5,7,8,9,11,13,16,18,19,20,22,23,24,25,26,27,28,29,32,34,36,38,44,45,49,51,52,53,54,58,60,64,78],
 'coefficient':[6,7,12,15,16,27,28,36,39,44,45,46,48,49,50,51,52,53,54,55,60,68,69,80],
 'totality':[4,8,13,23,32,33,34,48,55,60,79],
 'adjunction':[6,10,11,14,16,17,21,22,24,27,28,35,41,56,57,58,60,62,63,64,65,66,68,69,77,78],
 'duality':[44,45,46,49,50,51,52,53,54,57,65,66,68,69,77,80],
 'binomial':[59,82],
 'material':[40,47,67,75,76],
 'diagonal':[3,20,36,37,38,39,41,42,43,55,58],
 'asphericity':[6,8,10,12,15,18,23,30,32,33,34,42,43,48,50,54,55,56,60,61,62,64,70,71,74,79],
}
results={}
for key,query in groups.items():
 p=subprocess.run(['rg','-n','-i','--glob','*.md','--glob','*.tex',query,str(context)],text=True,capture_output=True)
 assert p.returncode in (0,1),(key,p.stderr)
 lines=p.stdout.splitlines()
 counts=collections.Counter()
 samples=[]
 for line in lines:
  path,number,body=line.split(':',2)
  rel=str(Path(path).relative_to(context))
  counts[rel]+=1
  if counts[rel]<=3:
   samples.append({'file':rel,'line':int(number),'excerpt':body[:350]})
 results[key]={'query':query,'total_hits':len(lines),'hits_by_file':dict(counts),'samples_first_three_per_file':samples,'stderr':p.stderr}
items=[]
for m in re.finditer(r'^### R(\d{3}) — (.+)$',draft,re.M):
 n=int(m.group(1))
 assigned=[k for k,ns in assignments.items() if n in ns]
 assert assigned,n
 items.append({'id':f'R{n:03d}','heading':m.group(2),'search_groups':assigned,'scope':'supplied context .md/.tex text files, no images','context_locations_and_status_links':'See this item in research_root_draft.md and the integrated notes.'})
assert len(items)==82
record={'created_utc':dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'method':'rg text search; grouped queries reused where several notes examine the same written functor, morphism, or hypothesis. Search counts are lexical evidence, not proof of mathematical equivalence. Each note separately identifies the inspected comparison passage.','root_draft_sha256_at_search':hashlib.sha256(draft.encode()).hexdigest(),'items':items,'queries':results}
(root/'records/research_context_search_ledger.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(f'{len(items)} root notes assigned to {len(results)} recorded context searches; no image files read.')
