from record_page import record
tex=r'''\scanpage{34}
% archive foliation: 33
à droite sur $k=\operatorname{End}(A)$, et cette
antiéquivalence n'est autre que la
dualité de tels modules.

Revenons à la \deleted{\unsure{notre}} condition que
$\forall$ objet de $C$ est une $\varinjlim$ dans $C$
de type $\tau'$ d'objets de $A$. Alors
$\forall$ catégorie $C'$ où ces limites existent,
si $\underline{\operatorname{Hom}}_{\tau'}(C,C')$ est la sous-catégorie
pleine de $\underline{\operatorname{Hom}}(C,C')$ formée des
foncteurs qui commutent à ces
$\varinjlim$, on trouve que
\[
\underline{\operatorname{Hom}}_{\tau'}(C,C')\longrightarrow
\underline{\operatorname{Hom}}(A,C')
\]
\margin{\uline{à vérifier}}
est pl. fidèle \deleted{(et $\simeq$ une équivalence
de cat. si $\unsure{\forall\text{ objet de }}C'\text{ est }\varinjlim$}
Supposons $C$ additive, et $\tau'$ l'ens
des cat. discrètes finies --- donc
$\forall$ objet de $C$ est somme d'objets
de $A$, alors on trouve, si $C'$ additive
\[
\underline{\operatorname{Hom}}_{add}(C,C')\simeq
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,C').
\]
Si, \unsure{repartons} de l'inclusion
\[
C\xrightarrow{\mathrm{pl.\ fid.}}\deleted{\unsure{\widehat A_{ab}}}
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A^\circ,\mathrm{Ab})
\]
et désignons par $D\subset\deleted{\unsure{\widehat A}}\widehat A_{ab}$ l'image
essentielle, on trouve alors
'''
record(34,tex,[('text','top continuation','à droite sur k=End(A); antiéquivalence dualité'),('text','upper-middle','Revenons condition; tout objet colim dans C type τ′'),('deletion','before condition','notre'),('text','middle','C′ où limites existent; Hom_τ′ sous-cat pleine; commute limites'),('display','middle-lower','Hom_τ′(C,C′)→Hom(A,C′)'),('margin note','left beside full faithfulness','à vérifier'),('text','lower-middle','est pl fidèle'),('deletion','after pl fidèle two lines','et ≃ équivalence de cat si tout objet de C′ est colim'),('text','lower','Supposons C additive; τ′ discrètes finies; objets sommes; C′ additive'),('display','lower','Hom_add(C,C′)≃Hom_Z-add(A,C′)'),('text','bottom','Si repartons de l’inclusion'),('display','bottom','C→Hom_Z-add(A°,Ab) pl fid'),('deletion','display codomain old notation','Â_ab'),('text','bottom continuation','D⊂Â_ab image essentielle; on trouve alors'),('deletion','after D⊂','Â')],doubts=[('deleted word before condition','notre','very small cancellation may be a different determiner','low'),('Hom subscript','τ′','prime is faint in first occurrence; included by local stroke','medium'),('cancelled equivalence condition','∀objet de C′ est colim','middle words obliterated; not silently completed beyond visible fragment','low'),('additive enrichment coefficient','Z-add','k-add; sign a looped bent stroke, both readings retained','low'),('bottom introduction','Si, repartons de l’inclusion','word after Si faint; reprenons possible','low'),('overwritten codomain','Â_ab','old notation heavily scribbled; replacement Hom clear','low')],notation=[('author’s verification flag',r'\margin{\uline{à vérifier}}','scan 34; explicitly beside full-faithfulness claim, not an editorial doubt')])
