from pathlib import Path
import json,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];p='149_scan003'
assert hashlib.sha256((R/'second'/f'{p}_second.tsv').read_bytes()).hexdigest()=='76042c5e6b22b2650d0a47f4bc8ea5171c0d77e1ece8813d32a3823aa7fa4564'
C={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
E={
'B01':'The large numbered heading and underline agree. The small high right mark has a short oblique entry and dark descending stroke without a secure base; 1 remains leading, with lambda admitted as an alternative. The page-number versus margin wrapper is not a different ink reading.',
'B03':'The live K- is raised and connected to the first automorphismes by a leader. The separate K- before the next automorphismes is cancelled; its stem and branches are partly merged with the strike, so K remains a doubtful candidate rather than being resolved. The K bars, Gal and E agree. The field-extension separator is nearly upright here, while the corresponding sign in the lower reconstruction clause is visibly oblique. These are the same local separator habit, retained with the existing slash convention; the second mid macro does not identify a different mathematical operation.',
'B04':'The abbreviation has a descending p and a separately raised crossed t, so p with superscript t replaces baseline pt. The raised de B_K attaches after it by a curved leader. The bar over the cancelled K remains visible. The detached mark after alg is horizontally extended and still admits both abbreviation point and short dash; the independent full stop does not resolve it. Dash length is typographic. The same upright-to-oblique field separator is retained consistently with the other local occurrences.',
'B06':'The crop starts with des because it includes the previous phrase boundary. The accepted paragraph already has topos des before this box; no second des is inserted. Ensembles has a clear tall initial E. The complete indexed E and its final point agree; slash versus mid is the same local field-separator encoding assessed across the five occurrences.'}
V={'B01':C['B01']['first'].replace(r'\unsure{1}',r'\unsure{1|$\lambda$}'),'B03':C['B03']['first'].replace(r'\deleted{$K$-}',r'\deleted{$\unsure{K}$-}'),'B04':C['B04']['first'].replace('du pt ',r'du $p^t$ ')}
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
for b,v in V.items():assert C[b]['first'] in s;s=s.replace(C[b]['first'],v)
pp.write_text(s)
D={b:dict(choice='keep_first',viewed=True,evidence=e) for b,e in E.items()}
for b,v in V.items():D[b].update(choice='reading',reading=v)
(R/'second'/f'{p}_main_decisions.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
r['doubts'][0].update(reading=r'\mspage{\unsure{1|$\lambda$}}',alternatives=r'1; \lambda',reason=E['B01'])
r['doubts'].append(dict(place='Cancelled K- before the second automorphismes',reading=r'\deleted{$\unsure{K}$-}',alternatives='K remains the only securely suggested letter, with its full contour obscured',confidence='low',reason='The crossing strokes overlap the stem and branching diagonals, so not every part of the cancelled letter can be isolated.'))
r['changes'].append(dict(id=p+'-07',place='Abbreviation after the second automorphismes: du pt',c='pt',h='pt',final=r'$p^t$',diff_c=True,diff_h=True,kind='misread symbol or index',error_kind='Symbols and indices',evidence='The p has its descender on the baseline; the following crossed t is written distinctly above and to the right, with its bottom near the upper half of p. The raised t is retained as an abbreviation superscript, without expanding the word.',crop=f'crops/{p}_second_B04.png',box=[280,970,1665,1560],confidence='high',marked_in_h=False,consequential=False))
for x in r['abbreviations']:
 if x['form']=='pt':x['form']=r'$p^t$'
r['notation'].append(dict(sign=r'\bar K/K',meaning_or_form='The field-extension separator ranges from almost upright to visibly oblique. Slash is retained as one transcription convention for this same local sign; it is not read as a new conditional relation.',places='149_scan003 Gal argument, following E index, associated closure, both reconstruction E indices',universality='All five were checked in the canonical second boxes and one additional complete reconstruction-clause crop.',witness_errors='The blind reader used mid for four instances; comparison of the complete local series does not establish a material symbol difference.'))
r['notes'].append(dict(id=p+'-N-audit',text='The independent reading was frozen before comparison; four unequal boxes were adjudicated. The abbreviation p with raised t replaces baseline pt. The high page annotation and cancelled K acquire explicit alternatives or uncertainty without extra witness-error counts. The five field-extension separators were compared locally: near-upright and oblique forms are retained under one slash convention. The extra des at the beginning of the second B06 reading is already present immediately before the first box fragment and is not duplicated.'))
dsfile=R/'second'/f'{p}_main_audit_details.json';ds=json.loads(dsfile.read_text())
for x in ds:x['viewed']=True
dsfile.write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
extra=[f'crops/{p}_second_B05.png',f'crops/{p}_reconstitue_full.png']+[x['path'] for x in ds]
r['second_main_review']=dict(viewed_boxes=list(E),reviewed_at=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),decisions=f'second/{p}_main_decisions.json',additional_existing_crops_viewed=extra)
r['main_reader_crops']=list(dict.fromkeys(r.get('main_reader_crops',[])+extra))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
