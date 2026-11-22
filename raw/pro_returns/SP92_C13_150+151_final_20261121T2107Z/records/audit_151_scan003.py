from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='151_scan003';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
def bracket(term,label='',upper=False):
 side='north' if upper else 'south';a='1' if upper else '-1';z='3' if upper else '-3'
 pic=r'\begin{tikzpicture}[baseline=(term.base)]\node[inner sep=0pt] (term) {$'+term+r'$};\draw ([yshift='+a+r'pt]term.'+side+r' west) -- ([yshift='+z+r'pt]term.'+side+r' west) -- ([yshift='+z+r'pt]term.'+side+r' east) -- ([yshift='+a+r'pt]term.'+side+r' east);\end{tikzpicture}'
 return ('\\overset' if upper else '\\underset')+'{'+label+'}{'+pic+'}' if label else pic
oldcancel=r'\deleted{\unsure{p_1\delta_0|p_{12}\delta_0}}';newcancel=r'\deleted{p_{\unsure{1|12}}\delta_{\unsure{1|0}}}'
reps=[(r'\deleted{\[p_{12}=p_{23}\]}',r'\deleted{\[p_{\unsure{12}}=p_{23}\]}'),(r'{}^{\unsure{a}}',r'{}^{\unsure{a|\leftarrow}}'),(oldcancel,newcancel)]
for term,label in [(r'\delta_3',r'\rho^{\deleted{\unsure{2|\sigma}}}\delta_1'),(r'p_{23}',r'p_{12}\rho'),(r'\delta_1',r'\deleted{\unsure{\rho}}'),(r'p_{31}',r'p_{12}\rho^2'),(r'\delta_2',r'\rho^2\delta_1')]:reps.append((r'\underbrace{'+term+'}_{'+label+'}',bracket(term,label)))
reps += [
 (r'\underbrace{\delta_0p_0}',r'\delta_0'+bracket(r'p_0')),
 (r'\underbrace{p_{12}\delta_1}_{\sigma}',bracket(r'p_{12}\delta_1',r'\sigma')),
 (r'\underbrace{p_{12}\rho\delta_1}_{\mathrm{id}}',bracket(r'p_{12}\rho\delta_1',r'\mathrm{id}')),
 (r'\underbrace{(p_{12}\rho)}_{p_{23}}','('+bracket(r'p_{12}\rho',r'p_{23}')+')'),
 (r'\underbrace{\rho\delta_1}_{\delta_2}',bracket(r'\rho\delta_1',r'\delta_2')),
 (r'\overbrace{\rho\delta_1}^{\delta_3}',bracket(r'\rho\delta_1',r'\delta_3',True)),
 (r'\underbrace{\rho_{\deleted{\unsure{1}}}^{2}\delta_1}_{\delta_2}',bracket(r'\rho_{\deleted{\unsure{1}}}^{2}\delta_1',r'\delta_2')),
 (r'\underbrace{p_0p_{12}}_{p_{\unsure{2|1}}}',bracket(r'p_0p_{12}',r'p_{\unsure{2|1}}')),
 (r'\overbrace{\underbrace{p_{12}\deleted{\unsure{\sigma}}\rho^2}_{p_{31}}\sigma_2}^{p_{12}}',bracket(bracket(r'p_{12}\deleted{\unsure{\sigma}}\rho^2',r'p_{31}')+r'\sigma_2',r'p_{12}',True))]
oldframe=r'\draw (current bounding box.south west) rectangle (current bounding box.north east);'
newframe=r'\draw (current bounding box.north west) -- (current bounding box.north east) -- ([yshift=10pt]current bounding box.south east);\draw ([yshift=4pt]current bounding box.south east) -- (current bounding box.south east) -- (current bounding box.south west) -- ([yshift=-4pt]current bounding box.north west);'
reps.append((oldframe,newframe))
oldlast=r'\boxed{\rho\delta_1\delta_0=\sigma_1\delta_1\delta_0=\delta_1\delta_0}'
newlast=r'\begin{tikzpicture}[baseline=(eq.base)]\node[inner sep=5pt] (eq) {$\rho\delta_1\delta_0=\sigma_1\delta_1\delta_0=\delta_1\delta_0$};\draw (eq.north west) -- (eq.north east) -- ([yshift=3pt]eq.south east);\draw (eq.south east) -- (eq.south west);\draw[->] (eq.south west) -- ([yshift=-3pt]eq.north west);\end{tikzpicture}'
reps.append((oldlast,newlast))
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert a in s,a;s=s.replace(a,z)
oldrel=bracket(r'p_0p_{12}',r'p_{\unsure{2|1}}')+'=p_0';newrel=bracket(r'p_0p_{12}',r'p_{\unsure{2|1}}')+r'\unsure{=|\ne}p_0';assert oldrel in s;s=s.replace(oldrel,newrel);reps.append((oldrel,newrel))
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id'] in ['C34','C36','C37','C38','C39','C42','C44','C47','C60']:
  x['against_C']=True;x['evidence']+=' Blind audit: the relevant annotation strokes have flat middles and short turned ends without a central cusp; preserve bracket geometry. '+('The first canceled-chain bracket lies under p0, to the right of the delta body.' if x['id']=='C42' else 'The first inequality bracket ends inside the parentheses.' if x['id']=='C44' else '')
 if x['id']=='C33':x.update(final=newcancel,confidence='low',evidence='The canceled p index may contain1 alone or12. The following delta’s exposed low index is an upright with a short turn, favoring1;0 remains possible under the crossing. Neither index is resolved.')
 if x['id']=='C45':x['final']=bracket(r'\rho\delta_1',r'\delta_2');x['evidence']+=' The lower annotation stroke is a square-ended bracket, with no central cusp.'
 if x['id']=='C26':x['evidence']+=' The small raised shape also admits a leftward arrow; its identity remains doubtful.'
for ident,place,C,H,final,box,why in [
 ('C63','Lower diagram frame gaps','continuous rectangle','lower diagram omitted',newframe,'B20','The upper-left horizontal rule stops before the left upright; the right upright also has a short gap above the bottom corner. Preserve both gaps in the diagram frame.'),
 ('C64','Final identity frame, arrow at left edge',oldlast,r'\boxed{\rho\,\delta_1\delta_0 = \sigma_1\,\delta_1\delta_0 = \delta_1\delta_0},',newlast,'B21','The left frame stroke rises to a distinct small arrowhead and stops before the top line. The lower right corner also has a short gap. The identity itself is unchanged.'),
 ('C65','Three-value box, lower annotation geometry',r'\underbrace{\rho^2\delta_1}_{\delta_2}',r'\underbrace{\rho^2\delta_1}_{\delta_2}',bracket(r'\rho_{\deleted{\unsure{1}}}^{2}\delta_1',r'\delta_2'),'B18','The annotation below rho squared delta1 has a flat middle and rising ends, without a central cusp. The separate canceled subscript is recorded in C48.'),
 ('C66','Bottom formula, left annotation bracket',r'\underbrace{p_0p_{12}}_{p_{\unsure{1|2}}}','left underannotation omitted',bracket(r'p_0p_{12}',r'p_{\unsure{2|1}}'),'B22','The lower line under p0 p12 has rising ends and no central cusp. Its partially clipped lower label remains2/1 doubtful.')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind='drawing or diagram',error_kind='4 drawings/diagrams',against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for x in r['decisions']:
 if x['id']=='M0737':x['reading']=r'{}^{\unsure{a|\leftarrow}}';x['ink']='The raised shape has a loop/return and an angled left stroke. It may be a or a left arrow; no secure identification is claimed.'
for x in r['doubts']:
 for a,z in reps:x['reading']=x['reading'].replace(a,z)
 if x['place']=='Small raised terminal in third delta-rho identity':x['alternatives']=['a',r'\leftarrow'];x['reason']='Raised loop/return and angled left stroke do not securely distinguish a from a leftward arrow.'
 if x['place']=='Cancelled expression beside identity box':x.update(reading=newcancel,alternatives=['p index1 or12','delta index1 or0'],reason='Crossings hide the p index length; the exposed low delta index favors an upright1, but0 cannot be excluded.')
for place,reading,alts,box,why in [('Canceled projection equality, first index',r'p_{\unsure{12}}',['12'],'B08','The thick crossing conceals independent boundaries of both small index digits.'),('Bottom formula relation',r'\unsure{=|\ne}',['=','ne'],'B22','Two horizontal bars survive; a dark connecting/retraced mark above them does not securely establish or exclude a crossing stroke.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
def update_current(v):
 if isinstance(v,str):
  for a,z in reps:v=v.replace(a,z)
  return v
 if isinstance(v,list):return [update_current(x) for x in v]
 if isinstance(v,dict):return {k:update_current(x) for k,x in v.items()}
 return v
for k in ['deletion_insertion_review','inventory','notation','hand_log']:r[k]=update_current(r[k])
r['notes']+='''\n### Blind crop adjudication\n\nThe main-chain delta after p23 remains the literal1, not the blind reader’s2; its upright and foot are visible. The live G glyphs have open bowls and inward returns, and the vertical membership marks open upward rather than forming arrowheads. The prose remains de avoir: the verb has no initial d ascender. The canceled small p/delta expression is now explicitly uncertain in both indices, with delta1/0. The raised mark after the cyclic delta identity remains a/left-arrow uncertain. The first index in the canceled p12=p23 is no longer certified through its heavy strike.\n\nSeveral annotation strokes are square-ended brackets, not central-cusped braces: all five underannotations of the main chain, the first three annotations in the canceled i.e. line, both annotations in the canceled inequality, the two in the three-value box, and the three at the bottom. The last annotation in the canceled i.e. line retains its genuine central cusp. The first short canceled-chain bracket is placed under p0; the first inequality bracket lies inside the parentheses. The lower diagram frame retains its two pen gaps, and the final identity frame has an upward-pointing left edge and two gaps. The bottom relation remains equality/inequality uncertain. None of these graphic corrections changes the coordinate computations already logged.\n'''
def put(k,why,changed=False):
 notes[k]=dict(viewed=True,evidence=why)
 if changed:
  f=b[k]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[k].update(changed=True,final=f)
put('B01','All live and canceled arrow paths and labels were inspected. The three upper return labels are12,23,13 as written; the lower13 is not31. Both group letters have open rounded bowls with internal returns, matching G rather than S. Beneath them the three-stroke membership marks open upward and have no arrow shaft/head. The three abandoned curved arrows remain canceled with the first two delta labels uncertain. Layout and mathcal/TikZ encodings do not change these readings.')
put('B03','The entire old coordinate expression is canceled. The two short lower equality bars are crossed by the long descending leader from the upper formula, not by an independent inequality slash. The lower live first letter remains sigma/delta uncertain because of retracing; do not replace it by a confident sigma.')
put('B04','A single upright1 is enclosed by a large circle. mspage versus margin is editorial placement, not a different number.')
put('B05','The first saturated low index remains1/0 doubtful; the second p0 and following p1 are clear. The comma is present. Quad/qquad is spacing only.')
put('B06','The live second-row p23 is visible above a densely canceled lower index. A separate second p body cannot be certified beneath the live p stem, so retain the old21 only as a doubtful subscript with inserted23. All three coordinate tuples and the final p31 agree.')
put('B07','The rho stem, all tuple letters and commas, equals and final closing parenthesis agree. Dollar versus parenthesized math delimiters is encoding only.')
put('B08','The three live cyclic projection equations and their frame agree. The canceled first12 is too crossed to certify both digits, so add local uncertainty. Neighboring sigma p12 and the beginning of the crossed coordinate chain are already transcribed in adjacent blocks and are not duplicated.',True)
put('B10','Both arrows and all three tuples in the canceled chain were inspected. The rho squared at the upper left belongs to the neighboring live boxed equation, not a new separate term in this canceled line.')
put('B11','All three cyclic delta equations agree, including indices and rho exponents. The small raised mark after the final delta2 can be a or a leftward arrow; retain both possibilities at its raised position.',True)
put('B12','The prose word has low a/v/o/i/r strokes without a d ascender, so retain de avoir rather than donner. The initial crossed a-like glyph is still tentative. Both group letters have the same open G bowls as the upper and lower diagrams. Entre and all tuple punctuation agree.')
put('B13','The boxed p0 delta0 identity is clear and has no separate following comma. In the crossed draft, the p index may be1 or12, while the low index on delta has an upright1-like stroke with0 still possible under cancellation. Keep both indices uncertain.',True)
put('B14','The complete chain shows literal delta1 after p23, with a distinct upright and foot rather than a curved2. The separately canceled raised glyph after rho remains visible and uncertain. All five annotation lines have flat middles and short rising ends, without central cusps; replace their brace geometry by brackets.',True)
put('B15','The framed sigma delta0=delta0 identity agrees. The heavily retraced delta loop remains the same live letter; no independent cancellation is present.')
put('B16','The entire i.e. chain is crossed. Its first short bracket begins to the right of the delta body and lies under p0. The first three annotation lines are flat with rising ends; only the last has a distinct central downward cusp and remains a brace. Sigma and id labels agree.',True)
put('B17','Both question marks stand above the explicit inequality sign. The crossed RHS p index still admits22/12/23 and is not resolved from the expected formula. The first square-ended bracket lies inside the parentheses; the right lower bracket has the clear delta2 label. Correct both bracket geometries.',True)
put('B18','The upper rho-delta annotation and lower rho-squared-delta annotation have flat lines and turned ends, not cusps. The live rho2 is retraced above a separate canceled1-like subscript; no independently separable complete old sigma1 is certified. Two faint dots before the last equals sit diagonally below its baseline and do not establish a colon.',True)
put('B19','Both marginal identities were read. The first is literally sigma3 delta1=delta1, including the clear two-lobed3. The second has p12 on both sides. Delimiters and newline syntax do not change the reading.')
put('B20','All four maps and live G2/G3 labels agree; the old group/index and Ens-like text remain doubtful under cancellation. The diagram frame has an upper-left gap and a lower-right gap, which the former continuous rectangle omitted.',True)
put('B21','The complete final identity agrees. Its left frame edge terminates in a small upward arrowhead and stops before the top rule; the lower-right corner also has a gap. Preserve that drawn frame. The partly visible annotation below belongs to B22.',True)
put('B22','The bottom formula has flat square-ended lower and upper annotation brackets. The outer label remains literal p12, the inner label p31; the live final sigma2 and canceled old sigma remain distinct. The left lower index remains2/1 because of clipping. The dark relation has two bars and a possible merged crossing, so equality/inequality remains uncertain.',True)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('003: all20 differing boxes viewed; ten changed boxes; bracket and frame geometry preserved.')
