from save_page import save
text=r'''\scanpage{23}
\mspage{\unsure{4|9}}
% archive foliation: 22

\uline{Mais attention} Il n'est pas vrai \uline{dans $\mathrm{Cat}$} que si on a un diagramme
cocartésien
\diagram{\begin{tikzcd}
Y\arrow[r,hook,dash,"i"]\arrow[d,"g"']&X\arrow[d,dash,"f"]\\
Y'\arrow[r,hook,dash,"i'"']&X'
\end{tikzcd}}
$i$ imm. fermée (ou ouverte), alors
\[
[\ i\in\underline W\ \Longrightarrow\ i'\in\underline W,\quad\text{ni que}\ ]\quad
 g\in\underline W\ \Longrightarrow\ f\in\underline W,
\]
$=$ pour l'\unsure{équiv.} faible habituelle, et \unsure{même}
si $g$ est \deleted{\unsure{fibré}}\inserted{cofibré}, \deleted{\unsure{fibré}}
et $i$ \unsure{une triv.} imm. fermée, $Y'\simeq\Delta^0$.

\margin{Si $i\in\underline W$, a-t-on pourtant $i'\in\underline W$ ?
(\uline{Ex} $Y,X$ asphériques $Y'=\Delta_0$) \uuline{Non}}
\margin{Il semble vrai pourtant que si $g$ induit une \deleted{iso} $1$-équiv.,
i.e. équiv. sur les groupoïdes fondamentaux, alors $f$ aussi. $[\ ]$ ?}

\uline{Ex} Considérons une $Z$ dans $(\mathrm{Cat})$, et
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
Z\arrow[r,hook,dash,"\alpha", "{\text{imm. fermée}}"']\arrow[d,"\alpha"']
&\check C(Z)\arrow[d]\arrow[r]&[\deleted{\unsure{e}}\ e_{u'_0}]\\
Y=\check C(Z)\arrow[r,hook,"{\text{imm. f. (\unsure{surj.})}}"']\arrow[d,"{g\in W}"']
&\unsure{\overline\Sigma'}(Z)=X\arrow[d,"f"]&[e_{w_0}]\arrow[l,hook]\\
Y'=e\arrow[r,hook,dash,"{\text{imm. f.}}"']&\unsure{\Theta(Y')}=X'&[e_{u'_0}]\arrow[l,hook]
\arrow[ul,phantom,"{\text{cocart}}",shift left=8ex]
\end{tikzcd}}
\margin{\unsure{cocart} \quad \unsure{cocart}}

Ici $g\in W$, et $X'\simeq\Delta^1$ ssi \deleted{\unsure{\pi_0}}
$Z$ \deleted{\unsure{n'}}est $0$-connexe.
(En général, $\mathrm{Hom}(e_{u'_0},e_{y'_0})\simeq\Pi_0(Z)$).
Mais \unsure{quand il en est ainsi}, $f\in\underline W$ ssi
$\unsure{\overline\Sigma}(Z)$ est $\underline W$-asph., ce qui n'est pas tjrs le cas.
(prendre p.ex. \deleted{\unsure{et}} $Z$ un groupoïde réduit à un \unsure{seul obj.}, avec $\Pi_1\ne1$)
'''
e=[('text','top','Mais attention Il n est pas vrai'),('diagram','upper middle','Y X Y prime X prime; i g f i prime'),('text','middle','i imm. fermée ou ouverte alors'),('display','middle','bracket i in W implies i prime in W ni que; g in W implies f in W'),('text','middle','pour l équiv. faible habituelle'),('deletion','middle','fibré first occurrence'),('insertion','middle','cofibré'),('deletion','middle','fibré second occurrence'),('display','middle right','Y prime is Delta0'),('margin note','upper right','Si i in W a t on pourtant i prime in W'),('display','upper right','Y X asphériques Y prime Delta0'),('text','upper right','Non double underlined'),('margin note','upper left diagonal','Il semble vrai pourtant que si g'),('deletion','upper left diagonal','iso'),('display','upper left','1 équiv. and empty brackets question mark'),('text','lower middle','Ex Considérons une Z dans Cat'),('diagram','lower large','Z check C Z; Y check C Z Sigma prime Z; e Theta Y prime'),('deletion','diagram top right','e'),('text','diagram two square interiors','cocart cocart'),('text','bottom','Ici g in W et X prime is Delta1'),('deletion','bottom','pi0 before Z'),('deletion','bottom','n before est'),('display','bottom','Hom e u0 prime e y0 prime is Pi0 Z'),('text','bottom','Mais quand il en est ainsi'),('display','bottom','f in W ssi Sigma Z W asph.'),('text','bottom','prendre p.ex. Z un groupoïde'),('deletion','bottom left','et'),('display','bottom right','Pi1 not equal1')]
save(23,text,'text',e,'Explicit warning Mais attention: not generally true in Cat that a cocartesian square with closed/open immersion preserves W. The right margin asks whether i in W at least forces i prime in W and answers Non. Left margin suggests g a 1-equivalence may imply f likewise. Cone/suspension example follows, with connected Z and Pi1 nontrivial. All these are manuscript statements, not yet checked; several overwritten adjectives, Sigma decoration, and the Theta argument are doubtful.')
