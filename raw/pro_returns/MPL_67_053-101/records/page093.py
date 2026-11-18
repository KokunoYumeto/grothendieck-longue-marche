import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{93}
% archive foliation: 95
\uline{Courbes elliptiques réelles}
\deleted{Elles sont} La catégorie de ces courbes
(avec morphismes pas néc des iso) équivaut à celle
des systèmes $(\pi,\sigma,c)$, où $\pi$ est un $\mathbb Z$-module
libre, \inserted{de rg $2$}\deleted{\unsure{muni}} $c$ une structure \deleted{conf} conforme orientée
sur $\pi_{\mathbb R}=\pi\otimes_{\mathbb Z}\mathbb R$, et $\sigma$ un anti-homomorphisme du
syst. $(\pi,c)$, qui peut s'interpréter comme une
involution de $\pi$, renversant l'\uline{orientation}
\inserted{de $\pi\otimes\mathbb R$ i.e. de déterminant $-1$}
(donc $\ne\pm\operatorname{id}_\pi$),
et \unsure{conservant} la structure conforme. Pour le couple
$(\pi,\sigma)$ il y a exactement deux possibilités, à isom. près.
\deleted{Pour} (elles sont d'ailleurs isogènes\ldots). Il reste, pour chacune
d'elles, à trouver les structures conformes qui \unsure{est|sont}
invariantes par $\sigma$. On peut les normaliser par \deleted{\unsure{\sigma\circ\sigma}}
\[
Q(\unsure{e_+})\deleted{(=Q(\unsure{e_-}))}=1
\]
\margin{\uline{NB} $e_+$ est une base de \deleted{\unsure{k}}$\pi_+$\par
$e_-$\rule{3cm}{0.3pt}$\pi_-$}
donc ce sont les structures de la forme
\[
Q(x\unsure{e_+}+y\unsure{e_-})=x^2+ay^2
\]
où $a\in\mathbb R^{*+}$. Il y a donc deux familles de courbes
elliptiques réelles, paramétrées chacune par $\mathbb R^{*+}$ ; on peut
les désigner par $E_a,E'_a$ ($a\in\mathbb R^{*+}$). \deleted{Considérons}

Considérons les autos \deleted{de ces courbes}\inserted{d'une courbe elliptique}
définie par $(\pi,\sigma,c)$, ils correspondent aux \deleted{\unsure{Aut de}}
autos $\theta$ de $\pi$ qui a) commutent à $\sigma$ et b) respectent la
structure conforme $c$, \inserted{\uline{orientée}} \deleted{\unsure{en particulier}}
ce qui revient \unsure{au|à} $=$ \inserted{c'est à d' $\theta$ transforme $\pi^+_{\unsure{\pm}}$ en $\pi^+$}
la forme $Q$ (à un facteur près).
\inserted{(en plus de C'est un $\unsure{U}$)}
\deleted{\unsure{Montrer}\unsure{ le}\unsure{ sg}\unsure{ fixe}\unsure{ est}\unsure{ le}}
Il transforme \deleted{\unsure{puisque}} $e_0$ en un multiple \inserted{ent} $\pm e_0$,
SPS quitte à composer avec la symétrie $\unsure{\lambda}=-\operatorname{id}$ que c'est $e_0$.
Mais le seul auto de $\mathbb R e_0+\mathbb R e_1$ qui respecte $Q$, qui fixe $e_0$ et qui
n'est pas l'identité, est $\sigma$, \deleted{\unsure{par conséquent}}\inserted{\unsure{exclu}} par l'orientation !
Donc il n'y a que l'\unsure{autom.} universel, \unsure{commun à tous} : $-\operatorname{id}_{\unsure{\pi}}$.
"""
save(93,tex,[('text','top title','Courbes elliptiques réelles'),('deletion','after title','Elles sont'),('text','upper','La catégorie de ces courbes'),('insertion','above libre','de rg 2'),('deletion','after libre','muni'),('deletion','before conforme','conf'),('insertion','below orientation','de pi tensor R i.e. de déterminant -1'),('text','middle','Pour le couple pi sigma'),('deletion','before parenthesis','Pour'),('text','middle','elles sont d’ailleurs isogènes'),('deletion','after normaliser par','sigma circ sigma'),('display','middle','Q(e+)=1'),('deletion','inside normalization','=Q(e-)'),('margin note','right of normalization','NB e+ est une base de pi+ ; e- pi-'),('deletion','inside margin before pi+','k'),('text','middle lower','donc ce sont les structures'),('display','middle lower','Q(xe+ +ye-)=x squared +a y squared'),('text','lower','où a in R star plus Il y a donc deux familles'),('deletion','after E_a,E_a prime','Considérons'),('text','lower paragraph','Considérons les autos'),('deletion','after autos','de ces courbes'),('insertion','above deletion','d’une courbe elliptique'),('deletion','after correspondent aux','Aut de'),('insertion','after c','orientée'),('deletion','after c','en particulier'),('insertion','right of ce qui revient','c’est à d’ theta transforme pi+ en pi+'),('insertion','below c','en plus de C’est un U'),('deletion','lower right long strike','Montrer le sg fixe est le'),('text','lower','Il transforme e0 en un multiple'),('deletion','below transforme','puisque'),('insertion','above multiple','ent'),('text','foot','Mais le seul auto'),('deletion','after est sigma','par conséquent'),('insertion','above deletion','exclu')],doubts=[('after involution paragraph','conservant','Several medial letters compressed; no replacement by mathematical expectation.','medium'),('structures conformes qui','est','sont possible; written agreement uncertain.','low'),('normalization basis subscripts','e+ e-','Both characters overdrawn, possibly replaced from e0/e1.','medium'),('last large paragraph insertion and cancellations','en plus de C’est un U; Montrer le sg fixe est le','Extremely fast intertwined marginal revision, weakest reading on this page.','low'),('pi in theta transforms clause','pi superscript plus with subscript plus/minus','Index strokes overlap cancellation; exact location uncertain.','low'),('symmetry symbol','lambda=-id','May be just -id without a separate named symbol.','low'),('last phrase','autom. universel, commun à tous','Ending of common phrase faint/compressed; final subscript could be V0 rather than pi.','low')],notations=[('integral lattice',r'\pi','Lowercase pi with long top bar, not uppercase Pi.'),('conformal structure',r'c','Plain lowercase c.'),('basis shift',r'e_+,e_-;\ e_0,e_1','Both styles occur; earlier signs overwritten, later 0 and 1 retained.'),('automorphism',r'\theta','Theta distinct from sigma.')],abbreviations=[('syst.','système'),('rg','rang'),('autos','automorphismes'),('SPS','supposons'),('ent','entier'),('c’est à d’','c’est-à-dire')],leads=['Two lattice-involution types and two positive-real families of real elliptic curves; claim the two types are isogenous.','Classification ignores or presupposes a chosen origin; check category convention because arbitrary real genus-one curves can have no real point.','Real automorphisms preserving orientation claimed to be only ±id, even where the complex curve has extra automorphisms; inspect the role of commuting with real conjugation.'])
