"""Explicit root audit decisions from the sixteen personally viewed mismatch crops."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='145_scan036';p=W/'reports'/f'{pg}.json';r=json.loads(p.read_text());tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repl=[(r'\deleted{on trouve que les}',r'\deleted{on trouve que les \unsure{2}}'),(r'\unsure{abstrayant}',r'\unsure{abstrayant|oubliant}'),('le sous-groupe','le sous groupe'),(r'\deleted{\unsure{ou} $\widehat{\widehat\pi}$}',r'\deleted{\unsure{ou|en} $\widehat{\widehat\pi}$}'),(r'$g_0=1,g_1=1',r'$g_0\unsure{=|\hat{=}|\overset{\cdot}{=}}1,g_1=1'),(r'\unsure{:}\ l_\infty',r':\ l_\infty')]
for a,b in repl:
 if a in t:assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
 else:assert b in t,(a,'neither original nor edited reading found')
tp.write_text(t)
bxs={x['box']:[int(x[k]) for k in ['x0','y0','x1','y1']] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
def setrow(i,b,final,e,conf='low',**kw):r['changes'][i].update(final=final,evidence=e,crop=f'crops/{pg}_second_{b}.png',box=bxs[b],confidence=conf,**kw)
setrow(4,'B05',r'\deleted{on trouve que les \unsure{2}}','After les there is a separate small angled upper stroke with a lower foot under the cancellation, compatible with 2 but not fully plain. It must not be omitted. The short horizontal near the preceding line end belongs to the canceled-line area; an independent live dash is not established.',against_C=True,against_H=True,kind='readable ink left as \\ill{}')
setrow(6,'B06',r'(\unsure{abstrayant|oubliant} la condition (13))','The opening has a compressed rounded cluster and tall b-like ascender. The internal joining cannot securely separate abstrayant from the independent oubliant proposal; a full initial d for donnant is not established. The entire pair and condition were checked.')
setrow(13,'B11',r'\deleted{\unsure{ou|en} $\widehat{\widehat\pi}$}','The low canceled word has a rounded initial loop and an obscured second join, permitting ou or en. The two hats and the curled right leg of pi remain distinct under the hatching.')
setrow(22,'B16',r':\ l_\infty^p l_1^p l_0^p=1','The independent crop confirms two separate dark points immediately before the first factor, in a colon arrangement. They are as dark as the nearby writing and form a coherent separator after the displayed label. The whole formula has indices infinity, 1, 0 and three p exponents; the colon doubt is removed.','high')
r['changes'].append(dict(place='Spacing between sous and groupe',C='sous-groupe',H='sous-groupe',final='sous groupe',evidence='B10 shows a blank interval between the final s of sous and the opening g; no separate horizontal hyphen crosses it. The g descender lies below the following word, not in that gap.',crop=f'crops/{pg}_second_B10.png',box=bxs['B10'],confidence='high',against_C=True,against_H=True,kind='other',marked_in_H='no',consequential=False))
for d in r['doubts']:
 if d['place'].startswith('M0907'):d.update(reading=r'\unsure{abstrayant|oubliant}',alternatives='abstrayant; oubliant',confidence='low',reason='B06: initial rounded cluster and ascender are overworked; compressed internal joins admit the independent oubliant proposal as well as abstrayant.')
 if d['place']=='Cancelled word before double-hatted pi':d.update(reading=r'\deleted{\unsure{ou|en} $\widehat{\widehat\pi}$}',alternatives='ou; en',confidence='low',reason='B11: opening loop favors ou, but hatching obscures the internal join and does not exclude en. Two hats over pi remain clear.')
r['doubts']=[d for d in r['doubts'] if d['place']!='Before first factor of (14)']
r['doubts'] += [dict(place='Canceled terminal after on trouve que les',reading=r'\unsure{2}',alternatives='unidentified small canceled character',confidence='low',reason='B05: independent angled top and lower foot survive after les; 2 is possible, but the crossing stroke prevents certainty.'),dict(place='First equality after rectificateurs',reading=r'\unsure{=|\hat{=}|\overset{\cdot}{=}}',alternatives=r'=; \hat{=}; \overset{\cdot}{=}',confidence='low',reason='B13: a small dark trace lies above a bowed upper equality stroke. It may be an incidental point, a hat-like decoration, or an overdot. The other two equalities are plain; no mathematical normalization is made.')]
for d in r['decisions']:
 if d['id']=='M0907':d.update(reading=r'\unsure{abstrayant|oubliant}',confidence='low',crop=f'crops/{pg}_second_B06.png',box=bxs['B06']);d['what the ink shows']='The compressed initial cluster and tall ascender favor abstrayant, but the independent oubliant reading cannot be excluded by the linked interior strokes. The mark remains undecided.'
for x in r['inventory']:
 if x['element']=='D02':x['first_words_or_objects']=r'on trouve que les \unsure{2}'
 if x['element']=='D04':x['first_words_or_objects']=r'\unsure{ou|en} \widehat{\widehat\pi}'
 if x['element']=='F02':x['first_words_or_objects']=r':\ l_\infty^p l_1^p l_0^p=1'
if isinstance(r['notes'],str):r['notes']=[r['notes']]
r['notes'].append('Independent audit changed six boxes: a doubtful canceled terminal 2 is retained after les; abstrayant/oubliant and canceled ou/en remain open; no hyphen is visible between sous and groupe; the first equality after rectificateurs has an uncertain upper mark; and the paired dots before (14) are now retained as a definite colon. The repeated narrow upright p is confirmed across the tuple, conditions and both displayed formulas, distinct from the rounder rho used on the preceding sheet. No proof of the exercise is claimed.')
r['hand_habits'].append(dict(habit='Narrow p versus rho in exponent and tuple notation',pages='145_scan033–036',consistency='On scan036 all inspected occurrences B02/B03/B05/B06/B08/B09/B15/B16/B17 share an upright stem with a small right-side bowl; p is retained. This is not a claim that every rho in the cote has a hooked tail.',witness_misread='Independent blind reader used rho throughout scan036; C/H use p here.',evidence='Root second crops B02,B03,B05,B06,B08,B09,B15,B16,B17'))
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
changed={
'B05':first['B05'].replace(r'\deleted{on trouve que les}',r'\deleted{on trouve que les \unsure{2}}'),
'B06':first['B06'].replace(r'\unsure{abstrayant}',r'\unsure{abstrayant|oubliant}'),
'B10':first['B10'].replace('sous-groupe','sous groupe'),
'B11':first['B11'].replace(r'\unsure{ou}',r'\unsure{ou|en}'),
'B13':first['B13'].replace('g_0=1',r'g_0\unsure{=|\hat{=}|\overset{\cdot}{=}}1'),
'B16':first['B16'].replace(r'\unsure{:}',':')}
ev={
'B01':('medium','Qui has a terminal i dot. Raised replacement starts with a descending p, has the short se, and ends in décrire, without a terminal -vons cluster. Keep peut se décrire. The canceled se définit remains doubtful because its ending is crossed.'),
'B02':('medium','Both p signs have an upright stem and small right bowl, unlike the rounded rho in the preceding page. Hat, star, two membership signs, parentheses and subscript 3 agree. Ornate S alphabet remains doubtful.'),
'B03':('high','All three superscripts are the same narrow upright p. Subscripts sigma(0), sigma(1), sigma(infinity), product order and equality to 1 agree; label (13) and no final point confirmed.'),
'B04':('medium','The compact a/u traces after S E can look like point/dash, but the following word has a tall l, a detached i dot and low eu ending: au lieu de. No L-ens sequence is established.'),
'B05':('low','The p, Z-star, braces and plus/minus 1 are clear. Cancellation crosses on trouve que les and a separate small angled terminal compatible with 2, now retained doubtfully. The short upper horizontal is in the cancellation area, not established as a separate live dash.'),
'B06':('low','The pair uses the same narrow p. The heavily joined word has a rounded opening and b-like ascender, but its interior allows abstrayant or oubliant; add the independent alternative without choosing by expected meaning.'),
'B07':('medium','The initial factor contains a diagonal/bar Z-like remnant crossed by the live braces and plus/minus 1; preserve the doubtful cancellation and insertion. Both ornate S alphabets remain doubtful. Two simeq signs, Z subscript 2 and final Gamma comma agree.'),
'B08':('high','Three short s forms are visible in sss; the third has a bent terminal and no i dot. The tuple begins with narrow p, as in B02. On voit que and satisfait (13) agree.'),
'B09':('medium','Tuple p has a small bowl; the Gamma subscript has the broader upper bowl of P, repeated under tilded Gamma. Inclusion signs, S E and double hats agree. Maintain the capital P and established calligraphic E encoding.'),
'B10':('high','The interval between sous and groupe is blank, so remove the supplied hyphen. Raised de S E attaches before baseline des. Autom ends without a separate point.'),
'B11':('low','Hatching crosses a short rounded word before two clear hats over pi. Ou is preferred, but en cannot be excluded by the obscured join; retain both. Pi has its curled right leg.'),
'B13':('low','Multiplicateurs is struck and rectificateurs is raised with short quotation ticks, not clear guillemets. The recurring g has variable straight/looped descender, especially a loop on g-infinity. An upper trace at the first equality is now marked uncertain (=, hatted equality or overdotted equality); whole three-equation string checked.'),
'B14':('high','The lower stroke is curved and m-like, with a separate straight bar above it. It differs from the two straight equality strokes later on the same sheet. Retain barred m.'),
'B15':('medium','P has the same upright stem. The insertion has two detached colon-like points after quitte, already uncertain against à. Corriger has two low r turns, dotted i and g descender, not conjuguer. A small i subscript is visible on tilded sigma; the following short horizontal has no comma tail. The tiny ou remains doubtful; no definite accent is seen.'),
'B16':('high','Two separate dark points before the first factor form a colon, confirmed independently. Remove its doubt. All three exponents are narrow p, and the full product has indices infinity, 1, 0 with equality to 1.'),
'B17':('high','Both signs are upright p with a small right bowl. Hat and star on Z, fixed-condition parentheses, final equality p=1 and the separate stop are clear.')}
out=[]
for b,(c,e) in ev.items():
 d=dict(box=b,changed='yes' if b in changed else 'no',confidence=c,evidence=e)
 if b in changed:d['final_reading']=changed[b]
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
