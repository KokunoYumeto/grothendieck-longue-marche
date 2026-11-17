# The actual mirror-even HNN exists, but the proposed edge enlargement fails

Research, cycle26. This is an exact obstruction to retaining the proposed
base group. It is not an obstruction to another presentation of the final
group and gives no selected-centralizer decision.

## 1. The genuine stable letter before the cross filling

Start from B125's proper ordinary star
A0=Q0 *_K R0 *_(K1) Q1, with K1=C K C,
j0=j and j1=CjC. Take the kernel of mirror parity, which is one on
j0,j1 and zero on R0. Its graph has two R0 vertices and two edges.
Collapse the K edge. Write p(r)=j0 r j0 and R0'=p(R0). The resulting
proper base is

    V=R0 *_K R0',   p(u)=eta(u) for u in K.

The second edge gives a genuine stable letter t=j0j1. Its exact
edge relations are

    t u t^-1 = sigma(u)=p(C eta(CuC) C),  u in K1.

Both edge maps are injective: they are the original K1 inclusion
and its actual reflected copy. This is a genuine HNN presentation
before the cross relation, with no fictitious independent z*=gh.

Put a1=CaC, k1=CkC and v0=p(a a1^-1). Then B125's t0 equals
v0 t. The actual cross relation t0 k1 t0^-1=k becomes

    t k1 t^-1=s,   s=v0^-1 k v0.

One might attempt to enlarge the domain edge from K1 to
L1=<K1,k1>=C<K,k>C, using B117, and to regard this as an HNN
extension of the unchanged proper V. The next calculation disproves
that proposed extension even at the level of a homomorphism.

## 2. An actual domain relation with nontrivial target

The actual domain has [k1,a1]=1, obtained by C-conjugating [k,a]=1.
Its proposed target is

    [s,sigma(a1)] = [v0^-1 k v0, p(C eta(a) C)].

Write A=eta(a), q=p(a1). Since p(a)=eta(a)=A is in the common K,
we have v0=A q^-1 and s=q A^-1 k A q^-1. Conjugate the displayed
target commutator by q^-1. The result is exactly

    [ A^-1 k A,  p(C v C) ],
    v=a^-1 eta(a)a.

The literal actual reflection formula is

    eta(a)=a B a^-1 B^-1 a^-1,
    v=B a^-1 B^-1.

Thus C v C=b a1^-1 b^-1 is nontrivial in the embedded free
conjugate neck C K C. The regional retraction r:R0->K fixes K
and has companion r(CuC)=zeta(u), where zeta kills a,B,d,e
and fixes f. Consequently r(C v C)=1. If C v C belonged to K,
the retraction would fix it and force it to be trivial, a contradiction.
Hence p(C v C) lies in R0' outside the common edge.

The other factor A^-1 k A lies in R0 outside K: the actual geometric
base-winding character is one on k and zero on K. Both its inverse
and the inverse of the second factor remain outside the edge.
Therefore this commutator is a reduced alternating word of length four
in the genuine amalgam V. It is nontrivial by ordinary normal form.

This proves the proposed extension L1->V does not respect the actual
relation [k1,a1]=1. No question of injectivity of that extension arises:
it is not a homomorphism with the specified values.

## 3. The actual final quotient kills a nontrivial base element

Before filling, the genuine HNN embeds V. After the actual cross
relation, t k1 t^-1=s and the retained edge relation sends a1 to
sigma(a1). Conjugating [k1,a1]=1 by t therefore kills the nontrivial
V word [s,sigma(a1)]. Thus V itself does not survive injectively
under this final cross quotient. This is a concrete actual failure
of the unchanged-base HNN proposal, not a general warning about
unspecified amalgams.

It does not rule out a further quotient of V followed by a legitimate
edge enlargement, a different graph-of-groups construction, or the
main selected-source centralizer equality. All actual regional
relations, both mirror edge maps and the full cross relation are
retained throughout. No finite group census is used.

Independent orientation/normal-form check: DE full read passed in
agent correspondence, with no correction. The literal universal word
identities are retained in the adjacent exact checker/output.
