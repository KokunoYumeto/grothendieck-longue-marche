# Continuation: local elliptic realizations and the transcendental-base kernel

These notes supplement `birational.md`. They do not solve A1 or B1. They contain two additional concrete results: an infinitely ramified representation which is an elliptic Tate module at every completion, with one fixed coefficient prime; and an explicit description of the field and diagonal inertia omitted by a proposed birational base change. The full system of representations supplied by a section of the tripod is retained as an unresolved additional constraint.

## 1. Opened primary sources

- C. Khare, M. Larsen, R. Ramakrishna, *Constructing semisimple p-adic Galois representations with prescribed properties*, Amer. J. Math. **127** (2005), 709–734. Opened author preprint <https://arxiv.org/pdf/math/0309283>. The arXiv version numbers its principal result **Main Theorem**, on manuscript pages 3 and 20; the local deformation description is **Definition 1, equation (3), Definition 2**, on pp. 7–8, and the construction is **§2.2**. **Corollary 14** is on p. 23. Publication metadata independently opened on the author's Cornell page <https://math.cornell.edu/ravi-ramakrishna>. The DOI 10.1353/ajm.2005.0026 was found in metadata, but its publisher resolver did not open; the theorem numbering here is explicitly that of the opened preprint. Web refs: `turn56view0`, `turn56view1`, `turn70view0`, `turn70view1`, `turn65view0`.
- C. Khare, C. S. Rajan, *The density of ramified primes in semisimple p-adic Galois representations*, IMRN **2001**, no. 12, 601–607, **Theorem 1**. Opened <https://arxiv.org/pdf/math/0011272> and publisher metadata <https://academic.oup.com/imrn/article-abstract/2001/12/601/750628>. The theorem gives density zero of the ramified places for a continuous semisimple representation into GL_m of a finite extension of Q_p. Web refs `turn54view1`, `turn58search0`.
- W. C. Waterhouse, *Abelian varieties over finite fields*, Ann. Sci. École Norm. Sup. (4) **2** (1969), 521–560, **Theorem 4.1**, printed p. 536. Opened <https://www.numdam.org/article/ASENS_1969_4_2_4_521_0.pdf>; bibliographic record <https://www.numdam.org/articles/10.24033/asens.1183/>. For a prime q≥5 every integer a with |a|≤2√q is the trace of an elliptic curve over F_q: nonzero a is prime to q, and a=0 is the odd-exponent case of part (5). Web refs `turn76search24`, `turn77view1`.
- G. Bresciani and F. Pop: the opened primary sources and theorem numbers are recorded in `birational.md`. Pop's preprint <https://arxiv.org/html/2604.26131v1>, Definitions/Remarks 1.2, Definition 1.5, Remarks 1.6 and Theorems 1.3/1.7 were reopened. Its t-lift still has a domain involving k(T). No theorem of that preprint is used in the two proofs below. Its header/body date discrepancy remains as recorded earlier.

Targeted searches included “infinitely ramified strictly compatible systems all primes”, “compatible family infinitely ramified”, “pure compatible system finite ramification”, and “Compatible systems and ramification”. The latter led to Lu–Zheng (2019), whose setting is schemes over the integers of one local field and does not supply the sought global finite-support conclusion. No theorem eliminating the finite-support input for the full Legendre system was established by this search. This is a report of what was checked, not a universal nonexistence claim about possible theorems.

## 2. An actual single-coefficient counterexample with local elliptic realizations

There exists a continuous representation

    ρ:G_Q→GL_2(Z_7)

with all the following properties:

1. Its residual representation is surjective, and ρ⊗Q_7 is absolutely irreducible.
2. det(ρ)=χ_7.
3. ρ is ramified at infinitely many rational primes; that set has density zero.
4. For every finite prime q there is an elliptic curve E_q/Q_q and an isomorphism of Z_7[G_{Q_q}]-modules ρ|_{G_{Q_q}}≅T_7(E_q).
5. E_7 can be taken to be the restriction of the fixed curve E:y²=x(x−1)(x−3). In particular, at its coefficient prime the representation is crystalline with the elliptic Hodge–Tate weights.
6. At every unramified q≠7 the Frobenius polynomial is X²−a_q X+q with a_q∈Z and |a_q|≤2√q.

This assertion concerns **one coefficient prime 7**. It does not construct a section of the tripod or an all-prime family with one common E_q realizing every coefficient at q.

### 2.1. A concrete initial residual representation

Take E:y²=x(x−1)(x−3). Its invariants are Δ=576 and c_4=112. At 3 it has multiplicative reduction because v_3(c_4)=0, and its minimal discriminant has valuation 2. The displayed integral equation is minimal at 3: a nonminimal integral equation would have discriminant valuation at least 12. Tate uniformization, after the unramified quadratic extension in the nonsplit case, gives an inertia element acting on E[7] as a nontrivial transvection; its upper-right entry is 2 times a generator of the mod-7 tame character. An unramified quadratic twist leaves this inertia action unchanged.

Direct counting gives #E(F_5)=4. Hence a_5=2, and the mod-7 Frobenius polynomial at 5 is X²−2X+5. Its discriminant is 5 modulo 7, a nonsquare. Thus the residual representation is irreducible over F_7.

For completeness this also proves its full image without an appeal to the classification of subgroups of GL_2(F_7). Let u be the transvection and L its unique fixed line. Irreducibility supplies g with gL≠L. In a basis along L and gL, u and gug^{-1} are nontrivial upper and lower unipotent matrices. Their powers contain all upper and lower elementary unipotents over the prime field F_7. These generate SL_2(F_7). The determinant is the mod-7 cyclotomic character, hence is onto F_7^×. Therefore the residual image is GL_2(F_7). In particular it is absolutely irreducible.

The exact point count, discriminant, valuations and good reduction at 7 are checked by `code/locally_elliptic_residual_certificate.py`, with output in the adjacent `_output.txt` file.

### 2.2. Choices in the opened KLR construction

Apply KLR §2.2 with coefficient prime 7, determinant χ_7, and residual representation E[7]. Include 2,3,7 in the initial finite set S. The proof, at the beginning of §2.2, allows a specified characteristic-zero local lift at every place of S. Choose T_7(E) at all of them, including any initial auxiliary places used to kill the relevant obstruction group. Start the mod-49 lifting process with E[49].

For the finite initial set R_2 of unramified primes, choose the actual Frobenius polynomials of E. These choices are already compatible with E[49], so they satisfy the required initial congruences and are pure of weight one. At all subsequently assigned unramified primes the trace choice in KLR §2.2 is an integer in the Hasse interval: the modulus at that stage is smaller than the available interval because those new primes exceed the bound prescribed in the construction. Thus the finitely many possible initial purity exceptions in the general Main Theorem are absent for these choices.

At every newly introduced auxiliary place q, choose the ramified branch A=0 in KLR equation (3), and choose a nonzero characteristic-zero value B lifting its finite-level value. Such a value exists even if the finite-level value is zero. The proof fixes the chosen local lift at subsequent stages. KLR's Main Theorem, Remark 1, and the paragraph immediately following the proof of the Main Theorem explicitly allow ramification to be forced at infinitely many auxiliary places. This gives ρ and retains all initially fixed local Tate modules.

Absolute irreducibility follows from the absolutely irreducible residual representation: a stable line after a finite coefficient extension, intersected with a stable lattice and saturated, would reduce to an invariant line after residue extension. The density assertion is then Khare–Rajan Theorem 1.

### 2.3. Identifying every auxiliary local representation with a Tate curve

For a new auxiliary place q, KLR's local model, with determinant χ_7, has the form

    ρ(Frob_q)=ψ(Frob_q) diag(q,1),
    ρ(τ_q)=[[1,B],[0,1]],

where ψ is an unramified quadratic character and B is a nonzero element of Z_7. The determinant fixes ψ²=1; the residual representation is unramified at q, and the chosen branch has unipotent inertia. Write B=7^m b with b∈Z_7^×. Conjugation by diag(b^{-1},1) replaces B by 7^m and fixes the diagonal Frobenius matrix.

The Tate curve over Q_q with parameter q^{7^m} has precisely this representation before the ψ-twist. Indeed its 7^n-torsion is generated multiplicatively by ζ_{7^n} and (q^{7^m})^{1/7^n}, and tame inertia changes the latter by ζ_{7^n}^{7^m}. A Frobenius lift fixing compatible roots of q gives diag(q,1). Twisting that elliptic curve by ψ therefore realizes ρ|_{G_{Q_q}} as an **integral** Tate module. The displayed basis change lies in GL_2(Z_7), so this assertion retains the lattice.

### 2.4. Identifying the unramified local representations

At an unramified q outside S, one has q≥5 and q≠7. Waterhouse Theorem 4.1 supplies an elliptic curve over F_q with the polynomial X²−a_qX+q. Lift its coefficients to Z_q; its discriminant stays a unit, so this gives an elliptic curve E'_q/Q_q with good reduction. Its rational 7-adic representation is unramified with the required Frobenius polynomial.

Since q is prime, a_q²−4q≠0. Consequently the Frobenius operators are semisimple and have the same characteristic polynomial, hence the two rational unramified representations are isomorphic. To retain the integral lattice, identify their rational Tate spaces and let L be the lattice corresponding to ρ. After multiplying L by a scalar power of 7, arrange

    T_7(E'_q) ⊂ L ⊂ 7^{-n}T_7(E'_q).

The finite quotient H=L/T_7(E'_q) is a G_{Q_q}-stable subgroup of E'_q[7^n]. The quotient elliptic curve E_q=E'_q/H exists over Q_q, and, under the rational identification furnished by the isogeny, its Tate lattice is L. The subgroup is unramified and extends to a finite étale subgroup of the good integral model, so the quotient still has good reduction. Scalar multiplication of a lattice does not change its isomorphism class as a free Z_7[G_{Q_q}]-module. This proves the claimed integral realization.

At every initial q∈S, the local realization was fixed as T_7(E) in §2.2. These two arguments cover every finite prime, including 2,3 and 7.

### 2.5. The precise comparison with the full Legendre data

For an all-prime system with common local elliptic curves, forgetting every component except the seventh gives the explicit map

    ((ρ_ℓ)_ℓ,(E_q)_q,(ι_{q,ℓ})_{q,ℓ}) ↦ (ρ_7,(E_q)_q,(ι_{q,7})_q),

where ι_{q,ℓ}:ρ_ℓ|_{G_{Q_q}}→T_ℓ(E_q) are the specified isomorphisms. The construction above produces an infinitely ramified object in this target. It does not produce an inverse image under this forgetful map; nor does it produce an inverse image under the further map from sections of π_1(U) using the Legendre monodromy representation. Thus it proves that the seventh component, even with all of its individual local elliptic realizations, cannot alone yield finite ramification. The other coefficients and the actual section must enter any successful remaining argument.

## 3. The exact extra field in birational base change

Let x,T be algebraically independent over Q and fix Ω=Q(x,T)^sep. Let L_x and L_T be the algebraic closures of Q(x) and Q(T), respectively, inside Ω. They contain the same copy Qbar of the algebraic closure of Q. Put L=L_xL_T.

There is a continuous surjective homomorphism

    R:G_{Q(x,T)}→G_{Q(x)}×_{G_Q}G_{Q(T)},

given by the two restriction maps, and its kernel is G_L=Gal(Ω/L).

Here is the field-theoretic verification. A common element α∈L_x∩L_T which was transcendental over Q would make x algebraic over Q(α) and also T algebraic over Q(α). This would force Q(x,T) to have transcendence degree at most one. Hence L_x∩L_T=Qbar. More concretely, finite subextensions of L_x/Qbar(x) and L_T/Qbar(T) are function fields of geometrically integral curves over Qbar; their product is integral, and x,T remain independent. Therefore the two closures are linearly disjoint over Qbar. A pair of automorphisms agreeing on Qbar consequently defines a unique automorphism of their compositum. Conversely every automorphism of L/Q(x,T) restricts to such a pair. Extending automorphisms through the algebraic closure proves the surjectivity of R and identifies the displayed kernel.

### 3.1. A visible nonzero subgroup of the kernel

Let v_Δ be the divisorial valuation x−T=0. It is trivial on Q(x)^× and on Q(T)^×. A finite extension of Q(x), pulled back to Q(x,T), is unramified at v_Δ: choose a monic separable primitive polynomial over Q(x); its coefficients are integral for v_Δ and its nonzero discriminant is a v_Δ-unit. The same proof applies to every finite extension of Q(T). Their finite composita are unramified as well, because composita of finite étale extensions of the henselian discrete valuation ring remain étale. Thus all of L/Q(x,T) is unramified at this divisor.

For a chosen prolongation to Ω, the full inertia subgroup satisfies

    I_Δ≅Zhat(1) ⊂ ker R.

In particular, for every prime ℓ the extension obtained by adjoining (x−T)^{1/ℓ} is ramified with index ℓ at Δ and is absent from L. This gives explicit finite covers detected by the kernel. It is stronger than merely observing that the source and target fields have different names.

### 3.2. The embedding problem attached to a chosen birational section

Let τ:G_Q→G_{Q(x)} be a chosen continuous birational section. It defines the continuous map

    b_τ:G_{Q(T)}→G_{Q(x)}×_{G_Q}G_{Q(T)},
    g↦(τ(g|Qbar),g).

Its second projection is the identity. Define the profinite pullback

    E_τ=G_{Q(x,T)}×_{R,b_τ}G_{Q(T)}.

Projection gives an exact sequence

    1→G_L→E_τ→G_{Q(T)}→1.

A lift of this chosen τ over Q(T), with the required two restrictions, is exactly a continuous splitting of this displayed sequence: either splitting is the graph of the other. A section of the fibre-product quotient is supplied by b_τ, but it does not specify a homomorphism into E_τ. The explicit diagonal inertia above is among the additional data a splitting must handle. Its nontriviality alone does **not** prove that the splitting is impossible; point and cusp sections supply actual splittings.

For a model section s of U, the standard geometric-base-change identification is

    π_1(U_{Q(T)})≅π_1(U)×_{G_Q}G_{Q(T)}.

This follows from invariance of geometric fundamental groups under algebraically closed extensions in characteristic zero, together with the arithmetic exact sequences. The exact embedding problem for Bresciani's t-birationality of s is the pullback of G_{Q(x,T)}→π_1(U_{Q(T)}) along s_{Q(T)}. The preceding E_τ maps to that pullback by forgetting the specified restriction to G_{Q(x)}. A solution of the latter problem may correspond to a birational section over Q different from the initially chosen τ. We do not identify the two lifting problems.

This calculation locates the precise missing map in the attempted Q-birational ⇒ Q(T)-birational upgrade. No splitting of either new extension has been constructed for an arbitrary section here.

## 4. Source scope of the all-prime attempt

The original KLR pure-representation and two-prime compatibility observations are already present in AP's `D_legendre_modularity_extension.tex`; they should not be counted as newly discovered progress. The extra result here is the single-coefficient local elliptic realization construction in §2, including an explicit residual starting curve and lattice-level comparisons. The explicit diagonal field calculation in §3 is a separate new clarification of the actual transcendental-base embedding problem.

The unresolved A1 input remains a uniform finite ramification conclusion for the actual all-prime Legendre system, or an actual splitting of the transcendental-base embedding problem. Neither is replaced by the counterexample or the kernel calculation above.
