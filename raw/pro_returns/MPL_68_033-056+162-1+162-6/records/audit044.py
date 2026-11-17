import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(44,[
 (r'\deleted{\unsure{Soit}}',r'\deleted{\unsure{S|Soit}}'),
 (r'\unsure{une|la}',r'\unsure{la|une}'),
],doubts=[
 ('Globalisation, cancellation before X','S','Soit; compact overwritten glyph','low'),
 ('Globalisation, article after Theta','la','une','low'),
],comment='Re-read both halves and three enlarged glyph groups. The plus sign between the two E terms and the bracket without a comma are plainly present and are retained.')
