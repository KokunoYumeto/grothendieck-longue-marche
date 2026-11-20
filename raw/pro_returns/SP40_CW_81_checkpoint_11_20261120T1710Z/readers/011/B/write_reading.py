from pathlib import Path
p=Path(__file__).parent
c=Path('/workspace/scratch/94548b74fbe0/packets/011/C.tex').read_text()
first=c[c.index(r'\figure{'):c.index(r'\[',c.index(r'\figure{'))]
last=c[c.rindex(r'\figure{'):c.index('% archive sheet number:')]
# Every original path was checked against the supplied halves. Preserve the observed arrowhead at the upper junction.
first=first.replace(r'\end{tikzpicture}}',r'''\draw (88,164) -- (98,158) (88,164) -- (100,166);
\end{tikzpicture}}''')
head=r'''\scanpage{11}
\[
 \unsure{=|\Rightarrow}
\]
\[
 \begin{aligned}
 &\mathbb P\left(
 \begin{tikzpicture}[x=.0043cm,y=-.0043cm,baseline={(0,82)},line cap=round,line join=round]
 \draw[line width=.5pt] (18,12) -- (59,76) (64,1) -- (23,78);
 \draw[line width=.5pt] (0,1) -- (30,3) (63,0) -- (76,1)
 (0,80) -- (26,78) (58,76) -- (78,77);
 \end{tikzpicture}\right)\qquad
 P(X\times\unsure{Z|2})\overset{?}{\simeq}
 \operatorname{Hom}(\deleted{\unsure{\mathcal E|e}}Z\times X,\mathscr E)\\
 &\hspace{6em}\mathrel{/\!/}\ 
 \overset{\unsure{\deleted{M}|M|\deleted{U}|U}\quad\deleted{H}\quad\unsure{\deleted{R}|R}}
 {\begin{tikzpicture}[baseline=(old.base),line cap=round,line join=round]
 \node[inner sep=0pt] (old) at (0,0) {$\rlap{\operatorname{Hom}(X)}\phantom{\deleted{\operatorname{Hom}(X)}}$};
 \draw (-.9,.02) -- (.9,.12);
 \draw (-.8,-.38) -- (-.14,.65);
 \draw (.04,-.45) -- (.34,.48);
 \draw (-.65,-.32) -- (.99,.63);
 \end{tikzpicture}}
 \\[-.2em]
 &\hspace{9em}\unsure{\operatorname{Hom}}(X,\underline{\operatorname{Hom}}(\mathscr E,Z)\\
 \unsure{O|0}\subset\mathbb P(X)&\qquad
 \operatorname{Hom}(\mathscr E,\underline{\operatorname{Hom}}(X,Z))\\
 &\qquad\mathrel{/\!/}\\
 &\qquad P(\operatorname{Hom}(X,Z)
 \end{aligned}
\]
% The upper-left X is drawn to retain its detached upper-left serif.
% Raised M/U and R have uncertain cancellation status; no writing chronology is supplied.
'''
bottom=r'''\[
 \begin{aligned}
 \underline{\operatorname{Hom}}(X,Y)&\subset P(X\times Y)\\
 \operatorname{Hom}\left(
 \overset{\unsure{\begin{tikzpicture}[x=.013cm,y=-.013cm,baseline=0,line cap=round,line join=round]
 \draw (0,4) -- (4,1) -- (7,4) -- (12,1) -- (18,3);
 \fill (22,3) circle (1.1); \fill[gray] (28,3) circle (.8);
 \end{tikzpicture}}}{\deleted{\unsure{t|1}}Z}
 \times X,Y\right)&\subset P(Z\times X\times Y)
 \end{aligned}
\]
% Detached wavy trace and spots above the overwritten Z: shape retained, role and hand undetermined.
\diagram{\begin{tikzpicture}[x=.011cm,y=-.011cm,line cap=round,line join=round]
% The diagram is positioned from the observed page, including its short unattached lower strokes.
\node[anchor=base] at (200,59) {$\rlap{H}\phantom{\deleted{H}}$};
\draw (170,70) -- (252,10);
\draw (187,50) .. controls (184,78) and (194,82) .. (226,63);
\node[anchor=base] at (188,111) {$\frown$};
\node[anchor=base west] at (57,154) {$\deleted{\unsure{H|R}}P\deleted{\unsure{e}}\times X\times Y$};
\node[anchor=base west] at (291,169) {$\supset\deleted{H}\Gamma$};
\node[anchor=base] at (124,266) {$\rlap{\unsure{H|U}}\phantom{\deleted{\unsure{H|U}}}$};
\draw (108,270) -- (152,195);
\draw (192,198) -- (187,264);
\draw (171,244) -- (187,264) -- (204,240);
\fill (165,246) circle (1.5);
\fill[gray] (218,266) circle (1.0);
\draw (329,193) -- (248,281);
\draw (257,257) -- (248,281) -- (273,273);
\node[anchor=base west] at (132,344) {$P\times X$};
\node[anchor=base west] at (321,343) {$U\times_{\unsure{V|Y}}U$};
\draw[line width=1.5pt] (170,365) -- (80,450);
\draw[line width=1.1pt] (86,419) -- (80,450) -- (106,451);
\draw (18,363) -- (17,562);
\draw (25,499) -- (31,555);
\node[anchor=base west] at (35,538) {$P$};
\node[anchor=base] at (207,468) {$\unsure{V|W}$};
\node[anchor=base] at (326,466) {$U$};
\draw[line width=1.5pt] (300,445) -- (222,450);
\draw[line width=1pt] (243,430) -- (222,450) -- (247,464);
\draw (238,426) -- (222,450);
\draw (199,500) .. controls (209,505) and (211,525) .. (218,534);
\draw[gray] (299,486) -- (271,535);
\draw (274,530) -- (271,535);
\node[anchor=base] at (242,618) {$P$};
\end{tikzpicture}}
'''
s=head+first+bottom+last+'% archive sheet number: 10\n'
s=s.replace(r'\rlap{\operatorname{Hom}(X)}',r'\rlap{$\operatorname{Hom}(X)$}').replace(r'\rlap{H}',r'\rlap{$H$}').replace(r'\rlap{\unsure{H|U}}',r'\rlap{$\unsure{H|U}$}')
s=s.replace(r'\figure{\begin{tikzpicture}', '% crop-candidate: scan 11\n'+r'\figure{\begin{tikzpicture}')
(p/'reading.tex').write_text(s)
print('reading.tex written',len((p/'reading.tex').read_text()),'characters')
