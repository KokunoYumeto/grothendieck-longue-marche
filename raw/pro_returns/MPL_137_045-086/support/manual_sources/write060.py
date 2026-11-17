import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
s=r'''\scanpage{60}
% archive foliation: 59
\unsure{Cela} signifie que l'on a une kyrielle de
suites $\Sigma$-exactes (donc exactes)
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
0\arrow[r,dash]&\Psi^0\arrow[r]&C^0\arrow[r,dash]&\Psi^1\arrow[r,dash]&0&&&\\
&&0\arrow[r,dash]&\Psi^1\arrow[r,dash]&C^1\arrow[r]&\Psi^2\arrow[r]&0&\\
&&&&0\arrow[r]&\Psi^2\arrow[r,dash]&C^2\arrow[r,dash]&\Psi^3\arrow[r,dash]&0\\
&&&&&&\cdots&&
\end{tikzcd}}
Par hyp on sait que
\[
\Psi_\bullet^i=k\text{ placé en dim }i
\]
On trouve aisément les \deleted{\unsure{$\operatorname{Hom}(\Phi$}}\inserted{hom} entre les
$C^i$, et \deleted{\unsure{$\operatorname{Hom}($ les}} $\Psi^j$
\margin{\unsure{résulte de}\quad\unsure{par a)}}
\[
C^i\unsure{-|\longrightarrow}\Psi^j,\quad\Psi^i\unsure{-|\longrightarrow}C^j,\quad
\Psi^i\longrightarrow\Psi^j\qquad(C^i\unsure{-|\longrightarrow}C^j\text{ déjà connus})
\]
on peut résumer la situation en
disant que sur la sous-cat. str. pleine
$\mathcal P_1\subset\mathcal P$ formée des objets isom. à des sommes
des $C^i$ et des $\Psi^{\unsure{i|j}}$, le foncteur $L\longmapsto L_\bullet=
\operatorname{Hom}(\Phi^\bullet,L)$ est pl. fidèle. Son image essentielle
est formée des complexes de chaînes $L_\bullet$
finis tels que les composantes \inserted{$L_i$, les $Z_i$ et les $B_i$}
\deleted{\unsure{$H_i(L)$}} soient libres de \unsure{t.f.|d.f.}

(On peut voir que le \deleted{\unsure{biplet}} $(\mathcal P_1,C^\bullet,\Psi^0,\varepsilon,\unsure{\Sigma\cap\mathcal P_1})$
est universel pour une cat. $k$-additive
munie d'une \uline{classe} $\Sigma$ de suites exactes et
d'une $\Sigma$-résolution d'un objet \deleted{$\Psi^0$} $Z^0$\ldots).

On va maintenant supposer de plus

d) Pour tte suite \inserted{$\Sigma$-}exacte de $\mathcal P$
\[
0\unsure{-|\longrightarrow}\unsure{L^\beta|L}\unsure{-|\longrightarrow}M\unsure{-|\longrightarrow}N\unsure{-|\longrightarrow}0
\]
\margin{il suffit de demander \unsure{l'une des deux propriétés}, par ex. \unsure{d)}}
et tout hom $L\unsure{-|\longrightarrow}L'$ (resp $N'\unsure{-|\longrightarrow}N$),
la suite \deleted{\unsure{nouvelle}} déduite par somme amalga-
mée (resp. produit fibré) existe dans $\mathcal P$
'''
e=[('text','top','Cela signifie que l’on a une kyrielle'),('diagram','upper','three Sigma-exact sequences Psi0 C0 Psi1'),('text','upper middle','Par hyp on sait que'),('display','upper middle','Psi^i = k placé en dim i'),('text','middle','On trouve aisément les hom'),('deletion','middle first line','Hom(Phi'),('insertion','above middle line','hom'),('deletion','middle second line','Hom( les'),('margin note','left middle','résulte de par a)'),('display','middle','C^i - Psi^j; Psi^i - C^j; Psi^i -> Psi^j'),('text','middle and lower','on peut résumer la situation'),('insertion','lower right','L_i les Z_i et les B_i'),('deletion','lower left','H_i(L)'),('text','lower','On peut voir que le'),('deletion','lower','biplet'),('deletion','lower right','Psi0 before Z0'),('text','lower','On va maintenant supposer de plus'),('text','bottom','d) Pour tte suite exacte'),('insertion','above d)','Sigma-'),('display','bottom','0 - L^beta - M - N -0'),('margin note','bottom left','il suffit de demander'),('text','bottom','et tout hom L-L prime'),('deletion','last lines','nouvelle')]
save(60,s,e)
