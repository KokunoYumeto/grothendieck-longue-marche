# Exact old-base row action and the remaining collision-stabilizer gate

Research only, checkpoint18. This gives the actual row action for all six
old-base generators and all eleven normalized source generators, together
with an exact stabilizer formulation. It does not determine those
stabilizers, replace an augmented collision by a full column identity, or
evaluate the full residual map kappa.

## 1. Actual inputs and composition convention

Use B94's actual generic-fiber quotient

G=(R_A times R_B) semidirect T, T=F(y1,...,y5), Omega=Z[G],

and its common peripheral basis x_(g,i), with paired slots
i in {2,3,5,6,7,8,10,11}. The retained involution beta in B94 is fixed.
The actual paired F21 basis has retained indices1,4,9,14,19; its A and B
deleted indices are i and i+10. F exchanges these two deleted generators
literally. All input words use the corrected geometric marking.

The finite certificate is

* work_A/code/check_old_base_augmented_row_action.py/.out/.err;
* work_A/old_base_augmented_row_action.json.

It reads the actual paired package, the full19-source package and the
independently computed old0 incidence certificate. It checks272 exact
peripheral conjugators across the six old and eleven source operators,
all eleven F-commutations and paired-head identities, all64 old0 augmented
rows and signed retained units,384 inverse row checks,704 source/far-word
comparisons and2304 ordered generator-pair compositions. Every actual input
and the producer are hashed. Initial output before adding inverse/source
checks is retained separately; it was already a passing finite check.

Geometric push has the convention alpha_g(x)=g^-1 x g, so
alpha_(uv)=alpha_v composed alpha_u. To avoid reversing a product silently,
use the operator group B_op=B^op below: a product a*c means alpha_a after
alpha_c and corresponds to geometric word c*a. Equivalently one may use
the original free old-base group with each acting generator inverted.
The JSON records this convention, and its source/far comparisons use the
actual chronological geometric words. B_op is still a free group of rank6.

## 2. Derivation of the complete row action

For any actual old operator alpha, write its peripheral images as

alpha(p_Ai)=k_Ai p_Ai k_Ai^-1,
alpha(p_Bj)=k_Bj p_Bj k_Bj^-1.

The actual old monodromies preserve each labelled deleted section. The
certificate obtains the conjugators by cyclic reduction of their literal
F21 words and checks the displayed free-word identities. Let

h_Ai=filled(k_Ai), h_Bj=filled(k_Bj), phi=filled(alpha)|T,
psi=beta composed phi composed beta.

The retained heads are independent of multiplying a conjugator by a power
of its deleted peripheral, because that peripheral fills to1.

An A label(g,i) is sent, on residual abelianization, to
(phi(g)h_Ai,i). A B common label(h,j) uses actual retained whisker beta(h),
so it is sent to (psi(h)beta(h_Bj),j). Inner residual conjugators disappear
in this augmentation. This is also intrinsic: P/(I_E P) is the tensor of
the two residual abelianizations, by the universal commutator pairing;
it does not require alpha to preserve the chosen free factors literally
before quotienting.

B94's row epsilon_(i,j,z) has A label(1,i) and B label(z,j). Its transformed
row and its retained unit are therefore exactly

  Theta_alpha(i,j,z)
       =(i,j, beta(h_Ai)^-1 psi(z) beta(h_Bj)),             (1)

  augmented unit for epsilon_(i,j,z) = h_Ai.              (2)

More generally a column with augmented entry epsilon*d_t in that row
has augmented entry with the same sign and retained word phi(t)h_Ai
in row(1). The independent64 old0 incidence/unit comparisons check this
formula on actual full transported columns, not merely on formal test rows.

For a normalized source operator, literal F-commutation gives
phi beta=beta phi and h_Bi=beta(h_Ai). Writing h_i=h_Ai, (1) becomes

  Theta_alpha(i,j,z)=(i,j,beta(h_i)^-1 phi(z)h_j).         (3)

All eleven actual source operators satisfy this. Their row maps agree
with the maps obtained from their literal far-base Schreier words. This
agreement is expected geometrically: their normalizing correction is an
inner generic-fiber action, hence multiplication by a G unit on P, which
does not change the normalized row.

For operator composition alpha after gamma the exact head rule is

h_(alpha gamma),Ai=phi_alpha(h_gamma,Ai)h_alpha,Ai,

and likewise on B, while phi_(alpha gamma)=phi_alpha phi_gamma.
Substituting this identity into(1) proves composition for arbitrary words.
Thus the finite data determine an actual action of the free operator group,
not a bounded approximation. The finite inverse and pair-composition
checks verify the recorded generator conventions. They do not solve an
all-word stabilizer or assert a full-column identity.

## 3. Exact component-pair stabilizers as section intersections

Fix physical slots i,j. Put

t_Ai(alpha)=beta(h_Ai)^-1,
t_Bj(alpha)=beta(h_Bj)^-1.

The head rule proves that both are ordinary left1-cocycles for the
operator-group action psi on T. Therefore, in the concrete semidirect
product Q_beta=T semidirect_psi B_op, each defines a section subgroup

Sigma_Ai={ (t_Ai(w),w):w in B_op },
Sigma_Bj={ (t_Bj(w),w):w in B_op }.

Their projection onto B_op is an isomorphism. Equation(1) says that the
row coordinate action is

               z -> t_Ai(w) psi_w(z) t_Bj(w)^-1.

Hence the exact stabilizer of a row(i,j,z) is the projection of

             Sigma_Ai intersect (z,1)Sigma_Bj(z^-1,1).   (4)

Indeed Theta_w(z)=z is precisely
sigma_Ai(w)(z,1)=(z,1)sigma_Bj(w). No finite quotient or abelianized
subgroup intersection is substituted in(4). The subgroup is free because
it injects into the free group B_op; finite generation is not asserted.

This also has the actual geometric interpretation. Each deleted A divisor
is the section v=u or v=q/u over the old base C* minus mu5, with u in mu5
minus{1}. Its coincidences with retained punctures occur only at excluded
q=0,u,u^2. The B divisors are their images under the retained-puncture
preserving involution F. Thus every A and B divisor is a genuine section
over the whole old base. The section-loop transport of its normal
meridian supplies exactly the cocycles above, up to the explicitly chosen
retained whiskers and inversion of the geometric push convention. Formula
(4) is the intersection of their actual lifted-divisor stabilizers in the
filled free-by-free group, written in the common beta-coordinate.

The64 initial seeds have one physical pair(i,j) each. For a fixed seed
row z_nu, equality Theta_u(z_nu)=Theta_v(z_nu) is equivalent to
v^-1*u belonging to(4). Thus the row index set of its full old-base orbit
is the set of cosets w Stab(z_nu). Different physical slot pairs cannot
collide. This is an exact reduction; no algorithmic determination of these
infinite-word cosets is claimed.

## 4. A sufficient full-column collision criterion

Let C_w,nu=alpha_w(c_nu), where the old-base action uses the convention
above. Each column still has exactly one signed retained-word augmentation.
Suppose that whenever two of these actual augmented rows coincide, their
full columns are related by a literal group unit in G, with the sign
included. This condition is strictly stronger than row equality.

Choose one column for each distinct row. Any relation among the chosen
columns has finite support. The corresponding finitely many rows form a
diagonal-unit minor modulo I_E Omega. B94's separated-filtration argument
then forces every coefficient to vanish. Consequently these representatives
are a free Omega basis of the full orbit span. No inversion of a matrix or
completion of coefficients is used, and the argument applies to an infinite
set of rows because each proposed relation is finite.

For one seed it suffices to prove the full-column unit relation for a
generating set of its exact stabilizer(4): compositions and inverses then
propagate the relation through the actual semilinear operators. A generating
set need not be finite; none is asserted here. B95 verifies one bounded
instance of this criterion: four old0 row stabilizations have complete
free-word/G-unit witnesses, while all other rows move.

Even a full collision theorem would still require identifying the resulting
F coefficient orbits and their actual source Tate values. The present note
does not infer that analysis from the augmentation labels. Conversely, a
failure of the unit-relation criterion need not be a nonzero kappa value:
it may introduce a nonmonomial relation whose Tate contribution vanishes.

## 5. All individual translates already have source-ideal image

The complete CE proof and exact odd-loop certificate are
work_CE/research_symmetric_old_translate_two_cosets_18h.txt and
work_CE/next_symmetric_nodes/symmetric_odd_old_translate.json.
They retain the positive-push versus canonical second-sheet pullback
convention. The actual index-two source cover has parity only at q=1;
its eleven returned operators preserve I and commute with F. The exact
odd representative has four neutral cone classes whose Tate values are
actual second-sheet source classes (or their branch-square source images).
Thus every individual translated module L_w is F-stable, has H2(C2,L_w)=0,
and has its H1 image in J_I. Summing the individual images gives exactly
J_I: the two sheets supply all eight source meridians, and the actual
eleven source-operator orbits generate I as a subgroup. The identities
uv-1=(u-1)+u(v-1) and u^-1-1=-u^-1(u-1) give the left-ideal equality.

This uniform statement concerns the sum of individual H1 images. It must
not be replaced by a statement about H1 of their module sum.

For clarity, let D_orb be the direct sum of all these actual F-stable
modules, mapping by addition onto the full transported image Lbar. Let
K_orb be its kernel. B91's complete presentation and B94's generic-fiber
factorization identify the image with the full old-base orbit sum. Finite
support and the two-periodic C2 resolution give

H2(C2,D_orb)=0,
image[H1(C2,D_orb)->H1(C2,P)]=J_I.

The exact sequence0->K_orb->D_orb->Lbar->0 therefore identifies
H1(C2,Lbar)/image H1(C2,D_orb) with H2(C2,K_orb). Composing with the
diagonal Tate map modulo J_I gives a well-defined map

     H2(C2,K_orb) -> I_F2[R]/J_I

whose image is exactly U/J_I. This is the same intrinsic excess measured
by B92's kappa, expressed through overlaps of already understood actual
retained-deck blocks. It does not identify the two relation kernels or
assert injectivity of the residual map. Pairwise overlap computations do
not determine K_orb or overlaps with an entire preceding sum.

## 6. A structural kernel reduction and an actual failure of the unit shortcut

The retained automorphisms phi for the four old generators about
zeta,zeta^2,zeta^3,zeta^4 are literally the identity, as their complete
five-generator images in the certificate show. Therefore the retained
action factors through the projection of the old free group onto its two
generators about0 and1. Let K be the kernel of this projection, with the
same opposite-group convention when using operator products. For every
element of K, phi=psi=identity. The two section cocycles in Section3 restrict
to ordinary homomorphisms on K; equivalently the h heads are antihomomorphisms.

Moreover h_Bi=beta(h_Ai) on all of K, not only on the four initial root
generators. Indeed the actual discrepancy F alpha F alpha^-1 is inner by
a generic-fiber word k. On the retained free group it is the identity
when phi=identity, so filled(k) is central in T and hence1. Evaluating the
discrepancy on a paired deleted meridian shows beta(h_Ai)=filled(k)h_Bi:
the difference of its two conjugators centralizes that free peripheral,
and its peripheral-power ambiguity disappears after filling. This proves
the asserted equality for every element of K.

For a diagonal physical row(i,i,z), the actual fixed-node condition gives
beta(z)z=1. The certificate checks this literally on all eight starting
rows. Its K-stabilizer condition is

                     beta(h_i)^-1 z h_i=z.

This is equivalent to h_i centralizing the involution tau*z in
T semidirect C2=C2*C2*F2. Reduced free-product normal form says that the
centralizer of this involution is its order-two subgroup, whose intersection
with T is trivial. Thus the K-row stabilizer is exactly ker(h_i). This
removes the twisted-equalizer ambiguity for these diagonal rows, without
claiming to determine all full-column actions of that kernel.

On the free subgroup generated by the four root lassos themselves, each
of the eight head maps kills exactly two generators and sends the other
two to noncommuting words in T. These are checked, together with an integral
abelian unit minor for each pair, by
work_A/code/check_root_four_head_kernels.py and its genuine output;
the complete words are in root_four_head_kernel_certificate.json.
The two noncommuting images freely generate their rank-two subgroup:
Nielsen--Schreier gives a free subgroup of rank at most two and noncommutation
excludes rank at most one; a surjection from F2 to a rank-two free group is
an isomorphism by Hopficity. The latter follows directly from residual
finiteness and finiteness of the number of subgroups of any fixed finite
index: preimage by a surjective endomorphism permutes this finite set, so
its kernel lies in every finite-index subgroup. Thus the kernel on this
four-root subgroup is exactly the normal closure of its two zero-head
generators. This does not describe the head kernel on all of K or control
the column actions of conjugates of these two generators.

There is a complete bounded diagnostic on its sixteen basic zero-head cases.
The four root generators and eight fixed diagonal nodes give exactly sixteen
pairs with both heads trivial. The producer and genuine output are

* work_A/code/check_zero_head_diagonal_node_actions.py/.out/.err;
* work_A/zero_head_diagonal_node_actions.json.

For every case it constructs the actual transformed F21 relator. It computes
the product-tree chain by the explicit horizontal-edge/vertical-path
contraction, recomputes its full boundary independently, and checks the eight
initial chains against the stored actual input. Normalization is the unique
G row normal form of B94. All sixteen transformed augmented rows and signed
retained units agree with their originals. Nevertheless all sixteen FULL
sets of nonzero G rows differ. A left G unit does not change this row set,
so none of the sixteen transformed columns is a G-unit multiple of its
original. Positive free-word conjugacy also fails in all sixteen cases.

For example, the zeta operator on node(8,0) has117 original terms and805
transformed terms. Its transformed support contains the row
(2,5,y2^-1), absent from the original support. The data retain the exact
nonzero-row witness, full transformed word, input hashes and canonical
chain hashes; the producer reconstructs the entire chain. The analogous
actual row-set witness is retained for each of the other fifteen cases.

Consequently the sufficient global unit-collision condition in Section4
is FALSE for this actual geometry. It is not merely unverified. Its formal
implication remains valid, but it cannot be applied as the global solution.
This conclusion does not show that the transformed column lies outside the
span of all other old-orbit columns, does not provide a nonzero kappa class,
and does not prove any source-ideal nonmembership. It identifies genuinely
nonmonomial column behavior inside an exact augmented-row stabilizer.

The initial producer used a wrong metadata key and its genuine failure is
preserved. A subsequent redundant unrestricted unit search/verbose chain
serialization was interrupted and then killed; those versions and outputs
are retained. The successful producer uses exact row-set witnesses and
compact chain hashes, without discarding any coefficient in its calculation.
Its first complete pass is preserved before a progress-label formatting
repair and addition of the explicit nonzero-row term witnesses.

## Status

The actual generator row action, its orientation, and the section-intersection
stabilizer formulation are proved. The finite generator certificate has
executed successfully. The diagonal stabilizers on K have the exact kernel
description above, but their general full-column actions remain unresolved.
The actual simple unit-collision shortcut is refuted by sixteen complete
finite witnesses. No finite-depth source nonmembership, augmentation-adic
source membership, global kappa value, nonlinear fixed lift or compact
coefficient comparison follows.
