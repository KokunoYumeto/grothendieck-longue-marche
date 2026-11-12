"""Rebuild the late-section source and result registers (standard library only).

Run B_late_sections.py first.  This file records source scope and proved
reductions, not an independent proof of the mathematical statements.
"""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
CHECKS = json.loads((BASE / 'code/B_late_sections.json').read_text())
assert CHECKS['restricted_modular_quotient']['corrected_image_order'] == 8
assert CHECKS['corrected_alpha_word']['identities_checked'] == 5184

results = [
    {
        'id': 'B.17',
        'statement': 'The smaller antidiagonal quotient of section 49.VI is undefined when its permitted loop subgroup is not contained in C^natural; the image construction uses L intersect C^natural and has the corrected exact sequence and numerical kernel.',
        'status': 'Refuted',
        'where_proved': 'sections/B_late_sections.tex, B.17 and equations (B.17.1)--(B.17.2)',
        'depends_on': 'Elementary semidirect-product algebra; E.15; code/B_late_sections.py',
        'manuscript_passages (section; folio; scan)': '49.VI; 631v--632v, 634--634v; C3:658(18)--(22),659(27)--(28),660(29)--(32),663(47)--(51),664(52 bis)',
        'depends_on_doubtful_reading (scan, alternatives)': 'The natural/sharp superscript is immaterial. The checked text explicitly permits L_0^natural strictly larger than L_0 intersect C^natural. No photographic decision is claimed for scans 658--664.',
        'notes': 'Counterexample also holds for C=completed SL2(Z), A=closure(Pi0): l=e0^2 is not in A but -l is in A, and both induce the same inner automorphism. The executed SL2(Z/4) image has |C|=48, |A|=4, L={1,l}, L intersect A=L intersect Z(C)=1; corrected image AL has order8 and automorphism kernel {I,-I}. Profinite repair assumes profinite D, continuous action and j, and closed D-stable A,L. The image kernel over D/jL is AL when j is injective, not A unless L is contained in A.'
    },
    {
        'id': 'B.18',
        'statement': 'The late normalized-section and restricted-conjugator constructions have a source-indexed dictionary, proved multiplication and fibre-product reductions, and explicit remaining universal profinite and integral comparisons.',
        'status': 'Open',
        'where_proved': 'sections/B_late_sections.tex, B.18, equations (B.18.1)--(B.18.8)',
        'depends_on': 'B.16 normalized conjugators and quotient sections; B.17 corrected image; D.8 and equation (D.15); E.15,E.19; code/B_late_sections.py',
        'manuscript_passages (section; folio; scan)': '49.V--VI; 595--601,621--627v,628--647v; C3:583--595(41)--(64),635--650(32)--(60),651--690(1)--(128)',
        'depends_on_doubtful_reading (scan, alternatives)': 'Working natural/sharp reading only. Records corrected sign prose594, commutator595(64), target647(50), coordinate order648(54)--(55), target649(57), omitted quotient650, weakened condition653(4)d, and unverified identifications686(115)--(116),689--690.',
        'notes': 'Proved formal cases: twisted a-law, exact corrected alpha word, source-order sign cocycle and cochain conversion, bisection under typed input hypotheses, central intersection, and projection-image intersection formula. Executed: 36 S3 pairs (12 fail naive multiplicativity), 5184 corrected words, 512 associativity triples, 16 sign pairs, and an order192 fibre-product model with order16 smaller subgroup; its order8 quotient has an involution whose two lifts have order4. B.16 already proves normalized maps in G_Z; residuals are their source identification and unquotiented lift, the actual index24 kernel, and the repaired natural comparisons for A=closure(Pi), then closure(Pi0), including 686 and 689--690. Integral representability/fppf comparison is not inferred from these profinite constructions. Open denotes the remaining work in this report, not a literature-wide novelty claim.'
    },
]

def reading(package, scan, place, support, strength='Mathematical consequence of the checked transcription; the photograph of this exact formula was not supplied.'):
    return {'package': package, 'scan': scan,
            'the \\unsure or \\illegible place': place,
            'what the mathematics supports': support,
            'how strongly': strength}

readings = [
    reading('LM_C3-568-586', 'C3:583--585',
            'Equations (41)--(48): a0 versus a and ordinary versus twisted multiplication.',
            'With delta(u)=t^nu(u) delta(a0(u)), the exact law is delta(a0(u\u2032u))=t^nu(u) delta(a0(u\u2032)) t^-nu(u) delta(a0(u)); B.18.1. All36 pairs in S3 satisfy it and12 fail the ordinary law.'),
    reading('LM_C3-568-586; LM_C3-587-605', 'C3:586--587',
            'Equations (49)--(53): normalization and exponent order in a=tau\u2032^nu3 alpha^-1 u.',
            'The fibre uses j modulo6 and i modulo4; choosing i=j=0 gives the normalized a, distinct from a0. B.16 proves normalized conjugators in its formal G_Z; source subgroup identifications are separately retained.'),
    reading('LM_C3-587-605', 'C3:594--595',
            'Prose sign criterion at594 versus equation (63) at595.',
            'For left factor primed, c((u\u2032,v\u2032),(u,v))=u(u\u2032+v\u2032); epsilon=+1 iff right epsilon3=+1 or left epsilon2 epsilon3=+1. The incompatible prose bad-case sign is corrected. All16 pairs and512 associativity triples executed.'),
    reading('LM_C3-587-605', 'C3:595',
            'Equation (64), withdrawn naive alpha\u2032\u2032 and final commutator correction.',
            'The exact word is epsilon u\u2032(alpha) alpha\u2032 t^nu3\u2032 [a\u2032,t^nu3] t^-nu3\u2032. The5184 finite word checks include a counterexample to omitting the commutator. Its validity is proved in an arbitrary ambient group with t^2=1 and central epsilon.'),
    reading('LM_C3-625-643', 'C3:635--641',
            'Subgroup lattice (32)--(44), deleted diagram, and inserted equivalence in (42).',
            'M^0(-j)=ker(epsilon2 on M\u2032(-j)) and M\u2032\u2032\u2032(-j)=<tau\u2032>M^0(-j) are recorded. Stability does not by itself imply tau\u2032(x)=x modulo Pi0; quotient action and actual normality/index claims remain to be proved. Deleted diagrams are not reinstated.'),
    reading('LM_C3-625-643; LM_C3-644-662', 'C3:643--647',
            'Equations (45)--(46), inserted correction645, and cancelled kernel filtration646.',
            'Exact residual is ker(Nrho* -> GL2(Z/4)/V4)=M^0(-j). E.19 computes the order24 target, not this kernel. The cancelled claim ker(epsilon3 on M\u2032\u2032!) is not adopted.'),
    reading('LM_C3-644-662', 'C3:647',
            'Equation (50), second inclusion target.',
            'The subgroup Nrho?=Zrho!<tau\u2032> belongs in Nrho*, not Nsigma*, for the following fibre product to be typed.'),
    reading('LM_C3-644-662', 'C3:648',
            'Central intersection following (54) and the repeated number (55).',
            'For coordinate order (rho,sigma,G), E_rho x_gamma S_sigma x_gamma G meets the central triple in mu_rho x1 xmu_G, not1 xmu xmu. Both formal proof and order192 executed model verify this.'),
    reading('LM_C3-644-662', 'C3:649--650',
            'Lower target in (57) and final arrow after (60).',
            'The lower target is gamma for the displayed kernel. The canonical bisection map has target M_full/mu_rho; a lift into M_full requires a splitting. The executed model has an involution with both lifts of order4, so a splitting is not a formal consequence.'),
    reading('LM_C3-644-662', 'C3:651--653',
            'Extra open normal subgroup; natural/sharp superscript; tau versus tau\u2032; amended condition (4)d.',
            'Fix A=C^natural, use conjugators in A semidirect <tau> with retained signs, and require identity on (C/A)/Im(Pi), not necessarily C/A. This differs from restricting only the numerical subgroup D in B.13/B.15. tau(rho)=sigma rho^-1 sigma^-1, so direct inverse conjugacy is not interchangeable when sigma is outside A.',
            'Scan652 photograph inspected and its semidirect product (3) checked. Adjacent formulas use the checked transcription. No decision between natural and sharp is asserted.'),
    reading('LM_C3-644-662', 'C3:656--657',
            'Examples A=Pi and Pi0 after weakening condition (4)d.',
            'The first named proper modular datum is A=closure(Pi), index6; next A=closure(Pi0), index12. Stronger deleted quotient-action conditions cannot silently be carried into the amended definitions.'),
    reading('LM_C3-644-662', 'C3:658--660',
            'Loop definition (18), margin allowing strict inclusion, and antidiagonal (28)--(32).',
            'L_A={l in L0:j(l) in Z^A} may not be contained in A. The smaller quotient is then undefined. B.17 replaces it by the image of A semidirect Z^A in the ambient quotient, with diagonal L_A intersect A. The actual completed modular Pi0 example and its mod4 image prove strictness.'),
    reading('LM_C3-663-681', 'C3:663--664',
            'Normalizer-with-multiplier (48)--(51) and kernel (52 bis).',
            'For the corrected image H_A the exact kernel is P_A/{(l,1):l in L_A intersect A}. Quotienting P_A by all L_A is ill-typed without containment; B.17.2. Injectivity of the loop parameter cannot be assumed when deleting the multiplier.'),
    reading('LM_C3-682-696', 'C3:682--686',
            'Definition (107), image (108), proposed G^natural=M^natural (115), and gamma=Gamma0^natural (116).',
            'Use the open subgroup A as the object stabilized by u, keeping tau-twisted conjugacy and loop data. Equality with the repaired H_A and its quotient is an explicit remaining comparison for A=Pi and Pi0, not a consequence of formal numerical-coordinate constructions.'),
    reading('LM_C3-682-696', 'C3:688--690',
            'Smaller M^{natural,?}, equation (127), and the author\u2019s avoided surjectivity checks.',
            'The image in M^A is exactly the inverse image of im(Nrho^{A,?}) intersect im(Zsigma0^{A,!}) in Gamma0^A. B.18.7 proves this reduction; the two actual images, hence surjectivity, remain to be determined for the named modular A.'),
]

coverage = [
    {'task': 'A.a', 'outcome': 'partly settled', 'statements': 'B.17; B.18',
     'details': 'Adds the exact late dictionary for C3:583--595,635--650 and651--690, including normalized sections, M^0(-j), the index24 quotient, early bisection, extra A=C^natural, multiplier-normalizer kernel, and later smaller fibre product. Named universal profinite source identifications and integral realization remain explicit, distinct assertions.'},
    {'task': 'A.b', 'outcome': 'partly settled', 'statements': 'B.17; B.18',
     'details': 'All used formal multiplication alternatives proved and tested:36 S3 pairs,5184 corrected words,512 cocycle triples,16 sign pairs; finite fibre product192; modular image48. Exact algebraic corrections recorded at594--595,647--650,658--664. The remaining actual profinite subgroup actions, index24 kernel and natural comparison maps are not replaced by a universal-coordinate computation.'},
    {'task': 'B.c', 'outcome': 'partly settled', 'statements': 'B.17; B.18; B.16',
     'details': 'C3:658--660 smaller quotient refuted and repaired with L_A intersect A;663--664 kernel corrected. C3:648--650 bisection exact sequences proved under typed input hypotheses with executed finite model. Remaining: actual unquotiented normalizer section/source identification,635--647 subgroup lattice/kernel,686(115)--(116),689--690 image. No general fppf exactness or integral representability is inferred from profinite groups.'},
    {'task': 'B.g', 'outcome': 'partly settled', 'statements': 'B.17; B.18; B.16',
     'details': 'Keeps numerical signs and multiplier, distinguishes tau from tau\u2032, gives the corrected natural construction, and proves exact fibre-product image reduction. B.16 normalized maps/quotient sections are used. The first proper natural datum is completed Pi in completed SL2(Z), then completed Pi0; exact signed source comparisons and integral lifting remain residual.'},
    {'task': 'Late49.583--595', 'outcome': 'partly settled', 'statements': 'B.18; B.16',
     'details': 'Twisted normalized law, corrected alpha word and sign cocycle are proved and exhaustively tested in finite cases. B.16 supplies normalized conjugators and quotient sections in G_Z. Residual: identify the congruence-defined S0^Pi Gamma! central extension with the source-order cocycle and source object.'},
    {'task': 'Late49.635--650', 'outcome': 'partly settled', 'statements': 'B.18; B.16; D.8; E.19',
     'details': 'Typed bisection formalism and corrected central intersection/quotient target proved;192-element finite model exhibits nonsplitting. Residual: normality/index lattice635--642; exact kernel Nrho* -> GL2(Z/4)/V4 at643--647; actual unquotiented S_sigma and source N_rho? identification.'},
    {'task': 'Late49.651--657', 'outcome': 'partly settled', 'statements': 'B.18',
     'details': 'Records extra open normal A and allowed conjugators A semidirect <tau>; weakened653(4)d acts trivially on (C/A)/ImPi. First named proper A=closure(Pi), next closure(Pi0). These are not the coefficient-only restrictions of B.13/B.15; no deleted stronger condition is silently reused.'},
    {'task': 'Late49.658--664', 'outcome': 'refuted', 'statements': 'B.17',
     'details': 'Literal smaller antidiagonal quotient and denominator L_A are ill-typed when L_A is not contained in A. The universal completed modular Pi0 example proves this; finite mod4 check has corrected image8 versus A4. Full repair, normality, profinite continuity and exact multiplier-kernel quotient are proved.'},
    {'task': 'Late49.682--690', 'outcome': 'partly settled', 'statements': 'B.18; B.17',
     'details': 'Records M^A(107), Z^A image(108), proposed G^A=M^A(115) and gamma=Gamma0^A(116), and smaller M^{A,?}(124)--(128). Proves exact projection-image intersection formula and finite formal case. Remaining: the two actual normalizer images and these comparisons for A=closure(Pi), then closure(Pi0), with the corrected B.17 image.'},
]

for name, data in [('results',results), ('readings',readings), ('coverage',coverage)]:
    (BASE/f'B_late_sections_{name}.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print('B_late_sections: 2 statements (Refuted, Open);',len(readings),'reading records;',len(coverage),'coverage rows.')
print('All count claims reconciled with code/B_late_sections.json; standard library only.')
