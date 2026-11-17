from record_page import record
tex=r'''\scanpage{36}
% archive foliation: 35
i.e.
\diagram{\begin{tikzcd}[column sep=small]
D'^\circ\arrow[d,hook]&\mathbin{\times}&
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,C')\arrow[r]&C'\\
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,\mathrm{Ab})^\circ
\end{tikzcd}}
noté
\[
\underline{\operatorname{Hom}}_C(F,G)
\]
---
\par\bigskip\hrule\bigskip
On suppose maintenant qu'on a
une catégorie $S$, une sous-catégorie
\inserted{pl. $C$} de $S_{ab}$ stable par sommes directes
(donc $C$ est additive) et une
sous-catégorie pleine $A$ de $C$ telle
que $\forall$ objet de $C$ est isom. à une
somme directe \deleted{de}\inserted{dans $C$, donc dans $S_{ab}$} d'objets de $A$.
On a alors \deleted{foncteur}
\[
\alpha:S^\circ\longrightarrow\deleted{\unsure{\widehat S_{ab}}}
\underline{\operatorname{Hom}}_{add}(C,\mathrm{Ab})
\]
\deleted{\unsure{comme}}
en associant à $\forall X\in\operatorname{Ob}S$
le foncteur $M\longmapsto\operatorname{Hom}_S(X,M)$.
Or ce foncteur est connu à équiv.
près par \unsure{la connaissance de} son image
dans $\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,(\mathrm{Ab}))$, donc l'étude
de $\alpha$ est équivalente à celle de
'''
record(36,tex,[('text','top','i.e.'),('diagram','top','D′°×Hom_Z-add(A,C′)→C′; inclusion into Hom(A,Ab)°'),('text','upper-middle','noté'),('display','upper-middle','underlined Hom_C(F,G)'),('text','after separator','On suppose catégorie S; sous-catégorie S_ab stable sommes directes'),('insertion','before de S_ab','pl C'),('text','middle','C additive; A pleine; chaque objet somme objets A'),('deletion','after somme directe','de'),('insertion','above after somme directe','dans C, donc dans S_ab'),('text','lower-middle','On a alors'),('deletion','after alors','foncteur'),('display','lower-middle','α:S°→Hom_add(C,Ab)'),('deletion','old codomain','widehat S_ab'),('deletion','before en associant','comme'),('text','lower','en associant X∈ObS; M↦Hom_S(X,M)'),('text','bottom','foncteur connu à équiv près par image; étude α équivalente')],doubts=[('top pairing / final Hom coefficient','Z-add','k-add; same ambiguous glyph as preceding scans','low'),('ambient category','S','ornate S with double curve; may be script S, represented plain consistently','medium'),('deleted codomain','widehat S_ab','could instead be widehat C_ab; heavy scribble retained','low'),('cancelled word before en associant','comme','short dark cancellation; best tentative reading','low'),('penultimate sentence','par la connaissance de son image','central words faint; par la donnée de son image possible','low')],notation=[('ambient category with group objects',r'$S,S_{ab}$','scan 36; double-curved S, not numeral 8'),('contravariant evaluation functor',r'$\alpha:S^\circ\to\underline{\operatorname{Hom}}_{add}(C,\mathrm{Ab})$','scan 36; alpha label retained, not conflated with S')])
