from pathlib import Path
import json
w=Path(__file__).resolve().parents[1];page='147_scan058'
c={e['box']:e for e in json.loads((w/'second'/f'{page}_comparison.json').read_text())}
ev={
'B02':'The crossed parenthesized number has a long7 stem and a return favouring2, but the upper numeral strokes merge with several cancellation diagonals. Keep the existing72/71 uncertainty. Et and its detached point remain live.',
'B03':'The whole opening formula confirms both M hats, hat-I with alpha-zero, the underline only beneath G in Gamma, and the live et. The words and numeric genus1 agree; changes apart from the unresolved crossed label are delimiters/braces/apostrophe encoding only.',
'B04':'Number72, one right-pointing arrow, Gamma with underlined G, ornamental fraktur S with hat-I-alpha-zero and parenthetical S4 all agree. Keep the first tikz-cd rendering rather than changing to an inline arrow.',
'B05':'The native crop shows où, genus0, image, underlined Gamma-G, the two S4 symbols, doit pouvoir être, n’importe quel sous-groupe, sauf erreur and Explicitons. Differences are math/apostrophe wrappers only.',
'B07':'The inequality is less-than-or-equal and the numbers are2 and1. After dim the low return ends without a detached black point; the tiny grey grain below/right is unlike the ink. Retain dim without the second reading’s period.',
'B08':'The entire i.e. clause is raised between main baselines and remains inserted; the small sign itself is another raised addition. It has an s-like lower bend and a short upright1, but the first glyph’s upper return also admits cursive delta. Mark s1/delta1 uncertainty instead of certifying either. The separate long connector is not the short1. G remains underlined and the final0/comma remain.',
'B09':'The rounded o/u with its upper accent gives où. Bare G,70, réduit à un sommet isolé and the terminal point agree; only inline delimiters differ.',
'B10':'The abbreviation has two low initial joined m strokes, a small o trace and a tall final d whose low curved exit continues into its dark terminal tip. That tip is not a detached point. Keep dim mod.',
'B11':'The whole phrase reads ambiante2, i.e. codim modulaire1, i.e.; both numerals and the abbreviation points agree. Only math wrappers differ.',
'B12':'The loop has one filled left point. The second figure has an open left ring, a short white gap before the shaft and a filled right point; comma, soit and final point are visible. Both encodings depict these same elements; retain the first.',
'B13':'The upper On trouve les trois cas de dim modulaire replaces the cancelled Dans le cas...sauf1; retain its insertion state. The lower cancellation over sont d’ordre runs into a left-pointing chevron at its right end, with the same long stroke forming its shaft and passing beyond the head. There is no independent numeral2 or less-than relation there. Remove the first-pass doubtful <|2 and record the arrow-shaped cancellation as a deletion mark, not mathematical text. The live ambiante2, dim modulaire1 remains; no detached point after this dim is secure.',
'B14':'The rotated note has MD-graphes, dim mod1, then dim. modulaire ambiante2 and a terminal point. Only math delimiters differ.',
'B15':'The segment has weights3 at lower-left and2 beside the right point, with alpha-zero below the left. The dark right alpha-like label has overlying strokes and a small trailing loop; its cancellation and letters remain qualified in the first reading. The other figure has two crossing shafts without a filled intersection and five ticks a,b,c,d,e, with type(0,5). Keep the first geometry and cancelled doubtful label.',
'B16':'The left loop is closed at a filled point with2 above and parenthesized alpha-zero below. The open self-crossing curve has two lower marks a,b and type(1,2), without a filled crossing. Both TikZ encodings preserve these source elements; retain the first.',
'B17':'The tall crop shows72 beside the middle of the long left brace, with upper/lower curled endpoints. The first traced figure preserves that shape; the second brace macro and math delimiters do not change the reading.',
'B18':'The third left weight is covered by separate diagonal cancellation strokes, so do not make it live. Its remaining triangular/upright form permits1 or4; add4 as an explicit alternative. The right2, parenthesized alpha-zero, both genus labels, filled crossing, two a/b marks and type(1,2) agree. The old genus formula has crossed g/index but visible =1; retain that narrower doubt.',
'B19':'Both ou poids marqué additions are interlinear with curved guides; zéro is live. The next line ends sur le and the bottom starts a singular graphe; no independent terminal s is clear in either article or noun. Keep le graphe and the unresolved au/en at the lower edge; the second reading does not settle that preposition.'}
d={b:{'root_viewed':True,'changed':False,'evidence':e} for b,e in ev.items()}
d['B08'].update(changed=True,final=c['B08']['first'].replace('$s_1$',r'$\unsure{s_1|\delta_1}$'))
d['B13'].update(changed=True,final=c['B13']['first'].replace(r"sont d'ordre $\unsure{<|2}$", "sont d'ordre"))
d['B18'].update(changed=True,final=c['B18']['first'].replace(r'\deleted{\unsure{1}}',r'\deleted{\unsure{1|4}}'))
(w/'second'/f'{page}_root_decisions.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=w/'pages'/f'{page}.tex';t=p.read_text()
for old,new in [('$s_1$',r'$\unsure{s_1|\delta_1}$'),(r"sont d'ordre $\unsure{<|2}$", "sont d'ordre"),(r'\deleted{\unsure{1}}',r'\deleted{\unsure{1|4}}')]:assert old in t,old;t=t.replace(old,new,1)
p.write_text(t)
p=w/'reviewed'/f'{page}.json';r=json.loads(p.read_text())
ch=next(x for x in r['changes'] if x['id']=='058-10');ch.update(final='no independent terminal mathematical sign; the leftward chevron is part of the cancellation stroke',evidence=ev['B13'],crop=f'{page}_second_B13.png',box=[229,1394,1643,1630],confidence='high',kind='text not on the page',error_sheet_kind='text not on page')
ch=next(x for x in r['changes'] if x['id']=='058-18');ch.update(final=r'\deleted{\unsure{1|4}}',evidence=ev['B18'],crop=f'{page}_second_B18.png')
r['doubts']=[x for x in r['doubts'] if x['place']!='cancelled sentence after d’ordre']
for x in r['doubts']:
 if x['place']=='third graph, cancelled digit above left point':x['reading']=r'\deleted{\unsure{1|4}}'
r['doubts'].append({'place':'Small symbol inserted after codim modulaire','reading':r'\unsure{s_1|\delta_1}','alternatives':'s1; delta1','confidence':'low','reason':ev['B08']})
r['unresolved']=[x for x in r['unresolved'] if not x.startswith('Cancelled terminal sign')];r['unresolved'].append('The tiny inserted sign after codim modulaire remains s1/delta1.')
r['notes'][-1]=r['notes'][-1].replace('the independent second reading remains to be performed.','the blind audit is now complete. The terminal <|2 candidate is removed: the crop shows an arrow-shaped end of the cancellation, not a separate mathematical sign. The tiny interlinear s1/delta1 and the cancelled weight1/4 remain doubtful.')
r['root_review_notes']+=' All seventeen differing blind boxes personally viewed. No expected graph weight or codimension formula has supplied a letter. The cancellation-arrow decision supersedes the first-pass tentative inequality.'
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
p=w/'workflow/root_audit_views.json';v=json.loads(p.read_text());v['58']={'crops':[f'{page}_second_{b}.png' for b in ev],'observations':ev};p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
