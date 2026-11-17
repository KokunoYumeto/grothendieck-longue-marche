import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(46,[
 ('Supposons $NA$ nilpotent',r'Supposons $NA$ \unsure{nilp.t|nilpotent}'),
 (r'\unsure{autom.|opérateur}',r'opérateur'),
 (r'\xrightarrow{\sim}G_K',r'\simeq G_K'),
],doubts=[
 ('first corollary, after NA','nilp.t','nilpotent; visibly compressed ending after dot','medium'),
],comment='Read both halves and four enlarged details. The first corollary says opérateur diff; the final correspondence uses a bare isomorphism sign, without an arrow. Both were corrected from the ink.')
