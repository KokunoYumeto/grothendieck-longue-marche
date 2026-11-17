import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(38,r'''
\scanpage{38}
% archive foliation: 37
\[
e_x(\lambda)=\sum\frac{x^n}{n!}\lambda^n
\]
d'où
\[
e_x=e_y\quad\Longleftrightarrow\quad\inserted{\forall n\in\mathbf N,}\ \frac{x^n}{n!}=\frac{y^n}{n!}\quad\Longleftrightarrow\quad x=y
\]
donc $x\longrightarrow e_x$ injectif $N(U)\longrightarrow\operatorname{Hom}\operatorname{Gr}(G_{aK},\operatorname{Un}(U))$.

On voit de \unsure{même} que $x\longmapsto\bar e_x$ $U\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(\overline G_{aK},\operatorname{Un}(U))$ est injectif.

Un hom quelconque \inserted{(pas néc. mult.)} $\bar\varphi:\overline G_a\longrightarrow\operatorname{Un}(U)\subset\inserted{W(U)}$ est donné par
\[
\bar\varphi(\lambda)=\sum_{n\geq0}a_n\lambda^n\qquad a_n\in U
\]
La condition $\bar\varphi(0)=1$ signifie $a_0=1$. Écrivons $\bar\varphi(\lambda+\mu)=\bar\varphi(\lambda)\bar\varphi(\mu)$ i.e.
\[
\begin{array}{ccc}
\displaystyle\sum a_n(\lambda+\mu)^n&=&\displaystyle\sum a_i\lambda^i\sum a_j\mu^j\\
\text{''}&&\text{''}\\
\displaystyle\sum_{i,j}a_n\frac{(i+j)!}{i!j!}\lambda^i\mu^j&&\displaystyle\sum_{\deleted{\unsure{i,j}}}a_i a_j\lambda^i\mu^j
\end{array}
\]
on trouve les conditions $\forall n\in\mathbf N$, $i,j\in\mathbf N$ tels que $i+j=n$
\[
\deleted{a_n(=a_{i+j})=}\qquad
\]
\[
\frac{(i+j)!}{i!j!}a_n=a_i a_j
\]
Donc, faisant $i=1$, $j=n-1$
\[
na_n=a_1a_{n-1}\qquad\text{i.e. }a_n=\frac1n a_1(a_{n-1})
\]
d'où par récurrence sur $n$
\[
a_n=\frac1{n!}\deleted{\unsure{a_1}}\inserted{x}^{n}\qquad x=a_1
\]
(condition aussi suffisante...). Donc $\bar\varphi=\bar e_x$.

\deleted{\unsure{Si} $\bar\varphi:\overline G_{aK}\unsure{\longrightarrow}$}
\inserted{\unsure{Soit|Si} $\varphi:G_{aK}\longrightarrow\operatorname{Un}(U)\subset W(U)$}, on aura même
\[
\varphi(\lambda)=\sum a_n\lambda^n\qquad a_n\in U,\ \text{les }a_n\text{ nuls sauf un nbre fini}
\]
Utilisant $\bar\varphi=\varphi\mid\overline G_a$, on trouve $a_n=\dfrac{x^n}{n!}$. Comme $a_n=0$ pour $n$ grand, on trouve $x$ nilpotent, cqfd.
''',[
('display','top','e_x(lambda)=sum x^n/n! lambda^n'),
('text','top','dou'),
('display','upper','e_x=e_y iff coefficients equal iff x=y'),
('insertion','above coefficient equality','forall n in N'),
('text','upper','donc x to e_x injectif; On voit de même'),
('text','upper-middle','Un hom quelconque bar phi'),
('insertion','above Un hom','pas néc. mult.'),
('insertion','after Un(U) subset','W(U)'),
('display','middle','bar phi(lambda)=sum_n>=0 a_n lambda^n'),
('text','middle','La condition bar phi(0)=1 signifie'),
('display','middle two rows with ditto marks','sum a_n(lambda+mu)^n and binomial expansion'),
('deletion','right expanded sum index','i,j'),
('text','below fold','on trouve les conditions forall n in N'),
('deletion','below conditions','a_n(=a_i+j)='),
('display','lower middle','(i+j)!/(i!j!) a_n=a_i a_j'),
('text','lower middle','Donc, faisant i=1, j=n-1'),
('display','lower middle','n a_n=a_1 a_n-1'),
('text','lower','dou par récurrence sur n'),
('display','lower','a_n=1/n! x^n; x=a_1'),
('deletion','coefficient formula base','a_1 overwritten'),
('insertion','coefficient formula base','x'),
('text','lower','condition aussi suffisante; Donc bar phi=bar e_x'),
('deletion','below preceding sentence','Si bar phi: bar G_aK arrow'),
('insertion','above deleted line','Soit phi: G_aK to Un(U) subset W(U)'),
('text','near bottom','on aura même'),
('display','near bottom','phi(lambda)=sum a_n lambda^n; finite nonzero coefficients'),
('text','bottom','Utilisant bar phi=phi restricted bar G_a; cqfd.')
],[
('de même','même','abbreviated horizontal strokes','medium'),
('right expansion sum index','i,j deleted','index crossed through; legible tentatively','medium'),
('recurrence closed form','deleted a_1, inserted x','base overwritten rather than separately placed','medium'),
('cancelled lower line','Si bar phi: bar G_aK arrow','cancellation obscures several symbols','low'),
('replacement lower line','Soit','Si','medium')])
