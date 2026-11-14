from record_page import save_page
save_page(120,6,r'''
a) $\mathcal M_n=$ parties de cardinal $\le1$ de $R^n$

b) $\mathcal M_n=$ parties finies de $R^n$

c) $\mathcal M_n=$ toutes les parties de $R^n$

\margin{ici les axiomes a), b), c) du NB \textcircled{2}, \uline{à l'exclusion} de $c_2)$}

Aucun de ces exemples n'est particulièrement \unsure{passionnant}.

\margin{\textcircled{II} \uline{espaces modérés}\par
Dans ce qui suit \unsure{au lieu de} $(M1)$ il suffit l'axiome concernant \deleted{\unsure{les applications}} \inserted{\unsure{les surjections}} \uline{pour les seuls} $[1,n]$ -- \unsure{c.-à-d. les} \unsure{linéaires des s.} \illegible{3} \unsure{applications} \unsure{des} \uuline{\unsure{directes}}.}
\margin{on n'exclut \unsure{pas} $I$ vide}

Terminologie : partie modérée de $R^I$, points modérés de $R$, de $R^I$.

\uline{déf} Soit $A\in\mathcal M_I$, $B\in\mathcal M_J$, $f:A\unsure{\longrightarrow|-}B$, d'où
\[
\Gamma_f\subset A\times B\subset R^I\times R^J\simeq R^{I\unsure{\cup|\amalg}J}.
\]
On dit que $f$ est \uline{modérée} si
\[
\Gamma_f\in\mathcal M_{I\unsure{\cup|\amalg}J}.
\]

\margin{\unsure{via|vu} $M2$}
\uline{Proposition} a) $\mathrm{id}_A$ (si $A\in\mathcal M_I$) est modérée

b) \diagram{\begin{tikzcd}[row sep=tiny,column sep=large]
f:A\arrow[r,no head]&B&g:B\arrow[r,no head]&C\\
\mathcal M_I\arrow[u,phantom,"\rotatebox{90}{\(\in\)}" description]&\mathcal M_J\arrow[u,phantom,"\rotatebox{90}{\(\in\)}" description]&&\mathcal M_{\unsure{K|n}}\arrow[u,phantom,"\rotatebox{90}{\(\in\)}" description]
\end{tikzcd}}\quad et\quad modérés $\Longrightarrow gf$ modéré

c) \diagram{\begin{tikzcd}[row sep=tiny]
f:A\arrow[r]&B\\
\mathcal M_I\arrow[u,phantom,"\rotatebox{90}{\(\in\)}" description]&\mathcal M_J\arrow[u,phantom,"\rotatebox{90}{\(\in\)}" description]
\end{tikzcd}} modéré et bijectif $\Longrightarrow f^{-1}$ modéré

D'où catégorie des \uline{modèles modérés} $\mathrm{Mod}_{\mathcal M_*}$, \inserted{(on prend $(I,A\in\mathcal M_I)$)} et un foncteur \uline{conservatif} \uline{fidèle}
\diagram{\begin{tikzcd}
\mathrm{Mod}_{\mathcal M_*}\arrow[r]&(\mathrm{Ens})
\end{tikzcd}}\qquad$(I,A)\longmapsto A$.
\margin{on n'exclut pas les modèles $\subset R^0=\{e\}$, \inserted{modèle} \deleted{\unsure{discret}} réduit à un point \ldots}

On en déduit\deleted{\unsure{on}} la catégorie des ensembles \inserted{(ou ``espaces'')} $(\mathcal M_*-)$ modérés, équivalente à : $\mathrm{Mod}_{\mathcal M_*}$, mais avec un foncteur
\diagram{\begin{tikzcd}
\deleted{\unsure{\mathrm{Mod}}}\ \mathrm{Esp}_{\mathcal M_*}\arrow[r]&(\mathrm{Ens})
\end{tikzcd}}\qquad$X\longmapsto|X|$
qui est fidèle, conservatif et de plus ``transportable'', i.e.
\mspage{5}
''',[
('text','top example a','M_n=parties de cardinal <=1 de R^n'),('text','top example b','M_n=parties finies de R^n'),('text','top example c','M_n=toutes les parties de R^n'),('margin note','upper right curved leader','ici les axiomes a,b,c du NB 2 à l’exclusion de c2'),('text','upper below examples','Aucun de ces exemples n’est particulièrement passionnant'),('margin note','upper left diagonal heading and dense note','II espaces modérés; Dans ce qui suit; au lieu de M1'),('deletion','upper diagonal note','les applications'),('insertion','upper diagonal note','les surjections'),('margin note','left below diagonal note','on n’exclut pas I vide'),('text','upper-middle terminology','Terminologie : partie modérée de R^I; points modérés'),('text','middle definition','déf Soit A in M_I, B in M_J, f:A to B'),('display','middle definition','Gamma_f subset A times B subset R^I times R^J simeq R^{I union J}'),('text','middle definition continued','On dit que f est modérée si'),('display','middle definition continued','Gamma_f in M_{I union J}'),('margin note','left beside Proposition','via M2'),('text','middle Proposition a','id_A est modérée'),('diagram','middle Proposition b','f:A to B and g:B to C; memberships in M_I,M_J,M_K'),('text','middle Proposition b conclusion','modérés implies gf modéré'),('diagram','lower Proposition c','f:A to B; memberships in M_I,M_J'),('text','lower Proposition c conclusion','modéré et bijectif implies f inverse modéré'),('text','lower category paragraph','D’où catégorie des modèles modérés'),('insertion','above category phrase from right','on prend (I,A in M_I)'),('text','lower functor introduction','et un foncteur conservatif fidèle'),('diagram','lower functor','Mod_{M_*} to (Ens)'),('display','right of lower functor','(I,A) maps to A'),('margin note','lower left diagonal','on n’exclut pas les modèles subset R^0={e}; réduit à un point'),('insertion','lower left note','modèle'),('deletion','lower left note','discret'),('text','bottom paragraph','On en déduit la catégorie des ensembles'),('deletion','after déduit','on'),('insertion','above ensembles at right','ou espaces'),('diagram','bottom functor','Esp_{M_*} to (Ens)'),('deletion','before Esp','Mod'),('display','bottom right','X maps to |X|'),('text','bottom continuation','qui est fidèle, conservatif et de plus transportable, i.e.'),('text','bottom left page number','5')
],observations='Defines moderate maps by their graphs and states identity, composition and inverse-bijection properties, then Mod_{M_*} and the transported category Esp_{M_*}. The upper oblique note overlaps other writing and contains several heavily overwritten words: the attempted readings applications/surjections and linéaires des s. are low-confidence; three overlapped words remain physically unreadable. It appears to weaken the invoked coordinate axiom; do not use the uncertain wording as a proved restriction without image review. Both the index-union glyph and the K/n subscript are explicitly marked. The examples at the head and the margin excluding c2 must be checked together in later notes.')
