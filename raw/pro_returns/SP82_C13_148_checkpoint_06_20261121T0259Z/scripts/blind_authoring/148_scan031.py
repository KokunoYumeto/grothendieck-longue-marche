"""Independent visual second reading of scan031.

Only the assigned image/box list and full fixed crops were reading inputs.
This script is an authoring record; it performs no recognition or comparison.
"""
import csv
import json
import os
import re
import tempfile
from pathlib import Path

BASE = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148')
INPUT = Path('/workspace/scratch/8132fe1cca43/work/blind_inputs/148_scan031/boxes.tsv')
DISPLAY = Path('/workspace/scratch/8132fe1cca43/work/blind_display/148_scan031')
with INPUT.open(newline='') as f:
    boxes = list(csv.DictReader(f, delimiter='\t'))
B = {int(r['box'][-3:]): tuple(int(r[k]) for k in ('x0','y0','x1','y1')) for r in boxes}

# Each drawing is described in its own fixed crop's coordinates, 0--10 on
# each axis, with y increasing down the displayed crop. Thick patches are
# filled paths, not inferred directional arrows.
S = {}
S[35] = r'''
\draw[gray] (1.0,5.0) .. controls (1.2,1.8) and (3.6,.1) .. (5.4,.5) .. controls (8.4,.4) and (9.0,2.3) .. (9.0,5.2) .. controls (9.0,8.7) and (7.2,9.7) .. (5.0,9.7) .. controls (2.3,9.6) and (.8,8.1) .. (1.0,5.0);
\draw[gray] (1.3,7.0) .. controls (1.7,9.8) and (7.9,10.7) .. (8.7,7.3);
\draw[gray] (1.2,6.9) .. controls (1.4,8.1) and (2.1,8.5) .. (3.0,8.4);
\draw[edge,dashed] (1.0,5.1) .. controls (2.2,3.9) and (6.8,3.8) .. (8.9,5.1);
\draw[edge] (1.0,5.1) .. controls (.5,6.9) and (9.6,7.0) .. (8.9,5.1);
\foreach \p in {(1.9,5.9),(5.3,6.4),(7.9,5.9),(3.6,4.3),(6.5,4.4)} {\fill[red!60!black] \p circle (.22);\fill[black] \p circle (.12);}
'''
S[36] = r'''
\draw[gray] (1.0,5.0) .. controls (1.2,1.4) and (4.9,-.1) .. (6.4,.7) .. controls (9.6,1.0) and (10.0,4.1) .. (9.2,6.8) .. controls (8.4,9.1) and (6.4,10.0) .. (4.2,9.5) .. controls (1.8,9.2) and (.6,7.5) .. (1.0,5.0);
\draw[gray] (1.1,6.0) .. controls (1.6,8.8) and (5.6,9.9) .. (8.9,7.5);
\draw[edge,dashed] (.9,5.0) .. controls (2.4,3.8) and (7.4,3.8) .. (9.5,5.1);
\draw[edge] (.9,5.0) .. controls (.6,6.6) and (9.2,7.0) .. (9.5,5.1);
\draw[edge] (6.0,1.0) .. controls (2.1,1.0) and (1.7,5.6) .. (2.8,8.3) .. controls (3.4,9.6) and (4.3,9.8) .. (4.9,9.5);
\draw[edge] (6.0,1.0) .. controls (9.8,.9) and (9.2,7.2) .. (6.9,9.2) .. controls (6.2,10.0) and (5.7,10.0) .. (4.9,9.5);
\draw[edge,dashed] (6.0,1.0) .. controls (6.1,3.5) and (5.5,4.3) .. (6.0,6.0) .. controls (5.9,7.8) and (5.2,8.8) .. (4.9,9.5);
\foreach \p in {(6.0,1.0),(2.4,6.0),(8.2,6.2),(5.9,4.2),(4.9,9.5)} {\fill[red!60!black] \p circle (.23);\fill[black] \p circle (.12);}
'''
S[37] = r'''
\draw[gray] (.5,5.1) .. controls (.6,2.0) and (2.6,.5) .. (4.3,.8) .. controls (6.4,.5) and (8.1,2.3) .. (8.0,5.2) .. controls (8.2,8.8) and (6.4,9.9) .. (4.1,9.8) .. controls (1.3,9.8) and (.1,7.5) .. (.5,5.1);
\draw[gray] (.7,6.5) .. controls (1.0,9.0) and (4.0,10.3) .. (6.2,9.1);
\draw[edge,dashed] (.4,5.2) .. controls (2.0,3.7) and (5.6,3.8) .. (8.0,5.1);
\draw[edge] (.4,5.2) .. controls (-.1,6.4) and (8.1,6.9) .. (8.0,5.1);
\draw[edge] (4.1,.9) .. controls (1.8,1.1) and (1.2,3.6) .. (1.3,5.9);
\draw[edge] (4.1,.9) .. controls (6.1,1.0) and (6.5,3.6) .. (6.0,5.9);
\draw[edge,dashed] (4.1,.9) .. controls (2.8,1.4) and (3.1,3.4) .. (2.9,4.1);
\draw[edge,dashed] (4.1,.9) .. controls (6.6,-.2) and (7.3,2.0) .. (7.2,4.4);
\foreach \p in {(4.1,.9),(1.3,5.9),(6.0,6.1),(2.9,4.1),(7.2,4.4)} {\fill[red!60!black] \p circle (.20);\fill[black] \p circle (.11);}
\draw[edge,->] (8.6,5.3) .. controls (9.6,4.7) and (9.1,4.3) .. (8.7,4.3);
'''
S[38] = r'''
\draw[gray] (.9,5.0) .. controls (1.2,1.6) and (4.9,.2) .. (6.0,.7) .. controls (8.6,.8) and (9.2,2.7) .. (9.1,5.2) .. controls (9.3,8.7) and (6.9,9.8) .. (4.2,9.7) .. controls (1.4,9.2) and (.7,7.6) .. (.9,5.0);
\draw[gray] (1.1,4.0) .. controls (1.3,1.5) and (4.9,.6) .. (5.7,.7) .. controls (5.3,4.0) and (5.1,8.0) .. (4.6,9.6);
\draw[edge,dashed] (.9,5.2) .. controls (2.2,4.0) and (7.6,4.3) .. (9.0,5.1);
\draw[edge] (.9,5.2) .. controls (.4,6.5) and (9.6,6.9) .. (9.0,5.1);
\draw[rededge] (5.6,.7) .. controls (6.1,1.5) and (5.7,4.6) .. (5.7,6.1) .. controls (5.6,8.4) and (5.0,10.0) .. (4.4,9.7);
\draw[rededge,dashed] (5.6,.7) .. controls (3.8,.5) and (4.8,7.4) .. (4.4,9.7);
\foreach \p in {(1.7,5.9),(4.7,6.3),(7.8,6.0),(3.0,4.4),(6.9,4.5)} {\fill[red!60!black] \p circle (.20);\fill[black] \p circle (.09);}
\fill (4.0,4.4)--(4.6,4.1)--(4.7,4.7)--cycle;
\fill (5.5,5.9)--(5.9,6.1)--(5.8,6.5)--(5.4,6.4)--cycle;
\node at (1.4,7.0) {$P$};\node at (4.8,7.2) {$\beta$};\node at (7.9,7.0) {$\beta'$};
\node at (3.1,3.4) {$\alpha$};\node at (7.5,3.6) {$\alpha'$};
'''
S[39] = r'''
\draw[gray] (1.9,5.4) .. controls (2.0,1.5) and (5.4,.7) .. (6.5,1.1) .. controls (9.4,1.1) and (9.4,5.3) .. (8.1,8.1) .. controls (6.5,10.3) and (2.4,9.7) .. (1.9,5.4);
\draw[edge,dashed] (2.0,5.2) .. controls (3.2,3.9) and (7.6,3.6) .. (9.0,5.1);
\draw[edge] (2.0,5.2) .. controls (1.6,6.3) and (8.6,6.9) .. (9.0,5.1);
\draw[rededge] (6.3,1.0) .. controls (7.3,1.8) and (6.8,7.9) .. (5.3,9.4);
\draw[rededge,dashed] (6.3,1.0) .. controls (3.9,2.8) and (5.0,7.9) .. (5.3,9.4);
\draw[edge] (6.3,1.0) .. controls (8.8,.8) and (9.8,3.7) .. (8.8,6.8) .. controls (8.0,8.3) and (6.5,9.3) .. (5.3,9.4);
\foreach \p in {(2.3,5.4),(4.1,4.3),(5.0,6.0),(8.9,2.7),(8.3,7.1)} {\fill[red!60!black] \p circle (.18);}
\draw[line width=1.25pt] (.8,5.6)--(4.5,.8) (1.6,4.6)--(5.6,.5) (2.2,5.8)--(6.3,1.0) (3.3,6.8)--(7.4,1.5) (4.6,7.3)--(9.2,2.0) (5.6,8.2)--(9.7,3.1) (6.4,8.7)--(9.4,5.8) (7.0,9.2)--(9.2,6.3);
\node at (1.1,6.9) {$1$};
'''
S[40] = r'''
\draw[gray] (1.0,4.8) .. controls (1.0,1.7) and (3.8,.1) .. (5.5,.5) .. controls (8.3,.5) and (9.0,4.1) .. (8.3,6.9) .. controls (7.3,9.7) and (4.7,10.0) .. (2.3,8.2) .. controls (1.3,7.2) and (.7,5.8) .. (1.0,4.8);
\draw[gray,dashed] (1.0,4.6) .. controls (3.1,3.7) and (7.7,3.6) .. (8.7,4.4);
\draw[gray] (1.2,5.2) .. controls (3.4,6.5) and (7.0,6.2) .. (8.7,4.4);
\draw[rededge] (5.5,.5) .. controls (6.8,1.3) and (6.5,7.7) .. (4.1,9.4);
\draw[rededge,dashed] (5.5,.5) .. controls (2.8,1.1) and (3.9,8.3) .. (4.1,9.4);
\draw[edge,dashed] (1.0,4.3) .. controls (1.5,4.0) and (2.2,3.8) .. (2.6,3.9);
\draw[edge] (1.0,4.3) .. controls (.6,5.9) and (3.7,6.5) .. (5.8,6.3);
\draw[edge] (2.6,3.9)--(3.7,3.7);
\draw[edge] (5.5,.5) .. controls (7.1,.6) and (7.6,1.4) .. (8.0,2.4) .. controls (9.4,4.7) and (7.9,7.2) .. (7.0,8.0) .. controls (5.9,9.4) and (4.8,9.7) .. (4.1,9.4);
\foreach \p in {(1.4,5.4),(2.6,3.9),(4.1,6.3),(8.0,2.4),(7.0,8.0)} {\fill[red!60!black] \p circle (.20);\fill[black] \p circle (.09);}
\fill (3.3,3.9)--(3.8,3.3)--(3.8,4.1)--cycle;
\fill (5.6,6.0)--(6.0,6.1)--(5.9,6.7)--(5.5,6.5)--cycle;
\fill (5.1,.6)--(5.5,.2)--(5.9,.5)--cycle;\fill (3.8,9.4) circle (.15);
\draw[->,line width=.7pt] (7.5,1.2)--(7.3,.5);
\draw[->,line width=.7pt] (7.0,8.9)--(6.3,9.8);
\node at (.6,6.2) {$P$};\node at (2.7,3.1) {$\alpha$};\node at (4.3,7.4) {$\beta$};
\node at (8.8,1.9) {$\beta'$};\node at (7.8,8.7) {$\alpha'$};
'''
S[41] = r'''
\draw[gray] (.7,4.9) .. controls (1.2,1.3) and (4.9,-.1) .. (6.7,.8) .. controls (8.5,1.0) and (8.8,5.0) .. (7.2,7.8) .. controls (6.4,10.2) and (2.4,10.1) .. (1.0,7.5) .. controls (.6,6.8) and (.5,5.6) .. (.7,4.9);
\draw[gray] (.6,5.9) .. controls (.7,9.3) and (6.2,10.9) .. (7.4,7.5);
\draw[rededge,dashed] (.5,4.6) .. controls (2.3,3.7) and (6.7,4.0) .. (8.1,4.8);
\draw[rededge] (.5,4.6) .. controls (-.6,5.9) and (7.9,6.7) .. (8.1,4.8);
\draw[edge] (2.6,1.7) .. controls (4.0,-.1) and (6.0,.4) .. (6.8,1.3);
\draw[edge] (2.6,1.7) .. controls (1.3,3.5) and (1.1,7.0) .. (2.2,8.6);
\draw[edge,dashed] (6.8,1.3) .. controls (7.7,2.6) and (7.5,3.6) .. (7.5,4.6);
\draw[edge] (6.9,5.8) .. controls (6.7,7.4) and (6.3,8.1) .. (5.6,8.9);
\draw[edge,dashed] (7.5,4.6) .. controls (7.8,6.6) and (6.8,8.1) .. (5.6,8.9);
\draw[edge,dashed] (4.4,4.1) .. controls (4.0,5.6) and (3.9,7.0) .. (4.0,8.2);
\draw[edge,dashed] (2.2,8.6) .. controls (3.3,7.9) and (5.9,8.0) .. (6.4,8.7);
\draw[edge] (2.2,8.6) .. controls (1.0,9.0) and (6.8,9.6) .. (6.4,8.7);
\foreach \p in {(2.6,1.7),(6.8,1.3),(2.8,8.9),(4.0,8.2),(5.6,9.1)} {\fill[red!60!black] \p circle (.19);}
\foreach \p in {(1.5,5.4),(4.3,5.9),(6.9,5.8),(7.5,4.6),(4.4,4.1),(1.9,4.1)} {\fill \p circle (.13);}
\node at (3.5,2.0) {$1$};\node at (7.5,1.0) {$\infty$};\node at (2.8,9.7) {$0$};
\node at (4.8,7.8) {$\unsure{P|\rho}$};\node at (5.8,9.8) {$\overline{\unsure{P|\rho}}$};
\draw[line width=.8pt] (4.5,7.0)--(5.0,7.1) (4.6,7.3)..controls (5.2,7.3) and (5.2,7.8)..(4.5,8.1);
\draw[line width=.7pt] (5.3,9.2)..controls (6.4,9.1) and (6.5,8.7)..(5.9,8.7);
\node at (2.4,5.3) {$u_0$};\node at (4.8,5.6) {$u_1$};\node at (6.7,5.4) {$u_2$};
\node at (8.4,4.5) {$u_3$};\node at (4.9,3.7) {$u_4$};\node at (2.7,3.7) {$u_5$};
\fill (3.1,8.1)--(3.8,7.9)--(3.8,8.4)--cycle;
\node at (.2,7.9) {$3$};\node at (2.4,.0) {$1$};
'''
S[42] = r'''
\draw[gray] (.8,5.1) .. controls (1.4,1.7) and (4.0,.5) .. (6.2,.8) .. controls (9.1,.8) and (9.8,3.0) .. (9.3,6.0) .. controls (8.8,8.6) and (6.0,10.0) .. (4.3,9.7) .. controls (1.6,9.5) and (.5,7.5) .. (.8,5.1);
\draw[gray] (.9,6.4) .. controls (1.4,8.5) and (3.0,9.5) .. (4.2,9.8);
\draw[edge,dashed] (.8,5.1) .. controls (2.8,4.0) and (7.2,4.0) .. (9.3,5.2);
\draw[edge] (.8,5.1) .. controls (.3,6.9) and (9.1,7.0) .. (9.3,5.2);
\draw[rededge] (4.4,1.0) .. controls (3.3,1.5) and (3.5,8.7) .. (4.2,9.8);
\draw[rededge,dashed] (4.4,1.0) .. controls (5.0,2.4) and (4.9,8.4) .. (4.2,9.8);
\draw[rededge] (6.7,.9) .. controls (7.7,2.2) and (7.0,8.8) .. (6.1,9.7);
\draw[rededge,dashed] (6.7,.9) .. controls (5.6,1.4) and (5.5,8.9) .. (6.1,9.7);
\foreach \p in {(1.8,6.1),(5.3,6.5),(8.6,5.9),(3.2,4.4),(6.5,4.5)} {\fill[red!60!black] \p circle (.17);}
\fill (3.5,6.3)--(3.9,6.1)--(3.9,6.6)--cycle;
\fill (6.8,6.2)--(7.2,6.0)--(7.3,6.5)--cycle;
\fill (4.6,4.2)--(4.9,4.3)--(4.8,4.6)--(4.5,4.4)--cycle;
\fill (5.7,4.2)--(6.2,4.3)--(6.0,4.7)--(5.6,4.5)--cycle;
\node at (5.3,7.4) {$P$};
'''
S[43] = r'''
\draw[gray] (1.5,5.0) .. controls (1.5,2.0) and (4.3,1.1) .. (6.0,1.5) .. controls (8.5,1.5) and (9.2,3.6) .. (8.9,5.7) .. controls (8.5,8.5) and (6.8,9.7) .. (4.4,9.1) .. controls (2.0,8.7) and (1.4,7.3) .. (1.5,5.0);
\draw[rededge,dashed] (2.0,3.3) .. controls (4.0,2.6) and (7.5,4.1) .. (8.8,4.9);
\draw[rededge] (2.0,3.3) .. controls (3.0,4.5) and (8.9,5.8) .. (8.8,4.9);
\draw[rededge,dashed] (2.2,7.8) .. controls (4.4,6.1) and (7.7,5.7) .. (8.8,5.9);
\draw[rededge] (2.2,7.8) .. controls (3.8,8.3) and (8.5,6.9) .. (8.8,5.9);
\draw[edge] (2.0,3.3) .. controls (1.2,4.2) and (1.2,6.2) .. (2.2,7.8) .. controls (3.2,9.6) and (6.7,9.7) .. (8.0,8.0) .. controls (8.7,7.2) and (9.2,5.3) .. (8.8,4.9);
\draw[edge] (4.8,4.5) .. controls (5.2,3.0) and (5.5,1.7) .. (6.0,1.5);
\draw[edge,dashed] (6.0,1.5) .. controls (6.5,2.4) and (6.0,3.3) .. (6.0,3.7);
\foreach \p in {(1.5,5.4),(4.5,9.1),(8.0,8.0),(5.2,2.7),(6.2,2.3)} {\fill[red!60!black] \p circle (.18);\fill[black] \p circle (.09);}
\foreach \p in {(2.0,3.3),(4.8,4.5),(6.0,3.7),(8.8,4.9),(8.8,5.9),(2.2,7.8)} {\fill \p circle (.11);}
\node at (2.2,5.5) {$0$};\node at (4.3,9.8) {$1$};\node at (8.5,8.6) {$\infty$};
\node at (4.4,2.5) {$\unsure{P|\rho}$};\node at (6.8,2.4) {$\overline{\unsure{P|\rho}}$};
'''
S[44] = r'''
\draw[gray] (1.7,5.0) .. controls (2.0,1.5) and (4.7,.3) .. (6.8,.6) .. controls (9.3,1.0) and (9.3,4.2) .. (8.7,6.4) .. controls (8.1,8.8) and (5.5,9.9) .. (3.8,9.0) .. controls (1.9,8.1) and (1.6,7.1) .. (1.7,5.0);
\draw[gray] (1.9,4.8) .. controls (4.3,3.9) and (6.5,3.9) .. (9.0,5.1);
\draw[gray,dashed] (1.9,4.8) .. controls (2.0,5.8) and (4.3,6.5) .. (6.9,5.9);
\draw[rededge] (4.5,.9) .. controls (3.3,2.3) and (3.2,8.0) .. (3.9,9.1);
\draw[rededge,dashed] (4.5,.9) .. controls (5.1,3.6) and (5.1,8.5) .. (3.9,9.1);
\draw[rededge] (6.9,.8) .. controls (8.2,2.5) and (7.1,8.7) .. (6.0,9.2);
\draw[rededge,dashed] (6.9,.8) .. controls (5.5,2.2) and (5.3,8.2) .. (6.0,9.2);
\draw[edge] (4.5,.9) .. controls (1.4,2.1) and (.8,6.9) .. (2.5,8.0) .. controls (2.9,8.7) and (3.4,9.2) .. (3.9,9.1);
\draw[edge] (3.4,5.7)--(5.1,6.0)--(7.0,6.0) .. controls (8.8,5.9) and (9.5,5.5) .. (9.0,5.1) .. controls (8.6,4.7) and (7.7,4.6) .. (6.8,4.3);
\draw[edge] (4.8,4.2)--(5.9,4.3);
\foreach \p in {(3.3,1.8),(2.5,8.0),(5.1,6.0),(8.0,5.7),(6.8,4.3)} {\fill[red!60!black] \p circle (.18);}
\foreach \p in {(4.5,.9),(3.4,5.7),(3.9,9.1),(7.0,6.0),(4.8,4.2),(5.9,4.3)} {\fill \p circle (.13);}
\fill (4.8,4.1)--(5.4,4.3)--(5.3,4.5)--(4.8,4.4)--cycle;
\node at (2.8,.9) {$P$};\node at (1.8,8.7) {$\overline P$};\node at (5.1,6.8) {$0$};\node at (8.0,6.5) {$1$};\node at (7.9,4.0) {$\infty$};
'''
S[45] = r'''
\draw[gray] (1.5,5.0) .. controls (1.7,2.0) and (4.6,.6) .. (6.8,1.0) .. controls (9.3,1.8) and (9.2,4.7) .. (8.6,6.7) .. controls (7.9,9.9) and (4.5,10.1) .. (2.6,8.3) .. controls (1.5,7.4) and (1.3,6.1) .. (1.5,5.0);
\draw[gray] (2.2,2.5) .. controls (3.8,.9) and (6.1,.3) .. (6.9,.4);
\draw[gray] (1.8,6.9) .. controls (2.5,8.9) and (4.2,9.9) .. (5.3,9.5);
\draw[rededge,dashed] (2.3,2.2) .. controls (4.3,1.9) and (7.4,3.6) .. (8.7,4.9);
\draw[rededge] (2.3,2.2) .. controls (3.2,3.8) and (8.8,5.8) .. (8.7,4.9);
\draw[rededge,dashed] (1.9,7.2) .. controls (4.6,5.9) and (7.7,5.9) .. (8.7,6.1);
\draw[rededge] (1.9,7.2) .. controls (3.3,8.6) and (8.3,7.4) .. (8.7,6.1);
\draw[edge] (2.3,2.2) .. controls (1.1,3.3) and (1.0,6.3) .. (1.9,7.2);
\draw[edge] (8.7,4.9) .. controls (9.0,5.3) and (8.9,5.8) .. (8.7,6.1);
\draw[edge] (4.8,3.9) .. controls (5.5,3.3) and (5.6,1.6) .. (6.5,1.1) .. controls (6.9,.7) and (7.0,1.2) .. (6.9,1.9);
\draw[edge,dashed] (6.9,1.9)--(6.4,3.7);
\draw[edge] (4.8,7.6)--(5.1,8.9) .. controls (5.8,10.2) and (6.6,9.5) .. (6.6,8.9);
\draw[edge,dashed] (6.6,8.9)--(6.7,7.8)--(6.4,6.2);
\foreach \p in {(1.5,5.0),(5.6,2.2),(6.9,2.0),(5.1,8.9),(6.7,7.8)} {\fill[red!60!black] \p circle (.18);}
\foreach \p in {(2.3,2.2),(4.8,3.9),(6.4,3.7),(8.7,4.9),(8.7,6.1),(6.4,6.2),(4.8,7.6),(1.9,7.2)} {\fill \p circle (.12);}
\node at (.7,5.1) {$P$};\node at (5.0,1.8) {$\alpha$};
\node at (7.8,1.9) {$\deleted{\unsure{\beta'}}\inserted{\alpha'}$};
\node at (4.4,8.9) {$\deleted{\unsure{\alpha}}\inserted{\beta}$};
\node at (7.4,7.9) {$\deleted{\unsure{\alpha'}}\inserted{\beta'}$};
'''
S[46] = r'''
\draw[gray] (.7,5.4) .. controls (.8,2.8) and (3.1,1.2) .. (5.4,1.4) .. controls (7.8,1.5) and (8.0,4.0) .. (7.7,6.4) .. controls (7.3,8.7) and (5.0,9.8) .. (2.8,9.0) .. controls (1.3,8.5) and (.5,6.8) .. (.7,5.4);
\draw[gray] (.7,6.6) .. controls (.9,8.5) and (2.4,9.5) .. (3.1,9.4);
\draw[gray] (6.1,1.7) .. controls (7.2,1.8) and (7.7,2.3) .. (7.9,2.6);
\draw[rededge] (3.2,1.6) .. controls (2.3,2.9) and (2.1,7.8) .. (2.8,9.0);
\draw[rededge,dashed] (3.2,1.6) .. controls (4.1,3.3) and (3.5,7.7) .. (2.8,9.0);
\draw[rededge] (5.4,1.4) .. controls (4.5,2.3) and (4.0,8.0) .. (4.6,9.2);
\draw[rededge,dashed] (5.4,1.4) .. controls (6.6,3.0) and (5.5,8.8) .. (4.6,9.2);
\draw[edge] (3.2,1.6) .. controls (4.0,1.1) and (4.9,1.3) .. (5.4,1.4);
\draw[edge] (2.8,9.0) .. controls (3.4,9.3) and (4.2,9.3) .. (4.6,9.2);
\draw[gray] (2.4,6.0)--(4.3,6.2);
\draw[gray] (3.6,4.6)--(5.7,4.7);
\draw[edge,dashed] (.7,5.4) .. controls (1.1,4.8) and (2.6,4.5) .. (3.6,4.6);
\draw[edge] (.7,5.4) .. controls (.2,6.1) and (2.0,6.2) .. (2.4,6.0);
\draw[line width=.5pt,dashed] (2.4,6.0)--(3.5,6.2);
\draw[edge] (4.3,6.2) .. controls (5.2,6.5) and (8.1,6.2) .. (7.7,5.3) .. controls (7.4,4.8) and (6.2,4.7) .. (5.7,4.7);
\foreach \p in {(4.4,1.3),(1.7,5.9),(5.0,6.2),(2.9,4.6),(6.4,4.8)} {\fill[red!60!black] \p circle (.20);}
\foreach \p in {(3.2,1.6),(5.4,1.4),(2.8,9.0),(4.6,9.2),(2.4,6.0),(4.3,6.2),(3.6,4.6),(5.7,4.7)} {\fill \p circle (.12);}
\node at (4.5,.4) {$P$};\node at (1.7,6.6) {$\alpha$};\node at (5.1,6.8) {$\alpha'$};\node at (3.1,3.9) {$\beta'$};\node at (7.1,4.5) {$\beta$};
\draw[edge,->] (8.2,5.8) .. controls (9.3,5.4) and (8.8,4.9) .. (8.3,4.9);
'''

STYLE = r'line cap=round,line join=round,edge/.style={black,line width=1.05pt},rededge/.style={red!65!black,line width=.85pt},every node/.style={font=\scriptsize,inner sep=.5pt}'

def figure(n):
    x0,y0,x1,y1=B[n]
    body=S[n]
    if n==39:
        # Actual diagonal cancellation strokes are drawn in the figure too.
        return '\\deleted{' + figure_body(body,x1-x0,y1-y0) + '}'
    return figure_body(body,x1-x0,y1-y0)

def figure_body(body,w=300,h=300):
    return ('\\figure{\\begin{tikzpicture}[x=%.4fcm,y=-%.4fcm,%s]\n' % (w/1000,h/1000,STYLE)
            + body.strip() + '\n\\end{tikzpicture}}')

def fragments(n, figures):
    """Clip drawing strokes to this already inspected fixed rectangle.

    Label nodes whose centers are outside this box are omitted; this never
    introduces the text of an unseen neighboring label into the reading.
    """
    x0,y0,x1,y1=B[n]
    result=[]
    for f in figures:
        a,b,c,d=B[f]
        if max(a,x0)>=min(c,x1) or max(b,y0)>=min(d,y1):
            continue
        body=S[f]
        def label(m):
            xx=a+float(m.group(1))*(c-a)/10
            yy=b+float(m.group(2))*(d-b)/10
            return m.group(0) if x0<=xx<=x1 and y0<=yy<=y1 else ''
        body=re.sub(r'\\node at \(([-.\d]+),([-.\d]+)\) \{.*?\};',label,body)
        result.append('\\begin{scope}[shift={(%d,%d)},xscale=%.5f,yscale=%.5f]\n%s\n\\end{scope}' % (a-x0,b-y0,(c-a)/10,(d-b)/10,body))
    if not result:
        return ''
    return ('\\figure{\\begin{tikzpicture}[x=.006cm,y=-.006cm,%s]\n\\clip (0,0) rectangle (%d,%d);\n' % (STYLE,x1-x0,y1-y0)
            +'\n'.join(result)+'\n\\end{tikzpicture}}')

def cd(body, options=''):
    return r'\diagram{\begin{tikzcd}['+options+']\n'+body+'\n'+r'\end{tikzcd}}'

def up(a,b,label):
    return cd(a+r'\\'+b+r'\arrow[u,"'+label+"\"']", 'row sep=18mm')

def horizontal(a,b,label,below=False):
    return cd(a+r'\arrow[r,"'+label+('"\'' if below else '"')+r'] & '+b,'column sep=22mm')

R={}
R[1]=r'''12 structures pentagonales sur $K$
$\{\sigma,\sigma^{-1}\}\in\unsure{\Pi_2(\operatorname{Circ}(K)|\Pi_2\operatorname{Circ}(K)}$
$G\simeq D_5$
$\widetilde G\simeq D_5\times\{1,\sigma\}$
'''+up('5','', '')
R[2]=r'''20 structures $K=J\amalg$
avec $\omega\xrightarrow{\sim}\underline\omega(J)$
$G\simeq\widetilde G_J\simeq\unsure{\mathfrak S_3|G_3}$
$\widetilde G\simeq\unsure{\mathfrak S_3|G_3}\times\{1,\sigma\}$'''
R[3]=r'''30 structures carrés orientés
$K=\{P\}\amalg I$ \quad $I$ structure carrée \uline{orientée} $(Q,\omega)=\vec Q$
$I=\coprod_{\alpha\in\delta}\alpha$ \quad $\delta=$ ens. des diagonales de
$\omega\in\delta\wedge\bigwedge_{\alpha\in\delta}\alpha$
$G=\widetilde G=\mathbb Z/4\mathbb Z$
\unsure{che})'''
R[4]=r'''60 structures ``pentagone avec sommet'' sur $K$
i.e. $K\simeq\unsure{J}\amalg\omega$, avec $\omega\hookrightarrow J$
i.e. $P\in J$ et $\omega\xrightarrow{\sim}\omega'=\unsure{J}\setminus\{P\}$
$G\simeq\mathbb Z/2\mathbb Z$
$\widetilde G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}$'''
R[5]=r'''même paramétrage que $II_2$
$G\simeq\mathbb Z/2\mathbb Z,\quad\widehat G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}$'''+ '\n'+fragments(5,[40])
R[6]=r'''120 structures entièrement épinglées,
$G=\deleted{\unsure{\mathbb Z_2|\mathbb Z/2\mathbb Z}}=\{1\}$
$\widetilde G=\{1,\sigma\}$
$[K=J\amalg\unsure{\varepsilon}$
$\omega\in\underline\omega$
$\tau_r^0:$'''+ '\n'+fragments(6,[41])
R[7]=r'''$[K=J\amalg\varepsilon\quad\operatorname{card}J=3,\operatorname{card}\varepsilon=2$
$\omega\in\underline\omega(J),\quad r\in J\times\varepsilon$
'''+horizontal(r'II_1(J,\varepsilon)',r'II_1(u_\omega(r))',r'\tau_r^0')+r'''
où $u_\omega=\omega\times(-1)$ sur $J\times\varepsilon]$'''
R[8]=r'''60 structures ``pentagone avec sommet'' sur $K$,
$G=\mathbb Z/2\mathbb Z,\quad\widetilde G=\mathbb Z/2\mathbb Z\times\{1,\sigma\}$'''+ '\n'+fragments(8,[42])
R[9]=r'''$III_1$ (triple triangle semi-gauche)'''
R[10]=r'''120 structures épinglées
$G=1,\quad\widehat G=\{1,\sigma\}$'''+ '\n'+fragments(10,[43,44])
R[11]=r'''$III^{\unsure{\prime|1}}_2$ (triple triangle gauche)'''
R[12]=r'''60 structures de carré orienté à codiagonale, $K=\{P\}\amalg I$,
$I$ muni d'une \inserted{str.} carrée \unsure{en|à} codiagonale
$\delta=\{\{\alpha,\beta\},\{\alpha',\beta'\}\}$
i.e. d'un repère de $\unsure{\mathcal X}(I)$
$G=\mathbb Z/2\mathbb Z\deleted{\unsure{\varepsilon}},\quad\widetilde G\simeq\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}$'''+ '\n'+fragments(12,[45,46])
R[13]=r'''\uline{niveau 2} \quad $I_{10},I_6,I_4$ \quad $12+20+30=62$
\uline{niveau 1} \quad $II_2,II'_2,II_1$ \quad $60+60+120=240$
\uline{niveau 0} \quad $III_2,III_{\unsure{4|1}},III'_2$ \quad $\underline{60+120+60=240}$
\hfill $542$'''
R[14]=r'''(l'indice ``i'' indique l'ordre du $G=\operatorname{Aut}^{+}\unsure{\}|)}$, donc le nb de structures \deleted{est} $120/i$)
\uline{NB} Sauf $I_4$, toutes ces structures sont ``réelles''.'''
R[15]=r'''$\pi\in\operatorname{Pent}(K)$ \quad $B\in\operatorname{Bitet}(K)$
$s\in K$ \quad $\vec Q\in\overrightarrow{\operatorname{Carr}}(K)$
$\rho\in\operatorname{Rep}(\pi)$ \quad $r\in\operatorname{Rep}(K')$
\uline{NB} $\{(\pi,\rho)\}\unsure{\simeq}\operatorname{Rep}(K))$'''
R[16]=r'''\margin{\mspage{30}}'''
R[17]=horizontal('3','2',r'f_{B,s}')+r'''
$(B\in\operatorname{Bitet}(K),\ s\in T(B)=J)$'''

map18 = cd(r'''& &4\arrow[ddll,bend right=14,"f_{\vec Q,a,\unsure{\alpha}}"']\\
&3&6\\
2&{}\arrow[u,"\gamma'_{\pi,s}"']&{}\arrow[u]''','row sep=12mm,column sep=15mm')
R[18]=fragments(18,[36,37,39,40])+r'''
20 structures $K=J\amalg\omega$
avec $\omega\xrightarrow{\sim}\underline\omega(J)$
$G\simeq\widetilde G_J\simeq\unsure{\mathfrak S_3|G_3}$
$\widetilde G\simeq\unsure{\mathfrak S_3|G_3}\times\{1,\sigma\}$
'''+map18+r'''
$(Q=\overrightarrow{\operatorname{Carr}}(K),\ a\in A(Q))$
comp. avec $\widetilde G$
$(\pi\in\operatorname{Pent}(K),\ s\in K)$
$II'_2=\operatorname{Tw}_{1/4}II_2$
(carr.-triangle gauche)
4 sommets \deleted{\unsure{-repères|-repérés}}
$30$ \quad $I$
\unsure{droit})'''
R[19]=up('5','1',r'\gamma_{\pi,s}')+r'''
$(\pi\in\operatorname{Pent}(K),\ s\in K)$'''
R[20]=r'''2 sommets \deleted{-repère}
'''+horizontal('1','1',r'\tau_{\pi,s}=\operatorname{tw}_{1/4}')
R[21]=cd(r'''3&6\\{}\arrow[u,"\gamma'_{\pi,s}"']&\\&1\arrow[uu,"\gamma_r^{\unsure{0}}"']''','row sep=16mm,column sep=20mm')+r'''
comp. avec $\widetilde G$
$(\pi\in\operatorname{Pent}(K),\ s\in K)$
(carr.-triangle gauche)
\unsure{mmets} \deleted{\unsure{-repères}}
compat. avec $\widetilde G$
$I=\coprod_{\alpha}$ \quad $\omega\in$
'''+fragments(21,[40])
R[22]=up('2','2',r'\gamma_{\pi,\rho}')+r'''
$(\pi\in\operatorname{Pent}(K),\ \rho\in\operatorname{Rep}\pi)$'''
R[23]=r'''$\unsure{I}\quad\omega$
'''+horizontal('2','1',r'\tau_{\pi,\rho}=\operatorname{tw}_{1/4}',True)
map24 = cd(r'''2&&3\\
&&\\
1\arrow[uu,"\gamma_r^1"']&3\arrow[uur,"\gamma_r^{1'}"{description,draw,ellipse,inner sep=2pt},"!"']&''','row sep=8mm,column sep=12mm')
R[24]=r'''$\unsure{Z|2},\ \unsure{G}\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}$
'''+map24+r'''
$(r\in\operatorname{Rep}(\unsure{K'|K}))$
$120$ \quad épi
'''+fragments(24,[41])
loop25 = cd(r'''{}\arrow[dd,out=60,in=-60,looseness=3,"\tau_r^0=\operatorname{tw}_{1/6}"]\\\\{}''','row sep=10mm')
R[25]=loop25
R[26]=horizontal('1','2',r"\tau'_r")

big27 = cd(r'''2&&\\&&2\arrow[ull,out=-130,in=-50,looseness=3,"\gamma_r^2"']''','row sep=35mm,column sep=18mm')
R[27]=r'''même paramétrage que $II_2$
$G\simeq\mathbb Z/2\mathbb Z,\quad\widehat G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}$
'''+map24+r'''
$(r\in\operatorname{Rep}(\unsure{K'|K}))$
120 \unsure{stru} \quad \unsure{épingl}
$III_1$ (triple triangle semi-gauche)
$\unsure{I}\quad\omega$
'''+horizontal('2','1',r'\tau_{\pi,\rho}=\operatorname{tw}_{1/4}',True)+r'''
2+4 sommets-repère
'''+fragments(27,[39,40,41,43,44,45])+r'''
$=$
120 structures épinglées
$G=1,\quad\widehat G=\{1,\sigma\}$
'''+horizontal('1','',r"\tau'_r")+'\n'+big27+r'''
$\pi\in\operatorname{Pent}(K)\quad B\in\operatorname{Bitet}(K)$'''
R[27]+=r'''
$\sigma\}$ \quad $1,\sigma\}$
\unsure{mmets}-\unsure{re} \quad )'''
big28=cd(r'''2\\\\1\arrow[uu,out=100,in=0,looseness=2.5,"\gamma_r^{\unsure{2'|21}}"']''','row sep=30mm')
R[28]=big28+r'''
orientés
\unsure{structure}
\uline{orientée} $(Q,\omega)=\vec Q$
diagonales de
$\mathbb Z/4\mathbb Z$
\unsure{r.}-triangle)
\unsure{6} sommets-repères
'''+loop25+r'''
\unsure{ièrement}
$[K=J\amalg\varepsilon\quad\operatorname{card}J=3,\operatorname{card}\varepsilon=2$
$\omega\in\underline\omega(J),\quad r\in J\times\varepsilon$
'''+horizontal(r'II_1(J,\varepsilon)',r'II_1(u_\omega(r))',r'\tau_r^0')+r'''
où $u_\omega=\omega\times(-1)$ sur $J\times\varepsilon]$
$1\}$ \quad $\}$
\unsure{le} triangle gauche)'''
R[29]=figure_body(r'\draw[line width=.8pt] (6.0,3.0)--(6.2,6.5)--(4.5,6.4);\draw[line width=.5pt] (6.3,0)--(6.5,.3);',80,75)
R[30]=r'''2+2 sommets-repère'''
R[31]=r'''2+4 sommets-repère'''+ '\n'+fragments(31,[44])
R[32]=r'''4+4 sommets-repère'''
R[33]=r'''6 sommets-repères'''
R[34]=r'''4 sommets \deleted{\unsure{-repères|-repérés}}'''+ '\n'+fragments(34,[40])
for n in range(35,47):
    R[n]=figure(n)

R[47]=figure_body(r'''
\draw[gray,line width=.75pt] (5.6,8.5)--(1.7,2.8) (5.6,8.5)--(3.9,1.8) (5.6,8.5)--(6.1,1.6) (5.6,8.5)--(7.7,1.3) (5.6,8.5)--(9.3,1.1);
\fill (5.6,8.5) circle (.35);
''',105,125)
R[48]=figure_body(r'''
\draw[gray,line width=.8pt] (1.6,7.1)--(.5,2.5) (1.6,7.1)--(2.5,2.2) (1.6,7.1)--(4.0,2.2) (1.6,7.1)--(7.8,7.0) (7.8,7.0)--(7.1,2.0) (7.8,7.0)--(8.9,1.1);
\fill (1.6,7.1) circle (.35);\fill (7.8,7.0) circle (.35);
''',125,85)
R[49]=figure_body(r'''
\draw[line width=.8pt] (1.5,8.1)--(.9,1.3) (1.5,8.1)--(2.0,1.5) (1.5,8.1)--(5.4,7.6)--(8.7,7.2) (5.4,7.6)--(5.1,1.9) (8.7,7.2)--(7.5,1.6) (8.7,7.2)--(9.7,1.7);
\foreach \p in {(1.5,8.1),(5.4,7.6),(8.7,7.2)} {\fill \p circle (.30);}
''',153,108)
R[50]=figure_body(r'''
\draw[gray] (2.2,0)--(1.7,10);
\draw[line width=.7pt] (1.6,5.1)..controls (3.9,4.6) and (6.3,4.6)..(8.4,4.1);
\draw[line width=.7pt] (4.7,4.8)..controls (6.8,5.8) and (7.7,5.9)..(8.6,5.3);
\draw[gray] (2.4,4.7)--(2.7,3.8)--(3.3,4.6) (4.0,4.9)..controls (4.1,5.8) and (3.8,6.3)..(3.3,6.9);
\fill (8.2,3.8)--(8.5,4.2)--(8.2,4.7)--cycle;
\fill (8.3,5.2)--(8.7,5.0)--(8.5,5.8)--cycle;
''',175,65)
R[51]=figure_body(r'''
\draw[gray] (1.8,0)--(1.7,10);
\draw[line width=.8pt] (1.9,4.8)..controls (4.7,4.7) and (6.3,4.8)..(8.2,4.2);
\draw[line width=.8pt] (1.8,5.2)..controls (4.0,5.2) and (6.0,5.4)..(7.8,5.9);
\draw[line width=.8pt] (1.8,5.2)..controls (4.0,5.9) and (6.5,6.1)..(8.5,6.4);
\draw[gray] (1.5,4.3)--(2.4,2.9)--(2.5,4.0) (2.4,5.3)..controls (2.6,6.0) and (2.7,7.0)..(3.2,7.4);
\fill (8.2,6.1)--(8.7,6.4)--(8.2,6.7)--cycle;
''',150,75)
R[52]=figure_body(r'''
\draw[gray] (1.6,0)..controls (1.5,1.4) and (1.6,2.1)..(1.8,2.7);
\draw[line width=.75pt] (1.7,4.9)..controls (3.5,4.4) and (5.1,5.9)..(6.6,5.3)..controls (7.8,5.0) and (8.7,5.9)..(9.0,5.9);
\draw[gray] (1.8,5.1)--(2.2,5.8) (9.0,5.9)--(9.0,6.7);
''',160,78)
R[53]=r'''i.e. $P\in J$ et $\omega\xrightarrow{\sim}\omega'=\unsure{J}\setminus\{P\}$
$G\simeq\mathbb Z/2\mathbb Z$
$\widetilde G\simeq\mathbb Z/2\mathbb Z\times\{1,\sigma\}$
$\gamma_{\pi,\rho}$ \quad $\pi\in\operatorname{Pent}(K),\quad\rho\in\operatorname{Rep}\pi)$
'''+up('2','2','')+'\n'+up('2','1',r'\gamma_r^1')+r'''
$III_2$ (triple triangle droit)
$III_1$ (triple \unsure{tri}
2+2 sommets-repère
$\unsure{I}\quad\omega$
'''+horizontal('2','1',r'\tau_{\pi,\rho}=\operatorname{tw}_{1/4}',True)+'\n'+fragments(53,[42,43])+r'''
60 structures ``pentagone avec sommet'' sur $K$,
$G=\mathbb Z/2\mathbb Z,\quad\widetilde G=\mathbb Z/2\mathbb Z\times\{1,\sigma\}$
120 \unsure{structu}
$G=1,\quad\widehat G$
'''+cd(r'''{}\arrow[ddrr,no head,out=-90,in=180,draw=gray,"\gamma_r^2"']&&\\&&\\&&{}''','row sep=18mm,column sep=12mm')+r'''
$I_{10},I_6,I_4$ \quad $12+20+30=62$
$II_2,II'_2,II_1$ \quad $60+60+120=240$
$III_2,III_{\unsure{4|1}},III'_2$ \quad $\underline{60+120+60=240}$
\hfill $542$
$\pi\in\operatorname{Pent}(K)\quad B\in\operatorname{Bitet}(K)$
$s\in K\quad\vec Q\in\overrightarrow{\operatorname{Carr}}(K$
$\rho\in\operatorname{Rep}(\pi)$'''
R[53]+='\n'+figure_body(r'''
\draw[gray] (.2,3.8)..controls (.1,5.4) and (.2,6.6)..(.2,7.5);
\draw[line width=.5pt] (.2,7.8)..controls (.6,7.7) and (.8,8.0)..(1.1,7.9);
''',1230,1050)

def atomic_write(path, callback):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd, temporary=tempfile.mkstemp(prefix=path.name+'.',suffix='.tmp',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8',newline='') as f:
            callback(f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temporary,path)
    except BaseException:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise

def main():
    assert set(R)==set(range(1,54))
    for n,reading in R.items():
        assert isinstance(reading,str) and reading.strip(), n
    journal={
      'page':'148_scan031',
      'protocol':'Independent blind visual reading; no witness, first reading, approved page, other review, OCR, external research or TeX compilation used.',
      'fixed_crop_run':'scripts/blind_io.py crop 31, once',
      'failed_display_note':'One attempted batch030–037 was truncated; it did not count as viewed. Each was subsequently successfully displayed in smaller batches.',
      'views':[],
      'source_notes':[
        'All53 fixed crops were fully displayed successfully. No additional word-detail rectangles were created.',
        'The two additional native-color enlargements enlarged the entire saved fixed crop, without recropping or rotation.',
        'Crop053 contains face handwriting and drawings as well as pale reverse-side printing. Its face ink is transcribed; the reverse printing is excluded.',
        'Dark ambiguous tapered patches in drawings are filled geometry and have not been assigned inferred arrow directions.',
        'Unresolved ink is retained with diplomatic uncertainty, including the canceled group expression006, the group alphabet002/018, word/link012, index013, and overwritten labels041/045.',
        'The final raw label traces in045 appear alpha/alpha-prime above and beta/beta-prime below; uncertain underlying overwritten letters are retained as uncertain deletions.',
        'The large curve027 has a visible source count2 and target count2;028 has source1 and target2.',
        'No rotated display was needed.'
      ]}
    for row in boxes:
        n=int(row['box'][-3:])
        entry={'box':row['box'],'fixed_crop':f'crops/second/148_scan031/{row["box"]}.png','successful_displays':[str(DISPLAY/(row['box']+'.jpg'))],'rotation_degrees':0,'successfully_inspected':True}
        if n in (41,45):
            entry['successful_displays'].append(str(DISPLAY/(row['box']+'_native5.png')))
        if n==53:
            entry['observation']='Substantial face ink is in scope; pale reversed printing is show-through.'
        journal['views'].append(entry)
    def write_tsv(f):
        writer=csv.writer(f,delimiter='\t',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        writer.writerow(['box','reading'])
        for row in boxes:
            writer.writerow([row['box'],R[int(row['box'][-3:])].strip()])
    atomic_write(BASE/'second/148_scan031_second.tsv',write_tsv)
    atomic_write(BASE/'second/148_scan031_blind_journal.json',lambda f:json.dump(journal,f,ensure_ascii=False,indent=2))
    print('Atomically wrote53 independent readings and53 successful-view journal entries.')

if __name__=='__main__':
    main()
