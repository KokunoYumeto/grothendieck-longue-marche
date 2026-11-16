from page_work import save_page
text=r'''\scanpage{108}
\mspage{107}
\deleted{
\uline{Corollaire} \unsure{4|2}.9.10. Soit $f:X\longrightarrow Y$ un morphisme \deleted{de}
\inserted{de type fini,} \deleted{\unsure{propre}} où $Y$ loc. noeth., $y\in Y$, on suppose
$f$ \unsure{univ.} ouvert en les \unsure{pts} de $X_y$, et $X_y$ séparable.
\deleted{Alors, la fonction $\unsure{y}\mapsto\unsure{\pi_0(y)}$}
\inserted{Pour tt $z\in\unsure{Z|Y}$, soit $\pi(z)=\unsure{\mathrm{nb}^{\mathrm{re}}}$ de}
\unsure{composantes} \unsure{géom} de $X_z$. Alors la fonction
$z\mapsto\unsure{\pi(z)}$ est
\deleted{\unsure{continue} \unsure{en} \unsure{y}}
\inserted{\unsure{continue}}
\unsure{en} \deleted{\unsure{voisinage}} de $y$.
[elle est continue en $y$].

\deleted{La \deleted{\unsure{fonction}} \unsure{définie} \unsure{ci-dessus} est ``$\frac12$ continue
\unsure{semi-inférieurement}'', par la ``\unsure{th.} de connexité''.}

\deleted{\unsure{Il reste} \illegible{4} \unsure{qu'elles sont}
\unsure{les composantes} \unsure{supérieures} \unsure{à} \unsure{ceux}
\unsure{connexes} (\unsure{comme} elles sont \unsure{constr.}).}

Pour \unsure{tout} \unsure{pt} géom $y'$ de $y$,
on a $\pi(y)\geq\pi(y')$. La \unsure{propriété}
\unsure{précitée} nous ramène alors
au cas où $Y$ est le spectre d'un
anneau de valuation discrète, et où
les \unsure{composantes} connexes de $\unsure{X_0},\unsure{X_1|X_\eta}$
\unsure{sont} géométriques. On peut \unsure{ainsi}
\unsure{supposer} $X$ connexe, \unsure{alors}
$\unsure{X_1|X_\eta}$ est connexe,
\deleted{$\unsure{X_0}$ \unsure{a} \unsure{fini}}
donc \deleted{$\pi(\unsure{X_0})$} $\pi(X_1)=1$,
\deleted{\unsure{donc}} \uline{et}
\uline{comme} $X_0\neq\varnothing$, on a fini.
}
\margin{\figure{\begin{tikzpicture}
\draw (0,0)--(0,1.5);\fill (0,0) circle (.04);
\end{tikzpicture}}}
\margin{\figure{\begin{tikzpicture}[scale=.7]
\draw (0,1.5)--(.8,2.1)--(1.7,.7)--(.9,0)--cycle;
\draw[line width=1.4pt] (0,1.5)..controls(.4,1.2)and(.8,1.4)..(1.6,.8);
\draw[line width=1.4pt] (.8,1.3)..controls(.6,.7)and(.1,.4)..(-.2,.1);
\end{tikzpicture}}}
\margin{\figure{\begin{tikzpicture}[scale=.8]
\draw (0,1.7)--(.8,2.7)..controls(1.5,2)and(1.8,.7)..(2.5,.2);
\draw (0,1.7)--(.8,.5);\draw (1.3,.25)--(1.6,-.1)--(2.5,.5);
\draw[line width=1.3pt] (0,1.7)--(.8,2.7);
\draw (0,1.6)--(.7,2.7);\draw (0,1.5)--(.65,2.7);
\draw[line width=1.3pt] (.4,0)..controls(1.6,.6)and(1.8,1.5)..(1.4,1.8);
\draw (-1.3,.95)--(1.45,.95);\fill (1.45,.95) circle (.05);
\node[left] at(-1.3,.95){$X_1\neq\varnothing$};
\node at(.8,1.4){$\unsure{X=\varnothing}$};
\end{tikzpicture}}}
\margin{\figure{\begin{tikzpicture}\draw (0,0) ellipse (.2 and 1.15);\end{tikzpicture}}}
\deleted{\diagram{\begin{tikzcd}[column sep=small,row sep=large]
0\arrow[r]\arrow[dr,dash,bend right=30]&
N\arrow[r,"\unsure{}"]\arrow[d,dash,bend right=20]&
M\arrow[r,dash]\arrow[d,dash,bend right=15]&
M/N\arrow[r,dash]\arrow[d,dash,bend left=25]&0\arrow[dl,dash,bend left=35]\\
0\arrow[r,dash]&N'+N\arrow[r,dash]&M'+M\arrow[r]&P'+P\arrow[r,dash]&0
\end{tikzcd}}}
\margin{\unsure{Lem} \unsure{d'homologie}}
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.5,.3)--(0,.6);\draw (1,0)--(1.4,.3)--(1,.6)--cycle;\end{tikzpicture}}}
'''
text=text.replace('\\arrow[r,"\\unsure{}"]','\\arrow[r]')
save_page(108,text,[('text','original bottom page number','107'),('deletion','whole inverted draft','Corollaire 4.9.10 and proof cancelled by diagonal stroke'),('text','reading top heading','Corollaire 4.9.10'),('text','reading upper paragraph','Soit f:X→Y un morphisme'),('deletion','end first line','de'),('insertion','above second line','de type fini'),('deletion','second line','propre'),('deletion','upper paragraph overwritten sentence','Alors la fonction y maps pi0(y)'),('insertion','above function sentence','Pour tt z in Z soit pi(z)=nbre de'),('text','upper paragraph continuation','composantes géom de Xz'),('deletion','upper function property','continue en y'),('insertion','above cancelled property','continue'),('deletion','upper sentence end','voisinage'),('text','end first block','elle est continue en y'),('deletion','reading middle first cancelled block','La fonction définie ci-dessus est 1/2 continue'),('deletion','same block inner deletion','fonction'),('deletion','reading middle heavily blacked block','Il reste ... quelles sont'),('text','reading lower proof','Pour tout pt géom y prime de y'),('display','within proof','pi(y) >= pi(y prime)'),('text','proof continuation','La propriété précitée nous ramène alors'),('deletion','proof after connexe','X0 a fini'),('deletion','proof pi expression','pi(X0)'),('deletion','proof near end','donc'),('drawing','left reading margin','vertical line with dot at bottom'),('drawing','right reading margin upper','quadrilateral crossed by branching lines'),('drawing','right reading margin lower','curved outlined shape with X1 nonempty and X=empty labels'),('drawing','left reading bottom','long oval'),('diagram','opposite orientation at original top','0 N M M/N 0; 0 Nprime+N Mprime+M Pprime+P 0'),('deletion','opposite orientation diagram','crossed diagram'),('margin note','beside opposite diagram','Lem d’homologie'),('drawing','beside opposite diagram','angle and triangular mark')],sheet_kind='cancelled_draft',observations='The original whole sheet is inverted; the rotated whole and both supplied halves were read, followed by enlarged top, middle, proof and opposite-facing diagram. This is a heavily cancelled and overwritten draft. Many lexical readings are uncertain, and four blacked-out words remain physically unreadable. The comparison pi(y)>=pi(y prime) is read from its ink. No completion of the mathematical statement has been supplied. Figure labels, the opposite-facing diagram, oval and marginal strokes are preserved.')
