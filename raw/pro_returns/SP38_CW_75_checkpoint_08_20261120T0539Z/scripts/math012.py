"""Small explicit certificate for a witness variant; no manuscript recognition."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
n=4
reflections={b:tuple((b-x)%n for x in range(n)) for b in range(n)}
point_reflections={t:tuple((2*t-x)%n for x in range(n)) for t in range(n)}
fibres={b:[t for t in range(n) if point_reflections[t]==reflections[b]] for b in range(n)}
assert fibres=={0:[0,2],1:[],2:[1,3],3:[]}
assert all(tuple(v[v[x]] for x in range(n))==tuple(range(n)) for v in reflections.values())
result={'n':n,'all_reflections_x_to_b_minus_x':reflections,'sigma_t_x_to_2t_minus_x':point_reflections,'fibres_by_b':fibres,'all_reflections_involutive':True,'H_all_fibres_cardinality_two':False,'C_empty_or_cardinality_two':True}
(root/'decisions/scan012_n4_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
