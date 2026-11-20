"""Root decisions for the six blind mismatches on scan008."""
from pathlib import Path
import csv,json,subprocess,sys
W=Path(__file__).resolve().parents[1];pg='147_scan008';rp=W/'reports'/f'{pg}.json';r=json.loads(rp.read_text());assert not r.get('audited')
tp=W/'pages'/f'{pg}.tex';t=tp.read_text();a=r'Soit $\unsure{X}$ une';b=r'Soit $\unsure{X|S}$ une';assert t.count(a)==1;t=t.replace(a,b);tp.write_text(t)
for d in r['doubts']:
 if d['place']=='Soit X':d.update(reading=r'\unsure{X|S}',alternatives=['X','S','overworked X/S without a separable revision sequence'],reason='B03: two strong crossed diagonals support X, while an upper rounded loop and lower returned curve also preserve an S-like outline. The blind reader proposes an earlier S, but no independent strike distinguishes a deleted S from the overworked current glyph. Keep one live uncertain symbol, X/S.')
for d in r['decisions']:
 if d['id']=='M0927':d.update(reading=r'\unsure{X|S}',**{'what the ink shows':'Strong X-like crossed diagonals with upper and lower returned loops also allow S. No independent strike separates an earlier glyph from the current one; the exact revision history is not recoverable. Blind B03 expands the explicit alternatives without resolving the mark.'})
for c in r['changes']:
 if r'\unsure{X}' in c['final']:c['final']=c['final'].replace(r'\unsure{X}',r'\unsure{X|S}');c['evidence']+=' Blind B03 retains S as an explicit local alternative, without inventing a separate revision sequence.'
if isinstance(r['notes'],str):r['notes']=[r['notes']]
r['notes'].append('Independent audit: the heavily overworked symbol after Soit now records X/S, without claiming a recoverable deleted-S/inserted-X sequence. The reduced final e of une is present. The slanted note is kept distinct from the crossing body lines: their loops do not supply an independent remplacer after il faut or after i.e. The round diagram label o is compared with the angular sigma in the quotient below and with the origin notation on scan009; it remains o. The whole diagram and display (7) were reread. This is a reading review, not a check of the geometric assertions.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
first={x['box']:x['reading'] for x in csv.DictReader((W/'second'/f'{pg}_first.tsv').open(),delimiter='\t')}
ev={
'B01':('low','The opening has the tall initial J and doubled p descenders of J’appelle, not two low letters on. Relative has a tall l/t and final v/e, and standart ends in crossed t. Compactifié has a p descender and c/t sequence. The tuple remains one overworked Y/X. The canceled word has a v-like dip followed by dotted i and angular s, supporting the retained dévisant/divisant alternatives; no tall f supports définissant. The marginal nbs lacks extra r/e, the second pl has no separate point, and the supposed remplacer loops belong to crossing body baselines. The next marginal line begins dans le contexte and later X par. Keep the phi/empty-set doubt and the existing parentheses; no comma is supplied from crossing body ink.'),
'B02':('high','Final t has an upright with a long crossing arm, unlike the looped internal d. The underline stops before the separate point. Retain standart and the period outside the underline.'),
'B03':('low','Crossed diagonals favor X, but upper and lower loops admit S. No independent stroke establishes a deleted-S/inserted-X history. Keep one uncertain X/S glyph. Une has three low joined movements, including its final e, not merely un.'),
'B04':('low','The final letter of standart is crossed t. The canceled entry has a tilde and triangular remnants under heavy hatching; the glyph and comma remain doubtful rather than resolved. The whole remaining tuple Y,I,tilde-A,sigma-sub-tilde-A agrees.'),
'B05':('high','The complete display has S, pi with small subscript 0, Y, a wavy-over-straight simeq, and the abbreviated caption as transcribed. All signs and label (7) agree; display wrappers alone differ.'),
'B06':('medium','The horizontal-arrow label is a closed round oval with a curved exit, unlike the narrow angular sigma under a straight top bar in the quotient below. This is o in the origin notation continued on scan009. All three arrows, endpoints, p and q labels, I, S and quotient were inspected. On a is compressed but present, and the diagram label is (8).')}
out=[]
for box,(c,e) in ev.items():
 final=first[box].replace(a,b)
 d=dict(box=box,changed='yes' if final!=first[box] else 'no',confidence=c,evidence=e)
 if final!=first[box]:d['final_reading']=final
 else:d['use_first']=True
 out.append(d)
subprocess.run([sys.executable,str(W/'scripts/record_audit.py'),pg],input=json.dumps(out),text=True,check=True)
