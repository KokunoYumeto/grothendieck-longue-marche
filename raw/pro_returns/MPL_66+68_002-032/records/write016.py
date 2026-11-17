from record_page import record
record(16,r'''\scanpage{16}
% The manuscript is upside down in the supplied scan; reading order below follows the writing.
\deleted{``cellules'' des décompositions cellulaires ``à la Bruhat'' des espaces homogènes projectifs sous des groupes semi-simples. Le cas particulier des ``cycles de Schubert'' sur les variétés grassmanniennes permet justement de développer des conséquences d'intérêt général en topologie différentielle.}

\margin{$x^2=u$}
\[
\begin{aligned}
(V_1\dotplus\{x\})\ast(V_1\dotplus\{\unsure{x|u}\})
&=2V_1\dotplus\{u\}+2\{x\}\ast V_1\\
&=2G+\{u\}
\end{aligned}
\]
\diagram{\begin{array}{ccccc}
&&\inserted{V_1\dotplus\{x\}}&&\\
\{e\}&V_1&\deleted{\unsure{\{x\}\ast V_1}}&V_2&\\
&\multicolumn{2}{c}{\unsure{\longleftrightarrow}}&&
\end{array}}
\[
\deleted{2V_1+\unsure{u}}\qquad\boxed{3\ 2\ 2\ 2}
\]
\[
E\ast F\qquad\begin{array}{l}a+b=a'+b'\\(a-a')=(b'-b)\end{array}
\]
\[
a_1+a_2\qquad b_1+b_2
\]
\[
\deleted{a_1}\qquad a\qquad 0\ a\ \big/\ 0\ \deleted{\unsure{b+a}}\ a
\]
\[
\unsure{-}\qquad\deleted{0\quad a}\quad0\quad a,a\quad2a\qquad a\ne0
\]
\[
\deleted{2a\ne0}\qquad 2a=0
\]
\diagram{\begin{array}{cc}
\begin{array}{llll}1&1&1&1\\2&1&1&\end{array}&
\begin{array}{llll}2&2&&\\2&1&1&\\\deleted{\unsure{2|4}}&1&1&1\end{array}
\end{array}}
\[
V_1\ast(V_1+\{x\})=2V_1+x\ast V_1
\]
\[
\uline{V_1+G}
\]
\diagram{\begin{array}{cc}
\begin{array}{llllll}2&2&1&1&&\\1&1&1&1&1&1\\2&1&1&1&&\\\deleted{\unsure{2}}&\deleted{\unsure{1}}&\deleted{\unsure{1}}&\unsure{1}&&\end{array}
&\begin{array}{ccc}E+&x\ast&E\\3&&3\\&&\deleted{\unsure{E+xE}}\end{array}
\end{array}}
% archive foliation: 15
''',[
('deletion','top in writing orientation (bottom of scan)','cellules ... topologie différentielle'),
('margin note','above first formula','x²=u'),
('display','below cancelled prose','(V_1 dot+ {x}) * (V_1 dot+ {x}) = ... =2G+{u}'),
('diagram','middle left','{e}, V_1, cancelled {x}*V_1, V_2, horizontal arrow'),
('insertion','above middle diagram','V_1 dot+ {x}'),
('deletion','middle right','2V_1+u'),
('display','middle right','boxed 3 2 2 2'),
('display','middle','E*F; a+b=a′+b′; (a−a′)=(b′−b)'),
('display','middle left','a_1+a_2; b_1+b_2'),
('deletion','middle left','a_1'),
('display','middle','a; 0 a / 0 ... a'),
('deletion','middle','b+a; 0 a'),
('display','lower middle','0 a,a 2a; a≠0'),
('deletion','lower right','2a≠0'),
('display','lower right','2a=0'),
('diagram','lower left','1111/211; 22/211/2111'),
('deletion','within numeral array','2 or 4'),
('display','lower right','V_1*(V_1+{x})=2V_1+x*V_1; V_1+G'),
('diagram','bottom left','2211/111111/2111/cancelled 2111'),
('diagram','bottom right','E+x*E; 3 3'),
('deletion','bottom right','E+xE')
],'''The sheet combines a wholly cancelled prose fragment on Bruhat cells/Schubert cycles and differential topology with additive or convolution-like calculations and numeral partitions. Orientation was reversed for reading; no content was inferred from the archive subject. The dot above plus is visible in the leading expansion, whereas later pluses are plain. This differs from earlier x and prime forms and must be included in the notation audit. The boxed 3222 is not a page count.''',sheet_kind='cancelled_draft')
