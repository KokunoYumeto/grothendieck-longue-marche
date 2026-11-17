from save_page import save_page
save_page(62,r'''\scanpage{62}
% archive foliation: 61
type fini, on a
\[
\mathbf{R}\Gamma_X=\mathbf{R}\Gamma_Y\,\mathbf{R}f
\]
d'où des suites spectrales dans (Ab),
\[
H^*(X,M)\Longleftarrow H^p(Y,R^qf_*(M))
\]

3°) Bien entendu, on veut que $H^i(X,M)=0$ si $i<0$, donc $H^0(X,M)$ est exact à g. De plus, isom fonctoriel
\[
H^0(X,M)=\mathrm{Hom}(\unsure{\mathbf{Q}|\mathbf{Z}}_X(0),M)
\]

[N.B. Rien n'empêche d'introduire des hyperext
\[
\unsure{\mathbb{E}\mathrm{xt}^i|\mathrm{Ext}^i}(X,M,N)=\mathbb{H}^i(X,\mathbf{R}\mathrm{Hom}(M,N)).
\]
]
Cela redonne bien, par le n° 7
\[
\mathrm{Hom}(M,N)\simeq\unsure{\mathbb{E}\mathrm{xt}^0|\mathrm{Ext}^0}(X,M,N)
\]
et on espère que $\mathrm{Ext}^1(X,M,N)$ est bien l'ensemble des \uline{classes} \uline{d'extensions} de $M$ par $N$. [On aimerait pouvoir dire que
''',[
('top continuation','text','type fini, on a'),
('upper','display','R Gamma_X = R Gamma_Y R f'),
('upper','text',"d'où des suites spectrales dans (Ab)"),
('upper-middle','display','H^*(X,M) <= H^p(Y,R^q f_*(M))'),
('middle','text','3°) Bien entendu; H^i=0 si i<0; exact à g.'),
('middle','display','H^0(X,M) = Hom(Q_X(0),M)'),
('lower-middle','text',"N.B. Rien n'empêche d'introduire des hyperext"),
('lower-middle','display','Ext^i(X,M,N)=H^i(X,R Hom(M,N))'),
('lower','text','Cela redonne bien, par le n° 7'),
('lower','display','Hom(M,N) ~= Ext^0(X,M,N)'),
('bottom','text',"et on espère; classes d'extensions; On aimerait pouvoir dire que")],remarks='Whole page and halves compared. Double-stroked hypercohomology H retained; doubled E in hyper-Ext remains doubtful. No subscript supplied on Rf in first display because none is visible.')
