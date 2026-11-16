# Root full proof and executable audit of C.47

**PASS; approved for canonical integration.** Root read the entire
candidate and its complete exact solver, freshly checked C.12 and
C.20's actual normalized congruence and CM-frame conventions, and
executed the entire solver independently. Root then read the two
final prose clarifications: one global sign is chosen for each CM
coordinate separately, and the normalized automorphism is stated
explicitly before its product law. The audited final draft is
`notes/pbc_finite_parity_detector_draft.tex`, SHA-256
`4e5da38f528cf2bf1e7f1f8b102bf39d2948f11adcf8c2feb7688bda133386eb`.
The independent DE full proof/dependency/code audit also passed.

## Actual marking and the finite base

The proof uses the actual pure subgroup of the modular free
product, with x=tau^(-2), y=sxs. Since Phi(tau)=tau and
Phi(s)=sf, the relation (sf)^2=1 gives sfs=f^(-1), and
restriction therefore sends x to x and y to f^(-1)yf.
This is the normalized pair convention used in the composition
argument. The old marking and its inner adjustment replace the
normalized conjugator by its inverse in the old letters and
preserve all closed derived subgroups. The actual CM difference
character is invariant under this common frame adjustment.

The finite quotient is SL_2(Z/12) modulo the single global sign,
of order 576. The signed images of the two pure generators are
U_0^2 and S U_0^2 S^(-1), and their subgroup is the kernel of
reduction to SL_2(F_2), of order 96. Its successive derived
orders are 8, 2, 1. The base torsion generators have orders
2 and 3 already modulo two; their cyclic groups meet the pure
base trivially. The complete finite enumeration in the retained
solver verifies these exact assertions, without replacing the
global sign quotient by separate primewise quotients.

## The centralizer obstruction is a literal coordinate equation

For an element h of prime order p and V=F_p[Q/<h>], the
affine element (delta_<h>,h) has order p because the norm
of its translation is p times that fixed basis vector. A
centralizer (a,b) must satisfy b h=h b and
(1-h)a=delta_<h>-b delta_<h>. At the h-fixed identity coset
the left coordinate is zero. The right is zero exactly when
b belongs to <h>. Conversely the affine powers realize every
element of <h> in the centralizer projection. The obstruction
persists when another module is added.

Apply this independently to the 288-dimensional binary coset
module and 192-dimensional ternary coset module. Their affine
lifts of s and r satisfy the exact torsion relations, giving an
actual homomorphism of the profinite free product into the finite
semidirect product. Its pure restriction lands in L=V semidirect
Q_0, whose order is 2^293 times 3^193. Since Q_0 has derived
length three and V is abelian, L has derived length at most
four. Neither of the two homomorphisms is assumed surjective.

The residue pi(f) determines the images of the two torsion
generators under the actual full Phi. Actual pure frames provide
conjugators in L. If any two L-conjugators give the same target,
their ratio centralizes the initial affine lift. Its base lies
both in Q_0 and in the corresponding order-two or order-three
subgroup, hence is one. Thus the two pure frame bases in Q are
uniquely determined by pi(f). This uses the images of actual
full identities and does not require Phi to descend to an
automorphism of the single affine quotient.

## The finite algorithm and the two signs

For each of the 96 possible pure base conjugators b, the
remaining conjugacy equation is (1-k)a=w-bv. On every cycle
of the permutation k, its image consists exactly of vectors
whose coordinate sum is zero. The solver checks these sums,
constructs a solution by successive partial sums, and verifies
the resulting full affine conjugation. For an actual residue
existence follows from the full frames, and the preceding
centralizer argument makes the base solution unique, even
though the solver is allowed to use all of L.

The base targets then determine the unique unipotent
intertwiner V modulo 12. C.12 provides existence for actual
pairs; uniqueness follows directly because a unipotent
matrix centralizing both base torsion generators has zero
off-diagonal parameter. The normalized coordinates are
T=q(A)^(-1)V and W=q(beta)^(-1)V, exactly as in C.20.
For each coordinate separately, choose its unique genuine
lift equal to I modulo four. That one sign is used at three
as well. This is not a separate choice of signs at each prime,
and it does not require T and W to share the same sign.

At three the signed cubic centralizer is cyclic of order
six; cubing detects its sign. The signed quartic centralizer
is cyclic of order four; squaring detects its class modulo
{I,-I}. Their sum is precisely the retained parity character.
The solver's default positive test is explicitly a finite
compatible frame test. It is not treated as a full lift;
the actual full nonzero witness is the already audited C.46.

## The characteristic envelope gives a finite group map

Intersect the kernels of all continuous maps F -> L. There
are exactly |L|^2 such maps, determined by the two free
generators. The intersection K is open and fully
characteristic: precomposing any such map by any endomorphism
again belongs to the same finite collection. Each map kills
F^(4), so F^(4) is contained in K, and the designated pi|F
is one of the factors of F/K. The displayed enormous order
bound is valid; no claim of optimality or actual enumeration
is made.

For normalized multiplier-one pairs, alpha_f(x)=x and
alpha_f(y)=f^(-1)yf. Their exact law is
f_(gh)=f_g alpha_g(f_h). The induced alpha on F/K depends
only on the retained f modulo K, so reduction is a
well-defined homomorphism onto a finite group of actual
pair residues. In particular, this is a genuine finite
group quotient of the actual gentle subgroup, not just a
set-valued evaluation. The frame algorithm depends on one
specified L-factor of that residue and computes Delta;
therefore Delta factors through this finite group.

If f belongs to F^(4), pi(f)=1, so the two torsion targets
are unchanged. Their unique pure frame bases and the
intertwiner are all one, giving Delta=0. C.46 has
f in F^(3) and Delta=1 in the actual full group. It also
lies in every lower derived kernel, so the least retained
conjugator depth is exactly four. The proof explicitly
excludes the stronger assertion about the outer-action
kernel on F/F^(4), which would need an additional
centralizer argument in that quotient.

## Exact execution and remaining scope

Root's complete independent execution reproduced the entire
owner JSON byte for byte. The source SHA-256 is
`1cedb45ccd61859aff61e870a27d1460b6646381d8ac4cf7cc6f4d640c87ec9b`;
the result SHA-256 is
`33f33c4f898b788b76b0d41f6ae294410aec8eb09485ce5c5a06c57045cd40d8`.
The run checks all 16 and 18 base-centralizer elements,
the full derived image chain, both affine torsion relations,
the identity, a common pure inner-frame change, and the
finite parity-one example. Its full output and exact
verification are retained in the root C47 certificate files.
The later separate 24-frame auxiliary program was reported
by its owner but is not claimed independently read or rerun
by root in this audit; it is unnecessary for the proof gate.

The result is an explicit finite multiplier-one detector
and a sharp retained-conjugator derived bound. It does not
identify the smallest finite detector, enumerate every
actual residue, give a full-multiplier evaluator, or
identify the outer-action kernel. PASS.

## Exact original level-four consequence

Root read `notes/pbc_C47_C6_added_proof.diff` and the exact C.14 definition. That envelope is the subgroup of S4^9 generated by the nine generating-pair representatives, equivalently the quotient by the intersection of all surjective S4-kernels. Since S4 has derived series S4, A4, V4, 1, the envelope kills F^(3). C.46 therefore has its identity normalized residue while Delta is one. The updated C.6 summary correctly distinguishes this original finite level four from closed derived depth four. PASS.
