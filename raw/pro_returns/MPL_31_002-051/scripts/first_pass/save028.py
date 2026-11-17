import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
s=r'''\scanpage{28}
\mspage{9}
Posons
\[
\text{(2.5)}\qquad\underline S=\operatorname{gr}_{\mathcal J}\underline O_{X'}
=\coprod_{k\in\underline{\underline N}}\mathcal J^k/\mathcal J^{k+1}
\]
\[
\text{(2.6)}\qquad\operatorname{gr}_{\mathcal J}(\underline F)
=\coprod_{k\in\underline{\underline N}}\mathcal J^k\underline F/\mathcal J^{k+1}\underline F
\]
\[
\text{(2.7)}\qquad\underline K^i=R^if_*(\operatorname{gr}_{\mathcal J}(\underline F))
=\coprod_{k\in\underline{\underline N}}R^if_*(\mathcal J^k\underline F/\mathcal J^{k+1}\underline F),
\]
il est clair que $\underline K^i$ est muni d'une structure de $\underline S$-Module
gradué.

\uline{Théorème 2.1.} Supposons que $\underline K^i$ soit un $\underline S$-Module gradué
\uline{de type fini} pour $i=n-1,i=n,i=n+1$, alors:

(i) $R^nf_*(F)$ est cohérent

(ii) l'homomorphisme $\unsure{\psi|\varphi}_n$, (2.3), est un isomorphisme
topo\inserted{l}ogique\inserted{, La filtration naturelle du deuxième membre
de (2.3.) est $\mathcal J$-bonne.}

(iii) le système projectif des $R^nf_*(F_k)$ vérifie
la condition de Mittag-Leffler uniforme.

La démonstration est très facile à partir de
E.G.A.$0_{\mathrm{III}}$.13.7.7.\inserted{(cf. E.G.A. III 3.4.2.)}, à condition de rectifier comme suit
le texte page 78:

\uline{Supprimer}

\begin{tabular}{ll}
ligne 6 & `` et $(R^{n+1}T(A_k))_{k\in\underline{\underline Z}}$ ''\\[1ex]
ligne 13 & `` et $p+q=n+1$''\\[1ex]
ligne 23 & `` et pour $n+1$''.
\end{tabular}

\uline{Théorème 2.2.} Soit $A$ un anneau adique noethérien et soit
$I$ un idéal de définition de $A$.\inserted{Soit $T$ une partie fermée de $X'=\operatorname{Spec}(A)$.}
Supposons que $I$ soit engendré par un $t\in A$. Reprenons les notations (1.31)\inserted{,}(1.32) et
(1.33). Soit $\underline F$ un $\underline O_{\widehat X}$-Module cohérent. Posons
\[
\text{\unsure{(2.8)|(2.89)}}\qquad F_0=\underline F/\mathcal J\underline F,
\]
où $\mathcal J=t\underline O_{\widehat X}$ est un idéal de définition de $\widehat X$.
\margin{27}
'''
e=[('margin note','upper right','9'),('text','top','Posons'),('display','2.5','S=gr_J O_X′=coprod J^k/J^(k+1)'),('display','2.6','gr_J(F)=coprod J^kF/J^(k+1)F'),('display','2.7','K^i=R^if_*(gr_J(F))'),('text','after 2.7','il est clair que K^i est muni'),('text','theorem 2.1','Supposons que K^i soit un S-Module gradué'),('text','item i','R^nf_*(F) est cohérent'),('text','item ii','l’homomorphisme ψ_n (2.3)'),('insertion','within topologique','l'),('insertion','between ii and iii','La filtration naturelle du deuxième membre'),('text','item iii','le système projectif des R^nf_*(F_k)'),('text','proof reference','La démonstration est très facile'),('insertion','above proof reference','cf. E.G.A. III 3.4.2.'),('text','proof correction introduction','à condition de rectifier comme suit le texte page 78'),('text','correction heading','Supprimer'),('text','correction line 6','et (R^(n+1)T(A_k))_(k∈Z)'),('text','correction line 13','et p+q=n+1'),('text','correction line 23','et pour n+1'),('text','theorem 2.2','Soit A un anneau adique noethérien'),('insertion','left margin after A','Soit T une partie fermée de X′=Spec(A)'),('text','theorem 2.2 continuation','Supposons que I soit engendré'),('insertion','between (1.31) and (1.32)','comma'),('display','2.8','F_0=F/JF'),('text','bottom','où J=t O_hat X est un idéal de définition'),('margin note','bottom left','27')]
save(28,s,e,sheet_kind='reused_typed',observations='All three supplied images and formula/insertion/end crops inspected. Coproduct-shaped marks are rendered as coproducts, without replacing them by expected sums. N and Z have two visibly separate underlines; module letters have their source underlines. The handwritten homomorphism symbol is tentatively psi with varphi alternative. The insertion after topologique says J-bonne. Formula-label overtyping remains doubtful. All three quoted deletion instructions are live text describing proposed corrections; they are not themselves encoded as struck-through source.')
