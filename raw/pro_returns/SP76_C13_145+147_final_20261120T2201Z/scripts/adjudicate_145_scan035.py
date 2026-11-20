"""Main-reader decisions after personal inspection of all 17 mismatching crops."""
from pathlib import Path
import csv, json, subprocess, sys
W=Path(__file__).resolve().parents[1]; page='145_scan035'
p=W/'reports'/f'{page}.json'; r=json.loads(p.read_text())
tpath=W/'pages'/f'{page}.tex'; t=tpath.read_text()
changes=[
 (r'\unsure{\subset|\in}',r'\unsure{\subset|\in|\leftarrow}'),
 (r'\operatorname{Autext}_{\mathrm{lac}}',r'\operatorname{Autext}_{\unsure{\mathrm{lac}|\mathrm{loc}}}'),
 (r'\hat\pi$.',r'\hat\pi$\unsure{,|.}'),
 (r'\deleted{\unsure{extérieurs}}',r'\deleted{\unsure{extérieurs|secteurs}}'),
 (r'qui remonte $\Gamma^+',r'qui \unsure{rem.te|remonte} $\Gamma^+'),
 ('\nOn peut dire aussi','\n'+r'\unsure{On|\deleted{On}} peut dire aussi'),
 (r'$1$ est un sous-\uline{groupe}',r'$1$ \unsure{est|$\to$} un \unsure{ss-|sous-}\uline{groupe}')]
for a,b in changes:
 assert t.count(a)==1,(a,t.count(a)); t=t.replace(a,b)
tpath.write_text(t)
boxes={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in csv.DictReader((W/'second'/f'{page}_boxes.tsv').open(),delimiter='\t')}
def meta(row,b,e):
 row.update(crop=f'crops/{page}_second_{b}.png',box=boxes[b],evidence=e,confidence='low')
def doubt(place,reading,alternatives,reason):
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alternatives,confidence='low',reason=reason))
for d in r['doubts']:
 if d['place']=='opening relation before double-hatted Gamma':
  d.update(reading=r'\unsure{\subset|\in|\leftarrow}',alternatives=[r'\subset',r'\in',r'\leftarrow'],reason='B02: a retraced upper curve, heavy middle shaft and left curve/vertical with a bottom loop do not separate subset, membership and a leftward arrow. Two arrowheads are not independently clear.')
 if d['place']=='struck extérieurs, not separately in MARKS':
  d.update(reading=r'\deleted{\unsure{extérieurs|secteurs}}',alternatives=['extérieurs','secteurs'],reason='B04: tall t and final -eurs/-urs survive, but the canceled opening and compressed internal letters admit secteurs as well as extérieurs. The complete ending does not establish sections.')
for row in r['changes']:
 if row['place']=='struck word after double-hatted E':
  row['final']=r'\deleted{\unsure{extérieurs|secteurs}}'
  meta(row,'B04','The tall t and final cursive -eurs/-urs remain visible through a horizontal cancellation. The opening and inner e/r/i sequence are obscured; the independent secteurs reading remains possible alongside extérieurs. The final cluster does not establish sections. Primary reading remains C, with expanded doubt.')
 if row['place']=='On at beginning of final paragraph':
  row['final']=r'\unsure{On|\deleted{On}}'
  meta(row,'B17','A dark horizontal crosses the left/interior of O but stops before n. It can be an entry/overworking stroke or a short cancellation. The independent reader treats the word as struck; the main reader retains live On as preferred but now marks its state as uncertain.')
 if row['place']=='final underline extent':
  row.update(place='final short form and underline extent',final=r'\unsure{ss-|sous-}\uline{groupe}',against_C=True,kind='abbreviation expanded or spelling modernised')
  meta(row,'B19','Before the hyphen the ink has two compact joined s-like traces, without independently separable o and u bowls; ss- is preferred, sous- remains possible. The long lower stroke lies under groupe; its leftward beginning is the returning g descender, so an underline of the whole prefix is not established.')
def row(place,C,H,final,b,e,kind):
 r['changes'].append(dict(place=place,C=C,H=H,final=final,evidence=e,crop=f'crops/{page}_second_{b}.png',box=boxes[b],confidence='low',against_C=True,against_H=True,kind=kind,marked_in_H='no',consequential=False))
row('opening formula terminal punctuation','.', '.',r'\unsure{,|.}','B02','The separate final mark is a short descending diagonal at the lower baseline, favoring a comma rather than a round point. Its small scale leaves period possible.','other')
row('live verb below equation (11)','remonte','remonte',r'\unsure{rem.te|remonte}','B15','After the low rem cluster a detached point and a gap precede the tall t and final e. No separate o-n sequence is secure. The abbreviated rem.te is preferred, while the full remonte remains an alternative. The canceled earlier qui remonte is fully written.','abbreviation expanded or spelling modernised')
doubt('opening Autext subscript',r'\unsure{\mathrm{lac}|\mathrm{loc}}',[r'\mathrm{lac}',r'\mathrm{loc}'],'B02: l and c are plain; the tiny middle bowl does not separate a from o. The same ambiguity occurs in 145_scan033 B10.')
doubt('opening formula terminal punctuation',r'\unsure{,|.}',[',','.'],'B02: the short descending terminal favors comma, but is too small to exclude a point.')
doubt('live verb below equation (11)',r'\unsure{rem.te|remonte}',['rem.te','remonte'],'B15: a detached point and gap before te favor an abbreviation; compressed intervening letters cannot be ruled out.')
doubt('state of On at final paragraph opening',r'\unsure{On|\deleted{On}}',['live On','canceled On'],'B17: horizontal trace crosses O but stops before n; intention remains uncertain.')
doubt('final paragraph predicate',r'\unsure{est|$\to$}',['est',r'$\to$'],'B19: a long low stroke and an up/down terminal can be compressed est or a rightward arrow; the expected syntax alone cannot decide.')
doubt('final short form',r'\unsure{ss-|sous-}',['ss-','sous-'],'B19: two compact s-like traces favor ss-; intervening o/u divisions are not secure.')
r['abbreviations'].append(dict(form='rem.te',expansion='remonte',places='145_scan035 below equation (11), reading doubtful'))
for a in r['abbreviations']:
 if a['form']=='ss-': a['places']+='; final paragraph, doubtful short form'
r['notes'].append('Independent audit: five boxes changed (B02, B04, B15, B17, B19). A comma is preferred at the opening formula end; rem.te and final ss- are preferred short forms, with full-word alternatives retained. The opening relation now also admits a left arrow; lac/loc, the canceled word, the state of On, and est versus an arrow remain explicit doubts. These are ink decisions, not mathematical proof checks.')
r['notes']=[s.replace('subset versus membership is retained as an explicit doubt','subset versus membership versus a left arrow is retained as an explicit doubt') for s in r['notes']]
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{page}_first.tsv').open(),delimiter='\t')}
finals={
 'B02':first['B02'].replace(r'\unsure{\subset|\in}',r'\unsure{\subset|\in|\leftarrow}').replace(r'_{\mathrm{lac}}',r'_{\unsure{\mathrm{lac}|\mathrm{loc}}}').removesuffix('.')+r'\unsure{,|.}',
 'B04':first['B04'].replace('extérieurs','extérieurs|secteurs'),
 'B15':first['B15'].replace(r'qui remonte $\Gamma^+',r'qui \unsure{rem.te|remonte} $\Gamma^+'),
 'B17':r'\unsure{On|\deleted{On}}',
 'B19':first['B19'].replace(r'$1$ est un sous-\uline{groupe}',r'$1$ \unsure{est|$\to$} un \unsure{ss-|sous-}\uline{groupe}')}
evidence={
'B02':('low','The vertical double bar below Gamma and hats are distinct. Ornate S remains alphabetically doubtful. The overworked relation admits subset/membership/left-arrow; a second arrowhead is not clear. Tiny subscript middle bowl admits a/o. The final diagonal terminal favors comma, now doubtful.'),
'B03':('medium','Separate canceled geometry precedes a plain live rho with an open upper bowl and descender. The long wave is in the canceled tau zone, not securely a tilde on rho. A dot sits above sigma0, none above sigma1 or sigma-infinity. No independent inserted tau is established; retain the drawn unidentified sign and doubtful canceled tau.'),
'B04':('low','Initial comma and NB point are separate. Tall t and final -eurs/-urs survive the strike; the compressed interior permits extérieurs or secteurs. The cancellation does not expose a complete sections ending.'),
'B05':('high','Straight upper bar is separate from two-humped cursive m. The upright-font/overline variant has the same reading; no expanded word is present.'),
'B06':('high','Two distinct chevrons sit above the round two-lobed E following S. The only disagreement is math delimiters.'),
'B07':('high','Horizontal bar above m and a separate descending comma are plain. Font and overline encoding do not change the reading.'),
'B08':('high','Dot on rho, barred-tail map arrows, dot on sigma0, tilde on target sigma0, equality and sigma0 tau0 all agree. The clipped preceding context and arrow/tilde length macros do not change the source signs.'),
'B09':('medium','Multiplicatif stands above relèvement de. The subscript is an upright stem with a closed bowl on its upper half, favoring capital P as again in B14. The ornate S alphabet remains doubtful; all tuple, sign, membership and brace signs agree.'),
'B10':('high','A q descender and separate apostrophe precede the low on connection. Aimerait starts with a low a and dotted i, has m humps and a tall final t; there is no initial d ascender for devrait.'),
'B11':('high','Et de, barred m, pour, dotted sigma0 mapping to plain sigma0, and tau mapping to tau0 are visible. Differences are overline, font and arrow length conventions.'),
'B13':('low','After conjugaison and comma the short stem plus tall loop and low ending favor idem but do not fully separate its letters. The next word has p descender and low our ending, without the t/s of points. Retain idem doubt and pour.'),
'B14':('medium','Label (11), varphi with descending return, colon, Gamma with star and upright upper-bowled P, and a right arrow to S E are visible. The P shape agrees with B09; no basis for lowercase p normalization.'),
'B15':('low','The cancellation crosses qui remonte and ends before its separate point. In the later live verb a detached point and gap precede te; prefer doubtful rem.te. Gamma superscript is a two-stroke plus, unlike the multi-arm star in B14. Remaining text agrees.'),
'B16':('high','Both full rows were checked: dots, primes, signs 1 and -1, tuple entries, two dfn labels, tildes, ampersand and the three indices agree. Layout and grouping of prime/dot macros account for the token mismatch.'),
'B17':('low','The dark horizontal traverses the left/interior of O and stops before n. Its status as entry/overworking or short cancellation is not settled; retain live On as preferred with canceled On as an explicit alternative.'),
'B19':('low','The first g0 has a lower loop; later cursive g forms have straighter descenders but belong to the same repeated tuple notation. Whole tuple and equality-to-1 condition checked. The compressed predicate admits est or an arrow. Two short s-like traces favor ss-, with sous- retained; underline principally follows groupe and final low stop remains doubtful. Leading de is outside the tight second crop but already in the adjoining context.'),
'B20':('high','Two-lobed 3 and looped crossing 4 are clear. Margin versus manuscript-page wrapper does not alter the numeral; hand attribution remains unassigned.')}
dec=[]
for b,(conf,e) in evidence.items():
 d=dict(box=b,changed='yes' if b in finals else 'no',evidence=e,confidence=conf)
 if b in finals:d['final_reading']=finals[b]
 else:d['use_first']=True
 dec.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),page],input=json.dumps(dec),text=True,check=True)
