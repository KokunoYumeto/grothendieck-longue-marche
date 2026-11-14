# Root review of A.29m

14 November 2026. The complete auxiliary-cover candidate and its finite certificate were read. The root independently computed the three permutations on P¹(F_r), their cycle decompositions, and both Riemann–Hurwitz genera for all nine primes. The results agree with the agent's exhaustive projective-matrix certificate.

For a chosen component of the normalized fibre product, the tame local compositum has ramification index lcm(e_C,e_H)=e_C. Thus the map to C is étale. Its Galois closure embeds in the compositum with the prime-to-p Galois closure of H, so that normal closure still has prime-to-p degree. The map from the component to H is Galois because C/P¹ is Galois. Collision lifting is performed after a finite extension and remains on the selected component. The elliptic case uses the required ramification and A.21; the higher-genus case uses its established point separation. Only equality on the common base is concluded before applying A.29l.

SGA 1, XIII, Corollary 2.12 was independently reopened from the primary PDF, recomposed p.290, PDF index305, especially the finite prime-to-p quotient realization with specified inertia generators. The explicit PSL₂ generating triple therefore realizes the exact (2,3,r) indices in every permitted characteristic. Its Borel quotient has genus zero, one or two for the nine displayed primes, and each of the corresponding positive-case arguments has the required prime-to-p degree. The condition excludes characteristic two and any prime dividing the displayed group order. It makes no universal assertion about arbitrary nonsolvable signatures.

The finitely generated-field comparison extends the entire base field, spreads the finite data, and invokes the previously proved specialization implication. It does not confuse a finite base extension with a constant-field extension.

**Verdict:** approved. The independent permutation calculation is saved as `code/A_branch_auxiliary_independent.py` with its JSON output.
