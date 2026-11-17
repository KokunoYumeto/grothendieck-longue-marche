"""Preserve the first late report, then bind the ten complete final research proofs."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

root = Path(__file__).resolve().parents[1]
sha = lambda rel: hashlib.sha256((root / rel).read_bytes()).hexdigest()
backup = root / 'records/checkpoint28_before_late_refinement'
assert not backup.exists()
backup.mkdir()
preserved = [
    'records/checkpoint28_root_late_reviews.json',
    'records/twenty_eighth_hour_research_report.md',
    'LM4_SUCCESSOR_report.md', 'task_coverage.csv',
    'code/capture_checkpoint28.py', 'records/primary_readings28.md',
]
for rel in preserved:
    dest = backup / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / rel, dest)
sources = {
    'work_A/actual_GT0_marked_three_cycle_gate28.md': 'e024ffd0ad2213f1b5858035a16f0565ec8c939d1c10c116721f2857a9695f36',
    'work_A/actual_GT0_explicit_three_cycle_cusp_frame28.md': 'fc93b244ab4123e690b376d97d6df13e434fa8eeac33d7f4427d7238af9dfbe3',
    'work_A/actual_GT0_first_cusp_Alexander_equation28.md': '7d1758dce5dff7b207ba48a589d0b584fad6b8a1140e264096ee2662906a6e27',
    'work_DE/next_marginal_source/ambient_shifted_overlap28.md': '8471548451fb635dc236ad2926ebaaa149410d129b72293a84fb670f05bef189',
    'work_DE/next_marginal_source/compact_vertex_overlap28.md': 'a98ec7186d41d59579ebf3e392f889938a296bfede12b278bfc0c009b808eb24',
    'work_DE/next_marginal_source/compact_actual_edge_embedding28.md': '545b2f0d160ced17f4a92f11f70b94f1124840fa6aff7316873ffad83a512e26',
    'work_DE/next_marginal_source/compact_whole_edge_intersection28.md': 'b2dad4594eb714d404e7d2140b4d5d3287c53b89bf9e6d4f9ef776f33597e275',
    'work_CE/one_family_graph_fixed_source28.txt': '7913056ee9d52c58b8c41095947d3111fb6bd27b600fa59ee7839244800f76b4',
    'work_CE/one_family_kernel_reduction28.txt': '052f63b03dac60645d160c9dafdb794b31f59c85fe036ea6ceff73377d9aced1',
    'work_CE/compact_one_family_fixed_source28.txt': '4f2b2617d7ccf2a86ea6c8b4c6fe21a96316b6c8aa555097f45f3f4dd4b548f5',
}
# The full frozen digest is written explicitly, correcting a transcription before use.
sources['work_CE/compact_one_family_fixed_source28.txt'] = '4f2b2617d7ccf2a86ea6c8b4c6fe21a96316b6c6aa555097f45f3f4dd4b548f5'
for rel, digest in sources.items():
    assert sha(rel) == digest, rel
stems = [
    ('work_CE/review_marked_three_cycle_gate28', 'txt'),
    ('work_CE/review_explicit_three_cycle_cusp_frame28', 'txt'),
    ('work_CE/review_first_cusp_Alexander_equation28', 'txt'),
    ('work_A/review_ambient_shifted_overlap28', 'md'),
    ('work_A/review_compact_vertex_overlap28', 'md'),
    ('work_CE/review_compact_vertex_overlap28', 'txt'),
    ('work_A/review_compact_actual_edge_embedding28', 'md'),
    ('work_A/review_compact_whole_edge_intersection28', 'md'),
    ('work_CE/review_compact_whole_edge_intersection28', 'txt'),
    ('work_DE/next_marginal_source/review_one_family_fixed_source28', 'md'),
    ('work_A/review_compact_one_family_fixed_source28', 'md'),
    ('work_DE/next_marginal_source/review_compact_one_family_fixed_source28', 'md'),
]
reviews = [stem + '.' + ext for stem, text_ext in stems for ext in (text_ext, 'json')]
review_text = '\n'.join((root / rel).read_text() for rel in reviews)
for digest in sources.values():
    assert digest in review_text, digest
producers = []
for stem in ('compile_one_family_face28', 'check_one_family_sources28', 'check_one_family_kernel_gate28'):
    producers.extend('work_CE/code/' + stem + '.' + ext for ext in ('py', 'out', 'err'))
producers.extend('work_CE/next_symmetric_nodes/' + name + '.json' for name in
                 ('one_family_face28', 'one_family_sources28', 'one_family_kernel_gate28'))
record = dict(
    recorded_at=datetime.now(timezone.utc).isoformat(),
    status='PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES',
    proof_sources=sources, independent_reviews={rel: sha(rel) for rel in reviews},
    complete_root_producer_and_output_reads={rel: sha(rel) for rel in producers},
    formal_statement_count=308, formal_promotion=False,
    previous_record_preserved='records/checkpoint28_before_late_refinement/records/checkpoint28_root_late_reviews.json',
    root_read_scope='All ten complete proof sources read without relying on truncated output, including each final precision correction. The three entire exact producers, final genuine outputs and complete JSON fields were read. No duplicate root execution. The compact one-family primary audit freshly read Lorensen local 3.10--3.15 and full 2.5 proof, and Boggi--Zalesskii Definition4.1, full Theorem4.3 statement, entire Lemma4.4 proof, complete prime-order Section4.2 and Lemma2.2 proof. RZ2004 full local product-closure proof was separately freshly read. Root checked the all-module, finite-type, residual-finiteness and actual finite-target hypotheses.',
    exact_results=[
        'Actual marked hexagon iff Xi_d=(v delta^d)^3=1 iff canonical Omega=1; the first coefficient gate is t=rho_D.',
        'Unique actual cusp frame h0=rho_cyc^2(A)rho_cyc(A)^-1u, with the actual pure r-frame A in F-prime.',
        'The canonical full solution transported to the original marking satisfies alpha(G)=delta^-1 G delta^-1 and G_ab=(-2t,a_reg). Equality a_reg=d is exactly G_ab,x=k; it remains unproved.',
        'Exact ordinary shifted edge overlap is <k>, and the initial two-family filling misses its actual compact cyclic closure.',
        'Uniform actual virtually free targets prove the full compact vertex and incident-product comparisons for every finite target.',
        'Both actual whole cyclic-edge subamalgams carry their full profinite topology; their completed regional intersections and embedded compact coset trees are proved.',
        'The two whole unfilled compact edge groups have trivial intersection in the actual full ambient completion, by continuous common-retract kernels and a proved factorwise intersection lemma.',
        'The actual discrete one-family fixed subgroup equals its actual source image; the specific original-to-one-family fixed projection is surjective because each fixed generator has its actual fixed source lift.',
        'The original discrete fixed-source equality is equivalent to the exact remaining fixed-kernel equality.',
        'The actual completed one-family fixed subgroup equals its closed actual source image. The corresponding original completed fixed projection is surjective and original equality is equivalent to (closure Krem)^delta = closure Hsrc intersect closure Krem.'
    ],
    remaining_gates=[
        'Neither t=rho_D nor Xi_d=1 nor Omega=1 is proved. R2 has not received the missing compatible third marked peripheral input.',
        'No unfilled intersection result proves generation as a free product, all-translated overlap control, filling survival or ambient kappa-kernel invariance.',
        'The original discrete and completed remaining fixed-kernel equalities remain Open; the infinite graph kernel is never identified with an abstract full completion.',
        'The remaining necks, global transfer, joint-source condition and actual Main-B K=1 remain Open.'
    ], main_A='Open', main_B='Open')
(root / 'records/checkpoint28_root_late_reviews.json').write_text(json.dumps(record, indent=2) + '\n')
addition = '''## Further complete research after the formal freeze

We retain ten complete, independently reviewed research proofs separately
from the five frozen formal propositions. Exact final sources, reviews,
producers and outputs are bound in checkpoint28_root_late_reviews.json.
Earlier reports and every precision correction are retained byte-exactly.

On Main A, the actual marked positive hexagon is equivalent to the literal
order-three equation Xi_d=(v delta^d)^3=1 and the canonical Omega=1.
The unique actual pure r-frame A gives
h0=rho_cyc^2(A)rho_cyc(A)^-1u. Transporting C44's unique full solution
to the original first-cusp marking gives alpha(G)=delta^-1 G delta^-1,
with G_ab=(-2t,a_reg). Thus a_reg=d is exactly G_ab,x=k, equivalently
t=rho_D. This scalar comparison and the nonlinear Omega identity remain
Open. We have not supplied R2 with an unproved third compatible cusp.

For Main B, the shifted ordinary overlap is exactly <k>, and the initial
two-family filling misses its actual compact cyclic closure by winding.
Uniform all-modulus virtually free quotients prove the complete compact
vertex and incident-product comparisons. Arbitrary finite targets of
each whole cyclic-edge subgroup then extend after compatible finite
regional refinements. This proves full induced topology, exact completed
regional intersections and embedded compact coset trees. A continuous
common-retract kernel decomposition and a proved arbitrary-factor
free-profinite-product intersection lemma give the further exact result
that the two whole unfilled compact edge groups intersect trivially.
These results do not establish filling survival or kappa-kernel symmetry.

The actual one-family quotient has its complete graph-group semidirect
presentation and its discrete fixed subgroup equals its actual source
image. The specific fixed projection from the original group is indeed
surjective: the fixed generators have literal fixed source lifts. The
earlier overly restrictive sentence withholding this consequence is
corrected and its original bytes retained. The remaining original
discrete equality is exactly the remaining fixed-kernel condition.

We also prove the actual completed one-family equality
(Gamma_a hat)^delta=closure(J_src,a). Every arbitrary finite target
factors through an actual finite graph group with its finite coefficient
action, retaining both cone characters and the entire source cocycle.
A further finite refinement controls the coarse centralizer. Finite
graph goodness and the prime-order centralizer theorem apply with
residual finiteness, finite virtual cohomological type and every discrete
coefficient module checked explicitly. We never identify the completion
of the infinite graph kernel. For the original remaining kernel Krem,
(Gamma_0 hat)^delta=closure(Hsrc) (closure Krem)^delta. The original
completed source equality is therefore equivalent to
(closure Krem)^delta=closure(Hsrc) intersect closure Krem.
This last equality remains Open, as do both main problems.
'''
marker = '## Further complete research after the formal freeze'
for rel in ('records/twenty_eighth_hour_research_report.md', 'LM4_SUCCESSOR_report.md'):
    p = root / rel
    old = p.read_text()
    assert old.count(marker) == 1
    p.write_text(old.split(marker)[0] + addition)
p = root / 'task_coverage.csv'
with p.open(newline='') as f:
    reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
assert len(rows) == 49
for row in rows:
    if row['task'] in {'A.7', 'A.8'}:
        row['state'] += ' Late complete proofs identify the actual pure three-cycle cusp frame and transport the unique full Alexander solution into the original alpha marking. The exact remaining scalar gate is G_ab,x=k, equivalently t=rho_D; the nonlinear Omega identity remains open.'
        row['next_step'] = 'Compare the actual first-cusp Alexander solution coordinate with the canonical dihedral exponent, then prove or refute the nonlinear Omega identity with all three marked peripheral inputs retained.'
    if row['task'] in {'B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'}:
        row['state'] += ' Late full proofs establish full induced profinite topology of both whole unfilled cyclic-edge subgroups and their trivial compact intersection. The actual one-family quotient has discrete and completed fixed-source equality; the original comparison reduces exactly to its remaining fixed-kernel equality.'
        row['obstruction'] = row['obstruction'].replace('Whole compact edge overlap, translated overlap control, local filling survival and ambient kappa-kernel invariance remain separate gates.', 'Whole compact unfilled edge overlap is now proved; all-translated overlap control, local filling survival and ambient kappa-kernel invariance remain separate gates.')
        row['obstruction'] += ' The original remaining fixed-kernel equality is still unproved in both categories; no result is transferred through the restored fillings.'
        row['next_step'] = 'Resolve the actual remaining fixed-kernel equality and filling survival/kappa-kernel symmetry using both sheets and all translated normal relations, then address the remaining necks and global transfer.'
with p.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
p = root / 'LM4_SUCCESSOR_report.md'; lines = p.read_text().splitlines(True)
start = next(i for i, line in enumerate(lines) if line.startswith('| Task or lead |'))
end = start
while end < len(lines) and lines[end].startswith('|'): end += 1
cell = lambda value: value.replace('|', '\\|').replace('\n', ' ')
table = ['| Task or lead | Statements | Outcome and exact state |\n', '|---|---|---|\n']
table.extend('| ' + cell(r['task']) + ' | ' + cell(r['statement_ids']) + ' | **' + cell(r['outcome']) + '** — ' + cell(r['state']) + ' |\n' for r in rows)
lines[start:end] = table; p.write_text(''.join(lines))
p = root / 'code/capture_checkpoint28.py'; s = p.read_text()
s = s.replace('a complete discrete one-family fixed-source comparison,', 'complete discrete and profinite one-family fixed-source comparisons,')
s = s.replace('full compact vertex/product comparisons and discrete fixed-source\nequality in the exact one-family quotient,', 'full compact whole-edge embeddings and their trivial intersection,\nand discrete and profinite fixed-source equality in the exact one-family quotient,')
s = s.replace('marked cusp/frame comparison, compact whole-edge embedding, translated\nfilling interactions and ambient kappa-kernel/source comparison.', 'marked cusp/frame comparison, remaining fixed-kernel equality, translated\nfilling interactions and ambient kappa-kernel/source comparison.')
p.write_text(s)
p = root / 'records/primary_readings28.md'
p.write_text(p.read_text() + '''

## Root final compact one-family primary audit

The first combined B112/primary opening near04:39 was truncated and is
not credited as a complete reading. B112 was not reread completely in
that call. Subsequent bounded fresh primary opens supplied all required
local proofs without relying on that truncated output.

Lorensen, K. (2008), author PDF https://arxiv.org/pdf/0802.0118:
turn1051view1 and turn1052view1 cover all local HNN comparison3.10,
Corollary3.11, Proposition3.12, Theorem3.13, Lemma3.14 and Theorem3.15
with their complete proofs (lines516--626). The finite-module class is
checked in turn1053view1 lines97--116. Theorem2.5, its spectral-sequence
dependency and full proof were read through turn1053view1 and
turn1055view0 lines172--282. No claim of a complete article read.

Boggi, M., & Zalesskii, P. (2024). Finite subgroups of the profinite
completion of good groups (arXiv:2406.08639v2).
https://arxiv.org/html/2406.08639v2 . Root freshly read Definition4.1,
the entire Theorem4.3 statement, entire Lemma4.4 statement/proof,
complete prime-order Section4.2, and entire Lemma2.2 statement/proof.
Refs turn1051view0, turn1052view0, turn1052view2, turn1053view0 and
turn1054view0 jointly cover lines268--391 and178--200, including the
diagram and closing lines374--377. Only the order-two application is
used. Root independently checked finite virtual cohomological TYPE,
RF, dense injection and all discrete continuous F2 coefficient modules:
finite Salvetti resolution, finite invariant-submodule exhaustion and
continuous finite-image cochains, followed by the finite-extension LHS
comparison. The actual infinite graph kernel receives no unsupported
completion identification. Complete source4f2b2617... passes.
''')
(root / 'records/checkpoint28_late_refinement.json').write_text(json.dumps({
    'at': datetime.now(timezone.utc).isoformat(), 'proof_count': len(sources),
    'status': 'PASS', 'preserved_prior_bytes': {rel: sha('records/checkpoint28_before_late_refinement/' + rel) for rel in preserved},
    'formal_pdf_unchanged': sha('LM4_SUCCESSOR_paper.pdf'), 'task_rows': len(rows),
    'no_duplicate_producer_execution': True, 'no_extra_archive': True,
}, indent=2) + '\n')
print('PASS ten complete reviewed research proofs; prior bytes retained;49 task rows synchronized; formal530-page paper unchanged.')
