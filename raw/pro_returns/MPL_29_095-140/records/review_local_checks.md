# Independent mathematical review of local checks P1–P5

Reviewed on 2026-11-18 by `/root/notes_torsors`, at the parent's request, after transcription freeze. This is a targeted mathematical peer review of `records/notes_local_support.md`, not an image review. No source image or crop was opened, and the reviewed support file was not edited. Frozen text for scans133 and135 was read solely to distinguish the stated mathematical checks from the uncertain source wording.

## Outcome

**P1–P4 are sound under their stated hypotheses. P5's calculation is sound and proves the stated distinction when “between algebraically closed fields” is kept explicit.** Two scope qualifications matter: P4's discussion of the source's inserted neighborhood condition assumes an appropriate étale/finite-presentation model, and P5 should say “different condition” rather than claim a generally “stronger condition” without proving that implication.

| Check | Exact reviewed statement | Verdict |
|---|---|---|
| P1 | For arbitrary commutative unital A and ideals I,J, A/IJ→A/I×A/J is surjective iff I+J=A, in which case it is bijective; equality I∩J=IJ alone gives injectivity. | Sound, including the counterexample (x),(y)⊂k[x,y] to the added converse. |
| P2 | Without constant component ranks, comaximal ideal factors of a monic principal ideal need not have global monic generators. | Sound: A=k×k, P=T, J=k[T]×(T), J′=(T)×k[T]. |
| P3 | If A≠0 has connected spectrum, P is monic, J+J′=A[T], and JJ′=(P), then there are unique monic Q,Q′ with J=(Q), J′=(Q′), P=QQ′. | Sound over arbitrary such A, including rings with nilpotents and zero divisors; no noetherian or completeness hypothesis is needed. |
| P4 | Cartesian cocycle-compatible quasi-finite étale separated objects over every local scheme Spec O_s need not arise from an étale object over S. | Sound: the proposed global image on Spec Q[t] is not open. This does not prove sufficiency of the source's added condition. |
| P5 | For the finite étale functor represented by Spec C/R, invariance under all algebraic separable extensions fails, but invariance under extensions between algebraically closed fields holds. | Sound for these exact quantifiers. It does not decide the source reading or compare the full representability criteria. |

## P1: CRT proof and converse counterexample

I checked both directions of surjectivity independently. The preimage of (1 mod I,0 mod J) gives an element a∈J with 1−a∈I, and hence I+J=A. Conversely, from u∈I, v∈J, u+v=1, the element xv+yu maps to any prescribed pair of residues (x mod I,y mod J). The kernel is exactly (I∩J)/IJ. Under comaximality, z∈I∩J satisfies z=zu+zv∈IJ, completing the asserted equivalence with bijectivity.

For k[x,y], the reduction-mod-x argument proving (x)∩(y)=(xy) is valid: if h=yb lies in (x), then y·b̄=0 in the domain k[y], so b̄=0. The sum (x,y) is proper. Thus equality of the intersection and product does not imply comaximality. No finiteness, Nakayama, domain hypothesis on general A, or properness hypothesis on I,J has been silently used.

**Limit:** this verifies the corrected algebraic statement and the explicit counterexample to the strengthened contextual assertion. It does not re-audit the source diagram's handwriting.

## P2–P3: connected-base monic-factor proof

### Disconnected example

In P2, J+J′=A[T] and JJ′=(T)×(T)=(P) are correct. A globally monic polynomial over k×k has monic component polynomials of the same degree: its leading coefficient is (1,1). A generator of k[T] in the first component must be the monic constant1, while a monic generator of (T) in the other must be T. The degrees cannot agree. This is a genuine counterexample to the formulation without rank control.

### Complete check of the characteristic-polynomial argument

1. P1 gives C=A[T]/(P)≅C₁×C₂, with C₁=A[T]/J and C₂=A[T]/J′. Since P is monic of degree n, C is a free A-module of rank n. The two Cᵢ are direct summands and are therefore finite projective.
2. Their rank functions are locally constant. Connected Spec A makes each constant, dᵢ, with d₁+d₂=n. No assumption that A is a domain or reduced is needed here.
3. Multiplication by T on Cᵢ has a globally defined monic characteristic polynomial Qᵢ of degree dᵢ. It can be defined on finite free local trivializations, where it is invariant under change of basis, and those coefficients glue. Thus the use of characteristic polynomials on projective modules is valid; a global basis of Cᵢ is not assumed.
4. Cayley–Hamilton holds after localization on those trivializations, hence globally. Applied to 1∈Cᵢ, it yields Qᵢ(T)=0 in Cᵢ. The quotient map therefore gives a surjection A[T]/(Qᵢ)→Cᵢ.
5. The source of this surjection is free of rank dᵢ. At every prime of A, the target is also free of rank dᵢ; surjectivity makes the square matrix invertible modulo the maximal ideal of the local ring, so its determinant is a unit. The map is an isomorphism at every prime and therefore globally. This establishes J=(Q₁) and J′=(Q₂); there is no unjustified assertion that an arbitrary quotient of a free module is free.
6. On C, multiplication by T has the companion matrix of P, so its characteristic polynomial is P. The direct-sum decomposition of the underlying module gives the product Q₁Q₂. Determinants can be checked on local trivializations, hence P=Q₁Q₂ globally.
7. If two monic polynomials generate the same ideal, each divides the other. Multiplication by a monic polynomial adds degrees even when A has zero divisors: the leading coefficient of the other factor survives multiplication by1. The two divisibilities force equal degrees and constant multipliers, and leading coefficients force those constants to equal1. This proves uniqueness.

The degree-zero case is also covered. P=1 gives C=0 and both factors equal1; a rank-zero Cᵢ is the zero module and has characteristic polynomial1. Excluding the zero ring A avoids conventions about the degree and monicity of the zero polynomial.

**Limits:** connectedness is a sufficient rank condition, not a logically necessary one. The same proof works over a disconnected A if both Cᵢ have globally constant ranks. This proof establishes the independent mathematical refinement; it does not recover the unfinished completion-based source argument or silently add a completeness hypothesis.

## P4: localization data and the non-open-image contradiction

### The local objects meet the claimed hypotheses

For S=Spec Q[t], every non-generic point is a closed point associated with an irreducible polynomial p. Its local ring A_p=Q[t]_(p) is a DVR. Inverting p in A_p inverts every nonzero polynomial because all other irreducible factors are already units, so A_p[1/p]=Q(t)=K.

Consequently Spec K→Spec A_p is the **principal open immersion D(p)**. It is quasi-finite, separated, étale, and of finite presentation. The distinction between this local map and the global map Spec K→S is essential: the global localization is not of finite presentation, while the local one is.

The choices X(s)=Spec A_s for integer rational points s∈E, X(s)=Spec K for all other closed s, and X(η)=Spec K therefore satisfy the prescribed local properties. Every nontrivial specialization chain is just η→s. The corresponding square is Cartesian because either A_s⊗_{A_s}K=K or K⊗_{A_s}K=K. Identities and compositions introduce no extra constraint in dimension one. Thus the example satisfies the stronger Cartesian transition requirement, not merely the weaker prose version in context.

### The proposed global object cannot exist

If an étale X→S induced these local objects, its fibre over s∈E would be Spec k(s), over every closed s∉E would be empty, and over η would be Spec K. Its image would be exactly {η}∪E.

An étale morphism is open. Every nonempty open subset of Spec Q[t] contains a nonempty principal open D(f), whose complement consists of finitely many closed points; therefore every nonempty open subset has finite complement. But the complement of {η}∪E contains the infinitely many distinct points (t−1/m), m≥2. This is a contradiction. It rules out any étale global realization, and therefore also the more restrictive quasi-finite separated étale realization in the proposed lemma.

### Scope of the neighborhood-model discussion

The final paragraph of P4 correctly states its additional assumption: the neighborhood model is taken in the natural quasi-finite étale category. If such a model has a nonempty fibre at s∈E, its open image contains a neighborhood of s. Maps from all its local restrictions to X(t) force its fibre at each closed t∉E to be empty, which is incompatible with that open image. This verifies the paragraph under its explicitly stated model hypothesis.

If “model” meant an **arbitrary** scheme over an open neighborhood, the conclusion about the added condition would no longer follow. One could take the whole neighborhood S and use Spec O_s as the model for s∈E and Spec K otherwise; for distinct closed s,t, O_s⊗_{Q[t]}O_t=K, giving the needed maps to the prescribed X(t). These global localization models are not of finite presentation over S. Thus a geometric/finite-presentation restriction on “definition over a neighborhood” matters, and the uncertain source insertion should not be resolved by this mathematical check. The robust result is the counterexample to Cartesian localization data alone; the sufficiency of the full inserted hypothesis remains unproved here.

## P5: exact field-extension quantifiers

The calculation F(k)=Hom_R-alg(C,k)={roots of U²+1 in k} is correct. F(R) is empty, F(C) has the two elements i and−i, and C/R is an algebraic separable extension. For any inclusion k⊂k′ of algebraically closed fields over R, both roots already belong to k and a quadratic polynomial gains no further roots in k′, so F(k)→F(k′) is bijective.

This proves the two specific invariance properties differ, even for the finite étale representable functor in question. Two qualifications should remain visible in the final note:

- It distinguishes **extensions between algebraically closed fields** from **all algebraic separable extensions**. It does not distinguish invariance under k→an algebraic closure of an arbitrary k from the separable version: R→C would fail both. The frozen scan133 wording remains uncertain, and the calculation cannot decide which reading was intended.
- Calling one condition “stronger” is not justified as a general logical implication by this example. Arbitrary extensions between algebraically closed fields may be transcendental, whereas Hua's quoted condition concerns algebraic separable extensions. For a simple field-functor illustration, on Q-fields take the singleton {0} for fields algebraic over Q and the two-element set {0,1} for fields transcendental over Q, with the evident inclusion maps; it is invariant under algebraic extensions but changes from Q̄ to an algebraic closure of Q̄(t). This illustration is only about the quantifiers and is not offered as a functor satisfying the full representability criterion.

Therefore the safe conclusion is **different invariance conditions**, with the exact between-algebraically-closed-fields formulation stated. No implication involving the criterion's other hypotheses, no proof of that criterion, and no refutation of its implication has been established in P5 or this review.

## Recording this review

This review is a **targeted proof check** independently performed after the original local support proofs. The parent may record separate events for P1–P5 using its eventual refined statement IDs. P3 may additionally be described as independently re-proved in this review because the entire finite-projective and characteristic-polynomial argument was reconstructed and checked; P4's local geometry and image contradiction were also independently reconstructed.

The review uses standard background facts about finite projective modules, Cayley–Hamilton, principal open immersions, and openness of étale morphisms. It does not claim a separate foundational proof of those background results. No computation or formal-certificate event should be inferred: this was a mathematical proof review, not a computer algebra calculation. No event is proposed merely for reading the frozen source or comparing its uncertain phrases.
