"""Apply main-reader decisions after viewing all twelve differing blind crops."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json
B=Path(__file__).resolve().parents[2]
stem=B/'second/148_scan027'
def rows(s):
 with Path(str(stem)+s).open() as f:return {r['box']:r for r in csv.DictReader(f,delimiter='\t')}
comp=rows('_comparison.tsv');boxes=rows('_boxes.tsv')
rp=B/'reviews/148_scan027.json';p=json.loads(rp.read_text());assert not p.get('second_audit')
page=B/'pages/148_scan027.tex';t=page.read_text()
two=r'\unsure{2|\deleted{6}\inserted{2}}'
order=r"\unsure{\text{d'ordre}|\text{dont}}"
dash=r'4\ \deleted{\text{triangles}}\inserted{\text{carrés}}\;\text{--}'
assert t.count(r'2\text{ hexag.}')==1
t=t.replace(r'2\text{ hexag.}',two+r'\text{ hexag.}')
old_order=r"8\text{ sommets}\\\text{d'ordre }4"
assert old_order in t;t=t.replace(old_order,r'8\text{ sommets}\\'+order+'4')
old_dash=r'4\ \deleted{\text{triangles}}\inserted{\text{carrés}}'
assert t.count(old_dash)==1;t=t.replace(old_dash,dash)
ink={
'B027-01':'The 4,16,10 and the three count words agree. The two short parallel strokes clipped at the right are the shaft of the already-transcribed double implication, not an additional equals sign after arêtes.',
'B027-02':"The parenthesis closes after ramifiés. Below it d'ordre has a separate d, apostrophe, rounded o and joined r/d/r/e; no numeral or ellipsis follows. Array wrappers do not change the reading.",
'B027-03':'The leading digit of the middle count has a crossing diagonal and closed lower loop, matching the separately written 8 above and the other 8s on this page. The next digit has an open curved head and basal turn:82. The numerical expectation32 does not override this ink.',
'B027-04':'The principal outline has a curved head, descending diagonal and broad baseline of2. A separate lower closed loop and extra oblique stroke admit an overwritten6, but neither the full earlier outline nor the writing order is secure. Retain2 first and add only an explicit uncertain overtrace alternative.',
'B027-05':'The open upper6 with a closed lower bowl, the word sommets, and the parenthesized dont4ramifiés are visible. The second reading differs only in layout syntax.',
'B027-06':'Two crossing lobes form8; the following word has the accented arêtes outline. No reading change.',
'B027-07':'The strike crosses triangles, leaving4 live; carrés is inserted above. A separate short dark horizontal dash follows the cancelled word at the baseline, beyond its final s. Retain this visible terminal stroke without treating it as an arithmetic minus.',
'B027-08':"Eight and sommets are clear. The following qualification begins with d and a low rounded loop and ends in a short joined stroke before4. A heavy nearly vertical crossing obscures the middle ascenders. The longer d'ordre remains favored by the visible approach and joined ending, but dont cannot be excluded; no grammatical or degree argument is used to force it.",
'B027-09':'The count begins with an upright1 and an open-topped6 with closed lower bowl, followed by arêtes. The extra wrappers do not alter16.',
'B027-10':'The initial8 lies outside the horizontal strike through triangles; carrés is written immediately above. Both readings preserve the same replacement.',
'B027-11':"The initial short upright and separate crossed angled form support the existing doubtful1×4 reading. The strike masks their lower strokes; dont4 and4×4 remain alternatives. The proposed tous les is not established by these few compact strokes. The clear d'ordre is crossed; the final tall4 stands beyond the strike endpoint and remains live.",
'B027-12':'The same crop rotated180degrees shows J,u,s,crossed t,dotted i,n,e. Justine and its upside-down position are already transcribed and documented by the page comment; adding rotatebox is a representation difference only.'}
changed={
'B027-04':comp['B027-04']['first'].replace(r'2\text{ hexag.}',two+r'\text{ hexag.}'),
'B027-07':dash,
'B027-08':comp['B027-08']['first'].replace(r"\text{d'ordre }",order),
}
entries=[]
for box,c in comp.items():
 if c['different']=='no':continue
 e=dict(box=box,choice='revised' if box in changed else 'first',viewed_by_main=True,ink=ink[box],confidence='low' if box in ['B027-04','B027-08','B027-11'] else 'high')
 if box in changed:e['final']=changed[box]
 entries.append(e)
def evidence(box):return dict(crop=f'crops/second/148_scan027/{box}.png',box=[int(boxes[box][k]) for k in ['x0','y0','x1','y1']])
for r in p['changes']:
 if r['place']=='Lower left corrected face name':r.update(final=dash,ink=ink['B027-07'],against_c=True,**evidence('B027-07'))
 if r['place']=='Upper right edge count':r.update(ink=ink['B027-03'],**evidence('B027-03'))
for d in p['decisions']:
 if d['id']=='M0275':d.update(ink=ink['B027-03'],**evidence('B027-03'))
for u in p['unresolved']:
 if u['place']=='Initial numeral of separate left count':u.update(reading=two,issue=ink['B027-04'],alternatives=[r'\deleted{6}\inserted{2}'],**evidence('B027-04'))
p['unresolved'].append(dict(place='Lower right qualification before4',reading=order,alternatives=[r'\text{dont}'],confidence='low',issue=ink['B027-08'],**evidence('B027-08')))
for n in p['notes']:
 if n['id']=='N027-03':n['text']='The separate left count reads a favored2hexag.,9arêtes,6sommets. A lower loop admits an overwritten6 beneath2, now marked as an alternative; the prior digit and chronology are not established.'
 if n['id']=='N027-04':n['text']="The lower comparison writes6sommets,dont4ramifiés,8arêtes and4carrés, leading to8sommets with a doubtful d'ordre|dont qualification before4, then16arêtes and8carrés. Both occurrences of carrés replace struck triangles. A short dash follows the first cancelled face name."
p['notes'].append(dict(id='N027-BLIND',text='All12 differing blind boxes were inspected by the main reader. The written82 is retained independently of the arithmetic expectation32. Two places are reopened as doubts, without counting certainty alone as new C/H correction rows. The terminal short dash is restored.'))
page.write_text(t);rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
Path(str(stem)+'_adjudications.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (B/'reviews/visual_log.tsv').open('a') as f:
 for e in entries:f.write(f'{now}\t027\tcrops/second/148_scan027/{e["box"]}.png\tMain reader viewed differing blind box; {e["ink"]}\n')
print('027:12 adjudications, three revised boxes; first readings unchanged.')
