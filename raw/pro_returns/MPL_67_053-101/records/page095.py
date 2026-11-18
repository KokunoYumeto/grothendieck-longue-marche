import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{95}
% archive foliation: 97
structures réelles s'identifie à $G^-$, qui est un \uline{torseur}
sous $G^+$ par translations à gauche. Par contre,
l'opération de $G^+$ sur $G^-$ par autos intérieurs est
\unsure{pas} libre, le centre $\zeta\simeq\{\pm1\}$ de $G$ opère trivialement,
et il y a deux orbites sous $G^+$ (ou encore $G^+/\zeta$).
Ce sont (pour $n=4$ ou $6$) les symétries par rapport
\deleted{\unsure{Dans un}\unsure{ premier}} respectivement aux sommets et aux centres
des \deleted{\unsure{ce}} polygone (carré ou hexagone) fondamental.
\figure{\begin{tikzpicture}[scale=.7]\draw (0,0)--(-.05,.9)--(.95,1)--(1.02,.15);\draw (0,-.08)--(.95,-.02);\end{tikzpicture}}

\uuline{Donc} en résumé

\uline{Proposition} Soit une courbe elliptique \deleted{réelle} complexe. \inserted{$X$}
\deleted{Pour qu'elle admette des}\inserted{Les} structures réelles \deleted{\unsure{sur}\unsure{ elle}}.
\deleted{qu'elles} correspondent aux \inserted{anti} autos \deleted{involutifs} de la
courbe \inserted{elliptique} conforme \deleted{\unsure{fournis}\unsure{ qu'il y en a}},\inserted{il y en a} si et seulement
si la suite
\diagram{\begin{tikzcd}
\unsure{0|1}\arrow[r,dash]&G^+\arrow[r,dash]&G\arrow[r,dash]&\pm1\arrow[r,dash]&\unsure{0|1}
\end{tikzcd}}
est exacte (à droite). Dans ce cas, $G$ est \deleted{\unsure{un}}\inserted{isom. au} groupe diédral
\inserted{$D_n$} dont $G^+$ (d'ordre $n=2,4$ ou $6$) est le groupe des rotations.
L'ens des structures réelles se partage en deux
orbites sous $G^+$ (opérant par autos intérieurs), et
les structures réelles correspondant à deux orbites
distinctes sont (par définition !) non isomorphes. \deleted{\unsure{et les}
deux orbites correspondent aux structures $E_a,E'_a$}

Je présume que si l'une est formée de structures
$E_a$ ($a\in\mathbb R^{*+}$ fixé), l'autre est formée des structures $E'_{\unsure{a|b}}$
(avec $b\unsure{=|\ne}a$), et inversement, i.e. qu'on peut trouver
un $a\in\mathbb R^{*+}$ unique, tel que les deux orbites sont
l'une formée de structures isom. à $E_a$, l'autre de
structures isom. à $E'_a$. De plus il faudrait
"""
save(95,tex,[('text','upper continuation','structures réelles s’identifie à G-'),('text','upper middle','Ce sont pour n=4 ou 6 les symétries'),('deletion','left before respectivement','Dans un premier'),('deletion','before polygone','ce'),('drawing','left small','square with gap at lower right'),('text','middle summary','Donc en résumé'),('text','middle proposition','Soit une courbe elliptique'),('deletion','before complexe','réelle'),('insertion','below complexe','X'),('deletion','start of rewritten proposition','Pour qu’elle admette des'),('insertion','above deletion','Les'),('deletion','after structures réelles','sur elle'),('deletion','before correspondent','qu’elles'),('insertion','above autos','anti'),('deletion','after autos','involutifs'),('insertion','above conforme','elliptique'),('deletion','after conforme','fournis qu’il y en a'),('insertion','above deletion','il y en a'),('diagram','middle','0 G+ G plus minus 1 0'),('text','middle lower','est exacte à droite Dans ce cas'),('deletion','after G est','un'),('insertion','above un','isom. au'),('insertion','above diédral','D_n'),('text','lower proposition','L’ens des structures réelles se partage'),('deletion','after non isomorphes','et les deux orbites correspondent aux structures E_a E_a prime'),('text','foot conjecture','Je présume que si l’une est formée')],doubts=[('operation is not free','pas libre','First word may be non; handwriting resembles par.','medium'),('cancelled draft before respectivement','Dans un premier','Second word and final noun very uncertain.','low'),('rewritten proposition opening','Les structures réelles ... correspondent aux anti autos','Several drafts overprint each other; insertion anti is over aux/auto region.','low'),('exact sequence endpoints','0','1 possible; both are round with a heavy vertical stroke unlike the clear 1s on preceding page.','low'),('conjecture family subscript','a','b alternative; the next parenthesis names b.','low'),('conjecture parenthesis','b=a','Could be b not equal a if a diagonal stroke is merged; visible mark chiefly has two horizontal strokes.','low')],notations=[('centre of dihedral group',r'\zeta\simeq\{\pm1\}','Curled lowercase zeta, not capital Z.'),('two families',r'E_a,E\prime_a','Prime above E, parameter below.')],abbreviations=[('isom. au','isomorphe au')],leads=['Two conjugacy classes of reflections in even dihedral groups give two nonisomorphic real forms of each complex elliptic curve with real j.','Self-flagged presumption: the two real-form orbits might be represented by E_a and E prime_a for a unique common positive parameter; likely requires counterexamples/special cases, keep exact claim separate from established two-orbit statement.','Explicitly withdrawn assertion identifying the two reflection orbits with the two lattice-involution types, then reintroduced as Je présume.'])
