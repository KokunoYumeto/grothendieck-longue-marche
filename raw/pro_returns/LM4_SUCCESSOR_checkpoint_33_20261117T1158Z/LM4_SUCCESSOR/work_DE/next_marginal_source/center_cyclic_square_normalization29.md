# An exact center-line retract and cyclic mixed-square normalization

Status: proposed complete research proof, cycle29. All cycle28 files and the frozen B138/B141 components are unchanged. This concerns the actual unfilled region and an explicitly specified cyclic part of the initial filling. It does not identify the complete filled kernel or assert that a regional subgroup survives both full fillings.

## 1. The actual center quotient has a free coset basis

Use B117/B141 and write V=f^{-1}Bf, h=fk. The actual color retraction R^0 -> L=<K,k> fixes the whole K and k. In the generators h,k,a,d,e,V, the exact presentation of L is

    L=<h,k,a,d,e,V | [h^2,k], [k,a], [k,d], [k,e], [k,V]>.

Indeed f=hk^{-1}, B=fVf^{-1}=hVh^{-1}, with the latter equality following from [k,V]. These substitutions are inverse to the actual B117 presentation. Put

    T_h=F(h,a,d,e,V),   Q_0=<h^2,a,d,e,V> <= T_h.

This is an auxiliary retained section, not an equality h=f. The original neck quotient identifies T_h with K by h->f and V->f^{-1}Bf. There is an exact isomorphism

    L = F(X_{gQ_0}:gQ_0 in T_h/Q_0) semidirect T_h,
    k=X_{Q_0},   t X_{gQ_0} t^{-1}=X_{tgQ_0}.

Both inverse maps are explicit: X_{gQ_0}->gkg^{-1}, with representative-independence because every element of Q_0 centralizes k; the reverse map sends k to the root basis letter and T_h to its permutation section. They respect all defining relations and are inverse on every generator. Thus the entire center kernel is free on these actual cosets. The color map N_reg->F(T_h/Q_0) is the actual deletion of all expanded family vertices from B141's graph, and is equivariant under the actual K action.

## 2. A long marked conjugator has zero correction

Set D=ded^{-1} and use the complete already-certified words

    w=a f V f^{-1} a^{-1} f D f^{-1}d^{-1},
    ell=afa^{-1},   eta(ell)=w f^{-1}w^{-1}.

Since both V and D commute with k, the actual equality is

    w=W:=a h V h^{-1}a^{-1}h D h^{-1}d^{-1} in T_h.

There is no suppressed center word here. The mixed-square convention of B141 is

    q=eta(ell)^{-1}=W f W^{-1}.

Put r=W h W^{-1} in the auxiliary section and define two center letters

    Y_0=X_{WQ_0},   Y_1=X_{WhQ_0}.

Then, literally in the displayed semidirect product,

    q=Y_1^{-1} r,    r(Y_0)=Y_1,    r(Y_1)=Y_0.

The last identities use h^2 in Q_0. These two correction centers are distinct because h is not in Q_0.

## 3. The whole pivot orbit is disjoint from the correction orbit

Let Z_n=X_{r^nQ_0} for every integer n. All these basis letters are distinct and none is Y_0 or Y_1.

Here is a complete all-exponent membership proof. The folded based core for Q_0 in the rose on h,a,d,e,V has two vertices joined by the two directed h edges of an h-cycle; a,d,e,V are loops only at the root. Completing its missing edges gives the Schreier cover, with trees attached to this finite core. The reduced word W begins a h V, so it leaves the core at the V step from the nonroot vertex, and W ends d^{-1}. For n!=0, W h^n W^{-1} is reduced at both displayed joins. Its initial W therefore leaves the core, and its reduced continuation cannot return from the attached tree. Thus r^n is not in Q_0. The same argument shows W h^s is not in Q_0 for every integer s, including s=0. Equality r^nQ_0=Wh^jQ_0, j=0 or1, would imply W h^{j-n} in Q_0. This is impossible. No finite-height calculation is being substituted for these statements.

Write q^n=nu_n r^n. For n>0, nu_n is the n-letter alternating word Y_1^{-1}Y_0^{-1}Y_1^{-1}...; for n<0 it is the (-n)-letter alternating word Y_0Y_1Y_0...; nu_0=1. Consequently

    u_n:=q^n k q^{-n}=nu_n Z_n nu_n^{-1}   (n in Z).

Every nu_n uses only the two complementary correction letters. Sending Z_n to nu_n Z_n nu_n^{-1} for every n, while fixing every other center basis letter, is an automorphism of the free center kernel. Its inverse conjugates by nu_n^{-1}, since the correction letters are fixed. Infinite rank presents no issue: each image is a finite word and both composites fix every free generator. Therefore F(u_n:n in Z) is an actual free factor of the center kernel, with precisely the indicated basis.

## 4. A genuine ordinary cyclic-preimage retract, with a necessary topology limit

Define pi on the center kernel by

    pi(Z_n)=u_n,    pi(X_z)=1 for z outside {r^nQ_0:n in Z}.

This is a retraction onto F(u_n). It is q-equivariant. Conjugation by q sends a center letter X_z to Y_1^{-1}X_{rz}Y_1. The pivot orbit and its complement are r-invariant, pi(Y_1)=1, and q u_n q^{-1}=u_{n+1}. These identities check equivariance on every basis letter.

Compose pi with the actual family-deletion retraction N_reg->center kernel. The composite is still q-equivariant because that deletion extends to the actual regional color retraction and fixes q in K. Hence it extends to an actual ordinary retraction

    r_reg^{-1}(<q>) = N_reg semidirect <q> -> <k,q>,

fixing both k and q. Its target is the already-established actual free pair. No extension over the rest of K has been proved or assumed.

In fact this specific retraction is NOT continuous for the topology on its domain induced from the full regional completion. Let g_m=h a^{m!}h^{-1}, m>=1. For every nonzero integer l and every integer n, r^{-n}h a^l h^{-1} is outside Q_0: at n=0 it leaves the core at the a step from the nonroot vertex; at n!=0 the reduced initial W leaves the core and cannot return. Thus every center X_{g_mQ_0}=g_m k g_m^{-1} is complementary and is killed by pi. But g_m tends to1 in the full profinite topology of T_h and of the region, so X_{g_mQ_0} tends to k. The image k is nontrivial in the regional completion, detected by the actual base-winding character. A continuous extension would send this convergent sequence both to1 and to k. This contradiction concerns the specified projection, not every possible continuous retraction. It also does not contradict the separately proved full induced topology of <k,q>.

## 5. The entire cyclic orbit of the mixed square has an exact normal form

Return to the actual common-kernel decomposition N=N_L*N_R and let alpha=Ad(q). The q action preserves both factors. In B141, gamma=cq with the actual c in N_R, and c_n=alpha^n(c). The left center line is exactly the free factor F(u_n) constructed above. The subgroup

    D=(F(u_n:n in Z)*N_R) semidirect <q>

is an actual ordinary subgroup and retract of (N_L*N_R) semidirect <q>: use pi on the left factor and the identity on the right factor. This statement precedes every filling.

The whole q^Z orbit of the actual mixed square is precisely

    u_n=(c_n u_{n+1} c_{n+1})u_{n+2}(c_n u_{n+1}c_{n+1})^{-1}
    for every n in Z.                                      (S_n)

The quotient of F(u_n)*N_R by the normal closure of all (S_n) is exactly

    N_R * F(u_0,u_1).

There is a direct inverse-presentation proof. Starting with the two free letters u_0,u_1, define all u_n for n>=2 recursively by

    u_{n+2}=c_{n+1}^{-1}u_{n+1}^{-1}c_n^{-1}u_n c_nu_{n+1}c_{n+1},

and all negative n recursively using the displayed formula (S_n). This constructs a map to N_R*F(u_0,u_1) killing every relation. The reverse map is the inclusion of N_R and u_0,u_1. Both composites are the identity by those two recursions, with no unproved stabilization or infinite-elimination limit.

The q action becomes the explicit automorphism beta given by

    beta|N_R=alpha,
    beta(u_0)=u_1,
    beta(u_1)=c_1^{-1}u_1^{-1}c_0^{-1}u_0c_0u_1c_1.

Its inverse restricts to alpha^{-1} on N_R and is

    beta^{-1}(u_1)=u_0,
    beta^{-1}(u_0)=(c_{-1}u_0c_0)u_1(c_{-1}u_0c_0)^{-1}.

Thus the square-only cyclic quotient is this explicitly described free-product-by-Z group. In particular its right kernel embeds. This is not a conclusion about adding the four leaf relations, other K translates, or the theta family.

## 6. An exact elimination in the COMPLETE presentation, without deleting either filling

The same construction can be used as a presentation change in the full actual initial quotient. In the B141 presentation of N_L, make the free-center basis change

    Z_n=nu_n^{-1}u_n nu_n,

leaving every other center and every family generator present. Rewrite every original graph relator by this substitution; this is a change of presentation, not an assertion that the changed basis still gives the same graph edges. In the full defining relation set retain ALL actual K translates of all five first-sheet words and all five theta words.

The subset (S_n) is among those complete relations. The explicit two-sided recursion above therefore eliminates the symbols u_n, n not0,1, from this complete presentation, substituting their actual words into EVERY other relation. It leaves both mirror families, all four leaf types, every other retained translate and all original regional graph relations. This is a genuine exact presentation of the same ordinary filled kernel. In particular it is not the previously withdrawn one-sheet quotient. The theta equations may become coupled recurrence words after the substitution; no independence, vanishing or redundancy is asserted for them.

The remaining substantive gate is to control these carried-along mixed relations on the remaining generators, or prove an appropriate relative basis-extension theorem. The square recurrence alone does not supply a faithful regional embedding after the full filling, a kappa-invariant ambient kernel, or either fixed-source equality. No compact normal-closure/intersection exchange is used.
