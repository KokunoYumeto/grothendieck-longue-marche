"""Explicit root crop adjudications on scan017; historical one-shot script."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan017';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text()
repls={r'\deleted{standart}':r'\deleted{\unsure{standart|stable}}','suppl.':r'suppl\unsure{-|.}'}
for a,b in repls.items():assert t.count(a)==1;t=t.replace(a,b)
tp.write_text(t)
for group,field in [('changes','final'),('inventory','first_words_or_objects'),('abbreviations','form')]:
 for q in r[group]:
  for a,b in repls.items():q[field]=q[field].replace(a,b)
for c in r['changes']:
 if c['place']=='abbreviated structure adjective':
  c.update(against_C=True,confidence='medium',evidence='The letters end at suppl. The separate following mark is elongated horizontally, favoring a short dash over a round abbreviation point; the point remains an alternative. No ink supplies the expanded ending émentaire. Root revisited the entire phrase in second B11.',crop=f'crops/{pg}_second_B11.png',box=[int(x) for x in next(x for x in csv.DictReader((W/'second'/f'{pg}_boxes.tsv').open(),delimiter='\t') if x['box']=='B11').values() if str(x).isdigit()])
 if c['place']=='standart revision: literal spelling':
  c['evidence']+=' Blind-audit B07 leaves the canceled middle letters partly covered, so the canceled form now explicitly admits stable; the raised replacement ends in the crossed/upturned t form and remains standart.'
  c['confidence']='medium'
r['doubts'].extend([
dict(place='Canceled adjective after courbe',reading=r'\deleted{\unsure{standart|stable}}',alternatives=['stable'],confidence='low',reason='B07: the initial s/t and tall middle and terminal strokes survive, but the long cancellation merges with the low middle letters. The raised replacement is clear enough to retain standart; it does not resolve every letter of the canceled word.'),
dict(place='Terminal mark of abbreviated suppl',reading=r'suppl\unsure{-|.}',alternatives=['abbreviation point'],confidence='medium',reason='B11: the separate terminal mark has a horizontal extent several stroke widths long, favoring a short dash. An elongated abbreviation point cannot be excluded at the native resolution.')])
r['notes']=[n.replace(' No second-pass crop has been made.','') for n in r['notes']]
r['notes'].append('Independent audit: the opening verbal sign consists of two horizontal strokes, and Ici has a low c with a terminal dotted stroke, unlike the tall final l of Il later in the paragraph. The second h_1 retains its low right-hand index. The poids/points cluster and canceled le remain doubtful. Both raised MD prefixes are struck and their possible hyphens remain inseparable from the strike. The canceled adjective now admits stable as an alternative, while both live spellings remain standart. Two e bodies support épinglée. The terminal abbreviation mark after suppl favors a dash, with point retained as an alternative. The crossed X/C and final canceled types/des phrase stay unresolved; the script base S, hat and separate I underline are retained. This audit does not independently verify the mathematical argument.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('medium','The verbal mark has two near-horizontal strokes without an independently formed m body. At the right, the capital I is followed by a low c and a terminal dot/short stroke, supporting Ici rather than Il; the latter has a conspicuous tall loop in B03. The full g=0 and nu<=2 condition agrees.'),
'B02':('high','The complete genus expression has g=0=sum g-alpha+h_1. The later h also has a small low right-hand stroke, positioned like the first numeric index 1; it is not omitted and does not form a separate comma. Retain both h_1 readings.'),
'B03':('high','The zero is a closed oval; the graph/tree sentence and following Il agree. Only math wrapping differs.'),
'B04':('low','The initial p-o and final s survive in the reworked word; the middle overlapping stems still admit poids/points. A bare pts abbreviation does not account for the separate rounded o body. The canceled short word retains its visible l loop, while its low ending is covered; do not resolve le from the blind reader’s certainty alone. The whole >=2 condition agrees.'),
'B06':('low','The raised MD is crossed, and its rightward horizontal joins the strike; an original hyphen cannot be certified or excluded. The lower graphe is also crossed and the raised maquette is live. Preserve the uncertain hyphen and insertion/deletion layering.'),
'B07':('low','The second MD addition is crossed twice. The canceled adjective retains initial s/t and tall strokes but its low middle letters merge with the strike, so retain standart as preferred and admit stable. The raised live spelling ends in the same crossed/upturned t as the later standart. A separate open C stands at the baseline end; it is not merely an opening parenthesis.'),
'B09':('high','After the l ascender there are two e bodies, the first looped and the second open, supporting épinglée. The G- insertion attaches before the underlined word and the underline is separate from the p/g descenders.'),
'B11':('medium','The abbreviated letters read suppl. The following separate mark is several stroke widths long horizontally, favoring a dash; a stretched point remains possible. Prefer the dash while retaining explicit point uncertainty.'),
'B12':('low','Two heavy diagonals form X over a thinner curved loop compatible with C. The apparent lower right bar can be part of the diagonal and does not establish an independent G. Retain X/C uncertainty without inventing a deletion or writing order.'),
'B13':('high','The hat has two sloping sides above X. The I has both its ordinary lower serif and a separate short bar beneath it. Both readers agree; braces alone differ.'),
'B14':('medium','The internal d has a tall loop; the last sign is a shorter raised/crossed stem with an upturned exit, matching the final t of live standart in B07 and the local recurring spelling. Retain literal standart.'),
'B15':('high','The base symbol has an inward spiral in its upper bowl and a returned lower foot, the ornate/script S used for the base. It is retained as mathcal S, not flattened to the plain combinatorial-set S.'),
'B16':('low','The canceled phrase has opening paired ticks and surviving type stems; strike and descender obscure the ending, closing ticks and s of des. Keep the whole inherited phrase unsure. The raised maquettes and following live des are separately present; the curved stroke near the insertion belongs to the preceding g descender. The G-type statement agrees.')}
out=[]
for box,(c,e) in ev.items():
 final=first[box]
 for a,b in repls.items():final=final.replace(a,b)
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
