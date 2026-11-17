from save_page import save_page
save_page(76,r'''\scanpage{76}
% archive foliation: 75
Si $S$ est de type fini sur $\mathbf{F}_p$, on aura (travaillant avec des \uline{faisceaux étales}) si $f:S\longrightarrow\mathrm{Spec}\,\mathbf{F}_p$
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r]&H^1(\mathbf{F}_p,R^0f_*A)\arrow[r]&H^1(S,A)\arrow[r]&H^0(\mathbf{F}_p,R^1f_*(A))\arrow[r]\arrow[d,phantom,"\Vert" description]&0\ \deleted{\unsure{H^2(\mathbf{F}_p,R)}}\\
&&&H^1(\overline{S},\overline{A})^\pi&
\end{tikzcd}}
Or on a, tjrs par ``Kummer''
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r]&\overset{\inserted{M\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell}}{H^0(\overline{S},\overline{A})\otimes\mathbf{Q}_\ell/\mathbf{Z}_\ell}\arrow[r,dash]&H^1(\overline{S},{}_{\ell^\infty}\overline{A})\arrow[r]&H^1(\overline{S},\overline{A})(\ell)\arrow[r]&0
\end{tikzcd}}
d'où le fait que $H^1(\overline{S},\overline{A})(\ell)$ est de poids $1-1=0$ \inserted{si p.ex. $S$ est projectif lisse sur $\mathbf{F}_p$} --- à priori rien ne s'oppose à ce qu'il y ait un gros module d'invariants. D'autre part, on a
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r,dash]&\underbrace{A^{\mathrm{fix}}}_{\substack{\unsure{\text{partie fixe}}\\\text{de la V.A. }A\text{ sur }S}}\arrow[r]&R^0f_*(A)\arrow[r]&\underbrace{M}_{\substack{\pi\text{-module,}\\\text{de type fini sur }\mathbf{Z}}}\arrow[r,dash]&0
\end{tikzcd}}
d'où
\diagram{\begin{tikzcd}[column sep=small]
H^1(\mathbf{F}_p,A^{\mathrm{fix}})\arrow[r,dash]\arrow[d,phantom,"\Vert" description]&H^1(\mathbf{F}_p,R^0f_*(\unsure{M|A}))\arrow[r]&H^1(\mathbf{F}_p,M)\arrow[r]\arrow[d,phantom,"\Vert" description]&0\\
\substack{0\\\text{par Lang}}&&(\underline{M}\otimes\mathbf{Q}/\mathbf{Z})^\pi&
\end{tikzcd}}
''',[
('top','text','Si S est de type fini sur F_p'),
('upper middle','diagram','0 → H^1(F_p,R^0 f_*A) → H^1(S,A) → H^0(F_p,R^1f_*A) → 0'),
('middle','text','Or on a, tjrs par Kummer'),
('middle','diagram','0 → H^0 tensor Q_l/Z_l → H^1(l∞Abar) → H^1(Abar)(l) → 0'),
('middle lower','text','d’où le fait que H^1(Sbar,Abar)(l) est de poids 1−1=0'),
('lower','diagram','0 — A^fix → R^0 f_*(A) → M — 0 and under-object labels'),
('bottom','text','d’où'),
('bottom','diagram','H^1(F_p,A^fix) — H^1(F_p,R^0f_*(M)) → H^1(F_p,M) → 0')
],remarks='Whole and halves inspected; label under A^fix enlarged. Last f_* argument visibly resembles M, retained as first alternative despite possible A. End of first sequence heavily cancelled and only partial formula recoverable.')
