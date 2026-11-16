from audit_page import audit
changes=[
(r"{}_nP\longrightarrow P''\quad\text{épimorphisme}",r"{}_nP\unsure{\mathbin{-}|\longrightarrow}P''\quad\text{épimorphisme}"),
(r"E\leftarrow E'(P',Q)",r"E\unsure{\vdash|\mapsto}E'(P',Q)"),
(r'les deux \unsure{objets}',r'les deux \unsure{mbs|objets}'),
(r'\margin{\deleted{\unsure{Si}',r'''\margin{\figure{\begin{tikzpicture}\draw (-.6,1.5)..controls (-.1,1.5) and (0,1.5)..(0,1.2)--(0,-.7)..controls (0,-.9) and (.1,-.9)..(.7,-.9);\end{tikzpicture}}\deleted{\unsure{Si}'''),
(r"\deleted{$\unsure{nP''=0}$}",r'''\margin{\figure{\begin{tikzpicture}\fill (0,0) ellipse (.03 and .015);\end{tikzpicture}}}
\deleted{$\unsure{nP''=0}$}'''),
(r'Un hom de biextensions',r'''\margin{\figure{\begin{tikzpicture}\fill (0,.45) circle (.02);\fill (0,0) circle (.03);\end{tikzpicture}}}
Un hom de biextensions''')
]
audit(48,changes,notes='Second whole page, top half and enlarged cancelled proof. Corrected left-arrow reading to the visible bar-and-stroke map symbol. The short word after les deux appears mbs, not the expanded contextual reading objets. Re-examined the densely overstruck words: the three prose words still marked illegible are physically occluded. Added the marginal bracket and isolated points.',extras=[('drawing','upper right','isolated point'),('drawing','beside cancelled upper-right note','curved bracket'),('drawing','right of morphism paragraph','two isolated points')],doubts=[{'line':'cancelled proof, bracketed sentence','reading':'mbs','alternatives':'objets','confidence':'medium'}])
