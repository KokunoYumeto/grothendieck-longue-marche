#!/usr/bin/env python3
"""Record reproducible, per-item searches of supplied context, not OCR."""
from pathlib import Path
import datetime,json,re
root=Path(__file__).resolve().parents[1]
src=root.parent/'source'
files=[src/'SP32_CW_156-3_context/notes/RESULTS_STATE.md',src/'SP32_CW_156-3_context/Esquisse_cote119_copy1_API_transcription.tex']
files += [src/f'SP32_CW_156-3_sweep3/readings/{c}.md' for c in ['156-3','156-5','156-7']]
terms={
'ORD':['bord|fronti|boundary','tronçon|closure|closed|adh','intersect|fronti','compat|ordre|order','interst|suprem|borne','compos|convex|inject','compos|connex|topolog','compl|interst|card','ordre|order|compat|meet','tronçon|product|produit','Boole|clopen|spectre','compos|connex|closed','Boole|subdiv|spectre','subdiv|découp|chaîne','inciden|clôture|closure|drapeau'],
'ALG':['Boole|compat|axiom','adh|closure|fronti','rare|fini|interior','fronti|compat','Boole|anneau','relativ|unit|major','relativ|compl|Boole','relativ|adh|stabili','clopen|Boole|compat','closure|adh|génér','invol|compl','De Morgan|union|réunion','fronti|relativ','famille|fini|join'],
'REC':['réseau|cut|découp','caractéris|Hilbert|axiom','between|entre|cut','divisib|dense|cut','between|entre|biord','biord|partition|between','Hua|betweenness|Hilbert','pro-object|découp|S14','Stone|limit|poset','pro-object|S14|finite poset','drapeau|Drap|flag','isotop|Hauptvermutung|homotop','link|recollement|rétraction','atelier|réseau|forme'],
'ROOT':['rare|fini','rare|interval|dense','Stone|spectre|Boole','spectre|compos|Boole','interst|sépar|separator','axiom|tronçon|relativ'],
'CTX':['constructib|modéré','support|Boole|compat','drapeau|recollement|link','isotop|Hauptvermutung|triangul','compos|exit|topolog','relativ|recollement|open.closed']}
records=[]
for prefix,patterns in terms.items():
 for i,pattern in enumerate(patterns,1):
  entry={'item':f'{prefix}-{i:02}','query':pattern,'files':[]}
  for f in files:
   matches=[];tag=None;section=None
   for n,line in enumerate(f.read_text().splitlines(),1):
    m=re.search(r'\\scanpage\{([^}]+)\}',line)
    if m:tag=m.group(1)
    if line.startswith('#'):section=line.strip()
    if re.search(pattern,line,re.I):
     matches.append({'line':n,'scan_tag':tag,'section':section,'excerpt':line[:300]})
   entry['files'].append({'path':str(f.relative_to(src)),'hit_count':len(matches),'first_hits':matches[:5]})
  records.append(entry)
out={'time_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'method':'Text search on supplied contextual text only. Matches are leads, not evidence for an ink reading or automatic mathematical support. Final notes identify the relevant passage and relation.','items':records}
(root/'records/context_searches.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'{len(records)} per-item searches recorded; no frozen file written')
