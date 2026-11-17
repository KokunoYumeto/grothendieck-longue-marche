# The completed boundary/neck intersection via an actual quotient retraction

Root late checkpoint24 addendum, 17 November 2026. Formal register remains
unchanged. This note uses the completely reviewed boundary-subgroup
embedding/full-topology proof in pentagon_hnn_boundary_proof_candidate24.md.
It does not use a closure/intersection exchange. Independent read-only
review was requested from A before capture; the response is recorded in
the final addendum review record.

## Statement and actual maps

Let R be the actual B112 regional group, before the two B114 cross
relations, with K=F(a,B,d,e,f), B=CbC, f=C z k^-1. Let c=aCa^-1 be
the actual selected cone, P=P5=aBfde the actual full ordinary prefix,
and T=cP=a b z d e k^-1. Put H=<c,k,T> in R.

The previously reviewed proof identifies H with C2(c)*Z^2(k,T) and
proves full induced profinite topology in R, through the actual quotient

q:R -> R_e=<C,k,z,e | C^2,[C,z],[k,z],[k,e],[e,CeC]>,

which kills a,b,d. In this quotient q(c)=C, q(T)=z e k^-1, and
q(P)=f e, where f=C z k^-1 denotes the retained actual word. Write
s=z e and H_e=<C,k,s> in R_e. The restriction q:H -> H_e is an
isomorphism, with the invertible change s=q(T)k in the abelian factor.
The reviewed argument also proves that H_e has full induced profinite
topology in R_e. Consequently the induced map

qhat restricted to Hhat: Hhat -> R_ehat

is injective, and its image is the embedded full completion H_ehat.
K has its full induced topology in R by B114/B117; all hats here mean
full profinite completions and their explicitly identified compact images.

We prove

K intersect H = <P> in R,
Khat intersect Hhat = closure(<P>) in Rhat.

The second equality is not inferred from the first.

## A genuine retraction in the one-family quotient

Let F=F(x,y) be an abstract free group of rank two. Define a homomorphism
tau:R_e -> F by

C -> 1, k -> 1, z -> x, e -> y.

Every defining relator is respected: the first four are immediate and
[e,CeC] maps to [y,y]=1. Define a homomorphism sigma:F -> R_e by

x -> f=C z k^-1, y -> e.

This exists because F is free. We have tau composed with sigma equal
to the identity on both x and y. Thus sigma is injective and
K_e=<f,e> is free of rank two. The endomorphism

rho=sigma composed with tau:R_e -> K_e <= R_e

is a retraction. In literal regional generators it sends C,k to 1,
z to the actual word f, and e to e. It fixes f and e exactly.
Therefore K_e has full induced profinite topology in R_e and rhohat
fixes its embedded full completion pointwise.

Put p=f e. Since rho(C)=rho(k)=1 and rho(s)=rho(z e)=f e, we have

rho(H_e)=<p>.

The cyclic subgroup <p> has full induced topology in K_e: (p,e) is
a free basis, so killing e gives a retraction onto <p>. It therefore
also has full induced topology in R_e. In particular its compact
closure is its full procyclic completion.

## Both intersections in R_e

If u belongs to K_e intersect H_e, then u=rho(u) belongs to <p>.
Conversely p=C s k^-1 belongs to H_e and p=f e belongs to K_e, so

K_e intersect H_e=<p>.

For a profinite element u in K_ehat intersect H_ehat, continuity gives
u=rhohat(u) in rhohat(H_ehat). The latter image is exactly closure(<p>):
the image of the compact group H_ehat is closed, and the image of its
dense subgroup H_e is <p>. Conversely closure(<p>) belongs to both
compact subgroups. Hence

K_ehat intersect H_ehat=closure(<p>) inside R_ehat.

This is a direct completed retraction argument. It neither exchanges
completion with intersection nor assumes separability of a product.

## Transfer back to the actual unfilled regional group

The quotient q sends the actual K onto K_e: a,B,d die, e is retained,
and f maps to the same literal f. Thus qhat sends Khat onto K_ehat;
equivalently, continuous image and density identify its compact image
with the closure of q(K)=K_e. It sends Hhat injectively onto H_ehat,
as established above.

Let v belong to Khat intersect Hhat. Then qhat(v) belongs to
K_ehat intersect H_ehat=closure(<p>). Because P belongs to H and
q(P)=p, the compact image qhat(closure(<P>)) is closure(<p>). Thus
there is w in closure(<P>) with qhat(w)=qhat(v). Both v,w belong to
Hhat and qhat is injective there, so v=w. The reverse containment
follows from P belonging to K and H. This proves the asserted full
completed equality. The discrete equality follows by the identical
retraction argument with ordinary elements, or by the earlier complete
Britton proof.

## Scope

This closes the boundary/neck intersection gate in the actual regional
group, in both the discrete and full profinite categories. The group is
still the regional group before B114's two added cross relations. Properness
of a proposed full profinite amalgam involving the isolated corner, and
the effect of all remaining marked mirror/regional relations on the actual
annular centralizer, remain unproved. Neither main decision follows.
