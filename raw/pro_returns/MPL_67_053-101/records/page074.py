import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{74}
\mspage{11}
% archive foliation: 76
d) Les séries convergentes
\[
f=\sum_{i\geq0}a_i z^i\qquad(a_i\in\mathbb C)
\]
de rayon de convergence $\geq1$ (donc
définissant $\mathring{\mathbb D}\longrightarrow\mathbb C$)
\inserted{avec $|f(z)|\leq1$ si $z\in\mathbb D$}, telles que la $f$
se prolonge par continuité en une
fonction $\mathbb D\longrightarrow\mathbb D$, celle-ci ayant les
propriétés 1) 2) 3) de B) ci-dessus.

\textcircled{6}
\margin{\uline{13.1.}}
Soit $(X,C)$ un objet du groupoïde
de Teichmüller analytique complexe
à bord, avec la condition différentiable.
Pour fixer les idées, supposons $X$ connexe,
de type $g,\nu$. Considérons la découpe \inserted{$X'$}
de $X$ suivant $C$, bouchons ses trous
\inserted{(canoniquement en utilisant la structure torique de $\delta X'$)*},
\margin{* via la métrique riemannienne can. de $X'$}
d'où \unsure{surfaces} holomorphes compactes \inserted{sans bord $X''$}, à disques
\inserted{ponctués} marqués, avec des \deleted{iso}\inserted{\unsure{antiiso|antiso}} de \deleted{ces}\inserted{certains de ces} disques
(qui se groupent \deleted{deux à deux} par paires, à l'exception
des $\nu$ disques correspondant à $\delta X$).
On peut considérer $X''$ comme la
normalisée d'une courbe \deleted{$\unsure{R}$}\inserted{$\mathbb C$-alg $X'''$} stable
(au sens de Mumford-Deligne), en
"""
save(74,tex,[('text','top','d) Les séries convergentes'),('display','top','f=Σ_{i≥0} a_i z^i'),('text','upper','de rayon de convergence≥1'),('insertion','upper','avec |f(z)|≤1 si z∈D'),('text','middle','6 Soit (X,C)'),('margin note','middle left','13.1.'),('text','middle lower','Pour fixer les idées'),('insertion','middle lower','X′'),('insertion','lower','canoniquement en utilisant la structure torique'),('margin note','lower left','via la métrique riemannienne can. de X′'),('insertion','lower','sans bord X″'),('insertion','lower','ponctués'),('deletion','lower','iso'),('insertion','lower','antiiso'),('deletion','lower','ces'),('insertion','lower','certains de ces'),('deletion','lower','deux à deux'),('text','bottom','On peut considérer X″'),('deletion','bottom','R'),('insertion','bottom','C-alg X‴')],
 doubts=[('after d’où','surfaces','singular/plural ending nearly flat; following plural retained','medium'),('inserted map type','antiiso','antiso possible spelling','medium'),('deleted before stable','R','overwritten capital hardly legible','low')],
 notations=[('Cut, capped, and stable curves',r"X',X'',X'''",'One, two, three primes; not exclamation marks'),('Antiholomorphic identification abbreviation',r'\unsure{antiiso|antiso}','scan 74 insertion')],
 abbreviations=[('C-alg','complex algebraic'),('iso','isomorphismes'),('antiiso / antiso','anti-isomorphismes')],
 leads=['Scholie adds convergent power-series encoding of normalized slit maps, with coefficient, radius, boundedness and boundary-extension conditions.','Dated 13.1, section 6 passes from cut bordered surfaces to capped compact holomorphic surfaces with paired pointed discs and anti-isomorphisms.','Capped surface regarded as normalization of a stable complex algebraic curve in the sense of Mumford–Deligne; continuation on scan 75.'])
