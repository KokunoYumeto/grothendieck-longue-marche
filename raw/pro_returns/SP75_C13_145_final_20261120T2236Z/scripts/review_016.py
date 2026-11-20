from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan016.json').read_text())
r['reader']='/root/reader_c'
r['main_reader_reviewed']=True
r['crop_count']=20
r['root_review']={'whole_image':True,'crops_viewed':'All twenty saved crops inspected against both witnesses. Accepted local capital Pi forms, plural endings, the live On and struck pourra, dotted geometric symbols, cancelled resp.|sur with a definite stop, the struck upper extension label, semicolon before via, and Gamma under the final brace. Kept crossed words and overwritten indices uncertain where their individual letters remain obscured. Removed the unsupported margin-final period. Checked the final TeX and report.'}
a=json.loads((E/'scripts/root_additions_016_018.json').read_text())['16']
r['notes'].extend(a['notes'])
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan016_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan016.tex').write_text((E/'reader_reports/145_scan016.tex').read_text())
