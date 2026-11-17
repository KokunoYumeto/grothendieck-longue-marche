# Actual cubic next layer after A65 — research, not yet formal

This note is separate from the frozen ninth-checkpoint source. The main
full involution and cofinality questions remain open. The constructions
below are actual finite groups pulled back over the initial profinite C.
Their action/norm and scalar-frame gates must be checked separately.

## 1. A concrete simultaneous group

Write A=V^4 for the four normalized cusp coordinates, T=(V^(2))^6
for A63's ordered pairs, U=(V^(3))^4 for the increasing triples, and
Z=(V^(3))^16 with ordered indices (r,i), 1≤r,i≤4. Multiplication is
coordinatewise in F8 at each of the36 weights. On (a,t,u,z), put

    a'' = a+b,
    t''_ij = t_ij+t'_ij+a_i*b_j,
    u''_ijk = u_ijk+u'_ijk+a_i*t'_jk+t_ij*b_k,
    z''_ri = z_ri+z'_ri+a_r^2*b_i.

The two coboundaries of the displayed u correction cancel literally;
all z corrections are biadditive over F2. Thus this is an actual
class-three finite2group. H acts by scalar degrees1,2,3,3 and its
unchanged weight permutations. This is a strict action.

Its derived group consists of T,U,Z. The four U directions are
attained by [a_i,[a_j,a_k]], one increasing triple at a time. The
six T directions are the original cup brackets. The sixteen Z
directions are independent: for r≠i their bracket functions are
a_r^2 b_i+b_r^2 a_i, with the two ordered directions on a pair
distinguished by the F2-bilinearly independent functions a²b and
ab²; on a diagonal the function a²b+ab² is nonzero overF8.
There is no common H-module relation with T because the T brackets
are supported within a single Frobenius family and Z brackets
between two different families. Consequently the Frattini quotient
is exactly A.

The source s has zero cusp coordinate. Set S pure, and set R to
the conjugate of pure r by a lift with abelian coordinate r e(r)
and all higher coordinates0. S²=R³=1, and the source projects
literally onto the A63 N quotient. Original-base H1(C,V)=0 makes
the actual initial R-image onto A; finite2group Frattini then
makes it the full displayed group.

Pairing with P_infty over A gives an actual quotient over the
A65 extension E_infty with kernel U⊕Z=(V^(3))^20. The joint
residual has abelianization A_infty and Frattini quotient V^8,
so the actual source image is the full fiber product. The old
globally central M_infty has no common H quotient with the new
nontrivial-weight derived factors. The four triple directions
cannot split over the old class-two residual: any section would
give a class-two group surjecting a group with nonzero third
commutators. The sixteen ordinary directions cannot split either:
their cross-Frobenius brackets cannot factor through the old
same-family T bracket or the trivial-weight old M bracket.
The same argument handles every nonzero linear combination,
separating first the triple part and then the ordinary part.

V^(3) has literal scalar action cubed. Its underlying binary
simple type is still108, because 3S=-4S=4S, but that is not an
identity of the literal F8 coefficient representations.

## 2. Explicit lifts of the stored degree-two shears

In the zero-t A64 witness, all eight-class H1 parts of CCOR and
PCOR are supported on the four cusp classes. Let L_ij,r be one
such6×4 coefficient matrix. The shear

    t_ij -> t_ij + sum_r L_ij,r a_r²

lifts to an actual H-equivariant automorphism F_L of the group
above. It fixes a and z and sends

    u_ijk -> u_ijk
             + sum_r [L_ij,r z_rk
                       + L_jk,r (z_ri + a_i*a_r²)].

Indeed, the coboundary of z_rk is a_r² b_k, and that of
z_ri+a_i a_r² is a_i b_r². Their sum is precisely the change
of the UT4 product correction after applying the t shear.
The formula is linear in L and fixes every argument occurring
in its own correction, so F_L²=1 and F_L F_K=F_(L+K).

Let v_c,v_p denote the six36-coordinate inner terms of CCOR
and PCOR, and W_c,W the old cusp affine inner terms. The
canonical-c candidate on the new group is

    Inner(v_c) F_Lc Inner(W_c) C.

The positive candidate is

    Inner(v_p+L_p(W²)) F_Lp Inner(W).

The extra L_p(W²) is needed because PCOR was written as a
source cocycle, whereas the shear is applied after Inner(W).
These formulas project literally to the stored A64 action.
They can then be corrected by actual (V^(3))^20 cocycles on
the old quotient. Initial-base H1 and the complete eight-class
source system give44 independent source-value columns per
coordinate; the positive cusp/s-class system has rank40.

The induced action on the new kernel is not diagonal in its
twenty multiplicities: F_L adds ordinary Z coordinates into
the four U coordinates. Thus a cusp-centralizing inner
correction can now change the negative square by a genuine
norm. It would be incorrect to import A64's fixed-square
argument without retaining this unipotent multiplicity action.

## 3. A genuinely new scalar resonance

The ordinary cubic cups pair two Frobenius families. An
invariant third commutator can now have weights λ,2λ,4λ,
whose sum is0 in the F7 character group. All three Jacobi
terms can survive; A65's cancellation no longer applies.

The smallest local example is G=F8×F8 with

    (a,z)(b,w)=(a+b,z+w+a²b).

The scalar7 action is (a,z)->(xi*a,xi³*z). An exact normalized
bar calculation in check_cubic_suzuki_center.py gives

    invariant C1 dimension9, invariant C2 dimension567;
    cocycle-equation rank556, hence Z2 dimension11;
    invariant B2 dimension9, hence H2(G,F2)^C7 dimension2.

There is also a direct formula, independent of that rank count.
For q inF8 and d=q+q², define

    kappa_q((a,z),(b,w))
       =Tr(d*a⁴*w + q*a⁶*b + q²*a⁴*b³).

The coboundary of the first term is Tr(d*a⁴*b²*c), and the
coboundary of the last two terms is the same. It is therefore
a normalized C7-invariant2cocycle. q=1 is the coboundary of
Tr(a⁷), so q moduloF2 gives the two independent scalar
directions. Their triple commutators are nonzero.

An even simpler F8-valued cocycle, independently supplied by
the parent, is

    f((a,z),(b,w))=z*b⁴+a²*w⁴.

It is a literal2cocycle, invariant under scalar7. For every q,
Tr(q f) differs from kappa_q by the coboundary of Tr(q a⁴z).
The512-element central cover has third commutators spanning
kerTr in its centralF8. Quotienting the central lineF2·1
gives a256-element stem cover with centralC2² and Frattini
quotientF8. The parent is independently checking all these
finite identities and the exact lower-central orders.

## 4. Actual source attainment of the scalar directions

Take36 weight copies of that stem cover and push out their
central(C2²)^36 by the permutation-sum map toC2². Scalar7
fixes the center, so the full monomial H-action descends.
The resulting group has Frattini quotientV, and its two
central directions are attained by third commutators at
one weight. Use one normalized cusp source row: S is pure,
R is the conjugate of pure r by the same affine lift as
above. Original-base H1 implies that the actual R-image
surjects V, hence attains the full stem cover by Frattini.

For each of the four diagonal cusp rows, the construction
projects literally onto z_ii's local cubic group in the
ordinary16-cup quotient. Their simultaneous fiber product
has eight independent central third-commutator directions:
triples supported in just row i attain the i-th pair and
vanish on the other rows and on the UT4 triples with three
distinct row indices. Its Frattini quotient is the same
complete old V^8, so it too is an actual source quotient.
Thus the new ordinary-cup quotient's actual first scalar
refinement has a quotient C2^8. This is an actual nonzero
scalar kernel, not yet an obstruction to lifting its
peripheral action, its negative square, or its frames.

The complete scalar kernel, its action, and the simultaneous
normalizer norm conditions have not yet been determined.

## 5. Exact computations after the construction

The actual20-chief model is implemented in check_A66_cubic_twenty.py.
Its source relations, projection to A64, literal canonical c, and
positive literal cusp/s-class equations all pass. The coefficient
negative action is (I+J)C³, where J maps the sixteen ordinary slots
into the four UT4 slots and J²=0. Here J has exact rank3, with
outputs z02+z20, z03, z03, z23. The cusp-inner norm therefore has
rank12, independently checked by CE. The stored A64 affine datum
has a nonzero literal inner square outside this image.

This is already visible in the ordinary16 projection, independently
implemented by check_A66_ordinary_cubic.py. Its00 coordinate has
inner-square value1 at weight0. Every cusp-inner norm projects to0
on the ordinary coordinates, and changes by the older T^tau action
freedom are forgotten by this quotient. Thus this is exhaustive
for the specified A56 affine datum/frame, but it does not exhaust
other A56 affine choices. CE independently reran the projection and
all80 cusp-inner columns.

The next target is W_free=0, which makes the positive action on
every free-cusp-only finite group literal identity. The old free
frame p then remains S-fixed; its higher norm still must be solved.
The stronger restrictions W_free=0 AND t_free=0 are linearly
feasible in the original360-coordinate A56 family: rank246,
114 homogeneous binary directions. However their complete old
central norm map has zero polar form and image rank2, and the
target is outside it. This exact restricted failure is stored in
check_A66_zero_W_t_norm.py/.out and A66_zero_W_t_quadratic_core.json;
the latter includes a dual annihilator supported at coordinate77
of the displayed normal-form norm quotient. The original and
successful zero-t witnesses are unchanged.

The alternative W_free=p_free=0 is already linearly impossible:
the canonical free c-inner vector is not beta-fixed, so it violates
the old affine normalizer norm. Root has an exact dual-annihilator
certificate for this distinct restricted target. Neither failure
settles W_free=0 with unrestricted compatible free t.

## 6. Larger-family repairs and precise remaining gates

Root's W0-only system has rank102 in the original360 variables,
leaving258 homogeneous directions. Its complete old central norm
has polar radical231, radical image0, and a27-bit quadratic core.
Exact enumeration found core assignment2128959 after4171819 steps.
The actual old action, literal cusp, and s-normalizer then pass.
The convenient r-frame J=(q,s) fails its central norm, so it is
explicitly flagged unresolved in A66_zero_W_free_t_partial.json.
This is not exhaustion of affine r-frames.

CE independently enumerated the complete local W0 s-frame gates
for the ordinary16 and lower-six cups. At each opposite weight
pair8↔11 and20↔23 there are29 allowed correction pairs: zero
plus four F8× orbits. The first partial tuple passed one pair
but failed the other. The231-dimensional old-norm radical has
local image rank24. Exactly29 of the841 paired local choices
are compatible with the SAME successful old norm core.
The linear certificate is A66_W0_radical_local_gate.json.

The first compatible choice, indices[6,0], was substituted into
the original group law and its remaining old central norm was
corrected. The resulting A66_W0_local_compatible_partial.json
passes negative action square, literal cusp, old s-conjugacy/norm,
W0, and the selected local coordinates. Its producer and stdout
are check_A66_W0_local_adjustment.py/.out. Full lower-six and
ordinary-sixteen group checks have now also passed: both actions
square to one and both complete s-frame norm systems solve.
Their positive correction coefficients are identically zero.
Current outputs explicitly label the r calculation not_tested;
the earlier ambiguous skipped-r stdout is separately preserved.
None
of the original or earlier failed witnesses was overwritten.

Root's initial-transporter review supplies an existential remedy
for the convenient r-frame failure. The A33 compact frame sets
can retain a pure transporter from s*d_s to d_r: it comes from
the common full Galois involution in the dyadic component and
from coprime complement conjugacy at odd components. This extra
closed condition preserves finite-common-refinement nonemptiness.
Once an actual pro-two quotient has an involutory negative action
and s-normalizer, lift that initial transporter, apply A16 while
retaining the resulting involution, and conjugate its order-three
complement onto actual r. This gives some involutory r-frame over
the exact original C-frame. It applies to these construction-
selected initial frames, not arbitrary later norm-zero frames.
The parent saved the complete proof in
records/A66_initial_transporter_and_r_frame_review.md, and I
independently reviewed it successfully.

Separately, CE exhaustively computed the ordinary16 action-square
function on the complete19-dimensional binary space of free W
values allowed by the old central class equations. The function
is quadratic. Exactly408 of524288 W values survive, including0.
Thus W0 is a useful admissible simplification, not a necessary
consequence of the ordinary norm equations. The certificate
includes every quadratic coefficient and64 independent direct-
group-law polarization checks. It is saved under work_CE.

The W0 simplification means that the positive action on every
functorial free-cusp-only quotient can be literal identity, paired
with the unchanged nonfree old action over C. The corresponding
negative action is the actual canonical source c, so its square
is automatically one. The next task is therefore the prescribed
commuting s-reflection: combine the lower T and ordinary Z frame
coordinates and solve the four UT4 residues, retaining actual
source comparisons. Homogeneous T/Z/U frame corrections have
zero A-coordinate, so this next correction system is linear.

Still open at this research stage: the simultaneous full20-chief
normalizer gate for the adjusted data; the complete actual scalar
refinement above that quotient (at least C2^8 is attained); its
framed action and norm lifting; cofinality; and full order two.
