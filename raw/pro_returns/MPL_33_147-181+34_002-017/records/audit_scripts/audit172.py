import sys
sys.path.insert(0,'/workspace/scratch/0ad792daea27/MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
revise(33,172,r"\unsure{Généraliser} aux faisceaux d'anneaux \unsure{plus généraux}.",r"\unsure{Généraliser} : aux faisceaux d'anneaux ``\unsure{plus généraux}''.")
revise(33,172,r"alors $\operatorname{Ext}^i(F,C)=0$",r"alors $\operatorname{Ext}^i(F,\unsure{G|C})=0$")
revise(33,172,r"\unsure{quotient} d'un \unsure{produit}",r"\unsure{quotient} d'un \unsure{produit|générateur}")
audit(33,172,'Both halves and enlarged proof and rotated margin re-read. The two horizontal strokes after plat are retained as an equals sign; the first Ext second argument is marked G|C because its internal stroke differs from the later open C. The marginal quotation marks and colon are restored. The quotient/product wording remains a low-confidence reading, with générateur as an ink-compatible alternative, not an imposed proof correction. The headless X-prime--X stroke, first overwritten Ext alphabet and the two faint margin strokes are retained.')
