"""Manual decisions from the saved blind crops and one new word-comparison crop."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan040'
r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,decision,evidence,changed=False):dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b01','retain first','Both readings give double-struck Z with separate rightward and downward arrows to 1, label 23 and a following comma. TikZ empty-cell and brace differences are representational.')
d('b02','broaden cancelled label doubt','The crossed last digit can be a 4 obscured by the strike or the two rounded returns of 3. Neither is secure; retain both. The F doubt, two waves above one straight bar, hat on C, and comma agree.',True)
d('b03','retain first','Two filled points are joined by a single rightward arrow, followed by a comma. The diagram and inline encodings represent the same ink.')
d('b04','retain first','The word after est has an e/n onset and then c-o-r-e; the connected r and final return do not make cone. The underline begins after F and spans est encore. No extra un is supplied.')
d('b05','retain first','The braced singleton is a, the equivalence has one wave over a bar, and C has a separate upright stroke. Math delimiters and spacing differ only.')
d('b06','broaden overtraced-glyph doubt','The large glyph has both the returning V contour and strong transverse/diagonal strokes that allow Z. Their layers cannot be dated. Add Z as an alternative without inventing a deleted underlying letter. The star, z,Z indices, doubled D stem and infinity index are secure.',True)
d('b07','retain first','The pi is small, with joined descending legs like the later K(pi,1). The following mark is one thick horizontal stroke with terminal ink pooling; no separate letter body is recoverable beneath it, so retain the dash rather than inventing a cancelled word.')
d('b08','qualify abbreviation and broaden word ending','The lower stroke of the shorthand has a loop and a small hump beneath the upper bar, allowing barred m as well as a roughly written equals abbreviation. The adjective has only one clear tall post-i stem and no separately secure final s; add singular contractile while retaining the other possibilities.',True)
d('b09','revise provisional cancelled phrase','Two short horizontal remnants precede a low loop and upright like si, then the clear l and returns of les. The old où les does not account for the initial shorthand. Retain the whole deletion as unsure, with barred-m si les / equals si les alternatives. The raised qui en and its attachment are clear.',True)
d('b11','qualify pierres/pièces; retain néanmoins','The noun has two angular low shoulders after the dotted i/e rather than a clearly open c, and no independent grave accent is distinguishable. Pierres is favored but pièces remains possible. The first occurrence was separately cropped at [310,1050,1115,1190] and has the same ambiguity. The insertion ends with low n/s-like returns and has no tall terminal t; néanmoins remains preferable to vraiment. Its curved leader ends between pas and le. Capital Pi has a flat roof and distinct legs. The opening quote remains uncertain.',True)
d('b12','qualify shorthand','The lower short stroke has a waved onset beneath the upper bar; it may be the equals abbreviation or a compressed barred m. Retain that distinction as a local doubt, without expanding either. The opening quote remains compressed and uncertain.',True)
d('b13','retain first','The lower-case pi and the written dash, followed by en d’autres termes and a comma, agree. The em-dash character versus three-hyphen LaTeX is representational.')
d('b14','retain first','The label is 24; a single rightward arrow joins X to the same F form. The sentence has raised t after néc and a final point. Inline display versus diagram wrapper changes no reading.')
repls=[(r'\unsure{(24)}',r'\unsure{(24)|(23)}'),(r'\unsure{V|\mathcal V}',r'\unsure{V|\mathcal V|Z}'),(r'premières $=$ \unsure{contractibles|contractiles}',r'premières $\unsure{\overline m|=}$ \unsure{contractile|contractiles|contractibles}'),(r'\deleted{\unsure{où les}}',r'\deleted{\unsure{$\overline m$ si les|$=$ si les}}'),('pièces de construction',r'\unsure{pierres|pièces} de construction'),(r'de $X$, $=$ si',r'de $X$, $\unsure{=|\overline m}$ si')]
for a,b in repls:t=t.replace(a,b)
updates={'r02a':r'\deleted{\unsure{(24)|(23)}}','r06a':r'\unsure{V|\mathcal V|Z}^*_{z,Z}','r08a':r'\unsure{\overline m|=}','r16':r'\unsure{contractile|contractiles|contractibles}','r09b':r'\deleted{\unsure{$\overline m$ si les|$=$ si les}}','r12a':r'\unsure{=|\overline m}'}
box_for={'r02a':'b02','r06a':'b06','r08a':'b08','r16':'b08','r09b':'b09','r12a':'b12'}
for row in r['changes']:
    if row['id'] in updates:
        row['final']=updates[row['id']];row['evidence']+=' Blind review: '+dec[box_for[row['id']]]['evidence'];row['confidence']='low'
        if row['id'] in ['r08a','r16','r09b']:row['diff_c']=True
        if row['id']=='r16':row['diff_h']=True
for q in r['decisions']:
    if q['id']=='M0954':q['reading']=updates['r06a'];q['evidence']+=' Blind review also admits Z; the overwritten layers remain undecided.'
for q in r['doubts']:
    if q['place'].startswith('first displayed label'):q['reading']=updates['r02a'];q['alternatives']='cancelled (24) / (23)'
    if q['place']=='first V, M0954':q['reading']=updates['r06a'];q['alternatives']='ordinary V / calligraphic V / Z; layer history unresolved'
    if q['place'].startswith('contractibility word'):q['reading']=updates['r16'];q['alternatives']='contractile / contractiles / contractibles';q['reason']=dec['b08']['evidence']
    if q['place']=='cancelled words below qui en':q['reading']=updates['r09b'];q['alternatives']='barred-m si les / equals si les';q['reason']=dec['b09']['evidence']
r['doubts'] += [
 {'place':'first shorthand, before contractibility adjective','reading':r'$\unsure{\overline m|=}$','alternatives':'barred m / equals shorthand','confidence':'low','reason':dec['b08']['evidence']},
 {'place':'two occurrences before de construction','reading':r'\unsure{pierres|pièces}','alternatives':'pierres / pièces','confidence':'medium','reason':dec['b11']['evidence']},
 {'place':'after de X','reading':r'$\unsure{=|\overline m}$','alternatives':'equals shorthand / barred m','confidence':'low','reason':dec['b12']['evidence']}]
for num,place,crop,box in [('r17a','first occurrence before the singleton','crops/151_scan040_notation_first_pieces.jpg',[310,1050,1115,1190]),('r17b','quoted occurrence after Pi_1','crops/second_151_scan040_b11.jpg',[315,1672,1651,1890])]:
    r['changes'].append({'id':num,'place':place,'c':'pièces','h':'pièces','final':r'\unsure{pierres|pièces}','evidence':dec['b11']['evidence'],'confidence':'medium','kind':'misread word','error_category':2,'diff_c':True,'diff_h':True,'marked_h':False,'crop':crop,'box':box,'consequential':''})
r['notes'].append('scan040.N11 Blind review broadens the cancelled number, the overtraced first V/Z, the short-form shapes, and the contractibility ending. The crossed phrase is provisionally shorthand + si les rather than où les. Both occurrences of the construction noun have the same angular low letters: pierres is favored, with pièces retained as an alternative. The inserted néanmoins and its leader are retained; no final t supports the blind vraiment proposal. The earlier notes describing a definite equals sign or plural adjective must be read with these final qualifications.')
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
finals={'b02':comp['b02']['first'].replace(r'\unsure{(24)}',r'\unsure{(24)|(23)}'),'b06':comp['b06']['first'].replace(r'\unsure{V|\mathcal V}',r'\unsure{V|\mathcal V|Z}'),'b08':r'$\unsure{\overline m|=}$ \unsure{contractile|contractiles|contractibles} !).','b09':comp['b09']['first'].replace(r'\deleted{\unsure{où les}}',updates['r09b']),'b11':comp['b11']['first'].replace('pièces de construction',r'\unsure{pierres|pièces} de construction'),'b12':comp['b12']['first'].replace('$=$',r'$\unsure{=|\overline m}$')}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'low'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
