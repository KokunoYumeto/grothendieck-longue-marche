import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(56,r'''
\scanpage{56}
% archive foliation: 55
$k$ anneau comm.

$\mathcal V=\mathcal V(k)$ catégorie des Modules libres de type fini sur $k$ (morphismes : \uline{iso})
\[
\begin{array}{c}
\text{''}\\
\displaystyle\coprod_{n\in\mathbf N}\mathcal V_n(k)
\end{array}
\qquad\mathcal V_n(k)\quad\text{catégorie des modules libres de rang }n\text{ sur }k
\]

$\mathcal V$ catégorie additive (graduée)

\deleted{a) $\mathcal V\xrightarrow{\Delta}\unsure{\mathcal V_1}$ foncteur}

\deleted{b) $\unsure{\Delta}$} $P(k)$ catégorie de Picard des $k$-modules libres de rang $1$ $\mathbf Z$-gradués, avec donnée de comm. l'isomorphisme de Koszul

\uline{Théorie des \inserted{modules} déterminants gradués}

a) $\mathcal V\xrightarrow{\Delta}P$ $\otimes$ foncteur [donc muni d'iso funct.
\[
\Delta(V+V')\overset{\varphi_{V,V'}}{\simeq}\Delta(V)\otimes\Delta(V')
\]
\[
(\Rightarrow\Delta(0)\simeq\mathbf1\quad\text{can}^{\mathrm t})
\]
\deleted{\unsure{gr}}

b)\deleted{\unsure{a)}} Si $\operatorname{rg}(V)=1$, $\Delta(V)\simeq V$, de degré $1$.

c) Soient $V\supset W_1$ ; $W_2,W_2'$ deux suppl. de $W_1$ dans $V$ ($W_1,W_2$ libres, donc $V,W_2'$ aussi)
\[
\begin{array}{l}
\alpha:W_1+W_2\xrightarrow{\sim}V\\
\alpha':W_1+W_2'\xrightarrow{\sim}V\\
\lambda:W_2\simeq W_2'
\end{array}
\]
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\Delta(W_1+W_2)\arrow[r,"{\substack{\Delta(\alpha)\\\sim}}"]\arrow[d,dash,"{\varphi_{W_1,W_2}}"',"\sim"{rotate=90}] &
\Delta(\unsure{V|W}) &
\Delta(W_1+W_2')\arrow[l,"{\substack{\Delta(\alpha')\\\sim}}"']\arrow[d,dash,"{\varphi_{\unsure{W_2|W_1},W_2'}}","\sim"'{rotate=90}]\\
\Delta(V_1)\otimes\Delta(W_2) &&
\Delta(W_1)\otimes\Delta(W_2')\arrow[ll,"{\substack{\operatorname{id}\otimes\Delta(\lambda)\\\sim}}"]
\end{tikzcd}}

commutatif.

[ Equivaut à : Si $u$ est un autom de $V$ qui est l'identité sur $W_1$ et sur $V/W_1\ (\simeq W_2)$, alors $\Delta(u)=\operatorname{id}_{\Delta(V)}$ ]
''',[
('text','top','k anneau comm'),
('text','upper','V=V(k) catégorie des Modules libres'),
('display','upper left','ditto and coproduct V_n(k)'),
('text','upper right','V_n(k) catégorie des modules libres de rang n'),
('text','upper right','V catégorie additive (graduée)'),
('deletion','upper cancelled line','a) V to V_1 labelled Delta foncteur'),
('deletion','before P(k)','b) Delta'),
('text','upper-middle','P(k) catégorie de Picard des k-modules libres de rang 1 Z-gradués'),
('text','middle heading','Théorie des modules déterminants gradués'),
('insertion','above heading','modules'),
('text','middle','a) V to P tensor foncteur'),
('display','middle','Delta(V+V prime) isomorphism Delta(V) tensor Delta(V prime) labelled phi'),
('display','middle','implies Delta(0) isomorphic 1 can^t'),
('deletion','left of unit line','gr'),
('text','middle','b) Si rg(V)=1 Delta(V) isomorphic V de degré 1'),
('deletion','after b)','a)'),
('text','below middle','c) Soient V superset W_1; W_2 W_2 prime deux suppl.'),
('display','right above diagram','alpha alpha prime lambda'),
('diagram','at and below fold','Delta complements to Delta(V); vertical phi lines; bottom arrow points left'),
('text','below diagram','commutatif'),
('text','bottom bracket','Equivaut à: Si u est un autom de V'),
('display','bottom within bracket','Delta(u)=id_Delta(V)')
],[
('first cancelled line target','calligraphic V_1','subscript-like stroke crosses cancellation','low'),
('cancelled b) before P(k)','Delta','triangular cancellation and residual loop','low'),
('small deleted item left of unit line','gr','could be a revised list label; not securely readable','low'),
('deleted label after b)','a)','overwritten small label','low'),
('diagram top middle','V','W; overlapping strokes at vertex','medium'),
('diagram right vertical phi first index','W_2','W_1; first index appears 2, retained as first reading','medium'),
('diagram lower left first object','Delta(V_1)','W_1 would be expected but visible letter has two strokes and is V','high'),
('diagram vertical edges','plain vertical isomorphism lines without arrowheads','lower right edge has short curved foot, no definite arrowhead','high')])
