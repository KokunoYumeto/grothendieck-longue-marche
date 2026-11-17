"""Bind genuinely completed root/independent late reads without changing the PDF."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, io, json, shutil

root = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
inputs = json.loads((root / 'records/checkpoint30_late_review_inputs.json').read_text())
assert inputs['root_complete_reads'] is True
specs = inputs['proof_sources']
for rel, digest in specs.items():
    assert sha(root / rel) == digest, rel
reviews, by_source = {}, {}
for rel, digest in specs.items():
    own = Path(rel).parts[0]
    matches = []
    for folder in ('work_A', 'work_CE', 'work_DE'):
        if folder == own:
            continue
        for path in sorted((root / folder).rglob('review*30*.json')):
            if 'before' in path.name:
                continue
            raw = path.read_text()
            json.loads(raw)
            if digest not in raw:
                continue
            companions = [q for q in (path.with_suffix('.md'), path.with_suffix('.txt')) if q.is_file()]
            text = raw + '\n' + '\n'.join(q.read_text() for q in companions)
            assert 'PASS' in text, str(path)
            for q in [path] + companions:
                key = str(q.relative_to(root))
                reviews[key] = sha(q)
                matches.append(key)
    assert matches, 'No independent final-hash review for ' + rel
    by_source[rel] = sorted(set(matches))
evidence = {}
for rel, digest in inputs['entire_root_read_evidence'].items():
    assert sha(root / rel) == digest, rel
    evidence[rel] = digest
record = {
    'status': 'PASS_COMPLETE_LATE_PROOF_REVIEW_WITH_EXPLICIT_REMAINING_GATES',
    'utc': datetime.now(timezone.utc).isoformat(),
    'proof_sources': specs, 'independent_reviews': reviews,
    'independent_reviews_per_source': by_source,
    'entire_root_read_evidence': evidence,
    'root_read_scope': inputs['root_read_scope'],
    'precise_scopes': inputs['precise_scopes'],
    'formal_statement_count': 323, 'formal_promotion': False,
    'main_A': 'Open', 'main_B': 'Open',
    'not_distinct_theorem_count': 'Separate proof records include a normalization followed by its stronger cyclic-stabilizer theorem and a mirrored-neck note whose final survival is explicitly already B121. Record count is not an independent-new-theorem count.',
    'execution_scope': 'Entire44-check and45-check producer/source outputs read; no duplicate execution by root. Matrix faithfulness, all-word stabilizers and all-head compactness use the full supplied proofs. No broad finite census or UNKNOWN-solver restart.',
    'failure_scope': 'Oversized combined source outputs were not counted; the relevant entire sources were subsequently returned separately. The incorrect proposal to extend an S-equivariant norm retraction over the full Q^0 head was withdrawn before promotion and is retained in the independent review. No ambient full topology or actual compact section is inferred from the new ordinary section.'
}
summary = (root / 'records/checkpoint30_late_research_summary.md').read_text()
changes = ['LM4_SUCCESSOR_report.md', 'task_coverage.csv',
           'records/thirtieth_hour_research_report.md', 'records/primary_readings30.md',
           'records/checkpoint30_computation_audit_state.md']
destination = root / 'records/checkpoint30_root_late_reviews.json'
backup = root / 'records/checkpoint30_before_late_research'
assert not destination.exists() and not backup.exists()
rows = list(csv.DictReader((root / 'task_coverage.csv').open()))
assert len(rows) == 49
fields = list(rows[0])
original = [(r['task'], r['statement_ids'], r['outcome']) for r in rows]
for row in rows:
    if row['task'] in ('A.7', 'A.8'):
        row['state'] += ' Late30 proves exact simultaneous all-odd-head common-word/duality realization and the literal canonical negative-hexagon equations in the three cyclic modules. The marked odd dihedral word coordinate can be prescribed independently at this source-word level; no canonical GT0 realization or coefficient counterexample is asserted.'
        row['approaches'] += ' Three explicit character-line idempotents; weighted norm-image proof; compact finite-intersection argument; complete negative-hexagon evaluation and coprime-factor joint image.'
        row['obstruction'] += ' These common-word and selected canonical-module identities add no missing weighted coefficient equation. The global canonical condition, full pentagon, and nonlinear cusp gate remain separate.'
        row['next_step'] = 'Retain the actual global canonical/pentagon condition in a further relative or nonlinear comparison capable of proving every odd-head identity; then resolve the full marked three-cycle/Omega word. Keep P, GT0 and full-GT scopes separate.'
    if row['task'] in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
        row['state'] += ' Late30 determines the ENTIRE ordinary stabilizer L=<m> by the actual invariant pillowcase quotient and faithful whole-source ping-pong. Thus the actual one-family fixed group is Z²*Z and its marked ordinary projection has the explicit section A->A_src,m->m,v->v. The entire original fixed kernel remains unresolved. An exact full first-family free-coset extension retains all opposite-family relations.'
        row['approaches'] += ' Invariant four-square pillowcase presentation, integer source matrices, rational affine coboundary, all-power ping-pong, B144 inverse presentations and actual B130 commutation; full family centralizer extensions over the actual opposite-region base.'
        row['obstruction'] += ' The ordinary marked section does not identify K_rem^delta with the source-kernel intersection or give a section of the actual compact fixed projection. The norm-copy retraction is S-equivariant only; its domain has infinite index in the full coarse-head preimage. Both original mirror families and all retained translates remain.'
        row['next_step'] = 'Use the new actual ordinary section to compare the remaining full fixed kernel with the source-kernel intersection; separately establish any required ambient topology. Continue the original B75 uniform characteristic finite-neighborhood condition for actual icosahedral K=1.'
assert [(r['task'], r['statement_ids'], r['outcome']) for r in rows] == original
for rel in changes:
    target = backup / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / rel, target)
destination.write_text(json.dumps(record, indent=2) + '\n')
for rel in ('LM4_SUCCESSOR_report.md', 'records/thirtieth_hour_research_report.md'):
    path = root / rel
    path.write_text(path.read_text() + '\n\n' + summary)
stream = io.StringIO(newline='')
writer = csv.DictWriter(stream, fieldnames=fields)
writer.writeheader(); writer.writerows(rows)
(root / 'task_coverage.csv').write_text(stream.getvalue())
for rel in ('records/primary_readings30.md', 'records/checkpoint30_computation_audit_state.md'):
    path = root / rel
    path.write_text(path.read_text() + f'''
## Final late-cycle complete proof review

The late record now binds {len(specs)} entire proof records and their
independent final-hash reviews. We entirely read the invariant pillowcase
presentation, the faithful all-power ping-pong argument, and the actual
marked ordinary section. These prove L=<m> and J_a=Z²*Z, superseding the
earlier unresolved ordinary-stabilizer gate in the frozen formal baseline.
The formal PDF remains323 statements and573 pages; no extra statement is
silently promoted. The precise complete proofs and their category limits
are supplied in the retained late sources and the appended research summary.
We also read the complete44-check and45-check producers and genuine outputs;
this is not a second execution. The proposed ambient extension of the
S-equivariant norm-copy retraction was explicitly withdrawn because its
head is only S, whereas the full ordinary head is Q^0=T0 semidirect S.
No full topology, completed stabilizer equality, or actual compact fixed
section is inferred from that invalid extension. Both main problems remain
Open; the original icosahedral uniform finite-neighborhood gate is retained.
''')
print(f'PASS {len(specs)} entire late proof records, {len(reviews)} independent review files, {len(evidence)} entire source/output reads;49 task rows;323 formal statements unchanged; both mains Open.')
