"""Consolidate the complete no-change second reading of scan090."""
import json
from audit_support import load, commit, OUT

r,a,s=load(90)
assert not a['changes']
p=OUT/'documentation/root_view_ledger.json'
ledger=json.loads(p.read_text())
crop='crops/scan090_audit_sous_groupe.jpg'
if crop not in ledger['90']['crops_seen']:
    ledger['90']['crops_seen'].append(crop)
p.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
r['notes'].append('The complete independent second reading confirms all 48 comparison places, 15 assigned C marks and 26 inventoried elements. All 12 current doubtful loci remain explicit. The newly focused, previously agreed sous-groupe has a compressed middle and separate final s-like hook before the hyphen; the main reader inspected its saved crop and retained the word. The dark slanted note remains separate from crossing main-text strokes. No new correction or mathematical check event is recorded.')
commit(90,r,a,s,
    'Complete independent second reading by reader_b, including the whole image and both native halves once. All 48 current comparison places, 15 assigned C marks and 26 inventory elements were reviewed. All 12 doubts remain at the same certainty. The main reader inspected the sole new agreed-token crop and retained sous-groupe. No text change or new mathematical check event.',
    [{'id':'090-no-change','decision':'retained complete page',
      'evidence':'The full second reading confirms the current text and all twelve explicit doubts. The saved new prefix crop supports the existing sous-groupe.',
      'crop':crop}])
