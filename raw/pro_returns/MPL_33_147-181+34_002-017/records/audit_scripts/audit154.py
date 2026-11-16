import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,154);t=p.read_text().replace(r'\underline{D}',r'\unsure{\underline{D}|D}')
t=t.replace(r'\mathrm{R}^{\unsure{\bullet}}(f\times g)^!',r'\mathrm{R}^!(f\times g)^{\unsure{!}}').replace(r'\mathrm{R}^{\unsure{\bullet}}f^!',r'\mathrm{R}^!f').replace(r'\mathrm{R}^{\unsure{\bullet}}g^!',r'\mathrm{R}^!g')
t=t.replace('K_X',r'\unsure{K|R}_X').replace('K_Y',r'\unsure{K|R}_Y').replace('K_{X',r'\unsure{K|R}_{X')
p.write_text(t)
audit(33,154,'Both halves and the small inserted formula were examined again. Corrected three upper marks from tentative bullets to visible exclamation marks and, in the right member, attached them to R rather than to f or g. The additional mark after (f×g) remains explicitly doubtful. The handwritten dualizing-complex letter resembles R as well as K here and is now flagged; the left-pointing boxed isomorphism, finite Tor hypothesis, and deleted finite-Tor condition on P,Q were checked.')
