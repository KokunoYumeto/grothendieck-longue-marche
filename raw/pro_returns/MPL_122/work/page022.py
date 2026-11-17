from record import save
save(22,r'''\scanpage{22}
\textcircled{e}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
&\mathbb R\Gamma(W_0)\simeq\mathbb R\Gamma(Q)\simeq\mathbb R\Gamma(\mathring Q) \arrow[dl,dashed,"\beta'"']\\
{\begin{tikzpicture}[baseline=(current bounding box.center)]\node[draw,ellipse,inner sep=6pt] {$[\mathbb R\Gamma_!(\mathring P)]$};\end{tikzpicture}} \arrow[r,dashed] &\mathbb R\Gamma(W) \arrow[u,"\rho_1\ \text{compatible aux cup}"]
\end{tikzcd}}
\margin{\uline{NB} $\rho_1=\alpha\rho_0$\par\deleted{\unsure{a}}}

[Suite exacte de cohomologie relative pour $(W,W_0)$, ou $(W,Q)$, ou $(W,\mathring Q)$].

\uline{NB}. On a un hom \inserted{$(u_0,u_1,u_2)$} du triangle \textcircled{e} dans le triangle \textcircled{b}, \unsure{induit} par $(P,\partial P)\subset(W,Q\inserted{\unsure{W_0}\deleted{\unsure{W}}})$, avec
\[
u_1=\rho_0,\qquad u_2=\operatorname{inj}_1
\]
et qui induit un isom $u_0$ qu'on aura à identifier \unsure{aux isos canons aux} $\unsure{\simeq|=}$ \unsure{objets} ....).
\margin{à \unsure{prouver} dans le cas algébrique; \unsure{donnera} \unsure{la justif. formelle} l'auto-dualité de $W$ et \unsure{une donnée de ce type} la donnée \textcircled{a'} plus bas}

\figure{\begin{tikzpicture}\draw (0,0)--(13,.4);\draw (3.5,.12)--(13,.45);\end{tikzpicture}}

Supposons $W$ non singulière, i.e. $\mathring M$ non singulière, i.e. $\mathring P$ non singulière. Alors on a un isomorphisme
\[
\mathbb R(\Gamma,\pi)_!(\mathring M)\simeq\mathbb R\operatorname{Hom}_{\Lambda}\left(\underset{\substack{\Vert\\\mathbb R(\Gamma,\pi)(M)}}{K^\bullet},\Lambda\right)[-2n]
\]
et la flèche verticale de \textcircled{a} est une flèche
\diagram{\begin{tikzcd}[column sep=large]
\boxed{u:\ \mathbb R\operatorname{Hom}_{\Lambda}(K^\bullet,\Lambda)[-2n]\longrightarrow K^\bullet}&\text{dans }\mathrm D(\Lambda[\pi])
\end{tikzcd}}
i.e. un élément de
\[
\deleted{\unsure{\mathbb R\Gamma(\Lambda)}}\ H^{2n}(K^\bullet\overset{\mathrm L}{\otimes}_{\Lambda}K^\bullet)
\]
La donnée fondamentale \textcircled{a} devient
\textcircled{a'}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
& L^{\bullet\,\mathrm{triv}} \arrow[dl,"\rho'"']\\
\mathbb R\operatorname{Hom}_{\Lambda}(K^\bullet,\Lambda)[-2n] \arrow[r,very thick] &K^\bullet \arrow[u,"\rho"]
\end{tikzcd}}
\margin{$K^\bullet\in\operatorname{ob}\mathrm D(\Lambda[\pi])$;\par
$L^\bullet\in\operatorname{ob}\mathrm D(\Lambda)$\par
$K^\bullet$ parfait rel. à $\Lambda$}

En fait, $\rho$ et $\rho'$ \uuline{sont transposés} \uline{l'un de l'autre} (signe ?)
\mspage{21}
''',[
('text','top left','circled e'),
('diagram','top','RΓ(W0)≃RΓ(Q)≃RΓ(interior Q); [RΓ!(interior P)]; RΓ(W)'),
('drawing','top triangle left','oval around bracketed RΓ!(interior P)'),
('margin note','top right','NB ρ1=αρ0'),
('deletion','under top-right NB','a'),
('text','below triangle','[Suite exacte de cohomologie relative pour (W,W0), ou (W,Q), ou (W,interior Q)]'),
('text','middle NB','On a un hom du triangle e dans le triangle b'),
('insertion','after hom','(u0,u1,u2)'),
('insertion','below Q in pair (W,Q)','W0'),
('deletion','next to W0 insertion','W'),
('display','middle','u1=ρ0, u2=inj1'),
('text','middle lower','et qui induit un isom u0 qu’on aura à identifier'),
('margin note','slanted left margin','à prouver dans le cas algébrique; auto-dualité de W; a′ plus bas'),
('drawing','across page centre','double separating rule'),
('text','below rule','Supposons W non singulière'),
('display','lower middle','R(Γ,π)!(interior M)≃RHomΛ(K bullet,Λ)[−2n]'),
('text','below isomorphism','et la flèche verticale de a est une flèche'),
('diagram','boxed formula','u:RHomΛ(K bullet,Λ)[−2n]→K bullet dans D(Λ[π])'),
('text','below box','i.e. un élément de'),
('deletion','before H^{2n}','RΓ(Λ)'),
('display','lower','H^{2n}(K bullet⊗^L_ΛK bullet)'),
('text','above last triangle','La donnée fondamentale a devient'),
('diagram','bottom triangle a′','L bullet triv; RHomΛ(K bullet,Λ)[−2n]; K bullet; ρ′; ρ'),
('margin note','right of bottom triangle','K bullet∈ob D(Λ[π]); L bullet∈ob D(Λ); K bullet parfait rel. à Λ'),
('text','bottom','En fait, ρ et ρ′ sont transposés l’un de l’autre (signe ?)'),
('margin note','bottom left','21')
],[
('middle NB','induit','A heavy stroke passes through the middle letters, possibly retracing rather than deletion.','medium'),
('pair (W,Q)','Q with W0 added beneath','No secure strike through Q; the addition and its adjacent black mark are retained.','low'),
('last line before rule','aux isos canons aux ≃ objets ....)','Very compressed unfinished parenthetical phrase; word division and final noun uncertain.','low'),
('slanted left margin','à prouver ... donnera la justif. formelle ... une donnée de ce type','Least secure prose on this sheet; each uncertain group is marked in place after rotated enlargement.','low'),
('cancelled expression before H^{2n}','RΓ(Λ)','Dense overwriting leaves only parts of R, Γ and a parenthesis secure.','low'),
('last line','(signe ?)','This is the author’s own question mark, distinct from editorial reading doubt.','high')
],['The comparison u0 of triangles is explicitly left to be identified; a marginal algebraic-case verification is difficult to read.','The auto-duality construction assumes nonsingularity and produces u from a tensor cohomology class.','The assertion that ρ and ρ′ are transposes ends with the author’s explicit signe ?.'])
