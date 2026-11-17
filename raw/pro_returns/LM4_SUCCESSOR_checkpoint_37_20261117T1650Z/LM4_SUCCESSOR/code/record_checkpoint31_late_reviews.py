"""Bind eight actually completed root proof reads and their independent reviews."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
sources = {
 'work_A/specified_center_free_head_boundary31.md':'4d9bd3f5d481bf4be29c2922ebd5368daeb42be660ea21b678bcfc5acd42cdb5',
 'work_A/actual_sphere_kernel_relative_two31.md':'7c65bf9ca0f3c3fab932675929dcec945c0f8b039ed1e5e840e8137b0b0d76b9',
 'work_A/actual_sphere_canonical_reflection31.md':'0fa8e8e72456db4995a545794f85dac1d98f2003553f870b39a020ec727a2e33',
 'work_A/actual_sphere_cabling_correction31.md':'bd9f4b7866e8e737b1ad5dcb563cd4bf97523cec4eaadd7e716ded6b884ca3dd',
 'work_A/actual_sphere_regular_cusp_bridge31.md':'7d4be641553b64fd966da8d495c41d83b70b69dab08f96247d1d9280a99cbb2d',
 'work_CE/one_fixed_coset_relative_kernel31.txt':'f881da8bdb1b131af2620d3a07c4086039a66922c91dc857679c7ded81fd8a99',
 'work_CE/remaining_kernel_family_basis31.txt':'5a1951870545dbc6cd96490353da9ad769ce53ea0aac89e7c942c8ce5faf2362',
 'work_DE/next_marginal_source/B75_recursive_cover_detector_boundary31.md':'9fb690c33df59c67cf344413572b1c59b4706a51f25f93877472a4d3e3a0ac1e',
}
reviews = [
 'work_CE/review_specified_center_free_head31.txt',
 'work_CE/review_specified_center_free_head31.json',
 'work_CE/review_actual_sphere_kernel_reflection31.txt',
 'work_CE/review_actual_sphere_kernel_reflection31.json',
 'work_DE/next_marginal_source/review_actual_sphere_kernel_and_reflection31.md',
 'work_DE/next_marginal_source/review_actual_sphere_kernel_and_reflection31.json',
 'work_CE/review_actual_sphere_cabling_correction31.txt',
 'work_CE/review_actual_sphere_cabling_correction31.json',
 'work_CE/review_actual_sphere_regular_cusp_bridge31.txt',
 'work_CE/review_actual_sphere_regular_cusp_bridge31.json',
 'work_A/review_one_fixed_coset_relative_kernel31.md',
 'work_A/review_one_fixed_coset_relative_kernel31.json',
 'work_DE/next_marginal_source/review_one_fixed_coset_relative_kernel31.md',
 'work_DE/next_marginal_source/review_one_fixed_coset_relative_kernel31.json',
 'work_DE/next_marginal_source/review_remaining_kernel_family_basis31.md',
 'work_DE/next_marginal_source/review_remaining_kernel_family_basis31.json',
 'work_A/review_B75_recursive_cover_boundary31.md',
 'work_A/review_B75_recursive_cover_boundary31.json',
]
for rel, digest in sources.items():
    assert sha(rel) == digest, rel
    assert any(digest in (root / review).read_text() for review in reviews), rel
record = {
 'recorded_at': datetime.now(timezone.utc).isoformat(),
 'status':'PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES',
 'formal_statement_count':333, 'formal_promotion':False,
 'proof_sources':sources,
 'independent_reviews':{rel:sha(rel) for rel in reviews},
 'root_entire_current_proof_reads':list(sources),
 'root_review_scope':'Every complete final proof listed above, and every listed independent review, was actually read in untruncated bounded outputs. In the cabling proof root read the final compact-abelianization notation edition. All complete arguments passed at their stated categories and scopes. New notes do not increase the formal register.',
 'main_A':'Open', 'main_B':'Open',
 'proved_late_scopes':[
  'Every invariant-free abelian lift over the specified center-free sphere head factors through that same literal free-two quotient; no arbitrary head classification.',
  'Exact N=F(P,A,C) kernel after removing only the central full twist; actual embedded N^(2) in the specified relative quotients, with primitive P retained.',
  'Actual full-GT preservation of N; unique normalized h0; beta=Inn(h0)alpha involutive with the literal B section invariant and the same original correction on both base generators.',
  'Original cabling gives gamma genuinely conjugate to alpha, the literal canonical free-factor copy, h0=t p, and h0_ab=-A; the negative normalization is a different section class even in the actual relative pro-two quotients.',
  'The exact regular-cusp bridge h_reg=S^-1 t A varphi^-1 S u and its full norm substitution retain every basepoint factor; abelianization gives no odd coefficient identity.',
  'Unique fixed coset, one ordinary cone factor, paired free pre-node fiber, and the entire actual node/source/deck relation scheme; compact statements use ambient closures only.',
  'An ordinary free-product basis retains every deleted core at every right coset; retained a/a-star cores are outside Q and their nodal connectors cannot be discarded.',
  'All recursive degree-five-cover permutation heads have prime divisors only2 and5 and cannot refine the explicit index3 source quotient; unrestricted characteristic Birman targets remain possible.'
 ],
 'remaining_gates':[
  'The actual all-odd-head equality a_reg=d_alpha, and the full nonlinear Omega_alpha=1.',
  'The full source-based associativity scope of any new canonical-u pentagon calculation; duality or fixed arrows alone do not establish it.',
  'Fixed generation after the complete nodal filling, including all nonlinear connectors and translates.',
  'Other necks, the full-base transfer, and the original B75 uniform finite-neighborhood condition for the actual icosahedral kernel.',
  'No full fixed-element lifting, abstract infinite-kernel completion, or arbitrary finite-subgroup centralizer theorem is inferred.'
 ],
 'primary_dependency_resolution':{
  rel:sha(rel) for rel in [
   'work_CE/compact_stabilizer_dependency_resolution31.txt',
   'work_DE/next_marginal_source/Boggi_S04_primary_marking_audit31.md',
   'work_DE/next_marginal_source/McReynolds_published_passage_audit31.md',
   'records/primary_readings31.md']},
 'execution_scope':'The late mathematics is by complete symbolic, inverse-presentation and topology proofs; no broad census, private build, or producer rerun is claimed.'
}
out = root / 'records/checkpoint31_root_late_reviews.json'
assert not out.exists()
out.write_text(json.dumps(record, indent=2)+'\n')
print('PASS:8 entire final late proofs,18 bound independent reviews;333 formal statements unchanged;both mains Open.')
