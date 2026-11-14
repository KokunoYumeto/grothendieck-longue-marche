from record_page import save_page
save_page(120,23,r'''
\mspage{11}

En effet, c'est aussi l'ens des
\[
\{(x,y)\in R^2\mid xy=1,\ x\in A
\]
Si on suppose qu'il existe \deleted{$B\subset R^*$}, $B\in\mathcal M_1$, contenant l'ens \deleted{\unsure{des}} $\{x^{-1}\mid x\in A\}$, on \unsure{gagne}, car l'ens est la partie modérée de $A\times B$ image inverse de $1\in A.B$ \inserted{$=C\in\mathcal M_1$} par l'application modérée $(x,y)\mapsto xy$.

\uline{Cor} \uline{$R_0$ est un sous-corps de $R$}

\deleted{\unsure{Alors}}

Si $X$ modéré, $Y\subset X$ une partie modérée qui soit donnée comme dans M6 comme
\[
Y=\bigcap_{\alpha\in I} f_\alpha^{-1}(\{e_\alpha\})\qquad e_\alpha\in R,
\]
alors quitte à remplacer les $f_\alpha$ par $f_\alpha-e_\alpha$, \unsure{OPS} les $e_\alpha=0$, i.e. $Y$ est l'ens des \uline{zéros} communs à des $f_\alpha$.

Soient $(g_\beta)_{\beta\in J}$ \deleted{\unsure{des}} des fonctions \inserted{modérées} réalisant un plongement $X\subset R^J$. Considérons les $f_\alpha$, $f_\alpha g_\beta$ \deleted{\unsure{—}} elles sont toutes nulles sur $Y$, et

\mspage{22}
''',[
('text','top right','11'),
('text','top','En effet, c’est aussi l’ens des'),
('display','upper','{(x,y) ∈ R² | xy=1, x∈A'),
('text','upper middle','Si on suppose qu’il existe'),
('deletion','upper middle','B ⊂ R*'),
('deletion','upper middle','des'),
('insertion','right, below A.B','=C ∈ M₁'),
('text','middle','Cor R₀ est un sous-corps de R'),
('deletion','below Cor','Alors'),
('text','middle lower','Si X modéré, Y⊂X'),
('display','lower middle','Y=intersection fα⁻¹({eα}), eα∈R'),
('text','lower','alors quitte à remplacer'),
('text','bottom','Soient (gβ)β∈J'),
('deletion','bottom','des'),
('insertion','above réalisant','modérées'),
('deletion','bottom line','—'),
('text','bottom left','22')], observations='The upper set-builder has no closing brace visible. The proof invokes the boundedness of reciprocal values from the revised M11(c). The subsequent construction begins with the common-zero presentation in M6, then combines fα and fαgβ. No interpretation from external context has been used.')
