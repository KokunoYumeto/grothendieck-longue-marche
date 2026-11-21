import json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
p=r/'review/accepted/149_scan115.json';d=json.loads(p.read_text());h=d['hand_observations'][-1];assert h['habit'].startswith('Accent varies within the same leaf:');h['places']='main line 12, quoted modele; main line 15, underlined modèle';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=r/'second/149_scan115_update_plan.json';d=json.loads(p.read_text());d['hand_observations_append'][0]['places']=h['places'];d['schema_repair']='Added required places field after assemble reported its absence; no reading changed.';p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
