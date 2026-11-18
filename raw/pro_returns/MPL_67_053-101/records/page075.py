import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{75}
% archive foliation: 77
identifiant les pts des centres des disques
qui se correspondent, et en ponctuant
par les centres des autres disques.
De plus, on obtient, \deleted{avec} pour chaque
point singulier $x$ de $X'''$, correspondant
à une paire $\{x_1,x_2\}$ de points de
$X''$ (centres des deux disques associés),
grâce à l'antiisomorphisme de ces
disques pointés, un élément \deleted{de}\inserted{non nul (i.e. une base)}
de
\[
T_{X'',x_1}\otimes_{\mathbb C}T_{X'',x_2}
\]
i.e. un élément de
\[
T^*_{X'',x_1}\wedge_{\mathbb C^*}T^*_{X'',x_2}.
\]

On trouve ainsi un foncteur de

a) catégorie \inserted{(groupoïde)} des courbes hol. cptes à bord \inserted{$X$} de
type $g,\nu$, avec découpage holomorphe
(avec comme flèches les iso)

vers

b) Catégorie des courbes \inserted{$\mathbb C$-alg} stables de type $(g,\nu)$
$X'''$, munies \inserted{1°)} d'une ``structure de propagation
\unsure{nodale}'' en ses pts singuliers, et 2°) d'un
\deleted{structure de \unsure{parallélismes}}\inserted{syst.} admissible de
disques autour des pts marqués.
"""
save(75,tex,[('text','top','identifiant les pts des centres des disques'),('text','upper','De plus on obtient'),('deletion','upper','avec'),('deletion','middle','de'),('insertion','middle','non nul (i.e. une base)'),('display','middle','T_{X″,x1}⊗_C T_{X″,x2}'),('text','middle','i.e. un élément de'),('display','middle lower','T*∧_{C*}T*'),('text','lower','On trouve ainsi un foncteur de'),('text','lower','a) catégorie des courbes hol.'),('insertion','lower','groupoïde'),('insertion','lower','X'),('text','lower','avec comme flèches les iso'),('text','bottom','vers b) Catégorie des courbes'),('insertion','bottom','C-alg'),('insertion','bottom','1°)'),('deletion','bottom','structure de parallélismes'),('insertion','bottom','syst.')],
 doubts=[('structure de propagation qualifier','nodale','first letters look longer than simple n; perhaps unnodale','low'),('last deleted noun','parallélismes','middle letters and ending crossed; tentative only','low')],
 notations=[('Nonzero tangent vectors in contracted product',r'T^*_{X\prime\prime,x_i}','star means deleted zero section here, not silently changed to dual'),('Node propagation datum',r'T_{X\prime\prime,x_1}\otimes_{\mathbb C}T_{X\prime\prime,x_2}','nonzero tensor / basis from paired discs')],
 abbreviations=[('hol.','holomorphes'),('cptes','compactes')],
 leads=['Paired pointed discs and their anti-isomorphism yield a nonzero tensor in the product of tangent lines at the two branches of a node.','Functor from bordered holomorphic curves with holomorphic cut systems to stable complex algebraic curves with nodal propagation data and admissible marked-disc systems.','The admissibility requirement is additional target data; relationship with prior bijective shadow conjecture remains to be assessed.'])
