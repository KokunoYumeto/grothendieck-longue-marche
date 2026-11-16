import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from save_page import save
tex=r"""
\figure{\begin{tikzpicture}\node[draw,circle] {$\mspage{\unsure{e|c}}$};\end{tikzpicture}}
\diagram{\begin{tikzcd}[column sep=large,row sep=huge]
X \arrow[r,bend left=24,"g_0=\varphi i"{name=t}]
  \arrow[r,bend right=24,"g_1=g"'{name=b}] \arrow[d,"i"'] & Y \arrow[d,"p"]\\
X' \arrow[ur,-,bend left=18,"\theta_0=\varphi"]
   \arrow[ur,dashed,"\theta_1=\bar\varphi"']
   \arrow[r,bend left=24,"g'_0=p\varphi"{name=u}]
   \arrow[r,bend right=24,"g'_1=g'"'{name=v}] & Y'
\arrow[from=t,to=b,"k"',shorten <=3pt,shorten >=3pt]
\arrow[from=b,to=t,shift right=8pt,shorten <=4pt,shorten >=4pt]
\arrow[from=u,to=v,"\unsure{h}"',shorten <=3pt,shorten >=3pt]
\arrow[from=v,to=u,shift left=8pt,shorten <=4pt,shorten >=4pt]
\end{tikzcd}}
We know \inserted{by assumption} there exist \inserted{simplicial} homotopies
\[
k:g_0=\varphi i\longrightarrow g_1=g\qquad\unsure{\text{and}}
\]
\[
h:g'_0=p\varphi\longrightarrow g'_1=g'.
\]
All we have to do, is to check that we can choose these homotopies \uline{compatible} with $i$ and $p$.
\margin{But in case $Y'$ is the final object, \deleted{\unsure{considering that}} \inserted{we are through!}}
\figure{\begin{tikzpicture}\draw (0,0)--(-.2,.7);\draw (.1,0)--(-.1,.8);\draw (.2,0)--(0,.6);\end{tikzpicture}}
\deleted{\diagram{\begin{tikzcd}[column sep=small]
(X\amalg X) \arrow[d,"\mathrm{cofib.}"] & \amalg & (X'\amalg X') \arrow[d,"\mathrm{cofib.}"]\\
X\otimes J & \amalg \arrow[d] & X'\otimes J \arrow[r] & (Y\otimes J)\amalg\unsure{\bar\theta}\\
Y & \amalg & Y'
\end{tikzcd}}}
diagram
\diagram{\begin{tikzcd}
X\otimes J \arrow[r,"k"] \arrow[d,"i\otimes J"'] \arrow[dr,bend left=9] \arrow[dr,bend right=9] & Y \arrow[d,"p"]\\
X'\otimes J \arrow[r,"h"'] & Y'
\end{tikzcd}}
\deleted{which a priori is \uline{not} commutative but only commutative \deleted{\unsure{for}} on $X\amalg X\longrightarrow X\otimes J$}
\deleted{\diagram{\begin{tikzcd}
X\otimes J \arrow[r,"k"] \arrow[d,"i\otimes J"'] & Y \arrow[d,"p"]\\
X'\otimes J \arrow[r,"h"'] & Y'
\end{tikzcd}}}
\deleted{\diagram{\begin{tikzcd}[row sep=large]
X\amalg X \arrow[d] \arrow[dr,bend left=18,"u=(g_0,g_1)"] & \\
X\otimes J \arrow[r,dashed,-,"h'!"] \arrow[d,"i\otimes J"'] & Y \arrow[d,"p"]\\
X'\otimes J \arrow[r,"h"'] & Y'
\end{tikzcd}}}
\deleted{This diagram is commutative and we look for $h'$ which keeps it commutative.}
\deleted{We invert the problem, \deleted{\unsure{forgetting}} \inserted{\unsure{shortcircuiting}} $X'\otimes J$ by the arrow $h\circ(i\otimes J)=v$.}
\deleted{We know there is a \deleted{\unsure{and we want a}} $k$ s.th. $kj=u$, but \unsure{unfortunately} $ph\ne v$; only $pk\overset{s}{\sim}v$}
\deleted{(But in case $Y'$ is final object, we are already through!)}
\deleted{\diagram{\begin{tikzcd}
X\amalg X \arrow[r,"u=(g_0,g_1)"] \arrow[d,"j", "\text{\uuline{non} trivial cofibration}"'] & Y \arrow[d,"p\ \text{fibration}"]\\
X\otimes J \arrow[r,"v"'] \arrow[ur,dashed,"h'?"] & Y'
\end{tikzcd}}}
\margin{\deleted{\unsure{\times 0}}}
\figure{\begin{tikzpicture}[scale=.6]
\draw (0,12)--(2,13);\draw (0,10)--(4,13);\draw (0,7)--(1,8);
\draw (1,8)--(6,11);\draw (3,13)..controls(4,12.7)and(5,12.5)..(5.5,12);
\draw (0,6)--(8,-1);\draw (2,-1)--(10,8);
\end{tikzpicture}}
\mspage{22}
"""
elements=[('text','top centre','circled e/c'),('diagram','top centre','X,Y,X′,Y′; g0,g1,θ0,θ1,k,h,i,p'),('text','top right','We know there exist homotopies'),('display','upper right','k:g0=φi→g1=g'),('display','upper right','h:g′0=pφ→g′1=g′'),('text','upper right','All we have to do'),('drawing','next to right addition','three oblique emphasis strokes'),('diagram','cancelled upper left','(X amalg X) amalg (X′ amalg X′)'),('text','centre','diagram'),('diagram','centre','X⊗J,Y,X′⊗J,Y′; k,h,i⊗J,p; parallel diagonals'),('text','centre right','which a priori is not commutative'),('diagram','cancelled middle left','X⊗J,Y,X′⊗J,Y′'),('diagram','cancelled lower centre','X amalg X; u=(g0,g1); h′!'),('text','lower right','This diagram is commutative'),('text','lower right','We invert the problem'),('text','lower right','We know there is a k'),('text','bottom right','But in case Y′ is final object'),('diagram','bottom left','j non trivial cofibration; h′?'),('drawing','across cancelled constructions','long cancellation diagonals'),('text','bottom left','22')]
if __name__=='__main__':save(107,23,tex,elements,'cancelled_draft',notes='Compatibility of chosen homotopies remains the issue. Two explicit final-object comments say “we are through!” and “we are already through!”; cancelled general construction observes only pk homotopic to v, not strict equality (literal ph≠v in text). Distinguish these provisional claims from a completed general lifting proof. The long cancellation strokes cover the lower attempts; top paragraph and principal comparison diagram remain live. Reading of shortcircuiting and the circled letter particularly uncertain.')
