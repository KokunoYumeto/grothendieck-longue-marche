# Cuspidal retention and the Green-comparison research history

Current status on 2026-11-16: AG40–AG42 complete the point-separation chain. AG40 proves the conditional criterion; AG41 proves the one-prime relative configuration fiber theorem directly; AG42 constructs the actual cusp-compatible transport and concludes P=Q. All four agents completed independent audits of the combined chain. See `AG40_42_end_to_end_audit.md` and the integrated source.

The notes below preserve the earlier research chronology, including open states and the source-scope discrepancy that prompted the independent proof. Those earlier open statements are superseded by AG41–AG42. The full prime-to-p configuration statement remains separate and is not used.

## Subsequent conditional proof and source-scope audit

The exact Green normalization can be bypassed. The separate file `cuspidal_conditional_separation_draft.tex` proves, conditional on an actual cusp-compatible isomorphism of the two maximal cuspidally pro-r groups over the identity proper group, that P=Q. On the fiber product of the two central extensions, the difference of the transported sections is a cyclotomic cocycle with residues (1,−1). Subtracting its p^e multiple from the Kummer class of f leaves a proper-curve H¹ class, hence a constant. The finite-neighborhood recognition and normalizer argument then give the decisive constant evaluations. Criteria independently audited the full five-step proof; root and F review were requested. It remains a draft, and no unconditional A1 conclusion follows from it.

The missing input is now the existence of that isomorphism at hypothetical exceptional coordinates, with the correct actual cuspidal quotients. Saidi–Tamagawa 2009 Corollary 2.3 explicitly restricts S,T to the complements of the exceptional sets. Its Theorem 2.7 invokes that comparison while its first sentence introduces x*,y*; this is insufficient justification for silently applying the normalized construction to a collision, whose points are exceptional.

A separate source-convention issue was found in both Mochizuki author PDFs: Proposition 1.6(ii) in the LaTeX version, or 1.8(ii) in the 87-page June 2007 version, states a full configuration-fiber preimage assertion under definitions apparently involving maximal pro-Sigma completion of the total geometric group. Taken literally for Sigma=p′, this conflicts with AG39. The February 2014 author comments do not revise that passage. The cited input, Stix's *A monodromy criterion for extending curves*, §2.3, actually completes only the fiber kernel and retains the **full** base fundamental group; it does not justify simultaneous completion of the base. This precise quotient-convention/source-scope discrepancy remains under review. No result depending on the disputed inference has been used to promote the conditional criterion to A1.

Primary source URLs checked for this discrepancy:

- https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations.pdf
- https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(comments).pdf
- https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXMonodromyCriterionIII.pdf

Retrieval audit: turn558view1, turn559view0–3, turn560view0, turn570view0, turn572view0. The comments' repaired decomposition-group recognition was read in full. No general criticism of the paper is inferred from this narrowly identified convention issue.

## Settled input

Let F be a geometric prime-to-p punctured-curve group, K its cuspidal kernel over the full proper group, r≠p, and N=ker(K→K^(r)). Every open I⊂F containing N satisfies I^(r)≅(I/N)^(r). The proof takes the F-core of I and then the F-core of the kernel of a finite r-quotient of I. K's resulting finite image is an r-group extension of an r-group and therefore kills N. Killing the cusp inertia then retains the full proper pro-r group of the compactification of every visible cover. Arithmetic Frobenius gives its exact integer Weil polynomial.

This establishes more than the existence of a few retained cohomology classes. It still does not supply the full proper prime-to-p group of a ramified intermediate curve: AG.39.11 gives dimensions 8 versus 26 at another odd prime in the genus-two cubic example. Nor does a Weil polynomial alone specify an integral p-primary rational torsion exponent or a compatible collection of point lifts in the original unramified tower.

## Exact primary source and its scope

Shinichi Mochizuki, *Absolute Anabelian Cuspidalizations of Proper Hyperbolic Curves*, author version:

https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Cuspidalizations%20(LaTeX%20version).pdf

The exact passages were opened and read:

- Theorem 3.1, printed pp. 80–81 (published numbering 3.10), reconstructs the maximal cuspidally pro-r quotient for one removed rational point from a Frobenius-preserving proper-group isomorphism matching its decomposition group. It does not assume separatedness.
- Remark 10, printed pp. 32–33, distinguishes decomposition-group recognition from point-label injectivity.
- Remark 12, Definition 2.1 and Remark 15, printed pp. 37–38, describe the Green sections in the central diagonal extension and their relation to function evaluation.
- Corollary 3.1, printed p. 85, assumes Sigma-separatedness when concluding global Green compatibility. Its proof uses closure under r-group kernel extensions and then identifies lifted noncuspidal decomposition groups.

Retrieval identifiers retained for audit: turn531view0, turn533view0–2, turn534view0–3. The source was read directly; no assertion that its separatedness hypothesis can be deleted is made.

## The concrete proposed implication

Suppose two distinct rational points P,Q have the same proper prime-to-p section, after choosing representatives. Their Jacobian difference is p-primary; write div(f)=p^e(P−Q). The one-point reconstruction produces an isomorphism between the cuspidally pro-r groups for C−P and C−Q over the identity proper group.

Outside the finite proper exceptional set, a decomposition subgroup has a unique point label. The proposed next step is to use the retained cover zeta functions to recognize noncuspidal decomposition groups in the cuspidally pro-r quotient, and then prove that the induced isomorphism identifies the actual Green sections at (P,R) and (Q,R) for every such R, in one fixed central extension over the proper group.

The normalization matters. The global diagonal extension pulls back along the two point sections. Equality of the base sections suggests a common extension, but equality of transported decomposition subgroups must be checked against the actual Green trivializations inside it. A nonconstant Kummer class on C−{P,Q} can have residues p^e and −p^e even though the relevant global H¹ of the proper curve has only constant Kummer classes. Global extension rigidity alone does not prove the required comparison of these two geometric trivializations.

This is the exact unresolved premise. It is stronger than saying that the two punctured groups have corresponding zeta functions, and it cannot be replaced by simply applying the separatedness-dependent corollary.

## Why a verified constant comparison would be decisive

The following elementary test explains the required strength. Let k be finite of characteristic p, r≠p, and let f∈k(C)×. If there is a class c∈H¹(G_k,Z_r(1)) such that

    κ_{r,k(R)}(f(R)) = res_{k(R)/k}(c)

for every closed point R outside a finite set containing the zeros and poles of f, then f is constant.

Indeed, finite-field Kummer theory gives a∈k× representing c. If f were nonconstant, it would map C over the algebraic closure surjectively to P¹. Choose an r-power root of unity ζ≠1 such that aζ avoids the finitely many excluded image values. A point R over f(R)=aζ has residue field containing ζ. The r-primary Kummer class of ζ in that finite field is nonzero, whereas the assumed equality makes it zero. This is a contradiction. Infinitely many r-power roots of unity are available because r≠p.

Thus a single fixed-prime constant comparison, valid at all closed points outside a finite set, would already settle the proposed collision. What remains unproved is its derivation from the cuspidal isomorphism and the common proper point section.

## Other routes reviewed in this interval

Exceptional-set finiteness does not by itself improve under the available unramified covers: the established pullback identity for exceptional sets makes their geometric size scale with the cover degree, just as g−1 does. No sublinear bound that forces emptiness was obtained. The full-configuration shortcut is ruled out by AG39, and formal cross-prime cuspidal induction loses the cohomology displayed there. These are precise limits of those procedures, not counterexamples to A1.
