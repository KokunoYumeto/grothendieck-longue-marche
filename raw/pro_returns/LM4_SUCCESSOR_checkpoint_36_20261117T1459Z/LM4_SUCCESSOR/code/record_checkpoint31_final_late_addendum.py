"""Preserve the eight-proof record and add two complete final late reviews."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
late_path = root / 'records/checkpoint31_root_late_reviews.json'
late = json.loads(late_path.read_text())
assert len(late['proof_sources']) == 8
saved = root / 'records/checkpoint31_root_late_reviews_before_coefficient.json'
assert not saved.exists()
shutil.copy2(late_path, saved)
new = {
 'work_A/actual_two_dimensional_pentagon_coefficient31.md':'f3c084c0d9c69cb5c5cf35c1cfe5a7b8274894df0688baaa92d1913d02492124',
 'work_DE/next_marginal_source/B75_solvable_source_heads_affine_gate31.md':'1e6a971fd4263f23089551a4792ca3fef2ef192b0a729cf3735a719ab0bb0d17',
}
reviews = [
 'work_CE/review_two_dimensional_pentagon_coefficient31.txt',
 'work_CE/review_two_dimensional_pentagon_coefficient31.json',
 'work_DE/next_marginal_source/review_actual_two_dimensional_pentagon31.md',
 'work_DE/next_marginal_source/review_actual_two_dimensional_pentagon31.json',
 'work_A/review_B75_solvable_affine_boundary31.md',
 'work_A/review_B75_solvable_affine_boundary31.json',
]
for rel,digest in new.items():
    assert sha(rel) == digest
    assert any(digest in (root/p).read_text() for p in reviews)
late['proof_sources'].update(new)
late['independent_reviews'].update({p:sha(p) for p in reviews})
late['root_entire_current_proof_reads'].extend(new)
late['final_addendum_at'] = datetime.now(timezone.utc).isoformat()
late['root_review_scope'] += ' Root then read both complete new sources and all six exact independent review files. For the coefficient proof root also reopened the entire A36/A37 proofs and the complete A88/A89 sources, checked all six new source relations and all five full-word evaluations, and verified the original coefficient normalization. CE and DE independently checked the entire new coefficient proof. The initial eight-proof record remains preserved.'
late['proved_late_scopes'].extend([
 'For actual full-GT involutions, a_reg=d_alpha in the full profinite integers: the genuine two-dimensional marked P4 quotients prove every odd component, and existing A89 proves the dyadic component. The full abelianization of Omega is zero.',
 'Solvable finite SOURCE heads cannot refine the actual A5 source quotient; an elementary abelian Birman quotient may still have nonsolvable affine source image. The exact identity-point stabilizer and the limited regular-module detector obstruction retain that distinction.'
])
late['remaining_gates'][0] = 'The full nonlinear Omega_alpha=1/cubic relation, and the coefficient comparison without the full-GT hypothesis. The full-GT coefficient equality is now Proved by the final added source.'
late['remaining_gates'][1] = 'The canonical-u pentagon used here is established by A37 only for actual full-GT involutions, including its trivial fixed-discrepancy input. No four-strand conclusion is supplied for arbitrary GT0.'
late['full_GT_coefficient_equality'] = 'PROVED_AFTER_COMPLETE_ROOT_CE_AND_DE_REVIEW'
assert len(late['proof_sources']) == 10 and len(late['independent_reviews']) == 24
late_path.write_text(json.dumps(late, indent=2)+'\n')
addition = r'''
## Final late-cycle progress: the full-GT coefficient gate is closed

After the frozen 333-statement PDF was built, we completed and independently reviewed a uniform proof that
\[
                    a_{\rm reg}=d_\alpha
\]
for every actual full-GT involution in the stated negative marking. This is a late research theorem; it does not silently change the formal statement count or the frozen PDF. Its complete proof is `work_A/actual_two_dimensional_pentagon_coefficient31.md`, with full independent CE and DE reviews and a complete root read. Both main decisions remain Open.

The construction retains the actual central-full-twist quotient of the original marked four-strand group. For an arbitrary odd-order root rho in a finite characteristic-two field, the kernel boundary P maps to the nontrivial scalar rho I on a two-dimensional space. Two specified transvections D and F have product with eigenvalues rho and rho inverse. The five prescribed P,A,C,d,f images respect all six complete action relations; the inverse presentation recovers the actual a,b,c,d,e,f tuple. This supplies a genuine family of full source quotients with a nonabelian linear head, beyond the one-dimensional affine boundary of A94.

We evaluate all five factors of the actual canonical-u pentagon. Two are the exact reversed and forward dihedral pairs, carrying the same canonical exponent k. Two give the original Alexander values U(rho) and U(rho inverse). The fifth has an actual unknown scalar Y; we keep it until the two nonzero eigencomponents equate their right sides. The resulting identity is
\[
 \theta(\rho^{-1})=\rho^{2k}\theta(\rho),\qquad
 \theta=1+(T-1)(U+\overline U).
\]
A88's original normalization, theta D_a=1, gives independently bar(theta)=T^(a-1)theta. Its unit property permits cancellation at rho, proving rho^(a-d)=1 with d=2k+1. Every odd order occurs in some finite characteristic-two field, so this proves every odd component. The already established full-GT dyadic equality in A89 completes the full profinite equality.

The pentagon is available for this particular canonical u by A37: the fixed associativity arrow and its five genuine insertions have a fixed discrepancy, and the separately proved trivial fixed subgroup in the completed four-strand pure group makes that discrepancy one. Fixed arrows or swap duality alone would not justify this step. The argument therefore keeps the full-GT hypothesis throughout. The exploratory shifted-theta formula was corrected before the final proof and is explicitly recorded as unused.

The consequence is that the full abelianization of the actual nonlinear cusp defect Omega vanishes. We have not proved Omega itself is one, the missing cubic relation, a general-GT0 coefficient equality, or Main A. The next Main A target is the full remaining group word with all original markings retained.

The preceding five sphere-kernel/cusp notes also now have entire root and independent reviews. They establish the actual free-three kernel, the retained primitive boundary in its relative pro-two quotients, the unique whole correction h0, its exact original cabling formula, and the negative/regular cusp bridge. In particular h0 has abelianization minus A and is not a coboundary in the retained negative section problem. The regular frame comparison cancels that odd coordinate without making the two negative sections interchangeable.

For Main B, two additional complete notes identify the unique fixed coset and an ordinary paired free pre-node fiber, then retain every deleted-family core in an explicit all-coset free-product basis. The entire nodal normal closure, both sheets, all source and deck translates, and all nonlinear connectors remain. Its filled fixed subgroup still requires a generation theorem; the compact statements use actual ambient closures only. The original B75 recursive-cover topology is not cofinal, and the separate solvable-source/affine note clarifies why this does not exclude elementary abelian or p-group Birman quotients with nonsolvable automorphism action.

The final late record binds ten complete proofs and twenty-four independent review files. Its initial eight-proof state is preserved. All 49 task outcomes, both main Open statuses, 333 formal statements, 590 PDF pages and 114 printed references remain unchanged. These late results justify CONTINUE at the scheduled review without treating a coefficient theorem as a main resolution.
'''
backup = root / 'records/checkpoint31_before_late_addendum'
backup.mkdir(exist_ok=False)
for rel in ['records/thirty_first_hour_research_report.md','LM4_SUCCESSOR_report.md']:
    path=root/rel
    dest=backup/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(path,dest)
    path.write_text(path.read_text()+addition)
print('PASS:10 final late proofs,24 exact independent review files; full-GT coefficient equality accepted;333 formal statements and both main Open outcomes retained.')
