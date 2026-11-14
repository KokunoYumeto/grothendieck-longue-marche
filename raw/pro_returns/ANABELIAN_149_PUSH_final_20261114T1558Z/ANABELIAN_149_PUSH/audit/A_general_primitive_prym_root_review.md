# Root review of A.C2.20

Reviewed on 14 November 2026. Verdict: PASS for the stated all-genus, all-characteristic sufficient criterion.

We read the full candidate and `sections/A_general_primitive_prym.tex`, including the corrected Cartesian-square wording. The hypothesis is a connected geometric cyclic étale cover of odd degree n prime to p, with zero p-rank of the image of `∏(1−σ^(n/ell))` on its Jacobian. This image has precisely the primitive characters up to isogeny. Its geometric p-primary points vanish when its p-rank is zero, so application to the lifted p-primary divisor class is direct and does not require an unproved linearization of the fundamental group.

The support, controlled-field, free-action and reduced-fibre arguments of A.C2.19 apply with genus(D)=n(g−1)+1≥n+1. They force a separable quadratic elliptic quotient with an involution commuting with the odd deck group. The resulting degree-two map C→E0 is ramified because genus(C)≥2. This is a genuine consequence of the assumed collision, not an additional hypothesis on C.

For each divisor m of n, the quadratic extension defining C and the degree-m étale genus-one extension defining Z_m are linearly disjoint. Their compositum is the function field of D_m. The fibre product W→C is étale and hence W is smooth; integrality and the function-field identification give W=D_m. The source correctly does not call the ramified quadratic horizontal morphism smooth. The ramification point count after this étale base change is exactly m times the positive count r1 on C→E0.

In characteristic two, the genus-one curves Z_m are isogenous and have equal two-rank epsilon. The ramified Deuring–Shafarevich formula therefore gives `f2(D_m)=m r1+2 epsilon−1`. Odd-order averaging and pullback/norm identify the invariant Tate summands with the Tate module of D_m, so Möbius inversion gives `f2(P_n)=r1 phi(n)>0`. The proof uses exact-conductor ranks of arbitrary dimension and does not import the one-dimensional genus-two theta calculation into higher genus.

In odd characteristic, the forced quadratic elliptic quotient is a prime-to-characteristic Galois cover, so the independently established A.29l directly excludes the original section collision. No Deuring–Shafarevich formula for a tame quadratic action is used. We checked this dependency against the actual scope of A.29l; it includes finite extensions and finitely generated field forms.

The root reran `code/BC_general_primitive_prym_checks.py`: PASS, 250 symbolic odd orders and 56 numerical rank examples. The general Möbius identity and its geometric interpretation are proved in the text.

The theorem does not assert that every curve admits such a cover. In particular, a nonordinary cover need not have a primitive factor of zero p-rank; Raynaud-type nonordinariness results cannot be substituted for this hypothesis. The result supplies a new sufficient condition and leaves universal A1/A2 unresolved. No priority is claimed.
