from save_page import save_page
save_page(65,r'''\scanpage{65}
% archive foliation: 64
$X$ étant projectif et lisse sur $k$ alg. clos, morphisme structural $f:X\longrightarrow\mathrm{Spec}\,k$.

\uline{Une autre façon est celle-ci}
\[
\boxed{A^i(X)\deleted{\otimes\mathbf{Q}_\ell}\simeq\mathrm{Im}\left[H^{2i}(X,\mathbf{Q}(i))\longrightarrow H^{2i}(X,\mathbf{Q}_\ell(i))\right]}
\]

\uline{NB.} Si $k$ est la clôture algébrique de $\mathbf{F}_p$, \unsure{on devrait} pour $X$ projectif lisse sur $k$
\[
H^{\unsure{i|2i}}(X,\mathbf{Q}(j))\inserted{\nearrow\ \uline{\text{pas}}\ \mathbf{Q}_\ell(i)!}=
\begin{cases}
0&\text{si }i\ne 2j,2j+1\\
A^i(X)\otimes_{\mathbf{Z}}\mathbf{Q}&\text{si }i=2j\quad\text{(canonique)}\\
A^{\unsure{i|j}}(X)\otimes_{\mathbf{Z}}\mathbf{Q}&\text{si }i=2j+1\quad\text{(\uline{pas} canonique)}
\end{cases}
\]
De plus, pour $i\ne 2j$, l'image de $H^i(X,\mathbf{Q}(j))$ dans $H^i(X,\mathbf{Q}_\ell(j))$ est nulle.

C'est un \uline{fait général} : si $k$ alg. clos, alors (si $X$ projectif lisse sur $k$) l'image de
\[
H^{\unsure{j|i}}(X,\mathbf{Q}(\unsure{i|j}))\longrightarrow H^{\unsure{j|i}}(X,\mathbf{Q}_\ell(i))
\]
est \uline{nulle} pour $j\ne 2i$ (question de poids) ; pour $j=2i$ ce sont les cycles algébriques \inserted{à coeffs} rationnels.
''',[
('top','text','X étant projectif et lisse'),
('upper','text','Une autre façon est celle-ci'),
('upper middle','display','A^i(X) ≃ Im[H^{2i}(X,Q(i)) → H^{2i}(X,Q_l(i))]'),
('middle','text','NB. Si k est la clôture algébrique de F_p'),
('middle','display','H^i(X,Q(j)) = three cases'),
('lower middle','text','De plus, pour i ≠ 2j'),
('lower','text','C’est un fait général'),
('lower','display','H^j(X,Q(i)) → H^j(X,Q_l(i))'),
('bottom','text','est nulle pour j ≠ 2i')
],remarks='Whole and halves inspected, formulas enlarged. Several exponents are overwritten, retained with alternatives. Faint mirrored typescript is bleed-through from verso, not live writing on this face.')
