from save_page import save_page
save_page(94,r'''\scanpage{94}
% archive foliation: 93
\uline{équivaut} à celle de
$\mathrm{cl}\,H^{2n}_!(X,F)-\mathrm{cl}\,H^{2n-1}_!(X,F)$
mod. les $=$ choses. On peut supposer $X$
[affine et] lisse sur $\mathbf F_p$, \inserted{(\deleted{\unsure{pure}}\inserted{\unsure{purement}} de dim $n$)} alors $H^{2n}_!(X,F)$
est dual de
\[
H^0(X,\mathcal Hom(F,\mathbf Q_\ell(n)))=H^0(X,\check F)(n),
\]
\inserted{donc} purement de poids $2n$. D'autre part, $H^{2n-1}_!(X,F)$
est dual de $H^1(X,\mathcal Hom(F,\mathbf Q_\ell(n)))$, et admet
une pièce de poids $2n-1$ \uline{et} des poids $2n-2$.
\margin{\uline{peut se raffiner}, \uline{en regardant une}
\uline{autre filtration} \uline{que par les poids},
\uline{savoir \unsure{le niveau|la dimension}}}

\deleted{Une analyse}
Si $F=\mathbf Q_\ell(0)$, \deleted{alors} donc
\deleted{le cas} si on s'occupe des fonctions $\zeta$
habituelles, la connaissance ``birationnelle
grossière'' de $\zeta$ est essentiellement équivalente à :
celle de $\pi_0(\bar X)$ comme Frob-ensemble,
et celle de l'Albanèse de $X$ sur $\mathbf F_p$\ldots
\margin{Modulo conjectures de Tate}

Une analyse plus serrée \deleted{\unsure{de ces faits}} (plus
fine que par les seuls \uline{poids}, mais en
utilisant aussi les niveaux) permet de
récupérer plus par la connaissance de
$\zeta(X\deleted{,F})$ \inserted{(disons, en prenant $F=\mathbf Q_\ell$)} modulo les
$\zeta(Y\deleted{,\unsure{F}})$ ($\dim Y<n$)
\deleted{poids $\unsure{\le\rho}$}
''',[
('top','text','équivaut à celle de cl H^2n_!(X,F) - cl H^{2n-1}_!(X,F)'),
('upper','text','mod. les = choses; X affine et lisse sur F_p, de dim n'),
('upper-middle','formula','H^2n_! dual de H^0(X,Hom(F,Q_l(n)))=H^0(X,F check)(n)'),
('middle','text','purement de poids 2n; H^{2n-1}_! dual de H^1'),
('middle','text','pièce de poids 2n-1 et des poids 2n-2'),
('left margin','margin note','peut se raffiner; autre filtration que par les poids; niveau/dimension'),
('middle','text','Si F=Q_l(0), fonctions zêta habituelles'),
('lower-middle','text','connaissance birationnelle grossière; pi_0(Xbar) comme Frob-ensemble'),
('lower-middle','text','Albanèse de X sur F_p'),
('lower-left margin','margin note','Modulo conjectures de Tate'),
('lower','text','Une analyse plus serrée, plus fine que par les seuls poids; niveaux'),
('bottom','formula','zeta(X) modulo les zeta(Y), dim Y<n'),
('bottom','insertion','disons, en prenant F=Q_l')
],remarks='Whole and halves inspected; full slanting left note rotated, dual F caron confirmed by crop, revised footer enlarged. Equal-sign abbreviation in mod. les = choses retained. Final cancelled weight expression remains uncertain.')
