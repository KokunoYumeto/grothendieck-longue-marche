import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{\unsure{3|7}}
En résumé, on trouve

\uline{Prop.} Pour que $\Psi:W_{\mathrm{cof}}^{-1}C_{\mathrm{cof}}\longrightarrow W^{-1}C$ soit une équiv. de cat., il f. et s. que la condition suivante soit vérifiée :

$(\unsure{*})$ Pour \deleted{tout} diagramme
\diagram{\begin{tikzcd}x \arrow[r,shift left=.65ex,"\varphi"] \arrow[r,shift right=.65ex,"\psi"'] & y \arrow[r,"f","\sim"'] & y'\end{tikzcd}}
où $f\varphi=f\psi$, $f\in W$, $x,y\in C_{\mathrm{cof}}$ \inserted{(d'où $[\varphi]=[\psi]$ dans $W^{-1}C$)}, on a $[\varphi]=[\psi]$ dans $W_{\mathrm{cof}}^{-1}C_{\mathrm{cof}}$.

(condition impliquée par celle que $\Psi$ soit \uline{fidèle})

Nous allons travailler maintenant avec $C_{\mathrm{cof}}$ au lieu de $C$. -- donc quitte à changer de notations, on va supposer que tt objet de $C$ est cofibrant.

[\uline{NB} $C_{\mathrm{cof}}$ avec les notions induites par $W$ et cof est encore une catégorie \unsure{C1 : C3}], l'inclusion de $C_{\mathrm{cof}}$ dans $C$ commute aux sommes amalgamées \deleted{\unsure{qui}} relatives à des diagrammes
\diagram{\begin{tikzcd}a \arrow[r,"f"] \arrow[d,"g"'] & b\\ c &\end{tikzcd}}
tels que $f$ ou $g$ soit dans cof (les seules sommes dont on postule l'existence !).]

Soit, pour $x,y$ dans $C$,
\[
\uline{\mathrm{Ch}}_0(x,y)=\text{catégorie des diagrammes}
\]
\diagram{\begin{tikzcd}x \arrow[dr,"f"'] & y \arrow[d,"i","\sim"']\\ &\bar y\end{tikzcd}}
où $i\in W\cap\mathrm{cof}$ \deleted{\unsure{i.e.}} (\unsure{équi. faible couniverselle}\inserted{si $\mathrm{cof}=\mathrm{cof}_W$}). On définit des accouplements
\[
\uline{\mathrm{Ch}}_0(x,y)\times\uline{\mathrm{Ch}}_0(y,z)\longrightarrow\uline{\mathrm{Ch}}_0(x,z),\quad (F,G)\longmapsto G\mathbin{\cdot}F
\]
par
\diagram{\begin{tikzcd}
\unsure{x|a} \arrow[dr,"f"',"\deleted{\unsure{\varphi}}"] & y \arrow[d,hook,"i","\sim"'] \arrow[dr,"g"] & z \arrow[d,hook,"j","\sim"']\\
& \bar y \arrow[dr,"g'"',"\text{cocart}"] & \bar z \arrow[d,hook,"\unsure{k}","\sim"']\\
&&\bar z'
\end{tikzcd}}
\deleted{$\unsure{g'f}$}
\[
(g,j)\mathbin{\circ}(f,i)=(\unsure{g'g|g'f})\mathbin{\cdot}\unsure{kj}.
\]
\mspage{5}
"""
elements=[('text','top left','3 / 7'),('text','top','En résumé, on trouve'),('text','upper','Prop. Pour que Psi'),('text','upper middle','(*) Pour tout diagramme'),('diagram','upper right','x parallel phi psi y weak f y-prime'),('text','under diagram','où f phi=f psi; x,y en C_cof; [phi]=[psi]'),('text','upper middle','condition impliquée par celle que Psi soit fidèle'),('text','middle','Nous allons travailler maintenant'),('text','middle lower, bracketed NB','C_cof avec les notions induites'),('diagram','right middle','a f b, a g c'),('text','below','tels que f ou g soit dans cof'),('text','lower','Soit pour x,y dans C'),('display','lower','Ch_0(x,y)=catégorie des diagrammes'),('diagram','lower right','x f bar-y; y i bar-y'),('text','lower','où i en W cap cof'),('text','lower','On définit des accouplements'),('display','lower','Ch_0(x,y) times Ch_0(y,z) -> Ch_0(x,z)'),('text','above bottom diagram','par'),('diagram','bottom','x y z bar-y bar-z bar-z-prime; cocart'),('display','bottom right','(g,j) circle (f,i)'),('text','foot left','5')]
notes='''The proposition makes the conditional lemma of 106/002 an explicit necessary-and-sufficient criterion for Ψ to be an equivalence; the parenthesis says it is implied by Ψ being faithful. The bracketed NB asserts without detailed proof that the cofibrant subcategory satisfies C1–C3 and that its inclusion preserves the designated amalgamated sums. The definition of Ch_0 and its composition uses a cocartesian construction; follow later pages for associativity and localization claims. The final compositional formula is graphically doubtful and is not corrected from the expected composite.'''
if __name__=='__main__':save(106,6,tex,elements,notes=notes)
