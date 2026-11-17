from record_page import record
tex=r'''\scanpage{35}
% archive foliation: 34
\[
\underline{\operatorname{Hom}}_{add}(D,C')\xrightarrow{\sim}
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,C')
\]
d'où un sens inverse
\[
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,C')\xrightarrow{\sim}
\underline{\operatorname{Hom}}_{add}(D,C')
\]
d'où un accouplement
\diagram{\begin{tikzcd}[column sep=small]
D\arrow[d,hook]&\mathbin{\times}&\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,C')\arrow[r]&C'\\
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A^\circ,\mathrm{Ab})
\end{tikzcd}}
qu'on note par la
\[
(F,G)\longmapsto F\underset{C}{\otimes}G.
\]
[dans le cas où $A$ est réduite à un
objet, donc où sa str. $\unsure{\mathbf Z|k}$-add. est
définie par un anneau $k_0$,
$F$ est un \inserted{$k_0$-}module à droite libre de
t.f., $G$ est un objet de $C'$ où $k$
opère à g. (i.e. un $k$-$C'$-module
à gauche) et $F\otimes G$ est le
produit tensoriel ``ordinaire''.
Si on considère le plongement
dual
\[
C\xrightarrow{\sim}D'^\circ\subset
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,\mathrm{Ab})^\circ,
\]
on trouve
\diagram{\begin{tikzcd}[column sep=huge]
\underline{\operatorname{Hom}}_{add}(D'^\circ,C')\arrow[r,"\sim"]&
\underline{\operatorname{Hom}}_{\unsure{\mathbf Z|k}\text{-}add}(A,C')\arrow[l,bend left=40,"\sim"]
\end{tikzcd}}
d'où
'''
record(35,tex,[('display','top','Hom_add(D,C′)→~Hom_Z-add(A,C′)'),('text','upper','d’où un sens inverse'),('display','upper','Hom_Z-add(A,C′)→~Hom_add(D,C′)'),('text','upper-middle','d’où un accouplement'),('diagram','middle','D×Hom_Z-add(A,C′)→C′; D⊂Hom_Z-add(A°,Ab)'),('text','middle','qu’on note par la'),('display','middle','(F,G)↦F⊗_C G'),('text','lower bracket','A réduite un objet; anneau k0; F module libre t.f.; G k-C′-module'),('insertion','above module','k0-'),('text','lower','F⊗G produit tensoriel ordinaire'),('text','lower','Si on considère plongement dual'),('display','lower','C→~D′°⊂Hom_Z-add(A,Ab)°'),('text','bottom','on trouve'),('diagram','bottom','Hom_add(D′°,C′)→~Hom_Z-add(A,C′), curved inverse equivalence'),('text','bottom continuation','d’où')],doubts=[('additivity coefficient','Z-add','k-add; looped glyph consistently ambiguous in this group of pages','low'),('tensor subscript','C','A possible but rounded C shape distinct from A immediately above','medium'),('ring name','k_0','subscript 0 tiny; later k appears without visible 0, retained','medium'),('mapping lead-in','qu’on note par la','par le / par (following formula) possible','low'),('lower opposite category','D′°','prime visible separately from opposite circle','high')],notation=[('tensor pairing over handwritten category',r'$F\underset{C}{\otimes}G$','scan 35; C-like subscript retained; not normalized to expected indexing category')])
