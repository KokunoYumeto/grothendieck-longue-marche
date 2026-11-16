from save_page import save
tex=r'''
\scanpage{31}

Supposons $j$ et $j'$ ainsi \unsure{choisis}. Si $j,j'$ sont injectifs, on en déduit une biextension \inserted{canonique} de $(A,A')$, où $A=G/M$, $A'=G'/M'$. Dans le cas général, posons

\deleted{pour dire qu'on a une biextension de}
\[
A=\left[\underset{\text{deg.}\,-1}{M}\longrightarrow\underset{\text{deg}\,0}{G}\right]\ ;\qquad
A'=\left[M'\mathbin{-}G'\right].
\]

d'où
\diagram{\begin{tikzcd}[row sep=small,column sep=small]
 & & A \arrow[dl,"1"'] & & & & A' \arrow[dl,"1"'] & \\
\phantom{0} & M \arrow[l,no head] \arrow[r] & G \arrow[u] \arrow[r,no head] & \phantom{0} & \text{\unsure{cônes de morphismes}} & M' \arrow[l,no head] & G' \arrow[u] \arrow[l,no head] &
\end{tikzcd}}

on va définir une \deleted{\unsure{biextension}} classe canonique
\[
\xi\in\operatorname{Ext}^1(A\mathbin{\overset{L}{\otimes}}A',G_m),
\]
jouant le rôle d'une biextension de $(A,A')$ par $G_m$.

Soit en effet \unsure{\ldots}
\margin{\unsure{pourquoi ?}}
\figure{\begin{tikzpicture}\draw (0,2.4) .. controls (-.18,1.6) and (-.2,.5) .. (0,.25) .. controls (.2,.05) and (.17,-.12) .. (.06,-.2);\end{tikzpicture}}

\unsure{Soit}
\[
{}_nA\overset{\text{déf}}{=}\deleted{\unsure{R}}\underline{\operatorname{Ext}}^0(\mathbf Z/n\mathbf Z,A),\qquad
{}_nA'=\underline{\operatorname{Ext}}^0(\mathbf Z/n\mathbf Z,A')
\]
on trouve, \unsure{grâce, par} aux triangles plus haut,
\margin{\deleted{\uline{\unsure{et}}}}
\[
\left\{\begin{aligned}
{}_nM&=0\quad\deleted{\unsure{{}_nM'=0}}\quad\inserted{\unsure{resp.}}\\
nG&=G\quad\text{puisque}\quad\deleted{\unsure{par}}\ nB=B,\ nT=T\quad(\text{ce dernier résulte de }{}_nM'=0
\end{aligned}\right.
\]

\margin{donne aussi autre \unsure{interprét\textsuperscript{tion}} de ${}_nA$, via hom. cobord si $nG=G$}
\figure{\begin{tikzpicture}\draw (0,0)--(0,1.7);\end{tikzpicture}}
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r] & \underset{\underbrace{\vphantom{G}}_{(D(M'_n),{}_nB),\ \text{si }nT=T}}{ {}_nG} \arrow[r] & {}_nA \arrow[r] & M_n \arrow[r] & 0
\end{tikzcd}}

et \unsure{on a de $\widehat{\mathrm m}$} une suite exacte
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r] & {}_nG' \arrow[r] & {}_nA' \arrow[r] & M'_n \arrow[r] & 0
\end{tikzcd}}

sous les hyp. duales; passant à la limite sur $n=\ell^\nu$, on a
\[
\left\{\begin{gathered}
\begin{tikzcd}[column sep=small]0 \arrow[r] & T_\ell(\unsure{G}) \arrow[r,no head] & T_\ell(A) \arrow[r] & M\otimes\mathbf Z_\ell \arrow[r,no head] & 0\end{tikzcd}\\
\begin{tikzcd}[column sep=small]0 \arrow[r,no head] & T_\ell(\unsure{A'|G'}) \arrow[r,no head] & T_\ell(A') \arrow[r,no head] & M'\otimes\mathbf Z_\ell \arrow[r] & 0\end{tikzcd}
\end{gathered}\right.
\]
\margin{30}
'''
e=[('text','top three lines','Supposons j et j prime ainsi choisis'),('insertion','top above de','canonique'),('deletion','above complexes','pour dire qu’on a une biextension de'),('display','upper quarter','A=[M -> G]; A prime=[M prime - G prime]'),('text','left of triangles','d’où'),('diagram','upper middle','A,M,G and A prime,M prime,G prime; degree 1 arrows'),('text','middle','on va définir une classe canonique'),('deletion','middle before classe','biextension'),('display','middle','xi in Ext^1(A tensor^L A prime,G_m)'),('text','below Ext display','jouant le rôle d’une biextension'),('text','middle abandoned line','Soit en effet ...'),('margin note','left middle slanted','pourquoi ?'),('drawing','left middle beside question','long curved brace'),('text','lower half opening','Soit'),('display','lower half definitions','nA def=Ext^0(Z/nZ,A); nA prime=Ext^0(Z/nZ,A prime)'),('deletion','first Ext operator overstrike','R uncertain'),('text','above divisibility brace','on trouve ... aux triangles plus haut'),('margin note','left of divisibility brace','et crossed and underlined'),('deletion','left of brace','et'),('display','lower half brace','nM=0; nG=G puisque nB=B,nT=T'),('deletion','first brace row','nM prime=0'),('insertion','above cancelled first brace row','resp. circled'),('deletion','second brace row before nB','par'),('margin note','left lower slanted','donne aussi autre interprét ... de nA via hom. cobord'),('drawing','beside lower marginal note','vertical separator'),('diagram','lower half first exact sequence','0 -> nG -> nA -> M_n -> 0; annotation D(M prime_n),nB'),('text','between first and second sequences','et ... une suite exacte'),('diagram','lower half second exact sequence','0 -> nG prime -> nA prime -> M prime_n -> 0'),('text','above final brace','sous les hyp. duales; passant à la limite'),('diagram','bottom first row','0,T_l(G),T_l(A),M tensor Z_l,0'),('diagram','bottom second row','0,T_l(A prime),T_l(A prime),M prime tensor Z_l,0'),('margin note','bottom left','30')]
d=[{'line':'1','reading':'choisis','alternatives':'donnés; heavily abbreviated strokes','confidence':'low'},{'line':'between triangles','reading':'cônes de morphismes','alternatives':'two faint short lines; whole phrase uncertain','confidence':'low'},{'line':'below Ext display','reading':'Soit en effet ...','alternatives':'following strokes may be abandoned word traces','confidence':'low'},{'line':'left middle','reading':'pourquoi ?','alternatives':'slanted faint question','confidence':'medium'},{'line':'torsion definition','reading':'deleted R before Ext^0','alternatives':'overwritten operator trace','confidence':'low'},{'line':'above divisibility brace','reading':'grâce, par','alternatives':'faint connective words unresolved','confidence':'low'},{'line':'above cancelled nM prime','reading':'resp.','alternatives':'circled insertion difficult','confidence':'low'},{'line':'left lower margin','reading':'interprét superscript tion','alternatives':'abbreviated ending; cannot confidently distinguish all letters','confidence':'low'},{'line':'between exact sequences','reading':'on a de m-hat','alternatives':'faint phrase beneath inserted annotation','confidence':'low'},{'line':'final first sequence','reading':'G; plain strokes between some objects','alternatives':'overwritten first object and incomplete arrowheads','confidence':'medium'},{'line':'final second sequence first T object','reading':'A prime','alternatives':'G prime; preserve first reading despite repeated A prime','confidence':'medium'}]
save(31,tex,e,d,'Defines A=[M→G] and A prime with degrees −1,0, then a class xi in Ext^1 of their derived tensor; proposes its role as a biextension. Abandoned proof line “Soit en effet ...” with a marginal “pourquoi ?” and brace is a self-flag requiring a note. Torsion objects, divisibility hypotheses, two exact sequences, and Tate-limit sequences follow; lower margin gives another interpretation through the coboundary if nG=G. Ink reads A prime at the first T object of the final second row, retained with G prime as alternative. Complex right-hand stroke and several final sequence strokes have no visible arrowhead. Verso typescript is show-through, not front text.')
