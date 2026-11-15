from pathlib import Path
from math import sin,cos,radians
from tikz import *
from commit_page import commit
R=Path(__file__).resolve().parents[1]
def cross(x,y,angle=0,scale=1,cap=True):
 out=''
 for line in [[(-.38,-.18),(.35,.16)],[(-.25,.33),(.05,0),(.34,-.32)]]:
  pts=[]
  for a,b in line:
   a*=scale;b*=scale;t=radians(angle);pts.append(f'{x+a*cos(t)-b*sin(t):.3f},{y+a*sin(t)+b*cos(t):.3f}')
  out+=path('r,line width=2.1pt',' '.join(pts),False)
 if cap:
  t=radians(angle);a=-.18*scale;b=-.12*scale;c=-.03*scale;d=-.29*scale
  out+=path('k,line width=1.8pt',f'{x+a*cos(t)-b*sin(t):.3f},{y+a*sin(t)+b*cos(t):.3f} {x+c*cos(t)-d*sin(t):.3f},{y+c*sin(t)+d*cos(t):.3f}',False)
 return out
def ticks(x,y,n,angle=0):
 out='';t=radians(angle)
 for j in range(n):
  a=(j-(n-1)/2)*.16
  pts=[]
  for b in [-.20,.20]:pts.append(f'{x+a*cos(t)-b*sin(t):.3f},{y+a*sin(t)+b*cos(t):.3f}')
  out+=path('r,line width=2pt',' '.join(pts),False)
 return out
s=r'\scanpage{171}'+'\n'
# Upper left arrangement: seven long curves and independent decorations.
s+=start()+paths('g','4.56,1.56 6.39,2.10 8.18,2.98 10.75,4.44 12.18,5.57 13.48,6.95 14.45,8.36 15.15,9.80 15.61,11.31;2.86,2.86 3.90,4.10 5.52,5.68 7.33,6.87 9.35,7.89 11.38,8.75 13.75,9.34 15.15,9.80 17.71,9.78;8.99,.47 9.72,1.20 10.13,1.88 10.50,2.96 10.75,4.44 11.02,5.46 11.19,6.57 11.39,8.75 11.41,10.72 11.16,11.49;10.73,1.45 9.12,2.24 8.18,2.98 6.78,4.17 5.52,5.68 4.29,7.28 3.35,9.13 2.95,10.12 2.66,11.99 2.70,12.64;1.35,8.07 3.35,9.13 4.64,9.61 5.89,9.87 7.48,10.03 8.90,9.94 11.40,9.44 12.34,9.15 14.45,8.36 16.82,6.66;1.32,11.61 2.68,11.18 4.28,10.60 5.89,9.87 7.81,8.88 9.35,7.89 11.19,6.57 12.18,5.57 13.28,4.41 13.96,3.40')
s+=paths('p','8.90,.46 9.58,1.42 9.95,2.24 10.38,3.58 10.69,5.18 11.06,7.41 11.28,9.45 11.11,11.21;1.14,8.05 3.35,9.13 5.89,9.87 8.90,9.87 11.39,9.37 14.44,8.28 17.01,6.72;2.86,2.86 2.67,2.32 3.21,2.30;5.52,5.68 7.34,7.04 9.82,8.57 11.40,9.00 13.88,9.51 15.90,9.75')
for args in [(3.90,4.10,5,.9),(6.39,2.10,-30,1.3),(9.12,2.24,25,.9),(10.50,2.96,155,1),(9.33,3.77,140,1),(6.78,4.17,60,1.1),(11.02,5.46,0,1),(11.61,5.18,140,.8),(11.69,6.00,20,.9),(13.48,6.95,-10,.9),(4.29,7.28,10,1),(7.33,6.87,130,1.1),(10.35,7.23,55,1),(11.26,7.62,0,1),(10.49,8.29,110,.8),(12.02,8.86,120,.85),(13.38,8.71,40,.9),(14.64,8.99,-5,.9),(13.75,9.34,120,.8),(7.81,8.88,50,.9),(4.64,9.61,90,.8),(2.95,10.12,0,1),(4.28,10.60,90,.9),(8.90,9.94,70,.9)]:s+=cross(*args)
s+=paths('b,line width=2pt','1.00,1.62 1.29,1.38;5.35,5.92 5.69,5.84;10.56,4.20 10.83,4.16;12.40,5.30 12.41,5.77;11.35,6.38 11.44,6.47 11.35,6.63;9.18,8.00 9.55,8.07;3.31,9.18 3.39,9.37;5.90,9.86 6.04,9.98;11.50,9.59 11.61,9.43;12.76,9.02 12.85,9.13;15.10,9.82 15.23,9.90;10.17,1.75 10.15,1.98;11.47,8.74 11.58,8.84')
s+=paths('k,line width=2.3pt','5.28,5.44 5.74,5.35;7.93,2.85 7.93,3.13;10.57,4.43 10.81,4.76;11.90,5.81 12.33,5.82;10.85,6.77 11.25,6.82;9.74,7.61 9.82,8.04')+path('g,thin','8.85,11.38 9.20,10.97')+end()
# Small upper-right key.
s+=start()+paths('g','19.73,4.93 21.86,4.94 24.02,4.58;20.48,3.93 20.38,6.17;22.97,4.01 23.27,4.88 23.46,6.06')+paths('r','21.62,4.44 22.15,5.50;22.04,4.35 21.63,5.71')+paths('k','21.56,4.71 22.27,4.63;22.84,4.84 22.99,4.48 23.15,4.39;23.34,4.82 23.50,4.74 23.42,5.08')+path('k,thin,dashed','19.91,4.78 20.18,4.59 20.67,4.64 20.86,4.96')+path('k,thin','19.91,5.07 19.85,5.18 20.02,5.16 19.96,5.30 20.11,5.26 20.13,5.40 20.38,5.44',False)+end()
# Lower drawing and its multiplicity ticks.
s+=start()+paths('g','7.04,12.01 8.88,12.52 10.61,13.14 11.67,13.62 13.10,14.31 14.25,14.91 15.97,16.20 17.31,17.13 18.99,18.80 19.96,20.03 19.77,20.72 18.44,21.53 17.03,21.92 15.05,21.93 14.05,21.54 13.99,20.47 14.20,18.89 14.29,17.49 14.28,16.11 14.25,14.91 14.08,13.70 13.95,12.54 13.73,11.76 13.20,10.73;4.51,16.03 6.26,16.66 7.70,17.01 9.95,17.44 11.07,17.51 14.29,17.49 15.97,17.25 17.31,17.13 19.21,16.55 20.64,15.69 21.47,14.63 21.55,13.50 21.15,12.43 20.32,11.65 19.24,11.28 17.98,11.34 16.05,11.81 13.95,12.54 12.84,13.03 11.67,13.62 9.49,15.19 7.70,17.01 6.95,18.05 6.18,19.25;10.12,21.75 12.12,21.21 13.99,20.47 15.48,19.87 15.93,19.10 15.99,17.25 15.97,16.20 16.36,14.69 16.65,13.72 17.29,12.61 17.98,11.34 18.88,9.81 19.65,8.51 19.96,7.78')
s+=path('black!65!green,line width=1.4pt','6.18,19.25 6.95,18.05 7.70,17.01 9.49,15.19 11.67,13.62 13.95,12.54 16.05,11.81 17.98,11.34')
for args in [(9.49,15.19,20,1.4),(7.70,17.01,10,1.5),(12.84,13.03,60,1),(13.10,14.31,100,.9),(14.25,14.91,15,1.6),(14.08,13.70,-10,1),(14.28,16.11,-5,1),(15.28,15.65,100,.9),(16.65,13.72,10,1),(16.05,11.81,65,1),(17.98,11.34,10,1.6),(21.47,14.63,-5,1.4),(16.76,16.55,150,.9),(16.67,17.25,80,.8),(15.25,17.35,85,1),(11.07,17.51,90,1),(14.20,18.89,-10,1.4),(15.93,19.10,0,1.2),(13.99,20.47,10,1.7),(12.70,20.99,90,1),(18.44,21.53,20,1.5)]:s+=cross(*args)
for args in [(10.66,13.16,4,22),(12.46,14.04,4,24),(12.28,13.28,4,-26),(13.44,12.78,2,-26),(13.78,12.00,2,78),(13.99,13.20,2,80),(15.08,12.16,2,-22),(16.78,11.50,1,-7),(19.72,11.40,1,5),(18.92,9.84,1,32),(17.29,12.61,1,22),(16.31,14.94,2,89),(14.12,14.13,1,80),(14.15,15.54,1,85),(13.53,14.57,1,23),(14.95,15.37,1,28),(15.59,15.85,2,25),(15.98,16.50,3,85),(16.25,16.24,2,30),(15.99,17.99,1,90),(15.59,17.33,1,-5),(16.32,17.29,1,-5),(10.05,17.36,1,8),(9.49,17.31,1,8),(6.35,16.59,2,10),(8.44,15.96,2,-54),(10.62,14.29,4,-32),(6.92,18.04,2,-53),(14.17,19.60,3,90),(15.28,20.04,3,-30),(13.43,20.86,3,-18),(14.86,21.87,3,12)]:s+=ticks(*args)
s+=paths('b,line width=2pt','7.02,12.16 7.78,12.20;4.66,15.96 5.47,16.22;6.40,19.28 6.89,18.42;10.28,21.64 11.29,21.37;13.41,10.77 13.74,11.47;19.42,8.74 19.75,8.12;11.39,13.79 11.67,13.73 11.86,13.81;13.96,12.55 14.18,12.51 14.04,12.78;14.27,14.99 14.45,15.16;15.83,16.03 16.02,16.23;15.87,17.13 15.99,17.22 16.01,17.35;14.27,17.38 14.46,17.53;17.24,16.99 17.30,17.13 17.15,17.16')
s+=labels([('13.19,13.57','21'),('15.65,13.40',r'\unsure{27|17}'),('19.04,14.34','12'),('11.11,16.10','24'),('15.28,16.57','17'),('16.47,16.87','12'),('15.08,18.24','14'),('17.60,19.30','15')])+end()
# Left small pair of crosses.
s+=start()+path('g','.34,14.66 1.74,14.68 2.75,14.65 4.31,14.38')+paths('r','1.48,13.84 1.74,14.68 2.03,16.13;1.91,13.70 1.74,14.68 1.49,15.65;2.51,13.55 2.75,14.65 3.20,15.72;2.96,13.35 2.75,14.65 2.59,15.86')+path('b,dotted','1.78,14.53 2.72,14.56')+end()
s+=r'''\unsure{surface} : bord\inserted{$*$} \unsure{avec} $K$ cellulaire \inserted{et $L$ (cellulaire)}

\unsure{a)} tout sommet \inserted{int} de $K$ est d'ordre $4$ (sommet sur le bord d'ordre $1$)

\deleted{b) \unsure{Fon.}} Il en résulte un \unsure{dépliement} $\unsure{\widetilde K'|K'}$ de $K$, $\unsure{K|K'}$ \unsure{courbe} topologique

\textcircled{b} On a une \unsure{section} du \unsure{rev.} à deux feuillets $\widetilde K'$ de $K'$ des bords de l'immersion $K'\to X$

\deleted{c) \unsure{on a} $L\subset X$, \unsure{1-compl.}}

c) \deleted{\unsure{le gr.}} Tout sommet de $L$ d'ordre \unsure{pair}

\margin{d) $L\cap K$ fini; \unsure{et} \unsure{point} \unsure{topologique}\par
En $K\cap L$, chaque \unsure{branche} de $K$ croise chaque \unsure{branche} de $L$}

\unsure{e)} Sur chaque arête \inserted{(\unsure{orienté})} de $K$, il y a exactement un sommet de $L$, \deleted{\unsure{En ch. point}\illegible{1}} \inserted{soit $\unsure{\nu_a|\ell_a}$ \unsure{sa} multiplicité \unsure{d'incidence}.}

f) Pour chaque sommet (int.) $s$ de $K$, dans les quatre arêtes qui en sortent, les nb de pts de $L$ entre $s$ et le sommet de $K$ sur l'arête est indépendant de l'arête soit $\unsure{\nu_s|\ell_s}$.

\margin{g) Pour chaque sommet int $s$ de $K$, ou bien $s\notin L$, ou bien $s$ est un sommet de $L$, \unsure{d'ordre incident} $2$. Soit
\[
\unsure{\varepsilon_s}=\begin{cases}0&\text{si }s\notin L\\1&\text{si }s\in L\end{cases}
\]}

\margin{h) $\forall$ face $F$ de $K$, on a
\[
\sum_{s\in S(K)\cap\unsure{\overline F}}(2\unsure{\nu_s|\ell_s}+\varepsilon_s)
+\sum_{a\in A(K),\,a\unsure{\subset|\in}\unsure{\overline F}}\unsure{\nu_a|\ell_a}=2n
\]
$n$ indép. de $F$}
\margin{170}
'''
(R/'pages/MPL_154_127-176_154_scan171.tex').write_text(s)
commit(171,[('drawing','upper left','seven curved lines with orange crosses and dark caps'),('drawing','upper right','three green lines and orange crossing'),('drawing','lower centre','marked curves; 21 27 12 24 17 12 14 15'),('drawing','left middle','two orange crosses joined by dotted blue line'),('text','right upper','surface : bord; K cellulaire'),('insertion','above right header','star; et L cellulaire'),('text','right upper a','tout sommet de K est d ordre 4'),('insertion','a above sommet','int'),('deletion','before depliement paragraph','b) Fon.'),('text','right below a','Il en resulte un depliement'),('text','right b','On a une section du rev. a deux feuillets'),('deletion','right between b and c','c) on a L subset X 1-compl.'),('text','right c','Tout sommet de L d ordre pair'),('deletion','above Tout','le gr.'),('margin note','beside c and e','d) L intersection K fini'),('text','right e','Sur chaque arete de K'),('insertion','above arete','oriente'),('deletion','end of e','En ch. point'),('insertion','above and below deletion in e','soit nu a sa multiplicite d incidence'),('text','right f','Pour chaque sommet int. s de K'),('margin note','bottom left g','Pour chaque sommet int s de K'),('display','bottom left g','epsilon s = 0 or 1'),('margin note','bottom left h','forall face F de K on a'),('display','bottom edge','sum over S(K) and A(K) = 2n; n indep. de F'),('margin note','bottom left','170')],observations='Whole/a/b personally inspected, followed by six enlarged text crops. The prose is extremely compressed; uncertain whole words, numbering and cancellations are explicitly marked. The e correction appears to introduce a subscripted multiplicity; nu versus ell is unresolved in both prose and bottom formula, and is marked consistently rather than inferred. The bottom summation is close to the cut edge. The relation attaching the small marginal d paragraph and the parenthetical above arete remains uncertain; no mathematical completion has been supplied. Two large curve systems and two small keys are independently drawn, with individual groups of multiplicity ticks and numeric labels.')
