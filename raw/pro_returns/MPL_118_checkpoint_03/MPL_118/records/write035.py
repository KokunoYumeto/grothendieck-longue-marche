from save_page import save
text=r'''
\scanpage{35}
% archive foliation: 34
Reste à examiner $(iv)$. Comme on sait déjà que $(\mathrm{Cat})\longrightarrow\mathrm{Hot}(\underline W)$ commute aux produits finis, $(iv)$ signifie que pour $X,Y$ dans $\widehat A$,
\deleted{$\unsure{A_{/X}\times A_{/Y}}$}
\[
A_{/X\times Y}\longrightarrow A_{/X}\times A_{/Y}
\]
est $\in\underline W$. \deleted{Cela implique} Dans le cas $X=a$, $Y=b$ dans $\operatorname{Ob}A$, cela signifie que $a\times b$ asphérique --- i.e. $\widehat A$ tot. \inserted{$\underline W$-}asph. Je dis que cela suffit, de façon précise que $A_{/X\times Y}\longrightarrow A_{/X}\times A_{/Y}$ est asph.

En effet, pour un objet $\alpha=(a_{/x},b_{/y})$ du deuxième \unsure{mb}, on a
\[
(A_{/X\times Y})_{/\alpha}\simeq A_{/a\times b}
\]
\deleted{et} on gagne. En résumé

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
& (i)\quad A\text{ tot. }\underline W\text{-asph.}\arrow[d,Leftrightarrow]\\
\left.\begin{gathered}a\longrightarrow X\times Y\\a\longrightarrow X\\a\longrightarrow Y\end{gathered}\right\}\arrow[r,"a"]
&(iv)\quad\widehat A\longrightarrow\mathrm{Hot}(\underline W)\text{ commute aux produits binaires}\arrow[d,Leftrightarrow]\\
&(iv\ \mathrm{bis})\quad\widehat A\longrightarrow\mathrm{Hot}(\underline W)\text{ commute aux produits finis}\arrow[d,Rightarrow]\\
&(ii)\quad\deleted{\unsure{Produit}}\inserted{\underline W_A\text{ stable}}\text{ par produits finis}\arrow[d,Leftrightarrow]\arrow[u,Rightarrow,bend left=70,"\text{si }A\ \underline W\text{-asph.}"']\\
&(ii\ \mathrm{bis})\quad f\in\underline W_A\Longrightarrow f\times\mathrm{id}_X\in\underline W_A\quad(\forall X\in\operatorname{Ob}\widehat A)\arrow[d,Rightarrow]\\
&(iii)\quad\widehat A\longrightarrow\mathrm{Hot}_A\text{ commute aux produits finis}\arrow[u,Rightarrow,bend left=65,"\text{\unsure{forte saturation}}"']
\end{tikzcd}}
'''
elements=[
('text','top','Reste à examiner iv'),
('display','upper','(Cat) → Hot(W)'),
('deletion','upper middle','A_/X × A_/Y'),
('display','upper middle','A_/X×Y → A_/X × A_/Y'),
('text','middle','est in W'),
('deletion','middle','Cela implique'),
('text','middle','Dans le cas X=a,Y=b dans Ob A'),
('display','middle','a × b asphérique; Ahat tot. asph.'),
('insertion','above asph.','W-'),
('text','middle lower','Je dis que cela suffit, de façon précise'),
('display','middle lower','A_/X×Y → A_/X × A_/Y est asph.'),
('text','lower','En effet, pour un objet alpha'),
('display','lower','alpha=(a_/x,b_/y)'),
('display','lower','(A_/X×Y)_/alpha ≃ A_/a×b'),
('deletion','before on gagne','et'),
('text','lower','on gagne. En résumé'),
('diagram','lower third','a → X×Y; a → X; a → Y; conditions i,iv,iv bis,ii,ii bis,iii'),
('deletion','within ii summary','Produit'),
('insertion','within ii summary','W_A stable'),
('margin note','summary left','si A W-asph.'),
('margin note','summary lower left','forte saturation'),
]
save(35,text,'text',elements,'Comparison of category-of-elements product map with the total-asphericity condition; lower third is a revised implication summary including binary versus finite products. The prose explicitly has Ahat at the total-asphericity phrase while summary (i) has A. Both are preserved. The two braces, reverse arrows and three left-hand maps are represented in the summary diagram. No proof verified during transcription.')
