"""Root image adjudications on scan022; historical one-shot script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan022';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repls={r'\unsure{\mathfrak S_J|\mathfrak G_J}':r'\unsure{\mathfrak S_J|\mathfrak G_J|\mathcal G_J}',r'\unsure{\mathfrak S_\nu|\mathfrak G_\nu}':r'\unsure{\mathfrak S_\nu|\mathfrak G_\nu|\mathcal G_\nu}',r'de $=$ \unsure{des|de}':r'de $\bar m$ \unsure{des|de}',r'de $\mathcal S$, la':r'de $\mathcal S$, \unsure{la|le}'}
for a,b in repls.items():assert t.count(a)==1;t=t.replace(a,b)
tp.write_text(t)
for group,field in [('changes','final'),('inventory','first_words_or_objects'),('notation','form'),('decisions','reading')]:
 for q in r[group]:
  for a,b in repls.items():q[field]=q[field].replace(a,b)
for d in r['decisions']:
 if d['id'] in ['M0943','M0944']:d['what the ink shows']+=' Blind-audit B05 also leaves the typographic alphabet open: a calligraphic G fits the rounded body and inward arm. This alternative is added without resolving the capital or changing the preferred reading.'
for d in r['doubts']:
 if 'M0943' in d['place'] or 'M0944' in d['place']:
  for a,b in repls.items():d['reading']=d['reading'].replace(a,b)
  d['alternatives'].append(r'\mathcal G_J' if 'M0943' in d['place'] else r'\mathcal G_\nu')
  d['reason']+=' The rounded outer body and inward arm also admit a calligraphic-G alphabet; the scan does not uniquely determine a font realization.'
r['doubts'].append(dict(place='Final article before continuation on next leaf',reading=r'\unsure{la|le}',alternatives=['le'],confidence='medium',reason='B15: a tall looped l is followed by a compact retraced oval and short exit. The inner stroke does not securely distinguish a from e. La stays preferred without using the next leaf’s noun to settle the letter.'))
boxes={x['box']:[int(x[k]) for k in ('x0','y0','x1','y1')] for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t')}
for c in r['changes']:
 if c['place']=='NB, verbal shorthand after Il en est donc de':c.update(final=r'$\bar m$',against_C=True,confidence='medium',evidence='B07: a separate straight upper bar stands above a low lower body with two shallow joins and an extended exit. The lower body is curved like the barred-m shorthand inspected on 145_scan029 B12, not a second straight equals stroke. Retain barred m, without expanding it. The blind pi/un proposal does not account for the detached upper bar and shallow body.',crop=f'crops/{pg}_second_B07.png',box=boxes['B07'])
for a in r['abbreviations']:
 if a['form']=='=':a.update(form=r'\bar m',places=r'147_scan022 Il en est donc de \bar m')
for h in r['hand_habits']:
 if h['habit'].startswith('A verbal equals shorthand'):
  h.update(habit='The barred-m shorthand has a detached straight upper bar above a low curved body with shallow joins.',places='147_scan022 Il en est donc de barred m; compared with 145_scan029 B12',scope='This local occurrence, confirmed by comparison with the previously inspected barred-m form; it does not replace genuinely straight two-stroke equals signs.',witness_errors='C reads an equals sign; H expands the written shorthand to même.')
r['notation'].append(dict(form=r'\bar m',meaning_or_use='Barred letter shorthand, visually distinct from the straight two-stroke verbal equals sign on scan017.',places='147_scan022 Il en est donc de ...'))
r['notes']=[n.replace("The literal equals shorthand is preserved instead of H's même.","The independent audit reads the shorthand as barred m from its curved lower body and detached upper bar; it remains unexpanded.") for n in r['notes']]
r['notes'].append('Independent audit: the moduli letters retain plain M, with upright first stems, unlike the longer curved initial feet of the script M forms on scans019/021. Both exclamation marks remain upper-right exponents. The two ornamental group symbols remain uncertain and now explicitly include a calligraphic-G realization. The verbal shorthand is revised to barred m after comparison with scan029 B12; this changes the preferred source sign, not its expansion in the text. All four X forms have opposing curved sides plus a separate central cross stroke and retain fraktur X. Both une endings have visible low final e bodies. The final la/le is left uncertain. The split title underline, g descender, underlined I, literal tt and curled base symbols were checked individually. No independent smoothness or moduli-scheme proof was performed.')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
r.setdefault('audit_consistency_checks',[]).append(dict(box='B08',crop=f'crops/{pg}_second_B08.png',reading=first['B08'],evidence='Exact-match box additionally inspected by root for the cross-page M comparison. Both final M letters have upright first stems; the later de has no separate s. The full bracketed-G identity and Gamma pair are retained.'))
ledger=W/'reports/root_viewed_crops.txt';v=ledger.read_text().splitlines();v.append(f'{pg}_second_B08.png');ledger.write_text('\n'.join(dict.fromkeys(v))+'\n')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ev={
'B01':('high','The head has an angled-cap upright 1 and closed oval 0. Both readers agree on 10; the page wrapper alone differs.'),
'B02':('medium','The rotated margin has one opening and one closing parenthesis around g, nu=card J, followed by anabélien with tall b/l and dotted i. The initial c of card is larger than the low a/r, but follows the same open curve as the recurring operator on scan014; size alone does not force a capital. Retain consistent lower-case card.'),
'B03':('high','Both M letters have near-upright first stems and a central valley, without the long curved left foot of script M on scans019/021. The exclamation mark is above and well right of M, not centered above it. Both g/nu/J indices agree; line-break and brace syntax alone differ.'),
'B04':('high','The whole expression has square brackets [1,nu], an intersection arch, double-stroked Z, one wave above a straight bar, J and one closing parenthesis. Only grouping of the parenthesis with math differs.'),
'B05':('medium','Both capitals have a broad rounded outer body, upper return and inward horizontal arm. These remain compatible with the existing ornamental S/G alternatives and also with a calligraphic G realization. Extend both doubts without resolving the capital from the permutation-group context. The J and nu subscripts and final point are clear; autom. has a separate point and no added or.'),
'B06':('high','The plain M, upper-right exclamation stroke with detached dot, and lower g/nu indices are all distinct. Only exponent bracing differs.'),
'B07':('medium','A detached straight bar lies over a low curved lower body with shallow joins, matching the barred m in 145_scan029 B12 more closely than a second straight equals stroke. Read barred m. The tiny separate remnant after de still favors s but remains des/de uncertain. Both M forms have upright initial stems and retain plain M.'),
'B09':('high','The long first underline ends beneath Mumford, before the hyphen; a separate stroke starts under Deligne. The lower curve under the second span is the g descender. The section number 4 and its point are outside the underline, and there is no final point after Deligne.'),
'B10':('high','The word has joined u/n humps followed by a low e-shaped join and extended exit. A real final e is present; retain une.'),
'B11':('medium','The ornate X has opposing curved sides crossed by a separate horizontal stroke. The following une has a small closed/low final e body. Only courbe is crossed; schéma and the curled base-S remain live. Retain fraktur X and the literal agreement mismatch.'),
'B12':('high','The second X repeats the opposing curved sides and independent transverse middle stroke, followed by a separate point. It is retained with the same fraktur alphabet as B11/B13/B14.'),
'B13':('high','The X again has the additional middle cross stroke. I has an ordinary lower serif plus an independent underline below it. The parentheses and comma are clear.'),
'B14':('high','The fourth X repeats the same ornate crossed form. The base S has an inward upper curl, and I has its independent underline. No separate line underlines MD-courbe relative. The entire flatness/finite-presentation wording agrees.'),
'B15':('medium','The tt has two separate upright stems and feet crossed by a common bar, unlike the converging universal sign on scan018. Both base-S letters have inward curls. The final l is clear but its following compact oval admits a or e; retain la with le alternative.')}
out=[]
for box,(c,e) in ev.items():
 final=first[box]
 for a,b in repls.items():final=final.replace(a,b)
 if box=='B07':final=final.replace(r'$=$',r'$\bar m$')
 if box=='B15':final=final.replace(r'de $\mathcal S$, la',r'de $\mathcal S$, \unsure{la|le}')
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
