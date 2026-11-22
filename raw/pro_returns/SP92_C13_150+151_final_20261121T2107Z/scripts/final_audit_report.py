"""Verify final bookkeeping and sealed readings; no reading or typesetting is performed."""
from pathlib import Path
import csv,json,hashlib,collections,datetime
W=Path(__file__).resolve().parents[1]
order=(W/'page_order.txt').read_text().splitlines()
records=[json.loads((W/'records'/f'{p}.json').read_text()) for p in order]
errors=[]
def require(condition,message):
 if not condition:errors.append(message)
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
sealed_files=0;boxes=0;different=0;changed=0;token_runs=0
for r in records:
 pg=r['page'];require(r.get('audited') and r.get('root_reviewed'),pg+' missing completed review')
 require((W/'pages'/f'{pg}.tex').read_bytes()==(W/'records'/f'{pg}.tex').read_bytes(),pg+' page/candidate mirror mismatch')
 c=json.loads((W/'second'/f'{pg}_comparison.json').read_text())
 for suffix,sha in c['input_sha256'].items():
  f=W/'second'/f'{pg}_{suffix}.tsv';require(hashlib.sha256(f.read_bytes()).hexdigest()==sha,pg+' changed sealed '+suffix);sealed_files+=1
 require(len({x['id'] for x in r['changes']})==len(r['changes']),pg+' duplicated current change ID')
 for x in r['changes']:
  require(x['against_C'] or x['against_H'],pg+'/'+x['id']+' not a witness difference')
  require(x['kind'] in allowed,pg+'/'+x['id']+' noncanonical kind '+x['kind'])
 boxes+=r['audit_boxes'];different+=r['audit_differing_boxes'];changed+=r['audit_changed_boxes'];token_runs+=r['audit_token_difference_runs']
coverage=[x for r in records for x in r['diff_coverage']]
require(len(coverage)==1032,'C/H difference count is not1032')
require(len({x['diff_id'] for x in coverage})==1032,'C/H difference IDs not unique')
require(len(order)==25 and boxes==389,'page/box count mismatch')
allchanges=[x for r in records for x in r['changes']]
confidence=dict(collections.Counter(x['confidence'] for x in allchanges))
events=list(csv.DictReader((W/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
decisions=list(csv.DictReader((W/'decisions.tsv').open(),delimiter='\t'))
require(len(decisions)==101,'mark decision count mismatch')
required=['SP92_C13_150+151_transcription.tex','SP92_C13_150+151_changes.md','SP92_C13_150+151_collation.tsv','decisions.tsv','SP92_C13_150+151_doubts.md','SP92_C13_150+151_inventory.csv','SP92_C13_150+151_notes.md','CHECK_EVENTS.tsv','progress.log','SP92_C13_150+151_sheet_feedback.md','SP92_C13_150+151_hand_log.md']
for f in required:require((W/f).is_file(),f+' missing')
result=dict(verified_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),errors=errors,pages=25,source_difference_rows=len(coverage),source_doubt_decisions=len(decisions),sealed_box_first_second_files=sealed_files,blind_boxes=boxes,differing_boxes=different,changed_boxes=changed,token_difference_runs=token_runs,changes=len(allchanges),against_C=sum(x['against_C'] for x in allchanges),against_H=sum(x['against_H'] for x in allchanges),confidence=confidence,inventory_elements=sum(len(r['inventory']) for r in records),remaining_doubt_entries=sum(len(r['doubts']) for r in records),mathematical_check_events=len(events),crop_images=len(list((W/'crops').glob('*.png'))),ocr_used=False,external_research_used=False,tex_compiled=False)
(W/'records/final_audit_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
