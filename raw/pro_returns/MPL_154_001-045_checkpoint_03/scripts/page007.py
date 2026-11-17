from workflow import save_page
save_page(7,r'''
\scanpage{7}
\mspage{5}
Cette carte \inserted{$\mathcal X_2$} est déduite de $\mathcal X_0$ en faisant ``éclater'' les \deleted{\unsure{p}} sommets supersinguliers, ou encore de $\mathcal X_1$ en découpant \inserted{l'int.} des faces supersingulières et en identifiant des pts antipodiques sur leurs bords. --- ce qui explicite aussi la façon dont les $D_i$ sont plongés dans $\mathcal X$. Cette fois, on a une carte où toutes les faces peuvent être considérées comme \inserted{des $\unsure{\square}$} \deleted{d'}ordre \deleted{$\unsure{2n}$} $(4n)$, où tous les sommets d'ordre pair (et $=$ d'ordre $4$). Sur cette carte, les $\operatorname{Pol}(D)$ forment un syst. local (\deleted{mais} --- alors que sur $\mathcal X_0$, c'est ramifié (\uline{avec indice de ramification $n$})) autour de chaque sommet. Quant aux bouts libres, de part et d'autre de $D_i\subset\mathcal X$, ils se raccordent de façon satisfaisante encore. Cette carte d'autre part ne s'envoie \uline{pas} dans $X$ (sauf erreur).

\margin{\figure{%
\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=north west,text width=6.1cm,align=left,inner sep=0pt] at (0,0) {Mais pourquoi, pour les raisons analogues, ne serait-il pas vrai qu'on a un syst. local sur $\mathcal X_0$ (ce qui est pourtant faux!) Il y a un pt qui en ce moment m'échappe. Je ne suis plus trop ds le coup, et \unsure{devrait|devrais} reconsulter les notes des semaines précédentes.};
\draw[orange!70!red,line width=1.4pt] (-.3,-1)..controls(-.15,2.2)and(6.6,1.9)..(6.5,-3.6)..controls(6.6,-4.3)and(6.3,-4.7)..(6.1,-4.9);
\draw[orange!70!red,line width=1.4pt] (5.6,-5.7)..controls(3.6,-7.5)and(.1,-6.7)..(-.25,-5.4)--(-.55,-5.7);
\end{tikzpicture}%
}}

4) Ce dernier inconvénient n'est pas présent pour la carte $\mathcal X_3$, qui \deleted{est} par ailleurs
\margin{\mspage{6}}
''',[
('text','top centre','5'),('text','left main block','Cette carte est déduite'),('insertion','above first line','X_2'),('deletion','before sommets','p'),('insertion','above des faces','l’int.'),('insertion','above ordre','des square-like sign'),('deletion','before ordre','d’'),('deletion','before (4n)','2n'),('deletion','parenthesis after local','mais'),('text','left lower','Quant aux bouts libres'),('margin note','right middle, encircled','Mais pourquoi, pour les raisons analogues'),('drawing','around right note','orange-red open oval'),('text','bottom item 4','Ce dernier inconvénient'),('deletion','last line','est'),('text','bottom left pencil','6')
],doubts=[('middle, face order','des square-like sign; d’ordre; 2n deleted; (4n)','Added sign and cancellation are hard to distinguish from caret','low'),('middle after (4n)','où tous les sommets d’ordre pair','No sont supplied','medium'),('marginal note ending','devrait / devrais','Final stroke not decisive; first reading preserved','medium'),('initial superscript-looking letter','p deleted before sommets','Overwritten small letter','low')],observations='Own page 5; separate pencil 6. Main text describes blow-up / antipodal boundary identification and local polygon system, contrasts ramification at X_0, and asserts absence of map into X “sauf erreur”. Circled marginal objection asks why the same reasoning would not give a local system on X_0 and says “Il y a un pt qui en ce moment m’échappe”; requests reconsulting earlier weeks’ notes. Variant 4 begins at bottom.')
