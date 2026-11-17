from record_page import record
tex=r'''\scanpage{25}
% archive foliation: 24
\uline{Cas $j=i-1$}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
&\Psi^{i-1}\arrow[r,dash]\arrow[d,"n\operatorname{id}"']&\Phi^i\arrow[r]\arrow[d]&\Psi^i\arrow[d,equal]\\
0\arrow[r,dash]&\Psi^{i-1}\arrow[r]\arrow[d,"\unsure{\theta|0}"']&\Phi(i,n)\arrow[r]\arrow[d,"\alpha=?"]&\Psi^i\arrow[r,dash]\arrow[d,"0"]&0\\
0\arrow[r]&\Psi^{i\deleted{\unsure{+1}}-2}\arrow[r]&\Phi(i-1,m)\arrow[r,dash]&\Psi^{i\deleted{\unsure{+1}}-1}\arrow[r,dash]&0
\end{tikzcd}}
la composée
\diagram{\begin{tikzcd}[column sep=small]
\Phi^i\arrow[r]&\Phi(i,n)\arrow[r,dash]&\Phi(i-1,m)\arrow[r,dash]&\Psi^{i-1}
\end{tikzcd}}
est nulle car $\operatorname{Hom}(\Phi^i,\Psi^{i-1})=0$,
donc l'hom
\deleted{$\Psi^i\longrightarrow\Psi^{\unsure{i-1}}$}
\inserted{$\theta=n\alpha?$}:
$\Psi^{i-1}\longrightarrow\Psi^{i-1}$
composé avec $n\operatorname{id}$ est nul, i.e.
$n\theta=0$, or $\operatorname{Hom}(\Psi^{i-1},\Psi^{i-1})\simeq k$, donc
$\theta=0$, donc on \unsure{reprend} la structure
d'extension, et on termine comme
plus haut pour conclure
$\alpha=0$. Donc on trouve
\[
\operatorname{Hom}(\Phi(i,n),\Phi(j,m))\simeq
\left\{\begin{array}{ll}
0&\text{si }j\neq i,i+1\\
k&\text{si }j=i+1\quad\text{(par la composée d'hom can.)}\\
k&\text{si }j=i\quad\text{(un hom }\deleted{\unsure{respecte}}\text{ ces struct. d'ext.)}
\end{array}\right.
\]
\margin{\diagram{\begin{tikzcd}[column sep=small]
\Phi(i,n)\arrow[r,dash]&\Psi^i\arrow[r]&\Phi(i+1,m)
\end{tikzcd}}}
et est déterminé par ce qu'il induit
sur $\Psi^i$ et $\Psi^{i-1}$, qui doit être de
la forme $t m'\operatorname{id}_{\Psi^i}$ et $t n'\operatorname{id}_{\Psi^{i-1}}$,
si $n'=\dfrac{n}{(m,n)}$, $m'=\dfrac{m}{(m,n)}$ (il y a
une base can. une fois qu'on a
choisi le pgcd $(m,n)$ à un \unsure{signe}).
'''
record(25,tex,[('text','top heading','Cas j=i−1'),('diagram','top three rows','Ψ^(i−1)→Φ^i→Ψ^i; Φ(i,n)→Φ(i−1,m), α=?'),('deletion','lower left superscript','+1 overwritten by −2'),('deletion','lower right superscript','+1 overwritten by −1'),('text','below diagram','la composée'),('diagram','upper-middle horizontal','Φ^i→Φ(i,n)→Φ(i−1,m)→Ψ^(i−1)'),('text','middle','est nulle car Hom; donc l’hom'),('deletion','middle old map','Ψ^i→Ψ^(i−1)'),('insertion','above cancelled map','θ=nα?'),('display','middle map','Ψ^(i−1)→Ψ^(i−1)'),('text','middle proof','composé avec n id; nθ=0; θ=0; structure d’extension'),('text','lower-middle','plus haut pour conclure α=0; Donc on trouve'),('display','lower-middle cases','Hom(Φ(i,n),Φ(j,m))≃0,k,k'),('deletion','third case parenthesis','respecte'),('margin note','right of cases','par la composée d’hom can; struct d’ext'),('diagram','right of second case','Φ(i,n)→Ψ^i→Φ(i+1,m)'),('text','bottom','et est déterminé; tm′ id et tn′ id; pgcd')],doubts=[('top heading','j=i−1','sign crossed by staff rule','medium'),('diagram side vertical maps','left θ, right 0, downward arrows','small loops might be zeros; arrowheads faint','low'),('diagram bottom exponents','i−2 and i−1 with cancelled +1','overwritten original digits not fully recoverable','low'),('middle insertion','θ=nα?','θ=nat.?; last mark might punctuation rather than question mark','low'),('after θ=0','on reprend la structure','verb faint on staff line','low'),('case j=i parenthesis','un hom [deleted respecte] ces struct. d’ext.','right edge abbreviations cramped','low'),('bottom induced maps','tm′ id_Ψi, tn′ id_Ψ(i−1)','m′/n′ glyphs faint; order read locally','medium'),('last word','signe','unité? visible endpoint short; phrase retained without mathematical correction','low')],notation=[('equations labelled by question mark',r'$\alpha=?$','scan 25 top diagram; author’s question sign retained independently of editorial uncertainty')])
