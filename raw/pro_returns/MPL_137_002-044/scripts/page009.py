from record_page import record
tex=r'''\scanpage{9}
% archive foliation: 8
\uline{Cor 1} \deleted{Dans} \deleted{\unsure{de plus}} ces conditions, on obtient encore
des conditions équivalentes en
exigeant \inserted{de plus} dans a) que les $L_n$, \deleted{$\pi_n(L_\bullet)$}
soient de type fini, dans a') que les
$L_n^!$, \deleted{$H_n(L^!_\bullet)$} soient de type fini, dans
b) et b') que les $M_i$ et $N_j$ soient de
type fini.

\unsure{On aura} sous les conditions de prop b
\[
L_n=\prod_{1\leq i\leq n+1}\unsure{\Lambda^i\Phi_{nk}}\otimes_k M_i
\times\prod_{\deleted{1}\inserted{0}\leq j\leq n}\unsure{\Lambda^j\Psi_{nk}}\otimes N_j
\]
\deleted{\unsure{donc on trouve}}

\uline{Cor 2} Sous les conditions équivalentes de
la proposition, pour que $L^!_\bullet$ soit à degrés
\deleted{\unsure{finis par}} degrés bornés, il faut,
qu'il n'y ait qu'un nombre \inserted{fini} d'indices
$i$ et $j$ tels que $M_i\neq0$, $N_j\neq0$.

\deleted{Sous les conditions}
On appellera un $L_\bullet$ \deleted{\unsure{spécial} \illegible{2}} \unsure{si}
$L^!_\bullet$ est \deleted{\unsure{parfait}}, \inserted{à degrés bornés et à composantes}
et à $H_n$ projectifs de \unsure{r.f.|t.f.} --- i.e.
si $L_\bullet$ est $\simeq$ somme finie de
modules de la forme \deleted{\unsure{$L$}}
\[
\Lambda^i\Phi_{\unsure{*|\bullet}}\otimes_k M_i\inserted{\ (i\geq1)},\quad
\Lambda^j\Psi_{\unsure{*|\bullet}}\otimes N_j\quad(j\geq0),
\]
avec les $M_i$ et $N_j$ proj. de \unsure{r.f.|t.f.}; \uline{stricte-}
\uline{ment spécial} si de plus les
$M_i$, $N_j$ sont \uline{libres}. Je reviens au cas des
'''
record(9,tex,[('text','upper corollary','Cor 1 ces conditions'),('deletion','first word after heading','Dans'),('deletion','above first line','de plus'),('insertion','above dans a','de plus'),('deletion','condition a','π_n(L)'),('deletion','condition a′','H_n(L!)'),('text','middle transition','On aura sous les conditions'),('display','middle products','L_n=products Λ^i Φ and Λ^j Ψ'),('deletion','second product lower bound','1'),('insertion','second product lower bound','0'),('deletion','below display','donc on trouve'),('text','middle-lower corollary','Cor 2 Sous les conditions'),('deletion','before degrés bornés','finis par'),('insertion','after nombre','fini'),('deletion','start of next paragraph','Sous les conditions'),('text','lower definition','On appellera un L'),('deletion','definition right-hand overwriting','spécial; two unreadable words'),('deletion','following L! est','parfait'),('insertion','above and after deleted parfait','à degrés bornés et à composantes'),('deletion','after de la forme','L'),('display','lower elementary objects','Λ^i Φ ⊗ M_i; Λ^j Ψ ⊗ N_j'),('insertion','after first tensor','i≥1'),('text','bottom definition continuation','avec les M_i et N_j; strictement spécial')],doubts=[('top deletions','Dans; de plus','first line obscured by printed staff rules','low'),('middle equality','Λ^i Φ_{nk}, Λ^j Ψ_{nk}; product bounds','subscripts and overstruck lower bound','medium'),('Cor 2','finis par; repeated degrés','deletion and live word boundary uncertain','low'),('definition overwritten words','spécial; parfait; si','multiple overwrites, staff and fading; no conjectural repair of syntax','low'),('definition insertion','à degrés bornés et à composantes','letters are faint but several are visible between staff lines','low'),('bottom adjective','strictement spécial','spécial appears underlined, ending faint','medium'),('bottom abbreviation','r.f.','t.f.','medium')])
