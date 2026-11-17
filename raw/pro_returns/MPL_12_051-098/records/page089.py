from save_page import save_page
save_page(89,r'''\scanpage{89}
% archive foliation: 88
De (vi) et (viii) résulte que pour tt
motif $M$ et entier $n$, l'isomorphisme
\[
\Phi^s(M)\simeq\Phi^s(M(n))
\]
est compatible avec les cônes amples.

De (iv) et \unsure{(vii)|(vi)} résulte que si $\rho=0$, une
forme ample sur $M$ induit une
forme \uline{définie positive}
\[
\Gamma_k M\times\Gamma_k M\longrightarrow\Gamma_k\mathbf Q(0)=\mathbf Q
\]

Si on décompose $M$ (de poids $\rho$) en
composantes isotypiques $M_\alpha$, il vient
\[
\Phi^s(M)\simeq\unsure{\prod|\bigoplus}_\alpha\Phi^s(M_\alpha)
\]
donc pour étudier les formes positives, il
suffit de les étudier en principe sur
des morceaux isotypiques, qui sont
d'ailleurs sous la forme
\[
I\otimes_A\unsure{V|W}
\]
où $I$ est un motif simple, $A$ son
anneau des endomorphismes, qui est
un corps, et $\unsure{V|W}$ un \uline{vectoriel} sur $A$
''',[
('top','text','De (vi) et (viii) résulte que pour tt motif M et entier n'),
('upper','formula','Phi^s(M) isomorphic Phi^s(M(n))'),
('upper-middle','text','compatible avec les cônes amples'),
('middle','text','De (iv) et (vii)/(vi) résulte que si rho=0'),
('middle','formula','Gamma_k M x Gamma_k M -> Gamma_k Q(0)=Q'),
('lower-middle','text','Si on décompose M en composantes isotypiques M_alpha'),
('lower-middle','formula','Phi^s(M) isomorphic product/direct sum over alpha of Phi^s(M_alpha)'),
('lower','text','étudier les formes positives sur les morceaux isotypiques'),
('lower','formula','I tensor_A V/W'),
('bottom','text','I motif simple, A son anneau des endomorphismes, un corps; V vectoriel sur A')
],remarks='Whole and both halves read. Overwritten product/direct-sum sign enlarged and retained uncertain. V/W retains ambiguity in the heavy strokes.')
