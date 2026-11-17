# Exact boundary subgroup: candidate HNN proof for independent review

Root research, 17 November 2026, before checkpoint24. This note is not a
new numbered theorem. Its complete comparison and topology argument were
sent to DE for independent review. No assertion about the final annular
cross quotient follows without a further comparison.

## Actual regional quotient and marking

Kill the regional generators a,b,d and retain e. In the actual regional
group the resulting presentation is

R_e = <C,k,z,e | C^2, [C,z], [k,z], [k,e], [e,CeC]>.

The selected cone c=aCa^-1 maps to C. The actual full boundary
T=a b z d e k^-1 maps to z e k^-1. Its product with k maps to z e.
The auxiliary character delta takes C to 1 and z,k,e to 0; it is NOT
the original ordinary-cover character, which takes z to 1.

The delta kernel is the graph group G on the five-cycle
k--z--K--E--e--k, where K=CkC and E=CeC. The involution C interchanges
k,K and e,E while fixing z. Thus R_e=G semidirect C2(C).

## An exact iterated HNN presentation

Put r=e^-1 E. The four-vertex path group on k--e--E--K is exactly

L semidirect_alpha Z(e),  L=F(k,K,r),
alpha(k)=k, alpha(r)=r, alpha(K)=r^-1 K r.

Indeed E=e r, so [e,E]=1 is [e,r]=1 and [E,K]=1 is precisely
e K e^-1=r^-1 K r. These substitutions give inverse presentations;
the displayed automorphism has inverse K -> r K r^-1, fixing k,r.

Adjoin z commuting with k,K and put s=z e. Then the full five-cycle
presentation becomes

G=<L,s,e | s k s^-1=k, s(r K r^-1)s^-1=K,
                e l e^-1=alpha(l), l=k,K,r>.

Let H0=<k,r K r^-1> and H1=<k,K> in L. They are embedded free groups
of rank two, and alpha restricts to an isomorphism H0 -> H1. Therefore

J=<L,s | s h s^-1=alpha(h), h in H0>

is a proper ordinary HNN extension, with L embedded. Also

G=J *_{L} (L semidirect_alpha Z(e)).

Both copies of L embed, so the ordinary amalgam normal form embeds J
in G. Replacing r by s^-1 q gives the inverse presentation

J=<k,K,s,q | [s,k], [q,K]>
 = Z^2(k,s) * Z^2(K,q),  s=z e, q=s r=z E.

The involution C interchanges the two indicated factors. Hence
<C,k,z e> in R_e is J semidirect C2(C), with C interchanging the two
free factors; equivalently it is C2(C) * Z^2(k,z e).

The actual regional subgroup <c,k,T> is consequently an embedded
C2(c) * Z^2(k,T): the presentation map exists since [k,T]=1 and c^2=1,
and its composite with R -> R_e is injective by the displayed calculation.

## Candidate full induced profinite topology proof

We claim that J has full induced profinite topology in G; the following
argument must be independently reviewed before formal use.

Let psi:J -> F be any finite quotient. Since L is finitely generated,
choose a characteristic finite-index subgroup N of L contained in
ker(psi restricted to L). In particular alpha(N)=N. Put Q=L/N. The
images of H0,H1 in Q are isomorphic through the induced automorphism
alpha, so the finite-base HNN extension

J_N=<Q,s | s h s^-1=alpha(h), h in image(H0)>

is proper. The map psi factors through J_N. Let m be the finite order
of alpha in Aut(Q), and form

G_N = J_N *_{Q} (Q semidirect_alpha C_m).

The original G maps onto G_N, sending e to the cyclic generator.
The group J_N is a finitely generated fundamental group of a graph of
finite groups, hence virtually free and residually finite. Choose a
finite quotient of J_N injective on the finite Q, and combine it with
psi. Its image F' is finite, contains Q injectively and maps onto the
image of psi. The ordinary amalgam

F' *_{Q} (Q semidirect_alpha C_m)

is again a finitely generated fundamental group of finite groups. A
finite quotient of it can be chosen injective on the finite F'. The
composite finite quotient of G therefore has kernel on J contained in
ker psi. This is exactly the full induced profinite topology assertion.
No virtual retraction of J from G is used.

For clarity, the finite-graph-of-finite-groups facts have an elementary
permutation proof in this setting. Represent each finite vertex group
freely on the same finite number of points, divisible by all its orders.
Restrictions to an edge group are disjoint unions of regular edge
actions with the same total cardinality, hence can be aligned by a
permutation. On a tree of vertex groups align these recursively; for
each HNN edge use a permutation intertwining the two free edge actions.
This gives a finite permutation quotient injective on every vertex
group. Its finite-index kernel acts freely on the Bass--Serre tree and
is a finitely generated free group. A finitely generated virtually free
group is residually finite: separate an element of the free kernel by
a characteristic finite-index subgroup of that finitely generated
free kernel, which is normal in the whole group; elements outside the
kernel are already separated by the finite quotient. These steps use
ordinary free-group residual finiteness and the tree normal form only.

Now J is invariant under C. Given a finite-index normal subgroup in
J semidirect C2, first use the full topology of J in G and then intersect
the resulting finite-index normal subgroup of G with its C-conjugate.
The finite semidirect quotient by C2 separates the C coordinate and
has intersection with J inside the prescribed kernel. Thus
J semidirect C2 has full induced topology in G semidirect C2.
The actual quotient R -> R_e transfers this topology back to the
already embedded marked <c,k,T> in R.

## Corner-side comparison and remaining gates

In the isolated corner's j-even subgroup, the exact graph product path
is D--k--u--k'--c, with D,c of order two and the other vertices infinite
cyclic. Put T=uD. The subgroup <c,k,T> is a retract of this j-even
subgroup: send D,k' to 1, u to the actual T, and fix c,k. Each graph
relation is respected because [k,T]=1, and T itself is fixed. Hence
the common subgroup also has full induced topology in the corner,
by this retraction and finite index.

This does not prove that a profinite amalgam of the two full vertex
groups over this common subgroup is proper. Nor does it show that any
such intermediate amalgam embeds after the four remaining actual prefix
mirror relations and the retained regional relations. The exact source
centralizer in the final quotient, the other necks, global transfer and
the main icosahedral decision remain Open.

## Additional discrete common-neck intersection candidate

There is a second HNN description of the same actual one-family quotient.
Write H=<C,k,s | C^2,[k,s]>, C'=s^-1 C s, r=C'C, and keep stable e.
The subgroup D0=<k,C,C'> is Z(k)*C2(C)*C2(C'). For example, the kernel
of H -> Z taking s to 1 and C,k to 0 is the free product of Z(k) and
the involutions C_n=s^-n C s^n over all integers n. This follows directly
by rewriting the presentation; D0 is its full free factor on k,C0,C1.

The automorphism beta of D0 is
beta(k)=k, beta(C)=C C' C, beta(C')=C.
Its inverse fixes k and sends C to C', C' to C' C C'. It fixes r=C'C.
The candidate exact presentation is

R_e=<H,e | e d e^-1=beta(d), d in D0>.

To verify it, put z=s e^-1. The equations [k,z]=[k,e]=1 are equivalent
to [k,s]=[k,e]=1. The equation [C,z]=1 is e^-1 C e=C'=s^-1 C s.
Together with [e,CeC]=1 it is equivalently the two equations
e C e^-1=r^-1 C and e r e^-1=r, which give the displayed beta action.
All substitutions are reversible; the two copies of D0 are embedded.

Set p=C s k^-1, the image of the actual P5. The homomorphism H -> Z
taking s to 1 kills D0 and takes p to 1. Thus every nonzero integral
power of p avoids both HNN associated subgroups. Britton reduction then
shows that <e,p> is free of rank two, and its intersection with H is
exactly <p>: every freely reduced word involving an e letter remains
HNN-reduced, after grouping adjacent e letters and nonzero p powers.

The actual common neck K maps onto <e,f>=<e,p>, because f=p e^-1 and
the other three deleted families were killed. Since the actual regional
H=<c,k,T> maps injectively to this H, any element of K intersect H maps
to p^n and must equal P5^n. Conversely P5 belongs to both. Hence this
argument proposes the exact DISCRETE equality K intersect <c,k,T>=<P5>.
It was sent for independent review. No completed intersection equality
is inferred from the discrete equality or from the two induced topologies.
