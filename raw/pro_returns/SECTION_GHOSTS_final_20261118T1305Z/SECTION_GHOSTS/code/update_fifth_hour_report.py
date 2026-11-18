#!/usr/bin/env python3
"""Update current state and append the third review without removing history."""
from pathlib import Path
from collections import Counter
import csv

p=Path(__file__).resolve().parents[1]
rp=p/'SECTION_GHOSTS_report.md'
report=rp.read_text()
hist=list(csv.DictReader((p/'notes/historical_audit.csv').open()))
results=list(csv.DictReader((p/'SECTION_GHOSTS_results.csv').open()))
hc=Counter(r['audit_status'] for r in hist)
rc=Counter(r['status'] for r in results)
events=len(list(csv.DictReader((p/'CHECK_EVENTS.tsv').open(),delimiter='\t')))
updates={
'A.2':('A.2; A.20–A.21; A.31; E.137–E.159; E.170–E.174','Undecided. One fixed ordinary pair must survive all classes and all coefficient primes. E.174 constructs an infinite-support ordinary pair with one all-prime class-two section matched at every off-diagonal support place, and an unrestricted global class-three lift. This is a finite-depth nonemptiness theorem, not movement on the all-depth claim. At three the restricted ordinary construction reduces to an infinite compatible branch through E.148 plus-character equations; E.149 proves that frozen nodes can fail. At two E.159 gives an exact finite-parameter matching test, retaining real stabilizers. Neither branch is established. Next: prove a branch or a uniform obstruction without changing the pair at each depth.'),
'A.3':('A.2–A.3; E.66–E.69; E.123–E.159; E.170–E.174','Undecided for every coefficient prime, including two and three. The three-primary one-step gate is the old-support plus system; E.151 preserves full ordinary arithmetic through successful steps. At two the odd-weight matching fibre, when nonempty, is a torsor under 4Z2 in each Lie coordinate, and the even-weight matching correction is unique. E.157 proves that every full pro-two survivor has the ordinary real interval class. At primes at least five E.152–E.154 prove relative finite class-two approximation, used once per prime in E.174. None constructs an all-depth section. Next: control simultaneous higher matching while retaining old valuations and full ordinary compatibility.'),
'A.4':('A.22–A.29; B.20–B.26; E.66–E.69; E.130–E.159; E.166–E.169','Exact continuous class-two/class-three tests, strict c0, and finite matching gates at two and three are proved. Dyadic global H2 is detected by real restriction plus tame residues; the real class of any full survivor is fixed. A.196 is independently reconstructed as a nonordinary cubic-field example with an invisible absolute continuous obstruction. It is not an ordinary Q counterexample. Ambient lim-one classes do not show that every ordinary ghost fails. Next: evaluate and control the compatible higher matching tests on one ordinary pair.'),
'B.1':('B.21–B.26; B.101–B.102; E.130–E.134; E.171–E.174','The original class-three remainder has exact scalar tests with one global predecessor fixed and strict c0 retained. A separate three-primary family has a nonempty closed fourth-matching remainder. E.174 gives a different all-coefficient family with support-matched class two and unrestricted class three. Neither result classifies the original A.44 all-coefficient remainder or provides a universal finite exclusion. Next: solve its later matching tests with one pair and all old primes retained.'),
'B.2':('E.35–E.38; E.60–E.83; E.118–E.139; E.160–E.169','Every specifically requested historical exclusion is now independently reconstructed, including A.196. Its fixed-S coefficient-nine obstruction is nonzero of order three, all absolute finite coefficient images vanish, and every local full quotient has a lift; the example is nonordinary over a cubic field. Harmonic class-eight and class-seventeen exclusions require actual local matching. The universal first-exclusion table for the surviving ordinary remainder remains undecided. Next: resolve that higher compatible remainder.'),
'C.3':('C.4; A.8; E.50–E.59; E.90–E.97; E.176–E.179','The compact separation lemma and LM4 negative and positive relative towers are independently proved. The marked arithmetic CM base is checked. E.176–E.179 now reconstruct qualitative finite fixed-component recognition, a common Klein centralizer source, both actual forgetting maps, and the full-GT mixed braid relation with the Schreier coefficient c2. Equality with the historical symmetrizer rho and the explicit finite compiler bound remain separate unproved dependencies. No full-GT parity theorem or universal section target is inferred. Next: close that exact coefficient comparison and audit the finite compiler.'),
'E.1':('Part E; E.160–E.179; historical audit table','All inputs used unconditionally have their stated proofs and scopes. A.196 has a complete arithmetic and actual-quotient reconstruction. The qualitative full-GT geometric repair E.176–E.179 is proved, but four broader historical GT claims remain pending. The symmetrizer/Ihara coefficient comparison and the specified finite compiler are not silently imported. Next: settle these exact dependencies, keeping arithmetic-subgroup and full-GT claims separate.'),
'E.2':('E.2; E.43; E.160–E.169; code/check_E2_coverage.py','Proved for the exact explicitly enumerated task: all sixteen SECTIONS_OVER_Q items and all fifty GT_TOWER_CHECK C.1.1–C.3.11 items have confirmed rows and complete proofs. A.196 was the final pending member. Exact coverage was executed and passed. Across the broader 90-row register there are 84 confirmed, 2 repaired and 4 pending rows. Those four additional GT claims belong to E.1 and L.5; completion of E.2 does not complete the overall task.'),
'L.1':('A.2; E.137–E.159; E.170–E.174','The full pronilpotent finite-support assertion is undecided. The restricted three-primary construction has an exact one-step plus gate, and the dyadic matching criterion is explicit. E.174 proves that the all-prime class-two necessary locus is nonempty for infinite support; this finite-depth fact is not an all-depth advance. Next: establish or exclude a coherent infinite branch and address every coefficient prime on the same ordinary pair.'),
'L.4':('A.23–A.24; B.23–B.26; E.66; E.155–E.159; E.166–E.169','Invisible continuous classes exist, with A.196 fully reconstructed in its nonordinary cubic-field scope. For boundary-matched predecessors the fixed-ramification obstruction at three vanishes; at two only real restriction remains, and an actual ordinary real match removes it. Preserving all support matches is a separate first-cohomology condition. No universal nonzero first obstruction is proved. Next: determine the higher matching obstruction for every candidate in the surviving ordinary locus.'),
'L.5':('C.1–C.5; C.7–C.8; A.8; E.50–E.59; E.90–E.97; E.176–E.179','The compact and LM4 comparisons are proved in their precise scopes. The new qualitative Klein geometry establishes the mixed braid identity for full GT with the exact Schreier coefficient. It does not identify that coefficient with the symmetrizer extension used by the historical CM discrepancy, and does not verify the explicit compiler bound. No universal section-side rigid target follows. Next: resolve that coefficient comparison and the finite construction, then prove the necessary transfer to sections.')}
lines=[]
for line in report.splitlines():
    if line.startswith('| '):
        key=line.split('|')[1].strip()
        if key in updates:
            refs,state=updates[key];line=f'| {key} | {refs} | {state} |'
    lines.append(line)
report='\n'.join(lines)+'\n'
marker='## Fifth work period: completed explicit audit and exact dyadic matching'
assert marker not in report, 'Refusing to rewrite a dated work period'
report+='''
## Fifth work period: completed explicit audit and exact dyadic matching

The historical A.196 audit is complete. E.166–E.169 rebuild its cubic field, actual semidirect quotient, global Kummer and cup certificate, all norm towers and local lifts. The coefficient-nine obstruction is nonzero of order three in the fixed-ramification group, whereas all absolute finite-coefficient images vanish. The full local towers and finite global solutions do not form a compatible global full tower. The pair fails ordinary local realizability at three and is over a cubic field; neither main question over Q is answered by this example. Root and independent readers checked the complete proofs, including exact primary-source norm and cohomology hypotheses, and reran the finite certificate. Task E.2 is now Proved: its exact sixty-six claims all have complete proof references and confirmed audit rows. The four additional GT dependencies remain pending.

E.155–E.159 complete the two-primary arithmetic and matching calculations used here. Finite-ramification second cohomology has only the real obstruction and explicit tame terms. The actual real pro-two extension is the free product of three order-two groups, with exactly the three ordinary interval section classes; the proof uses the exact pro-two theorem on an erasable reflected graph. For the stated support pattern, every odd-weight matching problem reduces to a finite joint image C2 times C4, with kernel 4Z2 in each Lie coordinate. Even-weight matching is a unique finite correction when it exists. The possible real stabilizer boundary is retained, so an apparent need to choose a unique real frame is not introduced. These are exact finite-step conditions; an infinite passing branch is still absent.

E.152–E.154 prove the relative class-two approximation input at primes at least five. E.170 handles the marked dyadic radical intersection using the actual cyclotomic action and an eighth-root mark. E.171–E.174 apply each large coefficient-prime repair once, preserving prior finite data while all later exponents become divisible by each fixed integer. They construct one full ordinary infinite-support pair with a global integral class-two section matched at every off-diagonal support point, simultaneously for every coefficient prime, and an unrestricted global class-three lift. The construction is different from A.44. It does not assert point matching in class three, local point matching at the coefficient place, or a full pro-prime or pronilpotent section. As another finite-depth survival statement it is explicitly excluded from the progress review's qualifying movement.

E.176–E.179 repair a qualitative full-GT geometric dependency. Complete Tate complexes and characteristic finite covers give fixed-component recognition and simultaneous finite fusion without assuming a finite cell decomposition. The two labelled Klein components and the permitted half twist produce one corrected source action. Two actual coloured forgetting maps have the required common-source cusp-swap relation, yielding the mixed braid identity with its integral Schreier coefficient and central braid factor. The exact label, coordinate and Schreier certificate was executed and independently rerun. The historical symmetrizer coefficient is not silently equated with the Ihara coefficient: the opened Nakamura–Schneps Proposition5.3 requires III-prime. The explicit historical finite compiler and all four pending historical GT rows are not certified by these qualitative results.

No all-depth branch or universal finite-support theorem is asserted. The detailed task table and dated ledger preserve the remaining gates and failed routes. Full independent reviews and finite computations are recorded separately from source checks and coverage checks.
'''
rp.write_text(report)
ledger=p/'PROGRESS_LEDGER.md';old=ledger.read_text()
marker='## Third formal hourly review — 2026-11-18 07:45 UTC / 08:45 CET'
assert marker not in old, 'Refusing to rewrite a dated formal review'
table=report[report.index('| Task or lead |'):report.index('# SECTION_GHOSTS research report')].strip()
new=marker+'''

Review interval: approximately06:45–07:45 UTC. **Qualifying movement: yes; consecutive no-movement reviews: zero.** The existing historical row SECTIONS_OVER_Q A.196 changed from pending to confirmed after complete arithmetic and quotient proofs and independent checks. This closes the last required member of task E.2, whose numbered result changed from Open to Proved. Exact coverage of all sixty-six required claims was executed. The new all-prime class-two survivor, added pages and packaging are not counted as movement.

### Main questions and their strongest proved gates

* A.2 remains open: one ordinary infinite-support pair must have compatible sections at every depth in every coefficient component. The fixed-pair compactness theorem does not give a compact space of varying ghosts. E.174 proves only that the necessary all-prime class-two support-matching locus is nonempty.
* A.3 at three remains open: an infinite compatible branch through the finite old-support plus-character equations in the E.151 ordinary construction would suffice. Individual frozen predecessors can fail. No such branch or universal failure is proved.
* A.3 at two remains open: every full survivor has its ordinary real interval class; the exact finite matching test in E.159 then retains all real frames. It gives no passing infinite branch. The odd step has a 4Z2 correction kernel and the even step at most one correction in each Lie coordinate.
* A.3 at primes at least five remains open: finite relative class-two approximation is proved, but no higher-weight iteration preserving all actual old support matches is proved.
* B.1–B.3 remain open in their universal scopes. All explicitly requested historical exclusions have now been reconstructed. Their quotient, coefficient, field and local-matching qualifications remain essential.
* C and L.5 retain the universal rigid-target gap. The new qualitative full-GT mixed relation leaves the symmetrizer coefficient comparison and explicit compiler as separate dependencies. D has only conditional consequences.

### Every task and lead at this review

'''+table+'\n\n### Every numbered result still labelled Open\n\n| Result | Exact current statement | Location |\n|---|---|---|\n'
for r in results:
    if r['status']=='Open':
        s=' '.join(r['statement'].split()).replace('|','/')
        new+=f'| {r["id"]} | {s} | {r["where_proved"]} |\n'
new+='\n### Every pending historical row\n\n| Historical claim | State reached | Remaining dependency |\n|---|---|---|\n'
for r in hist:
    if r['audit_status']=='pending':
        new+=f'| {r["historical_id"]} | {r["audit_scope"].replace("|","/")} | {r["remaining_check"].replace("|","/")} |\n'
new+=f'\nCurrent counts: {len(results)} numbered statements, {dict(rc)}; {events} check events; {len(hist)} historical rows, {dict(hc)}. Next formal review: approximately08:45 UTC /09:45 CET. Checkpoint05 identity and save success are recorded only after upload.\n'
ledger.write_text(old.rstrip()+'\n\n'+new)
print('Recorded third formal review: movement yes; consecutive no-movement count0.')
print('Historical:',dict(hc),'Results:',dict(rc),'Events:',events)
