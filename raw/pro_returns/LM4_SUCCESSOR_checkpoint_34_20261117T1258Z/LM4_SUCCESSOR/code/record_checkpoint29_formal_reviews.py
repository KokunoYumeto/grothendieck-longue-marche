"""Bind completed manual source reviews; no mathematical proof is automated."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
specs = [
    ('A.87', 'work_A/A87_marked_three_cycle_cusp_frame_proposed.tex', 'sections/a_marked_three_cycle_cusp_frame.tex', 'a0fbb3353bd111039cd19b8f2047e7c60541e67f42e34193c138af2113669540'),
    ('A.88', 'work_A/A88_Alexander_dihedral_coefficient_proposed.tex', 'sections/a_alexander_dihedral_coefficient.tex', 'b891f7243052175e00851db3c438c45652fe648bf7cd50cc7a2db8d1d6064e6a'),
    ('B.138', 'work_DE/B138_compact_unfilled_edges_proposed.tex', 'sections/b_compact_unfilled_edges.tex', 'fbbc70b6940cfd040dc593b4cf22eae10027b5f195f8c5e20144d7cde8899b1f'),
    ('B.139', 'work_CE/B139_one_family_fixed_source_proposed.tex', 'sections/b_one_family_fixed_source.tex', 'b0ccd7563fd172827593ef842b1d91b7be32a5f3e69625e6dd680b5d36634815'),
    ('B.140', 'work_CE/B140_retained_section_obstruction_proposed.tex', 'sections/b_retained_section_obstruction.tex', 'cf04739bbabd4dde615af5c5fbd02ea39ace289dc6a807193452fa94a1ffd534'),
    ('B.141', 'work_DE/B141_regional_kernel_mixed_filling_proposed.tex', 'sections/b_regional_kernel_mixed_filling.tex', 'da843aad3463fec533842471e11b244a0094591d123547551d593f9d517d3d9f'),
]
copies = []
for statement, source, target, digest in specs:
    assert sha(source) == digest, source
    copies.append(dict(statement=statement, source=source, target=target, sha256=digest))
reviews = [
    'work_CE/review_A87_formal_source29.txt', 'work_CE/review_A87_formal_source29.json',
    'work_CE/review_A88_formal_source29.txt', 'work_CE/review_A88_formal_source29.json',
    'work_A/review_B138_formal29.md', 'work_A/review_B138_formal29.json',
    'work_CE/review_B138_formal_source29.txt', 'work_CE/review_B138_formal_source29.json',
    'work_A/review_B139_formal29.md', 'work_A/review_B139_formal29.json',
    'work_DE/next_marginal_source/review_B139_formal29.md',
    'work_DE/next_marginal_source/review_B139_formal29.json',
    'work_A/review_B140_section_repair29.md', 'work_A/review_B140_section_repair29.json',
    'work_DE/next_marginal_source/review_B140_formal29.md',
    'work_DE/next_marginal_source/review_B140_formal29.json',
    'work_A/review_B141_formal29.md', 'work_A/review_B141_formal29.json',
]
qa = ['work_A/A87_A88_components29_manifest.json',
      'work_DE/B138_component_QA.json', 'work_CE/B139_component_QA.json',
      'work_CE/B140_component_QA.json', 'work_DE/B141_component_QA.json']
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
    primary_readings='records/primary_readings29.md',
    root_scope='All six entire formal proofs were read. The exact final A88 two-line epsilon notation repair and B140 initial-display wrap were separately read as complete diffs against preserved originals. Entire underlying research proofs and the complete C44 and B112 internal dependencies were read. Root read its entire coefficient producer, genuine stdout/stderr, all24 row summaries and the selected complete12-term class; long raw word arrays were retained and expansion-checked, without claiming a second literal read of all arrays. Both complete CE adjustment producers and their full genuine eight-case JSON/output were read. Independent reviews are separate; no duplicate producer execution is claimed. Private component QA is separate from final assembled PDF QA.',
    preserved_corrections=[
        'A88 original source and entire initial private QA are retained before replacing comma superscripts by parenthesized powers of the inverted epsilon.',
        'B140 original source/PDF and all genuine logs are retained before the initial display was wrapped; no algebra changed.',
        'B138 initial unavailable-pdflatex-format attempt is retained before the successful clean LuaLaTeX build.',
        'The root attempted a nonexistent integrate_checkpoint28.py read, corrected to integrate_checkpoint28_proofs.py; no mutation or computation occurred in that failed read.'
    ],
    main_A='Open', main_B='Open',
    limits=[
        'The exact full Alexander criterion and equality modulo8 do not establish equality of the two full profinite units or the nonlinear cusp word.',
        'The compact whole-edge comparison concerns the unfilled ambient group; the full translated compact overlap and post-filling survival remain distinct.',
        'The exact one-family fixed-source result does not decide the remaining fixed-kernel condition in the original group.',
        'The source-adjustment obstruction excludes the two named sections and their common J-conjugates, not arbitrary nonconjugate coarse sections.',
        'The faithful regional graph kernel and mixed square relation do not prove regional collapse, local filling survival, ambient kappa-kernel invariance, or the final source equality.'
    ])
dest = root / 'records/checkpoint29_root_formal_reviews.json'
assert not dest.exists()
dest.write_text(json.dumps(record, indent=2) + '\n')
print('PASS six complete frozen formal sources; both main decisions Open.')
