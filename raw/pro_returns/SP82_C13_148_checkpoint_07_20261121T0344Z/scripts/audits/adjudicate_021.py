"""Main-reader geometric decisions after viewing all four blind audit crops."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re
B=Path(__file__).resolve().parents[2]
with (B/'second/148_scan021_comparison.tsv').open() as f:
    comp={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
rp=B/'reviews/148_scan021.json';p=json.loads(rp.read_text())
page=B/'pages/148_scan021.tex';t=page.read_text()

def inner(s):
    return s.split('\n',1)[1].rsplit(r'\end{tikzpicture}',1)[0].strip()
def scope(body,x,y):return '\\begin{scope}[shift={('+str(x)+','+str(y)+')}]\n'+body+'\n\\end{scope}'
def figure(body):return '\\figure{\\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]\n'+body+'\n\\end{tikzpicture}}'

one=inner(comp['S21-D1']['second'])
one=one.replace('[line width=.35pt]','[gray!65,line width=.35pt]').replace('[line width=.4pt]','[gray!65,line width=.4pt]').replace('[line width=.45pt]','[gray!75,line width=.45pt]')
two=inner(comp['S21-D2']['second'])
three=inner(comp['S21-D3']['second'])
cut=three.index(r'\draw[line width=.55pt] (68,151)')
three=three[:cut].replace('[line width=','[gray!80,line width=')+three[cut:]
# The global page already draws the long ray beyond this crop. Do not duplicate it.
three_local='\n'.join(line for line in three.splitlines() if not ('(151,53)' in line or '(173,29)' in line))
old=r'\draw[gray!65,line width=.35pt] (392,493)..controls(403,480)and(405,468)..(427,461);'
assert old in t;t=t.replace(old,scope(one,376,449),1)
start=t.index('% The larger sketch:');end=t.index('% The smaller sketch',start)
t=t[:start]+'% The larger sketch, with visible partial retracings and six separated transverse strokes.\n'+scope(two,645,415)+'\n\n'+t[end:]
start=t.index('% The smaller sketch');end=t.index(r'\end{tikzpicture}}',start)
t=t[:start]+'% Smaller sketch: literal tapered dark patches, without assigned arrow directions.\n'+scope(three_local,900,330)+'\n'+t[end:]
page.write_text(t)

texts={
'S21-N20':'Both versions read20. The page already uses a margin wrapper; no numeral, punctuation or attribution changes.',
'S21-D1':'The oblique mark contains separated segments and unequal darkness, including a thicker middle patch. The first smooth curve flattened these visible gaps and weights. Adopt the segmented trace, without inferring an arrowhead or label.',
'S21-D2':'The same four vertices and six edges occur in both readings. The crop additionally shows short partial retracings along the doubled left edge, unequal transverse dashes, and distinct small endpoint gaps. The revised paths follow these visible details; no edge or arrow direction is inferred.',
'S21-D3':'The right outline has a visible gap, the center contains superposed dark strokes, and several ends broaden into tapered black patches. Reproduce those patches literally rather than calling them arrows. The pale oblique continuation belongs to the long ray already drawn elsewhere on the page, so its overlapping segment is not duplicated. Stroke order and intentional direction remain unresolved.'}
finals={'S21-D1':figure(one),'S21-D2':figure(two),'S21-D3':figure(three)}
entries=[]
for key in comp:
    d=dict(box=key,choice='revised' if key in finals else 'first',viewed_by_main=True,
           ink=texts[key],confidence='medium' if key in ('S21-D1','S21-D3') else 'high')
    if key in finals:d['final']=finals[key]
    entries.append(d)
(B/'second/148_scan021_adjudications.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
for r in p['changes']:
    for key in finals:
        if r['place'].startswith('P21-'+key.split('-')[-1]+';'):
            b=next(x for x in p['second_boxes'] if x['box']==key)
            r.update(final=finals[key],ink=texts[key],crop=f'crops/second/148_scan021/{key}.png',
                     box=[b[k] for k in ('x0','y0','x1','y1')])
for r in p['unresolved']:
    if r['id']=='U21-D1':
        r['reading']='segmented isolated stroke with a thicker middle patch'
        r['issue']='The gaps and weights are copied literally. No arrowhead, label or graphic function is securely established.'
    if r['id']=='U21-D3':
        r['reading']='superposed diagonal strokes and literal tapered black patches'
        r['issue']='The dark patches are reproduced without assigning arrow directions. Their stroke order and exact joins remain uncertain.'
p.setdefault('notes',[]).append(dict(id='148-021-BLIND',text='The independent audit prompted finer traces of the isolated mark, the partial retracings and gaps in the larger sketch, and the tapered dark patches in the smaller sketch. These are geometric refinements, not a new mathematical interpretation. The smaller crop also contains the beginning of a long ray already drawn on the full page; that overlap is not duplicated. The margin numeral remains20.'))
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (B/'reviews/visual_log.tsv').open('a') as f:
    for e in entries:f.write(f'{now}\t021\tcrops/second/148_scan021/{e["box"]}.png\tMain reader viewed differing blind box; {e["ink"]}\n')
print('021 geometric refinements and four crop decisions recorded; first readings unchanged.')
