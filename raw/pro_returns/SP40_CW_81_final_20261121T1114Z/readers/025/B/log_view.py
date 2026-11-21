import json,datetime,sys
from pathlib import Path
p=Path('out/readers/025/B/view_audit.json');d=json.loads(p.read_text());name=sys.argv[1];m=Path('out/readers/025/B/crop_manifest.json');cs=json.loads(m.read_text());c=next(c for c in cs if c['path']==name)
assert not c['viewed']
c['viewed']=True;d['events'].append({'image':name,'kind':'tight_crop','successful':True,'view_count':1,'logged_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bbox':c['bbox'],'purpose':c['purpose']})
p.write_text(json.dumps(d,indent=2)+'\n');m.write_text(json.dumps(cs,indent=2)+'\n')
