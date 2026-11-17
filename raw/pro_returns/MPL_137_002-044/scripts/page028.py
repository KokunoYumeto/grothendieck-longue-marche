from record_page import record
tex=r'''\scanpage{28}
% archive foliation: 27
En vertu de \unsure{tout ce} qui suit,
si $A$ est la sous-catégorie pleine
de $C$ engendrée par les $\Phi(i,n)$
et les $\Psi^i$, alors $C$ est connue
à équiv. près (\unsure{déf. can. unique par $A$})
si on connaît $A$ avec sa structure
$k$-additive. Or c'est \inserted{elle} qu'on vient
d'\unsure{être déterminer} (on a omis
de décrire la composition des
morphismes, qui est évidente...).
On trouve donc que $C\simeq$
\unsure{aux} $k$-simpliciaux ordinaires
str. $\partial$-parfaits ....

La chose restante à faire
est donc déterminer la $\otimes$-
structure et les opérations $\Gamma^i$.
'''
record(28,tex,[('text','upper paragraph lines 1–6','En vertu; A sous-catégorie pleine engendrée Φ(i,n), Ψ^i; C connue'),('text','middle continuation','k-additive; Or c’est qu’on vient; omis composition morphismes'),('insertion','above middle qu’on','elle'),('text','lower-middle','On trouve C≃aux k-simpliciaux ordinaires str ∂-parfaits'),('text','bottom','La chose restante à faire; ⊗-structure et opérations Γ^i')],doubts=[('opening line','tout ce','faint group between de and qui suit; literal word segmentation uncertain','low'),('parenthesis after équiv. près','déf. can. unique par A','highly abbreviated cursive on staff rule','low'),('inserted word','elle','small word above cancelled/corrected baseline attachment','medium'),('middle line after qu’on vient','d’être déterminer','visible reading does not yield secure syntax; d’être déterminée / de déterminer possible','low'),('before k-simpliciaux','aux','could be an equivalence abbreviation; mathematical category sign does not settle ink','low'),('final operations','Γ^i','superscript faint, possibly absent or different letter','medium')])
