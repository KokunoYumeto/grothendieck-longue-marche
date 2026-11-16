from page_work import save_page
text=r'''\scanpage{95}
Il faudrait aussi, de façon générale (dans le contexte ``quasi'') étudier
\deleted{\unsure{le}} si $H^i(k,G)$ peut se calculer comme une cohomologie
galoisienne\ldots
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)--(-.03,.7); \draw (.045,0)--(.01,.71); \draw (.085,.015)--(.05,.68);
\end{tikzpicture}}}

\deleted{N.B. Il n'y \unsure{a pas} \illegible{3} \unsure{élémentaire} de
Weil \unsure{permette}.}
\mspage{94}
'''
save_page(95,text,[('text','top three lines','Il faudrait aussi de façon générale'),('deletion','top second line after étudier','le'),('margin note','left of top paragraph','three vertical emphasis strokes'),('drawing','left of top paragraph','three vertical strokes'),('deletion','upper quarter two lines','N.B. Il n’y a pas'),('text','bottom left page number','94')],observations='The faint mirrored text across the lower sheet is show-through from its reverse, checked against the orientation of the preceding page, rather than a second live writing layer on this side. Cancelled N.B. inspected in enlarged crop; three words obscured by the heavy deletion remain unreadable.')
