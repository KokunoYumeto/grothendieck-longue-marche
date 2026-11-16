from audit_page import audit
from pathlib import Path
p=Path('pages/MPL_36_002-052_36_scan041.tex')
old=p.read_text();new=old
new=new.replace(r'''\[
\boxed{\underline{\mathcal H}^{1}(X/S;\underline{\operatorname{Hom}}_{S-gr}(\unsure{\gamma|\sigma},G))
\xrightarrow{\sim}\underline{\operatorname{Hom}}_{S-gr}(\gamma,\underline{\mathcal H}^{1}(X/S,G))}
\]''',r'''\figure{\begin{tikzpicture}
\node[inner sep=5pt] (h) {$\underline{\mathcal H}^{1}(X/S;\underline{\operatorname{Hom}}_{S-gr}(\unsure{\gamma|\sigma},G))\xrightarrow{\sim}\underline{\operatorname{Hom}}_{S-gr}(\gamma,\underline{\mathcal H}^{1}(X/S,G))$};
\draw (h.north west)--(h.north east);\draw (h.south west)--(h.south east);\draw ([yshift=-2pt]h.north west)--([yshift=2pt]h.south west);
\end{tikzpicture}}''')
start=new.index(r'\diagram{\begin{tikzcd}[row sep=large]')
end=new.index(r'\margin{40}',start)
new=new[:start]+r'''\figure{\begin{tikzpicture}
\node[inner sep=5pt] (d) {\diagram{\begin{tikzcd}[row sep=large]
H^1(X/S;\underline{\operatorname{Hom}}_{S-gr}(\gamma,G))\arrow[d,shift left=18mm]\\
\underline{\operatorname{Hom}}_{S-gr}(\gamma,H^1(X/S,G))
\end{tikzcd}}};
\draw (d.north west)--([xshift=8mm]d.north east);\draw (d.south west)--([xshift=8mm]d.south east);\draw (d.north west)--(d.south west);\draw (d.north east)--(d.south east);
\end{tikzpicture}}
'''+new[end:]
audit(41,[(old,new)],notes='Whole page and bottom half reread. Restored the open right edge of the first enclosure and attached the bottom rectangle to the actual vertical diagram, with horizontal overshoots and the left-positioned downward arrow. Checked underlines, cancelled wording and unfinished equality; glyph uncertainty retained.')
