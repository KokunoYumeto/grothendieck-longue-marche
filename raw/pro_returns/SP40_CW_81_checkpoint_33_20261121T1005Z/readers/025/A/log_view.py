import json,sys,datetime
from pathlib import Path
b=Path('out/readers/025/A');entry=json.load(sys.stdin)
a=json.loads((b/'view_audit.json').read_text())
entry.update(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),type='tight_crop',status='successful view',delivery_count=1)
a['events'].append(entry)
(b/'view_audit.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
m=json.loads((b/'crop_manifest.json').read_text())
for c in m:
 if c['path']==entry['path']:c['viewed']=True
(b/'crop_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
