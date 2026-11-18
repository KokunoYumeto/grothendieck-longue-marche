import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{85}
% archive foliation: 87
revient à se donner un scindage de l'extension
\diagram{\begin{tikzcd}[column sep=small]
(\ast)\qquad 1 \arrow[r] & V \arrow[r] & \Gamma \arrow[r,dash] \arrow[d,equal] & \operatorname{Aut}(V) \arrow[r,dash] \arrow[d,"\simeq",draw=none] & 1 \\
&& \operatorname{Nor}_G(V) & \unsure{\mathfrak S}_J &
\end{tikzcd}}
En termes géométriques, ces scindages sont associés
aux quatre systèmes de \inserted{paires de} faces antipodiques sur l'
octaèdre. \deleted{Ainsi, les} L'octaèdre combinatoire (non orienté
a priori) se définit à partir de l'ens $S$ de
ses sommets, et l'antipodisme \deleted{sur} $S$, de la façon
habituelle; ses faces sont les parties à trois éléments \deleted{qui}
$S'$ telles que $S'\cup\uline{a}(S')=S$. Pour un tel triplet,
le sous-groupe de $\Gamma$ qui l'invarie est un scindage
de l'extension $(\ast)$.

Le groupe $\Gamma$ est le groupe des autom. de
$S$ qui conserve \deleted{\unsure{des}} structure octaédrique
\uline{orientée} (définie par l'ens \inserted{$F\subset\mathcal P_3(S)$} des \deleted{8} faces \deleted{\unsure{et}} l'ens
des arêtes \inserted{$A\subset\mathcal P_2(S)$} est défini comme l'ens des parties de
card 2 contenues dans une face), par le choix
d'une orientation $\omega$. Choisir cette orientation, revient \inserted{donc}
à la choisir dans le cas standard $X=\mathbb P^1$, $S=\{0,\infty,\pm1,\pm i\}$,
où une face est $\{0,1,i\}$, et les faces \inserted{\uline{orientées}} $\overrightarrow{\{0,1,i\}}$ et
$\overrightarrow{\{0,1,-i\}}$ sont \uline{opposées}. Donc le choix d'une orientation
combinatoire revient au choix d'une racine carrée de
$-1$.

Pour un sous-groupe $V\simeq D_2$ de $G_X$, on désigne
par $\operatorname{Oct}(V)\subset X$ l'octaèdre correspondant, par $I(V)=F/\uline{a}_I$
l'ens de ses paires de faces antipodiques. Mais : $\Gamma(V)=\operatorname{Nor}_G(V)$
"""
save(85,tex,[('text','top','revient à se donner un scindage'),('diagram','top','1 V Gamma Aut(V) 1'),('text','upper to middle','En termes géométriques'),('insertion','above faces','paires de'),('deletion','before L’octaèdre','Ainsi, les'),('deletion','after l’antipodisme','sur'),('deletion','after éléments','qui'),('text','lower half','Le groupe Gamma est le groupe'),('deletion','before structure','des'),('insertion','above des faces','F subset P3(S)'),('deletion','before faces','8'),('deletion','after faces','et'),('insertion','above est défini','A subset P2(S)'),('insertion','above revient','donc'),('insertion','above oriented face triple','orientées'),('text','foot','Pour un sous-groupe V isomorphic D2')],doubts=[('symmetric-group glyph','mathfrak S_J','Same curled glyph as scan 84.','medium'),('after conserve','structure','No article reliably visible after deleted des.','medium'),('after faces','et','Tiny cancelled connector; reading very uncertain.','low'),('last quotient','F/a_I','The final I may be a subscript or stray upright stroke.','low'),('last sentence connector','Mais','Could be a very short alternative word; initial M appears clear.','medium')],notations=[('antipodism',r'\uline{a}','Underlined a, not Greek alpha.'),('oriented face',r'\overrightarrow{\{0,1,i\}}','Long arrow over the whole triple.'),('octahedron',r'\operatorname{Oct}(V)','Operator named Oct.'),('face pairs',r'I(V)=F/\uline{a}_I','Subscript I uncertain; retained from ink.')],abbreviations=[('Nor','normalisateur')],leads=['Splittings of 1 -> V -> normaliser -> Aut(V) -> 1 correspond to four antipodal face pairs; face stabiliser described as splitting.','Oriented combinatorial octahedron on {0,infty,+/-1,+/-i}: orientation choice identified with choice of square root of -1.','Intrinsic V-torsor I(V) of antipodal face pairs is introduced; connect to arithmetic descent only in notes after freeze.'])
