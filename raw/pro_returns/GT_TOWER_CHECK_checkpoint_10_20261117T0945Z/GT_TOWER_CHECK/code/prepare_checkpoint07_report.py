#!/usr/bin/env python3
"""Update the live outcome table and retain the seventh-hour audit narrative."""
from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'GT_TOWER_CHECK_report.md'
text=path.read_text()
text=text.replace('Current state during sixth-hour work','Current state during seventh-hour work')
def row(key,statements,state):
    global text
    pattern=r'^\| '+re.escape(key)+r' \|[^\n]*$'
    text,n=re.subn(pattern,lambda m:f'| {key} | {statements} | {state} |',text,flags=re.M)
    assert n==1,(key,n)
row('P.1(iii)','P.1, A.7, B.2.1--B.2.28',
    'Published scopes recorded; strict profinite inclusions, surjective descent, the full countable-dimensional quadratic annihilator, and two independent shift families are proved')
row('A.4','A.4, A.4.1--A.4.36',
    'Open; the actual630-factor ten-point quotient, its full joint image, explicit finite centralizer and labelled fusion refinements, and literal geometric source words are proved; the common five-point level and complete pentagon-shadow/parity census remain to be computed')
row('B.1','B.1, B.1.1--B.1.3, B.1.7--B.1.10',
    'Three literal subgroup assertions are refuted; the inclusion of the literal fixed subgroup in ker Delta remains open, with an exact full-kernel equation and both surviving signed-frame parities')
row('B.1: C^phi subset ker Delta','B.1, B.1.1--B.1.3, B.1.7--B.1.10, B.2.28',
    'Open; the physical fixed subgroup is annihilated by every harmonic pullback, while Delta parity remains unresolved; literal and physical maps are related by the stated inner conjugation')
row('B.2','B.2, B.2.1--B.2.28',
    'Open for further finite-image comparisons; the full quadratic annihilator is a countable-dimensional vector space, descent is surjective, and two explicit shift families are jointly independent')
row('B.2: finite images','B.2.1--B.2.3, B.2.9--B.2.28',
    'Actual images through class ten over F11 and every finite paired-binary-shift prefix are computed; the reduced central obstruction vanishes and descent has index1')
row('B.2: all quadratic annihilators','B.2.24--B.2.28',
    'Proved as an abstract group with an exact selected-basis morphism: the countable direct sum of C2; the Delta-iterate family does not span, and an actual full-kernel witness separates the harmonic family')
row('B.2: Delta generates the annihilator','B.2.8, B.2.25--B.2.28',
    'Refuted; two explicit character families and all their descent iterates are jointly independent, already on the multiplier-one subgroup')
row('B.4: all frame characters','B.4, A.7, B.2.25--B.2.28',
    'Open; the specified CM and harmonic characters and every descent pullback vanish on GT; the universal assertion for every frame construction remains unresolved')
row('Lead 1','A.8; A.1--A.7, A.4.1--A.4.36',
    'Main proof comparisons and signs are proved; explicit finite ten-point centralizer/fusion and source-word constructions advance the independent finite census, which remains open')
start=text.index('Sixth-hour checkpoint, 17 November 2026.')
end=text.index('\n\n',start)
text=text[:start]+('Seventh-hour working revision, 17 November 2026. Research began at approximately23:45UTC on16November. '
    'Checkpoints01--06 remain unchanged. The current source includes the independently audited ten-point, finite fusion, literal geometric braid and harmonic-kernel results. '
    'The next checkpoint and hourly progress review are due at approximately06:45UTC. '
    'The current source is not represented as a visually checked PDF until the new build and page inspection are complete.')+text[end:]
text=text.replace('Spanning by this particular iterated family and the literal fixed-subgroup parity question remain unproved.',
    'At checkpoint06, spanning by this particular iterated family and the literal fixed-subgroup parity question remained unproved. The seventh-hour result B.2.27 below refutes that spanning assertion; the fixed-subgroup Delta parity question remains open.')
text=text.replace("A.4's common effective census, B.1's remaining literal inclusion, spanning by the specified descent-character family, involution conjugacy,",
    "A.4's common effective census, B.1's remaining literal inclusion, further explicit finite-image comparisons, involution conjugacy,")
section='''## Seventh-hour advances

### The actual ten-point quotient and all of its four-point maps

A.4.29 determines the complete binary pure-abelian sphere quotient. Its pure module has dimension35. The actual crossing-mod-four extension is retained, including all of its source relations. The full linear system for Klein-four sections has128 cohomology classes; the named colored permutation centralizer has64 orbits of size two, and its stabilizer has the exact even-flip condition. The proof constructs the correction for every section, with a literal pure source word. Root independently reran the complete cocycle, rank, affine correction and section calculations.

A.4.30 proves equality between the full pure peripheral outer image and the actual geometric image for a specified class-three ternary ten-point quotient of order3^294. The common image has order3^119. Its35 first-order and84 cubic directions are realized by actual pair twists and their explicit commutators, checked in free-word Magnus coordinates. The comparison with the capped four-point target retains the actual map: its pure image has order108 and cyclic abelianization4, while the centralizer-only source maps to an order54 subgroup with cyclic abelianization2. The nonnilpotent image gives the stated obstruction to factoring this particular map through a nilpotent pure quotient.

A.4.31 gives the actual quaternary pure-abelian sphere quotient, with kernel C4^35. An integral minor of determinant minus one proves the exact relation lattice and its saturation. All four odd multiplier actions modulo8 are given on the actual crossing cocycle. At multiplier5 an explicit258-letter pure braid fixes every element above the named Klein-four permutations, independently of the chosen section. The correction has23 unit pivots and one residual two-pivot; exact star/total-relation witnesses are printed. Root separately reran this full calculation.

A.4.32 joins all630 four-subset/pair-partition forgetful maps in one actual finite quotient. The program stores all5670 generator edges and weights and verifies all28 distant commutators, eight adjacent braid relations and both sphere relations in every state. All45 literal pure pair twists are evaluated in every coordinate. Their630 characters satisfy every sphere relation, are pairwise distinct up to sign, and span the full C4 dual of rank35. The proof then uses the explicit character projectors and isolated Heisenberg commutators to recover the full kernel: the direct product of630 groups of order27. The pure image is the exact fibre product over C4^35; the full quotient has order10! times2^70 times3^1890 and has the actual quaternary sphere quotient as its quotient by that three-group. This is an equality of images under specified maps, with the central coordinates included.

### Finite recognition of the geometric centralizer and Klein-four action

A.4.33 constructs a finite detector for the point-pushing centralizer fibre in an actual one-point Birman sequence. Its source is the characteristic kernel kappa_s(F), followed by its binary and ternary homology covers. The binary graph argument recognizes the involution vertex. The ternary layer removes the kernel of the inner action by a faithful deck representation, including the finite-order integral-matrix argument. Both possible fixed-point vertices are retained.

A.4.34 applies that detector twice to an ordered fixed pair, then induces the finite homomorphism to the unordered pair. An actual binary sphere functional excludes a commuting element above the isolated pair transposition. The recursive construction takes the quotient by the actual pair-pushing image and uses the ordinary fixed-pair forgetful isomorphism. It therefore recognizes exactly the image of the full geometric Klein-four centralizer at every specified finite output, including A.4.32. The proof supplies all quotient maps and explicit bounds; it does not replace the finite fibre by an intersection of unspecified closures.

A.4.35 gives the accompanying labelled finite fusion construction. The one-point torsion comparison retains both cone-point types and their actual half-twist switch. After aligning one involution, the second is compared inside the retained finite centralizer fibre. The starting four-point group is checked by an explicit map from a free subgroup to C4. The final correcting mapping class is pure times at most the designated C0 flip, whose actual support makes it vanish under the required four-point forgettings. Root and the centralizer auditor checked the complete quotient recursion independently. A coordinate error in the nonadjacent half-twist square formula was corrected before integration by using the literal half twist as section.

A.4.36 supplies literal90- and86-letter source braid words for the geometric half-turns, with a26-letter marking. The ten-point configuration, stereographic chart and rotation paths are explicit. All90 pair polynomials and72 crossing events are certified by rational intervals, independent Sturm/Vieta counts, derivative and height signs, and adjacency. The source identification follows from the actual ambient paths and isotopy extension before finite reduction. Root independently reran every crossing and the full630-coordinate squares, commutator and section equations. The complete shadow census is still open: these maps must be joined to one finite five-point action with the frame and multiplier data retained.

### A second family of quadratic characters and the full descent kernel

B.1.10 shows by an actual witness that both parities survive equality of the signed source and descended frames. It gives the exact remaining nonlinear fixed-point equation in the kernel of the full shift map and proves that descent is onto that kernel. It also retains the arithmetic factor when comparing the physical and literal fixed subgroups. Frame equality alone therefore supplies no parity decision.

B.2.26 extends the harmonic defect to a character eta of the full gentle group, vanishing on GT and on the arithmetic group. The proof checks the full crossed composition law and conjugation covariance. The finite source retains its original A4 quotient as an additional marked factor. Root independently enumerated both centralizers of the full canonical cover and verified the saved odd source frame; the GAP replay took256.443 seconds and reported no errors.

B.2.27 upgrades the finite witness to the actual full descent kernel. The explicit Brunnian word lies in all six coordinate kernels and maps to the specified source double transposition. Its joined source is the exact V4 semidirect extension. Integral homology and the actual quaternion commutator give the extra central C2, and the named frame has zero obstruction in every central summand. The full central-cover lifting theorem then supplies an actual positive automorphism. The source correction is checked at every retained coordinate, giving an element with D=1 and eta=1. Combining it with the earlier Delta-one kernel element gives an element annihilated by every Delta iterate but detected by eta. Thus the Delta-iterate family does not span the full quadratic annihilator. The complete A4 map, all normalized source cocycles, all576 SL2(F3) products and the marked central correction were independently rerun.

B.2.28 proves that (D,Delta,eta) is onto H times F2^2. Recursive preimages give every finite coordinate vector, and compactness gives the full product of pairs of bits. The two character families are jointly independent under every descent iterate, with a stated injection of the free rank-two F2[t]-module. On the physical fixed subgroup every harmonic iterate vanishes and every Delta iterate equals Delta. The remaining Delta parity of that subgroup is still an open line.

'''
assert '## Seventh-hour advances' not in text
text=text.replace('## Sources, reproducibility and retained files',section+'## Sources, reproducibility and retained files')
start=text.index('The current ledger has141 numbered statements:126Proved')
end=text.index('The prior checkpoint manuscripts',start)
rows=list(csv.DictReader((ROOT/'GT_TOWER_CHECK_results.csv').open()))
counts={s:sum(r['status']==s for r in rows) for s in ('Proved','Known','Open')}
text=text[:start]+(f"The current source ledger has{len(rows)} numbered statements:{counts['Proved']}Proved,{counts['Known']}Known and{counts['Open']}Open. "
    'The new integrated computations and proofs have been independently reviewed or rerun. '
    'The last completed visual audit is checkpoint06:271pages and95 actually inspected full-page PNGs, with zero overfull boxes and no unresolved references or citations. '
    'The seventh-hour build and actual visual inspection are in progress; their exact counts and hash will replace this working-status paragraph when complete. ')+text[end:]
path.write_text(text)
print('Updated all task/lead rows and the complete seventh-hour audit narrative.')
