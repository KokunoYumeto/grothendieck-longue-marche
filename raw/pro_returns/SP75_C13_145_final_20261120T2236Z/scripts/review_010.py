from pathlib import Path
import json

E=Path(__file__).resolve().parents[1]
r=json.loads((E/'reader_reports/145_scan010.json').read_text())
r['main_reader_reviewed']=True
r['crop_count']=14
r['root_review']={
    'whole_image':True,
    'crops_viewed':'All fourteen saved crops directly inspected by the main reader.',
    'decisions':'Accepted ou encore, lowercase marginal il, passant and abélien, beta=gamma and q=-r, the omission of the spurious marginal , que, Condition and Si, dépendent, de son représentant, travaille sur les, the two local autom ext. forms, inserted donc p=±1 et, and footer 9. Kept the cancelled choix de u uncertain. The apparent cancelled material inside the first marginal equation is a descender from forme on the neighbouring line.'
}
r['notes'].append('Main-reader local check of the marginal rewriting: put a=l₀, b=l₁ and s=σ∞, so s interchanges a and b. The displayed g b^q s(g)=a^r implies s(g)⁻¹=a^−r g b^q. In the abelianization write g=(A,B); the equation gives A+B=r and A+B+q=0, hence q=−r. Thus the marginal beta and gamma equal −r and q respectively, explaining the written β=γ. This algebraic check does not replace the direct reading of the signs.')
r['notes'].append('Main-reader local check of representative invariance: if g′=a^α g b^−α, then s(g′)=b^α s(g)a^−α, and g′b^q s(g′)=a^α g b^q s(g)a^−α=a^α a^r a^−α=a^r. The same q and r therefore remain valid after the replacement shown. The discrete-group classification stated at the foot of the page was not independently proved here.')
r['notes'].append('The clearly written star in q,r∈Ẑ* is retained. Taken literally, requiring both exponents to be units excludes g=1 with q=r=0, even though the following discrete discussion includes the identity. This is a tension in the stated condition, not a license to remove the star.')
r['check_events']=[
    {'statement_id':'145-010-marginal-rewriting-and-abelianization','type':'targeted proof check','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'Rearranged g b^q s(g)=a^r and computed its two abelianized coordinates. Obtained beta=−r, gamma=q and q=−r, hence beta=gamma.'},
    {'statement_id':'145-010-representative-invariance','type':'targeted proof check','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'Substituted g′=a^alpha g b^−alpha and s(g′)=b^alpha s(g)a^−alpha, cancelled adjacent powers, and recovered a^r with unchanged q and r.'},
    {'statement_id':'145-010-unit-exponents-identity-tension','type':'targeted proof check','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader, cote 145 second pass','outcome':'For g=1 the abelianized coordinates force q=r=0. These exponents are not units; noted the tension with the literal starred condition and the later inclusion of the identity, retaining all source ink.'}
]
(E/'reader_reports/145_scan010_reviewed.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
(E/'pages/145_scan010.tex').write_text((E/'reader_reports/145_scan010.tex').read_text())
