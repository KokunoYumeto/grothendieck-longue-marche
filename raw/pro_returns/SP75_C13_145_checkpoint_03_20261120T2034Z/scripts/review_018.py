from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan018.json').read_text())
r['reader']='/root/reader_a'
r['main_reader_reviewed']=True
r['crop_count']=16
r['root_review']={'whole_image':True,'crops_viewed':'All sixteen saved crops inspected against C/H. Reused existing crops to adjudicate the margin attachment and separator, the boundary of the long cancellation, the live il faudra/product tail, both underlines beginning with pas, five upper and four lower short strokes around la relation, dotted indices, dis, C’est faux comma and absence of a terminal stop. No second first-pass crop was made. Final TeX, all substantive loci, indexed decisions and box coverage reviewed.'}
a=json.loads((E/'scripts/root_additions_016_018.json').read_text())['18']
r['notes'].extend(a['notes'])
r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan018_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan018.tex').write_text((E/'reader_reports/145_scan018.tex').read_text())
