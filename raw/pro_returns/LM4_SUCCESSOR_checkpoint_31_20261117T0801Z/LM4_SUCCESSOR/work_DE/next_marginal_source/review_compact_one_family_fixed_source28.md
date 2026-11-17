# Independent full review: compact one-family fixed-source comparison

Status: PASS. This is a complete source/proof review, with a fresh primary-source audit at the uses below; no duplicate execution or finite-target census is claimed.

Reviewed source: `work_CE/compact_one_family_fixed_source28.txt`.
SHA256: `4f2b2617d7ccf2a86ea6c8b4c6fe21a96316b6c6aa555097f45f3f4dd4b548f5`.

## Actual construction and all-target argument

I read the entire note, Sections0–8. The finite quotient retains the actual cocycle, not only the source action: characteristic N in the finitely generated Q_f makes both actions descend, and the finite holomorph homomorphism s↦(h_s^-1,alpha_s), together with the prescribed finite target on S, gives the required L. The resulting H_i is a genuine section over S_i. The two cone characters survive, so the seed edges do not collapse to loops and C cannot become conjugate to tau.

The arbitrary finite-target factorization through A(Gamma_i) semidirect D_i is valid on all graph generators. Equal finite coset labels differ by an actual H lift and an element killed by the prescribed target; H centralizes a. Every finite graph edge is the image of an actual edge, giving a genuine group homomorphism. The refinement construction is compatible with the first target.

The inverse-limit centralizer argument in Q_f is correctly used only to constrain images in a prescribed finite level. The finite-intersection argument does not require surjective maps between finite centralizers. Characteristic kernels are cofinal; therefore a further characteristic level makes every coarse centralizer image lie in <tau>. Source elements fix tau, and orientation removes its odd power from the even coarse image.

The finite graph involution has no fixed vertex because H_i projects injectively to S_i. Its swapped edges are precisely the tau edges indexed by the coarse centralizer: the C possibility is excluded by the retained two-cone character. The previously audited piling argument then describes the whole discrete fixed subgroup. Under the refined map its norms are actual source translates, and its even coarse part maps into the actual source group. This is uniform over every prescribed finite target.

## Finite graph hypotheses and primary input

Finite graph groups have finite Salvetti resolutions and the special-HNN/full-link argument gives their required full topology and residual finiteness. A finite extension by D_i preserves residual finiteness and the finite-index graph-group completion. Finite-module goodness extends to arbitrary discrete continuous F2 modules by their filtered union of finite invariant spans; the finite cellular resolution and compact continuous cochains justify the two cohomology colimits. The finite-extension spectral sequence gives the required comparison and finite cohomology in every degree. Thus finite virtual 2-cohomological TYPE, as well as goodness, is supplied. No bipartite or uniform clique-dimension hypothesis is used.

I independently opened Lorensen's author PDF https://arxiv.org/pdf/0802.0118 and read Theorem3.15 with its complete induction, Lemma3.14 with proof, and the local Theorem3.10/Corollary3.11/Proposition3.12/Theorem3.13 chain (PDFpp10–12; retrieved lines535–626). Successful references: turn1040view1, turn1041view2/3, turn1042view4, turn1043view3. No full-paper read is asserted.

I independently opened Boggi–Zalesskii https://arxiv.org/html/2406.08639v2 and read Definition4.1, the full Theorem4.3 statement, Lemma4.4 including its entire proof, Section4.2's prime-order proof, and Lemma2.2 including its complete proof. Successful references: turn1040view0, turn1042view0/1/2/3, turn1043view0/1/2, turn1044view0. The relevant ranges are lines178–200,268–314,318–391. The conclusion used is centralizer closure for the actual order-two element under an injective dense map satisfying the verified cohomological hypotheses. Neither an unrestricted solvable-subgroup theorem nor goodness alone is substituted for it.

## Exact conclusion and remaining scope

The centralizer-closure theorem applies separately to each finite graph model, and finite-index parity identifies its even completed centralizer. Hence every finite image of a fixed element of the actual completed one-family group lies in the corresponding finite actual-source image. This proves the asserted equality with the actual closed source subgroup, without identifying a completion of the infinite graph kernel.

The final quotient argument is also correct: completion of the actual quotient is the original completion modulo the actual closure of K_rem. The image of the actual source closure is the entire fixed subgroup of this particular quotient, so its fixed projection is onto and the original equality is equivalent to

    (closure K_rem)^delta = closure(H_src) intersect closure(K_rem).

This is an exact remaining-kernel criterion, not a solution of that criterion, not source injectivity/full topology, and not fixed lifting for other fillings. Both original main questions remain open. No correction requested.
