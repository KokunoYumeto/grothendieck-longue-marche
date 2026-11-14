# E.40: all higher central fibers and the next exact fiber group

Every nonempty lifting fiber from the full intrinsic quotient N/gamma_(r+1)N to N/gamma_rN, for r>=3, is evaluated by a finite matrix over Z3. Its central module is the actual integral free Lie lattice Lie_r(V), with arithmetic action induced from the already computed rank10 generalized-Jacobian lattice. This comparison is the opened Koch–Kukkuk–Labute Theorem2.1; the proof does not use a class3 Baker–Campbell–Hausdorff identification at the prime3.

Twisting by the lower section does not change the central-layer action because inner conjugation is trivial on a lower-central graded quotient. At any prime away3, an inertia value would be a Frobenius eigenvector of eigenvalue equal to the residue-field size. The Lie degree r>=3 has weights at least3, so that eigenvalue does not occur. Every central cocycle is therefore unramified away3, even when the lower section is ramified. The first nonzero graded coordinate similarly excludes every geometric stabilizer of a lower section. This proves that geometric conjugacy leaves the full computed H1 torsor, with no additional stabilizer quotient.

Evaluation on the actual pair of conjugate free Frobenius generators over7 gives the exact presentation

    Lie_r(V) / (Lie_r(A_tau)-1) Lie_r(V)^{complex conjugation}.

The free rank is the minus-space dimension given by Witt's character formula. The split sublattice T_D+j(T3E) contains3V. Frobenius at the K-prime2 acts by scalar (-2)^j on Lie words, with r<=j<=2r. This proves the uniform bound3^(r+b_r) on torsion, where b_r=max(1+v3(j)) over that interval. Modular Smith calculation one power above this bound therefore determines all elementary divisors in every fixed degree.

## Degree-three result

The Hall lattice has330 basis elements [[x_i,x_j],x_k] with i>j and k>=j. Complex conjugation has trace−2, so its plus and minus dimensions are164 and166. The exact integer cocycle matrix has Smith valuations

    0 repeated73; 1 repeated7; 2 repeated56; 3 repeated25; 4 repeated3;
    plus166 zero factors.

Consequently every nonempty class3 lifting fiber over a fixed full intrinsic class2 section is a torsor under

    Z3^166 + (Z/3)^7 + (Z/9)^56 + (Z/27)^25 + (Z/81)^3.

The program saves complete modular left and right transformations and every elementary operation, and independently verifies their product with the original matrix modulo729. An independent stacked invariant matrix yields the same torsion. The exact split-lattice identity proves that the torsion exponent divides3^5, so the calculation at3^6 is conclusive. The exact matrix presentation supplies full coordinates; the saved transformations give Smith coordinates modulo729 and can be continued at higher precision.

## Scope and exact further maps

The theorem computes every nonempty higher fiber. It does not assert that every lower section has a lift: E38 gives an entire explicit abelian fiber whose class2 sections all fail at class3. The full metabelian quotient maps onto N/gamma4N with kernel gamma4N/Ndoubleprime. The single-Q marked quotient maps onto it with kernel gamma4N/gamma3(I_Q), since the rank1 abelian image of I_Q gives [I_Q,I_Q] contained in gamma3N. These are the exact maps linking the new fiber calculation to the remaining metabelian and marked-depth problems.

## Sources and programs

Opened Koch–Kukkuk–Labute, *Nilpotent local class field theory*, Theorem2.1 in the author's PDF, pp4–5. Opened Aka–Breuillard–Rosenzweig–de Saxce, *Diophantine properties of nilpotent Lie groups*, TheoremA.1 and its proof in the author's PDF. The latter is used only for the free-Lie character formula, not for any claim about arithmetic section sets.

code/e_lie3_fibers.py/.out/.json completed with PASS. sections/E_higher_fibers.tex, ledger/e_higher_results.json and ledger/e_higher_refs.bib contain the proof and metadata.
