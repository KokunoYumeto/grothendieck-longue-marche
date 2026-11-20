from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan026.json').read_text())
r['reader']='/root/reader_a';r['main_reader_reviewed']=True;r['crop_count']=8
r['root_review']={'whole_image':True,'crops_viewed':'All eight single saved crops inspected directly: parameter trials and point subscript, operation-group adornments, crossed words and readable bien sûr, quotes, complete covariance and its plus/index/bar, both initial crossed clusters, entire rotated NB and overlap, and footer25. The short horizontal right bar is distinguished from the wavy left tilde by the same crop. No absent rho factor, marginal parenthesis or second copy of the parameter row is supplied. All25 corrected difference rows, M0867, six unlisted C marks, inventory and eight whole audit boxes checked.'}
for c in r['changes']:
    if c['id'] in ['s026-08','s026-12']:
        c['confidence']='low'
        c['math_consequence']=''
a=json.loads((E/'scripts/root_additions_026_027.json').read_text())['26']
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan026_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan026.tex').write_text((E/'reader_reports/145_scan026.tex').read_text())
