from record_page import record
record(15,r'''\scanpage{15}
\diagram{\begin{array}{ccccccccc}
&&\deleted{\unsure{x}}&&V&&&&\\
\{0\}&\big/&V_1&\big/&V_1+\{x_2\},\ V_2&\big/&V_2+\{x_3\}&\big/&
\begin{array}{l}V_2+x_3\unsure{\ast|\notin}V_1,\ V_{\unsure{1|2}}+x_3\unsure{\in}V_1+\{x_2+x_3\},\\ \hfill V_3\end{array}\\
&&\downarrow&&\hfill\downarrow&&&&\\
&&x_1&&\hfill x_2&&&&
\end{array}}

\deleted{$\unsure{1}\quad a\quad\unsure{1}$}
\[
a_1\ a_2\ a_3\qquad b_1\ b_2\ b_3
\]
\[
\begin{array}{l}
V_1+\{x_2\}\qquad V_2+\{x_3\}\\
\unsure{3}\ V_2+x_3\unsure{\ast|\notin}V_1+\{x_2+x_3\}\\
3\ 3\ 3\ 3\ 1\ 1\ 1
\end{array}
\]
\[
E\unsure{+|\dotplus}a\unsure{\notin|\in}E
\]
\[
(E_{2n}\unsure{\ast}E_2)\ \text{\unsure{dissociés|définis}}\ \text{\unsure{ssi|sss}}\quad
\left[\begin{array}{l}
E_2\text{ ss-gps (\unsure{élémentaire})}\\
E_{2n}\text{ stable par translation de }E_2
\end{array}\right.
\]
\deleted{$n$ pair,}
\[
E_{2n+1},E_2\quad\text{\unsure{donnés}}\qquad
\left\{\begin{array}{l}
E_2\text{ ss-gps}\\
E_{2n+1}=E'_{2n}+\{x\},\ \text{\unsure{où}}\ E'_{2n}\text{ est}\\
\hfill\text{stable p }E_2
\end{array}\right.
\]
\[
E_3\quad E_3\quad\text{\unsure{donné}}\qquad 3\ 2\ 2\ 2
\]
\[
a_1\ a_2\ a_3\quad\unsure{''}\quad b_1\ b_2\ b_3\qquad 3\ \unsure{2|1}\ \unsure{2|7}\ 1\ 1
\]
\[
\cdots
\]
\[
0\ a\ a'\qquad 0\ a\ b'
\]

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west] at (0,0) {$\begin{array}{ccc}0&a&\deleted{b'}\\a&\deleted{2a}&\deleted{a+b'}\\\deleted{a'}&\deleted{a+a'}&a'+b'\end{array}$};
\draw (0.7,-0.05) .. controls (2.0,0.8) and (1.8,-0.4) .. (0.1,-0.95) .. controls (-0.3,-1.1) and (0.3,-0.2) .. (0.7,-0.05);
\node[anchor=north west] at (4.0,0.25) {$\deleted{\unsure{\notin}}$};
\node[anchor=north west] at (3.4,-0.25) {$\deleted{2a\ne a}$};
\node[anchor=north west] at (3.25,-0.95) {$\deleted{\unsure{a'+b'=a'=b'=a}}$};
\node[anchor=north west] at (3.6,-1.45) {$\deleted{\unsure{a'+b'}}$};
\node[anchor=north west] at (1.25,-2.05) {$\deleted{\unsure{a'+b'=-a}}$};
\node[anchor=north west] at (3.6,-2.05) {$\deleted{b'=a}$};
\node[anchor=north west] at (1.3,-2.8) {$a'+b'=a$};
\node[anchor=north west] at (4.6,-2.85) {$\begin{array}{c}0\\a\end{array}$};
\node[anchor=north west] at (6.0,0) {$\begin{array}{ccc@{\qquad}ccc}0&a&a'&0&a&\uline{a-a'}\\0&a&2a&0&a&-a\end{array}$};
\node[anchor=north west] at (8.2,-2.3) {$\underbrace{-2a\quad -a\quad0\quad a}\quad2a$};
\node[anchor=north west] at (9.3,-3.1) {$\deleted{\unsure{2a\ne0}}$};
\node[anchor=north west] at (9.2,-3.55) {$2a\ne0$};
\node[anchor=north west] at (0,-3.7) {$\begin{array}{ccc}0&a&\uline{a-a'}\\a&\uline{2a}&2a-a'\\\uline{a'}&\uline{a+a'}&a\end{array}$};
\draw (0.05,-4.1) -- (1.55,-3.65) .. controls (1.8,-3.55) and (1.9,-4.45) .. (2.2,-4.7) .. controls (4.0,-4.9) and (3.6,-5.9) .. (2.2,-5.45) .. controls (1.8,-5.1) and (1.9,-4.05) .. (1.4,-4.2) -- (0.1,-4.9) -- (0,-4.5);
\node[anchor=north west] at (0.3,-5.9) {$\deleted{\unsure{2a=a}}\qquad\deleted{2a=0}$};
\node[anchor=north west] at (2.9,-6.25) {$\deleted{\unsure{a-a'=0}}$};
\node[anchor=north west] at (0.8,-6.5) {$0\qquad\left|\begin{array}{l}2a=0\\a'=-a\\a'=2a\end{array}\right.$};
\node[anchor=north west] at (4.4,-4.4) {$\deleted{0\quad a\quad -a\qquad0\quad a\quad2a\unsure{+}}$};
\node[anchor=north west] at (4.5,-5.2) {$\begin{array}{ccc}-a&\deleted{0}&\deleted{a}\\-a&0&a\end{array}$};
\node[anchor=north west] at (7.4,-5.0) {$\left[\begin{array}{ccc}-2a&-a&0\\-a&0&a\\0&a&2a\end{array}\right]$};
\draw (7.3,-5.05) -- (10.0,-4.95);
\draw (7.2,-5.45) -- (6.0,-6.7) .. controls (7.0,-8.0) and (8.2,-8.6) .. (10.0,-7.0);
\draw (7.15,-5.55) -- (6.1,-6.65);
\end{tikzpicture}}
% archive foliation: 14
''',[
('diagram','top across page','{0}/V_1/.../V_2+{x_3}/...V_3; downward arrows to x_1,x_2'),
('deletion','above and below first diagram','x; 1 a 1'),
('display','upper left','a_1 a_2 a_3; b_1 b_2 b_3'),
('display','upper right','V_1+{x_2}, V_2+{x_3}; 3 V_2+x_3 ...; 3333111'),
('display','upper middle','E+a∉E'),
('display','middle','(E_{2n} * E_2) ... E_2 ss-gps ...'),
('deletion','middle left','n pair,'),
('display','middle','E_{2n+1},E_2 donnés; E_2 ss-gps; E_{2n+1}=E′_{2n}+{x}'),
('display','middle lower','E_3 E_3 donné; 3222'),
('display','lower half top','a_1 a_2 a_3 ... b_1 b_2 b_3; 32211; ...'),
('display','lower half','0 a a′; 0 a b′'),
('drawing','lower half','tables, enclosing curves, equations, and crossed calculations'),
('diagram','lower left first table','0 a b′ / a 2a a+b′ / a′ a+a′ a′+b′'),
('deletion','lower half left and centre','table entries and adjoining equations'),
('display','lower centre','a′+b′=a; 0 a'),
('diagram','lower right upper','0 a a′ / 0 a 2a; 0 a a−a′ / 0 a −a'),
('display','lower right middle','underbraced −2a −a 0 a; 2a; 2a≠0'),
('deletion','lower right middle','2a≠0'),
('diagram','lower left second table','0 a a−a′ / a 2a 2a−a′ / a′ a+a′ a'),
('deletion','bottom left','2a=a; 2a=0; a−a′=0'),
('display','bottom left','0 | 2a=0; a′=−a; a′=2a'),
('deletion','bottom centre','0 a −a; 0 a 2a+; 0,a'),
('diagram','bottom centre','−a 0 a / −a 0 a'),
('diagram','bottom right','−2a −a 0 / −a 0 a / 0 a 2a')
],'''Dense scratch calculations in additive notation, distinct in appearance from the game definitions. Several tables of pairwise sums and translates V_i, x_i, E_{2n}, E_2 occur, with subgroup and translation-stability conditions. No claim of a connection to the game-theoretic section should be made without context evidence. The arithmetic tables and heavy cancellations are the least secure readings so far; the TikZ reproduces their arrangement and enclosing curves, with explicit doubts for overstruck formulas. All visible isolated numerals and repeated rows have been retained.''')
