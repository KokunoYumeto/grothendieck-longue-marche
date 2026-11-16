import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
revise(34,15,r'que deux équations séparables à coefficients',r'que deux équations séparables \unsure{\deleted{de $K$}|\inserted{de $K$}} à coefficients')
add_element(34,15,'deletion','lower, above gap before à coefficients','de K; deletion/insertion state uncertain')
audit(34,15,'Both halves re-read, followed by a close crop of the continuity-of-roots sentence. The separate de K above the coefficient condition was omitted in the first pass; it is now included with an explicit deletion/insertion-state alternative. The masculine voisins, plain V tensor subscript, all headless group connectors and the cancelled alternative argument are retained. The proof is transcribed as three lettered parts, without supplementing its invoked finiteness or continuity results.')
