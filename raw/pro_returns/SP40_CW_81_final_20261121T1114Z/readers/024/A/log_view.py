from pathlib import Path
from datetime import datetime,timezone
import json,sys
p=Path('out/readers/024/A/view_audit.json');a=json.loads(p.read_text())
name,result,note=sys.argv[1:4]
a['events'].append({'ordinal':len(a['events'])+1,'path':'out/readers/024/A/'+name,'kind':'local_crop','result':result,'recorded_utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'inspection':note})
a['pause']['status']='resumed after checkpoint25; no successful image reopened'
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
