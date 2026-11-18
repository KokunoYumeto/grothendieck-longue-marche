from save_page import save
text=r'''
\scanpage{34}
% archive foliation: 33
diag. commutatif
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
&Y\arrow[d,"\alpha\in W"']\arrow[dr,dash,"\beta=\prod\beta_j\in W"]&\\
X\arrow[r,shift left=.6ex,"f"]\arrow[r,shift right=.6ex,"g"']&Y'\arrow[r,"\varphi=(\varphi_j)"']&Y''=\prod Y'_j
\arrow[from=1-2,to=2-3,phantom,"\mathrm{comm}"'{pos=.55}]
\end{tikzcd}}
avec $\varphi f\sim\varphi g$, donc $\gamma(f)=\gamma(g)$

\uline{NB} Cela marcherait pour les produits infinis, si on savait qu'un produit infini d'éléments de $\underline W_A$ est encore dans $\underline W_A$

Venons-en au lemme plus haut
\[
(ii)\Longleftrightarrow(ii\ \mathrm{bis})\quad\text{trivial}
\]
($\Longleftrightarrow$ si $f\in\underline W_A$, alors $\forall a\in\operatorname{Ob}A$, $f\times\mathrm{id}_a:X\times a\longrightarrow Y\times a$ \inserted{$\in\underline W_A$})
\diagram{\begin{tikzcd}[row sep=large]
{}\arrow[d,Rightarrow,"\text{on vient de le prouver}"]\\(iii)
\end{tikzcd}}
\margin{\diagram{\begin{tikzcd}(iii)\arrow[u,Rightarrow]\\{}\end{tikzcd}}
est évident quand on sait que $\underline W_A$ est fortement saturé (\unsure{résulte de} $\unsure{\underline W}$ fortement saturé)}

\deleted{Examinons $(iii)$}

$(ii\ \mathrm{bis})$ \deleted{signifie} aussi que si $f\in\underline W_A$, alors $\forall Z$, $f\times\unsure{\mathrm{id}}_Z:X\times Z\longrightarrow Y\times Z$ est $\in\underline W_A$ loc. sur $Z$, et pour ceci il suffit de le voir pour $Z$ dans $A$, i.e.

\margin{raisonnement déjà fait plus haut}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
X\times a\arrow[r,"\in W"]\arrow[d]&Y\times a\arrow[d,dash]\\
X\arrow[r,"\in\underline W_A"']&Y
\end{tikzcd}}
Cela marche si on sait que $X\times a\longrightarrow X$ \inserted{et $Y\times a\longrightarrow Y$} $\in\underline W_A$, ce qui signifie aussi que $\unsure{\widehat A|A}$ est tot. asph. \deleted{et} Donc $(i)\Longrightarrow(ii\ \mathrm{bis})$

\deleted{En fait}\deleted{de même $(ii\ \mathrm{bis})$ implique} Inversement, on voit tout de suite que si $A$ asph, alors $(ii\ \mathrm{bis})\Longrightarrow(i)$ [prendre $f:a\longrightarrow e_{\widehat A}$)
\inserted{donc $(i)\Longleftrightarrow(\unsure{(ii)|(iii)}+A$ asphérique}
'''
elements=[
('text','top','diag. commutatif'),
('diagram','upper','Y; X ⇒ Y prime → Y doubleprime = product Y prime_j'),
('display','upper middle','phi f ~ phi g, donc gamma(f)=gamma(g)'),
('text','middle','NB Cela marcherait pour les produits infinis'),
('text','middle','Venons-en au lemme plus haut'),
('display','middle lower','ii iff ii bis trivial'),
('display','right','iff f in W_A implies for all a in Ob A'),
('insertion','beneath f × id_a','in W_A'),
('diagram','left of on vient','down double arrow to iii'),
('text','middle lower','on vient de le prouver'),
('diagram','left margin','up double arrow'),
('margin note','left slanted','est évident quand on sait que W_A est fortement saturé'),
('deletion','lower middle','Examinons iii'),
('text','lower middle','ii bis aussi que si f in W_A'),
('deletion','within ii bis paragraph','signifie'),
('display','lower','f × id_Z:X × Z → Y × Z'),
('text','lower','est in W_A loc. sur Z'),
('margin note','left lower','raisonnement déjà fait plus haut'),
('diagram','lower','X × a → Y × a; X → Y'),
('text','near foot','Cela marche si on sait que'),
('display','near foot','X × a → X in W_A'),
('insertion','right by X × a → X','et Y × a → Y'),
('text','near foot','ce qui signifie aussi que Ahat est tot. asph.'),
('deletion','before Donc','et'),
('display','near foot right','Donc i implies ii bis'),
('deletion','foot left','En fait'),
('deletion','foot above live line','de même ii bis implique'),
('text','foot','Inversement, on voit tout de suite que'),
('display','foot','A asph; ii bis implies i; f:a → e_Ahat'),
('insertion','bottommost','donc i iff (ii + A asphérique'),
]
save(34,text,'text',elements,'Continuation of injectivity proof and detailed product-lemma implications. The infinite-product extension is explicitly conditional on closure of W_A under infinite products. Margin says strong saturation makes a reverse implication evident. Lower notation A versus Ahat and the final ii/iii numbering remain uncertain; no mathematical repair applied.')
