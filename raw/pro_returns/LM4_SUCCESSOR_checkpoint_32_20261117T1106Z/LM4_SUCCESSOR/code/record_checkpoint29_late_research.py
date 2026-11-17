"""Bind complete late reads and append their exact scopes without formal promotion."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import shutil

root = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
specs = {
    'work_A/actual_GT0_hexagon_Alexander_defect29.md': 'bf1a62a68ab35dec55cc7113400ec4bd8bdce54b8b732d8ba0c4ad7ec510df3b',
    'work_A/actual_GT0_remaining_odd_head_gate29.md': 'e419fc93ed71a51df5a8218244c26778e5f1ecd10d621bcad0d8e3ab0b1cf97a',
    'work_A/actual_coarse_filling_no_virtual_section29.md': 'e49a80e4c9f8496b1e55bb4cd4ae9fe694ade2b84df696db405bec2f0a7ebc5a',
    'work_A/actual_one_family_no_virtual_section29.md': '8244ade657aec61acd5c3a565d41c480b4270bb63e466607b95d4572896b7056',
    'work_CE/delta_fixed_branch_correction_obstruction29.txt': '3679e54a3ccc6d53ea2c46e8c0bbcc07bd66200aba03b66d431507a6966a4a5f',
    'work_CE/arbitrary_coarse_section_obstruction29.txt': '76ae7ec95c098289a610b792b0c63ac0367cc63b72f7821962e29b1dc8682e25',
    'work_CE/actual_first_jet_extension_class29.txt': 'a794b1f77fdb652b0e2f7562372b4342511198b29249ff18a93c0e8dbf03c2eb',
    'work_DE/next_marginal_source/center_cyclic_square_normalization29.md': '8d4c4d354dc559e8cc2335d1dc4e439cad159dea529894efa1949c4d51d3a36e',
    'work_DE/next_marginal_source/cyclic_leaf_filling_continuation29.md': 'aba73ce33d83d12297b46dfd09d2a04fb15e00aaeaba663e94ef2cb942180bff',
    'records/root_arbitrary_section_moment_certificate29.md': '9b81cc3a662e64de007f0d6f25b4903f26e69501de7156027f9275b4d5a404ec',
    'work_CE/one_family_fixed_source_exact_presentation29.txt': '4a9caed1b0247f73bd00848e923e88701479a8158194bab808d2544aca0b8ef5',
    'work_DE/next_marginal_source/center_basis_family_extension_obstruction29.md': '6aaa457523c65ccb00eeb5aa3ef993678595d289ddde44d91b26d732c40438fa',
}
for rel, digest in specs.items():
    assert sha(root / rel) == digest, rel

reviews = {}
by_source = {}
for rel, digest in specs.items():
    own = Path(rel).parts[0]
    matches = []
    for folder in ('work_A', 'work_CE', 'work_DE'):
        if folder == own:
            continue
        for p in sorted((root / folder).rglob('review*29*.json')):
            if 'before' in p.name:
                continue
            raw = p.read_text()
            json.loads(raw)
            if digest not in raw:
                continue
            companions = [q for q in (p.with_suffix('.md'), p.with_suffix('.txt')) if q.is_file()]
            text = raw + '\n' + '\n'.join(q.read_text() for q in companions)
            assert 'PASS' in text, str(p)
            for q in [p] + companions:
                key = str(q.relative_to(root))
                reviews[key] = sha(q)
                matches.append(key)
    assert matches, 'No independent hash-bound full review for ' + rel
    by_source[rel] = sorted(set(matches))

evidence = []
for stem in ('check_delta_fixed_branch_correction29', 'check_arbitrary_equivariant_section_jet29', 'check_unrestricted_section_eight_equations29'):
    evidence += ['work_CE/code/' + stem + suffix for suffix in ('.py', '.out', '.err')]
evidence += ['work_CE/next_symmetric_nodes/' + name + '.json' for name in ('delta_fixed_branch_correction29', 'arbitrary_equivariant_section_jet29', 'unrestricted_section_eight_equations29')]
evidence += ['code/check_root_arbitrary_section_certificate29.py']
evidence += ['records/root_arbitrary_section_certificate29' + suffix for suffix in ('.json', '.out', '.err')]
evidence += ['work_DE/code/check_center_cyclic_square29' + suffix for suffix in ('.py', '.out', '.err')]
evidence += ['work_DE/next_marginal_source/center_cyclic_square29.json']
evidence_hashes = {rel: sha(root / rel) for rel in evidence}

record = {
    'status': 'PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES',
    'utc': datetime.now(timezone.utc).isoformat(),
    'proof_sources': specs,
    'independent_reviews': reviews,
    'independent_reviews_per_source': by_source,
    'entire_root_read_evidence': evidence_hashes,
    'root_read_scope': 'All twelve complete proof records read; earlier ten before context continuation, final two and their complete independent reviews after continuation. Actual B141 full link table freshly rechecked for the center/family obstruction. Entire listed producers and outputs read in preceding work; the root certificate was also genuinely executed.',
    'formal_statement_count': 314,
    'formal_promotion': False,
    'main_A': 'Open',
    'main_B': 'Open',
    'not_distinct_theorem_count': 'Twelve proof records include the independent root derivation of the same arbitrary-section obstruction.',
    'execution_scope': 'No duplicate execution or duplicate raw geometric extraction is claimed for reviewed author producers. No broad finite census or UNKNOWN-solver restart.',
    'failure_scope': 'The previous context-ending patch returned truncated output and created neither destination file; existence was checked before this actual first creation. A later oversized combined report-read output was truncated and is not credited as a complete fresh read. Earlier completed proof reads remain separately recorded.',
}

summary = (root / 'records/checkpoint29_late_research_summary.md').read_text()
changes = [
    'LM4_SUCCESSOR_report.md',
    'task_coverage.csv',
    'records/twenty_ninth_hour_research_report.md',
    'records/primary_readings29.md',
    'records/checkpoint29_computation_audit_state.md',
]
destination = root / 'records/checkpoint29_root_late_reviews.json'
backup = root / 'records/checkpoint29_before_late_research'
assert not destination.exists() and not backup.exists()
for rel in changes:
    assert (root / rel).is_file(), rel
tasks_path = root / 'task_coverage.csv'
rows = list(csv.DictReader(tasks_path.open()))
assert len(rows) == 49
fields = list(rows[0])
initial_ids = [(r['task'], r['statement_ids'], r['outcome']) for r in rows]
for r in rows:
    if r['task'] in ('A.7', 'A.8'):
        r['state'] += ' Complete late29 research proves the actual full-head hexagon-class identity and, under full GT only, equality of the dyadic components of a_reg and d. The remaining full scalar test is exactly all odd cyclic heads; nonlinear Omega remains separate.'
        r['approaches'] += ' Actual signed Alexander substitutions, the prescribed full-GT pro-two hexagon, and the odd cyclic norm-line augmentation argument.'
        r['obstruction'] += ' Neither all odd-head coefficient tests nor the nonlinear full-word identity has been established; the dyadic theorem is not asserted for GT0 alone.'
        r['next_step'] = 'Resolve the actual all-odd-head characteristic-two coefficient test under its exact hypotheses, then the nonlinear marked three-cycle/Omega identity; retain separate P, GT0 and GT scope.'
    if r['task'] in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
        r['state'] += ' Complete late29 research proves arbitrary ordinary/compact coarse nonsplitting, its nonzero actual first-jet class at every odd prime, and no virtual section for the coarse or one-family filling. The exact ordinary fixed source is S amalg_L (L times Z_A), L=H intersect S retained whole. Complete cyclic-leaf filling has a proper ordinary carrier amalgam, but its extra ambient restriction kernel remains Open.'
        r['approaches'] += ' Eight unrestricted first-moment equations; actual finite coefficient quotients; complete homogeneous-cochain prism and coset averaging; parity retraction and full stabilizer presentation; two-sided cyclic recurrence and all translated leaf relations.'
        r['obstruction'] += ' Whole-group virtual nonsplitting does not decide the fixed subgroup. The marked fixed lift requires [A_src,L]=1. The center basis change cannot fix all family vertices, and its ordinary cyclic retraction is not ambient-continuous. All K translates and both mirror families remain essential.'
        r['next_step'] = 'Determine the entire actual L=H intersect S or prove [A_src,L]=1 directly; compare the complete mixed filling restriction kernel with every original translated family relation retained. Keep this intermediate analysis separate from actual icosahedral K=1.'
assert [(r['task'], r['statement_ids'], r['outcome']) for r in rows] == initial_ids
for rel in changes:
    q = backup / rel
    q.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / rel, q)
destination.write_text(json.dumps(record, indent=2) + '\n')
for rel in ('LM4_SUCCESSOR_report.md', 'records/twenty_ninth_hour_research_report.md'):
    p = root / rel
    p.write_text(p.read_text() + '\n\n' + summary)
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fieldnames=fields)
writer.writeheader()
writer.writerows(rows)
tasks_path.write_text(stream.getvalue())
p = root / 'records/primary_readings29.md'
p.write_text(p.read_text() + '''
## Complete late proof and coefficient-action audit

The twelve separate late proof records and independent reviews are bound
in checkpoint29_root_late_reviews.json. Root read every complete proof.
The actual A42/A45 and B123 internal inputs were freshly read in full
during the coefficient and extension comparisons; B141's complete actual
link table was freshly rechecked for the center/family obstruction.
The finite-index restriction argument is supplied as an entire explicit
homogeneous-cochain proof with the actual module action. No external
transfer theorem or unverified new citation is used. The final ordinary
fixed-source presentation follows directly from B139 and its actual
parity graph. The central bibliography remains114 verified/unverified
labelled entries, all114 printed in the unchanged final PDF.
''')
p = root / 'records/checkpoint29_computation_audit_state.md'
p.write_text(p.read_text() + '''
## Late unrestricted extension and complete orbit research

Twelve complete proof records, their independent hash-bound reviews and
twenty entirely read evidence files are now recorded. The exact root
eight-equation producer genuinely ran with exit0 and empty stderr.
The source records retain arbitrary lift variables, the complete signed
actions, and actual finite quotient routes. The m-inverse head-order
precursor is preserved before its correction. Virtual nonsplitting uses
an entirely supplied coefficient-weighted cochain argument. The exact
fixed-source presentation retains the whole stabilizer. All cyclic leaf
relations and the specified center/family compatibility obstruction are
retained, with no ambient or compact promotion. Both main decisions
remain Open; the formal paper stays314 statements and551 pages.

The context-ending patch immediately before the final continuation had
no filesystem effect, as an explicit existence check established. Its
truncated result is not treated as successful creation. The later large
combined report-read output was also truncated and is not counted as a
fresh complete read; the new proof and independent-review outputs were
fully returned and read. All actual earlier whole-proof reads remain
bound in their existing records. No extra ZIP or optional render was
created during these final text-only updates.
''')
print('PASS12 complete late proof records,20 complete evidence reads,49 task rows;314 formal statements unchanged;both main decisions Open.')
