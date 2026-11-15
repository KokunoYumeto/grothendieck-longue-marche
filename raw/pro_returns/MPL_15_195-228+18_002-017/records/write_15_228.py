from record_page import save
save(15,228,'reused_typed',r'''
\mspage{227}
\begin{center}-- 5 --\end{center}\hfill n\textsuperscript{o}370

On définit de manière analogue les mesures invariantes, relativement invariantes et quasi-invariantes par $G$ sur $X$. Si $\mu$ est relativement invariante, on définit son multiplicateur $\chi$ par les formules
\[
\begin{array}{ll}
(7')&\delta(s)\mu=\chi(s)\mu\\
(8')&\displaystyle\int_X f(xs)d\mu(x)=\chi(s)^{-1}\int_X f(x)d\mu(x)\\
(9')&\mu(As)=\chi(s)\mu(A).
\end{array}
\]
Si on considère le groupe opposé $G^\circ$ à $G$ comme opérant dans $X$ par $(x,s)\longrightarrow xs$, $\mu$ est relativement invariante par $G^\circ$ de même multiplicateur $\chi$.

Soit enfin $G$ un groupe localement compact. Il opère sur lui-même par translations à gauche et à droite, suivant les formules $\gamma(s)x=sx$, $\delta(s)x=xs^{-1}$. Tout ce qui précède est applicable, et on a donc, sur $G$, les notions de mesures \uline{invariantes à gauche}, \uline{invariantes à droite}, \uline{relativement invariantes à gauche}, \uline{relativement invariantes à droite}, \uline{quasi-invariantes à gauche}, \uline{quasi-invariantes à droite} (cf., toutefois, les n\textsuperscript{os} 6 et 9).

L'application $x\longrightarrow x^{-1}$ est un homéomorphisme de $G$ sur $G$. Pour toute fonction $f$ sur $G$, on définira la fonction $\check f$ sur $G$ par
\[
(10)\qquad\check f(x)=f(x^{-1}).
\]
Pour toute mesure $\mu$ sur $G$, on définira la mesure $\check\mu$ par
\[
(11)\qquad\check\mu(f)=\mu(\check f)\qquad\text{pour }f\in\mathcal K(G).
\]
Autrement dit
\[
(12)\qquad\int_G f(x)d\check\mu(x)=\int_G f(x^{-1})d\mu(x)
\]
Si $A$ est un ensemble $\check\mu$-intégrable, $A^{-1}$ est $\mu$-intégrable, et
\[
(13)\qquad\check\mu(A)=\mu(A^{-1}).
\]
''',[
('text','sheet edge','227'),('text','typed header','–5–; n°370'),
('text','upper','On définit de manière analogue'),
('display','upper middle','(7′)–(9′), multiplier χ'),
('text','middle','Si on considère le groupe opposé'),
('text','middle','Soit enfin G un groupe localement compact'),
('text','lower middle','L’application x→x⁻¹'),
('display','lower middle','(10) check f(x)=f(x⁻¹)'),
('text','lower','Pour toute mesure μ'),
('display','lower','(11) check μ(f)=μ(check f)'),
('text','lower','Autrement dit'),
('display','lower','(12) integrals'),
('text','bottom','Si A est un ensemble check μ-intégrable'),
('display','bottom','(13) check μ(A)=μ(A⁻¹)')
], 'Whole reused typescript and both halves read after rotation; check accents, primes and multiplier signs checked.')
