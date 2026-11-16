import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(34,11);p.write_text(p.read_text().replace(r'\mathbf Z',r'\mathbb Z'))
revise(34,11,r'\uline{il existe}',r'\unsure{\deleted{\unsure{on a}}\inserted{il existe}|\uline{il existe}}')
add_element(34,11,'deletion','middle after pour tout ell','on a? beneath long stroke; state alternative underlining')
add_element(34,11,'insertion','above long stroke after pour tout ell','il existe; state alternative underlining')
audit(34,11,'Both halves and a close crop of il existe checked. Its long baseline stroke extends far to the left and may cover earlier words; the state is now explicitly doubtful between a cancelled tentative on a plus insertion, and simple underlining. This is a low-confidence state/reading issue rather than an asserted reconstruction. Double-struck Z has been corrected. The warning about the lack of a natural choice, the primitive-roots insertion, and the cancelled peut are fully retained.')
