import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,167);t=p.read_text().replace(r'\underline{D}',r'\unsure{\underline{D}|D}').replace(r'\unsure{R_X|A_X}',r'\unsure{A_X|R_X}')
t=t.replace(r'\margin{+ résolution et pureté sur $X$ -------}',r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)--(2.25,2.25)--(5.6,2.25);
\draw (.12,0)--(2.37,2.13)--(5.6,2.13);
\node[anchor=north west,align=left] at (2.35,1.9) {+ résolution et\\pureté sur $X$\\-------};
\end{tikzpicture}}}''')
p.write_text(t)
add_element(33,167,'drawing','lower right margin','double angled frame enclosing resolution and purity qualification')
audit(33,167,'Re-read both halves, exceptional superscript and subscript on R, the hypotheses, and the lower marginal qualification. Reproduced its double angled frame. The last coefficient symbol appears A_X before considering mathematical expectations, so that is now the first alternative to R_X; D-baseline uncertainty is marked consistently with the earlier duality sheets.')
