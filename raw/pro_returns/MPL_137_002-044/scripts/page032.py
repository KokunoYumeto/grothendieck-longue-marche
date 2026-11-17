from record_page import record
tex=r'''\scanpage{32}
% archive foliation: 31
$C$ est stable pour les limites projectives
du type envisagé.
En particulier, on trouve

\uline{Prop.} Soient $C$ une cat. (resp. cat.
additive), $A$ une sous-cat. pleine,
$\tau,\tau'$ deux sous-\deleted{catégories pleines}\inserted{ens}
de $\operatorname{Ob}(\mathrm{Cat})$, supposons que $C$ soit
stable par $\varprojlim$ de type $\tau$ et $\varinjlim$
de type $\tau'$, et que $\forall$ objet de
$C$ soit une $\varprojlim$ \inserted{dans $C$} de type $\tau$ d'objets
de $A$, et une $\varinjlim$, directe de type $\tau'$
d'objets de $A$. Alors $C$ est équivalente
à la fois à la sous-cat. pleine
de $\widehat A$ (resp. $\widehat A_{ab}$) \inserted{$\simeq\underline{\operatorname{Hom}}(A^\circ,\mathrm{Ens})$
(resp. $=\underline{\operatorname{Hom}}(A^\circ,\mathrm{Ab})$)} formée des
foncteurs \inserted{$A^\circ\longrightarrow\mathrm{Ens}$ (resp. $A^\circ\longrightarrow\mathrm{Ab}$)}
qui sont $\varprojlim$ \deleted{de type $\tau$}
de type $\tau$ de foncteurs repr.,
et à la \inserted{cat. opposée de la} sous-catégorie pleine de
$\widehat{A^\circ}\simeq\underline{\operatorname{Hom}}(A,\mathrm{Ens})$
(resp. $\widehat{A^\circ}_{ab}\simeq$
$\underline{\operatorname{Hom}}(A,(\mathrm{Ab}))$) qui sont
\deleted{\unsure{définis par}}\inserted{\unsure{isom. à des}}
$\varprojlim$ de type $\tau'$ de foncteurs
représentables.
'''
record(32,tex,[('text','top continuation','C stable limites projectives; En particulier'),('text','proposition first lines','Soient C cat additive, A sous-cat pleine; τ,τ′'),('deletion','after sous-','catégories pleines'),('insertion','above catégories','ens'),('text','hypotheses','Ob(Cat); stable lim types τ and τ′; object limits of A'),('insertion','above limit condition','dans C'),('text','conclusion first','C équivalente à sous-cat pleine Â resp Â_ab'),('insertion','above Â','Hom(A°,Ens), Hom(A°,Ab)'),('insertion','above foncteurs','A°→Ens (resp A°→Ab)'),('text','first image description','lim type τ foncteurs repr'),('deletion','after first lim in conclusion','de type τ'),('text','second image description','sous-catégorie pleine widehat(A°), Hom(A,Ens) resp Ab'),('insertion','before sous-catégorie','cat opposée de la'),('deletion','after qui sont','définis par'),('insertion','above cancelled phrase','isom à des'),('text','bottom','lim inverse type τ′ foncteurs représentables')],doubts=[('indexing classes','τ,τ′','could be calligraphic T,T′; repeated broad curved top read as tau','medium'),('replacement for catégories pleines','ens','possibly ens. without terminal dot','medium'),('word after second limit in hypothesis','directe','ink reads directe despite redundant right-arrow notation','medium'),('first conclusion comparison annotation','Hom(A°,Ab)','abbreviated Ab resembles M','medium'),('last cancelled / inserted phrase','définis par / isom. à des','overwriting faint; best reading retained locally','low')],notation=[('classes of diagram shapes',r'$\tau,\tau^{\prime}$','scan 32; broad cursive tau; distinction from objects C,A and source prime recorded')])
