#!/usr/bin/env python3
"""Apply root's completed scan028 adjudications mechanically; run once.

The main reader personally viewed all 17 differing fixed crops. This script
implements only those supplied decisions, without reinterpreting the images,
compiling TeX, changing locked readings, or editing shared audit logs.
"""
from pathlib import Path
import csv
import json
import re

B=Path(__file__).resolve().parents[2]
stem=B/'second/148_scan028'
with Path(str(stem)+'_comparison.tsv').open() as f:
    comp={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
with Path(str(stem)+'_boxes.tsv').open() as f:
    boxes={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
rp=B/'reviews/148_scan028.json'
p=json.loads(rp.read_text())
page=B/'pages/148_scan028.tex'
t=page.read_text()
ap=Path(str(stem)+'_adjudications.json')
assert not p.get('second_audit') and not ap.exists(), 'Non-idempotent: already applied.'

def key(name):
    return 'S28-'+name

def picture_body(s):
    return re.search(r'\\begin\{tikzpicture\}(?:\[[^\n]*?\])?\s*(.*?)\\end\{tikzpicture\}',s,re.S).group(1).strip()

def commands(name):
    s=picture_body(comp[key(name)]['second'])
    return [c.strip()+';' for c in s.split(';') if c.strip() and not c.strip().startswith(r'\clip')]

def index(cs,start):
    found=[i for i,c in enumerate(cs) if c.startswith(start)]
    assert len(found)==1,(start,len(found))
    return found[0]

def omit(cs,*starts):
    for start in starts:index(cs,start)
    return [c for c in cs if not any(c.startswith(start) for start in starts)]

def replace(cs,start,new):
    i=index(cs,start)
    cs[i:i+1]=new if isinstance(new,list) else [new]
    return cs

names=['top_polygon','top_cut_sphere','numbered_cap','upper_handle',
       'labelled_triangle','lower_left_torus','lower_middle_ring','lower_handle']
parts={name:commands(name) for name in names}
parts['top_polygon']=parts['top_polygon'][:index(parts['top_polygon'],r'\draw[line width=.65pt] (211,385)')]
parts['top_polygon']=replace(parts['top_polygon'],r'\draw[line width=.8pt,->] (84,262)',
    r'\draw[line width=.8pt] (84,262)--(93,275)--(105,256);')
parts['top_cut_sphere']=omit(parts['top_cut_sphere'],
    r'\draw[line width=.2pt] (147,234)',r'\draw[line width=.55pt] (222,311)')
parts['numbered_cap']=replace(parts['numbered_cap'],r'\fill (211,239)',[
    r'\fill (211,239) circle[radius=2.2pt];',r'\fill[white] (211,239) circle[radius=.65pt];'])
parts['upper_handle']=parts['upper_handle'][:index(parts['upper_handle'],r'\draw[line width=.7pt] (0,32)')]
parts['labelled_triangle']=parts['labelled_triangle'][:index(parts['labelled_triangle'],r'\draw[line width=.95pt] (0,268)')]
parts['labelled_triangle']=omit(parts['labelled_triangle'],r'\node at (48,9)')
parts['labelled_triangle']=replace(parts['labelled_triangle'],r'\node at (95,355)',r'\node at (95,355) {$b_a$};')
parts['lower_middle_ring']=parts['lower_middle_ring'][:index(parts['lower_middle_ring'],r'\node[rotate=25] at (370,38)')]
parts['lower_middle_ring'].append(r'\fill (241,321) circle[radius=1.5pt];')
all_handle=parts['lower_handle']
isolated_vertical=all_handle[index(all_handle,r'\draw[line width=.45pt] (54,44)')]
parallel_arc=all_handle[index(all_handle,r'\draw[line width=.65pt] (166,71)')]
parts['lower_handle']=all_handle[:index(all_handle,r'\draw[line width=1.1pt] (25,0)')]
parts['lower_handle']=omit(parts['lower_handle'],r'\draw[line width=.6pt,->] (127,146)',
    r'\draw[line width=.65pt,->] (61,231)',r'\draw[line width=.65pt] (64,209)')
parts['lower_handle']=replace(parts['lower_handle'],r'\draw[line width=.65pt,->] (223,132)',
    r'\draw[line width=.65pt] (223,132) .. controls (240,107) and (257,100) .. (276,98);')
parts['lower_handle']=replace(parts['lower_handle'],r'\draw[line width=.65pt,->] (191,398)',
    r'\draw[line width=.65pt] (191,398)--(211,398)--(212,415);')
parts['lower_handle']=replace(parts['lower_handle'],r'\draw[line width=.7pt,->] (483,326)',
    r'\draw[line width=.7pt] (483,326)--(504,339)--(512,316);')
parts['lower_handle']=replace(parts['lower_handle'],r'\draw[line width=.6pt,dash pattern=on 3pt off 5pt] (218,460)',
    r'\draw[line width=.6pt] (217,460)--(230,461) (236,460)--(239,461) (245,463)--(247,465) (233,468)--(236,471) (246,469)--(247,473);')
parts['lower_handle'] += [
    r'\draw[line width=.6pt] (285,84)--(291,87)--(286,95);',
    r'\fill (190,422) circle[radius=1.8pt];',
    isolated_vertical,parallel_arc,r'\draw[line width=.55pt] (329,28)--(333,38);']

# Every adopted second trace uses native crop coordinates, x=.014cm. The whole
# sheet uses x=.007cm: coordinate points need only translation, while absolute
# stroke widths, point radii and dash intervals in pt need a factor of 0.5.
# The inherited default is scaled as well so unqualified strokes keep their
# relative weight. First-retained drawings and their styles are untouched.
def half_pt(m):
    return f'{float(m.group(1))*.5:.6f}'.rstrip('0').rstrip('.')+'pt'

def scale_pt(s):
    return re.sub(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt',half_pt,s)

scopes={}
transforms={}
for name in names:
    k=key(name)
    rect=[int(boxes[k][s]) for s in ('x0','y0','x1','y1')]
    x0,y0,x1,y1=rect
    assert '[x=.014cm' in comp[k]['second']
    scopes[name]='\n'.join([rf'\begin{{scope}}[shift={{({x0},{y0})}},line width=.5\pgflinewidth]']+
                            [scale_pt(c) for c in parts[name]]+[r'\end{scope}'])
    transforms[k]=dict(basis='native crop pixels',native_box=rect,coordinate_scale=1,
        source_base_x_cm=.014,target_base_x_cm=.007,physical_size_ratio=.5)

picture_begin=r'\begin{tikzpicture}[x=.007cm,y=-.007cm,line cap=round,line join=round]'
def figure(body):
    return '\n'.join([r'\figure{',picture_begin,body,r'\end{tikzpicture}','}'])

cross=picture_body(comp[key('cross')]['first'])
middle=picture_body(comp[key('middle_ring')]['first'])
diagonal=picture_body(comp[key('arrow_end')]['first'])
loop_arrow=picture_body(comp[key('loop-arrow')]['first'])
assert cross in t and middle in t and diagonal in t and loop_arrow in t
whole=figure('\n'.join([
    scopes['top_polygon'],scopes['top_cut_sphere'],scopes['numbered_cap'],cross,
    scopes['upper_handle'],middle,diagonal,scopes['labelled_triangle'],
    scopes['lower_left_torus'],scopes['lower_middle_ring'],scopes['lower_handle'],loop_arrow]))
a=t.index(r'\figure{')
z=t.index('}% crop-candidate: scan 28',a)+1
t=t[:a]+whole+t[z:]
old_count=r'\unsure{hexagones|triangles}'
new_count=r'\unsure{hexagones}'
assert t.count(old_count)==1
t=t.replace(old_count,new_count)
finals={key(name):figure(scopes[name]) for name in names}
finals[key('lower_handle')]=figure(scopes['lower_handle']+'\n'+loop_arrow)
finals[key('counts')]=comp[key('counts')]['first'].replace(old_count,new_count)
finals[key('last-count')]=comp[key('last-count')]['first'].replace(old_count,new_count)

ink={
'top_polygon':'The thin contours have gaps, the right loop and lower bands are partly doubled, and a small crown loop and elongated interior sliver are visible. Dark vertices and the circular-arrow mark remain. At the left contour the two wings rise from the lower middle point (93,275); the blind generic arrow would point toward the last upper wing, so it is replaced with the literal three-point path. Other short arrows and patches are retained. The adjoining handle fragments are already in their own drawing.',
'top_cut_sphere':'The rounded object has open cuts, a partly doubled lower contour, an irregular upper dark ring with an opening and return, and a lower angular dark patch. The literal top-ring path replaces the former regular two-white-hole approximation. The two diagonal fragments are excluded because the complete global diagonal represents that ink once.',
'numbered_cap':'The labels and primes agree, while the interior 1 remains merged with its border and doubtful. The bottom-middle rim has an additional dark point with a white centre, which is retained explicitly. The medial loops, broken outlines and short heads are more detailed in the independent trace. The lower-left outer arc is uneven and partly solid, rather than a regular dashed ellipse.',
'cross':'The two crossing strokes and their short partial retracings are already represented in the first version. The second version changes coordinate description without improving the reading. Retain the exact first global paths.',
'upper_handle':'The left end disk contains a distinct upward arrow in addition to its interrupted diameter; this headed stroke was missing from the first version. Three contacts at the small upper hole, the boundary point, the small-ring gap, the dashed rear route and the arrows on the outer edges are visible. Adopt those own-object paths while omitting the neighboring polygon fragments.',
'middle_ring':'Four upper contact marks and three lower marks or contacts remain visible, together with interrupted rear routes, parallel contours and arrows. The first global scope already retains these details. The alternative trace drops some upper contacts and is not a stronger reading, so the entire first geometry is retained.',
'labelled_triangle':'The upper-right inner rim has an upward arrow, the central stroke has a downward head, the upper-left outer loop is open, and the margins are partly doubled with a lower angular patch. At the lower b_a label there is one principal lower bowl and a long upright; the small upper triangular white gap comes from the crossing diagonal, not a second rounded beta bowl. The subscript has a closed oval and exit, excluding c. The bottom raised flagged stroke favors a prime by the local prime forms, but has no secure foot excluding numeral 1, so a-prime versus a-to-the-1 remains doubtful. The contextual 6 and neighboring paths are already transcribed elsewhere.',
'lower_left_torus':'The outer and upper connector contours have open ends and free tips. Two tiny heads occur near the ends of the lower connector: the upper one points up-right and the lower one down-left. The complete independent body preserves these directions and the broken rear connector. Thickened joins are not promoted into extra nodes.',
'lower_middle_ring':'A short leftward head occurs at the top, separate from the down-right head toward the circled point. Inner traces remain distinct, the small contact ring encloses dark marks, and the lower connectors are broken. The dark marker on the bottom transverse connection, present in the first reading, is retained rather than lost from the independent trace. The following handwritten-count fragment belongs to the count text and is not duplicated.',
'lower_handle':'The source has open or partial rims, a faint left end closure, dotted rear routes, angular head wings, five separate short end marks and a separate circular-arrow sign. The inner free curved endpoint is headless. The left-end head is an L-shaped stroke with its tip at the upper corner, and the right V-shaped head points to the lower middle corner rather than its final wing. A redundant arc with an invented head is removed, while its literal small hook remains. The faint coherent vertical to the left and the parallel upper arc with a short tick are retained. The first dark left-end junction and other filled points remain. The circular arrow is kept once using the exact first global path; neighboring middle-ring, triangle and diagonal fragments are omitted.',
'arrow_end':'The long diagonal terminates in one fine hooked turn. There is no second arm establishing a complete symmetric arrowhead. The exact first full diagonal and return already represent this ink, so they are retained once.',
'counts':'The figures 4, 6 and 2 and the nouns sommets and arêtes are unchanged. In the last noun an initial ascender with an arch supports h, and a long g loop and the ones ending favor hexagones. The medial e/x/a run is still compressed, so the word remains doubtful. No secure crossed t or trian sequence supports triangles. Preserve the first three-line gather layout; rotated blind drawing context is not additional text.',
'interior-one':'The residual upright remains merged with the cap border and adjoining dark strokes. It cannot be securely isolated as a free numeral. Keep the first unsure 1; the expected sequence 1 through 6 supplies no evidence.',
'lower-left-label':'One principal lower bowl and a long upright support b, matching the unoccluded left b_a. The small triangular white gap above comes from the crossing diagonal, not a separate beta bowl. The subscript is a closed a oval with a short exit rather than an open c. Retain the first b_a at medium confidence.',
'loop-arrow':'The separate loop curves into an angular head with two converging ends. It is a circular-arrow sign rather than 5. The first global path already represents it; the other dark edge fragments in the blind box belong to the surrounding handle and are not additional text or a second sign.',
'last-count':'The initial ascender and arch form h, and the long descending g loop and ones ending favor hexagones. The compressed middle remains uncertain. No secure t crossbar or trian sequence supports the discarded triangles alternative. Only the doubt is narrowed; the leading 2 and favored noun are unchanged.',
'unsupported-gray-sweep':'Only paper texture, pale irregular traces and clipped pieces of neighboring real figures are visible. No coherent gray contour matching the proposed sweep can be followed. The dark fragments in the second reading are already represented in those neighboring figures. Retain the empty first reading and do not invent either a gray sweep or new isolated objects.',
}
different={k for k,c in comp.items() if c['different']=='yes'}
assert {key(name) for name in ink}==different
entries=[]
for k,c in comp.items():
    if c['different']!='yes':continue
    name=k.removeprefix('S28-')
    confidence='low' if name in ['counts','last-count','interior-one'] else 'high' if name in ['cross','arrow_end','loop-arrow'] else 'medium'
    d=dict(box=k,choice='revised' if k in finals else 'first',viewed_by_main=True,
           ink=ink[name],confidence=confidence)
    if k in finals:d['final']=finals[k]
    entries.append(d)

def crop(name):
    k=key(name)
    return dict(crop=f'crops/second/148_scan028/{k}.png',
        box=[int(boxes[k][s]) for s in ('x0','y0','x1','y1')])

p['changes'][0].update(final=whole,
    ink='The sheet contains the contours, free ends, arrows, numbered regions, lettered points and small filled or hollow marks inventoried below. The main reader retained the first cross and middle ring, and refined eight other drawings after inspecting their independent-reading crops. The full diagonal and lower circular-arrow path remain once. H prose descriptions are not copied as source text.',
    confidence='medium')
for i,name in [(2,'top_polygon'),(4,'top_cut_sphere'),(5,'numbered_cap'),
               (7,'upper_handle'),(8,'upper_handle'),(11,'labelled_triangle'),
               (12,'lower_left_torus'),(13,'lower_middle_ring'),(14,'lower_handle')]:
    p['changes'][i].update(final=finals[key(name)],ink=ink[name],**crop(name),confidence='medium')
p['changes'][5]['place']='Numbered cap, medial loops and bottom rim mark'
p['changes'][8]['place']='Upper handle, directional tips including left end disk'
p['changes'][11]['place']='Labelled triangle, directional heads and partial contours'
for i,name in [(1,'unsupported-gray-sweep'),(6,'cross'),(9,'middle_ring'),
               (10,'lower-left-label'),(15,'loop-arrow'),(16,'arrow_end')]:
    p['changes'][i].update(ink=ink[name],**crop(name))
p['changes'][17].update(final=finals[key('counts')])
# The isolated coherent vertical is genuine ink absent from both witnesses and
# is not covered by an earlier terminal-contour correction row.
x0,y0=[int(boxes[key('lower_handle')][s]) for s in ('x0','y0')]
isolated_scope='\n'.join([rf'\begin{{scope}}[shift={{({x0},{y0})}},line width=.5\pgflinewidth]',
                           scale_pt(isolated_vertical),r'\end{scope}'])
p['changes'].append(dict(place='Thin isolated stroke to the left of lower handle',
    c='omitted',h='omitted',final=figure(isolated_scope),
    ink='A faint but coherent thin stroke runs downward in three connected segments to the left of the lower handle. It is separate from the neighboring ring and from the long page diagonal; it is retained as a drawing stroke without assigning a label or a mathematical role.',
    **crop('lower_handle'),confidence='medium',kind='omission',
    against_c=True,against_h=True,math=False))

for d in p['decisions']:
    if d['id']=='M0276':d.update(ink=ink['interior-one'],**crop('interior-one'))
    elif d['id']=='M0277':d.update(ink=ink['lower-left-label'],**crop('lower-left-label'))
for u in p['unresolved']:
    if u['id']=='U28-02':
        u.update(reading=new_count,issue=ink['last-count'],alternatives=['hexagones'],**crop('last-count'))
p['unresolved'].append(dict(id='U28-03',place='Labelled triangle, bottom raised stroke',
    reading="\\unsure{a'|a^1}",issue='The short raised flagged stroke has no secure foot. A prime is favored by the local prime forms, but numeral 1 remains possible.',
    alternatives=[r'a^1'],confidence='low',**crop('labelled_triangle')))
for n in p['notation']:
    if n['form']=="a,b_a,c_a,c_b,a'":
        n['form']="a,b_a,c_a,c_b,\\unsure{a'|a^1}"
        n['observation']='Labels of the right-hand triangle. The b_a label is repeated at left and lower-left; c_b is at lower-right. The bottom raised stroke favors a prime but also admits numeral 1.'
for inv in p['inventory']:
    if inv['element']=='I28-07':
        inv['first_words_or_objects']="labelled triangle: a,b_a,b_a,c_a,c_b,unsure a prime/a to 1; open upper arc, upward inner-rim arrow and central downward head"
    elif inv['element']=='I28-12':
        inv['first_words_or_objects']='4 sommets; 6 arêtes; 2 unsure hexagones'
new_inv=dict(element='I28-14',kind='drawing',position='left of lower handle, x about 982–989 and y 699–791',
    first_words_or_objects='faint coherent isolated vertical stroke in three connected segments',
    sheet_kind='text',hand='his hand',transcribed='yes')
i=next(i for i,r in enumerate(p['inventory']) if r['element']=='I28-10')
p['inventory'].insert(i,new_inv)
for note in p['notes']:
    if note['id']=='N28-01':
        note['text']='Landscape manuscript drawing sheet in his hand. All nine principal drawings, the separate cross, the crossing diagonal, the thin isolated vertical stroke left of the lower handle, the three-line count text and marginal 27 are retained. No insertion, cancelled textual passage, typescript or letter was identified on this scan.'
    elif note['id']=='N28-04':
        note['text']='The first two lines read 4 sommets and 6 arêtes. The last noun favors hexagones from the initial h, long g loop and terminal ones, but its compressed middle remains doubtful. The triangles alternative is no longer supported. No Euler-characteristic or topological check has been used to decide it.'
    elif note['id']=='N28-06':
        note['text']='Drawings remain schematic TikZ reproductions. Eight geometric traces were refined, with literal head wings replacing generic arrows where those would reverse the visible tip. The first cross and middle ring retain their already adequate contours and contacts. The numbered cap includes the white-centred lower rim mark. The global diagonal and lower circular-arrow sign occur once, and overlapping neighboring fragments are excluded.'
p['notes'].append(dict(id='N28-BLIND',place='Independent second reading',
    text='The main reader personally inspected all 17 differing fixed crops. Eight drawing boxes and the two overlapping count readings were revised. The b_a reading remains, a new prime-versus-1 doubt is retained at the triangle bottom, and the last noun is narrowed to doubtful hexagones. Source-coordinate points are translated without additional scale; absolute pt strokes, radii, dash intervals and inherited stroke width are halved mechanically to preserve their relative weights in the whole-sheet figure. No new mathematical proof or computation was performed.'))
for h in p['hand_log']:
    if h['id']=='HL28-02':
        h.update(observation='Subscript a has a closed oval and short exit stroke under both b labels and the right c label. The lower-left b has one lower bowl and a long upright; the small triangular white gap above it is formed by the crossing diagonal, not a beta bowl.',
                 witness_effect='C M0277 alternative b_c and the blind beta_a alternative are rejected; b_a remains at medium confidence.',
                 crop='crops/second/148_scan028/S28-lower-left-label.jxl')
p['hand_log'].append(dict(id='HL28-05',pages=[28],
    observation='The triangle’s bottom raised stroke is short and flagged, with no secure foot. Local prime forms favor a prime, but numeral 1 remains possible.',
    crop='crops/second/148_scan028/S28-labelled_triangle.jxl',
    holds_at_every_observed_occurrence='One ambiguous occurrence; the six clear cap primes remain unchanged.',
    witness_effect='Both witnesses wrote a prime; the independent reading caused a local uncertainty to be added, not a different favored label.'))
p['blind_graphic_transforms']=transforms

# Static integrity checks; TeX compilation is explicitly prohibited.
assert len(entries)==17 and len(finals)==10
assert t.count(r'\begin{scope}')==t.count(r'\end{scope}')==9
assert cross in t and middle in t
assert t.count(diagonal)==1 and t.count(loop_arrow)==1
assert r'\fill[white] (211,239) circle[radius=0.325pt];' in t
assert r'\fill (241,321) circle[radius=0.75pt];' in t
assert r'\fill (190,422) circle[radius=0.9pt];' in t
assert r'\node at (95,355) {$b_a$};' in t and r'\node at (48,9)' not in t
assert old_count not in t and new_count in t
assert all((B/crop(e['box'].removeprefix('S28-'))['crop']).is_file() for e in entries)
level=0
for m in re.finditer(r'(?<!\\)[{}]',t):
    level+=1 if m.group()=='{' else -1
    assert level>=0,m.start()
assert level==0
page.write_text(t)
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
ap.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=28,adjudications=len(entries),revised_boxes=len(finals),
    changes_rows=len(p['changes']),inventory_rows=len(p['inventory']),
    against_c=sum(bool(r['against_c']) for r in p['changes']),
    against_h=sum(bool(r['against_h']) for r in p['changes']))))
