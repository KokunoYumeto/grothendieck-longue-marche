import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{65}
% archive foliation: 67
[On laisse tomber dorénavant les $'$ des $X'$ !]

\deleted{Mais sur $X^*=X\setminus\bigcup D_i$ (si \unsure{chaque composante}
\unsure{connexe} \unsure{$X$ est}}

OPS. $X$ connexe, $I$ non vide --- alors
il y a sur $X^*=X\setminus\bigcup_i\mathring D_i$ (surface
conforme à bord obtenue dans la
découpe de $X$ suivant $\bigcup\delta D_i$) une
\deleted{\unsure{mét}} métrique \deleted{hyperbolique} canonique modulo
constante (qu'on peut d'ailleurs normaliser
par la condition que le volume soit $1$)
\deleted{\unsure{sauf dim $=$}}\inserted{et} canonique \inserted{sans cte} dans le cas
hyperbolique (i.e. quand on n'a
\[
g=0\qquad \underset{\text{card }I}{\underbrace{\nu}}\in\{1,2\}
\]
) --- dans le cas
\margin{il y a aussi le cas \deleted{\unsure{dans}} \unsure{orienté}
du plan projectif réel $(\simeq S^2/\pm1)$
\deleted{\unsure{privé} d'un disque}\inserted{``avec un trou''}}
hyperbolique le bord est géodésique,
donc dans tous cas le bord est muni
d'une structure torique canonique
provenant de la structure riemannienne.
Il est tentant de restreindre le \inserted{syst. des}
disques envisagés, en exigeant que
les deux structures toriques sur
chaque $\delta D_i$ (provenant soit de $D_i$, soit de $X^*$)
"""
save(65,tex,[('text','top','On laisse tomber dorénavant les primes'),('deletion','top two lines','Mais sur X*'),('text','upper','OPS. X connexe I non vide'),('deletion','middle','mét'),('deletion','middle','hyperbolique'),('text','middle','canonique modulo constante'),('deletion','middle lower','sauf dim ='),('insertion','middle lower','et'),('insertion','middle lower','sans cte'),('display','lower middle','g=0 ν∈{1,2}'),('margin note','left diagonal','il y a aussi le cas'),('deletion','left diagonal','dans'),('deletion','left diagonal','privé d’un disque'),('insertion','left diagonal','avec un trou'),('text','lower','hyperbolique le bord est géodésique'),('text','bottom','Il est tentant de restreindre'),('insertion','bottom','syst. des')],
 doubts=[('top cancelled parenthesis','chaque composante connexe X est','last words almost obliterated; unresolved syntax retained','low'),('cancelled line before canonique','sauf dim =','multiple overlaid strokes','low'),('left diagonal margin','orienté','word and attachment uncertain; may belong to surrounding draft','low'),('left diagonal cancelled word','privé','thick crossing','low')],
 notations=[('Punctured bordered surface',r'X^*=X\setminus\bigcup_i\mathring D_i','interior circles over D retained'),('Number of marked points',r'\nu=\operatorname{card} I','nu and bracketed gloss on scan 65')],
 abbreviations=[('OPS.','On peut supposer'),('cte','constante'),('syst.','système')],
 leads=['Canonical metric on the complementary bordered surface, modulo constant then normalized by volume 1; canonical without scale in the hyperbolic case. Exceptional g=0, ν∈{1,2}, with a marginal projective-plane-with-hole case.','Proposed restriction: agreement of toric structures on each disc boundary coming from the disc and the complement; continuation on scan 66.'])
