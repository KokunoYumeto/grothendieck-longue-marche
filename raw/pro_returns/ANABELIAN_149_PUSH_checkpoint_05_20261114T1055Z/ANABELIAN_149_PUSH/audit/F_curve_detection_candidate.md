# Candidate: finite-quotient detection on arbitrary curves over finite extensions of Qsolv

Status: independently reviewed and approved by root; integrated as F.24 Proved in sections/F.tex, with its conditional comparison consequence F.25. Both have rows in audit/F_results.json. The historical filename records the review stage.

## Proposed statement

Let k=Qsolv, let L/k be finite, and let U/L be a smooth geometrically connected curve. For every finite quotient pi1(U) -> G there is a closed point x of U such that G_{L(x)} -> G is surjective. More precisely, the degree of x can be taken to be any sufficiently large degree n of a line bundle over a suitable descended number-field model of the smooth proper completion. In particular these detecting degrees are unbounded. No assertion of L-rational Hilbert irreducibility is made.

This strengthens F.20 from rational opens over k to arbitrary geometrically connected curves over every finite L/k. The proof uses a simply branched pencil, rather than the full symmetric power, and needs only coordinate surjectivity in the perfect residual of its wreath monodromy. The Abel–Jacobi constraint on the full base group therefore does not obstruct the argument.

## 1. Descent and constants

Descend U, its smooth proper completion C, the finite connected G-Galois cover Y -> U, the entire G-action, and the G-torsor isomorphism to a number field F contained in L. Enlarge F within L until L=Fk. This is possible because L/k is finite and all data have finitely many algebraic coefficients. The extension L/F is Galois and prosolvable: it is a base change of k/Q.

Choose the model geometrically connected, as follows from geometric connectedness after base change to L. The descended Y is connected because Y_L is connected. Let M be the algebraic closure of F in F(Y). Then M/F is Galois and

    1 -> N -> G -> P=Gal(M/F) -> 1

is exact, with N the geometric deck group. The curve Y is geometrically connected over M. Connectedness of Y_L implies M and L are linearly disjoint over F, in particular M intersect L = F. The group P need not be perfect in this stronger finite-L formulation. None of the subsequent steps assumes that it is.

Let B=C\U. The finite G-cover extends by normalization to a finite map of smooth proper curves Ybar -> C, ramified only over B. It remains geometrically connected over M.

## 2. A sufficiently ample simply branched pencil

Choose a line bundle A on C of degree n at least max(5,2g(C)+3), and two F-rational sections defining a morphism

    r:C -> P1_F

such that:

1. r has degree n and all its ramification is simple;
2. its distinct ramification points have distinct images;
3. r is unramified at B;
4. r is injective on B over Fbar, and r(B) is disjoint from the branch values of r.

Such pairs form a nonempty Zariski open in H0(C,A)^2. Here is an elementary jet-count justification, so no generic-projection theorem is used without hypotheses. Since deg(A) >= 2g+3, restriction of H0(C,A) to any subscheme of length at most four is surjective: H1(C,A(-Z))=0 by Riemann–Roch/Serre duality. The base-point condition at an unspecified point imposes two independent equations on the pair, with a one-dimensional point parameter. Ramification order at least three imposes two equations on the local ratio jet, again with one point parameter. Two distinct ramification points with the same image impose three independent equations (two first derivatives and one equality of values), with a two-dimensional pair parameter. Thus each bad incidence has dimension smaller than the parameter space. The diagonal in the last incidence is treated by the preceding order-at-least-three condition. At each of the finitely many geometric points in B, ramification imposes one equation; equality of two B-images imposes one equation. A ramification point sharing a value with a fixed b in B imposes two conditions, with one varying point parameter; its limiting diagonal is already excluded by unramifiedness at b. The jet-surjectivity just stated makes these dimension counts valid. The finitely many conditions are Galois-invariant and define an open over F. Since F is infinite, the open has F-rational points.

Base-point-free nonconstant pairs have r^*O(1)=A, hence degree n. Arbitrarily large such n are available by tensor powers of any ample line bundle defined over F. The available degrees may be restricted by the index of C; the statement does not promise every large integer n.

Remove from P1 the branch values of r and r(B), and call the resulting open V. Both r^{-1}(V) -> V and the composite Ybar|_V -> V are finite etale.

## 3. Elementary geometric monodromy lemma

Let H be the arithmetic Galois group of the Galois closure of F(Ybar)/F(P1). Choose a geometric fibre of r with n points, and label each of its G-torsor fibres using points inducing the same embedding of the constant field M. The monodromy representation embeds

    H <= (G x_P ... x_P G) semidirect S_n.

The common-P condition says that every coordinate induces the same automorphism of M. The map H -> P is onto, because M is a subfield of the Galois closure. The geometric monodromy Hgeom lies in N^n semidirect S_n; its action on the n|N| points in one chosen geometric component of Ybar is faithful and transitive.

Embed Fbar into C and use the finite-cover comparison of SGA1 XII.5.1–5.2. The geometric fundamental group of the punctured P1 is generated by small loops around the removed values. Their actions on the lifted fibre have only two forms:

- At a simple branch value of r, the action is a decorated transposition r_ij(a): it swaps blocks i and j with mutually inverse labels a,a^{-1} in N and fixes all other blocks. The order is two because Ybar -> C is unramified over that value.
- At a value r(b), b in B, the action is a single-coordinate element e_i(b0) with b0 in N. Conditions (3)–(4) ensure all other blocks are unramified and have trivial local monodromy.

Conjugating a local loop to the chosen base point preserves these forms. Identity generators may be omitted. The projection to S_n is generated by the transpositions in the first type and is transitive because C is geometrically connected. Their edge graph on {1,...,n} is therefore connected.

Choose a spanning tree of that graph. Conjugation by one element of N^n gauges all labels on its edges to 1: choose a root vertex and then its successive vertex labels. Its edge transpositions consequently generate the literal S_n inside Hgeom. Keep this gauge henceforth.

Let N0 be the subgroup of N generated by all remaining decorated-transposition labels and the single-coordinate labels. Every monodromy generator now has coordinates in N0, so the orbit of (1,i) lies in N0 x {1,...,n}. Transitivity on N x {1,...,n} forces N0=N.

For every remaining reflection r_ij(a), multiplication by the corresponding literal transposition yields a base element

    d_ij(a)=e_i(a)e_j(a^{-1}) in Hgeom intersect N^n.

Single-coordinate generators e_i(b0) already lie there. Thus there is a list of base elements of support at most two whose nonidentity coordinate labels generate all N. This is the only property needed below; no claim that Hgeom equals the unrestricted wreath group is made.

## 4. What survives every solvable base change

Write H^infinity for the stable term of the derived series of H. The literal A_n is perfect for n>=5, so A_n is contained in H^infinity. The group H^infinity is normal in H.

Fix a coordinate i. For any support-at-most-two element u above whose selected coordinate is a, choose tau in A_n with tau^{-1}(i) outside the support of u. Such tau exists for n>=5. Then

    [u,tau] = u tau u^{-1} tau^{-1}

belongs to H^infinity intersect N^n, and its i-th coordinate is

    u_i u_{tau^{-1}(i)}^{-1}=a.

Literal S_n-conjugation moves the selected coordinate wherever required. Consequently the projection of H^infinity intersect N^n onto every coordinate is all N. This proves the needed balanced-label conclusion even though an Abel–Jacobi constraint may prevent the geometric monodromy from containing N^n itself.

Hilbert irreducibility over the number field F supplies a specialization Omega/F with full group H. Serre (2007), Proposition 3.3.1 and Theorem 3.4.1, apply because the Galois closure is irreducible over F; geometric irreducibility is not required. Place Omega in Qbar so that its constant copy of M is the chosen M.

Set J=Gal(Omega L/L), regarded as the subgroup Gal(Omega/(Omega intersect L)) of H. Since L/F is prosolvable, H/J is solvable and H^infinity is contained in J. Since M intersect L=F, restriction J -> P is surjective.

The subgroup J contains literal A_n, so it acts transitively on the n blocks. Fix one block i, and put J_i=J intersect Stab(i). Its coordinate projection to G is a homomorphism. It contains N, by the preceding commutator calculation. It also surjects onto P: for h in J with a prescribed P-image, choose a literal tau in A_n moving the block h(i) back to i. Then tau h belongs to J_i and has the same P-image as h. This argument needs only transitivity of A_n; it does not require P to be perfect, does not require J's permutation image to be exactly A_n, and does not require an odd permutation to lie in J. Therefore

    J_i -> G

is surjective.

## 5. Detection at the specialized closed point

The specialized fibre C_a over L is a degree-n finite etale scheme whose permutation group contains A_n. It is therefore one closed point x of degree n over L, and x lies in U because the specialization avoids r(B). The image of G_{L(x)} in J is exactly the coordinate stabilizer J_i. On the G-torsor fibre Y_x, its action is the coordinate map J_i -> G. The preceding surjectivity proves the proposed assertion.

## 6. Consequence and exact remaining issue

The joint-image and compactness argument of F.21 now applies to arbitrary geometrically connected smooth curves over finite extensions of Qsolv whenever the two morphisms have the same geometric point values and a suitable algebraic comparison map. In particular, the generic comparison no longer requires the source to be rational. For a finite etale comparison map of curves, F.22 still supplies the full-topos conclusion.

This does not yet reconstruct the point function of an arbitrary pinned map C_et -> Gm_et as a regular unit. F.18 used Pic(C)=0 for its rational-source Kummer calculation, while an arbitrary curve may have a nonzero Picard Tate module. Detection does imply that a finite quotient is determined by its simultaneous restrictions to all closed-point decomposition groups; it does not by itself turn arbitrary pointwise actual Kummer values into one rational function. This was the next obstruction at the detection stage. The subsequently reviewed F.26–F.28 resolve the curve unit and point-function step, and F.29–F.31 establish all-scheme reconstruction over Qsolv and its finite extensions. The intrinsic arithmetic classification of all fields remains unresolved.

## Sources and review status

The proof uses the already opened primary passages Serre (2007), Topics in Galois Theory, Proposition 3.3.1 p.23 and Theorem 3.4.1 p.25; and SGA1 XII, Theorem 5.1 and Corollary 5.2, in the complete supplied source. The pencil jet count and finite-group argument are given above, rather than cited as unstated general monodromy theorems. Root independently reviewed the entire proof, including the possible extra constants of the Galois closure, the length-four jet count, the spanning-tree gauge, the support-two commutators, and the finite-L stabilizer argument, before promotion.
