# The actual odd central gate and a proposed symplectic extension argument

Working proof after A80; not yet a formal theorem. Root independently
derived the central-boundary correction, and CE is auditing the actual
central source model. No assertion below is promoted before those reviews.

Notation: Pi=C2 amalg C3, tau=sr, q:Pi→Q factor-faithful finite,
L=ker q, p∤2|Q|, M=L/Phi_p(L), G=Pi/Phi_p(L). The negative lower
action b0 and its two norm-one frames satisfy A80.1. Put k=Fp.

## 1. The actual new p-central source cover

Let N=Phi_p(L), Z=N/[N,Pi], and let E_p be the actual source-central
quotient Pi/[N,Pi] with all prime-to-p factors of its finite central
kernel removed. Finiteness follows by A79's transfer argument. Write
A=ker(E_p→G), and Ptilde for the preimage of M. Thus

  1→A→Ptilde→M→1

is central, A is a finite p-group, and Q acts on Ptilde up to inner
automorphisms. The module M has no Q-coinvariants: from the actual
relation sequence its trivial multiplicity is 1+1−1−1=0.

Put A'=ker(Ptilde_ab→M). The Q-action on Ptilde_ab is literal and A'
is trivial. Coinvariants are exact on finite abelian p-groups because
|Q| is invertible. If A' were nonzero, Ptilde_ab would have a nonzero
Q-invariant character to Cp. Pulling it back to L gives a nonzero
Q-invariant mod-p character of L, contradicting M_Q=0. Hence
Ptilde_ab=M and A=Ptilde'. The commutator pairing factors through M
and is Q-invariant, so

  A is a quotient of W=(Lambda²_k M)_Q.

In particular A is elementary abelian. Since p is odd, the pth-power
map is an additive Q-map M→A: the class-two cross term has coefficient
p(p−1)/2 and vanishes. Its target is trivial and M_Q=0, so this map
vanishes. Thus Ptilde has exponent p.

Conversely define the actual target P(M)=M×W with BCH law

  (a,z)(b,w)=(a+b,z+w+(a∧b)_Q/2),

and let Q act naturally on M and trivially on W. Split the actual
G=M⋊Q, and write its source s=(a_s,s0), r=(a_r,r0). The source lifts
in P(M)⋊Q are

  S=(a_s,0,s0),
  R=(a_r,−(a_r∧r0 a_r)_Q/6,r0).

Indeed (1+s0)a_s=0 and (1+r0+r0²)a_r=0. The displayed S has square1;
the cube of (a_r,z,r0) is 3z+(a_r∧r0 a_r)_Q/2. The source image
surjects G. Its L-image surjects M, so its commutators attain the
whole W. Therefore the source image is the entire P(M)⋊Q. The
upper bound and attained target identify E_p with this marked model.
This proves the actual central-kernel assertion, not merely a
calculation of an abstract Schur multiplier.

## 2. The exact cusp residue and its boundary ambiguity

Apply an inner change of the entire marked model identification over Q
so that the actual cusp has form

  tau=(a0,z,t),   t a0=a0,   tau^m=(m a0,m z,1),   m=ord(t).

This is possible because the non-t-invariant part of its affine
coordinate lies in (1−t)M. Lift the correcting affine vector to P(M)
and conjugate the marked source map by that element. The target law
and its canonical strict Q-action stay fixed, while the actual source
identification changes by an isomorphism over Q; its kernel is unchanged.
All source coordinates and their central terms are transported together.
Let P_boundary=<Q·a0>⊂M. It is the
boundary submodule of A80.9 (multiplication by m is invertible).

Let B be a b0-semilinear involution of M that acts as the prescribed
negative cusp permutation on P_boundary. Its exterior action B_W
on W has square1. The homogeneous automorphism of P(M)⋊Q sends

  (a,z,q)→(Ba,B_W z,b0(q)).

Its negative cusp discrepancy is (1+B_W)z. It is a W-valued central
element fixed by B_W. We can modify the action on G by Inn(v), with

  v∈M^t,   Bv=−v.

This keeps the action involutory and keeps the affine cusp literally
inverted. Its homogeneous lift in the BCH cover still has square1
because v+Bv=0 and v∧Bv=0. Its central cusp discrepancy changes by
−(v∧a0)_Q (equivalently +(a0∧v)_Q). All signs use commutator
[x,y]=xyx^{-1}y^{-1} and the displayed one-half BCH convention.

The map

  M^t→(P_boundary∧M)_Q,    v→(a0∧v)_Q

is surjective. Move every Q-translate of a0 back to a0 in coinvariants,
then average its other argument over <t>. It is equivariant if its
source is given the action −B and its target B_W. Consequently every
B_W-fixed element in this image has a preimage with Bv=−v, by C2
averaging. Thus all boundary/mixed central residues are removable.

Modulo this image, the center is (Lambda² H)_Q for H=M/P_boundary,
the compact-surface homology. Use an oriented surface presentation
with r=|Q|/m boundary generators, each conjugate to tau^m. In the
central BCH quotient after killing P_boundary, each boundary generator
contributes m z. The handle commutators contribute the symplectic
bivector omega=sum_i A_i∧B_i. Hence

  |Q| z + omega = 0  in (Lambda² H)_Q.

Any consistent reversal of the global boundary convention changes
both signs together and does not change the resulting criterion.
The class omega is Q-invariant and corresponds to the inverse of the
actual nondegenerate intersection form. Since p∤|Q|, invariants and
coinvariants agree by averaging. Therefore the remaining central
cusp residue vanishes precisely when

  (Lambda² B) omega = −omega,

that is, when B on H is anti-symplectic. With this condition the
boundary correction above makes the cusp exactly inverse in E_p.

Uniqueness of a lift over fixed G-data is also useful: its coefficient
action on W is forced by commutators, and two lifts with that action
differ by Hom(G,W)=0, since G_ab is a quotient of C6. The above
boundary corrections alter the G-action itself and are not being
mistaken for invisible scalar corrections.

## 3. Anti-symplectic involutions over an algebraic closure

Here is a proposed algebraic lemma, including the parity issue.
Work over an algebraically closed field of characteristic zero.
Let H be the actual compact-surface symplectic Q-module. For a
nontrivial irreducible Q-module S, its multiplicity is

  m_S=dim S−dim S^{s0}−dim S^{r0}−dim S^t.

The trivial multiplicity is zero. This follows by subtracting the
boundary module from the actual relation sequence:

  [H]=2[1]+[kQ]−[k(Q/<s0>)]−[k(Q/<r0>)]−[k(Q/<t>)].

Duality and b0 twisting commute on irreducibles. Decompose into their
orbits. The cases below construct a b0-semilinear involution B_H
that negates the actual symplectic form.

(a) On four-element orbits S,S*,S^b,(S*)^b, choose a twisted map
between the two dual pairs, give its dual partner the negative
adjoint, and use the inverse on the return map. This is anti-symplectic
and squares to1. If b fixes the two distinct dual constituents,
choose an involutory intertwiner A on S and use −(A^{-1})* on S*.

(b) Suppose S is not self-dual and S^b=S*. There is a nondegenerate
twisted bilinear form F on S, unique up to scalar, satisfying

  F(qx,b0(q)y)=F(x,y).

Its transpose is plus or minus F. If it is symmetric, tensor with a
symmetric form on the multiplicity space. If it is alternating, the
multiplicity m_S must be even; that parity is verified below, and one
tensors with an alternating form. In both cases the total twisted
form on X=S^{m_S} is symmetric. If A:X→X* is its matrix, then

  B_H(x,phi)=(A^{-1}phi,A x)

on X⊕X* has square1, is b0-semilinear, and negates the standard
symplectic pairing.

For the required parity in the alternating case, use the exact
norm-one lower frames. The forms

  F_s(x,y)=F(x,beta0 y),     F_r(x,y)=F(x,J0 y)

are alternating and nondegenerate because b0(beta0)=beta0^{-1}
and b0(J0)=J0^{-1}. The operator s0 preserves F_s. The operator r0
is self-adjoint for F_r: F_r(r0 x,y)=F_r(x,r0 y). Likewise t is
self-adjoint for F. Consequently the fixed subspace for each of
s0,r0,t is nondegenerate for its indicated alternating form. All
three fixed-space dimensions, and dim S itself, are even. The
displayed formula makes m_S even.

(c) Suppose S is self-dual and b0 fixes its isomorphism class. Let
F be its invariant form, of symmetry epsilon=±1. Choose an
involutory intertwiner A; its multiplier on F is nu=±1. The
symplectic isotypic block is S⊗U with form F⊗G, where G has
symmetry −epsilon. Seek B_H=A⊗J. If nu=−1, use J=1. If nu=+1,
take an involutory anti-isometry of G. This always exists for an
alternating G. For a symmetric G it exists over the algebraic
closure when dim U is even. In that case F itself is alternating,
so the fixed subspaces of every finite-order Q-element are
nondegenerate alternating spaces; the same multiplicity formula
again makes dim U even. Thus this final parity obstruction vanishes.

(d) If b0 exchanges two distinct self-dual constituents, their
symplectic isotypic blocks have the same type and multiplicity.
Choose a twisted anti-isometry between them and its inverse for
the return map. Such an anti-isometry exists over the algebraic
closure, since the invariant form on each simple is unique and
the multiplicity forms of a fixed symmetry and dimension are
isometric. Multiplication by a square root of −1 converts an
isometry to an anti-isometry if necessary.

These cases are exhaustive. All constructions can be performed
over algebraic numbers: the rational Q-representation and form are
defined by the actual integral homology lattice; decomposition,
intertwiners, and the finitely many required square roots use a
finite extension of Q. Extend the boundary submodule by its fixed
signed permutation action and use a rational Q-splitting of the
actual homology sequence.

## 4. Reduction at fresh split primes

Choose a number field containing all entries of the resulting B,
and a finite Galois closure. Avoid the finitely many denominators,
|2Q|, and any basis determinants. At every completely split prime
outside this set, reduction gives an Fp-linear B on the actual
mod-p relation module with

  B²=1,  B(qv)=b0(q)Bv,
  B|P_boundary = negative cusp permutation,
  B|H anti-symplectic.

Such primes exist infinitely often. Primary source opened directly:
Milne, J.S. (2020), Algebraic Number Theory, v3.08, Theorem8.31 and
Corollary8.32, printed147 (PDF index148),
https://www.jmilne.org/math/CourseNotes/ANT.pdf . Only existence of
completely split primes outside a finite set is used. No explicit
prime or huge coefficient matrix has been computed.

If Sections1--3 pass audit, each of these primes permits the boundary
correction and therefore an actual involutory action on the new
p-primary central source cover with literal cusp inversion.

## 5. The other central primes and the ordinary lifting criterion

This final compatibility passage also requires review. For ell≠p,
restriction along N⊂L gives

  Hom_Pi(L,Q_ell/Z_ell) ≅ Hom_Pi(N,Q_ell/Z_ell),

because L/N=M is a p-group and its positive-degree cohomology on
ell-primary trivial coefficients vanishes. Thus the ell-primary
parts of L/[L,Pi] and N/[N,Pi] agree under the actual source map.
There is no p-part in L/[L,Pi], since M_Q=0. Hence the full actual
central refinement above G is the actual fiber product of its new
p-primary cover with the old actual Q-central refinement over Q.

For A79 the old central refinement already has a compatible
involutory negative action with literal cusp and frames, independently
of the new coefficient choices. Pair that action with the corrected
new p-central action. The source image is the full fiber product:
over Q the two kernels have coprime orders, and the actual source
surjects both. Frames pair over their identical prescribed Q-values.
Canonical c acts on all these actual source quotients. Their product
with c gives the central positive automorphism required by A3.

If accepted, A3 supplies an ordinary full positive lift of the selected
finite G-action, while A80's detector argument excludes every full
negative involution inducing it even without cusp normalization.
This is a stronger source-central counterexample; it remains a
specified finite action and does not exclude the surviving W=0
existential choices. It does not assert compatible all-step scalar
actions beyond the first central refinement used by A3.
