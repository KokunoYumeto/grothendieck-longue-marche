import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{10}
\mspage{\unsure{8}}

d'un uniformisant \deleted{$\unsure{\varpi}$} $t$ de $V$, \inserted{donc de $\widetilde V$}, comme la réunion des sous-extensions \deleted{\unsure{abéliennes}} Kummeriennes
\[
(2.4.4)\qquad K_n=\widetilde K(\sqrt[n]{t})\subset\bar K,
\]
où $n$ parcourt les entiers $>0$ premiers à $p$.
Le groupe de Galois de cette extension $K_n$ est naturellement isomorphe au groupe
\[
\mu_n(\bar K)={}_n\bar K^*
\]
des racines nièmes de l'unité dans $\bar K$, et par passage à la limite on trouve
\[
 I_t=\operatorname{Gal}((\varinjlim_n K_n)/K)\simeq\varprojlim_n\operatorname{Gal}(K_n/K,\deleted{\unsure{\bar K}}\unsure{1}),
\]
i.e (2.4.2).

\uline{Remarque} 2.5. On notera que par définition, le sous-groupe $P$ de $I$ est stable par \uline{tout} autom. de $I$, en particulier par les automorphismes induits par les autom. int. de $\pi$. Donc $\pi$ opère par passage au quotient sur $I/P=I_t$; \deleted{On constate aussitôt que} dans cette opération, le \deleted{cette \unsure{opération}} ss-groupe $I$ de $\pi$ opère évidemment trivialement, $I_t$ étant commutatif, on en tire en fait une opération de $\pi/I\simeq\pi_0$ sur $I_t$. \deleted{\unsure{Compte tenu}} On vérifie trivialement que
\margin{9}
'''
e=[('text','top','d’un uniformisant t de V'),('deletion','top','varpi'),('insertion','above V','donc de Vtilde'),('deletion','before Kummeriennes','abéliennes'),('display','upper','(2.4.4) K_n=Ktilde(nth root t)'),('text','upper-middle','où n parcourt les entiers >0'),('text','middle','Le groupe de Galois de cette extension'),('display','middle','μn(Kbar)=n Kbar*'),('text','middle','des racines nièmes de l’unité'),('display','middle-lower','I_t=Gal((lim K_n)/K)'),('deletion','limit display right end','Kbar uncertain'),('text','below limit','i.e (2.4.2)'),('text','lower','Remarque 2.5 On notera'),('deletion','lower','On constate aussitôt que'),('deletion','lower interlinear','cette opération'),('deletion','bottom','Compte tenu'),('margin note','bottom left','9')]
save_page(34,10,tex,e,remarks='The two denominators K in the limit display have no confidently visible tilde and are retained as K. A heavily obliterated mathematical term at its right edge is very low confidence. The word Kummeriennes is retained without adding an accent absent from the ink.')
