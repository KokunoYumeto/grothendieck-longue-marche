import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{100}
% archive foliation: 102
\uline{Cor} Supposons $k$ principal \inserted{$2$-régulier}, $k_0=k/2k$ un corps.
Alors les $(M,\sigma)$ \inserted{\unsure{$C_2$ étales|$C_2$ objets}} précédents
\unsure{équiv. à} celles des paires $(P,Q,\deleted{\unsure{\bar p,\bar q,m}})$ où $P,Q$ libres de rg $1$,
et $\deleted{\unsure{p}}m\subset\underbrace{P/2P}_{p}\oplus\underbrace{Q/2Q}_{q}$ un espace vectoriel sur $k_0$,
\deleted{\unsure{de M, qui}}
qui est soit nul, soit une droite $\ne p,q$ (\unsure{trois cas seulement}).

\uline{Cor} Cela donne une description des classes de conjugaison,
d'éléments de $\mathrm{Gl}(2,k)^{\deleted{\unsure{*}}}$ qui sont d'ordre $2$ exactement, et
distincts de $\{\pm1\}$ : il y \deleted{\unsure{en a}} \inserted{celle de}
$\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ (correspondant au
cas $m=0$), puis \uline{une} \deleted{famille, \unsure{indexée} par les \unsure{points de}
$\mathbf P^1(k_0)$ distincts de $0,\infty$ (en supposant que
$k^\times\to k_0^\times$ est surjectif \unsure{sinon la classification sera plus fine})}
\margin{$\unsure{k'^\times\to k_0'^\times}$ \unsure{surj.}}
\unsure{en fait bien de} $P/2P\unsure{\to}Q/2Q$ en revenant au choix d'une base de $P,Q$.

\unsure{Plus} concrètement :
\[
P=k,\ Q=k,\ m=\text{diagonale de }k_0\oplus k_0\quad\text{i.e.}
\]
\[
M'=(2k\oplus2k)+\text{diag. de }k\oplus k
=\{(x,y)\mid x-y\in2k\}
\]
donc on peut prendre base de $M'$
\[
\unsure{e_0|u}=(2,0),\quad\unsure{e_1|v}=(1,1),\quad
\text{d'où}\quad-\unsure{e_0|u}+2\unsure{e_1|v}=(0,2)=\operatorname{sym}(\unsure{e_0|u})
\]
\margin{$u=2e_0$\quad$v=e_0\unsure{+|-}e_1$}
On trouve
\[
\sigma\unsure{e_0|u}=\unsure{e_0|u},\quad
\sigma\unsure{e_1|v}=(1,-1)=e_1-\operatorname{sym}\unsure{e_1|v}=\unsure{e_0-e_1|u-v}
\]
i.e. la matrice de $\sigma$ p.r. à $(\unsure{u,e_1|u,v})$ est
\[\begin{pmatrix}1&1\\0&-1\end{pmatrix}\]

Dans le cas $k=\mathbb Z$, c'est la matrice de la réflexion p.r. la
diagonale $0,e_0$ de l'hexagone régulier,
les \unsure{pts.|fl.} de l'hexagone étant rapportés à un
syst. de coordonnées obliques ayant comme base
deux sommets consécutifs $u$ $v$ ($M$ est le réseau
engendré par l'un des sommets).
\figure{\begin{tikzpicture}[scale=.9,>=stealth]
\draw[->](-1,0)--(-.5,.87);\draw(-.5,.87)--(-.08,.15);
\draw[->](-.45,1.03)--(0,1.73);\draw[->](.5,.87)--(.03,1.7);
\draw[->](.55,.78)--(1,0);\draw[->](.4,-.87)--(.6,-.87);
\draw[->](-.4,-.88)--(-.53,-.88);\draw(-.55,-.87)--(-1,0);
\draw[->](0,0)--(.5,.87);\draw[->](0,0)--(-.5,-.87);
\draw[->,very thick](.1,0)--(1.05,0);\draw(-1,0)--(-.2,0);
\draw[dashed](0,.1)--(0,1.65);\draw[dashed](0,.82)--(.5,.82)--(.5,-.9);
\draw(0,-.1)--(.18,-.8);
\node[left]at(-1,0){$-u$};\node[above left]at(-.5,.87){$v-u$};
\node[above right]at(.5,.87){$\unsure{e_1|v}$};\node[right]at(1,0){$u=u_+$};
\node[below left]at(-.5,-.87){$-\unsure{e_1|v}$};
\node[below right]at(.5,-.87){$\sigma\unsure{e_1|v}=u-v$};
\node[left]at(0,.92){$\unsure{e_1}$};\node[below]at(.55,0){$e_0$};
\node[above]at(0,1.73){$\deleted{\unsure{2e_1-e_0}}\ \unsure{v-u|2v-u}=u_-$};
\end{tikzpicture}}

\uline{NB} Soit $u_+$ une base de $\pi_+$, $u_-$ une base de $\pi_-$, alors
\deleted{dans} On peut représenter $\sigma_{\mathbb R}$ pour la base $(u_+,u_-)$ de $\pi\otimes_{\mathbb Z}\mathbb R$,
par la matrice $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ le réseau $\pi$ étant identifié
à $\mathbb Z u_-+\mathbb Z u_+$ \deleted{$\unsure{\simeq\mathbb Z^2}$} dans le premier cas et dans le $2$\textsuperscript{d}
à l'ens des $xu_++yu_-$ tels que $x-y\in\mathbb Z$, $x,y\in\frac12\mathbb Z$.
\margin{$\sigma^2(e_1)=\sigma e_0-\sigma e_1=e_0-(e_0-e_1)=e_1$}
"""
save(100,tex,[('text','top','Cor Supposons k principal'),('insertion','above principal','2-régulier'),('insertion','above M sigma','C2 étales'),('deletion','in pair','bar p bar q m'),('display','upper inline','m subset P/2P directsum Q/2Q'),('deletion','before m','p'),('deletion','after k0','de M qui'),('text','upper','Cor Cela donne une description'),('deletion','exponent of Gl','star'),('deletion','after il y','en a'),('insertion','above matrix','celle de'),('display','upper middle','matrix 1 0 0 -1'),('deletion','middle three lines','famille indexée par les points de P1(k0)'),('margin note','right middle','k prime units to residue units surj.'),('text','middle','en fait bien de P/2P to Q/2Q'),('text','middle','Plus concrètement'),('display','middle','P=k Q=k m=diagonale'),('display','middle','M prime=(2k directsum 2k)+diag'),('text','middle lower','donc on peut prendre base'),('display','middle lower','e0=(2,0) e1=(1,1)'),('margin note','left circled','u=2e0 v=e0+e1'),('text','middle lower','On trouve'),('display','middle lower','sigma e0=e0 sigma e1=(1,-1)'),('text','lower','i.e. la matrice de sigma'),('display','lower','matrix 1 1 0 -1'),('text','lower','Dans le cas k=Z réflexion hexagone'),('drawing','lower left','hexagon with apex vectors and dotted coordinates'),('deletion','diagram apex label','2e1-e0'),('text','foot','NB Soit u+ une base de pi+'),('deletion','NB second line','dans'),('display','foot inline','matrix 1 0 0 -1'),('deletion','foot after integral lattice','simeq Z²'),('display','last line inline','x u+ + y u- x-y in Z x,y in 1/2 Z'),('margin note','bottom left','sigma²(e1)=sigma e0-sigma e1')],doubts=[('top insertion above M sigma','C2 étales|C2 objets','Small insertion has a subscript-like 2 and a faint long word.','low'),('top equivalence verb','équiv. à','Compressed verb with uncertain ending.','low'),('end of first corollary','trois cas seulement','Numeral/word before cas is an open cursive stroke.','low'),('cancelled classification paragraph','famille indexée par les points de P1(k0), units surjectivity','Long cancellation leaves most letters visible but not the linking words; alternatives and uncertainties are retained.','low'),('line after cancellation','en fait bien de ... en revenant au choix d’une base','The beginning is interrupted by diagonal crossing strokes.','low'),('basis symbols throughout middle','e0|u; e1|v','The author repeatedly overwrites the old e labels with u/v, so both visible states remain uncertain.','low'),('side basis note','v=e0+e1|v=e0-e1','Short transverse stroke could belong to the following e.','medium'),('hexagon text','pts.|fl.','Abbreviation reduced to a loop and descending strokes.','low'),('diagram apex','v-u|2v-u','A possible initial 2 merges with a cancelled label.','low'),('NB lattice order','Z u- + Z u+','Subscripts are retained in visible order, independently of the expected order.','medium')],notations=[('ring letter',r'k','Handwritten tall loop, distinct from h despite resemblance.'),('basis replacement',r'\unsure{e_0|u},\unsure{e_1|v}','Heavy overstriking makes the final chosen state uncertain.'),('direct sum',r'\oplus','Circled plus in lattice expressions.'),('matrix',r'\begin{pmatrix}1&1\\0&-1\end{pmatrix}','Off-diagonal entry visibly one.')],abbreviations=[('rg','rang'),('p.r.','par rapport'),('syst.','système'),('NB','nota bene'),('ens','ensemble'),('surj.','surjectif')],leads=['Rank-two involution classification over a principal 2-regular ring with residue field: diagonal and nonsplit integral types; cancelled discussion of unit reduction surjectivity should be kept separate from asserted classification.','Integral normal form [[1,1],[0,-1]] and the half-integral parity lattice supply explicit constructive evidence for the real elliptic lattice dichotomy.','The phrase engendré par l’un des sommets for the rank-two hexagonal lattice appears insufficient literally; inspect as a wording issue, not silently repair.'])
