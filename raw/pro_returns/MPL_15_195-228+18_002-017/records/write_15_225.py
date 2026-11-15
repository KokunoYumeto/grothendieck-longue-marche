from record_page import save
save(15,225,'text',r'''
\margin{\deleted{\unsure{L'énoncé implique} $X$ de type fini, \unsure{qui} \unsure{intervient}}}
On a vu plus haut qu'une place est très loin d'être caractérisée par le foncteur fibre correspondant, \deleted{\unsure{Mais}} considéré comme foncteur dans les $\mathbf Z$-modules. Mais que se passe-t-il si on le regarde comme foncteur dans les structures de Hodge ?
\deleted{Ce \unsure{ceci devrait} \unsure{dire que}}
\inserted{Vrai pour un schéma \unsure{$k$ local}, et pour le premier \unsure{cas}}
\deleted{\unsure{p\textsuperscript{t} assez grand}, on est \unsure{ramené} \unsure{au cas où} \unsure{cela ne dépend} \unsure{que de} $k_0=$ clôture alg. de $\mathbf Q$ dans $k$, et \unsure{quitte au} $X$ \unsure{sur} de type

$X$ de type fini sur \deleted{un} $\mathbf Q$, puis par changement de base \unsure{au cas où} $X$ est connexe de type fini sur $\mathbf C$, et \unsure{point} \unsure{fermé} \inserted{ordinaire} de $X$ \unsure{est} sur $\mathbf C$. Supposant pour simplifier que $X$ est \deleted{affine}, \uuline{quasi-projectif}, \unsure{il suffit} \unsure{de considérer un cas} \unsure{plus simple} $X=\mathbf P^1_{\mathbf C}$.}
\margin{Attention, il faut parler des pl. complexes, \unsure{en restreindre} \unsure{précis}, pour \unsure{pouvoir} définir la structure de Hodge\ldots
\diagram{\begin{tikzcd}[row sep=small,column sep=small]
&X\arrow[dd,dash]\arrow[dr,dash]&\\
\mathbf Q\arrow[ur]\arrow[rr,dash]& &k\\
&\deleted{\unsure{A_i}}\arrow[ur,dash,bend left=35]&
\end{tikzcd}}}
\margin{\figure{\begin{tikzpicture}\node at (0,.6) {$\unsure{X}$};\draw (0,.3)--(.04,-.6);\end{tikzpicture}}}
Il semble qu'on le verrait facilement dans le cas de $X=\mathbf P^1_{\mathbf C}-(0)-(1)-(\infty)$, \inserted{et dans \unsure{ts éch. de cond.},} où la théorie classique \deleted{\unsure{doit}} le donne. --- [prendre comme motif celui défini par un schéma en courbes elliptiques sur $X$, d'invariant l'indéterminée $j$].
\mspage{224}
''',[
('text','top','On a vu plus haut qu’une place'),
('text','upper middle','Mais que se passe-t-il ... structures de Hodge?'),
('text','middle through lower','Cancelled successive versions from Ce ... to X=P¹_C'),
('diagram','left middle margin','Q, X, cancelled A_i, k'),
('drawing','left below diagram','X above vertical stroke'),
('text','bottom','Il semble qu’on le verrait facilement'),
('display','bottom inline','X=P¹_C−(0)−(1)−(∞)'),
('text','bottom','prendre comme motif celui défini ... indéterminée j'),
('text','bottom left','224')
], 'Whole and both halves inspected, with rotated marginal crops and blue-channel contrast enlargement of the cancellations. Long cancelled block, marginal wording, insertion after punctured projective line, and deletion boundaries have low confidence; no mathematical completion supplied.')
