#!/usr/bin/env python3
"""Copy exact, already frozen inputs for the positional53 continuation."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
W=R.parent
(R/'inputs').mkdir(exist_ok=True)
sources={
 'e122_literal_unit_witnesses.json':'research_e122/inputs/e122_literal_unit_witnesses.json',
 'e122_literal_unit_ring.json':'research_e122/code/e53_literal_unit_ring.json',
 'e121_normalizer_module.json':'research_e122/inputs/e121_normalizer_module.json',
}
rows=[]
for name,source in sources.items():
 p=W/source;q=R/'inputs'/name
 if q.exists():assert q.read_bytes()==p.read_bytes()
 else:shutil.copyfile(p,q)
 rows.append({'source':source,'copy':'inputs/'+name,'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
(R/'inputs/manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'status':'PASS','immutable_inputs':rows},indent=2))
