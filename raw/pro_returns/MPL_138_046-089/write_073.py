from workflow import save_page
save_page(73,r'''
\scanpage{73}
% archive foliation: 72
et $S,\mathcal J$ sont deux parties discrètes disjointes de $\widehat X$.

On va \deleted{\unsure{se}} passer aux catégories isotopiques correspondantes, et en donner des interprétations en termes de théorie des groupes. Bien entendu, pour cette description, on est ramené au cas connexe. On peut \deleted{aussi} noter tt de suite que pour ce pb, on est ramené au cas où $\mathcal J=\varnothing$ [en \deleted{remplaçant}\inserted{\unsure{décrivant|donnant}} dans le cas général comme celui de la donnée d'un $(\widehat X,I)$ \uline{plus} la donnée d'une partie $\mathcal J$ de $I$]. Mais on gardera le pb \unsure{ss} \inserted{la} forme générale, en gardant également la dissymétrie dans le rôle de $S,\mathcal J$ -- mais
''',[
('text','top','et S,J sont deux parties discrètes disjointes de Xhat'),
('text','upper half','On va passer aux catégories isotopiques correspondantes ...'),
('deletion','before passer','se'),
('text','middle','Bien entendu ... cas connexe; On peut noter tt de suite ...'),
('deletion','after On peut','aussi'),
('text','lower half','cas où J empty; cas général ... (Xhat,I) plus une partie J de I'),
('deletion','after en','remplaçant'),
('insertion','above remplaçant','décrivant or donnant'),
('text','bottom','Mais on gardera le pb ss la forme générale ... dissymétrie ...'),
('insertion','before forme','la')])
