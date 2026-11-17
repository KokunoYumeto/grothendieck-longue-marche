from save_page import save_page
save_page(75,r'''\scanpage{75}
% archive foliation: 74
On s'attend donc à pouvoir écrire $A(S)\otimes_{\mathbf{Z}}\mathbf{Q}$ en termes de ce motif $M$.
\unsure{Or|Et} en effet, des raisons heuristiques convaincantes \deleted{\unsure{que}} nous suggèrent
\[
A(S)\otimes_{\mathbf{Z}}\mathbf{Q}\simeq H^1(S,T_{\mathrm{mot}}(A))
\]
[NB. On doit avoir $H^0(S,T_{\mathrm{mot}}(A))=0$, à cause de \deleted{Mordell--Weil} considérations de poids ---].
\deleted{Une autre façon de} \inserted{Considérons \unsure{donc} le processus} \unsure{(aux $\ell$ inversibles à $X$)}
\diagram{\begin{tikzcd}[column sep=small]
\unsure{0|\varnothing}\arrow[r]&{}_{\ell^\nu}A\arrow[r,dash]&A\arrow[r,dash]&A\arrow[r,dash]&0
\end{tikzcd}}
d'où
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r]&H^0(S,A)_{\ell^\nu}\arrow[r,dash]&H^1(S,{}_{\ell^\nu}A)\arrow[r]&{}_{\ell^\nu}H^1(S,A)\arrow[r,dash]&0
\end{tikzcd}}
et par passage à la limite et $\otimes_{\mathbf{Z}_\ell}\mathbf{Q}_\ell$
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r]&\underbrace{H^0(S,A)}_{\substack{\text{de type fini}\\\text{sur }\mathbf{Z}}}\otimes_{\mathbf{Z}}\mathbf{Q}_\ell\arrow[r]&H^1(S,T_\ell^{\deleted{\unsure{\mathbf{Q}}}}(A))_{\mathbf{Q}_\ell}\arrow[r]\arrow[d,phantom,"\wr" description]&T_{\unsure{\ell|\cdot}}^{\deleted{\unsure{\mathbf{Q}}}}(H^1(S,A))_{\mathbf{Q}_\ell}\arrow[r]&0\\
&&H^1(S,T_{\mathrm{mot}}(A))\otimes_{\mathbf{Q}}\mathbf{Q}_\ell&&
\end{tikzcd}}
et le résultat escompté ici équivaut visiblement à celui-ci :
\[
\boxed{\begin{array}{l}
H^1(S,A)(\ell)\quad\uuline{\text{fini}}\quad\text{si }\ell\text{ ``premier à }S\text{''}\\
\hfill(S\text{ de type fini sur }\mathrm{Spec}\,\mathbf{Z})
\end{array}}
\]
p.ex. si $S=\mathrm{Spec}\,\mathbf{F}_q$, alors il est vrai par Lang !
''',[
('top','text','On s’attend donc à pouvoir écrire'),
('upper','text','Or en effet, des raisons heuristiques'),
('upper middle','display','A(S) tensor Q ≃ H^1(S,T_mot(A))'),
('middle','text','NB. On doit avoir H^0=0'),
('middle','text','Une autre façon de; Considérons donc le processus'),
('middle','diagram','0 → _{l^ν}A — A — A — 0'),
('middle lower','text','d’où'),
('lower middle','diagram','0 → H^0(S,A)_{l^ν} — H^1(S,_{l^ν}A) → torsion H^1 — 0'),
('lower','text','et par passage à la limite'),
('lower','diagram','0 → H^0 tensor Q_l → H^1(S,T_l(A)) → T_l(H^1(S,A)) → 0'),
('lower','text','et le résultat escompté ici équivaut'),
('bottom','display','H^1(S,A)(l) fini si l premier à S'),
('bottom','text','p.ex. si S=Spec F_q')
],remarks='Whole, halves and two enlargements inspected. Clause before first sequence has difficult wording. Plain strokes in first two exact sequences preserved as dashes. Superscript Q cancellations in T symbols explicitly marked.')
