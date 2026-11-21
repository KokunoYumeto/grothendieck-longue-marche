from pathlib import Path
from datetime import datetime,timezone
import json,sys
root=Path(__file__).parent
name,note=sys.argv[1:3]
p=root/'view_audit.json';a=json.loads(p.read_text())
assert not any(e['path'].endswith('/'+name) for e in a['events']),name
c=json.loads((root/'crops.json').read_text());m=next(x for x in c if x['path']==name);m['successfully_viewed']=True
now=datetime.now(timezone.utc).isoformat()
a['events'].append({'sequence':len(a['events'])+1,'path':str(root/name),'kind':'deep_crop','success':True,'view_count':1,'recorded_utc':now,'bbox':m['bbox'],'note':note})
p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n');(root/'crops.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
