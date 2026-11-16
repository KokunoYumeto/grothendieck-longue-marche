from save_page import save
tex=r'''
\scanpage{37}
\[
H^1\bigl(X,\underbrace{\underline{\operatorname{Ext}}^1(f^*(B),G_{mX})}\bigr)
\]
\margin{\unsure{.\ '}}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\operatorname{Ext}_X(\overbrace{f^*(B)}^{A},G_{mX})\simeq\operatorname{Ext}_S(B,\unsure{f_!|f_*}(G_{mX}))\\
H^p(X,\underline{\operatorname{Ext}}^q_X(A,G_{mX})) \arrow[u,Rightarrow]
\end{tikzcd}}

\figure{\begin{tikzpicture}\draw (0,.05)--(10,0);\end{tikzpicture}}

Suite exacte de Cohomologie. Critère de \unsure{surjectivité};

\unsure{Fibré universel}

Dualité de Cartier [voir \unsure{Pic.}\ldots]

Th. \unsure{projectivité} des V.A. (Th. de rigidité)

Propriétés \unsure{finicielles|fonctorielles} des groupes \ldots

Propriétés différentielles des \unsure{gpes} et fibrés

En particulier : \uuline{fibrés linéaires}, symplectiques, orthogonaux etc \ldots

\figure{\begin{tikzpicture}\draw (0,3.6) .. controls (-.14,3.7) and (-.08,2.9) .. (-.1,2.6) .. controls (-.18,2.4) and (-.26,2.8) .. (-.14,2.5) .. controls (.1,1.7) and (-.1,.3) .. (.35,0);\draw (.05,1.3)--(.22,1.05);\end{tikzpicture}}

\unsure{Leur dualité} \unsure{pour} les \unsure{représentations lin. de groupes} ??

\figure{\begin{tikzpicture}\draw (0,0)--(10,.05);\end{tikzpicture}}
\[
\deleted{\underline{\operatorname{Hom}}(G_a,G_m)}
\]
\[
\mathbf Z.\quad\unsure{\mapsto}\quad\mathbf Z
\]
\margin{36}
'''
e=[('display','top left','H^1(X,underline Ext^1(f star(B),G_mX)) with underbrace'),('margin note','below first display left','dot and curved mark'),('diagram','upper quarter','Ext_X(f star B,G_mX) ~= Ext_S(B,f_!(G_mX)); upward double spectral arrow'),('insertion','above f star(B)','A with overbrace'),('drawing','upper-middle divider','long horizontal line'),('text','first list line','Suite exacte de Cohomologie. Critère de surjectivité'),('text','second list line','Fibré universel'),('text','third list line','Dualité de Cartier [voir Pic...]'),('text','fourth list line','Th. projectivité des V.A. (Th. de rigidité)'),('text','fifth list line','Propriétés finicielles des groupes ...'),('text','sixth list line','Propriétés différentielles des gpes et fibrés'),('text','seventh list line','En particulier : fibrés linéaires, symplectiques, orthogonaux etc'),('drawing','left of list','long bracket and intermediate stroke'),('text','below list question','Leur dualité pour les représentations lin. de groupes ??'),('drawing','lower divider','long horizontal line'),('deletion','below lower divider','underline Hom(G_a,G_m)'),('display','bottom','Z . mapsto Z'),('margin note','bottom left','36')]
d=[{'line':'left below first display','reading':'dot and curved apostrophe-like mark','alternatives':'isolated ink traces, no word supplied','confidence':'low'},{'line':'Ext adjunction right side','reading':'f_!','alternatives':'f_*; small dot and vertical stroke visible, retained as exclamation first','confidence':'medium'},{'line':'list first line','reading':'surjectivité','alternatives':'abbreviated handwriting could be other -tivité word','confidence':'low'},{'line':'list second line','reading':'Fibré universel','alternatives':'Fibrés inverses; first and ending letters uncertain','confidence':'low'},{'line':'list Cartier bracket','reading':'Pic.','alternatives':'R...; short name/reference','confidence':'low'},{'line':'list V.A.','reading':'projectivité','alternatives':'quotientabilité; letters compressed','confidence':'low'},{'line':'list fifth line','reading':'finicielles','alternatives':'fonctorielles; read first form from strokes without silently supplying familiar word','confidence':'low'},{'line':'list sixth line','reading':'gpes','alternatives':'groupes contracted','confidence':'medium'},{'line':'question below list','reading':'Leur dualité pour les représentations lin. de groupes ??','alternatives':'most words uncertain; multiple plausible readings remain','confidence':'low'},{'line':'final line','reading':'Z . mapsto Z','alternatives':'bar and horizontal mark could be a short word or headless stroke','confidence':'low'}]
save(37,tex,e,d,'Homological-adjunction and local-to-global Ext sketch followed by a programme list: cohomology, a doubtful criterion, universal bundle (reading doubtful), Cartier duality, V.A. projectivity/rigidity, groups and linear/symplectic/orthogonal bundles. Last programme question ends in two question marks; exact wording is low confidence, so research interpretation must remain conditional. The f subscript looks like an exclamation mark (dot present); do not normalize to direct-image star from adjunction expectation. Bottom Hom(G_a,G_m) is cancelled. Typed blue mirrored background is verso show-through, not readable front typescript. Pencil 36.')
