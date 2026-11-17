import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(39,r'''
\scanpage{39}
% archive foliation: 38
2) Soit $M$ un $K$-module, $\operatorname{Aut}_K(M)$ \inserted{$\subset\operatorname{End}_K(M)$} le foncteur en groupes $K'\longrightarrow\operatorname{Aut}_{K'}(M_{K'})$ sur $\operatorname{Alg}_{/K}$.

On cherche les hom. de Groupes
\diagram{\begin{tikzcd}
G_a\arrow[r,"\varphi"]\arrow[d,phantom,"\cup" description]&\operatorname{Aut}_K(M)\\
\overline G_a\arrow[r,"\bar\varphi"]&\operatorname{Aut}_K(M)
\end{tikzcd}}
On donne comme \unsure{d'habt|d'hab}
\[
(*)\quad u\longmapsto\bar e_u:\quad\operatorname{End}_K(M)\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(\overline G_{aK},\operatorname{Aut}_K(M))
\]
\[
(**)\quad u\unsure{\longleftarrow|\longmapsto}e_u:\quad N\deleted{\unsure{U}}(\operatorname{End}_K(M))\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(G_{aK},\operatorname{Aut}_K(M))
\]
\[
\begin{aligned}
\bar e_u(\lambda\deleted{\unsure{u}})&=\exp(\lambda\unsure{u_K|u_{K'}})=\sum_{n\geq0}\frac{u_{K'}^n}{n!}\lambda^n
&\quad\lambda\in\overline G_a(K')=N(K')\\
e_u(\lambda)&=\ -\quad-\quad-\quad-\quad-
&\quad(\lambda\in G_a(K')=K')
\end{aligned}
\]
On trouve encore que $(*)$ et $(**)$ sont des bij.

(\uline{NB} Si $M$ est projectif de type fini, il suffirait d'appliquer le cas précédent $1^\circ$ : $U=\operatorname{End}_K(M)$)

On utilise le fait que $\forall$ morphisme de foncteurs $\bar\varphi:\overline G_{\unsure{K|aK}}\longrightarrow\operatorname{End}_K(M)$ (pas néc. multiplicatif) est donné de façon unique par
\[
\bar\varphi(\lambda)=\sum_{n\geq0}u_n\lambda^n\qquad u_n\in\operatorname{End}_K(M),
\]
et $\forall$ morphisme de foncteurs $\varphi:G_{aK}\longrightarrow\operatorname{End}_K(M)$ par
\[
\varphi(\lambda)=\sum_{n\geq0}u_n\lambda^n\qquad u_n\in\operatorname{End}_K(M)\text{ nuls sauf un nb fini.}
\]
Ceci posé, \deleted{\unsure{le calcul}} \inserted{on constate} que la condition n et s. pour que $\bar\varphi$ (resp $\varphi$) soit un hom de groupes, c'est qu'on ait $u_n=\dfrac1{n!}(u_1)^n$ \ldots
''',[
('text','top','2) Soit M un K-module; Aut_K(M)'),
('insertion','above Aut_K(M)','subset End_K(M)'),
('text','upper','On cherche les hom. de Groupes'),
('diagram','upper','G_a phi Aut_K(M); bar G_a bar phi Aut_K(M)'),
('text','upper middle','On donne comme dhab'),
('display','middle (*)','u maps to bar e_u: End_K(M) to Hom_gr'),
('display','middle (**)','u left-arrow e_u: N(End_K(M)) to Hom_gr'),
('deletion','N before End_K(M)','U (uncertain overwritten fragment)'),
('display','middle paired formulas','bar e_u(lambda)=exp; e_u(lambda)=dashes'),
('deletion','bar e_u argument after lambda','u'),
('text','around fold','On trouve encore que (*) et (**) sont des bij.'),
('text','fold parenthesis','NB Si M est projectif de type fini'),
('text','lower middle','On utilise le fait que forall morphisme de foncteurs'),
('display','lower middle','bar phi(lambda)=sum u_n lambda^n'),
('text','lower','et forall morphisme de foncteurs phi'),
('display','lower','phi(lambda)=sum u_n lambda^n; nuls sauf un nb fini'),
('text','bottom','Ceci posé; condition n et s. pour que'),
('deletion','bottom after Ceci posé','le calcul'),
('insertion','above deleted le calcul','on constate')
],[
('after On donne comme','dhabt','dhab; abbreviated ending uncertain','medium'),
('(**) arrow from u','left arrow','mapsto; left-facing arrowhead appears in ink','medium'),
('(**) N followed by overwritten fragment','N deleted U','could be an altered Nil symbol; do not infer locally nilpotent notation','low'),
('bar e_u argument','deleted u after lambda','small overwritten letter','medium'),
('exponential argument subscript','u_K','u_Kprime; prime not securely visible','medium'),
('formal group in lower prose','bar G_K','bar G_aK; a not visible','medium'),
('deleted bottom phrase','le calcul','first short word retraced','medium')])
