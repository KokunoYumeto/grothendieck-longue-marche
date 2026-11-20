"""Explicit root crop decisions; historical one-shot audit script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1]; pg='147_scan004'; rp=W/'reports'/f'{pg}.json'
r=json.loads(rp.read_text()); tp=W/'pages'/f'{pg}.tex'; t=tp.read_text()
assert not r.get('audited')
old=r'(loc. ét) à la courbe'; new=r'(loc. ét) à \unsure{un|\deleted{un}} la courbe'
assert t.count(old)==1; t=t.replace(old,new)
assert t.count(r'\unsure{contenu}')==1; t=t.replace(r'\unsure{contenu}',r'\unsure{contenu|courbe}')
tp.write_text(t)
bxs={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
r['changes'].append(dict(place='Condition b: small word after à at line end',C='(loc. ét) à la courbe',H='(loc. ét) à la courbe',final=new,evidence='After the clear oval-and-accent à are two low joined letter bodies, read un. A short horizontal runs through them, but its ends merge with the connecting/retraced strokes, so cancellation is not secure. The following line separately begins la courbe. Preserve the extra un, with deletion state doubtful, rather than remove it to repair the phrase. Root saw both B06 and overlapping B07; the blind reader independently described the same low letters and uncertain crossing after writing the second TSV.',crop=f'crops/{pg}_second_B06.png',box=bxs['B06'],confidence='medium',against_C=True,against_H=True,kind='omission',marked_in_H='no',consequential=False))
for d in r['doubts']:
 if d['place']=='Cancelled word after I est':
  d.update(reading=r'\deleted{\unsure{contenu|courbe}}',alternatives=['contenu','courbe'],confidence='low',reason='B09: initial c/o and low joins survive beneath the strike, followed by one taller stem with a lower loop. The blind reading courbe is also possible; the crossing prevents a complete letter-by-letter choice. Keep contenu preferred without resolving the canceled word.')
r['doubts'].append(dict(place='Condition b: un after à, before next-line la courbe',reading=r'\unsure{un|\deleted{un}}',alternatives=['live un','canceled un'],confidence='medium',reason='B06 shows two low joined letters after à; a horizontal through them may be cancellation or retracing. B07 confirms that la courbe starts the following line separately. No grammatical repair is made.'))
if isinstance(r['notes'],str):r['notes']=[r['notes']]
r['notes'].append('Independent audit: a small un after the line-final à in condition b is present in the ink but absent from both witnesses. Its possible cancellation is recorded in place; the literal sequence before next-line la courbe is not repaired. The canceled word after I est now retains contenu/courbe alternatives. The whole two-row display agrees. Title B01 has an oval body below the accent; in B11/B12/B13 that body is reduced to a thick point or short stroke. Their repeated prepositional à reading is retained at medium confidence under the local shape habit, not from a change to the formula. This is a reading decision, not an independent theorem check.')
r['audit_consistency_checks']=[dict(box=b,crop=f'crops/{pg}_second_{b}.png',evidence=e) for b,e in [('B01','Root compared the small oval below the detached accent with reduced à in B11/B12/B13; title retained.'),('B07','Root inspected the next-line la courbe and the entire local ring model; la is separate from the small preceding-line un.'),('B13','Root inspected the reduced two-stroke preposition after équivaut; its small body and detached accent match the local à habit.')]]
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
v=W/'reports/root_viewed_crops.txt'; lines=v.read_text().splitlines(); lines += [f'{pg}_second_{b}.png' for b in ('B01','B07','B13')];v.write_text('\n'.join(dict.fromkeys(lines))+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B02':('high','Final t has a tall upright, triangular turn and crossing bar, unlike the internal looped d. Retain standart. The underline ends before the period.'),
'B03':('high','Paired short quote ticks and the crossed final t are visible; retain the diplomatic paired quotes and standart.'),
'B04':('medium','Live un precedes a crossed e loop; the following separate canceled cluster contains several low curves and a taller stem. It is more than the final e alone, but every letter of courbe remains uncertain.'),
'B06':('medium','Quote clusters are asymmetric as transcribed; ét has an accent and no following dot. After clear à, low joined un-like letters have a possible crossing whose ends merge with their joins. Add un with live/canceled state uncertainty. B07 independently shows la courbe at the next line start.'),
'B08':('high','Donner begins with a looped d and has low n/n humps, not the t/r sequence of trouver. Complétion ends with dotted i and low o/n, not a second é. The inserted final que has q descender and u/e join at the right edge. Its attachment remains before baseline X s’identifie.'),
'B09':('low','The crossed word retains c/o, low joined traces and one taller stem with lower loop. Courbe is a plausible competing reading, but the strike prevents resolving it. Expand the retained doubt without changing its preferred contenu. I has integral top and bottom serifs.'),
'B11':('medium','One hat stands above final X. The long low strokes belong to g descenders in singuliers and analogue. The reduced à is a small body below a detached accent, consistent with B01/B12/B13. Braced hat syntax alone differs.'),
'B12':('high','Both full rows, hats, superscript lisse, field k, subset signs and captions agree. One left brace groups them. Paired quote ticks are visible. The manuscript line-wrap singu-/liers is reflowed as singuliers; aligned/array is layout only.'),
'B14':('high','The lower-left numeral has two rightward bowls meeting at a waist: 3. Margin/page-number wrapper does not change the ink.')}
out=[]
for b,(c,e) in ev.items():
 final=first[b]
 if b=='B06':final += r' \unsure{un|\deleted{un}}'
 if b=='B09':final=final.replace(r'\unsure{contenu}',r'\unsure{contenu|courbe}')
 d=dict(box=b,changed='yes' if final!=first[b] else 'no',confidence=c,evidence=e)
 if final!=first[b]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
