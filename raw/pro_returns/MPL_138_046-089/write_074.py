from workflow import save_page
save_page(74,r'''\scanpage{74}
% archive foliation: 73
on devra expliciter dans le paradigme
le passage d'une description à
l'autre.

\deleted{La description \unsure{$S\ne\varnothing$}}

1) Cas $\mathcal J=\varnothing$. On va supposer, pour
notre description, que l'on n'est
pas dans les cas $g=0$, $\nu=0,1$
($g=$ genre de $\widehat X$, $S=\operatorname{Card}\nu$)
On associe à $(\widehat X,\widehat o,S)$ \inserted{$(\leadsto)(X,o)$} le
groupe fondamental $\Pi=\pi_1(X)$, considéré
comme groupe extérieur, mais
muni de \unsure{sa|ses} $T$-\unsure{structures|structure} :
locales indexées par $S$, i.e. une
\deleted{famille}\inserted{application}
\[
S\longrightarrow\operatorname{Homext}(T,\Pi)
\]
\deleted{$\unsure{(\varphi_s)_{s\in S}}$}
\inserted{\textcircled{\unsure{1|4}} (Ceci permet
\deleted{$\unsure{\varphi_s\in\Pi}$} de définir
$\Pi_{\unsure{\wedge|1}}\ (\simeq\pi_1(\widehat X))$ comme
groupe quo. de $\Pi$ par le sous-groupe inv. engendré par les
$T\longrightarrow\Pi$.
Si $\nu=0$ i.e. $S=\varnothing$ il faut de
plus \unsure{en} donner un iso
$T\longrightarrow[\unsure{\bigwedge^2\Pi_{\wedge\mathrm{ab}}}]^\vee$
\unsure{qui} \unsure{de} $T$. \unsure{ou une forme}
i.e. \unsure{primitive} \unsure{sur}
\unsure{le groupe} \unsure{du} \unsure{dual} \unsure{ext.}
de \deleted{$\unsure{\Pi}$} $\unsure{\Pi_\wedge}$.)}
Ceci donne \inserted{\textcircled{$=$}} une description
$1$-isotopique, et $=$ $\infty$-isotopique,
sauf si $g=0$, $\nu=2$ et $g=1$, $\nu=0$,
où les composantes neutres
''',[
('text','upper','on devra expliciter dans le paradigme'),
('deletion','upper','La description S≠∅'),
('text','upper-middle','1) Cas J=∅'),
('insertion','middle','(↝)(X,o)'),
('text','middle','On associe à (Xhat,ohat,S)'),
('deletion','lower-middle','famille'),
('insertion','lower-middle','application'),
('display','lower-middle','S → Homext(T,Π)'),
('deletion','below display','(φ_s)_{s∈S}'),
('insertion','lower interlinear and left margin','Ceci permet de définir Π_∧'),
('deletion','within insertion','φ_s∈Π'),
('display','left margin within insertion','T → [∧²Π_∧ab]^∨'),
('deletion','left margin lower','Π'),
('insertion','lower','circled equality marker'),
('text','bottom','Ceci donne une description 1-isotopique')])
