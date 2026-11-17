# The actual symmetric deletion and its fixed-lifting gate

Research note, 16th hour. The geometry and the elementary quotient comparison
below are proved. The two global fixed-source/fixed-lifting assertions are
NOT proved. No full marginal equality or original centralizer K is asserted.

## 1. Actual surfaces, basepoint, and involution

Write U=mu5 minus {1}. Let

X=Y_b={(v,w):v,w are nonzero and unequal to1, v!=w, vw notin mu5}.

Let A be the union of the eight divisors v=u and w=u, u in U. Then the
original ordered surface is Y=X minus A. Its source is the actual line
v+w=2, with its nineteen excluded affine points. The filled source S0
has eleven excluded affine points. All groups use the literal basepoint
(v*,w*)=(399/200,1/200); old q=vw has value399/40000. The previous q=.01
marking is connected to this one by the specified short positive real
source interval. The involution

F(v,w)=(v(w-1)/(1-v), w(v-1)/(1-w))

preserves X, fixes this basepoint, has square1, and preserves q=vw.
On the q fiber it is F_q(v)=(v-q)/(v-1). Its fixed locus in X is exactly
S0: v+w=2. The original and filled q maps are genuine bundles over
B=C* minus mu5, with fourteen- and six-punctured sphere fibers,
respectively. In particular no special-fiber assertion is needed here.

A independently proved the filled comparison, discretely and for actual
full completions, in work_A/B87_filled_fixed_subgroup.tex. Its fiber
orbifold is C2*C2*F2; the selected cone class measures the actual
index-two source cover S0->B. We use that proof only for X. It does not
identify fixed subgroups after the new symmetric critical fibers are
filled.

Put Bdiv=F(A), Z=X minus (A union Bdiv), and S=S0 minus A. Since F fixes
S0 pointwise, S0 meets A and Bdiv in the same set; thus this S is exactly
the original source, unchanged by symmetrization. F preserves Z and is
an actual based involution there.

## 2. Two useful exact coordinate models

Put r=w(v-1)/(1-w). Then F literally swaps w and r, and
q=w+r-wr. The actual X in these coordinates is

w*r !=0, w+r !=0, q notin {0} union mu5.

The conditions w!=1 and r!=1 follow from q!=1. The coarse quotient has
coordinates s=w+r, p=wr and is the affine line-arrangement complement

p!=0, s!=0, s-p notin {0} union mu5.

The retained branch curve is s^2-4p=0. This is an orbifold description,
not an assertion that the ordinary quotient complement is aspherical.

Alternatively x=(v+1)/(v-1), y=(w+1)/(w-1). In projective coordinates,
F is represented by

[[1,-1,2],[-1,1,2],[1,1,0]], whose square is4I.

The fixed source line is x+y=2z. The other projective fixed point is
[-1:-1:1], which is the removed point v=w=0. The retained boundary is
the seven lines x=±z, y=±z, x=±y, z=0 together with the four invariant
conics

(x+z)(y+z)-u(x-z)(y-z)=0, u in U.

The eight A divisors and their eight F-translates are projective lines.
The exact matrix and conic identities are checked by the accompanying
program. The local arithmetic chart is a DIFFERENT q coordinate:
eta=(vw-1)/(w-1)^2, t=w-1. Direct substitution gives
F(eta,t)=(eta^-1,-eta*t). Its source is eta=-1. No global arithmetic
path comparison is inferred from this local identity.

## 3. All mixed intersections, including the actual boundary check

Each component of A is a q-section isomorphic to B. Distinct components
of A are disjoint in X: a constant/moving intersection has q in mu5;
components of the same type cannot meet in X. The same holds for Bdiv.
For u,t in U, the mixed intersections with A_v(u) are

A_v(u) and F(A_v(t)): v=u, w=(u+t-ut)/u, q=u+t-ut;
A_v(u) and F(A_w(t)): v=u, w=t/(u+t-1), q=ut/(u+t-1).

The other cases follow by exchanging v and w. The denominators do not
vanish. For unit u=e^(ia),t=e^(ib),

|u+t-1|^2-1=8 sin(a/2) sin(b/2) cos((a-b)/2).

It can vanish only if u=1, t=1, or u=-t, all impossible here. Also
u+t=1 would force u/t to have order3, impossible for fifth roots. The
two displayed q values therefore avoid0 and the entire unit circle;
the other retained exclusions likewise cannot occur. Equality v=w
would force u=-t. The transverse Jacobian is respectively u or
u+t-1, hence nonzero.

Consequently all64 A/Bdiv pairs meet once, transversely, inside X.
The points are all distinct because each family is internally disjoint.
Exactly eight are fixed by F: the matching component pairs. They are
the original source holes (v,w)=(u,2-u) or (2-u,u). The remaining56
points form28 free F-orbits.

The exact Q(zeta5) program checks all these assertions without numerical
root decisions. It finds18 distinct new q values, with collision-cluster
sizes eight2's, eight4's and two8's. Away from these values, Z has a
22-punctured sphere fiber, and the quotient fiber orbifold is
C2*C2*F10. All new collisions are the mixed transverse nodes just
listed; no A/A or Bdiv/Bdiv collision is hidden.

Files: check_symmetric_deletion_geometry.py/.out/.err and
symmetric_deletion_geometry.json. The initial run passed the assertions
but hit SymPy-integer JSON serialization; its genuine diagnostic is
preserved as check_symmetric_deletion_geometry_failed_json.err. The
corrected run converts the matrix entries to native integers.

## 4. The automatic group fiber-product surjection

Write GZ=pi1(Z), G=pi1(Y), G0=pi1(X), f:G->G0, and F0 for the actual
involution on G0. Let p:GZ->G fill Bdiv, and put p'=p composed with F.
Thus p' fills A and identifies the resulting complement with Y via F.
Define NA=ker(p') and NB=ker(p). Both are the actual normal closures of
their indicated meridians. Filling both sets gives

G0=GZ/(NA NB).

There is an ACTUAL SURJECTION

Psi=(p,p'):GZ -> E={(g,h) in G times G : f(h)=F0(f(g))}.

Its kernel is M=NA intersect NB. This is the standard elementary normal
subgroup identity, not a topological injectivity theorem. For normal
N1,N2 in any group, the map to the fiber product of the two quotient
groups over G/(N1N2) is onto: compatible representatives differ by a
product in N1N2, and changing by its two factors makes them equal.
The involution F on GZ corresponds to exchanging the two coordinates.

The exact same statement holds for actual full completions. Let
mathcalNA,mathcalNB be the closed normal meridian kernels in hatGZ.
Their product is compact and equals the closed kernel of hatGZ->hatG0.
The map to

mathcalE={(g,h) in hatG times hatG : hatf(h)=F0(hatf(g))}

is surjective, with kernel mathcalM=mathcalNA intersect mathcalNB.
The elementary quotient argument alone does NOT identify mathcalM with
the closure of M, or mathcalE with the full completion of the abstract E.
The additional actual comparison proved subsequently is recorded next.

## 4a. The actual mutual-commutator and completion comparison

A subsequently proved the stronger actual comparison in
work_A/symmetric_intersection_commutator_16h.md, proposed B89. This
proof was independently read and passed here, including the primary
Brown--Loday Lemma4.1 and the elementary full-topology argument.

The union Y union F(Y) is X minus the64 mixed points. Its pi2 vanishes
because X is aspherical and removing finitely many points from a real
four-manifold preserves pi2. Both partial complements are aspherical
free13-by-free6 bundles. Brown--Loday's weaker homotopy-fiber hypothesis
therefore applies without assuming Z aspherical and gives

NA intersect NB=[NA,NB].

Every finite-kernel extension of the actual filled group Q=F5 semidirect
F6 virtually splits: for a central finite kernel, lift the free fiber
and base and kill all discrepancy characters on the characteristic
subgroup [F5,F5]F5^e; for a noncentral kernel, pass to its centralizer.
This implies that every actual fiber product over Q has its full
profinite topology induced by the product. Density then identifies the
completion of E with mathcalE. Hence, in this actual example,

mathcalNA intersect mathcalNB
 = closed[mathcalNA,mathcalNB]
 = closure(NA intersect NB).

This is a proved comparison, not a general interchange of closure and
intersection. The remaining cocycle below now has its values in the
actual closed mutual commutator. Its neutrality is still unproved.

## 5. The precise fixed-element obstruction

Let R=ker(f). For r in R, the diagonal (r,r) belongs to E and is fixed
by coordinate exchange. Choose any lift x in GZ. Then

t=x^-1 F(x) lies in M and t F(t)=1.

Replacing x by xm changes t to m^-1 t F(m). Therefore a fixed lift
exists exactly when this cocycle represents the neutral element of
nonabelian H^1(C2,M), equivalently t=m F(m)^-1 for some m in M.
This is a pointed-set obstruction, not a homomorphism to an abelian
module. The same proof holds continuously with mathcalM and actual
compact groups. It does not require any completion/intersection swap.

The original source image in GZ is fixed pointwise, so its image in E
is diagonal. A source word in the kernel S->S0 gives a fixed lift of
its image in R. Conversely, if the fixed subgroup of GZ is the actual
source image, then the filled source injection established in B87
forces every fixed lift above diagonal R to arise from that source
kernel. Under this additional fixed-source assertion, surjectivity of
fixed lifting onto diagonal R is precisely the desired marginal
source-kernel equality I=R. The analogous compact implication uses
B87's actual embedded compact source and its actual kernel.

Thus two gates are explicit:
(1) identify the relevant fixed elements of GZ after all eighteen new
critical fibers are filled with actual source elements;
(2) make the above cocycle neutral for every diagonal element of R.
Neither is supplied by the automatic fiber-product surjection.

## 5a. The weaker projected fixed-subgroup gate

B87 gives an exact useful consequence before any new lifting theorem.
Let H be the actual image of pi1(S) in G, and Hb the embedded filled
source pi1(S0) in G0. Since the free filling pi1(S)->pi1(S0) is onto
and the latter group embeds in G0,

I=H intersect R, and f(H)=Hb.

The same statements hold for the actual compact source images: the
source free retraction has its actual compact kernel, and B87 embeds
the completed filled source. Consequently

I=R if and only if H=f^-1(Hb),

and the corresponding equality holds as an equivalence for actual
compact groups. Indeed, if R is contained in H, lift the Hb image of
any element of f^-1(Hb) by H and divide; conversely the full preimage
contains R.

In the convention of Section4, E^swap is the diagonal copy of
f^-1(G0^F0)=f^-1(Hb). If the second coordinate is left in pi1(F(Y))
instead of identified with G via F, the same copy is (g,Fg).
Thus full equality GZ^F=the source image is stronger than necessary.
The sufficient projected gate is only

p(GZ^F)=H,

together with surjectivity of fixed lifting onto E^swap (or just onto
diagonal R, since source lifts already cover Hb). Both formulations
have identical actual compact versions. No projected equality is
assumed here; this refinement records precisely the weaker claim that
would suffice for the original marginal equality.

## 6. What the local nodes prove, and what they do not

At a fixed mixed node choose coordinates alpha,beta=alpha composed with
F; F exchanges them and the fixed source is alpha=beta. Its positive
source meridian is the product a*b of the commuting local A and Bdiv
meridians. It is a fixed lift of the A meridian after Bdiv is filled.
This proves fixed lifting for the eight source-whiskered peripheral
words, and their source conjugates. It does not permit arbitrary
ambient conjugators. The fifty-six off-fixed mixed nodes occur in
F-pairs and add actual transported commutator relations; their uniform
impact on the cocycle classes remains to be proved.

There is already a sharp warning at a generic q fiber. Its orbifold
fiber is C2*C2*F10, whose selected involution has only its order-two
centralizer. Therefore the fixed subgroup of the generic punctured
sphere fiber is trivial, whereas the fixed fiber-product target
contains diagonal copies of the nontrivial fiber deletion kernel.
The critical fillings at source holes are essential, not an optional
technical detail.

## 7. Why ordinary product theorems do not settle the gate

The complete primary Oka--Sakamoto paper was opened and read:
Oka, M., & Sakamoto, K. (1978). Product theorem of the fundamental group
of a reducible curve. Journal of the Mathematical Society of Japan,
30(4),599--602. https://doi.org/10.2969/jmsj/03040599
Primary PDF: https://www.jstage.jst.go.jp/article/jmath1948/30/4/30_4_599/_pdf

Its theorem is about two curves in the affine plane with the full
number of distinct degree-product intersections. Its deformation proof
does not preserve an additional retained divisor. No relative
fiber-product injectivity claim is extracted from it.

Root's exact countermodel, independently reviewed here, is recorded in
records/relative_product_countermodel_16h.md and its executed checker.
For retained xy=1 and deleted axes, all mixed intersections are maximal
and avoid the retained curve, but Z times F2 maps to the relative
fiber product Z^3 with nontrivial commutator kernel. Nevertheless swap
has fixed lifts z^m a^(2m)c^l for every fixed target (m,m,l). This is
why fixed lifting, rather than comparison injectivity, is the target.

A further symmetrization of the already proved B76 counterexample is
being recorded separately. It rules out a broad inference from a
linear reflection and maximal mixed intersections alone. It is not a
counterexample to the actual mu5 arrangement and does not replace the
two actual gates above.

## 8. The first actual relative obstruction has now been removed

Subsequent checked research is in
work_A/symmetric_first_fixed_lift_module_16h.md; the independent full
review is review_first_fixed_module_16h.md. Put K=ker(GZ->G0) and
M=NA intersect NB. Its first relative coinvariant module is

C=M/[M,K].

The actual universal-X cover and Mayer--Vietoris identify C with the
free abelian module on disjoint lifted A/B component pairs; F acts by
minus-swap. Attached F21/F22, transported through the actual source and
ambient cover comparison B78.3, says that the discrete source kernel
normally generates R internally. Its H1 therefore surjects onto the
free meridian module of A lifts. The selected filled-source lift is
simply connected by B87, so its puncture meridians account for every
A lift. Every A lift consequently meets that fixed source lift and
therefore its own F-mate. There are no singleton orbits in the
signed-pair basis. Explicitly on each two-element orbit e,e', a cocycle
a(e+e') equals m-F(m) with m=a e. Thus H^1(C2,C)=0 discretely.

It follows that every discrete fixed target in E lifts fixed in
GZ/[M,K]. The completed fixed-target assertion also holds, by a
separate compact-density argument using B87 and B89. This does not
identify an arbitrary completed coefficient module with a permutation
module or assert its H^1 vanishes. The compact fixed-image is closed
and contains all dense discrete fixed targets, which suffices.

This removes the first relative commutator obstruction. It neither
lifts fixed elements in GZ itself nor identifies their projection with
the actual source image. In particular the two original nonlinear
and source-membership gates have not been closed.
