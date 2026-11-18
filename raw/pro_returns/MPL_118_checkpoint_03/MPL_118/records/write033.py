from save_page import save
text=r'''
\scanpage{33}
% archive foliation: 32
C'est le cas si $A$ catégorie test stricte, plus \unsure{génlt} si elle est \unsure{tot.} $\underline W$-asphérique.

\uline{Lemme} \unsure{(!)|(?)} Soit $A$ \deleted{une catégorie \unsure{finie}} \inserted{dans $(\mathrm{Cat})$}. \inserted{Conditions équiv.}

$(i)$ $A$ \deleted{est} tot. $\underline W$-asphérique, \deleted{il faut}

$(ii)$ \deleted{que produit de $2$ flèches $(\underline W_A)$}\inserted{Produit fini de flèches $(\underline W_A)$} est $\in\underline W_A$

\deleted{$\unsure{(iii)}$}\inserted{$(ii\ \mathrm{bis})$} Si $f:X\longrightarrow Y$ \deleted{dans $A$} est dans $\underline W_A$ et $Z$ dans $\widehat A$, $f\times\mathrm{id}_Z:X\times Z\longrightarrow Y\times Z$ est dans $\underline W_A$

$(iii)$ Le foncteur $\widehat A\longrightarrow(\mathrm{Hot}_A(\unsure{\underline W}))$ commute aux produits finis
\deleted{\uline{Dém}}

$(iv)$ Le foncteur $\widehat A\longrightarrow(\mathrm{Hot}_{\unsure{A}}(\underline W))$ commute aux produits finis

\margin{\diagram{\begin{tikzcd}[row sep=large,column sep=huge]
(i)\arrow[d,Rightarrow]\\
(ii)\arrow[d,Leftrightarrow]\\
(ii\ \mathrm{bis})\arrow[d,Rightarrow]\arrow[uu,Rightarrow,bend left=65,"{[\text{si }A\ \deleted{\unsure{est}}\ \underline W\text{-asph.}]}"']\\
(iii)\arrow[u,Rightarrow,bend left=65,"\text{\unsure{résolution forte}}"']
\end{tikzcd}}
\deleted{\unsure{cat. test faible}}}

On va revenir à ce lemme tantôt. Pour le moment, on suppose vérifié $(ii)$, qui assure surjectivité de $*$.

\uline{Injectivité}?
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
&Y\arrow[d,"\alpha"',"\in W"]\arrow[r,"\mathrm{pr}_j"]&Y_j\arrow[d,"\beta_j"',"\in\underline W"]\\
f,g:X\arrow[r,shift left=.5ex]\arrow[r,shift right=.5ex]&Y'\arrow[r,"\varphi_j"']&Y'_j\deleted{{}=\unsure{Y'\amalg_Y Y_j}}
\end{tikzcd}}
on suppose que pour $\forall j$, $\exists\,\beta_j:Y_j\longrightarrow Y'_j$, $\varphi_j$ tels que $\beta_j\mathrm{pr}_j=\varphi_j\alpha$, $\beta_j\in\underline W$, $\varphi_jf\underset h\sim\varphi_jg$,
\deleted{Donc}\deleted{On a donc}\deleted{\unsure{?}} posons
\[
\beta=\prod\beta_j:Y=\prod Y_j\longrightarrow Y''=\prod Y'_j,
\]
\deleted{\unsure{pourra}} on trouve
'''
elements=[
('text','top','C’est le cas si A catégorie test stricte'),
('text','upper','Lemme (!) Soit A'),
('deletion','upper','une catégorie finie'),
('insertion','above deleted phrase','dans (Cat)'),
('insertion','upper right','Conditions équiv.'),
('text','upper middle','(i) A tot. W-asphérique'),
('deletion','within i','est'),
('deletion','end of i','il faut'),
('text','upper middle','(ii) Produit fini de flèches'),
('deletion','within ii','que produit de 2 flèches (W_A)'),
('insertion','above cancellation in ii','Produit fini de flèches (W_A)'),
('deletion','before ii bis','(iii)'),
('insertion','left of next condition','(ii bis)'),
('text','middle','Si f:X → Y est dans W_A'),
('deletion','after f:X → Y','dans A'),
('display','middle','f × id_Z:X × Z → Y × Z'),
('text','middle','(iii) Le foncteur Ahat → Hot_A(W)'),
('deletion','below iii','Dém'),
('text','middle lower','(iv) Le foncteur Ahat → Hot_A(W)'),
('diagram','left margin','i ⇒ ii ⇔ ii bis ⇒ iii; reverse implications'),
('margin note','left vertical','résolution forte; si A W-asph.'),
('deletion','left vertical','est; cat. test faible'),
('text','lower middle','On va revenir à ce lemme tantôt'),
('text','lower','Injectivité?'),
('diagram','lower','X ⇒ Y prime; Y → Y_j; alpha, beta_j, phi_j'),
('deletion','after Y prime_j in diagram','= Y prime amalg_Y Y_j'),
('text','near foot','on suppose que pour forall j'),
('display','near foot','exists beta_j; beta_j pr_j = phi_j alpha; homotopy'),
('deletion','near foot','Donc'),
('deletion','near foot','On a donc'),
('deletion','before posons','?'),
('display','foot','beta = product beta_j'),
('deletion','bottom left','pourra'),
('text','bottom','on trouve'),
]
save(33,text,'text',elements,'Highly revised list of equivalent conditions, with implication arrows in the margin. The two product-preservation clauses are retained separately as written; their target notation and the reverse-implication annotation need a particularly close final audit. The author explicitly postpones the lemma and assumes (ii) for the present surjectivity proof. No mathematical checking performed.')
