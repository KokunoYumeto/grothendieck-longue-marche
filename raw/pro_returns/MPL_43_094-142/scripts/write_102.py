from page_work import save_page
text=r'''\scanpage{102}
\noindent 9) \uline{Application 1} L'isom.
$H^i(K,\gamma_K)\longrightarrow\operatorname{Ext}^i_{k\text{-gr}}(J_{K/k},\unsure{\gamma})$

\deleted{et le corps de classes de Serre}

(\unsure{Théorie} des corps de classes de Serre)

\margin{?\quad\figure{\begin{tikzpicture}\draw (0,0)--(.5,.2);\draw (0,-.04)--(.5,.16);\end{tikzpicture}}}
\noindent 10) \uline{Application 2} Autodualité de
\deleted{$\unsure{H^1}$}
$W_n(K)/F^mW_{\unsure{n}}(\unsure{K})$

\noindent 11) \uline{Application} 3 Cohomologie des V.A.

\noindent 12) L'isom de Lang \deleted{pour \unsure{un corps}}
\inserted{(sur corps $k$ fini)}

\noindent 13) \uline{Application} 4 Dualité de Tate.

\noindent 14) \uline{Compléments en égales caractéristiques}
\inserted{\uline{Théorie de Rosenlicht locale}}
\[
H^i(K,\gamma_K)\simeq\operatorname{Ext}^i_{k\text{-gr}}(J_{K/k},\gamma)
\]
\margin{?}
pour $i>0$, tt $k$-groupe $\gamma$, grâce à l'\unsure{isom}
canonique de $J(K)/J(V)'$.

\deleted{\[
\unsure{\mu_p\otimes\mu_p}\\
\unsure{\underline{\operatorname{Hom}}(\mu_p\otimes\mu_p,G_m)}
\unsure{\simeq}\unsure{\operatorname{Hom}(\mu_p,\mathbb Z/p\mathbb Z)}
\]}
\[
\left[\begin{array}{ll}
\uline{\text{Lang}}:&\text{\unsure{géom.} des corps de classes \unsure{prim.} globale par Rosenlicht + Lang}\\
\uline{\text{Serre}}:&\text{\unsure{géométrisation|généralisation} des corps de classes locale}\\
\uline{\text{Tate}}:&\text{Dualité de la cohomologie des V.A. sur un}\\
&\text{corps \unsure{p adique}.}
\end{array}\right.
\]
\mspage{101}
'''
save_page(102,text,[('text','top item 9','Application 1 L’isom'),('display','top right clipped','Hi(K,gamma K) to Ext i k-gr(J K/k,gamma)'),('deletion','below item 9','et le corps de classes de Serre'),('text','parenthetical beneath item 9','Théorie des corps de classes de Serre'),('text','upper item 10','Application 2 Autodualité'),('deletion','item 10 before W','H1'),('margin note','left item 10','question mark'),('drawing','left item 10','double slanted emphasis'),('text','upper middle item 11','Application 3 Cohomologie des V.A.'),('text','middle item 12','L’isom de Lang'),('deletion','item 12','pour un corps'),('insertion','above item 12 ending','sur corps k fini'),('text','middle item 13','Application 4 Dualité de Tate'),('text','middle lower item 14','Compléments en égales caractéristiques'),('insertion','below item 14 heading','Théorie de Rosenlicht locale'),('display','lower','Hi(K,gamma K) ≃ Ext i k-gr(J K/k,gamma)'),('margin note','left of lower display','question mark'),('text','lower beneath display','pour i>0 tt k-groupe'),('deletion','bottom above bracket','mu p tensor mu p; Hom formulas'),('display','bottom bracketed list','Lang; Serre; Tate'),('text','bottom left page number','101')],observations='Whole and halves reread; bottom pencil formula and clipped right-hand item 10 enlarged. The cancelled pencil calculation is exceptionally faint and its symbols remain low-confidence. Formula endpoints at the right paper edge are marked where clipped. This is the continuation of the outline, not a cover with a printed title.')
