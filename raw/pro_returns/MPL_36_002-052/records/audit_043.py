from audit_page import audit
changes=[
(r'\overset{\text{\unsure{les supérieurs}}}{\boxed{\underline{\operatorname{Pic}}^{\bullet}_{X/Y}}}',r'''\begin{tikzpicture}[baseline=(p.base)]
\node[draw,ellipse,inner xsep=5pt,inner ysep=12pt] (p) {$\underline{\operatorname{Pic}}^{\bullet}_{X/Y}$};
\node[anchor=south] at (p.north) {\unsure{les supérieurs}};
\draw ([xshift=-1pt,yshift=3pt]p.south)--++(0,-8mm);\draw ([xshift=1pt,yshift=3pt]p.south)--++(0,-8mm);
\end{tikzpicture}'''),
(r'\draw (2,1)--(2,0);\draw (2.08,1)--(2.08,0);',''),
(r'\begin{array}',r'\diagram{\begin{array}'),
(r'\end{array}',r'\end{array}}'),
(r'H^{\unsure{i-1|i+j}}',r'H^{i-1}'),
(r'_{\unsure{g}}(G,\operatorname{Pic}^{q}',r'_{\unsure{q|g}}(G,\operatorname{Pic}^{q}'),
(r'\operatorname{Ext}^{\unsure{i}}(G',r'\operatorname{Ext}^{\unsure{i|p}}(G')
]
audit(43,changes,notes='Whole page and enlarged lower array reread. Restored the oval around dotted Pic and its attached double stroke; retained exclamation-mark f upper/lower operations and the unshifted first duality display. Wrapped both tabulations as diagrams. The final H exponent is visibly i-1; spectral indices and clipped rightmost Pic term retain doubt.')
