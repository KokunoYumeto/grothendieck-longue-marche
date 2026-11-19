from work import *
from record_helpers import *
def audit(n,comment):
 assert not (OUT/'records/frozen_hashes.json').exists()
 p=OUT/'records'/f'scan{n:03}.json';r=json.loads(p.read_text());r['audited_utc']=utc();r['audit_comment']=comment;p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 with (OUT/'progress.log').open('a') as f:f.write(f'scan {n:03} audited {utc()}\n')
 print(f'Audited {n:03}: {comment}')
def amend(n,replacements,decisions=(),doubts=()):
 assert not (OUT/'records/frozen_hashes.json').exists()
 p=OUT/'pages'/Path(mapping(n)['codex_file']).name;s=p.read_text()
 for a,b in replacements:
  assert a in s,(n,a);s=s.replace(a,b)
 p.write_text(s)
 q=OUT/'records'/f'scan{n:03}.json';r=json.loads(q.read_text());r['changes']+=list(decisions);r['doubts']+=list(doubts);q.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 regenerate()
