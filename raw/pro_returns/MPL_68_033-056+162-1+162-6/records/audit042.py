import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(42,[
 (r'De \unsure{même}',r'De $=$'),
 (r"\unsure{d'endom|d'autom.}",r"d'endom"),
],comment='Both halves re-read; replaced expanded shorthand by the two visible horizontal strokes. The corollary reads d endom, and all tensor factors and indices were checked.')
