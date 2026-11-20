from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan025.json').read_text())
r['reader']='/root/reader_c';r['main_reader_reviewed']=True;r['crop_count']=11
r['root_review']={'whole_image':True,'crops_viewed':'All eleven enlarged crops inspected directly, including the complete rotated NB, every sixfold inverse glyph/state position, the straight upper support on (23), all three layers of (24), local Pi cases, four upper wavy traces, both handwritten page numbers, final edge-clipped factor and lower graphic traces. All four listed marks, thirteen unlisted C doubts, thirty-eight source difference rows, inventory and eleven full box readings reviewed. No mathematical repair was made to gauche, the awkward opening, or the unmatched parenthesis.'}
r['notes']=[s.replace('Root is comparing both algebraic conventions independently; this reader performed no mathematical verification and does not use either convention to decide the strokes.','The first reader performed no mathematical verification; the root checks below compare both conventions without using them to decide the strokes.') for s in r['notes']]
a=json.loads((E/'scripts/root_additions_024_025.json').read_text())['25']
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan025_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan025.tex').write_text((E/'reader_reports/145_scan025.tex').read_text())
