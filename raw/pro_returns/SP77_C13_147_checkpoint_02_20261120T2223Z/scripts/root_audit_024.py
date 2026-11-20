from pathlib import Path
import json,csv
W=Path(__file__).resolve().parents[1];n=24
with (W/'second/147_scan024_comparison.tsv').open() as f:comp={r['box']:r for r in csv.DictReader(f,delimiter='\t')}
changes=[(r'\mathcal M','M'),(r'\mathcal{M}','M'),(r'\text{relatives sur }',r'\text{\unsure{relatives|relives} sur }'),(r'\text{égal à }',r'\text{égal \unsure{à|:} }'),('On suppose',r'On \unsure{suppose|supp\textsuperscript{se}}')]
def revised(s):
 for a,b in changes:s=s.replace(a,b)
 return s
p=W/'pages/147_scan024.tex';p.write_text(revised(p.read_text()))
rp=W/'records/147_scan024.json';r=json.loads(rp.read_text())
for c in r['changes']:c['final']=revised(c['final'])
for q in r['notation']:q['form']=revised(q['form'])
r['doubts'] += [
 {'place':'display (24), word before sur','reading':r'\unsure{relatives|relives}','alternatives':'full relatives / compressed relives','confidence':'medium','reason':'The r-e-l beginning is clear, but the narrow intervening strokes do not securely show the complete at sequence. The blind reading raised a possible abbreviated or contracted form.'},
 {'place':'display (24), sign after égal','reading':r'\unsure{à|:}','alternatives':'à / colon','confidence':'medium','reason':'Two short marks survive; the lower body is too compressed to certify an a rather than punctuation.'},
 {'place':'left margin, word after On','reading':r'\unsure{suppose|supp\textsuperscript{se}}','alternatives':'suppose / abbreviated supp with raised se','confidence':'medium','reason':'The paired long descenders are clear; the compressed ending lies high on the slant and does not securely distinguish a complete word from a raised ending.'}]
r['unresolved']=['Display (24): full or contracted relatives; à or colon after égal.','Margin: suppose or abbreviated supp with raised se.']
r['audit_note']='The blind pass led to three explicit local doubts: the compressed word relatives in (24), the sign after égal, and the ending of suppose in the margin. The spiral-headed base S remains calligraphic, while the moduli capital is consistently rendered plain M: a swept foot is a pen variant, not a separate alphabet. The raised l in gén-l has no independent crossbar. The two diagonals of Z support the double-stroked letter. The margin separator is a layout rule, represented by margin placement rather than a separate mathematical drawing.'
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ev={
'024-B02':'The base S has a closed spiral head and lower hooked lobe, unlike a plain S; retain calligraphic S. The raised anabélien phrase, underline, 2g+nu>=3 and its curved attachment are independently visible and agree.',
'024-B03':'The formula number has a 2 followed by the angular 4 form; retain 24. The S symbols have spiral heads. M has two peaks and a swept foot, the same moduli capital as later straight-foot forms, rendered plain M. The complete expression is checked; the compressed relatives and sign after égal are now explicitly doubtful. Spacing and prose/display wrappers do not supply source differences.',
'024-B04':'The m humps, two dotted i positions, low r, tall descending f, q loop with long descender and ending ue support mirifique letter by letter. Retain the first reading without a new doubt.',
'024-B05':'On, the two p descenders, inequality 2g+nu>=3 and cas anabélien are visible. The high compressed ending after supp may be a raised se; add that doubt. The long vertical stroke separates the note from the text and is accounted for as margin layout; clipped neighbouring material is not new source text.',
'024-B06':'The raised final stroke has an upright and a small foot, with no separate transverse bar. It favours l, not t. Retain the written gén with superscript l and comma.',
'024-B07':'The hat appears only on the first M; the replacement M has no exponent. Both Z diagonals are distinct, supporting mathbb Z. The terminal stop has a heavy head and lower tail, retained as the first semicolon reading. The struck phrase remains readable from the surviving f/b/r/e/s, g/e/o/m and c/o/n/n/e/x/e/s shapes across the single rule. The blind uncertainties do not expose another letter. Adopt the consistent plain M typeface; retain both underlines and the replacement attachment.',
'024-B09':'The base symbols have the spiral-headed form, so retain calligraphic S. The hat, lower g/nu, mapping bar/head and parenthesized Sch are visible. Render the recurring M as plain Latin M, with no change to its index or hat.'}
plan={b:{'decision':'retain first with stated corrections' if revised(comp[b]['first'])!=comp[b]['first'] else 'retain first','evidence':e,'final_reading':revised(comp[b]['first']),'changed':'yes' if revised(comp[b]['first'])!=comp[b]['first'] else 'no','crop':f'crops/147_scan024_audit_{b.split("-")[1]}.jpg','viewed_by':'root'} for b,e in ev.items()}
(W/'review/024_reconciliation_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
