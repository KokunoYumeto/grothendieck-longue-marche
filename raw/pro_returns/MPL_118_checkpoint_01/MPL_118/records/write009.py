from save_page import save
save(9,r'''\scanpage{9}
% archive foliation: 8
$f:X\unsure{\to}Y$

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\text{\textcircled{\unsure{0}}}\quad f\in C\arrow[r,Leftrightarrow] & \begin{gathered}X_b\to X_{/b}\text{ : adj. à gauche}\end{gathered}\arrow[d,Leftrightarrow] & f\in F\arrow[r,Leftrightarrow] & {}\arrow[d,Leftrightarrow] \\
& \begin{gathered}{}_{a}\backslash X\to{}_{b}\backslash\unsure{X|Y}\text{ à fibres avec}\\\text{objet initial}\end{gathered}\arrow[d,Leftrightarrow] && {}\arrow[d,Leftrightarrow] \\
& \begin{gathered}\text{La catégorie des relèv. d'une}\\\text{flèche }b\to b',\text{ de source}\\\text{donnée }a\in X_b,\text{ a objet initial}\end{gathered} && {}
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\text{\textcircled{2}}\quad f\in\mathrm{Pr}\arrow[r,Leftrightarrow] & \begin{gathered}(\unsure{X_b}\to X_{/b})\text{ \unsure{strong} \inserted{$\leftarrow$} équiv ie coasph.}\\\text{i.e. }\in\mathrm{As}^{\circ}\end{gathered}\arrow[d,Leftrightarrow] & f\in\mathrm{Sm}\arrow[r,Leftrightarrow] & {}\arrow[d,Leftrightarrow] \\
& \begin{gathered}{}_{a}\backslash X\to{}_{b}\backslash Y\text{ à fibres asph.}\\\deleted{\unsure{{}_{a}\backslash X\to{}_{b}\backslash Y}}\quad({}_{a}\backslash X\to{}_{b}\backslash Y)\in S\quad\deleted{\unsure{\Longleftrightarrow({}_{a}X\to{}_{a}X)}}\end{gathered}\arrow[d,Leftrightarrow] && {}\arrow[d,Leftrightarrow] \\
& \begin{gathered}\text{La cat. des rel. d'une flèche }b\to b',\\\text{de source donnée }a\in\mathrm{Ob}\,\unsure{X_b},\text{ est asph.}\end{gathered}\arrow[d,Leftrightarrow] && {}\arrow[d,Leftrightarrow] \\
& \begin{gathered}R^i f_*\text{ commute }\deleted{\unsure{\Longrightarrow}}\text{ aux chgt de base}\\\text{quelc.}\end{gathered} && \begin{gathered}\text{\unsure{Le changt} de base par }f\\\text{commute à }R^i g_*\end{gathered} \\
& \left[\overset{?}{\Longrightarrow}\text{ base change by }f\text{ preserves \unsure{strong} équiv}\right] && \left[\overset{?}{\Longleftarrow}\quad\right]
\end{tikzcd}}
\margin{\diagram{\begin{tikzcd}
{}\arrow[d,Rightarrow]\\
\begin{gathered}({}_{a}X\to{}_{b}Y\text{ is}\\\text{proper}\\\text{with \unsure{trivial}}\\\text{fibers})\end{gathered}
\end{tikzcd}}}

\[
\text{\textcircled{1}}\quad f\in S\Longleftrightarrow
\forall\ g:Y''\to Y',\text{ sur }Y,\text{ si }g\in W,\text{ alors }(g\times_Y X:X''\to X')\in W.
\]

\diagram{\begin{array}{ccc}
\boxed{\left\{\begin{gathered}F\Longrightarrow\mathrm{Sm}\\C\Longrightarrow\mathrm{Pr}\end{gathered}\right.}
& \begin{gathered}\boxed{\mathrm{Sm}\cap\mathrm{Pr}\Longrightarrow S}\\\boxed{T\cap\mathrm{Pr}\subset S,\ T\cap\mathrm{Sm}\subset S}\end{gathered}
& \begin{gathered}\left\{\begin{gathered}C=F^{\circ},\ \deleted{\unsure{C\in C^{\circ}}}\\F=C^{\circ}\end{gathered}\right.\quad S=S^{\circ}\quad
\left\{\begin{gathered}\mathrm{Sm}=\mathrm{Pr}^{\circ}\\\mathrm{Pr}=\mathrm{Sm}^{\circ}\end{gathered}\right.\end{gathered}
\end{array}}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\text{\textcircled{3}}\quad f\in WSC\arrow[r,Leftrightarrow] & \forall b\to b'\text{ dans }Y,\ (X_{/b}\to X_{/b'})\in W\quad\text{\textcircled{a}}\arrow[d,Leftrightarrow] & f\in WSF\arrow[r,Leftrightarrow] & {}\arrow[d,Leftrightarrow] \\
& \left\{\begin{gathered}\forall\ Y''\xrightarrow{u}Y'\text{ sur }Y,\ Y''\text{ et }Y'\ \deleted{\text{\unsure{fibrés}}}\inserted{\text{cofibrés}}\text{ in }C,\\\text{si }u\in W,\text{ alors }(g\times_Y X:X''\to X')\in W\end{gathered}\right.\quad\text{\textcircled{b}}\arrow[d,Leftrightarrow]\arrow[l,Rightarrow] && {}\arrow[d,Leftrightarrow] \\
& \deleted{\unsure{\Longleftrightarrow}}\quad(\mathrm{Cofib}(X/Y)\to Y)\ \deleted{\unsure{\in W}}\in S\ \unsure{\in}\quad\text{\textcircled{a$'$}} && (\mathrm{Fib}(X/Y)\to Y)
\end{tikzcd}}
\margin{$\Longleftarrow$ $R^i f_*(\unsure{c^t})$ loc \unsure{constants}}

\uline{stable par chgt de base par \deleted{fibrations}\inserted{\unsure{fonct.} lisses}},
(mais non par $g\in S$ ?)
\margin{stable par chgt de base \uline{propres}}

\[
\boxed{WSC\cap\mathrm{Pr}\subset S}\qquad
\boxed{WSF\cap\mathrm{Sm}\subset S}
\]

\textcircled{3bis} $f\in WSB\deleted{\unsure{F}}\underset{\mathrm{déf}}{\Longleftrightarrow}$
\inserted{$\deleted{\unsure{\in}}\unsure{WSF}\Longrightarrow$}
pour
\diagram{\begin{tikzcd}
b'_0\arrow[r]\arrow[rrr,bend right=25,"u'"'] & b_0\arrow[r,"u"] & b_1\arrow[r] & b'_1
\end{tikzcd}}
dans $Y$,
\diagram{\begin{tikzcd}[column sep=large]
|[draw,ellipse]| {}_{b_0}\backslash X_{/b_1}\arrow[r]\arrow[d,dash] & |[draw,ellipse]| {}_{b'_0}\backslash X_{/b'_1}\arrow[dl,dash] & \text{est }\in W,\text{ i.e. l'équiv.} \\
\inserted{X[u]} & \inserted{X[u']} &
\end{tikzcd}}
\[
{}_{b_0}\backslash Y_{/b_1}\to{}_{b'_0}\backslash Y_{/b'_1}
\]
\deleted{\unsure{dans}} $Y$ est \unsure{transformée} en équiv. faible par $\unsure{X|Y}\times(?)$.
\[
\Updownarrow\quad\forall b\to b'\text{ dans }Y,\quad
{}_{b'}\backslash X\to{}_{b}\backslash X\text{ est }\in W\text{ loc. sur }Y.
\]
\[
\deleted{\text{et}}\quad\forall b\to b'\text{ dans }Y,\quad
X_{/b}\to X_{/b'}\text{ est }\in W\text{ \unsure{coloc.} sur }Y
\]
''','text',[
('text','top damaged header','f:X→Y'),
('diagram','top paired columns','f∈C; X_b→X_/b adj. à gauche; a\X→b\X; category of lifts; f∈F'),
('diagram','second paired columns','2 f∈Pr; strong équiv ie coasph.; a\X→b\Y; category of lifts; R^i f_*; f∈Sm; R^i g_*'),
('insertion','proper first criterion above équiv','←'),
('deletion','proper second criterion','a\X→b\Y; ⇔(aX→aX)'),
('deletion','proper base-change criterion after commute','⇒'),
('margin note','proper left edge with implication arrow','aX→bY is proper with trivial fibers'),
('text','foot of proper and smooth columns','[⇒? base change by f preserves strong équiv]; [⇐?]'),
('display','middle horizontal band','1 f∈S ⇔∀g:Y″→Y′ sur Y si g∈W alors g×_Y X∈W'),
('diagram','middle boxed band','F⇒Sm; C⇒Pr; Sm∩Pr⇒S; T∩Pr⊂S; T∩Sm⊂S; C=F°; F=C°; S=S°; Sm=Pr°; Pr=Sm°'),
('deletion','duality band after C=F°','C∈C°'),
('diagram','third paired columns','3 f∈WSC; a; b; a′; f∈WSF; Fib(X/Y)→Y'),
('deletion','third columns, second and third criteria','fibrés; ⇔; ∈W'),
('insertion','third columns, over fibrés','cofibrés'),
('margin note','left of third columns','R^i f_*(c^t) loc constants'),
('text','foot of WSC column','stable par chgt de base par fibrations / fonct. lisses; mais non par g∈S?'),
('deletion','stability sentence','fibrations'),
('insertion','stability sentence','fonct. lisses'),
('margin note','foot of WSF column','stable par chgt de base propres'),
('display','boxed band above 3bis','WSC∩Pr⊂S; WSF∩Sm⊂S'),
('text','bottom entry opening','3bis f∈WSB ⇔ déf pour'),
('deletion','bottom entry opening','F; ∈'),
('insertion','above bottom equivalence','WSF ⇒'),
('diagram','bottom composable-arrow string','b′_0→b_0→b_1→b′_1; u; u′'),
('diagram','bottom, circled comma-category objects and annotation lines','b_0\X_/b_1→b′_0\X_/b′_1; X[u]; X[u′]'),
('display','bottom comparison in Y','b_0\Y_/b_1→b′_0\Y_/b′_1'),
('text','bottom explanation','i.e. l’équiv. ... Y est transformée en équiv. faible par X×(?)'),
('deletion','bottom explanation and last line','dans; et'),
('display','bottom penultimate line','∀b→b′ dans Y; b′\X→b\X est ∈W loc. sur Y'),
('display','bottom last line','∀b→b′ dans Y; X_/b→X_/b′ est ∈W coloc. sur Y')
], 'Fragile overview sheet. The first comma-category target visually resembles X, although Y would be a possible alternative: retained with doubt. Empty dual-column slots contain only equivalence arrows on the page and are left empty. The numerous revisions around WSC criterion a′, the crossed class name at 3bis, and the functor X×(?) at the bottom remain low confidence. The manuscript marks the strong-equivalence preservation implication and its dual by question marks, and questions stability for g∈S. These are research leads only; no checking of the claims has yet occurred.')
