from workflow import *
n=345
cp=lambda lab,box:f'scan 345 {lab} {box}'
choices=[
('avec sa','The joined avec is followed by separate sa; no muni.', 'page','high'),
(r'\Delta_*^{m*}','A separate raised star follows m; the lower star is also visible.',cp('mstar',(410,267,642,355)),'high'),
('gr. des sections','Abbreviated gr., then des and the crossed t of sections.',cp('torseur',(580,355,1340,494)),'high'),
("s'insérant dans","Initial s-apostrophe, insérant, then dans.",cp('sequence_intro',(1685,265,2070,333)),'high'),
('y','Open fork and long descending stroke, not a closed g.','page','high'),
('n','One hump in the lower index; upper m has two.',cp('P_diagram',(1444,440,2110,765)),'high'),
(r'\operatorname{Hom}(P^m','Final raised letter has two humps; expression stops there.',cp('P_diagram',(1444,440,2110,765)),'high'),
(r'\Delta_*^m\in\operatorname{Ob}(\Delta)/X_*','Delta with raised m and lower star, Ob Delta, slash X star.',cp('limit_trial',(600,531,1078,662)),'high'),
("isom ou équiv. d'homotopie ?","A low m follows iso; abbreviated équiv. and the question mark remain.",cp('iso_question',(563,647,1177,701)),'medium'),
(r'\unsure{\overline\Phi_m|\overline T_m}','An upper horizontal stroke and rounded loop cross a vertical stem; Phi is favored, but a looped T remains possible.',cp('barred',(1369,1066,1657,1139)),'low'),
*[(r'y','Open two-branched head and descending tail, consistent in the small array.',cp('array',(1357,1160,1701,1365)),'high')]*5,
(r'\operatorname{Coker}','The ending has joined e/r strokes after k.',cp('coker',(417,1142,581,1220)),'medium'),
(r'-\cdots','A bare continuation stroke and separated dots; no arrowhead.','page','high'),
(r'-\cdots','A bare continuation stroke followed by dots.',cp('final_tail',(1962,1650,2211,1781)),'high'),
('induite par','The word has initial in-, crossed d/t strokes, then par.','page','high')]
t,ds=resolve(n,choices)
t=repl(t,r'\unsure{F(X_*)=}',r'F(X_*)=')
t=repl(t,r'T_1\otimes T_1',r'T_1\unsure{\circ|\otimes}T_1')
t=repl(t,r'\Lambda^2\Phi_n-\cdots])\}',r'\Lambda^2\Phi_n-\cdots\unsure{])\}}')
cc=[]
def add(place,c,h,f,ink,kind='other',dc=False,dh=True,**kw):cc.append(change(place,c,h,f,ink,kind,dc,dh,**kw))
add('opening prose','avec sa structure mult. et à puiss. div.',"muni d’une structure multiplicative et d’une dérivation [ill]",'avec sa structure mult. et à puiss. div.','Short gr-like run is avec sa; mult., puiss. and div. end with stops.','misread word',marked='yes')
add('first Hom source','C^bullet(X_bullet)','C^bullet(X_*)','C^bullet(X_bullet)','Small round dot under X, distinct from the star on the outer X.','misread symbol or index',consequential=True)
add('first Hom target','C(Delta_*^n)','C^bullet(Delta_*^n)','C(Delta_*^n)','No raised dot after this C.','text not on the page',consequential=True)
add('first definition ending','no closing square bracket','closing square bracket','no closing square bracket','The line stops after two round closing parentheses.','text not on the page')
add('F evaluated on simplex','Delta_*^{m*} or Delta_*^m','Delta_*^m','Delta_*^{m*}','A second star is raised after m; not normalized away.','misread symbol or index',crop=cp('mstar',(410,267,642,355)),consequential=True)
add('P definition','p_*^{m,-1}(T)','omitted','p_*^{m,-1}(T)','Entire inverse-image expression follows P_*^m.','omission',consequential=True)
add('torseur power','Phi_*^{m+1}','Phi_*^m','Phi_*^{m+1}','Tiny plus and final upright 1 follow m.','misread symbol or index',crop=cp('torseur',(580,355,1340,494)),consequential=True)
add('torseur parenthesis','gr. des sections; k^{m+1} simeq checkPsi_m','groupe des sections; k^{m+1}','gr. des sections; k^{m+1} simeq checkPsi_m','Abbreviated gr.; right-hand isomorphism and checked Psi are visible.','omission',crop=cp('torseur',(580,355,1340,494)),marked='yes')
add('p map','p_*^m: checkPhi_m tensor Phi_* -> Phi_*','omitted','p_*^m: checkPhi_m tensor Phi_* -> Phi_*','Separate line with p and arrow, above the sequence.','omission',consequential=True)
add('sequence introduction',"s’insérant dans or bilinéaire en",'omitted',"(s’insérant dans",'The parenthesis and phrase precede the sequence.','omission',crop=cp('sequence_intro',(1685,265,2070,333)))
add('five-term sequence','headless dashes','four right arrows','headless dashes','All four joins are strokes without heads.','drawing or diagram')
add('point of P','P_m^m or P_n^m','P_n^m','P_n^m','Lower n has one hump; raised m has two.','misread symbol or index',dc=True,dh=False,crop=cp('P_diagram',(1444,440,2110,765)),consequential=True)
add('upper right cancelled row','Delta_n^m=Hom_ens(...) -> P_n^m cancelled','live row','cancelled row','Long strike runs through the upper row to the P endpoint; descending curved connectors remain live.','deletion state',confidence='medium',crop=cp('P_diagram',(1444,440,2110,765)))
add('unfinished lower Hom','Hom(P^m doubtful','Hom(P^n [ill]','Hom(P^m','Raised final m has two humps. No closing continuation is written.','misread symbol or index',crop=cp('P_diagram',(1444,440,2110,765)),marked='yes')
add('curve left of Hom construction','curved line','omitted','curved line','Bent line continues from the torseur parenthesis into the diagram area.','drawing or diagram')
add('first limit trial','cancelled unsure C_bullet','live Box operator','cancelled unsure C_bullet','Small crossed trial before C remains partly obscured; no live square operator.','deletion state',crop=cp('limit_trial',(600,531,1078,662)),confidence='low',marked='yes')
add('two limit Hom targets','Delta_*^*','Delta_*^n','Delta_*^*','Raised asterisk in each of the two target arguments.','misread symbol or index',consequential=True)
add('question on upward arrow','iso ou équiv. d’homotopie ?','est-ce une équiv. d’homotopie ?','isom ou équiv. d’homotopie ?','Low terminal m after iso; no est-ce une.','misread word',dc=True,confidence='medium',crop=cp('iso_question',(563,647,1177,701)))
add('second limit trial','deleted Hom','live Box operator','deleted Hom','The crossed trial has the tall initial of Hom and its joined tail.','deletion state',crop=cp('deleted_Hom',(685,708,914,779)),marked='yes')
add('small Phi diagram lower row','T_m and T_n without connector','T_m mapsto T_n','T_m and T_n without connector','There is no ink connector between the two lower labels.','text not on the page')
add('beta condition','overlinePhi_m or overlineT_m','T_m','unsure overlinePhi_m or overlineT_m','Bar is present; loop under it leaves the letter unresolved.','misread symbol or index',confidence='low',crop=cp('barred',(1369,1066,1657,1139)))
add('small array top product','T_1 tensor T_1','T_1 circ T_1','T_1 unsure circ or tensor T_1','Rounded operator is heavily retraced at left; an internal cross is not secure.','misread symbol or index',dc=True,confidence='low',crop=cp('array',(1357,1160,1701,1365)))
add('array top-right dot','dot','omitted','dot','Isolated small dot at the right of the first row.','omission',crop=cp('array',(1357,1160,1701,1365)))
add('coequalizer arrow labels','delta_0, delta_1','partial_0, partial_1','delta_0, delta_1','Looped delta letters, not partial derivatives.','misread symbol or index',consequential=True)
add('kernel arrow labels','C^bullet(delta_0), C^bullet(delta_1)','C(partial_0), C(partial_1)','C^bullet(delta_0), C^bullet(delta_1)','Raised bullets and looped deltas are visible.','misread symbol or index',consequential=True)
add('kernel expression ending','no closing parenthesis','closing parenthesis','no closing parenthesis','After the last simplex only its own argument is closed.','text not on the page')
add('complex and left column','full downward complexes and Phi_m column','mostly omitted','full downward complexes and Phi_m column','Zero terms, downward arrows, wedge labels and dotted continuations are present.','omission',consequential=True)
add('degree-zero inclusion','diag','alpha mapsto 0','diag','Label above the horizontal arrow spells diag; 0 labels the downward map.','insertion or placement',consequential=True)
add('projections','delta_0^*=pr_0, delta_1^*=pr_1','partial_0=pr_0, partial_1=pr_1','delta_0^*=pr_0, delta_1^*=pr_1','Raised stars follow the lower delta indices.','misread symbol or index',consequential=True)
add('upper left map value','1=T_0','1=T_1','1=T_0','Small final index is a closed zero.','misread symbol or index',consequential=True)
add('isolated k and bottom margin','k; alpha in k, beta in T','omitted','k; alpha in k, beta in T','Standalone k beside the complex and separate bottom alpha/beta note.','omission')
add('bottom source complex','0-k ->^0 k -> 0-...','arrows at both end joins','0-k ->^0 k -> 0-...','First and last joins have no heads.','drawing or diagram')
add('bottom Hom target','Delta_*^*','Delta_*^n','Delta_*^*','Raised asterisk, not n.','misread symbol or index',consequential=True)
add('last source complex','[-]','[...]','[-]','A single short dash is inside the brackets.','misread symbol or index')
add('last target continuation','-...','->...','-...','The continuation stroke has no head.','drawing or diagram',crop=cp('final_tail',(1962,1650,2211,1781)))
# The borderline closing cluster adds uncertainty only; recorded in doubts, not a substantive change row.
items=[inv('deletion','top left','F(X_*)='),inv('text','top','C^bullet(X_*) avec sa structure'),inv('display','upper','F_*(X_*)=[n mapsto Hom'),inv('display','upper','F_*(Delta)=P=p inverse'),inv('insertion','below P definition','torseur sous; parenthesis'),inv('display','upper left','p_*^m'),inv('margin note','upper right','s’insérant dans'),inv('display','upper right','0-checkPsi tensor Phi'),inv('insertion','beneath sequence','Hom(Phi_m,Phi_*); T_m mapsto T_*'),inv('display','upper right','Delta_*^m -> P_*^m; y in P_n^m'),inv('diagram','upper right','cancelled Delta_n^m and Hom diagram'),inv('deletion','in upper right diagram','Delta_n^m=Hom_ens; P_n^m'),inv('drawing','upper middle','curved connecting line'),inv('diagram','middle','F_*(X_*) and two limits'),inv('deletion','in limit rows','C_bullet trial; Hom trial'),inv('diagram','middle right','Phi_m -> Phi_n; T_m,T_n'),inv('display','middle right','alpha in k, beta in barred symbol'),inv('display','middle right','T_0,T_1 product T_1; y array'),inv('diagram','lower middle','X_*=Coker'),inv('diagram','lower','kernel and four columns of complexes'),inv('margin note','left of complex','beta in Phi_m; k'),inv('display','bottom written area','F_*(X_*)=Hom of complexes'),inv('insertion','below final Hom','structure mult. induite par'),inv('margin note','bottom left','alpha in k, beta in T'),inv('text','foot','346')]
notes="The page defines F_* from the multiplicative divided-power complex, describes a torsor P, and asks whether a comparison from a colimit is ‘isom ou équiv. d’homotopie ?’. That question is not asserted or proved here. The lower example identifies the two vertices of a 1-simplex and writes its two-term complex. A direct check with T_1=e_0+e_1 gives T_1 wedge a(e_0+e_1)=0, supporting the visible diagonal inclusion and zero differential, not H’s horizontal alpha-to-zero label. The extra raised star in Delta_*^{m*}, missing closing bracket in the first definition, absent bullet in its target C, missing /X_* in the bottom colimit, and unfinished Hom(P^m are preserved. The source has printed music staves turned vertically beneath upright handwriting; these are blank ruling, not formula strokes. Manuscript number 346. The bar/letter after beta and the retraced top array operator remain doubtful. The final closing cluster lies at the scan edge and remains marked rather than silently completed."
# Syntax only: delimit control words before following letters.
t = t.replace('\\circy', '\\circ y')
commit(n,t,ds,cc,items,notes,hand=['The open fork and descending tail is y in the point label and all five array occurrences; neither a closed g nor a new gamma is imposed.','Vertical printed staff rules are distinguishable by regular spacing and are not counted as handwritten stems.','The small m has two humps; the point index n has one.'],notation=[('Delta_*^{m*}','Extra raised star follows m, distinct from lower star; retained at this occurrence.'),('barred Phi_m / T_m','Upper bar secure, underlying retraced letter unresolved.'),('delta_i^*','Looped delta and raised star in the lower projections.')],abbr=[('mult.','multiplicative'),('puiss. div.','puissances divisées'),('gr.','groupe'),('équiv.','équivalence'),('isom','isomorphisme'),('diag','diagonale')],checks=[check('345.diagonal-zero','Conditional on T_1=e_0+e_1, the two projections agree on a(e_0+e_1), and T_1 wedge aT_1=0 by alternation. This checks only the displayed diagonal and zero differential.','targeted proof check')],unresolved=[r'Cancelled trial C_\bullet before the first limit term (low).',r'Top array operator \unsure{\circ|\otimes} (low).',r'Final closing cluster \unsure{])\}} at the right scan edge (low).'])
