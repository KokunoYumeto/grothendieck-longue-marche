from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan013.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=18
r['root_review']={'whole_image':True,'crops_viewed':'All eighteen saved crops inspected. Accepted the missing opening parenthesis, barred-m abbreviation, two inverse exponents in the rejected trial, live equals/lower annotation beside the cancellation, and separate cancellation states. Retained doubts in blackened indices, the bracket scope, edge-clipped words, punctuation and overwritten marginal numeral.'}
a=json.loads((E/'scripts/root_additions_013_015.json').read_text())['13']
r['notes']=[n.replace('No mathematical verification was performed.','The first page reader performed no mathematical verification; separate main-reader checks are recorded below.').replace('No mathematical check was performed.','The first page reader performed no mathematical check; separate main-reader checks are recorded below.') for n in r['notes']]
r['notes'].extend(a['notes'])
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan013_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan013.tex').write_text((E/'reader_reports/145_scan013.tex').read_text())
