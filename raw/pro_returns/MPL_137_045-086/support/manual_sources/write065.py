import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{65}
% archive foliation: 64
(\unsure{Ds.} la cat. dérivée) puisque $C^\bullet$ est une résolution $\Sigma$-injective de $\Psi^0$.

\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,0) .. controls (-.5,-.6) and (-1.3,-.2) .. (-.9,.1) .. controls (-.5,.25) and (.8,.12) .. (1.4,.24);\end{tikzpicture}}

Nous considérons maintenant les réalisations $\tfrac12$ simpliciales $P_*\supset Q_*\supset P_{0*}\supset K_*\ \unsure{\text{etc.}}$ de $P\supset Q\supset P_0\supset K$. Sur $P_*$ il y a la structure $\unsure{\otimes_*|\otimes_k}$ ou $\otimes_*$
($L_*\otimes_*M_*$ défini composante par composante
\[
(L_*\otimes M_*)_{[n]}=L_{[n]}\otimes M_{[n]}
\]
)
avec contraintes d'ass, unité ($\Psi^0$), et de comm, \inserted{\unsure{de bilinéar.}} \deleted{Il est quasi évident} \inserted{On note que $K_*$ est un} \deleted{(\unsure{bidirectionnel}) $P^*,Q^*$,} ``co-idéal'', \deleted{que $P_0$ est un \unsure{idéal}} \inserted{(i.e. si l'un des facteurs} $L_*,M_*$ est dans $K_*$, l'autre aussi), $P_0$ et $Q$ sont stables par $\otimes$, car

\margin{\deleted{$\unsure{K}$} \unsure{Il s'agit} de $\unsure{\Psi_*}$ \unsure{qui sont} \unsure{contractiles} (\unsure{dualité})}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\Psi^0_* \arrow[d,equal] & \otimes & \Psi^0_* \arrow[d,equal] & \simeq & \Psi^0_* \arrow[d,equal] & (\Rightarrow\text{ stabilité de }\unsure{P_0})\\
\mathbf1_* && \mathbf1_* && \mathbf1_*
\end{tikzcd}}

et
\[
\Psi^i_*\otimes\Psi^j_*\simeq\Psi^{i+j}_*+\text{élém de }K
\]
\[
(\Rightarrow\text{ stabilité de }\unsure{P_{1*}=Q})
\]

On transporte cette structure multiplicative sur $P$ et ses sous-catégories (notation $*$, pour éviter des confusions) et sur autres réalisations $P_\bullet$ et $P^*,P^\bullet$ (ces deux dernières contravariantes). On note $*$ sur $P_\bullet$ et $P^\bullet$, et $\unsure{\otimes|\mathbin{\circledast}}$ sur $P^*$, car l'équivalence $\vee$ de'''
e=[('text','top','(Ds. la cat. dérivée) puisque Cbullet'),('drawing','upper separator','looped horizontal pen stroke'),('text','upper third','Nous considérons maintenant les réalisations'),('display','middle','(L*⊗M*)[n]=L[n]⊗M[n]'),('text','middle','avec contraintes d’ass unité et de comm'),('insertion','middle','de bilinéar.'),('deletion','middle','Il est quasi évident'),('insertion','middle','On note que K* est un'),('deletion','middle','(bidirectionnel) P*,Q*'),('deletion','middle','que P0 est un idéal'),('insertion','middle','i.e. si l’un des facteurs'),('text','middle/lower','L*,M* est dans K*, l’autre aussi'),('margin note','left middle diagonal','Il s’agit de Ψ* qui sont contractiles'),('deletion','left margin','K'),('diagram','lower middle','Ψ0*⊗Ψ0*≃Ψ0*; vertical identifications 1*'),('display','lower third','Ψi*⊗Ψj*≃Ψi+j*+élém de K'),('display','lower third','⇒ stabilité de P1*=Q'),('text','bottom','On transporte cette structure multiplicative')]
save(65,text,e)
