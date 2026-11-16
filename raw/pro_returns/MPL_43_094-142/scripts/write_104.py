from page_work import save_page
text=r'''\scanpage{104}
\diagram{\begin{tikzcd}k&V\arrow[l]\arrow[r]&K\end{tikzcd}}
\margin{\uuline{parfait} ?}
\diagram{\begin{tikzcd}[column sep=large]
\mathcal K\operatorname{Gr}_K\arrow[d,"T"'] &
\text{complexes finis de \deleted{\unsure{quasi}} $K$-groupes \deleted{\unsure{alg}}}\\
\mathcal K\operatorname{QuGr}_k & \text{complexes finis de $k$-quasi-groupes}
\end{tikzcd}}
\margin{\deleted{$\unsure{T^0}$}}
\margin{[Coh de $K$. \uline{ne se calcule pas} galoisiennement]}
\margin{[Coh. de $k$ se calcule galoisiennement, \deleted{\unsure{et}}
ne change pas en remplaçant $k$ par une clôture \unsure{parfaite}]}
\[
T(G)=T^0_{\unsure{a}}e(G)
\]
\[
\Gamma^*_{\unsure{K}}G\simeq\Gamma^0_K e(G)
\simeq\Gamma^0_k T^0e(G)\simeq\Gamma^*_kT(G)
\]
\deleted{\unsure{Question}}
\noindent (i) $T^0$ transforme injectifs en $\Gamma^0_k$-acycliques ??

\noindent (ii) $T^0$ de dim coh. $\leq2$
[et même $\leq1$ si on \deleted{\unsure{excepte}}\inserted{exclut}
les composantes de type $\mathbb Z$]

\noindent (iii) $T^*$ commute à ``\uline{l'extension du corps résiduel $k$}''.

i.e est ``de nature géométrique'' ;
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\underline{\underline H}^*(K,G^\bullet) &
H^p(k,\underline{\underline T}^{\unsure{q}}(G^\bullet))\arrow[l,Rightarrow]\\
\underline{\underline H}^*(k,T(G))\arrow[u,equal]&
\end{tikzcd}}
\[
\left[\begin{aligned}
\underline{\underline{\operatorname{Ext}}}^{\unsure{\bullet|*}}_{K\text{-gr}}(F,G)
&\Longleftarrow H^p(k,\underset{\sim}{\underline{\operatorname{Ext}}}^q_{K/k}(F,G))\\
&\Longleftarrow H^p(K,\underset{\sim}{\underline{\operatorname{Ext}}}^q_K(F,G))
\end{aligned}\right.
\]
\mspage{103}
'''
save_page(104,text,[('diagram','top left','k ← V → K'),('margin note','below k circled','parfait ?'),('diagram','upper category map','K Gr K downward T to K QuGr k'),('text','upper beside categories','complexes finis de K-groupes; complexes finis de k-quasi-groupes'),('deletion','upper beside category descriptor','quasi; alg'),('deletion','beside downward arrow','T0'),('margin note','upper right','Coh de K ne se calcule pas galoisiennement'),('margin note','right below','Coh. de k se calcule galoisiennement'),('deletion','inside right margin after galoisiennement','et'),('display','upper middle','T(G)=T0 a e(G)'),('display','middle','Gamma star K G ≃ Gamma0 K e(G)'),('deletion','left of item i','Question'),('text','middle item i','T0 transforme injectifs en Gamma0 k-acycliques ??'),('text','middle item ii','T0 de dim coh. ≤2'),('deletion','item ii','excepte'),('insertion','item ii above deletion','exclut'),('text','lower item iii','T star commute à l’extension du corps résiduel k'),('text','lower','i.e est de nature géométrique'),('diagram','lower spectral sequence with vertical equality','H star(K,G bullet); Hp(k,T q(G bullet)); H star(k,T(G))'),('display','bottom bracketed','Ext bullet K-gr ⇐ Hp(k,Ext q K/k) ⇐ Hp(K,Ext q K)'),('text','bottom left page number','103')],observations='Full and both halves reread; right bracketed margins enlarged. Both question marks in (i) retained. Double underlines are not merged with the straight-plus-wavy underlines. The lower H display includes the visible vertical equality as a diagram.')
