from audit_page import audit
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'pages/MPL_36_002-052_36_scan031.tex'
s=p.read_text()
old=r'\begin{tikzcd}[column sep=small]0 \arrow[r]'
old2=r'\begin{tikzcd}[column sep=small]0 \arrow[r,no head]'
changes=[
(r'\inserted{canonique}',r'\inserted{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {canonique};\draw (0,0) ellipse (.8 and .22);\end{tikzpicture}}}'),
(r'\inserted{\unsure{resp.}}',r'\inserted{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {\unsure{resp.}};\draw (0,0) circle (.35);\end{tikzpicture}}}'),
(r'\text{ce dernier résulte de }{}_nM\'=0',r'\text{ce dernier résulte de }{}_n\unsure{M|M\'}=0'),
(r'Soit en effet \unsure{\ldots}',r'Soit en effet \figure{\begin{tikzpicture}[baseline]\draw(0,.08)--(.1,.04);\draw(.16,.04)--(.26,.04);\draw(.31,.03)--(.43,.06);\draw(.53,.04)--(.82,.07);\draw(.94,.04)--(1.06,.08);\end{tikzpicture}}'),
(r'\mathbf Z',r'\unsure{\mathbb Z|\mathbf Z}'),
(old,r'\diagram{'+old),
(old2,r'\diagram{'+old2),
(r'& 0\end{tikzcd}',r'& 0\end{tikzcd}}')
]
# Prime must remain a literal, not a TeX accent control sequence.
changes=[(a.replace("\\'","'"),b.replace("\\'","'")) for a,b in changes]
audit(31,changes,notes='Whole page and enlarged middle/lower regions and rotated margin notes audited. Circled canonique and resp. now reproduced. Faint strokes after Soit en effet are drawn rather than treated as a placeholder ellipsis. Prime in the last divisibility premise is uncertain and no longer silently supplied. Integer alphabet flagged where doubled strokes may be overwritten bold lettering. Final two exact sequences now wrapped with diagram macros; literal A-prime in the first term of the second sequence remains primary.',extras=[('drawing','above first paragraph insertion','oval around canonique'),('drawing','divisibility conditions','circle around resp.'),('drawing','after Soit en effet','five short separated pen strokes')],doubts=[{'line':'divisibility parenthesis','reading':'M','alternatives':"M'",'confidence':'medium'},{'line':'Ext arguments and final coefficient modules','reading':'blackboard Z','alternatives':'bold Z / retraced plain Z','confidence':'medium'}])
