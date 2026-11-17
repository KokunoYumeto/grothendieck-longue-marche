from save_page import save_page
save_page(57,r'''\scanpage{57}
% archive foliation: 56
\uline{N.B.} a) Ceci ne caractérise pas les données algébriques elles-mêmes, mais seulement les $\mathbf{Q}_\ell$-espaces engendrés.

b) De même, on ne peut caractériser ainsi l'image de $\pi$, mais seulement l'algèbre enveloppante....

Passant à la limite sur les extensions finies de $K$, on trouve
\[
\left\{\begin{aligned}
H^{2i}(\overline{X},\mathbf{Q}_\ell(i))^{\unsure{\mathfrak{g}_\ell|g_\ell}(\overline{K}/K)}&\xleftarrow{\sim} A^i(\overline{X})\otimes_{\mathbf{Q}}\mathbf{Q}_\ell\\
\unsure{\mathcal{U}^i|\mathcal{W}^i}(X)\otimes_{\mathbf{Q}}\mathbf{Q}_\ell\quad&\text{et l'algèbre enveloppante de}\\
&\unsure{\mathfrak{g}_\ell|g_\ell}(\overline{K}/K)\text{ dans }\mathrm{End}_{\mathbf{Q}_\ell}(H^i(\overline{X},\mathbf{Q}_\ell(0)))\\
&\text{sont commutant l'un de l'autre.}
\end{aligned}\right.
\]

\uline{Question} Comment caractériser l'image de $\unsure{\mathfrak{g}_\ell|g_\ell}(\overline{K}/K)$ dans $\mathrm{End}_{\mathbf{Q}_\ell}(H^i(\overline{X},\mathbf{Q}_\ell(0)))$ ??
Cela doit être une sous Algèbre de Lie \uline{réductive}, on peut la considérer comme plongée dans
\[
H^{2n-i}(\overline{X})\otimes H^i(\overline{X})(n).
\]
''',[
('top','text','N.B. a) Ceci ne caractérise pas les données algébriques'),
('upper','text',"b) De même; l'image de pi; l'algèbre enveloppante"),
('middle','text','Passant à la limite sur les extensions finies de K'),
('middle-lower','display','brace: H^{2i} invariants <- A^i; U^i and enveloping algebra mutual commutants'),
('lower','text',"Question Comment caractériser l'image"),
('bottom','text','Cela doit être une sous Algèbre de Lie réductive'),
('bottom','display','H^{2n-i}(Xbar) tensor H^i(Xbar)(n)')],remarks='Whole page and both halves read and compared. The infinitesimal Galois symbol has a long cursive descender; its alphabet remains explicitly doubtful.')
