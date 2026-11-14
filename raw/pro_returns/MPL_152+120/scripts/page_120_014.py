from record_page import save_page
save_page(120,14,r'''
Soit $Z\hookrightarrow R^{\deleted{\unsure{n}}\inserted{I}}$ un plongement modéré. On peut (par $M7$) le prolonger en
\[
 X_i\longrightarrow R^I\qquad(i\in\{1,2\})
\]
Soit
\[
 X_i\longrightarrow R^{A_i}\qquad i\in\{1,2\}
\]
comme dans $M6$ (d'où un \deleted{\unsure{appl.}} plongement modéré $X_i/Z_i\hookrightarrow R^{A_i}$, \inserted{$Z_i=\unsure{u_i|i_i}(Z)$}), on a donc un : $X_1\longrightarrow R^{I\amalg A_1}$ qui est un plongement et s'insère dans un diagramme cartésien
\diagram{\begin{tikzcd}
X_1\arrow[r,hook]&R^{I\amalg A_1}=R^I\times R^{A_1}\\
Z\arrow[u,hook]\arrow[r,hook]&R^I\times\{e_1\}\arrow[u,hook]&e_1\in R_0^{A_1}
\end{tikzcd}}
et de $=$ pour $X_2$, \deleted{\unsure{on le}} qu'on peut considérer comme \deleted{\unsure{des}} s'insérant dans
\diagram{\begin{tikzcd}[column sep=small]
\deleted{X_1}\arrow[r,hook]\arrow[d]&\deleted{R^I\times R^{A_1}\times\{e_2\}}\arrow[r]\arrow[d]&\deleted{R^I\times R^{A_1}\times R^{A_2}}\\
\deleted{Z}\arrow[r]&\deleted{R^I\times\{e_1\}\times\{e_2\}}&\deleted{R^I\times\unsure{R^{A_2}|R^{A_1}}\times R^{A_2}}\arrow[u]
\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
X_1\arrow[r,hook]&R^I\times R^{A_1}\times\{e_2\}\arrow[r,hook]&R^I\times R^{A_1}\times R^{A_2}\\
& R^I\times\{e_1\}\times\{e_2\}\arrow[u,hook]\arrow[r,hook]&R^I\times\{e_1\}\times R^{A_2}\arrow[u,hook]\\
Z\arrow[uu,hook]\arrow[rr,hook]&\text{(*)}&X_2\arrow[u,hook]
\end{tikzcd}}
\mspage{13}
''',[
('text','top','Soit Z into R^I'),('deletion','exponent first formula','n'),('insertion','exponent first formula','I'),('display','upper','Xi to R^I'),('text','upper','Soit'),('display','upper middle','Xi to R^Ai'),('text','middle','comme dans M6'),('deletion','before plongement','appl.'),('insertion','under Zi','Zi=ui(Z)'),('diagram','middle','Cartesian square X1 Z'),('text','lower middle','et de = pour X2'),('deletion','after X2','on le'),('deletion','after comme','des'),('diagram','lower cancelled','X1 and ambient products'),('diagram','bottom','(*) ambient product diagram'),('text','bottom left','13')], observations='Construction for amalgamated sums: extend a coordinate embedding of Z using M7 and combine with M6 functions; large ambient-product diagram (*), preceded by a cancelled version. The overwritten index and cancelled ambient factor are uncertain.')
