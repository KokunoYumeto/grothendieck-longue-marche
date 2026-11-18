import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{97}
% archive foliation: 99
expliciter le lien du paramètre $a$ avec le paramètre $\tau$, ou
mieux, avec l'invariant modulaire $j\in\mathbb R^{\unsure{2}}$ (serait-ce
$j=\unsure{\tfrac14|4}\log a$ ?)
\deleted{\inserted{\unsure{i.e.} $a=\exp j$ ou $a=\exp(-j)$}\unsure{suivant qu'on est dans la famille} $E_a,E'_a$ ?}.

\deleted{Considérons} Notons que si $\sigma$ est dans $G^-$, alors
suivant les cas $-\sigma$ est conjugué, ou non conjugué,
à $\sigma$. \inserted{(réflexion p.r. à la \unsure{droite orthogonale} à celle de $\sigma$)}
Dans le cas hexagonal, il est non conjugué ;
dans le cas carré, il est conjugué. Dans le cas
non \unsure{anharmonique}, $n=2$, il est bien sûr non conjugué (car
$G$ est alors commutatif) -- donc le cas \deleted{hexagonal}\inserted{carré} est
le seul où $-\sigma$ \deleted{\unsure{ne}} soit \deleted{\unsure{pas}} conjugué à $\sigma$.
\deleted{Donc \unsure{si} dans le cas carré par ex., on trouve}
\figure{\begin{tikzpicture}[scale=.65]
\draw(-1,0)--(-.55,.8)--(.5,.8)--(1,0)--(.55,-.8)--(-.65,-.8)--cycle;
\draw(-1.03,.05)--(-.58,.85)--(.46,.85);\draw(.56,.77)--(1.02,.06);\draw(-1.04,-.09)--(-.69,-.8);\draw(.95,-.1)--(.5,-.8);\draw(.98,-.12)--(.59,-.84);
\draw(-1.03,0)--(1.08,0);\draw(0,-1.5)--(.1,1.6);\fill(.1,1.6)circle(.04);
\end{tikzpicture}}

\uline{Distinguons les cas}

1) \uline{$n=2$} Cas non \unsure{anharmonique}. Le groupe des autos
est $\pm1,\pm\sigma$, où $\sigma$ est un \inserted{anti} auto. On voit de
suite que si $\sigma$ est du type somme directe d'un
$\operatorname{id}_P$ et $-\operatorname{id}_Q$, il en est de même de $-\sigma$ (avec $P,Q$
échangés) donc on est dans cas $E_a$, \unsure{où}\deleted{\unsure{on}} donc
un $E_a$ et un $E_{a'}$, correspondent aux deux éléments de
$\unsure{\sigma},\sigma'$ de $G^-$, et on aura $aa'=1$.
\deleted{\unsure{En}} car
prenant un gén. $u=\unsure{e_+}$ de $\pi_+$, un autre \inserted{$v=e_-$}$v$ de $\pi_-$, on a
\[
a=a(\sigma)=\frac{Q(\unsure{e_-|e_+})}{Q(e_+)}
\]
et comme par passage de $\sigma$ à $-\sigma$ \deleted{\unsure{les}} $e_+$ et $e_-$ s'interchangent,
on aura bien
\[
a(-\sigma)=1/a(\sigma)
\]
\margin{Ceci vaut aussi bien dans le cas des $E_a$, que des $E'_a$}
(valable dans tous les cas), donc
\[
a(-\sigma)=a(\sigma)\quad\Longleftrightarrow\quad a(\sigma)=1\quad\Longleftrightarrow\quad\text{cas \uline{carré}}.
\]
"""
save(97,tex,[('text','top continuation','expliciter le lien du paramètre a'),('deletion','top crossed sentence','suivant qu’on est dans la famille E_a E_a prime'),('insertion','within top deletion','i.e. a=exp j ou a=exp(-j)'),('deletion','before Notons','Considérons'),('text','upper','Notons que si sigma est dans G-'),('insertion','above -sigma est conjugué','réflexion p.r. à la droite orthogonale'),('deletion','after le cas','hexagonal'),('insertion','above hexagonal','carré'),('deletion','before soit','ne'),('deletion','above conjugué','pas'),('deletion','above case heading','Donc si dans le cas carré par ex. on trouve'),('drawing','left of paragraph','hexagon with vertical and horizontal axes'),('text','middle heading','Distinguons les cas'),('text','middle case 1','n=2 Cas non anharmonique'),('insertion','before auto','anti'),('deletion','after E_a','on'),('text','lower','un E_a et un E_a prime correspondent'),('deletion','before car','En'),('text','lower','prenant un gén. u=e+'),('insertion','above v','v=e-'),('display','lower','a=a(sigma)=Q(e-)/Q(e+)'),('text','lower','et comme par passage de sigma à -sigma'),('deletion','before e+ et e-','les'),('display','lower','a(-sigma)=1/a(sigma)'),('margin note','right lower','Ceci vaut aussi bien dans le cas des E_a que E_a prime'),('text','foot','valable dans tous les cas donc'),('display','foot','a(-sigma)=a(sigma) iff a(sigma)=1 iff cas carré')],doubts=[('top j range','R superscript 2','Raised symbol is heavily retraced; possibly a correction or question mark rather than exponent.','low'),('top proposed j formula','one quarter log a','4 or a struck coefficient may be intended; written as a question, not normalized to a known modular formula.','low'),('cancelled top line','suivant qu’on est dans la famille','First words under a horizontal stroke.','low'),('case name','anharmonique','Could contain an extra t; word retained uncertain in both occurrences.','medium'),('after donc on est dans cas E_a','où on donc','Overlapping revisions and short connective not resolved.','low'),('pair of parameters','E_a and E_{a prime}','Prime appears after subscript a, not after E; essential distinction retained.','medium'),('quadratic ratio numerator','e-','e+ possible because sign overdrawn.','low')],notations=[('parameter inversion',r'a(-\sigma)=1/a(\sigma)','Minus sign and reciprocal explicit.'),('prime location',r'E_{a\prime}\text{ versus }E\prime_a','Parameter prime on this page distinct from curve-family prime on earlier pages.')],abbreviations=[('gén.','générateur'),('par ex.','par exemple')],leads=['Explicit request to relate a to tau or modular j, with a tentative logarithmic expression, not an established formula.','The discussion now contradicts the preceding presumption: for generic split lattices the two real forms are E_a and E_{a prime} with a a prime=1, of the same topological type.','Claims sigma and -sigma conjugate precisely in the square case among n=2,4,6.','Parameter reciprocal under sign reversal is asserted for both families, with equality exactly in the square case; inspect normalizations.'])
