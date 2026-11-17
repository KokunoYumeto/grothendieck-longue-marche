from records.record_page import save
save(124, r'''
\scanpage{124}
% archive foliation: 123
(auquel cas les pts correspondants des
$A_X$ \uline{ne sont pas} des sommets topologiques
\unsure{\ldots}) \deleted{\unsure{on}} \deleted{\unsure{en}} \inserted{\unsure{se permet de}}
\unsure{le considère|les considère} comme un ``milieu
d'arête'' des $A_X$.

À l'exclusion de ce cas, on peut dire
que $A$, avec l'ens de ses sommets
choisis (qui \unsure{c.} \deleted{\unsure{A}} \uline{tous} \uline{les} sommets
topologiques, et les pts $0,1,\infty$ \inserted{qui sont $\in A$}, (qu'ils
\unsure{soient ou non} sommets top., et éventuellement
$N$ autres, \unsure{enfin} suivant l'opération
qu'on veut obtenir sur les sommets
qu'on entend donner aux $A_X$), et
le choix des centres des faces fait
en conformité avec la condition $1^\circ$,
et enfin un choix \uline{arbitraire} des
milieux d'arête de $A$ (tous distincts
\unsure{même} de $0,1,\infty$) est \unsure{déduit} d'une
application $\varphi:S\to S$ ramifiée aux
seuls pts $0,1,\infty$, avec ramification
$2$ au dessus de $1$, en prenant l'image
inverse de $[0,1]$ -- et l'image inverse
\deleted{dans} $A_X$ dans $X$ par $f:X\to S$ de
$A$ n'est que $(\varphi f)^{-1}([0,1])$,
\unsure{où} $\varphi f$ est \deleted{ramifiée} un rev. \unsure{en dehors de}
$0,1,\infty$ (car $\varphi^{-1}\{0,1,\infty\}\supset\{0,1,\infty\}$ et
''', [
('text','top','(auquel cas les pts correspondants'),('deletion','top line 3','on / en'),('insertion','top line 3','se permet de'),
('text','upper-middle through bottom','À l’exclusion de ce cas'),('deletion','upper-middle','A'),('insertion','upper-middle','qui sont ∈ A'),('deletion','lower','dans'),('deletion','bottom','ramifiée')],
doubts=[('3–4','se permet de; le considère comme un milieu','les considère; overwritten preliminary words','low'),('7–10','qui c.; qu’ils soient ou non sommets top.','compressed cursive and cancellation','low'),('12','enfin suivant l’opération','enfin uncertain','low'),('20','déduit; même de','ending and qualifier uncertain','medium'),('bottom','un rev. en dehors de','rapid abbreviated phrase','low')],
leads='Continuation of the operations argument: A with vertex/face/edge-center choices is said to arise as inverse image of [0,1] under a sphere map φ; composition φf explains the induced graphs. Explicit inclusion φ^{-1}{0,1,∞} ⊃ {0,1,∞}. Several difficult syntactic qualifications remain marked; inspect with 123/125 during audit.')
