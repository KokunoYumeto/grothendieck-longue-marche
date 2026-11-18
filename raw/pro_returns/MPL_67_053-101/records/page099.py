import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{99}
% archive foliation: 101
\uline{Résumé} Cas $E_a$ :
\[
\left\{\begin{array}{l}
\text{base }u=e_0,\ v=e_1\\
\text{forme }\deleted{Q(e_0)=Q(e_1)}\quad Q(xe_0+ye_1)=x^2+ay^2
\end{array}\right.
\]
Si on \unsure{veut|met} la forme $Q$ sous forme standard on
prend la \inserted{nouvelle} base
$\underbrace{e_0}_{1},\underbrace{\frac1{\sqrt a}e_1}_{i}$, on trouve donc la base
$1,\sqrt a\,i$ d'où
\[\boxed{\tau=\sqrt a\,i},\]

Cas $E'_a$ : base, \deleted{$\unsure{u=e_0,v=\frac12u|u=e_0,v=u}$}
distinguée p.r. à $Q$ les
\[
e_0=u,\quad e_1=2v-u;\qquad Q(xe_0+ye_1)=x^2+ay^2
\]
\[v=\frac12(e_0+e_1).\]
\unsure{au|on} \deleted{\unsure{premier}} changement de base.
\[
\underbrace{e_0}_{1},\underbrace{\frac1{\sqrt a}e_1}_{i}
\qquad\text{bien orthonormale}
\]
et on a $u\Rightarrow1$, $v\mapsto\frac12(1+\sqrt a\,i)$, donc
\[\boxed{\tau=\frac12(1+\sqrt a\,i)}=\frac12+\frac{\sqrt a}{2}i.\]
\figure{\begin{tikzpicture}\draw plot[smooth]coordinates{(0,0)(.5,-.05)(1,0)(1.5,-.01)(2,.04)(2.5,.01)(3,.08)(3.5,.04)(4,.1)(4.5,.04)(5,.1)(5.5,.06)(6,.08)(6.5,.04)(7,.09)(7.5,.06)(8,.09)};\end{tikzpicture}}

Calcul du groupe des pts réels d'une courbe $E_a$, $E'_a$.

Pts réels sont les $x\bmod\pi$ ($x\in\pi_{\mathbb R}$) tels que
\[\sigma x\equiv x\quad(\pi)\]
\uline{Distinguons les deux cas}.

1) $\uline{E_a}$ \deleted{$\sigma(e_0,e_1)=$} $\sigma(x,y)=x,-y$
\[\text{donc}\qquad\sigma(x,y)-(x,y)=(0,2y)\]
donc la condition est que $2y\in\mathbb Z$. Donc il y a \deleted{\unsure{les}}
les pts de $\deleted{\unsure{\frac02}}\mathbb R e_0$ et de
$\deleted{\mathbb R}(0,\frac12)+\mathbb R e_0$, donc
\uline{deux composantes connexes} \deleted{pour} $X(\mathbb R)$.
"""
save(99,tex,[('text','upper title','Résumé Cas Ea'),('display','upper brace','base u=e0 v=e1 forme Q'),('deletion','upper display','Q(e0)=Q(e1)'),('text','upper paragraph','Si on veut la forme Q'),('insertion','above base','nouvelle'),('display','upper middle boxed','tau=sqrt a i'),('text','middle','Cas E prime a base distinguée p.r. à Q'),('deletion','after base','u=e0 v=...'),('display','middle','e0=u e1=2v-u Q=x²+ay²'),('display','middle','v=1/2(e0+e1)'),('text','middle','au changement de base'),('deletion','before changement','premier'),('display','middle lower','e0 1/sqrt a e1 bien orthonormale'),('text','middle lower','et on a u to 1 v to'),('display','boxed','tau=1/2(1+sqrt a i)'),('drawing','separator','wavy horizontal rule'),('text','lower heading','Calcul du groupe des pts réels'),('text','lower','Pts réels sont les x mod pi'),('display','lower','sigma x equiv x pi'),('text','lower','Distinguons les deux cas 1) Ea'),('deletion','before sigma(x,y)','sigma(e0,e1)='),('display','lower','sigma(x,y)-(x,y)=(0,2y)'),('text','foot','donc la condition est que 2y in Z'),('deletion','after il y a','les'),('deletion','before R e0','0/2'),('deletion','before (0,1/2)','R'),('text','foot conclusion','deux composantes connexes X(R)'),('deletion','before X(R)','pour')],doubts=[('first paragraph verb','veut|met','Fast connected strokes; both readings possible.','medium'),('cancelled basis formula','u=e0,v=1/2u|u=e0,v=u','Dense cancellation hides the equality and fraction; symbols retained with alternatives.','low'),('before changement','au|on; premier','Stroke may be a prefix or word; cancelled word is especially uncertain.','low'),('u arrow','Rightarrow','Two parallel shafts appear in first arrow, unlike the following mapsto.','medium'),('cancelled words in final paragraph','les; 0/2','Both heavily retraced, with a small fraction-like remnant at left.','low'),('sign in sigma difference','(0,2y)','Positive sign is what is visible; no minus inserted.','high')],notations=[('period parameter',r'\tau','Boxed in both families.'),('realification',r'\pi_{\mathbb R}','Lattice pi with real subscript.'),('underbraces identifying basis',r'\underbrace{e_0}_1,\underbrace{e_1/\sqrt a}_i','The first label is numeral one.')],abbreviations=[('pts','points'),('p.r.','par rapport')],leads=['Period parameters are explicitly sqrt(a)i and (1+sqrt(a)i)/2, settling that a is the squared length ratio and reinforcing the hexagonal sqrt3 inconsistency on098.','Real fixed-locus computation starts: split lattice yields two connected components; sigma difference is written with positive 2y, harmless for integrality but sign is literal.'])
