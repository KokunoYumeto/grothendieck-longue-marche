import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{101}
% archive foliation: 103
2) $\uline{E'_a}$ Donc $\pi$ engendré par $u,v$ avec $\sigma u=u$, $\sigma v=u-v$
\[\sigma(x,y)=\sigma(xu+yv)=xu+y(u-v)=(x+y)u-yv.\]
\[\sigma(x,y)-(x,y)=yu-2yv=y(u-2v),\quad\text{donc la condition est}\]
$y\in\mathbb Z$, donc on trouve \deleted{que} les points de $\mathbb R\unsure{u_+|u_0}\bmod\pi$,
donc dans ce cas $X(\mathbb R)$ est connexe.

\margin{9.2.}
\uline{NB} Pour bien faire il faudrait aussi classifier les
courbes elliptiques réelles \unsure{intrinsèques}, i.e. les
torseurs (sur $\mathbb R$) sous les \inserted{schémas en} groupes elliptiques
$E_a,E'_a$. Les torseurs non triviaux fournissent les
surfaces conformes \deleted{sans} bord non orientables de
genre $1$. La suite exacte de $\gamma$-modules ($\gamma=\mathrm{Gal}(\mathbb C/\mathbb R)\simeq\{\pm1\}$)
\diagram{\begin{tikzcd}
0\arrow[r]&\pi\arrow[r]&V\arrow[r]&E(\mathbb C)\arrow[r]&0
\end{tikzcd}}
fournit
\[
H^1(\gamma,E(\mathbb C))\simeq H^2(\gamma,\pi)\simeq
\pi^\gamma/(1+\sigma)\pi=\pi_+/(1+\sigma)\pi
\]
1) Cas de $E_a$. On a $\pi\simeq\pi_+\oplus\pi_-$, d'où $\pi^\gamma=\pi_+$
\[
H^1(\mathbb R,E_{\mathbb R})\simeq H^1(\gamma,E(\mathbb C))\simeq H^2(\gamma,\pi)
\simeq\underset{\substack{\Vert\\\mathbb Z/2\mathbb Z}}{\uline{H^2(\gamma,\pi_+)}}
\oplus\underset{\substack{\Vert\\0}}{\uline{H^2(\gamma,\pi_-)}}
\]
Il y a exactement une classe non
nulle dans $H^1$, qui est d'ordre $2$.

2) Cas de $E'_a$. On a $H^1(\mathbb R,E_{\mathbb R})\simeq0$.

Donc les seules courbes elliptiques vraiment
\unsure{intrinsèques} sur $\mathbb R$ sont les $E_a^!=$ torseurs non
triviaux (d'ordre $2$) sous $E_a$, dépendant du
paramètre $a\in\mathbb R^{*+}$.
"""
save(101,tex,[('text','top case 2','E prime a Donc pi engendré par u v'),('display','upper','sigma(x,y)=sigma(xu+yv)'),('display','upper','sigma(x,y)-(x,y)=y(u-2v)'),('text','upper conclusion','y in Z donc on trouve les points'),('deletion','before les points','que'),('text','upper conclusion','X(R) est connexe'),('margin note','left of NB','9.2.'),('text','middle NB','Pour bien faire il faudrait aussi classifier'),('insertion','above groupes','schémas en'),('deletion','before bord','sans'),('display','middle inline','gamma=Gal(C/R) approx plusminus1'),('diagram','middle','0 to pi to V to E(C) to 0'),('text','middle','fournit'),('display','middle cohomology','H1(gamma,E(C))=H2(gamma,pi)'),('text','lower case 1','Cas de Ea On a pi approx pi+ directsum pi-'),('display','lower','H1(R,ER) approx H1(gamma,E(C))'),('text','lower','Il y a exactement une classe non nulle'),('text','lower case 2','Cas de E prime a On a H1 approx 0'),('text','foot conclusion','Donc les seules courbes elliptiques vraiment intrinsèques'),('display','foot inline','E a exclamation=torsors; a in R star plus')],doubts=[('fixed-line label','u+|u0','Subscript is overwritten; a small vertical stroke favors plus.','medium'),('term after réelles and vraiment','intrinsèques','Compressed word, especially its middle letters; the same reading recurs twice.','medium'),('sans bord','deleted sans','A horizontal stroke passes through sans; preserved as a deletion despite the resulting wording.','medium'),('cohomology group letter','gamma','Looped lowercase gamma rather than an uppercase Gamma.','high'),('final family superscript','E_a^!','A separated dot under the high stroke is plainly visible; this is an exclamation mark, distinct from E prime earlier on the same page.','high')],notations=[('intrinsic genus-one torsors',r'E_a^!','Explicit exclamation-mark superscript, not a prime.'),('Galois group',r'\gamma','Small gamma with descending curved stroke.'),('cohomology',r'H^1,H^2','Numerals in superscript; no HN abbreviation.'),('nonzero positive reals',r'\mathbb R^{*+}','Both star and plus are superscript.')],abbreviations=[('NB','nota bene'),('i.e.','id est')],leads=['Scan101 completes fixed-locus topology and computes H1(R,E): Z/2 for split type Ea and zero for nonsplit E prime a. This relates real components to existence of nontrivial real genus-one torsors.','New notation E_a^! denotes the unique nontrivial order-two torsor, not E prime a; check for this distinction in context only after freezing.','No-real-point genus-one torsors give closed nonorientable conformal quotients (Klein bottle in topological classification); deleted sans before bord is a diplomatic reading question.','Self-flagged Pour bien faire il faudrait aussi classifier is substantially answered by the cohomology computation later on the same page; identify scope and whether all torsor isomorphism ambiguities are addressed.'])
