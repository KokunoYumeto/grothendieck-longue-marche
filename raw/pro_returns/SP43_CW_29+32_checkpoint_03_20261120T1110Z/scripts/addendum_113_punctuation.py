"""Record punctuation collation gaps discovered after 114, without altering 113 text."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parents[1];s='C29-05_29_scan113'
p=O/'decisions'/f'{s}.json';d=json.loads(p.read_text());ip=O/'adjudication_inputs'/f'{s}.json';i=json.loads(ip.read_text())
assert not any(x['id']=='D29' for x in d['differences']),'Addendum already recorded'
page=O/'pages'/f'{s}.tex';before=hashlib.sha256(page.read_bytes()).hexdigest()
rows=[('D29','Theorem 1 heading, colon','1:','1 :','m12_theorem1_colon',[640,265,770,320]),('D30','Inserted local heading, colon','2:','2 :','m06_raised_intro',[243,592,1644,644]),('D31','Corollary 3 heading, colon','3:','3 :','m13_corollary3_colon',[455,1060,570,1117]),('D32','Corollary 4 heading, closing parenthesis and colon','(de 1):','(de 1) :','m14_corollary4_colon',[520,2028,760,2085]),('D33','Transition to corollary 4, terminal colon','connexité:','connexité :','m15_connexite_colon',[240,1960,510,2010])]
added=[]
for ident,place,fin,h,f,box in rows:
 added.append(dict(id=ident,place=place,C=fin,H=h,reading=fin,diff_C=False,diff_H=True,kind='other',marked_in_H='no',evidence='The colon occupies the next typewriter cell after the preceding numeral/letter/parenthesis; there is no intervening blank cell. All three complete reader texts retained this adjacency, but their initial difference lists omitted the H spacing change.',source=f'crops/{s}/{f}.png',bbox=box,confidence='high',mathematical=False,readers={r:fin for r in ('r1','r2','r3')}))
d['differences'].extend(added);i['add_differences'].extend(added)
for x in d['differences']:
 if x['id']=='D12':
  x.update(C='déduit/formellement;',H='déduit formellement ;',reading=r'déduit\handwritten{/}formellement;',evidence=x['evidence']+' The same already inspected crop also shows the semicolon in the next cell after formellement, with no intervening blank. The H gap is included in this contiguous transition cluster.',readers={r:r'déduit\handwritten{/}formellement;' for r in ('r1','r2','r3')})
  i['overrides']['D12'].update({k:x[k] for k in ('C','H','reading','evidence','readers')})
new=[f'crops/{s}/{f}.png' for f in ('m12_theorem1_colon','m13_corollary3_colon','m14_corollary4_colon','m15_connexite_colon')]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
note=' Post-decision collation addendum '+now+': after the punctuation-gap comparison on 114, five omitted H-only colon-gap rows were added to 113 and the existing transition row expanded to include its semicolon gap. Four new narrow crops were inspected once; the local-heading and transition decisions used the two crops already inspected, without reopening them. The complete three-reader texts and consolidated page already had the final punctuation. The page text is unchanged. Main totals are now 28 effective inspections, thirteen existing reader crops and fifteen new main crops. This records the late coverage correction rather than treating it as part of the original done event.'
for obj in (d,i):
 obj['main_crops'].extend(new);obj['main_views'].extend(new);obj['adjudication']+=note
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');ip.write_text(json.dumps(i,ensure_ascii=False,indent=2)+'\n')
assert hashlib.sha256(page.read_bytes()).hexdigest()==before
with (O/'progress.log').open('a') as f:f.write(f'collation addendum 29/113 {now}; five H punctuation-gap rows plus existing-row expansion; four new crops; page text unchanged SHA256 {before}\n')
with (O/'adjudication_inputs'/f'{s}_observations.md').open('a') as f:f.write('\n## Punctuation collation addendum\n\n'+note+'\n\n'+'\n'.join('- '+x for x in new)+'\n')
print('Recorded addendum; page SHA256 unchanged',before)
