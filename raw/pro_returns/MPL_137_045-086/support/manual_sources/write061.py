import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
s=r'''\scanpage{61}
% archive foliation: 60
et est $\Sigma$-exacte

(Variante : si $L\xrightarrow{u}M$ \deleted{est un $\Sigma$-épi},
\deleted{\unsure{dont le noyau}}
$\operatorname{Hom}(\Phi^i,u)$ sont épi $\forall i$ (i.e. $u_i:L_i\unsure{-|\longrightarrow}M_i$
épi) alors $u$ \deleted{\unsure{d'ailleurs}} admet un noyau
(donc on a une suite $\Sigma$-exacte
\[
0\unsure{-|\longrightarrow}P\unsure{-|\longrightarrow}L\unsure{-|\longrightarrow}M\longrightarrow0\qquad).
\]
Utilisant ceci, on construit des objets
de $\mathcal P$ par ext. successives d'objets
$(\Psi_{\unsure{k}}^i)^{\unsure{r_i}}$ --- et on voit que $L\longmapsto L_\bullet=
\operatorname{Hom}(\Phi^\bullet,L)$ est \unsure{ess.} surjectif.

e) Tout objet de $\mathcal P$ est extension successive
d'objets de la forme $\Psi^i$ [qu'on peut
supposer \unsure{se succéder} par \unsure{ordre} croissant, dans
une filtration croissante \deleted{\unsure{de $\mathcal P$}}\inserted{\unsure{d'un objet} $L$},
laquelle sera alors canonique.]

\unsure{Je dois|Il doit} y avoir assez maintenant
pour conclure que le foncteur
$L\longmapsto L_\bullet=\operatorname{Hom}(\Phi^\bullet,L)$ est pl. fid. et
a l'image essentielle les $L_\bullet$ tels
que les $L_i,Z_i,B_i,H_i$ soient libres \unsure{t.f.}
et \inserted{$L_i$} nuls sauf un nb fini.
'''
e=[('text','top','et est Sigma-exacte'),('text','upper','Variante si L ->M'),('deletion','upper first line','est un Sigma-épi'),('deletion','upper second line','dont le noyau'),('deletion','upper third line','d’ailleurs'),('display','upper','0 - P - L - M ->0'),('text','middle','Utilisant ceci on construit'),('text','middle lower','e) Tout objet de P'),('deletion','inside e)','de P'),('insertion','inside e) above line','d’un objet L'),('text','lower','Je dois y avoir assez maintenant'),('insertion','last line','L_i')]
save(61,s,e)
