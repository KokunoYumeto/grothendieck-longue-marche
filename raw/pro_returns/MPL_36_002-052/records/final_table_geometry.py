from reconcile import revise,ROOT
p=ROOT/'pages/MPL_36_002-052_36_scan036.tex';s=p.read_text();a=s.index('\\margin{Cohomologie');b=s.index('\\diagram{\\begin{array}',a)
revise(36,s[a:b],r'''\figure{\begin{tikzpicture}[baseline=(t.base)]
\node[inner sep=0pt] (t) {''','Integrated the cohomology table and its left brace into one TikZ figure so the brace covers the first two rows as in the source.')
revise(36,'\\end{array}}\n\\margin{35}',r'''\end{array}}};
\coordinate (a) at ($(t.north west)!.07!(t.south west)$);
\coordinate (b) at ($(t.north west)!.60!(t.south west)$);
\coordinate (c) at ($(t.north west)!.95!(t.south west)$);
\draw ([xshift=-3mm]a) .. controls ([xshift=-7mm]a) and ([xshift=-4mm,yshift=9mm]b) .. ([xshift=-5mm,yshift=2mm]b)
.. controls ([xshift=-6mm]b) and ([xshift=-7mm]b) .. ([xshift=-9mm]b)
.. controls ([xshift=-2mm]b) and ([xshift=-7mm,yshift=4mm]c) .. ([xshift=-3mm]c);
\node[rotate=90,anchor=south] at ([xshift=-11mm,yshift=7mm]b) {\begin{minipage}{5cm}\margin{Cohomologie discrète}\end{minipage}};
\node[anchor=east] at ([xshift=-10mm,yshift=-5mm]b) {\begin{minipage}{8mm}\margin{$*$\unsure{[}}\end{minipage}};
\end{tikzpicture}}
\margin{35}''','Positioned the marginal title vertically beside its brace and kept the small star/bracket mark beneath it; no transcription wording changed.')
