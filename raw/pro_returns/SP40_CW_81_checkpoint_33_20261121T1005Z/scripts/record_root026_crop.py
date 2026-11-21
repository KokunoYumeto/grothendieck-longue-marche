"""Record an explicitly root-authored decision after its sole crop display."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, sys
OUT=Path(__file__).resolve().parents[1]
payload=json.load(sys.stdin)
plan=json.loads((OUT/'checks/scan026_root_crop_plan.json').read_bytes())
section=str(payload['section']).zfill(2)
item=next(row for row in plan['plan'] if row['section']==section)
audit_path=OUT/'checks/scan026_root_crop_audit.json'
audit=json.loads(audit_path.read_bytes())
assert payload['successful_display_observed_by_root'] is True
assert item['path'] not in {row['path'] for row in audit['viewed_once']}
jpath=OUT/'checks/scan026_root_decisions.json'
journal=json.loads(jpath.read_bytes())
assert section not in {row['section'] for row in journal['decisions']}
now=datetime.now(timezone.utc).isoformat()
digest=hashlib.sha256((OUT/item['path']).read_bytes()).hexdigest()
if 'sha256' in item: assert digest==item['sha256']
event={key:item[key] for key in ['path','bbox','rotation','created_by_root','source_loci','target_scope_note']}
event.update(sha256=digest,decision_sections=[section],successful_display_count=1,
    source_image=plan['source_image'],source_coordinate_system='full scan, top-left origin, pixels',recorded_utc=now)
audit['viewed_once'].append(event)
audit['total_distinct']=len(audit['viewed_once'])
audit['last_decision_recorded_utc']=now
row={'section':section,'title':payload['title'],'crop_path':item['path'],'crop_sha256':digest,
    'source_loci':item['source_loci'],'recorded_utc':now,'body':payload['body']}
for key in ['locus_decisions','original_C_rows','assembly']:
    if key in payload: row[key]=payload[key]
journal['decisions'].append(row)
for path,data in [(audit_path,audit),(jpath,journal)]:
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
md=['# Root decisions — scan026','',
    'All three final returns, complete TeX/Markdown/report contents, all three full pairwise TeX diffs, and the complete physical-locus union were read before the first root image. Each decision below follows one successfully delivered local crop. Root viewed no whole scan or supplied half. No mathematical proof check is claimed.','']
for row in journal['decisions']:
    md.extend([f"## {row['section']} — {row['title']}",'',
        f"Crop `{row['crop_path']}`; SHA-256 `{row['crop_sha256']}`. Loci: {', '.join(row['source_loci'])}.",'',
        row['body'].rstrip(),''])
(OUT/'checks/scan026_root_journal.md').write_text('\n'.join(md))
print(json.dumps({'section':section,'recorded_utc':now,'distinct_crops':audit['total_distinct']}))
