from record_page import record
record(21,r'''\scanpage{21}
\deleted{\unsure{4}}
Donc si $f$ et $g$ sont sym. à translation près, la condition $(f,g)$ \unsure{privilégié|priorisé} est une condition \uline{symétrique} en $f,g$.

4. \uline{Couples bons.}
\[
f,g\in\mathbb R[G]^+.
\]
\margin{Cette condition est inv. par translation. \deleted{\unsure{Donc}} Si $(f,g)$ est bon, $\check g,\check f$ aussi. Donc si $f,g$ sont sym. mod translation, alors $(f,g)$ bon sss $(g,f)$ bon.}

\uline{Prop} Conditions équivalentes

a) $f'\prec f$, $g'\prec g\Longrightarrow f'\ast g'\prec f\ast g$

b) $f'\sim f$, $g'\sim g\Longrightarrow f'\ast g'\prec f\ast g$

c) $\forall h\in\mathbb R[G]^+$
\[
\operatorname{Sup}_{\substack{f'\prec f\\g'\prec g\\h'\prec h}}
(f'\ast g'\ast h')(0)
\leq\operatorname{Sup}_{\substack{\deleted{\unsure{h'\prec h}}\\h'\sim h}}f\ast g\ast h'(0)
\]
\[
\left(\operatorname{Sup}_{h'\sim h}\|f\ast g\ast h'\|_\infty\right.
\]
c') $\forall A\in\mathcal P_f(G)$,
\[
\operatorname{Sup}_{\substack{A'\sim A\\f'\sim f\\g'\sim g}}f'\ast g'\ast A'(0)
\leq\operatorname{Sup}_{A'\sim A}f\ast g\ast A'(0)
\]
\[
\left(\operatorname{Sup}_{A'\sim A}\|f\ast g\ast A'\|_\infty\right.
\]
Cela implique que $(f,g)$ est \uline{\unsure{privilégié|priorisé}}

\uline{Cor} Soit $S\subset\mathbb R[G]^+$, $S$ \uline{stable par $\ast$}.
\deleted{Pour que}\inserted{Conditions équiv. :}

\deleted{$S$ soit} a) \unsure{tt.} couples $(f,g)\in S\times S$ sont bons, \deleted{il f. et s.}

b) \deleted{que} pour \deleted{tout} $n\in\mathbb N$, $n\geq2$, $f_1,\ldots,f_n\in S$, $f'_1,\ldots,f'_n\in\mathbb R(G)^+$
$f'_1\prec f_1\ldots$, $f'_n\prec f_n$ implique
\[
f'_1\ast\cdots\ast f'_n\prec f_1\ast\cdots\ast f_n
\]
c) [Si $\forall n\in\mathbb N^\ast$, \inserted{$n\leq\operatorname{card}G$}, $(\exists A\in S\cap\mathcal P_f(G)$ tel que $\operatorname{card}A=n$]
\margin{$\longrightarrow$ ``Condition $K$''}
\margin{condition $K$ $\Updownarrow$ \unsure{hyp}}
\[
f'_1\prec f_1,\ldots,f'_n\prec f_n\quad(f'_i\in\mathbb R(G)^+,\ f_i\in S)\Longrightarrow
\]
\[
\|f'_1\ast\cdots\ast f'_n\|_\infty\leq\|f_1\ast\cdots\ast f_n\|_\infty
\]
(ou $f'_1\ast\cdots\ast f'_n(0)$

\deleted{``condition $K$'' d) $\unsure{f'_1\sim f_1,\ f'_2\sim f_2,\ \ldots}\quad f'\sim f,\ g'\sim g,\ A'\sim A\in\mathcal P_f(G)\cap S\Longrightarrow f'\ast g'\ast A'(0)\leq\|f\ast g\ast A\|_\infty$}
% archive foliation: 20
''',[
('deletion','upper left','4'),
('text','top','Donc si f et g sont sym. à translation près ...'),
('text','heading','4. Couples bons.'),
('display','upper','f,g∈R[G]^+'),
('margin note','upper right','Cette condition est inv. par translation ...'),
('deletion','within margin','Donc'),
('text','upper','Prop Conditions équivalentes'),
('display','upper middle','a) f′≺f,g′≺g⇒f′*g′≺f*g'),
('display','upper middle','b) f′∼f,g′∼g⇒f′*g′≺f*g'),
('text','middle','c) ∀h∈R[G]^+'),
('display','middle','Sup(f′*g′*h′)(0)≤Sup f*g*h′(0)'),
('deletion','under right supremum','h′≺h'),
('display','middle','(Sup ||f*g*h′||∞'),
('text','middle','c′) ∀A∈P_f(G)'),
('display','middle lower','Sup f′*g′*A′(0)≤Sup f*g*A′(0)'),
('display','middle lower','(Sup ||f*g*A′||∞'),
('text','lower','Cela implique que (f,g) est privilégié/priorisé'),
('text','lower','Cor Soit S⊂R[G]^+, S stable par *'),
('deletion','lower right','Pour que'),
('insertion','lower right','Conditions équiv. :'),
('text','lower','a) tt. couples (f,g)∈S×S sont bons'),
('deletion','within a','S soit; il f. et s.'),
('text','lower','b) pour n∈N, n≥2 ... implique'),
('deletion','within b','que; tout'),
('display','lower','f′_1*...*f′_n≺f_1*...*f_n'),
('text','bottom','c) [Si ∀n∈N* ... ∃A ... cardA=n]'),
('insertion','above c condition','n≤cardG'),
('margin note','right of c','→ “Condition K”'),
('margin note','left of c','condition K; ⇕ hyp'),
('display','bottom','f′_1≺f_1,...⇒ norm inequality'),
('text','bottom','(ou f′_1*...*f′_n(0)'),
('deletion','bottom edge','condition K; d) f′_1∼f_1,... f′∼f,g′∼g,A′∼A ...')
],'''The symmetry reservation from scan 20 is narrowed: symmetry holds when f and g are symmetric up to translation; the marginal argument invokes inversion and translation. Section 4 defines good pairs through convolution preserving majorization and gives three/four equivalent tests without proofs on this page. A convolution-stable family S of pairwise good functions is asserted to yield all finite-product rearrangement inequalities. The explicitly named “Condition K” supplies indicator functions of every allowable cardinality and is attached to the norm-test equivalence. The crossed bottom alternative is retained; the distinction between ≺ in c and ∼ in c′ is literal.''')
