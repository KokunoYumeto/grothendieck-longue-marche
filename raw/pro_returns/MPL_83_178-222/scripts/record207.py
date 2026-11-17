import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(207,r'''\scanpage{207}
\figure{\begin{tikzpicture}
\node[draw,ellipse] at (0,0) {$R_a$};
\node[align=left] at (0,-1) {$12+12$\\relations};
\node[draw,rectangle] at (3.1,0) {$\begin{aligned}
\mathcal T_f+\mathcal T_{f'}&=\sigma_a\\
\mathcal T_f\mathcal T_{f'}&=\pi_a
\end{aligned}$};\end{tikzpicture}}
avec
\[\begin{aligned}
\sigma_a={}&\operatorname{Tr}X_kX_l\operatorname{Tr}X_iX_j
 +\operatorname{Tr}X_i\operatorname{Tr}X_jX_kX_l
 +\operatorname{Tr}X_j\operatorname{Tr}X_kX_lX_i\\
&-\operatorname{Tr}X_i\operatorname{Tr}X_j\operatorname{Tr}X_kX_l\\
&\deleted{=\unsure{t_s+t}}\\
={}&\underbrace{\unsure{t_{a'a''}|t_{a''}}}_{\unsure{t_{a''}}}t_a
 +b_s\mathcal T_s+b_t\mathcal T_t-b_sb_t t_{a'a''}
\end{aligned}\]
\[\pi_a=\text{---}\]
expression \deleted{plus}\inserted{un peu} compliquée en
\[\begin{gathered}
\deleted{\operatorname{Tr}X_i,\unsure{d}}\quad b_i,c_i,b_j,c_j,t_{kl},c_kc_l\\
t_{ij}\quad\underbrace{\mathcal T_{jkl}}_{\mathcal T_s}\quad
\underbrace{\mathcal T_{kli}}_{\mathcal T_t}
\end{gathered}\]
\figure{\begin{tikzpicture}
\draw (0,0)..controls(.6,-.5) and (1,-.9)..(1.1,-1.5);\end{tikzpicture}}
\[
28\text{ variables}\quad
\begin{array}{ccccc}
\multicolumn{3}{c}{\overbrace{\phantom{4\quad4\quad6}}^{14}}&
\multicolumn{2}{c}{\overbrace{\phantom{8\quad6}}^{14}}\\[-.6em]
4&4&6&8&6\\
b_s&c_s&t_a,&\mathcal T_s,&\mathcal T_f
\end{array}
\]
$32$ relations !
\margin{206}
''',[
('drawing','upper left','circled R_a; box T_f+T_f prime'),('text','upper left','12+12 relations'),('text','upper middle','avec'),('display','top right','sigma_a=Tr X_kX_l Tr X_iX_j'),('deletion','second equality line','t_s+t'),('display','middle','sigma_a expression in b_s,T_s'),('display','middle','pi_a=---'),('text','middle','expression plus compliquee en'),('deletion','middle','plus'),('insertion','above plus','un peu'),('deletion','variable list','Tr X_i,d'),('display','middle right','b_i,c_i,b_j,c_j,t_kl,c_kc_l'),('drawing','right of upper formula','curved descending pen stroke'),('display','bottom left','28 variables;4,4,6,8,6'),('text','bottom left','32 relations !'),('margin note','lower left','206')],
[('sigma_a second expression','t_a prime a doubleprime','heavily overwritten edge index; underbrace label t_a doubleprime uncertain','low'),('crossed line under trace formula','t_s+t','first index and unfinished second term crossed','low'),('pi variable list deleted prefix','Tr X_i,d','last letter partly hidden by cancellation','low')],
['Pi_a is expressly left as an unwritten expression; three dashes are authorial, not editorial omission.','The author counts 28 variables and 32 relations; equality with an invariant ring is not demonstrated here.','Pale reversed type is back-side show-through, not a second live text on this face.'],sheet_kind='reused_typed')
