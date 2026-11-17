"""Bind completed manual proof reviews; this script does not automate proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
specs=[
 ('B.131','work_A/B131_D_source_noncommutation_proposed.tex','sections/b_d_source_noncommutation.tex','382b343507a134a4e554a0bb77443a7f7b944659d981f6df4fc924f4a41f7865'),
 ('B.132','work_CE/B132_actual_free_source_pair_proposed.tex','sections/b_actual_free_source_pair.tex','7b6ab57274f7a119698015770585cf4bc71bf261acdb2e6a82eefd99057bee8b'),
 ('B.133','work_DE/B133_pre_cross_source_topology_proposed.tex','sections/b_pre_cross_source_topology.tex','481ed4beec7bcac4b44ca11f83c4dccb1e0720c6caf30804e1138cc9bb324a3d'),
 ('B.134','work_DE/B134_two_sheet_edge_matching_proposed.tex','sections/b_two_sheet_edge_matching.tex','988c79c946aba5e947ada543dbde7927a2d2c53ee4024be84dd4a5e74367efc5'),
]
copies=[]
for statement,source,target,digest in specs:
    assert sha(source)==digest
    copies.append(dict(statement=statement,source=source,target=target,sha256=digest))
reviews=[
 'work_CE/review_B131_final_source27.txt','work_CE/review_B131_final_source27.json',
 'work_DE/next_marginal_source/review_B131_B132_final_bytes27.json',
 'work_A/review_B132_formal27.md','work_A/review_B132_formal27.json',
 'work_DE/next_marginal_source/review_B132_proposed_source27.md',
 'work_CE/review_B133_pre_cross_source27.txt','work_CE/review_B133_pre_cross_source27.json',
 'work_A/review_B133_and_edge_regrouping27.md','work_A/review_B133_final_binding27.json',
 'work_A/review_B134_full_source27.md','work_A/review_B134_full_source27.json',
 'work_CE/review_B134_two_sheet_edge_matching27.txt','work_CE/review_B134_two_sheet_edge_matching27.json',
]
qa=['work_A/B131_component_QA.json','work_CE/qa_B132/qa_record27.json',
    'work_DE/B133_component_QA.json','work_DE/B134_component_QA.json']
combined='\n'.join((root/r).read_text() for r in reviews)
qa_text='\n'.join((root/r).read_text() for r in qa)
for row in copies:
    assert row['sha256'] in combined
    assert row['sha256'] in qa_text
producers=['work_DE/next_marginal_source/check_edge_regrouping27.py',
           'work_DE/next_marginal_source/check_two_cross_sheets27.py',
           'work_CE/code/compile_m_star_relative_presentation27.py']
record=dict(
 recorded_at=datetime.now(timezone.utc).isoformat(),status='PASS_COMPLETE_SOURCE_REVIEW',
 copies=copies,formal_sources={r['source']:r['sha256'] for r in copies},
 independent_reviews={r:sha(r) for r in reviews},private_QA_records={r:sha(r) for r in qa},
 root_complete_producer_reads={r:sha(r) for r in producers},
 primary_readings='records/primary_readings27.md',
 root_scope='All four complete formal proofs read without truncation. B131 final layout-only differences, B133 explicit killed z coordinate and B134 explicit left/right Phi assignment were read completely. B134 entire two-sheet source, both small producers and genuine output reviewed. B131/B132 full earlier working proofs and producer reviews remain bound in checkpoint26 records. No duplicate large-table execution is claimed. Private QA was performed by the authors; final combined visible QA is a separate root task.',
 correction='The earlier one-sheet actual-final-group identification was withdrawn before integration. Original sources, producer outputs, reviews and the explicit correction remain retained. The accepted B134 uses both mirror conjugates and an abstract free extra edge generator.',
 main_A='Open',main_B='Open',
 limits=['No post-filling source injection.','No equality between a closed discrete kernel and the compact kernel.','No finite-stage matching stabilization.','No discrete subgroup separability or virtual retraction inferred from induced topology.','No fixed-source equality or global transfer conclusion.'])
dest=root/'records/checkpoint27_root_formal_reviews.json'
assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
late='work_A/actual_GT0_V4_Fox_defect27.md'
late_review='work_CE/review_actual_GT0_V4_Fox_defect27.txt'
assert sha(late)=='99a0b83621cb24d8fe2f2386cf330244e87ff47906b63d9400f79d02bc05cda9'
(root/'records/checkpoint27_root_MainA_review.json').write_text(json.dumps({
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'status':'PASS_COMPLETE_ACTUAL_V4_DEFECT_PROOF_READ','source':late,'source_sha256':sha(late),
 'independent_full_review':late_review,'independent_full_review_sha256':sha(late_review),
 'checks':['Full row-Fox product order and all three actual semilinear intertwining identities.','Exact regular mod-two H1 and split H2 section count, using already audited prescribed-class lifting.','All three full coset fixed sets reduce to the basepoint.','Closed pointed transversal from compact clopen shells, with no open-basepoint assumption.','Induction over the constant finite-group ring only; no F-stable transversal or Lambda-linear splitting.','Actual third-cusp lift has square xy and is not counted as an involution.'],
 'outcome':'Stronger necessary structure for the actual canonical GT0 defect; no Fox-unit or marked-generation conclusion. No general-P extension.'
},indent=2)+'\n')
research=root/'records/twenty_seventh_hour_research_report.md'
shutil.copy2(research,root/'records/twenty_seventh_hour_research_report_before_final_B134_review.md')
s=research.read_text()
s=s.replace('assumed. The complete two-sheet derivation is being written and reviewed\nbefore its proposed B134 integration.','assumed. The complete two-sheet derivation has passed full root and two\nindependent source reviews, with a four-page clean private build and\nindividual-page visual inspection. The accepted frozen B134 retains both\nmirror sheets; the original failed identification remains explicitly withdrawn.')
s+='''
## Actual Main-A progress after the core-deletion barrier

The uniform core-deletion obstruction ended that restricted quotient
route. We returned to the actual negative-GT0 canonical Fox coefficient.
The full coupled Jacobian identities for the commuting involutions alpha
and v now accompany the previously known scalar semilinear Fox identity.
The three nonidentity elements of their actual Klein four group have only
the basepoint fixed on the full compact canonical coset space F/H. The
proof uses the exact split H2 calculation and the already audited
prescribed-class lifting property, without replacing F by a pro-p group.

A closed pointed transversal is constructed shell by shell in that
compact metrizable space. Consequently the actual reduced coset/Fox
cokernel is induced from the trivial subgroup over the constant ring
Z_p[V4]. This strengthens the earlier single-involution obstruction
description. The transversal need not be F-stable, so no Lambda_F-linear
splitting or vanishing follows. The actual third-cusp transporter has
square xy; treating it as an involution would be an error. The required
Fox-unit/marked-generation implication therefore remains Open.

This complete research proof and its independent full review are retained
and root-reviewed, but are not silently promoted to an additional formal
statement in this four-proposition integration. The exact whole-input
m-star basis conversion also remains a pre-node normalization: all 40
node words and every signed source translate are retained.
'''
research.write_text(s)
print('PASS four complete frozen formal proofs and actual Main-A research review bound; both main decisions Open.')
