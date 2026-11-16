from page_work import save_page
text=r'''\scanpage{120}
\[
\underline{\operatorname{Ext}}^i(A,{}_n\mu)=\left\{\begin{array}{l}0\\{}_nB\\0\\0\end{array}\right.
\]
\margin{$\mathbb Z/n\mathbb Z\qquad B$}
\diagram{\begin{tikzcd}[row sep=small]
\underline{\underline{\operatorname{Ext}}}^i(A,{}_n\mu)\simeq H^{i-1}(K,{}_nB)\\[-1ex]
\unsure{\wr}\\[-1ex]
\operatorname{Ext}^{i-1}(T(A),\mathbb Z/n\mathbb Z)
\end{tikzcd}}
\[
H^i(K,{}_nB)\xrightarrow{\sim}\operatorname{Ext}^i_{k\text{-gr}}(T(A),\mathbb Z/n\mathbb Z)
\]
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
H^i(K,{}_\infty B)\simeq\operatorname{Ext}^i_{k\mathrm{gr}}(&T(A)\arrow[d,leftrightarrow],&\mathbb Q/\mathbb Z)\\
&\mathcal A&H^1(K,A)
\end{tikzcd}}
\[
{}_nB(K),H^1(K,{}_nB),0\mathrel{-}\mathrel{-}\ \big|\qquad
[\text{dual de }H^1(K,{}_nA)]
\]
\figure{\begin{tikzpicture}[x=.7cm,y=.7cm]
\draw[line width=1.8pt,-stealth](0,.3)--(-.2,0)--(3,0);
\node[below]at(1.6,-.3){$V\times\deleted{\unsure{\mathbb Z}}D\mathrel{-}\uline{discrète}$};
\end{tikzpicture}}
\figure{\begin{tikzpicture}[x=.9cm,y=.9cm]
\draw[->](-.7,0)--(1.8,0)node[below]{$p$};
\draw[->](0,-2.7)--(0,.8)node[above]{$q$};
\draw(1.3,.65)--(1.3,-3);\draw(-.7,-1.4)--(1.65,-1.4);
\fill(0,-1.4)circle(2pt);\fill(1.3,-1.4)circle(2pt);
\node[above right]at(1.4,.2){$\operatorname{Ext}^1(\mathcal A,\mathbb Z/n\mathbb Z)$};
\draw(1.5,.55)..controls(2,1.7)and(5.6,1.7)..(5.7,.6)..controls(5.9,-.3)and(4,-1)..(1.5,-.4)..controls(.7,-.2)and(.6,.15)..(.9,.4);
\node[left]at(0,-.45){${}_n\Delta(\pi_0(\mathcal A))$};
\node[below left]at(0,-1.5){$\deleted{\unsure{H^1(K,A)}}$};
\node[below left]at(.1,-2.3){${}_n\Delta(H^1(K,A)')$};
\node[below right]at(1.4,-1.5){$\Delta(H^1(K,A)')_n=\Delta({}_nH^1(K,A))$};
\end{tikzpicture}}
\noindent $1^\circ)$ la partie discrète de $H^1(K,A)$ est \uuline{divisible}

\noindent $2^\circ)$
\[
0\mathrel{-}\mathbb Z/n\mathbb Z\mathrel{-}\mathbb Q/\mathbb Z\overset{n}{\mathrel{-}}\mathbb Q/\mathbb Z\mathrel{-}0
\]
\noindent (i) $H^1(K,A)'$ divisible, i.e. $\Delta H^1(K,A)'$ \deleted{$\unsure{a\mathbb Z}$} \inserted{sans torsion}

\noindent (ii) $H^1(K,{}_nB)\xrightarrow{\sim}\operatorname{Ext}^1_{k\mathrm{gr}}(\mathcal A,\mathbb Z/n\mathbb Z)$
\margin{?}

\noindent (iii) $n$
\mspage{119}
'''
save_page(120,text,[('display','top cases','underlinedExt i(A,nmu)=0 nB 0 0'),('margin note','upper right','Z/nZ B'),('diagram','upper second and third displays','doubleunderlinedExt i ≃ Hi-1(K,nB), vertical wr, Exti-1(T(A),Z/nZ)'),('display','upper middle','Hi(K,nB)→Exti k-gr(T(A),Z/nZ)'),('diagram','middle','Hi(K,infinityB)≃Exti kgr(T(A),Q/Z), T(A)↔scriptA, H1(K,A)'),('display','middle left','nB(K),H1(K,nB),0--| [dual de H1(K,nA)]'),('drawing','middle right heavy bar and label','V times deletedZ D-discrète'),('deletion','middle right factor','Z'),('drawing','lower left coordinate grid and oval','p q; Ext1(scriptA,Z/nZ); nDelta(pi0A); nDelta(H1(K,A)prime); Delta(...)n=Delta(nH1(K,A))'),('deletion','lower left graph label','H1(K,A)'),('text','lower right first item','1° la partie discrète de H1(K,A) est divisible'),('text','lower right empty second item','2°'),('display','lower short sequence','0-Z/nZ-Q/Z-n-Q/Z-0'),('text','bottom item i','H1(K,A)prime divisible i.e. Delta H1(K,A)prime sans torsion'),('deletion','bottom item i end','aZ'),('insertion','bottom item i above end','sans torsion'),('display','bottom item ii','H1(K,nB)→Ext1 kgr(scriptA,Z/nZ)'),('margin note','bottom right','?'),('text','bottom unfinished item iii','(iii) n'),('text','bottom left page number','119')],observations='Whole and both halves read, with enlarged coordinate-graph labels. The degree shifts in the first three displays are retained separately from the later degree-i identities. Graph labels distinguish left n and right n, and retain the prime after H1. Vertical isomorphism sign and blacked-out math carry explicit proposed readings; no symbols are replaced by illegible. The final item is unfinished after n.')
