from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan021.json').read_text())
r['reader']='/root/reader_a'
r['main_reader_reviewed']=True
r['crop_count']=13
r['root_review']={'whole_image':True,'crops_viewed':'All thirteen saved crops inspected against C/H, including the upper-mark extension crop. Root adjudicated the closed a indices, two capital Pi signs, cancelled first S upper mark, unresolved other S adornments, two four-mark continuations, complete Critique, undotted tau there, punctuation, footer20 and compressed sv|savoir. All substantive loci, four listed marks, two other C doubts, inventory and complete second-box readings reviewed.'}
r['notes'][-1]=r['notes'][-1].replace('No OCR, external research, other-page inspection, mathematical check or TeX compilation was used.','The first reader used no OCR, external research, other-page inspection, mathematical check or TeX compilation. Main-reader mathematical checks are reported separately below.')
a=json.loads((E/'scripts/root_additions_020_021.json').read_text())['21']
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan021_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan021.tex').write_text((E/'reader_reports/145_scan021.tex').read_text())
