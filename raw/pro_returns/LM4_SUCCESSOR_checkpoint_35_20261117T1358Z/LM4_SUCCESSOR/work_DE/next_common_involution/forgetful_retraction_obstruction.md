# The natural finite-index four-point retraction does not recover the source

Research result, 16 November 2026. The kernel computed here concerns a
specific additional forgetting map, not K and not an arbitrary virtual
retraction.

Use Q8-tilde from the full-dihedral-centralizer note. Write U for the
ordinary label from the original pole pair {1,3}; choose V to be the
ordinary label from {2,5}, the i=0 pair in the cyclic coordinates. Let
G=C_Gamma(D5)≅C2*Z, and let G_V be its subgroup fixing V. The induced D5
action on the five non-pole ordinary labels is faithful and transitive,
so [G:G_V]=5 and [G_V:H5]=2. The order-two stabilizer acts on the ordered
parameter by u↦1/u.

Pass to the finite-index ambient subgroup fixing V, then forget the
other four non-pole ordinary labels. The retained configuration has U,V
and the unordered branch pair. Its mapping-class group is Q4≅C2*Z.
On u=s², normalize the branches to0,infinity and U to1. Then

    x0(s)=((s+1)/(s-1))²

is V's coordinate. Interchanging the branch pair sends x0 to1/x0. Hence
the quotient coordinate of the target four-point orbifold is

    w=x0+2+x0^(-1)=4*((u+1)/(u-1))².

This w is a degree-two quotient for u↦1/u. The source orbifold for G_V
is P1_w with a cone point of order2 at0 and four punctures

    4, infinity, a=-4-(8/5)*sqrt(5), b=-4+(8/5)*sqrt(5).

The last two are the values of w at the pairs
{zeta,zeta^(-1)} and {zeta²,zeta^(-2)}. Equivalently they are the two
roots of 5*w²+40*w+16. Thus G_V≅C2*F3.

For reference the degree-five cover G_V→G is the exact rational map

    q = 4*w*(w²+40*w+80)²/(w-4)^5,
    q-4 = 16*(5*w²+40*w+16)²/(w-4)^5.

It has one cone point of order2 at w=0 above q=0, two further ordinary
ramification points of index2 above q=0, three cusps of indices1,2,2
above q=4, and one cusp of index5 above q=infinity. These types agree
with the degree-five D5 action on the ordinary labels.

The four-point forgetting map on G_V is precisely the orbifold filling
of a and b:

    C2*F3 → C2*Z.

It is surjective and has the two added cusp meridians in its kernel.
That kernel is the normal closure of these two free generators in the
orbifold fundamental-group presentation. In particular this forgetting
map is not a retraction onto the embedded G_V, even after this natural
finite-index ambient passage.

On the actual pure source H5=π1(P1_u\{0,infinity,mu5}) the kernel has an
even simpler exact form. The map factors as

    P1_u\{0,infinity,mu5} → P1_u\{0,infinity,1}
      → (P1_w\{4,infinity}; cone2 at0).

The first map fills the four punctures mu5\{1}; the second is the
unramified orbifold double cover w=4((u+1)/(u-1))². Hence the discrete
kernel is exactly the normal closure of the four corresponding source
meridians. The target image is an index-two free rank-two subgroup.
The completed kernel is exactly the closure of that normal subgroup
inside H5-hat: profinite completion is right exact for the specified
quotient, and the last subgroup has full topology since it is finite
index in Q4. No general image-topology assumption is being inserted.
This kernel is nontrivial, and its discrete and completed versions have
infinite index. If an abstract type is needed, the discrete kernel is
free of countably infinite rank, and the exact finite-word theorem used
in B70 applies to the completed kernel. Those types are not needed to
exclude the retraction.

At the actual common icosahedral basepoint, B61's cyclic parameter is
u_*=-phi², where phi=(1+sqrt(5))/2. Direct substitution gives

    q(u_*)=-121,       w(u_*)=4/5.

This specifies the common marking point for the reduced orbifold diagram.
Based meridians are obtained from that point by the same source paths;
no arbitrary ambient conjugator is substituted.

The obstruction is scoped: another homomorphism from a suitable finite-
index ambient subgroup could still be a retraction. The two particular
extra cusps show why the immediate coordinate forgetting cannot supply
it. The main profinite intersection remains Open.
