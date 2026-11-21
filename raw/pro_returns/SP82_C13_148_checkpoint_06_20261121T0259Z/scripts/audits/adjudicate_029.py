"""Record main-reader inspection of both sparse-page blind crops."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
B=Path(__file__).resolve().parents[2];stem=B/'second/148_scan029'
with Path(str(stem)+'_comparison.tsv').open() as f:c={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
with Path(str(stem)+'_boxes.tsv').open() as f:boxes={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
rp=B/'reviews/148_scan029.json';p=json.loads(rp.read_text());assert not p.get('second_audit')
page=B/'pages/148_scan029.tex';t=page.read_text();assert 'M_{0,5}' in t
t=t.replace('M_{0,5}',r'M_{\unsure{0|8},5}')
ink='The first small index has a tall closed lower oval and a compact upper return, which can be a retraced closure of0 or the upper loop of8. Retain0 first, but mark8 as an alternative. The comma and curved final5 are clear. The separate dark horizontal stroke above the right part of5 remains visible; the second reading omits it, but the crop does not prove whether it is the detached top bar of5 or a raised following dash. Preserve the existing uncertainty.'
e=[dict(box='B029-01',choice='revised',viewed_by_main=True,final=c['B029-01']['first'].replace('M_{0,5}',r'M_{\unsure{0|8},5}'),ink=ink,confidence='low'),dict(box='B029-02',choice='first',viewed_by_main=True,ink='The first digit has the curved head, long descending stroke and rightward foot of2; the second has a crossing waist and two lobes of8. Both readings give28. The mspage wrapper would add no new source reading.',confidence='high')]
p['unresolved'].append(dict(place='First index in upper-right heading',reading=r'\unsure{0|8}',alternatives=['8'],confidence='low',issue=ink,crop='crops/second/148_scan029/B029-01.jxl',box=[int(boxes['B029-01'][k]) for k in ['x0','y0','x1','y1']]))
for n in p['notes']:
 if n['id']=='N029-02':n['text']='The front heading reads M with a doubtful0|8 as its first index and5 as the second. The horizontal stroke above the right side of5 remains unresolved between a detached digit-top stroke and a following raised dash. No expected moduli-space notation is used to settle either uncertainty.'
for d in p['decisions']:
 if d['id']=='M0278':d['ink']=ink
for r in p['notation']:r['form']=r['form'].replace('M_{0,5}',r'M_{\unsure{0|8},5}')
for i in p['inventory']:
 for key in ['first_words_or_objects']:
  if isinstance(i.get(key),str):i[key]=i[key].replace('M_{0,5}',r'M_{\unsure{0|8},5}')
p['notes'].append(dict(id='N029-BLIND',text='The main reader inspected both differing boxes. The only revision is added uncertainty in the first subscript; no new C/H correction row is counted for certainty alone. No H transcription exists for this page.'))
page.write_text(t);rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n');Path(str(stem)+'_adjudications.json').write_text(json.dumps(e,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (B/'reviews/visual_log.tsv').open('a') as f:
 for d in e:f.write(f'{now}\t029\tcrops/second/148_scan029/{d["box"]}.png\tMain reader viewed differing blind box; {d["ink"]}\n')
print('029:both adjudications recorded; one uncertainty added.')
