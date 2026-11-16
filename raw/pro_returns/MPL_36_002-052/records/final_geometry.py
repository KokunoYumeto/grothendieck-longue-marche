from reconcile import revise,ROOT
revise(41,r'\arrow[d,shift left=18mm]',r'\arrow[d,shift right=18mm]','Placed the downward arrow on the left of the paired terms, matching the ink; TikZ shift is relative to arrow direction.')
p=ROOT/'pages/MPL_36_002-052_36_scan043.tex'; s=p.read_text()
a=s.index('\\[\n\\underline{\\operatorname{Ext}}^i_X(')
b=s.index('\\[\n\\boxed{G',a)
old=s[a:b]
new=r'''\figure{\begin{tikzpicture}[baseline=(d.base)]
\node[inner sep=0pt] (d) {$\underline{\operatorname{Ext}}^i_X(\underset{\inserted{\unsure{R}}}{f^*}(G),G_m)
\simeq\underline{\operatorname{Ext}}^i_Y(G,
\begin{tikzpicture}[baseline=(p.base)]
\node[draw,ellipse,inner xsep=5pt,inner ysep=12pt] (p) {$\underline{\operatorname{Pic}}^{\bullet}_{X/Y}$};
\node[anchor=south] at (p.north) {\unsure{les supérieurs}};
\draw ([xshift=-1pt,yshift=3pt]p.south)--++(0,-8mm);\draw ([xshift=1pt,yshift=3pt]p.south)--++(0,-8mm);
\end{tikzpicture})$};
\node[anchor=north] at ([xshift=-28mm,yshift=-2mm]d.south) {$\deleted{\unsure{R\Gamma(X,}}$};
\draw ([xshift=-13mm,yshift=2mm]d.south)--++(.02,-.7)--++(.16,-.4);
\draw ([xshift=-11mm,yshift=2mm]d.south)--++(.01,-.7)--++(-.03,-.4);
\end{tikzpicture}}
'''
revise(43,old,new,'Attached the cancelled R Gamma fragment and left double stroke beneath the corresponding Ext formula, preserving their source positions instead of detached paragraph placement.')
revise(43,r'H^2(X,D(G))\neq&',r'H^2(X,D(G))\underset{!}{\neq}&','Attached the exclamation mark below the degree-two non-equality, where the manuscript places it.')
revise(43,'\\margin{$!$}\n','', 'Removed the detached duplicate of the now positioned exclamation mark.')
