import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{57}
% archive foliation: 59
un pt de $K$ d'ordre $\geq2$, ou d'ordre 1 :

\uline{Lemme 2} Soit $K$ un segment topologique $\subset\mathbb C$,
et $x\in K$. \inserted{On suppose $K$ assez régulier (rectifiable suffit ??)} Alors

a) Si $x$ n'est pas extrémité de $K$, alors il existe
\deleted{un voisinage \inserted{ouvert} $U$ de $x$ dans $\mathbb C$, ne contenant pas
d'extrémités de $\unsure{U|K}$, tel que $U\setminus K\cap U$
ait deux composantes connexes $U'$ et $U''$
avec $\overline{U'}\cap U=U'\cup(K\cap U)$, $\overline{U''}\cap U=U''\cup(K\cap U)$, et
\unsure{fonction holo}}

\figure{\begin{tikzpicture}[scale=.65]
\draw[dashed] (-.1,1.1) .. controls (-1.6,1) and (-1.6,-.5) .. (-.4,-.5);
\draw (-.4,-.5) .. controls (.9,-.5) and (1,1) .. (-.1,1.1);
\draw (.85,1.5) .. controls (.65,.9) and (.0,.95) .. (-.3,.45)
.. controls (.05,.2) and (.1,-.5) .. (.14,-.8)
.. controls (.2,-1.15) and (.55,-1.3) .. (.5,-1.6);
\foreach \x in {0,.18,.36,.54} {\draw (\x,-.35)--({\x+.26},.77);}
\node at (-.85,-.05) {$x$};
\end{tikzpicture}}

\deleted{\unsure{$f$}} une application continue injective
\inserted{de $\deleted{\unsure{\mathbb C}}H\cap\mathring D\longrightarrow\mathbb C$},
\deleted{de $H\cap\mathring D$ dans $\mathbb C$, hol. dans $H\cap$
$\mathring D\subset\mathbb C$, continue}
holomorphe dans \deleted{$\unsure{D\setminus H\supset\mathbb R}$}
\inserted{$(\operatorname{Int}H)\cap\mathring D$},
\deleted{$=\,]-1,+1[\quad(\unsure{\ne}\ D^{++}\amalg D^{--})$}
\deleted{(mais pas \unsure{néct}\ dans deux plans $\mathbb R$)}
(mais pas néc \unsure{hol. au vts de}\ \deleted{dans}
$\delta H\cap\mathring D=\,]-1,+1[)$ telle que
$f(\delta H\cap\mathring D)\subset K$ et
$f(0)=x$. De plus, pour une rive donnée de
$K$ en $x$, OPS que cette rive est celle déterminée
par \inserted{$\operatorname{Im}f=$} $f(H\cap\mathring D)$.

b) Si $x$ est extrémité de $K$, alors $\exists$
$f:H\cap\mathring D\longrightarrow\mathbb C$, hol. \inserted{\deleted{et topologique}}
dans $(\operatorname{Int}H)\cap\mathring D$, \deleted{et}
\deleted{injective dans $\unsure{\mathring D}$ telle que
$\unsure{\{f(-t)=f(t)}$ $\unsure{\{\}}$}
\deleted{\unsure{soit en}\ $f$}
\inserted{telle que $f(0)=0$}
\deleted{$\unsure{f\,]-1,0)}$}
\deleted{$f\mid[-1,0]$ et $f\mid[0,1[$ soient injectifs,}

\figure{\begin{tikzpicture}[scale=.65]
\draw (-.08,2.4).. controls (-.6,1.7) and (.15,1.2) ..(-.25,.65)
..controls(-.7,.2)and(-.08,-.1)..(-.22,-.75);
\draw[dashed](-.85,-.7) arc[start angle=145,end angle=35,radius=1];
\draw (-1.05,-1.35) .. controls (-1.25,-2.25) and (.15,-2.8) .. (.7,-1.95);
\draw (.7,-1.95)..controls(1.1,-1.3)and(.9,-.85)..(.65,-.75);
\node at (-.25,-1.35) {$x$};
\end{tikzpicture}}
"""
save(57,tex,[('text','top','un pt de K d’ordre ≥2'),('text','upper','Lemme 2 Soit K'),('insertion','after K hypothesis','On suppose K assez régulier (rectifiable suffit ??)'),('text','upper middle','a) Si x n’est pas extrémité'),('deletion','large block upper middle','un voisinage U de x; composantes connexes'),('insertion','inside deleted block','ouvert'),('display','inside deleted block','U-bar′∩U; U-bar″∩U'),('drawing','left upper middle','K crossing a circle; hatched right side; x'),('deletion','middle left','f'),('text','middle','une application continue injective'),('insertion','above deleted line','de H∩D°→C'),('deletion','inside insertion','C'),('deletion','middle two lines','de H∩D° dans C; hol.; continue'),('text','middle','holomorphe dans'),('deletion','middle right','D\H ⊃ R'),('insertion','middle right','(Int H)∩D°'),('deletion','middle display',']-1,+1[; D++ ⊔ D--'),('deletion','middle two lines','mais pas néct; deux plans R'),('text','below middle','mais pas néc hol. au vts de δH'),('deletion','same parenthesis','dans'),('text','lower middle','telle que f(δH∩D°)⊂K et f(0)=x'),('text','lower','De plus pour une rive donnée'),('insertion','above f image','Im f='),('text','bottom','b) Si x est extrémité de K'),('display','bottom','f:H∩D°→C'),('insertion','above dans','et topologique'),('deletion','above and after dans','et topologique; et'),('deletion','bottom revisions','injective dans D° telle que; f(-t)=f(t)'),('deletion','bottom revisions','soit en f; f ]-1,0)'),('insertion','bottom revisions','telle que f(0)=0'),('deletion','bottom line','f|[-1,0] et f|[0,1[ soient injectifs'),('drawing','bottom left','arc ending inside circle; x')],
 doubts=[('cancelled upper paragraph','extrémités de U','K possible; written letter appears U','low'),('middle revisions','D\H⊃R; D++⊔D--; deux plans R','heavily crossed and reorganized formulas','low'),('bottom b)','injective dans D°; f(-t)=f(t); f(0)=0','overlapping cancellations; first two are cancelled, f(0)=0 appears as insertion','low')],
 abbreviations=[('néc','nécessairement'),('vts','voisinage / voisinages (reading uncertain)')],
 leads=['Self-flagged repeated regularity hypothesis in Lemme 2: On suppose K assez régulier (rectifiable suffit ??).','Interior-arc and endpoint local uniformization are separated; part b at bottom is substantially withdrawn/reworked. Compare continuation, not an established lemma in this draft form.'])
