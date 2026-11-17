import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{78}
% archive foliation: 77
\uline{Relations avec op.} $\otimes$ \uline{et} $\Gamma^p$.

La donnée d'une cat. polynomiale \inserted{$P$} permet de définir un foncteur triadditif
\[
P_1^\circ\times P_1^\circ\times P_1\longrightarrow\operatorname{Ab}
\]
par
\[
(X,Y;Z)\longmapsto P_{(1,1)}(X,Y;Z)
\]
(et de même pour plus d'arguments de gauche).
Si, pour $X,Y$ fixés, $Z$ variable, ce foncteur est représentable, l'objet qui le représente est noté $X\otimes Y$. Il dépend fonctoriellt de $X,Y$ dans $P_1$ (mais non pour $X,Y$ \deleted{\unsure{$\in\operatorname{Ob}P$}} considérés comme dans $P$ !). \deleted{\unsure{Il}} On sait que $X\otimes Y$ existe ssi $Y\otimes X$ existe, et \unsure{il y a un} can. isom (noté $s_{X,Y}$), on a
\[
s_{\unsure{X\otimes Y|X,Y}}\circ s_{\unsure{Y\otimes X|Y,X}}=\operatorname{id}_{Y\otimes X}.
\]

\unsure{Sur|Pour} $X,n\in\mathbf N$ fixés, si le foncteur
\[
Y\longmapsto P_n(X,Y)
\]
sur $P_1$ est représentable, l'objet qui le représente est noté $\Gamma^n X$; il dépend encore fonctoriellt de $X$ dans $P_1$. L'objet $\Gamma^0(X)$ existe ssi $\Gamma^0(0)$ existe il est noté $1$.

\unsure{Prouvons} que \deleted{\unsure{$\forall$}} si $1$ existe, alors $\forall X\in\operatorname{Ob}P$, $1\otimes X\simeq X$ i.e.
\[
P_{(1,1)}(1,X;Y)\mathrel{\mathop{\simeq}\limits_{\unsure{\text{sous bifoncteurs}}}}P_1(X,Y)\bigl(=\operatorname{Hom}_{P_1}(X,Y)\bigr)\quad ?
\]
et plus particulièrement $1\otimes1\simeq1$ i.e. $\forall Y$
\[
P_{1,1}(1,1;Y)\simeq P_1(1,Y)\qquad ?
\]'''
e=[('text','heading','Relations avec op ⊗ et Γp'),('text','top','La donnée d’une cat polynomiale permet de définir'),('insertion','above first line','P'),('display','upper','P1°×P1°×P1→Ab'),('display','upper','(X,Y;Z)↦P(1,1)(X,Y;Z)'),('text','middle','et de même pour plus d’arguments de gauche'),('text','middle','Si pour X,Y fixés Z variable ce foncteur est représentable'),('deletion','middle','∈ObP'),('deletion','middle','Il'),('text','middle','On sait que X⊗Y existe ssi Y⊗X existe'),('display','middle','sX⊗Y∘sY⊗X=idY⊗X'),('text','lower middle','Sur X,n∈N fixés si le foncteur'),('display','lower middle','Y↦Pn(X,Y)'),('text','lower','sur P1 est représentable'),('text','lower','L’objet Γ0(X) existe ssi Γ0(0) existe'),('text','lower','Prouvons que si 1 existe alors ∀X∈ObP'),('deletion','lower','∀'),('display','bottom','P(1,1)(1,X;Y)≃P1(X,Y)(=HomP1(X,Y)) ?'),('text','bottom','et plus particulièrement 1⊗1≃1'),('display','bottom','P1,1(1,1;Y)≃P1(1,Y) ?')]
save(78,text,e)
