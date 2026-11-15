from record_page import save
save(15,223,'text',r'''
Il suffirait de construire $X$ projectif lisse sur $k$, tel que $H^*(X_v,\mathbf Z)$ et $H^*(X_w,\mathbf Z)$ non isomorphes comme \uline{anneaux}. On devrait mettre Serre à contribution.
\margin{Peut-on \unsure{remplacer} $\mathbf Z$ par $\mathbf R$??}
\figure{\begin{tikzpicture}\draw (0,0)--(2.6,.08);\draw (.55,-.18)--(2.1,-.18);\end{tikzpicture}}

Soit $k$ un corps de nbres, $v_0$ une place de $k$, $M$ un motif sur $k$, d'où $G_{Mv_0}=G_{v_0}$, groupe algébrique \uline{défini sur} $\mathbf Z$. Toute autre place \deleted{de} $v$ définit un fibré principal homogène $P_v$ sous $G_{v_0}$, et si on admet ce qui a été \deleted{dit}\inserted{conjecturé} plus haut, \inserted{si $M$ est pris assez grand,}
\[
v\ne v'\ \Longrightarrow\ P_v\unsure{\not\simeq|\ne}P_{v'}.
\]
On peut aller plus loin et se demander si \deleted{en} (pour $M$ assez grand) \uline{$\forall$} fibré principal homogène $P$ sous $G_{v_0}$ provient d'une place $v$ \deleted{\unsure{unique}}.
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.05,.6);\draw (.05,.65) circle (.05);\end{tikzpicture}} Attention, la condition d'avoir un isomorphisme de foncteurs $\xi(M)\otimes_{\mathbf Z}\mathbf C\simeq M_\infty\otimes_k\mathbf C$, satisfaisant aux conditions de compatibilité genre Riemann--Hodge, risque d'être une \unsure{condit\textsuperscript{n}} \unsure{vraimt} décisive\ldots}
Les \deleted{\unsure{de}} \unsure{tout pris|sont pris}
\[
G_{Mv_0}(\mathbf Z)=\pi^1_M(k,v)
\]
ces groupes à priori ne sont pas \unsure{isomorphes}.
\unsure{Nom}: groupes \uline{fondamentaux \inserted{(arithmétiques)} discrets}.
\mspage{222}
''',[
('text','top','Il suffirait de construire X projectif lisse'),
('drawing','upper middle','two separating strokes'),
('text','middle','Soit k un corps de nbres'),
('display','middle','v ≠ v′ implies P_v not isomorphic P_v′'),
('text','middle below display','On peut aller plus loin'),
('drawing','left margin','line ending in a small circle'),
('text','lower','Les ... tout pris; ces groupes à priori'),
('display','lower','G_Mv0(Z)=π¹_M(k,v)'),
('text','bottom','Nom: groupes fondamentaux discrets'),
('text','bottom left','222')
], 'Whole page and both halves read; top and lower margins and central cancellations enlarged. Short phrase before final display remains particularly uncertain.')
