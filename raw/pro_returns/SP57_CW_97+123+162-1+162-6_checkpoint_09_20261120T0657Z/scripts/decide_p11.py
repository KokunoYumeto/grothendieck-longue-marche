"""Assemble page 11 from root's actual local-image decisions, without recognition."""
from pathlib import Path
import json,copy,re
O=Path('out');stem='C123-02_123_scan028'
R={n:json.loads((O/'readers'/stem/n/'report.json').read_text()) for n in ('R1','R2','R3')}
T={n:(O/'readers'/stem/n/'reading.tex').read_text() for n in R}
r1=f'readers/{stem}/R1/crops/';r2=f'readers/{stem}/R2/crops/';r3=f'readers/{stem}/R3/crops/';root=f'decisions/rootcrops/{stem}/'
t=T['R1']
def change(a,b):
 global t
 assert t.count(a)==1,(a,t.count(a))
 t=t.replace(a,b)
def d(n,i):return next(x for x in R[n]['differences'] if x['id']==('D' if n=='R1' else n+'-D')+f'{i:02}')
def picture(s,start):
 a=s.index(r'\begin{tikzpicture}',start); depth=0
 for m in re.finditer(r'\\(begin|end)\{tikzpicture\}',s[a:]):
  depth+=1 if m.group(1)=='begin' else -1
  if depth==0:return s[a:a+m.end()]
 raise ValueError('unclosed picture')

change(r"resp. $\mathrm{u}_{\handwritten{*}}$, en un sens",'resp. $'+d('R2',3)['reading']+'$, en un sens')
change(r'\handwritten{(\deleted{\unsure{2|3}}3.2.1)}}',r'\handwritten{(\deleted{\unsure{2|3}}3.2.1)}\unsure{.}}')
change(r'\deleted{\unsure{(I 2.11)|(I 4.11)}}.',r'\deleted{(I \unsure{2.11|4.11})}.')
change(r'est \unsure{exact} à gauche',r'est ex\unsure{.|a}ct à gauche')
change(r'$\mathrm{u}^{\handwritten{*}}$ \deleted{qui},',d('R2',20)['reading']+r' \deleted{qui},')
change(r'$(\mathrm{u}_{\handwritten{*}},\mathrm{u}^{\handwritten{*}})$',d('R2',21)['reading'])
inverse=d('R2',33)['reading']
change(r'son image \deleted{inverse} par',r'son image '+inverse+' par')
change(r"\inserted{l'expliciter et de}",r"\inserted{l'"+d('R2',36)['reading']+'xpliciter et de}')
change(r'($\handwritten{*}$)',d('R2',43)['reading'])
change(r"pour un foncteur $\mathrm{u}_{\handwritten{*}}:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$",'pour un foncteur '+d('R2',47)['reading'])
change(r"$\mathrm{u}^{\handwritten{*}}:\mathrm{E}'\handwritten{\longrightarrow}\mathrm{E}$ donné",d('R2',48)['reading']+' donné')
oldleader=r'''\draw[line width=.3pt] (-.25,-.3) .. controls (-.5,.45) and (-.2,.8) .. (.7,.82) .. controls (3.5,.92) and (6.6,1) .. (7.4,.83) .. controls (7.8,.82) and (7.85,1.2) .. (8,1.55);'''
newleader=r'''% Three visible stretches: pale left return, interrupted middle, dark right upturn.
\draw[gray,line width=.3pt] (-.25,-.3) .. controls (-.5,.45) and (-.2,.8) .. (1.7,.82);
\draw[gray,line width=.3pt] (2.3,.82) .. controls (3.7,1.02) and (5.6,.98) .. (7.3,.83);
\draw[line width=.35pt] (7.3,.83) .. controls (7.8,.82) and (7.85,1.2) .. (8,1.55);'''
change(oldleader,newleader)
change(r'\end{tikzpicture}}, pour un foncteur',r'\end{tikzpicture}},pour un foncteur')
change(r'\draw[line width=.35pt] (-.25,-.28) .. controls (-.6,.3) and (-.1,.75) .. (.45,.83) .. controls (1.2,1.05) and (2.8,1.35) .. (3.35,1.7);',r'''\draw[gray,line width=.3pt] (-.25,-.28) .. controls (-.6,.3) and (-.1,.75) .. (.45,.83);
\draw[line width=.35pt] (.45,.83) .. controls (1.2,1.05) and (2.8,1.35) .. (3.35,1.7);''')
subdiv=picture(T['R3'],T['R3'].index('% GRAPHIC G15')).replace('(s.base)','(p28subdiv.base)').replace(' (s) ',' (p28subdiv) ').replace(r'\unsure{(ii)|(iii)|(i)}',r'\unsure{(ii)|(iii)|(i)|(ii|(iii|(i}')
subdiv=subdiv.replace(r'\draw[line width=.2pt] (.40,.33) .. controls (.49,.28) and (.56,.25) .. (.67,.24);',r'''\node[inner sep=0pt] at (.535,.285) {\unsure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[gray,line width=.2pt] (-.135,.045) .. controls (-.045,-.005) and (.025,-.035) .. (.135,-.045);
\end{tikzpicture}}};''')
change(r'1.2.\unsure{(ii)|(iii)|(i)}','1.2.\\mbox{'+subdiv+'}')
change(r'''\draw[line width=.35pt] ([xshift=.375\linewidth,yshift=.04cm]p28r1footstart)
 .. controls ([xshift=.36\linewidth,yshift=-.4cm]p28r1footstart) and ([xshift=.345\linewidth,yshift=.35cm]p28r1footend)
 .. ([xshift=.325\linewidth,yshift=-.1cm]p28r1footend);''',r'''\draw[line width=.35pt] ([xshift=.375\linewidth,yshift=.04cm]p28r1footstart)
 .. controls ([xshift=.36\linewidth,yshift=-.4cm]p28r1footstart) and ([xshift=.35\linewidth,yshift=.6cm]p28r1footend)
 .. ([xshift=.342\linewidth,yshift=.36cm]p28r1footend);
\node[inner sep=0pt] at (0,0) {\unsure{\begin{tikzpicture}[remember picture,overlay]
\draw[gray,line width=.3pt] ([xshift=.342\linewidth,yshift=.36cm]p28r1footend)
 .. controls ([xshift=.336\linewidth,yshift=.20cm]p28r1footend) and ([xshift=.33\linewidth,yshift=.04cm]p28r1footend)
 .. ([xshift=.325\linewidth,yshift=-.1cm]p28r1footend);
\end{tikzpicture}}};''')
diag=r'''\mbox{\begin{tikzpicture}[baseline=(p28application.base),x=1em,y=1ex]
\node[anchor=base west,inner sep=0pt] (p28application) at (0,0) {application};
% Two visible light diagonal stretches; ink versus surface origin is unresolved.
\node[inner sep=0pt,anchor=base west] at (0,0) {\unsure{\begin{tikzpicture}[overlay,x=1em,y=1ex]
\draw[gray,line width=.2pt] (-.15,3.1) -- (1.6,1.75);
\draw[gray,line width=.2pt] (4.0,-.10) -- (5.6,-2.25);
\end{tikzpicture}}};
\end{tikzpicture}}'''
change('par application répétée','par '+diag+' répétée')
t+='\n% The pale end of the long cancellation is retained as a lighter continuation.\n% Small points and interrupted star rays are literal graphic details, not extra mathematical symbols.\n% The diagonal near application has no assigned textual significance.\n'

spec=dict(stem=stem,base_reader='R1',brief='reader_v11.md',main_new_crops=11,text_edits=[dict(old=T['R1'],new=t)],difference_overrides={},additional_differences=[])
def ov(i,**kw):spec['difference_overrides'].setdefault(f'D{i:02}',{}).update(kw)
for i,c in {2:'opening_prose.png',5:'exactness_prose.png',15:'exactness_prose.png',19:'second_underlined_clause.png',20:'second_underlined_clause.png',21:'structure_definition.png',22:'structure_definition.png',29:'internal_exactness.png',30:'internal_exactness.png',33:'formal_hesitation.png',36:'examples.png',38:'final_body_sentence.png',39:'separator.png',40:'vertical_cancellation.png',41:'footnote_criterion.png'}.items():ov(i,crop=root+c)
ov(34,crop=r2+'20_expliciter_insertion.png')
ov(1,confidence='low',readers='R1: first 2, alternative 7; R2: first 2, alternative 7; R3: first 7, alternative 2. Root retains 2|7: the rounded top and abbreviated basal return do not settle the first digit.')
ov(2,final=t[t.index(r'\deleted{un morphisme'):t.index('\n\n\\deleted{\\deleted{2}')],readers='All three agree on the opening prose and functor directions. R2 alone preserves a pale trace over the second u (ROOT/R2-D03); R3 alone preserves a clipped final point (ROOT-01). Those graphic disagreements are separately recorded.')
ov(4,readers='R1: old 2; R2: old 2|3; R3: old 2. Root resolves to 2 from the smaller diagonal and straight lower foot under the larger handwritten 3.')
ov(5,final=r'\deleted{'+t[t.index('Si $'):t.index('\n\\mbox{\\begin{tikzpicture}[baseline=(p28r1cest')]+r'}',H='Editorial synopsis: $u_*$ commute aux limites projectives et $u^*$ aux limites inductives et aux limites projectives finies, donc $u^*$ est exact; selected insertion quoted separately.',readers='The three full readings agree on this prose and the finite-limit hypothesis. The section digit, old references and small exact form are separately adjudicated.')
ov(7,final=r'\margin{\handwritten{\deleted{(I \unsure{2.11|4.11})}.}}',readers='R1: (I 2.11)|(I 4.11), beside inductives; R2: also (I 4.1), beside inductives; R3: I and parentheses definite, 2.11|4.11|4.1, but margin placed after the body. Root excludes 4.1, localizes doubt after definite I, and anchors beside inductives.')
ov(8,readers='R1: (2.11)|(I 2.11); R2/R3: also (2.1). Root excludes (2.1): two distinct final upright stems remain.')
ov(9,readers='R1 draws definite star with two additional extended lower prongs; R2/R3 use a plain star in parentheses. Root retains the two lower prongs as uncertain-function traces, with the point and no-space ).Comme boundary definite.')
ov(10,final=r'est ex\unsure{.|a}ct à gauche i.e.',c_changed=True,readers='R1: whole exact uncertain; R2/R3: ex(a|.)ct. Root reads definite e,x,c,t and a filled central point, so writes ex(.|a)ct with point first.',evidence='The e, x, c and final t are separable. Between x and c lies a filled short point without a visible a bowl. The normal word does not decide the first candidate.')
ov(11,readers='All three draw the main curved leader. R1 also draws the separate upper point, treated in D12; R2/R3 omit that point.')
ov(12,readers='R1: separate doubtful point above/right leader; R2: omitted; R3: omitted. Root retains the visible point without deciding ink or surface origin.')
ov(20,evidence=d('R1',20)['evidence']+' Root checked the first underline in R1 crop 09_on_peut_cest.png and the second in the root second_underlined_clause crop.')
ov(19,final=r"\uline{qui possède les propriétés d'exactitude les plus remarquables}")
ov(22,final=t[t.index('Ces propriétés assurent'):t.index('\n\\mbox{\\begin{tikzpicture}[baseline=(p28r1tout')],H='Editorial synopsis: espèce de structure algébrique ... définie par des limites projectives finies et des limites inductives quelconques.',readers='All three agree on the complete prose. The Sigma leader, faint arc, blank-cell x and newly noticed diagonal are recorded separately; the diagonal was omitted by all three.')
ov(24,readers='R1/R2/R3 all draw a separate faint shallow arc under Sigma; no disagreement in its presence. Function and ink/surface status remain open.')
ov(26,readers='R1/R2 draw the returning/upturned right hook; R3 ends with a rising segment without the return. Root retains the short returning hook visible in R1 crop 12.')
ov(27,final=r"\handwritten{``}objet de $\underline{\mathrm{E}}'$ muni d'une structure d'espèce $\handwritten{\Sigma}$''",evidence=d('R1',27)['evidence']+' Root checked the closing pair on internal_exactness.png as well as the opening in R1 crop 12.')
ov(28,final=r"$\underline{\mathrm{E}}'$",readers='All three: ordinary E with separate underline and prime. No same-letter double impression at this locus.')
heavy=picture(t,t.index('% E is certain')-200)
ov(29,final=t[t.index('(notion qui a un sens'):t.index(', son image')],readers='All three agree on the parenthetical prose and (II 4.1). The E lower material is separately adjudicated in D31; H omits this entire parenthesis.')
ov(31,final=heavy,readers='R1: ordinary E plus uncertain lower bar/right upturn; R2: ordinary E plus thick lower rectangular material; R3: ordinary E plus uncertain curved lower reinforcement. Root retains R1’s lower bar and right upturn; a second complete E is not separable. H has no reading for this parenthetical E.',H='')
ov(32,final=inverse,crop=r2+'19_inverse_cancellation.png',c_changed=True,kind='drawing or diagram',H='Editorial synopsis uses “l’image inverse par $u^*$”; it does not quote this cancelled source locus.',readers='R1/R3 mark inverse deleted without its shaped strike; R2 also draws the horizontal stroke, left upright and right upturn. Root adopts those visible contours.',evidence='Inverse is locally crossed by a heavy horizontal stroke with a separate left upright and right upturn. Son image and par remain locally live. H’s synopsis is a paraphrase, so its wording is not treated as a verbatim live reading of this locus; it omits the source cancellation and its drawing.')
ov(33,H='Quoted advice: « nous conseillons au lecteur de se convaincre de sa validité »; preceding refusal of formal justification is not transcribed.',evidence='The crop reads est muni and the entire Plutôt que d’entrer ... donner un sens précis ... justifier de façon formelle passage. H quotes the later reader advice but omits this explicit refusal and the source wording connecting it.')
ov(34,final=picture(t,t.index('baseline=(p28r1se.base)')-30),readers='All three preserve the raised typed insertion and leader. R2 alone draws the additional short diagonal at the first e; that extra trace is separately recorded as R2-D36.')
ov(35,readers='R1: three descending-left points; R2: omitted; R3: three descending-left points. Root confirms exactly three, with function/origin unresolved.')
ov(36,final=t[t.index('des espèces de structure telles'):t.index(' (Dans ces exemples')],readers='All three agree on the singular celle, all six examples and repeated qualifiers. The two extra cancellation x cells are separately recorded in D37.')
ov(40,final=t[t.rindex(r'\handwritten{\figure{'):t.index('\n% The pale end')],readers='R1: upper/lower paths, two detached points and a short segment at the raised footer reference; R2: main line with pale lower continuation; R3: continuous main line. Root retains R1’s interruption components and R2’s lighter lower continuation.',evidence='The root long local strip shows the slightly bowed main cancellation from the opening through the body and footnote, with a fading lower continuation. R1 crop 17_verifier_reference.png separately shows two detached points and a short segment at its intersection with the raised reference; those components are retained.')
foot=t[t.index(r'\deleted{($\handwritten{'):t.index('% The right image edge')]
ov(41,final=foot,H='Editorial note quotes the corrected vérifier and the cancelled final consequence; no full footnote transcription.',readers='All three agree on the adjoint criterion and directions. R3 alone keeps ,pour without a blank; R1/R2 insert a space. Root chooses R3. The marker and two star fragments, ce correction and last subdivision are separately adjudicated.')
ov(42,confidence='medium',readers='R1/R2: On peut; R3: On p(eu)t with local doubt. Root resolves On peut: the low e/u parts, p descender and final t survive the crossing.')
ov(45,final=picture(t,t.index('baseline=(p28r1verifier.base)')-30),readers='R1 draws a continuous reference leader; R2/R3 draw interrupted stretches. Root chooses the visible pale left return, interrupted middle and dark right upturn, with real baseline words anchored in the picture.',evidence='The raised (1.5 et 1.8) is definite. Its lighter leader has separated visible stretches and a dark upturned right end; it is not one continuously visible stroke. The following comma is locally live.')
ov(46,readers='R1/R2: old d corrected to definite c; R3: old d and c|d. Root resolves c from the wider open pen contour, distinct from the small typed d ascender.')
ov(48,final=picture(t,t.index('baseline=(p28r1limites.base)')-30),readers='R1/R3 use one uniform leader; R2 distinguishes pale left part and darker right rise. Root adopts the tonal distinction while retaining the same curve and U placement.')
ov(50,readers='All three retain the cancelled D’ailleurs word with doubt. R1 also doubts the following comma; R2/R3 give a definite comma, separately decided in D51.')
ov(51,readers='R1: doubtful comma; R2/R3: definite comma. Root retains doubt because the down-turn joins the cancellation and does not independently establish punctuation.')
ov(52,readers='All three preserve a separate faint down-right tail. Root distinguishes it from the nearby page cancellation, which descends left.')
ov(53,final='1.2.\\mbox{'+subdiv+'}',c_changed=True,readers='R1: ii|iii|i with closed parentheses; R2: iii|ii|i plus variants without closing parenthesis; R3: ii|iii|i plus drawn upper faint slant/lower heavy overrun. Root retains ii first, all stem-count alternatives and open variants, and R3’s two extra traces.',evidence='The typed 1.2. is definite. The following crossed cluster retains dotted narrow stems but does not settle their count or a closing parenthesis. A light upper-right slant and a separate heavy lower overrun remain and are drawn. H’s quotation stops at 1.2.')

for n,readers in [(3,'R1: omitted; R2: pale upright drawn; R3: omitted. Root retains R2’s visible trace with ink/surface doubt.'),(20,'R1: plain star; R2: explicit star with detached lower-right point; R3: star plus doubtful point. Root confirms the detached point and adopts R2 geometry.'),(21,'R1/R3: plain star; R2: detached lower-left point and separate lower-right ray. Root adopts the literal R2 graphic.'),(36,'R1/R3: first e without extra contour; R2: definite e plus doubtful upper-left diagonal. Root retains the definite letter and separate trace.'),(43,'R1/R3: plain star; R2: explicit star with detached lower-left point. Root adopts R2 graphic.'),(47,'R1/R3: plain lower star; R2: explicit star with detached lower-right point. Root adopts R2 graphic.'),(48,'R1/R3: plain upper star; R2: explicit star with detached lower-right point. Root adopts R2 graphic.')]:
 x=copy.deepcopy(d('R2',n));x['final']=x.pop('reading');x['marked_in_H']='no';x['readers']=readers
 spec['additional_differences'].append(x)
spec['additional_differences'] += [
 dict(id='ROOT-01',place='Clipped point after the opening reference',C=r'(\deleted{\unsure{2|3}}3.2.1)',H='« (3.2.1) »',final=r'(\deleted{\unsure{2|3}}3.2.1)\unsure{.}',evidence='A small round dark bulge is partly clipped just after the closing parenthesis at the image edge. It is retained with punctuation doubt.',confidence='low',kind='omission',marked_in_H='no',c_changed=True,h_changed=True,crop=r1+'02_opening_reference.png',bbox=[1668,311,1683,339],bbox_source='source/SP57_CW_97+123+162-1+162-6_scans/'+stem+'.jpg',readers='R1: no final point; R2: no final point; R3: doubtful clipped point. Root retains R3’s point.'),
 dict(id='ROOT-02',place='Footnote comma immediately before pour',C=', pour',H='No full footnote text',final=',pour',evidence='The comma is locally live and the following p occupies the immediately next typewriter cell, without an intervening blank cell.',confidence='high',kind='other',marked_in_H='no',c_changed=True,h_changed=True,crop=root+'footnote_criterion.png',bbox=[978,1880,1080,1919],bbox_source='source/SP57_CW_97+123+162-1+162-6_scans/'+stem+'.jpg',readers='R1: comma and space; R2: comma and space; R3: comma without space. Root follows R3.'),
 dict(id='ROOT-03',place='Light interrupted diagonal near flèches and application',C='',H='',final=diag,evidence='Two light descending-right stretches are visible: below flèches and across/below application toward the next-line gap. Their ink-versus-surface status and function are unresolved; both are drawn without assigning them to letters or an editing instruction.',confidence='low',kind='drawing or diagram',marked_in_H='no',c_changed=True,h_changed=True,crop=root+'structure_definition.png',bbox=[565,1035,738,1147],bbox_source='source/SP57_CW_97+123+162-1+162-6_scans/'+stem+'.jpg',readers='R1: omitted; R2: omitted; R3: omitted. Root preserves the two visible diagonal stretches with doubt.')]

cd=copy.deepcopy(R['R1']['c_doubts'])
for x in cd:
 p=x['place']
 if p=='Left marginal reference':x['decision']=r'\deleted{(I \unsure{2.11|4.11})}.'
 if p=='est exact à gauche i.e.':x.update(decision=r'est ex\unsure{.|a}ct à gauche i.e.',evidence='Definite e,x,c,t; filled central point, no separate bowl. The expected word does not determine the first alternative.')
 if p=='Final reference subdivision':x['decision']=r'\unsure{(ii)|(iii)|(i)|(ii|(iii|(i}; retain uncertain count/closure plus upper faint and lower heavy traces.'
 if p=='Own page number in prior C notes':x['confidence']='low'
 if p=='Agreement est muni':x['crop']=root+'formal_hesitation.png'
 if p=='Singular celle':x['crop']=root+'examples.png'
 if p=='des ensembles déduits':x['crop']=root+'structure_definition.png'
 if p=='Body right edge':x['crop']=root+'final_body_sentence.png'
 if p=='Footnote after droite':x['crop']=root+'footnote_criterion.png'
spec['c_doubts']=cd
rd=copy.deepcopy(R['R1']['remaining_doubts'])
for x in rd:
 if x['place']=='Own page number':x['confidence']='low'
 if x['place']=='Cancelled marginal reference':x['reading']=r'(I \unsure{2.11|4.11})'
 if x['place']=='Inserted exact':x.update(reading=r'ex\unsure{.|a}ct',alternatives=['ex.ct','exact'],confidence='medium')
 if x['place']=='Final reference subdivision':x.update(reading=r'\unsure{(ii)|(iii)|(i)|(ii|(iii|(i}',alternatives=['ii, iii or i; closing parenthesis present or clipped/covered'])
rd += [dict(place='Opening reference final point',reading=r'\unsure{.}',alternatives=['clipped punctuation point','unassigned edge trace'],confidence='low'),dict(place='Pale upright above opening second u',reading='short upright drawn',alternatives=['ink trace','surface trace'],confidence='low'),dict(place='Extra diagonal at first e of expliciter',reading='definite e plus short upper-left diagonal',alternatives=['additional impression','irregular letter contour'],confidence='low'),dict(place='Diagonal near flèches/application',reading='two light descending-right stretches drawn',alternatives=['ink of unestablished function','surface trace'],confidence='low'),dict(place='Pale lower continuation of page cancellation',reading='lighter lower continuation drawn',alternatives=['fading cancellation stroke','coincident surface trace'],confidence='low')]
rd.append(dict(place='Light upper trace at final subdivision',reading='short upper-right descending slant drawn',alternatives=['pen trace of unestablished relation to the cancelled reference','surface trace'],confidence='low'))
spec['remaining_doubts']=rd
inv=copy.deepcopy(R['R1']['inventory'])
for x in inv:
 x['hand']=x['hand'].replace('handwritten','unnamed handwriting').replace('typescript','typewriter')
 if 'marginal reference' in x['element'].lower():x['first_words_or_objects']=r'(I \unsure{2.11|4.11}).'
 if x['element']=='Final cancelled subdivision':x['first_words_or_objects']='ii|iii|i with uncertain closing parenthesis, upper light slant and lower heavy overrun'
def invadd(element,position,first,hand='unnamed handwriting or surface trace',kind='drawing'):
 inv.append(dict(sheet_kind='cancelled_draft',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
invadd('Pale upright above opening second u',[1342,224,1351,244],'short pale upright, origin unresolved')
invadd('Clipped point after opening reference',[1668,311,1683,339],'doubtful point after closing parenthesis')
invadd('Detached point at star after image inverse',[1170,727,1178,738],'star plus detached lower-right point','unnamed handwriting')
invadd('Interrupted second star in functor pair',[380,779,425,825],'lower-left point and separate lower-right ray','unnamed handwriting')
invadd('Light interrupted diagonal near application',[565,1035,738,1147],'two descending-right stretches, origin/function unresolved')
invadd('Shaped pen cancellation of inverse',[1400,1267,1580,1344],'horizontal stroke, left upright, right upturn','unnamed handwriting')
invadd('Additional diagonal at expliciter e',[1235,1467,1260,1497],'definite e with upper-left extra contour','typewriter or unnamed retouch')
invadd('Footnote marker detached star point',d('R2',43)['bbox'],'lower-left detached point','unnamed handwriting')
invadd('Footnote direct-image star detached point',d('R2',47)['bbox'],'lower-right detached point','unnamed handwriting')
invadd('Footnote inverse-image star detached point',d('R2',48)['bbox'],'lower-right detached point','unnamed handwriting')
invadd('Final subdivision upper trace and lower overrun',[1622,2052,1683,2137],'light upper slant and heavy lower stroke','unnamed handwriting')
invadd('Pale lower continuation of long cancellation',[719,1998,778,2129],'lighter descending-left continuation')
# Preserve top-to-bottom order even for the supplemental trace inventory.
inv.sort(key=lambda x:(x['position'][1] if isinstance(x.get('position'),list) else 9999,x['position'][0] if isinstance(x.get('position'),list) else 9999))
spec['inventory']=inv
spec['notes']=(O/'decisions'/f'{stem}_notes.md').read_text()
spec['abbreviations']=R['R1']['abbreviations']
spec['abbreviations'].append(dict(form='ex.ct (doubtful point reading in ex(.|a)ct)',expansion='Possibly exact with an internal abbreviation point; conditional interpretation only. The trace may instead be the compressed a of exact.'))
spec['consequential']=['The typed ordinary underlined U in the adjoint criterion is preserved; H’s script U is unsupported by the ink.','The parenthetical E has uncertain extra lower material, not a resolved second E impression; no definite blackboard E is supplied.','The finite-projective-limit phrase remains locally live after the raised exactness insertion; H’s replacement interpretation is rejected.','The adjoint criterion was checked only under explicit universe and topos structural hypotheses; none of the unseen numbered references was verified.']
spec['check_events']=[dict(statement_id='123-028-reader-adjoint-preservation-R1',who='GPT-6 Astra Pro; inherited effort (not exposed); fresh R1 page 11',type='targeted proof check',outcome='R1 wrote the Hom/Yoneda calculation for right-adjoint limit preservation and its dual for left-adjoint colimits; no general structure or converse theorem proof claimed.'),dict(statement_id='123-028-reader-variance-preservation-R2',who='GPT-6 Astra Pro; inherited effort (not exposed); fresh R2 page 11',type='used and rechecked in this run',outcome='R2 checked domains/targets with the adjunction Hom relation and rechecked the preservation direction plus the separately stated finite-limit assumption. The footer sufficiency was read, not proved by this reader.'),dict(statement_id='123-028-reader-variance-R3',who='GPT-6 Astra Pro; inherited effort (not exposed); fresh R3 page 11',type='used and rechecked in this run',outcome='R3 checked typing and variance of u* and u_* and the direction of the stated preservation assertions only; no adjoint-existence or general structure proof claimed.')]
spec['workflow_note']='Three fresh independent readers used v11, with 22/29/21 crops. Root compared all complete readings and reports, viewed every R1 crop, R2 crops 03/14/15/19/20/22/24/25, R3 crops 15/20, and eleven new local crops for H-omitted prose, the separator and the long cancellation. A five-image output at a context boundary failed; each saved image was then displayed separately, and the failed output was not counted as observation. The existing structure-definition crop was revisited once for a newly noticed diagonal, without recropping. A text-only union audit checked graphics against actual TeX and separated H’s synopsis from its quoted source contexts. R1’s baseline word anchors were retained; R3’s empty-anchor geometry was not adopted. Supplemental star fragments, the inverse strike, expliciter contour, clipped point and final subdivision traces were merged into the text and inventory. Eight root mathematical events were already logged at 04:20:43; finalization adds only the three actual reader check events. v12 will explicitly require synopsis/quotation separation and genuine baseline anchors for attached leaders.'
(O/'decisions'/f'{stem}_spec.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
(O/'decisions'/f'{stem}_preview.tex').write_text(t)
print(json.dumps({'loci':len(R['R1']['differences'])+len(spec['additional_differences']),'inventory':len(inv),'remaining':len(rd)}))
