"""Apply the main reader's directly viewed final-page adjudication.

Frozen first and blind second TSVs are deliberately not edited.
"""
from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

R = Path(__file__).resolve().parents[1]
p = '149_scan004'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest() == 'd58353cacae09be7f81c74646fcda4b4c3b04b3e6642e8f2bf2b545ad1ba6fb9'
C = {x['box']: x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
E = {
    'B01': 'The Spec shaft has a blunt, slightly downturned terminal without a separately drawn chevron or second arm. The dash is retained; the mathematical map context does not supply an arrowhead.',
    'B02': 'The first displayed shaft is likewise blunt. The target superscript has one dark descending core and overworked angular returns, without two independently recoverable parallel stems for a secure sharp or natural. Cancelled-prime/live-star alternatives remain; no layer order is inferred from the repeated shape.',
    'B03': 'A detached right-pointing curved head is visible beyond this shaft, so the arrow is retained. The label remains 2/1 because its hooked top and short lower stroke do not independently settle the digit. The target raised cluster remains cancelled-prime/live-star rather than a resolved sharp or natural.',
    'B04': 'The article consists of low joined humps and a long terminal; un remains first, with une admitted as a shape alternative. The long strike crosses cloture, whose final letters cannot all be isolated and therefore acquire doubt. The point abbreviation has a descending p and a distinctly raised crossed t followed by a separate point. The crossed closing parenthesis and following low ou run remain. Dark sep. overlies lighter tall-loop and lower-loop traces: a prior alg. overwritten by sep. is possible but not proved. Both that layer alternative and plain retraced sep. are recorded, with plain sep. first. The raised barred K-prime and its V-like insertion leader remain unchanged.',
    'B05': 'The opening is en definit: the tall looped f and following i/t strokes rule out on en fait. In the parenthesis, the compact a, short i stroke, low n, terminal s/i group and detached i dot support ainsi rather than associe. The superscripts retain their unresolved crossed clusters. Raised alg has no independent terminal point. The baseline abbreviation has dark sep strokes and lighter tall-loop/descender traces; live sep, cancelled sep and cancelled alg remain alternatives because neither complete layer nor a through-strike is separable.',
    'B06': 'The first-row abbreviation has a descending p followed by one raised crossed t with a curved lower return; there is no independent plural s or point. It is p with superscript t. The e of interprete has no securely separable accent in this faint group, so accented/unaccented forms remain alternatives. De groupes is retained. Spacing within p.ex. is not a material reading difference.',
    'B07': 'The shaft has a single blunt downturned end, without the detached head seen in B03. Both field separators are nearly upright versions of the oblique separator already compared on 149:003; slash remains the common encoding. Both target raised clusters retain their existing uncertain state. The label has a joined rising-and-falling hump and a separate right parenthesis: 3 remains provisional, n is admitted, and the opening parenthesis remains uncertain. Number order does not resolve it.',
    'B09': 'The left upright can be a numeral 1 or an unlabelled vertical mark; it remains a margin annotation. The prose is main text, not an entire marginal note. The final word has an open e, crossed x-like turn, tall t and low e/n/s run; no descending g supports categorie. Extension remains the candidate, now explicitly doubtful because the last pale strokes reach the physical scan edge. No continuation is supplied. The E index keeps the same local field separator convention.'
}
V = {}
V['B04'] = C['B04']['first'].replace("qu'un", r"qu'\unsure{un|une}").replace(r'\deleted{clôture}',r'\deleted{\unsure{clôture}}').replace('pt. de',r'$p^t$. de').replace('clôture sép.',r'clôture \unsure{sép.|\deleted{alg.}\inserted{sép.}}')
V['B05'] = C['B05']['first'].replace('(associé,','(ainsi,').replace(r'\unsure{sép|\deleted{sép}}',r'\unsure{sép|\deleted{sép}|\deleted{alg}}')
V['B06'] = C['B06']['first'].replace('deux pts ',r'deux $p^t$ ').replace("s'interprète",r"s'interpr\unsure{è|e}te")
V['B07'] = C['B07']['first'].replace(r'\unsure{(3)|3)}',r'\unsure{(3)|3)|(n)}')
V['B09'] = C['B09']['first'].replace(r'\unsure{1}',r'\unsure{1|$\vert$}').replace('sous-extension',r'sous-\unsure{extension}')
pp = R/'pages'/f'{p}.tex'
s = pp.read_text()
for b,v in V.items():
    assert C[b]['first'] in s, b
    s = s.replace(C[b]['first'],v)
pp.write_text(s)
D = {b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
for b,v in V.items(): D[b].update(choice='reading',reading=v)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')

rp = R/'records'/f'{p}.json'
r = json.loads(rp.read_text())
changes = {x['id']:x for x in r['changes']}
changes[p+'-08'].update(final='ainsi',diff_c=True,diff_h=False,confidence='medium',evidence='The enlarged parenthesis has a compact a followed by a short i stroke, a low n and a terminal s/i group with a detached dot. This supports ainsi. A complete s-s-o-c-i-é sequence is not present; the earlier interpretation of the final dot as an accent is withdrawn.',crop=f'crops/{p}_second_B05_parenthesis.png',box=[1295,1085,1620,1175])
for n in (11,12):
    changes[p+f'-{n:02}']['final'] = r'\unsure{sép|\deleted{sép}|\deleted{alg}}'
changes[p+'-11'].update(confidence='low',evidence='The dark s/e/p contours coexist with lighter tall-loop and looped-descender traces, allowing an older alg reading. No independent complete cancellation stroke or secure layer order can be isolated. Live sép, cancelled sép and cancelled alg remain explicit alternatives; no alternative has a terminal point.')
changes[p+'-19']['final'] = r'\margin{\unsure{1|$\vert$}}'
for num,place,c,h,final,b,box,evidence in [
    (21,'Object description, point abbreviation','pt.','pt.',r'$p^t$.','B04',[275,725,1665,1080],'The p descends from the baseline; the separate crossed t is raised to its upper right. A distinct point follows the t. Both witnesses flatten the raised abbreviation ending.'),
    (22,'Corresponding-points sentence, point abbreviation','pts','pts',r'$p^t$','B06',[280,1335,1630,1665],'The p has a long descender and the single raised t has a clear crossbar with a curved lower return. There is no separate plural s after it and no following point. The visible abbreviation is retained even after deux.')
]:
    r['changes'].append(dict(id=p+f'-{num:02}',place=place,c=c,h=h,final=final,diff_c=True,diff_h=True,kind='misread symbol or index',error_kind='Symbols and indices',evidence=evidence,crop=f'crops/{p}_second_{b}.png',box=box,confidence='high',marked_in_h=False,consequential=False))

for d in r['decisions']:
    if d['id']=='M0956':d['reading']=r'\margin{\unsure{1|$\vert$}}'
for d in r['doubts']:
    d['reading'] = d['reading'].replace('(associé,','(ainsi,').replace(r'\unsure{sép|\deleted{sép}}',r'\unsure{sép|\deleted{sép}|\deleted{alg}}').replace(r'\unsure{(3)|3)}',r'\unsure{(3)|3)|(n)}').replace(r'\margin{\unsure{1}}',r'\margin{\unsure{1|$\vert$}}')
    if d['place']=='Second sép in the closure definition':
        d.update(alternatives='Live sép; cancelled sép; cancelled alg. None has a terminal point.',confidence='low',reason=E['B05'])
    if d['place']=='Display (3), opening parenthesis of label':
        d.update(place='Display (3), label and opening parenthesis',alternatives='(3); 3); (n). The right parenthesis is separate and clear.',confidence='low',reason=E['B07'])
new_doubts = [
    ('Article before the cancelled clôture',r"qu'\unsure{un|une}",'un; une','medium','B04'),
    ('Cancelled clôture',r'\deleted{\unsure{clôture}}','clôture is suggested; the final letters are obscured by the strike','low','B04'),
    ('First sép., possible earlier overwritten abbreviation',r'\unsure{sép.|\deleted{alg.}\inserted{sép.}}','Retraced live sép.; older alg. replaced by sép.','low','B04'),
    ('Accent in interprète',r"s'interpr\unsure{è|e}te",'è; e','medium','B06'),
    ('Final word at the physical right scan edge',r'sous-\unsure{extension}','extension; final pale strokes incompletely separable','low','B09')
]
for place,reading,alternatives,confidence,b in new_doubts:
    r['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence=confidence,reason=E[b]+' This added uncertainty is not a separate material witness discrepancy.'))

for x in r['inventory']:
    f=x['first_words_or_objects']
    f=f.replace("qu'un",r"qu'\unsure{un|une}").replace(r'\deleted{clôture}',r'\deleted{\unsure{clôture}}')
    f=f.replace('pt. de',r'$p^t$. de').replace('deux pts ',r'deux $p^t$ ').replace("s'interprète",r"s'interpr\unsure{è|e}te")
    f=f.replace('(associé,','(ainsi,').replace(r'\unsure{sép|\deleted{sép}}',r'\unsure{sép|\deleted{sép}|\deleted{alg}}')
    f=f.replace(r'\unsure{(3)|3)}',r'\unsure{(3)|3)|(n)}').replace(r'\margin{\unsure{1}}',r'\margin{\unsure{1|$\vert$}}').replace('sous-extension',r'sous-\unsure{extension}')
    x['first_words_or_objects']=f
    if x['element']=='E16':x['position']='Second abbreviation: retraced sép and possible cancelled sép/alg; state unresolved'
ix=next(i for i,x in enumerate(r['inventory']) if x['element']=='E11')
r['inventory'][ix:ix]=[
    dict(element='E10a',sheet_kind='text',hand='his hand',kind='deletion',position='Possible old alg. beneath the first sép.; layer status remains doubtful',first_words_or_objects=r'\unsure{sép.|\deleted{alg.}\inserted{sép.}}',transcribed='yes'),
    dict(element='E10b',sheet_kind='text',hand='his hand',kind='insertion',position='Possible sép. replacement over earlier alg.; alternative to retracing only',first_words_or_objects=r'\unsure{sép.|\deleted{alg.}\inserted{sép.}}',transcribed='yes')
]
for n in r['notes']:
    if n['id']==p+'-N04':n['text']='The final paragraph begins to identify the image of (3) as a closed subgroup corresponding to a subextension. The candidate extension is now explicitly doubtful at the physical right edge: e, a crossed x-like turn, tall t and low e/n/s contours are visible, but the final pale strokes are not fully separable. No descending g supports the independent categorie candidate. No continuation or terminal period is supplied. The literal E index there is K-bar/K without the six overworked marks found above.'
    if n['id']==p+'-N06':n['text']='The ink gives capital Topos in the opening, de groupes, and an explicit detached accent in réconstituer. The quoted phrase has paired elevated quotation strokes. Raised alg has no separate terminal point. The first sép. has a point but also lighter possible old alg. traces under the darker letters; the layer alternative remains doubtful. The second baseline abbreviation has no point and retains live sép/cancelled sép/cancelled alg alternatives. The accent in interprète remains uncertain.'
    if n['id']==p+'-N07':n['text']='All handwritten numbering was checked. The first display label is (1); the second remains (2|1); the third has a joined hump-shaped character with a separate right parenthesis, retained as (3)|3)|(n) without resolving by numeric sequence. The final prose reference reads (3). The separate dark margin upright remains 1/vertical-stroke doubtful. The lower pale folio is 3, with writer attribution left uncertain.'
r['notes'].append(dict(id=p+'-N-audit',text='All eight unequal boxes of the ten-box frozen independent reading were adjudicated directly on their canonical crops. Eight existing helper crops were also viewed. The material reading changes are ainsi in the parenthesis and p with raised t in both point abbreviations; the latter has no written plural s in the deux sentence. Added uncertainty in the article, cancelled word, possible revision layers, accent, label and final edge word is recorded without additional material-change counts. Blunt map strokes, the one detached arrowhead and the unresolved six target clusters retain their local ink distinctions. Field-extension separators agree with the local near-upright/slanted habit on 149:003, without imposing a new operation.'))
for x in r['abbreviations']:
    if x['form']=='pt.':x['form']=r'$p^t$.'
    if x['form']=='pts':x['form']=r'$p^t$'
r['notation'].append(dict(sign=r'$p^t$. / $p^t$',meaning_or_form='A descending p with a distinctly raised crossed t; the lower return belongs to t, not an additional s.',places='149_scan004 object description and corresponding-points sentence; compare 149_scan003',universality='Each visible occurrence checked individually. A point is present after the first on 004 and absent after the second.',witness_errors='Both witnesses flatten the first to pt. and read an added s in pts at the second.'))
helpers=['B04_article','B04_oldword','B05_parenthesis','B06_points','B04_insertion','B05_replacement','B09_end','B07_number']
extra=[f'crops/{p}_second_{n}.png' for n in helpers]
r['second_main_review']=dict(viewed_boxes=list(E),reviewed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=f'second/{p}_main_decisions.json',additional_existing_crops_viewed=extra)
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
