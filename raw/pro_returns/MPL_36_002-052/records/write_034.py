from save_page import save
tex=r'''
\scanpage{34}

2. \uline{Accouplements définis par une biextension}.

2.1. Soit $n$ un entier $>0$, et supposons qu'on a
\[
(2.1.1)\qquad nP=P.
\]
Considérons alors l'homomorphisme composé
\figure{\begin{tikzpicture}\draw (0,0)--(1.5,.08);\draw (.08,-.1)--(1.3,-.05);\end{tikzpicture}}

(2.1.2)
\diagram{\begin{tikzcd}[column sep=large]
\operatorname{Biext}^{\inserted{1}}(P,Q;G) \arrow[r] \arrow[rr,bend left=20,"\phi^n"] & \operatorname{Biext}^{\inserted{1}}(P,{}_nQ;G) \arrow[r,"\sim"] & \operatorname{Hom}({}_nP\otimes{}_nQ;G)
\end{tikzcd}},

où la première flèche est la restriction à $(P,{}_nQ)$, et la deuxième est l'isomorphisme (1.3.6). Il permet, à tout élément $\xi\in\operatorname{Biext}(P,Q;G)$,

(2.1.3)

à fortiori à toute biextension \inserted{$E$} de $(P,Q)$ par $G$, de faire correspondre un\deleted{e \unsure{forme homomorphisme}} accouplement bilinéaire
\margin{$\phi$}
\[
(2.1.4)\qquad\phi_\xi\text{ ou }\phi^n_\xi:{}_nP\times{}_nQ\longrightarrow G,
\]
qu'on appelle l'accouplement \uline{associé à} $\xi$ (ou à la biextension $E$).

2.2. Soit \deleted{\unsure{n}} $n'$ un multiple de $n$,
\[
n'=mn,
\]
et supposons qu'on ait la relation (plus forte que (2.1.1))
\[
(2.2.1)\qquad n'P=P\quad\text{i.e.}\quad mnP=P,
\]
d'où comme en (2.1.4), pour toute $\xi\in\operatorname{Biext}(P,Q;G)$, un\deleted{e} accouplement
\[
\phi^{n'}_\xi:{}_{n'}P\times{}_{n'}Q\longrightarrow G.
\]
\deleted{Les relations entre cet accouplement et}\inserted{Il est lié à} l'accouplement $\phi^n_\xi$ \deleted{est donné} par la commutativité du diagramme suivant (\deleted{qu'on laisse au lecteur le soin d'établir)}\inserted{cf. 2.3 ci-dessous pour une démonstration)}:

(2.2.2)
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
{}_{n'}P \arrow[d,"m"'] & \times & {}_{n'\deleted{\unsure{n}}}Q\deleted{\unsure{Q}} \arrow[d,"m"] \arrow[rr,"\phi^{n'}_\xi"] & & {}_{n'}G \arrow[d,"m"]\\
\deleted{\unsure{P}}{}_nP & \deleted{\unsure{\times}}\times & {}_nQ \arrow[rr,"\phi^n_\xi"] & & {}_nG
\end{tikzcd}},
\inserted{où les flèches verticales sont induites par la multiplication par $m=n'/n$.}

Notons maintenant que moyennant (2.1.1), on peut prendre pour $n'$ n'importe quelle puissance de $n$. En particulier, soit $\ell$ un nombre premier, et supposons que\deleted{\unsure{e}} l'on ait
\margin{$\ell$}
\[
(2.2.3)\qquad\ell P=P,
\]
et considérons le système des accouplements
\margin{33}
'''
e=[('text','readable top title','2. Accouplements définis par une biextension'),('text','2.1 opening','Soit n un entier >0'),('display','(2.1.1)','nP=P'),('text','above composition','Considérons alors l’homomorphisme composé'),('drawing','left above (2.1.2)','two short horizontal marks'),('text','composition number','(2.1.2)'),('diagram','upper quarter composition','Biext^1 -> Biext^1(P,nQ;G) -> Hom(nP tensor nQ;G); phi^n composite'),('insertion','first Biext','1'),('insertion','second Biext','1'),('text','upper paragraph','où la première flèche ... tout élément xi'),('text','beside xi paragraph continuation','(2.1.3)'),('insertion','after biextension','E'),('deletion','before accouplement bilinéaire','e forme homomorphisme'),('margin note','left (2.1.4)','phi in oval'),('display','(2.1.4)','phi_xi ou phi^n_xi:nP x nQ -> G'),('text','below (2.1.4)','qu’on appelle l’accouplement associé à xi'),('text','2.2 opening','Soit n prime un multiple de n'),('deletion','after Soit','n'),('display','2.2 first','n prime=mn'),('text','above (2.2.1)','et supposons qu’on ait la relation'),('display','(2.2.1)','n prime P=P i.e. mnP=P'),('text','below (2.2.1)','d’où comme en (2.1.4), pour toute xi'),('deletion','un accouplement','e'),('display','middle','phi^n prime_xi:n prime P x n prime Q -> G'),('deletion','next paragraph opening','Les relations entre cet accouplement et'),('insertion','above deleted opening','Il est lié à'),('text','middle-lower paragraph','l’accouplement phi^n_xi ... commutativité du diagramme'),('deletion','after phi^n_xi','est donné'),('deletion','parenthetical proof deferral','qu’on laisse au lecteur le soin d’établir)'),('insertion','above proof deferral','cf. 2.3 ci-dessous pour une démonstration)'),('text','square label','(2.2.2)'),('diagram','lower square','n prime P x n prime Q -> n prime G; all vertical maps m'),('deletion','square upper second factor subscript','n'),('deletion','square upper second factor right','Q'),('deletion','square bottom first factor left','P'),('deletion','square bottom product','times'),('insertion','beneath square','où les flèches verticales ... m=n prime/n'),('text','bottom paragraph','Notons maintenant ... n’importe quelle puissance'),('deletion','supposons que l’on','e overtyped'),('margin note','left bottom','ell in oval'),('display','(2.2.3)','ell P=P'),('text','bottom final line','et considérons le système des accouplements'),('margin note','original bottom left','33')]
d=[{'line':'before accouplement bilinéaire','reading':'e forme homomorphisme','alternatives':'x-overtyping makes word endings uncertain','confidence':'medium'},{'line':'2.2 after Soit','reading':'deleted n','alternatives':'overtyped two-character trace','confidence':'low'},{'line':'square upper Q','reading':'deleted n in subscript and Q to right','alternatives':'heavy ink obliterations around rewritten n prime Q','confidence':'low'},{'line':'square bottom P and product sign','reading':'deleted P; deleted times','alternatives':'thick overwriting; prior symbols uncertain','confidence':'low'},{'line':'supposons que l’on','reading':'cancelled e','alternatives':'overtyped extra character','confidence':'low'}]
save(34,tex,e,d,'Upside-down reused typed page, whole and both halves read rotated. Internal title “2. Accouplements définis par une biextension.” Author changes “qu’on laisse au lecteur le soin d’établir” to “cf. 2.3 ci-dessous pour une démonstration”; record as withdrawal of a proof deferral, linked to 032 and 030. Explicit nP=P and n-prime P=P conditions and m=n-prime/n compatibilities. Formula (2.1.3) is inline and encircled, with E insertion and a long annotation line; no missing superscript 1 added to unmarked Biext in that line. Pencil 33.',sheet_kind='reused_typed')
