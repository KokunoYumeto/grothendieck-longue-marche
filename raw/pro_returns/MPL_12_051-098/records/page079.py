from save_page import save_page
save_page(79,r'''\scanpage{79}
% archive foliation: 78
fait $H^1(\mathbf{F}_p,A^{\mathrm{fix}})=0$ (Lang) et $H^1(\mathbf{F}_p,M)=\text{fini}$ [\unsure{trivial} ; Attention qu'il s'agit de la coh. \uline{étale}, i.e. de la coh. \uline{galoisienne} de $\widehat{\mathbf{Z}}$ !], donc la dernière flèche verticale du diagramme (\unsure{D|b}) est aussi bijective :
\[
H^1(S,A)(\ell)\xrightarrow{\sim}H^1(\overline{S},\overline{A})^\pi(\ell)
\]
\margin{\uline{surj. à noyau fini} ...}
Donc la \uline{conjecture} précédente signifie aussi
\[
\boxed{H^1(\overline{S},\overline{A})(\ell)^\pi=\text{groupe fini}}
\]

\deleted{Il y a une façon de le prouver,}
C'est \inserted{aussi} $\pm$ équiv. (via des jacobiennes) à ceci : $X\longrightarrow S$ morphisme propre [lisse de dim relative $1$], $S$ régulier de type fini sur $\mathbf{Z}$. Prouver que
\[
H^2(S,\mathbf{G}_m)\longrightarrow H^2(X,\mathbf{G}_m)
\]
est surjectif mod groupes finis ??
\figure{\begin{tikzpicture}[x=1mm,y=1mm]\draw (0,0) ellipse(.6mm and .5mm);\draw (0,0)--(5,8);\draw[->] (1.5,4)--(-5,8);\end{tikzpicture}}

\margin{\uline{NB} On devrait avoir $H^{\unsure{i|2}}(S,A)(\ell)$ fini aussi pour $\uuline{i\ge3}$, $S$ de type fini sur $\mathbf{Z}$, $\ell$ premier avec \unsure{car.} visiblement \unsure{on} (\inserted{\uline{NB}} si $i\ge2$, $T_\ell(H^i(S,A)(\ell))\simeq H^i(S,T_\ell(A))$)}
\margin{\unsure{donc les seuls} \illegible{1} \unsure{qui restent} sont $H^0$ et $H^2$ pour $A$, et \deleted{$\unsure{H^0}$}, $H^1$, $H^2$ pour $T_\ell(A)$}
''',[
('top','text','fait H^1(F_p,A^fix)=0 (Lang)'),
('upper','text','H^1(F_p,M)=fini; Attention ... coh. étale'),
('upper middle','text','donc la dernière flèche verticale'),
('middle','display','H^1(S,A)(l) →~ H^1(Sbar,Abar)^π(l)'),
('middle','text','Donc la conjecture précédente signifie aussi'),
('middle','display','H^1(Sbar,Abar)(l)^π = groupe fini'),
('middle lower','text','Il y a une façon de le prouver'),
('lower','text','C’est aussi ± équiv. via des jacobiennes'),
('lower','display','H^2(S,G_m) → H^2(X,G_m)'),
('lower','text','est surjectif mod groupes finis ??'),
('lower left','drawing','loop, rising stroke and leftward arrow'),
('bottom','margin note','NB On devrait avoir H^i(S,A)(l) fini aussi'),
('bottom left slanting','margin note','donc les seuls ... H^0 et H^2 pour A')
],remarks='Both halves, top qualification and footer enlarged; slanted bottom-left marginal addition rotated 35 degrees and enlarged. One word in marginal addition remains unreadable. No words supplied to complete the interrupted car./visiblement clause.')
