# Independent actual Z³ retract and nonasphericity audit

The proposed B100 mechanism passes. The owned exact checker
`check_symmetric_Z3_marking.py` reconstructs all relevant markings from
the authoritative paired/old-base data. It verifies a=p2=cut4,
b=p12 p13 p12^-1=cut16, node(6,3)=[a,b], and literal old0 push/pull
fixing p2,p12,p13. Thus the actual far old0 lift t commutes with both
a and b in Gamma=pi1(Z); the node relation gives their mutual commutation.

The two physical labels are3=A_v(zeta) and14=B_v(zeta^4). Their irreducible
holomorphic factors are fA=v-zeta and fB=q+(zeta^4-1)v-zeta^4. The latter
is primitive and linear in w, with its coefficient v coprime to its
constant term, hence irreducible. Both are distinct boundary components.
Their positive meridians are exactly a and b in the audited cut marking.
The winding map chi=(wind fA,wind fB,wind q) therefore sends a,b to the
first two standard basis vectors. The literal old0 far lift has constant
v=10^6/ROT. Its fA is constant and its fB=C+q has |C|>10^5 while the
entire old0 q lasso lies in |q|<1/10. Hence both first windings vanish
and its positive q winding is1. The checker proves stronger exact
rational bounds. Thus chi(a,b,t) is the identity matrix.

The literal B87 point is transported by the already certified
q399/40000→q1/100 fixed-source bridge and an outer-half-plane fiber
whisker to the far marking. All three loops are transported together;
characters are unchanged under this based conjugation. No generic-fiber
basepoint is silently identified with P. Commutativity and the primitive
detector show that the homomorphism Z³→Gamma with basis(a,b,t) is an
injection and chi is its retraction.

The actual surface Z is the principal complement D(v,w)≠0, where

 D=v w(v-w) product_{u∈mu5}(v-u)(w-u)(vw-u)
   times product_{u∈mu5\{1}}[v(w+u-1)-u][w(v+u-1)-u].

Its graph Dz=1 is a closed smooth affine complex surface in C³; the
z derivative is D, nonzero there. Milnor's Morse Theory(1963),
Theorems7.1 and7.2,printed pages39–41, therefore gives H3(Z;Z)=0 and
the homotopy type of a CW complex of dimension at most2. The actual
primary scan was reopened independently at
https://math.stanford.edu/~ralph/math215b/Milnor.pdf
(web refs turn876view0,turn877view0, screenshots turn878view0/1).
The exact source hypotheses are checked using the closed graph embedding,
not by treating an arbitrary open submanifold as closed affine.

Choose the actual three commuting loops and null-homotopies of their
commutators to define f:T³^(2)→Z. Let psi:S²→Z be the image of the
attaching sphere of the remaining torus3-cell. If psi were null, f
would extend to F:T³→Z. The continuous phase map defined by(fA,fB,q),
normalized at the basepoint, has chi as its pi1 map. Its composite with
F induces the identity on pi1(T³), hence is homotopic to the identity
because T³ is K(Z³,1). Its H3 map is therefore the identity, contradicting
H3(Z)=0. Thus psi is a concrete nonzero pi2 class. Since Z has a
2-dimensional CW model, the Hurewicz group pi2(Z)=H2(universal Z) is
a subgroup of a free abelian cellular2-chain group; the nonzero class
has infinite order. In particular Z is not aspherical.

This refutes the proposed aspherical-universal-cover/Smith shortcut for
this actual Z. It does not refute the projected fixed-source gate or the
nonlinear fixed-lifting conclusion, neither of which follows merely
from asphericity failing. No completed intersection or coefficient-module
claim is added.

## Final formal-source review and the mod-two strengthening

The complete formal candidate `sections/b_symmetric_nonasphericity.tex`
has now been read independently, including the exact principal-complement
polynomial, common based marking, far-lift estimate, torus-cell extension
argument, and final scope paragraph. The proof passes. In particular,
the literal bound |C|>10^5 for C=(zeta^4-1)10^6/ROT-zeta^4 is stronger
than needed against the formal lasso bound |q|<6. The owned certificate
also checks the much smaller actual old-zero lasso.

The following limitation is essential and is now present in the formal
candidate: the geometric torus attaching sphere is not identified with
an element of B92's particular relation kernel Z2. Such an identification
requires an actual geometric-to-presentation comparison. The old-zero
column slots occur in B95's induced involution summands, but that fact
does not by itself assign the sphere a class there or produce a nonzero
value of kappa.

The universal cover is also not mod-two acyclic. Let K be the
two-dimensional CW model supplied by Milnor and let Ktilde be its
universal cover. Covering invariance of higher homotopy and the
degree-two Hurewicz isomorphism give

  pi2(Z) = pi2(Ktilde) = H2(Ktilde; Z) != 0.

Since Ktilde has no cellular three-cells, H2(Ktilde; Z) is a subgroup
of the free abelian cellular chain group C2(Ktilde; Z), and hence is
free abelian. Its nonzero rank implies that tensoring with F2 is
nonzero. The homology universal coefficient theorem and
H1(Ktilde; Z)=0 therefore give

  H2(Ktilde; F2) = H2(Ktilde; Z) tensor F2 != 0.

This proves the existence of nonzero mod-two second homology, and the
nonzero torus sphere has infinite order. It does not assert that this
particular sphere is primitive or has nonzero reduction modulo two.

Primary textbook verification: Hatcher, A. (2002), Algebraic topology,
Cambridge University Press, Theorem 4.32 on printed page366 with its
complete proof on page367; the latter explicitly states the universal-
cover pi2/H2 consequence. Proposition4.1 on page342 proves covering
invariance in degrees at least two. Theorem3A.3 and Corollary3A.4 on
page264 give the homology universal coefficient theorem. The complete
author-hosted PDF and these precise passages were opened, not inferred
from an index or secondary quotation. Exact URLs and bibliographic
verification are in `B100_Hatcher_source_audit_19h.md`.

The amended formal B100.5 was then read in full and also passes. It
uses the shorter direct cellular argument instead of the optional
UCT paragraph above: take a nonzero finite integral two-cycle, divide
its coefficients by the largest common power of two, and use the
torsion-free cellular one-chain group to see that the quotient remains
a cycle. Its nonzero mod-two reduction cannot be a boundary because
the universal CW model has no three-cells. This proves the same
nonacyclicity with no assertion that the particular torus sphere is
primitive. The completed formal scope paragraph B100.6 retains the
required distinction from B92's chosen equivariant relation kernel.
