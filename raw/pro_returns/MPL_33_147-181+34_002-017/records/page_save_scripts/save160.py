import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,160,r'''\scanpage{160}
En particulier, si $X=Y$, $F=G$, prenant $\eta^0=\deleted{\unsure{\alpha}}\delta_{X,F}$ on trouve
\[
\boxed{\operatorname{Tr}(\xi^0\cup\delta_{X,F}^{0})=\sum\unsure{(-1)^i}\operatorname{Tr}(\xi^0)^i}
\]
C'est la \uline{formule de Lefschetz-Verdier}.

\margin{\textcircled{e}\quad 2}
\deleted{\unsure{\S}}
Considérons un morphisme
\[
u:T\longrightarrow X\times_S Y
\]
\unsure{défini} donc par deux morphismes
\[
u_1:T\longrightarrow X,\quad u_2:T\longrightarrow Y.
\]
On a alors un morphisme évident
\[
\mathrm{R}u_*\bigl(\mathrm{R}\mathcal{H}om(u_1^*(F_\bullet),u_2^!(G_\bullet))\bigr)
\longrightarrow\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F),\mathrm{pr}_2^!(G_\bullet))
\]
Car $u_i=\mathrm{pr}_i u$, donc le premier est un
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\mathrm{R}u_*\bigl(\mathrm{R}\mathcal{H}om(\deleted{\unsure{\mathrm{pr}}}u^*\mathrm{pr}_1^*(F),u^!(\mathrm{pr}_2^!(G_\bullet)))\bigr)\arrow[r,"\sim"]\arrow[d,phantom,"\simeq" description]
&\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F),u_*u^!(\mathrm{pr}_2^!(G)))\arrow[d,"\varepsilon"]\\
\mathrm{R}\mathcal{H}om(u_*u^*(\mathrm{pr}_1^*(F)),\mathrm{pr}_2^!(G_\bullet))\arrow[r]
&\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F),\mathrm{pr}_2^!(G))
\end{tikzcd}}

\deleted{Donc} tout élément de \deleted{$\unsure{\operatorname{Corr}^{0}(X,F,)}$}
\[
\alpha^0\in\mathrm{R}\operatorname{Hom}^{0}(u_1^*(F),u_2^!(G))
=\mathrm{R}^{0}\Gamma_T\bigl(\mathrm{R}\mathcal{H}om(u_1^*(F),u_2^!(G_\bullet))\bigr)
\]
définit un \unsure{élément}
\[
\overline{\alpha^0}\in\operatorname{Corr}(X,F;Y,G)
\]
De même, un élément $\beta^0$ de $\mathrm{R}\operatorname{Hom}^{0}(u_1^*(F),u_2^!(G))$ définit un \unsure{élmt} $\overline{\beta^0}\in\operatorname{Corr}(Y,G;X,F)$.
\margin{159}
''',[
('text','top','En particulier, si X=Y'),('deletion','top equation','overwritten alpha'),('display','upper framed','Tr(xi cup delta) sum trace'),('text','upper','C’est la formule de Lefschetz-Verdier'),('margin note','upper left','circled e, 2'),('deletion','upper left body','section mark'),('text','upper middle','Considérons un morphisme'),('display','upper middle','u:T to X times_S Y'),('text','middle','défini donc par deux morphismes'),('display','middle','u1:T to X, u2:T to Y'),('text','middle','On a alors un morphisme évident'),('display','middle','Ru_* RHom to RHom'),('text','lower middle','Car u_i=pr_i u'),('diagram','lower middle','direct image Hom comparison square'),('deletion','diagram upper left','pr'),('deletion','lower','Donc'),('text','lower','tout élément de'),('deletion','lower','Corr0(X,F,)'),('display','lower','alpha0 in RHom0 equals R0Gamma_T'),('text','lower','définit un élément'),('display','lower','bar alpha0 in Corr'),('text','bottom','De même, un élément beta0'),('margin note','bottom left','159')],remarks='Whole and both halves read. The first trace formula has no clearly legible summation subscript; none supplied. The final beta Hom expression appears to repeat u1*(F),u2!(G), although the Corr target reverses X,Y; retained. The direct-image functor is written without an R in the right-hand and lower nodes of the square. e and a separate 2 are both present in the margin.')
