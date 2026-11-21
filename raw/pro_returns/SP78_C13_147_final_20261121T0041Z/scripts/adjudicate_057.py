from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan057'
c={x['box']:x for x in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B01':'Both baselines have independent cancellation strokes. The short start of the second line has low un-like strokes without a separate tall d; retain un sommet. In the adjective the initial p descender is followed by a rounded o/n run, a tall looped d and two accented short groups. These favour pondérés over the first-pass prédéfini/particulier, but the strike hides the joins and terminal number; retain pondérés|pondéré as doubtful. The ending of déterminée is also crossed, so its final e is not certified. The short final par le remains doubtful; no independent final s can be certified.',
'B02':'The upper p, tall t and terminal els support ponctuels. Beneath the strike the p descender, adjacent upright and dotted i/terminal curved traces allow the tentative un pt iso already recorded, but not its certification. Retain the first reading and closing parenthesis.',
'B03':'The rotated crop shows the MD opening, the long insertion guide at isolé, and codim without a separate final point. No independent comma before i.e. is secure. The oblong after the live 1 is distinct from the lower struck baseline. On that baseline the tall trace before the final 1 can belong to the obscured word; it does not establish a separate less-than-or-equal sign. Keep the existing doubtful de dim|ambiante and placement.',
'B04':'The two filled points have weights4 and1 above, genera0 and1 below, and Gamma formulas to the right. The ornate capital has broad upper/lower S curves with an inner return, supporting fraktur S. Both raised Gamma marks have detached lower dots, hence exclamation marks. The two TikZ encodings depict the same source elements; keep the first.',
'B06':'The crop favours rationnels: initial r, low joining stroke, tall crossed t, a small round trace, two low undulations and final looped l/s; no independent hyphen. The tiny medial bodies and i-dot are still not separately decisive. The blind confident reading does not resolve the existing doubt; keep both alternatives and the underline/paired ticks.',
'B08':'The live upper sauf l-prime is clear. Its f has a very long descender running through the lower cancelled group. That same descender cannot establish an independent q; the low u/n-like group remains ambiguous under the strike. Keep doubtful et un rather than certify the second reading et que.',
'B10':'The first short word has an overworked round opening, a low n and terminal upright/crossing t; its extent is three letters. The next tous, leurs and sommets agree. Retain ont.',
'B11':'The cancelled initial curve is an opening parenthesis, followed by a looped d and low o/n/c traces; this supports (donc rather than tous. The inserted alpha-zero, hat-nu=3, tilde-mu with bare alpha, and final nu-alpha-zero=0 match the first reading.',
'B12':'The inequalities have two strokes, tilde-mu has alpha, and the inserted pour alpha-not-equal-alpha-zero sits above sont. Ne and neq encode the same visible crossed equality; no change.',
'B13':'The cancelled pour and alpha-not-equal have no visible following operand before the live et. The final nu-alpha-zero=0 and point agree. Ne/neq is only encoding.',
'B14':'The first subscript has a distinct small zero; the second has a tightly joined low tail, so alpha-zero versus alpha remains uncertain. Both readings preserve the same alternatives. Keep the first scope and math delimiters.',
'B16':'Both M hats, left G, right g-alpha-zero and hat-I-alpha-zero, simeq and71 agree in the crop. Only external math delimiters differ.',
'B17':'A separate dark descending comma is visible after cardinal4 ou1, above and left of the lower second g. It is not a g accent. Add this comma. Hat-I, bare I, tilde-A and the alpha-zero indices remain unchanged; no final period is supplied.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
d['B01'].update(changed=True,final=c['B01']['first'].replace('est déterminée',r'est \unsure{déterminée|déterminé}').replace(r'\unsure{prédéfini|particulier}',r'\unsure{pondérés|pondéré}'))
d['B17'].update(changed=True,final=c['B17']['second'])
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text()
for b in ['B01','B17']:
 assert c[b]['first'] in t,b;t=t.replace(c[b]['first'],d[b]['final'],1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text());ch=r['changes'][0];ch.update(final=r'avec un sommet \unsure{pondérés|pondéré}',evidence=ev['B01'],crop=f'{page}_second_B01.png',box=[320,45,1605,205])
r['changes'].append({'id':'057-17','place':'Final margin: comma after cardinal4 ou1','C':r'de cardinal $4$ ou $1$ suivant que','H':r'de cardinal $4$ ou $1$ suivant que','final':r'de cardinal $4$ ou $1$, suivant que','evidence':ev['B17'],'crop':f'{page}_second_B17.png','box':[1155,2187,1675,2350],'confidence':'high','against_C':True,'against_H':True,'kind':'omission','marked_in_H':False,'error_sheet_kind':'omissions','consequential':False})
r['doubts'][0].update(reading=r'\unsure{pondérés|pondéré}',alternatives='First pass: prédéfini/particulier; blind second: pondérés; the final number is obscured',reason=ev['B01'])
r['doubts'].append({'place':'Cancelled opening, déterminée ending','reading':r'\unsure{déterminée|déterminé}','alternatives':'Final e not separately certified','confidence':'low','reason':'The cancellation crosses the terminal small letters after the accented group; retain both endings.'})
r['unresolved'][0]='Cancelled opening: déterminée/déterminé and pondérés/pondéré remain uncertain; the latter supersedes first-pass prédéfini/particulier on the new crop.'
r['notes'][-1]=r['notes'][-1].replace('the independent second reading remains to be done.','that was the first-stage count. The completed blind audit supersedes the tentative head adjective with pondérés|pondéré and adds the visible comma after4 ou1; it also marks the crossed déterminée ending as uncertain. The original first TSV is preserved unchanged.')
r['root_review_notes']+=' Blind audit: all thirteen differing boxes personally viewed. The adjective and comma are updated; unresolved letter shapes, insertions and decorations remain explicitly qualified.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['57']={'crops':[f'{page}_second_{b}.png' for b in ev],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
