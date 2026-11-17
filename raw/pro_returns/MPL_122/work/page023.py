from record import save
save(23,r'''\scanpage{23}
\mspage{22}
\figure{\begin{tikzpicture}[scale=.85,line width=.45pt]
\draw (.9,8.1)--(5.6,8.35)--(4.7,6.05)--(0,5.85)--cycle;
\draw (.8,5.15)--(5.15,5.5)--(4.55,3.48)--(.05,3.28)--cycle;
\draw (.7,2.75)--(5.45,3.12)--(4.35,.72)--(-.08,.48)--cycle;
\foreach \d in {-.65,-.32,0,.32,.65}{
\draw[dashed] (1.4,7.35)..controls ({1.4+\d},5.7) and ({1.2+\d},2.5)..(1.05,1.27);
\draw[dashed] (4.03,7.48)..controls ({4.03+\d},5.8) and ({3.9+\d},2.6)..(3.76,1.5);
\begin{scope}\clip (-1,3.28) rectangle (6,5.9);
\draw (1.4,7.35)..controls ({1.4+\d},5.7) and ({1.2+\d},2.5)..(1.05,1.27);
\draw (4.03,7.48)..controls ({4.03+\d},5.8) and ({3.9+\d},2.6)..(3.76,1.5);
\end{scope}
\begin{scope}\clip (-1,.4) rectangle (6,3.3);
\draw (1.4,7.35)..controls ({1.4+\d},5.7) and ({1.2+\d},2.5)..(1.05,1.27);
\draw (4.03,7.48)..controls ({4.03+\d},5.8) and ({3.9+\d},2.6)..(3.76,1.5);
\end{scope}
}
\draw[dashed] (2.45,7.5)..controls (2.5,5) and (2.2,3)..(2.12,1.43);
\draw[dashed] (3.2,7.55)..controls (3.2,5) and (3,3)..(2.92,1.52);
\begin{scope}\clip (0,4.1) rectangle (5,5.9);
\draw (2.45,7.5)..controls (2.5,5) and (2.2,3)..(2.12,1.43);
\draw (3.2,7.55)..controls (3.2,5) and (3,3)..(2.92,1.52);
\end{scope}
\begin{scope}\clip (0,1) rectangle (5,3.3);
\draw (2.45,7.5)..controls (2.5,5) and (2.2,3)..(2.12,1.43);
\draw (3.2,7.55)..controls (3.2,5) and (3,3)..(2.92,1.52);
\end{scope}
\draw[dashed,line width=.8pt] (.52,3.55)--(1.97,4.95);
\draw[dashed,line width=.8pt] (3.42,3.55)--(4.95,5.06);
\foreach \p in {(1.4,7.35),(4.03,7.48),(2.45,7.5),(3.2,7.55),(2.37,4.16),(3.12,4.2),(1.05,1.27),(2.12,1.43),(2.92,1.52),(3.76,1.5)}{\draw \p circle (.035);}
\node[above] at (1.4,7.35) {$\ell_{11}$};\node[above] at (4.03,7.48) {$\ell_{12}$};
\node[below] at (1.05,1.27) {$\ell_{21}$};\node[below] at (3.76,1.5) {$\ell_{22}$};
\node at (6.3,7.45) {$\overline V_1$};\node at (6.3,4.65) {$\overline V_{12}$};\node at (6.3,2.05) {$\overline V_2$};
\node at (2.7,-.2) {$\overline V_4$};
\node at (-.9,2.35) {$E_1$};\draw[->] (-.55,2.4)..controls (.75,2.65) and (-.2,2.8)..(1.18,2.95);
\node at (6.3,6.2) {$E_2$};\draw[->] (5.9,6.2)..controls (4.3,6.05) and (5.8,5.75)..(4.22,5.55);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[scale=.9,line width=.45pt]
\draw (.5,7.8)..controls (2.1,7.65) and (4.4,8)..(5.6,8.2)--(4.55,5.82)..controls (2.6,5.7) and (.65,5.57)..(-.6,5.7)--cycle;
\draw (.45,2.05)..controls (2.5,1.9) and (3.8,2.1)..(4.65,2.4)--(3.68,.05)..controls (2.1,-.2) and (.1,-.2)..(-.7,0)--cycle;
\draw (.57,7.15)..controls (.8,7.04) and (.87,6.85)..(.92,6.8);
\draw[dashed] (.92,6.8)..controls (.95,6.25) and (.72,5.96)..(.5,5.73);
\draw (.45,5.65)..controls (.2,5.2) and (-.25,5.05)..(-.75,4.98)..controls (-1.05,4.95) and (-1.35,4.98)..(-1.5,5.02);
\draw (4.5,7.45)--(4.15,7.02);
\draw[dashed] (4.15,6.92)..controls (3.9,6.3) and (4.25,5.92)..(4.5,5.88);
\draw (4.6,5.85)..controls (4.85,5.63) and (5.08,5.5)..(5.33,5.45)..controls (5.6,5.3) and (5.9,5.38)..(6.18,5.45);
\foreach \d in {-.55,-.3,0,.3,.55}{
\draw (-.75,4.98)..controls ({-.75+\d},4.2) and ({-.64+\d},2.6)..(-.58,2.05);
\draw (5.33,5.45)..controls ({5.33+\d},4.75) and ({5.33+\d},3.2)..(5.33,2.94);
}
\draw (-1.5,1.92)..controls (-.8,2.3) and (.55,2.03)..(.75,.98);
\draw[dashed] (.75,.98)..controls (.75,.7) and (.58,.5)..(.55,.3);
\draw (5.65,2.9)..controls (4.6,3.28) and (3.15,1.98)..(3.68,1.08);
\draw[dashed] (3.68,1.08)..controls (3.8,.75) and (4.05,.6)..(4.2,.58);
\draw (4.2,.58)..controls (4.35,.5) and (4.55,.48)..(4.8,.46);
\draw (2.15,7.5)--(2.18,6.92);\draw[dashed] (2.18,6.82)--(2.08,5.72);
\draw (2.08,5.72)..controls (2.1,3.9) and (1.8,2.1)..(1.82,1.02);\draw[dashed] (1.82,.88)--(1.84,.12);
\draw (3.05,7.6)--(3.08,7.02);\draw[dashed] (3.08,6.93)--(3.04,5.77);
\draw (3.04,5.77)--(2.95,1.08);\draw[dashed] (2.95,.96)--(3.02,.2);
\foreach \p in {(.92,6.8),(2.18,6.87),(3.08,6.97),(4.15,6.97),(.75,.98),(1.82,.96),(2.95,1.05),(3.68,1.08)}{\draw \p circle (.035);}
\foreach \x/\y in {-.75/4.98,-.58/2.05,5.33/5.45,5.33/2.94}{\foreach \ang in {25,60,95,125,160,220,265,300}{\draw (\x,\y)--++(\ang:.2);}}
\node at (.28,5.12) {$R_{11}$};\node at (4.65,5.45) {$R_{12}$};\node at (.08,2.2) {$R_{21}$};\node at (4.2,2.68) {$R_{22}$};
\node at (.05,3.68) {$E_1$};\node at (4.64,4.26) {$E_2$};\node at (1.96,-.75) {$\overline V_5$};
\end{tikzpicture}}

\uline{Figure 8}
''',[
('margin note','top right','22'),
('drawing','upper half','three planes Vbar1,Vbar12,Vbar2; ell11,ell12,ell21,ell22; E1,E2; Vbar4'),
('drawing','lower half','two planes; R11,R12,R21,R22; E1,E2; Vbar5'),
('text','bottom centre','Figure 8')
],[],['Companion Figure 8 to the reused quotient-construction sheets: Vbar4,Vbar5 and exceptional curves E1,E2.'],sheet_kind='reused_typed')
