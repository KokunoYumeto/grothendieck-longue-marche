from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]; O=ROOT/'out'; stem='C123-01_123_scan016'
R={r:json.loads((O/'readers'/stem/r/'report.json').read_text()) for r in ('R1','R2','R3')}
M=json.loads((O/'decisions'/f'{stem}_pending_math.json').read_text())
r1='readers/'+stem+'/R1/crops/'; rc='decisions/rootcrops/'+stem+'/'
spec=dict(stem=stem,base_reader='R1',brief='reader_v04.md',main_new_crops=6,text_edits=[],difference_overrides={},additional_differences=[],exclude_difference_ids=[])
def edit(old,new): spec['text_edits'].append(dict(old=old,new=new))
def over(i,**kw): spec['difference_overrides'].setdefault('R1-D'+str(i).zfill(2),{}).update(kw)
def add(i,place,C,H,final,evidence,crop,kind='other',confidence='high',cc=True,hh=True,readers='R1, R2 and R3 agree unless otherwise stated.'):
 spec['additional_differences'].append(dict(id='M-'+str(i).zfill(2),place=place,C=C,H=H,final=final,evidence=evidence,crop=crop,kind=kind,confidence=confidence,c_changed=cc,h_changed=hh,marked_in_H='yes' if '\\ill' in H or '\\uncertain' in H else 'no',readers=readers))
edit('son algèbre de Lie.','son algèbre de Lie,')
qual=r'''\begin{tikzpicture}[baseline=(attachment)]
\coordinate (attachment) at (0,0);
\node[anchor=base west,inner sep=0pt] (qual) at (-.7,.43) {\inserted{avec $e\handwritten{\ne}0$, $e$ nilpotent.}};
\draw ([xshift=-.08cm,yshift=.05cm]qual.north west) .. controls ([xshift=-.22cm]qual.west) and ([xshift=-.12cm,yshift=-.10cm]qual.south west) .. ([yshift=-.08cm]qual.south west) .. controls (-.15,.23) and (-.03,.20) .. (0,.10) -- (0,-.10);
\draw (0,.10) .. controls (.05,.23) and (.18,.25) .. ([yshift=-.08cm]qual.south east) .. controls ([xshift=.15cm,yshift=-.08cm]qual.south east) and ([xshift=.15cm]qual.east) .. ([xshift=.03cm,yshift=.03cm]qual.north east);
\end{tikzpicture}'''
edit(r'\inserted{avec $e\handwritten{\ne}0$, $e$ nilpotent.}',qual)
doubleL=r'''\mathop{\begin{tikzpicture}[baseline=(ell.base)]\node[inner sep=0pt,anchor=base] (ell) at (0,0) {$\mathrm{L}$};\node[inner sep=0pt,anchor=base] at (-.025,0) {$\mathrm{L}$};\end{tikzpicture}\mathrm{ie}}'''
edit(r'\mathbb{L}\mathrm{ie}',doubleL)
oldb=r'''\[
\text{b)}\quad e\handwritten{\in\mathfrak{g}}(2),\quad\handwritten{\deleted{\unsure{et}}}\quad \operatorname{ad}(e):\handwritten{\mathfrak{g}}(0)\handwritten{\longrightarrow\mathfrak{g}}(-2)\quad\text{est surjectif},
\]
\inserted{\handwritten{et $x$ est de la forme $f(x_{\unsure{o|0}})$, pour $f:\operatorname{Sl}(2,\unsure{k'|k})\to G$ (\uline{élément de Dynkin}).}}

\handwritten{\deleted{b') Comme b), avec $\operatorname{ad}(e):\mathfrak{g}(0)\to\mathfrak{g}(\unsure{2|-2})$ \uline{\unsure{bijectif}}}}'''
newb=r'''\figure{\begin{tikzpicture}[every node/.style={anchor=base west,inner sep=0pt,font=\scriptsize}]
\node (bmain) at (0,0) {$\text{b)}\quad e\handwritten{\in\mathfrak{g}}(2),\quad\deleted{\unsure{et}}\quad\operatorname{ad}(e):\handwritten{\mathfrak{g}}(0)\handwritten{\longrightarrow\mathfrak{g}}(-2)\quad\text{est surjectif},$};
\node[xshift=.08cm] (addfirst) at (bmain.base east) {\inserted{\handwritten{et $x$ est de la forme}}};
\node (bprime) at (0,-.55) {\handwritten{\deleted{b') Comme b), avec $\operatorname{ad}(e):\mathfrak{g}(0)\to\mathfrak{g}(\unsure{2|-2})$ \uline{\unsure{bijectif}}}}};
\node[xshift=.18cm] (addlast) at (bprime.base east) {\inserted{\handwritten{$f(x_{\unsure{o|0}})$, pour $f:\operatorname{Sl}(2,\unsure{k'|k})\to G$ (\uline{élément de Dynkin}).}}};
% Thin hooked connector, distinct from the heavy b-prime cancellation. Its exact starting attachment is uncertain.
\path (bprime.north west) -- (bprime.north east) coordinate[pos=.60] (hookstart);
\draw ([yshift=.13cm]hookstart) -- ([yshift=.13cm]bprime.north east) .. controls ([xshift=.20cm,yshift=.13cm]bprime.north east) and ([xshift=.22cm,yshift=-.05cm]bprime.south east) .. ([xshift=.12cm,yshift=-.10cm]bprime.south east) -- ([yshift=-.14cm]addlast.south east);
\end{tikzpicture}}'''
edit(oldb,newb)
edit(r'x\deleted{\unsure{y}}',r'x\deleted{y}')
edit('il existe un homomorphisme $f:'+r'\operatorname{Sl}(2,k)', 'il existe un '+r'\unsure{homomorphisme} $f:\operatorname{Sl}(2,k)')
slash=r'''\begin{tikzpicture}[baseline=(stop.base)]\node[inner sep=0pt,anchor=base] (stop) at (0,0) {.};\draw[line width=.4pt] (-.08,-.02)--(.06,.25);\end{tikzpicture}'''
edit(r'i\handwritten{\unsure{/}}.e.','i'+slash+'e.')
oldpar=r'''\begin{tikzpicture}[baseline=(base.base)]
\node[anchor=base west,inner sep=0pt] (base) at (0,0) {\deleted{sous les éléments de}};
\node[anchor=south,inner sep=0pt,xshift=-0.25cm,yshift=0.08cm] at (base.north) {par};
\node[anchor=base west,inner sep=0pt,xshift=-0.25cm,yshift=0.20cm] at (base.base east) {\handwritten{$Z=$}};
\end{tikzpicture}'''
newpar=r'''\begin{tikzpicture}[baseline=(cancel.base)]
\node[anchor=base west,inner sep=0pt] (cancel) at (0,0) {\deleted{sous les éléments de}};
\path (cancel.base west) -- (cancel.base east) coordinate[pos=.34] (parpos) coordinate[pos=.90] (zpos);
\node[anchor=base west,inner sep=0pt,yshift=2.1ex] at (parpos) {\inserted{par}};
\node[anchor=base west,inner sep=0pt,yshift=1.3ex] at (zpos) {\inserted{\handwritten{$Z=$}}};
\end{tikzpicture}'''
edit(oldpar,newpar)
marks=r'''\unsure{\begin{tikzpicture}[baseline=(ec.base)]\node[inner sep=0pt,anchor=base] (ec) at (0,0) {$e$};\draw[line width=.45pt] (-.085,.19)--(-.065,.21);\draw[line width=.45pt] (-.015,.27)--(.010,.30);\end{tikzpicture}}'''
edit(r'\unsure{\acute e|e}',marks)
# Correct inaccurate witness excerpts in the reader's apparatus; do not alter its saved return.
for n,d in enumerate(R['R1']['differences'],1):
 if '\\prime' in d.get('C',''):over(n,C=d['C'].replace('\\prime',"'"))
 if d.get('kind')=='deletion state':over(n,kind='deletion state (struck given live or live given struck)')
over(1,c_changed=True,readers=r'R1: 1.2; R2: 1.2; R3: \unsure{1.2|4.2}. The low dot and comparison with the visible 4 in 3.4 support 1.2.')
over(2,confidence='high',readers='R1: four points; R2: four points in reading.tex; R3: four points.')
over(3,final='Raised typed qualification attached by the curved enclosure/leader after the comma of Soient x,e∈g; reproduced in TikZ.',readers='R1: unparenthesized insertion with enclosure described; R2: parenthesized insertion; R3: handwritten curved parentheses. Root retains the drawn enclosure/leader rather than converting it to ordinary parentheses.')
over(4,final=qual,h_changed=True,kind='drawing or diagram',readers='R1: no ordinary parentheses, enclosure described; R2: ordinary parentheses; R3: handwritten parentheses. Root reproduces the curved enclosure and downward leader in TikZ.',evidence='The two curved ends join a continuous lower line with a downward attachment before Pour. They are preserved as this drawn enclosure, not omitted or made independent typed parentheses.')
over(8,crop=rc+'blank.png')
over(9,final=doubleL,kind='other',confidence='medium',readers='R1: double-struck L via mathbb; R2: ordinary Lie; R3: ordinary Lie. Root preserves two offset L impressions graphically without assigning a new mathematical alphabet.',evidence='Two parallel typewriter stems and offset foot/top impressions are visible in L. The neighboring i and e are normal; the second impression is represented by an offset overlay.')
over(11,readers=r'R1: équiva\deleted{\unsure{e}}lentes; R2: same; R3: équiva\deleted{\unsure{e|a}}lentes. The extra crossed cell is certain; e remains the tentative first reading.')
over(12,h_changed=True,readers='R1: isom with possible point; R2: isom.|isom; R3: isom without a supplied point. Root retains a doubtful point because a dark nub projects into the white at punctuation height, merging with the edge.')
over(13,final=r'\deleted{\unsure{et}}',readers='R1: handwritten underlying et; R2: typed underlying et; R3: typed underlying et. Root favors typed letters under pen cancellation; the word remains doubtful. Medium is audited without counting the wrapper alone as a C change.')
over(14,C=r"par $f:\operatorname{Sl}(2,\unsure{k'|k})\to G$",final=r"pour $f:\operatorname{Sl}(2,\unsure{k'|k})\to G$",readers='R1: pour; R2: par; R3: pour. Root sees the rounded o followed by a separate low u turn and final r; pour is retained.')
over(19,final=r'\deleted{y}',c_changed=True,confidence='high',readers=r'R1: \deleted{\unsure{y}}; R2: \deleted{y}; R3: \deleted{y}. The descending curved tail and surviving upper fork settle y.')
over(21,crop=rc+'basis_subscripts.png')
over(22,c_changed=True,confidence='medium',readers='R1: lower e|o trace; R2: lower e trace doubtful; R3: lower e trace doubtful. Root retains the e/o alternatives beneath the live e, and the detached dash above it.')
over(23,C=r"\unsure{qu'il|qu'ib}",readers=r"R1: qu'i\deleted{\unsure{o|b}}l; R2: qu'i\deleted{\unsure{o}}l; R3: o|b under l. Root retains the rounded underlying trace separately, o first.")
over(24,crop=rc+'ii_subscripts.png')
over(28,readers=r'R1: \deleted{\unsure{(}}; R2: \deleted{(}; R3: \deleted{\unsure{(}}. The curvature survives but the crossed middle does not securely settle the character; doubt retained.')
over(30,final='i'+slash+'e.',kind='drawing or diagram',readers='R1: slash just left of first point, uncertain function; R2: slash before first point; R3: slash over the first point in TikZ. Root preserves the oblique line immediately beside/overlapping that point, without moving it to e=0.',evidence='A separate oblique stroke rises beside the first stop of i.e., several character cells to the right of e=0. Its geometry is reproduced. Its intended function is unresolved, but the stroke itself is clear.')
over(32,final=newpar,readers='All three preserve raised par and separately raised Z= in TikZ. Root uses relative anchors matching par over the left/middle and Z= at the far right of the canceled phrase; no arbitrary inline attachment is imposed.')
over(33,final=marks,crop='readers/'+stem+'/R3/19_cent_accent.png',kind='drawing or diagram',readers='R1: acute e|e; R2: e, marks not included; R3: acute e|e. Root preserves both small diagonal marks above e graphically; their status as an accent remains doubtful.',evidence='Two separate short dark marks lie on a rising diagonal above the typed e. Both are reproduced in their relative positions, without collapsing them into a certain acute or a new mathematical variable.')
over(35,crop=rc+'closing_comma.png')
over(36,readers='R1: no typewriter space between les and canceled morphismes; R2: space; R3: space. Root retains direct adjacency visible at the left of the cancellation; morphismes remains doubtful, g and int(g) clear.')
add(1,'Opening definition: comma after Lie','Lie.','Lie,','Lie,','A rounded punctuation head with a descending tail is a comma.','readers/'+stem+'/R3/03_lie_stop.png',readers='R1: Lie.; R2: Lie,; R3: Lie,. Root retains the visible comma.',hh=False)
add(2,'Theorem heading: underline',r'\uline{Théorème}',r'\textbf{Théorème}',r'\uline{Théorème}','A detached horizontal rule runs beneath the ordinary typewriter letters; boldface does not preserve it.',rc+'theorem_heading.png',cc=False)
add(3,'Theorem heading: added (i)',r'\inserted{\handwritten{(i)}}','(i)',r'\inserted{\handwritten{(i)}}','The handwritten (i) is raised and has an oblique insertion stroke before Soient.',rc+'theorem_heading.png',kind='insertion or placement',cc=False)
add(4,'First Lie-algebra glyph: retained alphabet doubt',r'\unsure{\mathfrak{g}|\mathscr{G}}',r'\mathfrak{g}',r'\unsure{\mathfrak{g}|\mathscr{G}}','The narrow hooked left stroke and long right descender support g but do not uniquely settle its typographic alphabet.',r1+'01_first_g.png',kind='misread symbol or index',confidence='medium',cc=False)
add(5,'Cancelled b′): retained sign doubt',r'\mathfrak{g}(\unsure{2|-2})',r'\mathfrak{g}(2)',r'\mathfrak{g}(\unsure{2|-2})','The heavy crossing line covers the place where a minus could be. The numeral 2 is visible, but absence of a preceding minus is not established.',r1+'10_cancelled_bprime.png',kind='misread symbol or index',confidence='low',cc=False)
add(6,'(ii), clipped homomorphisme',r'\unsure{homomorphisme}','homomorphisme',r'\unsure{homomorphisme}','The ending meets the black scan border; the partial terminal e is plausible but not completely separated from it.',r1+'14_homomorphisme_edge.png',confidence='medium',cc=False,readers='R1: definite homomorphisme; R2: doubtful homomorphisme; R3: doubtful homomorphisme. Root retains the edge doubt.')
add(7,'(ii), faint first par in handwritten insertion',r'\unsure{par}','par',r'\unsure{par}','A long faint p-descender and short joining strokes favor par; not all inner strokes are secure.',r1+'15_unique_insertion.png',kind='misread word',confidence='low',cc=False)
add(8,'b) annotation: reader-only arrow disagreement',r'\to G',r'\to G',r'\to G','The right head is definite. The left triangular thickening has no separately drawn pair of arms; a matching pen-start bulb occurs on the live b) arrow in the main-reader b_target crop. Root reads a right arrow.',r1+'09_b_addition.png',kind='misread symbol or index',confidence='medium',cc=False,hh=False,readers=r'R1: →; R2: \unsure{↔|→}; R3: →. Root: → after comparing the two local arrow forms.')
add(9,'b) complement beside canceled b′): line layout and thin hooked connector','Linearized b) addition, followed by canceled b′)','Linearized addition; note describes connecting trait','TikZ: addition begins after surjectif, continues to the right of canceled b′), with a separate thin hooked lower connector','R1 crops 09 and 10 show the addition and the thin hook rounding the right of the canceled line, distinct from its heavy strike; R3 independently describes the same relation from its retained view. The exact start attachment is not asserted.',r1+'10_cancelled_bprime.png',kind='drawing or diagram',confidence='medium',readers='All three linearize the addition in reading.tex. R3’s independent follow-up describes its second line to the right of b′), and the separate thin hooked connector; root reconstructs that visible geometry.')
# Retain every C doubt; replace only the root decisions that differ.
cd=copy.deepcopy(R['R1']['c_doubts'])
cd[8].update(decision=r'\deleted{y}; doubt resolved',confidence='high',evidence='The surviving upper fork and curved descender identify y under the overstrike.')
cd[10].update(decision=r'Retain \unsure{homomorphisme}',confidence='medium',evidence='The terminal e is partly clipped by the dark scan boundary; its complete edge is not visible.')
cd[18]['crop']=rc+'blank.png';cd[19]['crop']=rc+'b_target.png'
spec['c_doubts']=cd
rem=[copy.deepcopy(x) for i,x in enumerate(R['R1']['remaining_doubts']) if i!=9]
rem.append(dict(place='(ii), clipped right-edge homomorphisme',reading='homomorphisme',alternatives='terminal letter partially clipped',confidence='medium'))
for d in rem:
 if d['place']=='First Cent argument':d.update(reading='e with two diagonal upper marks, reproduced in TikZ',alternatives='broken/doubled acute; stray or displaced impressions',confidence='low')
 if d['place']=='Diagonal by i.e.':d.update(reading='visible oblique stroke at first point, reproduced in TikZ',alternatives='purpose and intended attachment unresolved; no inferred correction to e=0',confidence='medium')
rem.append(dict(place='b) complement: thin hooked connector',reading='broad hooked relation retained around the right end of canceled b′) and below the added continuation',alternatives='precise starting attachment to a symbol in b) cannot be established',confidence='medium'))
spec['remaining_doubts']=rem
inv=copy.deepcopy(R['R3']['inventory'])
for d in inv:
 d['hand']=d['hand'].replace('pen','unnamed hand')
 if d['element']=='First centralizer formula including marks over e':d['first_words_or_objects']='Cent(e with two diagonal upper marks)=Cent(u)'
 if d['element']=='Raised restriction with curved enclosure and connection to Soient':d['first_words_or_objects']='avec e≠0, e nilpotent.; curved enclosure and downward connector'
inv.extend([
 dict(sheet_kind='typescript',hand='typewriter',element='Double impression of first L in Lie(i)(1)',kind='text',position='first theorem definition, x=Lie(i)(1)',first_words_or_objects='two offset L impressions, followed by ie',transcribed='yes'),
 dict(sheet_kind='typescript',hand='unnamed hand',element='Thin hooked connector beside canceled b′) and below its right-hand addition',kind='drawing',position='between b) and c), to the right of canceled b′)',first_words_or_objects='hook and long lower line, distinct from strike and Dynkin underline',transcribed='yes'),
 dict(sheet_kind='typescript',hand='unnamed hand',element='Curved enclosure and downward leader around typed nilpotence restriction',kind='drawing',position='above Soient/Pour boundary',first_words_or_objects='curved ends, low joining line, downward leader',transcribed='yes')])
spec['inventory']=inv
spec['notes']=M['notes']
spec['check_events']=M['check_events']
for r in ('R1','R2','R3'):
 who='GPT-6 Astra Pro; inherited effort (not exposed); '+stem+'/'+r
 spec['check_events'].append(dict(statement_id='123-016-weight-plus2',who=who,type='targeted proof check',outcome='Independently performed the Jacobi weight-shift calculation during reading; recorded +2 shift. Definition after propre de remains literally blank.'))
 spec['check_events'].append(dict(statement_id='123-016-zero-exp',who=who,type='computation or formal certificate',outcome='Independently substituted e=0 in exp(e), obtaining 1; retained the contrary visible source equality/inequality.'))
spec['abbreviations']=R['R1']['abbreviations']
spec['consequential']=['123/016 b): the visible g(-2) target is retained; Jacobi and an explicit sl2 matrix computation expose the sign problem without emending it.','123/016 (ii): H’s e≠0 is rejected for the visible e=0; the separate slash remains at i.e., and the exp(0)=1 contradiction is recorded only in the notes.','123/016 d): two visible prime-like strokes on the second f remain uncertain; no differential convention is imposed.']
spec['workflow_note']='All three readers completed independent whole/half readings. Root viewed the 22 R1 crops, R2 b_annotation, R3 lie_stop and cent_accent, and six new crops for loci without reader crops. Initial display of R1 crops 01–03 was truncated and did not count as a view; they were displayed successfully one at a time. R3 supplied a no-new-image clarification of the b) connector from retained context. Disagreements showed that terminal edge points, overprinted letters and connector drawings need distinct treatment. Next brief clarifies that uncertainty changes are apparatus differences, and that connected enclosures should be drawn rather than converted to punctuation or dropped.'
# Every disagreement above has an explicit three-reader account. Normalize exact enum values.
for d in spec['additional_differences']:
 if d['kind']=='deletion state':d['kind']='deletion state (struck given live or live given struck)'
path=O/'decisions'/f'{stem}_spec.json';path.write_text(json.dumps(spec,ensure_ascii=False,indent=2));print(path)
# Assemble a temporary preview solely to check exact edit matches before the authorized finalizer.
t=(O/'readers'/stem/'R1'/'reading.tex').read_text()
for e in spec['text_edits']:
 assert t.count(e['old'])==1,(e['old'],t.count(e['old']))
 t=t.replace(e['old'],e['new'])
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print('All exact edits match; finalizer not invoked by this script.')
