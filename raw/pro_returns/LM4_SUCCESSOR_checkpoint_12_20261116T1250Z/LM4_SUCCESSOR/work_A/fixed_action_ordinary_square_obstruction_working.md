# A fixed-action ordinary-cup square obstruction

Research proposal, 2026-11-16, approximately12:44UTC. This is separate
from the frozen checkpoint12 formal source. CE's complete independent
proof review passed at approximately12:46UTC; parent review is pending.
The argument concerns a literally tau-fixed full positive
automorphism and a specified finite ACTION. It prescribes no s- or
r-frame and makes no universal Delta-one nonexistence claim.

## 1. The actual stored datum

Use the finite actual quotient D0 of A56/A64/A76, with residual
P0, finite head H, and P0_ab=V^8. Here k=F8, V=k^36, the binary
simple module has dimension108, and P0'=M is globally H-trivial.
The quotient includes the actual old36-dimensional k-center and
the actual C4 source carry; it is not an invented split source.
Its order is 2^972 * 72 * 7^13.

The positive finite action h0 is the one encoded by

  work_A/A63_zero_t_A56_solution.json

and NOT the later W=0 repair used in A66. Its SHA256 is

  4135fabf1500006d5ec6bbe5dc0571ea91018abf911e32136cf965729d18d4e9.

The earlier A64/A65 construction gives an actual full ordinary
positive lift, and passes the selected lower square/frame and
actual scalar tests. The proposed conclusion is that no full
positive h with h(tau)=tau and h_D0=h0 can have (h c)^2=1,
regardless of its conjugators for s and r.

## 2. The ordinary16 quotient and the full source image

Write a:D0 -> V^4 semidirect H for the four normalized free cusp
cocycles. They satisfy a(s)=0 literally. Let T0=V^(3), retaining
the literal cubed scalar action, and T=T0^16. The ordinary group
has multiplication

  (a,z)(b,w)=(a+b,z+w+C(a,b)),
  C(a,b)_(i,j)=a_i^2 b_j       (0<=i,j<4),

coordinatewise at the36 physical weights. Its action by H is
strict. The actual joint source quotient Eord over D0 therefore
has the displayed multiplication used in
work_A/check_A66_ordinary_cubic.py:

  (g,z)(h,w)=(gh,z+rho3(g)w+C(a(g),rho(g)a(h))).

The actual source S is (s0,0). R has the explicitly prescribed
central correction making R^3=1. These identities and the actual
canonical c source action are checked in the saved original-law
certificate.

The full source image is the stated fiber product. On one physical
weight, commutators between two distinct free rows give the pair
(u^2 v,v^2 u), whose F2-span is k^2; a trace annihilator would
force a polynomial with distinct powers2 and4 to vanish on all k.
The same-row brackets u^2 v+v^2 u span k. The old center pairs
opposite physical weights, so these one-weight commutators have
zero old-center component. Thus all16 new copies are attained in
the derived subgroup. The already attained old affine quotient
then gives the full joint residual, by the finite Frattini
argument of A66. In particular the actual new kernel is all T.
Thus the finite detector Eord has the explicit order

  |Eord|=2^(972+16*108) * 72 * 7^13
        =2^2700 * 72 * 7^13.

## 3. Kernel stability and the forced coefficient action

The finite head H has its actual normal odd subgroup with no
invariants on T0. Hence H^1(H,T0)=H^2(H,T0)=0. The five-term
sequence and P0_ab=V^8 give

  H^1(D0,T0)=Hom_H(V^8,T0)=k^8.

The literal intertwiner is j3(v)_lambda=v_partner(lambda)^4.
Its eight source cocycles, together with36 coboundaries, are the
44 columns in the existing ordinary script. Their source rank44
shows that inflation to H^1(Pi,T0) is the complete isomorphism.
Consequently the transgression from Hom_D0(ker(Pi->D0),T0) is
injective.

The16 ordinary extensions are the actual cup classes
e_i^[2] cup e_j, paired by the coordinate product into T0.
The specified h0 fixes the four cusp cohomology classes; canonical
c preserves them with its actual coefficient intertwiner. Their
equivariance and the injective transgression force preservation
of the actual joint source kernel by EVERY full candidate h
inducing h0, and by c. They also force h to act identically on T
and c to act by the coefficient C3, with no freely selectable
kernel action. The Frobenius twist is retained throughout; it is
not replaced by an untyped k-linear identification with V.

## 4. The decisive unframed centralizer-surjectivity lemma

For every g0 in C_D0(s0), the element (g0,0) belongs to
C_Eord(S). Indeed, since a(s0)=0 and g0 s0=s0 g0, the crossed
homomorphism identity gives a(g0)=S a(g0), and the H-head of g0
commutes with S. The two products with S are

  (g0,0)(s0,0)=(g0 s0,0),
  (s0,0)(g0,0)=(s0 g0,0),

because both cup terms involving a(s0) vanish. Therefore

  C_Eord(S) -> C_D0(s0)

is SURJECTIVE. This includes arbitrary centralizing head elements,
not just the original H-head or residual frame family. It is the
extra fact needed to remove the fixed-frame hypothesis.

If two automorphisms of Eord covering h0 both preserve the
conjugacy class of S, their S-images are conjugate by an element
of T. To see this, take their two conjugators B1,B2. The image of
B1^-1 B2 centralizes s0. Lift it to an actual centralizer using
the preceding surjectivity, and cancel it from B2; the remaining
difference from B1 is in T. Thus the difference cocycle has zero
restriction class at <s>, independently of all frame choices.

## 5. Exhaustion of ALL peripheral actions over h0

Let h_* be the actual finite ordinary action constructed by the
saved script. Every induced candidate action has the same action
on D0 and T, so differs from h_* by a T-valued1-cocycle on D0.
The preceding lemma kills its s-restriction class. Literal
h(tau)=h_*(tau)=tau kills its cusp restriction.

For T0 the joint restriction, after pullback to the actual
source subgroups <s> and <tau> in Pi,

  H^1(D0,T0) -> H^1(<s>,T0) directsum H^1(<tau>,T0)

is an isomorphism with dimensions8=4+4. This is the existing
44/40 ordinary coefficient computation, transported by j3 from
the complete source basis. Hence the difference is a coboundary.
More precisely, every candidate is Inner(v) h_* with v in T^tau.
The vector v is unique because T^H=0.

The negative coefficient C3 is the identity on T^tau, as verified
on the entire four-dimensional cusp basis in each copy. Thus
for b_*=h_* c,

  (Inner(v)b_*)^2=Inner(v+b_*(v)) b_*^2=b_*^2.

The negative action square is therefore independent of EVERY
peripheral action lift over h0. The proof did not fix either
frame, their finite heads, or their residual centralizer values.

## 6. The existing nonzero original-law value

work_A/A66_ordinary_cubic_result.json has SHA256

  f3f1c4996e85cc61c743b09238902dfc228696136f6aa0e7190722de0535b3c5.

It records b_*^2=Inner(t), with t in T^tau, and the literal
coordinate

  t_(ordinary00,weight0)=1.

Thus t is nonzero. Since T^H=0, Inner(t) is a nonidentity
automorphism of Eord. The script verifies the equality on the
actual S and R, not merely on an abstract coefficient space.

The independent saved source-law projection is
work_CE/A66_ordinary_projection_independent.json, produced by
work_CE/code/review_A66_ordinary_projection.py/.out. It separately
verifies the same coordinate1 and the vanishing of every
cusp-inner norm direction. Its earlier scope was deliberately
fixed-affine/frame; Sections3--5 above are the proposed exact
exhaustiveness strengthening.

This disproves full negative involutivity for the specified
normalized finite ACTION if the proposed audit passes. It does
not exclude the later W=0 actions (whose square is zero), does
not settle the existential Delta-one question, and does not drop
the literal-tau normalization. It does not require a fresh search
or invent a new scalar quotient.

## 7. Fresh action-only verification

The separate verifier
work_A/code/verify_fixed_action_ordinary_square.py executed
successfully, with genuine stdout in the corresponding .out file
and complete recorded result in
work_A/fixed_action_ordinary_square_verified.json. It preserves
the stored witness. The imported legacy group builder performs
its existing exploratory algebra but writes no artifacts.

The new run checks the actual S/R relations, canonical-c source
action and square, literal positive cusp, complete ranks44/40/36,
the zero free cusp coordinate at S, all192 binary cusp-inner
directions, the coordinate t_00(0)=1, and that the resulting square
moves an actual source generator. Centralizer surjectivity and
all-action exhaustion are the general proofs above, rather than
an enumeration of the enormous finite group.
