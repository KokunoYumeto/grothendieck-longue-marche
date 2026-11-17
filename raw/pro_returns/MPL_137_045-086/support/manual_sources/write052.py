import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{52}
% archive foliation: 51
\deleted{foncteurs admissibles étant maintenant
les foncteurs $\Sigma$-exacts.)}
\deleted{\uline{Indications sur dém.}
Dans $\mathcal P_\bullet$, il est évident que \uline{$C_\bullet^\bullet$ est une}
\uline{$\Sigma_\bullet$-spéciale résolution}. De façon précise,
si
\[
\unsure{\longrightarrow|-}\Psi_\bullet^i=\deleted{\unsure{H}(C_\bullet^i)\longrightarrow}\ k\deleted{[i]}\text{ placé en degré }i
\]
on voit que $\unsure{\Psi_\bullet^{-1}}=0$, et des suites $\in\Sigma_\bullet$
\[
\begin{aligned}
0&\unsure{-|\longrightarrow}\Psi_\bullet^0\longrightarrow C_\bullet^0\longrightarrow\Psi_\bullet^1\unsure{-|\longrightarrow}0\\
&\qquad0\longrightarrow\Psi_\bullet^1\unsure{-|\longrightarrow}C_\bullet^1\longrightarrow\Psi_\bullet^2\longrightarrow0\\
&\qquad\qquad0\unsure{-|\longrightarrow}\Psi_\bullet^2\unsure{-|\longrightarrow}C_\bullet^2\unsure{-|\longrightarrow}\Psi_\bullet^3\longrightarrow0.
\end{aligned}
\]
De plus, on voit que pour $L_\bullet\in\operatorname{Ob}\mathcal P_\bullet$,
$L_\bullet$ peut s'écrire comme extension successive
d'objets de la forme $(\Psi_\bullet^i)^{\unsure{r_i|\rho_i}}$ pour la
filtration croissante
\[
\operatorname{Fil}_i(L_\bullet)_j=\begin{cases}L_j&\text{si }j\leqslant i\\0&\text{si }j>i\end{cases}
\]
on a un isom can
\[
\deleted{\unsure{Fil}}\operatorname{Gr}_i(L_\bullet)\simeq L_i\text{ placé en degré }i
\underset{\mathrm{can}}{\simeq}\Psi_\bullet^i\otimes L_i
\underset{\text{non can}}{\simeq}(\Psi_\bullet^i)^{\unsure{r_i|\rho_i}}
\]
\uline{Enfin}, les \deleted{$\unsure{Q}$} $C_\bullet^i$ sont $\Sigma_\bullet$-projectifs.
Soit $B^\bullet_{\Sigma\text{-\unsure{nex|lex}}}$ (resp. $B^\bullet_{\Sigma\text{-ex}}$) les sous-catégories
pleines de $B^\bullet$ décrites dans a) (resp. b)).
On va définir des foncteurs
}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\deleted{B^\bullet_{\Sigma\text{-\unsure{nex|lex}}}}\arrow[r]\arrow[d,hook]&
\deleted{\underline{\operatorname{Hom}}_{\Sigma\text{-\unsure{lex}}}(\mathcal P_\bullet,B)}\arrow[d,hook]\\
\deleted{B^\bullet_{\Sigma\text{-ex}}}\arrow[r]&
\deleted{\underline{\operatorname{Hom}}_{\Sigma\text{-ex}}(\mathcal P_\bullet,B)}
\end{tikzcd}}
\deleted{(le premier induisant le deuxième)}
'''
save(52,text,[('deletion','entire sheet diagonal cancellation','whole draft'),('text','top continuation','foncteurs admissibles'),('text','upper heading','Indications sur dém.'),('text','upper paragraph','Dans P il est évident'),('display','upper quarter','Psi_i = k placé en degré i'),('deletion','within definition','H(C_i)→'),('deletion','after k','[i]'),('text','upper middle','on voit que Psi^{-1}=0'),('display','middle staggered','three Psi-C-Psi short sequences'),('text','lower middle','De plus on voit que'),('display','lower middle','Fil_i(L)_j cases'),('text','below filtration','on a un isom can'),('display','lower quarter','Gr_i(L) ≃ L_i ≃ Psi tensor L_i'),('deletion','before Gr','Fil'),('text','lower quarter','Enfin les C_i'),('deletion','before C_i','Q'),('text','bottom','Soit B_{Sigma-nex}'),('text','bottom before diagram','On va définir des foncteurs'),('diagram','bottom','B_nex B_ex Hom_lex Hom_ex'),('text','bottom final','le premier induisant le deuxième')],sheet_kind='cancelled_draft')
