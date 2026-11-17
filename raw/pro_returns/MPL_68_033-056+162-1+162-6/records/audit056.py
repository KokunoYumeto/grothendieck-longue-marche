import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit

audit(56, [
    (r'\Delta(\unsure{V|W})', r'\Delta(\unsure{W|V})'),
    (r'\deleted{b) $\unsure{\Delta}$}', r'\deleted{b) $\unsure{\Delta|\Delta_2}$}'),
], doubts=[
    ('lower diagram, top centre', r'\Delta(W)', r'\Delta(V)', 'low'),
    ('cancelled b) before Picard category', r'\Delta', r'\Delta_2', 'low'),
], comment='Whole and both halves reread. The overwritten central object looks more like W than V; W is placed first. Lower arrow points left, vertical connectors have no heads, the lower-left V_1 and right-hand phi subscript W_2 are retained literally. Cancelled Delta may carry a subscript 2.')
