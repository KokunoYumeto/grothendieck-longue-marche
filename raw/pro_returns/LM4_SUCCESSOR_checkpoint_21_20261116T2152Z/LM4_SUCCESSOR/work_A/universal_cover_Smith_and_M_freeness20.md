# Universal-cover Smith reduction and the actual freeness gate

Research, 2026-11-16. The universal-cover reduction below has passed
CE's independent conceptual review. It is not an additional vanishing
claim. B102 supplies the actual equivariant two-complex and all source
and covering comparisons used here.

## 1. The based universal cover

Let C be the actual pullback of the symmetric complement to the
universal filled surface, with group K_s. Let C_u be its universal
cover, and lift F at the selected fixed source basepoint. Let D_s be
the actual image in K_s of the fundamental group of the chosen punctured
fixed source. Thus D_s is contained in K_s^F; its projection to the
first residual coordinate is the subgroup I of B92. No source-group
injectivity is assumed.

The same fixed-path lifting argument as B102 gives

    pi0(C_u^F)=K_s^F/D_s.

Indeed a fixed point projects to the fixed source. The source path
from the original basepoint has a pointwise fixed lift; any other
fixed lift differs by a deck element g with F(g)=g. Within the source,
path transport identifies precisely the cosets of its actual image
D_s. Every fixed component is a covering of the punctured source and
is a graph up to homotopy.

## 2. The exact universal Smith group

The reduced cellular complex of C_u is bounded in degrees-2,-1,0 by
B102. Simple connectedness gives H1=0, and Hurewicz identifies H2 with
pi2(C). Consequently this reduced equivariant complex is
quasi-isomorphic to pi2(C) placed in degree-2. Apply the same complete
two-periodic C2 resolution and bounded totalization as B102. Its
degree-zero hypercohomology is H^2(C2,pi2(C)). Smith localization to
the actual fixed graph therefore yields

    H^2(C2,pi2(C)) = reduced H0(C_u^F,F2)
                   = ker(F2[K_s^F/D_s] -> F2).

All maps use the actual selected lift of F. This is not an assertion
that the universal cover is contractible or mod-two acyclic; B100
proves precisely the opposite. The isomorphism describes its genuine
invariant second-homotopy contribution.

Every difference of two universal fixed components has an actual
half-turn sphere representative. Choose fixed points in the two
components and a path gamma between them. The paths gamma and Fgamma
are homotopic relative endpoints because C_u is simply connected.
Glue such a homotopy and its F-image along the two meridian arcs.
The resulting equivariant sphere has exactly those two fixed poles.
Thus the component generators have the same concrete realization as
B102.7; no arbitrary invariant H2 class downstairs is being lifted.

## 3. Naturality to the coefficient cover

The based projection C_u -> C_E is F-equivariant and induces the
Hurewicz map pi2(C) -> Z2. Its fixed-component map is the literal map

    K_s^F/D_s -> R/I,

induced by the diagonal residual image. Naturality of the Smith
comparison gives the commuting square

    H^2(C2,pi2(C))  ->  H^2(C2,Z2)
          |                    | kappa
          v                    v
    reduced F2[K_s^F/D_s] -> reduced F2[R/I].

The bottom map is the coset projection, and both vertical maps use
B102's endpoint convention. For a sphere with poles at1 and diagonal r,
the value is rI-I. The specified diagonal r^-1 translation gives the
right-defect value r^-1I-I.

In particular this specific spherical contribution to kappa is generated
by actual nonlinear fixed-target coset differences. Its nonzero image
is equivalent to an actual fixed element of K_s with diagonal head
outside I. This is a reduction, not a proof that such an element
exists or does not exist. General H_b heads reduce by the actual fixed
source lift as already proved in B92.

## 4. What remains between pi2 and the full domain

The map H^2(C2,pi2(C)) -> H^2(C2,S_sph) is not known onto. Even
surjectivity of the underlying Hurewicz image does not make its group
cohomology map onto. The separate quotient H2(M) in B102.8 is also
uncontrolled. Thus the preceding universal calculation cannot replace
the whole kappa domain by equivariant sphere maps.

For additional precision, the equivariant Cartan–Leray homology spectral
sequence for the M-cover C_u -> C_E has only the rows q=0 and q=2.
Because C_E has a two-dimensional model, its degree3 homology vanishes.
The sole relevant transgression is d3:H3(M)->(pi2(C))_M. Its kernel
is the surviving degree(3,0) term and must be zero. In total degree2,
the filtration gives the exact sequence

    0 -> H3(M,Z) -> (pi2(C))_M -> Z2 -> H2(M,Z) -> 0.

This is compatible with F. It identifies S_sph as the quotient of the
M-coinvariants of pi2 by that H3(M) image, and explicitly records two
possible losses before taking C2 cohomology: M-coinvariants and the
H3(M) quotient. It does not assert their cohomology obstructions vanish.
CE independently reviewed this complete Cartan--Leray addition and
passed the differential degrees, injectivity, filtration, and F action
during checkpoint20.

## 5. Actual M-freeness: present status and source boundary

The group M is N_gen/L after all actual nodal fillings, with N_gen a
free subgroup of the generic free group. Showing that L is free, or
that each individual node relator has a free normal closure, would not
show that the quotient M is free. A proof would need, for example, an
actual simultaneous free-basis/free-factor elimination of the whole
nodal orbit, or an actual graph model for a full filling kernel N_A
containing M. Neither has been established.

The two-colour disjointness and asphericity of the one-sided filled
space do not by themselves give such a graph model. Contractibility
or fundamental-group injectivity of its lifted removed divisors has
not been proved. B101's explicit section kernels occur after filling
the four old q fibers to X0; they cannot be cited as a direct
noninjectivity theorem for the distinct punctured map A intersect V -> V.

Primary boundary read: Antolin, Dicks and Linnell, On the Local-indicability
Cohen–Lyndon Theorem, author PDF dated10February2010,
https://mat.uab.cat/~dicks/CohenLyndon.pdf. Definition2.3 and Corollary6.2,
including its proof, were opened at turn898view0 and turn899view0.
The theorem requires local indicability and an actual tree with trivial
edge stabilizers and the full strongly staggerable family. It produces
freeness of the normal subgroup generated by that family. No suitable
actual tree/staggering has been proved here, and applying it to node
relators in a free pre-filling group would still concern the normal
subgroup L, not the required quotient M. The single-relator case cannot
be extended to the entire orbit without those hypotheses.

No freeness or nonfreeness of M is concluded in this note.
