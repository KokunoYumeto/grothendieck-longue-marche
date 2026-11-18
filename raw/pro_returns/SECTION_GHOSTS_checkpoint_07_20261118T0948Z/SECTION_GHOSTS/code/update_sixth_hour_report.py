#!/usr/bin/env python3
"""Record the fourth formal review against immutable checkpoint05."""
from pathlib import Path
from collections import Counter
import csv
import datetime
import io
import zipfile

root = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc)
assert now >= datetime.datetime(2026, 11, 18, 8, 44, 30, tzinfo=datetime.timezone.utc), 'Review is not yet due'
results = list(csv.DictReader((root/'SECTION_GHOSTS_results.csv').open()))
history = list(csv.DictReader((root/'notes/historical_audit.csv').open()))
events = len(list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(), delimiter='\t')))
with zipfile.ZipFile(root.parent/'SECTION_GHOSTS_checkpoint_05.zip') as z:
    old_results = list(csv.DictReader(io.StringIO(z.read('SECTION_GHOSTS/SECTION_GHOSTS_results.csv').decode())))
    old_history = list(csv.DictReader(io.StringIO(z.read('SECTION_GHOSTS/notes/historical_audit.csv').decode())))
old_r = {r['id']: r for r in old_results}
old_h = {r['historical_id']: r for r in old_history}
movement = []
for r in results:
    if r['id'] in old_r and old_r[r['id']]['status'] == 'Open' and r['status'] != 'Open':
        movement.append(f"{r['id']}: Open to {r['status']}")
for r in history:
    if r['historical_id'] in old_h and old_h[r['historical_id']]['audit_status'] == 'pending' and r['audit_status'] != 'pending':
        movement.append(f"{r['historical_id']}: pending to {r['audit_status']}")
# No separately proved strict narrowing of a main gate occurred in this interval.
no_movement_count = 0 if movement else 1
rc = Counter(r['status'] for r in results)
hc = Counter(r['audit_status'] for r in history)
updates = {
 'A.2': ('A.2; A.20–A.21; A.31–A.32; E.137–E.159; E.170–E.174; E.185–E.187',
 'Undecided. One fixed ordinary infinite-support pair must survive every class and every coefficient prime. The earlier all-prime class-two construction supplies an unrestricted class-three lift only. At three the one-step gate remains the old-support plus-character system; at two it remains the finite matching test with all real frames. A.32 rules out projective arithmetic quotients retaining the cyclotomic character as a way to introduce ordinary infinite ramification. E.187 supplies compact preassigned valuation catalogs with the actual twisted dyadic relations, but no common catalog passes all finite tests. These scope and compactness results do not narrow the main gate. Next: establish one passing compatible branch or a uniform obstruction while retaining the same pair.'),
 'A.3': ('A.2–A.3; A.31–A.32; E.66–E.69; E.123–E.159; E.185–E.187',
 'Undecided for every coefficient prime. At three, no infinite branch through the old-support plus equations is established. At two, E.185 gives the exact arithmetic presentation with coupled Frobenius words; E.186 proves that a real-preserving arithmetic splitting can align an actual odd-prime Frobenius at at most one prime. E.187 retains those twists in a compact finite-test criterion, with common-catalog nonemptiness still missing. At primes at least five, finite class-two approximation has not been iterated through all weights. Next: solve the actual simultaneous higher matching conditions, rather than an untwisted or projective substitute.'),
 'C.3': ('C.4; A.8; E.50–E.59; E.90–E.97; E.176–E.184',
 'The compact separation lemma and LM4 relative-tower comparisons are proved. E.180 closes the exact symmetrizer/Schreier coefficient comparison. E.181–E.184 prove arithmetic normalization, the actual mixed pants action and ordinary forgetting, the same-parameter two-point branch marking, and positive pointwise translation-grid fusion with its full completed normalizer. Higher-point involution and branch covariance, CM vanishing, and the original finite compiler bounds remain unproved. No universal section target follows. Next: complete that common-parameter higher-point comparison and then audit the finite construction.'),
 'E.1': ('Part E; E.160–E.187; historical audit table',
 'All unconditional inputs have their stated proofs and source locators. The exact E.2 list is fully audited. The qualitative full-GT chain now includes the symmetrizer coefficient, mixed and forgetting actions, the two-point branch gauge, and the actual three-torsion-grid normalizer. Four broader historical GT claims remain pending; these qualitative dependencies do not certify their full CM and numerical conclusions. Next: complete the higher-point branch comparison and the finite compiler without importing either as a premise.'),
 'L.5': ('C.1–C.5; C.7–C.8; A.8; E.50–E.59; E.90–E.97; E.176–E.184',
 'The compact and LM4 comparisons are proved in their exact scopes. The historical coefficient identity and several qualitative full-GT geometry dependencies are now repaired, including the same-parameter two-point branch action and full translation normalizer. The higher-point branch comparison and historical explicit finite bound remain pending. The section-side ordinary family is still not a compact varying-pair family; E.187 only gives compactness after a common uniform valuation catalog is fixed. No catalog with every finite test nonempty, universal section obstruction, or CM parity theorem is asserted. Next: close the remaining geometry and establish a valid section-side all-depth argument.')
}
rp = root/'SECTION_GHOSTS_report.md'
report = rp.read_text()
marker = '## Sixth work period: arithmetic route obstructions and qualitative GT repairs'
assert marker not in report, 'Refusing to rewrite a dated work period'
lines = []
for line in report.splitlines():
    if line.startswith('| '):
        key = line.split('|')[1].strip()
        if key in updates:
            refs, state = updates[key]
            line = f'| {key} | {refs} | {state} |'
    lines.append(line)
report = '\n'.join(lines)+'\n'
report += '\n'+marker+'''

A.32 rules out an infinite-ramification projective arithmetic quotient as the proposed source of an ordinary ghost: retaining the cyclotomic character together with nonzero off-diagonal tame inertia would embed Z_ell semidirect Z_ell and force nonzero second cohomology. This obstruction does not depend on assuming a finite ramification set. Independently opened local ramification results of Hoshi and Hoshi–Mochizuki corroborate the existing support-prime singleton theorem A.31, but do not improve its zero-support or equal-coefficient scope.

E.185 proves the exact dyadic arithmetic presentation, including the full-group/maximal-pro-two H2 comparison and the actual one-prime free product at a prime congruent to3 or5mod8. Several support primes retain coupled Frobenius words. E.186 proves that a real-preserving splitting of the full maximal pro-two Galois group onto the group unramified outside2 can align actual Frobenius lifts at at most one odd prime; the bound is sharp. The quadratic-character proof retains the actual path terms rather than assuming a simultaneous arithmetic splitting of all local groups.

E.187 gives a rigorous compact catalog construction. Finite valuation alphabets have a uniform divisibility condition, and closed finite-block conditions force infinite support. The actual infinite arithmetic presentation uses converging inertia generators and every twisted Frobenius relator. Uniform divisibility makes evaluation of those profinite words continuous. Full pro-two existence is then equivalent to nonemptiness of all nested finite tests for the same catalog. No such catalog is shown to pass every test. Freezing one valuation alone is noncompact, as shown already by rational point sections. Removing the finitely many rational pairs from a compact catalog can destroy finite-test nonemptiness. This is not credited as a strict improvement of the main gate.

E.180 proves equality of the historical symmetrizer coefficient with the Schreier coefficient in the full-GT mixed relation. E.181 normalizes the multiplier and that coefficient arithmetically and checks the exact relation needed for the Hatcher–Lochak–Schneps pants action. E.182 proves the mixed extension, ordinary puncture forgetting and actual full point-pushing topology. E.183 identifies the two-point elliptic branch action with the original genus-zero parameter through one explicit pure gauge; five literal braid identities, with43 defining-relation steps, were independently executed. E.184 supplies positive pointwise C3-squared fusion and the actual completed translation normalizer, retaining all48 fixed components until the determinant test removes the opposite orientation. The ordinary Dehn–Nielsen–Baer input and the Nielsen rank-two identification were opened at their exact primary-text locations. These proofs do not certify the higher-point involution quotient, CM vanishing, or the old finite compiler bound.

The finite-field point/cusp investigation records actual cover and unit tests, a small-field proof, and exploratory cubic-orbit computations. No all-prime separation theorem is inferred from the census. The attempted affine-transformation shortcut fails because a forward power map cannot be applied after forgetting additional punctures without a compatible lift. The full proof-status distinction is retained in the dedicated notes.
'''
rp.write_text(report)
ledger = root/'PROGRESS_LEDGER.md'
old = ledger.read_text()
heading = '## Fourth formal hourly review — 2026-11-18 08:45 UTC / 09:45 CET'
assert heading not in old, 'Refusing to rewrite a dated formal review'
movement_text = '; '.join(movement) if movement else 'No previously open numbered result or pending historical row changed status, and no main question was proved to reduce to a strictly smaller gate.'
entry = heading+f'''\n\nReview interval: approximately07:45–08:45 UTC. **Qualifying movement: {'yes' if movement else 'no'}; consecutive no-movement reviews: {no_movement_count}.** {movement_text} New scope obstructions, the compact-catalog reformulation, qualitative GT dependencies, finite-field experiments and packaging are not counted as movement by themselves. The comparison was executed against immutable checkpoint05, not reconstructed from memory.

### Main questions and their strongest proved gates

* A.2 remains open: a single ordinary infinite-support pair needs sections at every depth in every coefficient component. A.32 and E.185–E.187 remove proposed shortcuts or make compact finite testing precise; they establish neither a passing branch nor universal failure.
* A.3 at three remains the old-support plus-character compatibility problem in E.148/E.151. Frozen predecessors can fail. No infinite branch is established or universally excluded.
* A.3 at two remains the exact E.159 matching problem with ordinary real interval and all real frames retained. The actual Frobenius words are coupled; E.187's common-catalog nonemptiness is an additional missing assertion, not a solved replacement for that gate.
* A.3 at primes at least five remains open beyond the relative finite class-two approximation. The same pair must be retained at all weights.
* B, C and the unconditional manuscript conclusion retain their previously recorded universal gaps. Four historical GT rows remain pending even though several of their qualitative dependencies are now proved.

### Every task and lead at this review

'''
entry += report[report.index('| Task or lead |'):report.index('# SECTION_GHOSTS research report')].strip()
entry += '\n\n### Every numbered result still labelled Open\n\n| Result | Exact current statement | Location |\n|---|---|---|\n'
for r in results:
    if r['status'] == 'Open':
        statement = ' '.join(r['statement'].split()).replace('|','/')
        entry += f'| {r["id"]} | {statement} | {r["where_proved"]} |\n'
entry += '\n### Every pending historical row\n\n| Historical claim | State reached | Remaining dependency |\n|---|---|---|\n'
for r in history:
    if r['audit_status'] == 'pending':
        entry += f'| {r["historical_id"]} | {r["audit_scope"].replace("|","/")} | {r["remaining_check"].replace("|","/")} |\n'
entry += f'\nCurrent counts: {len(results)} numbered statements, {dict(rc)}; {events} check events; {len(history)} historical rows, {dict(hc)}. Next formal review: approximately09:45 UTC /10:45 CET. If that review also has no qualifying movement, the user\'s stopping rule requires the final incomplete package. Checkpoint06 identity and successful persistence are recorded only after upload.\n'
ledger.write_text(old.rstrip()+'\n\n'+entry)
print('Baseline: immutable checkpoint05')
print('Existing-row status movements:', movement)
print('Consecutive no-movement reviews:', no_movement_count)
print('Results:', len(results), dict(rc))
print('Historical:', len(history), dict(hc), 'Check events:', events)
