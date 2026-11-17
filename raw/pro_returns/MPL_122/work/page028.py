from record import save
tex=r'''\scanpage{28}
$b)$ La portion de suite exacte
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
H^{2n}(W)\arrow[r,no head]\arrow[d,equals]&H^{2n}(W-W_0)\arrow[r,no head,"\mathrm{inj}"]&H^{2n-1}(W_0)\arrow[r,"\mathrm{surj}"]\arrow[d,equals]&H^{2n+1}(W)\arrow[r,no head]\arrow[d,equals]&H^{2n+1}(W-W_0)\arrow[r,no head]\arrow[d,equals]&H^{2n}(W_0)\arrow[r]\arrow[d,equals]&0\\
0&&\Lambda&&0&0\\[-1em]
&&&\Lambda
\end{tikzcd}}
\margin{si $W_0$ est connexe, tjrs le cas si $n\ge2$}
donne
\[\left\{\begin{gathered}
\boxed{H^{2n}(W-W_0)}=H^{2n+1}(W-W_0)=0\\
\underset{\Vert\;\Lambda}{H^{2n-1}(W_0)}\simeq\underset{\Vert\;\Lambda}{H^{2n+1}(W)}
\end{gathered}\right.\]
\margin{\unsure{conclusion visible de} Lefschetz affine local plus bas}
\margin{\uline{NB} $H^i(W_0)=0$ sauf si $i\in[0,2n-1]$. $H^\bullet(W_0)$ satisfait dualité de Poincaré}
\margin{\deleted{\unsure{supposons}}}
\margin{\uline{NB} $W$ sph. coh. $\Longleftrightarrow$ \deleted{\unsure{\(W-W_0\)}}
\[\left\{\begin{gathered}H^i(W-W_0)\xrightarrow{\sim}H^{i-1}(W_0)\quad\text{si }i\ne0,2n\\
\text{et }H^{2n}(\deleted{W}\unsure{W}-W_0)\hookrightarrow H^{2n-1}(W_0)\end{gathered}\right.\]
[Si \deleted{\unsure{de plus}} $W_0$ connexe, cela équivaut à $H^{2n}(W-W_0)=0$]
Si $n\ge2$, et $W$ non-singulier, il \uuline{f.} que $H^{2n}(W-W_0)=0$, $W_0$ connexe}

\figure{\begin{tikzpicture}\draw (0,0)--(13,0.4);\end{tikzpicture}}
Supposons que $X$ soit régulier en $\deleted{X}x$. Alors on a, par

\uline{Lefschetz local} :
\[\left\{\begin{array}{lll}
H^i(W)\longrightarrow H^i(W_0)&\text{un isom pour}&i\le n-\unsure{2|1}\\
&\text{un mono pour}&i=n\deleted{\unsure{-2}}-1
\end{array}\right.\]
\deleted{Donc si $W$ est une sphère,}

\deleted{Par la suite exacte associée à $e)$, cela signifie}
\inserted{\unsure{dualité cela s'interprète}}
\[\left\{\begin{array}{lll}
H^i_{\unsure{!}}(W_0)\longrightarrow H^{i+2}(W)&\text{un isom si}&i\ge n+\unsure{1}\\
&\text{un épim si}&i\unsure{\ge|=}n\deleted{\unsure{+1}}
\end{array}\right.\]
donc la connaissance de la cohomologie de $W$ implique celle de la cohomologie de $W_0$, sauf en les deux dimensions \deleted{$n-1,n$}\inserted{$H^{n-1}(W_0),H^n(W_0)$} (complémentaires, i.e. où les cohomologies sont duales pour $W_0$).

On peut dire aussi que l'on a
\[\left[\begin{array}{ll}H^i(W-W_0)=0&\text{si }i>n+1\\[-.4em]\quad\Vert&\\[-.4em]\quad H^i(P)&\end{array}\right.\]
\mspage{27}
'''
e=[('text','top','b) La portion de suite exacte'),('diagram','top','H^{2n}(W) — H^{2n}(W-W0)'),('margin note','under H^{2n-1}(W0)','si W0 est connexe, tjrs le cas'),('text','under sequence','donne'),('display','upper middle','H^{2n}(W-W0)=H^{2n+1}(W-W0)=0'),('margin note','right upper cloud','conclusion visible de Lefschetz affine local plus bas'),('margin note','right NB','H^i(W0)=0 sauf si'),('deletion','above left NB','supposons'),('margin note','left boxed NB','W sph. coh. iff'),('deletion','left NB first line','W-W0'),('display','left NB','H^i(W-W0) ≃ H^{i-1}(W0)'),('deletion','left NB second formula','W overwritten'),('text','left NB middle','Si W0 connexe'),('deletion','left NB middle','de plus'),('text','left NB bottom','Si n ge 2 et W non-singulier'),('drawing','middle rule','sloping separating line'),('text','middle','Supposons que X soit régulier'),('deletion','middle before x','X'),('text','middle heading','Lefschetz local'),('display','middle','H^i(W) → H^i(W0), isom/mono'),('deletion','middle degree','-2'),('deletion','lower middle first line','Donc si W est une sphère'),('deletion','lower middle second line','Par la suite exacte associée à e)'),('insertion','above second cancelled line','dualité cela s’interprète'),('display','lower middle','H^i_!(W0) → H^{i+2}(W), isom/épim'),('deletion','lower degree','+1'),('text','lower paragraph','donc la connaissance de la cohomologie'),('deletion','lower paragraph','n-1,n'),('insertion','above n-1,n','H^{n-1}(W0),H^n(W0)'),('text','bottom','On peut dire aussi que l’on a'),('display','bottom','H^i(W-W0)=0 si i>n+1; =H^i(P)')]
d=[('upper right cloud','conclusion visible de','First two words compressed; Lefschetz affine local plus bas clear.','low'),('above left NB','supposons','Heavily scribbled-out word.','low'),('left NB','sph. coh.; deleted W-W0','Abbreviated words and cancelled opening difficult.','low'),('left NB middle','deleted W; de plus','Overwritten fragments.','low'),('first Lefschetz bound','i le n-2 | n-1','Final overwritten numeral resembles 2; retain alternative.','medium'),('mono bound','deleted -2','Black cancellation between n and -1.','low'),('above cancelled line','dualité cela s’interprète','Insertion crosses the cancelled sentence; wording partly reduced.','medium'),('dual map','H^i_!(W0)','Small mark below H could be ! or a residual ink mark.','low'),('dual bounds','i ge n+1; i ge|= n deleted +1','Both endpoints overwritten; relation in second line ambiguous.','low')]
o=['Live b) revises cancelled endpoint line on scan026; connectedness is explicitly used.','Left NB states cohomology-sphere criterion; dependency on smoothness and n>=2 to examine.','Local Lefschetz and dual degree ranges are revised; implication only two middle cohomology groups remain undetermined.']
save(28,tex,e,d,o)
