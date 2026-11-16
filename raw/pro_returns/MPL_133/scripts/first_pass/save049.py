import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(49,r"""\scanpage{49}
\mspage{3}
\diagram{\begin{tikzcd}
1\arrow[r,dash]&\pi_1\arrow[r,dash]&E\arrow[r,dash]&\pi_0\arrow[r,dash]&1
\end{tikzcd}}

Les autom intérieurs de $E$ sont l'identité sur
$\pi_0$ et $\pi_1$, donc définissent des hom $\pi_0-\pi_1$,
et on trouve ainsi un accouplement
\[
c_E=c_{G,G_1}:\quad\pi_0\times\pi_0\longrightarrow\pi_1
\]
(associant à $x,y\in\pi_0$ : $\bar{x}\bar{y}\bar{x}^{-1}\bar{y}^{-1}$ \inserted{$\in\pi_1$}; où $\bar{x},\bar{y}$ relèvent
$x$ et $y$) C'est une forme alternée, nulle ssi
l'extension $E$ est commutative. On doit
trouver, au \uline{signe} près
\[
\psi_{G_1}=\psi_G+\deleted{\unsure{\beta}}\widetilde c_E\alpha.
\]
où $\widetilde c_E:\pi_0\longrightarrow\uline{\operatorname{Hom}}(\pi_0,\pi_1)$ est défini de façon
évidente par $c_E$ (choix de la droite ou la \uline{gauche}
correspondant au \deleted{\unsure{choix}}\inserted{changement} d'un \uline{signe} !), $\alpha$
l'hom de passage au quotient
\diagram{\begin{tikzcd}
\zeta\arrow[r,dash]\arrow[rr,bend right=30,"\alpha"']&M\arrow[r,dash]&\pi_0
\end{tikzcd}}

\deleted{$\beta:\uline{\operatorname{Hom}}(\pi_0,\pi_1)\longrightarrow\uline{\operatorname{Hom}}(\pi_0,N')$
déduit de l'inclusion $\pi_1\hookrightarrow N'$.}
Il faut donc
se borner aux $G_1$ i.e. aux $E$ pour lesquels
$c_E$ est tel que
\[
\psi_G+\deleted{\unsure{\beta}}\widetilde c_E\alpha:\zeta\longrightarrow\uline{\operatorname{Hom}}(\pi_0,\pi_1)
\]
soit injectif.

\deleted{On peut simplifier encore cette condition,
en notant \deleted{\unsure{ici}} que la composée
\diagram{\begin{tikzcd}[column sep=small]
\zeta\arrow[r,"\psi_{G_1}"]&\uline{\operatorname{Hom}}(\pi_0,N')\arrow[r,dash]&\uline{\operatorname{Hom}}(\pi_0,N'/\pi_1)
\end{tikzcd}}
ne dépend pas du choix de $G_1$ : c'est}

\margin{\uline{NB} on suppose $\pi_0$ commutatif ?!\par
\unsure{Que faire} sinon ? Regarder l'image $\pi_0^*$ de $\zeta$ dans $\pi_0$, invariant et central\par
on trouve $\pi_0^*\times\pi_0\longrightarrow\pi_1$}
\mspage{48}
""",'text',[
('text','top folio','3'),('diagram','top','1,pi_1,E,pi_0,1'),('text','upper third','Les autom intérieurs de E'),('display','upper third','c_E=c_G,G1'),('text','upper middle','associant à x,y'),('insertion','above commutator','in pi_1'),('display','middle','psi_G1=psi_G+...'),('deletion','before c tilde','beta'),('text','middle','où c tilde_E'),('deletion','change of sign parenthesis','choix'),('insertion','same parenthesis','changement'),('diagram','below fold','zeta,M,pi_0;alpha'),('deletion','lower middle','beta:Hom to Hom;déduit'),('text','lower middle','Il faut donc se borner'),('display','lower third','psi_G+c tilde_E alpha'),('deletion','bottom paragraph and diagram','On peut simplifier encore'),('diagram','inside cancelled bottom paragraph','zeta,Hom(pi_0,N prime),Hom(pi_0,N prime/pi_1)'),('margin note','left oblique','NB on suppose pi_0 commutatif'),('text','bottom folio','48')],doubts=[('left margin','Que faire sinon?','First two words in the margin uncertain; pi_0 commutatif?! is clearly a qualification','medium'),('sign parenthesis','choix de la droite ou la gauche','The small article before droite is faint; source phrasing retained','medium')],observations='Variation of psi under central extension; au signe près; left margin explicitly questions the assumption pi_0 commutative. Final proposed simplification withdrawn with diagonal cancellation.')
