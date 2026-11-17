# Full induced topology of the actual boundary carrier

Research, checkpoint25. The actual regional R, its ordinary index-two subgroup R^0, adapted cone C, selected gap cone c=aCa^-1, neck K=F(a,B,d,e,f), base loop k, and full prefix P=P5=aBfde are retained. Let H=<c,k,T>, T=cP. The proper intermediate group is

    M=R *_H B = <R,j | j²=1, [jcj,k]=1, jPj=P^-1>,

where B is the isolated boundary corner. The four remaining prefix relations are not imposed.

## 1. The exact discrete carrier and the corner intersection

Let D_inf=<P,j> in B. In the corner presentation

    B=<D,u,k,j | D²=j²=1, [k,D]=[k,u]=1, juj=u^-1>,

we have c=jDj, T=uD and P=jDjuD. There is a literal retraction B->D_inf: send D,k to1, u to the actual P, and j to j. The composite on P,j is the identity, since the established boundary relation is jPj=P^-1. Thus D_inf is the infinite dihedral group and has full induced topology in B.

The auxiliary j-parity is zero on H and P and one on j. Its kernel in D_inf is exactly <P>. Therefore

    D_inf intersect H=<P>.

The same argument works directly in the full completions: both subgroups are embedded full completions, the parity kernel in D_inf-hat is the closure of <P>, and that closure is already in H-hat. Consequently

    D_inf-hat intersect H-hat=closure<P> inside B-hat.

Together with the already proved actual K intersect H=<P>, ordinary amalgam normal form embeds the carrier

    J0=<K,j> = K *_{<P>} D_inf.

Since (P1,P2,P3,P4,P5) is a literal free basis of K, this is also

    J0=F(P1,P2,P3,P4) * D_inf(P,j).

These discrete statements do not by themselves assert profinite subamalgam immersion. The next argument proves full topology by extending each finite target.

## 2. The actual regional detector survives killing k

The B112/B114 ordinary detector, identified with its actual neck image, is a retraction

    r:R^0->K.

Its companion under the adapted cone is exactly

    r(CaC)=r(CBC)=r(CdC)=r(CeC)=1,
    r(CfC)=f.

The entire actual annular presentation, including all node and both signed base-action relations, was checked for this detector. It is not a generic-fiber map. Also h=fk and the detector sends both f,h to f, so

    r(k)=1,   r(CkC)=1.

For the second equality one may use the actual relation CkC=hkh^-1, or the recorded detector on barred f and h. Since R=R^0 semidirect <C>, the normal closure of k in R is the normal closure in R^0 of k and CkC. Thus r factors through the ordinary subgroup of

    Rbar=R/normal_closure_R(k).

The resulting map rbar:Rbar^0->K still fixes every element of K. It follows in particular that this actual filling preserves K injectively. For Q=CPC, the literal prefix gives

    rbar(P)=P,   rbar(Q)=f.

Here the cone is the adapted C throughout this calculation; the selected cone c is not substituted for it.

## 3. The exact two-reflection ordinary presentation

Killing k in the complete intermediate presentation gives exactly

    Mbar=M/normal_closure_M(k)=<Rbar,j | j²=1, jPj=P^-1>.

The cross relation disappears because k is killed. The original ordinary parity extends by epsilon(j)=0; epsilon(C)=1 and epsilon(P)=0. Its kernel has the exact Reidemeister--Schreier presentation, with transversal {1,C},

    Mbar^0=<Rbar^0,j0,j1 |
              j0²=j1²=1,
              j0 P j0=P^-1,
              j1 Q j1=Q^-1>,

where j0=j and j1=CjC, Q=CPC. There is no further relation between j0 and j1. This follows by rewriting each of the two added relators and its C-conjugate; all pre-existing regional relations give precisely Rbar^0. This auxiliary index-two step uses the original cone parity, not the mirror parity.

Define

    L=J0 *_{<f>} D_inf(f,j1)
     =<K,j0,j1 | j0²=j1²=1,
                   j0 P j0=P^-1,
                   j1 f j1=f^-1>.

The map rbar on the regional base, j0->j0 and j1->j1 respects the complete displayed presentation and gives Mbar^0->L. On the actual carrier it is the identity. Both cyclic maps in the displayed amalgam for L are injective: f has infinite order in the embedded K<=J0. Thus J0 embeds in L by ordinary normal form. This also proves directly that killing k in M does not collapse any carrier element.

## 4. Every finite carrier target extends far enough

Let psi:J0->F be an arbitrary finite target, replacing F by its finite image. Put g=psi(f), and let n be its order (n=1 is allowed). Form the finite dihedral group

    D_n=<g_0,t | g_0^n=1, t²=1, t g_0 t=g_0^-1>.

The maps identify the cyclic subgroups <g> in F and <g_0> in D_n. Hence L maps to the ordinary finite-group amalgam

    F *_{<g>=<g_0>} D_n,

by psi on J0 and j1->t. The relation on the existing j0 already holds in the given target F; its value is not modified or chosen anew.

This finite-group amalgam has a finite permutation quotient injective on both finite vertices. Indeed, take free regular-multiple actions of F and D_n on one finite set whose cardinality is divisible by both orders. Their restrictions to the common cyclic subgroup are free actions with the same number of orbits. An intertwining bijection aligns those restrictions. The two resulting permutation representations agree on the edge, define a homomorphism of the amalgam, and remain injective on both finite vertices.

Composing Mbar^0->L with this finite quotient gives a finite map whose restriction to J0 is an injective postcomposition of psi. Its kernel on J0 is therefore exactly ker(psi). Take the normal core of its finite-index kernel through the index-two inclusion Mbar^0<=Mbar. Concretely, since C²=1, intersect the kernel with its C-conjugate. The resulting finite-index normal subgroup of Mbar restricts to a subgroup of ker(psi) on J0. Pull it back through M->Mbar.

We have refined EVERY prescribed finite carrier kernel by a finite kernel of the actual intermediate M. This proves that J0 has its full induced profinite topology in M. No general profinite subamalgam-immersion theorem, separability of arbitrary products, or completed intersection-exchange is used.

## 5. Exact completed carrier and scope

The induced map J0-hat->M-hat is injective. Its image is precisely the closed subgroup generated by the actual K-hat and j, by compactness and density. As an abstract full profinite group it is

    J0-hat=K-hat amalgam_{closure<P>} D_inf-hat
          =Fhat_4 amalgam D_inf-hat,

where the first pushout is proper because <P> is the specified free factor of K. This assertion is proved by the finite-target construction, not inferred solely from the two completed edge intersections.

The four final prefix relations jP_i jP_i, i=1,2,3,4, remain unfilled. Nothing here proves carrier or vertex survival after imposing them, computes a completed centralizer of M, or decides either main question.

## Provenance

The actual detector and its complete-presentation checks are B112 and B114, with the literal companion dictionary in work_DE/next_marginal_source/annular_neck_retraction23.json. The actual H/K and corner comparisons are B118. The intermediate amalgam presentation and proper completion are work_A/intermediate_boundary_amalgam25.md. This proof uses these established actual maps and provides a new uniform finite-target extension; it is not an orbit or finite-depth test.
