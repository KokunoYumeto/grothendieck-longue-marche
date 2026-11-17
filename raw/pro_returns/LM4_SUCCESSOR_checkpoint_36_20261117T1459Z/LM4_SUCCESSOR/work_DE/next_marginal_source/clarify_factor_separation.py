"""Clarify a metadata label from the first genuine reconstruction run.

The root-separation estimate is within each individual difference
factorization, not between all nearby roots of different pair polynomials.
No polynomial, interval, braid word, or numerical bound is changed.
"""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
for name in ['positive_marginal_geometry.json','positive_marginal_braids.partial.json',
             'positive_marginal_braids.json','positive_marginal_words.json']:
    p=HERE/name;d=json.loads(p.read_text());g=d.get('geometry',d)
    if 'critical_separation_bound' in g:
        v=g.pop('critical_separation_bound')
        assert v=='1/10'
        g['within_each_factorization_root_separation_bound']=v
        p.write_text(json.dumps(d,indent=2 if name.endswith('geometry.json') or name.endswith('words.json') else None,
                                separators=None if name.endswith('geometry.json') or name.endswith('words.json') else (',',':'))+'\n')
        print(name+': metadata clarified; exact data unchanged')
    else:
        assert g['within_each_factorization_root_separation_bound']=='1/10'
        print(name+': already precise')
