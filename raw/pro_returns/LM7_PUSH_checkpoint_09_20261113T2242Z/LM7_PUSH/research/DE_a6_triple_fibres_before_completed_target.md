# Full correction image above the signed 3.A6 source

This new note continues the frozen source package without changing its
files. It records completed literal comparisons and the exact subgroup
argument that uses them. The new four-strand common-target calculation
is running separately; no unsaved target order is used here.

## Signed source comparison

Let X be the induced 3.A6 source, G the old A6 source, G_L the old
signed SL2(F5) source, and J=G x_(Q30) G_L the actual E.54 common
source. The completed source package gives the specified quotient

    X -> B0=im(B -> G x Q12),     kernel K=F3^79.

The map J->B0 uses its G coordinate and the literal G_L->Q12 map.
To compare the entire signed source, adjoin the affine-three block
to the previously certified actual G/A5 common source. The resulting
degree11334 base B1 has index two over that old degree11010 source.
The complete lifted presentation evaluates all1159255 Schreier
relations. Its full ternary kernel still has dimension79.
`de_a6_triple_signed_replay.py` independently evaluates all79 basis
words in X and B1, checks all158 source conjugates, and identifies
the resulting space with K by an explicit invertible79x79 matrix.

Thus im(B->X x B1)=X x_(B0) B1. The kernel of J->B1 is a subgroup
of the proved elementary-two kernel G_L->G_A. Over B1, the actual
joint kernel is subdirect in this two-group and K. Their common
quotient is trivial by coprime orders. Consequently the exact map is

    Y=im(B -> X x G_L)=X x_(B0) J.

This uses the actual base maps and literal kernel words; an abstract
group-order coincidence is not substituted for the quotient maps.

## Perfect bridge

Write C for the old perfect A6 residual, E for its preimage in X,
and D=E'. The complete central presentation and replay prove

    E_ab=V=F3^3,     D=D',     ker(D->C)=F3^76.

The F action on V is trivial. E.54 provides the actual common
simple quotient A=A5^3 and the perfect pullback

    V_old=C x_A U2,   U2=SL2(F5)^3.

The pullback W=D x_A U2 maps onto V_old with elementary-three kernel
F3^76 and onto D with central elementary-two kernel C2^3. Its
abelianization is therefore both3-primary and2-primary, so W is
perfect. The same universal-central-cover argument proved in E.54
now gives the perfect group

    D_J=D x_A C_L.

More explicitly, for K_D=ker(D->A), the perfect central extension
D/[D,K_D] of A is a quotient of U2. The actual pullback W maps
onto K_D/[D,K_D] by (d,u)->dbar phi(u)^-1. W's perfection makes
this quotient trivial. For D_J->C_L its kernel is K_D and
[D_J,K_D]=[D,K_D]=K_D. Since C_L is perfect, D_J is perfect.

Let E_J be the preimage in Y of C_J=C x_A C_L. Then

    E_J=E x_A C_L,     E_J/D_J=V.

The quotient map is precisely the E->V map, retaining the same
three coordinate characters. Its restriction to K has kernel
F3^76. Conjugation by the pure F image acts trivially on V.

## Exact alternating pairing in the stable module

The saved nine F' generators for the old ternary module are corrected
by the exact six binary basis words to obtain the old commuting
complement V9. Taking fourth powers keeps those order-three quotient
values and kills their ordinary Q12 values. This last assertion is
checked in the actual576-point Q12 action. The resulting words g_i
therefore belong to N. Their affine-three linear parts are identity;
their translations need not vanish.

For the exact six-column stable subspace V6 in E.48, form the literal
ordered products g_v. Their images lie in the old R1=P' x_A C_L:
their A6 coordinates are in P', and their G_L values lie in C_L
because they are F' words with trivial Q12 value and the specified
F'/C_L->Q12 map is injective.

All nine cubes, all36 commutators among the nine lifts, and all15
commutators among these six stable lifts are evaluated in E->V.
The query program sifts each actual A6 permutation through the
complete C chain, simultaneously dividing its full3.A6 value by
the identical literal transversal words. If the final kernel value
is k and the total ordinary C-generator exponent vector is e, the
answer is exactly L(k)+h(e), with the saved character matrices L,h.

The independent replay reconstructs all60 original F words, every
normal-form word used in the divisions, all actual kernel residues,
and all exponent signs. The cubes have zero image. The alternating
commutator image has rank three, and its restriction to V6 also has
rank three. The stable pairs (0,1),(0,2),(4,5) give the columns

    [1,2,0]^t, [1,1,1]^t, [2,0,0]^t,

whose determinant is4, a unit modulo three. The direct15 stable
queries also agree with restriction of the full9x9 alternating
pairing; bilinearity is thus checked in the actual word model.

## Every lower-central term, followed by the actual intersection

Let Rtilde1 be the full preimage of R1 in Y. It lies in both the
actual N image and the actual H image. Its perfect normal subgroup
D_J lies in every lower-central term of either image. E.54 proves
that the J image of gamma_j(N) is R1 for every j>=2.

Fix such a j and choose m>=j. Lift the six specified old R1 values
through the actual image of gamma_m(N). Compared with the six
literal g_v values, these lifts differ by K. Their commutators have
the same V values, because K maps into V and V centralizes the pure
F image modulo D_J. The three displayed commutators belong to
gamma_(2m)(N), hence to gamma_j(N), and fill V. Together with D_J
they fill E_J, including all of K. Surjectivity onto old R1 then gives

    rho_Y(gamma_j N)=Rtilde1  for every j>=2.

This proves all finite lower-central terms, not only one chosen
degree. To obtain the required simultaneous intersection, use the
actual subgroup sequence I0=gamma5(N), I_(n+1)=[H,I_n]. E.54 gives
[rho_J(H),R1]=R1. The new commutator image contains D_J by
perfection and contains all of V by the same stable pairing, with
both arguments lying in Rtilde1 subset rho_Y(H). It follows that

    [rho_Y(H),Rtilde1]=Rtilde1.

Thus every I_n has the full Rtilde1 image. These subgroups descend
and are contained in gamma5(N) and successively deeper gamma_n(H).
The fibres of each fixed finite value are nonempty nested compact
sets, so their intersection gives the exact surjection

    I=gamma5(N) intersect R_nil(H) -> Rtilde1.

The reverse inclusion follows from the already proved gamma5(N)
image. In particular I intersect ker(rho_J) maps onto every one of
the79 coordinates of K. This is the complete correcting image.

## Uniform old factors and complete source generation

By E.57, the actual rho_R image of I intersect ker(rho_J) is

    U=Gamma5(1) x product_(p>=7) SL2(Z_p).

The pro-five first factor has no quotient C3, and all the other
factors are perfect. Hence U has no elementary-three quotient.
Goursat applied to the specified maps from I intersect ker(rho_J)
to K and U gives their full product. Therefore

    rho_X(I intersect ker(rho_J) intersect ker(rho_R))=K.

This subgroup kills every old D23 and nilpotent-H boundary factor.
The same argument can simultaneously retain the actual E.59/E.62
finite source coordinates. I is contained in N', whose images in
those sources are two-groups. The actual joint image Z in U times
this finite two-group projects onto U and has a two-group kernel
over U. Every homomorphism Z->C3 kills that kernel and therefore
factors through U; it is trivial. Consequently Z has no nontrivial
elementary-three quotient. Goursat for the actual maps to K and Z
gives their full product, with no separate product decomposition
of Z assumed. This preserves already present coordinate values;
it does not assert an uncomputed simultaneous old E.57/E.62 family.

For every finite E.57 common source Gamma retaining J, the actual
new source is exactly Gamma x_(B0) X. Indeed the displayed actual
kernel subgroup maps onto K while killing Gamma. The same statement
holds for the coherent inverse system of these sources.

Take the full old word and the same actual Galois element sigma
from E.54 or E.57. The discrepancy between its X value and the
X value of f_sigma lies in K, because their J values agree. Choose
its preimage in the displayed kernel subgroup and multiply the old
word by this correcting word. Every old coordinate is retained;
all six new Ferrari evaluations equal those of f_sigma. The new
pentagon, both normalized cycles, braid relations and full twists
therefore hold, and the new target map is onto.

For common-source generation, Phi_sigma preserves N through the
actual retained Q12 cusp-gauge map and preserves H through its
ordinary abelianization. Thus Phi_sigma(I)=I. On I the corrected
J,R,X coordinates are their actual source maps precomposed with
Phi_sigma, and all remaining old nilpotent coordinates vanish.
The corrected image consequently contains the entire pure K over
Gamma. Its old Gamma projection is onto, so it is the whole actual
fibre product Gamma x_(B0) X. No invariance of the finite D23 or X
kernel under a general shadow is assumed.

## Preserved preliminary failures

The first query preparation incorrectly asserted that its N lifts
had zero entire affine value. The actual base theorem identifies
the affine map as a quotient of A6 times Q12; it does not identify
it as a quotient of Q12 alone. The original program/stdout/stderr
are preserved under `de_a6_triple_commutator_prepare_failed_affine_identity`.
The correction checks the literal Q12 value, retains the possible
affine translations, and checks affine identity only for the cube
and commutator query words, where it is actually needed.

A first C++ query wrapper failed at compilation because the included
collector defines and undefines its own main macro. It never ran.
Its source and explanation are preserved under
`de_a6_triple_query_failed_include`. The compiled query header is an
exact verified slice of the frozen CentralData/CentralProbe definitions;
the independent replay checks that equality again.

## Completed new program sequence

1. `de_a6_triple_signed_base_prepare.py`, complete base chain,
   and full signed kernel presentation: all1159255 relations.
2. `de_a6_triple_signed_replay.py`: all79 words and158 conjugates,
   full invertible comparison with the original K.
3. `de_a6_triple_commutator_prepare.py`: actual source lifts and60
   complete normal-form queries.
4. `de_a6_triple_query.cpp`: complete old C-chain replay and exact
   simultaneous normal-form division in both maps.
5. `de_a6_triple_commutator_replay.py`: independent Python word,
   residue, exponent and alternating-pairing verification.

The new target quotient programs have prefix `de_a6_triple_target_`.
They are separate ongoing work until their complete certificates finish.
