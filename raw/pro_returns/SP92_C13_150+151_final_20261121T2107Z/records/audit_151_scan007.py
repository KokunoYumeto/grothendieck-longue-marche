from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]; pg='151_scan007'; rp=W/'records'/f'{pg}.json'
r=json.loads(rp.read_text()); co=json.loads((W/'second'/f'{pg}_comparison.json').read_text()); b={x['box']:x for x in co['results']}
p=W/'pages'/f'{pg}.tex'; s=p.read_text(); finals={}
def bracket(body,label=None):
 z=r'\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=0pt](t){$'+body+r'$};\draw ([yshift=-1pt]t.south west)--([yshift=-3pt]t.south west)--([yshift=-3pt]t.south east)--([yshift=-1pt]t.south east);\end{tikzpicture}'
 return r'\underset{'+label+'}{'+z+'}' if label else z
old=r'\underbrace{p_{12}\rho^2}_{p_{31}}'; new=bracket(r'p_{12}\rho^2',r'p_{31}'); assert old in s;s=s.replace(old,new);finals['B02']=b['B02']['first'].replace(old,new)
old=b['B04']['first']; new=r'''\diagram{\deleted{\mbox{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (0,0) {$(x,y,z)$};
\node at (3.6,0) {$(z,y,x)$};
\draw (1.15,-0.12)--(1.15,0.12);
\draw[->] (1.15,0)--(2.30,0);
\draw (2.30,0.14)--(2.50,0)--(2.30,-0.14);
\draw[->] (1.15,-0.8)--(2.50,-0.8);
\node at (3.6,-0.8) {$(x,z)$};
\draw[->] (4.5,-0.8)--(5.4,-0.8);
\node at (5.8,-0.8) {$x$};
\end{tikzpicture}}}}''';assert old in s;s=s.replace(old,new);finals['B04']=new
old=r'\[\deleted{(x,x,y)}\]';new=r'\[\deleted{(\unsure{x},\unsure{x|z},y)}\]';assert old in s;s=s.replace(old,new);finals['B06']=b['B06']['first'].replace(r'(x,x,y)',r'(\unsure{x},\unsure{x|z},y)')
old=r'\delta_1\sigma=(x,y,y)';new=r'\delta_1\sigma=(x\unsure{,}y,y)';assert old in s;s=s.replace(old,new)
old2=r'(x,\unsure{x},y)';new2=r'(x,\unsure{x|z},y)';assert old2 in s;s=s.replace(old2,new2)
finals['B07']=b['B07']['first'].replace(old,new).replace(old2,new2)
old=r'\uline{y,x}';new=bracket('y,x');assert old in s;s=s.replace(old,new);finals['B08']=b['B08']['first'].replace(old,new)
main1=r'p_{12}'+bracket(r'\rho\delta_1',r'\delta_3')+r'=\text{application constante de valeur }e_1\quad\text{(p\textsuperscript{t} marqué de }E_1\text{)}'
main2=r'p_{12}'+bracket(r'\rho^2\delta_1',r'\delta_2')+r'=\mathrm{id}_{E_1}'
side1=r'p_{12}'+bracket(r'\rho\delta_2',r'\delta_1')+r'=\sigma'
side2=r'p_{12}'+bracket(r'\rho^2\delta_2',r'\delta_3')+r'=e_1'
caption=r'\begin{gathered}\text{(\unsure{application|\deleted{appl} constante}}\\\text{de }E_1\text{ sur}\\e_{\unsure{1|q}}\text{)}\end{gathered}'
repeat=r'\deleted{p_{\unsure{12}}\sigma_3\unsure{=\sigma}p_{12}}'
main_nodes=r'''\node[anchor=west] at (0.45,-0.55) {$p_{12}\delta_1=\sigma$};
\node[anchor=west] at (0.45,-1.65) {$'''+main1+r'''$};
\node[anchor=west] at (0.45,-3.05) {$'''+main2+r'''$};
\node[anchor=west] at (0.45,-4.35) {$\sigma_1\delta_1=\delta_1$};
\node[anchor=west] at (0.45,-5.45) {$p_{12}\sigma_3=\sigma p_{12}$};'''
side_nodes=r'''\node[anchor=west] at (10.1,-2.95) {$p_{12}\delta_2=\mathrm{id}_{E_1}$};
\node[anchor=west] at (10.1,-4.05) {$'''+side1+r'''$};
\node[anchor=west] at (10.1,-5.25) {$'''+side2+r'''$};
\node[anchor=west] at (14.0,-5.10) {$'''+caption+r'''$};'''
right_nodes=r'''\node[anchor=west] at (15.55,-2.45) {$\uline{p_{12}\sigma_3=\sigma p_{11}}$};
\node[anchor=west] at (16.05,-3.10) {$\sigma_2\delta_2=\delta_2$};
\node[anchor=west] at (16.65,-3.95) {$'''+repeat+r'''$};
\node[anchor=west] at (16.25,-4.65) {$\deleted{\unsure{\mathrm{id}}}$};
% The oblique line is part of the crossing of the two canceled entries.
\draw[line width=0.9pt] (15.65,-2.85)--(18.15,-5.0);'''
diagram_nodes=r'''\node at (18.7,-5.05) {$E_1$};
\node at (21.6,-5.05) {$E_2$};
\draw[->] (21.0,-5.05)--(19.25,-5.05);
\node at (20.1,-4.72) {$p_{12}$};
\draw[->] (19.25,-5.43) .. controls (19.8,-5.60) and (20.55,-5.60) .. (21.0,-5.43);
\node at (20.1,-5.85) {$\delta_1$};'''
frame=r'''% Open pen joins at upper left and bottom left; right upright overruns bottom.
\draw (0.18,0)--(20,0.40)--(20,-6.25);
\draw (0,-0.38)--(0.22,-5.98);
\draw (0.37,-5.98)--(20,-5.78);
% Inner compartment uses the outer right and bottom borders.
\draw[->] (9.95,-2.30)--(20,-1.96);
\draw (9.86,-2.65)--(10.05,-6.05);'''
head=r'\diagram{\begin{tikzpicture}[x=0.8cm,y=0.8cm,every node/.style={font=\footnotesize,inner sep=1pt}]'
cluster=head+'\n'+frame+'\n'+main_nodes+'\n'+side_nodes+'\n'+right_nodes+'\n'+diagram_nodes+'\n'+r'\end{tikzpicture}}'
start=s.index(r'\[\boxed{\begin{aligned}'); end=s.rindex(r'\margin{6}')
s=s[:start]+cluster+'\n'+s[end:]
finals['B24']=cluster
# B25 is a subregion of the common cluster; retain its three formulas and neighbors without duplicating them on the page.
finals['B25']=head+'\n'+r'\draw[->] (9.95,-2.30)--(20,-1.96);\draw (9.86,-2.65)--(10.05,-6.05);\draw (10.05,-5.88)--(20,-5.78)--(20,-1.96);'+'\n'+side_nodes+'\n'+right_nodes+'\n'+diagram_nodes+'\n'+r'\end{tikzpicture}}'
finals['B27']='$'+repeat+'$'
p.write_text(s);(W/'records'/p.name).write_text(s)
byid={x['id']:x for x in r['changes']}
updates={'C02':finals['B02'],'C04':finals['B04'],'C06':r'\deleted{(\unsure{x},\unsure{x|z},y)}','C07':finals['B08'],'C08':r'\deleted{\delta_1\sigma=(x\unsure{,}y,y)}','C10':r'\deleted{(x,\unsure{x|z},y)}\\\deleted{(y,y,x)}','C34':cluster,'C36':side1,'C37':side2,'C38':caption,'C40':repeat,'C42':head+'\n'+diagram_nodes+'\n'+r'\end{tikzpicture}}'}
for ident,val in updates.items():byid[ident]['final']=val
for ident in ['C02','C04','C34','C36','C37']:byid[ident]['against_C']=True
byid['C02']['evidence']+=' Blind audit: the lower annotation has a flat middle and two upturned ends, not a central cusp; its bracket geometry is corrected.'
byid['C04']['evidence']+=' Blind audit: two separate right-facing chevrons are visible after the barred tail. The first mapping is now drawn with both heads; the lower two arrows remain ordinary single heads.'
byid['C07']['evidence']+=' Blind audit: the y,x annotation has short upturned ends and is a bracket rather than a plain underline. The extra close parenthesis and literal coordinate order remain.'
byid['C34']['evidence']='All five main rows share the outer frame. Separate pen joins leave gaps at the upper-left and bottom-left; the right vertical overruns the bottom. The lower-right compartment shares the outer right and bottom borders; its top rule ends in a small right-pointing head and its left upright starts below that rule. Right-hand formulae and the lower diagram retain their positions, with the latter crossing the outer right boundary. Draw the common cluster, not two detached boxes.'
for ident in ['C36','C37']:byid[ident]['evidence']+=' Blind audit: the annotation has a flat middle and short upturned ends, so its brace is replaced by the square-ended bracket actually written.'
byid['C38']['evidence']='The crowded first line admits application, but the heavy horizontal through its beginning also permits a canceled appl followed by constante. Neither lexical/deletion-scope reading is certified: both are retained explicitly. The next line reads de E1 sur; the final subscript, crossed by the frame border, is 1/q uncertain. The whole parenthetic is absent from H.';byid['C38']['confidence']='low'
byid['C40']['evidence']='The left p, sigma with its protruding index3, and the right p12 are exposed. The initial 12 is partly merged with hatching and remains uncertain, as does the central equals/sigma. This is only partial recovery of C’s whole-formula doubt.'
for ident,body,label in [('C44',r'\rho\delta_1',r'\delta_3'),('C45',r'\rho^2\delta_1',r'\delta_2')]:
 r['changes'].append(dict(id=ident,place='Main relation lower annotation '+body,C=r'\underbrace{'+body+'}_{'+label+'}',H=r'\underbrace{'+body+'}_{'+label+'}',final=bracket(body,label),evidence='The lower rule has a flat middle and separate upturned ends; the descending delta label is not a central brace cusp. Preserve the square-ended annotation with the unchanged literal label.',crop=f'crops/{pg}_blind_B24.png',box=b['B24']['coordinates'],confidence='high',kind='drawing or diagram',error_kind='4 drawings/diagrams',against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for d in r['doubts']:
 if d['place']=='Middle coordinate of the lower repeated left tuple':d.update(reading=r'(x,\unsure{x|z},y)',alternatives=['x','z'],reason='The crossed middle letter has intersecting strokes compatible with x and a low angular return compatible with z; neither is certified.')
 if d['place']=='Center of the canceled right repeated relation':d.update(reading=repeat,reason='The first 12 subscript and central equals/sigma remain entangled with hatching; the sigma3 and final p12 are exposed.')
for place,reading,alts,why,box in [
 ('Separate upper tuple',r'(\unsure{x},\unsure{x|z},y)',['first x under strike','middle x','middle z'],'The first coordinate meets a diagonal cancellation; the middle intersecting/angled strokes admit x or z.','B06'),
 ('First tuple comma after x',r'\delta_1\sigma=(x\unsure{,}y,y)',['comma','x terminal curl'],'A separate comma cannot be distinguished securely from the first x terminal curl.','B07'),
 ('Small-compartment caption word and deletion scope',r'\unsure{application|\deleted{appl} constante}',['application','canceled appl followed by constante'],'The heavy horizontal and compressed succeeding letters do not settle whether this is one live word or a canceled short form followed by another word.','B25'),
 ('Small-compartment caption final subscript',r'e_{\unsure{1|q}}',['1','q'],'The lower frame crosses the small subscript and its descending return.','B25')]:
 r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
r['notes']+='''\n### Blind crop adjudication\n\nAll29 differing boxes were checked individually against the ink. Both circled3s occur at separate physical locations. The discarded upper calculations remain canceled en bloc even where a tight crop lacks its own crossing. The first coordinate mapping has a barred tail and two right-facing heads; later mappings preserve their loop-ended and square downturned terminals. No coordinate permutation or literal index is repaired from the algebra. The top p31 annotation and the y,x annotation are square-ended brackets, as are all four lower rho/delta annotations.\n\nThe lower five-relation frame and its inner three-relation compartment are now one spatial drawing, sharing the right and bottom borders. Its pen gaps and inner top-rule arrowhead are preserved, and the lower E1/E2 diagram crosses the right border. The small caption remains doubtful between one live application and canceled appl followed by constante; its last subscript is1/q uncertain. The underlined right-hand equation retains literal p11. In the canceled repeated equation, the first12 subscript is left uncertain under hatching. The existing mathematical checks and their limitations remain unchanged.\n'''
r['notation'].append(dict(sign='Barred tail followed by two right-facing heads',reading='First canceled coordinate mapping',evidence='The inner and outer chevrons are distinct; do not impose this form on the later loop/square terminals.'))
r['notation'].append(dict(sign='Square-ended lower annotation',reading='Flat rule with upturned ends, carrying a lower label where written',evidence='Confirmed at the upper p31 annotation, the y,x group and all four lower rho/delta labels.'))
r['hand_log'].append(dict(habit='A lower delta label can resemble the missing central cusp of an annotation brace.',places=['151_scan007 main and inner-compartment rho/delta annotations'],scope='All four lower annotations on this page have square-ended brackets; the literal delta labels are separate.',witness_errors='C and H give braces in the main relations; C uses braces in the smaller compartment.'))
r['abbreviations'].append(dict(form='appl',expansion='application; only a tentative canceled reading in the small-compartment caption'))
evidence={
'B01':'A clear upper-small/lower-large3 stands in a surrounding circle. This is the upper circled3 at x940–1040,y30–145, distinct from B11. Author-number wrapper difference only.',
'B02':'The complete canceled chain has literal indices0,12,13 and31, exponent2 and sigma2. The lower rule under p12 rho2 has flat middle and upturned ends, with no central cusp; use a bracket.',
'B03':'Both rho exponents2 and sigma indices2/3 are clear. The isolated crop has no separate strike, but this formula lies within the upper block canceled by the long diagonals and sweeping boundary; it stays canceled en bloc.',
'B04':'The first shaft has a barred tail and two independent right-facing chevrons, rather than a single mapsto head. Both lower arrows have ordinary single heads. All tuples and the final x agree; the whole diagram remains canceled.',
'B05':'Every p and index in p0p12 sigma1 = p0p12 is exposed and agrees. The formula remains in the canceled block; display/inline wrappers are the only other difference.',
'B06':'The first x meets a diagonal strike and is not fully separable; the middle crossed/angled glyph admits x or z; final y and delimiters are clear. Add these local doubts.',
'B07':'The comma after the first x of delta1 sigma cannot be separated confidently from its terminal curl. The middle glyph of the following tuple admits x/z under the overtrace. The last (y,y,x) is clear. All three rows are canceled.',
'B08':'The colon, first tail bar/head and extra closing parenthesis after (z,y,x)) are visible. The next mapping has a separate bar and loop endpoint, not an ordinary head. Its output is literally (y,x,z), with an upturned-ended bracket under y,x rather than a plain underline.',
'B09':'Bare z,x,y has no enclosing parentheses and all three letters are clear. Its placement in the en-bloc canceled upper draft determines its state, not the absence of a separate local strike.',
'B10':'The last upper mapping has a barred tail and downturned square right terminal without a chevron. The lower (x,z,y)=sigma1 remains inside the same canceled boundary. That boundary is not an added live rule.',
'B11':'The left-mid-page numeral has two distinct3 lobes and its own circle at x20–150,y940–1100. It is separate from the upper circled3; retain both. Wrapper only.',
'B12':'The d ascender and compressed onc precede a separate par with a descending p and low ar. Read donc par, not les p. The point abbreviation has a genuinely raised t, and all preceding words agree.',
'B13':'The delta0, delta1delta0 composition and E1/E2 subscripts are visible. The compressed devenir ending has the continuous nn run before the final t; retain deviennent des ens. pointés with the final comma.',
'B14':'Both G signs have enclosing bowls and low inward returns with separate2 and3. Mathematical font alternatives do not change the read capital G.',
'B15':'The singular la and one continuous ponctuation are visible: p descender, compact on/ct run, tall t and dotted i in the ending, then the final stop. There is no separate fixe word.',
'B16':'Paired quotation ticks enclose ponctués, with p descender, compact on/ct run and accented final é/s. There is no independent b ascender supporting a separate base word. Parentheses are present.',
'B17':'The old capital-loop opening remains Donc./On a. uncertain under its horizontal strike. Delta1 and respecte are exposed; the determiner final return remains les/le uncertain under the crossing.',
'B18':'The live words are Donc, en plus des opérations de: plus has a p descender followed by a tall l, not fera/fait. The raised et p12 belongs to the later curved insertion leader, not this baseline.',
'B19':'Both G signs and their indices2/3 are clear; the brief following on a is the same compressed low hand used elsewhere on the line. The comma after G3 is separate. No new separator rule is inserted.',
'B20':'The upper p12 arrow is straight and points left from E2 to E1. The lower delta1 arrow curves right with its label below. Both objects and every label agree; wrapper/curve-encoding differences only.',
'B21':'A comma precedes accented où and delta1. The curved leader starts with et p12 above and ends between delta1 and respectent. The compressed ending reaches the page edge and remains doubtful; no punctuation is supplied.',
'B22':'The low les and one continuous ponctuations are written, with the repeated compact n/c/t strokes and final plural return before the comma. Do not substitute points fixes.',
'B23':'The initial et is followed by accented où. The labels are p12,delta1, then the long satisfont with its descending f and final high t. The phrase continues outside this crop; no changed relation is inferred.',
'B24':'All five main relations were read in full. Their two lower rho/delta annotations are square-ended brackets. The outer frame has separate upper-left and lower-left joins and an overrun right vertical. The lower-right compartment shares the outer right and bottom, with an independently started left upright and a top rule ending in a small right arrowhead. The integrated drawing preserves the right notes and the lower diagram crossing the border. Neighboring lead-in fragments are already in the prose.',
'B25':'The three side relations have indices2 and lower labels delta1/delta3;3 has two bends, unlike the local2 foot. Both lower rules are square-ended brackets. The crowded caption admits application or canceled appl followed by constante; the high-density horizontal and following joins do not settle the lexical/deletion scope. Keep both in a doubt. The last subscript is1/q uncertain where crossed by the border. The adjoining literal p11 and other formulas are retained in the common cluster.',
'B26':'The underlined RHS has two distinct short upright strokes after p; neither has the baseline foot of the clearly written2 on the LHS. Retain literal p11. Sigma2 delta2 = delta2 below is clear.',
'B27':'The left p is clear, but its12 subscript is crossed and merged with hatching, so mark that subscript uncertain. Sigma and its protruding3, and final p12, are exposed. Central equals/sigma remains uncertain as a unit.',
'B28':'The separate short hatched entry has surviving upright and loop shapes compatible with id but no full recovery is possible. Keep unsure id; do not put an illegible placeholder inside the mathematical cluster.',
'B29':'The lower diagram has E1 and partly edge-adjacent E2, a straight left arrow labeled p12 above, and a shallow right curve labeled delta1 below. All symbols agree; the integrated frame preserves its crossing of the right border.'}
notes={}
for k,why in evidence.items():
 notes[k]=dict(viewed=True,evidence=why)
 if k in finals:notes[k].update(changed=True,final=finals[k])
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('151_scan007:29 differing boxes viewed;8 changed;45 current change rows. Ready for metadata cleanup and audit finalization.')
