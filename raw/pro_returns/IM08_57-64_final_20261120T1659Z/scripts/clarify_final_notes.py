#!/usr/bin/env python3
"""Make written readings explicit in notes using already reviewed evidence."""
from pathlib import Path
import importlib.util
import json

BASE = Path(__file__).resolve().parents[1]
PREFIXES = {
    ('58_scan003', 'L666'): "Written: the hypothesis gives the components of X' dimension at least 2, and the conclusion gives the components of Y' dimension at least 1 and says Y' is connected; it does not state that X' is connected in dimension at least 1. ",
    ('58_scan041', 'L662'): "Written: the invertible-module functor is « pl. fidèle » in (i), and « une équiv. de catégories » in (ii). ",
    ('58_scan067', 'L663'): "Written: Pic(X) → Pic(C_X) is marked as an isomorphism with a question mark. ",
    ('62_scan019', 'L1328'): r"Written: -27c^{\unsure{2}}/(b^3-27c^2)=j, then the unboxed b^3/c^2=j and boxed b^3/c^2=27(j-1)/j. ",
    ('62_scan019', 'L1555'): r"The written ratios are b^3/c^2=j and b^3/c^2=27(j-1)/j; the lower pair is b^{\deleted{\unsure{3}}}=27(j-1)/j and c=27(j-1)/j. ",
    ('62_scan019', 'L1556'): r"Written locally: -27c^{\unsure{2}}/(b^3-27c^2)=j, with boxed b^3/c^2=27(j-1)/j; no capital J or 1728 is written there. ",
    ('63_scan030', 'L1327'): "Written: if c_4 and c_6 are invertible, the only automorphisms of E are the identity and the symmetry, with no connectedness hypothesis on S in the proposition. ",
    ('64_scan050', 'L810'): "Written: the intersection of the stabilizers of infinity and -1 is {1}; the octahedral structure is uniquely determined by the divisor Delta, with Gamma contained in Aut_oct(Delta). ",
    ('64_scan103', 'L813'): "Written: multiplication by delta, a canonical-isomorphism arrow, and Ker Theta_delta = F_1 = k.1_E. ",
    ('64_scan105', 'L814'): r"Written: \wp'=\Theta_\delta(\wp) and \varepsilon_3(\wp')=\delta^{\otimes3}. ",
}
SUFFIXES = {
    ('64_scan050', 'L810'): " The supplied refinement states Delta=P^1(F_5) and Aut(X,Delta)=PGL_2(F_5)=S_5 in characteristic 5; a)↔b) holds away from characteristic 2, while c)↔b) requires the opposition to be part of the data. These additional statements are recorded from the supplied row only.",
    ('64_scan105', 'L814'): " For completeness, the supplied alternative retaining p'=Theta_delta p also gives p'^2=4(p^3+a_1 p^2+a_2 p+a_3) and Theta P'=2(3P^2+2a_1 P+a_2), alongside epsilon_3(p')=-2 delta^3. Those later formulas are supplied refinements, not readings verified on this page.",
}

for (page, statement_id), prefix in PREFIXES.items():
    for folder in ('reviews', 'accepted_reviews'):
        path = BASE / folder / f'{page}.json'
        review = json.loads(path.read_text())
        row = next(r for r in review['rows'] if r['id'] == statement_id)
        if not row['note'].startswith(prefix):
            row['note'] = prefix + row['note'] + SUFFIXES.get((page, statement_id), '')
        path.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n')

spec = importlib.util.spec_from_file_location('commit_review', BASE/'scripts/commit_review.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.refresh_tables()
print('Clarified 10 notes from existing reviewed readings; page bytes and decisions unchanged.')
