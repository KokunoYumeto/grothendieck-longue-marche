import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(36,r"""\scanpage{36}
\uline{Groupes formels}

\textcircled{I} Extension d'un $p$-divisible par un lisse (\unsure{ou unipotent}) est triviale

\uline{Cor} Extension d'un $p$-divisible a-torique par un lisse (\unsure{ou unipotent})
est un \deleted{\unsure{extension}} \inserted{produit}

[Tout \unsure{sous-groupe} $p$-divisible a-torique est central

Tout groupe quotient \inserted{$p$-div.} a-torique est abélien avec un
plus grand sous-groupe $p$-divisible a-torique
--- qui est néc. central $\ldots$

\unsure{formuler} sort des \deleted{\unsure{plus}} grds sous-gps $p$-divisibles
a-toriques :
$\left\{\begin{array}{l}
\text{existe}\\
\text{stabilité par ext. corps de base}\\
\text{inclusion, sous sous-groupes}\\
\text{$p$-div$^{\mathrm{les}}$, sous groupes quotients}
\end{array}\right.$

\uline{NB} Pour qu'un grp. formel soit a-torique il faut,
\unsure{que la repr. lin. soit} \unsure{unipotente}.]

\uline{Rem} $(G_{\mathrm{ab}})/\operatorname{Im}\unsure{\delta|d}=\pi_0$ n'a pas de partie a-torique i.e. est \uline{linéaire}.

\margin{\unsure{résulte aussitôt du} \unsure{fait que} $\unsure{(G/R)_{\mathrm{ab}}|G/R}\unsure{\simeq|\to}G/R$ \unsure{est linéaire}. \uline{NB} \unsure{Centre} $(G/\operatorname{Cent}G)$ est quasi unipotent}

\textcircled{II} Extension d'un groupe formel [lisse] par un $p$-divisible est
\inserted{[si $G$ lisse]} \deleted{\unsure{triviale}} un produit --- à isogén. près du moins$\ldots$

\uline{Cor} $DG\cap Z(G)$ est \unsure{quasi-unipotent} i.e. annulé par une
puiss. de $p$. [Même, \deleted{$\unsure{G|Z(G)}$} $\operatorname{Cent}(\operatorname{Dér}G)$ est quasi-unip.$^{\unsure{\times}}$]

[\uline{Dire} soit \deleted{\unsure{ainsi}} $T$ \inserted{la partie} $p$-divisible de \deleted{$\unsure{\operatorname{Cent}G|Z(G)}$} \inserted{$\operatorname{Cent}\operatorname{Dér}G$}, \deleted{alors} \inserted{elle se \unsure{trouve} \unsure{dans $Z(G)$}}
\[
G\simeq\unsure{T'|T}\times G/T\inserted{\unsure{\phantom{T}'}}\quad
\text{donc}\quad DG\cap T=\{e\}
\]
]

\uline{Cor} $G$ (lisse) est \deleted{\unsure{produit}} \inserted{(isogénie)} de la pure partie a-torique par un \unsure{fibré}$\ldots$?

\uline{Question} $DG\cap Z(G)$ est-il \unsure{un} unipotent, i.e.
un \unsure{contenu} par du $H_p$ (\unsure{dans la th. de cls}) ?

\uline{Structure}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
 & & L_1\arrow[r,"d"]&L_0\arrow[dr]& &\\
1\arrow[r]&\pi_1\arrow[ur]\arrow[dr]& & &\pi_0\arrow[r]&1\\
 & &D_1\arrow[r,dash,"\delta"]&D_0\arrow[ur]\arrow[d,"\theta"]&&\\
 & & & {[\operatorname{Aut}D_1]}&&
\end{tikzcd}}

\[
p^\infty\pi_1=e\qquad \operatorname{at}(\pi_0)=\{e\}
\]
\[
\left\{\begin{array}{ll}
L_1=Z(G),&D_1=D(G),\\
L_0=G/Z(G),&D_0=G/D(G),\\
\pi_1=L_1\cap D_1,&\pi_0=G/L_1D_1
\end{array}\right.
\qquad
\left\{\begin{array}{l}
D_1^{D_0}=\pi_1\\
\unsure{D_{1\,D_0}|(D_1)_{D_0}}=\{e\}
\end{array}\right.
\]

\unsure{se reconstruit} à partir
\[
\pi_1,\quad \operatorname{Im}d\times\operatorname{Im}\delta,\quad \pi_0
\]
\[
D'=D_1\amalg_{\pi_1}L_1\qquad L'=L_0\times_{\pi_0}D_0
\]
\margin{\uline{NB} $\operatorname{Im}\delta\simeq\widehat H$\quad $H$ grp. alg. canonique mod. is. \unsure{étale}}

[obstruction nulle dans $H^3(\pi_0,\pi_1)$

indétermination dans $H^2(\pi_0,\pi_1)$]

Traiter cas $\pi_0$ $p$-divisible (plus gén., description des
\unsure{fibres} \unsure{groupes} de $G$ \unsure{images inverses} de $p^\infty\pi_0$

\uline{Dire quels sont les} $L_1\xrightarrow{d}L_0$ possibles
$(D_1\xrightarrow{\delta}D_0,\theta)$ ---
\margin{(\deleted{\unsure{détermination}} \inserted{Conditions sur $\pi_1,\pi_0$} \unsure{\ldots})
$\unsure{(\ker\delta)^{D_0}|(\ker\delta)}=\pi_1$,
$\unsure{(\ker\delta)_{D_0}}\simeq\{0\}$}

\margin{\unsure{NB}}
\uline{Condition pour que} $G$ soit linéaire
\inserted{\unsure{DG div. comm. et algébrisable}$\ldots$}
\mspage{35}
""",'text',[('heading','top','Groupes formels'),('text','upper','I Extension d’un p-divisible'),('text','upper','Cor Extension d’un p-divisible a-torique'),('text','upper-middle','Tout sous-groupe'),('text','upper-middle','formuler sort des plus grands'),('marginalia','left sideways','résulte aussitôt'),('text','middle','NB Pour qu’un grp. formel'),('text','middle','Rem G ab / Im delta'),('text','middle','II Extension d’un groupe formel'),('text','middle','Cor DG intersection Z(G)'),('display','middle','G isomorphic T times G/T'),('text','middle-lower','Cor G lisse'),('text','middle-lower','Question DG intersection Z(G)'),('diagram','lower-middle','Structure L1 to L0 and D1 to D0'),('display','lower-left','p infinity pi1 = e'),('display','lower-right box','L1 = Z(G)'),('display','lower-right','D1 D0 = pi1'),('display','lower','pi1 Imd times Imdelta pi0'),('display','lower','D prime D1 coproduct L1'),('marginalia','lower-right','NB Imdelta H'),('text','lower','obstruction nulle dans H3'),('text','bottom','Traiter cas pi0 p-divisible'),('text','bottom','Dire quels sont les'),('marginalia','bottom-right','Conditions sur pi1 pi0'),('text','bottom edge','Condition pour que G soit linéaire'),('marginalia','bottom-left','35')],doubts=[('whole page','Grey and blue ink on ruled music paper','Several grey additions overlap staff lines; two visual contrast enlargements were used. Uncertain whole phrases are marked rather than silently reconstructed.','low'),('central bracket','p-divisible part and T notation','The primes and interlinear note are faint and overwritten; no structural conclusion has been used to complete them.','low'),('bottom-right','ker delta formulas','Arrows and overwritten strokes obstruct both the operation and indices.','low')],observations='Dense formal-group research agenda: extensions involving p-divisible and lisse groups; a-torique terms; DG and Z(G); central/derived structural diagram with pi1 and pi0; obstruction H3 and indeterminacy H2; questions about linearity. Many assertions are terse and qualified by isogeny or questions; later research should separate them carefully. No modern theory used to disambiguate ink.')
