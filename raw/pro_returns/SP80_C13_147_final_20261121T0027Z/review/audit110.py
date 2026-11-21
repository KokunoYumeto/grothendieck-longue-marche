"""Historical root adjudication after all13 differing crops were inspected."""
from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[1]
with (R/'second/147_scan110_comparison.tsv').open() as f:c={x['box']:x for x in csv.DictReader(f,delimiter='\t')}
choices=[]
def keep(b,e,**kw):choices.append(dict(box=b,selection='first',changed='no',evidence=e,**kw))
def change(b,s,e):choices.append(dict(box=b,selection='literal',changed='yes',final=s,evidence=e))
keep('B03','The small rounded o, low u and separate high accent support où; no i stem or complete e supports i.e. The definition label has d, a low connecting e and tall f, without an accent. Crossed n, live d and outer circle agree. The context crop confirms the boundary; calligraphic P remains the established encoding of this ornate powerset sign.',crop='crops/147_scan110_second_B03_context.jpg')
change('B04',c['B04']['first'].replace('H(J).','H(J),'),'The final low mark has a descending curved tail: comma, not full stop. D has a separate exclamation stem and dot; the crossed high cluster stays a tentative deleted tilde. The operation is an angular wedge with the ornate S and nested D base below, not a multiplication cross.')
keep('B05','The cancelled glyph retains a top stroke, right descent and returning lower hook compatible with J. F lacks that surviving lower skeleton; the diagonals are deletion strokes. The overwritten underlined c/d stays doubtful.')
keep('B06','The connector has an open curl at its left end, hence a hook. The target high mark is a crossed/retraced cluster, not two separable live primes or a clearly formed xi. Retain the doubtful cancelled prime.')
keep('B07','The p/l entrance and g descender are followed by one small raised terminal t-like stroke, without separate m humps. The terminal s of ordonnés and following comma remain distinct.')
keep('B08','The a entrance, paired p descenders, tall l, dotted i, c/a bodies, tall t and final ion survive on either side of the thin strike. Application remains sufficiently recoverable without an added doubt.')
keep('B09','The target prime is clean and detached. The source high cluster is blackened and crossed, unlike the target prime. The full right arrowhead and final comma are visible; retain the doubtful cancelled source prime.')
keep('B10','A j-like descent is followed by a separate low me group before demande; qui would suppress that group. The crossed words admit sous forme tentatively, with the f descender under the strike. Both live insertions are clear. The second D repeats the bang stem/dot and crossed high decoration of B04, not a clean co exponent.')
change('B11',r'peut \unsure{réconstituer|reconstituer}','The first word ends in a raised returning t-like stroke: peut, not pour. A detached dark short stroke lies over the early e of the following word; réconstituer leads, with reconstituer retained because attribution of the tiny stroke is less secure than the main letters.')
change('B12',r'\unsure{de|des} $D_J$ \unsure{p.v.|p.r.} à $J$, via (155).','The initial de has a terminal turn whose status as a separate s is unresolved. The abbreviation has a v-shaped trough, while a reduced handwritten r remains possible. Its form on131 supports the same v-leading order without resolving the expansion. J, comma, via,155 and point agree.')
keep('B14','The thin strike leaves the elongated élément skeleton, its ascender and final t recoverable. The last glyph is a small lowercase loop and exit like the earlier e, without capital-E lobes. Retain the full cancelled sentence.')
keep('B15','The pencil digits are1,0,9. Only the margin wrapper differs; the page already places109 in a margin macro.')
keep('B17','A separate tall looped f precedes low c/o, ascended d, dotted i and final m. The gap after f and the codim strokes exclude a single word gradins. The final comma is clear.')
(R/'review/147_scan110_root_choices.json').write_text(json.dumps(choices,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/147_scan110.tex';s=p.read_text()
for old,new in [('H(J).','H(J),'),('peut reconstituer',r'peut \unsure{réconstituer|reconstituer}'),(r'de $D_J$ \unsure{p.r.|p.v.} à $J$, via (155).',r'\unsure{de|des} $D_J$ \unsure{p.v.|p.r.} à $J$, via (155).')]:
    assert old in s,old;s=s.replace(old,new)
p.write_text(s)
rp=R/'review/147_scan110_reviewed.json';d=json.loads(rp.read_text());e={x['box']:x['evidence'] for x in choices}
def row(place,C,H,final,b,confidence,kind,category):
    coords=next(x['coords'] for x in d['second_boxes'] if x['box']==b)
    d['rows'].append(dict(place=place,C=C,H=H,final=final,scan_shows=e[b],crop=f'crops/147_scan110_second_{b}.jpg',box=coords,confidence=confidence,kind=kind,against_C=True,against_H=True,marked_in_H=False,math_consequential=False,error_category=category))
row('(155), terminal punctuation',r'H(J).',r'H(J) .',r'H(J),','B04','high','misread symbol or index','Other')
row('late prose, accent in reconstituer','reconstituer','reconstituer',r'\unsure{réconstituer|reconstituer}','B11','medium','misread word','Words')
row('late prose, relative abbreviation',r'\unsure{p.r.|p.v.}','p.r.',r'\unsure{p.v.|p.r.}','B12','medium','misread word','Abbreviations expanded, spelling modernised')
for x in d['decisions']:
    if x['id']=='M1198':
        x['reading']=r'\unsure{p.v.|p.r.}';x['decision']='undecided';x['ink']+=' Blind review retains both, with the visible v-shaped form first, consistently with131.';x['crop']='crops/147_scan110_second_B12.jpg';x['box']=next(b['coords'] for b in d['second_boxes'] if b['box']=='B12')
for x in d['doubts']:
    if 'p.r.' in x['reading']:x['reading']='p.v.';x['alternatives']='p.r.'
d['doubts'] += [dict(place='late prose, accent',reading='réconstituer',alternatives='reconstituer',confidence='medium'),dict(place='before D_J in the relative-dependence phrase',reading='de',alternatives='des',confidence='medium')]
d['unresolved'].append('Blind review: réconstituer/reconstituer accent and de/des terminal turn remain locally uncertain.')
n=len(d['notes'])+1
d['notes'].append('Independent image-only rereading: root inspected all13 differing boxes. The terminal comma in155 replaces the first-pass point. A detached mark gives an accented réconstituer-leading local doubt; de/des also remains uncertain. The v-shaped abbreviation now has p.v. first consistently with131, with p.r. retained. The bang, below-wedge group and cancelled primes were retained against the blind alternatives. B03 required one additional contextual crop during this second-reading adjudication; neither TSV nor any fixed box was changed.')
d['check_events'].append(dict(statement_id=f'AUD110; N110-{n:02d}',type='used and rechecked in this run',outcome='Root inspected all13 differing second crops and the B03 context crop; adjudicated ink readings only. No mathematical proof is claimed.'))
rp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'notation.md').open('a') as f:f.write('\n- Blind review110/131: the relative abbreviation has the same v-shaped second-letter skeleton on both pages. Both now lead with p.v., retaining p.r. as the possible reduced r. Its intended expansion does not remove the uncertainty.\n')
