import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(33,r"""\scanpage{33}
\deleted{entourées de pions de $A$}
(toutes les autres libertés étant prises par des
pions de $B$) \inserted{et celles-ci étant intérieures (\unsure{i.e.} entourées de pions de $A$)} et $c$ est une de ces deux-là.

[\uline{NB} si $A$ s'y mettait, dès au prochain coup
$B$ en \uuline{se} plaçant dans la \deleted{\unsure{autre}} dernière liberté
$c'$ disponible du groupement $E'=E\cup\{c\}$, capturerait
$E'$ --- et de proche en proche il capturerait
tous les pions de $A$ !\deleted{\unsure{]}} , même si $A$ avait
un avantage considérable sur $B$ par les
territoires couverts !] On exige de plus,
cependant, que le groupement $E$ soit
``indélogeable'', i.e. que si c'était le
tour de $B$ de jouer au lieu de $A$, il ne
pourrait se poser ni en $c$, ni en $c'$
(i.e. que l'on ne peut trouver un sous-
groupement $E_c$ de $E$ \inserted{entourant $c$} dont $c$ soit la
seule liberté \deleted{\unsure{inté}} restante, (\deleted{pas de} \inserted{ou, ce qui revient \unsure{au même}} le groupe-
ment $E_{c'}$ de $E$ entourant $c'$ dont $c'$ soit
la seule liberté restante), ni que $B$
puisse poser en $c$ ou $c'$ par la règle du
Ko.
\mspage{32}
""",'text', [('text','top','toutes les autres libertés'),('marginalia','upper-right insertion','et celles-ci étant intérieures'),('text','upper-middle','NB si A s’y mettait'),('text','middle to bottom','On exige de plus'),('marginalia','bottom-left','32')], doubts=[('upper-right edge','i.e. entourées','Insertion runs to the edge; the abbreviation is compressed.','medium'),('lower-middle insertion','au même','Two short interlinear groups are partly struck; the phrase is not secure.','low')], observations='Continuation of proposed Go end-game rule, requiring an indélogeable group with two remaining liberties and discussing the Ko exception. Distinct substitutions and visibly unmatched parentheses retained.')
