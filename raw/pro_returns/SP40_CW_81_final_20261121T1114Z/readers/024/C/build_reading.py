from pathlib import Path
import json,re,hashlib
D=Path('out/readers/024/C')
meta={}
def group(name,tex,**kw):
 meta[name]=kw
 return '\n% BEGIN '+name+'\n'+tex.strip()+'\n% END '+name+'\n'
def pic(body,box='(0,-4) rectangle (30,15)'):
 return r'\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt,line cap=round,line join=round]'+'\n'+r'\path[use as bounding box] '+box+';\n'+body.strip()+'\n'+r'\end{tikzpicture}'
M01=group('C024-M01',pic(r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] (soitword) at (0,0) {soit};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1,12) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\fill (0,0)--(.5,.55)--(1.05,.05)--(.55,-.45)--cycle;\end{tikzpicture}}};''','(0,-2) rectangle (20,15)'),owns=['soit','one detached upper point'],reading='soit; detached diamond-shaped point',alternatives=[],qualification='Only the point has unresolved role, attachment, hand and surface origin; soit and its own i dot stay firm.',units='pt',origin='(0,0), base-west word node; point at (1,12)',baseline='0pt',wrapper='inline TikZ; point-only unsure')
G02=group('C024-G02',r'\unsure{'+pic(r'''% Complete states: \deleted{On a} | \deleted{On}. Editorial separators are not manuscript punctuation.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\phantom{\deleted{\unsure{On a|On}}}};
\draw[line width=.45pt] (4,11) .. controls (1,12) and (0,3) .. (1,1) .. controls (3,-1) and (8,0) .. (8,3) .. controls (7,6) and (5,7) .. (4,5);
\draw[line width=.8pt] (7,2)--(40,2);
\draw[line width=.55pt] (11,2)--(12,.5) (20,2)--(21,-.5);
\fill (36,2)--(37.5,3.1)--(39,3.2)--(41,1.7)--(39,2)--cycle;''','(0,-2) rectangle (43,13)')+'}',owns=['cancelled On a / On','crossing rule with two lower ticks and swollen terminal'],reading=r'\deleted{On a}',alternatives=[r'\deleted{On}'],qualification='Whole cancelled wording unresolved; following Considérons la is outside.',units='pt',origin='(0,0)',baseline='0pt',wrapper='unsure around literal cancelled group; deleted annotation invisible')
G03=group('C024-G03',r'\figure{'+pic(r'''% Owns the full old and raised lines. Live insertion: Relation R entre S et I.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\phantom{\deleted{\uline{Lemme} $\forall i\in I$,}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,22) {\phantom{\inserted{Relation $R$ entre $S$ et $I$}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (3,0) {Lemme};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (3,18) {Relation};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (59,29) {$R$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (76,22) {entre};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (162,26) {$S$ et $I$};
\draw[line width=.55pt] (105,24)--(119,-1)--(132,25);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (132,3) {$i\in I$,};
\draw[line width=.45pt] (0,0) .. controls (67,5) and (135,11) .. (179,15);
\draw[line width=.45pt] (3,-7) .. controls (20,-4) and (31,-9) .. (49,-7) .. controls (56,-6) and (61,-6) .. (65,-6);
% The long cancellation run also crosses the old forall body. No second generic strike is printed.''','(0,-10) rectangle (215,39)')+'}',owns=['deleted underlined Lemme','deleted forall i in I comma','inserted Relation R entre S et I','one crossing rule','one underline'],reading=r'\deleted{\uline{Lemme} $\forall i\in I$,} \inserted{Relation $R$ entre $S$ et $I$}',alternatives=[],qualification='The state and wording are firm; geometry is a manual approximation from crop05, without a chronology claim.',units='pt',origin='(0,0), all nodes base-west',baseline='0pt',wrapper='figure; invisible deleted and inserted annotations')
M02=group('C024-M02',r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1,17) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\fill (0,0)--(.65,.5)--(1,.05)--(.35,-.4)--cycle;\end{tikzpicture}}};',owns=['one detached point above overwritten glyph'],reading='detached point',alternatives=[],qualification='Role, attachment, hand and surface origin undetermined.',units='pt inherited from C024-G04',origin='node at (1,17)',baseline='node base west',wrapper='point-only unsure')
G04=group('C024-G04',r'\unsure{'+pic(r'''% Complete states: \deleted{U}(s | \deleted{E}(s. Both own the live opening parenthesis and s once.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\deleted{\unsure{U|E}}(s}$};
\draw[line width=.45pt] (0,9) .. controls (-1,16) and (2,17) .. (3,10)--(3,-1) .. controls (4,-4) and (7,-3) .. (8,0)--(8,12);
\draw[line width=.45pt] (2,11) .. controls (4,16) and (6,17) .. (7,14) (7,11) .. controls (9,16) and (11,15) .. (12,14);
\draw[line width=.6pt] (3,10)--(9,12) (3,1)--(9,10) (4,-1)--(8,9) (3,2)--(9,2);
\draw[line width=.45pt] (4,13) .. controls (1,7) and (1,-3) .. (12,-7);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (10,-1) {$s$};
'''+M02,'(-2,-8) rectangle (20,21)')+'}',owns=['cancelled U/E predecessor','live (s prefix','crossing diagonals'],reading=r'\deleted{U}(s',alternatives=[r'\deleted{E}(s'],qualification='Predecessor U/E unresolved. Live parenthesis and s stay present. Separate upper point has its own scope in M02.',units='pt',origin='(0,0)',baseline='0pt',wrapper='unsure around literal group; phantom deleted annotation')
G05=group('C024-G05',pic(r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (8,7) {def};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\overset{\text{def}}{\Longleftrightarrow}}$};
\draw[line width=.5pt] (6,5) .. controls (2,5) and (0,1) .. (0,0) .. controls (0,-2) and (3,-2) .. (5,-2)--(31,-.5);
\draw[line width=.5pt] (1,1)--(29,1);
\draw[line width=.6pt] (29,1)--(32,-.8) .. controls (33,-1.8) and (31,-2.5) .. (30,-2.6);''','(0,-4) rectangle (34,16)'),owns=['def','complete double-shaft arrow'],reading=r'\overset{\text{def}}{\Longleftrightarrow}',alternatives=[],qualification='def resolved without accent; two shafts and hooked returns preserved.',units='pt',origin='(0,0)',baseline='0pt',wrapper='inline literal arrow')
G06=group('C024-G06',r'\unsure{'+pic(r'''% Complete states: (S,I)\deleted{R}) | (S,I\deleted{)},R). Pipes are editorial alternatives.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\unsure{(S,I)\deleted{R})|(S,I\deleted{)},R)}}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (5,0) {$S,I$};
\draw[line width=.45pt] (5,14) .. controls (-1,10) and (-2,-4) .. (8,-4)--(15,-4);
\draw[line width=.6pt] (30,13) .. controls (31,6) and (29,-1) .. (26,-4);
\draw[line width=.45pt] (34,-2)--(37,11) .. controls (44,13) and (43,7) .. (37,6) .. controls (35,4) and (39,0) .. (41,-2);
\draw[line width=.55pt] (34,10)--(44,14) (33,6)--(43,11) (33,5)--(48,8);
\draw[line width=.5pt] (36,5) .. controls (39,-2) and (49,3) .. (52,1) .. controls (55,-1) and (46,-4) .. (47,-6) .. controls (54,-10) and (59,7) .. (54,13);''','(-2,-9) rectangle (60,17)')+'}',owns=['complete tuple (S,I...)','first closer','revised R cluster','final hooked closer'],reading=r'(S,I)\deleted{R})',alternatives=[r'(S,I\deleted{)},R)'],qualification='Whole tuple state remains unresolved; de is outside this group. Final hook is preserved once with the long return.',units='pt',origin='(0,0)',baseline='0pt',wrapper='unsure; exact two states in invisible annotation')
G08=group('C024-G08',r'\unsure{'+pic(r'''% Complete word candidates: Le | Ce. Main body and detached upper run stay together.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\phantom{\unsure{Le|Ce}}};
\draw[line width=.55pt] (0,13)--(1,1)--(7,1) .. controls (9,-.2) and (11,.4) .. (13,2.8) .. controls (12,1) and (15,.4) .. (19,1.4);
\draw[line width=1pt] (2,12)--(2,14)--(5,17)--(7,16.6)--(9,17.5);''','(0,-2) rectangle (21,20)')+'}',owns=['whole Le/Ce word','detached upper zigzag'],reading='Le',alternatives=['Ce'],qualification='Whole word unresolved. Upper run has C-head/independent-trace attachment alternatives and undetermined hand, separately from main hand.',units='pt',origin='(0,0); parent node at (171,-36)',baseline='0pt',wrapper='unsure literal word')
M03=group('C024-M03',r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-16,-9) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\draw[gray,line width=.3pt] (0,0)--(.6,2.2);\draw[gray,line width=.2pt] (-.3,-.7)--(-.15,-.3);\end{tikzpicture}}};''',owns=['two separated runs of detached left oblique trace'],reading='oblique run and separated pale terminal',alternatives=[],qualification='Role, attachment, hand and surface origin undetermined.',units='pt inherited from C024-G07',origin='node (-16,-9)',baseline='base west',wrapper='unsure graphic')
G07=group('C024-G07',r'\figure{'+pic(r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {un graphe strict ayant $S$ comme};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,-18) {\unsure{ens de|ens des} sommets, $I$ comme ens.};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,-36) {d'\unsure{aretes|arêtes|arètes}.)};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (90,-36) {\rlap{Cette relation}\phantom{\deleted{Cette relation}}};
\draw[line width=.45pt] (88,-33)--(165,-29);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (171,-36) {'''+G08+r'''};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (195,-36) {graphe};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,-54) {est un \uline{arbre}};
\draw[line width=.5pt] (-8,12) .. controls (-6,15) and (-6,6) .. (-7,0) .. controls (-8,-14) and (-6,-34) .. (-6,-58);
\draw[line width=.3pt] (-8,12) .. controls (-9,7) and (-9,7) .. (-9,5);
'''+M03,'(-19,-61) rectangle (250,20)')+'}',owns=['all four lemma body lines from un graphe through arbre','cancelled Cette relation','left hooked rule','word and mark child groups G08/M03'],reading=r"un graphe strict ayant $S$ comme \unsure{ens de|ens des} sommets, $I$ comme ens. d'\unsure{aretes|arêtes|arètes}.) \deleted{Cette relation} \unsure{Le|Ce} graphe est un \uline{arbre}",alternatives=[],qualification='No final period after arbre. The node layout preserves the ruled block and all words once.',units='pt',origin='(0,0), fixed line nodes; child units remain pt',baseline='0pt',wrapper='figure')
M04=group('C024-M04',pic(r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {fait};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (-3,-9) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\draw[gray!45,line width=.25pt] (1,7) .. controls (4,4) and (3,1) .. (0,0)--(-2,0);\end{tikzpicture}}};''','(-6,-11) rectangle (19,10)'),owns=['fait','separate pale bent trace below-left'],reading='fait; pale bent trace',alternatives=[],qualification='fait firm. Trace has undetermined role, attachment, hand and surface origin.',units='pt',origin='word (0,0), trace node (-3,-9)',baseline='0pt',wrapper='inline TikZ; trace-only unsure')
G10=group('C024-G10',r'\unsure{'+pic(r'''% Complete phrase candidates: qu'on a | qu'on followed by an unassigned point.
% The final point's a/independent-mark question does not remove the whole-phrase qualification.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\phantom{\unsure{qu'on a|qu'on $\mathord{\cdot}$}}};
\draw[line width=.4pt] (1,2) .. controls (-2,9) and (1,10) .. (4,5) .. controls (4,2) and (0,1) .. (1,2);
\draw[line width=.35pt] (4,5) .. controls (5,-2) and (7,-12) .. (8,-15) .. controls (7,-16) and (6,-15) .. (6,-14);
\draw[line width=.45pt] (4,5)--(7,8)--(8,7)--(19,7)--(20,11)--(22,9);
\draw[line width=.35pt] (25,7)--(35,7);
\fill (44,7.5) .. controls (44,8.4) and (45.4,8.7) .. (46,8.2)--(45.5,7.4)--cycle;''','(-2,-17) rectangle (49,14)')+'}',owns=["complete qu'on a phrase",'solid final point'],reading="qu'on a",alternatives=["qu'on followed by an unassigned point"],qualification='Whole phrase remains doubtful; point has separate a/independent-mark attachment and undetermined hand/role. Following un is outside.',units='pt',origin='(0,0)',baseline='0pt',wrapper='unsure whole literal phrase')
G11=group('C024-G11',pic(r'''% Complete states: Il \deleted{existe} y a | Il \deleted{ex} y a.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\phantom{Il \deleted{\unsure{existe|ex}} y a}};
\draw[line width=.5pt] (1,4)--(3,1)--(5,0)--(7,1) (0,13)--(6,13)--(6,10);
\draw[line width=.4pt] (3,5)--(3,10);
\draw[line width=.45pt] (9,5) .. controls (12,7) and (16,14) .. (14,15) .. controls (10,15) and (11,0) .. (18,0);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (20,0) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt,line cap=round,line join=round]
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\phantom{\deleted{\unsure{existe|ex}}}};
\draw[line width=.45pt] (0,2)--(1,0)--(5,.6)--(6,2)--(7,0)--(12,0)--(13,2)--(14,0);
\draw[line width=.7pt] (0,.5)--(36,.5) .. controls (39,0) and (40,2) .. (40,7);
\draw[line width=.45pt] (18,.5)--(20,-2);
\end{tikzpicture}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (65,0) {y};
% Pale entrance to a is retained once and locally qualified; a remains a live reading.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (77,0) {\phantom{a}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (75,0) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\draw[gray!65,line width=.25pt] (0,-1)--(5,1.5);\end{tikzpicture}}};
\draw[line width=.5pt] (82,2) .. controls (77,1) and (78,-1) .. (84,0);''','(0,-7) rectangle (89,18)'),owns=['live Il','cancelled existe/ex','live y a','pale entry into a'],reading=r'Il \deleted{existe} y a',alternatives=[r'Il \deleted{ex} y a'],qualification='Only old word and pale entry are qualified. Capital I has its separate head; no deleted il y a is supplied.',units='pt',origin='(0,0), old-word child node (20,0)',baseline='0pt',wrapper='inline TikZ; local unsure old word and pale trace')
def sigma(name,body,reading,alt,qual,box='(0,-5) rectangle (24,19)',wrapper='inline literal glyph'):
 return group(name,pic(body,box),owns=[reading,'complete head/body/index/raised sign'],reading=reading,alternatives=alt,qualification=qual,units='pt',origin='(0,0)',baseline='0pt',wrapper=wrapper)
S01=sigma('C024-S01',r'''% Complete reading Sigma_i^+; detached-head role remains head/retrace or independent upper-run.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\Sigma_i^+}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt,line cap=round,line join=round]
\draw[line width=.5pt] (2,12)--(1.6,14)--(5,15)--(13,15);
\draw[gray!65,line width=.25pt] (0,11.3)--(2,11.2);
\draw[line width=.45pt] (3,11)--(10,10) .. controls (12,9) and (8,6) .. (1,1)--(15,1.3);
\draw[line width=.45pt] (18,4)--(18,-2);
\fill (18,6) circle (.45pt);
\draw[line width=.6pt] (19.5,16)--(23,16) (21.2,14)--(21.2,18);
\end{tikzpicture}}};''',r'\Sigma_i^+',[],r'Detached bent head and interrupted upper-body start; printed first recurring head-role qualifier. Clear dotted i and plus.',wrapper='inline glyph; first recurring head-role unsure')
S02=sigma('C024-S02',r'''% Complete locally qualified reading Sigma_i^-; head role remains recorded though first occurrence prints the recurring qualifier.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\Sigma_i^-}$};
\draw[line width=.5pt] (2,15)--(11,15.5);
\draw[line width=.3pt] (0,12.8)--(8,11.5);
\draw[line width=.45pt] (9,11) .. controls (11,9) and (4,4) .. (1,1)--(12,1) .. controls (14,1) and (14,-1) .. (14,-2);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (16,1) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\draw[line width=.5pt] (0,4)--(.3,1.2)--(0,0);\end{tikzpicture}}};
\draw[line width=.5pt] (19,15)--(23,15);''',r'\Sigma_i^-',[],r'Detached head role retained locally. Short dotless hooked index is read i with its own local uncertainty; raised minus firm.',wrapper='inline glyph; index-only unsure')
M06=group('C024-M06',r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (17,0) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\draw[gray!55,line width=.3pt] (0,1)--(.4,2);\fill[gray!70] (1.6,1.5) circle (.18pt);\end{tikzpicture}}};''',owns=['tiny pale tick','separate tiny point above-right of low sign'],reading='tick and point',alternatives=[],qualification='Role, attachment, hand and surface origin undetermined; separate from the sign reading.',units='pt inherited from C024-U01',origin='node at (17,0)',baseline='base west',wrapper='unsure two-component graphic')
U01=group('C024-U01',pic(r'''% Complete candidates U_{s_+} | U_{s_-}; plus remains primary at this physical sign.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$U_s\phantom{_{\unsure{+|-}}}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (15,-6) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\fill (0,0)--(0,2.5)--(1.3,3.6)--(2.5,3.5)--(2.7,4)--(3.4,3.5)--(5.7,3.5)--(6,2.4)--(4.7,1.9)--(5.7,1.7)--(5.7,.5)--(3,.3)--(0,0)--cycle;\end{tikzpicture}}};
'''+M06,'(0,-8) rectangle (24,15)'),owns=[r'U_{s_+}/U_{s_-}','solid lower sign','two small child traces M06'],reading=r'U_{s_+}',alternatives=[r'U_{s_-}'],qualification='Only sign interpretation is unresolved; complete glyph candidates retained. Tiny child marks have their own role/hand scope.',units='pt',origin='(0,0), sign node (15,-6)',baseline='0pt',wrapper='inline glyph; first recurring low-sign unsure')
S03=sigma('C024-S03',r'''% Complete candidates Sigma_i^- | Sigma_i^+; minus primary at this local solid raised mark.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\Sigma_i^{\unsure{-|+}}}$};
\draw[line width=.5pt] (0,15)--(14,15.3);
\draw[line width=.45pt] (5,15) .. controls (12,13) and (11,12) .. (7,10) .. controls (3,7) and (0,5) .. (0,4)--(14,4) .. controls (15,4) and (15,2) .. (15,1);
\draw[line width=.5pt] (17,10)--(16.8,6.5);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (21,14) {\unsure{\begin{tikzpicture}[x=1pt,y=1pt,baseline=0pt]\fill (0,0)--(-.3,1)--(.4,2.7)--(2,2.8)--(2.5,3.2)--(3.4,2.8)--(4.8,2.8)--(5.7,1.8)--(5.7,.1)--cycle;\end{tikzpicture}}};''',r'\Sigma_i^-',[r'\Sigma_i^+'],r'Joined head/body firm; short dotless index keeps its own local i uncertainty by recurring convention. Raised block retains minus/plus alternatives.','(0,-2) rectangle (29,20)','inline glyph; raised-sign unsure')
U02=group('C024-U02',pic(r'''% Complete local candidates \overline{U_{s_+}} | \overline{U_{s_-}}. Plus primary; later recurring sign printed without a second visible qualifier.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$U_s\phantom{_{\unsure{+|-}}}$};
\draw[line width=.5pt] (0,14)--(15,14.3)--(16,13.6);
\fill (14,-6)--(14.7,-3.6)--(17,-2.5)--(21,-2.2)--(21.7,-2.7)--(19.4,-3.1)--(19,-4)--(21.7,-4)--(21.8,-5.6)--(18.5,-5.7)--(18.3,-6.8)--(17.5,-6.1)--cycle;''','(0,-8) rectangle (25,18)'),owns=[r'complete barred U_{s_+}/U_{s_-}','literal outer bar','irregular low sign'],reading=r'\overline{U_{s_+}}',alternatives=[r'\overline{U_{s_-}}'],qualification='Bar firm; plus/minus locally unresolved. This later sign retains its local doubt in comments/record; first occurrence U01 carries printed recurring qualifier.',units='pt',origin='(0,0)',baseline='0pt',wrapper='inline glyph; invisible local candidate annotation')
E01=group('C024-E01',pic(r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{E_i}$};
\draw[line width=.45pt] (0,13.8) .. controls (4,15) and (6,15.5) .. (9,15.5);
\draw[line width=.45pt] (0,12) .. controls (3,10) and (4,7) .. (3,6) .. controls (2,3) and (1,1) .. (1,0)--(11,1);
\draw[line width=.45pt] (3,6)--(12,6) .. controls (17,6) and (20,2) .. (21,-1);
\fill (22,8) circle (.5pt);''','(0,-4) rectangle (25,18)'),owns=['E_i with separate upper arm and extended middle/index return'],reading=r'E_i',alternatives=[],qualification='Literal local form confirms E_i. No new mathematical reading is assigned to the detached upper arm.',units='pt',origin='(0,0)',baseline='0pt',wrapper='inline literal glyph')
S04=sigma('C024-S04',r'''% Complete Sigma_i^-; joined head/body. Short dotless index retains its local recorded qualification.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\Sigma_i^-}$};
\draw[line width=.45pt] (0,15)--(14,14.6);
\draw[line width=.45pt] (5,14.8) .. controls (12,12) and (11,10) .. (7,8) .. controls (4,5) and (1,3) .. (1,2)--(15,1) .. controls (16,.5) and (16,-.5) .. (15,-1);
\draw[line width=.5pt] (17,6.5)--(16.3,4.2);
\draw[line width=.45pt] (20,14)--(25,14);''',r'\Sigma_i^-',[],r'Head and body are joined. Raised minus is firm. Short dotless i retains its local recorded uncertainty; first instance S02 prints it.','(0,-4) rectangle (28,18)')
S05=sigma('C024-S05',r'''\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,0) {$\phantom{\Sigma_i^-}$};
\draw[line width=.5pt] (0,15)--(15,16);
\draw[line width=.45pt] (4,15.4) .. controls (12,13) and (14,11) .. (7,7) .. controls (3,4) and (1,2) .. (1,2)--(17,2);
\draw[line width=.5pt] (20,2)--(20,-2);
\fill (20.4,6) circle (.4pt);
\draw[line width=.45pt] (21,15.5)--(27,15.5);''',r'\Sigma_i^-',[],r'Joined head/body, dotted i and separate raised minus are firm.','(0,-5) rectangle (29,19)')
parts=[r'\scanpage{24}',r'\unsure{Considerons|Considérons} la partition $\Pi_I^{\unsure{\circ|0}}$ de $X\setminus\bigcup_{\alpha\prime\in I}E_{\alpha\prime}$,',M01,r"$S$ l'ens des classes, notées $U_s$ $(s\in S)$.",G02,r'Considérons la',G03,r'\[',G04,r',i)\in R\quad',G05,r'\quad \overline{U_s}\cap E_i\ne\varnothing.',r'\]',r'\uline{Lemme} Cette relation fait de $',G06,r'$',G07,r'\unsure{le|Le}',M04,G10,r'un graphe strict signifie que a) $\forall i\in I$,',G11,r"exactement deux $U_s$ tels que $\overline{U_s}\cap E_i\ne\varnothing$, et b) $i$ est caractérisé par \unsure{l'ens|l'une} de ces deux $U_s$.",r'\unsure{Soient|Soit} $',S01,r',',S02,r'$ les deux comp. \unsure{connexes|conn} de $X\setminus E_i$, alors a) se précise en : il y a \unsure{exactemt|exactement} \uline{un} $',U01,r'$ contenu dans $',S03,r'$ tel que $',U02,r'\cap',E01,r'\ne\varnothing$ (et de $=$ pour $',S04,r"$, \unsure{de|dé|qui} definit un $U_{s_-}\subset",S05,r'$ tel que $\overline{U_{s_-}}\cap E_i\ne\varnothing$),',r'% archive sheet number: 23']
tex='\n'.join(parts)+'\n'
# Keep comments on their own lines and remove unintended blank physical lines.
tex=tex.replace(r'\alpha\prime',r"\alpha'")
tex=re.sub(r'\n{2,}','\n',tex)
for anchor in [r'\uline{Lemme} Cette relation',r'\unsure{le|Le}',r'\unsure{Soient|Soit}']:
 tex=tex.replace(anchor,'\n'+anchor,1)
D.joinpath('reading.tex').write_text(tex)
for gid,g in meta.items():
 g['complete_states']=[{'reading':g['reading'],'qualification':g['qualification']}]+[{'reading':a,'qualification':g['qualification']} for a in g.get('alternatives',[])]
for gid,tex in [('C024-S01',r'\Sigma_i^+'),('C024-S02',r'\Sigma_i^-')]:
 meta[gid]['complete_states']=[{'reading':tex,'upper_run_role':role,'index':('dotted i, firm' if gid.endswith('S01') else 'short dotless i, qualified'),'raised_sign':('plus, firm' if gid.endswith('S01') else 'minus, firm'),'upper_run_hand':'undetermined hand'} for role in ['head/retrace','independent upper run']]
meta['C024-S03']['complete_states']=[{'reading':t,'head':'joined, firm','index':'short dotless i, qualified','raised_sign':sgn} for t,sgn in [(r'\Sigma_i^-','minus candidate'),(r'\Sigma_i^+','plus candidate')]]
meta['C024-G10']['complete_states']=[{'reading':"qu'on a",'whole_phrase':'qualified','final_mark_role':'a candidate','final_mark_hand':'undetermined hand'},{'reading':"qu'on followed by an unassigned point",'whole_phrase':'qualified','final_mark_role':'independent point','final_mark_hand':'undetermined hand'}]
D.joinpath('group_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print('reading.tex written; group identities:',len(meta))
