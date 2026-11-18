from save_page import save
text=r'''
\scanpage{27}
% archive foliation: 26
\uline{Corollaire 1} Dans $\mathrm{Hot}(\underline W)$, les sommes directes finies existent, et les foncteurs canoniques $(\mathrm{Cat})\longrightarrow\mathrm{Hot}(\underline W)$, $\widehat A\longrightarrow\mathrm{Hot}_A,\longrightarrow\mathrm{Hot}(\underline W)$ y commutent.

\margin{\uline{finies} inutile, \unsure{par argument plus bas}}
\margin{pas de conditions sur $A$ ici!}

On est ramené au cas de $(\mathrm{Cat})$ (vu que $i_A:\widehat A\longrightarrow(\mathrm{Cat})$ commute aux $\varinjlim$ \unsure{donc aux} sommes), via le

\uline{Lemme} Soit $(\underline M,W)$ avec $W\subset\mathrm{Fl}(\underline M)$, $W$ permettant calcul des fractions à droite. \deleted{Si dans $M$ les} \inserted{Alors} \inserted{le} foncteur canonique $M\longrightarrow W^{-1}M$ commute aux $\varinjlim$ finies, \deleted{\unsure{les}} et en particulier aux sommes finies.

On appliquera ceci à $(\overline{\mathrm{Cat}},\overline{\underline W})$, il faut voir que les sommes finies y existent (sinon le lemme n'apprend pas \unsure{gd} chose!), et que $\mathrm{Cat}\longrightarrow\overline{\mathrm{Cat}}$ y commute. \deleted{Donc} Mais on a de façon générale
'''
elements=[
('text','top','Corollaire 1 Dans Hot(W)'),
('display','top','(Cat) → Hot(W); Ahat → Hot_A → Hot(W)'),
('margin note','upper left','finies inutile'),
('margin note','left beside Ahat','pas de conditions sur A ici!'),
('text','upper middle','On est ramené au cas de (Cat)'),
('text','middle','Lemme Soit (M,W)'),
('deletion','middle','Si dans M les'),
('insertion','above deleted opening','Alors'),
('insertion','above deleted opening','le'),
('display','middle','M → W^-1 M'),
('deletion','middle lower','les'),
('text','lower','On appliquera ceci à (barCat,barW)'),
('deletion','near foot','Donc'),
('text','foot','Mais on a de façon générale'),
]
save(27,text,'text',elements,'The finite-coproduct statement has a marginal objection to finiteness and a separate note that there are no conditions on A here. The right-fraction wording is retained as written. The abbreviation before chose and the short connective after the direct-limit sign are uncertain. No mathematical claim checked at this stage.')
