# Harmonic attack, 2026-11-15 11:55 UTC

The unique conjugator computation in E22 reduces the same-parameter nonseparating clutching comparison to the full profinite B3 equation (E51), not just its central quotient. A discrepancy central in B3 is detected by exponent sum, since the central generator has sum six.

## Normalization of c2

Let H=ker(Fhat(x,y)->C2), with Schreier basis (x²,y,xyx^-1). The homomorphism c2 on H is the y-coordinate after killing the last generator. On Fhat' it vanishes on Fhat'', takes [x,y]=xyx^-1y^-1 to -1, changes sign under conjugation by x, and is invariant under conjugation by y. Hence if f=A_F(xbar,ybar)*[x,y] in the metabelian commutator module, then c2(f)=-A_F(-1,1), with no unspecified sign. NS Proposition5.3 proves rho2=c2 already on IΓ′, the subgroup defined by III′, before IV is imposed.

## What Enriquez distribution proves as an exact map

Write Phi(x)=x^lambda, Phi(y)=f^-1 y^lambda f, lambda=2m+1. It preserves H. Let delta:H->Fhat(X,Y) send x²->X, y->Y, xyx^-1->1. Enriquez Theorem8.1 gives delta(f)=Y^c2 f(X,Y). Therefore delta Phi(x²)=X^lambda, delta Phi(y)=f(X,Y)^-1 Y^lambda f(X,Y), and delta Phi(xyx^-1)=1: the last word is a conjugate of (xyx^-1)^lambda because lambda is odd. Thus delta∘Phi|H=Phi∘delta genuinely in these normalizations. This is a precise covering/filling compatibility, proved for every GT element.

## Why the filling comparison alone does not determine the four-puncture action

Put H4=Fhat(a,b,c), d=(abc)^-1, p=ab. The automorphism T sends a->pap^-1,b->pbp^-1,c->c. Its inverse replaces conjugation by p with conjugation by p^-1, since T(p)=p. It preserves all four peripheral conjugacy classes. Filling a or b makes T the identity. Filling c makes it Inn(p) on Fhat(a,b). Filling d gives c=p^-1, so it again becomes Inn(p). Yet T is not inner: an inner representative would centralize both c and p, whose maximal procyclic centralizers have trivial intersection, and then would be identity, whereas T(a)≠a. Thus the product of all four peripheral filling maps on outer automorphisms has a nontrivial kernel. This does not prove that the GT relations fail to imply E51; it invalidates deriving the result merely from equality of the four filled outer actions.

## Geometric formulation

The harmonic four-punctured sphere {0,1,-1,infinity} has commuting involutions z->-z and z->1/z. They descend to the S3 symmetries of the quotient tripod, so the restricted GT action can be compared with each of these. The Möbius involution z->(1-z)/(1+z) interchanges these two degree-two quotient structures. Its compatibility is the new comparison required in E22. A conjugacy after each filling does not provide this extra compatibility, as T above demonstrates.

## Status

No all-GT derivation of E51, and no genuine GT counterexample, has been obtained. Enriquez's full profinite GTK=GT theorem and all four supporting lemmas were opened and read. The fixed-elliptic-curve section A_F still leaves the exact modular normalizer membership A_F^-1 T_- A_F in image(B3hat) unverified outside the arithmetic subgroup.
