"""Bind actual complete proof reads to the final formal source bytes."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
formal = ['sections/b_neck_comparison.tex',
          'sections/b_middle_neck_obstruction.tex',
          'sections/b_slit_bad_centralizer.tex',
          'sections/b_annular_diagonal_obstruction.tex']
reviews = ['work_A/review_B108_B109_final22.md',
           'work_A/review_profinite_one_neck_retract22.md',
           'work_A/review_B110_final22.md',
           'work_A/review_B111_final22.md',
           'work_CE/review_B110_and_regional_source22.txt',
           'work_CE/review_inner_bad_hnn22.txt',
           'work_DE/next_marginal_source/review_B110_final22.md',
           'work_DE/next_marginal_source/review_B111_final22.md',
           'work_DE/next_marginal_source/review_inner_bad_regional22.md',
           'work_DE/next_marginal_source/review_auxiliary_and_q0_22.md']
research = ['work_A/auxiliary_RAAG_HNN_centralizer22.md',
            'work_CE/inner_bad_regional_presentation_22h.txt',
            'work_CE/paired_regional_retractions_22h.txt',
            'work_DE/next_marginal_source/inner_fixed_source_identification22.md',
            'work_DE/next_marginal_source/one_neck_fixed_source_corollary22.md',
            'work_A/review_q0_and_one_neck22.md',
            'work_A/V4_Heisenberg_pentagon_boundary22.md',
            'records/regional_antipodal_wall22.md']
for rel in formal+reviews+research:
    assert (root/rel).is_file(), rel
for rel in reviews:
    assert 'PASS' in (root/rel).read_text(), rel
digest = lambda rel: hashlib.sha256((root/rel).read_bytes()).hexdigest()
assert digest('sections/b_annular_diagonal_obstruction.tex') == digest('work_CE/B111_q0_diagonal.tex')
record = {
    'recorded_at':datetime.now(timezone.utc).isoformat(),
    'status':'PASS','main_A':'Open','main_B':'Open',
    'formal_scope':{
        'B108':'Root complete proof read; independent A completion review and CE paired-retraction proof.',
        'B109':'Root complete proof read; A and CE complete independent reads of actual geometry and calibrated words.',
        'B110':'Root complete proof read; A,CE,DE complete formal-source reviews, plus independent actual path, deformation, source and algebra certificates.',
        'B111':'Root complete proof read; A and DE independent full proofs and literal conjugacy replays; canonical source copied byte-identically.'},
    'formal_sources':{rel:digest(rel) for rel in formal},
    'independent_reviews':{rel:digest(rel) for rel in reviews},
    'research_sources':{rel:digest(rel) for rel in research},
    'editorial_changes_after_initial_reviews':[
        'B109: three unbreakable filenames changed to path commands; no mathematics changed.',
        'B110: finite HNN title clarified to finitely presented; explicit braid record path added; inverse Nielsen display gathered.',
        'B111: graph group notation unified as Gamma and completed nontriviality expressed via RF of base and proper topology.'
    ],
    'primary_dependencies':'Root reopened/read BZ Theorem4.3 prime-order element proof, Lemmas4.4 and2.2; Lorensen Theorem3.15 and complete HNN dependencies3.10--3.14. See primary_readings22.md.',
    'computation_reads':'Root read the full normalized/HNN producers, geometric proof and deformation certificate, actual source producer, literal q0 witness producer and independent A witness checker; genuine outputs retained.',
    'main_A_attempt_scope':'Root read complete V4--Heisenberg note, producer and final genuine output. This bounded family fails to couple the coefficient and was stopped; no new formal row or full GT counterexample.',
    'late_annular_scope':'Subsequent q0-adapted basis research is separate; no annular centralizer decision is included in B110 or B111.'
}
(root/'records/checkpoint22_root_formal_reviews.json').write_text(json.dumps(record,indent=2)+'\n')
print('Final B108--B111 sources bound to complete root and independent reviews; both main decisions Open.')
