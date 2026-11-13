from pathlib import Path
import csv,re,json
ROOT=Path(__file__).resolve().parents[2]
records=json.loads((ROOT/'work/data/layout_pass_sites.json').read_text())
out=[]
for r in records:
 p=ROOT/'sources/draft_readers'/(r['reader']+'.tex');t=p.read_text();lines=t.splitlines(True);n=int(r['input line of the reader source']);offset=sum(map(len,lines[:n]));upto=t[:offset]
 for typ in ('tikzcd','tikzpicture'):
  ms=list(re.finditer(r'\\begin\{'+typ+r'\}.*?\\end\{'+typ+r'\}',upto,re.S))
  if not ms:continue
  m=ms[-1];tail=t[m.end():offset]
  # A displayed math diagram may be enclosed in several macro braces.
  if re.sub(r'\\\]|[\s}]','',tail):continue
  scanstart=list(re.finditer(r'\\scanpage\{\d+[^}]*\}',t[:m.start()]))[-1].start()
  ordinal=len(list(re.finditer(r'\\begin\{'+typ+r'\}',t[scanstart:m.start()])))+1
  d={k:r[k] for k in ('package','cote','scan')};d.update(environment=typ,ordinal=ordinal,prior_kind=r['what the pass did'],prior_scale=r['scale'])
  key=(d['package'],d['scan'],typ,ordinal)
  if not any((x['package'],x['scan'],x['environment'],x['ordinal'])==key for x in out):out.append(d)
# Equation (122) has a comma and \quad after the diagram, so its display
# warning cannot be detected by the immediately-closing-environment rule.
out.append({'package':'LM_C4-267-280','cote':'140-4','scan':271,'environment':'tikzcd','ordinal':1,'prior_kind':'scaled_display','prior_scale':'0.786'})
out.append({'package':'LM_C4-058-076','cote':'140-4','scan':66,'environment':'tikzcd','ordinal':1,'prior_kind':'scaled_display','prior_scale':'0.897'})
for d in out:
 if d['package']=='LM_C1-001-019' and d['scan']==10:d.update(font_size=8.5,column_sep=6,row_sep=12)
 if d['package']=='LM_C1-001-019' and d['scan']==10 and d['ordinal']==1:d.update(font_size=8.2,column_sep=5)
 if d['package']=='LM_P031' and d['scan']==302:d['landscape']=True
 if d['package']=='LM_P035' and d['scan']==344:d.update(landscape=True,font_size=9,row_sep=9)
 if d['package']=='LM_C3-549-567' and d['scan']==561:d['landscape']=True
(ROOT/'work/data/layout_diagram_targets.json').write_text(json.dumps(out,indent=2))
for d in out:print(d)
