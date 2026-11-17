import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(43,[
 (r'aux \deleted{\unsure{les}}',r'aux \deleted{\unsure{tous les}}'),
 (r'\structure',r'\structure'),
] if False else [
 (r'aux \deleted{\unsure{les}}',r'aux \deleted{\unsure{tous les}}'),
 (r'G_a$-Module \unsure{les}',r'G_a$-Module \unsure{lin.|les}'),
],doubts=[
 ('middle, cancellation after aux','tous les','t...s les; first word heavily crossed','low'),
 ('last word at lower right edge','lin.','les; loc.','low'),
 ('semilinearity diagram, vertical stroke',r'\downarrow','shaft clear, terminal stroke faint','medium'),
],comment='Both halves re-read, with enlarged cancellation, overwritten coefficient-ring letter and lower clipped word. Added the first cancelled word; the last abbreviation remains uncertain.')
