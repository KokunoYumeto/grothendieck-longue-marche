"""Consolidate unchanged scan099 text and correct one inventory position."""
import json,subprocess,sys
from audit_support import load,commit,OUT
r,a,s=load(99)
assert not a['changes']
assert s==(OUT/'audit/scan099/proposed.tex').read_text()
item=next(x for x in r['inventory'] if x['element']=="Author's page number")
assert item['position']=='top right';item['position']='top centre'
r['notes'].append('The complete independent second reading confirms the text unchanged: all 23 comparison loci, seven recorded decisions, five certainty entries, four doubts and 13 inventory elements were reviewed. The author’s 17 is at top centre; the inventory position is corrected without a witness-error count. Main reader checked the existing native top half for that position and the new focused crop for the later groupoïdes, whose two separate i points confirm the existing diaeresis. The earlier singular groupoïde likewise retains its two points. No new mathematical check event.')
p=OUT/'documentation/root_view_ledger.json';j=json.loads(p.read_text())
crop='crops/scan099_audit_groupoides_diaeresis.jpg'
if crop not in j['99']['crops_seen']:j['99']['crops_seen'].append(crop)
j['99']['audit_inventory_view']='Reused existing native top half for author 17 position only; top centre confirmed.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=OUT/'documentation/notation_audit_updates.json';j=json.loads(p.read_text())
x=next(x for x in j if x.get('sign','').startswith('connait;'))
x['pages']='082, 085–086, 088, 093, 096, 098–099'
x['evidence']+=' Both the singular groupoïde and later plural groupoïdes on 099 have two detached i points; those diaereses remain, separately from the single-point forms on 088 and 096.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(99,r,a,s,
    'Complete independent second reading by reader_a. All 23 comparison loci, seven decisions, five certainty entries, four retained doubts and 13 inventory elements were reviewed. No transcription change or new doubt. The inventory location of author 17 is corrected to top centre after root checks the existing native half. The new later-groupoïdes crop confirms its two points; root also inspected it. No new mathematical check event.',
    [{'id':'099-no-change','decision':'retained after complete audit','reading':'Text unchanged; all four doubts retained.','evidence':'Complete audit report and saved image evidence.'},
     {'id':'A099-I01','decision':'accepted; inventory only','reading':'Author 17 at top centre.','evidence':'Existing native top half; number near x850 on 1677-pixel-wide page.','confidence':'high'}])
