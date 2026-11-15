import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(42,r'''\scanpage{42}
Appelons F-V-\uline{cristal} \uline{filtré}\inserted{ sur S} (par abus de langage) un F-V-cristal en Mod. loc. lib. sur S muni de\deleted{une filtr} la donnée d'une filtration de $M_S$ par une sous-module localement facteur direct. On trouve donc en fait un foncteur
\[
\diagram{\begin{tikzcd}
\mathrm{BT}(S) \arrow[r] & \text{F-V-cris fil }(S),
\end{tikzcd}}
\]
compatible aux images inverses.

\inserted{\uline{Remarque}}
La filtration (*) doit être considérée comme étant l'équivalent d'une filtration ``de Hodge'' sur une \unsure{cohomoologie|cohomologie} de De Rham \inserted{relative} en dimension 1. \deleted{Pour expliciter} Ce point\deleted{, partons par exemple \unsure{d'un schéma abélien} A sur S, et prenons $G=\unsure{A}(\infty)=\unsure{\lim|\varinjlim}A(n)$. On peut alors}\inserted{ sera explicité plus bas.}

Soit maintenant S' un épaississement à p.div. de S. On se propose de trouver tous les prolongements possibles (à isom. près) \unsure{da|du} groupe de BT G donné sur S en un groupe de BT G' sur S'. On \deleted{trouve} prouvera que si à tout tel G', on associe la filtration correspondante de $D(G')_{S'}=\underline D^*(G)_{S'}=\underline D^*(G_0)_{S'}$ (cf.\qquad pour le fait que S' peut être envisagé comme un objet du site cristallin absolu de $S_0$), qui prolonge la filtration qu'on a sur $\underline D^*(G)_S=\underline D^*(G_0)_S=\underline D^*(G')|S$, on trouve une bijection entre l'ensemble des classes d'isomorphie cherchés et l'ensemble des filtrations qui prolongent. De façon plus précise, on a:\deleted{une équivalence de catégories}

\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0,1.5);\end{tikzpicture}}}
\uline{Théorème de déformation pour les groupes de} BT : Soient S un schéma où p est loc. nilp., S' un épaississement à p.div. de S, Considérons le foncteur canonique
\[
\diagram{\begin{tikzcd}[column sep=large]
\mathrm{BT}(S') \arrow[r] & \begin{array}{l}
\text{catégorie des }\deleted{\text{triples}}\inserted{\text{paires}}\text{ d'un groupe de BT G sur S, et}\\
\text{d'un}\deleted{\text{e}}\text{ sous-module localement facteur direct de}\\
\underline D^*(G)_{S'}\text{ qui prolonge le sous-module }\operatorname{Fil}^1\underline D^*(G)_S=\underline\omega_G\\
\text{de }\underline D^*(G)_S.
\end{array}
\end{tikzcd}}
\]
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(0,.6);\end{tikzpicture}}}
Ce foncteur est une \uline{équivalence de catégories}, \inserted{\uline{si} S' \uline{est à p. div. nil} ou si on se borne à des G qui sont infinitésimaux, ou à \unsure{duaux} infinitésimaux.}
\figure{\begin{tikzpicture}\draw (0,.1)..controls (3,.45) and (5,-.15)..(7,.1)--(13,.1);\end{tikzpicture}}

\inserted{Remarques}
Si le \deleted{\unsure{questio|question}} problème 1 avait une réponse affirmative, on en conclurait une description de la catégorie des groupes de BT sur S en termes de cristaux de Dieudonné filtrés sur S, en appliquant le théorème de
\margin{41}
''','typed',[
('text','first paragraph','Appelons F-V-cristal filtré'),('insertion','after filtré','sur S'),('deletion','muni de...','une filtr'),('diagram','upper display','BT(S) to F-V-cris fil(S)'),('text','below display','compatible aux images inverses'),('insertion','above La filtration','Remarque'),('text','remark paragraph','La filtration (*)'),('insertion','after De Rham','relative'),('deletion','remark, start abandoned sentence','Pour expliciter'),('deletion','remark, two cancelled lines','partons par exemple d’un schéma abélien ...'),('insertion','above cancelled lines','sera explicité plus bas.'),('text','middle paragraph','Soit maintenant S’'),('deletion','On trouve prouvera','trouve'),('deletion','end middle paragraph','une équivalence de catégories'),('drawing','left of theorem','vertical emphasis stroke'),('text','theorem heading and hypotheses','Théorème de déformation'),('diagram','theorem functor','BT(S’) to category of pairs'),('deletion','diagram target','triples'),('insertion','diagram target above triples','paires'),('deletion','diagram target d’une','e'),('drawing','left of conclusion','short vertical emphasis stroke'),('text','theorem conclusion','Ce foncteur est une équivalence'),('insertion','handwritten appended hypotheses','si S’ est à p. div. nil ...'),('drawing','above final remark','long curved separating stroke'),('insertion','above final remark','Remarques'),('text','bottom paragraph','Si le problème 1'),('deletion','before problème 1','questio'),('margin note','bottom left','41')
],[
('remark, cohomology word','cohomoologie','cohomologie','medium','An extra rounded overtyped character is visible near the middle.'),('cancelled example after partons','d’un schéma abélien A sur S','','medium','The cancellation is dense but most lower letter outlines survive.'),('cancelled example, group formula','G=A(infinity)=lim A(n)','direct limit','medium','A is partly crossed; no definite lower arrow survives beneath lim.'),('middle paragraph, before groupe','da','du','medium','The second letter appears closed and a-like.'),('theorem, handwritten qualification','duaux','','medium','Word reaches the right edge and has compressed final letters.'),('bottom deleted partial word','questio','question','medium','Seven letters are visible; a final n is not clear.'),('theorem qualification abbreviation','p. div. nil','','high','The source stops at nil; no expansion is supplied.'),('middle, first D expression','D(G prime)_S prime','','high','Unlike neighbouring occurrences, this first D has neither underline nor superscript star.')
])
