# Independent actual Z3 retract and nonzero-sphere review

Status: PASS, 2026-11-16. Read the complete formal candidate
`sections/b_symmetric_nonasphericity.tex`.

## Exact finite and based checks

The independent producer is `work_A/code/verify_actual_Z3_retract19.py`;
its genuine stdout/error files are adjacent, and its complete input-bound
record is `work_A/actual_Z3_retract_independent19.json`.
It independently reduces the actual paired-to-cut Nielsen maps, the
node commutator, and the old0 substitutions. The exact data are:

- a=p2=cut4, the positive meridian of A_v(zeta).
- b=p12*p13*p12-inverse=cut16, the positive meridian of
  B_v(zeta^4)=F(A_v(zeta^4)).
- Node(6,3) has physical labels3 and14 and relator[a,b].
- Old0 fixes p2,p12,p13 literally; hence its actual far lift commutes
  with both a and b in the total group, independently of fiber injectivity.

The exact polynomial check modulo Phi5 verifies the intersection value
q=zeta+zeta^4-1 and that it avoids every retained divisor. The units are
v-zeta, q+(zeta^4-1)v-zeta^4, and q. Their first two meridian columns are
the first two standard basis vectors; the third column has q-winding1.
The determinant is1 regardless of its first two entries.

For the literal far marking, the old path certificate has |q|<5, and
v_infinity=10^6/(1+(371/1000)i). Since |zeta^4-1|>1 and the denominator
has modulus less than2, the constant part of f_B has modulus greater
than499999. Thus the actual old0 loop has zero first two windings.
The common connecting paths cancel in every winding character. The
literal matrix is I3, as asserted in the formal source.

## The retract and sphere

The three commuting elements define Z3 into the actual group. The three
global units define a homomorphism back with identity composite. Hence
the subgroup is Z3 and a retract; no abstract presentation equality or
completion argument is being used.

The displayed D(v,w) is precisely the product of the old factors, both
deleted root families, and their F-images. Its nonzero locus is the
actual symmetric complement. The graph sD=1 is a closed smooth complex
surface in C3, since its s derivative is nonzero. I independently read
Milnor's Theorems7.1–7.2 and their full proof on printed pages39–41 in
the primary scan at
`/workspace/scratch/a50d05093ca1/source_downloads19/Milnor_MorseTheory_1963.pdf`.
Both the OCR and the rendered physical pages22–23 were inspected; the
Morse-index bound is at most the complex dimension. The closed embedding
therefore gives H3(Z,Z)=0 with all hypotheses explicit.

For any choices of the three commutator nullhomotopies, the map of the
two-skeleton of T3 exists. If its remaining attaching sphere were null,
it would extend to T3. Its composite with the winding map induces I3
on H1 and therefore I on H3 by the exterior cup product, contradicting
H3(Z)=0. This proves a nonzero actual pi2 class for every such choice;
it requires no homotopy model for the nodal presentation complex.

The final scope is correct. X,Y,V remain the aspherical bundles already
used; this refutes asphericity of Z itself. The relevant old0 column
relation lies in the previously audited paired involution orbit, so the
sphere alone does not give a nonzero Tate syzygy or kappa value.

No mathematical correction requested.

## Final strengthening reread

The added section5 also passes. Lift the2-dimensional CW homotopy model
and its inverse to universal covers. Degree-two Hurewicz identifies pi2
with the kernel of a boundary between free integral chain groups, so the
particular nonzero sphere has infinite order. Dividing a nonzero finite
cycle by its largest common power of2 still gives an integral cycle;
the one-chain group has no torsion. Its mod2 reduction is nonzero and
cannot be a boundary because there are no3-cells. Thus the universal
cover is not mod2-acyclic. The proof correctly does not assert that the
original specified sphere is itself primitive or mod2-nonzero.

The final paragraph now explicitly avoids identifying the geometric
sphere with B92's particular syzygy kernel before a geometric comparison.
This is the appropriate scope while the separate comparison note is
under review.
