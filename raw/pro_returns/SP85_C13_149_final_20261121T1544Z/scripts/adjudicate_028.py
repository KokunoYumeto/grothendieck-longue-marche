"""Main-reader decisions from the fourteen scan028 blind crops."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];p='149_scan028'
rp=R/'records'/f'{p}.json';r=json.loads(rp.read_text())
pp=R/'pages'/f'{p}.tex';s=pp.read_text()
cmp={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
f={b:x['first'] for b,x in cmp.items()}
repls=[
 (r'\deleted{est} a un',r'\deleted{est} \unsure{a|-} un'),
 (r'réduit à $(1)$, \deleted{\unsure{$X$ normal}} \deleted{\unsure{on}}',r'réduit à $(1)$ ; \deleted{\unsure{$X$ normal|$X$ admet}} \deleted{\unsure{on|un}}'),
 (r'\unsure{à un point}.',r'\unsure{à un point},'),
 (r'$\pi_1(U)\longrightarrow\pi_1(X)$ surj.',r'$\pi_1(U)\unsure{\longrightarrow|-}\pi_1(X)$ \unsure{surj.|surj}'),
 (r"d'éléments d'ordre fini! Sinon, se borner dans le cor. au cas de fibres",r"\unsure{d'éléments|d'élts} d'ordre fini! Sinon, se borner dans le cor. \unsure{au|aux} cas \unsure{de|des} fibres"),
]
for old,new in repls:
 assert old in s,old;s=s.replace(old,new,1)
 for b in f:f[b]=f[b].replace(old,new)
old=r"le cas c) est un cas particulier de d); \deleted{\unsure{des variétés|de même} $X$ \unsure{aurait}}"
new=r"le cas c) est un \deleted{\unsure{des variétés|de même} $X$ \unsure{aurait}} cas particulier de d);"
assert old in s;s=s.replace(old,new,1);f['B10']=f['B10'].replace(old,new)
pp.write_text(s)
r['rows'][1]['final']=r'\deleted{est} \unsure{a|-} un'
r['rows'][1]['scan_shows']+=' Blind B01: the very flat replacement a is no longer treated as certain; a short dash is also possible.'
r['rows'][11]['final']=r'\deleted{\unsure{$X$ normal|$X$ admet}}'
r['rows'][11]['scan_shows']+=' Blind B06: the obscured tall/low sequence also permits admet; the cancellation does not settle either word.'
r['rows'][12]['final']=r'\deleted{\unsure{on|un}}'
r['rows'][12]['scan_shows']+=' Blind B06: the first low curve can be o or u; retain both.'
r['rows'][21]['place']='cancelled interlinear phrase between un and cas particulier'
r['rows'][21]['scan_shows']+=' Blind B10 fixes its placement: it lies immediately below le cas c) est un and above cas particulier de d), with no leader taking it past d). Place the cancelled fragment after un; retain its unresolved words.'
r['rows'][21]['final']=r'un \deleted{\unsure{des variétés|de même} $X$ \unsure{aurait}} cas particulier de d)'
r['rows'][24]['final']=r'\unsure{surj.|surj}\unsure{)),|))|),}'
r['rows'][24]['scan_shows']+=' Blind B12: the possible stop touches the descending/closing curves and is also left doubtful.'
r['rows'][29]['final']=r['rows'][29]['final'].replace(repls[4][0],repls[4][1])
r['rows'][29]['scan_shows']+=' Blind B13: the compressed éléments/élts sequence and the tiny endings of au(x) and de(s) remain locally doubtful; n’a pas is still resolved.'
def row(place,C,H,final,ink,b):
 return dict(place=place,C=C,H=H,final=final,against_C=True,against_H=True,kind='text not on the page',error_category='Other',scan_shows=ink,crop=f'crops/{p}_second_{b}.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']==b),confidence='medium',marked_in_H=False,consequential=False)
r['rows'].append(row('d) punctuation after reduced to (1)',',',',',';','There are two separate dark marks at the same horizontal position: an upper mark at text height and a descending comma below. Retain a semicolon before the crossed X phrase.','B06'))
r['rows'].append(row('boxed marginal note, terminal punctuation','.','(not transcribed)',',','A separate curved hook descends below the final point outline; it is a comma, not the supplied full stop. This does not resolve any crossed word.','B09'))
for d in r['doubts']:
 if d['place']=='d) cancelled X normal and lower fragment':d.update(reading=r'\unsure{$X$ normal|$X$ admet}; \unsure{on|un}',alternatives='X normal / X admet; on / un')
 if d['place']=='final punctuation':d['reading']=r'\unsure{surj.|surj}\unsure{)),|))|),}'
for place,reading,alts,why in [
 ('opening replacement before un','a','-','The small pale form is almost horizontal; a closed bowl is not secure.'),
 ('last-line map connector',r'\longrightarrow','-','The shaft ends in a small dark wedge that may be a head or accumulated endpoint ink; both groups and U were re-read together.'),
 ('asterisk note, noun before d’ordre fini','éléments','élts','The compressed medial strokes do not securely establish the full word against the abbreviation.'),
 ('asterisk note, before cas','au','aux','The short terminal return can hide or imitate x.'),
 ('asterisk note, before fibres','de','des','The shallow ending may include a compressed s.')]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=why))
r['notes']+='\n\n[Blind audit] All fourteen boxes were viewed. The d) clause has a two-part semicolon after (1); the boxed note ends with a descending comma. The cancelled phrase des variétés / de même X aurait is placed after un and before cas particulier, following its interlinear position. The flat a in the crossed opening, X normal / X admet, on / un, the last map endpoint, the surj stop, and three compressed marginal endings remain doubtful. The blind omission of f=g is not adopted: its f descender, equality bars and g body survive at the upper box edge and were already seen in the original page. The other added contexts and wrapper differences do not change the page.'
r['hand_log'].append(dict(habit='Two-part punctuation can be mistaken for one comma',places='149_scan028, after (1) in d), blind B06',scope='An upper mark and lower comma are separate at this occurrence.',witness_errors='Both witnesses give a comma; the blind crop supports a semicolon.'))
r['abbreviations'].append(dict(form='éléments / élts (unresolved)',expansion='éléments'))
inks={
'B01':'The raised ending has a low n/e sequence, without a clear terminal s; retain anabélienne. Donc has its low d-on-c outline clear between cancellations. The very flat a before un could be a dash, now marked locally. Son, the separately cancelled est, centre trivial and the absence of a stop after Ceci posé remain.',
'B02':'The upper edge still shows the f descender, both short equality bars and the g body above du; the original page had already shown the complete raised f=g. The blind omission does not erase this insertion. Underlined Corollaire 2 and the title’s lack of a final stop agree.',
'B03':'The crossed item letter has a tall b stem and lower bowl followed by a closing curve; retain b) and its surviving comma. The old verb remains too crossed to settle sera/est, and reste is not securely readable. At the right, a low initial au cluster precedes a tall l and ieu-like trace under the strike, so keep cancelled au lieu rather than les. The raised est and absence of a comma after si stand.',
'B04':'The cancellation runs continuously across de supposer, the looped f, low ou, the descending g and dominant(s); none is a live raised est phrase. The strike stops before on suppose. The new que k est de car. 0, X normal, et occupies the interline, and k is the small base-field letter. The crossed word before on est has an f descender and dotted i, supporting enfin: rather than et si. Its punctuation and the dominance ending remain as first read.',
'B05':'The tall looped f lies between the curved parenthesis strokes; their joining can resemble psi, but there is no independent psi fork. Read pi_1(f), as in B06, with the full formula. The open subgroup, pi_1(Y) comma and the added Y hypothesis agree.',
'B06':'The same parenthesized looped f is present. The crossed opening has de and a separate tall t of tout before sous-groupe; the lower line ends ouvert with its t, not a clear plural s. After (1) an upper mark and a separate lower descending comma form a semicolon. The crossed X word and the short lower word remain obscured: extend the local alternatives to normal/admet and on/un. Et Y begins the following insertion and is not duplicated.',
'B07':'The second reader included the preceding line and its doubts; those are dealt with in B06. The actual group-condition insertion agrees, including et Y, VA and the absence of a terminal stop after tore. Its full extent remains one insertion.',
'B08':'The initial L has a high unlooped upright and long foot before e, supporting the first capital Le. The rest of the wholly cancelled e) passage agrees, including singular centralisateur and de son image.',
'B09':'The heavy vertical cancellations obscure the opening and several word bodies; the blind les hypothèses is not securely recovered and does not displace the first marked Remarquons. The visible tall/low fragments permit the already doubtful simple, centre, est non/not-equal-1, réduit and à un point; no wholesale illegibility substitution resolves them. The final detached hook descends like a comma, so correct the full stop. The note is already margin-boxed and deleted in the page; the wrapper difference is formatting.',
'B10':'The cited c) has an open crescent without an interior e bar, so retain c). The crossed phrase is visibly between the line ending est un and the next cas particulier; move it there, without changing its doubtful des variétés/de même and aurait. D’autre part remains struck. The asterisk’s empty superscript group is only TeX formatting.',
'B11':'The crossed old reduction begins at d) and continues through the old ouvert d’Artin. The live dash and mais sit above it as replacement continuation, so retain their live state after the cancelled old passage. A curved opening stroke precedes the new dans le cas d), which remains parenthetical and lower-case; the blind capital/no-opening reading is not adopted.',
'B12':'The source letter has a single broad lower U turn with a returning pen stroke, not two independent W valleys. Retain U after re-reading the full map. Its right endpoint is a tiny dark wedge, insufficient to resolve a head against a bare shaft, now locally doubtful. The j descender and closing curves overlap; preserve the closing-punctuation alternatives and also doubt the abbreviation stop. The extra leading text belongs to preceding context.',
'B13':'The starred margin placement is already encoded. Keep barred m, travailler! and g>=2; ge/geq and superscript wrappers do not change ink. The compressed noun before d’ordre fini allows éléments/élts, now marked. A short upper stroke above a separate dot supports the exclamation after fini, and the initial of Sinon is the larger looped form. Se borner has its b ascender and rn sequence; baser is not supported. The tiny endings of au(x) and de(s) remain doubtful. Non complètes and the final stop agree.',
'B14':'The two thin foliation digits are 27. The page already places them in margin; the difference is only the audit snippet’s wrapper.'}
reviews=[dict(box=b,decision=('correct' if b in ['B06','B09','B10'] else 'mark doubt') if f[b]!=x['first'] else ('formatting' if b in ['B07','B14'] else 'keep'),final=f[b],ink=inks[b],changed=f[b]!=x['first']) for b,x in cmp.items() if x['different']]
(R/'second'/f'{p}_review.json').write_text(json.dumps({'box_reviews':reviews},ensure_ascii=False,indent=2)+'\n')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
