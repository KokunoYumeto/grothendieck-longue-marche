from save_page import save_page
save_page(77,r'''\scanpage{77}
% archive foliation: 76
Si $S$ de type fini sur $\mathbf{F}_p$, on obtient le diagramme suivant
\margin{(b)}
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&M^\pi\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell\arrow[d,phantom,"\wr" description]&&&\\
0\arrow[r]&H^0(S,A)\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell\arrow[r,dash]\arrow[d]&H^1(S,{}_{\ell^\infty}A)\arrow[r,dash]\arrow[d]&H^1(S,A)(\ell)\arrow[r,dash]\arrow[d]&0\\
0\arrow[r,dash]&(H^0(\overline{S},\overline{A})\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell)^\pi\arrow[r,dash]\arrow[d,phantom,"\wr" description]&H^1(\overline{S},{}_{\ell^\infty}\overline{A})^\pi\arrow[r,dash]&H^1(\overline{S},\overline{A})(\ell)^\pi\arrow[r,dash]&0\\
&(M\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell)^\pi&&&
\end{tikzcd}}
\figure{\begin{tikzpicture}[x=1mm,y=1mm]\draw (0,0)--(.2,3);\draw (0,2)--(2,2);\draw (.2,3)--(2,3.2);\end{tikzpicture}}

[où $M=H^0(\overline{S},\overline{A})/H^0(\overline{\mathbf{F}}_p,\overline{A}^{\mathrm{fix}})$, $\pi$ est le groupe de Galois de $\overline{\mathbf{F}}_p$ sur $\mathbf{F}_p$]

Les déterminations $H^0(S,A)\simeq M^\pi$ et $H^0(\overline{S},\overline{A})\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell\simeq M\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell$ sont \unsure{standart|standard} ; on sait que la première flèche verticale est un isomorphisme mod groupes finis. D'autre part, on trouve (suite spectrale de Leray de $f:S\longrightarrow\mathrm{Spec}\,\mathbf{F}_p$ pour la \uline{top. étale})
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r,dash]&H^1(\mathbf{F}_p,R^0f_*(A))\arrow[r,dash]\arrow[d,phantom,"\wr" description]&H^1(S,A)\arrow[r,dash]&H^0(\mathbf{F}_p,R^1f_*(A))\arrow[r,dash]\arrow[d,phantom,"\Vert" description]&0\\
&\text{groupe fini}&&H^1(\overline{S},\overline{A})^\pi_{\deleted{\unsure{\pi}}}&
\end{tikzcd}}
\inserted{$\curvearrowright$ comme on voit utilisant}
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r,dash]&\unsure{\overline{A}|\widetilde{A}}^{\mathrm{fix}}\arrow[r,dash]&R^0f_*(A)\arrow[r,dash]&M\arrow[r,dash]&0
\end{tikzcd}}
, et le
''',[
('top','text','Si S de type fini sur F_p'),
('upper through middle','diagram','two exact rows with vertical maps; M^π and (M tensor Q_l/Z_l)^π'),
('below second diagram row','drawing','small isolated pen strokes'),
('middle','text','où M=H^0(Sbar,Abar)/H^0(Fpbar,Abar^fix)'),
('middle lower','text','Les déterminations ... sont standart'),
('lower','diagram','0 — H^1(F_p,R^0f_*A) — H^1(S,A) — H^0(F_p,R^1f_*A) — 0'),
('bottom','text','comme on voit utilisant'),
('bottom','diagram','0 — Abar^fix — R^0f_*(A) — M — 0'),
('bottom right','text',', et le')
],remarks='Whole and halves compared. Most horizontal connectors lack visible arrowheads and are kept as dashes; three vertical arrows have heads. Final fixed-part accent and cancelled lower π uncertain.')
