#!/usr/bin/env python3
"""Record review five against immutable checkpoint06, without counting side results."""
from pathlib import Path
from collections import Counter
import csv, datetime, io, zipfile

root = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc)
assert now >= datetime.datetime(2026, 11, 18, 9, 44, 30, tzinfo=datetime.timezone.utc)
results = list(csv.DictReader((root/'SECTION_GHOSTS_results.csv').open()))
history = list(csv.DictReader((root/'notes/historical_audit.csv').open()))
events = len(list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(), delimiter='\t')))
with zipfile.ZipFile(root.parent/'SECTION_GHOSTS_checkpoint_06.zip') as z:
    old_results = list(csv.DictReader(io.StringIO(z.read('SECTION_GHOSTS/SECTION_GHOSTS_results.csv').decode())))
    old_history = list(csv.DictReader(io.StringIO(z.read('SECTION_GHOSTS/notes/historical_audit.csv').decode())))
old_r = {r['id']: r for r in old_results}
old_h = {r['historical_id']: r for r in old_history}
movement = [f"{r['id']}: Open to {r['status']}" for r in results
            if r['id'] in old_r and old_r[r['id']]['status']=='Open' and r['status']!='Open']
movement += [f"{r['historical_id']}: pending to {r['audit_status']}" for r in history
             if r['historical_id'] in old_h and old_h[r['historical_id']]['audit_status']=='pending'
             and r['audit_status']!='pending']
assert len(movement) >= 3, 'Expected independently checked historical closures are missing'
no_movement_count = 0 if movement else 2
rc, hc = Counter(r['status'] for r in results), Counter(r['audit_status'] for r in history)
updates = {
 'P.1': ('P.1–P.14; A.22–A.24', 'The requested literature comparisons use opened primary sources and exact coefficient hypotheses. P.14 checks the 2023 twisted Massey theorem and the 2026 strong vanishing theorem, including the latter authors\' explicit projective-limit limitation. Neither existential finite defining systems nor modulus-dependent auxiliary primes gives the retained integral ordinary section. No priority claim is made.'),
 'P.1.1': ('P.1–P.4; P.14', 'Nilpotent, Massey and nongeometric pro-p results are checked. Published nonordinary examples do not answer the ordinary limit question. The rank-one twisted finite Massey comparison is explicit; preserving one actual predecessor and the integral ordinary ramification remains additional.'),
 'A.2': ('A.2; A.20–A.21; A.31–A.33; E.137–E.159; E.174; E.185–E.200', 'Undecided. One fixed ordinary infinite-support pair must survive every class and coefficient prime. A.33 proves density zero for the support of every ordinary pair, not finite support. E.192–E.194 give actual finite point/cusp detectors. E.200 forces infinitely ramified elliptic-family representations, at least two absolutely irreducible, from a putative pro-three ghost section; no finite-conductor or Hodge hypothesis follows. These necessary conditions leave the all-depth gate unresolved. Next: establish one compatible branch or a uniform obstruction while retaining the same pair.'),
 'A.3': ('A.3; E.148–E.159; E.185–E.187; E.192–E.200', 'Undecided for every coefficient prime. At three, the old-support plus-character equations have neither an infinite branch nor a universal failure theorem. At two, the exact matching test retains real frames and coupled arithmetic Frobenius words; no common compact valuation catalog is known to pass every test. At primes at least five, the necessary higher conditions have not been iterated through all weights. Finite elliptic detectors and density zero do not prove finite support.'),
 'B.1': ('B.21–B.26; B.101–B.102; E.171–E.174; E.199; E.202', 'The original class-three remainder remains undecided. With the original factorial exponents and minimal five-adic prime shells, E.202 reduces the first two five-primary tests, over all continuations of fixed legal q0,r0, to one explicit 2-by-2 affine system over F5. Its matrix is expressed in quintic residue logarithms and its obstruction coset is defined by a finite Heisenberg cochain over {2,3,5,q0,r0,infinity}. Later choices cannot repair inconsistency. No legal pair with a consistent system, all later divisibilities, or strict c0 decay is proved. Next: decide this finite obstruction and the remaining compatible tests.'),
 'C.3': ('C.4; A.8; E.50–E.59; E.90–E.97; E.176–E.198; E.201', 'The full-GT geometry and signed CM comparison are proved. E.191 gives CM-character vanishing, E.195 compact finite pentagon separation, and E.197–E.198 both strict inclusions GT < ker Delta < GT0 with an actual full profinite witness. E.201 recovers the exact original identity-relative-action CM family. The literal numerical compiler A4.57 remains pending. No map transporting this obstruction to every ordinary section ghost is established.'),
 'E.1': ('Part E; historical audit table; E.188–E.202', 'The broader 90-row register has 87 confirmed, 2 repaired and 1 pending claim. The sole pending row is GT_TOWER_CHECK A.4.57, whose specified numerical construction depends on absent bound recursions and finite inputs. Qualitative finite separation does not certify that literal bound. C.5, A.4.1 and A.7 now have complete replacement proofs and independent checks. No unverified compiler is used as a section premise.'),
 'E.2': ('E.2; E.43; E.160–E.169; code/check_E2_coverage.py', 'Proved for all 66 explicitly enumerated claims: sixteen SECTIONS_OVER_Q and fifty GT_TOWER_CHECK Part C statements. The scope of each quotient and local condition is retained. The broader register now has 87 confirmed, 2 repaired and 1 pending row; A4.57 is outside the exact E.2 list. This does not complete the overall task.'),
 'L.5': ('C.1–C.8; A.8; E.50–E.59; E.90–E.97; E.176–E.198; E.201', 'The automorphism-side CM obstruction, same-parameter covariance, compact finite separation and strict GT/kernel comparison are now proved, including the exact original relative family. The requested universal theorem joining these to all ordinary section ghosts remains absent; no comparison map with the needed transfer property is constructed. The finite numerical compiler A4.57 is also pending. Section compactness still requires a fixed pair or a specified common valuation catalog whose finite-test nonemptiness has not been proved.')
}
rp=root/'SECTION_GHOSTS_report.md'
report=rp.read_text()
marker='## Seventh work period: exact CM closure and finite arithmetic gates'
assert marker not in report, 'Refusing to rewrite a dated work period'
lines=[]
for line in report.splitlines():
    if line.startswith('| '):
        key=line.split('|')[1].strip()
        if key in updates:
            refs,state=updates[key];line=f'| {key} | {refs} | {state} |'
    lines.append(line)
report='\n'.join(lines)+'\n'
report+='\n'+marker+'''

The historical claims GT_TOWER_CHECK A.4.1, A.7 and C.5 changed from pending to confirmed. E.188–E.189 retain the actual higher-point involution centralizer, the induced profinite topology and one common GT parameter. E.190 gives a single CM covariance conjugator with the ordered-pole signs retained; E.191 proves the character vanishes on full GT. E.195 then proves qualitative finite separation by compactness. E.197–E.198 construct an actual full gentle element whose degree-seven pentagon is nonzero, and then a parity-zero witness, proving both strict inclusions. The explicit braid, matrix, Lie and cyclic sphere-pentagon computations have saved programs and outputs and independent reads. None of these proofs is a certification of the enormous literal A4.57 compiler.

E.196 remains a correct changed-relative-family witness. It was not silently replaced: E.201 supplies the stronger, separate recovery of the original LM7 identity action on every relative prime factor, with a dyadic frame obtained by coprime centralizer lifting and the full ordinary lift retaining those frames. It gives the original signed matrices T=5I and W=I, complete rho=0 and Delta=1. The finite joint quotient of order1728 was independently enumerated. This closes the specific historical C.5 family gap; its originally open universal section-target clause remains open. The checkpoint06 unintegrated E.188–E.189 drafts are now integrated after full proof review, as this dated update records.

A.33 proves the support of every ordinary completed pair has upper relative prime density zero. One nonzero ordinary valuation gives full finite affine Kummer quotients; a fixed-N Chebotarev argument gives the bound phi(N)/N, and varying squarefree N proves density zero. No uniform-in-N counting estimate is used, and no finite-support conclusion is inferred.

E.192–E.194 prove finite-field interior/cusp separation by actual elliptic monodromy, including characteristic two and the corresponding coefficient-two detector. This resolves the separation question left open in the sixth-period notes. The local consequence preserves the actual reduction point and cusp label, and explains why a fixed good-reduction reference cannot remain unchanged through cofinal finite quotients after an ordinary nonzero valuation is introduced. E.200 derives infinitely ramified coefficient-three representations from a putative full pro-three ghost section, with at least two absolutely irreducible. The necessary de Rham, finite-conductor and cross-coefficient compatibility assumptions for further geometric conclusions are not supplied by ordinary abelian localizations.

E.199 preserves the original factorial exponents and makes the first coefficient-five denominator explicit. E.202 proves a two-by-two F5 criterion with twenty-five realizable root parameters, and then proves that these exhaust every original continuation for the same legal first prime pair. Its Kummer matrix uses Q(zeta5), class number one, and specified Frobenius lifts; its constant class is defined using a finite Heisenberg cochain over the first finite ramification set. Later root choices cannot repair an inconsistent system. No actual legal numerical pair or consistency result is asserted; later divisibility and strict c0 convergence remain necessary.

P.14 checks the finite twisted Massey theorem and the 2026 strong vanishing theorem against the exact arithmetic source, coefficients and quantifiers. The latter paper explicitly disclaims the relevant integral projective limit after its Theorem4.2. The current work also proves directly why auxiliary finite higher-weight tame ramification cannot be inserted unchanged into an integral correction. This literature audit is not counted as main-question movement.
'''
rp.write_text(report)
lp=root/'PROGRESS_LEDGER.md';old=lp.read_text()
heading='## Fifth formal hourly review — 2026-11-18 09:45 UTC / 10:45 CET'
assert heading not in old, 'Refusing to rewrite a dated review'
entry=heading+f'''

Review interval: approximately08:45–09:45 UTC. **Qualifying movement: yes; consecutive no-movement reviews:0.** {('; '.join(movement))}. Comparison used immutable checkpoint06. Added finite detectors, density zero, the first five-primary gate and additional literature are not counted as movement by themselves. No main full-pronilpotent or full-pro-prime finite-support question is declared solved.

### Strongest main gates

* A.2 still requires one fixed ordinary infinite-support pair with every integral-class section, equivalently every full pro-prime section. No such pair is constructed and finite support is not proved.
* A.3 at three remains the all-weight old-support matching problem; at two the actual coupled Frobenius and real matching problem remains. At every larger prime the compatible higher-weight construction or exclusion remains missing.
* B.1 now has an explicit finite first-five obstruction for each original legal q0,r0, but its consistency and every later strict condition are unresolved. This does not classify all ordinary ghosts.
* The automorphism-side C.3/L5 historical CM conclusions are proved, while a universal section-side comparison and the A4.57 literal compiler remain absent.

### Every task and lead at this review

'''
entry+=report[report.index('| Task or lead |'):report.index('# SECTION_GHOSTS research report')].strip()
entry+='\n\n### Every numbered result still labelled Open\n\n| Result | Exact current statement | Location |\n|---|---|---|\n'
for r in results:
    if r['status']=='Open':
        entry+=f"| {r['id']} | {' '.join(r['statement'].split()).replace('|','/')} | {r['where_proved']} |\n"
entry+='\n### Every pending historical row\n\n| Historical claim | State reached | Remaining dependency |\n|---|---|---|\n'
for r in history:
    if r['audit_status']=='pending':
        entry+=f"| {r['historical_id']} | {r['audit_scope'].replace('|','/')} | {r['remaining_check'].replace('|','/')} |\n"
entry+=f'\nCurrent counts: {len(results)} numbered statements, {dict(rc)}; {events} check events; {len(history)} historical rows, {dict(hc)}. Next review: approximately10:45 UTC /11:45 CET. Checkpoint07 save identity will be recorded only after successful upload.\n'
lp.write_text(old.rstrip()+'\n\n'+entry)
print('Baseline: immutable checkpoint06')
print('Existing-row status movements:',movement)
print('Consecutive no-movement reviews:',no_movement_count)
print('Results:',len(results),dict(rc))
print('Historical:',len(history),dict(hc),'Check events:',events)
