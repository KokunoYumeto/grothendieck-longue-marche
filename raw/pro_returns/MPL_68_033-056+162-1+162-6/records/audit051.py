import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(51,[
 (r'\unsure{cela|trace}',r'\unsure{collier}'),
],doubts=[
 ('paragraph 3, typed word beneath handwritten trace','collier','middle and final type partly covered by added ink','medium'),
],comment='Read both halves and enlarged this copy s revisions. Underlying c/o and tall typed strokes support collier; the overtyped assemble correction and clipped bottom pairs remain marked. No text was filled from another copy.')
