#!/usr/bin/env python3
"""Retain the completed A187/A188 source, map, and primary-reference audits."""
from pathlib import Path
import hashlib
import datetime

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
bibpath = w/'SECTIONS_OVER_Q_references.bib'
bib = bibpath.read_text()
addition = (' For A.187 the root reopened I Proposition6.4 and its snake-lemma proof, '
            'printed75, Proposition6.5 and its unramified local-lifting proof, '
            'printed75--76, Corollary6.6 and its proof, printed76--77, and '
            'Remark6.7, printed77. The finite-S hypotheses include the '
            'archimedean places, bad reduction and2; the exact all-place '
            'comparison proves finiteness of the finite2-power Selmer and Sha groups.')
if 'For A.187 the root reopened I Proposition6.4' not in bib:
    start = bib.index('@book{BIR_MilneADT,')
    end = bib.index('\n}',start)
    block = bib[start:end]
    assert block.endswith('}')
    bib = bib[:start]+block[:-1]+addition+'}'+bib[end:]
new_bib = r'''@incollection{RootMilneJV2021,
 author={Milne, James S.},
 title={Jacobian Varieties},
 booktitle={Arithmetic Geometry},
 publisher={Springer}, year={1986}, pages={167--212},
 url={https://jmilne.org/math/xnotes/JVs.pdf},
 note={Verified: author's revised version dated12 June2021 opened. Theorem2.5 and its proof, revised pp.7--8, identify the algebraic Jacobian with the complex period quotient and the point-divisor map with Abel--Jacobi integration. The root read the whole proof and its stated Abel and Jacobi inputs. A.188 derives its cotangent trace and integration-adjoint formulas directly from the moving inverse branches of the actual curve maps. No principal polarization on a Prym is assigned.}
}
'''
if '@incollection{RootMilneJV2021,' not in bib:
    bib = bib.rstrip()+'\n\n'+new_bib
bibpath.write_text(bib)

note = '''# Root audits of the exact two-primary maps and integral reverse isogeny

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

## A.187

The root read the complete saved source in `sections/point3_fermat8_two_primary_selmer.tex` and every line of its local map certificate. The quartic map over k(sqrt(d)) has X=2dt²+2sn and Y=2stX, with inverse t=Y/(2sX), n=(X−2dt²)/(2s). Its image is E′:Y²=X³−4bX and its composition with psi_b is (dt²,dtn). Changing s to −s is translation by (0,0), with X↦−4b/X and Y↦4bY/X². This proves the torsor's exact orientation. Both local Selmer lists in A.185 apply to these full torsors, include endpoint charts, and are attained by global points. The two isogeny Sha kernels vanish; composing the maps proves vanishing of both elliptic two-primary Sha groups.

The unscaled reciprocal elliptic quotients are literally exchanged by the quadratic Galois action. Their pullback sum descends, lands in the connected anti-invariant Prym, and has composite 2+j_++j_−=[2]. The reverse composite also equals[2]; the cross maps are killed by2 and therefore zero as homomorphisms of connected abelian varieties. The actual coinduced-module cocycle formula for Shapiro and its local double-coset partition identify Sha of the Weil restriction with Sha over the quadratic field, including archimedean places. Hence each Prym's full two-primary Sha is killed by2.

For F of A.182, multiplication by N=deg(F) factors through its finite kernel and gives the stated rational homomorphism G with GF=FG=[N]. The target product's two-primary Sha is killed by2. The resulting finite annihilator on Sha(J8)[2∞], its finite Kummer transition images, and the inverse-limit argument on the finite sets of cocycle representatives and cobounding zero-cochains are valid for the actual continuous cohomology. These comparisons commute with every specified homomorphism and localization. The last assertion uses a full Selmer section of the stated open curve, followed by compactification and its actual pointed Abel--Jacobi map; it supplies only that Jacobian image.

The root independently reran the complete map certificate, which passed. The Birational peer read the full saved source and independently reran it, also passing. The Local peer was separately asked to audit the same source. The root reopened Milne ADT I6.4 with its proof (p75), I6.5 with its proof (pp75–76), Corollary6.6 and its proof (pp76–77), and Remark6.7 (p77), at https://www.jmilne.org/math/Books/ADTnot.pdf . The finite-S hypotheses at the start of Section6 were checked: S contains archimedean and bad-reduction places and all primes dividing the coefficient. The already checked I4.15 supplies finite-S cohomological finiteness. The source labels6.6 a Corollary, and the agent's audit note has been corrected accordingly.

## A.188

The root constructed the map H as the literal sum of rational divisor pullbacks. Its first three genus-two components are multiplied by2; every other coefficient is1. The exact generic-fiber counts are16 for each elliptic map,8,8,8,16,16,16 for the six genus-two maps, and8 for each quartic map. All inverse equations are displayed in the source. Every choice recovers the forward functions and satisfies the source curve equation on the given target curve, so these are degree calculations for the specified maps.

The local exact certificate constructs a Groebner basis over the rational function field of each displayed target coordinate pair. It counts the standard monomials in the inverse equations and checks the source equation and both forward coordinates modulo the target relation. It then checks the two additional double covers, all twenty-one distinct character labels and each weighted operator multiplier16. This verifies the finite algebra in the proof; the trace/integration proof itself is written out in the source.

For a finite curve map q, differentiating the sum of Abel–Jacobi integrals over the moving inverse images gives the cotangent trace for divisor pullback. Integration over inverse branches shows that this trace is adjoint to ordinary differential pullback. The trace/pullback composition is therefore deg(q) times the orthogonal projection onto its actual pullback subspace. Invariance of the positive Hermitian integral under μ8² makes the distinct A.182 character lines orthogonal. For the Prym contribution the operator is h* (1−iota) h_*, with its literal inclusion into Jac(D); the anti-involution supplies factor2. No polarization is presumed on the Prym itself. The twelve supports partition the full21-line basis, proving HF=[16] on the cotangent space and then as an actual rational homomorphism by its complex linear lift. Surjectivity of F gives FH=[16]. The stated kernel assertion, the two-power degree of F, the Sha annihilator32 and finite Selmer transition offset5 follow from those exact maps.

The Legendre peer independently checked the inverse fibers and operator argument, then read the full saved source and reran the final certificate. Both audits passed. The primary source for the algebraic/analytic Jacobian comparison is Milne, Jacobian Varieties, Theorem2.5 and its proof in the12June2021 author revision, pp7–8, https://jmilne.org/math/xnotes/JVs.pdf . The root read the whole proof, including its stated Abel and Jacobi integral identities. Search recorded: `site.jmilne.org Jacobian varieties morphism curves pullback transpose norm canonical polarization pdf`. This search supplied the primary source; no exhaustive literature or priority assertion is made.

Both principal A1 assertions remain open. These results strengthen the exact arithmetic quotient comparisons used in the positive-rank route.
'''
note += '\nAudit recorded: '+stamp+'\n'
for name in [
    'code/point3_fermat8_two_primary_maps_certificate.py',
    'code/point3_fermat8_two_primary_maps_root_audit_output.txt',
    'code/point3_fermat8_retraction_certificate.py',
    'code/point3_fermat8_retraction_certificate_output.txt',
]:
    p=w/name
    note += f'\n`{name}`: {p.stat().st_size} bytes; SHA-256 `{hashlib.sha256(p.read_bytes()).hexdigest()}`.\n'
(w/'notes/point3_fermat8_exact_maps_root_audit.md').write_text(note)
p=w/'notes/point3_fermat8_genus2_root_comparison.md'
old=p.read_text()
extra='\nThe Local peer independently read and passed the added direct Weil-reciprocity paragraph, including the moved rational divisor, the actual permuted cocycle and both local-parameter evaluations.\n'
if extra.strip() not in old:
    p.write_text(old+extra)
print('PASS: A187/A188 root exact-map audits retained; primary bibliography updated.')
