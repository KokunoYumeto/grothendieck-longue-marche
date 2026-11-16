import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(44,r"""\scanpage{44}
\uline{NB} Les groupes $\mathfrak z$ qui peuvent intervenir (pour $G$ connexes
satisfaisant la condition de Chevalley) sont \deleted{\unsure{ceux}} les groupes
alg. comm. affines pour lesquels a) $\exists$ mono \inserted{central} $\mathfrak z\hookrightarrow L$,
avec $L$ lisse connexe affine --- tjrs vérifié, et même avec
$L$ commutatif --- ce qui donnera un $G$ commutatif ---
et b) $\exists$ schéma abélien $A$ et mono $D(\mathfrak z)\hookrightarrow\uline{\operatorname{Pic}}_{A/k}$, ce
\deleted{\unsure{qui est nécessaire}} \inserted{qui} (pour $k$ alg. clos, pour simplifier)

1°) si $\operatorname{Car}k=0$, \deleted{\unsure{par}} est \uline{tjrs} vérifié

2°) si Car. $k=p>0$ est vérifié sss $\mathfrak z_u$ fini.

\margin{\unsure{cette} note est \unsure{triviale} sur ce point}

\uline{NB} Ceci \deleted{montre} \inserted{pour isogénies caractéristiques} \deleted{que} la construction de $G_{\mathrm{aff}}$ \deleted{n'est pas \unsure{cat}} (pour $G$
groupe affine lisse à fibres connexes sur base $S\ldots$) n'est pas
de nature ``constructible en général''. Prenons p.ex. pour $G$
une extension d'un schéma abélien $A$ par $G_a$, non triviale
en un pt maximal \deleted{\unsure{y}} de $S$ de car. 0, donc $(G_\unsure{y|\eta})_{\mathrm{aff}}=1$, cependant
aux \deleted{\unsure{pts}} spécialisations $s$ de $y$ de car. $p>0$, on aura $(G_s)_{\mathrm{aff}}\simeq G_a$.
Par contre, cela montre en même temps qu'en égalis. car.
résiduelles, c'est une construction \inserted{de nature} ``constructible''.

\uline{Reformulation} Il est maladroit de prendre $\mathfrak z\subset\operatorname{Cent}(L)$ et
\uline{mono} \deleted{\unsure{a}} $D(\mathfrak z)\hookrightarrow\uline{\operatorname{Pic}}_{A/k}$, il vaut mieux dire qu'on se
donne

A) groupe alg. affine lisse connexe $L$ et V.A. $A$

B) extension de $A$ par $\operatorname{Cent}(L)$ i.e. hom.
\[D(\operatorname{Cent}(L))\longrightarrow\uline{\operatorname{Pic}}_{A/k}\]

L'avantage de la présentation adoptée plus haut semble
uniquement dans le fait qu'elle permet d'expliciter
la donnée B) sans faire intervenir des ``schémas'' à la
Cartier trop \uline{dégueulasses} ---
\mspage{43}
""",'text',[('text','top','NB Les groupes z qui peuvent intervenir'),('text','upper','a) existe mono central'),('text','upper-middle','b) existe schéma abélien'),('text','upper-middle','1° Car k=0'),('text','upper-middle','2° Car k=p>0'),('marginalia','left-middle','cette note'),('text','middle','NB Ceci la construction de Gaff'),('text','middle','Prenons p.ex. pour G'),('text','middle-lower','Par contre cela montre'),('heading','lower-middle','Reformulation'),('text','lower-middle','Il est maladroit'),('text','lower','A) groupe alg.'),('text','lower','B) extension de A'),('display','lower','D(Cent(L)) to Pic'),('text','bottom','L’avantage de la présentation'),('marginalia','bottom-left','43')],doubts=[('middle paragraph','groupe affine lisse','Affine is visibly written in the parenthesis; retained even though the surrounding example may create a mathematical tension.','high'),('middle insertion','pour isogénies caractéristiques','Small addition above the sentence is uncertain as a whole.','low')],observations='Conditions on the central affine kernel, characteristic-dependent finiteness, and a warning that affinization is not generally constructible under mixed-characteristic specialization. Source itself seems to write groupe affine in the parenthesis: research should flag rather than silently repair it. Reformulation uses a hom from Cartier dual of Cent(L) to Picard, with explicit adverse comment about Cartier schemes.')
