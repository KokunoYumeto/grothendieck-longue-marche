# Independent audit of A.56

**Result: PASS.** Read the complete notes/fgh_A56_draft.tex and independently reran notes/fgh_A56_certificate.py. This extends the already independently audited A.55 construction without a CM splitting. The hypothesis is potentially good reduction of the proper curve itself, not merely good reduction of its Jacobian.

## Exact specialization lattice

Independently opened Tate's original *p-Divisible Groups* scan at https://math.bu.edu/people/jsweinst/AWS/Files/TatePDivisibleGroups.pdf . Direct URL retrieval first timed out, but the actual primary scan was successfully reopened through the cached source as turn896view0, and its later passage as turn897view0. Section 1.4, printed page 160, supplies the connected–étale sequence for finite group schemes over a complete noetherian local ring. Section 2.2, printed page 164, equation (4), gives the corresponding sequence of p-divisible groups. Section 2.4 identifies geometric generic torsion and Tate modules. On geometric generic points the finite sequences are exact; multiplication-by-p transitions on the connected kernels are surjective. Their inverse limit is therefore an exact surjection from T_p J to the étale special Tate module, with free quotient of rank f and saturated kernel. No integral arithmetic splitting is needed or asserted.

The linear choice in the draft is valid for every p, including two. The primitive-vector perpendicular hyperplane has dimension 2g−1. The specialization kernel has dimension 2g−f at most 2g−2; the original vector line is also a proper subspace because g is at least two. Their union cannot fill the hyperplane. Perfect integral symplectic duality lifts the selected vector to an exactly perpendicular integral vector. Its specialization is primitive. Every finite-level torsion point is algebraic over the original number field; finite field extension, rigidification and the relative Picard scheme give the actual line bundle and trivialization. There is no reliance on a Galois-stable complement to the connected kernel.

For n larger than the valuation of the original proper vector, the latter is annihilated by the cover character but is outside its Poincaré-dual line modulo p^n. The proof by dividing the possible scalar multiple by p^r is integral because the chosen Picard vector is primitive. A.55's normal finite-flat torsor, unique radicial main component, Raynaud Prym and stable-line exclusion work in every genus. The higher-genus Schreier lattice has exactly the two fixed generators and the regularly permuted pairs stated in (A.56.5). Hence the actual lifted integral class produces the claimed contradiction.

## Elliptic target and degree bound

For a cover of the specified punctured Gaussian elliptic curve, the norm/pullback decomposition makes E an isogeny factor. At p congruent to one modulo four its good reduction is ordinary. If the total special p-rank is one, the complementary Prym has p-rank zero and A.46 forces any stable line to project nontrivially to E. The actual punctured morphism carries the normalized subgroup to one with nonzero proper homology, contradicting the previously established elliptic criterion. This also handles genus one; no genus-zero proper source can cover an elliptic curve nonconstantly.

Independently reopened the original SGA1 recomposed edition at https://arxiv.org/pdf/math/0206203 : references turn895view2 and turn897view1–2, Exposé XIII Corollary 2.9, Section 2.10 and Corollary 2.12's proof. The prime-to-residue-characteristic torsor specialization applies to the good marked pair. If p>d, the geometric Galois closure has order prime to p because its group embeds in S_d. After finite extension it therefore extends over the pair. The tame local equation t=z^e, with e prime to p, makes its proper source smooth; the same description applies to subgroup quotients. Thus there is no extra unnamed finite exceptional set of primes in the final degree-bound conclusion.

## Executed certificate

Command: python LM8_PUSH/notes/fgh_A56_certificate.py

Output: PASS. The run checked 35 specialization kernels and 525 vector/kernel pairs modulo two, 130 kernels and 10400 pairs modulo three, four higher-genus integral Schreier lattices, the ordinary Gaussian elliptic coefficient at 147 primes below 2000, and the S_d order bound for degrees 1 through 25 and primes below 200. The finite checks corroborate the formulas; the theorem's uniform scope follows from the structural argument.

No correction is required. The conclusion concerns actual procyclic arithmetic normalizers; it does not supply fixed-subgroup comparisons or cofinal refinements of arbitrary covers.
