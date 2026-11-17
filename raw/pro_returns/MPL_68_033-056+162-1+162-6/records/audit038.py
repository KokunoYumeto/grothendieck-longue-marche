import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(38,[
 (r'On voit de \unsure{même}',r'On voit de $=$'),
 (r'\unsure{Soit|Si}',r'Soit'),
 (r'\overline G_{aK}\unsure{\longrightarrow}',r'\overline G_a\unsure{(K)|{}_K}\unsure{\longleftarrow|\longrightarrow}'),
],doubts=[
 ('lower rewritten line, cancelled group and arrow',r'\overline G_a(K)\longleftarrow',r'\overline G_{aK}; arrow overwritten','low'),
],comment='Re-read both halves; enlarged the coefficient condition and lower rewritten sentence. Corrected expanded shorthand and the first reading of the cancelled arrow; did not regularise the coefficient subscripts.')
