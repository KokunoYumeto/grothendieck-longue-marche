import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{51}

\uline{Lemme 1}\quad Soit $k$ un corps algébriquement clos, $K$ une extension de type fini, de degré de transcendance $1$, de $k$. Alors $K$ est \deleted{\unsure{alg.}} quasi-algébriquement clos
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0)--(-.04,1.5);\end{tikzpicture}}

\uline{Corollaire 1}\quad $\widehat H^i(K^{\unsure{a|'}},G_m)=0$ pour tout $i$

En effet, $K$ est une extension galoisienne \unsure{un|d'un} $K'$ est quasi-alg. clos, donc \deleted{$\unsure{\widehat H^i(K,G)}$} la conclusion est bien connue.

\uline{Corollaire 2}\quad $\unsure{\widehat H}^i(K,\Gamma)=0$ \deleted{$i>0$ pour} \inserted{pour tt $i>1$ et} tout groupe abélien fini $\Gamma$ où $G_K$ opère trivialement.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0)--(-.02,.7);\end{tikzpicture}}

Soit en effet $\widetilde K$ \deleted{la} \inserted{une} clôture galoisienne de $K$,
$[U\subset\widetilde K^*$ \unsure{le} groupe des racines de l'unité dans $\widetilde K$.
Alors $\widetilde K^*/U$ est uniquement divisible sauf pour $p$ (exposant car.) d'où la suite exacte \uline{mod} $p$
\[
\widehat H^i(K,\unsure{U_m|G_m})\xrightarrow{\sim}\widehat H^i(K,G_m)\deleted{\text{\unsure{mod}}\ p}\qquad\uuline{\text{mod }p}
\]
\margin{est-ce $\simeq$ un vrai isomorphisme?}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[->,line width=.7pt] (1,0)--(0,0);\end{tikzpicture}}
Or le \deleted{premier} deuxième mb. est nul, donc le premier l'est, donc comme le premier \deleted{\unsure{n'a que}} a $p$-composante nulle, il est nul.$]$
On \deleted{\unsure{en déduit}} \inserted{\deleted{peut} voit} plus précisément que si $n$ est premier à la caractéristique, alors
\diagram{\begin{tikzcd}\widetilde K\arrow[r,"x\to x^n"]&\widetilde K^{\unsure{n}}\end{tikzcd}}
est un épimorphisme de \deleted{groupe de} noyau $\simeq\mathbb Z/n$, donc la suite exacte de cohomologie donne le résultat $H^i(K,\unsure{\mathbb Z_n|\mathbb Z/n})=0$.

Reste à prouver $H^i(K,\mathbb Z/p)=0$ si $i>1$. Pour ceci
\deleted{\uline{Lemme 2} Soit}
on considère la suite exacte
\diagram{\begin{tikzcd}0\arrow[r]&\unsure{\mathbb Z}/p\arrow[r,no head]&\widetilde K\arrow[r,"\wp"]&\unsure{\widetilde K'|\widetilde K}\arrow[r]&0\end{tikzcd}}.

\mspage{50}'''
e=[('text','top','Lemme 1; Soit k un corps algébriquement clos'),('deletion','lemma conclusion','alg.'),('drawing','left of lemma','vertical emphasis stroke'),('text','upper','Corollaire 1'),('display','upper','Hhat^i(K^a,G_m)=0 pour tout i'),('text','upper','En effet, K est une extension galoisienne'),('deletion','upper proof','Hhat^i(K,G)'),('text','upper middle','Corollaire 2'),('display','upper middle','Hhat^i(K,Γ)=0'),('deletion','corollary 2 condition','i>0 pour'),('insertion','above condition','pour tt i>1 et'),('text','corollary 2 conclusion','tout groupe abélien fini Γ où G_K opère trivialement'),('drawing','left of corollary 2','short vertical stroke'),('text','middle','Soit en effet Ktilde'),('deletion','before clôture','la'),('insertion','above clôture','une'),('text','middle','[U ⊂ Ktilde* le groupe des racines'),('display','middle','U ⊂ Ktilde*; Ktilde*/U'),('text','middle','Alors ... uniquement divisible sauf pour p'),('text','middle lower','(exposant car.) d’où la suite exacte mod p'),('display','middle lower','Hhat^i(K,U_m) →~ Hhat^i(K,G_m)'),('deletion','after comparison map','mod p'),('text','right of comparison map','mod p doubly underlined'),('margin note','left of comparison map','est-ce ≃ un vrai isomorphisme?'),('drawing','between margin and comparison','left-pointing arrow'),('text','lower','Or le deuxième mb. est nul'),('deletion','lower','premier'),('deletion','lower','n’a que'),('text','lower','a p-composante nulle, il est nul.]'),('deletion','lower continuation','en déduit'),('insertion','above continuation','peut [deleted] voit'),('deletion','inside insertion','peut'),('text','lower','plus précisément que si n est premier'),('diagram','lower','Ktilde →^(x→x^n) Ktilde^n'),('text','lower','est un épimorphisme ... noyau'),('deletion','lower','groupe de'),('display','lower','≃ Z/n; H^i(K,Z_n)=0'),('text','bottom','Reste à prouver ... Pour ceci'),('display','bottom','H^i(K,Z/p)=0 si i>1'),('deletion','bottom','Lemme 2 Soit'),('text','bottom','on considère la suite exacte'),('diagram','bottom','0 → Z/p — Ktilde →^wp Ktilde′ → 0'),('text','bottom left','50')]
save(51,text,e,observations='Whole, halves and six main crops read directly; additional high-zoom crops inspected for the overwritten cohomology coefficient, crossed formula, cancelled wording, power map and final exact sequence. The K superscript in Corollary 1 and the overwritten coefficient U_m/G_m remain uncertain. The source has a bare connector after Z/p in the last sequence; it is retained without an arrowhead. The final K has an apparent prime, explicitly marked as uncertain. The margin asks whether the displayed comparison is a true isomorphism. No continuation supplied.')
