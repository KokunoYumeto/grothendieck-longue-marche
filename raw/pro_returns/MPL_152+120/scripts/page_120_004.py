from record_page import save_page
save_page(120,4,r'''
En résumé on voit que $M1$, $M2$, $M3$ peuvent être remplacés par

a) \deleted{$\unsure{\forall n}\ \forall\sigma\in\mathfrak S_n$} $\forall n\in\mathbb N^{\unsure{*|0}}$, $\sigma\in\mathfrak S_n$, $A\in\mathcal M_n$, on a $\sigma^*(A)\in\mathcal M_n$

b) $\forall n\in\mathbb N^*$, d'où
\[
\alpha_n:[1,\ldots n+1]\longrightarrow[1,n]\qquad
\left\{\begin{gathered}\text{identité sur }[1,n]\\ n+1\longmapsto n\end{gathered}\right.
\]
d'où \deleted{$\unsure{R}$}
\[
\alpha_n^*:R^n\hookrightarrow R^{n+1}\qquad(x_1,\ldots,x_n)\longmapsto(x_1,\ldots,x_n,x_n),
\]
on a
\[
\begin{aligned}
b_1)\quad&\forall A\in\mathcal M_n,\quad\alpha_n^*(A)\in\mathcal M_{n+1},\\
b_2)\quad&\forall B\in\mathcal M_{n+1},\quad\alpha_n^{*-1}(B)\in\mathcal M_n
\end{aligned}
\]
c) $\forall n\in\mathbb N^*$, d'où $\beta_n:[1,n]\hookrightarrow[1,n+1]$ inclusion can., d'où
\[
\beta_n^*:R^{n+1}\longrightarrow R^n,\quad(x_1,\ldots,x_{n+1})\longmapsto(x_1,\ldots,x_n),
\]
on a
\[
\begin{aligned}
c_1)\quad&\forall A\in\mathcal M_{n+1},\ B\in\mathcal M_n,\text{ on a }A\cap\beta_n^{*-1}(B)\in\mathcal M_{n+1}\\
c_2)\quad&\forall A\in\mathcal M_{n+1},\quad\beta_n^*(A)\in\mathcal M_n
\end{aligned}
\]

\textcircled{3} $M1$ implique que si un des $\mathcal M_n$ est vide, tous le sont -- et alors les axiomes $M1$ à $M4$ sont satisfaits trivialement. On va exclure ce cas \inserted{trivial}, i.e. supposer
\[
(*)\qquad\mathcal M_1\ne\varnothing.
\]
$\unsure{M1|M4}$ implique que si un des $\mathcal M_n$ contient $\varnothing$, tous le contiennent. Si ce n'est pas le cas, alors chaque $\mathcal M_n$ (étant stable par intersection de deux ens) est une base de filtre sur $R^n$.

On exclut ce cas, i.e. on suppose la relation suivante, plus forte que $(*)$
\[
(**)\qquad\varnothing\in\mathcal M_1\qquad(\text{d'où }\varnothing\in\mathcal M_n\quad\forall n\in\mathbb N)
\]
\uline{NB} Si cette propriété \unsure{n'étant|n'était} vérifiée, les présents
\mspage{3}
''',[
('text','top','En résumé on voit que M1,M2,M3'),('text','upper item a','forall n; sigma in S_n; sigma*(A) in M_n'),('deletion','item a opening','forall n; forall sigma in S_n'),('text','upper item b','forall n in N*, d’où'),('display','item b definition','alpha_n:[1,...n+1] to [1,n]; identité; n+1 maps to n'),('text','item b','d’où; on a'),('deletion','before alpha_n*','R'),('display','item b','alpha_n*: R^n hook to R^{n+1}; coordinate duplication'),('display','item b1','forall A in M_n; alpha_n*(A) in M_{n+1}'),('display','item b2','forall B in M_{n+1}; alpha_n^{*-1}(B) in M_n'),('text','middle item c','forall n; beta_n:[1,n] hook to [1,n+1]; inclusion can.'),('display','item c','beta_n*: R^{n+1} to R^n; coordinate projection'),('text','item c','on a'),('display','item c1','A intersection beta_n^{*-1}(B) in M_{n+1}'),('display','item c2','beta_n*(A) in M_n'),('text','lower comment 3 first paragraph','M1 implique que si un des M_n est vide'),('insertion','right of lower first paragraph','trivial'),('display','lower first','(*) M_1 not empty'),('text','lower second paragraph','M1 implique que si un des M_n contient emptyset'),('text','lower third paragraph','On exclut ce cas'),('display','bottom','(**) emptyset in M_1; emptyset in M_n forall n in N'),('text','bottom continuation','NB Si cette propriété n’étant vérifiée, les présents'),('text','bottom left page number','3')
],observations='The comments explicitly restate M1–M3 using permutations, alpha_n (last-coordinate duplication), beta_n (projection), and five conditions a,b1,b2,c1,c2. The two empty-family or filter-base cases are excluded via (*) M_1 nonempty and the stronger (**) emptyset in M_1. The last NB continues; its short verb form is uncertain and is not normalized. The positivity star is visible in the axioms; the final quantifier after (**) is written N without a visible star.')
