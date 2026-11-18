import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{86}
% archive foliation: 88
qui opère sur $\operatorname{Oct}(V)$, opère sur $I(V)$, et on trouve
\diagram{\begin{tikzcd}
\Gamma(V) \arrow[r,"\sim"] \arrow[d,equal] & \unsure{\mathfrak S}_{I(V)},\\
\operatorname{Aut}^+(\operatorname{Oct}(V)) &
\end{tikzcd}}
et cet iso \deleted{\unsure{\operatorname{Aut}}} définit une structure de
$V$-torseur sur $I(V)$. (Ceci résulte de la théorie
combinatoire de l'octaèdre, ou du cube c'est kif kif.)

\uline{Proposition} Soit $X$ droite projective \unsure{réelle} sur un corps alg. clos $k$
(il suffit qu'il \deleted{contienne} soit stable par extraction des racines
carrées) de car. $\ne2$, et $G=\operatorname{Aut}_kX$. Alors il y a corr 1-1
entre

a) les sous-groupes $V$ de $G$ isom. à $D_2$

b) \rule{3cm}{0.2pt} $\Gamma$ de $G$ isom. à $\unsure{\mathfrak S}_4$ \deleted{\unsure{un}}

c) les parties $S\in\mathcal P_6(X(k))$ qui sont ``octaédrales'', i.e.
\deleted{\unsure{telles que}}\inserted{isom. à} $(\mathbb P^1_k,\{0,\infty,\pm1,\pm i\})$

par
\[
\begin{aligned}
\Gamma&=\operatorname{Nor}_G(V)\\
V&=\inserted{\text{unique}}\ \text{sous-groupe }\deleted{\text{\unsure{invariant isom. à}}}\inserted{\text{inv. de }\Gamma\ \text{isom. à}}\ D_2\ \deleted{\unsure{\subset G}}\\
S&=\text{ens de ramification de l'action de }V\text{ sur }X
\end{aligned}
\]
\deleted{\unsure{ou de l'action}}
(\uline{NB} $\Gamma$ a un ens de ramification
plus grand qui comprend, en plus de $S$,
les ``milieux d'arêtes'' et ``centres des faces''
de l'octaèdre,

\margin{\uline{Cor} la catégorie (quand $k$ fixé)
des couples $(X,V)$ (ou $(X,\Gamma)$
$(X,S)$) \unsure{est} équivalente à celle
des octaèdres \inserted{\unsure{combin.}} \uline{orientés}, une
fois choisi \deleted{\unsure{a}} une racine
carrée de $-1$ dans $k$. Mieux : la
cat. des couples $(X,V)$ \unsure{est} équivalente
à celle des couples $(\operatorname{Oc},\varphi)$
où $\operatorname{Oc}$ est un octaèdre combinatoire et
$\varphi:\{\pm i\}\overset\sim\longrightarrow\unsure{\operatorname{or}}(\operatorname{Oc})$.}

Dans l'ensemble $S$, on a un antipodisme $\uline{a}_S=\uline{a}_V$
défini par la condition que pour $\sigma\in V^*$, $a_S$ \deleted{est}\inserted{induit} la transposition
de $X^\sigma$ (de cardinal 2). On définit sur $S$ une
structure octaédrale, admettant $\Gamma$ comme groupe des
autom. orientés, et $\uline a$ comme antipodisme, via l'antipodisme
(les faces sont les parties $S'\in\mathcal P_3(S)$ telles que $S'\cup-S'=\unsure{S'|S}$).
"""
save(86,tex,[('text','top','qui opère sur Oct(V)'),('diagram','top','Gamma(V) isomorphic symmetric group I(V)'),('deletion','under diagram','Aut'),('text','upper','et cet iso définit'),('text','upper middle proposition','Soit X droite projective'),('deletion','proposition second line','contienne'),('text','middle a','les sous-groupes V de G'),('text','middle b','Gamma de G isom. à symmetric group 4'),('deletion','end b','un'),('text','middle c','les parties S in P6(X(k))'),('deletion','under c','telles que'),('insertion','under c','isom. à'),('display','below a,b,c','Gamma=Nor; V=unique subgroup; S=ramification'),('insertion','after V=','unique'),('deletion','after sous-groupe','invariant isom. à'),('insertion','above deletion','inv. de Gamma isom. à'),('deletion','end V line','subset G'),('deletion','below ramification line','ou de l’action'),('text','lower middle NB','Gamma a un ens de ramification'),('margin note','left diagonal lower','Cor la catégorie'),('insertion','margin above orientés','combin.'),('deletion','margin before une racine','a'),('text','bottom','Dans l’ensemble S'),('deletion','after a_S','est'),('insertion','above est','induit')],doubts=[('proposition after projective','réelle','The word reads r-...-lle; mathematical expectation has not been used to replace it.','low'),('b ditto','horizontal stroke','Long stroke repeats preceding les sous-groupes; represented by a rule, without expansion.','high'),('V formula corrections','invariant isom. à / inv. de Gamma isom. à','Heavy overlapping corrections; order inferred from placement and caret only.','low'),('margin corollary first connector','est','A short arrow-like stroke may serve as est.','low'),('margin inserted adjective','combin.','Tiny word between two lines.','low'),('margin final target','or(Oc)','Orientation-set notation; cursive initial glyph uncertain.','medium'),('last formula right member','S prime','S; short stroke after S could be prime or punctuation.','low')],notations=[('orientation-preserving automorphisms',r'\operatorname{Aut}^+','Plus superscript.'),('fixed points',r'X^\sigma','Sigma superscript.'),('orientation set',r'\operatorname{or}(\operatorname{Oc})','Tentative operator reading.')],abbreviations=[('inv.','invariant'),('corr','correspondance'),('alg. clos','algébriquement clos'),('Cor','corollaire'),('combin.','combinatoire(s)')],leads=['Proposition generalises Klein-four / S4 / octahedral six-point correspondences to quadratically closed fields of characteristic not 2; potential small-characteristic exception deserves a targeted check (especially characteristic 5).','Gamma has extra ramification at edge midpoints and face centres; branch orders likely 2,3,4 but must verify rather than import.','Margin asserts categorical equivalence with oriented combinatorial octahedra after choosing sqrt(-1), or intrinsic orientation-torsor identification; potential descent content.'])
