import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{78}
\mspage{13}
% archive foliation: 80
\uline{Question} Ces flèches sont elles des iso
--- et si oui, comment expliciter un
iso en sens inverse ? \deleted{\unsure{Si}}

Si la détermination conjecturale des
syst. admissibles de disques sur une
surface holomorphe \inserted{compacte} ponctuée (de type
hyperbolique) était connue, on trouve-
rait aisément \deleted{\unsure{des flèches}} un sens
inverse; Au niveau plus naïf des
foncteurs (entre les catégories-solutions
de ces multiplicités) on \unsure{donnerait|fournirait}
ceci : à l'aide d'un \deleted{\unsure{u}}
\[
u_i\in T_{x_i'}^*\wedge_{\mathbb C^*}T_{\unsure{a|x}_i''}^*
\]
\margin{ou ce qui revient au même, un
$v_i\,(=u_i^{-1})\in T_{x_i'}^{\vee *}\wedge T_{x_i''}^{\vee *}$}
\deleted{choisissant}\inserted{i.e. un} \deleted{iso} accouplement \unsure{dualisant}
\diagram{\begin{tikzcd}
\deleted{T_{a_i'}^\vee} \arrow[r,"\deleted{\sim}",dashed] & \deleted{T_{a_i''}} & T_{x_i'}\otimes T_{x_i''} \arrow[r] & \mathbb C
\end{tikzcd}}
choisissant un \deleted{\unsure{entier}} disque conforme
$D_i'$ en $T_{a_i'}$, \deleted{\unsure{on en déd.}} d'où disque
conforme plein $D_i''$ dans $T_{a_i''}$, on
trouverait \deleted{des} pour le syst. $(D_i')\ (D_i'')$
des \unsure{réalisations} de ces disques comme
"""
save(78,tex,[('text','top','Question Ces flèches sont elles des iso'),('deletion','after inverse ?','Si'),('text','upper to middle','Si la détermination conjecturale'),('insertion','above ponctuée','compacte'),('deletion','after aisément','des flèches'),('deletion','before display','u'),('display','middle lower','u_i in T* wedge T*'),('margin note','right of display','ou ce qui revient au même'),('deletion','under display','choisissant'),('insertion','above choisissant','i.e. un'),('deletion','before accouplement','iso'),('diagram','under accouplement','deleted T dual isomorphism; tensor product to C'),('text','bottom','choisissant un disque conforme'),('deletion','before disque','entier'),('deletion','after T a prime','on en déd.'),('deletion','after trouverait','des')],doubts=[('middle prose','catégories-solutions','The second component is written in a very compressed hand.','medium'),('middle prose','donnerait','fournirait; initial ascender overwritten.','low'),('u display second index','a_i double-prime','x_i double-prime; the initial glyph resembles a but nearby formula uses x.','low'),('after accouplement','dualisant','Compressed ending; retained as a tentative reading.','medium'),('deleted adjective before disque','entier','Several letters obscured by strike.','low'),('final line','réalisations','Initial strokes are indistinct.','medium')],notations=[('prime notation',r"a_i',a_i'';x_i',x_i''",'a and x are not silently identified.'),('dual nonzero tangent',r'T^{\vee *}','Distinct from T*; explicit dual sign followed by star.')],abbreviations=[('syst.','système(s)'),('i.e.','id est')],leads=['Explicit question whether moduli maps are isomorphisms; inverse construction is conditional on conjectured determination of admissible discs.','Tensor u_i versus inverse dual tensor v_i and a dualising pairing are used to transfer conformal discs; inspect exact gauge invariance in notes.'])
