from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan024.json').read_text())
r['reader']='/root/reader_b';r['main_reader_reviewed']=True;r['crop_count']=12
r['root_review']={'whole_image':True,'crops_viewed':'All twelve saved crops inspected directly, including the full rotated NB, both intersection formulas, entire (21)/(22), the word pour, inserted pour être, map letter, all three local Pi signs, underline and footer. Root confirmed the separated tau dot, doubled-left Gamma, continuous-bottom cup, preferred k with kappa alternative, absence of two stops, and four explicit exponent glyph/state uncertainties. All9 listed and5 unlisted marks, all35 corrected target differences, inventory and full box readings reviewed.'}
for c in r['changes']:
    if c['id']=='s024-01':
        c['C']=r'\unsure{qui contient|qui centralise}'
        c['H']=r'\ill{} \ill{}'
        c['final']=r'\unsure{qui contient}'
    if c['id']=='s024-11':c['C']='des élts de'
    if c['id'] in ['s024-07','s024-17','s024-18']:c['marked_in_H']='no'
a=json.loads((E/'scripts/root_additions_024_025.json').read_text())['24']
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan024_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan024.tex').write_text((E/'reader_reports/145_scan024.tex').read_text())
