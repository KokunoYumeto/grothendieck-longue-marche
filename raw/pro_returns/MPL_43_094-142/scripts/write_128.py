from page_work import save_page
text=r'''\scanpage{128}
\deleted{\unsure{Schémas}}

$C$ courbe algébrique [complète non singulière sur $k$]

\deleted{\illegible{1}} On suppose définie la notion de $C$-groupes [= faisceaux de Weil sur les préschémas de \deleted{\unsure{petit}} type fini sur $C$, pour la descente fid plate\ldots]. \deleted{\unsure{Ils}} Les $C$-groupes forment une catégorie abélienne avec assez d'injectifs, d'où des Ext (globaux et locaux), des $H^i(C,G)$ \inserted{$\simeq\operatorname{Ext}^i(C;\mathbb Z,G)$}, etc.

Sur $k$, on a les $k$-groupes [définis comme les $C$-groupes ? Cela est-il équivalent aux foncteurs de Weil \inserted{-schémas} sur les \deleted{\unsure{les}} $k$-ensembles algébriques ?]

On a un foncteur \deleted{$\unsure{f_*}$}
\[
f_*:\operatorname{Gr}_C\mathrel{-}\operatorname{Gr}_k\mathrel{-}\operatorname{QuGr}_k
\]
[image directe par $f:C\mathrel{-}\operatorname{Spec}k$] qui est exact à g., \deleted{\unsure{donc}} et transforme injectifs en injectifs, d'où des foncteurs dérivés
\[
\underline H^i_f(G)=\deleted{\unsure{Rf(E}}\ H^i(Rf_*)(G)
\]
[si $G$ est un complexe \unsure{borné} \unsure{à} \unsure{g.} --- \unsure{nous admettrons} que $f_*$ \uline{est de dim \unsure{ch.} finie}] On définit de $\unsure{=}$
\[
\underline{\operatorname{Ext}}^i_f(F,G)=H^i(\underline E^{\unsure{\bullet}}_f(F,G))
=H^i((R\underline{\operatorname{Hom}}_f(F,-))(G))
\]
D'où comme d'habitude des suites spectrales
\[
\deleted{H^{\unsure{i}}_f}\quad\operatorname{Ext}^{\unsure{*}}(C;F,G)
\Longleftarrow H^p(\unsure{K|X};\underline{\operatorname{Ext}}^q(F,G))
\]
en particulier
\[
H^{\unsure{*}}(C,G)\Longleftarrow H^p(k;\underline H^q_f(G))
\]
\mspage{127}
'''
save_page(128,text,[('deletion','top heading','Schémas'),('text','upper opening','C courbe algébrique [complète non singulière sur k]'),('deletion','upper paragraph left start','one blacked-out word'),('text','upper paragraph','On suppose définie la notion de C-groupes'),('deletion','upper second line before type fini','petit'),('deletion','upper third line before Les','Ils'),('insertion','upper paragraph end above etc','≃Exti(C;Z,G)'),('text','middle paragraph','Sur k on a les k-groupes [définis comme les C-groupes ?]'),('insertion','middle above sur les','-schémas'),('deletion','middle before k-ensembles','les'),('text','middle functor introduction','On a un foncteur'),('deletion','middle end of functor introduction','f*'),('display','middle functor','f*:GrC-Grk-QuGrk'),('text','lower bracket and derived functors','[image directe par f:C-Spec k] qui est exact à g.'),('deletion','lower before et transforme','donc'),('display','lower cohomology definition','underlinedHif(G)=Hi(Rf*)(G)'),('deletion','lower cohomology definition after equals','Rf(E'),('text','lower bracket and Ext introduction','[si G est un complexe borné à g. - nous admettrons que f* est de dim ch. finie]'),('display','lower Ext definition','underlinedExtif(F,G)=Hi(underlinedEbulletf(F,G))=Hi((RunderlinedHomf(F,-))(G))'),('text','bottom spectral introduction','D’où comme d’habitude des suites spectrales'),('display','bottom first spectral sequence','Ext*(C;F,G)⇐Hp(K;underlinedExtq(F,G))'),('deletion','bottom before first spectral sequence','Hif'),('text','bottom before last formula','en particulier'),('display','bottom last spectral sequence','H*(C,G)⇐Hp(k;underlinedHqf(G))'),('text','bottom left page number','127')],observations='Whole and both halves read, then enlarged four text/formula areas and the complex-degree phrase. The compact text is fast and several deletions and clause words remain doubtful. Mathematical expectations were not used to supply the faint degree, base letter, or deleted term. The two category connectors and C-to-Spec connector are plain strokes in the ink. The handwritten equivalence question and finite-cohomological-dimension phrase are retained, including underlining. The inserted -schémas is placed after Weil as indicated by the curved insertion mark; attachment to be rechecked in audit.')
