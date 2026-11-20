from pathlib import Path
import json

E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan012.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=17
for c in r['changes']:
    if c['id']=='s012-01': c['marked_in_H']='yes'
    if c['id']=='s012-09': c['C']=c['C'].replace("l\\'extension", "l'extension")
r['notes']=[n.replace('No mathematical verification was performed.','The first page reader performed no mathematical verification; separate main-reader checks are recorded below.') for n in r['notes']]
r['root_review']={
    'whole_image':True,
    'crops_viewed':'All seventeen saved crops directly inspected.',
    'decisions':'Accepted le donnée, the g-shaped but still locally ambiguous factor in the cancelled relation, uppercase L subgroups, des, sous- attached between article and extension, Aut_lac, inverse exponent −1, groupes de ramification, canoniq[t] isomorphes and comma, inserted autom., la classe mod pi des sigma_i, cancelled et, and handwritten 11. Kept the blackened index, nested cancellations, overwritten par/près, article correction state, S alphabet and edge-clipped final phrase uncertain.'
}
r['notes'].append('Main-reader inspection of the cancelled fundamental relation finds a right-sided head and hooked descending tail after u, closer to the local g than to the following rho, whose stem descends on the left. The diplomatic reading therefore puts g first while retaining rho as an alternative. The earlier uρ=int(g)ρu supplies the mathematical expectation; it does not authorize replacing the visible g-like form. The nonstandard le donnée is plainly written and is preserved.')
r['notes'].append('Main-reader local algebra check of the two adjacent product formulas: σ₀σ₁=l₁⁻¹ρ gives ρ=l₁σ₀σ₁ by multiplication on the left. The following written ρ=σ₀σ₁l₁ would require l₁ to commute with σ₀σ₁. Thus the stated i.e. is not a valid noncommutative rearrangement without an additional commutation condition. Both written product orders are retained, and this note records only the necessary algebraic qualification.')
r.setdefault('check_events',[]).append({'statement_id':'145-012-noncommutative-rearrangement','type':'targeted proof check','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'Multiplied σ₀σ₁=l₁⁻¹ρ on the left by l₁. Derived ρ=l₁σ₀σ₁ and identified the additional commutation condition needed for the written right-multiplied version. No source order was silently corrected.'})
(E/'reader_reports/145_scan012_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan012.tex').write_text((E/'reader_reports/145_scan012.tex').read_text())
