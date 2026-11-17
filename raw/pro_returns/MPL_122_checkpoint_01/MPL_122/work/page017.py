from record import save
save(17,r'''\scanpage{17}
\diagram{\begin{array}{cccc}
W&P&Q&R\\
V'&\overbrace{X'_{\unsure{\eta|\gamma}}=V'_{\unsure{\eta|\gamma}}}&\unsure{V'_s}&V'_s\times\unsure{\eta|\gamma}
\end{array}}
\diagram{\begin{tikzcd}
& W \arrow[dl,dash] \arrow[dr,dash] & \\
P \arrow[dr,dash] && Q \arrow[dl,dash]\\
& R &
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw (0,0)--(6,0)--(6,-.6)--(12,-.6);\end{tikzpicture}}
\diagram{\begin{array}{cccc}
M&N&T=\dot M,&S=\dot N\\
X'_{\overline{\unsure{\eta|\gamma}}}&\deleted{\unsure{D}}\unsure{\sim}e&V'_s&\unsure{\eta|\gamma}\sim S^1
\end{array}}

\diagram{\begin{tikzcd}[row sep=1.1em,column sep=1.1em,
execute at end picture={
\draw[gray,rotate around={-35:(-1,0)}] (-1,0) ellipse (1.3 and 2.1);
\draw[gray,rotate around={-35:(1.2,0)}] (1.2,0) ellipse (1.3 and 2.1);
\draw[gray,rotate around={-35:(-3,-1.4)}] (-3,-1.4) ellipse (1.1 and 1.7);
\draw[gray,rotate around={-35:(3,-1.4)}] (3,-1.4) ellipse (1.1 and 1.7);
\foreach \x in {0,.25,.5,.75,1,1.25}{\draw (-4.5+\x,-1.2-\x) -- (-5+\x,-2.3-\x);\draw (3+\x,-1.8-\x/2)--(2.4+\x,-2.9-\x/2);}
}]
&&S&&W&&&&\\
s \arrow[urr] &&&P \arrow[ul] \arrow[ur,hook] &&&&T&\\
&M \arrow[ul,very thick] \arrow[urr,hook] &&&&Q \arrow[uul,hook] \arrow[urr] &&&t \arrow[ul]\\
&&T \arrow[ul,hook,very thick] &&{\begin{gathered}R\\\Vert\\T\times S\end{gathered}} \arrow[uul,hook,very thick] \arrow[ur,hook] &&&N \arrow[ull,hook] \arrow[ur]&\\
\unsure{s}&&\unsure{s}&&(s,t) \arrow[uul,hook] \arrow[rr,hook] &&S \arrow[ul,hook] \arrow[ur,hook,"\unsure{\times}"'] &&\unsure{T}\\
&&&&\varnothing \arrow[u,hook] &&&t \arrow[ul,very thick] \arrow[ur,dashed,hook]&
\end{tikzcd}}

\margin{$\displaystyle\binom{5}{2}=\frac{5.4.3}{12.}=10$}

\diagram{\begin{tikzcd}
D^1\times B\sim B\\
S^1\times B \arrow[u,hook]
\end{tikzcd}}
\deleted{\diagram{\begin{tikzcd}
& H^{\unsure{n+i}}\\
H^i(B)\times H^{i-1}(B) \arrow[r] \arrow[d] & {}\\
H^i(B &
\end{tikzcd}}}

\margin{\diagram{\begin{array}{ccccc}1&2&3&4&5\\\cdot&\cdot&\cdot&\cdot&\cdot\end{array}}}
\margin{\diagram{\begin{array}{ccc}
123&234&345\\124&235&\\125&245&\\134&\cdot&\\135&&\\145&&
\end{array}}}

\diagram{\begin{tikzcd}[row sep=1.1em,column sep=1.3em,
execute at end picture={
\draw[very thick] (-2.7,1.3)--(-1.4,2.4)--(2.2,-.3)--(.7,-1.7)--cycle;
\draw (-2.55,1.4)--(-1.25,2.5)--(2.35,-.2)--(.85,-1.6);
\draw[gray] (-4,-.4)--(-2.8,.7)--(-.8,-1.4)--(-2,-2.5)--cycle;
\draw (2.2,-1.1)--(3.2,-.1)--(4.1,-.7)--(3.1,-1.8)--cycle;
\foreach \x in {0,.18,.36,.54,.72}{\draw (2.3+\x,-1.15+\x)--(3.1+\x,-1.7+\x);}
}]
&\unsure{\eta|S}&&V'&&V'_s&\\
s \arrow[ur] &&X'_{\unsure{\eta|\gamma}} \arrow[ul] \arrow[ur,hook,very thick] &&V'_s \arrow[ul,hook,very thick] \arrow[ur,"\sim"] &&t \arrow[ul]\\
&X'_{\overline{\unsure{\eta|\gamma}}} \arrow[ul,very thick] \arrow[ur,hook,very thick] &&V'_s\times\unsure{\eta|\gamma} \arrow[ul,very thick] \arrow[ur,very thick] &\unsure{S^1}&&e \arrow[ull,very thick] \arrow[u,"\sim"']\\
&&V'_s \arrow[ul,very thick] \arrow[ur,very thick] &&\unsure{\eta|\gamma} \arrow[ul,very thick] \arrow[urr] &&\unsure{X'_s}\\
\unsure{\cdot}&&&(s,t) \arrow[ul,very thick] \arrow[ur] &&t&
\end{tikzcd}}

\margin{$10+10+2$}
\margin{\diagram{\begin{array}{ccc}
\varnothing&T\sim S&R\\
5+5&2+2&2\\
3&3+3&\\
2+2&1+1&\\
1+2&1+1&\\\hline
\boxed{20}&\boxed{14}&\boxed{2}
\end{array}}}
\margin{\diagram{\begin{array}{c}M\sim N\\2+2\\\hline\boxed4\end{array}}}

\diagram{\begin{tikzcd}[row sep=large,column sep=large]
&H^{i-1}(R) \arrow[d,very thick]&\\
H^{n-i}(P)^\vee \arrow[dr]& & H^{n-i}(Q)^\vee \arrow[dl]\\
&H^i(W) \arrow[dl,very thick] \arrow[dr]&\\
H^i(P) \arrow[dr]&&H^i(Q) \arrow[dl] \arrow[dr,very thick]&\\
&H^i(R) \arrow[d,dash]&&H^{n-i\unsure{-1}}(P)^\vee\\
&H^{i+1}(W)&&
\end{tikzcd}}
\diagram{\begin{tikzcd}
H^i(Q)\times H^{n-i\unsure{-1}}(P) \arrow[r] & H^{n-1}(R)\simeq\Lambda\\
H^{\unsure{n-i}}(P)^\vee \arrow[r] & H^i(P)
\end{tikzcd}}

\margin{\figure{\begin{tikzpicture}\node[draw,ellipse] {$40$};\end{tikzpicture}} suites exactes de coh. \unsure{relative}}
\margin{et autant pour l'homologie ...}
\margin{Cela fait $80$ suites exactes, mais}
\mspage{16}
''',[
('diagram','top left','W P Q R / V′ X′η=V′η V′s V′s×η'),
('diagram','top right','W—P,Q—R'),
('drawing','below header','stepped separating rule'),
('diagram','below rule','M N T=Ṁ S=Ṅ / X′barη e V′s η∼S¹'),
('deletion','table N entry','D'),
('diagram','upper central','S W T; s P Q t; M R N; T S; (s,t); ∅'),
('drawing','overlaid upper central diagram','oval outlines, hatching, s t T labels'),
('margin note','upper right','(5 choose 2)=5.4.3/12.=10'),
('diagram','left middle','D¹×B∼B / S¹×B'),
('deletion','left below product diagram','H^i(B)×H^{i−1}(B), H^{n+i}, H^i(B'),
('diagram','within cancelled formula','downward arrow and unfinished right arrow'),
('margin note','right middle','1 2 3 4 5 and dots'),
('diagram','right middle','123 124 125 134 135 145; 234 235 245; 345'),
('diagram','central lower','V′, X′η, V′s, X′barη, V′s×η, e, (s,t)'),
('drawing','overlaid central lower diagram','two outlined quadrilaterals and hatched small quadrilateral'),
('margin note','right below triples','10+10+2'),
('diagram','right lower arithmetic','∅; T∼S; R; totals 20 14 2'),
('diagram','right below arithmetic','M∼N; 2+2; 4'),
('diagram','lower left','H^{i−1}(R), H^{n−i}(P)vee, H^i(W), H^i(P), H^i(Q)'),
('diagram','bottom centre','H^i(Q)×H^{n−i−1}(P)→H^{n−1}(R)≃Λ'),
('margin note','bottom right','40 suites exactes de coh. relative'),
('drawing','bottom right around 40','oval around 40'),
('margin note','bottom right','et autant pour l’homologie ...'),
('margin note','bottom right last lines','Cela fait 80 suites exactes, mais'),
('margin note','bottom left','16')
],[
('header and diagrams','η|γ','Repeated descending Greek letter; provisional consistent first reading η, alternative γ.','medium'),
('table N entry','D (deleted), ∼e','The black overwritten letter and relation are indistinct.','low'),
('upper central diagram','s; s; T; crossed × on S→N','Labels overlap hatching; arrows and oval outlines intersect.','low'),
('upper central diagram','M→P and P→W hooks','Both ends are heavily retraced; hook tails are retained, with directions from the visible heads.','medium'),
('upper right count','(5 choose 2)=5.4.3/12.=10','Numerator and denominator copied literally; no missing factor supplied.','high'),
('left cancellation','H^{n+i}; H^i(B','Upper exponent incomplete/overwritten; lower expression has no secure closing parenthesis.','low'),
('lower central diagram','η|S; S¹; X′s','Black corrections and intersecting outlines obscure these separate labels.','low'),
('lower cohomology diagram','n−i−1','Stroke before 1 is thick and blot-like; marked within both occurrences.','medium'),
('last cohomology arrow','H^{n−i}(P)vee','Exponent is overwritten and partly raised above the original baseline.','low'),
('right bottom prose','relative','Last word is compressed against the edge; no final plural s established.','medium')
],['Forty relative-cohomology sequences and as many homology sequences are counted; final mais leaves a qualification unfinished.','The displayed binomial arithmetic is not silently corrected.','Boundary notation changes to dotted letters Ṁ,Ṅ on this diagram sheet.'])
