# Independent adversarial review of A.49

Reviewed 16 November 2026, approximately 05:28–05:32 UTC, from `work_A/A49_mixed_head_working.md`, the developing formal A.49 in `work_A/A_involutions.tex`, and both finite affine/Clifford scripts and their retained output. No A-owned file was edited.

## Outcome and scope

The central-kernel bound and the new scalar-stabilization argument pass. Together with the already established framed lifting theorem, stabilization allows the specified action on the **actual** central refinement to be retained by a full positive lift. Composing that lift with genuine complex conjugation yields the claimed negative element and its order-two quotient image. This does not prove its square is one in the full group.

## Finite central-kernel bound

For a finite quotient retaining the joint affine quotient, the exact sequence on the abelianization is `0 → A_i' → M_i^ab → Vbar → 0`, where `A_i'` is the image of the central kernel. Duality over finite abelian groups is exact. Relative perfectness makes the middle dual's C-invariants vanish. Since `A_i'` is a trivial C-module, the invariant long exact sequence injects its full dual into `H¹(C,Vbar^vee)=0`. Thus `A_i'=0`, and, because the quotient Vbar is abelian, `A_i=M_i'`.

The cohomology vanishing has the needed actual-source justification. Each simple summand has a one-dimensional `H¹(Pi,V)`, and its nonzero class is the generating affine quotient. Its restriction to R is nonzero because the R-image is the full module. Inflation from C is injective, so it is zero. The invariant alternating dot product identifies each summand with its finite dual. This argument does not assert that arbitrary noncentral modules have vanishing H¹.

The resulting commutator pairing is alternating, bilinear and C-invariant on Vbar. Its image is therefore a quotient of the two-dimensional coinvariant exterior square. The first central kernel has order at most4 in every finite quotient, and the residual image has order at most2^14. The actual Clifford quotient attains both bounds. If an additional global kernel existed, it would survive in a finite quotient retaining the Clifford map and violate the bound. Thus the proof does identify the actual profinite refinement, rather than a chosen central cover.

## Scalar stabilization

Work in a finite quotient of `Pi/W2` retaining the finite Clifford quotient. Such quotients are cofinal: intersect any open kernel with the kernel of the Clifford map. The old residual group and old center are therefore retained faithfully.

The same dual argument now gives `M2^ab=Vbar` and puts A2 inside M2'. Since the old center A1 is the old derived subgroup, its full preimage Z0 is exactly M2'. For a lift of an A1-element, commutation with M2 takes values in the new central A2. It is a homomorphism in the second variable, hence factors through Vbar; changing the first lift by A2 does not change it. This gives a well-defined C-invariant pairing `A1 ⊗ Vbar → A2`. Both A1 and A2 are trivial C-modules and `(Vbar)_C=0`, so this pairing vanishes.

Therefore Z0 centralizes M2. The group M2 is of class two, and Z0=M2' is elementary abelian: the commutator pairing factors through the elementary abelian Vbar. It is a quotient of `wedge² Vbar`, so its C-action factors through the actual finite head Hbar. This last factorization must precede the use of its odd subgroup J; the proof supplies it.

J has odd order147 and is normal of index2 in Hbar. Its action on the subquotients A2 and A1 is trivial. Semisimplicity over F2 makes its action on the whole finite module Z0 trivial. The direct 66-coordinate check in `check_review_A49.py` independently constructs the paired permutation action and verifies exterior-square coinvariant rank64, so `dim (wedge² Vbar)_J=2`. Since Z0 already surjects onto the two-dimensional A1, its kernel A2 is zero. Cofinality of the retained finite quotients gives the global closed-commutator equality `[[W,Pi],Pi]=[W,Pi]`.

There is no assumption of global finiteness in this argument: both rounds of duality and Maschke are used in finite images, and the passage back is justified by cofinality. There is no unproved implication that acting trivially on central subquotients means acting trivially on the whole module for an even group; the odd subgroup and its exterior-square dimension are exactly what make this step valid.

## Frames and sequencing

The specified positive automorphism of the actual fiber product fixes the finite Clifford coordinates and has the retained C-action. The finite s-lift is pure; the r-lift is conjugate to a pure lift by an element of the normal2-group, by the coprime complement theorem. Consequently the finite torsion centralizers surject to the corresponding head centralizers, which is what the literal frame gluing needs. The actual cusp is fixed literally.

Before stabilization, applying the lifting theorem only retains the action on `Pi/W`. After the closed-commutator equality, applying it with the stabilized kernel `W1` retains the whole specified action on `E=Pi/W1`. The developing proof now observes this order. The parent and other reviewers already audited the finite scalar-cover lifting theorem used here; this review checks that its central-refinement input is now the required actual quotient.

For a finite earlier perfect refinement, independence from the new solvable head follows from absence of a common nontrivial quotient. On R the earlier perfect image and the abelian Vbar are likewise independent. Thus the earlier residual kernel still surjects onto Vbar; taking its relative commutator preserves that image since `[Vbar,Gbar]=Vbar`. Given the earlier proved relative-perfectness and stabilization, the same cohomology and central-layer argument applies to the enlarged base. Compactness then preserves all finite requirements; it still does not promote quotient involutions to a full involution.
