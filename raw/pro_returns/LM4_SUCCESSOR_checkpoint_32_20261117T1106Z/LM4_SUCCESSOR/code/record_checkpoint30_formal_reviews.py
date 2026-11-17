"""Bind actually completed manual source reads; this does not automate proofs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
specs = [
 ('A.89','work_A/A89_hexagon_Alexander_dyadic_proposed.tex','sections/a_hexagon_alexander_dyadic.tex','2c221934c030cfdc8a8f532db8820e03bd07cf8fcd6645f99f5452443fdd15a4'),
 ('A.90','work_A/A90_remaining_odd_head_criterion_proposed.tex','sections/a_remaining_odd_head_criterion.tex','df09cc937ffff8a26548a20e2c400985be7db48f541f9b37f0c11f7413b21240'),
 ('A.91','work_A/A91_dihedral_covariance_limitation_proposed.tex','sections/a_dihedral_covariance_limitation.tex','4636c94648d2dc3ebb503fee69f55407a80ff72331c659a64c69ffa9fc8101af'),
 ('B.142','work_CE/B142_unrestricted_coarse_nonsplitting_proposed.tex','sections/b_unrestricted_coarse_nonsplitting.tex','23f52a5a0093408d3c370ec606873745dfc83abfc6da5db8f551af8ba73d1651'),
 ('B.143','work_A/B143_virtual_nonsplitting_fixed_restriction_proposed.tex','sections/b_virtual_nonsplitting_fixed_restriction.tex','cc8586dc8dc7313ed067a9fe78cabefd9db60778f39723ba7f030fbea4101cb9'),
 ('B.144','work_CE/B144_one_family_fixed_source_presentation_proposed.tex','sections/b_one_family_fixed_source_presentation.tex','4cb08b5080b1e9b4342ce6abaefc2063ffc722b8ed796cc713cab836b435c75d'),
 ('B.145','work_DE/B145_center_cyclic_normalization_proposed.tex','sections/b_center_cyclic_normalization.tex','62317a2999d8f48f4cef1c61452d031127ed8e109cc55e387b7a558d4a990148'),
 ('B.146','work_DE/B146_cyclic_leaf_carrier_proposed.tex','sections/b_cyclic_leaf_carrier.tex','a31a00c3bb747d287143339b058edfde8a0a2e8da0ad5cbfd327c3ae6eb4483e'),
 ('B.147','work_DE/B147_center_extension_obstruction_proposed.tex','sections/b_center_extension_obstruction.tex','076f533b132275f99f75412f28d6bf5a595d438fe234e33aa7b8243429378610'),
]
copies = []
reviews = {}
by_source = {}
for statement, source, target, digest in specs:
    assert sha(source) == digest, source
    copies.append(dict(statement=statement, source=source, target=target, sha256=digest))
    matches = []
    for folder in ('work_A', 'work_CE', 'work_DE'):
        if folder == Path(source).parts[0]:
            continue
        for p in sorted((root / folder).rglob('review*30*.json')):
            if 'before' in p.name:
                continue
            raw = p.read_text()
            json.loads(raw)
            if digest not in raw:
                continue
            companions = [q for q in (p.with_suffix('.md'),p.with_suffix('.txt')) if q.is_file()]
            assert 'PASS' in raw + '\n'.join(q.read_text() for q in companions), str(p)
            for q in [p] + companions:
                rel = str(q.relative_to(root))
                matches.append(rel)
                reviews[rel] = sha(rel)
    assert matches, 'Missing final-byte independent review: ' + source
    by_source[source] = sorted(set(matches))
record = {
 'recorded_at': datetime.now(timezone.utc).isoformat(),
 'status': 'PASS_COMPLETE_SOURCE_REVIEW',
 'copies': copies,
 'independent_reviews': reviews,
 'independent_reviews_per_source': by_source,
 'root_scope': 'All nine complete formal proofs read. A89/A90/A91 current complete sources read after their notation corrections. B142 complete source plus both exact retained TeX-only diffs read. B143/B144 entire source proofs read. An oversized combined output truncated B145; a subsequent separate entire B145 read and entire B146/B147 reread resolved that boundary. The complete final B145 citation and B146/B147 gathered-display diffs were read. The whole triple-link proof was also independently derived by root in conversation before author preservation. Every prism/averaging sign and arbitrary-lift coefficient convention was checked. No headline-only or truncated-output pass is credited.',
 'substantive_new_interval_work': ['Actual integral/three-cover covariance limitation','Exact zero restriction of first-jet classes to the actual fixed source','Whole all-coset triple-link obstruction to every injective prescribed-center extension'],
 'final_render_policy': 'No private PDF/PNG previews created. One assembled final build and individual QA of every new mathematical page are required separately before capture.',
 'preserved_corrections': ['A89 pro-two u notation and A91 K_x clarification','Both B142 missing quad backslashes and its initial display terminator','B145 exact B138.5/B117 citation for the identical inverse-generated pair','B146/B147 explicit gathered display wraps'],
 'bibliography_entries': 114,
 'main_A': 'Open',
 'main_B': 'Open',
 'limits': [
  'Full-GT dyadic equality does not prove the all-odd-head condition; the nonlinear word remains separate.',
  'Whole-group virtual nonsplitting classes actually restrict to zero on the selected fixed source.',
  'The entire L=H intersection S and its marked fixed-lifting commutation test remain unresolved.',
  'The cyclic carrier is internally proper; its full ambient restriction kernel remains Open.',
  'No injective extension exists for this specified center normalization in the ordinary unfilled group; noninjective extensions exist and no filling collapse is inferred.',
  'The actual icosahedral B75 uniform finite-cover condition remains unresolved.'
 ]
}
p = root / 'records/checkpoint30_root_formal_reviews.json'
assert not p.exists()
p.write_text(json.dumps(record,indent=2)+'\n')
print('PASS nine complete final-byte formal source reviews; both main decisions Open.')
