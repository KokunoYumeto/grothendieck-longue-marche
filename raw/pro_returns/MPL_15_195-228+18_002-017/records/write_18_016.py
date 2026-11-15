from record_page import save
save(18,16,'reused_typed',r'''
A - 21 -\hfill n\textsuperscript{o} 413

de V dans N comme étant un élément de $\operatorname{Hom}(U(\underline V);N)$ et noter $\widehat P(\underline V;N)$ le module ainsi défini, $\widehat P_+(\underline V;N)$ désignant le sous-module des applications linéaires nulles sur $U_0(\underline V)$. Ceci ne peut être gênant puisque dans le cas d'un module libre, il y a un isomorphisme canonique de l'un sur l'autre des deux modules notés $\widehat P_+(\underline V;N)$.
Si $N=K$, on identifiera $\widehat P(\underline V;K)$ et $\widehat P(\underline V)$.

Soient $\underline V$ et $\underline W$ deux noyaux formels. Nous allons caractériser les applications linéaires de $U(\underline V)$ dans $U(\underline W)$ qui proviennent d'applications formelles de $\underline V$ dans $\underline W$:

PROPOSITION 8.--- \uline{Pour qu'une application linéaire} $\psi$ \uline{de} $U(\underline V)$ \uline{dans} $U(\underline W)$ \uline{soit de la forme} $\varphi_*$ \uline{avec} $\varphi\in\widehat P_+(\underline V;\underline W)$, \uline{il faut et il suffit que} $\psi(U_0(\underline V))=U_0(\underline W)$ \uline{et que} $\psi$ \uline{soit compatible avec les applications diagonales} (\uline{c'est-à-dire que}
\[
(\psi\otimes\psi)\circ\unsure{\Gamma|T}=\unsure{\Gamma|T}\circ\psi).
\]
Que les conditions soient nécessaires résulte de la prop. 6. La prop. 7 montre d'ailleurs que si $\varphi$ existe, elle est unique. Pour démontrer l'existence de $\varphi$, on se ramène en prenant des cartes formelles, au cas de noyaux formels définis par des modules libres M et N. Soit alors $(e_i)_{i\in I}$ une base de M, $(e'_j)_{j\in J}$ une base de M', et posons:
\[
(30)\qquad\psi(e_\alpha)=\sum a_{\alpha,\beta}\,e'_\beta\qquad(a_{\alpha,\beta}\in K).
\]
La condition $\psi(U_0(V))=U_0(W)$ entraîne
\[
(31)\qquad a_{0,\beta}=0\quad\text{pour }|\beta|\geq1,\quad a_{0,0}\ne0.
\]
La compatibilité de $\psi$ avec les applications diagonales donne:
\[
(32)\qquad a_{\alpha,\beta_1+\beta_2}=\sum_{\alpha_1+\alpha_2=\alpha}a_{\alpha_1,\beta_1}\,a_{\alpha_2,\beta_2}.
\]
\figure{\begin{tikzpicture}[scale=.6]\draw[line width=.7pt] (0,.5)--(.23,.17);\draw[line width=.7pt] (-.11,-.28)--(-.11,-.45);\fill (-.2,-.3) circle (.012);\end{tikzpicture}}
\mspage{15}
''',[
('text','typeset top','A - 21 -; n° 413'),
('text','upper','de V dans N comme étant un élément de Hom'),
('text','upper middle','Soient V et W deux noyaux formels'),
('text','middle','PROPOSITION 8. Pour qu’une application linéaire psi'),
('display','middle','(psi tensor psi) compose Gamma = Gamma compose psi'),
('text','middle lower','Que les conditions soient nécessaires résulte de la prop. 6'),
('display','lower','(30) psi(e_alpha)=sum a_alpha,beta e_prime_beta'),
('text','lower','La condition psi(U_0(V))=U_0(W) entraîne'),
('display','lower','(31) a_0,beta=0; |beta|>=1; a_0,0 not=0'),
('text','bottom','La compatibilité de psi avec les applications diagonales donne'),
('display','bottom','(32) a_alpha,beta_1+beta_2'),
('drawing','left of (30)-(31)','short diagonal stroke and short vertical marks')
], 'Whole and original halves inspected, then both halves rotated 180 degrees for line-by-line reading. M et N followed by base de M prime is retained. Gamma/T is uncertain from the typed diagonal-map glyph. Underlining of formal-kernel letters is copied where present, not supplied in the later un-underlined condition.')
