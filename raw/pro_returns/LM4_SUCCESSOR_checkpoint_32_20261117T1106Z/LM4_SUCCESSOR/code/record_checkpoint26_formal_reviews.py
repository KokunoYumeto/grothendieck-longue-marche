"""Bind complete source reviews and genuine evidence; this does not automate proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
sources={
 'work_DE/B124_outer_source_retract_proposed.tex':'6cfc7088de7d71f7b16b433f661e033f324dae2074fb64c0638b26e2f394dc1a',
 'work_A/B125_ordinary_star_single_cross_proposed.tex':'26c0ff6ddcd93fd86438807c8c7d1f88dca46b47d3975e103737b8b3d1bfc4e6',
 'work_A/B126_final_prefix_axes_proposed.tex':'7db9acb55d232f94ebdddca6b2514ab1ffe1fdfd55d547ab263097434c4a5e97',
 'work_CE/B127_family_kernel_schreier_proposed.tex':'21db36f4547f8e47bc95d759f9316b783df7084e07c758a3d50e4bacb918c8a5',
 'work_DE/B128_compact_family_module_proposed.tex':'e55c8b67d24b7501ae606c7c420d413728972fdfede9e7268db162511ed9b7fe',
 'work_CE/B129_compact_nonlifting_proposed.tex':'a95516bb36665e78f8d3455ad527437fc1e5d1be1f5c470ba4c782a34963bc4b',
 'work_CE/B130_actual_source_commutator_proposed.tex':'fdd7c200bc945d5f4dd22ed9adb2e344457335349985222bc7c66ca3272a1f48',
}
for rel,digest in sources.items(): assert sha(rel)==digest,rel
reviews=[
 'work_A/review_B124_B130_formal26.md',
 'work_A/review_B127_B128_B129_formal26.md',
 'work_A/final_byte_binding_B128_B130_26.md',
 'work_CE/review_B125_B126_frozen26.txt',
 'work_DE/next_marginal_source/review_formal_B125_B126_B127_B129_B130_26.md',
]
for rel in reviews: assert 'PASS' in (root/rel).read_text(),rel
all_reviews='\n'.join((root/rel).read_text() for rel in reviews)
for rel,digest in sources.items(): assert digest in all_reviews,rel
qa=[
 'work_DE/formal_components26_DE_QA.json',
 'work_A/B125_component_QA.json',
 'work_A/B126_component_QA.json',
 'work_CE/qa_B127/qa_record26.json',
 'work_CE/qa_B129/qa_record26.json',
 'work_CE/qa_B130/qa_record26.json',
]
qa_text='\n'.join((root/rel).read_text() for rel in qa)
for digest in sources.values(): assert digest in qa_text
producers=[
 'work_DE/next_marginal_source/check_outer_source_retract25.py',
 'work_A/code/check_ordinary_star_cross25.py',
 'work_CE/code/compile_family_kernel_schreier25.py',
 'work_CE/code/check_compact_nonlift_residue3_26.py',
 'work_CE/code/check_actual_source_commutator26.py',
 'work_DE/next_marginal_source/check_actual_source_commutator_independent26.py',
]
for rel in producers: assert (root/rel).is_file(),rel
record={
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_COMPLETE_SOURCE_REVIEW',
 'formal_sources':sources,
 'independent_reviews':{rel:sha(rel) for rel in reviews},
 'private_QA_records':{rel:sha(rel) for rel in qa},
 'root_complete_producer_reads':{rel:sha(rel) for rel in producers},
 'root_scope':'All seven complete formal proofs read in untruncated chunks. B130 includes the entire completed intermediate witness proof. B128 final syntax/reference changes checked. Earlier complete working-note and producer reads remain scoped to their recorded inputs; no truncated read was counted.',
 'independent_raw_source_replay':{
   'producer':producers[-1],
   'output':'work_DE/next_marginal_source/check_actual_source_commutator_independent26.out',
   'checks':18,
   'root_read':'Complete program and genuine stdout/stderr read; independent execution was DE-owned, not newly rerun by root.',
 },
 'large_table_scope':'Complete all40/all80/all32/all12 input and separate all-word proofs; independent replay records are retained. No fresh duplicate large-table execution by root is claimed.',
 'primary_readings':'records/primary_readings26.md',
 'main_A':'Open','main_B':'Open',
 'limits':[
   'Source-map noninjectivity is proved in both categories; the actual fixed-source equalities remain Open.',
   'The actual compact kernel is not identified with the abstract completion of the infinite discrete kernel.',
   'The abelian invariant discrepancy does not construct a fixed element outside the source.',
   'B129 proves nonlinear nonlifting via an actual continuous retract.',
   'B126 axis/malnormality statements are discrete; only the corner intersection is also completed.',
   'The completed intermediate witness is detected through compatible finite vertex targets, without a full Fhat6 embedding.',
 ],
}
(root/'records/checkpoint26_root_formal_reviews.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS seven complete root and independent proof reviews bound to frozen source bytes.')
