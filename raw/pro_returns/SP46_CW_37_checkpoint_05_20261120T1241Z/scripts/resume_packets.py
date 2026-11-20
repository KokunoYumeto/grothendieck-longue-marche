"""Recreate per-page input packets after restoration; never overwrite deliverables.

Place the checkpoint contents in ROOT/out and unpack the original user ZIP once
under ROOT/source. Run this script from out/scripts. The historical init_work.py
is the original initialization record and MUST NOT be rerun on restored work.
"""
from pathlib import Path
import json,csv,re,shutil
O=Path(__file__).resolve().parents[1];R=O.parent;W=R/'source/SP46_CW_37_witnesses'
rows=json.loads((O/'page_order.json').read_text())
for row in rows:
 n=int(row['our_scan']);folder=row['folder'];p=R/'packets'/f'scan{n:03}';p.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(W/row['codex_file'],p/'C.tex')
 s=(W/row['hua_file']).read_text();matches=list(re.finditer(r'\\page\{(\d+)\}',s))
 j=next(i for i,m in enumerate(matches) if int(m[1])==int(row['their_page']))
 h=s[matches[j].start():matches[j+1].start() if j+1<len(matches) else len(s)]
 corrections=json.loads((O/'packet_corrections.json').read_text()) if (O/'packet_corrections.json').exists() else {}
 if str(n) in corrections:
  for marker in corrections[str(n)].get('trim_before',[]):
   if marker in h:h=h[:h.index(marker)]
 (p/'H.tex').write_text(h.rstrip()+'\n')
 context=[]
 for kind in ['doubts','notes']:
  t=(W/f'codex/{folder}/{folder}_{kind}.md').read_text()
  context.append(f'# Witness C {kind}: rows for scan {n}\n')
  context.extend(line for line in t.splitlines() if re.match(r'\|\s*'+str(n)+r'\s*\|',line))
 (p/'C_context.md').write_text('\n'.join(context)+'\n')
 meta=dict(row);meta['images']=[str(R/'source/SP46_CW_37_scans'/f'{folder}_37_scan{n:03}{suffix}.jpg') for suffix in ['', '_a','_b']]
 (p/'meta.json').write_text(json.dumps(meta,indent=2)+'\n')
 # A new page receives only notation established before it.
 notation=[]
 for dec in sorted((O/'decisions').glob('scan*.json')):
  d=json.loads(dec.read_text())
  if d['scan']<n:notation.extend(dict(scan=d['scan'],**v) for v in d.get('notation',[]))
 (p/'notation.json').write_text(json.dumps(notation,ensure_ascii=False,indent=2)+'\n')
print('Recreated input packets only. Deliverables and historical reader returns were not modified.')
