import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(44,r'''
\scanpage{44}
% archive foliation: 43
b) Si $u\in\operatorname{End}_K(\mathcal M)$, alors on définit
\[
\bar e_u:\overline G_{aK}\longrightarrow\unsure{\operatorname{Aut}|\operatorname{End}}_K(\mathcal M)
\]
\[
\bar e_u(\lambda)=\exp(\lambda u)
\]
\uline{NB} La question se pose encore si $u\longmapsto\bar e_u$ et $u\longrightarrow e_u$ sont des \uline{bij.}
\margin{?}
\[
\begin{aligned}
\operatorname{End}_K(\mathcal M)&\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(\overline G_{aK},\operatorname{Aut}_K(\mathcal M))\\
N(\operatorname{End}_K(\mathcal M))&\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(G_{aK},\operatorname{Aut}_K(\mathcal M))
\end{aligned}
\]
Extension aux \deleted{\unsure{f}} algèbres symétriques, tensorielles, \unsure{extérieures} ---

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0.30)--(1.7,0.34);
\draw (0.10,0.16)--(1.72,0.19);
\draw (0.19,0)--(1.80,0.03);
\end{tikzpicture}}
\deleted{\unsure{II}}

\uline{Globalisation} \deleted{\unsure{Soit}} $X$ schéma de car 0,

$\Theta$ \unsure{une|la} dérivation de $\underline O_X$, supposons $\Theta$ loc nilpotent. Alors $\exp\Theta$ est un autom de $\underline O_X$ qui induit l'identité sur $\underline O_{X_{\mathrm{réd}}}=\underline O_X/N\underline O_X$, et correspond à un autom de $X$ : que nous désignerons par $E_\Theta$. Si $\unsure{X}$ est sur $S$ et $\Theta$ est une $S$-dérivation, $E_\Theta$ est un $S$-autom. On a
\[
\left\{\begin{aligned}
E_0&=\operatorname{id}\\
E_{\Theta+\Theta'}&=E_\Theta+E_{\Theta'}\qquad\text{si }[\Theta\Theta']=0
\end{aligned}\right.
\]
''',[
('text','top','b) Si u in End_K(Mcal)'),
('display','upper','bar e_u: bar G_aK to Aut_K(Mcal)'),
('display','upper','bar e_u(lambda)=exp(lambda u)'),
('text','upper-middle','NB La question se pose encore si'),
('margin note','left of bijectivity question','?'),
('display','middle two arrows','End_K(Mcal), N(End_K(Mcal)) to Hom_gr'),
('text','middle','Extension aux algèbres symétriques, tensorielles, extérieures'),
('deletion','before algèbres','f'),
('drawing','middle separator','three horizontal strokes'),
('deletion','left above fold','II'),
('text','below fold heading','Globalisation X schéma de car 0'),
('deletion','before X','Soit'),
('text','lower','Theta une dérivation de underline O_X'),
('display','bottom','E_0=id; E_Theta+Theta-prime=E_Theta+E_Theta-prime')
],[
('first target functor','Aut','End; letters overwritten in place','medium'),
('before algèbres','deleted f','short crossed character','low'),
('end of extension list','extérieures','initial letters retraced','medium'),
('cancelled heading above Globalisation','II','overwritten Roman numeral','low'),
('cancelled word before X','Soit','compact scribble','low'),
('after Theta','une','la; small overwritten abbreviation','low'),
('Si X est sur S','X','overwritten capital','medium'),
('structure sheaf alphabet','underlined O','literal underline retained; script O possible','medium'),
('last identity operator','plus','visibly cross-shaped sign retained; not silently changed to composition','high')])
