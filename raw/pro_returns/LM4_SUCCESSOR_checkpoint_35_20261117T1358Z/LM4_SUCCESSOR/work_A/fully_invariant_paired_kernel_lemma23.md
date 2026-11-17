# Compatible finite edge kernels without a vanishing conjugate retraction

**Independent proof: PASS.** This is an abstract split-index-two amalgam statement. It does not identify the actual annular one-neck group with such an amalgam; the geometric pushout may impose additional good-side base relations.

## 1. Hypotheses and the fully invariant kernel

Let K be finitely generated, embedded as a retract of each H_i. Let r_i:H_i→K be the specified retractions. Suppose R_i=H_i semidirect <c_i>, with c_i of order two; H_i is the specified ordinary index-two subgroup. The order-two splitting is part of the hypothesis. Define the endomorphism

`nu_i = r_i Ad(c_i)|K : K -> K`.

No assertion that this endomorphism is trivial or involutory is made.

Given N normal of finite index in K, put Q=K/N and

`L = intersection_{phi:K->Q} ker(phi)`.

There are finitely many such homomorphisms because K is finitely generated and Q is finite. Thus L is normal and of finite index. The quotient homomorphism K→Q is among them, so L is contained in N. For every endomorphism theta of K and every phi, phi theta is again among these homomorphisms. Hence theta(L) is contained in L: L is fully invariant. In particular each nu_i descends to an endomorphism of K/L.

## 2. Paired maps and exact edge kernel

Write Q_L=K/L. On H_i define

`Phi_i(x) = (r_i(x) mod L, r_i(c_i x c_i) mod L)`.

This is a homomorphism to Q_L×Q_L, and conjugation by c_i exchanges its coordinates. It therefore extends to

`Phi_i:R_i -> (Q_L×Q_L) semidirect_swap C2`,

sending c_i to the nontrivial swap. For k in K its restriction is

`k |-> (k mod L, nu_i(k) mod L)`.

The first coordinate forces any element of its kernel to lie in L; full invariance makes the second coordinate trivial on L. Thus the restricted kernel is **exactly L**. This argument neither discards the conjugate K nor requires r_i(c_i K c_i)=1.

To refine arbitrary finite-index normal M_i of R_i simultaneously, choose N contained in both M_i∩K and construct L as above. Put N_i=M_i∩ker(Phi_i). Then N_i is finite-index normal in R_i, N_i is contained in H_i, and N_i∩K=L for both vertices. The induced finite edge subgroup is K/L in both quotients, with its two actual graph embeddings retained.

## 3. Full completed amalgam

Form the abstract amalgam G=R_- *_K R_+. For the preceding kernels, the finite-vertex amalgam

`V=(R_-/N_-)*_(K/L)(R_+/N_+)`

is virtually finitely generated free. Explicitly, choose a common finite cardinal divisible by both vertex-group orders and use repeated regular actions. Both restrictions to the edge are free actions with the same number of edge orbits, so their underlying edge actions can be identified. This gives a finite permutation quotient embedding both vertex groups. Its kernel acts freely on the ordinary amalgam tree and has finite index and finite rank; consequently V is residually finite.

Every specified finite vertex quotient is thus retained after refinement in a finite quotient of G. The edge has its full topology in each H_i by the retraction and in each R_i by index-two cores. These facts prove that the full vertex and edge completions embed and that

`hat G = hat R_- amalgam_{hat K} hat R_+`

is the proper full profinite amalgam. Every finite quotient of G factors through one of the V: start with the kernels of its vertex restrictions, construct the compatible refinement, and retain its original two vertex maps. This is cofinality for arbitrary finite quotients.

## 4. Selected odd-cone centralizer

Each head has a character to C2, since both edge images are even. The image of c_i is an odd involution, hence cannot belong to a conjugate edge subgroup. It fixes precisely its base vertex in the ordinary tree, and

`C_V(c_i)=C_{R_i/N_i}(c_i)`.

The finite-rank virtually free head satisfies the exact residual-finiteness, finite virtual cohomological TYPE and all-discrete-module comparison hypotheses verified in B108. The already read prime-order-element theorem of Boggi–Zalesskii therefore identifies its completed centralizer with this finite vertex centralizer.

Now let an element of hat G centralize c_i. Its image in every completed head lies in the corresponding finite vertex. If it lay outside the compact image of hat R_i, some finite quotient would separate it from that image. Factor that quotient through a head to obtain a contradiction. Thus

`C_{hat G}(c_i)=C_{hat R_i}(c_i)`.

The same discrete equality follows directly from the ordinary tree. No residual-finiteness assumption on the original R_i is needed for this completion argument. No centralizer computation inside the vertex is implied.

## 5. Application boundary

The lemma applies to the stated abstract amalgam whenever the ordinary retractions and actual order-two splittings are supplied. A geometric annular neck decomposition must first identify its complete pushout, including all retained good-side base commutators. The lemma cannot remove or ignore those additional relations.
