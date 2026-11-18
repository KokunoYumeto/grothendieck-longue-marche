import sys
sys.path.insert(0,'MPL_159/scripts')
from record_page import commit
commit(32,r'''\scanpage{32}
\[G\supset G_0\qquad C\supset C_0\]
$G$ gpe, $G_0$ ss-gpe, \deleted{\unsure{invariant}}

$C$ $G$-ens, $C_0$ sous-ens
\diagram{\begin{tikzcd}
G_0\times C_0\arrow[r,"\sim"] & C\\
(h,c)\arrow[r,mapsto] & h.c
\end{tikzcd}}
Soit $c\in C_0$, et soit
\[G(c)=\{g\in G\mid g.c\in C_0\}.\]
Alors $G(c)\xrightarrow{\sim}{}_{G_0}\backslash G\deleted{/G_0}$ i.e.

\deleted{En effet,}
\deleted{
\diagram{\begin{tikzcd}
G_0\times G(c)\arrow[r,"\sim"] & G\\
(h,g)\arrow[r,mapsto] & h.g
\end{tikzcd}}
En effet, si $hg=h'g'$, \quad $h,h'\in G_0$, $g,g'\in G(c)$,
\[
\underbrace{(h'^{-1}h)}_{h''}g=g'\quad\text{d'où}\quad
h''\underbrace{(gc)}_{\substack{\uparrow\\C_0}}=\underbrace{g'c}_{\substack{\uparrow\\C_0}}=1.\underbrace{(g'c)}_{\substack{\uparrow\\C_0}}
\]
donc $h''=1$ i.e. $h=h'$ et $g=g'$, d'où l'injectivité.
}
\margin{\unsure{Si}\ $\leftrightarrow$}
\margin{\uline{Cor} ${}_{G_0}\backslash C\simeq C_0$ (bij. ens abstraits).
\uline{Rem.} (\unsure{Si $G_0$ inv. dans $G$}) $G/G_0$ opère sur $C_0$, $C/G\simeq C_0/(G/G_0)$.}
Surjectivité: Soit $k\in G$, alors $kc\in C$ de la forme $h'c'$
($h'\in G_0$, $c'\in C_0$) donc $\underbrace{h'^{-1}k}_{g}c=c'$,
donc $h'^{-1}k=g\in G(c)$ donc
\[k=h'g,\quad h'\in G_0,\quad\uline{g\in G(c)}.\]
\unsure{Q.S.}\ \deleted{\unsure{Soit}} $g\in G$, $c\in C_0$, $gc=c\Longrightarrow g=1$ ?

\deleted{On aura $g\in G(c)$, $1\in\unsure{G}$}

Considérons une orbite de $G$ dans $C$, soit $G.x$, et considérons $O\cap C_0$. Alors
\[O\cap C_0\simeq\deleted{\unsure{C/}}{}_{G_0}\backslash G.\]
En effet, \unsure{si}
\[x=h.\hat c_0\quad(h\in G_0,\ c_0\in C_0,\text{uniques})\quad\text{donc}\]
\[\deleted{\unsure{nous}\ \unsure{\mathrm{WTS}}\ g\inserted{x}\in G_0\unsure{\longmapsto h}\quad g.h.c}\]
% archive foliation: 31
''',[
 ('display','upper left','G contains G_0; C contains C_0'),('text','top right','G gpe G_0 ss-gpe; C G-ens C_0 sous-ens'),('deletion','top right','invariant'),
 ('diagram','upper third','G_0 times C_0 isomorphic C, (h,c) maps h.c'),('text','upper middle','Soit c in C_0'),('display','upper middle','G(c)={g in G | gc in C_0}'),
 ('text','upper middle','Alors G(c) isomorphic left quotient'),('deletion','quotient after G','/G_0'),('deletion','middle left','En effet'),
 ('deletion','large central crossed block','G_0 times G(c) isomorphic G and injectivity proof'),('diagram','inside crossed block','(h,g) maps h.g'),
 ('display','inside crossed block','h inverse h times g; h second acting on gc'),('margin note','left central','Si and two-ended arrow'),
 ('margin note','right sloping','Cor G_0 quotient C isomorphic C_0; Rem quotient action'),
 ('text','lower middle','Surjectivité Soit k in G'),('display','lower middle','k=h prime g'),('text','lower quarter','Q.S. g in G gc=c implies g=1?'),
 ('deletion','question line','Soit'),('deletion','below question','On aura g in G(c), 1 in G'),
 ('text','bottom','Considérons une orbite de G dans C'),('display','bottom','O intersect C_0 isomorphic G_0 quotient G'),('deletion','orbit quotient','C/'),
 ('text','bottom','En effet si'),('display','bottom','x=h hat c_0'),('deletion','last line','nous WTS g x in G_0 maps h, g.h.c'),('insertion','last cancelled line','x')
],observations='Abstract group action argument with G_0 times C_0 mapping bijectively to C. Central injectivity proof is crossed through; surjectivity continues below. The freeness implication gc=c => g=1 is explicitly questioned, and the orbit quotient statement at the bottom is provisional. Sloping margin proposes a quotient corollary; some qualifiers remain uncertain.')
