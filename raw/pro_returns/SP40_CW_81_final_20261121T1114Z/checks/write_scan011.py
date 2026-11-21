"""Write the root's crop-adjudicated scan011, using only existing conventions."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
c=(R/'readers/011/C/reading.tex').read_text()
a=(R/'readers/011/A/reading.tex').read_text()
b=(R/'readers/011/B/reading.tex').read_text()
# Upper-left X: retain the observed detached serif with the resolved doubled P.
xb=b[b.index(' &\\mathbb P\\left(')+2:b.index('\\right)\\qquad')+len('\\right)')]
c=c.replace('\\mathbb{P}(X)&\\qquad',xb+'&\\qquad',1)
# Independently settled glyphs and separately qualified deletion targets.
c=c.replace(r'{\rlap{$\unsure{M|U}$}\phantom{$\deleted{\unsure{M|U}}$}};',r'{$\unsure{\rlap{$M$}\phantom{\deleted{M}}|M|\rlap{$U$}\phantom{\deleted{U}}|U}$};',1)
c=c.replace(r'{\rlap{$\unsure{H|X}$}\phantom{$\deleted{\unsure{H|X}}$}};',r'{\rlap{$H$}\phantom{$\deleted{H}$}};',1)
c=c.replace(r'{\rlap{$R$}\phantom{$\deleted{R}$}};',r'{$\unsure{\rlap{$R$}\phantom{\deleted{R}}|R}$};',1)
c=c.replace(r'\draw (75,151) .. controls (120,111) and (191,54) .. (277,11);',r'\draw[gray] (75,151) .. controls (120,111) and (191,54) .. (277,11);',1)
c=c.replace(r'\draw (172,190) -- (204,38);',r'''\draw (172,190) -- (204,38);
 \draw (190,60) -- (219,35) (190,45) -- (220,59);''',1)
# Upper drawing: A's shortened heavy shaft, disconnected diagonal, and precise local returns.
start=a.index('\\figure{'); end=a.index('\\end{tikzpicture}}',start)+len('\\end{tikzpicture}}')
upper=a[start:end]
upper=upper.replace('\\end{tikzpicture}}',r'''\draw (211,190) -- (217,192) -- (219,188);
% crop-candidate: scan 11
\end{tikzpicture}}''')
start=c.index('\\figure{'); end=c.index('\\end{tikzpicture}}',start)+len('\\end{tikzpicture}}')
c=c[:start]+upper+c[end:]
# Tiny detached path immediately left of the first lower Hom.
c=c.replace(r'\underline{\operatorname{Hom}}(X,Y)&',r'''\begin{tikzpicture}[baseline=(hom.base),line cap=round]
 \node[inner sep=0] (hom) at (0,0) {$\underline{\operatorname{Hom}}$};
 \node[inner sep=0] at (-.78,.12) {\unsure{\begin{tikzpicture}[x=.015cm,y=-.015cm]
 \draw[gray] (0,0) .. controls (3,3) and (6,5) .. (10,6);
 \draw (10,6) -- (12,6.5);
 \end{tikzpicture}}};
 \end{tikzpicture}(X,Y)&''',1)
# The observed upper trace above the final overwritten Z remains locally qualified.
c=c.replace(r''' \draw (.03,.41) -- (.11,.47) -- (.18,.44) -- (.26,.47) -- (.33,.45);
 \fill (.41,.45) circle (.012);
 \fill[gray] (.46,.44) circle (.009);''',r''' \node[inner sep=0] at (.19,.45) {\unsure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round]
 \draw (-.16,0) -- (-.08,.06) -- (-.01,.03) -- (.07,.06) -- (.14,.04);
 \fill (.22,.04) circle (.012);
 \fill[gray] (.27,.03) circle (.009);
 \end{tikzpicture}}};''',1)
c=c.replace(r'&\subset P(Z\times X\times Y)',r'''&\subset
 \underset{\text{\unsure{\begin{tikzpicture}[x=.014cm,y=-.014cm,baseline=0,line cap=round,line join=round]
 \draw (-13,0) -- (-8,1);
 \draw (-2,2) -- (0,-2) -- (3,1) -- (5,-1) -- (6,2);
 \draw (10,-1) -- (11,3);
 \end{tikzpicture}}}}{P}
 (\underset{\text{\unsure{\begin{tikzpicture}[x=.014cm,y=-.014cm,baseline=0,line cap=round]
 \fill (-8,0) circle (1.2);
 \fill[gray] (1,1) circle (1.4);
 \draw[gray] (6,2) -- (8,-1) (12,1) -- (13,-1) (15,0) -- (17,-2);
 \end{tikzpicture}}}}{Z}\times X\times Y)''',1)
# Genuine tikz-cd matrix; local TikZ nodes retain overwritten placement and detached paths.
diagram=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=small,column sep=small,
 execute at end picture={
  % Retraced lower horizontal arrow shaft and extended upper head stroke.
  \draw[line width=.45pt] ([xshift=-4pt,yshift=-1pt]sxiU.west)
    .. controls ([xshift=-18pt,yshift=-5pt]sxiU.west) and ([xshift=15pt,yshift=-5pt]sxiV.east)
    .. ([xshift=4pt,yshift=-1pt]sxiV.east);
  \draw ([xshift=8pt,yshift=5pt]sxiV.east) -- ([xshift=11pt,yshift=9pt]sxiV.east);
  % Loop at the downward arrowhead, plus its two detached marks.
  \draw ([xshift=-5pt,yshift=9pt]sxiPX.north)
    .. controls ([xshift=-9pt,yshift=14pt]sxiPX.north) and ([xshift=-10pt,yshift=8pt]sxiPX.north)
    .. ([xshift=-4pt,yshift=6pt]sxiPX.north);
  \node[inner sep=0] at ([xshift=-12pt,yshift=14pt]sxiPX.north) {$\unsure{\cdot}$};
  \node[inner sep=0] at ([xshift=14pt,yshift=5pt]sxiPX.north) {$\unsure{\textcolor{gray}{\cdot}}$};
 }]
 \& {\begin{tikzpicture}[baseline=(h.base),line cap=round,line join=round]
 \node[inner sep=0] (h) at (0,0) {\rlap{$H$}\phantom{$\deleted{H}$}};
 \draw[gray] (-.28,-.18) -- (.31,.29);
 \draw (-.26,-.17) -- (.18,.03);
 \draw (-.13,-.22) .. controls (-.08,-.30) and (.09,-.14) .. (.19,-.08);
 \draw (.19,-.08) -- (.25,-.57);
 \draw (-.18,-.43) .. controls (-.08,-.16) and (.11,-.21) .. (.19,-.51);
 \end{tikzpicture}} \& \& \\
 \& {\begin{tikzpicture}[baseline=(prod.base),line cap=round,line join=round]
 \node[inner sep=0] at (-.12,0) {\rlap{$\unsure{H|R}$}\phantom{$\deleted{\unsure{H|R}}$}};
 \node[inner sep=0] (prod) at (.04,0) {$P$};
 \draw (-.27,.18) -- (-.10,-.17) (-.28,-.08) -- (.03,.05);
 \node[inner sep=0] at (.45,0) {\rlap{$e$}\phantom{$\deleted{e}$}};
 \node[inner sep=0] at (.45,-.02) {$\times$};
 \node[anchor=base west,inner sep=0] at (.69,-.04) {$X\times Y$};
 \end{tikzpicture}}
 \arrow[d,"{\begin{tikzpicture}[baseline=(u.base),line cap=round,line join=round]
 \node[inner sep=0] (u) at (0,0)
 {\rlap{$\unsure{H|U}$}\phantom{$\deleted{\unsure{H|U}}$}};
 \draw (-.21,-.21) -- (.24,.36);
 \draw (.05,-.13) .. controls (-.03,-.45) and (.13,-.54) .. (.33,-.31);
 \end{tikzpicture}}"'] \& \&
 {\supset\begin{tikzpicture}[baseline=(g.base),line cap=round,line join=round]
 \node[inner sep=0] at (.09,-.04) {\rlap{$H$}\phantom{$\deleted{H}$}};
 \node[inner sep=0] (g) at (0,.03) {$\Gamma$};
 \draw[line width=1.1pt] (-.13,-.22) -- (-.12,.28) -- (.40,.34);
 \end{tikzpicture}}\arrow[dll] \\
 \& |[alias=sxiPX]| P\times X\arrow[dl] \& \& U\times_{\unsure{Y|V}}U\\
 {\begin{tikzpicture}[baseline=(p.base),line cap=round]
 \node[inner sep=0] (p) at (.29,-.25) {$P$};
 \node[inner sep=0] at (-1.03,.91) {$\unsure{\cdot}$};
 \draw[gray] (-1.11,.94) .. controls (-1.10,.92) and (-1.08,.91) .. (-1.07,.90);
 \draw (-.08,1.0) .. controls (-.06,.35) and (-.12,-.55) .. (-.09,-1.04);
 \draw (-.06,.48) .. controls (-.03,-.10) and (.02,-.67) .. (.08,-.92);
 \node[inner sep=0] at (.21,.03) {\unsure{\begin{tikzpicture}[x=.015cm,y=-.015cm,line cap=round]
 \draw[gray] (0,0) .. controls (3,-3) and (4,0) .. (3,3) -- (4,8);
 \end{tikzpicture}}};
 \end{tikzpicture}}
 \& |[alias=sxiV]| \unsure{V|W} \& \& |[alias=sxiU]| U\arrow[ll]\\
 \& \& {\begin{tikzpicture}[x=.011cm,y=-.011cm,baseline=(p.base),line cap=round]
 \node[inner sep=0,anchor=base] (p) at (0,0) {$P$};
 \draw (-42,-102) .. controls (-30,-94) and (-30,-78) .. (-22,-66);
 \draw[gray] (60,-113) -- (30,-59);
 \fill (30,-59) circle (1.2);
 \node[inner sep=0] at (2,21) {\unsure{\begin{tikzpicture}[x=.011cm,y=-.011cm,line cap=round]
 \draw[line width=.7pt] (-1,-13) .. controls (0,-4) and (1,5) .. (3,13);
 \fill (3,13) circle (1.2);
 \end{tikzpicture}}};
 \end{tikzpicture}} \&
\end{tikzcd}}
'''
start=c.index('\\diagram{');end=c.index('\\figure{',start)
c=c[:start]+diagram+c[end:]
# Lower sketches: preserve all checked C paths, adding the root-observed small details.
c=c.replace(r'\draw (13,425) -- (98,46) -- (215,4) -- (282,69) -- (267,303) -- (145,352) -- cycle;',r'''\draw (13,425) -- (98,53);
\draw (98,46) -- (130,35) (139,32) -- (155,26) (164,23) -- (215,4);
\draw (215,4) -- (282,69);
\draw (282,76) -- (267,303) -- (145,352) -- (13,425);
\draw (215,4) -- (210,-3) (219,5) -- (218,-4);
\draw (13,425) -- (6,414) (267,303) -- (270,313);''',1)
old=r'\draw (627,259) -- (745,421);'
new=r'''\draw (416,389) .. controls (421,396) and (430,396) .. (438,389);
\draw (562,388) -- (574,391) (564,398) -- (578,402);
\node[inner sep=0] at (523,276) {\unsure{\begin{tikzpicture}[x=.011cm,y=-.011cm,line cap=round]
\fill (0,0) circle (1.2); \draw[gray] (1,1) -- (3,2);
\end{tikzpicture}}};
\draw (627,259) -- (745,421);'''
assert old in c;c=c.replace(old,new,1)
# The questioned relation and all manuscript delimiter omissions remain unchanged.
assert c.count('\\scanpage{11}')==1 and '\\cotefile' not in c
(R/'pages/J81-02_81_scan011.tex').write_text(c)
print('wrote',R/'pages/J81-02_81_scan011.tex')
