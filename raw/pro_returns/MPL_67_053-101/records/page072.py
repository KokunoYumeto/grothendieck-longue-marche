import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{72}
\mspage{10}
% archive foliation: 74
\uline{NB 1} Cette fonction est unique, \unsure{dû au fait}
que le groupe des automorphismes \deleted{conformes}
holomorphes de $\mathbb D$ agit de façon simple-
ment transitive sur l'ens des
triples \deleted{\unsure{ordonnés}} de pts distincts $(r,s,t)$ \inserted{sur $S^1=\delta\mathbb D$} qui se
suivent pour l'orientation canonique de
\deleted{$\unsure{\delta\mathbb D}$} $S^1$. \deleted{\unsure{Donc $f$}}

\uline{NB 2} La condition 3) implique qu'on a un
\unsure{homéo} canonique
\[
\varphi:\beta=\widehat{(1,\zeta)}\overset\sim\longrightarrow
\overline\beta=\widehat{(1,\overline\zeta)}
\]
tel que $\varphi(1)=1$, $\varphi(\zeta)=\overline\zeta$).

B) Cette application $\varphi$ est rectifiable. Inverse-
ment, tout \deleted{application}\inserted{homéom} rectifiable $\varphi:\beta\overset\sim\longrightarrow\overline\beta$
provient d'une situation comme en A.
De façon plus précise, \deleted{on peut}\deleted{il existe} (quitte
à \unsure{remplacer} $\overline V$ par $\mathbb D$ par le th. d'uniformi-
sation A) simplifié sans segment intérieur $\overline I$,
et normaliser la situation en \deleted{\unsure{faisant}} envoyant
$a$ en $0$, $b$ en $1$) \deleted{il existe un} Il existe
une application continue
\[
f=f_\varphi:\mathbb D\longrightarrow\mathbb D
\]
telle que

1) $f|\mathring{\mathbb D}$ soit \deleted{holo} injection holomorphe
"""
save(72,tex,[('text','top','NB 1 Cette fonction est unique'),('deletion','upper','conformes'),('deletion','upper','ordonnés'),('insertion','upper','sur S^1=δD'),('deletion','upper middle','δD'),('deletion','upper middle','Donc f'),('text','upper middle','NB 2 La condition 3)'),('display','middle','φ:β=arc(1,ζ)→barβ=arc(1,barζ)'),('text','middle','tel que φ(1)=1 φ(ζ)=barζ'),('text','middle lower','B) Cette application φ est rectifiable'),('deletion','middle lower','application'),('insertion','middle lower','homéom'),('deletion','lower','on peut'),('deletion','lower','il existe'),('text','lower','quitte à remplacer V-bar'),('deletion','lower','faisant'),('deletion','lower','il existe un'),('display','bottom','f=f_φ:D→D'),('text','bottom','1) f|D° soit injection holomorphe'),('deletion','bottom','holo')],
 doubts=[('opening connector','dû au fait','written form may be du au fait; no grammatical normalization','medium'),('above triples','ordonnés','abbreviation or full word under strike uncertain','low'),('end of NB 1 cancellation','Donc f','letters nearly obliterated','low'),('before V-bar','remplacer','initial strokes faint','medium')],
 notations=[('Standard closed disc with doubled vertical stroke',r'\mathbb D','Clearly double-stem D in scans 71–72; audit earlier standard-disc occurrences'),('Oriented closed boundary arcs',r'\widehat{(1,\zeta)}','arc placed over parenthesized pair')],
 abbreviations=[('homéom','homéomorphisme'),('holo','holomorphe')],
 leads=['Uniqueness attributed to simple transitivity of holomorphic disc automorphisms on cyclically ordered boundary triples.','Lemme 4B claims the welding map induced by a rectifiable slit is rectifiable, and conversely every rectifiable boundary-arc homeomorphism arises this way.','Normalized inverse construction chooses slit endpoints 0 and 1; detailed conditions continue on scan 73.'])
