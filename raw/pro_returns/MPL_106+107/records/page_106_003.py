import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\texttt{DATA SET UTILITY - GENERATE}\hfill\texttt{PAGE 0001}

\texttt{IEB352I WARNING : OUTPUT RECFM/LRECL/BLKSIZE COPIED FROM INPUT}

\texttt{PROCESSING ENDED AT EOD}

\diagram{\begin{tikzcd}
x \arrow[r,hook,"\sim"] \arrow[d,"\sim"'] & x' \arrow[dl,"\sim"]\\
y\deleted{\unsure{y}} \arrow[ur,bend right=18,"\sim"'] &\\
y \arrow[u,"\unsure{w}"'] &
\end{tikzcd}}
\diagram{\begin{tikzcd}
& y \arrow[d,"\sim"'] \arrow[dr,"\sim"] &\\
x \arrow[r] & y' \arrow[dr] & y'' \arrow[d]\\
&&y'''
\end{tikzcd}}
\diagram{\begin{tikzcd}
\unsure{x|a} \arrow[dr] \arrow[dd,bend right=15] & y \arrow[d,"\sim"]\\
& \bar y \arrow[dl,"\sim"'] \arrow[d,"\sim"]\\
\bar y' \arrow[r,hook] & \bar y''
\end{tikzcd}}
\diagram{\begin{tikzcd}
\unsure{x|a} \arrow[r,hook] \arrow[d,equal] & \bar y \arrow[d] & y \arrow[l] \arrow[d,equal]\\
x \arrow[r,hook] \arrow[d,equal] & \unsure{\bar y''} & y \arrow[l,very thick] \arrow[d,equal]\\
x \arrow[r] & \bar y' \arrow[u,very thick] & y \arrow[l]
\end{tikzcd}}
\diagram{\begin{tikzcd} {} \arrow[r] & {} \end{tikzcd}}
\diagram{\begin{tikzcd}
{} \arrow[r,hook] \arrow[d] & {} \arrow[d,"\sim"'] & {} \arrow[l,"\sim"'] \arrow[d]\\
{} \arrow[r] & {} & {} \arrow[l]\\
{} \arrow[r] \arrow[u] & {} \arrow[u] & {} \arrow[l] \arrow[u]
\end{tikzcd}}
\diagram{\begin{tikzcd}x \arrow[r,hook] & {}\end{tikzcd}}
\deleted{$\unsure{x\amalg x}$}
\diagram{\begin{tikzcd}x \arrow[r,very thick] & y\end{tikzcd}}
\diagram{\begin{tikzcd}
x \arrow[r,"\deleted{u}"] \arrow[dr,"u"] \arrow[ddr,"u'"'] & y \arrow[d,equal]\\
& y \arrow[d,equal]\\
& {}
\end{tikzcd}}
\diagram{\begin{tikzcd}x \arrow[r,shift left=.8ex,"u"] \arrow[r,shift right=.8ex,very thick] & y\end{tikzcd}}
\diagram{\begin{tikzcd}
&& y \arrow[dl,"\sim"'] \arrow[dr,"\sim"] \arrow[dd,"\unsure{r}"] &&\\
x \arrow[r,hook,"f"] \arrow[drr,"\unsure{i_1f}"'] & y'_1 && y'_2 & x \arrow[l,"g"'] \arrow[dll,"i_2g"]\\
&& \bar y \arrow[ul,"r_1"] \arrow[ur,"r_2"'] &&
\end{tikzcd}}
\diagram{\begin{tikzcd}
x \arrow[r,"f"] & y &\\
x \arrow[r] & \bar y & y \arrow[l]\\
x \arrow[r,"g"] & y &
\end{tikzcd}}
\diagram{\begin{tikzcd}
x \arrow[r,"f"] \arrow[d,equal] & y \arrow[d,"i","\sim"'] & y \arrow[l,"1"'] \arrow[d,equal]\\
x \arrow[r,"h"] \arrow[d,equal] & \bar y & y \arrow[l,"i"'] \arrow[d,equal]\\
x \arrow[r,"g"] & y \arrow[u,"i"] & y \arrow[l,"1"']
\end{tikzcd}}
\diagram{\begin{tikzcd}
x \arrow[r,shift left=.7ex,"f"] \arrow[r,shift right=.7ex,"g"'] \arrow[dr,"h"'] & y \arrow[d,"i","\sim"']\\
& \bar y
\end{tikzcd}}
\diagram{\begin{tikzcd}{} \arrow[r,leftrightarrow,very thick] & {}\end{tikzcd}}
\diagram{\begin{tikzcd}x \arrow[r,very thick,"\sim"] \arrow[d] & y\\ {} \arrow[ur] &\end{tikzcd}}
\diagram{\begin{tikzcd}
y\vee y \arrow[r] & y &\\
x\vee x \arrow[u,"f\vee g"] \arrow[r,very thick] & C \arrow[u,"h"'] & \deleted{\unsure{x}} \arrow[l,shift left=.7ex,"\deleted{\unsure{g}}"] \arrow[l,shift right=.7ex]
\end{tikzcd}}
\diagram{\begin{tikzcd}x \arrow[r,shift left=.7ex,"\unsure{j_1}"] \arrow[r,shift right=.7ex,"\unsure{j'_2|j_2}"'] & C \arrow[r,"\deleted{g}\ h"] & y\end{tikzcd}}
\diagram{\begin{tikzcd}
a \arrow[dr] & y \arrow[d,"\sim"] \arrow[dr] & {} \arrow[d]\\
& \deleted{\unsure{\bar y}} \arrow[dr,shift left=.4ex] \arrow[dr,shift right=.4ex] & {} \arrow[d,"\sim"]\\
&& {}
\end{tikzcd}}
\diagram{\begin{tikzcd}x. & x\end{tikzcd}}
\diagram{\begin{tikzcd}
a \arrow[r] \arrow[d] & \unsure{a} \arrow[r,shift left=.8ex,"\sim"] \arrow[r,shift right=.8ex] \arrow[d,"\unsure{w}","\sim"'] & \bar x \arrow[dl,very thick,"\sim"]\\
b \arrow[r] \arrow[urr,no head,shorten >=15pt] & y \arrow[ur,"\sim"'] &
\end{tikzcd}}
\diagram{\begin{tikzcd}y & {} \arrow[l]\end{tikzcd}}
\diagram{\begin{tikzcd}y \arrow[r,hook] & {}\end{tikzcd}}
$x$

\deleted{$\unsure{x}$}
\diagram{\begin{tikzcd} & {} \arrow[d]\\ {} \arrow[r,bend right=8] & {}\end{tikzcd}}
\deleted{$\unsure{x}$}
\diagram{\begin{tikzcd}a \arrow[r] & y \arrow[d]\\ & {}\end{tikzcd}}
\diagram{\begin{tikzcd}
x\ \mathrm{cof} \arrow[r,hook] \arrow[dr,hook] & y'\ \mathrm{cof} \arrow[r,"\sim"] \arrow[d,"\sim"'] & y\ \mathrm{cof}\\
& \bar y \arrow[ur,"\sim"] & {} \arrow[l,dashed]
\end{tikzcd}}
\diagram{\begin{tikzcd}
x & {} \arrow[dl,no head] & y &\\
y'\ \mathrm{cof} \arrow[r,very thick,"\sim"] \arrow[dr,"?"'] \arrow[ddd,bend right=10] & \bar y \arrow[ur] \arrow[dr,very thick] &&\\
& \bar y_1 \arrow[r] & y_1 &\\
&&&\\
y_2&&&
\end{tikzcd}}
\diagram{\begin{tikzcd}
x \arrow[dr] && y \arrow[dl,"\sim"'] \arrow[dr,"\sim"] \arrow[dd,"\sim"] &\\
& y' \arrow[dr,bend right=25,"\deleted{\unsure{g}}"'] && y''\\
&& y''' \arrow[ul,bend left=15,"\sim"'] \arrow[ur,"\sim"'] &
\end{tikzcd}}
\diagram{\begin{tikzcd}
\bar y \arrow[r,"\sim"] \arrow[d,"\sim"'] & y' \arrow[dl,bend left=28]\\
y'' \arrow[ur,very thick] &
\end{tikzcd}}
\diagram{\begin{tikzcd}x \arrow[r] & y'\end{tikzcd}}
\diagram{\begin{tikzcd}
& \unsure{\varnothing} \arrow[r,hook] \arrow[d,dashed] & y \arrow[d] \arrow[dl]\\
\unsure{x\amalg x'} \arrow[r,hook] & \tilde y \arrow[r,"\sim"] \arrow[d,very thick] & \bar y \arrow[dl,bend left=12]\\
& \tilde y' \arrow[ur,bend right=10] &
\end{tikzcd}}
\diagram{\begin{tikzcd}
\deleted{\unsure{x}} & y \arrow[d]\\
x \arrow[r,shift left=.7ex] \arrow[r,shift right=.7ex] & \bar y
\end{tikzcd}}
\diagram{\begin{tikzcd}&&y \arrow[d]\\ x \arrow[r,hook] & \bar y' \arrow[r,"\sim"'] & \bar y\end{tikzcd}}
\diagram{\begin{tikzcd}&&& y \arrow[d,very thick,"\sim"]\\ x\amalg x \arrow[r,hook] & \deleted{\unsure{x\amalg x}} \arrow[r,hook] & \bar y' \arrow[r,very thick,"\sim"'] & \bar y\end{tikzcd}}
\figure{\begin{tikzpicture}[x=.25cm,y=.25cm]
\draw (0,9) .. controls (5,10.6) and (12.8,15.8) .. (17,18);
\draw (2.6,0) .. controls (10.3,4.3) and (19.8,13.3) .. (27,16.8);
\end{tikzpicture}}
\mspage{2}
"""
elements=[('text','printed top left','DATA SET UTILITY - GENERATE'),('text','printed top right','PAGE 0001'),('text','printed second line','IEB352I WARNING : OUTPUT RECFM/LRECL/BLKSIZE COPIED FROM INPUT'),('text','printed third line','PROCESSING ENDED AT EOD')]
names=['x x-prime y y; weak equivalences','x y y-prime y-double-prime y-triple-prime','x y bar-y bar-y-prime bar-y-double-prime','three rows x bar-y y','isolated right arrow','unlabelled three-by-three array','x hooked arrow to empty end','x arrow y','x three arrows to y and empty endpoint','x two arrows y; u','y y1-prime y2-prime bar-y and two x','three separate rows x-f-y x-bar-y-y x-g-y','x y y / x bar-y y / x y y','x parallel f,g y down bar-y','isolated opposed arrow','x weak arrow y and unlabelled lower vertex','x vee x, C, y vee y, y; overwritten right part','x j1,j2 C h y','a y and overwritten lower object; empty right vertices','isolated x-dot and x','a a bar-x / b y','y left arrow','y hooked right arrow','unlabelled curved and vertical arrows','a y downward arrow','cof x,y-prime,y and bar-y','y-prime bar-y bar-y1 y1 y2','x y y-prime y-double-prime y-triple-prime','bar-y y-prime y-double-prime','x y-prime','empty object y tilde-y bar-y tilde-y-prime','x double arrow bar-y and y above','x bar-y-prime bar-y and y above','x coproduct x, overwritten x coproduct x, bar-y-prime bar-y']
for i,n in enumerate(names,1):elements.append(('diagram',f'sketch {i:02}, top-to-bottom reading order',n))
elements += [('text','middle lower','isolated x'),('drawing','crossing sheet diagonally','two long diagonal strokes'),('text','bottom left','2')]
notes='''Reused typed sheet: the printout bears “PAGE 0001”, not a manuscript page-count claim. Handwritten number 2 at foot. Almost entirely trial diagrams for weak equivalences, roofs, coproducts, and comparison; incomplete diagrams are preserved without supplying missing objects. Two long diagonal strokes cross the sheet. No explicit verbal conjecture or proof on this sheet.'''
if __name__=='__main__':save(106,3,tex,elements,kind='reused_typed',notes=notes)
