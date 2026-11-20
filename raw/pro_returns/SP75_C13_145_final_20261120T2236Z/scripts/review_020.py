from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan020.json').read_text())
r['reader']='/root/reader_b';r['main_reader_reviewed']=True;r['crop_count']=23
r['root_review']={'whole_image':True,'crops_viewed':'All twenty-three saved crops inspected. Root adjudicated the entire cancelled marginal product and its newly exposed blank ending, the uncertain live/cancelled exponent, lexical disagreements, prime against inverse, extra closing parenthesis, all punctuation removals, cancelled lower formulas and footer. All substantive loci, four listed and fifteen other C doubt occurrences, inventory and complete second-box readings reviewed.'}
for c in r['changes']:
    if c['id']=='s020-06':c['ink']+=' The recovered terminal edge is crops/145_scan020_23_margin_deleted_relation_uncovered_end.png, original pixels (325, 780, 475, 960).'
    if c['id']=='s020-20':
        c['c_changed']=True
        c['ink']+=' The preferred symbol changes from C’s sigma_i prime to E prime, while the C reading remains an explicit alternative.'
    if c['id']=='s020-10':c['math_consequence']='A cancelled inverse exponent gives the loop word (rho sigma0)^2 verified in the local C2*C3 calculation; a live inverse gives a different word. The ink state remains uncertain, so both are retained.'
for d in r['unlisted_decisions']:
    if d['id']=='U020-01':d['ink']+=' Recovered-edge crop: crops/145_scan020_23_margin_deleted_relation_uncovered_end.png, original pixels (325, 780, 475, 960).'
a=json.loads((E/'scripts/root_additions_020_021.json').read_text())['20']
r['notes'].extend(a['notes']);r.setdefault('check_events',[]).extend(a['check_events'])
(E/'reader_reports/145_scan020_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan020.tex').write_text((E/'reader_reports/145_scan020.tex').read_text())
