import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(51,r"""\scanpage{51}
\deleted{clair sur la formule précédente donnant $\psi_{G_1}$ en
termes de $\widetilde c_E$, mais on peut définir cet hom
\[
\psi_0:\zeta\longrightarrow\operatorname{Hom}(\pi_0,N'/\pi_1)
\]
en termes des données de départ (I II \uline{III})
qui définissent en fait un groupe $K\simeq G/\pi_1$
ext. \inserted{centrale} de $M$ par $N'/\pi_1$, d'où comme précédemment
\[
M\longrightarrow\uline{\operatorname{Hom}}(\zeta,N'/\pi_1)
\]
se factorisant par $\pi_0$, i.e.
\[
\zeta\xrightarrow{\psi_0}\uline{\operatorname{Hom}}(\pi_0,N'/\pi_1).
\]
Soit $\zeta_0=\operatorname{Ker}\psi_0$}

\mspage{4}

\margin{\deleted{\diagram{\begin{tikzcd}[row sep=small]
\zeta\arrow[r,dash]\arrow[d,phantom,"\supset" description]&\deleted{\unsure{\pi_0}}\uline{\operatorname{Hom}}(\pi_0,\pi_1)\\
\zeta_0\arrow[ur]&
\end{tikzcd}}
$\pi_0^*=\zeta/\zeta_0\subset\pi_0$\par
$\pi_0^*\longleftrightarrow\uline{\operatorname{Hom}}(\pi_0,\pi_1)/\unsure{\zeta_0}$\quad\textcircled{inj}}}

\diagram{\begin{tikzcd}
\unsure{K}\arrow[r]&\Sigma\\
I\arrow[u]&
\end{tikzcd}}

On peut dévisser un peu plus en introduisant
\[
\zeta_0=\operatorname{Ker}(\zeta\longrightarrow\pi_0)
\]
\margin{$\begin{aligned}
&=\deleted{\unsure{\operatorname{Im}}}\ d(\operatorname{Cent}(N)\cap d^{-1}(\operatorname{Cent}M))\\
&=d(\operatorname{Cent}(N))\cap\operatorname{Cent}(M)\\
&\simeq\operatorname{Cent}(N)/\pi_1\cap\unsure{\operatorname{Cent}M}
\end{aligned}$}
et l'hom induit par $\psi_G$:
\[
\psi_{0\unsure{G}}:\zeta_0\longrightarrow\uline{\operatorname{Hom}}(\pi_0,\pi_1).
\]
\margin{?}
On trouve que la définition de celui-ci
ne dépend pas du choix de $G_1$, mais
\deleted{peut se faire en termes du groupe $H$
et $N,N'\subset H$ (construits par les données
I II III) Une condition préliminaire indépendante
de $G_1$ (i.e. de $E$) est que \textcircled{b} \uline{$\psi_0$ soit
injective}} --- cela exprime que $N'$ est \uline{égal}
au centre de $H$, $N'=\uline{\operatorname{Cent}}(H)$. Ceci
étant supposé acquis, \deleted{\unsure{pour}}\inserted{soit}
\margin{(annulé!)}
\mspage{50}
""",'text',[
('deletion','upper half diagonal cancellation','clair sur la formule précédente'),('display','cancelled upper paragraph','psi_0:zeta to Hom'),('insertion','cancelled paragraph','centrale'),('display','cancelled paragraph','M to Hom; zeta to Hom; zeta_0'),('text','right upper middle folio','4'),('margin note','left rotated cancelled diagram','zeta,zeta_0,Hom'),('diagram','left rotated cancelled diagram','zeta to Hom; zeta_0'),('deletion','left margin','diagram and pi_0 star formula'),('diagram','centre gap','I,K,Sigma'),('text','below fold','On peut dévisser un peu plus'),('display','below fold','zeta_0=Ker(zeta to pi_0)'),('margin note','right below fold','d(Cent(N) intersection d inverse CentM)'),('deletion','right margin','Im'),('text','lower third','et l’hom induit par psi_G'),('display','lower third','psi_0G:zeta_0 to Hom'),('margin note','left lower third','?'),('text','lower third','On trouve que la définition'),('deletion','bracketed lower paragraph','peut se faire; condition préliminaire'),('text','bottom','cela exprime que N prime est égal'),('insertion','bottom edge','soit'),('deletion','bottom edge','pour'),('margin note','left beside bracket','annulé!'),('text','bottom folio','50')],doubts=[('lower bracket cancellation','peut se faire ... injective','The bracket marked annulé! does not make its exact scope wholly certain; adjoining explanatory words remain transcribed','medium'),('rightmost formula','Cent M','Right edge clips part of last letters; no mathematical completion beyond marked reading','low'),('left cancelled scratch diagram','pi_0 star to Hom/pi_0','Uncertain quotient in a rotated overlapping cancellation; retained with doubt','low')],observations='Continuation of withdrawn simplification. New zeta_0=Ker(zeta to pi_0), question mark and annulé! attached to proposed invariant criterion; do not cite as an established theorem.')
