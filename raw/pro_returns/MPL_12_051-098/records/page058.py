from save_page import save_page
save_page(58,r'''\scanpage{58}
% archive foliation: 57
\deleted{
dimensionnel $\leq n-2p$, donc que les $\mathrm{gr}^{p}_{\unsure{\Phi}}(H^n(X,\mathbf{Z}(0)))$ sera \deleted{\unsure{par un type}} de type \uline{dimensionnel} \uline{purement} \uline{$n-2p$}. Or de façon précise, on sait qu'il est de \uline{poids} $n$, d'autre part le terme
\[
E_1^{pq}=\unsure{\coprod|\bigoplus}_{x\in X(p)}H^{n-2p}(x,\mathbf{Z})\unsure{(-p)}
\]
\deleted{\unsure{Groupe}} (où $q=n-p$) élément de $M^+(X)$ est \unsure{en fait} dans
\[
\unsure{\xi|\zeta}^{p}\left[M^+_{n-2p}+\unsure{\xi|\zeta}M^+_{\unsure{n-2p-1}}+\cdots\right]
\]

\diagram{\begin{tikzcd}
H^{\unsure{i|j}}_Y(X) \arrow[r,dash] & H^{\unsure{i|j}}(X) \arrow[r,dash] & H^{\unsure{i|j}}(U) \arrow[r,dash] & H^{\unsure{i+1|j+1}}_Y(X)
\end{tikzcd}}
\diagram{\begin{tikzcd}
H^i_!(Y) & H^i_!(X) \arrow[l] & H^i_!(U) \arrow[l] & H^{\unsure{i-1}}_!(Y) \arrow[l]
\end{tikzcd}}

\[
j\leq n\qquad i\geq n>\dim Y=n-1\qquad i+j=2n
\]
\[
\begin{gathered}
H^i_!(Y)\in\unsure{\xi|\zeta}^{i-n}M^+_{2n-i}\qquad\deleted{\unsure{i+j}}\\
\unsure{\cap|\supset}\\
\unsure{\xi|\zeta}^{i-n}M^+_{2n-i-2}=\unsure{\xi|\zeta}^{i-n}M^+_{j-2}
\end{gathered}
\]
\[
H^{i-1}_!(Y)\in\unsure{\xi|\zeta}^{i-n-1}M^+_{2n-(i-1)-2}=\unsure{\xi|\zeta}^{i-n-1}M^+_{j-1}
\]
si $i$
}
''',[
('top; cancelled portrait text','text','dimensionnel <= n-2p; gr^p; type dimensionnel purement n-2p'),
('upper-right edge','display','E_1^{pq} = coproduct H^{n-2p}(x,Z)(-p)'),
('middle portrait','text','où q=n-p; élément de M^+(X)'),
('middle portrait','display','xi^p[M^+_{n-2p}+xi M^+_{n-2p-1}+...]'),
('rotated block; first row','diagram','H_Y^i(X) -- H^i(X) -- H^i(U) -- H_Y^{i+1}(X)'),
('rotated block; second row','diagram','H_!^i(Y) <- H_!^i(X) <- H_!^i(U) <- H_!^{i-1}(Y)'),
('rotated block; upper right','display','j <= n; i >= n > dim Y = n-1; i+j=2n'),
('rotated block; middle','display','H_!^i(Y) in xi^{i-n}M^+_{2n-i}; cap; equality of lower terms'),
('rotated block; lower','display','H_!^{i-1}(Y) in xi^{i-n-1}M^+_{2n-(i-1)-2}'),
('rotated block; bottom','text','si i')],sheet_kind='cancelled_draft',remarks='Whole page and both halves read; sheet also rotated clockwise for the transverse calculations. Enlarged transverse block and right-edge E_1 formula inspected. The top sequence visibly uses strokes without arrowheads, retained as dashes.')
