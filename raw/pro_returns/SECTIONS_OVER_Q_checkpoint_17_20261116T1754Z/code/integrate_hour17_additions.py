#!/usr/bin/env python3
"""Integrate completely audited seventeenth-hour results and their exact scopes."""
from pathlib import Path
import datetime
import json
import subprocess
import sys

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
specs = {
    'A.205': {
        'file': 'selmer_central_local_matching.tex',
        'after': 'selmer_general_unramified_obstruction.tex',
        'heading': 'The exact compact central correction fibre and fourth-layer local test',
        'detail': 'A.205 constructs the actual global central correction torsor and every local allowed subset, retaining the real geometric stabilizer action and all cusp labels. Its compact closed-intersection criterion is exact. At weight4 the full global correction group is C240 in each of three Hall coordinates, with literal generator(chi^4−1)/240. Every finite-place restriction is injective. The three coefficient projections at(3,2),(2,3),(2,5) give an exact CRT normalization; all remaining local conditions retain their stated tests. An ordinary finite local image leaves at most one globally matching candidate, and failure is witnessed at at most two places.',
        'answers': 'A1; A5; A9; A15; L10; L11; L14; L20',
        'depends_on': 'A.40 actual weight-two Euler and real normalization; A.60 literal local Frobenius comparison; A.61 unramified weight-four H2 and its real injection; A.204 global class-four lifting; Milne ADT I4.10(c), I4.15 and I5.1; Jannsen(1.6), Theorem2.2; integral Hall coordinates and actual local cusp decomposition maps',
        'uses_local_theorem': 'no; local matching is an explicitly retained input or an explicitly tested condition in the stated full nilpotent quotients',
        'manuscript_passages': 'cote149; scans54–58,79–85,126–127; exact continuous quotient lifting and point-or-cusp local comparisons',
        'notes': 'The first nonzero Hall weight proves global and finite-local geometric centralizer vanishing. At the real place the actual lifted-conjugator difference defines a continuous homomorphism into H1 and its exact translation cosets. Local point and cusp images are aligned by actual geometric conjugators before forming central differences. Full local Kummer injectivity gives the finite-place allowed-set bound, and real path transport retains the three intervals and two tangent signs. The literal tame inertia equation makes every integral Tate-weight cocycle unramified away from its coefficient prime. Finite fixed-support cohomology and the zero finite-H0 derived limit give compact continuous H1, with a complete compact Nakayama proof. At weight4 the retained H2 bound and zero integral H3 yield bounded finite H1; fractional coboundaries then give exactly16,3,5 at coefficients2,3,5. The actual CRT map is k to(k/3 modulo16,k/16 modulo3,k/16 modulo5). Thus the lift torsor has240^3=13824000 classes. Root and both peers audited the full saved source and exact certificate. The resulting normalization proves matching of the three specified projections; success of every remaining local condition is not asserted. Both principal A1 statements remain open.'
    },
    'A.206': {
        'file': 'two_inert_ninth_root_class_group.tex',
        'after': 'selmer_central_local_matching.tex',
        'heading': 'The complete ninth-root three-class group, capitulation and localized norm',
        'detail': 'A.206 proves the exact ordinary subfield-unit index3^6, the regulator ratio3^(−5), and Cl(M){3}=C3^4 with cyclotomic-module lengths(2,1,1). The actual ideal norm onto Cl(E2){3}=C3^3 has order-three kernel. Every three-primary E2 ideal class capitulates in M. The unique ramified three-prime generates both augmentation images and the norm kernel, so the S-localized ideal norm is an isomorphism C3^3.',
        'answers': 'A1; A5; A9; A15; L10; L11; L20; L21',
        'depends_on': 'A.138 base three-class vanishing; A.173 full E2 three-class group and detecting characters; A.191 actual ninth-root fields, F-prime class group and residue-weighted ideal norm coinvariants; A.194 actual norm-sum identity; A.199 complete unit lattice; A.203 both actual unit norm maps; Darmon1995 Section2 Theorem2.1, printed304',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans54–58,79–85,126–127; actual unit, ideal and continuous lifting comparisons',
        'notes': 'All four cubic subfields are embedded explicitly. The norm-sum identity kills the actual unit quotient by3, so its full ordinary index is the completed index3^6. The shared logarithmic lattices equal the actual base lattice: Kronecker and the changed-prime Kummer valuation prove this for the three radical fields, and the literal1+4+7 root norm proves it for the cyclotomic field. The summation-map kernel and orthogonal determinant both contribute4; coordinate repetition contributes3^10 and the regulator covolume conversion contributes3. The opened primary analytic formula gives class order81. The actual root norm annihilator and order27 coinvariants give the O-module lengths2,1,1 and exponent3. The other cyclic ambiguous-class formula gives rank(h−1)=1; its square-zero transfer, together with the actual onto ideal norm, proves full E2 capitulation. The unit H1 group has order27 and is exhausted by the capitulation map. Its Hilbert90 ramified-valuation map is therefore zero, proving the upper three-prime has a nonzero order-three class. A191’s residue-weighted ideal norm kills every S-prime class, which identifies the complete localization kernel. The degree6 E2 primes above2 split in M/E2; their individual upper classes are not replaced by extended lower ideals or asserted to vanish. Root and the independent peer read the full saved proof, rechecked the exact A191 norm map, reopened Darmon’s primary formula, and reran the lattice, Euler-factor and transfer certificate. The comparison of eta with the secondary continuous obstruction still requires its actual fractional-divisor map.'
    }
}

specs.update({
    'A.207': {
        'file': 'point3_class_four_1129_obstruction.tex',
        'after': 'two_inert_ninth_root_class_group.tex',
        'heading': 'An ordinary infinite-support ghost with an explicit finite matching obstruction',
        'detail': 'A.207 prescribes the ordinary residue t=828 modulo1129 in the actual A62 infinite-support recursion, while retaining a continuous global full class-four lift and the separate mod8 frame(3,−2). Every one of the eight local sheets of the cyclic-eight genus-two cover fails the complete localized two-Selmer image. Its actual geometric quotient has order128 and class4, and the everywhere locally matching class-four fibre of this same completed pair is empty.',
        'answers': 'A1; A5; A9; A10; A15; L9; L10; L11; L14; L19; L20',
        'depends_on': 'A.59 actual radical-field intersections, CRT and Chebotarev maps; A.61 global full class-four lifting with exact valuation factors; A.62 cubic-exponent ordinary recursion and its local analytic bijections; A.186 full genus-two two-Selmer image and literal branch Kummer map; A.192 cyclic-eight cover; A.193 arithmetic finite quotient and lower-central calculation; A.205 exact local allowed-set maps',
        'uses_local_theorem': 'no; ordinary local data and the point-or-cusp matching failure are proved in the explicitly named arithmetic quotients',
        'manuscript_passages': 'cote149; scans54–58,79–85,126–127; actual quotient sections, completed ordinary data and local matching',
        'notes': 'The initial modulus is D0=53747712000 and the actual homogeneous residues are59,28,1 with powers276,978,1. All138 possible exponent/target preimage cases have admissible inputs. The original local analytic bijections lift these to the exact1129 homogeneous equation, and the unchanged splitting intersections retain the global prime recursion. Every later common-value update preserves the ratio828; factorial limits remain ordinary at every place with disjoint infinite support. No giant prime-search stage is represented as executed. The branch-Weil dual basis gives the actual four Kummer coordinates and deck action. At1129 globalD has vector1111 andT has0000; all eight rational cover sheets have the four explicitly listed excluded vectors. Simple-root Hensel maps prove the entire residue-ball statement. The fixed sheet, local geometric conjugator and proper compactification maps place every proposed locally matching quotient section in the entire finite Jacobian Selmer group. Root read the full proof and its exact A62 inputs and reran the certificate; both independent full-source audits passed. A209 strengthens the same-pair matching exclusion to the actual class-two quotient of order32. Neither statement asserts a locally matching lower section for this ghost.'
    },
    'A.208': {
        'file': 'two_inert_secondary_divisor_comparison.tex',
        'after': 'point3_class_four_1129_obstruction.tex',
        'heading': 'The actual support-class map and principal divisor of a secondary unit lift',
        'detail': 'A.208 identifies the actual unit-support quotient U_E2/N_hU_M canonically with the two-dimensional minus three-class group by the literal ideal norm. Every pure-unit preimage defining the secondary character has a cyclic-nine Hilbert90 divisor that is principal in the full ordinary class group. Its secondary coordinates are exactly twice the two changed-prime valuations of the principalizer. The complete next tame unit-norm matrix has rank3, giving unit field-norm index27 and root-invariant three-class order3^7 in the next field.',
        'answers': 'A1; A5; A9; A15; L10; L11; L20; L21',
        'depends_on': 'A.173 exact class eigenspaces; A.184 actual one-step unit norms and well-defined secondary characters; A.191 actual ninth-root fields and ideal norms; A.199 complete M unit lattice; A.203 actual unit norm quotient and relative-unit map eta; A.206 full ordinary class group and capitulation; actual Hilbert90, global reciprocity and cyclic Hasse norm theorem',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans54–58,79–85,126–127; actual fractional-divisor and continuous norm-lifting comparison',
        'notes': 'For N_h(w)=a, the integral divisor equation div(w)=(h−1)D is solved orbitwise. Principal changes and strongly ambiguous divisors give exactly the kernel generated by the ramified three-prime; ideal norm then gives the actual support-class isomorphism. Surjectivity uses actual invariant ideal classes, and principalization of a prime-to-three multiple plus Bezout proves injectivity before completion. For a pure norm preimage b, the cyclic-nine Hilbert90 divisor descends to J with3J=div(f). Its sigma-strong ambiguity lies in the plus line generated by the three-prime, while the literal tau identity makes its class minus. The full ordinary class is killed by3 and therefore vanishes, permitting an actual principalizer x and unit factorization. At each changed prime the exact uniformizer t²/q gives the residue zeta^(2v(x)); normalization in the pure F_(q²) residue field gives precisely the secondary character. All51 complete-source unit residues for the next cyclic extension are evaluated through exact unramified q-adic rings, including every denominator division; the compact13-column matrix recovers all51 columns and has a displayed determinant−1 and complete row relation. Reciprocity at the unique3-prime and the cyclic Hasse norm theorem give the actual index27, with the completed maps retained separately. Root and independent peer audited the full saved source and reran the exact certificate. The h-alignment equation retains its actual unit h(x)/(r0x); the two class and valuation maps are not identified by their dimensions.'
    },
    'A.209': {
        'file': 'point3_class_two_norm_obstruction.tex',
        'after': 'point3_class_four_1129_obstruction.tex',
        'heading': 'The complete quadratic norm Selmer image and the class-two failure',
        'detail': 'A.209 computes the whole projected Selmer group for J[2]/delta²J[2] as the four squareclasses generated by−(2+sqrt6) and3+sqrt6 in Q(sqrt6). The actual coefficient map is the quadratic norm from Q(theta), theta⁴=54. All four global classes are trivial at1129, while all eight local cover sheets have vector(1,1). The geometric quotient has order32 and class2. Hence A207’s same ordinary infinite-support pair has a continuous global class-four lift and no everywhere locally matching class-two lift.',
        'answers': 'A1; A5; A9; A10; A15; L9; L10; L11; L14; L19; L20',
        'depends_on': 'A.186 actual branch pairing, Kummer coordinates and rational divisor classes; A.193 and A.207 actual cyclic-eight arithmetic quotient and fixed-sheet comparison; A.207 prescribed1129 ordinary ghost and full class-four lift; Milne ANT Theorem4.3 printed70; explicit quadratic unit and ramified-prime calculations',
        'uses_local_theorem': 'no; the entire projected Selmer condition and the ordinary/cuspidal quotient comparisons are explicit',
        'manuscript_passages': 'cote149; scans54–58,79–85,126–127; exact full nilpotent quotient maps and failure of local matching',
        'notes': 'In the literal branch basis ei=T+Ti, delta² identifies opposite roots. Pair sums give the actual Res_(Q(sqrt6)/Q) mu2 coefficient quotient and the norm Kummer map x−theta to x²−3sqrt6. Good-place Kummer classes are unramified, so all global candidates have even valuations away from2,3. The Minkowski bound and a norm−2 generator prove class number one. The full quadratic unit group is proved directly from Pell equations; the complete S-unit squareclass basis is−1,epsilon,pi2,pi3. The complex-over-negative-real norm condition equates the−1 andpi2 exponents. At3 the quartic is irreducible, J(Q3)/2 has order2, and the nonzero projectedT class gives the entire local image. Its residue and valuation conditions eliminate the epsilon exponent. The four surviving classes are all actual projectedD,T classes, proving sufficiency at every place, including2. Thus the smaller coefficient Selmer group is computed independently, rather than inferred by projecting a larger Selmer group. The actual order32 group has central commutator of order2 and receives E2. Explicit1129 square witnesses for both global generators and nonsquare norm values for all eight sheets prove the empty locus. Full local Kummer injection transfers it to the same completed pair, retaining all three cusp maps. Root and two independent peers audited the complete proof and certificate; all16 candidate classes,128 module equivariance identities,32768 group associativity identities and all eight sheets were checked. Both principal A1 assertions remain open.'
    }
})

specs['A.210'] = {
    'file': 'point3_dihedral_local_correction.tex',
    'after': 'point3_class_two_norm_obstruction.tex',
    'heading': 'An evaluated one-place central correction for the same ordinary ghost',
    'detail': 'A.210 evaluates the local class-two mismatch of the same A207 ordinary infinite-support pair at1129 alone. Every one of its24 continuous global class-two lifts has the point-three image in the actual order-eight dihedral quotient. The explicit rational cover has eight local point-three sheets and central-involution Frobenius over the prescribed ordinary residue828. The local correction group is C16 and the global correction sends k inC24 to6k. The discrepancies are exactly all eight odd classes, each occurring three times.',
    'answers': 'A1; A5; A9; A15; L9; L10; L11; L14; L20',
    'depends_on': 'A.40 exact full class-two lift torsor, local Frobenius quotient and C24 generator; A.43 literal Hall coordinates and pure class-two Ihara action; A.62 and A.207 exact infinite-support valuation pattern and ordinary residue1129; explicit D8 arithmetic quotient and rational degree-eight cover',
    'uses_local_theorem': 'no; all global quotient lifts and their actual ordinary local comparison are computed directly',
    'manuscript_passages': 'cote149; scans54–58,79–85,126–127; evaluated continuous central correction and local matching',
    'notes': 'In the fixed tangential gauge the exact tame relation gives c=(B_q m−A_q n)/(q−1)−mn/2. The actual A207 update exponents make c even and the two abelian inertia coordinates divisible by4 at every new support prime. Zero abelian inertia gives zero central inertia elsewhere outside2,3. The actual D8 images of any global lift and point3 therefore differ by a central quadratic character unramified outside2,3,∞; all eight possible characters split at1129. The rational cover t=((w⁴−1)/(w⁴+1))² has the exact same geometric kernel, proved by its meridian presentation. Its point3 fibre has eight simple local roots, while residue828 has two square but non-fourth-power radicands and central Frobenius on all eight sheets. This handles every geometric conjugator. The twenty-fourth-power completed identities also align the full coefficient-two local abelian classes, because the local unit two-completion has order8. The resulting continuous central discrepancy is odd in C16. The literal Frobenius value53110 gives the exact global image6k, proving all eight odd discrepancies with multiplicity3 and no zero. Root and both peers audited the full saved proof and reran the certificate; the37,485 finite tame parity checks supplement the all-prime proof. This is the same pair as A207, with its proved global class-four lift. Its first failure of continuous nilpotent local matching is exactly class2. The principal full-section classification and birational lifting assertions remain open.'
}

specs['A.211'] = {
    'file': 'two_inert_secondary_capitulation_coordinates.tex',
    'after': 'point3_dihedral_local_correction.tex',
    'heading': 'The normalized capitulation class and complete necessary unit coordinates',
    'detail': 'A.211 proves the exact cyclotomic norm identity for the alignment scalar, normalizes the Hilbert90 factor into the base field while preserving the original unit preimage, and constructs the actual lower capitulating ideal class. Its two changed-prime coordinates give the secondary character by multiplication by2. The complete necessary invariant anti-unit cubeclass space is three-dimensional, with the explicit lower basis epsilon,u11,u59 and exact coordinate map to that ideal class.',
    'answers': 'A1; A5; A9; A15; L10; L11; L20; L21',
    'depends_on': 'A.159 full completed relative-unit basis; A.173 exact minus class-group basis and ramified primes; A.184 well-defined actual/completed secondary character; A.199 complete unit lattice and residue isomorphism; A.206 ordinary capitulation; A.208 principalization, tame matrix and retained h-alignment; exact cyclic-nine integral group-ring identities',
    'uses_local_theorem': 'no',
    'manuscript_passages': 'cote149; scans54–58,79–85,126–127; actual secondary norm, ideal and completed-unit comparison',
    'notes': 'Three explicit integer group-ring vectors prove Norm_h(r0)=1 with every root-of-unity factor retained. Actual Hilbert90 then changes w and x by the same lower-field factor and f by its cube, preserving b,u,c literally while making f lie in F and r0=1. At the unique3-prime the total ramification9 gives the divisibility needed for the invariant M-divisor to descend to E2. The full ordinary class is killed by3 and capitulates; the tau-fixed lower cube class intersects the actual cyclotomic restriction kernel trivially, so the same conjugation identity descends and gives its minus class. The two changed-prime valuations give its actual ordered Δ11,Δ59 coordinates and the secondary character2(k11,k59). The A199 full residue isomorphism computes every sigma,h,tau action entry; exact rank23 and rank24 minors are−38080 and246784. The three explicit lower radicals have actual M-unit representatives by the proved ordinary capitulation and their degree-three divisors. Their determinant8 minor fills the complete necessary space, and the extra zeta9 class fills the full four-dimensional invariant anti-space. The actual Kummer restriction kernel from F to M proves the sign and final two coordinate identifications. Root and independent peer audited the full proof, and independent certificate reruns passed. The original Omega-unit norm equation still selects the coordinates for each input; no unevaluated secondary value or equality with Theta_h eta is asserted.'
}

selected = sys.argv[1:]
assert selected and all(key in specs for key in selected)
meta_path = w / 'notes/register_metadata.json'
meta = json.loads(meta_path.read_text())
paper_path = w / 'SECTIONS_OVER_Q_paper.tex'
paper = paper_path.read_text()
report_path = w / 'SECTIONS_OVER_Q_report.md'
lines = report_path.read_text().splitlines()
assert lines[0] == 'INCOMPLETE'
for key in selected:
    s = specs[key]
    source = w / 'sections' / s['file']
    assert '{' + key + '}{Proved}' in source.read_text()
    include = '\\input{sections/' + s['file'] + '}'
    if include not in paper:
        anchor = '\\input{sections/' + s['after'] + '}'
        assert paper.count(anchor) == 1
        paper = paper.replace(anchor, anchor + '\n' + include, 1)
    meta[key] = {name: s[name] for name in (
        'answers', 'depends_on', 'uses_local_theorem', 'manuscript_passages', 'notes')}
    answers = {a.strip() for a in s['answers'].split(';')}
    for i, line in enumerate(lines[:55]):
        if not line.startswith('| '):
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells) == 3 and cells[0] in answers:
            if key not in cells[1]:
                cells[1] += ', ' + key
            if s['detail'] not in cells[2]:
                cells[2] += ' ' + s['detail']
            lines[i] = '| ' + ' | '.join(cells) + ' |'
    heading = '## Continued work: ' + s['heading']
    if heading not in lines:
        lines += ['', heading, '', stamp + ': ' + s['detail'], '', s['notes'], '']
    for name in ['notes/hour17_root_audits.md', 'notes/root_progress.md']:
        with (w / name).open('a') as f:
            f.write('\n' + stamp + ' ' + key + ' integrated after complete source and exact-map audits. ' + s['detail'] + '\n')

if 'A.206' in selected:
    refpath = w / 'notes/root_references.bib'
    refs = refpath.read_text()
    if '@article{BIR_Darmon1995,' not in refs:
        refs += '\n' + (w / 'notes/two_inert_regulator_references.bib').read_text()
        refpath.write_text(refs)
paper_path.write_text(paper)
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')
report_path.write_text('\n'.join(lines) + '\n')
outputs = []
for script in ['build_bibliography.py', 'build_register.py']:
    proc = subprocess.run(['python', str(w / 'code' / script)], capture_output=True, text=True, check=True)
    outputs.append(proc.stdout)
out = 'Integrated audited sections: ' + ', '.join(selected) + '\n' + ''.join(outputs)
suffix = '_'.join(x.replace('.', '') for x in selected)
(w / 'code' / ('integrate_hour17_' + suffix + '_output.txt')).write_text(out)
print(out, end='')
