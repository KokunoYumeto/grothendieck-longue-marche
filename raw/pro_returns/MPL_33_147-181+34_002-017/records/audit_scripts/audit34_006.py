import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(34,6);t=p.read_text().replace(r'\mathbf Z',r'\mathbb Z').replace(r'\mathbf P',r'\mathbb P');p.write_text(t)
revise(34,6,r'\unsure{2.3|2.2}.',r'''\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) circle(0.06);\draw (0.06,0)--(0.85,0.02);
\draw (1.02,0.85)..controls(0.9,0.35) and(1.03,0.2)..(1.4,0.08)..controls(1.07,-0.1) and(1.02,-0.35)..(0.94,-0.8);
\end{tikzpicture}}}
\unsure{2.3|2.2}.''')
add_element(34,6,'drawing','left of overwritten 2.3/2.2','open circle, horizontal stroke and curved bracket')
audit(34,6,'Both halves re-read, including the full cancelled lower block. The Z/P outlines have been made double-struck. The open circle with horizontal stroke and curved left bracket beside the overwritten paragraph number was missing from the first pass and is now drawn and inventoried. No n was supplied before the right-hand K-bar-star in the cancelled display; the repeated cancelled u subscripts and overwritten residue formula remain explicit. The final empilements reading remains low confidence.')
