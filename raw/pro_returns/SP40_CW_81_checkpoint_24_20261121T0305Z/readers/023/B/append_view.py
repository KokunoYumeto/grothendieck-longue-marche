from pathlib import Path
import json,sys
p=Path('/workspace/scratch/94548b74fbe0/out/readers/023/B/view_audit.json')
d=json.loads(p.read_text())
name,utc=sys.argv[1:3]
assert not any(v['path']==name for v in d['views']),name
v={'sequence':len(d['views'])+1,'path':name,'purpose':'unique target enlargement, once','utc':utc,'successful':True}
d['views'].append(v)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(name,utc)
