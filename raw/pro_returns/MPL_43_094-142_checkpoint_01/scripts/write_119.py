from page_work import save_page
text=r'''\scanpage{119}
\[
\underline{\operatorname{Ext}}^i(A,\mu_\infty)=
\left\{\begin{array}{l}0\\{}_\infty B\\0\\0\end{array}\right.
\]
\[
\underline{\underline{\operatorname{Ext}}}^i(A,\mu_\infty)\simeq H^{i-1}(K,{}_\infty B)
=\left\{\begin{array}{l}0\\H^0(K,{}_\infty B)\\H^1(K,{}_\infty B)^{\unsure{\times}}\\0\end{array}\right.
\]
\[
H^i(K,A)=\left\{\begin{array}{l}A(K)^{\unsure{\times}}\\H^1(K,A)\\\unsure{\oplus|0}\\0\\0\end{array}\right.
\]
\[
\deleted{B\qquad H^1(K,{}_\infty B)\longrightarrow H^1(K,B)\mathrel{-}0}
\]
\[
0\longrightarrow H^0(K,B)\unsure{\otimes\mathbb Q/\mathbb Z}\mathrel{-}
H^1(K,{}_\infty B)\longrightarrow H^1(K,B)\mathrel{-}0
\]
\deleted{$H^1(K,A)\longrightarrow$}
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
0\arrow[r,dash]&H^0(K,{}_\infty B)\arrow[r]&DH^1(K,A)\arrow[r]\arrow[d,equal]
\arrow[dr,bend left=40]&\deleted{H^1(K,{}_\infty B)}&\\
&&H^0(K,B)&\inserted{H^0(K,B)\otimes\mathbb Q/\mathbb Z}\arrow[dl,bend right=40]&\\
&&H^1(K,{}_\infty B)\arrow[r]&DH^0(K,A)\arrow[r]\arrow[d,equal]&0\\
&&&H^1(K,B)&
\end{tikzcd}}
\figure{\begin{tikzpicture}[x=.7cm,y=.6cm]
\draw (0,4)--(12,4);\draw(.4,3.9)--(.45,1.5)..controls(.45,.9)and(.8,.8)..(1.7,.8)
--(5,.8)..controls(6,.8)and(7,.7)..(7,.3)..controls(7,-.1)and(9,0)..(12,-.5);
\end{tikzpicture}}
\[
0\mathrel{-}H^0(K,{}_\infty B)\mathrel{-}DH^1(K,A)\longrightarrow Q\mathrel{-}0
\]
\[
0\mathrel{-}N\mathrel{-}H^1(K,{}_\infty B)\mathrel{-}DH^0(K,A)\mathrel{-}0
\]
\[
\deleted{Q:\ \deleted{H^1(K,B)}\ \operatorname{Ker}\ H^0(K,B)\longrightarrow
H^0(K,B)\otimes\mathbb Q/\mathbb Z}
\]
\[
Q\subset N\qquad H^0(K,B)\longrightarrow H^0(K,B)\otimes\mathbb Q/\mathbb Z
\]
\mspage{118}
'''
save_page(119,text,[('display','top first cases','underlinedExt i(A,mu infinity)=0 infinityB 0 0'),('display','upper second cases','double-underlinedExt i(A,mu infinity) ≃ Hi-1(K,infinityB)'),('display','upper middle cases','H i(K,A)=A(K),H1(K,A),oplus,0,0'),('deletion','upper middle right sequence','B H1(K,infinityB)→H1(K,B)-0'),('display','middle left sequence','0→H0(K,B)tensorQ/Z-H1(K,infinityB)→H1(K,B)-0'),('deletion','middle above large region','H1(K,A)→'),('diagram','lower large revised sequence','0-H0(K,infinityB)→DH1(K,A)→H0(K,B)tensorQ/Z→H1(K,infinityB)→DH0(K,A)→0'),('deletion','lower diagram first target','H1(K,infinityB)'),('insertion','lower diagram replacement target','H0(K,B)tensorQ/Z'),('drawing','lower enclosing and dividing curve','long horizontal line and bent lower boundary'),('display','lower left sequence','0-H0(K,infinityB)-DH1(K,A)→Q-0'),('display','lower middle sequence','0-N-H1(K,infinityB)-DH0(K,A)-0'),('deletion','bottom Q definition','Q: H1(K,B) Ker H0(K,B)→H0(K,B)tensorQ/Z'),('deletion','nested bottom Q term','H1(K,B)'),('display','bottom left','Q subset N'),('display','bottom right repeated map','H0(K,B)→H0(K,B)tensorQ/Z'),('text','bottom left page number','118')],observations='Whole and both halves read. The left infinity subscript on B is retained in every occurrence, separately from mu infinity. Single/double underlines are distinct. The isolated cross-shaped marks at the ends of two case entries and the overwritten circled symbol in the H cases are doubtful rather than normalized. Curved revision arrows and two vertical equality signs in the large diagram are reproduced. Source dashes are retained without supplying arrowheads.')
