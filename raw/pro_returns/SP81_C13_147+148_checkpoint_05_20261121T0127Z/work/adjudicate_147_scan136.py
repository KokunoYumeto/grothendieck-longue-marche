from pathlib import Path
from datetime import datetime,timezone
import json,csv
root=Path(__file__).resolve().parents[1];page='147_scan136'
p=root/'pages'/f'{page}.tex';t=p.read_text()
subs=[('immersion locale de codim','immersion loc.le de codim'),
 (r'codim $d_0$\deleted',r'codim $\unsure{d_0|d\prime_0}$\deleted'),
 (r'\unsure{On a}',r'\unsure{On a|Quand}'),
 (r'\{\uline{d_1}>-- >d_r\}',r'\{d_1\uline{>--} >d_r\}'),
 (r'\unsure{comme on voit}',r"\unsure{comme on voit|c'est à dire}"),
 (r'\unsure{tjs}',r'\unsure{tjs|tjrs}'),
 (r'D_{\widetilde d\prime_*}',r'D_{\unsure{\widetilde d\prime_*|\widetilde d_*}}'),
 (r"D_{\widetilde d'_*}",r"D_{\unsure{\widetilde d'_*|\widetilde d_*}}"),
 ('seulement, non',r'seulem\textsuperscript{t}, non')]
for a,b in subs:t=t.replace(a,b)
# The asymmetric right terminal tick does not determine a full arrowhead.
t=t.replace(r"D_{d'_0\,--\,d'_{r'}}\arrow[d,no head]",r"D_{d'_0\,--\,d'_{r'}}\arrow[d,no head,\"{\unsure{}}\" description]".replace(r'\"','"'))
p.write_text(t)
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text())
for c in r['changes']:
 for a,b in subs:c['final']=c['final'].replace(a,b)
 if c['id'].endswith('-03'):
  c['final']=r'\arrow[d,no head,"{\unsure{}}" description]'
  c['evidence']+=' The blind crop shows one short curved terminal arm at the right, without a separate opposing arm. Head status is now marked uncertain in place.'
  c['confidence']='medium'
 if c['id'].endswith('-07'):
  c['evidence']+=' The small raised dark mark beside the first d_0 admits a prime, so d_0/d-prime_0 is now left open. Quand is added as an alternative to the heavily cancelled On a.';c['confidence']='low'
 if c['id'].endswith('-10'):
  c['final']=r'\{d_1\uline{>--} >d_r\}'
  c['evidence']+=' Blind audit places the underline below the first greater-than and the two short separator strokes: its left end lies to the right of the subscript 1.'
  c['crop']=page+'_second_B04.png';c['box']=[275,805,1618,1032]
 if c['id'].endswith('-11'):c['evidence']+=' C’est à dire is an additional candidate from the exposed tall stroke in the last group, but the long cancellation still hides the centres of the words.'
 if c['id'].endswith('-13'):c['evidence']+=' The blind crop does not settle a small r among the cancelled loops; tjs/tjrs is retained as an explicit alternative.'
 if c['id'].endswith('-16'):c['evidence']+=' The upper-middle prime remains uncertain beneath the tilde. All six objects and seven shafts were recounted; two shafts bear four intermediate dark marks each. The middle rightward shaft has one upturn without a complete head.';c['confidence']='medium'
 if c['id'].endswith('-18'):
  c['evidence']+=' The shortened word ends in a low m-like run and a detached raised t; the full -ment is not written. Seulem with raised t is restored.'
  c['crop']=page+'_second_B08.png';c['box']=[278,1525,1601,1693]
# New lexical abbreviation locus, agreed incorrectly by both original witnesses.
r['changes'].append(dict(id=page+'-22',place='body line 6, abbreviation before codim',C='immersion locale',H='immersion locale',final='immersion loc.le',evidence='The crop shows l-o-c, a dark baseline point, then a tall l and e-return; no a is visible between c and l. The blind reading restores the written loc.le.',crop=page+'_second_B03.png',box=[305,565,1668,821],confidence='high',kind='abbreviation expanded or spelling modernised',error_sheet_kind='Abbreviations expanded, spelling modernised',differs_C=True,differs_H=True,marked_in_H=False,consequential=False))
for d in r['doubts']:
 for a,b in subs:d['reading']=d['reading'].replace(a,b)
r['doubts'] += [dict(place='(224), right vertical shaft',reading=r'\unsure{\text{unheaded shaft}|\downarrow}',alternatives='unheaded shaft with terminal tick; incomplete downward arrow',confidence='medium',reason='One short curved arm is visible at the lower right; no opposing arm can be isolated. The question is placed on the shaft.'),dict(place='body line 6, first codimension index',reading=r'\unsure{d_0|d\prime_0}',alternatives='d_0; d-prime_0',confidence='low',reason='A small dark raised mark lies beside the d; cancellation begins immediately to its right.'),dict(place='marginal diagram, upper middle subscript',reading=r"\unsure{\widetilde d'_*|\widetilde d_*}",alternatives='with prime; without prime',confidence='medium',reason='A short upright under the right part of the tilde can belong to a prime or the adjoining letter strokes.')]
r['abbreviations'] += [dict(form='loc.le',expansion='locale'),dict(form=r'seulem\textsuperscript{t}',expansion='seulement')]
r['hand'].append(dict(habit='A contracted final -ment can be a long low run ending in a small raised t; medial omission can be marked by a point.',places='loc.le before codim; seulem with raised t in Attention sentence',scope='Both occurrences independently cropped and root-checked; no expansion remains in the transcription.',witness_errors='Both C and H wrote locale and seulement in full.'))
r['notes']+=' Blind audit restores loc.le and seulem with raised t, shifts the short underline beneath >--, and adds local alternatives for a possible prime, a crowded tilded index, and crossed words. Six marginal objects and seven connector shafts were recounted. The asymmetric upper right vertical endpoint remains uncertain in place. No mathematical statement was checked during this audit.'
# Use actual crop metadata, not a copied coordinate guess.
coords={x['file']:x['box'] for x in map(json.loads,(root/'work'/f'{page}_crops.jsonl').read_text().splitlines())}
for c in r['changes']:
 if '_second_' in c['crop']:c['box']=coords[c['crop']]
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());ds={x['box']:x for x in comp['differences']}
ev={
'B01':('The curved upper/lower loop of 6 and long descending stem with cross-stroke of 7 read 67. The wrapper is the only difference.','high'),
'B02':('Four D objects and four shafts are visible. The numeral 4 overlies earlier dark strokes, which remain uncertain and cancelled. The top-right indices have one prime above each d and another after r. The lower-right star is densely crossed. The right vertical terminal has only one short curved arm, so its head status is now explicitly doubtful while the drawn shaft remains.','medium'),
'B03':('Loc.le has an internal point and no written a. The first d_0 is live before the strike; a raised dark mark allows a prime without settling it. Cancellation obscures On a/Quand. The (225) scalar remains d/delta and the entire equality agrees.','low'),
'B04':('Typique has separate y/p/q descenders; the parenthesis has an auq- group and a final réduit-like tall d/t sequence. Où remains preferred. The short underline begins after d_1, below the comparison and two separator strokes. The preceding curly mark stays uncertain.','medium'),
'B05':('The long strike hides the centres of the phrase under plus gén.t; c’est à dire is added beside comme on voit. The later short cancelled loops permit tjs/tjrs. Reste stays doubtful and the raised si d-prime_0=d_1 is clearly attached before et.','low'),
'B06':('Six objects and seven shafts were checked. The two left/down connectors each have four dark intermediate marks. The middle rightward shaft has a single small upturn without separate head arms. The crowded upper-middle tilde leaves the prime uncertain; fini étale and cart remain visible. No new star is added above any D.','medium'),
'B07':('The source alone has a superscript star, and both d subscripts carry their small star indices. One right arrow and label (225) agree; column spacing alone differs.','high'),
'B08':('The word after the first D has a low seulem run and a detached raised t, so the shortened form is restored. Two vertically placed dark marks after non form a colon. All formula indices and the final exclamation agree.','high'),
'B09':('The two Theta subscripts and the D subscripts match exactly, including prime/star positions. Only math delimiters differ.','high'),
'B10':('The first Theta exponent has parentheses around p; the second is plain p. Quotation marks and the cancelled p-like start agree. Only math delimiters differ.','high'),
'B11':('The pencil numerals are 135; only the margin wrapper differs.','high')}
choices=[]
for b,d in ds.items():
 final=d['first']
 for a,z in subs:final=final.replace(a,z)
 if b=='B02':final=final.replace(r'\arrow[d,no head]',r'\arrow[d,no head,"{\unsure{}}" description]')
 it=dict(box=b,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[b][0],confidence=ev[b][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_a',choices=choices),ensure_ascii=False,indent=2)+'\n')
