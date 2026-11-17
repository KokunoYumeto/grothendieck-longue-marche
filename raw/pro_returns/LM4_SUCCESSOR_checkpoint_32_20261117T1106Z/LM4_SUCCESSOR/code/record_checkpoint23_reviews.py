"""Bind completed source-level reads and independent reviews to final bytes."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parents[1]
formal=['sections/b_annular_centralizer.tex',
        'sections/b_whole_annular_regions.tex',
        'sections/b_annular_neck_comparison.tex']
reviews=['work_CE/review_B112_formal23.txt',
         'work_CE/review_annular_source_detector23.txt',
         'work_CE/review_B114_formal23.txt',
         'work_DE/next_marginal_source/review_B112_B113_final23.md',
         'work_DE/next_marginal_source/review_B114_upper_collar23.md',
         'work_DE/next_marginal_source/review_B114_frozen_final23.md']
research=['work_DE/next_marginal_source/annular_neck_reflection_proof23.md',
          'work_DE/next_marginal_source/review_annular_finite_and_fold23.md',
          'work_A/actual_annular_mirror_fold23.md',
          'work_A/annular_regional_edge_centralizer23.md',
          'work_CE/review_regional_edge_centralizer23.txt',
          'work_CE/annular_neck_height_kernel23.txt',
          'work_DE/next_marginal_source/coarse_annular_height_kernel23.md',
          'records/annular_coarse_bundle_root23.md',
          'records/primary_readings23.md']
for p in formal+reviews+research:
    assert (root/p).is_file(),p
for p in reviews:
    assert 'PASS' in (root/p).read_text(),p
digest=lambda p:hashlib.sha256((root/p).read_bytes()).hexdigest()
assert digest(formal[0])==digest('work_A/B112_annular_centralizer.tex')
assert digest(formal[2])==digest('work_A/B114_annular_neck_comparison.tex')
frozen=json.loads((root/'work_DE/next_marginal_source/review_B114_frozen_final23.json').read_text())
assert digest(formal[2]) in json.dumps(frozen)
record={
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS','main_A':'Open','main_B':'Open',
 'formal_scope':{
  'B112':'Root complete proof/source read before and after source-order clarification, plus every final mathematical page. CE and DE complete independent formal reviews and separate actual source/detector reconstructions.',
  'B113':'Root authored and read the complete proof; DE complete independent source review, including cofinal compact separation, actual mirror and selected connected original cover.',
  'B114':'Root complete proof/source and final page reads; CE earlier complete proof plus changed-section review; DE complete corrected-upper-collar review and final frozen-byte reread, including both independent S3 detectors.'},
 'formal_sources':{p:digest(p)for p in formal},
 'independent_reviews':{p:digest(p)for p in reviews},
 'research_sources':{p:digest(p)for p in research},
 'root_exact_computation_reads':[
  'Root independently wrote and executed the complete infinite-graph source triangular verifier, retaining T^2 order and the established E/bar-E commutation.',
  'Root read the complete actual upper-gap word/section comparison, corrected lift and full DE common-K proof.',
  'Root read the complete CE actual9/36 compiler and A actual8/24 compiler, together with their independent comparison reviews.',
  'Root read the complete CE exact contact-intersection producer and genuine trivial output; its weighted Stallings dependency was already independently audited in prior work.'
 ],
 'primary_dependencies':'B112--B114 use the already completely reopened prime-order element theorem and finite-graph goodness proofs recorded in primary_readings22.md. No nonsolvable finite-subgroup equality is assumed. The two new orbit-configuration references are opened hypothesis audits only; no theorem application to the actual surface is claimed.',
 'preserved_corrections':[
  'The first lower-corridor word was valid but selected-lift interpretation was false; the exact old gauge and failed interpretation are retained. Final B114 uses the upper collar and transports the entire K/section/cone marking.',
  'The source triangular proof explicitly defines delta_E and invokes [E,bar E]=1 before changing the T^2 factor order.',
  'The two new bibliography notes were explicitly included for printing; their unescaped path failure and subsequent path-command repair are retained with genuine build outputs.'
 ],
 'scope':'No post-cross-relation centralizer/source injection, all-neck/global comparison or main decision follows. Later research stays separate from the frozen283-statement register.'
}
(root/'records/checkpoint23_root_formal_reviews.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS final B112--B114 source hashes bound to complete root and independent reviews.')
