from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan014.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=13
r['root_review']={'whole_image':True,'crops_viewed':'All thirteen saved crops inspected. Accepted Ce qui redonne, On retrouve, unstruck vertical connector, the marginal negative statement and consequences word, omitted end punctuation in upper displays, the colon after the cyclic rho display, and manuscript13. Kept struck words, the obscured final epsilon index, cancelled exponent and final abbreviation uncertain.'}
a=json.loads((E/'scripts/root_additions_013_015.json').read_text())['14']
r['notes']=[n.replace('No mathematical verification was performed.','The first page reader performed no mathematical verification; separate main-reader checks are recorded below.').replace('No mathematical check was performed.','The first page reader performed no mathematical check; separate main-reader checks are recorded below.') for n in r['notes']]
r['notes']=[n.replace('These are the author’s written formulas; no independent mathematical verification is claimed.','These are the author’s written formulas. The first reader made no mathematical check; the main reader’s later local checks are recorded below.') for n in r['notes']]
r['notes'].extend(a['notes'])
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan014_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan014.tex').write_text((E/'reader_reports/145_scan014.tex').read_text())
