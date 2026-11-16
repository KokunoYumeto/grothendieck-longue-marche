from save_page import save
tex=r'''
\scanpage{8}
\mspage{6}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {11};\draw (0,0) ellipse (0.28 and 0.31);\end{tikzpicture}}
pg101\quad $\ell-6$.\quad Dire où on trouve que Néron commute à $S\mapsto\widehat S$.

pg103\quad Le renvoi au courage du lecteur est désagréable --
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {que faire ?};\draw[rotate=12] (0,0) ellipse (0.96 and 0.41);\end{tikzpicture}}}

Si j'ai bien compris, tu affirme que prolonger une biextension à $A\times A'$ est ``la $\hat{\mathrm m}$ chose'' que de la prolonger aux ${}_{\ell^\infty}A\times{}_{\ell^\infty}A'$.

\margin{7}
'''
e=[('text','upper right','6'),('drawing','upper left section marker','circled 11'),('text','top pg101 l-6','Dire où on trouve que Néron commute'),('text','upper pg103','Le renvoi au courage du lecteur'),('margin note','upper left pencil beside pg103','que faire ?'),('drawing','upper left pencil','oval around que faire ?'),('text','upper paragraph after pg103','Si j’ai bien compris, tu affirme'),('margin note','bottom left pencil','7')]
save(8,tex,e,[], 'Requests: source for Néron commuting with completion S -> S-hat; complains about leaving proof to the reader; restates assertion that extending a biextension to A x A-prime is the same as extending to ell-primary torsion subgroups. Pencil “que faire ?”. End of six numbered editorial sheets; main manuscript page 6, pencil 7. Lower half visually inspected: blank except pencil 7.')
