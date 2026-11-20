"""Record the root reader's completed second visual readings; no recognition."""
from record_reading import *
def get(n):
 return runpy.run_path(str(RECORDS/f'{n:03}.py'))['DATA']
def put(d):
 (RECORDS/f"{d['scan']:03}.py").write_text('DATA = '+pprint.pformat(d,width=140,sort_dicts=False)+'\n')
def audited(n,summary):
 d=get(n)
 if d.get('audit'):raise RuntimeError('Audit already recorded')
 # Isolated archival pencil foliation is a different, unnamed hand.
 d['inventory']=[tuple(x[:3])+('another unnamed hand',) if x[0]=='margin note' and x[2]==str(n-1) and any(w in x[1].lower() for w in ('bottom','lower')) else x for x in d['inventory']]
 d['audit']={'utc':now(),'summary':summary}
 put(d);render()
 p=ROOT/'audit_log.md'
 if not p.exists():p.write_text('# Second visual reading\n\nEvery entry below was made by the same reader after comparing that whole scan with the consolidated page. These are audit observations, not additional independent witness-difference counts.\n\n')
 with p.open('a') as f:f.write(f"## Scan {n:03}\n\n{summary}\n\nCompleted {d['audit']['utc']}.\n\n")
 with (ROOT/'progress.log').open('a') as f:f.write(f"scan {n:03} audited {d['audit']['utc']}\n")
 print(f'scan {n:03} audited')
