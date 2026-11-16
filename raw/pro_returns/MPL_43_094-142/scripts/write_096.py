from page_work import save_page
text=r'''\scanpage{96}
On va définir un foncteur fondamental \inserted{dit \uline{de Néron}}
\[
\mathcal N:C(S)\longrightarrow C'(k).
\]
Pour ceci, si $F$ est un faisceau de Weil sur $S$, on définit un faisceau
de Weil sur $\mathcal T_k$ en prenant, pour tt anneau \unsure{comm.} $A$ sur $k$
\inserted{\[
\simeq F(\varinjlim_{P}\mathbb V(A^P))
=F(\varprojlim_{P}\operatorname{Spec}(\mathbb V(A^P)))
\qquad\inserted{\operatorname{Spec}(\varinjlim_{P}\mathbb V(A^P))}
\]}
\[
\begin{aligned}
\mathcal N(F)(A)&=\varinjlim_{P}
 F\left(\unsure{\operatorname{Spec}}\left(\mathbb V
 \left(\underbrace{\prod_{i\in I_P} A_i^P}_{A^P}\right)\right)\right)\\
 &=\underline{\lim}_{P}\prod_{i\in I_P}F(\mathbb V(A_i^P)).
\end{aligned}
\]
\margin{N.B. On a en fait une ``application continue''
$\mathcal T'_k\longrightarrow\mathcal T_S$, \unsure{correspondant}
aux \unsure{pro-objets}, d'où le foncteur image directe de faisceaux, et
ses propriétés ``formelles''\ldots ! ? !}

$P$ parcourt les ``partitions constructibles finies'' de $A$, et où pour
une telle $P$, $I_P$ est son ensemble d'indices, et $A_i^P$ les composantes
correspondantes de $A$. En d'autres termes, un \unsure{quasi-schéma}
\unsure{flasque} \inserted{cpt} étant considéré comme un pro-(schéma affine)
sur $k$, on le transforme par $\mathbb V$ en un pro (schéma affine) sur $S$,
et on lui applique le foncteur $F$.
\deleted{[N.B. $\mathcal N(F)$ est compatible \unsure{avec} les limites
inductives d'anneaux \unsure{donc si on y tient}, on peut se limiter}
\margin{Non, car le foncteur $\mathbb V:k\text{-alg}\longrightarrow V\text{-alg.}$
ne commute pas aux limites inductives\ldots}
\mspage{95}
'''
save_page(96,text,[('text','top','On va définir un foncteur fondamental'),('insertion','top right curved bracket','dit de Néron'),('display','upper','N:C(S)→C prime(k)'),('text','upper middle','Pour ceci si F est un faisceau'),('insertion','above main display','F(lim V(A P))=F(lim Spec(V(A P)))'),('insertion','right above inserted equation','Spec(lim V(A P))'),('display','middle two lines','N(F)(A)=lim F(Spec(V(product A i P)))'),('margin note','left diagonal bracket','N.B. On a en fait une application continue'),('text','lower half','P parcourt les partitions constructibles finies'),('insertion','lower after flasque','cpt'),('deletion','bottom across page','N.B. N(F) est compatible'),('margin note','bottom left','Non car le foncteur V'),('text','bottom left page number','95')],observations='Whole, halves, enlarged formula, rotated left margin, lower paragraph and footnote read. The double-stroked V is retained as mathbb V, the partition sign as P. The lower displayed lim has an underline without a safely visible arrowhead. The two upper formula insertions are retained separately; their exact attachment is uncertain and will be checked during audit.')
