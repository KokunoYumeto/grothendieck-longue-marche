from record import save
tex=r'''\scanpage{32}
\deleted{En d'autres termes, le \unsure{triangle}}
\deleted{\[H^i(W_0)=0\quad\text{si }i\ne\unsure{i|1}\]}
\deleted{\[\begin{gathered}\unsure{i=n+1}\\\unsure{2n-i=n-1}\end{gathered}\]}
\margin{\uline{\unsure{intéressant}}}
\[\left\{\begin{array}{ll}
H^i(W_0)\xrightarrow{\sim}H^{2n-i-1}(M)^\vee&\text{si }i\ge n+\unsure{1|2}\\
\boxed{H^i(M)\xrightarrow{\sim}H^i(W_0)}&\text{si }i\le n-2
\end{array}\right.\]
\margin{(épim si $i=\unsure{n-1|n}$)}
\margin{(donc $2n-i-1\le n-3$)}
\margin{(mono si $i=n-1$)}
Donc $H^{\unsure{*|q}}(M)$ est connu en termes de $H^{\unsure{*|q}}(W_0)$ sauf aux dimensions \deleted{$\unsure{n}$} $n-1,n$, \deleted{$\unsure{n}$}, où on a la suite exacte
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\deleted{0}\arrow[r]&\deleted{H^{n-2}(M)}\arrow[r]&\deleted{H^{n-2}(W_0)}\arrow[r]&\deleted{H^{\unsure{n+1|2n+1}}(M)^\vee}\inserted{0}\arrow[r]&H^{n-1}(M)\arrow[r]&H^{n-1}(W_0)\arrow[r,"\mathrm{surj}"]\arrow[d,no head,"\deleted{\unsure{\simeq}}"]&H^{\unsure{n}}(M)^\vee\arrow[d]\\
\deleted{0}&\deleted{H^{n-2}(M)^\vee}\arrow[l]&\deleted{H^{n+1}(W_0)}\arrow[l]&\deleted{H^{n+1}(M)}\inserted{0}\arrow[l]&H^{n-1}(M)^\vee\arrow[l]&H^n(W_0)\arrow[l]&H^n(M)\arrow[l,"\deleted{\unsure{\rho}}"]
\end{tikzcd}}

Supposons maintenant que $W$ \unsure{est} la sphère topologique. Alors on a vu que $H^i(W_0)=0$ si $i\ne0,n-1,n,2n-1$.

\uuline{Si donc} $\textcircled{\(n\ge3\)}$, on trouve aussi \uline{$H^{\inserted{i}\deleted{\unsure{n-2}}}(M)=0$}, \deleted{$\unsure{H^{n-2}(M)=0}$}
\inserted{si $i\ne0,n-1,n$, \deleted{$\unsure{2n}$}}

\deleted{et la suite exacte précédente devient}
\deleted{\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&+&-&+&-\\
0\arrow[r]&H^{\unsure{n+1|n-1}}(M)^\vee\arrow[r,"u"]&H^{n-1}(M)\arrow[r]&H^{n-1}(W_0)\arrow[r]&H^n(M)^\vee\arrow[d,very thick]\\
0&H^{n+1}(M)\arrow[l]&H^{n-1}(M)^\vee\arrow[l,"u'"']&H^n(W_0)\arrow[l]&H^n(M)\arrow[l]\\
&-&+&-&+\\
&\unsure{H}
\end{tikzcd}}}
\mspage{31}
'''
e=[('deletion','top prose','En d’autres termes, le triangle'),('deletion','top display','H^i(W0)=0 si i ne i'),('deletion','top small enclosed calculations','i=n+1; 2n-i=n-1'),('margin note','left upper','intéressant'),('display','upper','H^i(W0) ≃ H^{2n-i-1}(M)^vee; H^i(M) ≃ H^i(W0)'),('margin note','right upper first','épim si i=n-1'),('margin note','right upper second','donc 2n-i-1 le n-3'),('margin note','right upper third','mono si i=n-1'),('text','middle','Donc H^*(M) est connu en termes de H^*(W0)'),('deletion','middle first degree','n'),('deletion','middle last degree','n'),('diagram','middle','serpentine exact sequence with deleted endpoints'),('deletion','middle diagram upper left','0 → H^{n-2}(M) → H^{n-2}(W0) → H^{n+1}(M)^vee'),('insertion','middle diagram upper endpoint','0'),('deletion','middle diagram lower left','H^{n+1}(M) → H^{n+1}(W0) → H^{n-2}(M)^vee → 0'),('insertion','middle diagram lower endpoint','0'),('deletion','middle diagram between W0 terms','simeq'),('deletion','middle diagram right lower arrow','rho'),('text','lower','Supposons maintenant que W est la sphère topologique'),('text','lower next line','Si donc n ge 3 on trouve aussi'),('display','lower underlined','H^i(M)=0'),('deletion','lower exponent','n-2'),('insertion','lower exponent','i'),('deletion','lower right formula','H^{n-2}(M)=0'),('insertion','above lower formula','si i ne 0,n-1,n'),('deletion','insertion end','2n'),('deletion','lower prose','et la suite exacte précédente devient'),('diagram','bottom cancelled','u and u-prime serpentine sequence with signs'),('deletion','bottom full diagram','u sequence and +/- signs')]
d=[('top cancelled prose','triangle','Last word crosses a heavy strike.','low'),('top cancelled formulas','i ne i|1; i=n+1; 2n-i=n-1','Very compressed unfinished calculation.','low'),('left margin','intéressant','Small sloping word.','low'),('upper bound','i ge n+1 | n+2','Bold revised numeral; following parenthesis retained literally.','low'),('right margin first','épim si i=n-1 | n','Tiny terminal degree against page edge.','low'),('middle prose','H^* | H^q','Superscript resembles handwritten q/asterisk.','medium'),('middle sequence','n+1 | 2n+1; n; deleted simeq/rho','Overwritten exponents and cancelled labels.','low'),('lower vanishing','i over deleted n-2; cancelled H^{n-2}(M)=0','Revised and scribbled-over degree expressions.','low'),('bottom first nonzero object','H^{n+1}(M)^vee | H^{n-1}(M)^vee','Overwritten and underlined degree; full diagram cancelled.','low'),('bottom faint isolated letter','H','Pencil mark beneath diagram.','low')]
o=['Cancelled last sequence with u,u-prime and alternating pencil signs, compare next manuscript scan for replacement.','Claim: cohomology of M known from W0 except middle degrees; n>=3 sphere hypothesis strengthened vanishing.']
save(32,tex,e,d,o)
