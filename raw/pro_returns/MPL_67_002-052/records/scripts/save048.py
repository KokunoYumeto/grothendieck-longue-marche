import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(48,r'''\mspage{1}
% archive foliation: 50
\unsure{10369CNU|10369GNU}\qquad 15.1.

$X$ \deleted{non singulière} \inserted{lisse de type $g,\nu$} (sur $\overline{\mathbb Q}$)

$Y$ stable non lisse type $(g,\nu)$ avec propagateur normal $N$ d'où un groupe fondamental \unsure{ét.}\deleted{\unsure{indép.}} $\pi_1([Y,N])$

\diagram{\begin{array}{c}X\overset f{\underset T\simeq}Y\end{array}} un isomorphisme de Teichmüller.

\uline{NB} Cet isomorphisme induit un isom de groupes extérieurs \deleted{\unsure{celui est de}} (\unsure{il est déterminé} plus bas)
\diagram{\begin{tikzcd}[column sep=large]\pi_1(X)\arrow[r]&\pi_1([Y,N])\end{tikzcd}}

Quand on se donne un ``pt base sur $X$'' (ordinaire ou à l'infini), et un sur $[Y,N]$ (alors --- et de plus distinct des pts singuliers de $Y$) on a une notion d'isom de Teichmüller respectant les pts marqués, \deleted{et \unsure{d'un}} (on suppose qu'ils sont tous deux à distance finie, ou tous deux à l'infini). Et on trouve alors un isom de groupes (pas ext. !)
\diagram{\begin{tikzcd}[column sep=large]\pi_1(X,\unsure{\bullet|x})\arrow[r]&\pi_1([Y,N],y)\end{tikzcd}}

En tout état de cause, \deleted{\unsure{les}} l'isom extérieur déjà n'est pas compatible avec les actions ext. de $\operatorname{Gal}(\overline{\mathbb Q}/K)$, $K$ \inserted{\unsure{est}} une extension finie de $\overline{\mathbb Q}/\mathbb Q$ assez grande

\margin{\uline{NB} Mettre en évidence \uline{trois} classes de conjugaison d'\deleted{éléments} hom. $\widehat{\mathbb Z}(1)\longrightarrow\pi_1(X)$ (deux seulement si $\nu=0$, l'une des trois est alors ``le vide'').}
''',[
('text','top printed code and handwritten date','10369CNU; 15.1.'),
('text','upper','X ... sur Qbar'),
('deletion','upper','non singulière'),
('insertion','upper','lisse de type g,ν'),
('text','upper','Y stable non lisse type(g,ν) ... propagateur normal N'),
('deletion','upper','indép.'),
('diagram','upper middle','X≃_T^f Y'),
('text','upper middle','un isomorphisme de Teichmüller'),
('text','middle','NB Cet isomorphisme induit ...'),
('deletion','middle','celui est de'),
('diagram','middle','π₁(X)→π₁([Y,N])'),
('text','middle to lower','Quand on se donne un pt base ...'),
('deletion','lower middle','et d’un'),
('diagram','lower middle','π₁(X,•)→π₁([Y,N],y)'),
('text','lower','En tout état de cause ... Gal(Qbar/K)'),
('deletion','lower','les'),
('insertion','lower','est'),
('margin note','bottom','NB Mettre en évidence trois classes de conjugaison'),
('deletion','bottom','éléments')],leads='Dated15.1, authorpage1. Smooth X over Qbar and stable non-smooth Y with normal propagator N; Teichmüller isomorphism induces outer fundamental-group isomorphism, and based version when both points ordinary or at infinity, smooth on Y. Strong claim of noncompatibility with outer Gal(Qbar/K) actions for sufficiently large finite K; no proof on this page. NB task: exhibit three conjugacy classes of hom Zhat(1)→π1(X), two when ν=0 (third is le vide). Must search RESULTS_STATE and congruence/Longue Marche context after freeze; no inference about status beforehand.')
