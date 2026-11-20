from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan017.json').read_text())
r['reader']='/root/reader_b'
r['main_reader_reviewed']=True
r['crop_count']=25
r['root_review']={'whole_image':True,'crops_viewed':'All twenty-five saved crops inspected against C and H, including the newly opened preceding-line suivant des. The duplicated des is genuine. Accepted the low dot on the fibre map, distinct undotted/dotted sigma lists, insertion attachments, full underline à gauche, and cancelled extra à-like mark. Kept the retraced tuple letter, first fibre index, repeated a-indexed labels, possible prime and question-like mark uncertain. Final report, decisions and TeX reviewed.'}
r['notes']=[n.replace('No external research, OCR, other-page comparison, TeX compilation, proof check, or mathematical computation was used.','The first page reader used no external research, OCR, other-page comparison, TeX compilation, proof check, or mathematical computation.') for n in r['notes']]
a=json.loads((E/'scripts/root_additions_016_018.json').read_text())['17']
r['notes'].extend(a['notes'])
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan017_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan017.tex').write_text((E/'reader_reports/145_scan017.tex').read_text())
