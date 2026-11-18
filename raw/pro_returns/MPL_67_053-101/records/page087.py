import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{87}
% archive foliation: 89
\uline{NB} On sait que la donnée d'un octaèdre \inserted{comb.} non orienté
revient à celle d'un système $(I,\omega)$, \deleted{\unsure{dans}} $\operatorname{Ens}_4\times\operatorname{Ens}_2$,
ens des \unsure{octo-quartes} et des orientations. Ici $\omega=\{i,-i\}$, \deleted{\unsure{et on}}
\deleted{par la donnée de $I$, que}\inserted{Mais ici on n'a pas $I$ qui est \unsure{abstrait}, mais}
$S$, qui est un ens de cardinal 6 sur lequel $V$ opère.
La condition à mettre \deleted{est} pour que ceci définisse une
\deleted{des} structure octaédrale (dont $S$ sera l'ens des sommets)
est que $\forall\sigma\in V^*$, \deleted{$\unsure{V}$} $\operatorname{card}S^\sigma=2$, et $S=\bigcup_{\sigma\in V^*}S^\sigma$
(réunion forcément disjointe) (cela entraîne que
$\sigma$ opère sur $(S\setminus S^\sigma)$ par transposition de \deleted{\unsure{les}}\inserted{\unsure{chacune}} des deux
composantes $S^{\sigma'},S^{\sigma''}$, ici $V^*=\{\sigma,\sigma',\sigma''\}$). Donc la
donnée de \deleted{$\unsure{S,V\subset}$} $(V,S,u:V\hookrightarrow\unsure{\mathfrak S}_S)$, ou $(S,V\subset\unsure{\mathfrak S}_S)$,
équivaut à celle de $S$, avec une involution sans pts fixes
$a$ (ayant les $S^\sigma$ comme orbites).

Revenant à la donnée d'un $V$ qui opère \inserted{fid.\textsuperscript{t}} sur $X$,
considérons une orbite \inserted{$I$} de $V$ sur $X^*=X\setminus S(V)$.
Donc $I$ est un torseur sous $V$. La donnée de
$(X,I,I\hookrightarrow X)$ équivaut à celle de $(X,I,V(I)\hookrightarrow G_X,$
$I$ orbite de $V(I)$ dans $X)$, et on se propose de
comparer le $(V=V(I))$-torseur $I$, avec le
$V$-torseur $I(V)$ \inserted{$=I(V,X)$} défini via l'octaèdre $\operatorname{Oc}(V)=\operatorname{Oc}(V,X)$.

En termes de \inserted{$I\deleted{\unsure{V}},\{\pm i\}$}, on peut définir un octaèdre \deleted{\uline{orienté}}
canonique \deleted{\unsure{sans base marquée, défini par la}}
condition que \deleted{\unsure{le groupe de ses} \illegible{1} \unsure{soit} $V$} \inserted{l'ens de ses \unsure{faces} ``\unsure{ant.}'' $I_\pm$, l'ens de ses orientations $\{\pm i\}$}
\deleted{\unsure{bipartitions}}.
Cet \deleted{oct.} octaèdre, \deleted{une fois choisi un $i=\sqrt{-1}$,} peut
se réaliser canoniquement \deleted{\unsure{par des cas}}\inserted{comme un} $(X,S)$
$=(X(I),S(I))$. On a un iso can
"""
save(87,tex,[('text','top NB','On sait que la donnée d’un octaèdre'),('insertion','top after octaèdre','comb.'),('deletion','before Ens4 times Ens2','dans'),('deletion','end third line','et on'),('deletion','fourth line','par la donnée de I, que'),('insertion','above fourth line','Mais ici on n’a pas I'),('deletion','after mettre','est'),('deletion','before structure','des'),('deletion','before card S sigma','V'),('deletion','after transposition de','les'),('insertion','above deleted les','chacune'),('deletion','before V,S,u','S,V subset'),('text','middle lower','Revenant à la donnée d’un V'),('insertion','above sur X','fid.t'),('insertion','above de V','I'),('insertion','above défini','=I(V,X)'),('text','bottom','En termes de'),('insertion','after En termes de','I, +/-i'),('deletion','inside insertion after I','V'),('deletion','after octaèdre','orienté'),('deletion','after canonique','sans base marquée, défini par la'),('deletion','after condition que','le groupe de ses ... soit V'),('insertion','above old condition','l’ens de ses faces ant. I plus-minus'),('deletion','right of inserted condition','bipartitions'),('deletion','after Cet','oct.'),('deletion','after octaèdre comma','une fois choisi un i=sqrt(-1)'),('deletion','before comme un','par des cas'),('insertion','above deleted par des cas','comme un')],doubts=[('line 3 noun','octo-quartes','The compound is highly compressed; best visual reading only.','low'),('inserted line 4','abstrait','Several middle letters are not individually separable.','low'),('transposition insertion','chacune','Possibly chacun; ending cramped near caret.','low'),('deleted formula before V,S,u','S,V subset','Heavy scribble obscures complete contents.','low'),('bottom cancelled drafts','sans base marquée, défini par la / le groupe de ses ... soit V','Most cancellation-heavy passage of this page; both readings highly tentative.','low'),('bottom inserted condition','faces ant. I plus-minus','May describe antipodal face pairs; text not expanded or repaired.','low'),('bottom deletion','bipartitions','Doubly crossed word, very low confidence.','low'),('final abbreviation','iso can','Ending can is visible before page edge.','medium')],notations=[('unoriented octahedron data',r'(I,\omega)','omega is a two-element orientation set.'),('set categories',r'\operatorname{Ens}_4\times\operatorname{Ens}_2','Ens written with cardinal subscripts.'),('free locus',r'X^*=X\setminus S(V)','Star denotes removal of fixed points.'),('standard octahedron',r'(X(I),S(I))','Construction indexed by the four-element set I.')],abbreviations=[('fid.t','fidèlement'),('ant.','antipodales (tentative)'),('can','canonique')],leads=['Combinatorial criterion for V action on six vertices: three fixed pairs, disjoint union, each involution transposes other pairs; equivalence with a fixed-point-free involution a.','Problem of comparing an arbitrary free V-orbit I in X with canonical face-pair torsor I(V,X).','Construction of canonical octahedron from I and orientation pair +/-i, heavily revised; preserve uncertainty and distinguish any post-context reinterpretation.'])
