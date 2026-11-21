from pathlib import Path
import json,csv
R=Path('/workspace/scratch/d12e26a9cd50/SP93_C13_151_work');p=R/'reports/151_scan020.json';d=json.loads(p.read_text());tp=R/'reports/151_scan020.tex';t=tp.read_text()
rows=list(csv.DictReader((R/'second/151_scan020_comparison.tsv').open(),delimiter='\t'));f={r['box']:r['first'] for r in rows};b={r['box']:[int(r[k]) for k in ('x0','y0','x1','y1')] for r in csv.DictReader((R/'second/151_scan020_boxes.tsv').open(),delimiter='\t')};rev={};reps=[]
def change(box,old,new):
 global t
 assert old in t,(box,old)
 t=t.replace(old,new,1);rev[box]=rev.get(box,f[box]).replace(old,new);reps.append((old,new))
num=r'\mspage{\begin{tikzpicture}[baseline=-.5ex]\node at (0,0) {3};\draw(-.29,.17)..controls(-.34,-.39)and(.34,-.39)..(.29,.17);\end{tikzpicture}}'
change('B003',r'\mspage{\textcircled{3}}',num)
change('B003',r'\node at (1.55,-1.04) {$\unsure{\delta|\partial}_0$};',r'\node at (1.55,-1.04) {$\unsure{u|v}\,\unsure{\delta|\partial}_0$};')
change('B003',r'\node at (4.75,-.16) {$p_{31}$};',r'\node at (4.75,-.60) {$p_{31}$};')
old='\n'.join(f['B003'].splitlines()[16:22])
start=f['B003'].index(r'\draw[->,line width=.65pt]');end=f['B003'].index(r'\end{tikzpicture}',start)
old=f['B003'][start:end]
new=r'''\draw[->,line width=.65pt] (4.05,-.83)..controls(4.26,-1.12)and(4.85,-1.16)..(5.30,-1.10);
\draw[->,line width=.65pt] (3.63,-.82)..controls(3.85,-1.48)and(4.95,-1.57)..(5.57,-1.30);
\draw[->,line width=.65pt] (3.21,-.65)..controls(3.55,-2.02)and(5.65,-2.03)..(6.50,-.57);
\node at (4.95,-2.03) {$\unsure{\delta|\partial}_1,\unsure{\delta|\partial}_2,\unsure{\delta|\partial}_3$};
'''
change('B003',old,new)
change('B004',r'\draw(2.97,1.10)--(3.10,-1.28)..controls(3.10,-1.54)and(2.82,-1.57)..(-2.23,-1.55);',r'\draw(2.97,1.10)--(3.10,-.20)..controls(3.10,-.45)and(2.82,-.48)..(-2.10,-.40);')
change('B004',r'\draw(-2.23,-1.55)--(-2.23,1.15);',r'\draw(-2.23,-.30)--(-2.23,1.15);')
change('B007',r'\mathbb E_1\arrow[r]\arrow[d]\&\mathbb E_2\arrow[d]',r'\mathbb E_1\arrow[r]\arrow[d,no head,to path={([xshift=3pt,yshift=-4pt]\tikztostart.south)--(\tikztostart.south)--(\tikztotarget.north)--++(-3pt,4pt)\tikztonodes}]\&\mathbb E_2\arrow[d]')
# The complete page already uses explicit cancellation paths without the invalid outer deleted wrapper.
change('B012',r'\draw(-.83,.28)--(.27,.25)--(.25,-.22)--(-.84,-.22)--(-.83,.16);',r'\draw(-.83,.28)--(.27,.25)--(.25,-.15)--(.17,-.13);\draw(.21,-.22)--(-.84,-.22)--(-.83,.16);')
change('B012',r'\fill(-.43,-1.02)circle(.05); \fill(.43,-1.02)circle(.05);',r'\fill(-.43,-1.02)circle(.05); \fill(.43,-1.02)circle(.05);'+'\n'+r'\draw(-.40,-.40)--(-.39,-.65)..controls(-.34,-.79)and(-.24,-.70)..(-.20,-.63);')
change('B012',r'--(.36,-1.17)..controls(.28,-1.36)and(.40,-1.34)..(.52,-1.16);',r'--(.36,-1.17)..controls(.28,-1.36)and(.40,-1.34)..(.52,-1.16)'+'\n'+r'--(1.46,.26)..controls(1.58,.40)and(1.68,.34)..(1.57,.14)--(1.03,-1.30)--(1.07,-1.20);')
change('B015',r'\draw[<-] (.40,0)--(1.15,0); \draw(1.24,0)--(2.88,0);',r'\draw[<-] (.40,0)--(2.15,0); \draw(2.30,0)--(2.88,0);')
change('B015',r'\draw(0,-1.38)--(0,-.39)..controls(0,-.22)and(.17,-.22)..(.17,-.40);',r'\draw(0,-1.38)--(0,-.40);\draw(-.17,-.37)..controls(-.12,-.15)and(.14,-.16)..(.17,-.37);')
change('B015',r'\node at (1.65,-1.43) {$\unsure{\delta|\partial}_1$};',r'\node at (1.65,-2.10) {$\unsure{\delta|\partial}_1$};')
# Keep the audit snippet in the same valid wrapper used in the page.
rev['B012']=rev['B012'][len(r'\deleted{'):-1]
for c in d['changes']:
 for old,new in reps:c['final']=c['final'].replace(old,new)
updates={
'020-C02':('B003',num,'The numeral 3 sits in a deep cup open across the top; it is not enclosed by a complete circle. The open course is now drawn.',True),
'020-C03':('B003',rev['B003'],'Three straight left arrows have p12, p23, p31. Below them, two inner rightward curves end near the centre, whereas only the outer curve reaches towards X3. The three inclusion labels stand in one comma-separated horizontal group below the curves. The thin independent upper return remains. A short unresolved u/v-like trace precedes delta0; no deletion state is asserted for it.',True),
'020-C05':('B004',rev['B004'],'The frame lower edge passes above the lower X1, across its upward hooked shaft and diagonal arrow. Its left upright is separated from both adjoining horizontal courses. The p0sigma relation is vertical above p1, the group glyph is outside, and the leader descends to iso with three question marks.',True),
'020-C13':('B007',rev['B007'],'Four doubled E objects have indices 1,2,2,3. Both horizontal arrows and the right downward arrow have full heads. The left vertical has only a short right-hand branch at the top and a short left-hand branch at the bottom; neither end is completed to a conventional chevron.',True),
'020-C18':('B012',rev['B012'],'There are three upper and two lower filled points. The inner rectangle has a lower-right gap. A short vertical curved return between the ovals is visible independently of the long oblique cancellation. A final far-right rising and descending cancellation course is restored. The numerous crossings do not establish three independent mapping arrows.',True),
'020-C21':('B015',rev['B015'],'The left vertical has a separate rounded cap without a complete chevron, and a lower hook; the right has a full upward head and lower hook. K is capital. The top shaft has a gap to the right of p12. The lower delta1 label lies below its arrow, not above it. The irregular surrounding contour is closed.',True)}
for cid,(box,final,ev,dc) in updates.items():
 c=next(x for x in d['changes'] if x['id']==cid);c.update(final=final,evidence=ev,differs_C=dc,crop=f'crops/151_scan020_second_{box}.png',box=b[box])
d['changes'].append(dict(id='020-A07',place='Top system, short trace before delta0',C='',H='',final=r'\unsure{u|v}',evidence='A short upright and shallow joined trough survive immediately left of delta0. They are absent from both witnesses. Their character and possible overwritten state cannot be settled; u/v are only local shape candidates.',confidence='low',kind='omission',crop='crops/151_scan020_second_B003.png',box=b['B003'],differs_C=True,differs_H=True,marked_in_H='no',consequential=''))
d['doubts'].append(dict(place='Top system, trace before delta0',reading=r'\unsure{u|v}',alternatives=['u-like remnant','v-like remnant','unresolved earlier label fragment'],confidence='low',reason='A short joined trace precedes the clear looped inclusion label; neither its original letter nor any cancellation state is securely separable. It is preserved as uncertain text, not assigned a map role.'))
d['notes']=[x.replace('dark encircled 3','dark 3 within a cup open at the top').replace('Retaining an explicitly uncertain deleted wrapper','Retaining the explicit uncertainty around the drawn strip') for x in d['notes']]
d['notes'].append('Second-reading adjudication corrected the open foliation cup, short inner inclusion curves and comma-separated labels, triangle frame above the lower X1, incomplete ends of the unlabeled E square, cancelled-sketch gap/short return/final cancellation course, and placement of delta1 below the lower circled square. The short trace before delta0 remains unresolved. No mathematical correction was inferred from these diagrams.')
e={
'B001':'The three printed lines and two rules agree. Typeface wrappers do not alter the wording.',
'B002':'The first looped descender favours p/rho; the final oval with right descender favours q/sigma. Crossings obscure both heads, so the existing alternatives remain; neither f nor g is securely exposed.',
'B003':'The cup is open above 3. Two inner curves stop centrally, the outer reaches X3, and the three labels form one comma-separated group below them. These placements are corrected. The tiny trace before delta0 is preserved as an unresolved u/v-like fragment; group and inclusion alphabet doubts remain.',
'B004':'The lower frame edge crosses the two ascending shafts above the separate lower X1. Its left vertical is detached at both ends. These courses replace the oversized connected frame; the vertical relation, external group glyph, iso leader and three questions agree.',
'B005':'The closed left bowl/right descender of q and the separate two-lobed 3 settle q3. Both shafts have paired heads, id has subscript X1, and the bent stroke above the chain is independent. Existing reading retained.',
'B006':'Both maps have paired heads. Parenthesized p1 and p0 sit above the two X2 factors, and four separate strokes frame only the first part. The two readings differ in drawing syntax.',
'B007':'Short single branches occur at opposite ends of the left vertical. Both conventional downward and bidirectional chevrons overcomplete the ink, so the actual partial ends are drawn. Objects and the other three arrowheads agree.',
'B008':'Three filled points are visible. The lower brace spans the first two with downward cusp; the upper spans the last two with upward cusp. First drawing retained.',
'B009':'The right vertical ends in a single leftward foot, without a second head wing. All K letters have tall uprights and angular arms, and the left prime is detached. First drawing retained.',
'B010':'The top course returns left in a blunt curl without a full arrowhead. The outer oval is open at the upper right. Both verticals have upward heads and lower hooks; the lower shaft points left and returns at the right. The retraced lower-left index remains unsure2, and the looped labels remain delta/partial doubts.',
'B011':'The top shaft has only its upper terminal wing. Its label ends in a retraced 3/2 form and the left K index is filled; both doubts stay. The right prime is visible, and the other three heads agree.',
'B012':'The five points and long crossing zigzag agree. A lower-right gap in the inner rectangle, a short curved vertical between the ovals and a final far-right cancellation course are added. The short curve is not promoted to a full downward arrow. Explicit cancellation paths already replace the invalid outer deletion wrapper.',
'B013':'Both readings show three upper and two lower points, the inner rectangle and open outer courses. The small curl between rows is already preserved; the isolated speck is not a sixth point. First retained.',
'B014':'The two dark point-like swellings and retraced strip are visible, with open corners of the three-sided frame. Retracing alone does not settle cancellation. The page retains its uncertainty around the graphic; the prior invalid deletion wrapper was only a syntax issue.',
'B015':'The lower delta1 label lies below its shaft. The top gap is right of p12, and the left vertical has a distinct rounded cap. These placements are corrected; capital K, its prime, the right head, lower hooks and closed surrounding course remain.',
'B016':'X1 has a tall narrow index, and X2 remains readable beside the paper abrasion. K is capital, the filled left index stays unsure1, and the independent S-shaped stroke does not settle the group alphabet. The separate lower L course and four arrows agree.',
'B017':'The cancelled E-like start is crossed by a continuous zigzag; the apparent lower-right 3 cannot be isolated from its return, so no definite subscript is supplied. The five prose lines agree, with the established group and inclusion doubts retained.',
'B018':'The small diagram has an upper hook and curved leftward return labelled capital K2. The cancelled starting glyph remains obscured; delta/partial and its small2 are uncertain. The replacement is raised above/right of the struck pts fixes; its crowded letters do not securely yield ensembles. Existing alternatives and the final identity without period remain.',
'B019':'Both doubled E signs, indices1/2, upper hooked rightward arrow and curved left return agree. Shift parameters only alter diagram layout.',
'B020':'The final small upright with crossbar belongs to the pen-test pattern and is preserved graphically; its isolated position does not establish a textual t. The first drawing retains the continuous zigzag and separate surrounding dots/strokes.'}
m={k:dict(changed=k in rev,evidence=v) for k,v in e.items()}
for k,v in rev.items():m[k]['final']=v
(R/'reviews/151_scan020_manual.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');tp.write_text(t)
