#!/usr/bin/env python3
"""Add the audited finite five-point action and infinite prime-character results."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'GT_TOWER_CHECK_report.md'
text=path.read_text()
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| '):
        line=line.replace('A.4.1--A.4.36','A.4.1--A.4.37')
        line=line.replace('B.2.1--B.2.28','B.2.1--B.2.30').replace('B.2.9--B.2.28','B.2.9--B.2.30')
        line=line.replace('B.2.24--B.2.28','B.2.24--B.2.30').replace('B.2.25--B.2.28','B.2.25--B.2.30')
        line=line.replace('two independent shift families','countably many independent shift families')
        line=line.replace('two explicit shift families are jointly independent','countably many explicit prime-indexed shift families are jointly independent')
        line=line.replace('every finite paired-binary-shift prefix','every finite coordinate set of the countably generated binary shift')
        line=line.replace('the Delta-iterate family does not span, and an actual full-kernel witness separates the harmonic family',
                          'the full quotient V/D*V has dimension aleph0, and no finite family generates under descent')
        line=line.replace('two explicit character families and all their descent iterates',
                          'countably many explicit character families and all their descent iterates')
        if line.startswith('| A.4 |'):
            line='| A.4 | A.4, A.4.1--A.4.37 | Open; the actual630-factor ten-point quotient, finite centralizer/fusion refinements, literal source words and an explicit characteristic five-point action construction are proved; the retained frame comparison and complete genuine shadow/parity census remain to be executed |'
        lines[i]=line
text='\n'.join(lines)+'\n'
text=text.replace('source ledger has153 numbered statements:138Proved,2Known and13Open',
                  'source ledger has156 numbered statements:141Proved,2Known and13Open')
section='''### A specified finite five-point action and infinitely many character directions

A.4.37 supplies an explicit characteristic five-point quotient for every prescribed finite arity-ten output bound m. Its coefficient is C=(m!)^((m!)^45). The central cap of each inserted four-strand test preserves every zero-abelian pentagon defect and has order at most C. The defining symmetric-group coordinates prove that the newly constructed action descends to each characteristic kernel. A finite genuine gentle-pair record gives invertibility as a positive power, with no full pentagon assumption for an inverse pair. The proof retains both sphere relators, their literal quotient square, and all labelled forgetting maps. The nested-level construction incorporates the finite subgroup recognition refinements without asserting that an arbitrary intermediate kernel is invariant. Root opened and checked the ordinary presentation in Fresse Theorem6.2.4 and its unitary extension, and independently replayed every strand-doubling, block-twist and sphere-relator identity in the faithful Artin action for arities2 through10. The complete genuine shadow image and parity census remain uncomputed.

B.2.29 proves that adjoining a new actual PSL2(Fp) source quotient gives the direct product with the entire retained source whenever p is at least5 and does not divide its finite retained factor's order. The specified integral Brunnian matrix is noncentral at every odd prime, with the exact gcds128 and2. The integral H2 product map has no cross term because the new factor is perfect. Every Q/Z-valued central class kills the commutator of the designated frame pair, so the integral commutator itself vanishes and the full central-cover lifting theorem applies. This gives an actual full descent-kernel element with the prescribed new source frame. Root and an independent auditor checked the entire argument and opened the cited simplicity proof.

B.2.30 uses the signed Cartan centralizer at each odd prime to define a new harmonic defect. Ascending primes congruent3 or5 modulo8 supply triangular independent values on the full descent kernel while retaining every previous signed source factor. Normalization multiplies the frame and its intertwiner by the same actual matrix, so no divisibility of its exponent by the new prime is assumed. The resulting explicit map from the countable direct sum of F2[t] into the annihilator is injective. The entire quotient V/D*V has dimension aleph0; therefore no finite family, together with all its iterated pullbacks, generates the full annihilator. The actual binary product indexed by N^2 is onto already on H, with every finite coordinate image computed. Every new coordinate vanishes on GT and on the physical fixed subgroup. Root independently reran the integral matrix, all Cartan multiplication/character tables and every normalization exponent for the eleven displayed primes.

'''
assert '### A specified finite five-point action' not in text
text=text.replace('## Sources, reproducibility and retained files',section+'## Sources, reproducibility and retained files')
path.write_text(text)
print('Updated A437, B229--30 and the156-statement source ledger.')
