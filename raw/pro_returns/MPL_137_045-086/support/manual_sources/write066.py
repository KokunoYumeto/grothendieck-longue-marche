import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{66}
% archive foliation: 65
$P_*$ avec $P^*$ est compatible aux $\otimes$.

Soit $B$ une cat. $(k-)$additive avec op. $(k-)$bil. $\otimes$ \inserted{(propriété du foncteur $\otimes$)} \uline{muni} d'une contrainte d'ass, d'unité, et de comm. \deleted{\unsure{les}} \inserted{(données)}, \unsure{satisf.} aux compatibilités habituelles (propriété). Soit $B'$ une autre telle. Si on a un foncteur $(k-)$additif (propriété)
\[
F:B'\longrightarrow B
\]
on appelle \uline{structure multiplicative sur $F$} des hom de foncteurs
\[
F(X)\otimes F(Y)\xrightarrow{u_{X,Y}}F(X\otimes Y)
\]
et un \deleted{$\unsure{F(1)\longrightarrow}$} $\mathbf1_B\xrightarrow{\alpha}F(\mathbf1_{B'})$ qui sont compatibles aux données d'ass, d'unité de comm.

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
(F(X)\otimes F(Y))\otimes F(Z) \arrow[r,"{u_{X,Y}\otimes F(Z)\ \deleted{\unsure{u}}}"] \arrow[d,"{a^B_{F(X),F(Y),F(Z)}}","\sim"'] & F(X\otimes\deleted{\unsure{F(}}Y\deleted{\unsure{)}})\otimes F(Z) \arrow[d,"{u_{X\otimes Y,Z}}"]\\
F(X)\otimes(F(Y)\otimes F(Z)) \arrow[d,"{F(X)\otimes u_{Y,Z}}"] \arrow[r,phantom,"{\text{comm}}"] & F((X\otimes Y)\otimes Z) \arrow[d,no head,"{F(a^{B'}_{X,Y,Z})}","\sim"']\\
F(X)\otimes F(Y\otimes Z) \arrow[r,"{u_{X,Y\otimes Z}}"'] & F(X\otimes(Y\otimes Z))
\end{tikzcd}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.15) .. controls (1,-.15) and (2,.05) .. (3,0) .. controls (4,-.2) and (5,.2) .. (6,.35);\end{tikzpicture}}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
F(X)\otimes\mathbf1_B \arrow[r,"{F(X)\otimes\alpha}"] \arrow[ddr,"{\unsure{\delta^B_{F(X)}|\beta^B_{F(X)}}}"',"\sim"] & F(X)\otimes F(\mathbf1_{B'}) \arrow[d,"{u_{X,\mathbf1_{B'}}}"]\\
\text{comm} & F(X\otimes\mathbf1_{B'}) \arrow[d,"{F(\unsure{\delta_X^{B'}|\beta_X^{B'}})}","\sim"']\\
& F(X)
\end{tikzcd}}
et symétrique

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
F(X)\otimes F(Y) \arrow[r,"{u_{X,Y}}"] \arrow[d,"{\sigma^B_{F(X),F(Y)}}"'] & F(X\otimes Y) \arrow[d,"{F(\sigma^{B'}_{X,Y})}"]\\
F(Y)\otimes F(X) \arrow[r,no head,"{u_{Y,X}}"] \arrow[ur,phantom,"{\text{comm}}" description] & F(Y\otimes X)

\end{tikzcd}}'''
e=[('text','top','P* avec P^* est compatible aux ⊗'),('text','upper','Soit B une cat. (k-)additive'),('insertion','upper','propriété du foncteur ⊗'),('deletion','upper','les'),('insertion','upper','données'),('display','upper middle','F:B′→B'),('text','middle','on appelle structure multiplicative sur F'),('display','middle','F(X)⊗F(Y)→F(X⊗Y)'),('deletion','middle','F(1)→'),('text','middle','et un 1B→F(1B′)'),('diagram','middle/lower','associativity hexagon'),('deletion','associativity diagram top arrow','u'),('deletion','associativity diagram upper right','F('),('deletion','associativity diagram upper right',')'),('drawing','lower middle','curved separator'),('diagram','lower','unit compatibility triangle'),('text','right lower','et symétrique'),('diagram','bottom','symmetry compatibility square')]
save(66,text,e)
