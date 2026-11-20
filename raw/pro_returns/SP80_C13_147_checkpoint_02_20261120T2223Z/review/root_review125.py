from pathlib import Path
import json,re
R=Path('edition')
p=R/'reports/147_scan125_report.json'; d=json.loads(p.read_text())
d['rows'][0]['math_consequential']=False
d['rows'][2]['math_consequential']=False
mapping={'S125-01':3,'S125-02':5,'S125-03':10,'S125-04':11}
covered=set()
for e in d['check_events']:
 i=mapping[e['statement_id']]; covered.add(i);e['statement_id']+=f'; N125-{i:02d}'
for i,n in enumerate(d['notes'],1):
 if i not in covered:
  d['check_events'].append({'statement_id':f'N125-{i:02d}','type':'used and rechecked in this run','outcome':'Root checked this descriptive/process note against the page crops, proposed TeX, inventory and reported reading scope; it is not an additional mathematical proof.'})
(R/'review/147_scan125_reviewed.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
with (R/'review/root_visual_readings.md').open('a') as f:
 f.write('\n## Scan125 final root review\n\nAll8 listed first crops visually inspected. Agreed literal a donnée, unaccented def labels, two live interlinear insertions, cancelled paragraph and separate uncertain formula, all7 recorded local doubts. 198 horizontal symbol is one wave over one bar. Right definition belongs to underbraced P factor, not whole contracted product. 197 label-side placement and the alternative rendering of the visually same simeq relation are not counted as mathematical corrections. 199 and pencil124 read as recorded. All fixed-box readings checked against proposed TeX.\n')
with (R/'review/mathematical_checks.md').open('a') as f:
 f.write('\n## MC125-R — conditional associativity of extension of structure group\n\nFor homomorphisms φ:G→H and ψ:H→K, take a right G-torsor P and the quotient relation (pg,h)∼(p,φ(g)h). The map [[p,h],k]↦[p,ψ(h)k] is invariant under the first relation because [pg,ψ(h)k]=[p,ψφ(g)ψ(h)k], and under the second because ψ(hh₀)k=ψ(h)ψ(h₀)k. The inverse is [p,k]↦[[p,1],k]: the G relation is respected by moving φ(g) across the second contracted product. The two composites are identities, using [[p,h],k]=[[p,1],ψ(h)k]. This proves only the stated formal associativity conditional on the group actions and quotients. It does not certify the manuscript index pairings, base spaces or the crowded product sign in198. Root independently checked these relations; linked to S125-03/N125-10.\n')
