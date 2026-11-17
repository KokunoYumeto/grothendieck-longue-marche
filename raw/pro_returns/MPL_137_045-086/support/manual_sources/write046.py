import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{46}
% archive foliation: 45
\margin{\uline{NB} Le foncteur $DP^*$ \unsure{défini de façon} \unsure{fidèle} dans $B$ additive (\unsure{par les sommes}).}
\uline{Ex 3} La théorie de Dold-Puppe nous donne
une \deleted{\unsure{équivalence de catégories}} \inserted{équivalence de catégories}
(pour les catégories \deleted{$\unsure{Ab}_k^\bullet$} $Ab_k$ additives avec facteurs directs)
\margin{$ND={}$\unsure{non dégénéré}\\ $DP={}$\unsure{Dold-Puppe} \deleted{\unsure{catégorie de} $Ab$}}
\diagram{\begin{tikzcd}
B_\bullet \arrow[r,shift right=.7ex,"DP^*"'] & B_* \arrow[l,shift right=.7ex,"ND_\bullet"']
\end{tikzcd}}
\[
\simeq
\]
donc aussi (en \unsure{appliquant à} $B^\circ$)
\diagram{\begin{tikzcd}
B^\bullet \arrow[r,shift right=.7ex,"DP_*"'] & B^* \arrow[l,shift right=.7ex,"ND^\bullet"']
\end{tikzcd}}
\[
\simeq
\]
\margin{\unsure{Isom.} compatibles aux fonct. additifs.}
en particulier
\[
Ab_{\unsure{k}\bullet}\simeq Ab_{k*},\qquad Ab_k^\bullet\simeq Ab_k^*.
\]
\deleted{Il est immédiat \illegible{1}.}
L'image essentielle de $K_\bullet^{\unsure{k}}$ et $K_{\unsure{k}}^\bullet$ par ces
deux foncteurs sont notés $K_*$ et $K^*$.
\margin{$k$ est \unsure{sous-entendu dans les notations}, \unsure{sinon} c'est $K_\bullet(k)$ \unsure{avec indices ou exposants} $\bullet$ ou $*$.}
On a donc un diagramme d'équivalences
canoniques
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\deleted{\unsure{Ab_{k\bullet}}}\arrow[r,shift right=.6ex,"\deleted{DP}"'] &
\deleted{\unsure{Ab_{k*}}}\arrow[l,shift right=.6ex,"\deleted{ND}"']\\
\deleted{Ab_k^\bullet}\arrow[r,shift right=.6ex] &\deleted{Ab_k^*}\arrow[l,shift right=.6ex]
\end{tikzcd}}
\margin{Convention d'écriture. Pour un objet $C$ de $K$,
on note $C_\bullet,C_*,C^\bullet,C^*$ les objets correspondants
obtenus en appliquant $\alpha_\bullet,\alpha_*,\alpha^\bullet,\alpha^*$, et les
comp. sont notés $C_n,C_{[n]},C^n,C^{[n]}$
(\unsure{Attention}, ne pas oublier les signes $[\ ]$
et $C_\bullet,C_*,C^\bullet,C^*,C$).}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
K_\bullet \arrow[rr,shift right=.7ex,"DP^*"']
\arrow[dd,leftrightarrow,"\underset{\circ}{\vee}\ \deleted{\unsure{\mathrm{inv}}}"'] &&
K_* \arrow[ll,shift right=.7ex,"ND_\bullet"']
\arrow[dd,leftrightarrow,"\underset{\circ}{\vee}\ \deleted{\unsure{\mathrm{inv}}}"]\\
&K\arrow[ul,"\alpha_\bullet"]\arrow[ur,"\alpha_*"]
\arrow[dl,"\underset{\circ}{\alpha^\bullet}"']\arrow[dr,"\underset{\circ}{\alpha^*}"]&\\
K^\bullet\arrow[rr,shift right=.7ex,"DP_*"']&&K^*\arrow[ll,shift right=.7ex,"ND^\bullet"']
\end{tikzcd}}
Les flèches \deleted{\unsure{ainsi}} marquées d'un signe
$\circ$ sont des foncteurs \uline{contravariants}.

On a

\uline{Proposition 4} \deleted{\unsure{de (C)}} On a tjs un
hom canonique
'''
save(46,text,[('margin note','upper left','NB Le foncteur DP'),('text','top','Ex 3 La théorie'),('deletion','second line','équivalence de catégories'),('insertion','below second line','équivalence de catégories'),('deletion','before Ab_k','Ab_k'),('margin note','left upper','ND; DP'),('diagram','upper third left','B_• ↔ B_*'),('text','upper third right','donc aussi'),('diagram','upper third right','B^• ↔ B^*'),('margin note','left of en particulier','Isom. compatibles'),('text','upper middle','en particulier'),('display','upper middle','Ab_k• ≃ Ab_k*'),('deletion','middle','Il est immédiat'),('text','middle','L’image essentielle'),('margin note','left middle','k est sous-entendu'),('text','middle','On a donc un diagramme'),('diagram','middle lower cancelled','Ab_k• Ab_k* Ab_k^• Ab_k^*'),('deletion','whole cancelled diagram','Ab_k equivalences'),('margin note','lower left','Convention d’écriture'),('diagram','lower third','K and four associated categories'),('deletion','vertical arrows','inv labels'),('text','below diagram','Les flèches'),('deletion','below diagram','ainsi'),('text','bottom','On a Proposition 4'),('deletion','Proposition 4 line','de (C)')])
