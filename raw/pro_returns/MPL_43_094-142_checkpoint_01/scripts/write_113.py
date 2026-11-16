from page_work import save_page
text=r'''\scanpage{113}
\deleted{
\unsure{ou}, \inserted{pour tt $x\in X$,} \deleted{\unsure{des}}\inserted{un}
\unsure{élément} \deleted{\unsure{de $\mathcal G_x$}}
$\lambda_x\in\gamma(\deleted{\unsure{\xi}}\xi_x,\xi)
=\operatorname{Is}_K(K(\unsure{O_\xi}),K(\unsure{O_x}))
=\operatorname{Is}_K(K',K(\unsure{O_x}))$,
i.e. donnons nous un \unsure{point-g.} \unsure{certifié}
\deleted{\unsure{de}} de $K'$ au dessus de $x$.

On a une famille d'homomorphismes
\diagram{\begin{tikzcd}[column sep=large]
\varphi_x:\operatorname{Gal}(\overline K_x/K_x)\arrow[r,"\text{épim.}"]&
\operatorname{Gal}(K'/K_x^{\unsure{\mathrm{dec}}})\subset\operatorname{Gal}(K'/K)
\end{tikzcd}}
(homomorphismes de réciprocité).
\margin{application de réciprocité i.e. \unsure{logarithme} local}
\deleted{\unsure{Le groupe}} \deleted{\unsure{Donne}}
\uline{Le groupe \inserted{\uuline{invariant} dans $\operatorname{Gal}(K'/K)$}
engendré par les} $\operatorname{Im}\varphi_x$
\uline{est le} \deleted{\uline{plus gr.}\ \unsure{sous-gr.}}
\inserted{groupe de Galois}
$\operatorname{Gal}(K'\deleted{\unsure{{}_x^{\mathrm{dec}}}}/K_X^{\unsure{\mathrm{D\acute ec}}})$,
\uline{où} $K_X^{\unsure{\mathrm{D\acute ec}}}$ \uline{est la plus grande sous-extension}
\inserted{galoisienne} \uline{de} $K'$, \uline{de} $K$, \uline{qui est complètement}
\deleted{\unsure{en}} \uline{décomposée sur chaque} \deleted{$x\in X$} $x\in X$.

\unsure{De même}, quand on prend les hom. induits par les $\varphi_x$
\diagram{\begin{tikzcd}[column sep=large]
\operatorname{Gal}(\overline K_x/\overline K_x^{i})\arrow[r,"\text{épim}"]&
\operatorname{Gal}(K'/K_x^i)\subset\operatorname{Gal}(K'/K)
\end{tikzcd}}
\uline{on trouve comme groupe \inserted{\uuline{invariant} \unsure{par}} fermé engendré
par les} $\varphi_x(\operatorname{Gal}(\overline K_x/\overline K_x^I))$ \uline{le groupe
de Galois} $\operatorname{Gal}(K'\deleted{\unsure{{}_x}}/K_X^{\unsure{\mathrm{Iner}}})$,
\uline{où} $K_X^{\unsure{\mathrm{Iner}}}$ \uline{est la}
\deleted{\unsure{plus}}
\uline{plus grande sous-extension de} $K'$ \uline{non ramifiée
sur $X$}.
}
\mspage{112}
'''
save_page(113,text,[('deletion','whole sheet','blue draft crossed by long diagonal strokes'),('text','top continuation','ou un élément lambda x'),('insertion','top above first line','pour tt x in X'),('deletion','top article','des'),('insertion','top article','un'),('deletion','top before lambda','de Gx'),('display','upper two lines','lambda x in gamma(xi x,xi)=Is K(K(Oxi),K(Ox))=Is K(Kprime,K(Ox))'),('deletion','gamma argument','xi'),('text','upper paragraph continuation','i.e. donnons nous un point-g. certifié'),('deletion','upper before de Kprime','de'),('text','upper middle','On a une famille d’homomorphismes'),('diagram','upper middle Galois map','phi x Gal(Kbarx/Kx) epim→Gal(Kprime/Kxdec) subset Gal(Kprime/K)'),('text','middle parenthesis','homomorphismes de réciprocité'),('margin note','left sloping','application de réciprocité i.e. logarithme local'),('deletion','middle right','Le groupe'),('deletion','middle left','Donne'),('text','middle underlined assertion','Le groupe engendré par les Im phi x'),('insertion','above groupe engendré','invariant dans Gal(Kprime/K)'),('deletion','middle group description','plus gr. sous-gr.'),('insertion','above group description','groupe de Galois'),('display','middle Galois group','Gal(Kprime/KXDec)'),('deletion','middle Galois numerator','x dec'),('text','middle lower description','où KXDec est la plus grande sous-extension'),('insertion','above de Kprime','galoisienne'),('deletion','before décomposée','en'),('deletion','after chaque','x in X'),('text','lower paragraph opening','De même quand on prend les hom. induits'),('diagram','lower inertia map','Gal(Kbarx/Kbarx i) epim→Gal(Kprime/Kx i) subset Gal(Kprime/K)'),('text','lower underlined assertion','on trouve comme groupe fermé engendré'),('insertion','above groupe fermé','invariant par'),('display','lower image and Galois group','phi x(Gal(Kbarx/KbarxI)); Gal(Kprime/KXIner)'),('deletion','lower Galois numerator','x'),('text','bottom description','KXIner est la plus grande sous-extension de Kprime non ramifiée sur X'),('deletion','bottom before plus grande','plus'),('text','bottom left page number','112')],sheet_kind='cancelled_draft',observations='Whole and both halves read, plus enlarged first lines, central and final statements and rotated sloping margin. Upper/lowercase i/I in the two inertia occurrences is preserved. The field superscript words are overwritten and marked doubtful. Long diagonal strokes cancel the draft as a whole; local revisions are nested separately. The lexical reading point-g. certifié and the marginal logarithme are especially uncertain.')
