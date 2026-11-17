import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(37,[
 (r'\unsure{\bar e_x|e_x}(\lambda)',r'\unsure{\varphi_x|\bar e_x}(\lambda)'),
 (r'on définit de \unsure{même}',r'on définit de $=$'),
],doubts=[
 ('lower half of top image, evaluation after i.e.',r'\varphi_x',r'\bar e_x, heavily overwritten','low'),
],comment='Read both halves and enlarged verb, evaluation symbol and clipped parenthesis. Preserved the literal equals-sign shorthand; the overwritten evaluation letter is marked uncertain.')
