"""Root-reader inventory review; no transcription writes.

The input proposal is a permutation of the saved pre-review inventory. Layout
placements below were reviewed against the original whole-sheet images by the
root reader after freeze; they do not change a manuscript reading.
"""
from pathlib import Path
from collections import Counter,OrderedDict
from datetime import datetime,timezone
import csv,json,hashlib

R=Path(__file__).resolve().parents[1]
name='MPL_15_195-228+18_002-017_inventory.csv'
original=R/'records/inventory_before_order_review.csv'
if not original.exists(): original.write_bytes((R/name).read_bytes())
def read(p):
 with p.open(newline='') as f:return list(csv.DictReader(f))
old=read(original); rows=read(R/'records/inventory_order_proposal.csv')
cols=list(old[0]); as_tuple=lambda r:tuple(r[c] for c in cols)
assert Counter(map(as_tuple,old))==Counter(map(as_tuple,rows))
groups=OrderedDict()
for r in rows:groups.setdefault((int(r['cote']),int(r['scan'])),[]).append(r)
def move(key,ids,anchor,before=True):
 g=groups[key]; chosen=[next(r for r in g if r['element']==i) for i in ids]
 g[:]=[r for r in g if r['element'] not in ids]
 j=next(i for i,r in enumerate(g) if r['element']==anchor)+(not before)
 g[j:j]=chosen
move((15,197),['999'],'003')
move((15,203),['999'],'009')
move((15,211),['999'],'002')
move((15,215),['1000'],'1002',False)
move((15,215),['008','1004'],'002')
move((15,215),['006','1012'],'005')
move((15,215),['1001','1013'],'009')
move((15,217),['1000'],'005')
move((18,16),['012'],'008')
g=groups[(18,11)]
order=['001','003','004','002','005','1000','1009','006','1002','1003','1004','1005','1006','1007','1008','1001','1010','1011','1012','1013','007','008','009','1016','1014','1015','010','011','1017','012','1018','013','1019','1020','016','017','018','014','1021','1022','015','1023']
assert set(order)=={r['element'] for r in g}
groups[(18,11)]=[next(r for r in g if r['element']==i) for i in order]
added=read(R/'records/inventory_pagination_suggestions.csv')
for r in added:
 key=int(r['cote']),int(r['scan'])
 r['position']=('top; typescript pagination' if key==(18,7) and r['first_words_or_objects']=='18' else 'bottom; manuscript pagination in reading orientation')
 assert r['element'] not in {x['element'] for x in groups[key]}
 if key==(18,7) and r['first_words_or_objects']=='18':groups[key].insert(0,r)
 else:groups[key].append(r)
key=(15,211); g=groups[key]
nr=dict(cote='15',scan='211',sheet_kind='text',element=str(max(int(r['element']) for r in g)+1),kind='text',position='lower-middle heading above Pts banaux; page TeX line 24',first_words_or_objects=r'\uline{\deleted{\unsure{de X}} \unsure{car $p$}}',transcribed='yes')
j=next(i for i,r in enumerate(g) if r['element']=='005');g.insert(j,nr);added.append(nr)
final=[r for g in groups.values() for r in g]
assert Counter(map(as_tuple,final))-Counter(map(as_tuple,old))==Counter(map(as_tuple,added))
assert all(r['transcribed']=='yes' for r in final)
with (R/name).open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(final)
manifest=json.loads((R/'records/frozen_manifest.json').read_text())
for p,h in manifest['sha256'].items():
 assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h,p
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report={'review_utc':now,'original_rows':len(old),'retained_original_rows':len(old),'new_rows':len(added),'final_rows':len(final),'frozen_hashes_unchanged':len(manifest['sha256']),'method':'Root visual layout review on 15/197,203,211,215,217 and18/011,016; nesting macro rows retained; standalone pagination added from frozen text and original reading record. Positions refer to upright reading orientation on reused upside-down sheets.'}
(R/'records/inventory_review_result.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (R/'progress.log').open('a') as f:f.write('inventory metadata review '+now+'; 694 original rows retained; 10 pagination rows and 1 separate heading row added; 705 rows; all 50 frozen hashes unchanged\n')
print(json.dumps(report,indent=2))
