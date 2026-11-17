import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(211,r'''\scanpage{211}
\[a,b,c,d,a'\deleted{\unsure{=a+\alpha}};u\]
\[\alpha=a'-a\]
\margin{\unsure{les sommes} sur les arêtes de chacune des faces}
\[S_1=a+b+c+d\]
\[S'_1=a+b+c+d+4(a'-a)=-3a+b+c\inserted{+d}+4a'\]
\[S_2=\uline a+\uline u+\uline{a'}+\uline u+(\uline d-\uline b)
 =a-b+\cdot+d+a'+2u\]
\[\begin{aligned}
S'_2={}&\uline c+\uline u+\uline c-\uline a+\uline c+
\overset{\inserted{a'-a}}{\unsure{\alpha}}
 +\uline u-\uline d+\uline b+\uline c-\uline a\\
={}&-3a+b+\unsure{4|\deleted3\inserted4}c-d+a'+2u
\end{aligned}\]
\[S_3=\uline u+\uline d+\uline{a'}-\uline a+\uline u+\uline c-\uline a+\uline d
 =-2a+\cdot+c+2d+a'+2u\]
\[S'_3=\uline b+\uline u-\uline d+\uline b+\uline b+\uline{a'}-\uline a
 +\uline u-\uline d+\uline b+\uline c-\uline a
 =-2a+4b+c-2d+a'+2u\]
\[
\begin{array}{c}
\begin{array}{rrrrrr}a&b&c&d&a'&u\end{array}\\[.7em]
\begin{pmatrix}
1&1&1&1&0&0\\
-3&1&1&1&4&0\\
1&-1&0&1&1&2\\
-3&1&4&-1&1&2\\
-2&0&1&2&1&2\\
-2&4&1&-2&1&2
\end{pmatrix}
\end{array}
\]
\[\begin{aligned}
\Delta={}&\det\begin{pmatrix}
1&1&1&4&0\\-1&0&1&1&2\\1&4&-1&1&2\\0&1&2&1&2\\4&1&-2&1&2
\end{pmatrix}
-\det\begin{pmatrix}
-3&1&1&4&0\\1&0&1&1&2\\-3&4&-1&1&2\\-2&1&2&1&2\\-2&1&-2&1&2
\end{pmatrix}\\
&+\det\begin{pmatrix}
-3&1&1&4&0\\1&-1&1&1&2\\-3&1&-1&1&2\\-2&0&2&1&2\\-2&4&-2&1&2
\end{pmatrix}
-\det\begin{pmatrix}
-3&1&1&4&0\\1&-1&0&1&2\\-3&1&4&1&2\\-2&0&1&1&2\\-2&4&1&1&2
\end{pmatrix}
\end{aligned}\]
\margin{210}
''',[
('display','upper left','a,b,c,d,a prime;u'),('deletion','parameter list','a prime=a+alpha'),('display','upper left','alpha=a prime-a'),('margin note','upper middle','les sommes sur les aretes de chacune des faces'),('display','left first line','S_1=a+b+c+d'),('display','left second line','S_1 prime=a+b+c+d+4(a prime-a)'),('insertion','above end second line','+d'),('display','left third line','S_2'),('display','left fourth and fifth lines','S_2 prime'),('insertion','above alpha in S_2 prime','a prime-a'),('display','left sixth line','S_3'),('display','left seventh line','S_3 prime'),('display','upper right','six by six matrix with columns a,b,c,d,a prime,u'),('display','bottom','Delta four five by five determinants'),('margin note','lower left','210')],
[('top caption','les sommes','first two words reduced to connected strokes','low'),('crossed parameter clause','=a+alpha','very heavy overstrike','low'),('S_2 prime coefficient','4c','digit 4 retraced over possible3','medium'),('S_2 prime alpha','alpha with a prime-a written above','curved callout could indicate replacement, no confident cancellation inferred','medium')],
['Face-sum linear map written as explicit6x6 integer matrix. Determinant expansion left to continuation.','The S2 formula uses +(d-b), despite the preceding cube page using v=u-(d-b); preserve and examine discrepancy after freeze.'],sheet_kind='reused_typed')
