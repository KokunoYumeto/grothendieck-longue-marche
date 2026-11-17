# Uniform direct two-dimensional linear boundary for the actual sphere pentagon

Conversation-only complete proof authored by A and independently fully read by root and CE. All cases and the inverse presentation were checked. No target search, census, execution, saved source hash, or formal promotion is claimed.

THEOREM. For every finite field k, every homomorphism from the full completion of the ACTUAL G=P4/<Delta4²> into GL2(k), and every u in Fhat(x,y)' satisfying u(y,x)=u(x,y)^(-1), the original marked equation
u(a,ce) u(bc,f)=u(c,f) u(ab,ef) u(a,c)
holds. Thus every DIRECT GL2(k) evaluation of this pentagon is already a consequence of the commutator and duality conditions.

## 1. Reversible original presentation

Use generators a,c,d,f,P with the six relations
[a,f]=[c,d]=[P,a]=[P,c]=[P a f^(-1),d]=[c d^(-1)P,f]=1.
Retain exact inverse words
A=a f^(-1), C=c d^(-1),
b=a^(-1)P^(-1)c^(-1), e=d^(-1)P f^(-1).

This is precisely the original A.96 presentation. The first two relations give F(A)=A and D(C)=C. The next two give F(P)=A^(-1)PA and D(P)=C^(-1)PC. The relation [PA,d]=1 then gives D(A)=C^(-1)P^(-1)CPA. The relation [CP,f]=1 gives F(C)=CPA^(-1)P^(-1)A. Conversely the original six action rows give these six commutations. All based sphere relations and original inverse words are retained.

## 2. Elementary facts

For u in Fhat', multiplying either evaluated input by an element CENTRAL IN THE WHOLE subgroup involved does not change u. This follows for finite words from zero exponent sums and then for arbitrary profinite u by continuity in finite targets. In particular commuting inputs give value 1. Evaluations also split componentwise when the two relevant subgroups commute with each other.

For a nonscalar 2-by-2 matrix P over any field k, its commutant algebra is k[P]. Choose v with v,Pv independent; a commuting map is determined by its value a v+b Pv and hence equals aI+bP. Therefore
T=C_GL2(k)(P)=k[P]^times
is abelian. If Q in T is nonscalar, write Q=aI+bP with b!=0. Then k[Q]=k[P] and C_GL2(k)(Q)=T. No enumeration or field-size restriction is used.

## 3. Scalar P

If P is scalar, the original action rows show that <A,C> commutes with <d,f>; neither subgroup is assumed abelian internally. In the displayed pentagon order the five evaluations are
u(a,ce)=u(A,C),
u(bc,f)=1,
u(c,f)=u(d,f),
u(ab,ef)=1,
u(a,c)=u(A,C)u(f,d).
Thus the right side is u(d,f)u(A,C)u(f,d)=u(A,C), by subgroup commutation and duality. The left side has the same value.

## 4. Nonscalar P

Put T=C(P). The original relations place a,c in T.

Case 1: both a and c nonscalar. The relations [a,f]=[c,d]=1 give f,d in T. Every original generator lies in the abelian T, so every u-value is 1.

Case 2: a nonscalar and c scalar. First f lies in T. From [c d^(-1)P,f]=1 and [P,f]=1 follows [d,f]=1. If f is nonscalar then d lies in C(f)=T, so the image is abelian. If f is scalar, the remaining relation [P a f^(-1),d]=1 becomes [Pa,d]=1. If Pa is nonscalar, d lies in T and again the image is abelian. The sole remaining case has f scalar and Pa scalar, so a is a scalar multiple of P^(-1); c and b are scalar. By central decoration, the ordered list of five u-values is
(U,1,1,U,1), U=u(P^(-1),d^(-1)P).
The two sides are literally equal without any condition on U.

Case 3: a scalar and c nonscalar. Now d lies in T. The relation [P a f^(-1),d]=1 and [P,d]=1 give [f,d]=1. If d is nonscalar, f lies in T and the image is abelian. If d is scalar, the last relation becomes [cP,f]=1. If cP is nonscalar, f lies in T. The sole remaining case has d scalar and cP scalar, so c is a scalar multiple of P^(-1); a and b are scalar. The five values are
(1,V,V,1,1), V=u(P^(-1),f).
Again they give literal equality.

Case 4: a and c scalar. The two remaining relations are
[P f^(-1),d]=1, [d^(-1)P,f]=1.
Put z=d^(-1)P. Then [z,f]=1. Since P=dz, the first relation says [d,z f^(-1)]=1. Thus h=z f^(-1) commutes with d,f,z, and hence with P and every original generator. It is central in the whole image. The five values are
(1,u(P^(-1),f),1,u(P^(-1),z),1).
Since z=h f, central decoration makes the two nontrivial-looking values identical. This exhausts the nonscalar-P cases and proves the theorem.

## Consequence and limitations

The proposed direct GL2(F3) target, despite containing the signed SL2(F3) and noncentral involutions J,JX, cannot extract an additional equation linking the actual canonical epsilon_u and d from this pentagon. The identity already holds for every profinite commutator/duality word.

This is uniform over ALL direct GL2(F_q) homomorphisms of the actual group, not a conclusion from a target sample. It does not evaluate q3(H_d), exclude other GT0 relations, or cover affine semidirect targets, higher-dimensional representations, or the successful L² semidirect C2 wreath construction. In particular Aff2(F_q) is not GL2(F_q).

Independent full review: A author and recheck; CE complete all-field audit; root read all three source parts and independently derived every scalar/nonscalar case and the inverse original presentation.
