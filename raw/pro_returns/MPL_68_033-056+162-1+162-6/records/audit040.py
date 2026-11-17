import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(40,[
 (r'\margin{\unsure{univ.}',r'\margin{\unsure{univ\textsuperscript{t}.|univ.}'),
 (r'\deleted{\unsure{c}}',r'\deleted{\unsure{c|et}}'),
],doubts=[
 ('right margin by first proof display',r'univ\textsuperscript{t}.','univ.','medium'),
 ('Cor, small cancellation above sont','c','et','low'),
],comment='Re-read both halves, including all four conditions, and enlarged the tiny cancellation and marginal abbreviation. The missing bar in the first proposition is retained.')
