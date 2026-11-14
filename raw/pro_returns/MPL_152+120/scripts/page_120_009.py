from record_page import save_page
save_page(120,9,r'''
\mspage{4}
\margin{\unsure{le donner} \uline{après} la proposition qui suit, \unsure{ou postuler}\ldots}
\uline{Proposition} Si \deleted{$R_0\ne\varnothing$}, \inserted{$\operatorname{Card}R_0\geq2$}, \deleted{\unsure{alors} \unsure{(si $R\in\mathcal M_1$)}, \unsure{$\mathcal E$} \unsure{dans}} $\mathcal E$
\deleted{\unsure{existe un} \unsure{$(\operatorname{Hom}_{\mathcal E}(e,R))$} \unsure{de l'objet} \unsure{$R_0$}}
\deleted{$\operatorname{Hom}_{\mathcal E}(R^0,R)\ne\varnothing$} \inserted{$\underset{\{e\}}{\unsure{''}}$} dans \unsure{des}
\deleted{$\mathcal E$ \unsure{est}, \unsure{a des} sommes finies} \unsure{(uniquement} et $X\mapsto|X|$ y commute.

\figure{\begin{tikzpicture}\node[draw,ellipse] {$M5$};\end{tikzpicture}}
\uline{Corollaire} Sur $\forall$ ens fini il $\exists$ une structure modérée et une seule, pour laquelle les parties uniponctuelles soient modérées (str. mod. discrète).

\unsure{On se propose} \unsure{les sommes} \unsure{à construire} $X_1\amalg_Z X_2$, sans supposer $Z$ vide. Notons d'abord ceci :

\uline{Proposition} Soit $I$ un \deleted{type de} \inserted{type de} diagrammes fini, et $(X_i)_{i\in I}$ un diagramme de type $I$ dans $\mathcal E=\operatorname{Esp}_{\mathcal M_*}$, i.e. d'espaces modérés. Soit $X$ la limite inductive \uline{dans} $(\mathrm{Ens})$, qui est donc un \inserted{certain} quotient de $\coprod X_i$ (comme toujours). Supposons qu'il existe sur $X$ une structure modérée, telle que les appl. can. $g_i:X_i\longrightarrow X$ soient modérées. Alors $X$, muni de cette structure, est \inserted{une} $\varinjlim$ des $X_i$.
\mspage{8}
''',[
('text','top right','4'),('margin note','upper left oblique','le donner après'),('text','upper','Proposition Si'),('deletion','upper','R0 nonempty'),('insertion','above condition','Card R0 greater equal 2'),('deletion','upper right','alors (si R in M1)'),('deletion','second and third lines','existe un Hom'),('deletion','third line','Hom_E(R0,R) nonempty'),('insertion','under R0','{e}'),('text','upper middle','dans des'),('deletion','fourth line','E est a des sommes finies'),('text','below cancellation','et X maps to |X| y commute'),('drawing','left middle','circled M5'),('text','middle','Corollaire Sur tout ens fini'),('text','middle','On se propose'),('text','lower','Proposition Soit I'),('deletion','above diagrammes','type de'),('insertion','above diagrammes','type de'),('insertion','above quotient','certain'),('insertion','bottom above lim','une'),('text','bottom left','8')], observations='Finite sums proposition substantially cancelled and changed from R0 nonempty to Card R0 at least 2; corollary for finite sets. Later proposition states that a finite set colimit with a moderate structure and moderate canonical maps gives a categorical colimit. Readings of several cancelled upper lines remain low confidence.')
