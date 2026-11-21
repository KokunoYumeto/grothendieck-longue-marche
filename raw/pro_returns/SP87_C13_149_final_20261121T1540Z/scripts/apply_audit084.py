from pathlib import Path
import json,csv
w=Path('/workspace/scratch/b8c6ff258063/SP87_C13_149_work');p='149_scan084';rp=w/'readers'/p/'report.json';r=json.loads(rp.read_text());pp=w/'pages'/f'{p}.tex';t=pp.read_text();t=t.replace(r'\operatorname{Gal}(\overline{k(x)}/k(x))',r'\operatorname{Gal}(\overline{k(\unsure{x|\dot{x}})}/k(x))');pp.write_text(t)
r['unresolved'].append(dict(place='formula (7), numerator residue-field argument',reading=r'\unsure{x|\dot{x}}',alternatives=['x',r'\dot{x}'],confidence='low'))
r['notes'] += '\n\nBlind review of (7) exposes a small isolated point above the numerator x. Its role as a deliberate diacritic rather than an incidental ink point is not secure; the text now retains x/dotted-x uncertainty locally, without placing the entire formula in doubt. The initial connector remains a plain shaft and the following connectors arrows. All eight token-different boxes were inspected; the short form hyp has no supplied stop, and le dit remains two written groups.\n'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
cs={x['box']:x for x in csv.DictReader((w/'second'/f'{p}_comparison.tsv').open(),delimiter='\t')}
e={
'B003':'After the opening parenthesis the short word has a small o and low u run, with no separate initial s needed for son. Retain ou; stabilisateur agrees.',
'B006':'All group terms, tilde indices, label (7), initial flat shaft and later arrowheads agree. A small isolated point above the numerator x is dark enough to notice, but its diacritic status is not secure. Add local x/dotted-x doubt, rather than a doubt around the complete sequence. The denominator x is unmarked.',
'B008':'The rotated note reads à cause de / l’hyp de / car. 0 !. Hyp ends without a separate stop; car has one. Both readings agree; the difference is only math-mode wrapping of zero.',
'B012':'The old upper bar and descending traces remain crossed under the new E. Two lower strokes favor pi, while their overlap with the replacement prevents certainty; retain the existing pi/Gamma doubt. A single I is not better established. K, the arrowhead, and the live target E_S agree; calligraphic rendering changes no letter.',
'B013':'There is a clear gap between the low return of le and the initial looped d of dit. Retain the two written groups le dit, followed by noyau and comma.',
'B014':'The first word after Soit has a tall angular initial and compressed low run; donc remains preferred, but the uncertain d bowl does not exclude sur. Keep the existing doubt. The underlined O in the U index, plain O after Spec and the final factorisations agree in letters and scope.',
'B015':'Both readings give 83: two loops followed by the open two-lobed 3. Retain its lower-left margin placement.',
'B016':'Label (8), tilde x, both isomorphism signs, infinity indices, field overbars and raised stars agree. Differences are tilde sizing, braces and display delimiters; retain the first reading.'}
d={k:dict(evidence=v,changed=k=='B006') for k,v in e.items()};d['B006']['final']=cs['B006']['first'].replace(r'\overline{k(x)}',r'\overline{k(\unsure{x|\dot{x}})}')
(w/'review'/f'{p}_audit_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
