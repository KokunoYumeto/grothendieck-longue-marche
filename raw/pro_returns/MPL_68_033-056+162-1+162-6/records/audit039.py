import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit
audit(39,[
 (r'\unsure{\longleftarrow|\longmapsto}',r'\unsure{\longleftarrow\!\mid|\longmapsto}'),
 (r'=\exp(\lambda\unsure{u_K|u_{K\prime}})',r'=\unsure{\operatorname{Exp}|\exp}(\lambda\unsure{u_K|u_{K\prime}})'),
] if False else [
 (r'\unsure{\longleftarrow|\longmapsto}',r'\unsure{\longleftarrow\!\mid|\longmapsto}'),
 (r'=\exp(\lambda',r'=\unsure{\operatorname{Exp}|\exp}(\lambda'),
],doubts=[
 ('(**), arrow from e_u towards u',r'\longleftarrow\!\mid',r'\longmapsto','medium'),
 ('exponential display',r'\operatorname{Exp}',r'\exp','medium'),
],comment='Read both halves and three enlarged details; retained the left arrowhead and its right terminal stroke, and marked the capital-looking E. The finite-support claim for arbitrary M remains as written.')
