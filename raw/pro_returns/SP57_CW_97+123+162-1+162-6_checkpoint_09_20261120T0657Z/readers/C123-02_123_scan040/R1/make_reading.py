from pathlib import Path
p=Path('out/readers/C123-02_123_scan040/R1')
s=Path('packets/C123-02_123_scan040/C.tex').read_text()
def rep(old,new):
 global s
 assert old in s,old
 s=s.replace(old,new,1)
rep(r'\mspage{\handwritten{23}}',r'''\mspage{\handwritten{\begin{tikzpicture}[baseline=(p.base)]
\node[inner sep=1pt] (p) {23};
\draw ([xshift=-1mm,yshift=-1mm]p.south west) .. controls ([xshift=-1mm,yshift=3mm]p.north west) and ([xshift=2mm,yshift=3mm]p.north) .. ([xshift=1mm,yshift=1mm]p.north east);
\end{tikzpicture}}}''')
rep(r'inductives)\handwritten{)}.',r'''inductives)\handwritten{\unsure{\begin{tikzpicture}[baseline=-.5ex,x=1ex,y=1ex]\draw (0,1.7) .. controls (.65,.7) and (.6,.15) .. (0,-.4);\end{tikzpicture}}}.
% The close-shaped pen trace may belong to the insertion boundary; its shape is retained without assigning punctuation.''')
rep(r'''De plus, le foncteur $u^{*}$ ``\uline{commute}'' à toutes
\tikz[baseline=-0.3ex,scale=.18]{\draw (0,1.3)--(0,.15) .. controls (-.4,-.2) and (.4,-.2) .. (0,.15);}''',r'''\begin{tikzpicture}[baseline=(plus.base)]
\node[inner sep=3pt] (plus) {De plus, le foncteur $u^{*}$ ``\uline{commute}'' à toutes\quad\tikz[baseline=-0.3ex,scale=.18]{\draw (0,1.3)--(0,.15) .. controls (-.4,-.2) and (.4,-.2) .. (0,.15);}};
\draw ([xshift=-2mm,yshift=1mm]plus.west) .. controls ([xshift=-1mm]plus.south west) and ([xshift=2mm]plus.south west) .. (plus.south west) -- ([xshift=-6mm]plus.south east) .. controls ([xshift=-1mm,yshift=-3mm]plus.south east) .. ([xshift=1mm]plus.south east);
\end{tikzpicture}''')
rep(r"qui \inserted{peuvent} s'exprime\deleted{nt}\unsure{r}",r'''qui \begin{tikzpicture}[baseline=(v.base)]
\node[inner sep=0pt] (v) {s'exprime\deleted{nt}\unsure{r}};
\node[anchor=south west,inner sep=0pt] (i) at ([yshift=2mm]v.north west) {\inserted{peuvent}};
\draw ([xshift=-1mm,yshift=-1mm]v.west) .. controls ([xshift=-2mm,yshift=3mm]v.west) and (i.south west) .. ([xshift=1mm,yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=2mm]i.south east) .. ([xshift=2mm,yshift=1mm]i.south east);
\end{tikzpicture}''')
rep(r'''\margin{\handwritten{\figure{\begin{tikzpicture}\node[align=left,text width=1.8cm,inner sep=3pt] (n) {à la ligne après : Quant au...};\draw (n.north west)--(n.north east) .. controls ([xshift=1mm]n.east) .. (n.south east)--(n.south west);\end{tikzpicture}}}}''',r'''% margin note slanted upward to the right
\margin{\handwritten{\begin{tikzpicture}[x=1cm,y=1cm]
\begin{scope}[rotate=12]
\node[anchor=west,inner sep=0pt] at (0,.45) {à la ligne};
\node[anchor=west,inner sep=0pt] at (-.22,0) {après : Quant au...};
\draw (-.12,.8)--(1.65,.8) .. controls (2,.8) and (2.06,.65) .. (2.06,.4)--(2.06,-.3) .. controls (2.06,-.4) .. (1.88,-.42)--(-.35,-.42);
\end{scope}
\end{tikzpicture}}}''')
rep(r'''\handwritten{\tikz[baseline=-.6ex,scale=.18]{\draw (0,1.5)--(.5,1.4)--(.6,0)--(0,-.15);\draw (1.4,1.4)--(.9,1.35)--(.9,-.1)--(1.5,-.15);}}
Quant au''',r'''\begin{tikzpicture}[baseline=(q.base)]
\node[inner sep=2pt] (q) {Quant au};
\handwritten{\draw ([xshift=-7mm]q.north west)--([xshift=-4mm,yshift=-.5mm]q.north west)--([xshift=-3mm]q.south west)--([xshift=-7mm,yshift=-1mm]q.south west);
\draw ([xshift=2mm]q.north east)--([xshift=-2mm]q.north west)--([xshift=-2mm]q.south west)--q.south east;}
\end{tikzpicture}''')
rep(r'''$\mathrm{u}_{\handwritten{*}}$\inserted{$:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$},''',r'''\begin{tikzpicture}[baseline=(d.base)]
\node[inner sep=0pt] (d) {$\mathrm{u}_{\handwritten{*}}$,};
\node[anchor=south west,inner sep=0pt] (i) at ([xshift=2mm,yshift=2mm]d.north west) {\inserted{$:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$}};
\handwritten{\draw ([xshift=-1mm,yshift=-1mm]d.south east) .. controls ([xshift=-3mm,yshift=3mm]d.east) and (i.south west) .. ([yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=2mm]i.south east) .. ([xshift=1mm,yshift=1mm]i.south east);}
\end{tikzpicture}''')
rep(r'''\inserted{par suite} toute''',r'''\begin{tikzpicture}[baseline=(b.base)]
\node[inner sep=0pt] (b) {toute};
\node[anchor=south,inner sep=0pt] (i) at ([yshift=2mm]b.north) {\inserted{par suite}};
\handwritten{\draw ([xshift=-1mm,yshift=-1mm]b.south west) .. controls ([xshift=-2mm,yshift=2mm]b.north west) and (i.south west) .. ([yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=1mm]i.south east) .. ([xshift=1mm,yshift=1mm]i.south east);}
\end{tikzpicture}''')
rep(r'''\inserted{exclusivement} (telles''',r'''\begin{tikzpicture}[baseline=(b.base)]
\node[inner sep=0pt] (b) {(telles};
\node[anchor=south,inner sep=0pt] (i) at ([yshift=2mm]b.north) {\inserted{exclusivement}};
\handwritten{\draw ([xshift=-1mm,yshift=-1mm]b.south west) .. controls ([xshift=-2mm,yshift=2mm]b.north west) and (i.south west) .. ([yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=1mm]i.south east) .. ([xshift=1mm,yshift=1mm]i.south east);}
\end{tikzpicture}''')
rep(r'''c'est d'ailleurs \deleted{\unsure{comme}''',r'''c'est d'ailleurs\begin{tikzpicture}[baseline=(x.base)]
\node[inner sep=0pt] (x) {\texttt{x}};
\node[inner sep=0pt,anchor=south west] at ([xshift=.2ex,yshift=-.2ex]x.north east) {\handwritten{\unsure{\begin{tikzpicture}[x=1ex,y=1ex]\draw (0,0)--(.25,.75);\end{tikzpicture}}}};
\end{tikzpicture}\deleted{\unsure{comme}''')
rep(r'''torseur sous un groupe, et ne''',r'''torseur sous un groupe\unsure{,} et ne''')
rep(r'''\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}un''',r'''\deleted{se donne}\begin{tikzpicture}[baseline=(b.base)]
\node[inner sep=0pt] (b) {un};
\node[anchor=south east,inner sep=0pt] (i) at ([xshift=3mm,yshift=3mm]b.north east) {\inserted{est \inserted{\handwritten{en}} présenced'}};
\handwritten{\draw ([xshift=-1mm,yshift=-1mm]b.south west) .. controls ([xshift=-1mm,yshift=3mm]b.north west) and ([xshift=1mm,yshift=-1mm]i.south west) .. ([yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=2mm]i.south east) .. ([xshift=1mm,yshift=1mm]i.south east);}
\end{tikzpicture}''')
rep(r'''\inserted{\handwritten{toutes}} les propri\deleted{t}é\deleted{é}tés''',r'''\begin{tikzpicture}[baseline=(b.base)]
\node[inner sep=0pt] (b) {les};
\node[anchor=south west,inner sep=0pt] (i) at ([yshift=2mm]b.north west) {\inserted{\handwritten{toutes}}};
\handwritten{\draw ([xshift=-1mm,yshift=-1mm]b.south west) .. controls ([xshift=-2mm,yshift=2mm]b.north west) and (i.south west) .. ([yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=1mm]i.south east) .. ([xshift=1mm,yshift=1mm]i.south east);}
\end{tikzpicture} propri\unsure{\begin{tikzpicture}[baseline=(a.base)]\node[inner sep=0pt] (a) {é};\node[inner sep=0pt] at ([xshift=.3pt,yshift=.2pt]a.center) {t};\end{tikzpicture}}\unsure{\begin{tikzpicture}[baseline=(a.base)]\node[inner sep=0pt] (a) {t};\node[inner sep=0pt] at ([xshift=-.3pt,yshift=.2pt]a.center) {é};\end{tikzpicture}}és
% The two é/t superpositions are preserved without assigning an impression order.''')
rep(r'''\deleted{l'}\inserted{une}intuition''',r'''\begin{tikzpicture}[baseline=(b.base)]
\node[inner sep=0pt] (b) {\deleted{l'}intuition};
\node[anchor=south west,inner sep=0pt] (i) at ([xshift=-1mm,yshift=2mm]b.north west) {\inserted{une}};
\handwritten{\draw ([xshift=-1mm,yshift=-1mm]b.south west) .. controls ([xshift=-2mm,yshift=2mm]b.north west) and (i.south west) .. ([yshift=-1mm]i.south west) -- ([yshift=-1mm]i.south east) .. controls ([xshift=2mm]i.south east) .. ([xshift=2mm,yshift=1mm]i.south east);}
\end{tikzpicture}''')
rep(r'''\draw ([xshift=2mm,yshift=2mm]n.north)--(n.west) .. controls (n.south west) .. (n.south east);''',r'''\draw ([xshift=2mm,yshift=2mm]n.north) .. controls ([xshift=-2mm,yshift=2mm]n.north west) .. (n.west) .. controls (n.south west) .. (n.south east);''')
rep(r'''gauche,\deleted{$\mathrm{g}$}''',r'''gauche,\deleted{$\mathrm{g}$}\begin{tikzpicture}[baseline=(x.base)]\node[inner sep=0pt] (x) {\texttt{x}};\end{tikzpicture}
% Separate typewriter cancellation x in the following cell; not a further live variable.''')
(p/'reading.tex').write_text(s)
print(str(p/'reading.tex'))
print('Characters:',len(s))
