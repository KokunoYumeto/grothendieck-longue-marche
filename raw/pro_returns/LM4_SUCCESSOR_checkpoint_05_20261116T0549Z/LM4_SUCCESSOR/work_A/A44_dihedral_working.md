# A.44 working proof: the first mixed finite-base obstruction is absent

**Status:** independently reviewed by the parent and incorporated as formal A.44, 2026-11-16. The formal source is authoritative. This result concerns every full peripheral negative involution, not only GT involutions.

Let alpha=(-1,f) be a nonidentity involution of P. Let u in F' be its canonical R1 parameter, u=f*alpha(u). Put y'=u^(-1)y*u, so alpha(y')=(y')^(-1). In E=F semidirect <c>, where c acts by alpha, put

    C=c, X=x*c, Y=y'*c.

These are representatives of the three full F-conjugacy classes of involutions. Their mod-two abelian labels are 0,x,y, so they are distinct. The x cusp has endpoints C,X, and the y cusp, conjugated by u^(-1), has endpoints C,Y. C.28's three-cusp incidence cycle therefore says that the third cusp has endpoints X,Y. Every section centralizer in F is trivial.

## 1. Dihedral notation and the induced action

For an odd prime p let q:F -> D_(2p) be the quotient with

    q(x)=a, q(y)=a*t, a^2=t^p=1, a*t*a=t^(-1).

Thus t=q(xy), and write q(f)=t^l, q(u)=t^k. The map q*alpha sends x to a and y to a*t^(2l+1). Since alpha is an automorphism, this map is onto. Its kernel is the same as that of q, because every generating pair of reflections of D_(2p) is obtained from the named pair by an automorphism fixing a. Thus alpha induces an automorphism on this actual quotient, fixing a and sending t to t^(2l+1). Its square is one, so 2l+1 is either 1 or -1 modulo p.

The canonical substitution x -> x, y -> y' fails to generate D_(2p) precisely when

    q(y')=a*t^(2k+1)=a,

or equivalently 2k+1=0 modulo p. We show that this is impossible.

## 2. The nontrivial quotient action is impossible

If alpha sends t to t^(-1), then l=-1. The coboundary equation u=f*alpha(u) gives 2k=l=-1, so the forbidden collapse occurs automatically. The induced action is conjugation by a. Identify

    D_(2p) semidirect_(Int a) <c>  =  D_(2p) x C2

by g*c^epsilon -> (g*a^epsilon,epsilon). The images of both X=x*c and Y=y'*c are then the same central involution (1,1). Every conjugate of either full section class has this same central image. But the third cusp's two local reflections belong to those two classes, so their product would have trivial image. Their product is a conjugate of z or z^(-1), whose image has order p. This is a contradiction.

Hence alpha acts identically on D_(2p), and q(f)=1.

## 3. The degree-p cover is pure negative

Assume now the forbidden collapse 2k+1=0, and put U=q^(-1)(<a>). This is alpha-stable because alpha acts identically on the quotient.

The cosets U\F are indexed by j in F_p through U*t^j. Right multiplication by x sends j to -j, right multiplication by y sends j to 1-j, and right multiplication by z sends j to j-1. Thus above x there is one width-one cusp and (p-1)/2 width-two cusps; the same is true above y; and above z there is one width-p cusp. There are p+2 cusps in total. The index-p pants cover has Euler characteristic -p, so its genus is zero and U is the full profinite sphere group of rank p+1.

The induced alpha preserves every x and y cusp class individually: its quotient action is identity and their normalized finite frames are q(1)=q(f)=1. The z cusp is unique, so it is preserved regardless of its finite frame. Every cusp meridian is inverted up to U-conjugacy. Thus alpha restricted to U is a pure negative involution, and C.28 applies to its p+2 cusps.

For p=3 one may use the explicit five representatives

    x, y*x^2*y^(-1), u^(-1)*y*u, y^2, z^3.

The third is U-conjugate to the discrete width-one representative y*x*y*x^(-1)*y^(-1). The corresponding real reflecting sections are respectively c, y*c*y^(-1), c, u*c*u^(-1), and a local z-reflection adjusted by an even power of z to have quotient a. Each lies in U semidirect <c>. For the width-two x cusp the alpha-frame is y*alpha(y)^(-1), and for the width-two y cusp it is f; both have trivial finite quotient. The width-one x/y' frames are 1. The adjusted z-reflection is v_z*c with q(v_z)=a, giving a U-frame for the unique z^3 cusp. This lists all five actual frames without assuming the z-frame is trivial.

## 4. The section incidence graph cannot be connected

The full C-class splits into precisely p U-classes, indexed by U\F: write C_j for the class of g*c*g^(-1) with Ug=U*t^j. All these conjugates lie in U semidirect <c>, because c is central in the finite semidirect quotient. Their U-conjugacy classes are distinct because C_F(c)=1.

Each of the full X and Y classes contributes exactly one U-class. Their finite image is a*c, so a conjugate belongs to U semidirect <c> exactly when its conjugator has image in C_D(a)=<a>. Such a conjugator lies in U. There are therefore precisely p+2 section classes, namely C_j together with X and Y, as also required by C.28.

The width-one x cusp joins C_0 to X. The width-one y cusp can be represented by y'=u^(-1)y*u and joins C_0 to Y. The unique z cusp has odd width p, so its two endpoints remain in the opposite full classes X,Y; it joins their unique U-classes. Concretely an even power of z adjusts either base z-reflection into U semidirect <c>, because q(z) has odd order p, and its product with z^p gives the other endpoint. These three edges form a triangle.

For every nonzero pair {j,-j}, the width-two x cusp joins C_j to C_(-j). The reason is the exact local identity x^2*c=x*c*x^(-1): the two reflections above the orbit Ug,Ug*x are g*c*g^(-1) and (g*x)*c*(g*x)^(-1).

For y use its actual real reflection r_y=u*c*u^(-1), which inverts y. The two endpoints of a width-two y cusp with representative g are the C-classes indexed by Ug*u and Ug*y*u. If Ug=U*t^j, these indices are j+k and 1-j+k. Under the forbidden equality 2k+1=0, they are negatives of each other. The unique fixed y-cusp gives j=1/2 and j+k=0, as already used above. Thus the width-two y edges give exactly the same nonzero pairs as the x edges.

The incidence graph is consequently the triangle C_0-X-Y plus (p-1)/2 separate digons C_j-C_(-j). It is disconnected. This contradicts C.28, which says that the pure negative involution on this genus-zero (p+2)-cusp group has one incidence cycle using all its cusps and all its section vertices.

The forbidden collapse is impossible. The canonical substitution is therefore onto every D_(2p) reflection quotient. It is onto every finite dihedral reflection quotient as well: failure to generate a rotation subgroup for odd composite order is detected modulo an odd prime; the two-primary factor of 2k+1 is automatically a unit.

## 5. Consequence for the relative pro-p quotient over the parity character

Let V=ker(F -> C2), where both x and y have image -1. Its Schreier basis is

    A=x^2, B=y*x^(-1), C=x*y.

On V^ab, conjugation by x sends A to A, B to C-A, C to A+B. For odd p, the invariant subspace is spanned by A and B+C (the latter is y^2), and the sign subspace is spanned by A+B-C. These three vectors form a basis over F_p, with determinant -2.

The canonical substitution preserves V and O^p(V), so induces an endomorphism of G_p=F/O^p(V). Let H be the closed subgroup generated there by x and y'. Its intersection with the free pro-p kernel V^(p) contains x^2 and (y')^2, whose Frattini images are the two invariant basis vectors. The quotient killing that invariant plane is precisely a D_(2p) reflection quotient: the original x,y are reflections whose product has nonzero sign coordinate. The dihedral result says that H surjects onto it. Thus H intersect V^(p) also surjects onto the sign coordinate, and hence onto the entire Frattini quotient. Frattini gives H intersect V^(p)=V^(p), and H=G_p. The induced endomorphism is therefore an automorphism.

At p=2, the relative group G_2 is the maximal pro-2 quotient F^(2), since it is an extension of a pro-2 kernel by C2. The already supplied R1 pro-p generator assertion gives the same conclusion there. For every prime, the same full identity u=f*alpha(u) shows that this automorphism intertwines the induced alpha and c actions.

This is a generation and unmarked automorphism-conjugacy assertion at the stated relative level. It does not assert that the multiplier-one canonical substitution preserves the third cusp, nor that an arbitrary other relative level has this property.
