"""Root-reviewed expansion of grouped inventory annotation rows.

The mapping below was checked against the already audited page fragments.
It preserves manual physical positions and indexes each separate annotation.
No transcription page is written by this script. Run once only.
"""
from pathlib import Path
import csv
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from save_page import macro_args

R=Path(__file__).resolve().parents[1]
p=R/'MPL_67_002-052_inventory.csv'
rows=list(csv.DictReader(p.open()))
assert not any('.part' in r['element'] for r in rows), 'Already expanded'

# In the order of the existing rows of each kind: one-based macro indices.
maps={
 (11,'deleted'):[[1,2],[3,4],[5,6],[7],[8],[9,10,11,12],[13],[14],[15,16,17,18],[19,20]],
 (11,'inserted'):[[1],[2],[3,4,5],[6]],
 (13,'deleted'):[[1],[2,3],[4],[5,6,7],[8],[9,10],[11]],
 (13,'inserted'):[[2],[3,4,5],[6,7],[8],[9,10],[11]],
 (19,'deleted'):[[1,2],[3,4],[5],[6],[7],[8]],
 (19,'inserted'):[[1],[2,3],[4],[5],[6],[7],[8],[9]],
 (27,'deleted'):[[1],[2],[3,4],[5],[6],[7]],
 (27,'inserted'):[[1],[2,3]],
 (29,'deleted'):[[1],[2,3],[4],[5],[6]],
 (31,'deleted'):[[1],[2],[3,4],[5,6]],
 (31,'inserted'):[[1,2]],
 (33,'deleted'):[[1],[2],[3],[4],[5],[6],[7],[8,9],[10],[11],[12],[13]],
 (34,'deleted'):[[1],[2],[3],[4],[5],[6],[7],[8,9,10]],
 (35,'deleted'):[[1],[2],[3,4],[5,6]],
 (37,'deleted'):[[1,2],[3],[4,5,6],[7,8,9],[10,11],[12]],
 (38,'deleted'):[[1,2],[3,4]],
 (38,'inserted'):[[1,2],[3],[4],[5],[6]],
 (39,'deleted'):[[1],[2],[3,4,5],[6],[7,8,9,10]],
 (41,'deleted'):[[1,2,3],[4,5]],
 (43,'deleted'):[[1,2]],
 (50,'deleted'):[[1,2]],
 (51,'deleted'):[[1],[2,3],[4]],
}
kind={'deleted':'deletion','inserted':'insertion'}
replacement={}
for (n,m), groups in maps.items():
 args=macro_args((R/'pages'/f'MPL_67_002-052_67_scan{n:03d}.tex').read_text(),m)
 old=[r for r in rows if int(r['scan'])==n and r['kind']==kind[m]]
 assert len(old)==len(groups),(n,m,len(old),len(groups))
 for row,indices in zip(old,groups):
  expanded=[]
  for j,i in enumerate(indices,1):
   line,arg=args[i-1];rr=dict(row)
   if len(indices)>1:rr['element']+=f'.part{j}'
   rr['position']+=f'; TeX line {line}, {m} occurrence {i}'
   rr['first_words_or_objects']=arg.replace('\n',' ')[:220]
   expanded.append(rr)
  replacement[row['element']]=expanded

add_after={}
for n,macro_index,anchor,pos in [(11,7,'011.23','bottom chain, inserted and cancelled label'),(13,1,'013.05','item 2, inserted and cancelled words')]:
 line,arg=macro_args((R/'pages'/f'MPL_67_002-052_67_scan{n:03d}.tex').read_text(),'inserted')[macro_index-1]
 base=next(r for r in rows if r['element']==anchor)
 rr=dict(base,element=f'{n:03d}.audit_insert{macro_index}',kind='insertion',position=f'{pos}; TeX line {line}',first_words_or_objects=arg.replace('\n',' ')[:220])
 add_after.setdefault(anchor,[]).append(rr)

base=next(r for r in rows if r['element']=='008.01')
add_after['008.01']=[dict(base,element='008.table',kind='diagram',position='printed table as a whole, with individual text-row entries below',first_words_or_objects='Réf.; locality; area; land and building descriptions; prices')]

out=[]
for row in rows:
 if row['element']=='045.02':
  row=dict(row,kind='display',position='under X in the inclusion',first_words_or_objects='ouvert 0-connexe')
 out.extend(replacement.get(row['element'],[row]))
 out.extend(add_after.get(row['element'],[]))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
 w.writeheader();w.writerows(out)
print(f'Expanded {len(rows)} rows to {len(out)}; no page files changed.')
