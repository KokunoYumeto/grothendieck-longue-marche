from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];page='148_scan002'
p=root/'pages'/f'{page}.tex';t=p.read_text()
subs=[(r'\deleted{\unsure{en}}',r'\deleted{\unsure{en|on}}'),
 (r'\deleted{\unsure{\mathrm{bijec.}}}',r'\deleted{\unsure{\mathrm{bijec.}|\mathrm{diag}}}'),
 (r'\text{ de Aut qui induit}',r'\text{ \unsure{de|des} Aut qui induit}'),
 (r'\deleted{\unsure{\mathbb U_i}}',r'\deleted{\unsure{\mathbb U_i|(\mathbb U_i)|(T_i)}}'),
 (r'$T_i=$ comp.',r'$T_i\unsure{=|:}$ comp.'),
 (r'$\unsure{i}$',r'$\unsure{i|\varphi}$')]
for a,b in subs:
 assert a in t,a
 t=t.replace(a,b)
old=r'\draw (bottom.north east) -- (right.south west) node[midway,below right] {$T^!(X)$};'
extra=r'''
% Short terminal returns are drawn; their arrowhead status remains uncertain.
\draw (left.south east) -- ++(-.02,-.13);
\draw (right.south west) -- ++(-.15,-.035);
\node at (-1.24,-.4) {$\unsure{}$};
\node at (1.27,-.39) {$\unsure{}$};'''
assert old in t;t=t.replace(old,old+extra);p.write_text(t)
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text())
for c in r['changes']:
 for a,b in subs:c['final']=c['final'].replace(a,b)
 if c['id'].endswith('-01'):c['evidence']+=' On is retained beside en as a candidate under the same cancellation; the preferred reading and deletion state are unchanged.'
 if c['id'].endswith('-02'):c['evidence']+=' The crossed word also permits diag; the letter centres remain covered. The following de/des ending is now explicitly doubtful, with de retained first.'
 if c['id'].endswith('-09'):
  c['final']=c['final'].replace(old,old+extra)
  c['evidence']+=' The blind crop exposes a small return at each upper endpoint of the two lower diagonals. Their head status is now questioned in place; five objects and five shafts remain. The return strokes are drawn directly.'
  c['confidence']='medium'
 if c['id'].endswith('-14'):c['evidence']+=' The outer curve permits a parenthesis and the heavy central strokes also admit a T-like capital; the parenthesized U_i/T_i candidates are added without resolving the crossed group.'
 if c['id'].endswith('-15'):
  c['final']=c['final'].replace(r'$T_i=$',r'$T_i\unsure{=|:}$')
  c['evidence']+=' The upper mark of the following separator is point-like and the lower is a short horizontal dash; equality/colon is now left open.'
  c['confidence']='medium'
 if c['id'].endswith('-16'):c['evidence']+=' The detached dotted upright has a small closed lower loop and descending stem; varphi is added as a possible form beside i.'
for d in r['doubts']:
 for a,b in subs:d['reading']=d['reading'].replace(a,b)
 if d['place']=='L04 struck word':d['alternatives']='en; on; another cancelled short word'
 if d['place']=='L06 struck word':d['alternatives']='bijec.; diag; another abbreviation'
 if d['place']=='Product before T_i':d['alternatives']='U_i; parenthesized U_i; parenthesized T_i'
 if d['place']=='Below boundary note':
  d['reading']=r'\unsure{i|\varphi}';d['alternatives']='i; varphi-like dotted loop and stem; correction to the preceding word'
r['doubts'] += [dict(place='definition, before Aut qui induit',reading=r'\unsure{de|des}',alternatives='de; des',confidence='medium',reason='The short terminal return is compressed; a separate final s cannot be isolated securely.'),dict(place='large lattice, upper ends of two lower diagonals',reading='directly drawn terminal returns with in-place question marks',alternatives='pen returns; small incomplete heads towards the lateral nodes',confidence='medium',reason='Each endpoint has a short return, but separate opposed head arms are not exposed clearly.'),dict(place='boundary note, separator after T_i',reading=r'\unsure{=|:}',alternatives='equality sign; colon',confidence='medium',reason='The upper mark is point-like, while the lower mark is a short dash.')]
r['notes']+=' Blind audit leaves the recurring looped group letter at the same preferred fraktur-S reading with its local uncertainty. The long upright beside the torus U continues into the t of torique on the baseline below; it is not supplied as a new subscript. The lower lattice endpoint returns are reproduced with uncertain head status. Local alternatives are added within crossed text, at the de/des ending, at the boundary-note separator and at its detached dotted glyph. The written can! and contracted défini. are retained. No mathematical claim was checked in this audit.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text())
ev={
'B02':('The annotation reads i.e. torseur sous, followed by U and the set of z with |z|=1. The long upright beside U continues down into the tall t of torique in the contextual sentence; no separate subscript 1 is added. The surrounding curved attachment and low V bend are retained.','high'),
'B03':('The X is overworked. The compact autom has no final point. The short word before resp. is crossed and permits en/on; the crossed group after Aut permits bijec./diag. The short following de/des return is now doubtful. Orientation, structures toriques and all remaining text are retained.','low'),
'B04':('The initial d-loop, accented e, low repeated strokes and g descender support dévissage. All words agree; operatorname/mathrm serialization differs.','high'),
'B05':('The subscript star has merged arms, and the short stroke above X has a thick right end, so both local doubts remain. The recurring outer arch with lower curl is retained as the same tentative fraktur S. Four upper blocks and the Aut annotation are present.','medium'),
'B06':('The four objects agree. The rightmost outer arch and inward lower curl recur on this page; the first preferred fraktur-S reading and its uncertainty are retained.','medium'),
'B07':('The mark after can has a detached upright and a separate dark lower point, with no transverse t bar. Droit has an exposed d loop, connected roi and terminal tall t; the insertion and its attachment above R^I remain.','high'),
'B08':('The lower argument has a closed left loop and crossing right tail; alpha is retained against the open X above it. The target has one detached raised stroke and no clear exclamation dot. The equation, bracket and rightward lower map agree.','medium'),
'B09':('The upper connector has a curved left end; the left vertical merges with crossed lettering above and has a curved lower return. The right vertical has an upper head and lower hook, and the lower horizontal has a left hook and right head. Cocart ends in a tall crossed t. The two dots, two inclusion signs and the unresolved lambda/crossed-2 strokes are retained. The cancelled phrase remains uncertain.','low'),
'B10':('NB is underlined. The product starts with a plain T having a broad top bar and long curved vertical; no distinct script alphabet is established. Parentheses and lower i-in-I agree, and the recurring group letter retains its existing local doubt.','medium'),
'B11':('The next-line short word before fait has a low n/e run without a separate apostrophe or a-loop. Ne is retained. The group before la remains dont; défini. ends in a short vertical and a dark point, without written -tion. The rest of the diagonal note and underlined s agree.','high'),
'B12':('Five nodes and five shafts were recounted. The two lower diagonal upper ends have short returns, whose arrowhead status is now marked uncertain while their strokes are drawn. The top three shafts, all five labels, both side braces and the Aut annotation remain.','medium'),
'B13':('The crossed (X), quotient by Z^I, accented déf above equality, SUT(X), downward shaft, lower T^!(X) times U^I, right brace, group label and wavy lower separator are all visible. The cancellation stays explicit.','medium'),
'B14':('The sequence has five objects. Its last connector is one plain horizontal stroke ending bluntly, so no final arrowhead is supplied. The overworked T-like target retains its uncertain earlier looped form and deletion state.','low'),
'B15':('The final short de-like group after pt is crossed by a thick horizontal stroke through its body. It remains deleted and uncertain; the preceding two prose lines agree.','medium'),
'B16':('The full product and lower index agree. Dense crossing obscures the preceding object; its exposed outer curve permits a parenthesized U_i or T_i, now retained beside the former U_i candidate.','low'),
'B17':('The separator after T_i has a point-like upper mark and short lower dash, leaving equality/colon open. The detached lower glyph has a dot, closed loop and descending stem, permitting i/varphi. Comp. connexe (torique), partial X and d’indice i agree.','low'),
'B18':('The embedding has a left hook and right head. Its raised deleted mark remains doubtful. Déduise remains preferred, with the compressed s/r alternative kept open.','medium'),
'B19':('The cancelled upper mark, starred lower index, underlined s, wedge with Z^I beneath, R^I and simeq agree. Differences are only math layout and underline serialization.','medium')}
choices=[]
for d in comp['differences']:
 b=d['box'];final=d['first']
 for a,z in subs:final=final.replace(a,z)
 if b=='B12':final=final.replace(old,old+extra)
 it=dict(box=b,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[b][0],confidence=ev[b][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_b',choices=choices),ensure_ascii=False,indent=2)+'\n')
