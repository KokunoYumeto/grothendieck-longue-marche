import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
s=r'''\scanpage{27}
On a (i)$\Rightarrow$(ii) par suite spectrale
\[
H^{\unsure{p+q|\ast}}(S,F)\Longleftarrow H^p(\mathcal U,H^q(F))=E_2^{pq}
\]
l'hyp (i) implique $E_2^{pq}=0$ pour $0<q\leq n$, \uline{et}
\deleted{l'hyp préliminaire que $E_2^{\unsure{p0|pq}}=0$ pour $q=0$,}
\margin{\figure{\begin{tikzpicture}\draw (0,1.2)--(.03,0);\end{tikzpicture}}}
d'où
\[
H^i(S,F)\xleftarrow{\sim}H^i(\mathcal U,F)\quad\text{pour }i\leq n
\]
et par suite $H^i(\mathcal U,F)\simeq0\deleted{\unsure{H^i}}$ pour $0<i\leq n$.

(ii)$\Rightarrow$(iii) trivial

(iii)$\Rightarrow$(i) par récurrence sur $n$. C'est
\deleted{\unsure{trivial}}\inserted{vide} si $n\leq0$. Supposons $n>0$, et l'assertion
prouvée pour $n'<n$. \deleted{Alors on a déjà, par
l'hyp de récurrence
\[
E_2^{pq}=0\quad\text{si }0<q<n
\]}
\inserted{Regardons}
\[
H^{\unsure{p+q|\ast}}(S,F)\Longleftarrow\varinjlim_{\mathcal U}H^p(\mathcal U,H^q(F))=E_2^{pq}
\]
Par hyp de récurrence, on a
\[
\text{a)}\quad E_2^{pq}=0\quad\text{si }0<q<n
\]
\deleted{de plus, $\unsure{E_2^{p0}=0}$, \unsure{on a que}}
Par hyp (iii), on a
\[
\text{b)}\quad E_2^{pq}=0\quad\text{si }q=0,\ 0<p\leq n
\]
Enfin on sait par \deleted{\unsure{la}}\inserted{l'hyp. préliminaire}
\[
\text{a)}\quad E_{\unsure{2|4}}^{pq}=0\quad\text{si }p\unsure{\geq|=}0,\ q>0
\]
\margin{\figure{\begin{tikzpicture}[x=.42cm,y=.42cm]
\draw[line width=.8pt] (0,6.8)--(0,0)--(8.2,0);
\node[above] at (0,6.9) {$q$};\node[right] at (8.25,0) {$p$};
\node[left] at (-.2,5.35) {$n$};\node[below] at (5.2,-.12) {$n$};\node[below] at (6.15,-.12) {$n+1$};
\node at (4,7) {\unsure{ch}};
\foreach \y in {1,2,3,4,4.6,6.8}{\fill (0,\y) circle (.07);}
\foreach \x in {1,2,3,4,5,5.6}{\fill (\x,0) circle (.07);}
\foreach \x in {0,1,2,3,4,5,6,7}{\node at (\x,5.35) {$\times$};\node at (\x,6.2) {$\times$};}
\foreach \x in {0,6.15,7.1,8}{\node at (\x,0) {$\boldsymbol\times$};}
\draw[dashed] (.15,4.9)--(5.15,.15);
\end{tikzpicture}}}
On trouve alors $E_2^{pq}=0$ si $p+q=n$, d'où
$H^n(S,F)=0$, \unsure{qfd.|cqfd.}
\margin{26}
'''
e=[('text','top','On a (i)⇒(ii) par suite spectrale'),('display','top','H^(p+q)(S,F) ⇐ H^p(U,H^q(F))=E2'),('text','upper','l’hyp (i) implique'),('display','upper','E2^pq=0 pour 0<q≤n'),('deletion','upper following line','l’hyp préliminaire que E2=0 pour q=0'),('drawing','upper beside E2 rows','vertical emphasis stroke'),('text','upper middle','d’où'),('display','upper middle','H^i(S,F) ←~ H^i(U,F) pour i≤n'),('text','middle','et par suite'),('display','middle','H^i(U,F) ≃0 pour 0<i≤n'),('deletion','middle after 0','H^i'),('text','middle','(ii)⇒(iii) trivial'),('text','middle','(iii)⇒(i) par récurrence sur n'),('deletion','middle','trivial'),('insertion','middle above cancelled word','vide'),('text','middle','Supposons n>0 et l’assertion prouvée'),('deletion','middle lower','Alors on a déjà par l’hyp de récurrence'),('deletion','middle lower display','E2^pq=0 si 0<q<n'),('insertion','middle lower','Regardons'),('display','lower middle','H^(p+q)(S,F) ⇐ lim_U H^p(U,H^q(F))'),('text','lower','Par hyp de récurrence on a'),('display','lower a','E2^pq=0 si 0<q<n'),('deletion','lower','de plus E2^p0=0 on a que'),('text','lower','Par hyp (iii) on a'),('display','lower b','E2^pq=0 si q=0 0<p≤n'),('text','lower','Enfin on sait par'),('deletion','lower after par','la'),('insertion','lower above cancelled phrase','l’hyp. préliminaire'),('display','lower repeated a','E2^pq=0 si p≥0 q>0'),('drawing','lower left','p,q quadrant with crossed positions and diagonal'),('text','bottom','On trouve alors E2^pq=0 si p+q=n'),('display','bottom','H^n(S,F)=0 qfd.'),('margin note','bottom left','26')]
save(27,s,e,observations='Whole and halves checked against all proof lines; four enlarged regions read. Čech checks are not supplied on H where no separate accent is visible. The final case is visibly labelled a) again. Its p comparison is heavily overwritten; ≥ is kept first with = as alternative rather than selecting from the spectral-sequence argument. The quadrant sketch is reproduced with its two crossed upper rows, crossed horizontal tail, dots, dashed diagonal and written labels. Degree and E subscript uncertainties remain explicit.')
