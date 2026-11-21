"""Root-accepted descriptive fixes from the final 077/078 QA reports."""
from pathlib import Path
from datetime import datetime, timezone
import json, re
B=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
journal=B/'reviews/final_077_078_metadata_journal.json';assert not journal.exists()
rp=B/'reviews/149_scan078.json';r=json.loads(rp.read_text())
qa=json.loads((B/'reviews/final_078_review_a.json').read_text())
records=[]
for x in qa['findings']:
 m=re.fullmatch(r'(source_line_map|inventory)\[(\d+)\]\.(text|position)',x['field']);assert m
 field,number,key=m[1],int(m[2]),m[3]
 assert r[field][number][key]==x['current_value'],x['field']
 r[field][number][key]=x['needed_value']
 records.append(dict(page='149_scan078',field=x['field'],before=x['current_value'],after=x['needed_value'],utc=stamp))
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
r77=json.loads((B/'reviews/149_scan077.json').read_text())
expected='kernel; the earlier locally hatched Ker remains tentative, while the following Ker is readable within the larger canceled display'
assert r77['abbreviations'][4]['expansion']==expected
records.append(dict(page='149_scan077',finding='077-C01',field='abbreviations[4].expansion',before='kernel; the written operator remains tentative',after=expected,utc='2026-11-21 16:27:56 UTC',recorded_utc=stamp))
journal.write_text(json.dumps(dict(completed_utc=stamp,scope='Current descriptive metadata only; authoritative pages and fixed second-pass records unchanged.',edits=records),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'metadata_fixes':len(records),'utc':stamp}))
