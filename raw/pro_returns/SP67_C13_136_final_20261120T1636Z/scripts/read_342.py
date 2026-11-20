from workflow import *
n=342
boxes={'G':(241,348,413,427),'u':(423,476,611,707),'small':(551,720,805,930),'beta':(79,931,444,1114),'hom':(422,1007,765,1112),'margin':(79,1182,244,1262),'exp':(1340,1652,1480,1746),'K':(605,1850,690,1918),'functor':(508,1996,775,2083),'strokes':(37,1956,91,2113)}
b=lambda k:f'{n} {boxes[k]}'
text,ds=resolve(n,[
('G','The small loop and inward right bar agree with the G explicitly defined alongside.'),
('K','The upright and two diagonal arms remain visible through retracing.',b('u'),'medium'),
(r'$\otimes$','A circle is crossed by two strokes; it is not the cursive word et.',b('u')),
('i','A small upright stroke with a separate dot labels the oblique line.',b('small')),
(r'\unsure{d_0|\mathrm{diag}}','The label has a looped d and a low rounded ending; the tiny intervening strokes do not securely decide d_0 versus diag.',b('small'),'low'),
(r'\beta T_n\wedge\beta','The first letter has two loops and a descending stem, unlike the alpha in the row below.',b('beta'),'medium'),
(r'\Psi_{[n]}','The overworked symbol has forked upper arms and a descending central stem; the same Psi occurs in the direct-sum formula.',b('margin'),'medium'),
(r'\bullet','A single high dot follows Hom, matching the two degree-bullet arguments.'),
('*','The star is raised to the upper right of Hom, not placed below it.'),
('K','The overwritten letter has the K stem and lower diagonal arm.'),
('K','The same overwritten K form occurs before N_*.'),
('can.','The low connected letters read can followed by a short final dot.'),
('K','The upright and lower diagonal agree with the two preceding K forms.'),
(r'\Delta_*^n','There is a raised n above Delta and an overworked star below it.',b('exp'),'medium'),
(r'\unsure{K|P}','Superposed upright and rounded strokes before an unfinished parenthesis leave K/P unresolved.',b('K'),'low'),
(r'\unsure{G_M|K_M}','The outer rounded stroke supports G, but angular overwork admits K; it is not a secure F.',b('functor'),'low'),
(r'\otimes','The final overwritten sign retains a circular outline and crossing diagonals.'),
])
text=repl(text,r'\deleted{G(M_*)}',r'\deleted{\unsure{C|G}(M_*)}')
text=repl(text,r'\unsure{\alpha_M^K}',r'\alpha_M^K')
text=repl(text,r'\unsure{\beta_M^K}',r'\beta_M^K')
text=repl(text,r'&k\arrow[r]&\Lambda^2',r'&k\arrow[r,Rightarrow]&\Lambda^2')
text=repl(text,r'\deleted{M_{[n]}\otimes N}',r'\deleted{=M_{[n]}\otimes N}')
text=repl(text,r'\mspage{343}',r'\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0,.35) (0,.7)--(0,1.6);\draw (.34,.1)--(.34,.35) (.34,.7)--(.34,1.65);\end{tikzpicture}}}'+'\n'+r'\mspage{343}')
cs=[]
def c(place,C,H,F,ink,kind='misread symbol or index',dc=False,dh=True,conf='high',box='page',cons=False,marked='no'):
 cs.append(change(place,C,H,F,ink,kind,dc,dh,conf,box,marked,cons))
c('second line, kernel map','hooked arrow','ordinary arrow','hooked arrow','The left end has a short inward hook.','drawing or diagram')
c('cancelled line under functors',r'G(M_*)',r'C(M_*)',r'\unsure{C|G}(M_*)','A clear open C-like curve survives; the cancellation crosses the place of any G bar.','misread symbol or index',True,True,'low',b('G'))
c('left simplex diagram','two headless bowed lines','two arrows','two headless bowed lines','Both curved connectors lack heads.','drawing or diagram')
c('left simplex diagram, last object','Delta^1_* down to S','S labels arrow to ellipsis','Delta^1_* down to S','S is below the downward arrow as its endpoint; there is no ellipsis.','drawing or diagram')
c('u_M annotation',r'\unsure{$\otimes$|et} fonctoriel ?','fonctoriel ?',r'$\otimes$ fonctoriel ?','The tensor symbol precedes fonctoriel; the question mark is written below the slanted text.','omission',False,True,'high',b('u'),True,'yes')
c('below K(M_*)',r'\parallel F_S(K)',r'F_S(K), possibly F_S double-prime',r'\parallel F_S(K)','Two vertical equality strokes lie above F_S; they are separate from F and not primes.','drawing or diagram',False,True,'high',b('u'),False,'yes')
c('small diagram, top horizontal map','single arrow','two parallel arrows','double-stem right arrow','Two stems terminate in one shared right-facing head.','drawing or diagram',True,True,'high',b('small'),True)
c('small diagram, upward map at left','0','i_0 / alpha maps to 0','0','The circular zero is beside the vertical arrow; the dotted i belongs to the separate oblique connector.','insertion or placement',False,True,'high',b('small'))
c('small diagram, lower map label',r'\unsure{diag|d_0}','no clear label',r'\unsure{d_0|\mathrm{diag}}','A looped d and low rounded terminal are present under k to k^2; the internal strokes remain ambiguous.','omission',False,True,'low',b('small'))
c('small diagram, exterior differential',r'\Lambda T_n',r'\wedge T_2',r'\Lambda T_n','The subscript has the rounded arch of n, not the diagonal and foot of 2.','misread symbol or index',False,True,'high',b('small'),True)
c('above Lambda^2 k^2','up arrow to dot','omitted','up arrow to dot','A short vertical arrow ends at a separate filled dot above the row.','omission')
c('between F_Delta1 and Lambda^2 Phi','vertical two-headed arrow','not represented','vertical two-headed arrow','There is a head at each end of the upright connector.','drawing or diagram')
c('left exterior formula',r'\unsure{\beta T_n\wedge\beta}',r'\alpha T_n\wedge\beta',r'\beta T_n\wedge\beta','The initial sign has a long descending stem and two loops, contrasting with the alpha below.','misread symbol or index',False,True,'medium',b('beta'),True)
c('lower left scalar row',r'k^{\Delta_n}',r'k^{\Delta^n}',r'k^{\Delta_n}','The n is low to the right of Delta, not raised above it.','misread symbol or index',False,True,'high',b('beta'))
c('cancelled Hom, first argument',r'\unsure{\alpha_M^K}',r'\alpha_M^*',r'\alpha_M^K','The superscript has an upright with two angular arms, a K.','misread symbol or index',False,True,'medium',b('hom'))
c('cancelled Hom, second argument',r'\unsure{\beta_M^K}',r'\beta_M^*',r'\beta_M^K','The raised letter has the same stem-and-arm form, not a detached star.','misread symbol or index',False,True,'medium',b('hom'))
c('right Hom identities, third row',r'\operatorname{Hom}^{\unsure{*}}',r'\operatorname{Hom}_*',r'\operatorname{Hom}^{*}','The star stands above the word Hom.','misread symbol or index',False,True,cons=True)
c('large tensor diagram, central vertical map','can. label','omitted','can. label','The short word is placed by the downward arrow from K(M) tensor K(N).','omission')
c('large tensor diagram, lower right connection','paired headless lines','two right arrows','paired headless lines','Both lower horizontal strokes end without heads.','drawing or diagram')
c('large tensor diagram, leftward lower map','double-stem left arrow','single left arrow','double-stem left arrow','Two close strokes converge into the left-pointing head.','drawing or diagram')
c('cancelled equality after lower left vertex',r'\deleted{M_{[n]}\otimes N}',r'\deleted{=M_{[n]}\otimes N}',r'\deleted{=M_{[n]}\otimes N}','Two short equality strokes precede the crossed M.','omission',True,False)
c('example introduction','prenons','Prenons, with final full stop','prenons','The initial p is lower-case and no full stop follows the displayed formula.','abbreviation expanded or spelling modernised')
c('example terminal exponent',r'\unsure{\Delta_n}',r'\Delta_*^n',r'\Delta_*^n','A raised n and an overwritten lower star are both visible.','misread symbol or index',True,False,'medium',b('exp'),True,'yes')
c('example downward continuation',r'\unsure{K|P}(','omitted',r'\unsure{K|P}(','A down arrow points to the heavily overwritten letter and abandoned opening parenthesis.','omission',False,True,'low',b('K'))
c('lower Hom_* formula','no closing parenthesis','closing parenthesis','no closing parenthesis','The line ends after K_* without a right parenthesis.','text not on the page')
c('bottom functor name',r'\unsure{G_M|F_M}',r'K_M',r'\unsure{G_M|K_M}','The rounded outer curve survives angular overwriting; neither a plain K nor F is certain.','misread symbol or index',False,True,'low',b('functor'),True)
c('last Hom product connection','dash','right arrow','dash','The short horizontal connector has no arrowhead.','drawing or diagram')
c('lower left margin','omitted','omitted','two vertical margin strokes','Two uneven pen lines flank the punch holes; their surviving segments are reproduced.','drawing or diagram',True,True,'high',b('strokes'))
c('foot','343','omitted','343','The pencil number 343 is present at bottom left.','omission')
inventory=[inv('diagram','top left','K to F to F prime, F to G'),inv('display','top middle','G (=F_Delta_*^n)'),inv('diagram','second row','K(M_*) hooked into F(M_*)'),inv('deletion','under second row','C/G(M_*)'),inv('diagram','upper left','Delta^0_* to Delta^1_* to S'),inv('diagram','upper middle','K(M_*) to M_[1] and M_[n]'),inv('margin note','under K(M_*)','vertical equals F_S(K)'),inv('diagram','middle left','F_S to F_Delta1 to F_Delta0 and exterior-power comparison'),inv('deletion','under comparison','Hom(alpha_M^K,beta_M^K)'),inv('margin note','left','alpha in k; beta in Psi_[n]'),inv('display','right','K(M_*)=Z^0 and Hom identities'),inv('display','right below','K_*^*=Psi_* plus Lambda^2 Psi_*='),inv('diagram','middle lower','tensor compatibility diagram'),inv('deletion','lower left tensor vertex','equals M_[n] tensor N'),inv('text','right of tensor diagram','prenons Phi_*=C_*^0'),inv('diagram','below','K(Phi_*) to F_Delta^n_*(Phi_*) and unfinished downward K/P('),inv('deletion','lower left','Hom('),inv('display','lower centre','Hom_*(M_*,K_*'),inv('deletion','lower left next','K(M_*)'),inv('deletion','lower left next','Hom('),inv('display','bottom','G_M/K_M(K)=Hom(M,K)'),inv('display','bottom','Hom(M,K) tensor Hom(M,L) dash Hom(M,K tensor L)'),inv('display','last row','M to M tensor M'),inv('drawing','lower left margin','two near-vertical strokes'),inv('text','foot','343')]
note='''Upright notes on printed music-staff paper; foot number 343. A kernel/equalizer-type functor K is compared with evaluation in simplicial degree n, followed by chain/cochain Hom descriptions and a tensor-compatibility diagram. The manuscript asks “⊗ fonctoriel ?”. The first factor in the exterior expression reads beta, not H’s alpha, even though alpha occurs in the row beneath; the clear beta is retained. The lower simplex index in that row is Delta_n, while the bottom example has Delta_*^n. Hom in the third right-hand identity has a superscript star. The label under k to k^2 remains d_0/diag; no mathematical expectation was used to force it. The letters preceding the unfinished bottom parenthesis and naming the bottom functor remain doubtful because of overwriting. The last Hom expression is connected by a bare dash. Conditional check: given a linear diagonal D:M→M⊗M, (f,g)↦(f⊗g)D is bilinear in f and g, hence factors through Hom(M,K)⊗Hom(M,L). This explains the final question but neither proves the existence of D nor the earlier identifications. The cancelled Hom has K superscripts, distinct from the live star labels above. The printed ruling is background, not handwritten equality strokes.'''
# Syntax only: delimit control words before following letters.
text = text.replace('\\otimesK', '\\otimes K').replace('\\otimesM', '\\otimes M')
commit(n,text,ds,cs,inventory,note,hand=['The same heavily retraced K appears in the kernel and tensor diagram. It can look like P or a looped R; the incomplete bottom trial remains uncertain rather than being forced by the other occurrences.','Beta has a long descender and two loops in beta T_n wedge beta; alpha below has no such descender. H reads the former as alpha.','The lower small-diagram label and several bottom letters are overwritten; the marks retained there are local uncertainties, not alternative notational systems.'],notation=[(r'\operatorname{Hom}^{*}','Raised star in the right-hand comparison, contrasted with subscript star on the last Hom.'),(r'\Delta_n / \Delta_*^n','Both are written here in distinct places; not normalized to one form.'),(r'\beta T_n\wedge\beta','Clear initial beta retained despite nearby alpha.')],abbr=[('can.','canonique')],checks=[check('342-diagonal-induced-product','For a specified linear D:M→M⊗M, tensoring linear maps and composing with D is bilinear; the universal property of the tensor product yields the displayed type of map. No existence of D is asserted.','targeted proof check'),check('342-kernel-comparisons','The K, Z^0 and Hom comparisons are recorded as source assertions; no general proof was performed.')],unresolved=[r'cancelled C/G(M_*)',r'd_0/diag label below k to k^2',r'overwritten K/P before unfinished parenthesis',r'overwritten G_M/K_M at bottom'])
