# Direct targets with abelian noncentral-element centralizers

This is the first filesystem materialization of the complete abstract extension proved and reviewed by root and A during the execution outage. It is newly saved text, not a recovered old file. No producer or census was run.

THEOREM. Let H be a finite group such that C_H(g) is abelian for every g outside Z(H). Every homomorphism from the actual completed sphere group G=P4/<Delta4²> to H makes the original marked pentagon of every profinite commutator word u with duality u(y,x)=u(x,y)^-1 an identity.

The actual presentation is on a,c,d,f,P with
[a,f]=[c,d]=[P,a]=[P,c]=[P a f^-1,d]=[c d^-1 P,f]=1,
and original b=a^-1 P^-1 c^-1, e=d^-1 P f^-1.
This is the reversible A96 presentation, with A=af^-1,C=cd^-1. No boundary quotient is imposed.

A central decoration in the whole subgroup being evaluated does not change a commutator-word value: both exponent sums vanish, first for ordinary words and then by continuity. If two subgroups commute elementwise, evaluation of a word on their products splits into the two subgroup evaluations.

First suppose P is central. The six relations imply that <A,C> commutes elementwise with <d,f>. In the original five-pair order the values are
u(A,C), 1, u(d,f), 1, u(A,C)u(f,d).
Their ordered pentagon is the identity by duality and the displayed subgroup commutation.

Now suppose P is noncentral, and put T=C_H(P), which is abelian. If Q is any noncentral element of T, then C_H(Q)=T. Indeed T is contained in C_H(Q); conversely P lies in the abelian C_H(Q), so every element of C_H(Q) commutes with P and belongs to T. The original relations put a,c in T.

Case1: a,c both noncentral. Their centralizers are T. The relations [a,f]=[c,d]=1 force f,d into T. All original images lie in T and every u-value is1.

Case2: a noncentral and c central. First f lies in T. From [c d^-1 P,f]=1 and [P,f]=1 obtain [d,f]=1. If f is noncentral then d lies in C_H(f)=T and the image is abelian. If f is central, the other relation becomes [Pa,d]=1. If Pa is noncentral, again d lies in T. In the only remaining case f and Pa are central. Then a is a central multiple of P^-1; c,b are central too. The five ordered values are (U,1,1,U,1), with U=u(P^-1,d^-1P), so the two sides are literally equal.

Case3: a central and c noncentral. First d lies in T. From [Paf^-1,d]=1 obtain [f,d]=1. If d is noncentral then f lies in T. If d is central, the last relation reduces to [cP,f]=1. If cP is noncentral then f lies in T again. In the remaining case d,cP are central, so c is a central multiple of P^-1 and a,b are central. The five values are (1,V,V,1,1), with V=u(P^-1,f), and the equation holds.

Case4: a,c both central. The remaining two relations are [Pf^-1,d]=1 and [d^-1P,f]=1. Put z=d^-1P, so [z,f]=1. Since P=dz, the first relation implies [d,zf^-1]=1. Thus h=zf^-1 commutes with d,f,z, hence with P and every original generator. It is central in the whole image, even if it need not be central in all H. The five values are (1,u(P^-1,f),1,u(P^-1,z),1). Since z=hf, their two nontrivial-looking values are equal by central decoration.

The cases are exhaustive. The proof uses only the stated centralizer property and the original marked presentation. It invokes no classification of finite groups. The earlier direct GL2(k) theorem follows because the centralizer of every nonscalar2x2 matrix is the abelian unit group of k[P], and the noncentral elements of GL2(k) are exactly its nonscalar matrices.

This is a boundary for those DIRECT targets. It does not apply to the successful affine2-dimensional target: a nonzero translation has a nonabelian centralizer containing the translation group and a unipotent stabilizer. It does not decide canonical realization, the full nonlinear hexagon, or either separately normalized CM character.
