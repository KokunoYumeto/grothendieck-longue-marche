"""Bind the actual complete source reviews; this does not automate proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
sources={
 'work_DE/B118_boundary_neck_intersection_proposed.tex':'d598740704183781fd28ba22fc2b2d0f956c452d8d51d7bf34a91d5515661064',
 'work_CE/B119_ordinary_filling_fixed_source_proposed.tex':'2f30e70d43c53f160e0be3fbf27779e94862637c202af274988fcc98f2bfe2a2',
 'work_A/B120_intermediate_boundary_amalgam_proposed.tex':'db428943826c777482d482170a008bc476a6a7e9e94bdfcaef9bc483af86b673',
 'work_A/B121_final_neck_retraction_proposed.tex':'4ed4690b9b2133b4048d198df699f05e98447126f27c3bb0ef5a237e99ada985',
 'work_DE/B122_intermediate_completed_centralizer_proposed.tex':'4995c9913626ba5b59f5cac7c41c0bee250f04100a76f8692201215cad64f1b6',
 'work_CE/B123_two_operator_fixed_kernel_proposed.tex':'d806d5fe02c243d9dc1569fc6a81cfe6b2e01bff73cb3ccab1c35462a56fa3ee',
}
for rel,digest in sources.items(): assert sha(rel)==digest,rel
reviews=[
 'work_CE/review_B118_boundary_intersection25.txt',
 'work_A/review_B118_B119_formal25.md',
 'work_DE/next_marginal_source/review_B119_frozen_source25.md',
 'work_CE/review_B120_intermediate_boundary25.txt',
 'work_DE/next_marginal_source/review_B120_full_source25.md',
 'work_DE/next_marginal_source/review_B121_final_source25.md',
 'work_CE/review_B121_final_neck_retraction25.txt',
 'work_A/review_B122_B123_full25.md',
]
for rel in reviews: assert 'PASS' in (root/rel).read_text(),rel
assert sources['work_A/B120_intermediate_boundary_amalgam_proposed.tex'] in (root/'work_CE/review_B120_intermediate_boundary25.txt').read_text()
for n in (122,123):
    key=next(k for k in sources if f'/B{n}_' in k)
    assert sources[key] in (root/'work_A/review_B122_B123_full25.md').read_text()
qa=['work_DE/B118_QA/review.json','work_CE/qa_B119/qa_record25.json',
    'work_A/B120_component_QA.json','work_A/B121_component_QA.json',
    'work_DE/B122_QA/review.json','work_CE/qa_B123/qa_record25.json']
for rel in qa: assert (root/rel).is_file(),rel
producers=['code/check_B119_literal_source25.py','code/check_B119_raw_source25.py',
 'work_CE/code/compile_annular_two_operator25.py','work_CE/code/check_two_operator_filling25.py',
 'work_DE/next_marginal_source/check_final_neck_retraction25.py']
record={'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_COMPLETE_SOURCE_REVIEW','formal_sources':sources,
 'independent_reviews':{p:sha(p) for p in reviews},
 'private_QA_records':{p:sha(p) for p in qa},
 'root_complete_producer_reads':{p:sha(p) for p in producers},
 'root_scope':'Complete proofs of all six sources read, including the amended raw table, full carrier section, final neck retraction, compact fixed-graph argument with added strict-edge characters, and whole two-operator reduction. Three B123 end-equation repairs are syntax-only and preserved. No truncated output was counted as a complete read.',
 'independent_large_table_replay':False,
 'raw_source_check':'records/B119_raw_source25.json passes all six literal words; earlier simplified-table failure retained.',
 'primary_readings':'records/primary_readings25.md','main_A':'Open','main_B':'Open',
 'limits':['Intermediate centralizer equality is not transferred through final squares.',
           'No completed F6 centralizer injection is asserted.',
           'The neck retraction is not claimed equivariant for the selected cone.',
           'All forty node seeds and every signed operator translate are retained.',
           'Both actual family-kernel fixed-source equalities remain Open.']}
(root/'records/checkpoint25_root_formal_reviews.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS six complete root/independent proof reviews bound to frozen source bytes.')
