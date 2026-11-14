# Independent adversarial review: RNS and the full local cyclotomic fixed subgroup

**Reviewer:** `/root/topos`. **Date:** 14 November 2026. **Final outcome:** the complete written Claim C.7h in `sections/C_RNS_full_fixed_extension.tex` passes independent adversarial review. The exact RNS hypotheses and its cited Topics IV dependency were independently checked. No mathematical correction is required.

## Exact primary clauses opened

Mochizuki–Tsujimura, *Resolution of nonsingularities, point-theoreticity, and metric-admissibility for p-adic hyperbolic curves*, author PDF revised30March2024, <https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf>. I opened the primary PDF and read the complete local text of Definition2.2(i)–(ii), Proposition2.3(v) and the relevant proof, Proposition2.4(vii) including its proof, and Theorem2.17.

Proposition2.4(vii) really has two distinct clauses. Uniqueness of an H-fixed primitive valuation requires a prime ell∈Sigma−{p} and a continuous surjection H∩I_K→Z_ell. Openness of the ell-adic cyclotomic image is used only for existence. For a given actual point or cusp section the required primitive valuation is already constructed explicitly, so the cyclotomic kernel's trivial character does not violate the uniqueness hypothesis.

Theorem2.17 supplies Sigma-RNS for a p-adic local field whenever Sigma contains p and at least one other prime. In particular it applies to the full profinite group. It does **not** supply this RNS hypothesis for the prime-to-p group; the distinction is essential and prevents a contradiction with the prime-to-p good-reduction fixed subgroup.

## 1. The inertia hypothesis for the cyclotomic kernel

Put H=G_{K(mu_infinity)}. Every closed commutator of G_K lies in H. Write T=prod_{ell≠p}Z_ell(1) for tame inertia. In the tame quotient, conjugation by an arithmetic Frobenius acts by q, where q is the residue cardinality. Hence commutators of a Frobenius lift with inertia lifts have tame images (q−1)T. These commutators belong to both H and I_K. For any ell≠p their images contain the nonzero open subgroup (q−1)Z_ell of the ell-primary tame factor.

If H' is open in H, then H'∩I_K has finite index in H∩I_K. Its ell-primary tame image is consequently a nonzero open subgroup of Z_ell. It is compact, hence closed, and as a topological group is isomorphic to Z_ell. The projection onto its image followed by this isomorphism is the continuous surjection required by Proposition2.4(vii). No claim that H is open in G_K is made, and no cyclotomic openness is needed.

This argument covers p=2 as well. The positive integer q−1 is nonzero in every Z_ell; it need not be a unit.

## 2. The correct composite valuation is primitive

Let F be the **algebraic** function field of the universal geometrically pro-Sigma cover, containing Kbar. Choose the compatible geometric point xi of the normalized compactified finite covers fixed by the actual point section, or by the chosen cuspidal section. Let A be its horizontal valuation ring in F. Its residue field is Kbar: this holds at every finite geometric level and constants are retained in F. Let ev:A→Kbar be the residue map and define

\[
R=\operatorname{ev}^{-1}(\mathcal O_{\overline K}).
\]

This is the composite valuation in the order **horizontal place first, then p-adic valuation of the residue**. It restricts to O_K on K.

For primitivity, let m_h be the kernel of ev. It satisfies p^{-1}m_h=m_h, so m_h⊂pR. Every prime ideal of R containing p therefore contains m_h. Its image in R/m_h=O_Kbar is a prime containing p. This rank-one valuation ring has only its maximal prime containing p. Consequently R has exactly one prime containing p, its maximal ideal. This is precisely Definition2.2(i).

The order of composition matters. RNS Remark2.3.4 gives a nonprimitive valuation by first taking a vertical component and then a residue-curve point: its intermediate prime already contains p. That is the opposite order and is not the ring used here.

## 3. Recovery of the horizontal place by inverting p

One has the literal equality

\[
R[1/p]=A.
\]

One inclusion holds because p is a unit in the horizontal valuation ring A. For the other, if f∈A has residue zero then f∈R. If its residue alpha∈Kbar is nonzero, choose an ordinary integer N≥0 with p^N alpha∈O_Kbar. Then p^N f∈R, so f∈R[1/p]. The residue's valuation is a finite rational number; no completion of the function field or nonalgebraic coefficient is introduced.

Multiplying a horizontal pole by powers of p never makes it regular at xi. Thus this operation retains exactly the horizontal place, not merely its image in a model or a coarser Berkovich point.

## 4. Section invariance and the centralizer argument

The actual point section fixes xi by its definition as the arithmetic decomposition subgroup of that geometric pro-point. A cuspidal section lies in the corresponding cusp decomposition group and fixes the same compactified pro-point. In either case its action on the residue Kbar is the specified coefficient action of G_K, which preserves O_Kbar. Hence it preserves R.

If z∈Pi centralizes the restriction of the section to H', then zR is another H'-fixed primitive p-valuation. The action preserves K and p, so zR is again a p-valuation with the same primitivity property. Proposition2.3(v) identifies these valuations with the primitive centre chains, equivariantly, and Proposition2.4(vii) gives zR=R. Inverting p gives zA=A.

The geometric stabilizer of A is its horizontal inertia. This can be checked at finite Galois levels: above an ordinary point of U every finite cover is étale, and over Kbar the residue decomposition is trivial, so the geometric stabilizer is trivial. Passing to the inverse limit keeps it trivial. Above a boundary point the inverse-limit stabilizer is exactly the full pro-Sigma cusp inertia. No vertical decomposition group or p-adic inertia is substituted for this horizontal stabilizer.

Therefore the fixed subgroup is trivial for an ordinary point section. For a cusp section it is contained in cusp inertia. Conversely conjugation on that inertia is the cyclotomic character; a tangential cocycle does not change this action because inertia is abelian. Since H'⊂ker(chi), the entire cusp inertia centralizes H'. Thus equality holds for a cusp section, with no integrality condition on its tangent class.

## 5. Scope

This argument proves the claimed full-group point/cusp formula for any reduction type over a p-adic local field, and in fact for any pro-Sigma group with p∈Sigma and |Sigma|≥2 for which the stated universal-cover construction is used. The local theorem D.6/D.19 is needed only if the conclusion is extended from actual point/cusp sections to arbitrary continuous sections. The three-punctured-line point2 and integral tangent at0 require no such existence theorem: their sections are explicit.

The proof does not apply to the pure prime-to-p quotient unless Sigma-RNS is separately supplied there. It therefore does not collapse the distinct prime-to-p bad-reduction analysis.

**No precise gap found in the source match, inertia hypothesis, primitive valuation, recovery by R[1/p], or stabilizer argument.**

## 6. Final written-candidate pass

I read the entire integrated Claim C.7h and its proof after its move from the audit candidate to `sections/C_RNS_full_fixed_extension.tex`. Its additional assertion H⊂I_K is correct: prime-to-p roots of unity generate the maximal unramified extension of the finite p-adic field K. Thus its use of H′ rather than H′∩I_K is justified. The proof does not accidentally assume that H′ is normal or that the tame image equals a chosen full lattice; an open nonzero image is topologically Z_ell, which is precisely enough.

I also read the full statement of Hoshi–Mochizuki, *Combinatorial anabelian topics IV*, Corollary1.15, and the relevant proof. Its standing hypothesis is that H∩I_K has open image in the pro-Sigma-dagger tame inertia. Taking Sigma-dagger={ell} gives the required condition. Part(iii) separately introduces cyclotomic fullness for existence. Part(iv) uses the previously defined set Stab(s), but does not inherit that extra existence hypothesis: its proof invokes Lemma1.11(ii), not part(iii)'s existence argument. This confirms the literal source dependency of RNS Proposition2.4(vii)'s uniqueness clause.

The integrated statement correctly includes every continuous section into the fixed cusp decomposition group D_c. The argument uses preservation of the cusp and the cyclotomic action on its abelian inertia; it does not require the corresponding completed Kummer class to be represented by an actual tangent coefficient in K*. Its final point-uniqueness consequence concerns the underlying ordinary point or cusp only, and explicitly avoids claiming uniqueness of a tangent vector.

This is a source-based deduction for the full group, valid for all reduction types. The limitation to prime sets containing p remains essential. No passage silently transfers the result to the prime-to-p quotient.
