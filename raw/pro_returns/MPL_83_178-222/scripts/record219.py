import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(219,r'''\scanpage{219}
\[\begin{aligned}
&\det\left(\begin{array}{c|ccc|ccc|}
\multicolumn{1}{c}{}&\multicolumn{1}{c}{a}&\multicolumn{1}{c}{b}&\multicolumn{1}{c}{c}&\multicolumn{1}{c}{a'}&\multicolumn{1}{c}{b'}&\multicolumn{1}{c}{c'}\\\cline{2-7}
&\unsure{-1}&2&2&1&0&0\\
&2&-1&2&0&1&0\\
&2&2&-1&0&0&1\\\cline{2-7}
&1&0&0&-1&2&2\\
&0&1&0&2&-1&2\\
&0&0&1&2&2&-1\\\cline{2-7}
\end{array}\right)
=\det\begin{pmatrix}27&1\\1&27\end{pmatrix}\\
&=27^2-1\in\mathbb Q^*\\
&=(3^3)^2-1=3^6-1\\
&=728\\
&=8.91\\
&\boxed{=2^3.7.13}
\end{aligned}\]
\uline{premier à $3$}
\[-1+8+8-(-4-4-4)=16+12-1=27\]
\unsure{OK}
\[\deleted{\unsure{27}}\]
\diagram{\begin{array}{rrr}
&2&7\\
&2&7\\\hline
1&8&9\\
5&4&\\\hline
7&2&9
\end{array}}
\margin{218}
''',[
('display','upper left','six by six block determinant, headers a,b,c,a prime,b prime,c prime'),('display','upper right','det(27,1;1,27)=27 squared-1'),('text','middle right','premier a3'),('display','middle left','-1+8+8-(-4-4-4)=27'),('text','middle right','OK'),('deletion','lower left','27'),('diagram','lower middle','vertical multiplication27 by27'),('margin note','lower left','218')],
[('first matrix entry','-1','vertical digit blackened','medium'),('lower-left cancelled number','27','crossed strokes','low'),('isolated approval','OK','K has V-shaped second stroke','medium')],
['Author equates 6x6 block determinant to determinant of 2x2 matrix of block determinants, obtaining728=2^3*7*13 and coprime3. This reduction should be checked, not accepted.','Possible own lead: block A=-3I+2J has A squared=9I, suggesting determinant512 rather than728; verify only after freeze.'],sheet_kind='reused_typed')
