#!/usr/bin/env python3
"""Integrate the checked rank-ten obstruction and update the living main state."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'code/assemble_draft.py';t=p.read_text()
needle=' "main_finite_cm_forgetting_discrepancy.tex":"part_a_cm_forgetting_discrepancy.tex",'
assert needle in t
t=t.replace(needle,needle+'\n'+
 ' "centralizer_reversed_binary_obstruction.tex":"part_a_reversed_binary_obstruction.tex",')
p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_paper.tex';t=p.read_text()
needle=r'\input{part_a_cm_forgetting_discrepancy}'
assert needle in t
t=t.replace(needle,needle+'\n'+r'\input{part_a_reversed_binary_obstruction}')
p.write_text(t)
p=ROOT/'code/update_results.py';t=p.read_text()
pos=t.index("pat=re.compile(r'\\\\begin")
addition="""
add('A.4.43','B.1.3; B.2.7--B.2.9; A.4.41; literal rank10 Schreier basis and exponent4 class2 coordinates; exact signed source map', 'Task A.4; Lead 1(2)',
    'The reversed-prime class-two source admits a genuine parity-one identity record, and one existing actual element survives the entire specified nilpotent-kernel family',
    'The actual source has order54*2^65, pure abelianization C12^2 and generator orders12. The296-letter product of the three r-conjugates of [[x4,y4],z4]^2 is an r-centralizing involution with all six signed values5I. Its full canonical-cover lift commutes with r by the coprime2/3 identity and gives a normalized full gentle element with f=1 in the whole source. Fresh root and independent auditor replays check all45 commutator coordinates and exact signed32-element image. The already constructed k in R_nil(Fprime F^3) proves simultaneous survival whenever the inserted subgroup image is nilpotent.')

"""
t=t[:pos]+addition+t[pos:]
t=t.replace('A.4.1--A.4.42;', 'A.4.1--A.4.43;')
p.write_text(t)
p=ROOT/'part_a_finite.tex';t=p.read_text()
old=('prescribed finite mixed-braid target.  The remaining task\n'
     'constructs the finite genus-one and CM frame comparison\n'
     'and executes its complete genuine-source shadow/parity\n'
     'census.  The compactness result below supplies existence\n'
     'but no substitute for that computation.')
new=('prescribed finite mixed-braid target.  A.4.40 constructs\n'
     'the finite genus-one, universal-curve and ordinary\n'
     'forgetting actions.  A.4.41 and A.4.43 prove genuine\n'
     'parity-one survival for the stated odd-derived, odd-normal\n'
     'and relative nilpotent families, including the exact\n'
     'reversed-prime source.  A.4.42 computes the full $C_3^4$\n'
     'discrepancy between finite CM descent and ordinary\n'
     'forgetting at the current joined output.  The remaining\n'
     'task constructs a stronger geometric recognition\n'
     'refinement and executes the complete genuine-source\n'
     'shadow/parity census.  The compactness result below\n'
     'supplies existence but no substitute for that computation.')
assert old in t;t=t.replace(old,new);p.write_text(t)
p=ROOT/'GT_TOWER_CHECK_report.md';t=p.read_text()
t=t.replace('A.4.1--A.4.39','A.4.1--A.4.43')
t=t.replace('Three further independently audited results have now been integrated.',
            'Seven further independently audited results have now been integrated.')
t=t.replace('159 statements:144Proved','163 statements:148Proved')
t=t.replace('159 numbered statements:144Proved','163 numbered statements:148Proved')
t=t.replace('All three newly integrated proofs and their finite certificates',
            'All seven newly integrated proofs and their finite certificates')
t=t.replace('Open; the actual630-factor quotient and ordinary-image census are proved, and a specified characteristic five-point input forces every prescribed finite elliptic coefficient test; the finite genus-one/CM comparison and complete genuine shadow/parity census remain to be executed',
            'Open; the specified finite five-point input gives the genus-one and universal-curve actions; genuine survivors eliminate the stated relative nilpotent families, while the exact C3^4 discrepancy requires a stronger geometric recognition refinement before the complete shadow/parity census')
t=t.replace('The finite genus-one/CM comparison and complete genuine-source census remain under construction.',
            'A.4.40 now supplies the finite genus-one actions; A.4.42 identifies the exact remaining CM comparison obstruction, and the complete genuine-source census remains active.')
addition='''A.4.40 constructs the finite genus-one and actual universal-curve actions from the specified five-point input. The ninety-generator bound retains every required stabilizer map. A finite group of genuine gentle records proves invertibility of the quilt action, without a subgroup assumption on the reduced pentagon locus. The mod3 graph cover kills projected centers, so the actual Birman subgroup gives Aut(Q) by P/kappa_s(P), with peripheral conjugacy inside Q. The full ordinary Jc forgetting factor and its nine induced coordinates are retained. Root and the centralizer auditor checked the complete kernel and finite-record arguments.

A.4.41 proves genuine parity-one survival for every finite family of odd-derived targets and for targets with a specified odd normal subgroup and exponent-four quotient. A suitable odd power of [[x4,y4],z4]^2 supplies a central order-two auxiliary frame with six signed values5I. The full canonical-cover certificate and the exact C_N^2 abelian normalization give an actual full gentle element with identity pair record. Compactness gives one survivor for each entire directed family, also with D_P=1 and harmonic parameter0. In the concrete cap216 case, root independently replayed the actual source of degree3954 and order3673320192, its pure abelianization C12^2 and all six retained frame values. This rules out the stated entire relative-three refinement routes, rather than merely recording formal finite survivors.

A.4.42 proves that finite CM descent and ordinary forgetting have exact discrepancy image C3^4 at the current joined output. An explicit order-three Hermitian isometry centralizes the deck group and has a nontrivial descended class. The sixth derived subgroup of the actual joint geometric source realizes it with all lower and all nine ordinary-forgetting values identity. Six actual Cayley lifts give all729 first-order values, whose actual inner translation subgroup has order9; the81 outer classes are exactly the full signed-period kernel. The retained period basis comparison proves the reverse inclusion. The same discrepancy survives every finite additional solvable family. Root replayed all matrix and quotient equations, and two independent auditors reviewed the proof. The next recognition layer must control this source discrepancy.

A.4.43 eliminates the proposed reversed-prime class-two source by a full genuine certificate. Its actual B quotient has order54*2^65, with pure abelianization C12^2 and exact x,y orders12. The explicit296-letter norm of the three r-conjugates of the auxiliary square is r-fixed of order2, with all six signed values5I. The canonical-cover commutator identity gives an actual normalized parity-one element with identity pair record in this source. Root and the independent auditor replayed the rank-ten Schreier collection, all45 commutator coordinates and the signed32-element image. The previously constructed full k moreover survives every finite map whose image of Fprime F^3 is nilpotent, simultaneously for the same element; the five actual insertion maps transfer this to the stated whole five-point family.

'''
needle='The separate all-multiplier normalization supplement is preserved'
assert needle in t;t=t.replace(needle,addition+needle)
p.write_text(t)
print('Integrated A.4.43 and recorded all seven eighth-hour advances; next ledger count163.')
