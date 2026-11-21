"""Root adjudication after all13 differing crops and full diagram inspection."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan047';r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,e,changed=False):dec[b]={'decision':'retain first with local doubt' if changed else 'retain first','changed':'yes' if changed else 'no','evidence':e}
d('b01','The two dark uprights are the authorial 11. The wrapper records its role; no numeral differs.')
d('b02','The small lower index is a continuous upright with a darker lower body, not a separately dotted i. The Delta-one notation recurs in the whole formulas; the explicit 1 remains.')
d('b03','Every object, coordinate, index, brace and relation agrees; only math delimiters differ.')
d('b04','The relation has two parallel shafts with heads at both ends. Both inequalities have lower strokes. Le/leq and display delimiters are equivalent syntax; the comma between x=y and i≤j is present.')
d('b05','The compressed -ant strokes and final crossed t are part of live étant, not a cancelled word. Both blind and first readings now agree on the text; only math delimiters differ.')
d('b06','The two factors, subscripts and intervening product sign agree. The dense central crossing is the product sign, not a struck object; delimiters are representational.')
d('b07','The final short word has a low initial curve rising to a tall uncurling stem and a long rightward return, closely resembling the clear et in b12. Prefer et while retaining de as alternative. The awkward resulting wording is not repaired from grammar.',True)
d('b08','After the q descender the low u/e bodies continue to a terminal s-shaped return, supporting plural topologiques. Two raised closing quote strokes and the following dash are clear; dash length in TeX is representational.')
d('b09','The d loop is clear, but the following low a/n/e bodies are strongly contracted into a nearly level run. Dans remains preferred; des is now explicit rather than ruled out by grammar.',True)
d('b10','The first body after the formula has an open c followed by o and low m strokes, then a distinct line-end hyphen. The next baseline continues me; au- does not account for that open first c.')
d('b11','The two diagonals establish the final X. A left loop and lower basin suggest a possible older U-like form, but no independent cancellation layer establishes a readable old U rather than retracing. Keep X and retain the existing documentary doubt about pen history; do not invent a certain deleted glyph.')
d('b12','The oval source label has no separate a-only stem and is explicitly linked to (6), whose sigma is established by (7)a on scan046. Retain that same notation; b and the reference agree.')
d('b13','The full diagram has the same source sigma, target b, fibre product over X_Delta0, one horizontal arrow and two independent cap-shaped relations above the triple and double products. The alternative array placement of caps changes no reading.')
t=t.replace('``objet ordonné de',r'``objet ordonné \unsure{et|de}').replace('catégorie, dans la catégorie',r'catégorie, \unsure{dans|des} la catégorie')
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
r['changes'].append({'id':'r15','place':'after objet ordonné','c':'de','h':'de','final':r'\unsure{et|de}','evidence':dec['b07']['evidence'],'confidence':'medium','kind':'misread word','error_category':2,'diff_c':True,'diff_h':True,'marked_h':False,'crop':f'crops/second_{p}_b07.jpg','box':boxes['b07'],'consequential':''})
r['doubts'] += [{'place':'after objet ordonné','reading':'et','alternatives':'de','confidence':'medium','reason':dec['b07']['evidence']},{'place':'after catégorie comma','reading':'dans','alternatives':'des','confidence':'medium','reason':dec['b09']['evidence']}]
r['notes'].append('scan047.N9. Blind adjudication reopens two compressed function words. The first now favors et with de as alternative, from its similarity to the clearly written et beside sigma and b; the syntactically smoother de is not imposed. Dans/des remains open in the next phrase. The final X is secure, but its looped pen history is not promoted into a definite deleted U. The full diagram and both sigma selections stand.')
finals={'b07':r"``objet ordonné \unsure{et|de}",'b09':r'catégorie, \unsure{dans|des}'}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'medium'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
