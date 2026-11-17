from record import save
save(24,r'''\scanpage{24}
donc le triangle \textcircled{a} ou \textcircled{a'} apparaît comme \uline{autotransposé}.

Appliquons le foncteur oubli, on trouve
\textcircled{c'}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
&L^\bullet\simeq\mathbb R\Gamma(W_0) \arrow[dl]\\
\mathbb R\operatorname{Hom}_{\Lambda}(K^{\bullet\mathrm{oub}},\Lambda)[-2n] \arrow[r] \arrow[d,equal] &K^{\bullet\mathrm{oub}}\simeq\mathbb R\Gamma(M) \arrow[u]\\
\mathbb R\Gamma_!(\mathring M)&
\end{tikzcd}}
\margin{\uline{dire que c'est encore un triangle autotransposé}}

Appliquons $\mathbb R\Gamma^\pi$, on trouve
\margin{[\uline{expliquer} comment ?]}
\textcircled{b'}
\margin{\deleted{\unsure{1}}}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
&L^\bullet\overset{\mathrm L}{\otimes}_{\Lambda}\mathbb R\Gamma(S^1)\simeq L^\bullet\times L^\bullet[-1]\simeq\unsure{I|l} \arrow[dl,"(\alpha',\beta')"']\\
\mathbb R\operatorname{Hom}_{\Lambda}(K^{\bullet\pi},\Lambda)[-2n-1] \arrow[r,very thick] \arrow[d,equal]&K^{\bullet\pi}\simeq\mathbb R\Gamma(P)\simeq\mathbb R\Gamma(W-W_0) \arrow[u,"(\alpha,\beta)",very thick]\\
\mathbb R\Gamma_!(\mathring P)\simeq\mathbb R\Gamma_!(W-W_0)&
\end{tikzcd}}
\margin{\fbox{\begin{minipage}{.33\linewidth}vérifier la commutation de $\mathbb R\Gamma^\pi$ à $\mathbb R\operatorname{Hom}_{\Lambda}(-,\Lambda)=(-)^\vee$\end{minipage}}}
\margin{(triangle autotransposé)}

\deleted{\unsure{Et les} \uline{triangles} \textcircled{d} et \textcircled{e} \uline{deviennent chacun}}

Comme nouvelle \deleted{\unsure{donnée}} \inserted{structure}, ce triangle introduit
\deleted{\diagram{\begin{tikzcd}
u_1:\ \mathbb R\operatorname{Hom}_{\Lambda}(K^\bullet,\Lambda)[-2n-1] \arrow[r] &\unsure{H|K}
\end{tikzcd}}}
\diagram{\begin{tikzcd}[column sep=large]
\boxed{u_1:\ \mathbb R\Gamma(W-W_0)^\vee[-2n-1]\mathbin{-}\mathbb R\Gamma(W-W_0)}
\end{tikzcd}}
et des accouplements
\diagram{\begin{tikzcd}
\boxed{\begin{gathered}
\lambda:\ \mathbb R\Gamma(W_0)\times\mathbb R\Gamma(W-W_0)\mathbin{-}\Lambda[-2n]\\
\mu:\ \mathbb R\Gamma(W_0)\times\mathbb R\Gamma(W-W_0)\mathbin{-}\Lambda[-(2n-1)]
\end{gathered}}
\end{tikzcd}}
\diagram{\begin{tikzcd}
\lambda:\ H^{\deleted{i}\inserted{2n-i}}(W_0)\times H^{\deleted{\unsure{2n-i}}\inserted{i}}(W-W_0) \arrow[r] &\Lambda\\
\mu:\ H^{\deleted{i}\inserted{2n-1-i}}(W_0)\times H^{\deleted{\unsure{2n-1-i}}\inserted{i}}(W-W_0) \arrow[r,dash] &\Lambda
\end{tikzcd}}
i.e.
\diagram{\begin{tikzcd}
\lambda':\ H^{\deleted{\unsure{2n-}}i}(W-W_0) \arrow[r]&H^{i-1}(W_0)&\text{je dis que c'est }\deleted{\unsure{le}}\ \beta\\
\mu':\ H^i(W-W_0) \arrow[r]&H^i(W_0)&\text{je dis que c'est }\alpha
\end{tikzcd}}
\mspage{23}
''',[
('text','top line','donc le triangle a ou a′ apparaît comme autotransposé'),
('text','top','Appliquons le foncteur oubli'),
('diagram','upper triangle c′','L bullet, RHomΛ(K bullet oub,Λ)[−2n], K bullet oub, RΓ!(interior M)'),
('margin note','upper right','dire que c’est encore un triangle autotransposé'),
('text','upper middle','Appliquons RΓ^π, on trouve'),
('margin note','right beside instruction','[expliquer comment ?]'),
('deletion','left near b′','1'),
('diagram','middle triangle b′','L bullet⊗^L RΓ(S¹); RHomΛ(K bullet π,Λ)[−2n−1]; K bullet π; α β α′ β′'),
('margin note','left oblique box','vérifier la commutation de RΓ^π à RHomΛ(−,Λ)=(−)vee'),
('margin note','right below b′','(triangle autotransposé)'),
('deletion','below b′','Et les triangles d et e deviennent chacun'),
('text','middle-lower','Comme nouvelle structure, ce triangle introduit'),
('deletion','after nouvelle','donnée'),
('insertion','above deleted donnée','structure'),
('deletion','above boxed u1','u1:RHomΛ(K bullet,Λ)[−2n−1]→H|K'),
('diagram','boxed u1','u1:RΓ(W−W0)vee[−2n−1]—RΓ(W−W0)'),
('text','above pairings','et des accouplements'),
('diagram','boxed pairings','λ and μ from RΓ(W0)×RΓ(W−W0)'),
('diagram','below box','cohomology pairings λ,μ with revised exponents'),
('deletion','cohomology λ exponents','i; 2n−i'),
('insertion','cohomology λ exponents','2n−i; i'),
('deletion','cohomology μ exponents','i; 2n−1−i'),
('insertion','cohomology μ exponents','2n−1−i; i'),
('text','bottom left','i.e.'),
('diagram','bottom two lines','λ′:H^i(W−W0)→H^{i−1}(W0); μ′:H^i(W−W0)→H^i(W0)'),
('deletion','λ′ source exponent','2n−'),
('deletion','before β identification','le'),
('text','bottom right','je dis que c’est β; je dis que c’est α'),
('margin note','bottom left','23')
],[
('c′, K superscripts','oub','Three small letters appear, rather than a single ω as on scan 020.','medium'),
('b′ top object final sign','I|l','A single vertical stroke follows the final ≃, with no secure foot or dot.','low'),
('left of b′','1 (deleted)','Isolated scribbled numeral/letter; best reading 1.','low'),
('cancelled prose','Et les triangles d et e deviennent chacun','The initial phrase is overlapped by the cancellation zigzag.','medium'),
('after nouvelle','donnée (deleted)','Only parts of the abandoned word remain visible.','low'),
('cancelled u1 target','H|K','Two vertical strokes remain; the expected complex name is not silently supplied.','low'),
('cohomology pairings','revised exponents','Original exponents heavily overwritten; current values and best readings of deleted values are distinguished.','low'),
('before β','le (deleted)','Small black retraced word, possibly an abandoned article.','low')
],['Author explicitly asks expliquer comment ? after applying derived invariants.','The boxed margin explicitly says vérifier la commutation of derived invariants with derived Λ-duality.','The triangle carries duality shift −2n−1 after invariants; do not normalize it to a dimension argument.','λ′ is identified with β and μ′ with α without proof here.'])
