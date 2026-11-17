from workflow import save_page,ROOT
tex=r'''\scanpage{12}
\mspage{1}
\margin{23.12.83}

Structure sur l'ens des positions relatives $P=\operatorname{PR}(\underline\Sigma)$ d'un syst. $\underline\Sigma=(X,\Sigma)$ de pseudodroites.

a) Relations de spécialisation $D\longrightarrow D'$ (ou de générisation en sens inverse). À vrai dire, on a un ensemble $\widetilde P$ de ``flèches de spécialisation'' en paires $(D,T)$, où $D$ est dans $\operatorname{PR}$. et $T$ est un ``triangle de spécialisation'' pour $D$ i.e.
\deleted{c'est-à-dire}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\fill[gray!15] (0,0)--(1.15,1.5)--(2.65,0)--cycle;
\foreach \y in {.18,.36,.54,.72,.90,1.08,1.26}{\draw[gray!60,thin] ({.7667*\y},\y)--({2.65-\y},\y);}
\draw[yellow!55!brown,line width=4pt] (-.55,0)--(3.3,0);
\draw[orange!80!brown,line width=3pt] (-.4,-.45)--(1.48,1.94);
\draw[orange!80!brown,line width=3pt] (.93,-.5)--(1.25,1.99);
\draw[orange!80!brown,line width=3pt] (2.30,-.47)--(.83,1.91);
\draw[orange!80!brown,line width=3pt] (3.13,-.55)--(.57,1.83);
\draw[thick] (0,0)--(2.65,0);
\foreach \x in {0,.99,1.95,2.65}{\fill (\x,0) circle(2.4pt);}
\node[above right] at (1.15,1.5){$s$};\node[above left] at (0,0){$r$};\node[above right] at (2.65,0){$t$};
\end{tikzpicture}}

\deleted{\unsure{un sous-ens.} de $\nu\geq1$ sur $D$, \deleted{non réduites à un sommet de $\Sigma$, formant} un arc sur $\widetilde D$ (le rev. des \unsure{vis} de $D$, avec sa structure polygonale) et dont les $\nu+1$ sommets s'identifient aux \unsure{$\nu$-arêtes orientations} de $\widetilde D$) \deleted{correspondant à $\nu+1$}\inserted{sont \unsure{non-seulement dans}} $\Sigma$, et correspondent à des $D_i\in\Sigma$ que se rencontrent en un $=$ point $s$ \uline{d'ordre exactement} $\nu+1$, et sans sommet de $\Sigma$ dans le triangle $s,r,t$ \unsure{ni à l'intérieur, sauf} $s\ldots$}

[On exclut le cas où $\Sigma$ est trivial, qu'il est mieux traiter à part.] On a une application
\diagram{\begin{tikzcd}\widetilde P\arrow[r,"{(\text{source,but})}"]&P\times P\end{tikzcd}}
qui associe à $(D,T)$ le couple $(D,D')$, où $D'$ est ``déduit de $D$ par balayage-spécialisation de $D$ au dessus de $T$''. Cette application est-elle injective? Quand on connaît $(D,D')$, on connaît aussi $s$ (qui est l'unique sommet de $\Sigma$ qui est dans $D'$, non dans $D$) donc aussi l'ens \deleted{des extrémités} des \inserted{$\nu+1$} sommets de $\Sigma\cup\{D\}$ qui sont inclus dans le triangle $T$ --- savoir les sommets communs à $D$ et aux $\nu+1$ éléments de $\Sigma$ passant par $s$. D'autre part, on voit qu'aucune de ces ps. droites (en tant que p. dr. de \deleted{$\unsure{\Sigma}$} $\Sigma'=\Sigma\cup\{D\}$) n'est un bigone, \deleted{ce qui} (sinon $\Sigma$ serait trivial de centre $s$) ce qui implique que les arêtes \deleted{joignant}\inserted{contenues} dans $T$ qui joignent $s$ aux $2$ sommets \deleted{\unsure{con.}} envisagés sur $D$, \unsure{sont ainsi uniques} \deleted{\unsure{d'autre p.}} \unsure{(les vts de $\Sigma$ que sur $D$!)} à \unsure{moins un autre sommet que ceux-là}, ce qui implique que l'aire qu'ils \unsure{cernent} est également déterminée --- bref, $\widetilde P\to P\times P$ est bien injectif. On trouve donc un \deleted{graphe}\inserted{\uline{strict orienté}} \unsure{simple} $P$ comme ens des sommets, $\widetilde P$ comme ens. d'arêtes, ch. que arête étant orientée \deleted{\unsure{d'un sens}}\inserted{(i.e. munie} d'une origine privilégiée).

\margin{\uline{NB} on a tjs $D\ne D'$, car $D'\cap S=(D\cap S)\cup\{s\}$}

Soit, pour $D\in P$, $\operatorname{Sp}_0(D)$ l'ens de ses spécialisations \inserted{(immédiates) ou ``successeurs''}, \deleted{et $\operatorname{Gen}(D)$ l'ens de ses} qui correspond à l'ens des triangles de spécialisation formés pour $D$. Soit de $=$ $\operatorname{Gen}_0(D)$ l'ens de ses générisations (immédiates), qui correspond à l'ens des couples $(s,\widetilde{\unsure{\varphi|\xi}})$, où $s\in D\cap S$, et $\widetilde{\unsure{\varphi|\xi}}$ est une or. de $D$ en $s$ i.e. un pt de $\widetilde D$ sur $s$.

\margin{11}
'''
e=[('text','top centre','1'),('margin note','top left','23.12.83'),('text','title','Structure sur l’ens des positions relatives'),('text','left top paragraph','a) Relations de spécialisation'),('deletion','left beneath i.e.','c’est-à-dire'),('drawing','left upper middle','triangle s,r,t with four concurrent orange lines'),('deletion','left middle large cancelled block','un sous-ens. de ν≥1'),('deletion','inside cancelled block','non réduites à un sommet; formant'),('deletion','inside cancelled block','correspondant à ν+1'),('insertion','inside cancelled block','sont non-seulement dans'),('text','left lower middle','On exclut le cas'),('diagram','left lower middle','P̃ → P×P (source,but)'),('text','left lower','qui associe à (D,T)'),('deletion','left bottom','des extrémités'),('insertion','left bottom','ν+1'),('text','right top continuation','savoir les sommets communs'),('deletion','right top','Σ'),('deletion','right upper middle','ce qui; joignant'),('insertion','right upper middle','contenues'),('deletion','right upper middle','con.; d’autre p.'),('text','right middle','à moins un autre sommet'),('deletion','right middle','graphe'),('insertion','right middle','strict orienté'),('text','right middle','P comme ens des sommets'),('deletion','right middle','d’un sens'),('insertion','right middle','i.e. munie'),('margin note','column gutter below centre','NB on a tjs D≠D′'),('text','right lower','Soit, pour D∈P, Sp_0(D)'),('insertion','right lower','(immédiates) ou successeurs'),('deletion','right lower','et Gen(D) l’ens de ses'),('text','right bottom','qui correspond; Soit de = Gen_0(D)'),('margin note','bottom left','11')]
d=[('large cancelled block','un sous-ens.; vis; ν-arêtes orientations; non-seulement dans','Multiple overlapping deletions and a bounding cancellation line obscure both wording and syntax.','low'),('right lines 7–10','sont ainsi uniques; les vts de Σ que sur D; à moins un autre sommet','The added parenthetical and continuation are compressed; no grammatical repair has been supplied.','low'),('right middle','strict orienté; simple; ch. que','The graph terminology and abbreviation are uncertain under revisions.','low'),('right bottom','φ̃ / ξ̃','The looped orientation sign has an extended descender; compare all later occurrences visually.','low'),('left lower diagram continuation','D′ est','The prime on this isolated D is very slight.','medium')]
save_page(12,tex,e,d,'New manuscript text, own page 1, dated 23.12.83, title Structure sur l’ens des positions relatives. Defines specialization arrows via triangles, asks whether (source,but) is injective, then gives a geometric argument concluding yes. Large previous definition is cancelled. Excludes the trivial system for separate treatment. NB D≠D′ and change in vertex incidence. Introduces Sp_0 and Gen_0 and orientation lifts; detailed proof clauses remain reading questions.')
p=ROOT/'MPL_154_001-045_doubts.md';s=p.read_text();s=s.replace('# Abbreviations','## Additional recurring notation\n\n| Visible sign | LaTeX | Scans / issue |\n|---|---|---|\n| Underlined capital Sigma, system | `\\underline\\Sigma` | 9, 12; distinguish plain family `\\Sigma`. |\n| Pair space and arrow space | `P`, `\\widetilde P` | 12; do not suppress the tilde. |\n| Looped orientation sign | `\\unsure{\\varphi|\\xi}` | 12; requires comparison to later ink. |\n| Two horizontal strokes in prose | `$=$` | 9, 12; preserved without expanding to “même”. |\n\n# Abbreviations',1);p.write_text(s)
