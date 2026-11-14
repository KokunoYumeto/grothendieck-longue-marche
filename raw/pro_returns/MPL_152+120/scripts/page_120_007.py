from record_page import save_page
save_page(120,7,r'''
\mspage{6}\hfill\mspage{3}
pour tout diagramme
\diagram{\[
\left\{\begin{gathered}\begin{tikzcd}[row sep=large]
X&\\
|X|\arrow[r,"\alpha","\sim"']&E
\end{tikzcd}\end{gathered}\right.
\]}
avec $X\in\mathrm{Ob}\,\mathrm{Esp}_{\mathcal M_*}$, $\exists$ une unique \deleted{$Y$ et} flèche $f:X\unsure{\longrightarrow|-}Y$ de $\mathrm{Esp}_{\mathcal M_*}$, qui relève $\alpha$ (``Transport de structure'').

\uline{Proposition} Dans la catégorie $\mathrm{Esp}_{\mathcal M_*}$ des espaces $\mathcal M_*$-modérés, il y a des
\deleted{produits \unsure{fibrés|finis}, et des produits (de deux objets), et le foncteur $X\longmapsto|X|$ y commute. Si on suppose
\[
(\unsure{M5'|M5})\qquad R_0\ne\varnothing
\]
alors il \deleted{foncteur} y a aussi un objet final (qui est uniponctuel) et \unsure{le} \unsure{foncteur}}
\inserted{(\deleted{\unsure{pas des objets}} \unsure{sans restriction})}
\margin{\unsure{des limites finies}}
et le foncteur $X\longmapsto|X|$ commute.
\margin{\unsure{trivialité de} \unsure{celui} \illegible{1} d'un \illegible{1} \unsure{des} \unsure{lois} \illegible{2} des \unsure{foncteurs}}

\uline{Proposition} Si pour \uline{un} $n\in\mathbb N^*$ on a \deleted{$\unsure{R}$} $R^n\in\mathcal M_n$, alors \unsure{c'est} vrai pour $\forall n$, \unsure{et même} pour $\forall I$ fini
\[
R^I\in\mathcal M_I.
\]
Considérons l'axiome (\uline{facultatif})
\[
\deleted{\unsure{M5}}(M0)\qquad R\in\mathcal M_1\qquad(\Longrightarrow\forall I\in(\mathrm{Ens\ fini}),\ R^I\in\mathcal M_I)
\]
\margin{Quand on n'a pas $(M0)$, mais que l'on suppose $(M5)$, alors la \unsure{réunion} des $A\in\mathcal M_1$, \unsure{fait que} $\unsure{R'}$ est \unsure{obtenu} \unsure{comme} \illegible{2} \unsure{de} $\unsure{R}$ \unsure{réunion} \unsure{filtrante} \illegible{2}.\par
\unsure{On dispose} de \unsure{ces} \unsure{ens.} \unsure{stables} \illegible{2} \unsure{l'axiome} $(M1)$ \unsure{réciproque} \illegible{1} \unsure{l'influence} \unsure{de} \unsure{foncteurs} \illegible{2}.\par
\unsure{comme} $(M5)$ \unsure{l'expression} \unsure{espace} \unsure{muni de} \unsure{l'} $\unsure{R}$ \unsure{aussi} \unsure{vide} \unsure{annulé}.}
\margin{\unsure{objet} \unsure{abs.} \unsure{Cat}\uline{\unsure{f}}}
''',[
('text','top left page number','6'),('text','top right page number','3'),('text','top continuation','pour tout diagramme'),('diagram','top brace','X over |X|; |X| isomorphic to E via alpha'),('text','upper','avec X in Ob Esp; exists unique flèche f'),('deletion','upper before flèche','Y et'),('text','upper parenthesis','Transport de structure'),('text','middle Proposition opening','Dans la catégorie Esp des espaces M_*-modérés'),('deletion','large crossed central block','produits fibrés; produits de deux objets; foncteur; M5; objet final'),('display','within central crossed block','M5 prime; R_0 not empty'),('deletion','nested in central crossed block','foncteur'),('insertion','above produits at right','pas des objets; sans restriction'),('deletion','within upper inserted parenthesis','pas des objets'),('margin note','right below central cancellation','des limites finies'),('text','below central cancellation','et le foncteur X maps to |X| commute'),('margin note','right oblique across crossed block','trivialité de; d’un; des foncteurs'),('text','lower Proposition','Si pour un n in N* on a R^n in M_n'),('deletion','lower Proposition before R^n','R'),('display','lower Proposition conclusion','R^I in M_I'),('text','bottom axiom introduction','Considérons l’axiome facultatif'),('display','bottom axiom','M0 R in M_1; all finite I, R^I in M_I'),('deletion','bottom before M0','M5'),('margin note','large lower-left to middle oblique block over Proposition','Quand on n’a pas M0 mais que l’on suppose M5; réunion des A in M_1'),('margin note','lower-right small continuation','objet; abs.; Cat f')
],observations='Transport of structure is formulated by unique lifting of a bijection |X| to E. A large crossed block discusses products, a hypothesis written M5 or M5 prime (R_0 nonempty), and a one-point final object; later marginal additions overlap its boundary. The bottom introduces optional M0, R in M_1, with its finite-index consequence. The two oblique revision blocks are the least secure readings in cote 120 so far: several words are physically obscured by crossing strokes and overlapping base text, and the remaining attempted readings are all explicitly marked. No research inference should rely on these reconstructed phrases without checking the scan.')
