# Independent review: the actual torus sphere and its involution mate

Reviewed 16 November 2026, checkpoint20 cycle. Working proof, complete
producer, and final formal-source reviews: PASS.

## Inputs read completely

- B100, `sections/b_symmetric_nonasphericity.tex`.
- B104, `work_DE/B104_boundary_models.tex`.
- `work_DE/next_marginal_source/finite_node_F2_provenance_20h.md`.
- `work_DE/next_marginal_source/check_actual_cube_sphere20.py`.
- Its genuine `.out`, `.err`, and `actual_cube_sphere20.json`.
- Full formal proposal `work_DE/B105_torus_spherical_block_proposed.tex`.

The separate geometric face-map audit is
`work_A/review_finite_node_F2_provenance20.md`.

## 1. Actual source and cell conventions

The actual old-zero source lift has both recorded correction words empty.
Thus the far lift t of B100 is literally the source generator, and
u=t^-1 acts on the generic fiber by the stored positive old-zero push.
That push fixes p2,p3,p12,p13 literally. The producer verifies these
statements against the actual full source data, rather than selecting a
new lift with the same lower head.

Set a=p2, x=p12, y=p13 and b=xyx^-1. The node face (6,3) has the
literal attaching word [a,b]. The actual old-zero cylinder faces c_(u,j)
have attaching words [u,p_j] for the generators used here. In the
coefficient group these elements commute with u. Writing e_u=-u e_t,
their boundaries are

    d c_(u,j) = (u-1)e_j + (1-p_j)e_u.

This is exactly B104's cylinder boundary in the original source-edge
coordinate, not a change in the geometric cell convention.

## 2. The conjugated cylinder is an actual disk

The free-word identity

    [u,xyx^-1]
      = [u,x] · x[u,y]x^-1 · (xyx^-1)[u,x]^-1(xyx^-1)^-1

constructs a based van Kampen disk from the actual two cylinder faces.
Its cellular chain is therefore

    C_u(b) = (1-b)c_(u,12) + x c_(u,13).

In particular this is not merely a formal chain with a convenient
boundary. Its boundary is

    d C_u(b) = (u-1)Fox(b) + (1-b)e_u,
    Fox(b) = (1-b)e_12 + x e_13.

## 3. Product-cube sphere and exact boundary

Use the actual node disk, this conjugated cylinder disk, and the actual
cylinder disk for [u,a] as the three faces of a map from the standard
two-skeleton of the three-torus. Its remaining three-cell attaching
sphere has cellular chain, with the indicated consistent orientation,

    z = (u-1)c_[a,b] - (a-1)C_u(b) + (b-1)c_(u,2).

The node boundary is (1-b)e_a+(a-1)Fox(b). Substituting the three
displayed boundaries gives d z=0: the e_a, Fox(b), and e_u coefficients
cancel separately because a,b,u commute in the actual coefficient group.
This identifies an actual spherical element, rather than replacing the
spherical gate by the condition of being a two-cycle.

The complete producer independently evaluates the actual359-face
boundary of this ten-term chain. Its semidirect multiplication uses
u h u^-1=psi_old0(h), with the required powers checked in the actual
word map. Both d z and d F(z) are zero coefficientwise.

## 4. Actual mate and free rank two

The actual node-face map has mate (6,7), with literal generic-fiber
conjugator p12 p14^-1 p12^-1 and stored raw sign +1. The note on the
geometric node-face provenance justifies that this is a single face;
the word identity alone would not have been sufficient.

Thus z has exactly one node-face row, (6,3), with coefficient u-1.
Its mate F(z) has exactly one different node-face row, (6,7), whose
coefficient is (u-1) times a right group unit. The source-cylinder
terms cannot enter either of those node rows. The producer checks the
full word conjugacy, both support statements, and F^2(z)=z.

The element u has infinite order, as witnessed by its old-base free
quotient. Right multiplication by u-1 on any integral group ring is
injective: a finite-support equality lambda u=lambda would make the
support a union of finite right-u orbits, whereas every such orbit is
infinite. This proof needs no domain assertion for the larger ring
Lambda=Z[G semidirect S]. Looking at the two private node rows now gives

    Lambda z + Lambda F(z) = Lambda z direct-sum Lambda F(z)
                           isomorphic to Lambda^2.

## 5. Precise equivariant consequence

F exchanges these two free summands semilinearly. Their underlying
abelian C2-module is consequently induced: use the coefficient action
of F to identify the second copy with the first. All its Tate groups
vanish. Therefore this full actual sphere-orbit submodule contributes
zero to the residual map through its own second involution cohomology.

It is not asserted to be a direct summand of the entire Z2. No assertion
about the Tate groups of the quotient, arbitrary relations with other
spheres, the nonspherical H2(M) quotient, or vanishing of the whole
kappa map follows.

## Final formal-source confirmation

The entire proposed B105 was read after the complete working proof and
producer. Its product orientation (u,a,b), the literal raw node sign,
the order (u-1)h, and the induced integral basis g z <-> F(g)F(z) agree
with the preceding review. The final scope paragraph retains every
necessary limitation. No correction was requested.
