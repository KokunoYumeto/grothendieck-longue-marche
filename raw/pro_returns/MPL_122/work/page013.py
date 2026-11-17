from record import save
save(13,r'''
\scanpage{13}
Soit $W$ une variété \deleted{topologique} diff.

$P,Q$ deux sous-variétés à bord

avec
\[
P\cap Q=\partial P=\partial Q
\]
\[
P\cup Q=W
\]
et $P$ et $Q$ étant \unsure{deux|des} fibrés diff.

\deleted{Alors on a}
\margin{$\partial P$}
\margin{\deleted{\unsure{W}}}
\diagram{\begin{tikzcd}[column sep=small]
P\arrow[r]&S&Q\arrow[r]&T\\
M\arrow[u,hook]&&N\arrow[u,hook]
\end{tikzcd}}
de bases $S,T$ des variétés diff \unsure{cptes} $S,T$, de fibres des variétés à bords $M$, resp. $N$. Donc $\partial P$ est un fibré sur $S$ de fibre $\partial M$, et $\partial Q$ un fibré sur $T$ de fibre $\partial N$ :
\diagram{\begin{tikzcd}[column sep=small]
\partial P\arrow[r]&S&\partial Q\arrow[r]&T\\
\partial M\arrow[u,hook]&&\partial N\arrow[u,hook]
\end{tikzcd}}
On suppose donnés des isomorphismes
\[
\alpha:S\simeq\partial N\qquad\beta:T\simeq\partial M
\]
et \deleted{pour les fibres} des trivialisations
\[
\sigma:\partial P\simeq S\times\partial M\qquad\tau:\partial Q\simeq T\times\partial N
\]
D'où, par composition
\[
(\alpha,\sigma):\partial P\simeq\partial N\times\partial M,\quad(\beta,\tau):\partial Q\simeq\partial M\times\partial N
\]
et par suite un isom
\[
\varphi:\partial P\simeq\partial Q
\]
\mspage{12}
''',[
('text','top','Soit W une variété diff.'),('deletion','top','topologique'),('text','upper','P,Q deux sous-variétés à bord'),('text','upper','avec'),('display','upper','P intersection Q=partial P=partial Q'),('display','upper','P union Q=W'),('text','upper middle','et P et Q étant deux fibrés diff.'),('deletion','upper middle','Alors on a'),('margin note','left middle','partial P'),('margin note','left middle','cancelled W'),('deletion','left middle','W'),('diagram','middle','M to P to S; N to Q to T'),('text','middle lower','de bases S,T des variétés diff cptes'),('diagram','lower middle','boundary M to boundary P to S and boundary N to boundary Q to T'),('text','lower','On suppose donnés des isomorphismes'),('display','lower','alpha:S isomorphic boundary N; beta:T isomorphic boundary M'),('text','lower','et des trivialisations'),('deletion','lower','pour les fibres'),('display','lower','sigma and tau trivializations'),('text','lower','D’où par composition'),('display','bottom','alpha,sigma and beta,tau boundary product identifications'),('text','bottom','et par suite un isom'),('display','bottom','phi:boundary P isomorphic boundary Q'),('text','bottom left','12')],
[('before first fibration diagram','deux','des; word retraced.','medium'),('base-manifold qualification','cptes','Abbreviation for compactes appears likely, without expanding it in transcription.','medium'),('left marginal cancelled mark','W','Small overwritten isolated letter.','low')],
['New smooth-fibration gluing setup, topologique explicitly replaced by diff.','Isomorphism of the two boundaries constructed from alpha,beta and boundary trivializations, implicitly exchanging the two factors.'])
