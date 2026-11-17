import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(41,[
 (r'e_v(\unsure{1|0})f=fe_u(\unsure{1|0})',r'e_v(\unsure{0|1})f=fe_u(\unsure{0|1})'),
 (r'\unsure{v}^{n-1}',r'\unsure{v|u}^{n-1}'),
],doubts=[
 ('first parenthesis, two evaluation arguments','0','1; both are thick looped forms','low'),
 ('delta_n expansion, first base','v','u; overwritten','low'),
],comment='Read both halves and enlarged the top insertion, evaluation digits and first coefficient. Loop-shaped digits are kept first in the doubt; the displayed c_ij and End_K(M) are not repaired.')
