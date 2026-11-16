from audit_page import audit
changes=[
(r'\margin{$\phi$}',r'\margin{\figure{\begin{tikzpicture}\node at(0,0){$\phi$};\draw[rotate=15](0,0)ellipse(.35 and .5);\end{tikzpicture}}}'),
(r'\margin{$\ell$}',r'\margin{\figure{\begin{tikzpicture}\node at(0,0){$\ell$};\draw[rotate=-20](0,0)ellipse(.3 and .5);\end{tikzpicture}}}'),
(r'\inserted{$E$}',r'\inserted{\figure{\begin{tikzpicture}[baseline=(e.base)]\node(e){$E$};\draw(0,0)ellipse(.27 and .22);\draw(.17,-.18)--(0,-.45);\end{tikzpicture}}}'),
(r'$\xi\in\operatorname{Biext}(P,Q;G)$,',r'\figure{\begin{tikzpicture}[baseline=(x.base)]\node(x){$\xi\in\operatorname{Biext}(P,Q;G)$};\draw(0,0)ellipse(1.9 and .4);\draw[->](-1.9,-.2)..controls(-2.2,-.4)and(-3.7,-.2)..(-4.1,-.45);\end{tikzpicture}},'),
(r'soit $\ell$ un nombre',r'soit \figure{\begin{tikzpicture}[baseline=(l.base)]\node(l){$\ell$};\draw[rotate=-10](0,0)ellipse(.22 and .5);\end{tikzpicture}} un nombre'),
(r'(2.2.3)\qquad\ell P=P,',r'(2.2.3)\qquad\figure{\begin{tikzpicture}[baseline=(l.base)]\node(l){$\ell$};\draw[rotate=-20](0,0)ellipse(.23 and .55);\end{tikzpicture}} P=P,')
]
# Last displayed relation may carry no punctuation in first pass; annotate the ell alone in that case.
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'pages/MPL_36_002-052_36_scan034.tex'
s=p.read_text()
if changes[-1][0] not in s:
 changes[-1]=(r'(2.2.3)\qquad\ell P=P',r'(2.2.3)\qquad\figure{\begin{tikzpicture}[baseline=(l.base)]\node(l){$\ell$};\draw[rotate=-20](0,0)ellipse(.23 and .55);\end{tikzpicture}} P=P')
audit(34,changes,notes='Rotated whole typescript re-read. Reproduced previously missing circles around marginal phi/ell, inserted E, xi-membership expression and two in-text ell glyphs. Added leader on xi annotation. Rechecked cancellation of proof deferral and replacement by cf.2.3, superscript 1 additions, and all multiplication-by-m labels.',extras=[('drawing','around xi membership expression','oval and curved leftward leader'),('drawing','inserted E','oval and insertion tail'),('drawing','left margin beside (2.1.4)','circled phi'),('drawing','left margin lower','circled ell'),('drawing','last paragraph and (2.2.3)','two faint ell ovals')])
