# Frobenius combined with the cubic deck action and hyperelliptic involution

Status: independently reviewed by root and integrated as A.29f. It builds on the approved A.29d–A.29e and makes no universal assertion about all ordinary elliptic auxiliaries.

## Statement

Let B:y²+y=(s³+b)+a/(s³+b), ab≠0, over F_q containing μ₃. Use the Prym A and γ(P)=[P−δP] of A.29d. Let Φ be q-power Frobenius. Its action on the rank-one module T₂A over O=Z₂[ζ₃] is multiplication by λ∈O*. For ε∈μ₆=〈ζ₃,−1〉, choose the corresponding automorphism a_ε=δ^jι^e of B, and let Ψ=a_ε∘Φ^u, where u≥1.

If b_ε,u=v₂(ελ^u−1)≥2, then every 2-primary γ-value has order at most2^{b_ε,u}. Every point with a nonzero such value is fixed by Ψ. In particular, if b_ε,u is2 or3, the nonzero packet consists only of the three finite Weierstrass points.

If the elliptic branch pair has exact order3, this last condition proves A1 for B over every finite extension, by the translated-cover argument of A.29e.

There exists such a pair (ε,u) with valuation2 or3 if and only if the reduction of λ modulo16 does not lie in the reduction of μ₆. When it exists, one can choose u=1 or2.

## Proof of the geometric equivariance

The cubic deck transformation δ and the hyperelliptic involution ι commute and are defined over F_q. They both fix infinity. The involution acts by−1 on the Jacobian, so

\[
 \gamma(\delta P)=\delta\gamma(P),\qquad
 \gamma(\iota P)=-\gamma(P),\qquad
 \gamma(\Phi P)=\Phi\gamma(P).
\]

Thus γ(ΨP)=ελ^uγ(P) on geometric 2-primary points. The map Ψ preserves the non-Weierstrass locus and permutes geometric points bijectively. Nothing in the argument requires Ψ to be a Galois automorphism: the curve maps and these equivariance identities suffice. Its iterates correspond to the powers of ελ^u because all the factors commute.

Put θ=ελ^u and b=v₂(θ−1)≥2. This valuation is finite: θ=1 would imply λ^{6u}=1, contradicting that Φ^{6u}−1 is an isogeny with finite kernel. If D=γ(P) has exact order2^a with a>b, then

\[
 v_2(\theta^{2^{a-b-1}}-1)=a-1.
\]

Hence γ(Ψ^{2^{a-b-1}}P)−γ(P) is nonzero 2-torsion. A Weierstrass point has γ-order at most2, so P and its image here are both non-Weierstrass; A.29d excludes this difference. Thus a≤b. It follows that θD=D. For D≠0, the unique-preimage assertion for γ gives ΨP=P. The zero fibre is the three-point deck-fixed locus and requires no uniqueness assertion.

If the order of a_ε is d dividing6, then Ψ^d=Φ^{ud}; thus every nonzero packet point lies in F_{q^{ud}}. The two affine zero-fibre points lie in at most a quadratic constant extension. No claim that every zero-fibre point is fixed by Ψ is needed or made.

For b≤3, A.29e excludes every non-Weierstrass value of order2,4,8, so only the finite Weierstrass triple remains. The exact-order-three branch hypothesis is used only in the translated-cover elimination, not in the Frobenius bound or small-order exclusions.

## The exact arithmetic predicate modulo16

Choose ξ∈μ₃ such that λ/ξ has residue1 in F₄. Write v=λ/ξ∈1+2O.

If v modulo4 is neither1 nor−1, write v=1+2c. The residue of c is one of the two elements of F₄ outside F₂. Therefore c and1+c are both units, and

\[
 v_2(v^2-1)=v_2(4c(1+c))=2.
\]

Take u=2 and ε=ξ^{−2}.

If v≡1 modulo4 and λ modulo16 is not a sixth root of unity, then v≢1 modulo16. Hence v₂(v−1) is2 or3; take u=1 and ε=ξ^{−1}.

If v≡−1 modulo4, the same argument applied to−v gives valuation2 or3 for−v−1; take u=1 and ε=−ξ^{−1}.

Conversely, if λ modulo16 belongs to μ₆, then every ελ^u modulo16 also belongs to μ₆. Among the six roots of unity, only1 is congruent to1 modulo4: the nontrivial cube roots already differ modulo2, and−1 differs modulo4. Therefore any such ελ^u with valuation at least2 is actually1 modulo16 and has valuation at least4. This proves both directions and the bound u≤2.

This predicate can equivalently be tested by the degree of the étale isogeny εΦ^u−1: its 2-adic valuation is2b_ε,u, since O has residue degree2. The isogeny is étale because Frobenius has zero differential and−1 has invertible differential. The criterion asks for that degree valuation to be4 or6.

## Concrete effect on earlier computations

If v₂(λ^u−1)=1 and v₂(λ^{2u}−1)=c, then

\[
 v_2(\lambda^u+1)=c-1.
\]

Thus a large untwisted bound c=3 or4 can be replaced by a twisted bound2 or3. For A.29c, the saved counts give c=3 at u=3, and using ιΦ³ bounds the packet exponent by4. For the four cube-parameter cases in the F16 survey, c=4 at u=1, and using ιΦ bounds the exponent by8. The existing finite certificates remain independent verification; neither their finite scope nor a generic-density claim is used in this proof.

## Exact limit

The remaining arithmetic case for this mechanism is λ modulo16 lying in μ₆. Passing to a larger constant field can force this condition rather than remove it. No argument that it never occurs for a minimal field of definition is supplied. The higher translated-cover method and higher-order norm equations remain distinct possible routes; this lemma does not silently resolve them.


The standard-library certificate `code/A_twisted_frobenius_certificate.py/.json` verifies all192 units in O/16. It records186 witnesses with u=1 or2 and exactly six excluded roots of unity. This checks the finite residue predicate independently of the general unit-group proof.
