# Independent root review of the general solvable-closure extension

Date:14November2026, approximately12:48UTC.

Reviewed the complete audit/F_general_solvable_closure_candidate.md,
the earlier integrated F.32–F.37 on which its geometric arguments depend,
and the exact newly opened field statements. Verdict: approved for
integration as F.43, in the corrected closed-point-preserving sense.
The universal intrinsic converse in F.9 is not proved by this result.

## 1. Constants and radical descent

For a finitely generated K/Q with algebraic constant field C, regularity
of K/C makes finite algebraic constant extensions linearly disjoint.
The two directions of Ksolv intersect Qbar = Csolv are both valid:
solvable constants remain solvable after base change, while normality
of a finite solvable K-extension forces it to contain every C-conjugate
of an algebraic constant it contains. The constant-field normal closure
then has solvable Galois group as a quotient. No normality of K/Q is used.

The alternating residual degrees after S_n Hilbert specializations over
C are unbounded. Since kQbar/k has those degrees and a finitely generated
L/k has finite relative algebraic closure, there is an algebraic number
outside L. Taking its Q-normal closure supplies a missing finite Galois
number field. This is the precise input needed by the later split-prime
Gauss valuations; a merely geometric finite extension would not suffice.

The proof of D(E*)=k* for finite E/k correctly fixes one finitely
generated field F=MS before allowing the root level to vary. The
automorphisms commute on M and k separately. A root z of a has
sigma(z)/z fixed by Gal(Mk/F), so sigma(a)/a is an n-th power in the
same F for every n. D(F*)=1 follows from the normal-projective divisor
argument and the finitely generated number-field unit group. This
forces a into k. Repeating the divisor argument over k proves D(L*)=k*
for all finitely generated L/k and all their finite extensions.

## 2. Every changed arithmetic hypothesis is checked

Finite descent fields explicitly contain K. Consequently L/F is
Galois prosolvable and G_L is normal in G_F. The balanced-wreath
finite-quotient detection argument uses precisely prosolvability and
Hilbertianity of a finitely generated characteristic-zero F, both of
which remain available. Its geometric pencil and Bertini arguments
do not acquire a new arithmetic hypothesis.

In the punctured-line step the finite model M is normal over an
ordinary rational function field over Q, so the chosen sigma preserves
M and moves its number-field constants. The arithmetic Gauss-place
construction is unchanged. The crucial tau preserves k because it fixes
K and k/K is Galois. The fixed field MS0 is finite over M even though
S0 need not be a number field. The norm valuation therefore still
converts each profinite exponent into an ordinary integer.

In the generalized Albanese step the finite set of points and actual
values still descends to a finitely generated characteristic-zero M.
Jannsen's Theorem4.3(ii) is applied over that M, within its stated field
hypothesis. The spanning argument, normal coinvariants, fixed boundary
unit lattice, residue norms, integral divisor matrix, and normalized
constant-class descent are the same verified steps of F.36. No claim
that the entire Picard-Tate module vanishes is made.

## 3. Actual point functions and the CHW conclusion

The scalar ambiguity lies in k, which is a fixed subfield of L; it need
not be algebraic over Q. The high-degree-point argument uses only
that fixed-field property. In the constant case one first passes to
a finite extension containing beta/h outside k; all original values
remain in h*k, and the divisibility-kernel assertion remains valid
after that extension. The pole-degree argument then proves constancy.
The higher-dimensional curve restriction is normalized at the same
rational base point, so its residual constant is one.

These are actual geometric-point functions, including the closed
subtopos argument excluding a generic-point-only exception. CHW4.18(5)
then yields the full reconstruction assertion, rather than an inference
that pointwise equality alone always identifies arbitrary topos maps.
The repaired closed-point-preserving definition is retained throughout.

## 4. The subfield descent is genuinely algebraic

The candidate correctly does not apply F.32 to k0*Ksolv/k0 when K has
positive transcendence degree. Instead, take a finite transcendence
basis B of k0/Q, F0=Q(B), and a finitely generated descent field F
containing K and B. Its relative algebraic constant field C over F0
is finite. Regularity of F/C and normality of L/F put the C-normal
closure of every a in k0 inside L, where it has solvable group.
Thus k0 lies in Csolv and Csolv/k0 is algebraic. Applying the core
theorem to C and then the already verified F.32 is legitimate.

This also proves the proposed arithmetic description of the sufficient
class. In the reverse direction, finitely many conjugates of Csolv
have prosolvable compositum over the finite normal closure of C/F0.
The resulting Galois group is virtually prosolvable, and the normal
closure of k0 has a quotient of that group. Conversely an open
prosolvable subgroup of the given normal closure has finite fixed
field C and embeds the whole extension into Csolv. These statements
characterize the sufficient class, not all reconstruction fields.

## 5. Strictness and sources

Q(t)solv has divisible multiplicative group and contains a
transcendental t. Under an embedding into any finitely generated
extension of Qsolv, t would map into its divisible subgroup, which
F.33 identifies with the algebraic field Qsolv. This contradicts
preservation of transcendence. The enlargement is therefore strict
without relying on an unverified degree comparison for number fields.

Root independently opened:

- Milne, J. S. (2022). Fields and Galois theory, Version5.10,
  Proposition7.15 and Corollary7.16, printedp.99,
  https://www.jmilne.org/math/CourseNotes/FT.pdf . Web records
  turn682view0 and turn682view2. The stated compositum isomorphism
  includes arbitrary common-overfield extensions and infinite Galois
  extensions, exactly as used.
- The Stacks Project, Section9.26, tag030D, Lemma9.26.11,
  https://stacks.math.columbia.edu/tag/030D . Web record turn682view1.
  The relative algebraic-closure finiteness hypothesis is finite
  generation as a field, which holds in every use above.

No mathematical correction is required. The exact statement should
remain one sufficient-field-class theorem, with the unresolved
intrinsic converse explicitly retained.
