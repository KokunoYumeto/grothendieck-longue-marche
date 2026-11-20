"""Root image adjudications on scan019; historical one-shot script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan019';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repls={r'\unsure{0|6}':r'\unsure{6|0}',r'g\deleted{\unsure{\alpha}}':r'g\deleted{\unsure{\alpha|\nu}}',r'\deleted{catégorie}':r'\deleted{\unsure{catégorie|catég.}}'}
for a,b in repls.items():assert t.count(a)==1;t=t.replace(a,b)
tp.write_text(t)
for group,field in [('changes','final'),('inventory','first_words_or_objects'),('additional_crop_checks','reading')]:
 for q in r[group]:
  for a,b in repls.items():q[field]=q[field].replace(a,b)
for c in r['changes']:
 if c['place']=='first connectedness qualifier: written digit and hyphen':
  c.update(against_C=True,confidence='medium',consequential=True,evidence='The first digit has a long entry stroke rising above a closed lower loop, favoring the written shape 6; the later 0-connexes has a short round oval without that tall entry. A zero written with an unusually long entry remains possible. The preferred uncertainty is therefore 6|0, without imposing the expected connectedness value. H omits the numeral and hyphen altogether. The whole parenthetic condition was inspected in B02 and in the existing relt crop.')
 if c['place']=='canceled index after the later natural integer g':c['evidence']+=' Audit B04 also admits nu among the obscured strokes; alpha remains preferred but is not resolved.'
for d in r['doubts']:
 if d['place']=='first connectedness digit':d.update(reading=r'$\unsure{6|0}$-connexe',alternatives=['0'],reason='B02 and the existing relt crop: a tall entry rises above a closed lower loop, giving a six-like outline. The later zero is a short round oval. Prefer 6 from these strokes while retaining 0 as an alternative; the mathematical expectation does not decide the digit.')
 if d['place']=='canceled index after the later g':d.update(reading=r'g\deleted{\unsure{\alpha|\nu}}',alternatives=[r'\nu'],reason='B04: diagonal cancellation strokes cover the small lower group. A loop and tail compatible with alpha remain, but the oblique remnants also admit nu; neither can be certified through the crossing strokes.')
r['doubts'].append(dict(place='Canceled category word beside (19)',reading=r'\deleted{\unsure{catégorie|catég.}}',alternatives=['catég.'],confidence='low',reason='B05 and the existing definition19 crop: the c/a opening and g descender survive, but the strike merges with the low internal and right-edge ending strokes. The full catégorie remains preferred, with an abbreviated ending admitted; not every canceled letter is plain.'))
for q in r['additional_crop_checks']:
 if q['place']=='category-to-groupoid replacement by the circled notation':q.update(confidence='low',evidence='Le remains live and the horizontal strike crosses the old category word; groupoïde is raised above it. The c/a opening and g descender survive, but the low internal and right-edge ending strokes merge with the strike. The audit therefore adds catégorie/catég. uncertainty without changing the preferred word or the replacement state.')
r['abbreviations'].append(dict(form='catég. (alternative in canceled text)',expansion='catégorie, if the abbreviated alternative is retained',places='147_scan019 canceled word beside (19)'))
r['notes']=[n.replace('The first connectedness digit remains 0|6, independently of what the mathematics might suggest.','The first connectedness digit is retained as 6|0 after the independent audit: its tall entry and lower loop favor the six-like shape, independently of what the mathematics might suggest.') for n in r['notes']]
r['notes'].append('Independent audit: the two separate stems and feet before alpha favor tt, unlike the converging universal sign on scan018 B07; the forall alternative remains. The first connectedness digit now prefers 6 over 0 from its tall entry and lower loop, while the later round zero stays clear. This is an uncertain ink reading, not a correction of the mathematical statement. Both live spellings are standart, and no hyphen is supplied across the opening au dessus line break. The raised hatted-I replacement retains the uncertainty of its alpha attachment. The canceled later index admits nu as well as alpha, and the canceled category word is now explicitly uncertain in its hidden ending. Entier naturel has no separately visible final s. The open oval, leftward arrow to (19), underlined I-ponctuées, two hooked arrows and complete formulas (20)/(21) were rechecked visually. The final relation has two waves over a straight bar. No independent groupoid-equivalence proof was performed.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('high','The opening au is at the end of one baseline and dessus at the next, without a written hyphen. Standart has the internal looped d followed by r and a final crossed t; stable would not account for those final strokes. The base-S has the returned form used more elaborately in B03/B07. The whole I-alpha/tilde-A-alpha phrase agrees, including plain A in the second pair.'),
'B02':('medium','The short form before alpha has two independent near-parallel stems with separate feet and one shared crossbar, favoring tt; unlike scan018 B07 its lower legs do not converge. Keep the forall alternative. The first connectedness digit has a tall entry above a closed lower loop, favoring 6 over 0; retain zero as an alternative. The inserted rel with raised t and the complete parenthetical condition were inspected, with no abbreviation point supplied.'),
'B03':('medium','The initial letter of sur remains retraced and cannot be resolved merely from the readable u/r ending. All three base symbols have curled returns. The first mono has a separate point. The complete hatted-I-alpha map has both a left hook and right arrowhead, and the S- insertion attaches before mono. The et underline is independent.'),
'B04':('low','The canceled notation retains the lower nu-alpha and the raised hatted-I replacement before whole-span cancellation; no separate raised alpha is visible, so its attachment remains doubtful. The canceled word before un still favors deux over de, without a distinct apostrophe supporting d’un. Entier and naturel end in their own r/l exits without separate final-s bodies. The canceled index after g has loop/oblique remnants admitting alpha or nu; retain alpha first and add nu as an alternative.'),
'B05':('low','The oval is open at upper right and sends a leftward arrow from its lower-left edge to (19); the formula inside has script M, g,I and the curled base symbol. The canceled category word has a visible c/a opening and g descender, but strike and edge compression obscure its ending: retain catégorie with catég. alternative. Groupoïde is raised. Ponctuées has the low n/c sequence before the crossed t, and the underline starts under I. The later zero is a short closed oval, distinct from the tall-entry digit in B02.'),
'B06':('high','The verb begins with a tall crossed t and a following low r, then the joined ou/v/e sequence: trouve, not aura. Both words donc, si and their punctuation are present. The lower mono has no separate abbreviation point. The whole I-base hooked map agrees.'),
'B07':('high','Both complete displays were inspected. The relation in (21) contains two separately undulating upper strokes over one straight lower bar, approxeq rather than a one-wave relation. Script M has its long curved initial foot; the base S has an inward curl. All g/alpha/G/I indices, hats, product limit, numbers 20/21 and the final point are present. The live adjective again ends in crossed t, retaining standart.')}
out=[]
for box,(c,e) in ev.items():
 final=first[box]
 for a,b in repls.items():final=final.replace(a,b)
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
