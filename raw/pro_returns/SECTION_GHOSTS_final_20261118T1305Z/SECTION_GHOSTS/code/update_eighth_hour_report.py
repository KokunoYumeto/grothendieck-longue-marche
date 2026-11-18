#!/usr/bin/env python3
"""Record review six against immutable checkpoint07, preserving dated reviews."""
from pathlib import Path
from collections import Counter
import csv, datetime, io, zipfile

root=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime(2026,11,18,10,44,30,tzinfo=datetime.timezone.utc)
results=list(csv.DictReader((root/'SECTION_GHOSTS_results.csv').open()))
history=list(csv.DictReader((root/'notes/historical_audit.csv').open()))
checks=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
by_id={r['id']:r for r in results}
with zipfile.ZipFile(root.parent/'SECTION_GHOSTS_checkpoint_07.zip') as z:
    old_results=list(csv.DictReader(io.StringIO(z.read('SECTION_GHOSTS/SECTION_GHOSTS_results.csv').decode())))
    old_history=list(csv.DictReader(io.StringIO(z.read('SECTION_GHOSTS/notes/historical_audit.csv').decode())))
old_r={r['id']:r for r in old_results};old_h={r['historical_id']:r for r in old_history}
row_moves=[f"{r['id']}: Open to {r['status']}" for r in results if r['id'] in old_r and old_r[r['id']]['status']=='Open' and r['status']!='Open']
row_moves += [f"{r['historical_id']}: pending to {r['audit_status']}" for r in history if r['historical_id'] in old_h and old_h[r['historical_id']]['audit_status']=='pending' and r['audit_status']!='pending']
assert all(by_id.get(s,{}).get('status')=='Proved' for s in ['E.209','E.210'])
assert 'E.209' not in old_r
assert 'E.209' in by_id['A.2']['statement']
strict_reduction='E.209 removes the previously retained fixed-ramification H2 obstruction in every weight for each odd ell with ell not dividing h(Q(zeta_ell)), including five. E.210 computes the remaining exact integral H1 correction groups and local images. The main single-prime induction is thereby strictly reduced to simultaneous support matching at those primes.'
movement=True
no_movement_count=0
has212=by_id.get('E.212',{}).get('status')=='Proved'
has213=by_id.get('E.213',{}).get('status')=='Proved'
hasp15=by_id.get('P.15',{}).get('status')=='Proved'
two_place=(' E.212 shows that failure of the next matching step above one fixed predecessor is witnessed by at most two support places; this does not bound their sizes or decide consistency.' if has212 else '')
five=('E.213 proves that legal first pairs with an invertible first matrix exist by choosing two alternative first primes and a common second prime. E.211 then constructs an unchanged original factorial continuation matching every coefficient-five class-two support point, and E.205 gives its continuous class-three survival. The all-coefficient class-three remainder and all higher matching remain undecided.' if has213 else 'E.205 and E.211 prove that consistency of E.202\'s first finite system is sufficient for an original continuation with every coefficient-five class-two support match and continuous class-three survival. E.206 identifies its exact dual obstruction; E.208 gives a sufficient quintic first-prime condition. Existence of a legal consistent first pair remains undecided.')
if has213:
    five+=' Its epsilon-unit refinement makes each individual next weight-three support equation solvable; the remaining condition is pairwise agreement of the two-vector residues, with at most one global correcting vector.'
updates={
 'P.1':('P.1–P.'+('15' if hasp15 else '14')+'; A.22–A.24','Opened primary sources and exact comparison maps cover the requested nilpotent, pro-prime, unipotent and continuous-cohomology literature. Finite Massey vanishing does not retain the actual predecessor. '+('P.15 checks three regular-prime embedding routes and gives an explicit nonzero restricted-ramification approximation group despite fixed-S H2 vanishing. These theorem hypotheses do not supply the ordinary matching tuple.' if hasp15 else 'The integral matching condition remains separate.')),
 'P.1.1':('P.1–P.4; P.14'+('; P.15' if hasp15 else ''),'The ordinary full-tower comparison remains outside the opened nongeometric and finite embedding theorems. Their source groups, cyclotomic quotients, allowed ramification and local prescriptions are retained explicitly. No theorem with different local hypotheses is applied to an ordinary ghost.'),
 'A.2':('A.2; A.20–A.21; A.31–A.33; E.148–E.159; E.174; E.185–E.210','Undecided. The same ordinary pair must survive all integral classes and all coefficient primes. The all-weight fixed-ramification obstruction now vanishes for regular odd coefficients, including five; only their simultaneous support-matching step remains.'+two_place+' Neither density zero, finite elliptic detectors nor a fixed-depth survivor proves finite support. Next: prove or exclude one compatible infinite branch while keeping the same ordinary pair.'),
 'A.3':('A.3; E.148–E.159; E.185–E.187; E.209–E.210'+('; E.212' if has212 else ''),'Undecided at every coefficient prime. For each odd ell with ell not dividing h(Q(zeta_ell)), E.209 eliminates fixed-S H2 at every weight, and E.210 gives the exact global H1 correction modules: free rank one in odd weights, explicit cyclic torsion in weights divisible by ell minus one, zero in the other even weights.'+two_place+' At two, coupled Frobenius and real matching remain; irregular odd coefficients retain their fixed-S gate. No infinite branch or universal failure theorem is proved.'),
 'A.4':('A.22–A.29; B.20–B.26; E.66–E.69; E.155–E.169; E.209–E.210'+('; E.212' if has212 else ''),'Continuous class-two/class-three residues and strict c0 are explicit. Regular odd coefficients now have an exact all-weight matching-only induction; the two-primary real restriction and coupled Frobenius conditions remain explicit. Invisible continuous classes do not prove nonvanishing for an ordinary ghost.'+two_place+' Next: evaluate the actual higher discrepancies along a retained ordinary pair.'),
 'B.1':('B.21–B.26; B.101–B.102; E.199; E.202; E.205–E.208; E.211'+('; E.213' if has213 else ''),five+' The matrix criterion classifies the first finite gate for each fixed legal pair; it does not classify all ordinary ghosts or give a bound on their first failure. Next: combine coefficient components and solve the actual higher support-matching tests.'),
 'C.3':('C.4; A.8; E.188–E.198; E.201; E.203–E.204; E.207','The full-GT CM comparison, strict kernel inclusions and original relative CM family are proved. The compact quaternion detector, its actual ordinary outer image, ordered-pole target and faithful homology map are now independently reconstructed with exact finite certificates. The literal A4.57 compiler remains pending, and no universal comparison transfers this automorphism obstruction to every ordinary section ghost.'),
 'E.1':('Part E; historical audit table; E.188–E.207','The broader register remains 90 rows:87 confirmed,2 repaired,1 pending. E.203–E.204 and E.207 reconstruct the recoverable quaternion finite inputs. The sole pending claim A4.57 still requires the literal finite branch-parameter compiler and its absent bound recursions. Qualitative compact separation and completed automorphism classification do not prove those numerical bounds. No missing proof is treated as a counterexample.'),
 'L.1':('A.2; E.148–E.159; E.174; E.209–E.210'+('; E.212' if has212 else ''),'The full-pronilpotent finite-support assertion remains undecided. Regular coefficients now have no fixed-S second obstruction at any depth, but the separate support-matching equations remain.'+two_place+' Existence of one fixed ordinary pair passing these equations in all weights is not proved. Finite-depth nonemptiness is not counted as a main-question solution.'),
 'L.4':('A.23–A.24; B.23–B.26; E.155–E.169; E.209–E.210','The existence of invisible continuous classes remains distinct from evaluating a ghost\'s obstruction. For a predecessor already matching every support point away from a regular odd coefficient prime, every fixed-S obstruction vanishes in every weight. Preserving matching is still a global H1 localization problem. The nonordinary cubic example does not yield a universal ordinary failure theorem.'),
 'L.5':('C.1–C.8; A.8; E.188–E.198; E.201; E.203–E.204; E.207','The actual automorphism-side geometry, common CM conjugator and finite quaternion inputs are reconstructed. A universal rigid-object statement covering ordinary section ghosts still lacks its comparison map and transfer proof. The exact finite numerical compiler A4.57 also remains pending. Fixed-pair compactness is valid; nonemptiness of all tests in a common changing-pair catalog is not proved.')
}
rp=root/'SECTION_GHOSTS_report.md';report=rp.read_text()
marker='## Eighth work period: regular coefficients and the original five-primary gate'
assert marker not in report,'Refusing to rewrite a dated work period'
lines=[]
for line in report.splitlines():
    if line.startswith('| '):
        key=line.split('|')[1].strip()
        if key in updates:
            refs,state=updates[key];line=f'| {key} | {refs} | {state} |'
    lines.append(line)
report='\n'.join(lines)+'\n\n'+marker+'\n\n'
report+=strict_reduction+' This is an all-weight reduction of a main gate, not another finite-level survivor. Two independent readers checked both full proofs and the exact primary sources. The local integral comparison explicitly retains the exceptional finite-local dimension-two case. No full pronilpotent or full pro-prime finite-support question is decided.\n\n'
if has212:report+='E.212 further makes the matching failure test exact: for a fixed predecessor and a chosen global lift, each odd-weight local constraint is an empty set or a coset of ell^k Z_ell^{b_w}. Intersecting such nonempty cosets makes them nested, so a failure is witnessed by one or two support places. The even-weight parameter groups give the same bound, or one place when the correction group is zero. This does not supply an effective bound on the witness primes or automatically solve any pair of constraints.\n\n'
report+=five+' E.206 supplies the finite Poitou–Tate dual and its adjusted Kummer basis; E.208 isolates the conjugate-prime quintic residue in a sufficient one-first-prime route. '
if has213:report+='The two-first-prime construction bypasses the need for a spin-distribution theorem; it does not prove that E.208\'s particular zero-diagonal condition occurs. '
report+='The exploratory 280-prime computation remains explicitly nonlegal for the original recursion. Its small prime2281 is below the original cutoff and is not used as a constructed example.\n\n'
report+='E.203–E.204 reconstruct the actual compact quaternion quotient, of order32 times3^14, its ordinary outer image of order93312, and the ordered-pole image of order13436928. Complete surface-word, Cayley–Schreier, inner-coboundary and centralizer certificates were read and independently rerun with matching hashes. E.207 constructs the actual rank73 cover homology: theta has rank12, the involution eigenspaces have dimensions37 and36, and the faithful kernel is precisely the augmentation-square image of dimension24. Its independent rerun matches the recorded digest. These statements complete the recoverable finite input, while the literal BCV/HCF/KFU compiler bounds remain pending. No extra root execution is claimed for E.207; root performed a complete proof/code read and the peer performed the independent rerun.\n\n'
if hasp15:report+='P.15 checks Schmidt\'s relative free-product theorem, the roots-of-unity condition in Jarden–Ramiharimanana, and Liu\'s separate approximation group. For A=F5(3), S={5,infinity}, T={11,31}, the dual of that approximation group has dimension at least one: its source has dimension two and its local target at five has dimension one. This is a checked obstruction to silently equating two theorem hypotheses; it is not identified with a point-section discrepancy.\n\n'
report+='The checkpoint07 draft note has a dated resolution. No earlier checkpoint or dated review was rewritten. A single LaTeX tag placement in E.210 was corrected before the clean rebuild; final overflow and visual-inspection counts are recorded below after the current PDF is checked.\n'
rp.write_text(report)
lp=root/'PROGRESS_LEDGER.md';old=lp.read_text()
heading='## Sixth formal hourly review — 2026-11-18 10:45 UTC / 11:45 CET'
assert heading not in old,'Refusing to rewrite a dated review'
entry=heading+'\n\nReview interval: approximately09:45–10:45 UTC. **Qualifying movement: yes; consecutive no-movement reviews:0.** Comparison of existing result and historical rows used immutable checkpoint07. Existing-row status changes: '+('; '.join(row_moves) if row_moves else 'none')+'. '+strict_reduction+' The finite-depth five-primary construction, extra quaternion inputs, computations, pages and packaging are not counted as movement by themselves.\n\n### Strongest main gates\n\n'
entry+='* A.2 remains the same-pair all-coefficient infinite-tower question, with neither finite support proved nor a full ghost constructed.\n* A.3 at regular odd coefficients now has only the actual simultaneous H1 support-matching step; at two the coupled Frobenius and real conditions remain; irregular odd coefficients retain their fixed-S H2 gate.\n* '+five+'\n* The compiler A4.57 remains the sole pending historical row; no universal section-side rigid target or cover-wise countersign is proved.\n\n### Every task and lead at this review\n\n'
entry+=report[report.index('| Task or lead |'):report.index('# SECTION_GHOSTS research report')].strip()
entry+='\n\n### Every numbered result still labelled Open\n\n| Result | Exact current statement | Location |\n|---|---|---|\n'
for r in results:
    if r['status']=='Open':entry+=f"| {r['id']} | {' '.join(r['statement'].split()).replace('|','/')} | {r['where_proved']} |\n"
entry+='\n### Every pending historical row\n\n| Historical claim | State reached | Remaining dependency |\n|---|---|---|\n'
for r in history:
    if r['audit_status']=='pending':entry+=f"| {r['historical_id']} | {r['audit_scope'].replace('|','/')} | {r['remaining_check'].replace('|','/')} |\n"
rc=Counter(r['status'] for r in results);hc=Counter(r['audit_status'] for r in history)
entry+=f'\nCurrent counts:{len(results)} numbered statements,{dict(rc)};{len(checks)} check events;{len(history)} historical rows,{dict(hc)}. Next formal review:approximately11:45 UTC /12:45 CET. Checkpoint08 save identity is recorded only after successful upload.\n'
lp.write_text(old.rstrip()+'\n\n'+entry)
print('Baseline: immutable checkpoint07')
print('Existing-row status changes:',row_moves)
print('Strict main-gate reduction:',strict_reduction)
print('Consecutive no-movement reviews:',no_movement_count)
print('Results:',len(results),dict(rc))
print('Historical:',len(history),dict(hc),'Check events:',len(checks))
