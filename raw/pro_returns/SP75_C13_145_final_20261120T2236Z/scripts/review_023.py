from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan023.json').read_text())
r['reader']='/root/reader_a';r['main_reader_reviewed']=True;r['crop_count']=13
r['root_review']={'whole_image':True,'crops_viewed':'All thirteen saved crops inspected directly. Root adjudicated inverse-first lexical uncertainty from the dotted initial and lack of p/q descenders, pondéré, Malgoire, all live and old indices, both insertion scopes, seven local Pi forms, four points, detached rho, graphic NB mark, full diagram and uncertain vertical sign, and footer22. Every listed/unlisted doubt, substantive difference, inventory and full box reading was reviewed.'}
a=json.loads((E/'scripts/root_additions_023.json').read_text())
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan023_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan023.tex').write_text((E/'reader_reports/145_scan023.tex').read_text())
