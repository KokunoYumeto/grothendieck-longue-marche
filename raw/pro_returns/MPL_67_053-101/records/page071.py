import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{71}
% archive foliation: 73
\uline{Lemme $4$}
\margin{\uline{NB} il y a une version plus faible de A),
où $\dot U=C$ (sans $I$), \unsure{mais la formulation ci-contre implique A)}}

A) Soit $U$ une partie ouverte bornée
de $\mathbb C$, dont la frontière est \deleted{une}\inserted{réunion de}
courbe de Jordan \deleted{rectifiable. Alors}
$C$, et d'un intervalle \deleted{topologique}
\deleted{il existe une fonction, à savoir}
topologique $\overline I$ tel que
\deleted{$f:D\longrightarrow$}
$I\cap C=\{b\}$, \deleted{et} (alors $I\setminus\{b\}$ est
contenu dans la comp. connexe
bornée $V$ de $\mathbb C\setminus C$, et $b$
est une extrémité de $\overline I$,)
\inserted{(alors $U=V\setminus I'$, où $I'=\overline I\setminus\{b\}$)}.
On suppose de plus que $C$ et $I$ soient rectifiables.
Soit $a$ l'autre extrémité de $\overline I$. Alors il
existe une fonction \deleted{continue} $f:D\longrightarrow\mathbb C$
telle que

\figure{\begin{tikzpicture}[x=.8cm,y=.8cm]
\draw (0,0) .. controls (-1.8,-.2) and (-2.2,1.4) .. (-1.9,3)
 .. controls (-1.8,3.8) and (-1.4,4.8) .. (-.7,5.1)
 .. controls (-.3,5.7) and (-.1,5.1) .. (.2,5.1)
 .. controls (.7,5.2) and (1.4,5) .. (1.6,4.6)
 .. controls (2.6,3.8) and (2.7,2.8) .. (2.4,1.5)
 .. controls (2.2,.3) and (1.3,-.1) .. (0,0);
\draw[very thick] (.7,2.8) .. controls (.8,3.7) and (.9,4) .. (1.6,4.6);
\node[right] at (.7,2.8) {$a$}; \node[above] at (1.6,4.6) {$b$};
\draw[->] (.05,1.4) .. controls (.4,1.3) and (.6,1.8) .. (.55,2);
\draw[->] (.5,6.1) .. controls (.6,5.5) and (1,5.1) .. (1.4,4.65);
\node[above] at (.5,6.1) {$\unsure{\overline\zeta}$};
\draw[->] (2.5,5.6) .. controls (2.4,5.1) and (1.9,4.7) .. (1.6,4.5);
\node[above] at (2.5,5.6) {$\zeta$};
\draw (1.15,4.7)--(1.37,4.55) (1.18,4.78)--(1.4,4.58)
 (1.53,4.44)--(1.7,4.32) (1.58,4.5)--(1.76,4.35);
\end{tikzpicture}}

a) $f$ est continue, et induit une \deleted{\unsure{ho}} bijection
(voire un homéo !) $\mathring D\overset\sim\longrightarrow U$.

b) $f(\zeta)=f(\overline\zeta)=b$, et $f$ induit une bijection,
(voire un homéo) $\deleted{\alpha}\inserted{\alpha\setminus\{\zeta,\overline\zeta\}}\overset\sim\longrightarrow C\setminus\{b\}$.
(NB $\zeta=\exp\frac{2i\pi}{3}$, et $\alpha,\beta,\overline\beta$ sont les trois
arcs de $\delta D$ déterminés par $1,\zeta,\overline\zeta$).

\figure{\begin{tikzpicture}[scale=.85]
\draw (0,0) ellipse (1.25 and 1.35);
\draw (1.2,0)--(1.36,0) node[right] {$1$};
\draw (-.68,1.13)--(-.78,1.3) node[above left] {$\zeta$};
\draw (-1.16,-.49)--(-1.34,-.49) node[left] {$\overline\zeta$};
\node at (-.95,.4) {$\alpha$};\node at (.2,.9) {$\beta$};
\node at (.1,-1) {$\overline\beta$};
\draw (-.85,-1) .. controls (-.3,-1.4) and (.45,-1.5) .. (.95,-1.26);
\end{tikzpicture}}

3) $f|\beta$ et $f|\overline\beta$ induisent des bijections de
$\beta$ et $\overline\beta$ sur $\overline I$).
NB a) b) c) peuvent
s'exprimer en disant que $f$ induit un
\deleted{isom}\inserted{\unsure{homéo}} de $D$ sur la découpe de $\overline U=\overline V$
suivant $\overline I$ (on scinde $I\cup C=\dot U$).

4) $f|\mathring D$ est holomorphe.
"""
save(71,tex,[('text','top','Lemme 4'),('margin note','top left diagonal','NB il y a une version plus faible'),('text','upper right','A) Soit U une partie ouverte bornée'),('deletion','upper right','une'),('insertion','upper right','réunion de'),('deletion','upper right','rectifiable Alors'),('deletion','upper right','topologique'),('deletion','upper right','il existe une fonction à savoir'),('deletion','upper right','f:D→'),('deletion','upper middle','et'),('insertion','upper middle','alors U=V\I′'),('drawing','upper left','Jordan curve slit a b ζ barζ'),('text','middle','On suppose de plus que C et I'),('deletion','middle','continue'),('text','middle lower','a) f est continue'),('deletion','middle lower','ho'),('text','lower','b) f(ζ)=f(barζ)=b'),('deletion','lower','α'),('insertion','lower','α\{ζ,barζ}'),('drawing','lower left','circle α β barβ 1 ζ barζ'),('text','lower','NB ζ=exp(2iπ/3)'),('text','bottom','3) f|β et f|barβ'),('text','bottom','NB a) b) c) peuvent'),('deletion','bottom','isom'),('insertion','bottom','homéo'),('text','bottom','4) f|D° est holomorphe')],
 doubts=[('diagonal top note','mais la formulation ci-contre implique A)','several words partly overlap heading and figure','low'),('crossed sentence above topologique','il existe une fonction à savoir','last two words strongly crossed','low'),('first drawing left label','barζ','bar and zigzag overlap','medium'),('NB near bottom insertion','homéo','small letters above struck isom','medium')],
 notations=[('Frontier notation',r'\dot U','dot above U in marginal note and final parenthesis'),('Slit interval',r'\overline I','bars copied only where visible; some plain I occurrences on same sheet'),('Disc interior',r'\mathring D','circle above D'),('Boundary labels',r'\zeta,\overline\zeta,\alpha,\beta,\overline\beta','disc diagram scan 71')],
 leads=['Global slit-disc uniformization lemma 4A with rectifiable Jordan boundary and attached rectifiable interval, endpoint identifications, and holomorphic interior map.','Marginal weaker version omits the slit; compare the exact hypotheses and topological boundary extension.','The numerical labels a), b), 3), 4) coexist with an NB referring to a), b), c); numbering kept diplomatically.'])
