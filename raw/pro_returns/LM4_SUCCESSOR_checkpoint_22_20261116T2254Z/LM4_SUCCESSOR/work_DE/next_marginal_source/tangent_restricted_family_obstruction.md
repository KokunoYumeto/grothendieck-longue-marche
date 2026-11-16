# Exact restricted-family obstruction and the actual remaining source

This note concerns the B81 marking. It does **not** refute the full actual
marginal equality I=R, nor the joint-source comparison or the completed A5
centralizer statement.

## The actual restricted subgroup and its one uniform normalizer

Write V=(V1,V2,V4,V6), with A,B,C as in B81. These seven elements are a
free basis of the unordered fiber F7. Put Gamma0=<alpha0,alpha2,alpha3,
alpha4,alpha5> and J0=<gamma(Vj):gamma in Gamma0>. Exact substitution of
the original inverse source meridians gives, in their original order,

    w4=V4, w1=V1, w2=C^-1 V2 C, w6=C^-1 V6 C.

The width-one restrictions give alpha5(C^-1 V2 C)=V2 and
alpha3(C^-1 V6 C)=V6. Consequently J0 is exactly the Gamma0 orbit subgroup
of the actual four source meridians. This is a source identification,
not only an inclusion of convenient words.

Let K0=ker(V*<C> -> <C>). The node argument proves K0<=J0. Every generator
of Gamma0 and its inverse sends C to k C k^-1 for k in K0. For a positive
node k=Vj; for its inverse k=C^-1 Vj^-1 C; alpha0 fixes C. Starting with
K0 and repeatedly adjoining all images under these ten operators gives
an increasing union equal to J0. If a stage Kn is normalized by C, then
for each operator gamma, gamma^-1(C) belongs to Kn C Kn. It normalizes
Kn, so C normalizes gamma(Kn), and hence the next stage. Thus C normalizes
the **whole** J0. Closure gives the same actual compact normalizer
statement. This does not supply the other ordered-fiber directions.

## Ordered fiber and the missing direction

The ordered double-cover character has chi(A)=chi(B)=1 and vanishes on
V and C. Choose transversal {1,A}. A literal Schreier free basis of its
index-two subgroup F13 is

    s1,s2,s3,s4 = V1,V2,V4,V6;
    s5,s6,s7,s8 = A V1 A^-1,A V2 A^-1,A V4 A^-1,A V6 A^-1;
    s9=C, s10=E=A C A^-1, s11=A^2, s12=B A^-1, s13=A B.

The independent actual sheet calculation in
work_CE/research_tangent_selected_family.txt identifies the normal closure
N=< <s1,s2,s3,s4> > in F13 with one complete moving-point family, for the
larger-root base lift. Its quotient Q is free on s5,...,s13. Let ell:Q->Z
be exponent sum in s10=E (sixth in that quotient basis). Compose with the
filling map to regard ell also as a character of F13.

The exact ordered action table proves, for every generator/inverse gamma
of Gamma0,

    ell o gamma = ell on all13 basis elements;
    gamma(Vj)=h_(gamma,j) Vj h_(gamma,j)^-1 with ell(h_(gamma,j))=0.

These are finite identities for all ten actual automorphisms and all40
peripheral conjugators. They imply the same two assertions for arbitrary
compositions: the new conjugator is gamma(h) h_(gamma,j), whose ell value
is zero. No finite-depth orbit extrapolation is used.

In N_ab, the free basis is indexed by Q and the four selected meridians.
Every Gamma0 translate of Vj is supported at a Q-index with ell=0.
Therefore E V1 E^-1, supported at ell=1, is not in J0. The next finite
argument strengthens this to separation of actual closures.

## Explicit finite separation

Let W=(C2 x C2) semidirect C2, the order-eight wreath product. Write its
elements ((a0,a1),t), with t exchanging the two coordinates. Define a
homomorphism F13->W by

    s1,s2,s3,s4 -> ((1,0),0);
    s10=E -> ((0,0),1);
    every other si -> identity.

For h in F13, conjugation of the first toggle depends only on ell(h)
modulo2. The preceding exact invariant therefore implies that every
Gamma0 translate of every Vj maps to the first toggle. Hence J0 maps
into its order-two subgroup. But E V1 E^-1 maps to the second toggle,
which is outside that subgroup. Thus J0<N, and the actual closure of J0
is proper in the closed selected-family kernel in the full completion
of F13. The finite quotient is continuous and F13 has full induced
topology in the actual ambient group by B81 and finite index.

This map is not asserted to factor through the entire bundle group.
It separates a fiber subgroup, exactly as needed to refute the proposed
J0=N route. It is not a separator of I.

## Why the full source has not been tested by this obstruction

Gamma0 omits alpha1^2, although this actual even source loop preserves the
ordered family. It also omits alpha1 Gamma0 alpha1^-1. The full even base
subgroup has all eleven of these Schreier generators. In the ordered
retained marking,

    D^2=(BC)^2 = (B A^-1)(A C A^-1)(A B) C
               =s12 s10 s13 s9,

so ell(D^2)=1. The exact whole-U transport of B81 already supplies this
missing direction to the full source. The new even action table is being
checked without inferring normality from its index lattice. Additional
conjugation by the other source-family meridians also belongs to the
actual full subgroup. All of these must be retained in any full-source
claim.

## Genuine certificates and scope

`tangent_ordered_family.py/.out` constructs and checks the actual ordered
Schreier basis and all ten restricted automorphisms; it also computes a
rank-six invariant affine index lattice for each selected label. The
finite separation uses only the common exact character ell, not the
larger lattice computation. `tangent_restricted_family_obstruction.py/.out`
checks all whole-character/peripheral identities and the exact order-eight
head. JSON files contain all maps and the separating word. The first
producer's JSON-serialization failure is preserved separately; its rerun
succeeded after converting exact SymPy integers to JSON integers.
