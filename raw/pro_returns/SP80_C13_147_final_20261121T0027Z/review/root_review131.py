"""Historical pre-blind review; do not rerun after the baseline is frozen."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'reports/147_scan131_report.json').read_text())
replacements=[(r'\mathord{\text{.\,--}}',r'\mathord{\text{.}\,-}'),
              (r'\text{-\,-}',r'\mathord{-\, -}'),(r'\text{--}','-')]
def recode(value):
    if isinstance(value,str):
        for a,b in replacements: value=value.replace(a,b)
        return value
    if isinstance(value,list): return [recode(x) for x in value]
    if isinstance(value,dict): return {k:(v if k in ('C','H') else recode(v)) for k,v in value.items()}
    return value
d=recode(d)
page=recode((R/'reports/147_scan131_proposed.tex').read_text())
# The first root crop separates two strokes in the prose Pi index as well as T.
old=r'$\Pi_{d_0,-,d_r}$.'
new=r'$\Pi_{d_0,\mathord{-\, -},d_r}$.'
assert old in page
page=page.replace(old,new)
row=d['rows'][7]
row['final']=row['final'].replace(old,new)
row['crop']='crops/147_scan131_components.jpg'
row['scan_shows']='The root’s first crop of this previously uncropped line separates two short horizontal strokes in the T index, without commas. The Pi index likewise has two separated horizontal marks, the first appreciably shorter, between a low comma after d_0 and another before d_r. There is a clear white gap between the two strokes. The final full stop is separate. The first reader’s single-dash Pi reading from the native half is corrected before freezing the blind baseline.'
d['second_boxes'][8]['reading']=d['second_boxes'][8]['reading'].replace(old,new)
d['notes'][0]+=' Root subsequently made and inspected the first components crop for a disagreement previously recorded only against the native bottom half; the retained first-crop total is12.'
d['notes'][5]=d['notes'][5].replace('whereas Pi has a single dash between commas','and Pi has two separate horizontal strokes between commas (the shorter first one became clear on root’s first crop of that line)')
for h in d['hand_log']:
    for key,value in list(h.items()):
        if isinstance(value,str): h[key]=value.replace('Pi has a single dash','Pi has two separate horizontal strokes')
links=[3,4,5,7,8]
for e,n in zip(d['check_events'],links):e['statement_id']+=f'; N131-{n:02d}'
d['check_events'].append({'statement_id':'N131-01; N131-02; N131-06; N131-09','type':'used and rechecked in this run','outcome':'Root inspected all12 first crops, including the newly retained component-formula crop. Read the final digit, retraced Delta, every index continuation and comma, quote marks, abbreviation and unfinished last line. This is a visual transcription check, not a proof of the geometric claims.'})
d['notes'].append('MC131-R: root tested the geometric last-vertex restriction on the coordinate crossing D={xy=0} in C². Here D₁ is the disjoint union of the two coordinate lines, D₂ is the crossing point, D₁* is two copies of C*, and D₂*=D₂. The two points of D₂,₁* map to the excluded origins of D₁, so this geometric target map does not restrict to D₂,₁*→D₁*. This exhibits an obstruction to inheriting the simplicial map after a first-vertex restriction. It does not rule out every abstract groupoid functor, a construction using additional choices, or a tangential construction, and does not complete the manuscript’s final (par. See review/mathematical_checks.md, MC131-R.')
d['check_events'].append({'statement_id':'MC131-R; N131-10','type':'computation or formal certificate','outcome':'Root computed the strata, their indicated open complements, the two incidence points, and their images for the explicit coordinate-axis divisor. The target origins lie outside D₁*, verifying the failure of that geometric restriction only. No general nonexistence theorem for abstract groupoid functors is claimed.'})
(R/'review/147_scan131_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
(R/'pages/147_scan131.tex').write_text(page)
with (R/'notation.md').open('a') as f:
    f.write('\n- Scan131: the final digit of the first formula number remains 212/217 doubtful. In214 the upper right tuple has a duplicated comma after d_1; continuation marks include a point-plus-dash and single continuous dashes. The subsequent prose T and Pi indices both have two separate horizontal strokes; only the Pi tuple has flanking commas. The abbreviation after simpliciale is p.v./p.r., with v-shaped ink first.\n')
with (R/'review/root_visual_readings.md').open('a') as f:
    f.write('\n### Scan131 final return review\nRoot inspected all11 reader crops, then made the first components crop [270,1770,1295,1905] for the previously uncropped lower formula disagreement. That crop reveals two separated continuation strokes in both T and Pi; the Pi single-stroke reading from the first reader’s half is corrected before baseline freeze. Existing simpliciale and formula214 crops were reopened to confirm the v-shaped abbreviation and duplicated upper comma. All12 rows and all second boxes were checked. M1295 stays undecided; all10 notes have scoped events, including the explicit coordinate-crossing test MC131-R. No sequence-based resolution of212/217 or completion of(par was supplied.\n')
