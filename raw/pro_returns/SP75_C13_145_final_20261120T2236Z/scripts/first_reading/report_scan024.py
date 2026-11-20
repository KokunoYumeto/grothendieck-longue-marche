from pathlib import Path
import csv
import json
import re

ROOT=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
PACKET=ROOT/'packets/145_scan024'
OUT=ROOT/'edition/reader_reports'
C=(PACKET/'C.tex').read_text()
H=(PACKET/'H.tex').read_text()
meta=json.loads((ROOT/'edition/crops/145_scan024_crop_meta.json').read_text())
crops={int(x['file'].split('_')[2]):x for x in meta}
# The target is the words; the native half, not this word crop, showed the hats.
crops[6]['target']='des elts de lexical omission; following E body is context, with upper hats clipped by the crop'
for x in meta:
    if x['file']==crops[6]['file']:x['target']=crops[6]['target']
(ROOT/'edition/crops/145_scan024_crop_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

state=r'\unsure{\deleted{\unsure{-1}}|\unsure{-1}}'
right_term=r'\unsure{\Gamma_{\unsure{0,3}}|\mathbb\Gamma}'
map_letter=r'\unsure{\hat k_0|\hat\kappa_0}'
tex=C
replacements=[
    (r'\unsure{qui contient|qui centralise}',r'\unsure{qui contient}'),
    (r'\unsure{\tau}',r'\dot\tau'),
    (r'\unsure{\Gamma|\mathbb\Gamma}',r'\mathbb\Gamma'),
    (r'\Gamma_{\unsure{0,3}}',right_term),
    (r'&=\{1\}.',r'&=\{1\}'),
    (r'\deleted{\uline{NB}}',r'\deleted{\uline{\unsure{NB}}}'),
    (r'\unsure{\cup|\Vert}',r'\cup'),
    ('est une égalité.}','est une égalité}'),
    (r'\hat\kappa_0',map_letter),
    ('\\margin{\\uline{NB}\n\\[\n\\diagram', '\\margin{\\uline{NB}\n\\diagram'),
    ('\\end{tikzcd}}\n\\]\n---','\\end{tikzcd}}\n---'),
]
for old,new in replacements:
    assert tex.count(old)==1,(old,tex.count(old))
    tex=tex.replace(old,new)
assert tex.count(r'\hat\pi')==3
tex=tex.replace(r'\hat\pi',r'\hat\Pi')
assert tex.count(r'^{\deleted{\unsure{-1}}}')==4
tex=tex.replace(r'^{\deleted{\unsure{-1}}}',r'^{'+state+'}')
tex=tex.rstrip()+'\n'
OUT.mkdir(parents=True,exist_ok=True)
(OUT/'145_scan024.tex').write_text(tex)

changes=[]
def change(place,c,h,final,ink,crop,kind,cats,cc=False,hc=True,confidence='high',marked='no',math=''):
    assert cc or hc
    cr=crops[crop]
    x=dict(id=f's024-{len(changes)+1:02d}',place=place,C=c,H=h,final=final,ink=ink,
           confidence=confidence,kind=kind,c_changed=cc,h_changed=hc,marked_in_H=marked,
           crop=cr['file'],box=cr['box'],error_category=cats,math_consequence=math)
    changes.append(x)
    return x['id']

ins_c=r'\inserted{(\unsure{qui contient|qui centralise} $\unsure{\tau}$)}'
ins_final=r'\inserted{(\unsure{qui contient} $\dot\tau$)}'
id_ins=change('Opening paragraph, interlinear parenthesis',ins_c,r'(\ill{} \ill{})',ins_final,
    'The parenthesis is above the double-hatted Gamma and has an attachment stroke descending beside it. A long q descender, short ui run and the next word’s c/on/t-like strokes favor qui contient. The compressed ending is not wholly plain, so the words remain doubtful; qui centralise is not supported by the visible word length and tall strokes.',1,
    'readable ink left as \\ill{}',[2,5,6],confidence='medium',marked='yes')
id_tau=change('Opening insertion, final dotted symbol',r'\unsure{\tau}',r'\ill{}',r'\dot\tau',
    'There is a separate dark dot above the short tau bar and curved descending body. The body can be compared with the undotted tau in {1,tau} in crop03; the added dot is a genuine separated mark, not part of the bar.',1,
    'misread symbol or index',[1,3,5],cc=True,marked='yes')
id_pi1=change('Opening extension sentence, after par',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
    'A flat horizontal cap has two separate full-height descending legs and a distinct circumflex above. This is read locally as capital Pi. The nearby doubled-left Gamma has only a short right downturned cap and is graphically different.',2,
    'misread symbol or index',[1],cc=True)
id_leftgamma=change('First intersection formula, left term',r'\unsure{\Gamma|\mathbb\Gamma}',r'\Gamma',r'\mathbb\Gamma',
    'A separate narrow inner left stroke runs below the cap beside the outer long left stroke. The lower row has the same doubled-left form; neither has a second full right leg.',3,
    'misread symbol or index',[1],cc=True)
term_c=r'\deleted{\unsure{\mathfrak S_3}}\Gamma_{\unsure{0,3}}'
term_final=r'\deleted{\unsure{\mathfrak S_3}}'+right_term
id_rightgamma=change('First intersection formula, overwritten right term',term_c,r'\boldsymbol{\Gamma}',term_final,
    'The thick left wall and top cap overwrite a pale curving ornate-letter body. A dense low cluster can be read as 0,3, but cannot be separated securely from the earlier letter and retracing. Both a subscripted Gamma and a doubled Gamma are retained locally; the underlying struck ornate S_3 remains doubtful.',3,
    'deletion state',[1,5,7],confidence='low',marked='yes')
id_set_stop=change('Second intersection formula, after closing brace',r'\{1\}.',r'\{1\}',r'\{1\}',
    'The right curly brace ends the lower row. The following paper is blank; no isolated full stop follows it.',3,
    'text not on the page',[9],cc=True,hc=False)
nb_final=r'\margin{\deleted{\uline{\unsure{NB}}}}'
id_cancelnb=change('Separate right-margin cancelled NB',r'\margin{\deleted{\uline{NB}}}', '',nb_final,
    'A tall N-like outline and two curved B-like lobes remain beneath several diagonal crossing strokes. A separate underline survives below. The letter outlines suggest NB, but the dense cancellation warrants a local struck-word doubt. H supplies only an editorial notice of a rature, not the inscription.',4,
    'omission',[2,3,7],confidence='medium',marked='yes')
diagram_c=r'''\diagram{\begin{tikzcd}
\unsure{\mathfrak S_3|\mathcal S_3}\times\widehat{\widehat\Gamma}^!\arrow[d,phantom,"{\unsure{\cup|\Vert}}"]&&\\
\widehat{\widehat\Gamma}\arrow[r,phantom,"\supset"]&\unsure{\mathfrak S_3|\mathcal S_3}\times\mathbb\Gamma&
\end{tikzcd}}'''
diagram=diagram_c.replace(r'\unsure{\cup|\Vert}',r'\cup')
id_diagram=change('Left marginal NB, two-level inclusion diagram',diagram_c,
    r'$\mathfrak{S}_3 \times \hat{\hat\Gamma}^{!}$ \quad $\cup$ \quad \textbf{NB} $\hat{\hat\Gamma} \supset \mathfrak{S}_3 \times \boldsymbol{\Gamma}$',diagram,
    'The upper product is over the lower double-hatted Gamma. Between them is a cup with a continuous curved bottom joining two upright sides; it is not two disconnected vertical bars. The lower row has a right-facing superset sign before the product, not an arrow. The distinct vertical and horizontal arrangement is retained; the two ornate S alphabets remain locally uncertain.',5,
    'drawing or diagram',[1,4,6],confidence='medium')
id_marginwords=change('Left margin, first part of the author’s uncertainty statement',
    "--- j'ignore si cette inclusion est une égalité, i.e. si",r"--- j'ignore si elles \uncertain{coïncident}, \ill{} une égalité, i.e.\ si",
    "--- j'ignore si cette inclusion est une égalité, i.e. si",
    'After si, the word has two tall t strokes and an e ending: cette. The next run has the in/cl/u/sion sequence and a tall l. Est begins the next slanting line, followed by une égalité. The first-person j’ignore is clear and preserved.',5,
    'misread word',[2,5],marked='yes')
id_margininclusion=change('Left margin, final inclusion and prose ending',
    r'$\mathbb\Gamma\subset\widehat{\widehat\Gamma}^!$ est une égalité.',
    r'$\hat{\hat\Gamma}^{!} \to \boldsymbol{\Gamma}$ \ill{} \uncertain{est} une égalité',
    r'$\mathbb\Gamma\subset\widehat{\widehat\Gamma}^!$ est une égalité',
    'The doubled-left Gamma is on the left, then a curved left-joined subset sign, then a single-stem double-hatted Gamma with exclamation. There is no arrow between those two groups. Est une égalité follows in the same marginal direction. The final letter/accent is not followed by a separate full stop.',5,
    'misread symbol or index',[1,2,3,5,9],cc=True,marked='yes')
id_elts=change('Symmetric-description paragraph, des élts', 'des élts','','des élts',
    'The first short word has d/e plus a final s stroke. The next abbreviated word has an accent, high l, rising t and trailing s, followed by a separate de. No full stop follows élts. The word crop clips only the upper context of the following E symbol, whose hats were read in the native half.',6,
    'omission',[2,3,8])
id_engendre=change('Role of L_0, before engendré par l_0',r'à $L_0$ engendré par $l_0$',r'à $L_0$ = \uncertain{sous-groupe engendré} par $l_0$',
    r'à $L_0$ engendré par $l_0$',
    'After L_0 the next written word begins directly en-gendré; there are no equals bars and no sous-groupe. Par l_0 continues on the following line.',7,
    'text not on the page',[2,9],marked='yes')
id_map=change('Parenthetical definition of L_0, hatted map letter',r'\hat\kappa_0',r'k_0',map_letter,
    'The base letter has a long upright ascender above two right-hand k-like arms, favoring Latin k. Greek kappa is retained as a local letter-form alternative rather than settled by the expected map name. A distinct circumflex above the letter is present and must not be omitted.',7,
    'misread symbol or index',[1,3],cc=True,confidence='medium')
id_pouretre=change('Above défini, inserted pour être',r'\inserted{pour être}', '',r'\inserted{pour être}',
    'The raised words show a descending p, low ou/r and an accented être. Their curved attachment line runs below the insertion and down toward défini. The earlier est on the preceding main line remains live; it has no cancelling stroke.',7,
    'insertion or placement',[2,3,6])
id_pi20=change('Relation (20), group after membership sign',r'(20)\qquad g_i\in\hat\pi\qquad i=0,1,\infty',
    r'(20)\quad g_i \in \hat\pi \qquad i = 0, 1, \infty',r'(20)\qquad g_i\in\hat\Pi\qquad i=0,1,\infty',
    'The hatted group letter has a level cap and two full legs; the left side is retraced but the right leg extends fully downward. The g loop/descender, i subscript and the complete 0,1,infinity list were independently read.',8,
    'misread symbol or index',[1],cc=True)
id_pour=change('Small word before relation (21)','pour',r'\struck{\ill{}}','pour',
    'The p stem and head, rounded o/u and final r-like exit are visible. There is no separate continuous crossing-out stroke through the whole word; darker touches coincide with letter strokes. Preserve it as live pour.',9,
    'deletion state',[2,5,7],confidence='medium',marked='yes')
rel21_c=r'(21)\qquad u(l_i)=\operatorname{int}(g_i^{\deleted{\unsure{-1}}})l_i^p'
rel21=r'(21)\qquad u(l_i)=\operatorname{int}(g_i^{'+state+r'})l_i^p'
id_exp21=change('Relation (21), complete formula and dark exponent state',rel21_c,
    r'(21)\quad u(l_i) = \operatorname{int}(g_i^{-1})\, l_i^{\,p}',rel21,
    'The raised dark group has a right upright and a thick angular mass with extra small upstrokes at the supposed minus position. Cancellation is favored, but the underlying minus/1 and the live-versus-cancelled state cannot both be certified. Both states are explicit, and the underlying -1 stays doubtful. Parentheses around the int argument are visible here.',9,
    'deletion state',[1,7],confidence='low',marked='yes',
    math='The live inverse and cancelled inverse give different conventions for conjugating elements; this first reader made no algebraic choice between them.')
rel22_c=r'''(22)\qquad(\operatorname{int}(g_\infty^{\deleted{\unsure{-1}}})l_\infty^p)
(\operatorname{int}g_1^{\deleted{\unsure{-1}}}\cdot l_1^p)
(\operatorname{int}(g_0^{\deleted{\unsure{-1}}})l_0^p)=1'''
rel22=rel22_c.replace(r'\deleted{\unsure{-1}}',state)
rel22_h=r'''(22)\quad (\operatorname{int}(g_\infty^{-1})\, l_\infty^{\,p})\,
(\operatorname{int}(g_1^{-1})\, l_1^{\,p})\,
(\operatorname{int}(g_0^{-1})\, l_0^{\,p}) = 1,'''
id_exp22=change('Relation (22), all three dark exponent states',rel22_c,rel22_h,rel22,
    'The infinity factor has a compact w-like dark zigzag; the 1 factor has an extra oblique/upward stroke through a thick horizontal and upright; the 0 factor has a small angular overstroke across the inverse position. These favor cancellations, with varying legibility. None yields a fully plain underlying -1, and each retains a live-state alternative. Every factor, index, power p and outer parenthesis was read on the complete formula crop.',10,
    'deletion state',[1,7],confidence='low',marked='yes')
id_midint=change('Relation (22), middle int expression',r'\operatorname{int}g_1^{\deleted{\unsure{-1}}}\cdot l_1^p',
    r'\operatorname{int}(g_1^{-1})\, l_1^{\,p}',r'\operatorname{int}g_1^{'+state+r'}\cdot l_1^p',
    'Unlike the first and last factors, the middle factor has no opening or closing argument parentheses around g_1. A separated low dot follows the g_1 expression before l_1. Preserve this literal asymmetry.',10,
    'misread symbol or index',[1,3,9])
id_22stop=change('Relation (22), after final 1','=1','= 1,','=1',
    'The final 1 is a single downstroke. No separate comma follows it.',10,
    'text not on the page',[9])
id_underline=change('Last sentence, engendrent emphasis',r'\uline{engendrent}','engendrent',r'\uline{engendrent}',
    'An independent horizontal line lies below the central part of engendrent, separate from the g descender, and marks the word for emphasis.',11,
    'other',[10])
id_pi_end=change('Last sentence, group generated topologically',r'\hat\pi',r'\hat\pi',r'\hat\Pi',
    'The final hatted group letter again has a cap and two complete legs. The right leg has a short curved foot, but it remains full height; it is distinct from the short right tip of Gamma.',11,
    'misread symbol or index',[1],cc=True)
id_footer=change('Physical lower-left page number',r'\mspage{23}','',r'\mspage{23}',
    'The first digit has a curved top, descending diagonal and long base: 2. The second has two right-facing rounded lobes: 3.',12,
    'omission',[3])

decisions=[]
def decision(id_,which,reading,ink,crop,confidence='high',**kw):
    cr=crops[crop]
    d=dict(id=id_,decision=which,reading=reading,ink=ink,crop=cr['file'],box=cr['box'],confidence=confidence)
    d.update(kw)
    return d
S=r'\unsure{\mathfrak S_3|\mathcal S_3}'
decisions.append(decision('M0854','undecided',S,
    'The large group sign has a broad outer sweep, upper return and lower inner curl, with subscript3. It is an ornate S form, but the precise fraktur-versus-calligraphic typographic rendering is not settled locally.',1,'medium'))
decisions.append(decision('M0855','undecided',r'\unsure{qui contient}',
    'The long q descender and short ui run are visible. The next word’s c/on/t strokes favor contient; the cramped ending is not fully distinct. The first reading is narrowed but not certified.',1,'medium'))
decisions.append(decision('M0856','other',r'\dot\tau',
    'A dark isolated dot is above the short bar and curved tau body. The body matches the undotted tau in crop03, making the local overdot explicit.',1))
decisions.append(decision('M0857','alternative',r'\mathbb\Gamma',
    'Two separate left vertical strokes lie under one cap, with a short right tip. The form matches the doubled-left Gamma in the lower row.',3))
decisions.append(decision('M0858','undecided',r'\unsure{0,3}',
    'The lower cluster under the overwritten second Gamma is dense. An oval, comma-like turn and3-like final angular trace support 0,3, but they overlap the prior ornate symbol; the whole right term also retains a doubled-Gamma alternative.',3,'low'))
decisions.append(decision('M0859','undecided',S,
    'The lower intersection sign is an ornate S with a3 below; the broad outer loop and interior curl do not settle the exact typographic alphabet.',3,'medium'))
decisions.append(decision('M0860','undecided',S,
    'The upper marginal product has the same broad ornate letter and clear3 index; fraktur and calligraphic renderings remain alternatives.',5,'medium'))
decisions.append(decision('M0861','first',r'\cup',
    'A continuous curved bottom joins the two uprights of the vertical relation. Two disconnected bars would not account for this bottom stroke.',5))
decisions.append(decision('M0862','undecided',S,
    'The lower product has an ornate S with an especially straight/retraced left entry stroke and a clear3 index. Its alphabet remains unresolved; no additional cancellation is inferred from the entry stroke alone.',5,'medium'))

unlisted=[]
def unlisted_dec(mark,reading,ink,crop,confidence='low'):
    unlisted.append(decision(f'U024-{len(unlisted)+1:02d}','undecided',reading,ink,crop,confidence,source_mark=mark))
unlisted_dec(r'\unsure{\mathfrak S_3}',r'\deleted{\unsure{\mathfrak S_3}}',
    'Pale curving strokes under the thick Gamma replacement support the earlier ornate S_3, but the overwritten lower body/index are not all plain.',3)
for where,crop in [('g_i in (21)',9),('g_infinity in (22)',10),('g_1 in (22)',10),('g_0 in (22)',10)]:
    unlisted_dec(r'\unsure{-1}',state,
        where+': the angular dark mass favors deletion, but crossing/retracing prevents certifying the underlying -1 or excluding a live exponent. Both uncertainties remain explicit.',crop)

doubts=[]
def doubt(place,reading,alternatives,reason,confidence='low'):
    doubts.append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=reason))
for place in ['Opening commutant group sign','Second intersection formula, ornate group sign','Upper marginal product, ornate group sign','Lower marginal product, ornate group sign']:
    doubt(place,S,[r'\mathfrak S_3',r'\mathcal S_3'],
        'Ornate S-shaped ink and the subscript3 are present; the precise font alphabet cannot be inferred from mathematical meaning.', 'medium')
doubt('Opening insertion, words',r'\unsure{qui contient}',['qui contient'],
    'Contient is favored over the discarded centralise alternative, but the compressed last letters remain insufficiently separate.','medium')
doubt('First intersection, overwritten ornate letter',r'\deleted{\unsure{\mathfrak S_3}}',[r'\mathfrak S_3'],
    'The replacement Gamma and low dark strokes obscure part of the prior symbol and its index.')
doubt('First intersection, proposed subscript',r'\unsure{0,3}',['0,3'],
    'The low oval and angular strokes overlap the prior letter, so0,comma,3 are not individually certified.')
doubt('First intersection, complete right replacement term',right_term,[r'\Gamma_{0,3}',r'\mathbb\Gamma'],
    'Thick retracing can resemble a doubled left wall; the lower cluster may be a subscript or part of the overwritten material.')
doubt('Separate cancelled NB',r'\deleted{\uline{\unsure{NB}}}',['NB'],
    'Letter outlines remain under dense diagonal cancellation; retain the word doubt.','medium')
doubt('Hatted map letter in L_0 definition',map_letter,[r'\hat k_0',r'\hat\kappa_0'],
    'The long ascender and two arms favor k, but the local hand does not decisively exclude kappa; the circumflex and0 index are clear.','medium')
for where in ['g_i in (21)','g_infinity in (22)','g_1 in (22)','g_0 in (22)']:
    doubt(where,state,[r'\deleted{\unsure{-1}}',r'\unsure{-1}'],
        'Cancellation is the preferred state because of extra angular/upward strokes. The underlying minus and1 remain occluded, and a live inverse cannot be excluded from ink alone.')

inventory=[]
def inv(kind,position,first,box):
    eid=f'E{len(inventory)+1:02d}'
    inventory.append(dict(element=eid,kind=kind,position=position,first_words_or_objects=first,box=box,
                          sheet_kind='text',hand='his hand',transcribed='yes'))
    return eid
inv('text','Upper main block, four lines','qui contient hat-E comme sous-extension',[270,75,1645,530])
inv('insertion','Above end of second main line','(qui contient dot-tau), words doubtful',[1300,155,1645,325])
inv('display','Upper main, two braced intersection rows','doubled Gamma cap overwritten term = {1,tau}',[585,525,1050,735])
inv('deletion','First intersection, under replacement Gamma','ornate S_3, doubtful',[755,545,850,630])
inv('deletion','Right of intersections','underlined NB, doubtful',[1305,525,1435,635])
inv('margin note','Diagonal left upper margin','underlined NB; j’ignore si cette inclusion',[18,445,600,990])
inv('diagram','Inside left NB, two levels','ornate S_3 times doublehatGamma! above doublehatGamma',[25,445,360,730])
inv('text','Central main paragraph, six physical lines','On veut donner d’abord une description plus symétrique',[245,800,1658,1385])
inv('insertion','Above défini','pour être',[245,1220,490,1340])
inv('display','Relation (19)','p=chi(u) in hat-Z-star',[275,1385,1110,1530])
inv('text','Before (20)','et des',[260,1540,510,1620])
inv('display','Relation (20)','g_i in hat-Pi; i=0,1,infinity',[260,1580,1255,1725])
inv('text','Before (21)','pour, live',[270,1750,440,1840])
inv('display','Relation (21)','u(l_i)=int(g_i...)l_i^p',[245,1775,970,1918])
inv('deletion','Relation (21), raised mark on g_i','doubtful -1; cancellation preferred, live alternative',[770,1780,825,1830])
inv('text','Between (21) and (22)','les données (19), (20) étant liées par la relation',[250,1910,1640,2020])
inv('display','Relation (22)','three ordered int factors =1',[235,2015,1510,2170])
inv('deletion','Relation (22), g_infinity exponent','doubtful -1 and uncertain state',[625,2020,675,2070])
inv('deletion','Relation (22), g_1 exponent','doubtful -1 and uncertain state',[925,2015,975,2070])
inv('deletion','Relation (22), g_0 exponent','doubtful -1 and uncertain state',[1200,2015,1255,2070])
inv('text','Final two lines','et par le fait que les u(l_i) définis par (21); engendrent',[245,2165,1640,2348])
inv('text','Lower-left margin','23',[24,2265,115,2348])

second=[]
def sec(kind,box,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,coords=box,reading=reading))
opening=tex[tex.index('qui contient'):tex.index('\n\\[\n\\left')]
intersections=r'''\[
\left\{\begin{aligned}
\mathbb\Gamma\cap\deleted{\unsure{\mathfrak S_3}}'''+right_term+r'''&=\{1,\tau\}\\
\mathbb\Gamma\cap\unsure{\mathfrak S_3|\mathcal S_3}&=\{1\}
\end{aligned}\right.
\]'''
margin=r"\margin{\uline{NB}"+'\n'+diagram+'\n'+r"--- j'ignore si cette inclusion est une égalité, i.e. si $\mathbb\Gamma\subset\widehat{\widehat\Gamma}^!$ est une égalité.}"
margin=margin.replace('égalité.}','égalité}')
central=tex[tex.index('On veut donner'):tex.index('\n\\[\n(19)')]
ending=r'et par le fait que les $u(l_i)$ définis par (21) \uline{engendrent} $\hat\Pi$ topologiquement. Pour $u$ fixé, $p$'
sec('Complete selected opening block, inserted parenthesis, all group formulas and3 index',[270,75,1645,530],opening)
sec('Both complete intersection formulas, all doubts, replacement/deletion and numeric indices',crops[3]['box'],intersections)
sec('Complete separate cancelled and underlined marginal inscription',crops[4]['box'],nb_final)
sec('Complete selected marginal note and two-level diagram, authorial j’ignore and all numeric/group signs',crops[5]['box'],margin)
sec('Complete selected central paragraph, lexical disagreements, hatted map formula, L_0 indices and insertion',[245,800,1658,1385],central)
sec('Complete numbered relation (19), all formula signs and handwritten numerals',[275,1385,1110,1530],r'\[(19)\qquad p=\chi(u)\in\hat{\mathbb Z}^{*}\]')
sec('Complete et des and relation (20), all indices and local Pi form',crops[8]['box'],r'et des \[(20)\qquad g_i\in\hat\Pi\qquad i=0,1,\infty\]')
sec('Live pour and entire relation (21), doubtful inverse signs and both exponent states',crops[9]['box'],'pour\n'+r'\['+rel21+r'\]')
sec('Complete agreed prose line with both handwritten relation references',[250,1910,1640,2020],'les données (19), (20) étant liées par la relation')
sec('Entire relation (22), all three uncertain exponent states, literal parentheses and dot',crops[10]['box'],r'\['+rel22+r'\]')
sec('Complete final two lines, handwritten(21), underline and final Pi',crops[11]['box'],ending)
sec('Handwritten physical footer number',crops[12]['box'],r'\mspage{23}')

coverage=[]
def cover(n,ids=(),why=''):
    if isinstance(ids,str):ids=(ids,)
    d=dict(row=n,status='substantive' if ids else 'macro/editorial')
    if ids:
        d['change_id']=ids[0]
        if len(ids)>1:d['related_change_ids']=list(ids[1:])
    if why:d['explanation']=why
    coverage.append(d)
cover(1,why='Editorial scan identifier; the physical footer23 is independently transcribed.')
cover(2,why='C alternative-font apparatus for the ornate S. M0854 remains undecided; this is not a certainty-only changes row.')
cover(3,(id_ins,id_tau))
cover(4,id_leftgamma,'Tokenization of C’s alternatives overlaps the actual first term; the double left stem resolves the second choice.')
cover(5,id_rightgamma)
cover(6,(id_rightgamma,id_set_stop),'Includes C font alternatives and H editorial discussion. Substantive replacement/deletion and the supplied stop are covered separately.')
cover(7,why='H editorial explanation of uncertainty, with C alternative-font tokens. Both read the second-row equality {1}; no equality is omitted.')
cover(8,(id_cancelnb,id_diagram),'H editorial rature notice does not transcribe the separate cancelled NB; the marginal layout is also represented differently.')
cover(9,id_diagram,'TikZ syntax carries the real vertical relation; no ordinary directed arrow is inferred from the macro.')
cover(10,id_diagram,'Cup shape and NB placement are retained; the C alternative bars are rejected on the joined lower curve.')
cover(11,id_diagram,'TikZ phantom-arrow syntax represents a horizontal superset relation, not an arrowhead.')
cover(12,why='Literal quote/TikZ closing syntax and C font alternative apparatus. The complete diagram is covered by '+id_diagram+'.')
cover(13,why='TikZ closing environment/display tokens only.')
cover(14,id_marginwords)
cover(15,id_margininclusion)
cover(16,id_margininclusion,'H commentary about later use is editorial; the literal final phrase and unsupported C stop are handled at this locus.')
cover(17,id_elts)
cover(18,id_engendre)
cover(19,id_map)
cover(20,id_pouretre)
cover(21,id_pour)
cover(22,why='H thin-space macro between factors, tokenized as comma; exponent state is separately covered by '+id_exp21+'.')
cover(23,why='H thin-space macro before p; no handwritten comma.')
cover(24,id_exp21,'H’s prose claim that inverse signs were later additions is editorial; the actual ink-state disagreement is retained explicitly.')
cover(25,why='H thin-space macro in first factor of(22); exponent state covered by '+id_exp22+'.')
cover(26,why='H thin-space macro before first p.')
cover(27,why='H thin-space macro between the first and second factors.')
cover(28,id_midint)
cover(29,id_midint,'Argument close and spacing tokens; the missing argument parentheses and actual separated dot are substantive.')
cover(30,why='H thin-space macro before middle p.')
cover(31,why='H thin-space macro between the second and third factors.')
cover(32,why='H thin-space macro before the last l_0 factor.')
cover(33,why='H thin-space macro before the last p.')
cover(34,id_22stop)
cover(35,id_footer)

report=dict(scan=24,reader='reader_b',lines_read=30,
    layout='Upright subject notes continuing mid-sentence, with a small inserted parenthesis above the second line; two braced intersection formulas; a separate cancelled NB at right; an oblique left NB containing a two-level inclusion diagram and three prose/formula lines; a central pour être insertion; relations(19)–(22); final underlined engendrent; footer23, with no upper manuscript number.',
    changes=changes,decisions=decisions,unlisted_decisions=unlisted,doubts=doubts,inventory=inventory,second_boxes=second,
    notation=[
        'The doubled-left Gamma has two left strokes, a top cap and only a short right downturned tip. The three distinct hatted fundamental-group signs have two full legs under a cap and are read locally as capital Pi: opening extension sentence, relation(20), and final engendrent sentence.',
        'Four ornate S_3 occurrences retain fraktur/calligraphic alternatives. The lower marginal one has a straighter or retraced left entry; this alone does not establish an extra cancelled letter.',
        'The final symbol in the opening insertion is dot-tau; its body is comparable with the undotted tau in the first intersection’s right side. The dot is independently visible.',
        'The vertical marginal relation is a cup with a joined bottom; the horizontal marginal relation is superset. In the prose the doubled Gamma is on the left of subset and the double-hatted Gamma with exclamation is on the right.',
        'The hatted map in the L_0 parenthesis is k-like with a long ascender; k is favored, kappa is retained locally, and the visible circumflex is preserved.',
        'Each of the four tiny inverse-position marks has a preferred cancelled state but retains a live-state alternative and uncertainty about the underlying -1. The middle int g_1 in(22) is written without argument parentheses and with a following dot.'
    ],
    hand=[
        'All inscriptions are in his hand. The marginal note is oblique; no identifiable other hand is present. Darker strokes occur in retracing and possible cancellations, but ink darkness alone does not date them.',
        'Doubled-left Gamma and hatted Pi are distinguishable by the right-hand stroke length in this page’s inspected occurrences. The heavily overwritten second term of the first intersection does not permit the same certainty.',
        'The small opening insertion compresses several low letters; the word contient is favored but remains doubtful. Its dot-tau has a clearly separate dot.',
        'Local cancellation can appear as compact angular dark masses with extra upstrokes rather than a long strike. These shapes favor, but do not prove, the cancelled interpretation of all four inverse-position marks.',
        'The author’s engendrent underline is a separate line beneath the word, unlike the nearby g descender. The cancelled NB is legible in outline but not fully plain under crossing ink.'
    ],
    abbreviations=[
        dict(form='NB',expansion='nota bene',place='Live left note and cancelled right inscription'),
        dict(form='élts',expansion='éléments',place='Symmetric-description paragraph; no abbreviation stop is supplied'),
        dict(form='i.e.',expansion='id est',place='Left marginal uncertainty statement'),
        dict(form='int',expansion='inner-conjugation notation',place='Relations(21) and(22), with local argument parentheses preserved')
    ],
    notes=[
        'The sheet continues a sentence about an extension containing a hatted E. It names a doubled-Gamma commutant and a corresponding E extension by hatted Pi, then asserts two intersection formulas. The right term in the first formula is overwritten and remains doubtful; no correction is supplied from the expected centralizer statement.',
        'The marginal NB places one group product over a larger double-hatted Gamma and gives a second product on the lower row. The author explicitly writes j’ignore si cette inclusion est une égalité and restates the issue using doubled Gamma subset double-hatted Gamma with exclamation. The authorial ignorance statement is preserved verbatim in substance and not converted to an assertion.',
        'The main continuation seeks a more symmetric description, avoiding a special role for L_0. It gives a multiplicateur p=chi(u) in the units of the hatted integers, then three conjugating elements g_i and their action formulas. The product relation(22) and topological-generation clause are the author’s conditions. This first reader did not prove the claims or calculate the relations.',
        'The insertion pour être is attached before défini, while the preceding est remains live. The awkward resulting wording is preserved. The middle factor of(22) lacks the argument parentheses present in the other two factors; its separated dot is transcribed. No normalization is made to the differing local syntax.',
        'The four inverse-position marks are darker, compact angular groups. C calls them cancellations and H calls them later additions. This reader and the root reader favor cancellation from extra zigzag/upward strokes, while retaining both states and the underlying -1 doubts. Any root centralizer/proof discussion is separate; no mathematical check is claimed here.',
        'The physical page has footer23 and no visible top page number or date. It ends at Pour u fixé, p. No continuation from another scan has been read or supplied. All thirty counted line units include the insertion lines, two-level diagram relation, separate cancelled NB and footer.',
        'The whole page and two supplied native halves were each viewed once. Twelve saved crops cover the mandatory lexical disagreements, resolved C marks and open loci; root has reviewed all twelve. Crop06 targets des élts de and clips the upper context of the following E; its hats were visible in the native half and the complete formula is included in the larger second-reading selection. No OCR, external research, TeX compilation or additional agents were used.',
        'The initial scan024 differences packet erroneously included trailing rows for025–027 because of TSV quote handling. Those rows were exposed in a packet read, were not used for this reading, and no corresponding witnesses, images or reports were opened. Root replaced the packet with exactly35 target rows; all coverage here uses that corrected target-only file. This reader is excluded from blind reading025–027, as documented by root.'
    ],
    check_events=[],diff_coverage=coverage,crop_manifest=meta)

def macros(s,name):
    out=[]
    for m in re.finditer(r'\\'+name+r'\{',s):
        k,d=m.end(),1
        while d and k<len(s):
            if s[k] in '{}':
                p,b=k-1,0
                while p>=0 and s[p]=='\\':b+=1;p-=1
                if b%2==0:d+=1 if s[k]=='{' else -1
            k+=1
        assert d==0
        out.append(s[m.start():k])
    return out
report['c_markup_audit']=dict(deleted_spans=6,inserted_spans=2,indexed_marks=9,unlisted_unsure_occurrences=5,
    all_accounted_in_inventory=True,all_selected_for_second_reading=True)
for name,mapping in [
    ('deleted',[('E04','B02'),('E05','B03'),('E15','B08'),('E18','B10'),('E19','B10'),('E20','B10')]),
    ('inserted',[('E02','B01'),('E09','B05')])]:
    original=macros(C,name)
    assert len(original)==len(mapping)
    report['c_markup_audit'][name+'_details']=[dict(occurrence=n,source=s,inventory_element=e,second_box=b)
        for n,(s,(e,b)) in enumerate(zip(original,mapping),1)]

rows=list(csv.DictReader((PACKET/'differences.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
assert len(rows)==35 and all(x['page']=='145_scan024' for x in rows)
assert len(coverage)==35
(OUT/'145_scan024.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(tex=str(OUT/'145_scan024.tex'),report=str(OUT/'145_scan024.json'),
    crops=len(meta),changes=len(changes),indexed_decisions=len(decisions),unlisted_decisions=len(unlisted),
    doubts=len(doubts),inventory=len(inventory),second_boxes=len(second),diff_rows=len(coverage)),indent=2))
