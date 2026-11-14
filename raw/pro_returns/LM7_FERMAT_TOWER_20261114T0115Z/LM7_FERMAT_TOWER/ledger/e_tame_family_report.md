# Local arithmetic module and the infinite obstruction family

E.42 derives the full local tame equation in the actual quotient H from E.38. For nonzero first inertia, quotienting by T^a-1 identifies the problem with invariants of an explicit affine permutation of Z/3^v3(a). The two augmentations give a finite two-row integral matrix. All cocycles are reconstructed by the displayed division formula; conjugations preserving all four coordinates remove precisely the free U-part. For zero first inertia, a nonzero second inertia value forces a unique binomial series. Its integrality is equivalent to b/(q-1) belonging to Z3, regardless of the finite divisibility of the second inertia value.

The executed program e_tame_module.py checks96 orbit systems and28 zero-first-inertia cases, verifies the original tame relation and both augmentations, and recovers the exact E.38 coefficient1729/384.

E.43 improves the class-two denominator bound to the exact exponent3^(v3(q-1)+1) at every K-prime away3. The upper bound uses the actual index lattice3M0 inside the split cross-plus-toric sublattice. The lower bound uses six rank4 direct summands, each with Smith exponents m-1,h-1,s+1,s+1; the integral elimination maps and h<=s are proved.

For every rational prime p=1 mod9 with2 a noncube modulo p, and every k>=v3(p-1)+1, the global class alpha_P+3^k kappa3(p)e_B0 lifts through the full intrinsic class-two quotient and has the entire E.37 fiber. Every class of that fiber fails to lift to the full pro3, metabelian and indicated marked groups. The local obstruction holds for every k>=0. The set of such primes has density1/9 by the explicit six-element conjugacy class in Gal(Q(zeta9,2^(1/9))/Q).

The source used for infinitude is Milne, Class Field Theory v4.03, Chapter V Theorem3.23 (printed p164, PDF p173), opened directly at https://www.jmilne.org/math/CourseNotes/CFT.pdf. Its full Chebotarev statement, including the conjugacy-class density, is the exact assertion used. No claim of priority is made. The earlier original-source searches for Ihara1986 and Coleman1989 still did not yield readable originals; their bibliography statuses are unchanged.

The program e_infinite_obstructions.py checks every eligible prime through1000, counts the cubic points independently, computes both primary CM matrices and all38 local rank44 Smith forms, and records additional inert/split examples. These checks supplement the uniform proofs. The family enlarges the explicitly evaluated negative locus. Arbitrary ramified intrinsic metabelian and marked sections remain to be computed, as do the remaining full profinite prime components and mixed quotients.

