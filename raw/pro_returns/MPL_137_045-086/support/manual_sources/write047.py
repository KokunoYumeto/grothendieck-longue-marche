import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{47}
% archive foliation: 46
\[
\alpha_*(C_\bullet^i)\simeq DP(C_\bullet^i)\simeq\bigwedge^{i+1}\Phi_*
\]
\[
(\text{d'où}\qquad \alpha^*(C_i^\bullet)\simeq DP(C_i^\bullet)\simeq\bigwedge^{i+1}\Phi^*\quad)
\]
\deleted{\unsure{L'obj. déf.} de $\alpha(C_\bullet^i)$ est \unsure{l'image} de $\unsure{T}_{*\wedge}$
par le foncteur $ND:K_*\longrightarrow K_\bullet$ \unsure{donné} \unsure{can.}
de $(\bigwedge^{\geqslant1})\unsure{\Phi}_*$.}
\deleted{\unsure{Par suite}}
\deleted{\uline{Cor. 1} Le foncteur $DP:Ab_{k\bullet}\longrightarrow\unsure{Ab}$}

Appliquant la théorie de Dold-Puppe à $K$
\deleted{(qui est bien additive et stable par facteurs
directs, au moins si $k$ est principal, p.ex.
$k=\mathbf Z$)} on trouve dans $K$ un complexe
\[
\deleted{\unsure{C}}\qquad C^*=DP(C^\bullet)
\]
(\unsure{qu'on} \deleted{\unsure{pourra}} \unsure{a donc défini} dans \deleted{$\unsure{K}$} $K(k)$ \unsure{quelque}
\unsure{part soit} $k$), d'où pour les $B$ $k$-additives
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\underline{\operatorname{Hom}}_{k\text{-lin}}(K,B)\arrow[d,"\simeq"',"\mathrm{rest}"]
\arrow[ddr,bend left=18,"F\longmapsto F(C^*)"]&\\
\underline{\operatorname{Hom}}_{k\text{-lin}}(\unsure{A},B)\arrow[d,"\simeq"',"F\longmapsto F(C^\bullet)"]&\\
B^\bullet\arrow[r,"DP",hook]&B^*
\end{tikzcd}}
donc un foncteur $F\longmapsto F(C^*)$ qui est pl. fid.
Si $B$ est karoubienne, $DP_B$ est une équivalence,
donc aussi $F\longmapsto F(C^*)$. Donc
$C^*$ apparait comme objet simplicial \uline{universel}
dans cat. $k$-additive karoubienne.

\uline{Prop 5} Si $B$ est $k$-additive karoubienne, alors
$F\longmapsto F(C^*)$ est une équivalence
\[
\underline{\operatorname{Hom}}_{k\text{-lin}}(K,B)\longrightarrow B^*.
\]
(On a un \unsure{sens} canoniquement \inserted{\unsure{bif. de}}
$F\in\operatorname{Ob}\underline{\operatorname{Hom}}_{k\text{-lin}}(K,B)$ et $x\in\operatorname{Ob}K$.
'''
save(47,text,[('display','top','alpha_*(C_i)'),('display','second line','d’où alpha^*(C_i)'),('deletion','upper quarter','L’obj. déf. de alpha'),('deletion','upper quarter','Par suite'),('deletion','upper quarter','Cor. 1 Le foncteur DP'),('text','upper middle','Appliquant la théorie'),('deletion','parenthesis upper middle','qui est bien additive'),('display','middle','C^*=DP(C^•)'),('deletion','left of display','C'),('text','middle parenthesis','qu’on a donc défini'),('deletion','within parenthesis','pourra'),('deletion','before K(k)','K'),('diagram','middle lower','Hom(K,B) Hom(A,B) B^• B^*'),('text','below diagram','donc un foncteur'),('text','lower quarter','Prop 5 Si B'),('display','lower quarter','Hom(K,B) → B^*'),('text','bottom','On a un sens canoniquement'),('insertion','above bottom line','bif. de')])
