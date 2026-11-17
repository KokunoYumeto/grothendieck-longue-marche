import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(215,r'''\scanpage{215}
\[b-\alpha'=\gamma'-c'=\gamma-b'=c-\beta=-\delta\]
\[\begin{aligned}
\alpha'&=\delta+b\\
\gamma'&=-\delta+c'\\
\gamma&=-\delta+b'\\
\beta&=\delta+c
\end{aligned}\]
\[\boxed{\deleted{\delta+b=-\delta''+b'}}\]
\[\boxed{-\delta+c'=\unsure{\delta'}+c}\]
\[\boxed{\deleted{-\delta+b'=\delta''+b}}\]
\[\boxed{\delta+c=-\delta'+c'}\]
\figure{\begin{tikzpicture}\node[draw,ellipse] {$\begin{aligned}
\delta+\delta''&=b'-b\\
\delta+\delta'&=c'-c\deleted{\unsure{\varepsilon}}
\end{aligned}$};\end{tikzpicture}}
\[\begin{aligned}
\delta'+\delta''&=a'-a\\
\delta''+\delta&=b'-b\\
\delta+\delta'&=c'-c
\end{aligned}\]
\figure{\begin{tikzpicture}\draw (0,0)--(3.5,.15);\end{tikzpicture}}
\[\begin{aligned}
\delta+\delta'+\delta^{\unsure{''|4}}
 &=\frac12\bigl(a'+b'+c'-(a+b+c)\bigr)\\
 &=\frac12\bigl(\underbrace{(a'-a)}_{\varepsilon_1}
 +\underbrace{(b'-b)}_{\varepsilon_2}+\underbrace{(c'-c)}_{\unsure{\varepsilon_2|\varepsilon_3}}\bigr)
\end{aligned}\]
\[\boxed{\left\{\begin{aligned}
\delta&=\frac12(-\varepsilon_1+\varepsilon_2+\varepsilon_3)\\
\delta'&=\frac12(\varepsilon_1-\varepsilon_2+\varepsilon_3)\\
\delta''&=\frac12(\varepsilon_1+\varepsilon_2-\varepsilon_3)
\end{aligned}\right.}\]
\margin{214}
''',[
('display','top','b-alpha prime=gamma prime-c prime'),('display','upper left','four expressions for alpha prime,gamma prime,gamma,beta'),('display','upper middle','boxed delta+b=-delta doubleprime+b prime'),('deletion','first box','delta+b=-delta doubleprime+b prime'),('display','upper middle','boxed -delta+c prime=delta prime+c'),('display','middle','boxed -delta+b prime=delta doubleprime+b'),('deletion','third box','-delta+b prime=delta doubleprime+b'),('display','middle','boxed delta+c=-delta prime+c prime'),('drawing','upper right','circled two delta sum equations'),('deletion','circled equation ending','epsilon'),('display','lower middle','three delta sum equations'),('drawing','below three equations','horizontal rule'),('display','bottom','delta+delta prime+delta doubleprime=one half sum differences'),('display','lower right','boxed three half-integer formulas'),('margin note','lower left','214')],
[('second box','delta prime','thick initial loop overlaps other stroke','medium'),('last underbrace','epsilon_2','index looks2 though third in list, alternative3','medium'),('sum of deltas','double prime or4','same joined superscript strokes as scan213','medium')],
['Division by2 solves the three delta equations; integral and characteristic2 interpretation remains to be examined in research notes.','Two boxed equations are diagonally cancelled, while the extracted sum equations remain live.'],sheet_kind='reused_typed')
