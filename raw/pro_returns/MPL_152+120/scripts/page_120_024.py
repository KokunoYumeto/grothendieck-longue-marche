from record_page import save_page
save_page(120,24,r'''
\deleted{Si $x\in X\setminus Y$, $\exists\alpha$ tel que $f_\alpha(x)\ne0$, et}

définissent $Y$ comme l'ens des zéros communs. \deleted{de $X$} : ces fonctions, de plus elles séparent les pts de $X\setminus Y$, car si $x,y$ sont des pts distincts, \deleted{$\exists\beta$ tel que $f_\alpha(x)\ne0$ $g_\beta(x)\ne g_\beta(y)$ d'où}

Si les $f_\alpha$ \unsure{ne} suffisent pas à les séparer, montrons que les $f_\alpha g_\beta$ les séparent : en effet, $\exists\beta$ tel que $g_\beta(x)\ne g_\beta(y)$ \deleted{d'où} et $\alpha$ tel que $\lambda=f_\alpha(x)\ne0$, donc $f_\alpha(y)$ $(=f_\alpha(x)=\lambda\text{ par hyp.})\ne0$, d'où
\[
f_\alpha\underbrace{g_\beta(x)}_{\lambda}=\lambda g_\beta(x)\ne f_\alpha g_\beta(y)=\lambda g_\beta(y)
\]

Donc :

\uline{Proposition}. Si on a M1 à \unsure{M4} et M11, alors pour \unsure{tte} partie \deleted{\unsure{telle}} \inserted{modérée} $Y$ d'un esp. modéré $X$, qui est ens des zéros communs d'une famille finie de fonctions modérées sur $X$, on peut trouver une telle famille qui sépare les pts de $X$ (donc $X/Y$ est un espace modéré).

\mspage{23}
''',[
('deletion','top line','Si x∈X\\Y, ∃α tel que'),
('text','upper','définissent Y comme l’ens des zéros communs'),
('deletion','upper','de X'),
('deletion','upper middle, two lines','∃β tel que fα(x)≠0 gβ(x)≠gβ(y) d’où'),
('text','middle','Si les fα ne suffisent pas'),
('deletion','middle lower','d’où'),
('display','lower middle','fαgβ(x)=λgβ(x)≠fαgβ(y)=λgβ(y)'),
('text','lower','Donc :'),
('text','lower','Proposition. Si on a M1 à M4 et M11'),
('deletion','within Proposition','telle'),
('insertion','above cancelled telle','modérée'),
('text','bottom left','23')], observations='The proposition supplies a construction separating points outside the zero set, but the final sentence visibly says the family separates the points of X. This is retained as written. The lambda annotation is placed under gβ(x), following its visible brace rather than moving it to the factor that would make mathematical sense.')
