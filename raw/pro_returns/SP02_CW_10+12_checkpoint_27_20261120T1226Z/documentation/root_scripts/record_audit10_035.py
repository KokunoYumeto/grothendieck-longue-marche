from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from record_audit import build_revision
key='B10-01_10_scan035';out=Path('SP02_CW_10+12')
s=json.loads((out/f'documentation/audit_sessions/{key}_audit001.json').read_text());r=json.loads((out/f'documentation/page_records/{key}.json').read_text())
p=dict(audit_id=s['audit_id'],baseline_page_sha256=s['baseline_page_sha256'],audit_reading_complete=True,audit_inventory_confirmed=True)
p['inventory_patches']={'10.5-correction':{'hand':'another unnamed hand'},'cancelled-v':{'first_words_or_objects':r'\unsure{i)|v)} être un monomorphisme central'}}
p['inventory_extra']=[dict(scan='10:035',sheet_kind='typescript',hand='another unnamed hand',element='audit-archive',kind='margin note',position='bottom left below T',first_words_or_objects='archive folio34 retained in comment',transcribed='yes')]
p['crops_upsert']=json.loads(Path('work/audit10_035_crops.json').read_text())
p['observations']='Root ordered second reading from the whole and both supplied halves before the image-first receipt and text-open event. All16 fresh audit crops were personally viewed, including every doubtful locus, cancelled and replaced text, the boxed clause and leader, the products and inequalities, the topology symbol and archival34. Every word, accent, punctuation mark, mathematical letter/index/prime, underline and editorial state was compared with the consolidated text. The apparent lack of a circumflex in handwritten même was only a full-page impression: the close crop shows the two oblique accent strokes intersecting the rule above, so même is retained. Cancelled fermé has visible final accented e; the typed p beneath d before du lemme is confirmed. All five existing uncertainties remain: the first list label, final cancelled P, old capital/index in10.5 and overprinted second letter in situation. No textual change is justified. Top3 remains manuscript numbering; bottom34 remains an archival comment and is added to the inventory. The inventory label for the first cancelled item is brought into agreement with its explicit i)|v) doubt. No context or mathematical proof check was used.'
Path('work/audit10_035.json').write_text(json.dumps(p,ensure_ascii=False,indent=2));_,t=build_revision(p,s,r,(out/f'pages/{key}.tex').read_text());Path('work/audited10_035.tex').write_text(t)
