from record import save_page
tex=r'''\scanpage{11}
\mspage{5}
% archive foliation: 10
\deleted{$\unsure{HC|H^C}$}
\diagram{\begin{tikzcd}A\arrow[r,hook,"\text{pl fid}"']&B\end{tikzcd}}
\[
x\in B\qquad H_x\in\widehat A\qquad H_x(a)=\mathrm{Hom}_B(a,x)
\]
\[
H^x\in A^\vee\qquad H^x(\cdot)=\mathrm{Hom}_B(a,x)
\]
\[
H_x(a)\times H^x(b)\xrightarrow{\alpha_x}\mathrm{Hom}_A(a,b)
\]
Soit $\widetilde A_{\deleted{\unsure{*}}}$ la catégorie des triples $(H_*,H^*,\alpha)$
\[
H_*\in\widehat A,\quad H^*\in A^\vee,\quad
\alpha:H_*(a)\times H^*(b)\longrightarrow\mathrm{Hom}_A(a,b)
\]
(bifonctoriel)

les flèches
\[
(H_*,H^*,\alpha)\xrightarrow{\varphi}(H'_*,H'^*,\alpha')
\]
étant données par
\[
\left\{\begin{aligned}
\varphi_*:H_*&\longrightarrow H'_*&&\text{dans }\widehat A\\
\varphi^*:H'^*&\longrightarrow H^*&&\text{dans }A^\vee
\end{aligned}\right.
\]
tels que \deleted{\unsure{l'}} l'on ait
\margin{\diagram{\begin{tikzcd}[row sep=small,column sep=small]
a\arrow[d,"u"']\arrow[dr,"(u')"]&\\
x\arrow[r]\arrow[d,"(v)"']&x'\arrow[dl,"v'"]\\
b&
\end{tikzcd}}}
\diagram{\begin{tikzcd}[row sep=large,column sep=small]
\unsure{u\in}\ \deleted{\unsure{a}}H_*(a)\arrow[d,"\varphi_*"']&\times&H^*(b)\arrow[rr,no head,"\alpha_{a,b}"]&&\mathrm{Hom}(a,b)\arrow[d,equal]\\
H'_*(a)&\times&H'^*(b)\arrow[u,"\varphi'_*"']\arrow[rr,no head,"\alpha'_{a,b}"']&&\mathrm{Hom}(a,b)\\
&&\unsure{v'}\arrow[u,phantom,"\in" description]&&
\end{tikzcd}}
\[
\alpha_{a,b}(u,\varphi'_*(\unsure{v'|u'}))=\alpha'_{a,b}(\varphi_*(u),\unsure{v'|u'})
\]
\deleted{Soit $\unsure{A^\sim}$}
Pour un foncteur pl. fid \(A\xrightarrow{\varphi}B\), on déduit un foncteur
\[
\begin{aligned}
\varphi^{\unsure{\sharp|G}}:B&\longrightarrow\widetilde A\\
x&\longmapsto(\varphi^*_{\unsure{(!)}}(x),\varphi^{\circ *}(x),\alpha_x)
\end{aligned}
\]
'''
el=[('deletion','top left','HC'),('diagram','top left','A ↪ B, pl fid'),('display','top upper','x∈B; H_x∈Ahat; H_x(a)=Hom_B(a,x)'),('display','top lower','H^x∈Avee; H^x(·)=Hom_B(a,x)'),('display','upper','H_x(a)×H^x(b) → alpha_x Hom_A(a,b)'),('text','upper middle','Soit Atilde la catégorie des triples'),('deletion','Atilde subscript','*'),('display','middle','H_*∈Ahat; H^*∈Avee; alpha bifonctoriel'),('text','middle','les flèches'),('display','middle','(H_*,H^*,alpha) → phi (H′_*,H′*,alpha′)'),('text','middle','étant données par'),('display','middle lower','phi_*:H_*→H′_*; phi*:H′*→H*'),('text','lower','tels que l’on ait'),('deletion','above l’on','l′'),('diagram','left margin','a → x → x′ → b, u,u′,v,v′'),('diagram','lower','H_*(a) × H*(b) — Hom(a,b) and primed row'),('insertion','lower diagram factor annotations','u∈ and v′∈'),('deletion','lower diagram left','a'),('display','lower compatibility','alpha_a,b(u,phi′_*(v′))=alpha′_a,b(phi_*(u),v′)'),('deletion','bottom above Pour','Soit Atilde'),('text','bottom','Pour un foncteur pl. fid A→phi B, on déduit'),('display','bottom','phi^sharp:B→Atilde; x↦(phi*(x),phi°*(x),alpha_x)')]
save_page(115,11,tex,el,doubts=[('top cancelled','HC','H^C','low'),('H^x definition','Hom_B(a,x)','same order as preceding H_x definition, retained as seen','high'),('triple category subscript','cancelled *','overwritten small mark','low'),('compatibility right vertical arrow','varphi′_*','prime and lower star clear, differs from definition varphi^*','medium'),('compatibility argument','v′','u′','medium'),('bottom functor superscript','sharp','G / 4-shaped sign','low'),('bottom first phi* annotation','(!)','tiny marks below the first phi*','low')],notes='Defines the triple category Atilde from H_*∈Ahat, H^*∈Avee and a bifunctorial composition pairing into Hom_A. Morphisms have opposite variance on H^*. Shows functor induced by fully faithful A→B. H^x definition appears to repeat Hom_B(a,x), although later pairing would suggest the opposite variance; retained literally. Compatibility uses a visibly primed phi with lower star instead of the previously defined phi^*: retained, requiring later reading/mathematical note only.')
