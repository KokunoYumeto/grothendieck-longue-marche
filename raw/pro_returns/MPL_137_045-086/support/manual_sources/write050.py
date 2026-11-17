import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{50}
% archive foliation: 49
Un $\Sigma$-monomorphisme (épimorphisme)
$A\longrightarrow B$ de $B$ est un morphisme qui s'insère
dans une suite $\in\Sigma$
\[
0\unsure{-|\longrightarrow}A\unsure{-|\longrightarrow}B\longrightarrow K\longrightarrow0
\quad(\text{resp. }0\unsure{-|\longrightarrow}P\unsure{-|\longrightarrow}A\longrightarrow B\longrightarrow0).
\]
Un morphisme \inserted{$A\longrightarrow B$} est $\Sigma$-strict s'il a un
noyau $P$ et un conoyau $Q$, \inserted{\unsure{et si} $\operatorname{Coim}u\longrightarrow\operatorname{Im}u$}
(et si $P\longrightarrow A$, $(B\longrightarrow Q)$ est un $\Sigma$-mono ($\Sigma$-épi)), il
revient au même de dire que l'on peut trouver
des suites $\in\Sigma$
\margin{\unsure{définition de} $\Sigma$-\unsure{strict}.}
\[
\begin{aligned}
0&\unsure{-|\longrightarrow}P\longrightarrow A\longrightarrow R\longrightarrow0\\
0&\unsure{-|\longrightarrow}R\longrightarrow B\longrightarrow Q\longrightarrow0
\end{aligned}
\]
telles que $A\longrightarrow B$ soit le composé $A\longrightarrow R\longrightarrow B$.
(Il faut peut-être exiger qu'un composé de
$\Sigma$-mono (resp. $\Sigma$-épi) est idem.)

On définit de façon évidente les \inserted{objets} $\Sigma$-projectifs
et $\Sigma$-injectifs. Une \deleted{suite \unsure{complexe de cocha. (chaines)}}
\deleted{$\cdots\longrightarrow C^{i-1}\longrightarrow C^i\longrightarrow C^{i+1}\longrightarrow\cdots$}
\deleted{est dit spécial.}
\[
A\xrightarrow{u}B\xrightarrow{v}C
\]
est dite \deleted{\unsure{spéciale si}} \inserted{$\Sigma$-spéciale} \deleted{\unsure{dès}} si elle
\deleted{\unsure{s'insère dans un diagramme} \unsure{exact}}
\inserted{$vu=0$, $u$ et $v$ stricts et \unsure{si l'on a}}
la suite exacte $\in\Sigma$
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
0\arrow[r]&\operatorname{Ker}u\arrow[r]&A\arrow[r]&\operatorname{Coim}u\arrow[r]\arrow[d,equal]&0&&&&\\
&&0\arrow[r]&\operatorname{Im}u\arrow[r]&\operatorname{Ker}v\arrow[r]\arrow[d,equal]&H\arrow[r]&0&&\\
&&&0\arrow[r]&\operatorname{Ker}v\arrow[r]&B\arrow[r]&\operatorname{Coim}v\arrow[r]\arrow[d,equal]&0&\\
&&&&&0\arrow[r]&\operatorname{Im}v\arrow[r]&C\arrow[r]&\unsure{\operatorname{Coker}v}\arrow[d]\\
&&&&&&&&\unsure{0}
\end{tikzcd}}
(c'est une notion autoduale) On dit qu'un
complexe $C^\bullet$ dans $B$ est \uline{$\Sigma$-spécial} si \unsure{...},
\uline{$\Sigma$ acyclique} si \uline{de plus} les $H^i(C^\bullet)$ sont nuls,
une $\Sigma$-résolution si c'est un complexe
de cochaines ($C^i=0$ si $i<0$) et
$H^i=0$ pour $i\unsure{>|\neq}0$.
'''
save(50,text,[('text','top','Un Sigma-monomorphisme'),('display','upper','0 A B K 0; 0 P A B 0'),('text','upper quarter','Un morphisme est Sigma-strict'),('insertion','above morphisme','A→B'),('insertion','above noyau line','Coim u → Im u'),('margin note','upper left diagonal','définition de Sigma-strict'),('display','upper middle','0 P A R 0; 0 R B Q 0'),('text','middle','telles que A→B'),('text','middle parenthesis','Il faut peut-être exiger'),('text','middle lower','On définit de façon évidente'),('insertion','above Sigma-projectifs','objets'),('deletion','after Une','suite complexe de cocha.'),('deletion','below Une','C^{i-1} C^i C^{i+1}'),('deletion','below cancelled complex','est dit spécial'),('display','lower middle','A u B v C'),('text','lower middle','est dite Sigma-spéciale'),('deletion','definition line','spéciale si; dès'),('insertion','definition line','Sigma-spéciale'),('deletion','above diagram','s’insère dans un diagramme exact'),('insertion','above diagram','vu=0; u et v stricts'),('text','above diagram','la suite exacte ∈ Sigma'),('diagram','lower quarter staircase','Ker u A Coim u Im u Ker v H B Coim v Im v C Coker v'),('text','bottom','c’est une notion autoduale')])
