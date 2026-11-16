from page_work import save_page
text = r'''\scanpage{132}
On a une suite exacte de $C$-groupes
\diagram{\begin{tikzcd}
0 \arrow[r] & \mu_n \arrow[r] & G_m \arrow[r,"n"] & G_m \arrow[r,dash] & 0
\end{tikzcd}}
d'où
\diagram{\begin{tikzcd}
H^1(C,G_m) \arrow[r,"n"] & H^1(C,G_m) \arrow[r,dash] & H^2(C,\mu_n) \arrow[r] & H^2(C,G_m)
\end{tikzcd}}
[N.B. On a $\underline H^i_f(G_m)=0$ pour $i\geq2$, \inserted{$\underline H^0_f(G_m)\simeq G_m$,} d'où une suite exacte\unsure{\ldots}]
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r] & H^1(k,G_m) \arrow[r] \arrow[d,equal] & H^1(C,G_m) \arrow[r] & H^0(k,\underline H^1_f(G_m)) \arrow[r] \arrow[d,equal] & H^2(k,G_m) \arrow[d,equal] \\
& 0 & & \operatorname{Pic}(C/k) & \operatorname{Br}(k) \\
& \unsure{\text{th. 90}} & & &
\end{tikzcd}}
Ainsi, $H^1(C,G_m)\subset\operatorname{Pic} C$.

$\unsure{\sigma|\tau}$ groupe \inserted{fini} \deleted{\unsure{ab}} \unsure{étale} sur $k$,
définit un groupe \deleted{$\unsure{\sigma|\tau}\otimes\mu_n$ sur $k$ de} $D(\Delta\unsure{\sigma|\tau})$ de type multiplicatif [isomorphe à $\unsure{\sigma|\tau}\otimes\mu_n$ si $n\unsure{\sigma|\tau}=0$].

Posons $S\unsure{\sigma|\tau}=(D\Delta\unsure{\sigma|\tau})(2)$

On va définir un \deleted{hom} accouplement
\[
\text{a)}\qquad \operatorname{Ext}^i(C;G,S\unsure{\sigma|\tau})\longrightarrow
\operatorname{Ext}^{i\deleted{\unsure{-2}}}(k;Rf_*G,\unsure{\sigma|\tau})
\]
associé à un hom
\[
\text{b)}\qquad \textcircled{$*$}\qquad
\underline E_f(G,S\unsure{\sigma|\tau})\longrightarrow\underline E_k(Rf_*G,\unsure{\sigma|\tau})
\]
[évidemment bifonctoriel en $G,\unsure{\sigma|\tau}\ldots$], qui définit aussi un hom
\[
\underline{\operatorname{Ext}}^i_f(G,S\unsure{\sigma|\tau})\longrightarrow
\underline{\operatorname{Ext}}^i_k(Rf_*G,\unsure{\sigma|\tau})
\]
c)
\mspage{131}
'''
elements=[('text','top','On a une suite exacte de C-groupes'),('diagram','top','0, mu_n, G_m, G_m, 0'),('text','upper','d’où'),('diagram','upper','H^1(C,G_m), H^2(C,mu_n), H^2(C,G_m)'),('text','upper middle','N.B. On a H^i_f(G_m)=0 pour i>=2'),('insertion','above d’où','H^0_f(G_m) ≃ G_m'),('diagram','middle','0, H^1(k,G_m), H^1(C,G_m), H^0(k,H^1_f(G_m)), H^2(k,G_m); th. 90, Pic(C/k), Br(k)'),('text','middle','Ainsi, H^1(C,G_m) subset Pic C'),('text','lower middle','sigma/tau groupe étale sur k'),('insertion','above groupe','fini'),('deletion','after groupe','ab'),('text','lower middle','définit un groupe D(Delta sigma) de type multiplicatif'),('deletion','after groupe','sigma tensor mu_n sur k de'),('text','lower middle','Posons S sigma = (D Delta sigma)(2)'),('text','lower','On va définir un accouplement'),('deletion','before accouplement','hom'),('display','lower','a) Ext^i(C;G,S sigma) to Ext^i(k;Rf_*G,sigma)'),('deletion','superscript after i','-2'),('text','lower','associé à un hom'),('display','lower','b) circled star; E_f to E_k'),('text','bottom','évidemment bifonctoriel en G,sigma; qui définit aussi un hom'),('display','bottom','Ext^i_f(G,S sigma) to Ext^i_k(Rf_*G,sigma)'),('text','bottom left','c)'),('text','bottom left','131')]
save_page(132,text,elements,observations='Both halves revisited after whole-page reading. Enlarged the first cohomology sequence, the finite-group paragraph and revised exponent. Recurring Greek letter left as an explicit unresolved sigma/tau pair; canceled superscript retained as a doubtful attempted reading.')
