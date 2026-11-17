from save_page import save_page
save_page(51,r'''\cotefile{12}
\scanpage{51}
% archive foliation: 50
$X$ \textcircled{\unsure{liss}} \deleted{\unsure{affine.} \unsure{conn.}} de dim $n$ \unsure{partout}.

\[
\left\{\begin{aligned}
H^i_!(X,\mathbf{Z}(0))&\in\mathrm{Ob}\,M_i^+(K)\deleted{\unsure{M_0}}\inserted{\text{et }\in\mathrm{Ob}\,M_n^+(K)}\quad\forall i\qquad\text{mieux :}\\
H^{n+k}_!(X,\mathbf{Z}(0))&\in\mathrm{Ob}\left[\unsure{\xi|\zeta}^{k}M_{n-k}^+(K)\right]\deleted{+\unsure{\xi|\zeta}^{k+1}M^+_{\unsure{n-k-2}}}
\end{aligned}\right.
\]

\[
H^i(X,\mathbf{Z}(0))\in\mathrm{Ob}\,\underbrace{D_i(M^+(K)),\ \text{et }\in\mathrm{Ob}\,D_n(M^+(K))}_{\text{et }=\text{ mieux}}\quad\forall i
\]

\deleted{$H^i(X,\mathbf{Z}(0))\in$}
\[
\begin{aligned}
H^i(X,\mathbf{Z}(0))&\in\mathrm{Ob}\left[\deleted{\unsure{\xi|\zeta}}M_i^++\unsure{\xi|\zeta}M_{i-1}^++\unsure{\xi|\zeta}^{2}M_{i-2}^+\unsure{+\cdots|+\text{---}}\right]\quad\text{si }i\leq n\\
&\qquad\deleted{M^+_{\unsure{n}}+\unsure{\xi|\zeta}M^+_{\unsure{n-1}}+\unsure{\xi|\zeta}^{2}M^+_{\unsure{n-2}}\unsure{+\cdots|+\text{---}}}\\
&\in\mathrm{Ob}\,\unsure{\xi|\zeta}^{i-n}\left[M^+_{2n-i}+\unsure{\xi|\zeta}M^+_{2n-i-1}+\unsure{\xi|\zeta}^{2}M^+_{2n-i-2}\unsure{\cdots|\text{---}}\right]\quad\text{si }i\geq n
\end{aligned}
\]

\[
\mathrm{cl}\,H^i(X,\mathbf{Z}(0))\in\sum_{i\leq\alpha\leq\mathrm{Inf}(2i,2n)}\mathrm{Gr}_{\unsure{i|\alpha}}(M^+(K))
\]
\margin{plus gén.}
\[
\mathrm{cl}\,H^i(X,M)\in\sum_{\rho+i\leq\alpha\leq\rho+\mathrm{Inf}(2i,\unsure{n|2n})}\mathrm{Gr}_{\unsure{i|\alpha}}
\]
\margin{si $M$ pur de poids $\rho$}
''',[
('top','text','X liss; de dim n partout'),
('upper','display','H^i_! and H^{n+k}_!; two lines under a brace'),
('middle','display','H^i in Ob D_i and Ob D_n; underbrace et = mieux'),
('middle-lower','display','H^i expansion for i <= n; cancelled row; expansion for i >= n'),
('lower','display','cl H^i(X,Z(0)) in sum Gr_i'),
('lower','display','cl H^i(X,M) in sum Gr_i')],remarks='Whole image, both supplied halves, and enlarged header/middle/footer inspected; first visual comparison completed. Some overwritten symbols cannot be uniquely resolved.')
