from page_work import save_page
text=r'''\scanpage{130}
\deleted{
Soit un elt $\unsure{f|\varphi}\in\operatorname{Ext}^i(C;G,S\unsure{\tau|\sigma})$, i.e. un hom de degré $i$ $G\mathrel{-}S\unsure{\tau|\sigma}$, d'où un hom de degré $i$ $Rf_*G\mathrel{-}Rf_*S\unsure{\tau|\sigma}$, donc il reste à définir un hom de degré $0$
\[
Rf_*S\unsure{\tau|\sigma}=Rf_*(\unsure{\tau|\sigma}\otimes\mu_n(1))\longrightarrow\unsure{\tau|\sigma}
\]
\[
R^{\unsure{i}}
\]
i.e. un élément de
\[
\operatorname{Ext}^2(k,Rf_*(\unsure{\tau|\sigma}\otimes\mu_n),\unsure{\tau})\mathrel{-}\quad---
\]
}
On a un hom \unsure{évident}
\[
\underline E_f(G,S\unsure{\tau|\sigma})\mathrel{-}E_f(Rf_*G,Rf_*S\unsure{\tau|\sigma})
\]
et si nous définissons un élément
\[
\gamma\in\deleted{\unsure{\operatorname{Ext}^0}}\inserted{\operatorname{Hom}^0}(Rf_*S\unsure{\tau|\sigma},\unsure{\tau|\sigma})
\]
nous en déduisons un \deleted{élément} hom
\[
E_f(Rf_*G,Rf_*S\unsure{\tau|\sigma})\mathrel{-}E_f(Rf_*G,\unsure{\tau|\sigma})
\]
et en composant, on trouve l'hom voulu
\[
E_f(G,S\unsure{\tau|\sigma})\longrightarrow E_f(Rf_*G,\unsure{\tau|\sigma})
\]
Ceci dit, le th. de dualité s'énonce

\uline{Th.} (i) Si $G$ est \inserted{un \deleted{\unsure{proalgébrique}} faisceau de Weil} fini [plus gén les $\unsure{H^i(G)}$ sont \deleted{\unsure{tous finis}}], \deleted{alors} plus gén est affine, et sans composantes abéliennes, alors
\[
E_f(G,S\unsure{\tau|\sigma})\xrightarrow{\sim}E(Rf_*G,\unsure{\tau|\sigma})
\]
\margin{\unsure{préciser}}
\figure{\begin{tikzpicture}\draw(0,0)--(0,1.2);\end{tikzpicture}}
(ii) Si $G$ est \inserted{de type fini} sans composantes abéliennes, alors $E_f(G,S\unsure{\tau|\sigma})\longrightarrow E(Rf_*G,\unsure{\tau|\sigma})$ est un isom mod $\theta$ [i.e. \unsure{les} $\underline E$ dans $\mathbb Q/\mathbb Z$ \deleted{\unsure{est un}} \unsure{se transforme} en un isom\ldots].
\mspage{129}
'''
save_page(130,text,[('deletion','upper crossed construction','Soit un elt f in Exti(C;G,S tau) i.e. un hom de degré i'),('display','within upper crossed construction','Rf*S tau=Rf*(tau tensor mu_n(1))→tau'),('display','upper isolated term beneath Rf','Ri'),('text','upper crossed before Ext2','i.e. un élément de'),('display','upper crossed Ext2','Ext2(k,Rf*(tau tensor mu_n),tau)---'),('text','middle live restart','On a un hom évident'),('display','middle first comparison','underlinedEf(G,S tau)-Ef(Rf*G,Rf*S tau)'),('text','middle element introduction','et si nous définissons un élément'),('display','middle gamma','gamma in Hom0(Rf*S tau,tau)'),('deletion','middle gamma overwritten functor','Ext0'),('insertion','middle gamma above overwritten functor','Hom0'),('text','middle next map introduction','nous en déduisons un hom'),('deletion','middle next map introduction','élément'),('display','middle next comparison','Ef(Rf*G,Rf*S tau)-Ef(Rf*G,tau)'),('text','middle composition','et en composant on trouve l’hom voulu'),('display','middle composed comparison','Ef(G,S tau)→Ef(Rf*G,tau)'),('text','lower theorem introduction','Ceci dit le th de dualité s’énonce'),('text','lower theorem item i','Th (i) Si G est fini [plus gén les Hi(G) sont...]'),('insertion','lower above fini','un faisceau de Weil'),('deletion','lower inserted wording','proalgébrique'),('deletion','lower bracket end','tous finis'),('deletion','lower after bracket','alors'),('display','lower item i comparison','Ef(G,S tau)→~E(Rf*G,tau)'),('margin note','left beside item i','préciser'),('drawing','left beside item i','short vertical line'),('text','bottom theorem item ii','Si G est de type fini sans composantes abéliennes'),('insertion','bottom above sans composantes','de type fini'),('display','inline bottom comparison','Ef(G,S tau)→E(Rf*G,tau) est un isom mod theta'),('text','bottom bracket','i.e. les underlinedE dans Q/Z se transforme en un isom'),('deletion','bottom after Q/Z','est un'),('text','bottom left page number','129')],observations='Whole and both halves read, with enlarged upper cancellation, Hom replacement, theorem and last line. Cancellation applies to upper construction through Ext2, not the live comparison and theorem. The recurring target Greek letter is recorded as tau|sigma throughout pending cross-page ink comparison. Plain comparison strokes and actual arrowheads are distinct. Underline is present on the first E and in the final Q/Z remark, and not supplied to every later E. The theorem has overlaid revisions, recorded rather than reordered into a corrected statement.')
