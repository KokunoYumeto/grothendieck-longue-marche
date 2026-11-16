#!/usr/bin/env python3
"""Build a NEW modular search from complete standard-GAP source rows.

The failed native-collected attempt is neither modified nor silently reused.
Only the group source, genuine word templates and separately proved diagonal
power bounds are shared. Every vector in this search comes from the fresh
standard original-presentation collector.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,math
from pbc_source_coordinate_bounds import coordinate_bounds
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=CODE/'pbc_quotient86_original_source.json';s=json.loads(source.read_text())
collected=CODE/'pbc_quotient86_standard_recollection.json'
rows=json.loads(collected.read_text())
log=CODE/'pbc_quotient86_standard_recollection_resume13.out'
assert 'STANDARD_RECOLLECTION_COMPLETE' in log.read_text()
assert len(rows)==9083 and sum(r[1]=='identity' for r in rows)==9000
targets=[r[3] for r in rows if r[1]=='target'];assert len(targets)==1
extras={r[2][0]:r[3] for r in rows if r[1]=='extra'};assert sorted(extras)==list(range(1,83))
identities=[(r[2],r[3]) for r in rows if r[1]=='identity']
for _,kind,meta,vec,match in rows:
    assert kind in ('target','identity','extra') and len(vec)%2==0
    assert vec[::2]==sorted(set(vec[::2])) and all(isinstance(v,int) for v in vec)
M=2**14;n=86;bounds,_=coordinate_bounds(s);bounds=[math.gcd(v,M) for v in bounds]
data=CODE/'pbc_quotient86_standard2.dat';rowsfile=CODE/'pbc_quotient86_standard2_rows.dat'
def emit(f,w):f.write(' '.join(map(str,[len(w)]+w))+'\n')
with data.open('w') as f:
    f.write(str(n)+'\n'+' '.join(map(str,s['relative_orders']))+'\n')
    for w in s['powers']:emit(f,w)
    for i,j,w in s['conjugates']:emit(f,w)
    f.write(sha(source)+'\n'+str(M)+'\n71 9\n'+' '.join(map(str,bounds))+'\n')
    emit(f,targets[0])
    for i in range(1,83):emit(f,extras[i])
with rowsfile.open('w') as f:
    for meta,v in identities:emit(f,meta);emit(f,v)
initial=CODE/'pbc_quotient86_standard2_initial_rows.json'
initial.write_text(json.dumps(dict(source_sha256=sha(source),standard_collection_sha256=sha(collected),
                                  target=targets[0],extras=[extras[i] for i in range(1,83)]),separators=(',',':'))+'\n')
out=dict(status='PREPARED: complete fresh standard-GAP rows; no search conclusion',
         source_sha256=sha(source),standard_collection_sha256=sha(collected),
         standard_collection_output_sha256=sha(log),builder_sha256=sha(__file__),
         standard_templates=len(rows),identity_rows=len(identities),
         mismatches_against_failed_native_attempt=sum(not r[4] for r in rows),
         input_sha256=sha(data),rows_sha256=sha(rowsfile),initial_rows_sha256=sha(initial),
         modulus=M,coordinate_counts=dict(Counter(bounds)),
         permitted_corrections='Only the71 genuine original s-centralizer commutators',
         scope='Fresh G86 quotient computation only. A successful arithmetic search must pass independent original-row replay; then the two top homology bits still remain.')
(CODE/'pbc_quotient86_standard2_preparation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
