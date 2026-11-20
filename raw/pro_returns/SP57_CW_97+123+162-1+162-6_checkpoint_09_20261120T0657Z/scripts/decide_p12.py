"""Page 12 assembly from the main reader's recorded local-image decisions."""
from pathlib import Path
import json,copy,re
O=Path('out'); stem='C123-02_123_scan040'
R={n:json.loads((O/'readers'/stem/n/'report.json').read_text()) for n in ('R1','R2','R3')}
T={n:(O/'readers'/stem/n/'reading.tex').read_text() for n in R}
r1=f'readers/{stem}/R1/crops/';r2=f'readers/{stem}/R2/crops/';root=f'decisions/rootcrops/{stem}/'
t=T['R2']
def change(a,b):
 global t
 assert t.count(a)==1,(a,t.count(a));t=t.replace(a,b)
def d(n,i):return next(x for x in R[n]['differences'] if x['id']==n+'-D'+(f'{i:03}' if n=='R3' else f'{i:02}'))
def pic(s,start):
 a=s.index(r'\begin{tikzpicture}',start);depth=0
 for m in re.finditer(r'\\(begin|end)\{tikzpicture\}',s[a:]):
  depth+=1 if m.group(1)=='begin' else -1
  if depth==0:return s[a:a+m.end()]
 raise ValueError('unclosed picture')

page=r'''\mspage{\handwritten{\begin{tikzpicture}[baseline=(p.base)]
\node[inner sep=1pt] (p) {23};
\draw ([xshift=-1mm,yshift=-1mm]p.south west) .. controls ([xshift=1mm,yshift=2mm]p.north west) and ([xshift=2mm,yshift=2mm]p.north east) .. ([xshift=1mm,yshift=.4mm]p.north east);
\end{tikzpicture}}}'''
change(r'\mspage{\handwritten{23}}',page)
oldles=pic(t,t.index('baseline=(op.base)')-30)
newles=r'''\begin{tikzpicture}[baseline=(op.base)]
\node[inner sep=0pt] (op) {opérations};
\node[anchor=south west,inner sep=0pt] at ([xshift=-.35em,yshift=-.3ex]op.north west) {les};
% The pale rising trace has no assigned alphabetic or editorial function.
\node[inner sep=0pt] at ([xshift=.4em]op.north west) {\unsure{\begin{tikzpicture}[overlay,x=1em,y=1ex]
\draw[gray,line width=.3pt] (-.6,-.65)--(-.6,-.2) .. controls (-.05,.4) and (.6,.9) .. (.9,1.8);
\end{tikzpicture}}};
\end{tikzpicture}'''
change(oldles,newles)
change(r'\draw ([xshift=-.25em,yshift=-.4ex]plus.south west) .. controls (plus.south west) and ([yshift=-.3ex]plus.south east) .. ([yshift=-.3ex]plus.south east);',r'''\draw ([xshift=-.25em,yshift=.5ex]plus.south west) .. controls ([xshift=-.5em,yshift=.6ex]plus.south west) and ([xshift=.2em,yshift=-.3ex]plus.south west) .. ([xshift=.7em,yshift=-.3ex]plus.south west)
-- ([xshift=-1em,yshift=-.3ex]plus.south east) .. controls ([xshift=-.4em,yshift=-1.5ex]plus.south east) .. ([xshift=.1em,yshift=-.7ex]plus.south east);''')
parmi=r'''\begin{tikzpicture}[baseline=(dans.base)]
\node[inner sep=0pt] (dans) {\deleted{dans}};
\node[anchor=south west,inner sep=0pt] at ([yshift=-.35ex]dans.north west) {\inserted{parmi}};
\end{tikzpicture}'''
change(r'\deleted{dans}\inserted{parmi}',parmi)
presence=r'''\begin{tikzpicture}[baseline=(estp.base)]
\node[inner sep=0pt] (estp) {est};
\node[anchor=base west,inner sep=0pt] at ([xshift=.6em]estp.base east) {présenced'};
\node[anchor=south west,inner sep=0pt] at ([xshift=.1em,yshift=-.3ex]estp.north east) {\inserted{\handwritten{en}}};
\end{tikzpicture}'''
change(r"\inserted{est \inserted{\handwritten{en}} présenced'}",r'\inserted{'+presence+'}')
oldintuition=pic(t,t.index('baseline=(intuition.base)')-30)
newintuition=oldintuition.replace(r'\end{tikzpicture}',r'''\handwritten{
\draw[line width=.4pt] ([xshift=-.05em,yshift=.25ex]intuition.base west)--([xshift=.9em,yshift=1.3ex]intuition.base west);
\draw[line width=.4pt] ([xshift=.35em,yshift=-.05ex]intuition.base west)--([xshift=.85em,yshift=.5ex]intuition.base west);}
\end{tikzpicture}''')
change(oldintuition,newintuition)
change(r'(f.south west)--(f.north west)',r'(f.south west) .. controls ([xshift=-1mm]f.west) .. (f.north west)')
change(r'(u.south west)--(u.north west)',r'(u.south west) .. controls ([xshift=-.6mm]u.west) .. (u.north west)')
# The common point is the actual right border of the u-map enclosure.
assert t.count(r'\draw ([xshift=-.3em]est.west)')==2
t=t.replace(r'\draw ([xshift=-.3em]est.west)',r'\draw (u.east)')
atrace=r'''\begin{tikzpicture}[baseline=(a.base)]
\node[inner sep=0pt] (a) {\handwritten{à}};
\node[inner sep=0pt] at (a.north west) {\unsure{\begin{tikzpicture}[overlay,x=1ex,y=1ex]
\draw[gray,line width=.25pt] (.1,2.2) .. controls (.02,1.5) and (.02,.8) .. (-.05,.25);
\draw[gray,line width=.25pt] (-.05,.1)--(.08,-.4);
\end{tikzpicture}}};
\end{tikzpicture}'''
change(r'qui est \handwritten{à} la source',r'qui est '+atrace+' la source')
t=t.replace('(x) {x};',r'(x) {\texttt{x}};').replace(r'del.base west) {x};',r'del.base west) {\texttt{x}};')

spec=dict(stem=stem,base_reader='R2',brief='reader_v12.md',main_new_crops=9,text_edits=[dict(old=T['R2'],new=t)],difference_overrides={},additional_differences=[])
def ov(i,**kw):spec['difference_overrides'].setdefault(f'R2-D{i:02}',{}).update(kw)
maps={1:r1+'22_page_number.png',2:root+'opening_prose.png',3:r1+'01_top_deleted.png',4:r1+'01_top_deleted.png',5:r1+'02_top_verb.png',6:r1+'02_top_verb.png',7:r2+'04_top_initial.jpg',8:r2+'04_top_initial.jpg',9:r1+'04_de_plus_boundary.png',10:r1+'04_de_plus_boundary.png',11:r1+'05_margin.png',12:r1+'05_margin.png',13:root+'direct_body_upper.png',14:r1+'06_direct_map.png',15:r1+'07_insertions.png',16:r1+'07_insertions.png',17:r1+'07_insertions.png',18:r1+'08_contre_ne.png',19:r1+'09_punctuation.png',20:r1+'10_deleted_clause.png',21:r1+'10_deleted_clause.png',22:r1+'11_second_note_start.png',23:r1+'11_second_note_start.png',24:r1+'12_section_correction.png',25:root+'section_body_upper.png',26:r1+'12_section_correction.png',27:r1+'12_section_correction.png',28:r1+'13_properties.png',29:r1+'13_properties.png',30:r1+'14_cancelled_exact.png',31:r1+'14_cancelled_exact.png',32:r1+'15_qui_une.png',33:root+'section_body_middle.png',34:r1+'16_lower_formulas.png',35:r1+'16_lower_formulas.png',36:r1+'17_quotes.png',37:r1+'18_final_g.png',38:r1+'19_footer_start.png',39:r1+'20_footer_end.png',40:r1+'20_footer_end.png',41:r1+'20_footer_end.png',42:root+'footer_separator.png',43:root+'final_body.png'}
for i,p in maps.items():ov(i,crop=p)
for i in range(1,44):
 if d('R2',i)['H'].startswith(r'\note{Feuillet'):
  ov(i,H='Editorial synopsis only; no literal transcription of this source locus.')
ov(1,final=page,c_changed=True,kind='drawing or diagram',H='Own manuscript number not transcribed; H’s page{39} is an archive reference.',readers='R1: 23 with a separate rising partial arch; R2: 23 only; R3: 23 only. Root retains the separate rising stroke and upper-right curl. The lower horizontal boundary belongs to the top marginal note, not to an extra circle around 23.',evidence='The two numerals are 2 and 3. A separate pen stroke rises from below their left toward their upper right and turns down at its end. It is drawn without adding a closed enclosure.')
ov(2,final='sent en termes de limites projectives finies exclusivement, tandis que les autres notions impliquent implicitement des constructions faisant appel également à des limites inductives)',evidence='Root read the three typed opening lines on opening_prose.png. The fragment sent is visible, with no supplied prefix. The final trace and bracket are separately adjudicated in D10.',readers='All three agree on the opening prose. Their differing placement of the top continuation is separately recorded; no word is supplied from another scan.')
ov(7,final=newles,readers='R1: les inline before opérations; R2: les above/left of opérations; R3: les inline. Root confirms the raised position. The separately visible pale slant is a new root locus, not part of the word reading.')
ov(8,final=t[t.index(r'\inserted{\handwritten{\figure{'):t.index('\n\nsent ')],readers='R1/R3 draw one low loop and shaft; R2 also preserves the filled joining blob above the open lower loop. Root adopts that extra dark material. All three preserve the left and stepped lower enclosure.',evidence=d('R2',8)['evidence']+' Root also checked the lower step in R1/03_top_examples.png; the right-hand boundary near the own number is visible in R1/22_page_number.png.')
ov(10,readers='R1: doubtful separate close-shaped pen trace, both heavy brackets placed before Quant; R2: doubtful close-shaped trace and heavy closing bracket attached to the preceding stop; R3 final: definite connected thin boundary from that trace to De plus. Root keeps the close-shaped trace locally uncertain and the heavy closing bracket at the stop. Its physical connection to the upper boundary is not established by the visible interval.',evidence='A definite typed close is followed by a thinner bowed pen trace and the typed stop; a heavy closing bracket surrounds the break. Root does not turn the thin trace into a certain second punctuation parenthesis or assert R3’s connected topology. The opening Quant bracket is recorded separately.')
ov(13,final=t[t.index('foncteur image directe'):t.index(r'\inserted{\handwritten{Par suite, il ne')],H='Editorial synopsis: direct image respects limit-defined structures, is generally not right exact, and this is the source of later cohomological properties.',evidence=d('R2',13)['evidence']+' Root read the upper body on direct_body_upper.png and the rest, including both bare épimorphisme occurrences and the cohomological parenthesis, on direct_body_lower.png. Local graphic loci have their own rows.')
ov(17,final=parmi,c_changed=True,kind='insertion or placement',readers='All three identify cancelled dans and raised parmi in their reports, but all three saved texts flatten the addition inline. Root preserves the actual position of parmi above the cancelled cells.',evidence='The source has readable d-a-n-s under typewriter cancellation and p-a-r-m-i directly above. The new node layout encodes the height visible in the crop; an insertion wrapper alone does not do so.')
ov(18,readers='R1/R2/R3 final: literal c/f superposition, chronological order unresolved. Root confirms the tall f hook and open c bowl; C’s definite old-f/final-c assignment is not adopted.')
ov(19,readers='R1: unsure semicolon|comma; R2: drawn loop, tall shaft and detached upper angle; R3: drawn loop/tail, rising segment and detached upper hook. Root adopts R2’s literal drawing and retains punctuation uncertainty.',evidence='The mark includes a low dark loop/tail, a long rising stroke and a separate short upper angular stroke. A conventional semicolon drops visible ink. The following large open parenthesis is separate, and is in pen.')
ov(21,final=t[t.index(r'\begin{tikzpicture}[baseline=(del.base)]'):t.index('\nce défaut')],readers='R1: leading extra x and doubtful short rising pen trace, no explicit interword x cells; R2: leading lowered x, four interword x marks, horizontal strike and rising trace; R3: leading x and pen traces, no separate interword x cells. Root confirms all five extra cells and both pen traces. The upper tick’s function is not assigned.',evidence='The leading x is lower than the following word cells. Four further x impressions occur between comme/nous/le/verrons/au. A separate horizontal pen stroke crosses the beginning, with a short rising tick at the first x.')
ov(22,readers='All three separate the handwritten Par suite line from the typed section replacement; H joins them. R1 makes transforme pas certain; R2/R3 qualify transforme and R2 also qualifies cancellation of lower pas. Those reading/state differences are recorded in D23.')
ov(23,readers='R1: deleted transforme pas, certain; R2: deleted unsure transforme and pas|deleted pas; R3: deleted unsure transforme pas with definite cancellation of pas. Root follows R2: the dense middle crossing does not establish all letters, and its extent over most of the lower pas is not secure.',evidence='The raised s’étend pas is legible. Below it, a t-like beginning, f descender and covered medial strokes support tentative transforme. Most of the lower pas retains a formed outline beyond the strongest cancellation; its live/deleted state remains locally doubtful.')
ov(25,final=t[t.index("En pratique, lorsqu'on"):t.index("\ny compris l'existence")],H='Editorial synopsis: 3.1.3 discusses a functor f:E→F between topoi and its exactness. It uses calligraphic U in that synopsis; no literal transcription of the typed passage.',readers='All three agree on the opening prose, arrow direction and ordinary underlined typed U. R3 labels H’s synopsis alphabet a source-symbol misreading; root instead treats this as omission of literal text. The flattened nested en and the additional x are separately adjudicated.',evidence=d('R2',25)['evidence']+' Root read the full opening section line in R1/12_section_correction.png, the underlined U in R2/16_U.jpg, and the following lines in section_body_upper.png.')
ov(26,final=pic(t,t.index('baseline=(un.base)')-30),readers='All three read est, pen en, and adjacent présenced’, with the replacement above se donne/un. All three saved texts nevertheless put en on the same baseline within the raised phrase. Root raises en separately above the gap after est and preserves the leader to un. R2’s extra blank-cell x is retained (D27).',evidence='The pen en is visibly above the gap between typed est and présenced’. The source has no machine blank between présence and d’. The thin leader descends just before the following un. The nested layout preserves both levels.')
ov(27,final=r'\deleted{se}\tikz[baseline=(x.base)]{\node[inner sep=0pt] (x) {\texttt{x}};}\deleted{donne}',readers='R1/R3 mark se donne deleted as one phrase; R2 also draws the x in the former space. Root confirms and retains that separate cancellation impression.')
ov(29,readers='All three final readings preserve both é/t cells and leave their chronological order unresolved. Root confirms the two distinct mixed cells; neither grammar nor blackness establishes an earlier/final sequence.')
ov(31,final=t[t.index(r'\deleted{y}\tikz'):t.index("\ny compris l'existence")],readers='R1/R3 mark the ten words deleted but do not separately encode x impressions in their spaces; R2 draws nine interword x marks. Root confirms the run fills every intervening space and retains R2’s nine marks.')
ov(32,final=newintuition,readers='All three identify cancelled l’ and raised une with a leader. All three omit the two distinct oblique pen cancellation strokes over l’ from their saved drawings. Root retains the leader and adds those two strokes; the baseline intuition stays in the same node.',evidence='The cancelled l’ cells show typewriter x impressions plus two separate oblique pen strokes rising to the right. The longer curved insertion leader passes to their left and above them; it is not a substitute for either short strike. The preceding cancelled qui remains legible.')
ov(33,final=t[t.index("y compris l'existence"):t.index(r'\begin{tikzpicture}[baseline=(f.base)]')],H='Editorial synopsis summarizes exactness and the conditional f=u* interpretation, omitting the continuous prose on adjoints and geometric intuition.',evidence=d('R2',33)['evidence']+' Root read the adjoint/note-reference lines in section_body_upper.png, the central passage in section_body_middle.png and the final y a lieu d’écrire f sous la forme line in formula_introduction.png.')
ov(34,final=pic(t,t.index('baseline=(f.base)')-30),c_changed=True,readers='R1/R2: angular left side; R3: bowed left side. Root adopts the visible bow, keeping the top, right side, low feet, star and live comma.',evidence='The first formula’s left side bows outward between its top and lower foot. The comma is inside the open-bottom contour. C has a straight left side; the root drawing preserves the curvature.')
ov(35,final=pic(t,t.index('baseline=(u.base)')-30),readers='R1/R3 use a separate est-un picture; R2 uses one picture and claims contact, but its saved coordinates leave a gap. Root joins both arms to the actual right border (u.east). R1/R3 use one curved path, R2 two arms; the shared joining point is what the ink establishes.',evidence='Both arms around est un meet the right border of the u:F→E enclosure at the left of est. The upper arm rises toward the right and the lower arm underlines est un. The left side of this enclosure is also slightly bowed. Root encodes actual contact, not merely proximity in one picture.')
ov(37,final=r'gauche,\deleted{$\mathrm{g}$}\tikz[baseline=(x.base)]{\node[inner sep=0pt] (x) {\texttt{x}};}',readers='All three retain the readable cancelled g and separate following x. Root confirms the g’s lower oval and the next full x cell; no continuation is supplied.')
ov(39,readers='R1/R2/R3 all retain a doubtful comma after groupe. Root also cannot separate it securely from the returning terminal stroke; C’s definite comma is weakened, H omits it.')
ov(42,final=t[t.index('\n\\begin{tikzpicture}\n\\node[anchor=north west'):],readers='R1/R3 place the bottom continuation immediately after the earlier Par suite addition; R2 retains it beneath the final typed line, with its upper-loop call and separator. Root follows physical placement. All three describe the left step; the root crop confirms the rise then downward jog into the page-width line.',evidence='The long separator sits below the final typescript. It starts with a short rising left segment, bends downward, then continues across the page. The matching upper-loop call and en un continuation are below it; R1/19_footer_start.png and R1/21_footer_last.png supply the footer details.')
ov(43,final=r'''morphisme de topos, i.e. d'interpréter $\mathrm{f}$ comme un foncteur ``image inverse'' par une ````application continue'' de topos. Lorsque $\mathrm{f}$ commute aux limites projectives quelconques, donc qu'il admet un adjoint à gauche,\deleted{$\mathrm{g}$}\tikz[baseline=(x.base)]{\node[inner sep=0pt] (x) {\texttt{x}};}''',H='Editorial synopsis gives the inverse-image interpretation but not these final sentences or their cancellation state.')

def add(i,place,C,H,final,evidence,readers,crop,bbox,confidence='high',kind='drawing or diagram',c_changed=True,h_changed=True):
 spec['additional_differences'].append(dict(id=i,place=place,C=C,H=H,final=final,evidence=evidence,readers=readers,crop=crop,bbox=bbox,bbox_source='source/SP57_CW_97+123+162-1+162-6_scans/'+stem+'.jpg',confidence=confidence,kind=kind,marked_in_H='no',c_changed=c_changed,h_changed=h_changed))
quant=pic(t,t.index('baseline=(quant.base)')-30)
add('ROOT-01','De plus lower boundary with right dip',d('R1',10)['C'],d('R1',10)['H'],quant,'A long pen line begins beside De plus, runs beneath the addition and dips downward just before the right call sign. C omits this long line. Root retains the dip and the raised addition above Quant au.','R1/R3 draw a right dip; R2 draws a lower line without that dip. Root adopts the dipped contour, without asserting R3’s connection to the separate close-shaped trace.',r1+'04_de_plus_boundary.png',[1039,224,1681,345])
add('ROOT-02','Opening bracket attached to Quant au',d('R1',13)['C'],'H quotes Quant au but draws no bracket.',quant,'The heavy opening bracket runs above and below Quant au. It is separate from the heavy closing bracket around the preceding stop.','R1 places both bracket signs before Quant au; R2/R3 attach the closing sign to the preceding stop and the opening sign to Quant au. Root follows the latter geometry.',r1+'04_de_plus_boundary.png',[1039,224,1681,345],kind='insertion or placement')
add('ROOT-03','Top continuation kept above the opening typescript','Top continuation is embedded after the later De plus insertion.','H explicitly describes the continuation as at the top of the sheet.',t[t.index(r'\inserted{\handwritten{\figure{'):t.index('\n\nsent ')],'The top continuation occupies the upper margin, above the first typed line. The low-loop calls link it to De plus farther down the sheet. The source order is preserved while the calls retain the logical relation.','R1/R3 put the top note after De plus in logical reading order; R2 puts it before sent. Root retains R2’s physical order.',r2+'04_top_initial.jpg',[241,15,1668,147],kind='insertion or placement',h_changed=False)
add('ROOT-04','Pale hooked slant beneath raised les','','',newles,'A light rising-right stroke starts with a short downward hook left of the first o, passes beneath les and reaches the upper image edge. Its relation to the raised word, and whether it is ink or a surface trace, remain unresolved.','R1/R2/R3 omit the separate stroke. Root preserves it with local uncertainty without assigning a new letter or editing instruction.',r2+'04_top_initial.jpg',[280,15,330,46],confidence='low')
add('ROOT-05','Pale upright above and left of the added à',r'\handwritten{à}','No literal source transcription here.',atrace,'A pale near-vertical trace extends above the black added à and continues in a short lower slant. It is distinct in tone from the black letter, but its origin and function cannot be established.','All three retain à without this extra trace. Root retains the letter and draws the pale material separately under a local doubt.',root+'added_a_trace.png',[708,883,768,966],confidence='low')

# Witness columns contain literal supplied strings; editorial descriptions belong
# in the evidence, not in a field purporting to quote a witness.
Ctext=Path('packets/'+stem+'/C.tex').read_text()
for number,override in spec['difference_overrides'].items():
 if override.get('H','').startswith(('Editorial synopsis','Own manuscript number')):
  label=override['H']
  override['evidence']=override.get('evidence',next(x['evidence'] for x in R['R2']['differences'] if x['id']==number))+' H context: '+label
  override['H']=''
ov(1,H=r'\page{39}')
ov(13,H=r'''$u_*$
respecte toute structure algébrique définissable exclusivement en termes de
limites projectives, mais n'est en général pas exact à droite — source des
propriétés cohomologiques étudiées dans l'exposé suivant''')
ov(25,H=r'''3.1.3 : devant un
foncteur $f \colon E \to F$ d'un $\mathcal{U}$-topos dans un autre, expliciter
ses propriétés d'exactitude''')
ov(33,H=r'''s'il commute aux limites inductives quelconques
et aux limites projectives finies, l'écrire $f = u^*$ pour un morphisme de
topos $u \colon F \to E$''')
for item in spec['additional_differences']:
 if item['id']=='ROOT-02':item['H']="Quant au foncteur image\ndirecte $u_*$"
 if item['id']=='ROOT-03':
  item['C']=Ctext[Ctext.index('sent en termes'):Ctext.index('\n\n\\margin')]
  item['H']="\\note{en tête du feuillet, encadré, relié par un trait à l'insertion\nsuivante}"
 if item['id']=='ROOT-05':item['H']=''

cd=copy.deepcopy(R['R2']['c_doubts'])
for x in cd:
 p=x['place']
 if p=='Opening fragment':x['crop']=root+'opening_prose.png'
 if p=='Articles before épimorphisme':x['crop']=root+'direct_body_lower.png'
 if p=='Own page and corrected section number':x['decision']='Own page 23 with separate rising arch; typed 2 corrected to handwritten 3 in 3.1.3. The numeral and the graphic have distinct evidence (R1/22 and R1/12).'
 if p=='Interlinear section wording':x['decision']='Retain typed est présenced’ with no blank before d’; raise pen en separately above the gap after est; preserve the leader to un.'
 if p=='After inductives':x['decision']='Keep the separate close-shaped trace locally uncertain; do not assert a connection to the De-plus boundary.'
spec['c_doubts']=cd
rd=copy.deepcopy(R['R2']['remaining_doubts'])
rd.extend([dict(place='Pale hooked slant beneath les',reading='drawn pale rising-right stroke',alternatives=['insertion-related pen trace','surface trace; relation unresolved'],confidence='low'),dict(place='Pale upright above added à',reading='pale upright and short lower slant drawn separately',alternatives=['ink trace of unknown function','surface trace'],confidence='low'),dict(place='Upper tick beside leading cancellation x',reading='short rising pen tick retained',alternatives=['part of cancellation','unassigned pen mark'],confidence='low')])
spec['remaining_doubts']=rd
inv=copy.deepcopy(R['R2']['inventory'])
for x in inv:
 x['hand']=x['hand'].replace('handwritten','unnamed handwriting').replace('typewritten','typewriter')
 if x['element']=='Own page number':x['first_words_or_objects']='23, with separate rising partial arch'
 if x['element']=='Upper marginal continuation':x['kind']='margin note'
 if x['element']=='Footer continuation':x['kind']='margin note'
def invadd(element,bbox,first,hand='unnamed handwriting',kind='drawing'):
 inv.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position=dict(bbox=bbox,bbox_source='source/SP57_CW_97+123+162-1+162-6_scans/'+stem+'.jpg'),first_words_or_objects=first,transcribed='yes'))
invadd('Own number rising partial arch',[1598,73,1675,137],'rising stroke and short upper-right curl')
invadd('Pale slant beneath raised les',[280,15,330,46],'pale hooked rising-right trace','unnamed handwriting or surface trace')
invadd('Two pen strikes over cancelled l-apostrophe',[1182,1550,1228,1586],'two short rising-right oblique strokes')
invadd('Pale upright at added à',[708,883,768,966],'pale upright and short lower slant','unnamed handwriting or surface trace')
inv.sort(key=lambda x:(x['position']['bbox'][1],x['position']['bbox'][0]))
spec['inventory']=inv
spec['notes']=(O/'decisions'/f'{stem}_notes.md').read_text()
spec['abbreviations']=R['R2']['abbreviations']
spec['consequential']=['The top note reads fonctorielles, not H’s fonctionnelles.','The typed est présenced’, with raised pen en, belongs to section 3.1.3; H misattaches en présence d’ to the preceding handwritten line.','The footer begins en un foncteur, not H’s ou un foncteur.','The f:E→F and u:F→E directions, the upper/lower stars, and the ordinary underlined U are retained from the ink. H’s synopsis alphabet is not counted as a direct glyph error.','The fixed-point examples substantiate failures of epimorphism, torsor, free-module and tensor preservation; the bialgebra example concerns the inherited comultiplication only. No mathematical correction is inserted into the source.']
spec['check_events']=[dict(statement_id='123-040-reader-direction-'+n,who='GPT-6 Astra Pro; inherited effort (not exposed); fresh '+n+' page 12',type='used and rechecked in this run',outcome=n+' checked that f:E→F and u:F→E have the inverse-image variance required by f=u*. The reader also checked the two local lim-arrow directions. This was a notation/type check, not a proof of adjoint existence or preservation theorems.') for n in R]
spec['workflow_note']='Three fresh independent readers used v12; their crop counts were 22/25/22. Root compared all complete texts and reports, including R3’s final revised connected-boundary drawing, and viewed all 22 R1 crops, R2 crops 03/04/16, and nine new bounded crops. The new crops cover H-omitted prose, a separator, and the newly noticed pale trace near à. Two earlier image outputs at a context boundary were not counted as observations until displayed individually; a later transport failure was retried with the same saved image. Root chose R2 physical marginal placement, added R1’s page arch, R3’s bowed first formula side, and actual contact for the est-un arms. A fresh text-only audit exposed flattened parmi/en positions, an R1 TikZ coordinate defect, and a gap between R2’s claimed connected strokes. The unused original reader defect is documented; the consolidated paths and placements are repaired. Root also retained two pen strikes over l’, the top pale slant, and the pale à-adjacent trace. Ten root mathematical events were already recorded at 04:52:49; finalization adds only three actual reader direction checks. v13 will require physical marginal ordering, genuine nested raised positions, actual shared path endpoints, preservation of interword cancellation cells, and newline-safe TeX comments.'
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(json.dumps(dict(loci=len(R['R2']['differences'])+len(spec['additional_differences']),inventory=len(inv),remaining=len(rd))))
