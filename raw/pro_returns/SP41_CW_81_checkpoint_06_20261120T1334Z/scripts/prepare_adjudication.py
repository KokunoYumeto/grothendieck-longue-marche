"""Align candidate loci for main-reader review. Alignment is mechanical, never an ink decision."""
from pathlib import Path
import json,csv,re,sys,difflib
w=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);base=w/f'readers/scan{n:03d}'
r=[json.loads((base/f'R{k}/return.json').read_text()) for k in (1,2,3)]
indices=[x for x in csv.DictReader((w/'validation/C_doubt_index.tsv').open(),delimiter='\t') if int(x['scan'])==n]
for reader in r:
 for f in reader['findings']:
  ids=f.get('c_doubt_ids',[])
  if isinstance(ids,str):ids=[ids]
  ids += [x['source_doubt_id'] for x in indices if '\\'+x['macro']+'{'+x['content']+'}' in f.get('c','')]
  f['c_doubt_ids']=sorted(set(ids))
def overlap(a,b):
 if not a or not b:return 0
 aa=max(1,(a[2]-a[0])*(a[3]-a[1]));bb=max(1,(b[2]-b[0])*(b[3]-b[1]))
 inter=max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))
 return inter/min(aa,bb)
def score(a,b):
 ids=set(a.get('c_doubt_ids',[]))&set(b.get('c_doubt_ids',[]))
 c=difflib.SequenceMatcher(None,a.get('c',''),b.get('c','')).ratio()
 h=difflib.SequenceMatcher(None,a.get('h',''),b.get('h','')).ratio()
 ov=overlap(a.get('bbox'),b.get('bbox'))
 return (10 if ids else 0)+4*ov+2*c+h
out={'scan':n,'readers':r,'candidate_loci':[],'warning':'Machine alignment only. Main reader must inspect/correct candidates and decide all readings from crops.'}
for f in r[0]['findings']:
 row={'base_id':f['id'],'place':f['place'],'c_doubt_ids':f['c_doubt_ids'],'R1':{'id':f['id'],'reading':f['reading']},'c':f['c'],'h':f['h']}
 for k in (1,2):
  ranked=sorted(r[k]['findings'],key=lambda g:score(f,g),reverse=True)
  row[f'R{k+1}_candidates']=[{'id':g['id'],'reading':g['reading'],'score':round(score(f,g),2),'place':g['place']} for g in ranked[:2]]
 out['candidate_loci'].append(row)
draft=w/'decisions/drafts';draft.mkdir(exist_ok=True)
(draft/f'scan{n:03d}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('R1 FULL TEXT\n'+(base/'R1/reading.tex').read_text())
for k in (2,3):
 print('\n'.join(difflib.unified_diff((base/'R1/reading.tex').read_text().splitlines(),(base/f'R{k}/reading.tex').read_text().splitlines(),fromfile='R1',tofile=f'R{k}',n=0)))
print('LOCUS CANDIDATES')
for x in out['candidate_loci']:
 row={'id':x['base_id'],'place':x['place'],'C':x['c'],'H':x['h'],'R1':x['R1']['reading']}
 for k in (2,3):row[f'R{k}']=x[f'R{k}_candidates'][0]
 print(json.dumps(row,ensure_ascii=False))
print('READER COUNTS',[(i+1,len(x['findings']),x.get('crop_count'),len(x.get('unresolved',[]))) for i,x in enumerate(r)])
