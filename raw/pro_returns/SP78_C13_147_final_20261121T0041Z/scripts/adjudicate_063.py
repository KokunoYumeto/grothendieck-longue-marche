from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan063';c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B01':'The first underbrace begins beneath U, after chi and its opening parenthesis, and stops beneath the group argument. The second also spans the arguments rather than the entire chi term. Move both underbraces inside the parentheses without changing their numerical annotations. Hat-M, an exponents, lower exclamations,-1/24,+1/8 and terminal1/12 with point agree.',
'B02':'The raised compact quotation pair precedes the long-descender g of groupe; de has a looped d. Curly versus prescribed backtick encoding only differs.',
'B03':'The capital G, tall t/h sequence and joined end of Grothendieck agree; the two raised closing quotation strokes are retained in the prescribed apostrophe convention.',
'B04':'The marginal words, double-stroked Z,1/6, Spec Z and ellipsis agree. The compressed group after pour does not decisively separate an intervening me or the final ending, so retain the existing pour dispenser/pour me dispenser doubt. In native orientation the number has a crossed7 with a long descender below its middle bar, followed by9:79, independent of the sloping note. The brace is present.',
'B05':'The M shoulder is retraced, but no independent angular accent is separable above it; do not add a cancelled hat. Its dotted exclamation and0,4 are clear. The first U index remains a crowded oval/comma group allowing0,4/3,4. The T(1) brace, quoted Tate, doubled E1 and augmentation1 agree.',
'B06':'The cancelled area retains fraction-like strokes, parentheses and fragments consistent with the first tentative1/24(T(1)-2), but not every symbol is exposed. Retain that whole-expression doubt rather than replacing surviving ink by an uninformative question mark. The subsequent live1/4(T(1)-2),1/12,1/8 and final expression agree.',
'B07':'The cancelled trial visibly starts with1/24 and contains T/parenthesis and plus-like surviving strokes; its full sequence remains qualified. All live terms, the initial hat and the three later fractions agree. Do not resolve the cancelled formula.',
'B08':'After égale the short resp group has a small raised t. It is followed by two vertically separated colon-like marks, with no separately readable à. The reader’s later addendum also withdraws that à. Retain the first text and all three numerical values.',
'B09':'The underlined Cas de/des ends in a compressed low return after d, so the shorter blind de does not certify absence of s. Retain the doubt. Both index ones, hat and point agree.',
'B10':'The divider-crossing arrow, its1, three other labels, two points and closed right loop agree. The lower-left label has a looped upper entry and a long horizontal base. The first underlined1 remains preferred, but the loop admits the blind g alternative; mark this small glyph uncertain without changing the drawing.',
'B11':'The underline ends after au dessus de at the approach to the double-stroked Z; the bracketed1/2 and parenthesis are visible. Fraction style and math wrappers alone differ.',
'B12':'All three dark accents above M are crossed; their former wedge shape is still not fully exposed. Retain the three cancelled-accent doubts. The middle prime, final dotted exclamation,1,1 and literal1,4 indices, right arrow and accented déf agree.',
'B13':'The two crossed accents remain doubtful rather than certified wedges. The prime, gerbe, groupe constant and plus/minus1 agree. The short characteristic abbreviation has c and a low continuation before its point, with no separate r body: retain ca. The literal1,4 remains.',
'B14':'The live coefficient has a large2-like contour with an internal horizontal stroke; the2/1/2 layering doubt remains. The cancelled tail exposes a doubled E and fraction/sign fragments consistent with the qualified first transcription but is not wholly recovered. The live T(1) is physically below the tail with no connector fixing its exact scope; retain the positional underset and its documented uncertainty.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
a=r'\underbrace{\chi_!(U^{\mathrm{an}}_{0,3},\mathfrak S_4)}_{-1/24}';z=r'\chi_!(\underbrace{U^{\mathrm{an}}_{0,3},\mathfrak S_4}_{-1/24})'
a2=r'\underbrace{\chi_!(\{0,1,\infty\},\mathfrak S_4)}_{1/8}';z2=r'\chi_!(\underbrace{\{0,1,\infty\},\mathfrak S_4}_{1/8})'
d['B01'].update(changed=True,final=c['B01']['first'].replace(a,z).replace(a2,z2))
d['B10'].update(changed=True,final=c['B10']['first'].replace(r'\underline1',r'\underline{\unsure{1|g}}'))
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text()
for x,y in [(a,z),(a2,z2),(r'\underline1',r'\underline{\unsure{1|g}}')]:assert x in t;t=t.replace(x,y,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text());row=next(x for x in r['changes'] if x['id']=='063-16');row.update(final=d['B10']['final'],confidence='medium');row['evidence']+=' Blind audit: '+ev['B10']
r['changes'].append({'id':'063-30','place':'Opening characteristic formula, spans of the two underbraces','C':a+'; '+a2,'H':a+'; '+a2,'final':z+'; '+z2,'evidence':ev['B01'],'crop':f'{page}_second_B01.png','box':[260,15,1680,228],'confidence':'high','against_C':True,'against_H':True,'kind':'insertion or placement','marked_in_H':False,'error_sheet_kind':'insertions put in wrong place','consequential':False})
r['doubts'].append({'place':'Diagram77, underlined label below isolated point','reading':r'\underline{\unsure{1|g}}','alternatives':'1;g','confidence':'low','reason':ev['B10']});r['unresolved'].append('Diagram77 lower-left underlined glyph:1 favored, g remains possible.')
r['notes'].append('Blind audit: all fourteen differing boxes were personally viewed, plus a native-orientation crop confirming79. Both initial underbraces now span their arguments as drawn. The looped lower graph label remains uncertain between underlined1 and g; the cancelled formulas and accents remain qualified. The independent reader’s B08 addendum withdrew an unsupported à; the first colon-only reading stands.')
r['root_review_note']=r.get('root_review_note','')+' All fourteen differing second boxes and the native-orientation number crop viewed; brace spans corrected and one small-label doubt added.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['63']={'crops':[f'{page}_second_{b}.png' for b in ev]+[f'{page}_second_root_B04_number.png'],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
