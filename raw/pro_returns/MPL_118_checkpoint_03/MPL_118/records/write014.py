from save_page import save
text=r'''\scanpage{14}
\diagram{\begin{array}{l|l}
f^\sharp\in\text{fibration}\cap\text{mono}&\unsure{f^b|f^\flat}\in\text{fibration (not \uuline{yet Serre})}\\\hline
\sigma_f\in\text{cofibration}\cap\text{mono}\cap\mathrm{tr}&\rho_f\in\text{cofibration}\cap\mathrm{Serre}\cap\mathrm{tr}\\\hline
\lambda_f\unsure{\notin}\;\big|\;\begin{gathered}\text{not a fibration or cofibration}\\\text{nor Serre, but trivial}\\\text{fibers (with final}\\\text{object}\end{gathered}&
\unsure{\eta_f|H_f}\unsure{\notin}\;\big|\;\begin{gathered}\text{not a fibration nor cofibration}\\\text{nor Serre ?}\end{gathered}
\end{array}}

\margin{NB $\text{proper discret}\Rightarrow\text{cofib}$

$\text{smooth discret}\Rightarrow\text{fibration}$

$\left[\begin{gathered}\text{but proper Serre}\not\Rightarrow\text{cofib}\\\text{smooth Serre}\not\Rightarrow\text{fib}\end{gathered}\right]$}

\diagram{\begin{tikzcd}
(Y\longrightarrow X) \arrow[r] & X & & Y\\
 & Y_x \arrow[r] & \deleted{\unsure{X|x}}\\
0 \arrow[r] & 1
\end{tikzcd}}

$(\lambda_f,\sigma_f)$ adjoint ?

$(\unsure{\eta_f|H_f},\rho_f)$ adjoint

\diagram{\begin{tikzcd}[execute at end picture={\draw (current bounding box.center) ellipse [x radius=3.7cm,y radius=1.15cm];}]
X\arrow[r]&\text{Cofiber of }f^\sharp\;?\\
Y\arrow[r]&\text{Cofiber of }\sigma_f\;?
\end{tikzcd}}

\figure{\begin{tikzpicture}[x=.9cm,y=.9cm]
\draw[line width=1.3pt] (-.35,0)--(.35,0) (0,-.35)--(0,.35);
\node at (0,.7) {Serre};
\node at (0,1.8) {bifibration};
\draw[->] (0,1)--(0,1.5);
\node at (-2.35,0) {smooth $\unsure{\subset}$ fibration};
\node at (2.3,0) {proper $\supset$ co- \unsure{proper}};
\draw (-5.5,0)--(-4,0) (4.1,0)--(5.5,0);
\node at (0,-.9) {discrete};
\node[gray] at (0,-1.5) {\unsure{mono}};
\draw[->] (0,-1.1)--(0,-1.65);
\node at (0,-2) {mono};
\node[anchor=east,align=left] at (-.5,-1) {$\left.\begin{gathered}\text{discrete fibration}\\\widehat X\text{ i.e. }X^\circ\longrightarrow(\mathrm{Sets})\end{gathered}\right\}$};
\node[anchor=west,align=left] at (.5,-1) {$\left\{\begin{gathered}\text{discrete cofibration}\\\check X\text{ i.e. }X\longrightarrow(\mathrm{Sets})\end{gathered}\right.$};
\node[anchor=east,align=left] at (-.5,-3.1) {$\left.\begin{gathered}
X^\circ\longrightarrow\left[\overset{\substack{0\\\Vert}}{\varnothing},\overset{\substack{1\\\Vert}}{\{\varnothing\}}\right]=\Delta_1\\
Y=\varphi^{-1}(\{1\})=\psi^{-1}(\{0\})\\
(\psi:X\xrightarrow{\varphi^\circ}\Delta_1^\circ\simeq\Delta_1\\
\text{open immersion}
\end{gathered}\right\}$};
\node[anchor=west,align=left] at (.5,-3) {$\left\{\begin{gathered}
X\xrightarrow{\varphi'}[\varnothing,\{\varnothing\}]=\unsure{\Delta^1_1|\Delta_1}:\;[0\longrightarrow1]\\
Y=\varphi'^{-1}(\{1\})\\
\text{closed immersion}
\end{gathered}\right.$};
\end{tikzpicture}}
% archive foliation: 13
'''
e=[('diagram','top two columns','f sharp; sigma_f; lambda_f / f b; rho_f; eta_f properties'),('margin note','top right','NB proper discret; smooth discret; but proper Serre not imply cofib'),('diagram','upper middle','(Y→X)→X; lone Y; Y_x→deleted x; 0→1'),('deletion','upper middle target of Y_x','X or x'),('text','middle left','(lambda_f,sigma_f) adjoint ?; (eta_f,rho_f) adjoint'),('diagram','middle oval','X→Cofiber of f sharp ?; Y→Cofiber of sigma_f ?'),('drawing','lower half','Serre to bifibration; smooth/fibration/proper/co-; discrete to mono'),('display','lower scheme left first brace','discrete fibration; X hat; X opposite→Sets'),('display','lower scheme right first brace','discrete cofibration; X check; X→Sets'),('display','lower scheme left bottom brace','X opposite→[empty,{empty}]=Delta1; Y; psi; open immersion'),('display','lower scheme right bottom brace','X→[empty,{empty}]; Y; closed immersion')]
save(14,text,'text',e,'The open-immersion factorization is here written f sharp in fibration intersection mono; retained literally. Questions about adjunction, Serre property of eta, and the two cofibers are explicit. The lower right horizontal label stops at “co-” followed by faint “proper”; not expanded to cofibration. In the lower left formula the parenthesis before psi has no clearly visible closing mate. Pale earlier lettering is retained in place where readable; it is not automatically declared cancelled without a visible strike.')
