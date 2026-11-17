from record import save
save(7,r'''
\scanpage{7}
$W$ variété \deleted{\unsure{par}}

$P\subset W$ sous-variété à bord telle que $P=\overline{\mathring P}$.

Soit $Q=P-\mathring P$.

Alors $Q$ est une sous-variété à bord satisfaisant $Q=\overline{\mathring Q}$, et
\[
\unsure{\alpha}\qquad W=P\cup Q,\qquad P\cap Q=\partial P=\partial Q.
\]
Si $W$ est purement de \unsure{dim|codim} $n$, alors $P$ et $Q$ aussi, et $P\cap Q=\partial P=\partial Q$ est purement de \unsure{dim|codim} $n-1$.

Soit $R=\partial P=\partial Q$. On \deleted{\unsure{précisera}} a donc
\[
W-R=\mathring P\amalg\mathring Q.
\]
\[
\deleted{\unsure{H^i(W)}\longrightarrow\unsure{H^i(W,F)}}
\]
La suite exacte de coh. relative pour $W,R,W-R$ donne
\margin{\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&&\mathring Q\arrow[d]\\
&W\arrow[r]\arrow[d]&Q\arrow[d]\\
\mathring P&P\arrow[l]\arrow[r]&P\cap Q=\unsure{R}\arrow[d,phantom,"="{rotate=90}]\\
&&\partial P=T
\end{tikzcd}}}
\diagram{\begin{tikzcd}[column sep=small]
\cdots\arrow[r]&H^i(W,F)\arrow[r]&H^i(W-R,F)\arrow[r]\arrow[d,phantom,"="{rotate=90}]&H^{\unsure{i}}(R,F\otimes\unsure{\mathcal T|\tau}_{T/W})\arrow[r]&H^{i+1}(W,F)\\
&&H^i(\mathring P)\times H^i(\mathring Q)\arrow[d,phantom,"="{rotate=90}]\\
&&H^i(P)\times H^i(Q)
\end{tikzcd}}
\margin{faisceau d'orientation normale à $T$ dans $W$, ici $\simeq\mathbf Z_T$}

Cette suite exacte relative n'est sans doute autre que la suite exacte de Mayer-Vietoris associée à $\unsure{\alpha}$,

On a aussi [\unsure{en faisant} transposée]
\diagram{\begin{tikzcd}[column sep=small]
\cdots\arrow[r]&H_!^i(W-\unsure{T},F)\arrow[r]\arrow[d,phantom,"\simeq"{rotate=90}]&H_!^i(W,F)\arrow[r]&H_!^i(R,F)\arrow[r]&\cdots\\
&H_!^i(\mathring P,F)\times H_!^i(\mathring Q,F)\arrow[d,phantom,"\simeq"{rotate=90}]\\
&H^{n-i}(\mathring P,F^\vee\otimes\unsure{\mathcal T|\tau}_W)^\vee\times H^{n-i}(\mathring Q,F^\vee\otimes\unsure{\mathcal T|\tau}_W)^\vee\arrow[d,phantom,"\simeq"{rotate=90}]\\
&H^{n-i}(P,F\otimes\unsure{\mathcal T|\tau}_W)^\vee\times H^{n-i}(\unsure{Q|R},F^\vee\otimes\unsure{\mathcal T|\tau}_W)^\vee
\end{tikzcd}}
\mspage{6}
''',[
('text','top','W variété'),('deletion','top','par'),('text','upper','P subset W sous-variété'),('text','upper','Soit Q=P-interior P'),('text','upper','Alors Q est une sous-variété'),('display','upper','alpha W=P union Q; P intersection Q'),('text','upper middle','Si W est purement'),('text','middle','Soit R=boundary P=boundary Q'),('deletion','middle','précisera'),('display','middle','W-R=interior P disjoint union interior Q'),('deletion','middle','H^i(W) to H^i(W,F)'),('text','middle','La suite exacte de coh. relative'),('margin note','left middle','W P Q diagram'),('diagram','left middle','Q interior to Q; W P Q and intersection'),('diagram','middle','relative exact sequence and ordinary cohomology products'),('margin note','right middle','faisceau d’orientation normale'),('text','lower middle','Cette suite exacte relative n’est sans doute'),('text','lower middle','On a aussi en faisant transposée'),('diagram','lower','compact-support sequence and three product duality identifications'),('text','bottom left','6')],
[('line 1 deleted word','par','Only initial p and dense horizontal cancellation remain.','low'),('definition of Q','P minus interior P','The first letter reads P, not W; this is retained despite the later decomposition.','high'),('dimension sentence','dim','codim; long initial stroke ambiguous.','medium'),('after Soit R','précisera','Cancelled word partly overlaid.','low'),('orientation sheaf, repeated','calligraphic T','tau; same looped handwritten sign retained consistently here.','medium'),('relative sequence third term exponent','i','Overwritten addition or cancellation adjacent to exponent; no secure extra digit.','low'),('after Mayer-Vietoris','alpha','Reference symbol matches the mark beside W=P union Q.','medium'),('square-bracket phrase','en faisant transposée','Abbreviated/compressed initial words.','medium'),('last sequence first object','W-T','W-R; letter is faint and narrower than most R’s.','medium'),('last line second space','Q','R; heavy overwritten letter.','low'),('last line first coefficient','F without dual sign','No vee visible over first F; do not harmonize with preceding line.','high')],
['Self-flagged expectation: n’est sans doute autre que la suite exacte de Mayer-Vietoris.','Q=P-interior P as actually written conflicts with later W=P union Q; research reading question only.','Orientation normal to T in W claimed trivial; compact-support transposition and coefficient conventions need proof/check.'])
