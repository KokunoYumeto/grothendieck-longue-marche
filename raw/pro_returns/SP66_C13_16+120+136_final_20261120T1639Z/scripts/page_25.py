from record import *
k='136_scan329';t=(SOURCE/'pages'/f'{k}.tex').read_text()
for a,b in [
 (r'\gamma^{\unsure{B|A}}_{pq}',r'\gamma^B_{pq}'),
 (r'\Gamma^{\unsure{e|\bullet}}M',r'\Gamma^e M'),
 (r'\Gamma^p(\Gamma^e M)\arrow[r]',r'\Gamma^p(\Gamma^e M)\arrow[r,no head]'),
 (r'\unsure{coalg}',r'coalg'),(r'\unsure{co. unit. comm.}',r'co. unit. comm.'),
 (r'\unsure{\mathrm{Ab}}',r'\mathrm{Ab}'),(r'\unsure{équivalentes}',r'équivalentes'),
 (r'\unsure{avec|aux}',r'avec'),
 (r'A\longrightarrow\Gamma^p(A)',r'A\mathrel{\relbar\joinrel\relbar}\Gamma^p(A)'),
 (r'u_{\unsure{p+q|pq}}',r'u_{pq}'),(r'3\unsure{ie|i.e}',r'3 ie'),
 (r'\deleted{\unsure{gradué}}',r'\deleted{gradué}'),(r'\unsure{divisées}',r'divisées'),
 (r'\unsure{\text{algèbre}}',r'\text{algèbre}'),(r'\unsure{\text{grâce à}}',r'\text{grâce à}'),
 (r'\unsure{\text{structure}}',r'\text{structure}'),(r'\unsure{\text{grde}}',r'\text{grde}')
]:
 if a not in t:raise ValueError(a)
 t=t.replace(a,b)
B=lambda s:k+' '+s
A=B('(385,55,595,222)');O=B('(241,926,1419,1058)');T=B('(201,1088,1334,1303)');E=B('(222,1272,864,1356)');S=B('(657,1498,1286,1639)');P=B('(574,1800,1002,1919)');H=B('(239,1933,1405,2051)');U=B('(808,2034,1401,2194)')
rows=[
 R('upper square: superscript of gamma',r'\unsure{B|A}','A','B','An upright stem and two separate right lobes form B; the neighbouring overwritten argument remains uncertain.','misread symbol or index',crop=A,con='The written gamma superscript is B; A would make the square type-consistent.'),
 R('upper-right Hom diagram: connector','vertical headless shaft','rightward arrow','vertical headless shaft','A short vertical stroke separates the two Hom expressions; no arrowhead is visible.','drawing or diagram'),
 R('middle diagram: inner Gamma exponent',r'\unsure{e|\bullet}','*','e','The superscript is a small open loop with a left entry stroke, unlike the solid multi-stroke asterisk above.','misread symbol or index',conf='medium'),
 R('middle diagram: rightmost Gamma exponent',r'\unsure{e|\bullet}','*','e','The same small looped e is repeated at the rightmost object.','misread symbol or index',conf='medium'),
 R('middle diagram: last connector','right arrow','right arrow','headless horizontal shaft','The short connector ends bluntly before Gamma; no return stroke forms an arrowhead.','drawing or diagram','yes','yes'),
 R('rule below the diagrams','drawn rule','absent','drawn rule','A separate slightly rising black rule runs below the last square.','drawing or diagram'),
 R('opening words',r'\unsure{Soit} A une k-coalg co. unit. comm., de sorte que','Les A munis de ill cocommutative ill par',r'\unsure{Soit} A une k-coalg co. unit. comm., de sorte que','After the compressed first word, A une k-coalg and the three short qualifiers are visible; the line ends de sorte and continues que.','misread word',conf='medium',crop=O,marked='yes'),
 R('Ab diagram: connector','headless F shaft','F arrow','headless F shaft','The short horizontal F-labelled stroke has no arrowhead.','drawing or diagram'),
 R('following line opening','est muni','ill','est muni','A short est precedes the two low joined groups of muni.','readable ink left as \\ill{}',marked='yes'),
 R('quasi-commutation phrase',r'à \unsure{\otimes}','ill',r'à \unsure{\otimes}','The accented a is followed by a retraced circular symbol; the interior cross is obscured.','readable ink left as \\ill{}',conf='low',crop=T,marked='yes'),
 R('compatibility list',r'\unsure{co. unit., comm.}','ill, comm.',r'\unsure{co. unit., comm.}','Three compressed groups precede the closing parenthesis; unit. and comm. are more secure than the first abbreviation.','readable ink left as \\ill{}',conf='low',crop=T,marked='yes'),
 R('first condition label','circled 1','(1)','circled 1','A continuous drawn oval encloses 1.','other'),
 R('gamma structure qualifier',r'\unsure{numér.|itérée}','ill',r'\unsure{numér.|itérée}','The compressed word has an initial upright curved group and a low multi-humped middle; the alternatives remain unresolved.','readable ink left as \\ill{}',conf='low',crop=S,marked='yes'),
 R('second condition label','circled 2','(2)','circled 2','A continuous drawn oval encloses 2.','other'),
 R('family description',"d'élts","d'éléments","d'élts",'The word is contracted to elts with a tall final t and low s.','abbreviation expanded or spelling modernised'),
 R('u_p display: map sign','A right arrow Gamma^p(A)','A right arrow Gamma^p(A)','A headless shaft Gamma^p(A)','The sign after A is a plain horizontal stroke without a head.','misread symbol or index','yes','yes'),
 R('product equation: coefficient','C_pq','c_pq','C_pq','The large open C rises to the full height of u and exceeds the subscript letters.','misread symbol or index',crop=P),
 R('product equation: final index',r'p+q|pq','p+q','pq','A p descender and q descender are present with no intervening plus stroke.','misread symbol or index','yes','yes',conf='medium',crop=P,con='The manuscript writes u_pq in the product law; the graded multiplication law requires u_(p+q).'),
 R('third formulation opening',r'3\unsure{ie|i.e}','ill','3 ie','An uncircled 3 stands to the left of a dotted i and shallow e; no internal stop is securely visible.','readable ink left as \\ill{}',conf='medium',crop=H,marked='yes'),
 R('third formulation: hom','hom','homomorphisme','hom','Only h and the low joined om group are written.','abbreviation expanded or spelling modernised'),
 R('deleted adjective after hom',r'\unsure{gradué}','ill','gradué','The descending g, joined middle letters and last raised stroke survive the horizontal cancellation.','readable ink left as \\ill{}',conf='medium',crop=H,marked='yes'),
 R('underbrace explanation',r'algèbre grâce à structure de coalg. de A et d’alg. grde de Gamma*(A)','algèbre quasi-commutative ill de la cogèbre A et ill gradué de Gamma*(A)',r'algèbre grâce à structure de coalg. de A et d’alg. grde de Gamma*(A)','The first line has algèbre, a second g-descender group, à, and structure; the next begins de coalg. de A et d’alg.; the last begins the contracted grde.','misread word',conf='medium',crop=U,marked='yes')
]
marks=[
 ('M0606','undecided',r'\unsure{A|B}','The argument is retraced: an oblique A outline and two B-like lobes overlap; their order cannot be secured.',A,'low'),
 ('M0607','first','B','Upright left stem and two right lobes are clear.',A,'high'),
 ('M0608','first','e','Small loop and entry stroke, not a dot or asterisk.','page','medium'),
 ('M0609','first','e','The same small looped form occurs at the rightmost object.','page','medium'),
 ('M0610','undecided',r'\unsure{Soit}','The very compressed initial word retains a tall first stroke and low ending; Soit remains plausible but not secure.',O,'low'),
 ('M0611','first','coalg','The c/o loops, tall l and descending g remain distinguishable.',O,'medium'),
 ('M0612','first','co. unit. comm.','The three abbreviated groups have separated starts; unit has a high t and comm a long shallow final group.',O,'medium'),
 ('M0613','first',r'\mathrm{Ab}','The angular A and small looped b are visible.','page','high'),
 ('M0614','first',r'\mathrm{Ab}','The repeated angular A and small b match the left object.','page','high'),
 ('M0615','undecided',r'\unsure{\otimes}','A circle is clear, but the thick interior does not securely resolve the crossing strokes.',T,'low'),
 ('M0616','undecided',r'\unsure{co. unit., comm.}','The first compressed abbreviation remains insecure; unit. and comm. are clearer.',T,'low'),
 ('M0617','first','équivalentes','The accent, q descender, high l and t, and final low es are visible.',E,'high'),
 ('M0618','undecided',r'\unsure{numér.|itérée}','The compressed interior and accents do not settle the alternative qualifiers.',S,'low'),
 ('M0619','first','avec','The initial a, shallow v and open final c fit avec; no x crossing is visible.','page','medium'),
 ('M0620','alternative','pq','The two descenders and their joining upper strokes have no intervening plus.',P,'medium'),
 ('M0621','first','ie','A dotted i is followed directly by a shallow e; no internal stop is secure.',H,'medium'),
 ('M0622','first','divisées','The tall d is followed by the contracted ivis and the final es group.',H,'medium'),
 ('M0623','first',r'\text{algèbre}','The a/l rise, g descender and following bre group are distinguishable.',U,'medium'),
 ('M0624','first',r'\text{grâce à}','The second descending g group is followed by a distinct accented a.',U,'medium'),
 ('M0625','first',r'\text{structure}','Tall initial strokes and the later t rise join the low remaining letters.',U,'medium'),
 ('M0626','first',r'\text{grde}','The short g-r-d-e group is contracted and is not the full word gradué.',U,'medium')
]
commit(k,t,rows,marks,[
 'diagram|top left|A to Gamma pq A/B square',
 'diagram|top right|Gamma p Hom(A,M) vertical shaft Hom(A,Gamma p M)',
 'diagram|upper middle|A to Gamma star M; Gamma p A to Gamma p Gamma e M',
 'diagram|middle|A to J; Gamma p A to Gamma p J to J',
 'drawing|below diagrams|slightly rising separator rule',
 'text|below rule|Soit A une k-coalg',
 'diagram|within opening paragraph|Ab k headless F Ab k',
 'text|opening continuation|est muni d’une structure',
 'deletion|heading|Conditions',
 'insertion|above Conditions|Données',
 'text|heading continuation|équivalentes',
 'text|lower half first condition|circled 1 Donnée d’une quasi-commutation',
 'text|lower half second condition|circled 2 Donnée d’une famille d’élts',
 'display|below second condition|u p in F A Gamma p A',
 'text|before brace|satisfaisant',
 'display|two-row brace|u p u q equals C pq u pq; composition law',
 'text|third formulation|3 ie d’un hom',
 'deletion|after hom|gradué',
 'display|bottom|k braces T to Hom(A,Gamma star A)',
 'text|underbrace|algèbre grâce à structure',
 'text|bottom left above final formula|satisfaisant',
 'display|bottom|Gamma p u(T(q)) composed with u(T(p))',
 'text|bottom left|330'
],'''This black-ink leaf switches from the previous leaf’s cohomology diagrams to divided powers of a coalgebra. Nothing from H’s editorial reference to absent pages is imported. The four upper diagrams are transcribed separately, followed by the rule and the prose. Manuscript page number 330.

The opening equips F_A(M)=Hom_k(A,M) with a tensor quasi-commutation structure from the coalgebra A. It presents equivalent data in terms of compatibility with Gamma^p, multiplication beta_pq and the iteration maps gamma_pq, then a family u_p and a map out of k{T}. The exact qualifier following “structure” in the gamma clause remains uncertain; it is not completed from the expected mathematics. The last line of the underbrace retains the short form grde.

136-329-gamma-type: the top arrow label unmistakably has superscript B. If its upper-right object is Gamma^(pq)(A), its target is Gamma^p(Gamma^q(A)), so the natural iteration map required there has superscript A. The prose equation below indeed writes gamma^A. The clear B is retained as written; the overwritten A/B above it is not forced to A by this check. The two e-shaped superscripts in the next diagram are also retained, distinct from the unmistakable asterisk in its upper-right object.

136-329-product-as-written / refined 136-329-product-graded: the first brace equation writes u_p u_q = C_pq u_pq, without a visible plus in the final index. In the graded convolution algebra Hom(A,Gamma*(A)), a product of degrees p and q has degree p+q. The usual divided-power relation would be u_p u_q = binomial(p+q,p) u_(p+q). For p=q=1 the written index pq is 1, whereas the product has degree 2; with A=Q and its grouplike coalgebra and the standard divided-power generators, the two homogeneous elements cannot agree. This checks the degree mismatch, not every equivalence asserted on the leaf. The written pq stays in the transcription.

136-329-iteration-types: both Gamma^p(u_q) composed with u_p and gamma^A_pq composed with u_pq map A to Gamma^p(Gamma^q(A)); the final T-formula has the same source and target. This type check does not establish existence of compatible data. The coalgebra-to-convolution construction and the full asserted equivalence are recorded, not independently proved here.''',checks=[
 ('136-329-gamma-type','targeted proof check','Compared source and target of the displayed gamma arrow with the lower equation: A is needed for the typed map, while the upper label visibly says B.'),
 ('136-329-product-as-written',"refuted, with the refined statement's id",'136-329-product-graded: for the standard divided powers of the grouplike coalgebra Q, p=q=1 gives degree 2 on the left and degree 1 on the written right; the omitted-plus reading cannot be the general graded product law.'),
 ('136-329-product-graded','targeted proof check','The convolution product adds grades, and T^(p)T^(q)=binomial(p+q,p)T^(p+q); this is the refined index, not a correction made in the manuscript text.'),
 ('136-329-iteration-types','targeted proof check','Composed the displayed domain/codomain pairs: both sides map A to Gamma^p(Gamma^q(A)).'),
 ('136-329-equivalent-data','carried as background without fault found','Recorded the asserted equivalence and its degree-0,1 conditions; no independent proof of the full equivalence is claimed.')
],habits=[
 'Scan 329: small open-loop e superscripts differ from the dense multi-stroke asterisk on the same diagram; H regularizes both to *. The clear two-lobed B in gamma^B is different from the retraced A/B object above it. The product-law subscript has only p and q; a required plus must not be supplied. The short forms hom, élts and grde are retained. Several function connectors are bare shafts, while neighbouring diagrams have explicit pointed heads.'
],notation=[
 ('Gamma^e versus Gamma^*','Two small looped e forms in the middle diagram, distinct from its solid asterisk above; no regularization to one grading symbol.'),
 ('gamma superscripts B / A','B is clear in the top square; A is clear in the lower iteration equation. The overwritten top object remains A/B.'),
 ('product versus iteration indices','The product law visibly has pq, as does the iteration law; the mathematical need for p+q in the former is noted separately.')
],abbreviations=[('coalg','coalgebra / coalgèbre'),('co.','coassociative, possibly; the abbreviated qualifier remains uncertain in the compatibility list'),('unit.','unitaire'),('comm.','commutative'),('comp.','compatibilité'),('élts','éléments'),('ie','id est'),('hom','homomorphisme'),('gr.','graduées'),('grde','graduée')],doubts=[
 ('upper-right object of first square',r'A|B','overwritten argument; no secure sequence of correction','low'),
 ('opening word','Soit','compressed initial word','low'),
 ('tensor sign',r'\otimes','interior strokes obscured by retracing','low'),
 ('compatibility list','co. unit., comm.','first abbreviation less secure than the last two','low'),
 ('gamma structure qualifier','numér.|itérée','compressed middle and accents','low')
],certainty=[('deleted adjective after hom',r'\unsure{gradué}','gradué','The surviving g descender, joined middle and last raised stroke are consistent beneath the strike.',H,'medium')])
