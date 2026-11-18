from save_page import save
text=r'''\scanpage{12}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
Y & \mathrm{Fl}(Y) \arrow[l] \arrow[d] & \mathrm{Fib}(f) \arrow[l] \arrow[ll,bend right=30,"\unsure{f^b|f^\flat}"'] \arrow[d,"\rho_f"]\\
 & \unsure{Y|Y'} \arrow[u,dashed,bend right=30] & X \arrow[l,"f"'] \arrow[u,dashed,bend right=45,"\unsure{\eta_f|H_f}"']
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=large]
Y & \mathrm{Fib}(f) \arrow[l,"\unsure{f^b|f^\flat}","\text{fibration}"'] \arrow[r,bend right=30,"\rho_f"'] & X \arrow[l,"\unsure{\eta_f|H_f}\ \text{mono}"']
\end{tikzcd}}

(fibers ${}_{b}\backslash X$ discretely cofibered over $X$)

\uline{but not yet Serre}

trivial Serre \unsure{cofibering} retraction

(fibers $Y_{/b}$ discr. fibred over $Y$)

and homotopism

\figure{\begin{tikzpicture}[x=.8cm,y=.8cm]
\draw[rounded corners=12pt] (-.7,3.1)--(.7,3.1)--(.7,.5)--(4.6,.5)--(4.6,-.5)--(.7,-.5)--(.7,-2.7)--(-.7,-2.7)--(-.7,-.5)--(-4.6,-.5)--(-4.6,.5)--(-.7,.5)--cycle;
\draw[line width=1.6pt] (-.45,0)--(.45,0) (0,-.45)--(0,.45);
\node at (0,2.65) {Serre};
\node[align=center] at (0,1.05) {$[\mathrm{Serre}\cap W$\\$=\text{triv.Serre}]$};
\draw[->] (0,1.5)--(0,2.35);
\node at (-2.65,0) {smooth $\longleftrightarrow$ \uline{fibration}};
\node at (2.65,0) {\uline{cofibration} $\longleftrightarrow$ proper};
\node[align=center] at (0,-1) {mono\\\deleted{\unsure{fibered} \unsure{discrete}}};
\draw[->] (0,-1.45)--(0,-2.05);
\node at (0,-2.35) {discrete};
\draw (-4.6,1.7)--(-1,1.7) (-3.1,.7)--(-3.1,2.8);
\node at (-4,2.35) {Smooth Serre};
\node at (-1.95,2.35) {Serre fibration};
\node at (-4,1.05) {trivial smooth};
\node at (-1.95,1.05) {trivial Serre fibration};
\draw (1,1.7)--(4.9,1.7) (2.9,.7)--(2.9,2.8);
\node at (1.8,2.35) {Serre cofibration};
\node at (4,2.35) {Serre proper};
\node at (1.8,1.05) {trivial cofibration};
\node at (4,1.05) {trivial proper};
\node[anchor=east,align=right] at (-.85,-1.2) {$\left.\begin{gathered}
\text{open immersions}\longleftrightarrow X^\circ\xrightarrow{\varphi}\Delta^1=[0\longrightarrow1]\\
\longleftrightarrow\unsure{\mathrm{crib}}(X)\\
Y=\varphi^{-1}(\{1\})=\psi^{-1}(\{0\})=X_0
\end{gathered}\right\}$};
\node[anchor=east] at (-.85,-2.5) {$\left.\text{discrete fibrations}\longleftrightarrow\widehat X,\text{i.e. }X^\circ\longrightarrow(\mathrm{Sets})\right\}$};
\node[anchor=west,align=left] at (.85,-1.2) {$\left\{\begin{gathered}
\text{Closed immersions}\longleftrightarrow X\xrightarrow{\varphi}\Delta^1=\left[\overset{\substack{0\\\Vert}}{\varnothing}\to\overset{\substack{1\\\Vert}}{\{\varnothing\}}\right]\\
=\hspace{3cm}\Longleftrightarrow\mathrm{Cocrib}(X)\\
Y=\varphi^{-1}(\{1\})=X_1
\end{gathered}\right.$};
\node[anchor=west] at (.85,-2.5) {$\left\{\text{discrete cofibration}\Longleftrightarrow\check X,\text{i.e. }X\longrightarrow(\mathrm{Sets})\right.$};
\end{tikzpicture}}

\margin{(où $\psi:X\xrightarrow{\varphi^\circ}\Delta_1^\circ\xrightarrow[\sim]{\mathrm{can.}}\Delta_1$)}

\diagram{\begin{tikzcd}[column sep=large]
Y \arrow[r,hook,"f^\sharp","\text{open imm}"'] & C(f) \arrow[r,"\lambda_f\ \text{epi}"] & X \arrow[l,bend left=35,"\sigma_f","\substack{\text{closed section}\\\text{and \uline{homotopism}}}"']
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=large]
Y \arrow[r,hook,"f^{\sharp\prime}","\text{closed imm.}"'] & C'(f) \arrow[r,"\lambda'_f"] & X \arrow[l,bend left=35,"\sigma'_f","\substack{\text{open section}\\\text{\uline{and homotopism}}}"']
\end{tikzcd}}

\margin{$\text{discret}\cap\mathrm{Serre}\;(=\text{étale covering})\subset\text{smooth}\cap\text{proper}\unsure{\subset}\mathrm{Serre}$

\deleted{$\text{mono}\cap\mathrm{Serre}$} $=$ \deleted{open} closed imm $=$ direct summand

$\unsure{\text{discret}}\cap\unsure{\text{triv.Serre}|\text{strictSerre}}=\mathrm{iso}$

\uline{NB} $\text{proper}\cap\text{discret}\Rightarrow\text{cofib}$, $\text{smooth}\cap\text{discret}\Rightarrow\text{fibration}$

but does not imply mono, and $\text{proper}\cap\text{free}$ does not imply cofibration \inserted{nor trivial}, $\text{smooth}\cap\text{free}$ not imply fibration \inserted{nor trivial}}
% archive foliation: 11
'''
e=[('diagram','top left','Y ← Fl(Y) ← Fib(f); X to Y; return dashed arrows'),('diagram','upper left centre','Y ← Fib(f) ← X; retraction'),('text','below upper fibration','fibers b\\X discretely cofibered; but not yet Serre'),('text','below upper retraction','trivial Serre cofibering retraction; and homotopism'),('drawing','centre','Cross of smooth, fibration, cofibration, proper; Serre/trivial grid; mono/discrete'),('deletion','inside bottom arm','fibered discrete'),('display','within cross upper arm','Serre intersection W = triv.Serre'),('display','left of bottom arm','open immersions; crib(X); Y=phi inverse(1)=psi inverse(0)=X0'),('margin note','left edge below open immersion','où psi:X→Delta1 opposite→Delta1'),('display','lower left of cross','discrete fibrations ↔ X hat'),('display','right of bottom arm','Closed immersions; Cocrib(X); Y=phi inverse(1)=X1'),('display','lower right of cross','discrete cofibration ↔ X check'),('diagram','lower left','Y ↪ C(f) → X; closed section and homotopism'),('diagram','lower right','Y ↪ C prime(f) → X; open section and homotopism'),('margin note','bottom right','discret intersection Serre; étale covering; NB proper intersection discret'),('deletion','bottom right second line','mono intersection Serre'),('deletion','bottom right second line','open'),('insertion','bottom right last lines','nor trivial (twice)')]
save(12,text,'text',e,'The crossing-out in the central lower arm is dense: “fibered discrete” is a low-confidence attempted reading. Bottom margin corrects an earlier mono/Serre relation and crosses out “open”; the unstruck closed-immersion/direct-summand portion is preserved. The third margin line is heavily retraced and its Serre qualifier uncertain. The lower factorization superscripts visibly differ from the rounded b in the upper diagram and are sharp signs. Compare scan 011 lower exponents at audit. The von Neumann ordinal labels on the right have vertical equality strokes under 0 and 1. No mathematical checks performed.')
