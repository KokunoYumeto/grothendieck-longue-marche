"""Consolidate the complete no-change second reading of scan097."""
import json,subprocess,sys
from audit_support import load,commit,OUT
r,a,s=load(97)
assert not a['changes']
assert s==(OUT/'audit/scan097/proposed.tex').read_text()
r['notes'].append('The full independent second reading confirms all 43 comparison loci, 11 recorded decisions including seven assigned marks, four resolved certainty entries, both diagrams and all 12 inventory elements. All six inherited doubts remain. A first crop of i.e. independently confirms its internal and terminal points; main reader also inspected it. No text change, omitted element or mathematical check event.')
p=OUT/'documentation/root_view_ledger.json';j=json.loads(p.read_text())
crop='crops/scan097_audit_ie.jpg'
if crop not in j['97']['crops_seen']:j['97']['crops_seen'].append(crop)
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
p=OUT/'documentation/notation_audit_updates.json';j=json.loads(p.read_text())
x=next(x for x in j if x.get('sign','').startswith('ie.;'))
x['pages']='080, 086, 090, 093–094, 097'
x['evidence']+=' The new audit crops on 094 and 097 separately confirm both points in their i.e. occurrences; both were also inspected by the main reader.'
p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
subprocess.run([sys.executable,str(OUT/'scripts/canonical_notation.py')],check=True)
commit(97,r,a,s,
    'Complete independent second reading by reader_b, with no proposed change. All 43 comparison loci, 11 recorded decisions including seven assigned marks, six doubts, four resolved certainty entries and 12 inventory elements were reviewed. The main reader inspected the new i.e. crop, which confirms both abbreviation points without changing the text. No new inventory element or mathematical check event.',
    [{'id':'097-no-change','decision':'retained after complete audit','reading':'Consolidated page unchanged; six doubts retained.','evidence':'Complete audit report and the independently inspected i.e. crop.'}])
