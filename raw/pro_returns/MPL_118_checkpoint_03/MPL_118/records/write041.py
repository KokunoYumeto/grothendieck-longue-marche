from save_page import save
text=r'''
\scanpage{41}
% archive foliation: 40
Soit $f=f_0\in\operatorname{Fl}(\unsure{\underline{\mathrm{Cat}}|\mathrm{Cat}})$ \inserted{:\unsure{$f$}$:X_0\mathbin{-}X_1$} telle que $\unsure{\sigma|\gamma}(f)$ iso: prouver $f\in\underline W$. OPS $f=f_0$ imm. ouverte. Par calcul des fractions, $\exists\unsure{f_1|g}:X_1\mathbin{-}X_2$, telle que $\unsure{f_1|g}f_0\in\underline W$; donc $\sigma(\unsure{f_1|g}f_0)=\sigma(\unsure{f_1|g})\sigma(f_0)$ iso, donc $\sigma(\unsure{f_1|g})$ iso. OPS quitte à factoriser que $g$ imm. ouverte.

\margin{\diagram{\begin{tikzcd}[row sep=tiny,column sep=large]
X_0\arrow[d,equal]&X_1\arrow[d,equal]\\
X\arrow[r,"\substack{f\\\Vert\\f_0}"']&Y\arrow[r,dash,"\substack{g\\\Vert\\f_1}"']&X_2
\end{tikzcd}}}

Donc de proche en proche
\deleted{$f_0,g_0,f_1,g_1,\unsure{f_n|f_2},\unsure{g_n|g_2}$}
\deleted{$f_0,f_1,f_2$}
\deleted{donc}
\diagram{\begin{tikzcd}[column sep=large]
X_0\arrow[r,"f_0=\unsure{f}"]&X_1\arrow[r,"f_1=\unsure{g}"]&X_2\arrow[r,dash,"\unsure{f_3|f_2}"]&{}
\end{tikzcd}}
système inductif d'imm. ouvertes, telles que les produits de deux consécutifs \unsure{soit|soient} $\in\underline W$. Soit $X_\infty=\varinjlim_n X_n$, on a
\diagram{\begin{tikzcd}
X_0\arrow[rr,"f=f_0"]\arrow[dr,"i_0"']&&X_1\arrow[dl,"i_1"]\\
&X_\infty&\text{commutatif}
\end{tikzcd}}
il suffit de prouver que $i_0$ et $i_1$ sont $\in\underline W$.
\deleted{\unsure{Cela résulte du}} \inserted{Il suffit bien sûr de} le prouver pour $i_0$ \deleted{\unsure{lemme}} [pour $i_1$, on remplacera $f_0$ par $f_1$]. Or on a
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
X_0=\varinjlim_n\arrow[d,"i_0"']&(&X_0\arrow[r,dash]&X_0\arrow[r,dash]&X_0\arrow[r]&\cdots&X_0\unsure{)}\arrow[d]\arrow[r,dash]&\cdots&)\\
X_\infty=\varinjlim_n&(&X_0\arrow[r,dash]&X_2\arrow[r,dash]&X_4\arrow[r,dash]&\cdots&X_{2n}\arrow[r,dash]&\cdots&)
\end{tikzcd}}
et $i_0$ est $\varinjlim$ des $i_0^{2n}:X_0\mathbin{-}X_{2n}$, qui sont $\in\underline W$: donc on gagne!!

\margin{\deleted{\unsure{Djamel|Djamal}}}
'''
elements=[('text','top','Soit f=f0 in Fl(Cat)'),('insertion','above first line','f:X0 - X1'),('display','upper','sigma(f) iso; f in W'),('text','upper','OPS f=f0 imm. ouverte'),('text','upper middle','Par calcul des fractions'),('display','upper middle','exists f1:X1 - X2; f1 f0 in W'),('display','upper middle','sigma(f1 f0)=sigma(f1)sigma(f0) iso'),('text','upper middle','OPS quitte à factoriser que g imm. ouverte'),('margin note','upper left','X0=X, X1=Y; f=f0; g=f1'),('diagram','upper left','X →Y - X2'),('text','middle','Donc de proche en proche'),('deletion','middle','f0,g0,f1,g1,f_n,g_n'),('deletion','above preceding deletion','f0,f1,f2'),('deletion','middle left','donc'),('diagram','middle','X0 f0=f →X1 f1=g →X2 f3 -'),('text','middle lower','système inductif d’imm. ouvertes'),('display','middle lower','products of two consecutive in W; X_infty=lim X_n'),('diagram','lower middle','X0 f=f0 →X1; i0; i1; X_infty; commutatif'),('text','lower','il suffit de prouver que i0 et i1 sont in W'),('deletion','lower','Cela résulte du'),('insertion','above cancelled phrase','Il suffit bien sûr de'),('text','lower','le prouver pour i0'),('deletion','under le prouver','lemme'),('text','lower','pour i1 on remplacera f0 par f1'),('text','lower','Or on a'),('diagram','bottom','X0=lim constant sequence; X_infty=lim X0 X2 X4 X2n; i0'),('text','bottom','et i0 est lim des i0^2n'),('display','bottom','i0^2n:X0 - X2n; in W'),('text','bottom','donc on gagne!!'),('margin note','bottom left upside down','Djamel or Djamal'),('deletion','bottom left upside down','Djamel or Djamal')]
save(41,text,'text',elements,'Reworked saturation proof after cancelled scan-040 draft. Old g becomes f1 in several overwritten formulas; alternatives marked. The third label in the sequence appears f3 rather than expected f2 and is retained as first reading. Plain dashes remain plain. Last comparison diagram includes the extra visible parenthesis after X0. Bottom blue name cancelled by brown/black diagonal was rotated and is uncertain. No proof checked while transcribing.')
