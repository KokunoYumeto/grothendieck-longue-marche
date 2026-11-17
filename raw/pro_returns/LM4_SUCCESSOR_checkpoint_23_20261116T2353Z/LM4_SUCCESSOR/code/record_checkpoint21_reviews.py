"""Record actual completed full-proof reads and their retained sources."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

root=Path(__file__).resolve().parents[1]
formal=['sections/b_free_swap_quotient.tex']
reviews=['work_A/review_B107_retracted_amalgam21.md',
         'work_DE/next_marginal_source/review_B106_B107_21h.md']
research=['records/free_swap_quotient21.md','records/inner_critical_halfplane21.md',
          'work_CE/shared_five_generator_neck_21h.txt',
          'work_A/canonical_image_section_test_boundary21.md',
          'work_A/annulus_prescribed_lift_disk21.md',
          'work_CE/mixed_neck_marking_limitations_21h.txt',
          'work_CE/subcomplex_product_trees_freeness_21h.txt']
research_reviews=['work_A/review_shared_neck_detector21.md',
 'work_DE/next_marginal_source/review_shared_neck21.md',
 'work_DE/next_marginal_source/review_canonical_image_sections21.md',
 'work_A/review_product_tree_subcomplex_21h.md',
 'work_DE/next_marginal_source/review_product_trees_freeness21.md']
for rel in formal+reviews+research+research_reviews:assert (root/rel).is_file(),rel
for rel in reviews:assert 'PASS' in (root/rel).read_text()
record={
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS','main_A':'Open','main_B':'Open',
 'formal_scope':{
  'B106':'Root complete proof read; DE complete independent proof read and exact replay.',
  'B107':'Root complete proof read; DE complete geometry and completion read; A separate complete retracted-amalgam proof read.',
  'last_source_change':'Only citation spacing after final mathematical review; final source hash is recorded below.'},
 'formal_sources':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in formal},
 'independent_reviews':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in reviews},
 'research_scope':{
  'first_neck':'Root full proof read plus A/DE complete reviews; ordinary detector and discrete one-neck amalgam only.',
  'canonical_image':'Root complete note and DE full review read; actual section-count/fixed-coset/Tate limitation only, no Fox unit.',
  'annular_disk':'Root complete proof read; unrestricted prescribed lifts are possible, actual common support restricts the cover character.',
  'mixed_marking_note':'Root complete note read, including the expressly withdrawn incidence-only vanishing-arc inference. A later repaired strip proof must have its own record.',
  'product_trees':'Root complete note and DE/A reviews read; actual M comparison still missing.'},
 'research_sources':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in research},
 'research_reviews':{rel:hashlib.sha256((root/rel).read_bytes()).hexdigest() for rel in research_reviews},
 'primary_dependency':'HR1985 Theorem B-prime and complete Lemma3 proof reopened/read by root at this use; records/primary_readings21.md.'}
(root/'records/checkpoint21_root_formal_reviews.json').write_text(json.dumps(record,indent=2)+'\n')
addition='''
## Formal completion and subsequent main-problem research

The final formal paper now has 276 statements and 408 pages. B106--B107
passed root and complete independent proof reviews; the retracted-amalgam
completion argument has a separate A review. DE independently checked
26 exact rational identities and all20 collision root candidates using
separate Fraction arithmetic in Q(zeta5), confirming18 distinct values,
nine per region and16 quotient nodes per region. The final source,
review and exact certificate paths are recorded in
records/checkpoint21_root_formal_reviews.json. The final typesetting and
visible page checks are complete in records/checkpoint21_typesetting.txt.
No formal claim of the global fixed-source equality was added.

The actual first-neck comparison is complete as a research proof:
work_CE/shared_five_generator_neck_21h.txt. At q=exp(i*pi/5), a common
five-puncture disk selects exactly the four A points and one branch
point. The ordinary one-family F7 bundle detects its F5 subgroup, with
full induced topology. The filling map is expressly not equivariant;
the proof passes through the ordinary index-two subgroup and takes a
finite-index core. Over simply connected slit inner/outer bases joined
through this one neck, the actual discrete group is an amalgam of the
two bad vertices over that F5. The selected cone centralizer remains
in the opposite bad vertex, where it is not yet computed. Full topology
of the edge alone does not prove profinite amalgam efficiency. Root,
A and DE read the entire proof and passed precisely these assertions.

The unrestricted annular prescribed-lift disk lemma is proved by actual
point-push isotopies. It does not extend the same marking across all
actual necks: exterior-supported tracks have equal winding about0 and1,
whereas interior-supported tracks have zero winding about1. A common
pure class therefore has zero cover character and cannot independently
switch sheets. This is an exact limitation of that support mechanism.
It is not a proof that all alternative common markings fail.

A first mixed-neck inference from physical incidences alone was
explicitly withdrawn by CE: the short local vanishing arc need not
lie in the transported disk. The failed inference and its reason are
retained in work_CE/mixed_neck_marking_limitations_21h.txt. A later
explicit strip-path repair is being independently checked and will
receive a separate late-proof record; the earlier inference is not
silently reused as evidence.

Main A's focused test has a proved limitation. The actual canonical
image already has exactly the three ambient section classes; its
coset space has only the selected fixed point, and the actual reduced
dyadic coset module is Tate-acyclic. Prescribed-class real projectivity,
the three-generator bound, and compact finite-level boundary equations
give the complete argument. Root and DE read it fully. It proves no
vanishing of that module, no canonical Fox unit, and no third-cusp
conjugacy statement. Proof:work_A/canonical_image_section_test_boundary21.md.
Both main full decisions remain Open.
'''
p=root/'records/twenty_first_hour_research_report.md';s=p.read_text()
assert '## Formal completion and subsequent main-problem research' not in s
p.write_text(s+addition)
print('Root and independent complete proof reviews recorded; both main decisions Open.')
