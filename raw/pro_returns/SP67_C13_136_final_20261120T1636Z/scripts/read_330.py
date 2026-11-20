from workflow import *
n=330
cp=lambda s:f'scan 330 {s}'
t,ds=resolve(n,[
 ('pq','Joined p and q; no separate plus cross.',cp('(600, 278, 992, 371)'),'high'),
 ('pq','Two connected subscript letters, no comma.',cp('(174, 383, 1020, 498)'),'high'),
 (r'\unsure{*|p}','Star-like strokes over a p-shaped stem; overwrite cannot be separated confidently.',cp('(174, 383, 1020, 498)'),'low'),
 ('2','Small loop and descending diagonal ending in a rightward base: a 2.',cp('(174, 383, 1020, 498)'),'high'),
 (r'\Delta','Triangular sign, overwritten but still triangular.',cp('(1050, 20, 1520, 207)'),'medium'),
 (r'\alpha','Closed lower loop and right arm, unlike the open crossed X elsewhere.',cp('(1082, 282, 1560, 397)'),'high'),
 ('OK','Large O followed by K.','page','high'),('OK','Second large O followed by K.','page','high')])
t='\\cotefile{136}\n'+t
t=repl(t,r'\unsure{\beta}',r'\beta')
t=repl(t,r'\Delta:\ A-A\otimes A',r'\Delta:\ A\longleftarrow A\otimes A')
t=repl(t,r'u_p:\ A-\Gamma^p A',r'u_p:\ A\longleftarrow\Gamma^p A')
t=repl(t,r'\tau^{\alpha}_p',r'\sigma^{\alpha}_p')
t=repl(t,r'\unsure{algèbre|définie}','algèbre')
t=repl(t,r'\unsure{$k$-lin.}',r'$k$-lin.')
t=repl(t,r'\unsure{i.e un hom can. de}','i.e un hom can. de')
t=t.replace(r'\Gamma^{\unsure{*|\alpha}}',r'\Gamma^\alpha')
t=repl(t,r'\unsure{,\,V}',r',\,V')
t=repl(t,r'\ \unsure{\longrightarrow}','')
t=repl(t,r'\unsure{\text{i.e.}}',r'\text{i.e.}')
t=repl(t,r'\unsure{\text{un élt}}',r'\text{un élt}')
t=repl(t,r'\unsure{\text{p. ex.}|\text{puiss.}}',r'\text{p. ex.}')
t=repl(t,r'A\underset{k}{\Longrightarrow} B',r'A\underset{\unsure{h|k}}{\Longrightarrow} B')
t=repl(t,r'\operatorname{Sym}^*(\unsure{\,}',r'\operatorname{Sym}^*(')
# The drawn boundary strokes mark separation/cancellation, not an extra mathematical figure.
a=t.index('\\figure{\\begin{tikzpicture}')
b=t.index('\\end{tikzpicture}}',a)+len('\\end{tikzpicture}}')
t=t[:a]+r'\par\noindent\rule{.9\linewidth}{.3pt}'+t[b:]
a=t.index('\\figure{\\begin{tikzpicture}')
b=t.index('\\end{tikzpicture}}',a)+len('\\end{tikzpicture}}')
t=t[:a]+t[b:]
ch=[
 change('composition map label',r'\deleted{\unsure{\beta}}\inserted{\gamma}',r'\gamma',r'\deleted{\beta}\inserted{\gamma}','A double-loop beta is overwritten by a descending gamma.','omission',False,True,crop=cp('(155, 30, 666, 225)')),
 change('beta target exponent',r'\unsure{p+q|pq}','p+q','pq','The p joins the q directly, as in the composition degree above; no plus is visible.','misread symbol or index',crop=cp('(600, 278, 992, 371)'),consequential=True),
 change('alpha subscript','p,q','pq','pq','No comma between the two joined letters.','misread symbol or index',True,False,crop=cp('(174, 383, 1020, 498)')),
 change('alpha source, first exponent','*|p','p',r'\unsure{*|p}','A p-shaped stem is overworked with crossed strokes; star is the better current reading.','misread symbol or index',False,True,'low',cp('(174, 383, 1020, 498)')),
 change('alpha source, second exponent','*','q','*','Several intersecting short strokes form a star, not a descending q.','misread symbol or index',False,True,crop=cp('(174, 383, 1020, 498)')),
 change('Delta display','A-A tensor A','A to A tensor A',r'A\longleftarrow A\otimes A','A faint two-stroke head is at the left end.','misread symbol or index',crop=cp('(1050, 20, 1520, 207)'),consequential=True),
 change('u_p display','A-Gamma^p A','A to Gamma^p A',r'A\longleftarrow\Gamma^p A','The head is again at the left end.','misread symbol or index',crop=cp('(1050, 20, 1520, 207)'),consequential=True),
 change('F(Gamma) comparison label',r'\tau^{X|alpha}_p',r'\sigma^X_p',r'\sigma^\alpha_p','The letter has a closed lower bowl and a rightward top bar; the superscript is looped alpha.','misread symbol or index',crop=cp('(1082, 282, 1560, 397)'),consequential=True),
 change('OK annotations','OK OK','« ok ok »','OK OK','Two capitals; no quotation signs around either.','text not on the page',False,True),
 change('boundary and cancellation strokes','two separate TikZ pictures','cancellation described in note','separator rule; cancelled draft in deleted macro','The long oblique strokes cross prose and formulas; the enclosing outline is a drafting/cancellation boundary, not a separate figure.','drawing or diagram',True,False),
 change('draft opening, erased qualification','de car. 0',r'\ill{}','de car. 0','The crossed phrase preserves de, car. and 0.','readable ink left as \\ill{}',False,True,crop=cp('(220, 573, 1420, 744)'),marked='yes'),
 change('draft opening, second line','on va définir un hom can.','on définit une flèche can.','on va définir un hom can.','va is distinct before définir; hom has a tall initial and joined low strokes.','misread word',False,True,crop=cp('(220, 573, 1420, 744)'),marked='yes'),
 change('draft opening, erased linearity','k-lin.',r'\ill{}','k-lin.','Crossed k, hyphen and lin. remain legible.','readable ink left as \\ill{}',False,True,crop=cp('(220, 573, 1420, 744)'),marked='yes'),
 change('before Sym^n map','par ses restrictions',r'\ill{} restriction','par ses restrictions','par, ses and final plural strokes survive.','readable ink left as \\ill{}',False,True,marked='yes'),
 change('before u_n formula','et en prenant','et on prendra','et en prenant','The line has en and the continuous -nant ending.','misread word',False,True),
 change('underbrace label','Sym^*(A)','Sym^n(A)','Sym^*(A)','The raised sign is a small crossed star; it has no arch of n.','misread symbol or index',False,True,crop=cp('(590, 1045, 1040, 1144)')),
 change('diagram introduction','Je dis que le diagramme',r'je dis que \ill{} le diagramme','Je dis que le diagramme','Continuous text; no additional word in the alleged gap.','text not on the page',False,True,marked='yes'),
 change('lower paragraph opening','i.e un hom can. de',r'\ill{} une \ill{} can. de','i.e un hom can. de','i.e, un and the tall initial of hom survive above the erased formula.','readable ink left as \\ill{}',False,True,'medium',cp('(285, 1460, 1010, 1696)'),marked='yes'),
 change('after erased completed tensor','a separate right arrow','no separate arrow','no separate arrow','The rightward hook belongs to the strike through the expression; no independent map has a source and target here.','drawing or diagram',True,False,crop=cp('(285, 1460, 1010, 1696)')),
 change('second erased Gamma expression',r'\Gamma^{*|alpha},V(A)',r'\Gamma^\alpha(V(A))',r'\Gamma^\alpha,V(A)','V is on the baseline, after a comma; alpha is a raised closed loop.','misread symbol or index',True,True,'medium',cp('(285, 1460, 1010, 1696)')),
 change('Hom subscript','k-lin.','omitted','k-lin.','Small k-lin. is below Hom.','omission',False,True,crop=cp('(285, 1460, 1010, 1696)')),
 change('Hom target parenthesis','B with no closing parenthesis','B)','B with no closing parenthesis','There is no curved closing stroke after B.','text not on the page',False,True,crop=cp('(285, 1460, 1010, 1696)')),
 change('lower tensor explanations','i.e. un élt de; Gamma^*(check A) tensor B; p. ex. de check A tensor_k B','reordered; Gamma^alpha(check A) tensor B','i.e. un élt de; Gamma^*(check A) tensor B; p. ex. de check A tensor_k B','The two lines proceed left to right; the lower exponent is crossed, and the check A tensor belongs after p. ex. de.','insertion or placement',False,True,'medium',cp('(345, 1695, 1300, 2025)'),marked='yes'),
 change('last map label','k','h',r'\unsure{h|k}','A tall stem with low rightward connection; both h and his cursive k remain possible.','misread symbol or index',True,False,'low',cp('(345, 1695, 1300, 2025)')),
 change('final incomplete formula',r'\operatorname{Sym}^*(\unsure{\,}',r'\mathrm{Sym}^*(\ldots',r'\operatorname{Sym}^*(','Only the opening parenthesis and stray ink dots follow the star; no lost readable symbol or ellipsis is supplied.','text not on the page',True,True,crop=cp('(345, 1695, 1300, 2025)')),
 change('bottom archive number','331','omitted','331','331 written separately at the foot.','omission',False,True)
]
items=[inv('diagram','upper left','Gamma^p(Gamma^q(X)) / Gamma^{pq}(X)'),inv('deletion','composition label','beta'),inv('insertion','composition label','gamma'),inv('diagram','upper left, second line','beta^X_{p,q}'),inv('diagram','upper left, third line','alpha^{X,Y}_{pq}'),inv('display','upper right','Delta: A <- A tensor A'),inv('display','upper right, below','u_p: A <- Gamma^p A'),inv('diagram','upper right, next two lines','F(X tensor Y); F(Gamma^p(X))'),inv('text','upper right below diagrams','OK OK'),inv('deletion','entire lower draft','Soit A algèbre ... Sym^*('),inv('text','draft first two lines','Soit A algèbre'),inv('deletion','draft line 1','de car. 0'),inv('deletion','draft line 2','k-lin.'),inv('display','draft first display','Sym^* A -> A'),inv('text','draft after display','par ses restrictions'),inv('display','draft second display','Sym^n(A) -> A (n>=0)'),inv('text','draft before formula','et en prenant'),inv('display','draft formula with underbrace','u_n(x_1...x_n)=1/n! ...'),inv('text','draft above diagram','Je dis que le diagramme'),inv('diagram','middle-lower','Sym^{p+q} A; A; Sym^p A tensor Sym^q A; A tensor A'),inv('text','below diagram','i.e un hom can. de'),inv('deletion','lower erased formulas','(Gamma^alpha(A) tensor A)^hat; Gamma^alpha,V(A)'),inv('display','lower Hom line','Hom_{k-lin}(Sym^* A,B'),inv('display','lower equalities','Gamma^*(check A) tensor_k B'),inv('text','alongside equalities','i.e. un élt de; p. ex. de'),inv('deletion','lower left','u'),inv('display','near bottom','A => B; k lin.'),inv('display','bottom incomplete lines','Sym^* A; Sym^*('),inv('text','foot','331',hand='unnamed hand')]
commit(n,t,ds,ch,items,
 'Opening operations on divided powers, followed by a cancelled draft about maps Sym^*A to A and the factors 1/n!. The sheet bears 331 at the foot. The product map is written with target degree pq, although the usual homogeneous product would have degree p+q; this visible slip is retained. The alpha target is visibly 2, not the expected star. Both short right-hand maps point left. Their directions agree with multiplication and divided-power operations on an algebra, so the apparent coalgebra interpretation was rejected. The comparison label reads sigma with an alpha-shaped superscript, retained even though X is natural there. The draft division by n! has no surviving characteristic-zero assumption (that qualification was crossed out); its unrestricted validity is not asserted. No missing end of the Hom parenthesis or final Sym expression has been supplied. The lower map name remains h|k. The erased exponents read alpha. The faint first exponent of the alpha source remains *|p.',
 hand=['p and q may be joined by a long connector (composition and product targets); that connector is not a plus sign. Both witnesses normalized the beta target to p+q.','Small alpha has a closed lower loop; X is open and crossed. At the F(Gamma) label C preferred X and H printed X; the crop shows alpha.','Short left arrows may look like bare dashes at page scale (Delta and u_p). C used dashes and H reversed the direction.','Large oblique lines cancel whole regions; the surrounding irregular outline is not a separate mathematical drawing.','The cursive k in k-lin. and tensor subscripts can resemble h. The last map label is not settled.'],
 notation=[(r'\Gamma^p,\Gamma^{pq}','Divided powers; joined degree letters must not acquire an inferred plus.'),(r'\alpha,\beta,\gamma;\tau,\sigma','Operation and comparison labels; alpha-shaped superscript retained where visibly written.'),(r'\check A','A short vee above A, not a prime.'),(r'\operatorname{Sym}^*','Symmetric algebra; tiny crossed stars can resemble 2 or alpha.')],
 abbr=[('hom can.','homomorphisme canonique'),('k-lin.','k-linéaire'),('p. ex.','par exemple'),('élt','élément'),('i.e.','id est')],
 checks=[check('330-note-product-degree','Degree of a homogeneous product adds: p+q; the ink pq is retained as a manuscript slip.','targeted proof check'),check('330-note-map-directions','Left arrowheads confirmed on the image; algebra interpretation is compatible, but no algebra structure is proved.','used and rechecked in this run'),check('330-text-draft','Cancelled construction with 1/n!, Hom and divided powers read as manuscript claims; not proved.')],
 unresolved=[r'alpha source first exponent \unsure{*|p}',r'last map label \unsure{h|k}',r'crossed isolated \unsure{u} retained; its strokes do not settle a fuller reading'])
