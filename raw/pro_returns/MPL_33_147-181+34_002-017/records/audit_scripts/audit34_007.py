import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(34,7);p.write_text(p.read_text().replace(r'\mathbf Z',r'\mathbb Z'))
revise(34,7,r'\margin{$(2.3.4)',r'\margin{$(2.3.\unsure{3|4})')
revise(34,7,r'$\pi\longrightarrow\pi_0$',r'$\pi\unsure{-|\longrightarrow}\pi_0$')
audit(34,7,'Both halves and enlarged final/tensor paragraphs checked. Double-struck Z corrected throughout. The interlinear abandoned formula number looks 2.3.3 rather than 2.3.4 and now records 3|4; the full following display still reads 2.3.4. The final pi-to-pi0 stroke has no unambiguous head and now prefers a plain dash. The cancelled sont compatibles aux remains cancelled despite the resulting fragmentary syntax; inserted et and the possible ou remain separate. The actual dots after the abandoned Z_l(1) formula are retained.')
