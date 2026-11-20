from audit_tools import *
old=r'\overset{\simeq\mathrm{Ab}_*}{\mathcal B_0}'
new=r'''\tikz[baseline=(bo.base)]{\node (bo) {$\mathcal B_0$};
\node[anchor=south] (ab) at ([yshift=7pt]bo.north) {$\simeq\mathrm{Ab}_*$};
\draw ([xshift=-7pt,yshift=-6pt]bo.west) .. controls ([xshift=-10pt,yshift=6pt]bo.west) and ([xshift=8pt,yshift=4pt]bo.north) .. (ab.east);}'''
oldbox=r'''\[
\boxed{F(X_*)=\Omega_{*}(\mathbb C_*^{(X)})=\Omega_\bullet(\mathbb C_\bullet(X))}
\]'''
newbox=r'''\figure{\begin{tikzpicture}
\node[inner sep=9pt] (fx) {$F(X_*)=\Omega_{*}(\mathbb C_*^{(X)})=\Omega_\bullet(\mathbb C_\bullet(X))$};
\draw ([xshift=-3pt,yshift=3pt]fx.north west) -- ([xshift=-8pt,yshift=10pt]fx.north)
 -- ([xshift=3pt,yshift=4pt]fx.north) -- ([yshift=-2pt]fx.north east)
 .. controls ([xshift=5pt,yshift=-3pt]fx.north east) and ([xshift=4pt]fx.east) .. ([xshift=1pt,yshift=-4pt]fx.east);
\draw ([xshift=-3pt,yshift=3pt]fx.north west) -- ([xshift=-2pt,yshift=7pt]fx.south west)
 .. controls ([xshift=-2pt,yshift=-3pt]fx.south west) and ([xshift=5pt,yshift=-3pt]fx.south west) .. ([xshift=10pt,yshift=-2pt]fx.south west)
 -- ([xshift=4pt,yshift=1pt]fx.south east);
\end{tikzpicture}}'''
finish(355,replacements=[(old,new),(oldbox,newbox)],changes=[change('callout linking B_0 to upper Ab_* annotation','annotation above B_0 without connecting stroke','Ab_* written on the earlier equality line; callout omitted','upper annotation with curved headless callout','A curved line starts below-left of B_0 and rises toward the Ab_* annotation.','drawing or diagram',True,True,'high','page'),change('enclosure of F(X_*) formula','regular box','regular box','sloping stepped top, rounded lower-left and open right gap','The upper edge rises then steps down near the centre; the left edge rounds into the lower stroke and the right ends do not meet.','drawing or diagram',True,True,'high','page')],note='Reread the two differently oriented halves. Added the omitted curved callout at B_0 and replaced the regular boxed-formula outline with the drawn sloping/stepped, open-right enclosure. Confirmed all opposite-category signs, the separate C_* membership fragment, hook directions, four headless lower curves, circled deleted node, Hom underlines, the ab subscripts, two inclusions, all four triangle arrows and final opposed phi/psi arrows. No reading is supplied for the unfinished Hom trials.')
