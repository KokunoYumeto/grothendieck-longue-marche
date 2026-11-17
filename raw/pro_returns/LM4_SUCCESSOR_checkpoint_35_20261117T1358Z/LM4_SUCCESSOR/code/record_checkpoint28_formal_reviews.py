"""Bind completed manual proof reviews; this script does not automate proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
specs = [
    ('A.85', 'work_A/A85_V4_Fox_defect_proposed.tex', 'sections/a_v4_fox_defect.tex', '72e3ff7cb8a80eb17071f39dc37ab83ae34d2427f973857013d15fd94eaf2960'),
    ('A.86', 'work_A/A86_canonical_cusp_frame_proposed.tex', 'sections/a_canonical_cusp_frame.tex', 'b9cc677da863a714ef37ca9e9a8059df522789fbdb0c51e1774bcb25c09862ee'),
    ('B.135', 'work_CE/B135_m_star_face_kernel_proposed.tex', 'sections/b_m_star_face_kernel.tex', '2f55c95b4cbf4abb4ad8c1f51d3c2cca4db4cdeeb912e733c4379c4d7eece1fd'),
    ('B.136', 'work_DE/B136_unfilled_edges_local_symmetry_proposed.tex', 'sections/b_unfilled_edges_local_symmetry.tex', 'b7436c3af4e14ac18d1d6ea2fd3726ed7e66593561dc97375aed516055821819'),
    ('B.137', 'work_DE/B137_ambient_vertex_overlap_proposed.tex', 'sections/b_ambient_edge_intersection.tex', '7493a13ca86246d5e369f56f7ec302a514ad7ba3938a7484b6da3522e3f845bc'),
]
copies = []
for statement, source, target, digest in specs:
    assert sha(source) == digest
    copies.append(dict(statement=statement, source=source, target=target, sha256=digest))
reviews = [
    'work_CE/review_A85_formal_source28.txt', 'work_CE/review_A85_formal_source28.json',
    'work_CE/review_A86_formal_source28.txt', 'work_CE/review_A86_formal_source28.json',
    'work_A/review_B135_formal28.md', 'work_A/review_B135_formal28.json',
    'work_DE/next_marginal_source/review_B135_final_source28.md',
    'work_DE/next_marginal_source/review_B135_final_source28.json',
    'work_A/review_B136_formal28.md', 'work_A/review_B136_formal28.json',
    'work_CE/review_B136_formal_source28.txt', 'work_CE/review_B136_formal_source28.json',
    'work_A/review_B137_formal28.md', 'work_A/review_B137_formal28.json',
    'work_CE/review_B137_formal_source28.txt', 'work_CE/review_B137_formal_source28.json',
]
qa = ['work_A/A85_A86_components28_manifest.json', 'work_CE/B135_component_QA.json',
      'work_DE/B136_component_QA.json', 'work_DE/B137_component_QA.json']
review_text = '\n'.join((root / r).read_text() for r in reviews)
qa_text = '\n'.join((root / r).read_text() for r in qa)
for row in copies:
    assert row['sha256'] in review_text
    assert row['sha256'] in qa_text
record = dict(
    recorded_at=datetime.now(timezone.utc).isoformat(),
    status='PASS_COMPLETE_SOURCE_REVIEW', copies=copies,
    independent_reviews={r: sha(r) for r in reviews},
    private_QA_records={r: sha(r) for r in qa},
    primary_readings='records/primary_readings28.md',
    root_scope='All five complete formal proofs were read. The final A86 square-cancellation precision and B135 proper-edge precision were separately read as complete diffs and in context. Both complete B137 research notes, its entire actual-word producer and genuine output were read. No repeated producer execution is claimed. Author private QA covers all 24 component pages; final combined PDF QA is a separate root task.',
    preserved_corrections=[
        'A86 initial source, PDF and QA directory precede the explicit r-square torsion-free cancellation.',
        'B135 initial union-control-sequence typo and pre-compact source/PDF remain retained.',
        'B135 compact precursor was reconstructed by the author, exactly hash-matched, and honestly labeled as reconstructed rather than contemporaneously preserved.',
        'B137 initial vertex-only source remains retained before the whole ordinary intersection upgrade.'
    ],
    main_A='Open', main_B='Open',
    limits=[
        'The constant V4-ring induced module is not asserted to split over the full completed group ring.',
        'Neither a_reg=d nor the exact nonlinear cusp word Omega=1 is proved.',
        'No final ambient fixed-source equality follows from the inner-star or retract-block calculations.',
        'The whole edge-group intersection in B137 is ordinary only.',
        'No generated-subgroup free-product assertion, filling survival or ambient kappa-kernel invariance is inferred.'
    ])
dest = root / 'records/checkpoint28_root_formal_reviews.json'
assert not dest.exists()
dest.write_text(json.dumps(record, indent=2) + '\n')
print('PASS five complete frozen sources; both main decisions Open.')
