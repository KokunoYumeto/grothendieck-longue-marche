#!/usr/bin/env python3
"""Advance the living report after the seventh immutable checkpoint."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'GT_TOWER_CHECK_report.md'
text = path.read_text()
assert 'Seventh-hour checkpoint, 17 November 2026.' in text
text = text.replace('Current state at checkpoint07', 'Current state during eighth-hour work')
start = text.index('Seventh-hour checkpoint, 17 November 2026.')
end = text.index('\n\n', start)
text = text[:start] + (
    'Eighth-hour working revision, 17 November 2026. Research began at approximately23:45UTC on16November. '
    'Checkpoints01--07 are saved and remain unchanged. The seventh checkpoint contains the clean310-page manuscript '
    'and101 actual full-page inspections. Three further independently audited results have now been integrated. '
    'The source ledger has159 statements:144Proved,2Known and13Open. The new manuscript build and final visual review '
    'are in progress. The next checkpoint and hourly progress review are due at approximately07:45UTC.') + text[end:]
text = text.replace('A.4.1--A.4.37', 'A.4.1--A.4.39')
text = text.replace('B.2.1--B.2.30', 'B.2.1--B.2.31')
old = ('Open; the actual630-factor ten-point quotient, finite centralizer/fusion refinements, literal source words '
       'and an explicit characteristic five-point action construction are proved; the retained frame comparison '
       'and complete genuine shadow/parity census remain to be executed')
new = ('Open; the actual630-factor quotient and ordinary-image census are proved, and a specified characteristic '
       'five-point input forces every prescribed finite elliptic coefficient test; the finite genus-one/CM '
       'comparison and complete genuine shadow/parity census remain to be executed')
assert old in text
text = text.replace(old, new)
text = text.replace(
    'Open; the physical fixed subgroup is annihilated by every harmonic pullback, while Delta parity remains unresolved; literal and physical maps are related by the stated inner conjugation',
    'Open; all full prime harmonic values on the literal fixed subgroup are the displayed multiplier bits, while all vanish on the physical fixed subgroup; Delta parity remains unresolved')
start = text.index('## Pending work retained at the source freeze')
end = text.index('## Sources, reproducibility and retained files', start)
text = text[:start] + '''## Eighth-hour advances

A.4.38 determines the actual ordinary centralizer image in the named630-state quotient. Two explicitly marked quartet motions descend to a based free generating pair in the three-punctured quotient sphere. Their exact crossing certificates give words of lengths74 and64. The complete174-orbit fixed-kernel computation gives the finite centralizer order2^27*3^510. All4096 two-motion states and8192 literal source Schreier edges give ordinary image order2^14*3^302, hence index2^13*3^208 in that same finite centralizer. The198 noncentral directions,98 initial central directions and six additional bracket directions are verified independently. The proof and all three fresh-copy programs passed root review and replay; the audit is in notes/eighth_hour_ordinary_centralizer_audit.md.

A.4.39 gives a specified finite five-point input for every prescribed finite elliptic coefficient test. The actual C2*Z graph has a cusp cycle whose deck stabilizer is exactly the cusp subgroup. Two explicit homology refinements therefore reduce the two conjugacy equations to k*d^t*h=v^s. Retained index-two abelian coordinates determine t=-4c modulo2e. The two actual1260-coset induced quartet maps, followed by finite centralizer recognition and labelled fusion in that order, give the required finite outer S-square. The mixed action and its gauge are proved at every multiplier, and the join-and-cap map restores the original braid center. Thus the bounded characteristic five-point quotient forces TA.2 at the specified finite target on the actual gentle source. Root and an independent auditor checked the complete proof; root replayed all216 finite cusp graphs and the literal source identities. The finite genus-one/CM comparison and complete genuine-source census remain under construction.

B.2.31 gives a choice-free full signed-frame formula for each prime harmonic annihilator. The signed harmonic matrices form a literal representation of the whole gentle group. The quotient W_p(g)*W_p(Dg)^-1 lies in the norm-one Cartan, and its quadratic bit plus the exact multiplier correction is the full character. The split and nonsplit Cartan calculations retain every sign. On the literal fixed subgroup the value is exactly the displayed local quadratic-residue bit corrected by the multiplier modulo4; on the physical fixed subgroup it is zero. Root checked R1's full all-prime covariance at its actual source and independently replayed the normalizer tables at nine primes and all4096 and16384 products in the two smallest complete matrix-pair groups. The remaining Delta parity question is unchanged by this result.

The separate all-multiplier normalization supplement is preserved with the source snapshots. The auxiliary PC52 cohomology run was terminated as superseded by the integral perfect-factor proof; no cohomology result is claimed for it, and its actual source and output remain retained.

''' + text[end:]
text = text.replace('Checkpoints 01, 02, 03, 04 and 05 are retained unchanged.',
                    'Checkpoints01--07 are retained unchanged.')
start = text.index('The current ledger has156 numbered statements')
end = text.index('The prior checkpoint manuscripts', start)
text = text[:start] + (
    'The current ledger has159 numbered statements:144Proved,2Known and13Open. '
    'All three newly integrated proofs and their finite certificates have passed root review and independent replay. '
    'The eighth-hour build is in progress; the final exact PDF hash, page count, overflow count and actual page inspections '
    'will be recorded after the proof freeze. Checkpoint07 retains its separately verified310-page PDF,101 inspected pages '
    'and exact hash ddc2b4623e3565442139392d1154ac179c5e080cac683701db14fbc125c893f2. ') + text[end:]
rows = list(csv.DictReader((ROOT / 'GT_TOWER_CHECK_results.csv').open()))
assert len(rows) == 159 and sum(r['status'] == 'Proved' for r in rows) == 144
path.write_text(text)
print('Prepared eighth-hour living report with159 statements; previous checkpoint remains immutable.')
