import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{12}
\mspage{10}

3. \uline{Comportement par \deleted{\unsure{base}} $S$ variable}.

Soit
\[
(3.1)\qquad f:S'=\operatorname{Spec}(V')\longrightarrow S=\operatorname{Spec}V,
\]
un morphisme \uline{dominant} de traits, \deleted{Alors} donc $f(s')=s$, $f(\eta')=\eta$. La donnée d'une \deleted{extension} \inserted{clôture} séparable \deleted{\unsure{nous donne}} $\bar K'$ de $K'$ en définit une $\bar K$ de $K$, à savoir la clôture séparable de $K'$ dans l'extension $\bar K'$. Alors $\widetilde K$ est contenue dans $\widetilde K'$, et $\widetilde V$ dans $\widetilde V'$. L'hom d'inclusion $\widetilde V\hookrightarrow\widetilde V'$ définit ainsi un hom $\bar k\longrightarrow\bar k'$, correspondant à \deleted{l'hom} \inserted{un} diagramme commutatif de corps.

\diagram{\begin{tikzcd}
(3.2)\quad K'\arrow[r,no head]\arrow[d,no head]&\widetilde K'\arrow[r,no head]\arrow[d,no head]&\bar K'\arrow[d,no head]\\
K\arrow[r,no head]&\widetilde K\arrow[r,no head]&\bar K
\end{tikzcd}}
\diagram{\begin{tikzcd}
(3.3)\quad V'\arrow[r,no head]\arrow[d,no head]&\widetilde V'\arrow[d,no head]\\
V\arrow[r,no head]&\widetilde V
\end{tikzcd}}
\diagram{\begin{tikzcd}
(3.4)\quad k'\arrow[r,no head]\arrow[d,no head]&\bar k'\arrow[d,no head]\\
k\arrow[r,no head]&\bar k
\end{tikzcd}}

On trouve ainsi un diagramme commutatif d'extensions, induit par $\operatorname{Gal}(\bar K'/K)=\pi'\longrightarrow\operatorname{Gal}(\bar K/K')=\pi$ :
\diagram{\begin{tikzcd}
1\arrow[r,no head]&\unsure{I'|P'}\arrow[r,no head]\arrow[d]&\pi'\arrow[r,no head]\arrow[d,no head]&\pi'_0\arrow[r,no head]\arrow[d,no head]&1\\
(3.5)\quad1\arrow[r]&I\arrow[r,no head]&\pi\arrow[r]&\pi_0\arrow[r]&1
\end{tikzcd}}
L'hom $\pi'_0\longrightarrow\pi_0$ n'est autre que l'hom
\diagram{\begin{tikzcd}
(3.6)\quad\operatorname{Gal}(\bar k'/k')\arrow[r,no head]\arrow[d,equal]&\operatorname{Gal}(\bar k/k)\arrow[d,equal]\\
\pi'_0&\pi_0
\end{tikzcd}}
déduit de (3.4). L'hom $I'\mathrel{\text{---}}I$ s'insère de \unsure{même} dans un diagramme de suites exactes
\diagram{\begin{tikzcd}
1\arrow[r]&P'\arrow[r,no head]\arrow[d]&I'\arrow[r]\arrow[d]&I'_t\arrow[r,no head]\arrow[d,no head]&1\\
(3.7)\quad1\arrow[r,no head]&\unsure{p|P}\arrow[r,no head]&I\arrow[r,no head]&I_t\arrow[r,no head]&1
\end{tikzcd}}
\margin{11}
'''
e=[('text','heading','3 Comportement par S variable'),('deletion','heading','base'),('text','upper','Soit'),('display','upper','(3.1) f:S′=Spec(V′)→S=SpecV'),('text','upper-middle','un morphisme dominant de traits'),('deletion','after traits','Alors'),('deletion','after une','extension'),('insertion','above extension','clôture'),('deletion','before Kbar′','nous donne'),('deletion','after correspondant à','l’hom'),('insertion','above l’hom','un'),('diagram','middle left','(3.2) K′ Ktilde′ Kbar′ / K Ktilde Kbar'),('diagram','middle left lower','(3.3) V′ Vtilde′ / V Vtilde'),('diagram','middle beside 3.3','(3.4) k′ kbar′ / k kbar'),('text','middle-lower','On trouve ainsi un diagramme'),('display','middle-lower inline','Gal(Kbar′/K)=π′→Gal(Kbar/K′)=π'),('diagram','lower','(3.5) inertia extension rows'),('text','lower','L’hom π′₀→π₀'),('diagram','lower','(3.6) Gal residue extensions'),('text','bottom','déduit de (3.4) L’hom I′—I'),('diagram','bottom','(3.7) wild and tame inertia rows'),('margin note','bottom left','11')]
save_page(34,12,tex,e,remarks='The two Galois denominators in the line introducing (3.5) visibly read K and K′ respectively and have not been exchanged. The prose earlier also reads K′ in the separable-closure clause. The small field and ring diagrams have plain strokes without visible heads; the larger diagrams preserve the clearly visible arrowheads selectively. The first object after 1 in the upper row of (3.5) is overwritten and marked I′|P′.')
