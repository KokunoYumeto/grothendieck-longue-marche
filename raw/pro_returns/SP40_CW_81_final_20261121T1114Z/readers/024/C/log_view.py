from pathlib import Path
import json,datetime,sys
p=Path('out/readers/024/C/view_audit.json');d=json.loads(p.read_text())
path,status,purpose,observed=sys.argv[1:5]
d['events'].append({'sequence':len(d['events'])+1,'path':path,'kind':'crop','status':status,'event_recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':purpose,'observed':observed})
d.pop('safe_boundary',None)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
