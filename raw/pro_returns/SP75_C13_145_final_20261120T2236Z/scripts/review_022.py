from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan022.json').read_text())
r['reader']='/root/reader_c';r['main_reader_reviewed']=True;r['crop_count']=10
r['root_review']={'whole_image':True,'crops_viewed':'All ten saved crops inspected, including the complete product system, complete negative question, both marginal structures, every lexical difference and all arrows/dots/punctuation. Root adjudicated the 4 exponents, uncertain second-row index and cancelled rho heads, graphic reproduction rather than forced punctuation, plain arrow in12, absent three stops and footer. Four listed and two other C doubts, inventory and complete second readings reviewed.'}
for c in r['changes']:
    if c['id']=='s022-08':c['math_consequence']='The literal que non conflicts with the first surviving product, which solves for rho as a word in the epsilons. Both are preserved; the algebraic rearrangement is given in the notes and check events.'
a=json.loads((E/'scripts/root_additions_022.json').read_text())
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan022_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan022.tex').write_text((E/'reader_reports/145_scan022.tex').read_text())
