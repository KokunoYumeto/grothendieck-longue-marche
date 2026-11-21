#!/usr/bin/env python3
"""Apply root's completed crop adjudications mechanically; run once.

Root personally viewed all 20 differing crops before assigning these changes.
No image interpretation, TeX compilation, rebuild, or shared-log edit occurs here.
The original first and independent second reading TSVs remain unchanged.
"""
from pathlib import Path
import csv
import json
import re
from PIL import Image

B = Path(__file__).resolve().parents[2]
stem = B / 'second/148_scan026'
with Path(str(stem) + '_comparison.tsv').open() as f:
    comp = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
with Path(str(stem) + '_boxes.tsv').open() as f:
    boxes = {r['box']: r for r in csv.DictReader(f, delimiter='\t')}
rp = B / 'reviews/148_scan026.json'
p = json.loads(rp.read_text())
page = B / 'pages/148_scan026.tex'
t = page.read_text()
ap = Path(str(stem) + '_adjudications.json')
assert not p.get('second_audit') and not ap.exists(), 'Non-idempotent: already applied.'

def key(n):
    return f'B026_{n:02d}'

def commands(n):
    s = comp[key(n)]['second']
    content = s.split('\n', 1)[1].rsplit(r'\end{tikzpicture}', 1)[0]
    return [x.strip() + ';' for x in content.split(';') if x.strip() and not x.strip().startswith(r'\clip')]

def index(cs, start):
    matches = [i for i, c in enumerate(cs) if c.startswith(start)]
    assert len(matches) == 1, (start, len(matches))
    return matches[0]

def omit(cs, *starts):
    for s in starts:
        index(cs, s)
    return [c for c in cs if not any(c.startswith(s) for s in starts)]

def replace(cs, start, new):
    i = index(cs, start)
    cs[i:i+1] = new if isinstance(new, list) else [new]
    return cs

graphic_numbers = [5,6,7,4,8,14,20,19,13,15,16,17,12]
parts = {n: commands(n) for n in graphic_numbers}
parts[4] = parts[4][:index(parts[4], r'\draw (151,49)')]
parts[7] = replace(parts[7], r'\fill (223,839)', [
    r'\fill (223,839) ellipse (38 and 31);',
    r'\fill[white] (232,821) ellipse (9 and 8);'])
cs = parts[8]
leaders = [cs[index(cs, r'\draw (1,181)')], cs[index(cs, r'\draw (185,216)')]]
parts[8] = leaders + cs[index(cs, r'\draw[line width=1.0pt] (106,181)'):
                         index(cs, r'\draw (448,506)') + 1]
parts[8] = omit(parts[8], r'\fill (951,306)')
parts[8] = replace(parts[8], r'\draw (374,175)', [
    r'\draw (375,180)--(400,317)--(395,321);',
    r'\draw (402,331)--(429,496);'])
parts[12] = parts[12][:index(parts[12], r'\draw (349,46)') + 1]
parts[13] = omit(parts[13], r'\draw (0,40)', r'\draw (0,101)')
parts[14] = replace(parts[14], r'\draw (0,556)', r'\draw (56,545)--(135,641);')
parts[14] = omit(parts[14], r'\draw (0,361)', r'\draw (254,415)')
parts[17] = omit(parts[17], r'\draw[line width=1pt] (128,45)')
parts[19] = omit(parts[19], r'\draw (0,281)',
    r'\draw[line width=1.2pt] (823,26)', r'\draw[line width=1pt] (778,0)',
    r'\fill (823,26)')
parts[20] = omit(parts[20], r'\draw[line width=1pt] (0,58)')

display_dir = B.parent / 'blind_display/148_scan026'
scopes, transforms = {}, {}
for n in graphic_numbers:
    k = key(n)
    x0,y0,x1,y1 = [int(boxes[k][f]) for f in ('x0','y0','x1','y1')]
    if n in (5,8):
        # These two independent traces use native crop pixel coordinates.
        dw,dh = x1-x0,y1-y0
        opts = f'shift={{({x0},{y0})}}'
        basis = 'native crop pixels'
    else:
        dw,dh = Image.open(display_dir / (k + '.jpg')).size
        opts = f'shift={{({x0},{y0})}},xscale={{{x1-x0}/{dw}}},yscale={{{y1-y0}/{dh}}}'
        basis = 'display pixels'
    # TikZ coordinate transforms do not scale absolute pt dimensions. Restore
    # their relative physical size when embedding the independent trace into
    # this smaller whole-sheet coordinate system. Coordinate radii already
    # transform and are deliberately unchanged. This also preserves the explicit
    # 6pt/4pt dash-pattern proportions in the pants drawing.
    source_base_x = float(re.search(r'\[x=([0-9.]+)cm', comp[k]['second']).group(1))
    physical_ratio = .0065 * ((x1-x0)/dw) / source_base_x
    opts += rf',line width={physical_ratio:.8f}\pgflinewidth'
    def scale_pt(m):
        return f'{float(m.group(1))*physical_ratio:.6f}'.rstrip('0').rstrip('.') + 'pt'
    parts[n] = [re.sub(r'(?<![A-Za-z0-9.])([0-9]*\.?[0-9]+)pt', scale_pt, c) for c in parts[n]]
    scopes[n] = '\n'.join([rf'\begin{{scope}}[{opts}]'] + parts[n] + [r'\end{scope}'])
    transforms[k] = dict(basis=basis, coordinate_size=[dw,dh],
        native_box=[x0,y0,x1,y1], native_x=f'{x0}+({x1-x0}/{dw})*u',
        native_y=f'{y0}+({y1-y0}/{dh})*v', source_base_x_cm=source_base_x,
        physical_size_ratio=physical_ratio)

picture_begin = r'\begin{tikzpicture}[x=.0065cm,y=-.0065cm,line cap=round,line join=round]'
def figure(content):
    return '\n'.join([r'\figure{', picture_begin, content, r'\end{tikzpicture}', '}'])

finals = {key(n): figure(scopes[n]) for n in graphic_numbers}
whole_figure = figure('\n'.join(scopes[n] for n in graphic_numbers) + '\n' +
                       r'\draw (521,962)--(535,940);')
a = t.index(r'\figure{')
z = t.index('}% crop-candidate: scan 26', a) + 1
t = t[:a] + whole_figure + t[z:]

diagram = comp[key(1)]['first'].replace(r'\text{dont tous les sommets sont}',
    r'\text{dont tous les sommets \unsure{sont}}').replace(
    r'\text{cartes }\uline{\text{cellulaires}}', r'\text{carte }\uline{\text{cellulaire}}')
struck = r'\deleted{\unsure{variétés|variété} \unsure{algébriques|algébrique} d}'
relation = (r'\sigma_0^{\unsure{2|1}}=\sigma_1^2=\sigma_2^{\unsure{2|1}}='
            r'(\sigma_0\sigma_2)^2=(\sigma_0\sigma_1)^3=1')
r_curves = r'\(\mathbb R\)-\unsure{courbes|courbe} \unsure{algébriques|algébrique}'
margin = r'\margin{\(\sigma_0,\sigma_1,\sigma_2\)\quad ses pts fixes}'
old_relation = r'\sigma_0^2=\sigma_1^2=\sigma_2^2=(\sigma_0\sigma_2)^2=(\sigma_0\sigma_1)^3=1'
replacements = [(comp[key(1)]['first'],diagram), (comp[key(9)]['first'],struck),
                (old_relation,relation), (comp[key(11)]['first'],r_curves),
                (r'\margin{\(\sigma_0,\sigma_1,\sigma_2\)\quad ss pts fixes}',margin)]
for old,new in replacements:
    assert t.count(old) == 1, old
    t = t.replace(old,new,1)
finals[key(1)] = diagram
finals[key(9)] = struck
finals[key(10)] = '\\[' + relation + '\\]'
finals[key(11)] = r_curves
finals[key(12)] += '\n' + margin

ink = {
1: 'Two separate opposed shafts remain visible: the upper one has a leftward head and the lower one a rightward head. They are not merged into a single double-headed shaft. The four-letter conn and the inserted ou 1 remain. In the compact word after sommets, an initial s-like rise and terminal t-like turn survive, but the middle is too compressed to assert sont without doubt. The right caption begins with a small x-height c and ends each word with a single e; no separate plural s is visible. Read lowercase singular carte, with cellulaire underlined.',
2: 'The compact prefix has baseline o-r followed by a raised t. The separate long slash before triangulée is visible and must remain. There is no i-e-n sequence or full stop establishing orient. The first reading and the similarity sign are retained.',
3: 'The prefix has crossed Z-like strokes followed by n and a short bar, without a secure subscript n-minus-1. The revêtements retracing still leaves its deletion status uncertain. The projective-line formula has a raised 1 and doubled/open C subscript. The word after ramifiés remains compressed and doubtful; no clearly raised mt justifies changing it to a new abbreviation. Retain the complete first reading.',
4: 'The six named boundary endpoints and labels remain in their observed positions. The lower rim has separate dashes, and several edges have partial doubled contours and open head strokes. The central curved arrow and small top-edge patch are traced literally. The tall upright and retraced double bowl at b_A obscure its case; favor b_A from its visible lower bowl and the paired local b_C, while retaining B_A as an alternative. Neighboring context marks are not duplicated.',
5: 'The narrow shape has a small interior loop, a short vertical stroke ending in a dark point, a doubled outer rim and a dark bottom patch. These details are preserved by the complete independent trace in native crop pixels, rather than by expanding its coordinates as display pixels.',
6: 'The polygon has open upper and right junctions, a doubled lower-left diagonal, a fork at the centre and small tapered patches. Adopt these literal gaps and traces. No direction or mathematical meaning is assigned to the tapered marks.',
7: 'There are three surrounding rings. The top and right inner marks are filled, while the dark lower-left mark contains a tiny off-centre white hole. Preserve that hole explicitly instead of accepting a uniformly filled blind patch. Three small rim ticks and the uneven outer contour are also visible.',
8: 'The primary central graph has partly retraced bands, three branch edges, the vertical branch and its lower head, a long crossing lower curve and a short right-pointing head near the crossing. The two curved leaders above it are retained. The nearly vertical triangular side has an interruption and a small kink, so the blind straight line is replaced by two separated bent strokes. The large-loop junction is supplied once by its own box. Prose, correspondence arrows, the segment, labels and neighboring figures are omitted from this overlapping crop because their dedicated elements already transcribe them.',
9: 'The cancellation crosses the low endings of both words. The favored plurals variétés and algébriques remain, but the singular endings cannot be excluded. The final d has a clear tall ascender and low oval. No separate e is visible before the cancellation stroke ends, so no de or doubtful e is supplied.',
10: 'The first and third tiny sigma exponents have curved upper strokes but incomplete feet. Their curvature favors 2, while 1 remains possible in each place. The middle exponent 2 and the later exponents 2 and 3 and final 1 are clear. No involution argument is used to select the uncertain exponents.',
11: 'The c-o-u-r sequence is followed by a tall b ascender, securing the courbe stem against cartes. The low terminal joining strokes do not establish a plural s in either courbes or algébriques. Retain the favored plurals with singular alternatives, and keep the doubled R and hyphen.',
12: 'The oval has an upper-right gap, two filled marks and a lower-left open ring, plus a short detached upper tick. In the adjoining note a distinct small closed e loop lies between two s-like strokes: ses, not ss or sans. The t ascender and s body of pts return to the same baseline as the p body, so ts is not superscripted. Keep the sigma list and ses pts fixes once in the separate margin text; the crossing graph arrow is supplied by the central graph.',
13: 'The three-lobed cycle has a small open right endpoint, filled or tapered marks at other junctions, partial doubled contours and visible gaps. The left lower junction is not a separate filled circular dot. Adopt the literal paths and patches without giving them extra arrow semantics, and omit the two incoming context fragments.',
14: 'The large loop has three partly overlapping rims and a dark junction patch. Its sign consists of a cross with a separate lower bar, hence plus/minus. Retain the short outgoing lower-right stroke but omit the incoming segment already supplied by the central graph. The final two cursive context fragments belong to nearby text and are not drawn a second time.',
15: 'The two unequal loops are joined by a sloping stem. The lower opening has a visible gap close to the connector, and the upper junction has a small angular dark patch. Preserve the complete independent tracing; no arrow is added at that patch.',
16: 'The large annulus has an open inner contour, a doubled thin pole ribbon, a dark top junction, lower tapered patches and partial parallel traces at the upper and right sides. Adopt the explicit paths, retaining the gaps rather than replacing them with smooth closed ellipses.',
17: 'The figure-eight lobes are unequal. The top rim is partly doubled and a small angular patch lies near its returning contour; it is not a definite arrowhead. The detached upper context stroke is omitted here because the full native isolated tick is retained once outside the scopes.',
18: 'The pencil 2 has a curved head and long baseline foot. The 5 has an open head and a rounded lower curve. Both readings give 25; the extra mspage wrapper changes no numeral.',
19: 'The open oval surrounds a heavy segment with a filled endpoint labelled 0 and a blunt opposite end labelled 1. The long foot belongs to the numeral 1, not an underline. The diagonal, upper branch, vertical stem and junction patch in the crop belong to the central graph and are not duplicated.',
20: 'The three sigma labels carry subscripts 0, 1 and 2. Two distinct shallow brackets remain beneath them, with a clear gap. The readings and bracket scopes are unchanged; their separate positions are refined to the native crop coordinates. The incoming diagonal is already in the central graph.',
}
assert {key(n) for n in ink} == {k for k,c in comp.items() if c['different']=='yes'}
entries=[]
for k,c in comp.items():
    n=int(k.rsplit('_',1)[1])
    d=dict(box=k,choice='revised' if k in finals else 'first',viewed_by_main=True,
           ink=ink[n],confidence='low' if n in [3,9,10] else 'high' if n in [2,18] else 'medium')
    if k in finals:
        d['final']=finals[k]
    entries.append(d)

def crop(n):
    k=key(n)
    return dict(crop=f'crops/second/148_scan026/{k}.png',
                box=[int(boxes[k][s]) for s in ('x0','y0','x1','y1')])

def update(index,n,final=None,**extra):
    row=p['changes'][index]
    row.update(ink=ink[n],**crop(n),**extra)
    if final is not None:
        row['final']=final

update(1,1,r'\text{carte }\uline{\text{cellulaire}}',
       place='Right caption: lowercase singular carte cellulaire and underline',confidence='medium')
update(2,1)
update(9,12,'ses pts fixes',place='Fixed-point note: ses',
       kind='misread word',confidence='medium')
update(11,18)
for i,n in [(12,7),(13,8),(14,20),(16,13),(17,16),(18,17),(19,12)]:
    # The diagram row need not repeat the separately logged fixed-point words.
    update(i,n,figure(scopes[n]),confidence='medium')
update(15,14,r'\pm')
for i,n in [(0,1),(3,2),(4,2),(5,2),(6,3),(7,3),(10,10)]:
    # These unchanged textual readings retain their original focused evidence;
    # the new audit evidence is added rather than replacing it with broad prose.
    p['changes'][i]['ink'] += ' Blind-audit confirmation: ' + ink[n]
    p['changes'][i].update(**crop(n))

# The former courbes row was only a resolution of C's uncertainty. The favored
# plural remains unchanged, and it is doubtful again; no C/H text difference
# remains that warrants this row. The stem and ending evidence goes in doubts.
removed=p['changes'].pop(8)
assert removed['place']=='R-courbes algébriques'
new_drawings=[
    (4,'Pants drawing: partial doubled rims, lower dashes and endpoint marks'),
    (5,'Narrow nested loop: inner loop, point and bottom patch'),
    (6,'Upper polygon: open junctions, doubled diagonal and tapered marks'),
    (14,'Large loop: overlapping rims and junction strokes'),
    (15,'Joined unequal loops: lower opening and angular junction'),
    (19,'Open oval and segment: uneven contour and blunt endpoint'),
]
for n,place in new_drawings:
    p['changes'].append(dict(place=place,c=comp[key(n)]['first'],
        h='Drawing described only',final=figure(scopes[n]),ink=ink[n],**crop(n),
        confidence='medium',kind='drawing or diagram',against_c=True,against_h=True,math=True))

for d in p['decisions']:
    if d['id']=='M0273':
        d.update(decision='undecided',reading=r'\unsure{courbes|courbe}',
                 ink=ink[11],**crop(11),confidence='medium')
    elif d['id']=='M0274':
        d.update(decision='first',reading='ses',ink=ink[12],**crop(12),confidence='medium')
for u in p['unresolved']:
    if u['place']=='First word of the struck phrase':
        u.update(place='Endings in the struck phrase',reading=struck,issue=ink[9],
                 alternatives=['variété','algébrique'],**crop(9),confidence='low')
p['unresolved'] += [
    dict(place='Top definition, word after sommets',reading=r'\unsure{sont}',
         issue=ink[1],alternatives=['sont'],confidence='low',**crop(1)),
    dict(place='Pants drawing, right upper endpoint label',reading=r'\unsure{b_A|B_A}',
         issue=ink[4],alternatives=[r'B_A'],confidence='low',**crop(4)),
    dict(place='Sigma relation, first and third exponents',reading=relation,
         issue=ink[10],alternatives=['1 in either tiny exponent'],confidence='low',**crop(10)),
    dict(place='R-courbes phrase, plural endings',reading=r_curves,
         issue=ink[11],alternatives=['courbe','algébrique'],confidence='medium',**crop(11)),
]
for inv in p['inventory']:
    replacements={
        'I026.02':r'dont tous les sommets \unsure{sont}',
        'I026.05':r'two shafts, upper leftward and lower rightward; carte \uline{cellulaire}',
        'I026.15':r'pants; A,B,C,c_B,c_A,b_C,\unsure{b_A|B_A},a_C,a_B; literal orientation strokes',
        'I026.21':struck,'I026.22':relation,'I026.23':r_curves,'I026.30':'ses pts fixes'}
    if inv['element'] in replacements:
        inv['first_words_or_objects']=replacements[inv['element']]

for note in p['notes']:
    if note['id']=='S026.01':
        note['text']='The page places a connected, non-oriented cellular map with vertices of order 3, and the interlinear addition ou 1, in a correspondence with a singular carte cellulaire. The two opposed shafts remain separate. The compact sont is now doubtful. These are source readings, without a supplied proof.'
    elif note['id']=='S026.03':
        note['text']='The first and third small sigma exponents remain doubtful between 2 and 1, with 2 favored by their curved tops. The middle exponent 2, the later exponents 2 and 3, and the final 1 are clear. No involution expectation, algebraic proof or independent computation was used to settle the doubtful exponents.'
    elif note['id']=='S026.04':
        note.update(text='Beside the three-point oval, the page lists sigma0, sigma1, sigma2 and writes ses pts fixes. The small closed e between two s-like strokes distinguishes ses from ss and sans. The short form pts is retained at baseline; its expansion remains confined to the abbreviation list.',**crop(12))
    elif note['id']=='N026.02':
        note['text']='The horizontal strike crosses the low endings of variétés and algébriques, so the favored plurals remain doubtful against singular alternatives. The final d is legible and no e is supplied. The following R-courbes algébriques phrase also has uncertain plural endings; the b ascender secures the courbe stem.'
p['notes'].append(dict(id='N026.BLIND',kind='audit',place='Independent second reading',
    text='The main reader personally inspected all 20 differing boxes. Thirteen graphic boxes were refined, preserving the lower-left white centre in the three-point oval, the kink and gap in the central graph, and the isolated tick. Overlapping text, labels and neighboring figures were retained once in their dedicated elements. The caption is singular carte cellulaire; the fixed-point note reads ses pts fixes. Doubts were reopened in sont, plural endings, one endpoint label and two small exponents. Absolute pt stroke widths, the inherited default stroke width and explicit dash intervals were scaled mechanically by the physical coordinate-unit ratio; coordinate radii were already transformed. No new mathematical check was performed.'))
p['abbreviations']=[a for a in p['abbreviations'] if a['form']!='ss']
for h in p['hand_log']:
    if h['observation'].startswith('The written short form ss'):
        h.update(observation='The compact word ses has a small closed e loop between two s-like strokes.',
            holds_at_every_observed_occurrence='One occurrence, in ses pts fixes.',
            witness_effect='C offered ses or sans, H read sans, and the initial consolidated reading ss omitted the visible medial e; the blind audit restored ses.')
    elif h['observation'].startswith('Connected prose'):
        h['witness_effect']='The tall b secures the courbe stem against C’s cartes alternative, but the low plural endings remain doubtful.'
    elif h['observation'].startswith('The initial C in Carte'):
        h['observation']='The initial C in Carte is taller than the small open c beginning carte in the right caption.'
for n in p['notation']:
    if n['form']==r'a_B,a_C,b_C,b_A,c_B,c_A':
        n['form']=r'a_B,a_C,b_C,\unsure{b_A|B_A},c_B,c_A'
        n['caution']='The right upper endpoint label has a retraced bowl and tall upright; its case remains uncertain. The local b_C supports b_A as the favored reading without regularizing the source.'
p['notation'].append(dict(form=relation,use='Displayed sigma relation.',pages=[26],
    caution='The first and third tiny exponents favor 2 but also admit 1; algebraic expectations do not resolve them.'))
p['blind_graphic_transforms']=transforms

# Meaningful static checks only; no TeX compilation is permitted.
assert len(entries)==20 and len(finals)==17
assert t.count(r'\begin{scope}')==t.count(r'\end{scope}')==13
assert t.count(r'\draw (521,962)--(535,940);')==1
assert t.count(r'\fill[white] (232,821) ellipse (9 and 8);')==1
assert t.count('ses pts fixes')==1 and 'ss pts fixes' not in t
assert r'\draw (374,175)--(427,507);' not in t
assert r'\draw (375,180)--(400,317)--(395,321);' in t
assert r'\draw (402,331)--(429,496);' in t
assert t.count(r'\arrow[r,leftarrow,shift left=.6ex]\arrow[r,shift right=.6ex]')==1
assert all((B/crop(int(e['box'].rsplit('_',1)[1]))['crop']).is_file() for e in entries)
level=0
for m in re.finditer(r'(?<!\\)[{}]',t):
    level+=1 if m.group()=='{' else -1
    assert level>=0,m.start()
assert level==0
page.write_text(t)
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
ap.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=26,adjudications=len(entries),revised_boxes=len(finals),
    changes_rows=len(p['changes']),inventory_rows=len(p['inventory']),
    against_c=sum(bool(r['against_c']) for r in p['changes']),
    against_h=sum(bool(r['against_h']) for r in p['changes']))))
