from save_page import save
tex=r'''
\scanpage{39}

$X$ propre et simple sur $k$ [\unsure{généralisons|généralisable} à une base quelconque]

$A$ V.A. sur $k$

$H^1(X,A)=\underset{n}{\varinjlim}\ {}_nH^1(X,A)$ \deleted{$\unsure{=}$} d'autre part on a une suite exacte
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r] & \operatorname{Hom}(X,A)_n \arrow[r] & \deleted{\unsure{n}}H^1(X,{}_nA) \arrow[r] & {}_nH^1(X,A) \arrow[r] & 0
\end{tikzcd}}
qui s'écrit aussi
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r] & \operatorname{Hom}(\operatorname{Alb}_X,A)_n \arrow[r] & \operatorname{Hom}(D({}_nA),\operatorname{Pic}_X) \arrow[r] & {}_nH^1(X,A) \arrow[r] & 0
\end{tikzcd}}

ou encore, sachant que
\[
\operatorname{Hom}(\operatorname{Alb}_X,A)\simeq\operatorname{Hom}(A',(\operatorname{Alb}_X)')=\operatorname{Hom}(A',\operatorname{Pic}_X^0)
\]
\[
D({}_nA)\simeq{}_nA'
\]
une suite exacte

$(*)$
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r] & \operatorname{Hom}(A',\operatorname{Pic}_X^{\unsure{0}})_n \arrow[r] & \operatorname{Hom}({}_nA',\operatorname{Pic}_X) \arrow[r] & {}_nH^1(X,A) \arrow[r] & 0
\end{tikzcd}}
et passant à la limite \inserted{\unsure{inductive}} on a :
\diagram{\boxed{\begin{tikzcd}[column sep=small]
0 \arrow[r] & \operatorname{Hom}(A',\underline{\operatorname{Pic}}_X^0)\otimes_{\mathbf Z}\mathbf Q \arrow[r] & \operatorname{Hom}(T_{\unsure{\cdot}}(A'),\underline{\operatorname{Pic}}_X) \arrow[r,no head] & H^1(X,A) \arrow[r] & 0
\end{tikzcd}}}

Or la suite exacte $(*)$ se compare à la suite exacte déduite de
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r,no head] & {}_nA' \arrow[r,no head] & A' \arrow[r] & A' \arrow[r] & 0
\end{tikzcd}}
en appliquant $\deleted{\operatorname{Ext}}\underline{\operatorname{Hom}}(-,\operatorname{Pic}_X)$, on \unsure{trouve}

$(**)$
\diagram{\begin{tikzcd}[column sep=small]
0 \arrow[r,no head] & \operatorname{Hom}(A',\underline{\operatorname{Pic}}_X)_n \arrow[r] & \operatorname{Hom}({}_nA',\underline{\operatorname{Pic}}_X) \arrow[r] & {}_n\operatorname{Ext}^1(A',\underline{\operatorname{Pic}}_X^{\unsure{0|2}}) \arrow[r] & 0
\end{tikzcd}}
qui donne à la limite
\diagram{\boxed{\begin{tikzcd}[column sep=small,row sep=tiny]
0 \arrow[r,no head] & \operatorname{Hom}(A',\operatorname{Pic}_X)\otimes_{\mathbf Z}\mathbf Q \arrow[r] & \operatorname{Hom}(T_{\unsure{\cdot}}(A'),\operatorname{Pic}_X) \arrow[r,no head] & \operatorname{Ext}^1(A',\operatorname{Pic}_X) \arrow[d,bend left=25]\\
 & & & 0
\end{tikzcd}}}
\margin{38}
'''
e=[('text','top hypotheses','X propre et simple sur k [généralisons à une base quelconque]'),('text','second hypothesis','A V.A. sur k'),('display','upper line','H^1(X,A)=lim_n nH^1(X,A)'),('deletion','after upper equality','equals-like mark'),('text','upper right','d’autre part on a une suite exacte'),('diagram','upper first sequence','0 -> Hom(X,A)_n -> H^1(X,nA) -> nH^1(X,A) -> 0'),('deletion','before H^1 in first sequence','n'),('text','below first sequence','qui s’écrit aussi'),('diagram','upper second sequence','0 -> Hom(Alb_X,A)_n -> Hom(D(nA),Pic_X) -> nH^1 -> 0'),('text','middle connective','ou encore, sachant que'),('display','middle Hom duality chain','Hom(Alb_X,A) ~= Hom(A prime,(Alb_X) prime)=Hom(A prime,Pic_X^0)'),('display','middle duality','D(nA) ~= nA prime'),('text','above (*)','une suite exacte'),('text','left (*)','(*)'),('diagram','(*)','0 -> Hom(A prime,Pic_X^0)_n -> Hom(nA prime,Pic_X) -> nH^1 -> 0'),('text','before first box','et passant à la limite ... on a'),('insertion','above limite on a','inductive'),('diagram','first boxed sequence','0 -> Hom(A prime,Pic_X^0) tensor Q -> Hom(T_dot(A prime),Pic_X) - H^1 -> 0'),('text','lower comparison paragraph','Or la suite exacte (*) se compare à la suite exacte déduite de'),('diagram','lower short sequence','0 - nA prime - A prime -> A prime -> 0'),('text','above (**)','en appliquant underline Hom(-,Pic_X), on trouve'),('deletion','before Hom','Ext'),('text','left (**)','(**)'),('diagram','(**)','0 - Hom(A prime,Pic_X)_n -> Hom(nA prime,Pic_X) -> nExt^1(A prime,Pic_X^0) -> 0'),('text','before last box','qui donne à la limite'),('diagram','last boxed sequence','0 - Hom(A prime,Pic_X) tensor Q -> Hom(T_dot(A prime),Pic_X) - Ext^1 -> 0 below right edge'),('margin note','bottom left','38')]
d=[{'line':'top bracket','reading':'généralisons','alternatives':'généralisable; ending compressed','confidence':'medium'},{'line':'after first direct-limit equality','reading':'deleted equals','alternatives':'short ink obliteration','confidence':'low'},{'line':'first exact sequence before H^1','reading':'deleted n','alternatives':'small overstruck prefix','confidence':'low'},{'line':'(*) Pic superscript','reading':'0','alternatives':'filled superscript blob','confidence':'medium'},{'line':'insertion above first box','reading':'inductive','alternatives':'ending letters run together','confidence':'medium'},{'line':'both boxed sequences T index','reading':'dot','alternatives':'small lower point, not an l; no expansion to Tate symbol beyond ink','confidence':'medium'},{'line':'end of comparison sentence','reading':'trouve','alternatives':'tire; faint word','confidence':'low'},{'line':'(**) final Pic superscript','reading':'0','alternatives':'2; compact superscript unclear','confidence':'low'},{'line':'last box terminal arrow and zero','reading':'downward-bent arrow to 0','alternatives':'partly at page edge; zero on lower baseline','confidence':'medium'}]
save(39,tex,e,d,'Proper simple X and an abelian variety A over k; bracket proposes generalizing to an arbitrary base. Compares Kummer/Albanese/Picard torsion sequences and their inductive limits with the Ext sequence from nA prime. Uses T with a lower dot, not silently T_l. Potential key programme: compare H^1(X,A) and Ext^1(A prime,Pic_X); source has differing Pic superscripts/underlines and headless segments preserved. No complete commutative comparison diagram or proof is given on this sheet. Final arrow to zero turns down at right edge. Pencil 38.')
