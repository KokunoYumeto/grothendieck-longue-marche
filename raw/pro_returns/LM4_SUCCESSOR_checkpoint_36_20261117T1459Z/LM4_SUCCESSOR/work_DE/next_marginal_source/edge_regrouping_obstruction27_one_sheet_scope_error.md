# Actual edge regrouping: four necessary relations and the exact saturation gate

Research, checkpoint27. This carries the failed unchanged-base HNN proposal to a precise quotient construction. It neither declares the new base injective prematurely nor substitutes a plain norm for a corrected actual source word.

## 1. The actual mirror-even ordinary presentation

Retain the notation of `hnn_edge_enlargement_failure26.md` and B125. The proper pre-cross base is

`V=R0 *_K p(R0)`,  `p(r)=j0 r j0`,  `p(u)=eta(u)` for u in K.

Let `K1=CKC`, `k1=CkC`, `a1=CaC`, `v0=p(a a1^-1)`, and

`sigma(CuC)=p(C eta(u) C)`,  `s=v0^-1 k v0`.

The final ordinary mirror-even group has exactly the relative presentation

`G=<V,t | t x t^-1=sigma(x) (x in K1), t k1 t^-1=s>`.

These are the genuine pre-existing HNN relations plus the actual single cross relation. In particular neither t nor any composite replacing it is treated as an unrelated new free generator.

Put `E=C L C`, where L is the actual B117 subgroup `<K,k>`. Its exact finite presentation consists of K1, k1 and the five relations obtained by C-conjugating

`[k,a], [k,d], [k,e], [k,f^-1 B f], [(f k)^2,k]`.

The first four are called leaf relations only to identify this explicit list. The fifth retained-axis relation is also retained.

There are specified images of all generators of E in V, sending K1 by sigma and k1 to s. They do not yet define a homomorphism E->V, precisely because their five relation images need not vanish.

## 2. An actual quotient detecting the four leaf images

The B112/B114 retraction `r:R0->K` fixes K and has

`r(CuC)=zeta(u)`,  `zeta(a)=zeta(B)=zeta(d)=zeta(e)=1`, `zeta(f)=f`,

as well as `r(k)=r(CkC)=1`. Let `q:K->F4(a,B,d,e)` kill f, and set

`lambda=q r Ad(C):R0->F4`.

It kills K and k, and maps `CuC` to q(u). In particular it is onto F4. On the left vertex use the actual base-winding map `R0->Z(z)`, which kills K and sends k to z. These maps agree on the entire amalgamated K, giving an actual epimorphism

`Phi:V -> Z(z)*F4`.

The literal reflection preserves the normal closure of f, as is checked by its full word. Let `e=eta mod f`, an involutive automorphism of F4, and define

`Y_u=a^-1 e(u) a` for `u=a,B,d,e`.

These four words form a free basis: their map is the composition of e with one inner automorphism. Both inverse substitutions are included in the exact certificate. In particular

`Y_a=B a^-1 B^-1`.

The actual images are

`Phi(v0)=a^-1`,  `Phi(s)=a z a^-1`,
`Phi(sigma(CuC))=e(q(u))`.

Consequently the four specified leaf relation images have values

`a [z,Y_a] a^-1`, `a [z,Y_d] a^-1`,
`a [z,Y_e] a^-1`, `a [z,Y_B] a^-1`,

in their stated B117 order. The fifth relation has value one in this particular quotient, because the image of the retained h1=f1 k1 is s and `[s^2,s]=1`. That fifth relation is not omitted from the actual quotient construction below.

## 3. The known actual source commutation is not enough for this regrouping

The exact earlier word comparison is

`U=a v0 sigma(a1) v0^-1`.

Thus `Phi(U)=Y_a`. Quotienting the actual V only by its known source relation `[k,U]` still has an epimorphism onto

`(Z(z) x Z(Y_a)) * F(Y_d,Y_e,Y_B)`.

In this group each of `[z,Y_d]`, `[z,Y_e]`, `[z,Y_B]` is a nontrivial alternating free-product word of length four. Therefore the corresponding three target leaf relations remain nontrivial in `V/normal([k,U])`.

This is a structural all-word obstruction to repairing the edge extension by that single source relation. It is not a numerical target test. It also does not identify these three leaf words with `[m,D_s]` or the corrected e-contact: such identifications are false without the full actual raw-word comparison. In particular it does not conflict with B131's nontriviality of the corrected D-source commutator.

## 4. The target before filling is itself a genuine free-six subgroup

For clarity, the underlying target marking has no hidden relation before filling. The regional retraction proves

`K intersect CKC=1`.

Indeed, if `x=C u C` is in K with u in K, then `x=zeta(u)` and, applying the same argument to u, `u=zeta(x)`. Hence x and u are the same power of f. Such a power commutes with C, and the proved regional cone/neck intersection forces it to be one. This reasoning also applies continuously to the actual closed groups, but no new full topology for V is needed here.

Write `A0=eta(a)` and `q0=p(a1)`. Conjugating the entire proposed target by q0^-1 gives

`k1 -> A0^-1 k A0`,
`CuC -> p(C (a^-1 eta(u) a) C)`.

The latter map identifies K1 with the entire p(K1), since `u->a^-1 eta(u)a` is an automorphism of K. Nonzero powers of the first element lie outside K by base winding. Every nonidentity element of p(K1) lies outside K by the preceding intersection. Ordinary amalgam normal form therefore embeds their free product `Z*F5=F6` in V.

Thus the first necessary quotient replaces an actual embedded free-six target by the exact B117 edge presentation. Its injectivity after that filling cannot be assumed.

## 5. A well-typed initial pushout

Let D be the free group on the six specified generators of E, let `pi:D->E` be the marked presentation map, and let `b:D->V` be the target free-six embedding of Section 4 (before or after the stated common conjugation). Let

`N1=normal_V(b(ker pi))`.

Equivalently N1 is the ambient normal closure of all five exact relation images listed in Section 1. Put `V1=V/N1`. There are now two genuine homomorphisms

`i,j:E -> V1`:

- i is the actual inclusion `E=C L C <= R0 <= V`, followed by the quotient;
- j is the target map induced by b.

The final group G has the exact presentation

`G=<V1,t | t i(e) t^-1=j(e), e in E>`.

The reason this adds no extra relation is that, in G's original presentation, conjugating every actual relation of E by t already kills its target image. Conversely the new presentation retains the original K1 relations and the one actual cross relation. This is a genuine pushout presentation even when i or j has a kernel. It is not yet declared a proper HNN extension.

## 6. Exact kernel matching, without a finite stabilization assumption

There is a precise necessary and sufficient remaining base quotient. Define normal subgroups of V1 recursively by

`M0=1`,
`M_(n+1)=normal_(V1)(M_n, i(j^-1(M_n)), j(i^-1(M_n)))`.

Let `M_infty=union_(n>=0) M_n`, and put `V_infty=V1/M_infty`.
The union is a normal subgroup because the sequence is increasing. The two maps from E to V_infty have the same kernel Q: if i(e) belongs to the union it belongs to some finite stage, so j(e) belongs to the next stage, and conversely. Therefore the two induced maps

`E/Q -> V_infty`

are injective. The group with base V_infty and stable letter t identifying these two embedded images is a proper HNN extension by the ordinary normal-form construction.

This proper HNN extension is exactly G. To prove it, every M_n is killed in G by induction: if one image of e is already trivial, its t-conjugate image is trivial too. Hence G receives the quotient V_infty and satisfies its stable-letter relations. In the opposite direction the proper HNN extension satisfies all original V and cross relations. The two maps fix V and t and are inverse. Ordinary HNN normal form now proves

`ker(V->G) = inverse_image_in_V(M_infty)`.

The notation includes the first quotient N1. Equivalently the kernel is the preimage of M_infty under V->V1. This is an exact description, not an assertion that a few sampled stages stabilize. No subgroup completion or inverse limit is interchanged with this union.

The next concrete normal-form gate is thus to control the actual two kernels `ker i,ker j` and their repeated matching. Equality of the two kernels at the first stage would already make V1 the exact embedded base. Injectivity of both would be a stronger sufficient condition. Neither follows from B117's regional retractions or from the free target before filling.

## 7. Consequence for the actual source kernel and fixed-source gate

The pre-cross actual source F6 lies in V, with its full gap conjugations. Its final discrete kernel is its intersection with the exact base kernel in Section 6. Hence the source-kernel problem can be studied as a specified subgroup intersection with this matching closure. It cannot be replaced by the internal normal closure of the first source commutator, and Section 3 explains why that replacement does not even repair the proposed edge map.

This construction does not decide whether all kernel matching is generated at the first stage, does not determine the entire source intersection, and does not prove the selected-cone centralizer equality. A compact version would require an independently controlled closed saturation and proper completed HNN comparison; none is silently inferred from the discrete union.

## Exact certificate

`check_edge_regrouping27.py/.out/.err/.json` independently reads the certified actual eta table and checks 25 exact free-word identities: eta squared, its quotient after killing f, both complete inverse Y-basis substitutions, all four leaf images, the known U image, and the retained-square image. The actual retractions, free-product arguments, and saturation proof above are uniform mathematical proofs, not deductions from those finite checks.

## 8. A separate exact finite-target characterization

The compact comparison can be specified without taking the closure of the discrete union in Section 6. Keep the two actual homomorphisms i,j:E->V1. Let B be the family of all finite-index normal subgroups N of V1 satisfying

`i^-1(N)=j^-1(N)`.

This family describes exactly the restrictions of finite quotient kernels of G to V1. Necessity is immediate from the actual stable-letter equation: in any finite target, the two images of an element of E are conjugate, so one is trivial exactly when the other is trivial.

For sufficiency, take such an N. Put F=V1/N and Q=i^-1(N)=j^-1(N). The two edge images are isomorphic copies of the finite group E/Q in F. On the finite set F, represent F by its faithful left regular action. The restrictions of this action through the two edge embeddings are free actions of the same finite group E/Q. They have the same number of orbits. Choose a bijection between their orbits and an equivariant bijection on each pair. The resulting permutation t_star conjugates the first entire edge action to the second. Consequently the faithful regular map F->Sym(F), together with t->t_star, defines a homomorphism from the ACTUAL G to the finite symmetric group. Its restriction to V1 has kernel exactly N. No residual-finiteness theorem for an unspecified HNN extension is needed.

Let Nhat denote the corresponding open normal subgroup of V1hat. It follows directly, by intersecting all finite quotient kernels, that

`ker(V1hat -> Ghat) = intersection_(N in B) Nhat`.

The family B is closed under finite intersections, since equality of the two preimages is preserved under intersections. Thus it gives a concrete compatible finite-kernel system. An equivalent formulation uses the continuous extensions from Ehat to V1hat; the equality of their open kernels is equivalent to the equality on the dense discrete E.

This formula is proved independently of the union M_infty. Every matching N contains M_infty, by the induction in Section 6. Therefore closure(M_infty) is contained in the displayed compact kernel. Equality would require the additional cofinal finite compatibility needed for the full topology of the discrete embedded base V_infty in G. Neither equality nor that topology is asserted.

The actual source completion maps to V1hat, and its final kernel is the preimage of this exact intersection of matching open normals. The newly proved pre-cross source full topology in B133 also identifies the same kernel as the actual closed normal-cross intersection inside Ahat. These two descriptions retain their different ambient maps. In particular no inverse limit, completion, or source intersection is exchanged with the countable saturation union.
