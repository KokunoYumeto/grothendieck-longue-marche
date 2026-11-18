import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{98}
% archive foliation: 100
2) \uline{Cas carré} $n=4$. On voit que l'on a un $\sigma$ de type $E_1$,
et $-\sigma$ est du même type. Cela correspond aux
symétries p.r. aux \deleted{\unsure{bissectrices}}\inserted{diagonales} du carré de
départ. La symétrie par rapport à un côté
échange $e_0$ et $e_1$, les invariants et anti-invariants
sont resp. engendrés par $e_0+e_1$ et $e_0-e_1$, qui n'engendrent
pas le réseau, donc on est dans le cas $E'_{\unsure{a'}}$. Or
\figure{\begin{tikzpicture}[scale=.8]
\draw(-.6,-.6)--(-.6,.6)--(.6,.6)--(.6,-.6)--cycle;
\draw[dashed](-1.15,0)--(1.35,0);\draw[dashed](0,-1.25)--(0,1.3);
\draw[->,thick](0,0)--(-.6,.6)node[above left]{$e_1$};\draw[->,thick](0,0)--(.6,.6)node[above right]{$e_0$};
\draw[thick](-.52,.73)--(0,1.15);\draw[dashed](0,1.15)--(.6,.65);
\end{tikzpicture}}
\[
a'=\frac{Q(e_0-e_1)}{Q(e_0+e_1)}=\deleted{4}1\qquad\text{aussi}
\]
\deleted{\unsure{E_1}}
Donc on trouve les types $E_1$ (``sommets'') et $E'_1$ (``côtés'').

3) \uline{Cas hexagonal} $n=6$.

\uline{Réflexions-sommets}. Les \deleted{\unsure{premiers}} invariants pour
la réflexion p.r. à $\mathbb R u$ sont \uline{engendrés}
par $u$, les anti-invariants par $2v-u$, c'est
du type $E'_a$, avec
\figure{\begin{tikzpicture}[scale=.85,>=stealth]
\draw(-1,0)--(-.5,.87)--(.5,.87)--(1,0)--(.5,-.87)--(-.5,-.87)--cycle;
\draw(-.4,1.03)--(0,1.73)--(.45,1.08);\node[above]at(0,1.73){$2v-u$};
\draw[->](0,0)--(1,0)node[right]{$u$};\draw[->](0,0)--(.5,.87)node[above right]{$v$};
\draw[->](0,0)--(-.5,.87)node[above left]{$v-u$};\draw[->](0,0)--(-1,0)node[left]{$-u$};
\draw[->](0,0)--(-.5,-.87)node[below left]{$-v$};\draw[->](0,0)--(.5,-.87)node[below right]{$u-v$};
\end{tikzpicture}}
\[
a=\frac{Q(2v-u)}{Q(u)}=\sqrt3
\]

\uline{Réflexions-faces} ce sont les $-\sigma$, on trouve donc $E'_{1/a}=E'_{1/\sqrt3}$.

\uline{En résumé} Dans tous les cas, sauf le cas carré, \deleted{\unsure{tous les}}\inserted{l'ens des}
\deleted{les}\inserted{les types de} structures réelles sur $X$ sont soit \deleted{du type}
$\{E_a,E_{1/a}\}$,
\deleted{\unsure{le cas}} soit $\{E'_a,E'_{1/a}\}$ \inserted{avec $a>1$}
(le cas hexagonal étant dans le
deuxième cas \inserted{avec $a=\sqrt3$}), à l'exclusion bien sûr l'un de l'autre.
Dans le cas carré, l'ens des structures réelles
est $\{E_1,E'_1\}$ i.e. il y a à la fois des structures $E$ et $E'$.
\figure{\begin{tikzpicture}\draw(0,0)--(-.04,-3.7);\end{tikzpicture}}
"""
save(98,tex,[('text','upper case 2','Cas carré n=4'),('deletion','after aux','bissectrices'),('insertion','above deletion','diagonales'),('drawing','upper left','square axes e0 e1 arrows'),('display','upper middle','a prime=Q(e0-e1)/Q(e0+e1)=1'),('deletion','before 1','4'),('deletion','left of Donc','E1'),('text','middle','Donc on trouve les types E1 sommets E1 prime côtés'),('text','middle heading case 3','Cas hexagonal n=6'),('text','middle','Réflexions-sommets Les invariants'),('deletion','after Les','premiers'),('drawing','middle left','hexagon vectors u v v-u -u -v u-v apex 2v-u'),('display','middle lower','a=Q(2v-u)/Q(u)=sqrt3'),('text','lower','Réflexions-faces ce sont les -sigma'),('text','lower summary','En résumé Dans tous les cas sauf le cas carré'),('deletion','after cas carré','tous les'),('insertion','above deletion','l’ens des'),('deletion','before structures','les'),('insertion','above structures','les types de'),('deletion','after soit','du type'),('deletion','before second soit','le cas'),('insertion','above parenthesis','avec a>1'),('insertion','above deuxième cas','avec a=sqrt3'),('text','foot','Dans le cas carré l’ens des structures réelles'),('drawing','left of summary','vertical delimiting rule')],doubts=[('cancelled word before diagonales','bissectrices','Long strike obscures most letters.','low'),('first E prime parameter','a prime','Retraced subscript before Or.','low'),('cancelled sign at left before Donc','E1','Looks like a capital and numeral under repeated strokes.','low'),('cancelled word before invariants','premiers','May instead be a first attempt at invariants itself.','low'),('hexagonal value','sqrt3','Radical clearly visible; not changed to 3 despite the quadratic-form quotient.','high'),('summary opening revisions','l’ens des; les types de','Two overlapping insertions create syntactic duplication, preserved.','medium')],notations=[('hexagonal quadratic ratio',r'Q(2v-u)/Q(u)=\sqrt3','Radical transcribed literally.'),('strict inequality',r'a>1','Greater-than sign in insertion.'),('square labels',r'e_0,e_1','Zero and one, not plus/minus here.')],leads=['Withdrawn-in-same-text presumption from scan095 is replaced by a classification: outside square, both real forms have same lattice type and reciprocal a; square has one of each type.','Hexagonal calculation gives quadratic-form quotient sqrt3; with Q quadratic and angle60 degrees the ratio should be 3. Requires explicit check and a separate refined claim; do not alter transcription.','Two real structures at j=1728 have different real-locus topology; at j=0 both nonsplit; distinguish pointwise real descent from marked family quotient.'])
