from record import save
tex=r'''\scanpage{30}
Revenant au cas $W$ une sphère, on trouve
\[\left\{\begin{array}{ll}H^i(W-W_0)=0&\text{si }i>n+1\\H^i(W_0)=0&\text{si }i\ne n-1,n,0,2n-1\end{array}\right.\]
\margin{[en fait, si $i\ne\deleted{\unsure{n,n+1}}\deleted{\unsure{]}}0,1,n,n+1$]}
\margin{(d'abord si $i\ge n+1$ et $i\ne2n-1$, puis le reste par dualité]}

La suite exacte associée à $d)$ est triviale, sauf la portion
\[\left\{\begin{gathered}
0\longrightarrow H^0(W)\longrightarrow H^0(W-W_0)\longrightarrow0\\
0\longrightarrow H^n(W-W_0)\longrightarrow H^{n-1}(W_0)\longrightarrow0\\
0\longrightarrow H^{n+1}(W-W_0)\longrightarrow H^n(W_0)\xrightarrow[\text{si }n\ne1]{}0\\
0\longrightarrow H^{2n-1}(W_0)\longrightarrow H^{2n+1}(W)\longrightarrow0
\end{gathered}\right.\]
\[0\longrightarrow H^1(W-W_0)\longrightarrow H^0(W_0)\longrightarrow0\]
\deleted{\[\unsure{n+1\ne2n+1}\]}
\deleted{\[n+2\ne2n+1\]}

[Si $n=1$, on trouve
\[\begin{gathered}
0\longrightarrow H^0(W)\xrightarrow{\sim}H^0(W-W_0)\mathbin{-}0\\
0\longrightarrow H^1(W-W_0)\longrightarrow H^0(W_0\deleted{\unsure{\Lambda}})\mathbin{-}0\\
0\longrightarrow H^2(W-W_0)\longrightarrow H^1(W_0)\longrightarrow\underset{\Vert\;\Lambda}{H^3(W)}\longrightarrow0
\end{gathered}\]
]
\figure{\begin{tikzpicture}\draw (0,0)--(13,0.6);\end{tikzpicture}}
Notons que, par \unsure{passage} à la limite, \deleted{\unsure{les les}} les relations
\[H^i(W\unsure{-}W_0,\Lambda)=0\quad\text{pour }i>n\deleted{\unsure{+1}}\]
donnent
\[\boxed{H^i(M,\Lambda)=0\quad\text{si }i>n\deleted{\unsure{+1}}}\]
\margin{[\unsure{Indépendt} du fait que $W$ non singulier] \inserted{et \unsure{même} que $W_0$ non singulier}}

La suite exacte relative (si $W$ non singulier)
\[\mathbin{-}\longrightarrow H^{\unsure{2n-i}}(M)^\vee\longrightarrow H^i(M)\longrightarrow H^i(W_0)\longrightarrow H^{2n-i\unsure{+1|-1}}(M)^\vee\longrightarrow H^{i+1}(M)\longrightarrow H^{\unsure{i+1}}(W_0)\]
montre donc que

\deleted{Si $i>n+1$}
\mspage{29}
'''
e=[('text','top','Revenant au cas W une sphère'),('display','top','H^i(W-W0)=0; H^i(W0)=0'),('margin note','top right first','en fait, si i ne 0,1,n,n+1'),('deletion','top right first','n,n+1 and bracket'),('margin note','top right second','d’abord si i ge n+1'),('text','upper middle','La suite exacte associée à d)'),('display','middle left brace','four short exact sequences'),('display','middle right','0 → H^1(W-W0) → H^0(W0) → 0'),('deletion','middle right','n+1 ne 2n+1'),('deletion','middle right below','n+2 ne 2n+1'),('text','lower middle','Si n=1 on trouve'),('display','lower middle','three short exact sequences for n=1'),('deletion','n=1 second sequence','Lambda after W0'),('drawing','below n=1','separating line'),('text','lower','Notons que, par passage à la limite'),('deletion','lower prose','les les'),('display','lower','H^i(W-W0,Lambda)=0 pour i>n'),('deletion','lower exponent bound','+1'),('text','before box','donnent'),('display','lower boxed','H^i(M,Lambda)=0 si i>n'),('deletion','boxed bound','+1'),('margin note','lower right','Indépendt du fait que W non singulier'),('insertion','under margin note','et même que W0 non singulier'),('text','bottom','La suite exacte relative (si W non singulier)'),('display','bottom','H^{2n-i}(M)^vee → H^i(M) → H^i(W0)'),('text','bottom end','montre donc que'),('deletion','bottom last line','Si i>n+1')]
d=[('top right deletion','n,n+1 and ]','Heavy overwriting after i ne.','low'),('right crossed inequalities','n+1 ne 2n+1','First left-hand n overwritten.','medium'),('n=1 second sequence','deleted Lambda','Small overwritten mark after W0.','low'),('lower prose','passage; deleted les les','Rapid handwriting and two crossed small words.','medium'),('lower vanishing bounds','deleted +1','Both terminal groups are blacked out.','low'),('lower right','Indépendt; même','Abbreviated opening and short added word.','medium'),('last exact sequence','2n-i+1 | 2n-i-1','The ink before 1 appears plus-like; mathematical expectation not used to resolve it.','low'),('last object','H^{i+1}(W0)','Small crowded exponent.','medium')]
o=['Vanishing for M by passage to limit asserted, with note of independence from W and W0 smoothness.','Lower dual exact-sequence exponent needs later reading question; preserve plus-like ink.','Low-dimensional n=1 exception explicitly separated.']
save(30,tex,e,d,o)
