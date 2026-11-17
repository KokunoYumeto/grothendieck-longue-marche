from record import save
save(20,r'''\scanpage{20}
\textcircled{a}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
& L^{\bullet\,\mathrm{triv}}=\mathbb R\deleted{\unsure{(\Gamma,\pi)}}\Gamma_{\unsure{*}}(W_0)^{\mathrm{triv}} \arrow[dl,dashed] \arrow[r,bend left] & \text{on met dessus op. triviale de $\pi$}\\
{\begin{tikzpicture}[baseline=(current bounding box.center)]\node[draw,ellipse,inner sep=6pt] {$\begin{gathered}[R^\bullet]\\\Vert\\\mathbb R(\Gamma,\pi)_!(\mathring M)\end{gathered}$};\end{tikzpicture}} \arrow[r,dashed] & K^\bullet=\mathbb R(\Gamma,\pi)_{\unsure{*}}(M) \arrow[u,"\rho\ \text{compatible aux cup}"] &
\end{tikzcd}}
\margin{dans catégorie dérivée de $\Lambda[\pi]$}

\textcircled{b} Appliquons $\mathbb R\Gamma^\pi$ à \textcircled{a}, on trouve
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
& {\begin{gathered}L^{\bullet\pi}=\mathbb R\Gamma(W_0\times S^1)\simeq\mathbb R\Gamma(W_0)\overset{\mathrm L}{\otimes}_{\Lambda}\mathbb R\Gamma(S^1)\\\simeq\mathbb R\Gamma(W_0)\times\mathbb R\Gamma(W_0)(-1]\end{gathered}} \arrow[dl,dashed]\\
{\begin{tikzpicture}[baseline=(current bounding box.center)]\node[draw,ellipse,inner sep=6pt] {$\begin{gathered}[R^{\bullet\pi}]\\\Vert\\\mathbb R\Gamma_!(\mathring P)\end{gathered}$};\end{tikzpicture}} \arrow[r,dash,dashed] \arrow[d,equal] & K^{\bullet\pi}=\mathbb R\Gamma(P)=\mathbb R\Gamma(W-W_0) \arrow[u,"(\alpha,\beta)",very thick]\\
\mathbb R\Gamma_!(W-W_0)&
\end{tikzcd}}
\margin{Suite exacte de cohomologie relative pour $(P,\partial P=S^1\times W_0)$}
\diagram{\begin{tikzcd}[column sep=large]
\mathbb R\Gamma(P)\simeq\mathbb R\Gamma(W-W_0) \arrow[r,"\text{compatible aux cup}","\alpha"'] &\mathbb R\Gamma(W_0)\\
\mathbb R\Gamma(P)=\mathbb R\Gamma(W-W_0) \arrow[r,"\beta",very thick] &\mathbb R\Gamma(W_0)(-1)
\end{tikzcd}}
\margin{s'identifie sur la cohomologie au $\partial$ de la suite exacte de \unsure{dévolution} qui relie $H^i(W-W_0)$ et $H^{i-1}(W_0)$ ...}

\textcircled{c} Appliquons foncteur oubli $\omega$ à \textcircled{a}, on trouve
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
&L^\bullet=\mathbb R\Gamma(W_0) \arrow[dl,dashed]\\
{\begin{tikzpicture}[baseline=(current bounding box.center)]\node[draw,ellipse,inner sep=6pt] {$\begin{gathered}[R^\omega]\\\Vert\\\mathbb R\Gamma_!(\mathring M)\end{gathered}$};\end{tikzpicture}} \arrow[r,dash,dashed] & K^{\bullet\omega}=\mathbb R\Gamma(M) \arrow[u,"\text{compatible aux cup}"]
\end{tikzcd}}

\textcircled{d}
\margin{NB. c'est le $\beta$ de \textcircled{b}}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
&\mathbb R\Gamma(P)\simeq\mathbb R\Gamma(W-W_0) \arrow[dl,"\beta"',very thick]\\
\mathbb R\Gamma(W_0)(-2] \arrow[r] & [\mathbb R\Gamma_!(W)] \arrow[u,"\rho\ \text{compatible avec cup}"']
\end{tikzcd}}
[Suite exacte en \unsure{Cohomologie|cohomologie} relative pour $(W,W-W_0)$, ou au choix pour $(W,P)$]
\margin{Permet de trouver $\mathbb R\Gamma(W)$ en fonction de \textcircled{a}}
\mspage{19}
''',[
('text','upper left','circled a'),
('diagram','top','L bullet triv; [R bullet]; K bullet; ρ'),
('deletion','top after derived R','(Γ,π)'),
('margin note','top right linked from triv','on met dessus op. triviale de π'),
('margin note','upper right','dans catégorie dérivée de Λ[π]'),
('drawing','top left around R','ellipse around [R bullet]=R(Γ,π)!(interior M)'),
('text','below top triangle','circled b; Appliquons RΓ^π à a'),
('diagram','upper middle','L bullet π=RΓ(W0×S¹), K bullet π, R bullet π'),
('drawing','middle left','ellipse around R bullet π and RΓ!(interior P)'),
('margin note','middle right','Suite exacte de cohomologie relative pour (P,∂P=S¹×W0)'),
('diagram','middle','RΓ(P)≃RΓ(W−W0)→α RΓ(W0)'),
('diagram','below α','RΓ(P)=RΓ(W−W0)→β RΓ(W0)(−1)'),
('margin note','below β','s’identifie sur la cohomologie au ∂'),
('text','lower middle','circled c; Appliquons foncteur oubli ω'),
('diagram','lower middle','L bullet=RΓ(W0), K bullet ω=RΓ(M), R^ω'),
('drawing','lower left triangle','ellipse around R^ω and RΓ!(interior M)'),
('text','lower left','circled d'),
('margin note','beside d','NB. c’est le β de b'),
('diagram','bottom','RΓ(P)≃RΓ(W−W0); RΓ(W0)(−2]; [RΓ!(W)]'),
('text','bottom two lines','[Suite exacte en Cohomologie relative pour (W,W−W0), ou au choix pour (W,P)]'),
('margin note','bottom right','Permet de trouver RΓ(W) en fonction de a'),
('margin note','bottom left','19')
],[
('a), after derived R','(Γ,π) (deleted)','Dense scribble before Γ; only the best reading can be offered.','low'),
('a), Γ subscripts','*','Small star-like marks beneath both Γ occurrences; distinct from ! in the left object.','medium'),
('a), notation R','mathbb R','The derived-functor R is drawn with doubled vertical stems, unlike the separate object R.','high'),
('b), product formula','(-1]','Round opening and square closing marks retained as visible.','high'),
('b), β annotation','dévolution','Word after “suite exacte de” is compressed; do not substitute a familiar name for the sequence.','low'),
('c), superscripts','R^ω, K^{bullet ω}','No separate bullet securely visible on the R object.','medium'),
('d), lower left object','(-2]','Again a round opening with square closing shift mark.','high'),
('last bracketed note','Cohomologie|cohomologie','Initial letter much larger than the following letters.','medium')
],['Four labelled constructions a–d: equivariant triangle, derived invariants, forgetting action, and relative triangle.','The β arrow of d is explicitly identified with β of b despite the visible shifts; record relation without repairing it.','Compatibility with cup products is repeatedly asserted, with no proof on this sheet.','The β identification uses a difficult word read as dévolution and visible degrees i and i−1.'])
