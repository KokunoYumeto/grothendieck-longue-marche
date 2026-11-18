#!/usr/bin/env python3
"""Record the second formal review, preserving all earlier dated reports."""
from pathlib import Path
from collections import Counter
import csv
import re

p = Path(__file__).resolve().parents[1]
rp = p / 'SECTION_GHOSTS_report.md'
report = rp.read_text()
hist = list(csv.DictReader((p / 'notes/historical_audit.csv').open()))
results = list(csv.DictReader((p / 'SECTION_GHOSTS_results.csv').open()))
hc = Counter(r['audit_status'] for r in hist)
rc = Counter(r['status'] for r in results)
events = len(list(csv.DictReader((p / 'CHECK_EVENTS.tsv').open(), delimiter='\t')))
updates = {
 'A.2': ('A.2; A.20–A.21; A.31; E.137–E.139; E.144–E.151', 'Undecided. Full survival implies every off-diagonal support-point match; the all-prime class-two gate pins at most one of the 24 classes. For the specified pro-three support pattern, E.146–E.148 make the unchanged-support quotient test necessary and sufficient for one finite ordinary extension. E.151 preserves the full ordinary completed pair through that same finite step. Thus an actual infinite path in these explicit finite plus-character equations would give a full ordinary ghost with one pro-three section. No such path, no section at every other coefficient prime, and no universal finite-support implication are proved. E.149 refutes automatic extension of frozen predecessors. Next: prove or obstruct an infinite compatible path, allowing earlier choices to change before they are frozen.'),
 'A.3': ('A.2–A.3; E.66–E.69; E.123–E.151', 'Undecided for 2, 3 and every prime at least 5. At three the remaining constructive gate is an actual infinite branch through the old-support plus equations of E.148, with full ordinary compatibility supplied by E.151. This is a sufficient construction route in a restricted support pattern, not an equivalence with every possible counterexample. Finite Frobenius freedom, H2 vanishing and new ramification cannot repair a failed frozen quotient; E.149 gives an exact failure. E.150 refutes a general finite-field interior-point separation premise, but does not identify an interior point with a cusp. Next: solve the branch problem at three and establish ordinary-compatible relative approximation at other coefficients.'),
 'A.4': ('A.22–A.29; B.20–B.26; E.66–E.69; E.130–E.151', 'Exact continuous class-two and class-three tests and strict c0 are proved. The pro-three finite continuation obstruction is now a necessary-and-sufficient system of plus-character Frobenius equations for the restricted construction, retaining every aligning frame. E.149 gives a genuinely failed finite predecessor, and E.139 gives a nonzero relative Bloch class; neither evaluates every higher obstruction of every original A.44 ghost. Ambient lim-one classes alone do not imply nonvanishing. Next: determine the compatible all-depth solutions or show that every branch eventually fails.'),
 'B.2': ('E.35–E.38; E.60–E.65; E.70–E.83; E.118–E.139; E.160–E.165', 'The selected original exclusions, the same-pair A.207/A.209 class-four claim, and both harmonic A.137/A.139 exclusions are independently reconstructed. The harmonic detectors have exact classes 8 and 17, and their exclusions require actual local section matching. They are not unrestricted class-8 or class-17 failures. A.196 remains pending beyond its complete local nonordinary scope check; the universal first-exclusion table for surviving closed remainders is also undecided. Next: reconstruct the missing specific A.196 global arithmetic certificate and resolve the higher matching remainder.'),
 'E.1': ('A.20–A.31; B.20–B.26; Part E', 'All historical claims used unconditionally are supported in their stated scopes. E.160–E.165 now replace the unavailable harmonic initialization by a complete new proof and verify both exact finite detectors, including the class-17 certificate. R8 remains repaired with the ordinary/nonordinary distinction explicit. The remaining A.196 and full-GT configuration dependencies are pending and not imported as authorities. Next: reconstruct those precise arithmetic and geometric steps or identify their errors.'),
 'E.2': ('notes/historical_audit.csv; E.160–E.165; Part E audit table', f'The complete demanded list has a row. There are {len(hist)} historical rows: {hc["confirmed"]} confirmed, {hc["repaired"]} repaired, {hc.get("refuted",0)} refuted and {hc["pending"]} pending. A.137 and A.139 changed from pending to confirmed through replacement proofs of their missing dependencies and independent finite certificates. Remaining: SECTIONS_OVER_Q A.196; GT_TOWER_CHECK C.5, A.4.1, A.7 and A.4.57. Next: finish their exact missing global arithmetic or configuration comparisons; a targeted calculation alone does not certify them.'),
 'L.1': ('A.2; E.137–E.151', 'The main finite-support assertion remains undecided. The new conditional pro-three construction has only explicit old-support plus equations left at each step, and retains a full ordinary pair. An actual infinite branch is still absent; finite satisfiability at selected depths does not supply one. Next: establish or exclude a coherent branch, then address all coefficient-prime sections on the same pair.'),
 'L.3': ('A.22–A.24; C.3–C.5; E.163–E.165', 'Restricted-product defects and concrete proper-cover Brauer exclusions are established. The harmonic proper target now has a fully checked class-8 detector and class-17 refinement, but requires actual local matching. Neither supplies a universal target or an unrestricted section obstruction for every ordinary ghost. Next: justify the precise local comparison at the coefficient place or find a target with a universal necessary obstruction.'),
 'L.6': ('C.6–C.7; E.163–E.165', 'The base finite-character sum vanishes on completed rational data. A concrete additional cover-wise Brauer sign now excludes the harmonic locally matched family, with all sheets checked and an actual arithmetic central-extension descent. This does not establish the universal countersign assertion. Next: prove that an appropriate cover/path invariant is defined and nonzero for every surviving ghost in the quotient under study.')
}
lines=[]
for line in report.splitlines():
    if line.startswith('| '):
        key=line.split('|')[1].strip()
        if key in updates:
            refs,state=updates[key]
            line=f'| {key} | {refs} | {state} |'
    lines.append(line)
report='\n'.join(lines)+'\n'
marker='## Fourth work period: exact ordinary continuation and completed harmonic audits'
if marker in report:
    report=report.split(marker)[0].rstrip()+'\n\n'
report += '''## Fourth work period: exact ordinary continuation and completed harmonic audits

E.146 proves that the old-support quotient gate of E.144 is sufficient for one finite pro-three extension, with at most two new ordinary support primes. E.147 adds actual finite local point images at every prime other than three using a uniform tame-cover bound. E.148 removes the unnecessary higher-point conditions at zero-support places while retaining ordinary good-reduction abelian data. It leaves precisely finitely many plus-character equations, tested over every allowed local aligning frame. The minus equations, the abelian digits at three and all zero-support abelian ordinary conditions introduce no further one-step obstruction.

E.151 supplies the missing all-coefficient arithmetic bridge. The exponents have exact three-adic valuation n−1 while their prime-to-three parts grow factorially. A simultaneous diagonal-curve refinement retains unit-coordinate solutions at every completion, the ordinary error bounds, all old pro-three point matches and the literal lower section. Its fixed-root Chebotarev step checks the actual cyclotomic/radical intersections. It introduces between nine and twenty-one fresh primes at each successful step. Thus any actual infinite path gives one full completed ordinary infinite-support pair and one continuous pro-three section above its three-primary part. No infinite path is asserted, and no other coefficient-prime sections are constructed. The statement is a sufficient restricted construction route; it is not an equivalence between this route and all potential counterexamples to A.3.

E.149 proves that the gate really can fail. A selected old prime carries a central Heisenberg discrepancy that the global cyclotomic cubic line cannot correct while the point-five match is retained. Every possible new ordinary inertia dies in the relevant quotient, so even arbitrary new support primes cannot repair that frozen predecessor. The finite certificate independently enumerates all 27 conjugators and all three global twists. This invalidates an automatic-extension strategy without proving that all possible infinite branches fail.

E.138 identifies the exact one-place all-prime class-two comparison at five: it imposes no restriction on the ordinary pair beyond selecting its unique global class. E.139 identifies the relative finite-field Bloch obstruction, constructs a nonzero order-nine example modulo the global order-three ambiguity, and verifies harmonic cancellation only for the stated rational reference. E.150 gives explicit distinct interior points over finite fields with the same full pro-three section class. It refutes general interior-point separation, but gives neither a point/cusp collision nor the prime-field statement needed for the remaining route. The primary source distinctions are recorded precisely.

E.160–E.165 complete the harmonic audit. A new exact initialization replaces the missing A.134 proof; it checks all 661 good primes through 5000 and every exceptional prime. The boundary root-stabilizer intersections and six Hilbert-symbol products justify the mixed-exponent recursion. The proper Brauer class has invariant one-half at every dyadic point and zero everywhere else. Both possible sheets of the cyclic degree-eight cover are checked. Its actual group is (C2)^8 semidirect C16, of order 4096 and class eight. The larger quotient is represented faithfully through the mod-two cycle space of a 128-vertex, 256-edge covering graph. It has order 2^136 and exact class seventeen. The lower-central recurrence and an explicit nonzero weight-seventeen word are checked independently, including the expanded-word SHA256. These results confirm A.137 and A.139 in their local-matching scope. They do not claim unrestricted nilpotent exclusion above the ordinary abelian pair.

No work was discarded. The harmonic replacement is explicitly distinguished from the unavailable original initialization; earlier dated descriptions of that missing input remain historical records. The pending full-GT and A.196 assertions remain separate from proved inputs.

### Fourth-checkpoint verification

The current paper has 218 pages and 163 numbered statements: 137 Proved, 3 Refuted, 13 Known and 10 Open. There are 65 bibliography entries, 62 cited keys and 507 recorded check events. The historical register has 90 rows: 83 confirmed, 2 repaired and 5 pending. All numbered statements have a recorded event; coverage checks do not themselves certify proofs. The final build has zero overfull boxes, zero boxes exceeding 2pt and zero unresolved references. Thirty-two pages spread through the document and all new proof sections were rendered and visually inspected; final changed audit pages are checked after the last rebuild. The fourth checkpoint is an ongoing-work checkpoint, not a completed answer.
'''
rp.write_text(report)

ledger=p / 'PROGRESS_LEDGER.md'
text=ledger.read_text()
marker='## Second formal hourly review — 2026-11-18 06:45 UTC / 07:45 CET'
if marker in text:
    text=text.split(marker)[0].rstrip()+'\n\n'
table=report[report.index('| Task or lead |'):report.index('# SECTION_GHOSTS research report')].strip()
text += marker+'''\n\nReview interval: from the first formal review at 05:44:51 UTC to approximately 06:45 UTC. **Qualifying movement: yes; consecutive no-movement reviews: zero.** The two historical open rows SECTIONS_OVER_Q A.137 and A.139 changed from pending to confirmed after complete replacement proofs, finite certificates and independent checks. This is actual audit-row closure, not a count of pages, computations or another fixed-depth survivor.

There is also a sharper constructive gate at coefficient three: E.146–E.148 prove one-step sufficiency of the old-support plus equations, and E.151 removes the separate full-ordinary arithmetic compatibility condition from that one-step construction. This does not prove that all possible A.3 counterexamples reduce to this restricted route, and no all-depth existence claim is used to justify movement. E.149 demonstrates a failed frozen predecessor; it does not exclude every branch.

### Main questions and their strongest proved gates

* A.2, full pronilpotent: still open. One fixed ordinary pair must have compatible sections in every coefficient component. Every off-diagonal support-point condition is necessary; E.137 pins at most one global class-two predecessor. The fixed-pair compactness equivalence is proved. No same-pair all-prime construction or finite-support implication follows from it.
* A.3 at three: still open. For the explicit E.151 construction, an actual infinite compatible solution of the finite old-support plus equations would give a full ordinary ghost with a pro-three section. Full ordinary arithmetic compatibility introduces no further one-step condition. The branch itself is unproved, and frozen predecessors can fail. Other support patterns remain possible.
* A.3 at two and at primes at least five: still open. Ordinary local boundary rigidity and the exact finite obstruction framework apply, but no full ordinary all-depth section or universal exclusion has been proved. Relative approximation at primes at least five is being investigated; provisional arguments are not counted as results.
* B.1–B.3: original all-coefficient closed remainder and universal first-exclusion assertions remain open. Exact selected exclusions and harmonic local-matching detectors are established; unrestricted and locally matched section fibres stay distinguished.
* C.1–C.4 and L.5–L.6: no universal rigid target or cover-wise countersign theorem. The harmonic proper Brauer target is now completely checked for its specified family. The full-GT configuration comparison is still missing.
* D.1: conditional consequences are proved; their unresolved premise prevents an unconditional manuscript theorem.

### Every task and lead at this review

'''+table+'\n\n### Every numbered result still labelled Open\n\n| Result | Exact current statement | Location |\n|---|---|---|\n'
for r in results:
    if r['status']=='Open':
        statement=' '.join(r['statement'].split()).replace('|','/').replace('\n',' ')
        text += f'| {r["id"]} | {statement} | {r["where_proved"]} |\n'
text += '\n### Every pending historical row\n\n| Historical claim | State reached | Remaining dependency |\n|---|---|---|\n'
for r in hist:
    if r['audit_status']=='pending':
        text+=f'| {r["historical_id"]} | {r["audit_scope"].replace("|","/")} | {r["remaining_check"].replace("|","/")} |\n'
text+=f'\nCurrent counts: {len(results)} numbered statements, {dict(rc)}; {events} check events; {len(hist)} historical rows, {dict(hc)}. The next formal review is due about 07:45 UTC / 08:45 CET. Checkpoint04 save success and its immutable identity will be recorded only after successful upload.\n'
ledger.write_text(text)
print('Recorded second formal review: movement yes; consecutive no-movement count 0.')
print('Historical:',dict(hc),'Results:',dict(rc),'Events:',events)
