import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(34,5);p.write_text(p.read_text().replace(r'\mathbf Z',r'\mathbb Z').replace(r'\mathbf P',r'\mathbb P'))
revise(34,5,r'\uline{globale} \inserted{cohomologique}',r'\inserted{cohomologique} \uline{globale}')
revise(34,5,r'\inserted{linéaire}',r'\inserted{\unsure{linéaire|linéaires}}')
audit(34,5,'Both halves, the long Néron-model insertion and two additional close crops checked. The cohomologique caret enters before globale, and its attachment has been corrected. The end of inserted linéaire(s) is now marked instead of choosing singular from grammar. Doubled Z and P have been encoded double-struck consistently with 003–004. The question at the marginal H^i, deleted Deligne phrase, empty reference brackets and degree ≥4 are all preserved.')
