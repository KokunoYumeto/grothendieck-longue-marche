from record import save
tex=r'''\scanpage{34}
$V$ une sphère cohomologique
\[\Downarrow\]
\[\left\{\begin{gathered}
H^i(V_{\unsure{\eta|\gamma}})\longrightarrow H^{i-1}(V_s)\quad\text{un \uline{isom} si }\deleted{i,i+1\ne0,2n+1}\\
\inserted{\text{i.e. }i\ne0,2n\deleted{\unsure{+1}}}\\
\text{\uline{et }}\left\{\begin{array}{l}
H^0(V_{\unsure{\eta|\gamma}})\xleftarrow{\sim}\Lambda\\
H^{2n}(W_{\unsure{\eta|\gamma}})\longrightarrow H^{2n-1}(V_s)\quad\mathrm{inj}\text{ et conoyau }\deleted{\unsure{\ne}}\simeq\Lambda\\
\deleted{H^{2n+1}(V_s)\simeq\Lambda}
\end{array}\right.
\end{gathered}\right.\]
\margin{(\unsure{demand} $n\ge1$)}
\margin{$2n+1>n+1$}
\diagram{[\begin{tikzcd}[column sep=small,row sep=small]
\unsure{0}\arrow[r]&H^{2n}W_{\unsure{\eta|\gamma}})\arrow[r]\arrow[d,equals]&H^{2n-1}(V_s)\arrow[r]&H^{2n+1}(V)\arrow[r]&H^{2n+1}(V_{\unsure{\eta|\gamma}})\arrow[r]\arrow[d,equals]&H^{2n}(V_s)\arrow[r]\arrow[d,equals]&0\\
&0&&&0&0\\
&\text{si }n\ge2&&&\text{si }n>1
\end{tikzcd}]}
\diagram{\begin{tikzcd}[row sep=large]
\text{si on suppose de plus que l'on a ``singularité isolée''}\arrow[d,Rightarrow,very thick]\\
H^i(V_s)=0\quad\text{si }i\ne0,n-1,n
\end{tikzcd}}
\margin{$H^i(V_{\unsure{\xi|\bar s}})\xrightarrow{\sim}H^i(V_s)$}
\figure{\begin{tikzpicture}\draw (0,0)--(0,2.4);\end{tikzpicture}}
\margin{\unsure{-}}
\mspage{33}
'''
e=[('text','top','V une sphère cohomologique'),('display','below V','double downward implication'),('display','upper brace','H^i(V_eta) → H^{i-1}(V_s) un isom'),('deletion','upper condition','i,i+1 ne 0,2n+1'),('insertion','under condition','i.e. i ne 0,2n'),('deletion','insertion end','+1'),('display','second brace','H^0(V_eta) ← Lambda'),('display','second brace middle','H^{2n}(W_eta) → H^{2n-1}(V_s)'),('deletion','before simeq Lambda','ne'),('deletion','second brace last','H^{2n+1}(V_s) simeq Lambda'),('margin note','upper right','demand n ge 1'),('margin note','above middle sequence','2n+1>n+1'),('diagram','middle','0 → H^{2n}W_eta) → H^{2n-1}(V_s)'),('diagram','lower','singularité isolée implies vanishing'),('margin note','lower right','H^i(V_xi) ≃ H^i(V_s)'),('drawing','lower right','vertical separating line'),('margin note','below main text left','isolated short dash')]
d=[('generic-point subscript throughout','eta | gamma','Loop with long descending stroke; package comparison required.','medium'),('condition replacement','i ne 0,2n; deleted +1','Last cancelled group overwritten.','low'),('second brace conoyau','deleted ne','Small overwritten relational sign.','low'),('right bracket','demand','Abbreviated or incomplete word before n ge 1.','low'),('middle sequence first term','H^{2n}W_eta)','No opening parenthesis visible; retained.','high'),('lower right map','xi | bar s','Dense three-stroke subscript, distinct from the clear s at target.','low'),('below text left','dash','Isolated ink dash; no readable word.','low')]
o=['V notation replaces W; cohomology-sphere criterion and isolated-singularity vanishing stated, degree restrictions corrected.','Potential comparison to nearby algebraic formalism after freeze; do not infer subscript from context.']
save(34,tex,e,d,o)
