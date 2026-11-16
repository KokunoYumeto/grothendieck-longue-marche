#!/usr/bin/env python3
"""Integrate only selected results with completed source and arithmetic audits."""
from pathlib import Path
import datetime, json, subprocess, sys

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
specs = {
    'A.185': {
        'file': 'point3_fermat8_prym_ranks.tex',
        'after': 'two_inert_secondary_unit_character.tex',
        'heading': 'Exact elliptic and quadratic Prym ranks on the pointed Fermat-eight cover',
        'detail': 'A.185 constructs three explicit rational isogenies from the Prym factors to Weil restrictions of elliptic curves over Q(sqrt(-3)), Q(sqrt(2)) and Q(sqrt(-6)). Exact two-isogeny connecting images give their ranks 1, 2 and 2. The three rational elliptic factors each have rank 1. The actual Jacobian decomposition therefore gives rank J(C8)(Q)=8 plus the sum of the six genus-two ranks, and hence rank at least 14.',
        'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
        'depends_on': 'A.182 literal factor isogeny and genus-two positive ranks; exact reciprocal involutions and cotangent maps; explicit two-isogeny Kummer maps and complete supported squareclasses; Milne ANT Theorem4.3 and AV I Theorem16.7',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans54–58; positive-rank cover route for A1 and A10',
        'notes': 'The proof fixes all three quadratic-field scalings and global points. It verifies the two-isogeny kernel cocycle and its exact index formula. Euclidean arguments settle the first two class groups; the Minkowski bound and literal ideal relations settle the third. Odd-prime residue tests, real signs and complete finite dyadic exclusions give the full connecting images, and displayed global points attain every surviving class. Root and Local peer read the complete saved proof and reran the retained certificates. No analytic or external-service rank computation is used. The six genus-two upper bounds and the full section classification are outside A.185.'
    },
    'A.186': {
        'file': 'point3_fermat8_genus2_ranks.tex',
        'after': 'point3_fermat8_prym_ranks.tex',
        'heading': 'Six exact genus-two descents and the rank-fourteen Jacobian',
        'detail': 'A.186 proves rank one, rational torsion Z/2, a two-dimensional two-Selmer group, and zero two-primary Tate–Shafarevich group for each of the six genus-two factors in A.182. The six literal quartic-field S-unit bases and seventeen local point tests give exhaustive upper bounds, matching the rational divisor classes already proved in A.182. Together with A.185 and the actual factor isogeny, this gives rank J(C8)(Q)=14 and genus 21.',
        'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
        'depends_on': 'A.182 literal Jacobian decomposition, rational non-torsion classes and torsion bounds; A.185 elliptic and Prym ranks; explicit odd-degree Kummer module and Weil-reciprocity comparison; Stoll 2001 Proposition4.6 and Corollary4.7; Poonen–Rains Corollary4.7 and Propositions4.9,4.11; complete default-flag-zero PARI class/unit certification',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans54–58; positive-rank cover route for A1 and A10',
        'notes': 'The proof gives the actual changes x=AX,y=A²Y, the full five-branch-point coefficient map, its inverse eta↦(N eta,eta), the square-root cocycle from Weil reciprocity, and the local Hilbert pairing including its rational coordinate. All 29 generators span the complete supported squareclass groups by fully certified class/unit calculations and full coordinate rank modulo two. All 17 local point witnesses and 85 Hilbert products are retained and independently rerun. Both peer agents read the complete saved source. Root read the used primary passages and independently reran the final certificate including the two nonzero localized-prime classes at c=13824. The finite Kummer exact sequence yields the exact rank and vanishing two-primary groups, with all finite 2-power Selmer comparisons. The full section and birational-lifting assertions remain open.'
    },
    'A.187': {
        'file': 'point3_fermat8_two_primary_selmer.tex',
        'after': 'point3_fermat8_genus2_ranks.tex',
        'heading': 'The full two-adic Selmer image of the Fermat-eight Jacobian',
        'detail': 'A.187 identifies both exact two-isogeny Selmer images for the six elliptic curves of A.185 and proves their two-primary Tate–Shafarevich groups vanish. The literal Prym pull–push maps have composite [2], so each rational Prym two-primary Tate–Shafarevich group is finite and killed by two. The actual A.182 isogeny then gives a finite two-primary Tate–Shafarevich group for J(C8), zero T2Sha, and the full continuous two-adic Selmer image equal to the completed rank-fourteen Mordell–Weil group.',
        'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
        'depends_on': 'A.182 actual Jacobian isogeny; A.185 complete local isogeny-squareclass bounds; A.186 exact genus-two descents; literal twisted quartic torsors and Prym pull–push maps; Milne ADT I Proposition6.4, Corollary6.6 and Remark6.7; explicit continuous finite-cocycle inverse limits',
        'uses_local_theorem': 'no; the final section-image assertion is explicitly for full Selmer sections',
        'manuscript_passages': 'cote149; scans54–58; full Selmer-section comparison on the pointed positive-rank cover',
        'notes': 'The two isogeny Selmer orientations are proved using the actual quartic-torsor isomorphism, its inverse and its kernel-point cocycle. Each necessary local bound is attained by the displayed global points. Galois descent and Shapiro include the literal local-place partition. Both Prym composites are [2]. The finite Selmer transition is proved from its Sha-coordinate and its rational-point inverse; continuous H1 is checked through finite cocycle and zero-cochain inverse limits. The final comparison only describes the Jacobian image of a full Selmer section. No passage to a full section classification is asserted. Complete source and map-certificate audits passed.'
    },
    'A.188': {
        'file': 'point3_fermat8_integral_retraction.tex',
        'after': 'point3_fermat8_two_primary_selmer.tex',
        'heading': 'An integral reverse map and an explicit five-level Selmer bound',
        'detail': 'A.188 constructs an explicit rational divisor-pullback map H from the twelve-factor product to J(C8). For the specified decomposition F, both HF and FH are multiplication by16. The proof gives all twelve literal generic fibers and exact curve degrees, then computes the actual trace/pullback operators on all twenty-one character lines. Consequently the kernel of F is killed by16, its degree is a power of two, 32 annihilates Sha(J(C8))[2-infinity], and the image from Selmer level 2^(n+5) to level 2^n is exactly the Mordell–Weil Kummer image.',
        'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
        'depends_on': 'A.182 literal curve maps and full twenty-one-character cotangent table; A.187 factor Tate–Shafarevich annihilators and finite Kummer transitions; direct inverse-branch trace/integral calculation; Milne Jacobian Varieties Theorem2.5',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans54–58; exact positive-rank quotient maps used toward A1 and A10',
        'notes': 'Every component of H is an actual rational divisor pullback, weighted by2 only for the first three genus-two maps. The remaining genus-two maps have degree16; elliptic maps have degree16; quartic maps have degree8 and their anti-involution doubles the Prym operator. Hermitian adjunction is proved from inverse branches and Abel–Jacobi integrals. The distinct mu8-squared characters prove orthogonality, and the computed sum is [16] as an actual homomorphism by faithfulness of the differential. All generic source/forward substitutions and basis counts are retained in an exact local Groebner certificate. No principal polarization of a Prym is assumed and no section classification is inferred.'
    },
    'A.189': {
        'file': 'point3_fermat8_dyadic_chabauty.tex',
        'after': 'point3_fermat8_integral_retraction.tex',
        'heading': 'The exact dyadic point locus in the pointed Fermat-eight class',
        'detail': 'A.189 proves that the global-completion-compatible locus on y²=x⁵−54x with x in3+8Z2 is exactly (3,±9). Its explicit Abel–Jacobi logarithm computation compares the global slope1 modulo4 with slope3 modulo4 for every other point in that disc. Through the actual Fermat map this proves C8(Q)={(±1,±1)}. Every locally point-or-cusp-matching section of the full metabelian tripod extension in finite Kummer class([3],[-2]) consequently has ordinary dyadic centre3, with global first-factor compact two-adic class D or−D.',
        'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
        'depends_on': 'A.182 literal Fermat genus-two map; A.186 exact rank-one completion generators and Selmer images; A.187 continuous Kummer comparison; A.178 finite-sheet local comparison; actual Cantor divisor doubling and all-coefficient binomial bounds; McCallum–Poonen Section4.1 Remark4.1; Poonen Theorem5.7.25 and Proposition5.7.26',
        'uses_local_theorem': 'no; the section assertion explicitly assumes local point-or-cusp matching in the stated full metabelian extension',
        'manuscript_passages': 'cote149; scans54–58; positive-rank finite Kummer class and its actual local section images',
        'notes': 'The proof supplies two literal divisor-doubling functions, the quadratic smooth-disc branch, the Néron-model comparison, and bounds on every coefficient of both infinite integrations. It determines the full relevant dyadic intersection and the four rational points on this specified curve. The geometric subgroup H=ker(Pi→(Z/8)^2) satisfies Pi-double-prime contained in H-prime, giving the actual arithmetic cover and compact two-adic maps. Root and both peer agents read the full saved proof, reopened the primary Néron/formal logarithm passages and independently reran the exact certificate. The global full-section classification remains open.'
    },
    'A.190': {
        'file': 'point3_fermat8_dyadic_injectivity.tex',
        'after': 'point3_fermat8_dyadic_chabauty.tex',
        'heading': 'The four exact global compact two-adic Jacobian classes',
        'detail': 'A.190 proves injectivity of completed Mordell–Weil localization at2 for all twelve factors and for J(C8). The two rank-two quadratic elliptic factors are treated by an exact conjugate-isogeny determinant and a rational formal-logarithm certificate with rigorous infinite-tail bounds. The actual Prym and Jacobian reverse maps transfer injectivity with the rational torsion comparison. Combining A.187–A.189, the full continuous two-adic Selmer intersection with C8(Q2), including its global class, is exactly the four rational point pairs (kappa2(j(P)),P).',
        'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
        'depends_on': 'A.185 exact factor ranks; A.186 completed genus-two generators; A.187 continuous Selmer and actual Prym composites[2]; A.188 actual Jacobian composite[16]; A.189 exact dyadic locus and full metabelian fixed-sheet maps; exact quadratic-field elliptic logarithm determinant and tail bounds',
        'uses_local_theorem': 'no; its section application uses the explicitly locally matching metabelian class of A.189',
        'manuscript_passages': 'cote149; scans54–58; actual global compact two-adic point classes in the selected full metabelian finite frame',
        'notes': 'For Q(sqrt(2)), the actual conjugate two-isogeny makes the log determinant a²+2b², nonzero by valuation parity. For Q(sqrt(-6)), the displayed P and scaled-dual point have twice-log coefficient matrix [[2526,270],[1435,4006]] modulo4096; exact pole-branch and all-tail bounds prove determinant valuation−1, with error valuation at least18. Completed local kernels are compared explicitly with finite odd torsion. The [2] and [16] reverse homomorphisms give exact injectivity on each global completion. Four point classes are separated by the second and third genus-two projections. Root and Legendre completed full source/certificate audits. The conclusion is in the specified continuous compact Jacobian quotient; the full section and birational-lifting assertions remain open.'
    },
    'A.191': {
        'file': 'two_inert_ninth_root_class_comparison.tex',
        'after': 'point3_fermat8_dyadic_injectivity.tex',
        'heading': 'The ninth-root base and its exact localized class quotient',
        'detail': 'A.191 specifies the actual cyclotomic base F′=Q(cuberoot(3),zeta9), radical field M=Q(t,zeta9), and both commuting cubic generators. Nine literal global units have a full nine-dimensional cubeclass saturation certificate and a rank-three six-prime tame norm matrix. The unit field-norm index is27 and the root-invariant three-class subgroup has order27. The actual ideal norm M→E2 induces isomorphisms from both ordinary and S-localized root coinvariants onto Cl(E2){3}=C3³; ideal extension into the S-localized group is zero.',
        'answers': 'A1; A5; A9; A15; L10; L11; L20; L21',
        'depends_on': 'A.138 one-prime three-class vanishing; A.170 and A.173 literal unramified characters and E2 class group; A.173 exact ambiguous-class formula; A.175 cyclic field-norm comparison; explicit ninth-root field maps, saturated unit residue certificates and ideal norms',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans54–58,79–85,126–127; exact norm comparison in the birational and continuous obstruction routes',
        'notes': 'The root generator sigma fixes F′, whereas the cyclotomic generator h fixes E2. Full local Kummer degree and the holomorph abelianization prove total ramification at3. Nine unit characteristic polynomials and nine independent residue rows certify the complete pro-three unit lattice; all162 small printed coefficients and all six tame rows are checked. The norm to E2 has residue-degree factor3 at changed primes and kills every S-prime class. Disjointness of the old Hilbert class field and the ramified cyclotomic extension gives surjectivity by degree-one prime norms. Its trivial target action and the exact invariant order prove both coinvariant isomorphisms. Root read the complete source and reran the full certificate; Local also completed an independent source/certificate audit. No full class-group order, module length or tertiary unit-character value is inferred.'
    }
}
specs['A.192'] = {
    'file': 'point3_genus2_full_dyadic_locus.tex',
    'after': 'two_inert_ninth_root_class_comparison.tex',
    'heading': 'The complete dyadic locus and its cyclic-eight section map',
    'detail': 'A.192 determines the entire continuous two-adic Selmer intersection on C:y²=x⁵−54x, including its global coordinate: the four pairs at infinity, (0,0), and (3,±9), with classes0,T,D,−D. The actual cyclic degree-eight cover z⁸=−t(1−t)³/24 has compactification C. In its single finite Kummer class[-24], every locally matching full metabelian section has dyadic ordinary centre3 or cusp0 or1, with the corresponding exact compact coefficient class.',
    'answers': 'A1; A5; A7; A10; A11; L7; L10; L15; L19',
    'depends_on': 'A.186 exact genus-two two-primary Selmer group and completed generators; A.189 actual logarithm slope and unit-disc intersection; A.178–A.189 fixed-sheet and cuspidal maps; Poonen Theorem5.4.8(ii) and perfect-field chain5.9.1; explicit smooth integral charts and restricted formal primitives',
    'uses_local_theorem': 'no; the full metabelian assertion explicitly assumes local point-or-cusp matching and the single stated finite class',
    'manuscript_passages': 'cote149; scans54–58; exact finite-character cover and compact coefficient comparison toward A1',
    'notes': 'The positive-valuation chart has two residue points. Its entire special-fibre Abel–Jacobi image factors through the unipotent radical of dimension at most2, and the literal multiplication-by4 map is zero there. This proves the actual formal-logarithm comparison on the full restricted disc, including unit scaled parameter. All positive and negative valuations are excluded by all-coefficient bounds; unit valuations use A.189. The explicit inverse maps are x=−6z²/(1−t),y=−18z/(1−t), and all boundary fibres and ramification indices are checked. Root and both peers read the full proof and independently reran its exact finite certificate; root reopened both primary algebraic-group passages. Finite series checks supplement the infinite coefficient proof. The full section-classification and birational-lifting assertions remain open.'
}
selected = sys.argv[1:]
assert selected and all(k in specs for k in selected), selected
meta_path = w / 'notes/register_metadata.json'
meta = json.loads(meta_path.read_text())
paper_path = w / 'SECTIONS_OVER_Q_paper.tex'
paper = paper_path.read_text()
report_path = w / 'SECTIONS_OVER_Q_report.md'
lines = report_path.read_text().splitlines()
assert lines[0] == 'INCOMPLETE'
for key in selected:
    spec = specs[key]
    source = w / 'sections' / spec['file']
    assert ('{' + key + '}{Proved}') in source.read_text()
    include = '\\input{sections/' + spec['file'] + '}'
    if include not in paper:
        anchor = '\\input{sections/' + spec['after'] + '}'
        assert paper.count(anchor) == 1
        paper = paper.replace(anchor, anchor + '\n' + include, 1)
    meta[key] = {k: spec[k] for k in ['answers', 'depends_on', 'notes', 'uses_local_theorem', 'manuscript_passages']}
    answers = {a.strip() for a in spec['answers'].split(';')}
    for i, line in enumerate(lines[:55]):
        if not line.startswith('| '):
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(cells) == 3 and cells[0] in answers:
            if key not in cells[1]:
                cells[1] += ', ' + key
            if spec['detail'] not in cells[2]:
                cells[2] += ' ' + spec['detail']
            lines[i] = '| ' + ' | '.join(cells) + ' |'
    heading = '## Continued work: ' + spec['heading']
    if heading not in lines:
        lines += ['', heading, '', stamp + ': ' + spec['detail'], '', spec['notes'], '']
    audit = stamp + ' ' + key + ' integrated after complete saved-source and exact-map audits. ' + spec['detail'] + '\n'
    for name in ['notes/hour15_root_audits.md', 'notes/root_progress.md']:
        with (w / name).open('a') as f:
            f.write('\n' + audit)
paper_path.write_text(paper)
meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')
report_path.write_text('\n'.join(lines) + '\n')
proc = subprocess.run(['python', str(w / 'code/build_register.py')], capture_output=True, text=True, check=True)
out = 'Integrated audited sections: ' + ', '.join(selected) + '\n' + proc.stdout
suffix = '_'.join(x.replace('.', '') for x in selected)
(w / 'code' / ('integrate_hour15_' + suffix + '_output.txt')).write_text(out)
print(out, end='')
