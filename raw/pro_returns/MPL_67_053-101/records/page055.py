import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{55}
% archive foliation: 57
$U\longrightarrow\overline H^+$ sont exactement les cartes topologiques
(i.e. \deleted{applications continues injectives,}
\inserted{plongements \unsure{topologiques} \deleted{\unsure{ouverts}}\unsure{--- ouverts et topologiques}}
appliquant bord sur bord) qui sont conformes dans $\operatorname{Int}U$.
Cela \deleted{\unsure{résulte du}}\inserted{équivaut au}

\uline{Lemme 1} Soit $U$ un ouvert de $\overline H^+$, alors \deleted{toute}
\deleted{application injective}
\inserted{plongement ouvert $f:U\longrightarrow\overline H$}
\deleted{fonction continue sur $V$} qui est hol.
dans $\unsure{U|V}\cap H$, est holo. (i.e. se prolonge holomorphiquement
dans $\mathbb C$, au voisinage de tt
pt de $U\cap\delta H=U\cap\mathbb R$).

C'est un cas particulier du \uline{lemme de
\unsure{Schwartz|Schwarz}}, qui dit que tt fonction \deleted{hol.}
continue complexe $f$ dans $U$, qui est
\uline{réelle} sur $U\cap\mathbb R$, est holomorphe.

Pour terminer la dem du \deleted{lemme}\inserted{th}, il faut
voir encore que la $f$ du lemme est bien
(au voisinage de tt pt $x$ de $U\cap\delta H$) une
carte holomorphe de \deleted{\unsure{$V$}} $U$ (i.e. de $H$) en $x$,
i.e. que le germe \inserted{en $x$} de fonction holomorphe
\uline{sur $\mathbb C$} défini par $f$ est inversible. Mais \unsure{ce}
germe n'est pas constant, \deleted{de la structure}\inserted{de par}\ \unsure{son} développe-
"""
save(55,tex,[('text','top','U → H-bar+ sont exactement'),('deletion','line 2','applications continues injectives'),('insertion','above line 2','plongements topologiques; ouverts et topologiques'),('deletion','within insertion','ouverts'),('text','line 4','Cela équivaut au'),('deletion','line 4','résulte du'),('insertion','line 4','équivaut au'),('text','upper middle','Lemme 1 Soit U'),('deletion','lemma first line','toute'),('deletion','lemma second line','application injective'),('insertion','lemma second line','plongement ouvert f:U→H-bar'),('deletion','lemma third line','fonction continue sur V'),('text','middle','C’est un cas particulier du lemme'),('deletion','Schwartz paragraph','hol.'),('text','lower','Pour terminer la dem du'),('deletion','lower first line','lemme'),('insertion','lower first line','th'),('deletion','lower fourth line','V'),('insertion','lower fifth line','en x'),('deletion','last line','de la structure'),('insertion','last line','de par')],
 doubts=[('top insertion','plongements topologiques --- ouverts et topologiques','crowded correction; attachment and repeated words uncertain','low'),('lemma','U or V','overwritten letter','medium'),('Schwartz paragraph','Schwartz','Schwarz; spelling not normalized','medium'),('last line','de la structure; de par son','multiple corrections','low')],
 abbreviations=[('tt','tout / toute'),('pt','point'),('dem','démonstration'),('th','théorème'),('holo.','holomorphe')],
 leads=['Reflection principle is invoked as lemme de Schwartz (spelling uncertain). In the stated general version, hol. is visibly struck out and interior holomorphicity is not explicitly restated; examine as a literal gap, not a corrected transcription.','Proof still needs boundary local invertibility after extension; continuation follows.'])
