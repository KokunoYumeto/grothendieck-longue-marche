import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{84}
% archive foliation: 83
Enfin, si $X=\bigoplus_{1\leq i\leq r}X_i$, la décomposition de $\Gamma^*(X)$ en \deleted{les} $\bigotimes\Gamma^*(X_i)$ donne \deleted{\unsure{une}} décomposition des $P_n(\prod X_i;Y)$ en des $P_{\nu_1,\ldots,\nu_r}(X_1,\ldots,X_r,Y)$.
On vérifie alors les axiomes c) à g), et le fait que \deleted{\unsure{il y a}} les produits tensoriels de $P_1$ sont \uline{stricts} pour $P$ (\unsure{vis} quelc. des facteurs), que les $\Gamma^{\nu_i}$ existent et satisfont la condition énoncée précédemment\ldots
\figure{\begin{tikzpicture}\draw (0,0)--(2.5,.05);\end{tikzpicture}}
Une catégorie polynomiale $P$ est dite \uline{stricte} si elle satisfait aux conditions préliminaires permettant de définir $\otimes$ et $\Gamma^*$ avec toutes les propriétés envisagées. D'autre part, une cat additive $P_1$ avec $\otimes$ et $\Gamma^*$ avec les structures décrites, est dite une $\otimes$-pd-catégorie. Les deux notions sont donc en équivalence.

On dit que $P$ est \deleted{\unsure{$k$-li}} une catégorie polynomiale (resp $\otimes$pd-cat) $k$-linéaire ($k$ anneau comm) si on a donné un hom d'anneau
\[k\longrightarrow\operatorname{End}(\mathrm{Id}_{P_1})\quad(\unsure{\subset\mathrm{id}_P}).\]
'''
e=[('text','top','Enfin si X = direct sum Xi'),('deletion','top','les'),('deletion','top third line','une'),('text','upper-middle','On vérifie alors les axiomes'),('deletion','upper-middle','il y a'),('drawing','middle','horizontal separator'),('text','middle-lower','Une catégorie polynomiale P est dite stricte'),('text','lower','On dit que P est'),('deletion','lower','k-li'),('display','bottom','k -> End(Id_P1) (subset id_P)')]
save(84,text,e)
