"""Export the exact finite-residue null vectors as nominated root tests."""
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parents[1]
p=r/'code/e53_upper_residue_search.json';d=json.loads(p.read_text())
v=[[(-1 if a==2 else a) for a in row] for row in d['residue_nullspace_candidates']]
q=r/'code/e53_upper_root_candidates.txt';q.write_text(json.dumps(v)+'\n')
print(json.dumps({'status':'PASS','candidate_count':len(v),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'data_sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'scope':'These vectors are only nominated exact root tests.'},indent=2))
