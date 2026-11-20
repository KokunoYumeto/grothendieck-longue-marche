"""Record the root reader's second image audit; does not inspect images itself."""
from workflow import *
ORDER=[139,141,142,143,144,147,148,149,150,151,152,157,159,160,161,162,163,164,165,172,173,174,176,177,179]
def amend(scan,replacements=(),rows=(),doubts=None,extra='',notes=None):
 p=ROOT/'pages'/f'15_scan{scan}.tex';t=p.read_text()
 for a,b in replacements:
  assert a in t,(scan,a)
  t=t.replace(a,b)
 p.write_text(t)
 p=ROOT/'records'/f'{scan}.json';d=json.loads(p.read_text())
 d['rows'].extend(rows)
 if doubts is not None:d['doubts']=doubts
 if extra:d['extra']+='\nSecond audit: '+extra
 if notes is not None:d['notes']=notes
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 assemble()
def audited(scan,evidence):
 p=ROOT/'progress.log';log=p.read_text();done=[int(s) for s in re.findall(r'^scan (\d+) audited ',log,re.M)]
 assert scan==ORDER[len(done)],(scan,done)
 with p.open('a') as f:f.write(f'scan {scan:03d} audited {utc()}\n')
 with (ROOT/'audit_notes.md').open('a') as f:f.write(f'## Scan {scan}\n\n{evidence}\n\n')
