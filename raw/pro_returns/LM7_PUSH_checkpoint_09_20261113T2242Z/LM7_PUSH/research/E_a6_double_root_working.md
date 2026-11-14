# Literal central double cover of the retained A6 Ferrari quotient

This note records completed cover and target-model facts and the exact
ongoing source computation. It does not yet assert a whole CM fibre result.
The reserved future statement number is E.63.

## The actual finite cover

The field is F9=F3[t]/(t²+1), with a+bt encoded by a+3b. The program
`e_a6_double_cover_root.py` enumerates all6561 two-by-two matrices and
the720 determinant-one matrices U. Its centre is exactly {I,-I}.
The first retained projective (2,3,5) pair generates a subgroup of
order60 in U/{I,-I}; its two actual lifts generate a subgroup of
order120 in U. The six left cosets of that subgroup give a literal
permutation homomorphism q:U→A6. All720² products agree under q with
the previously retained six-point A6 table, and every fibre has size2.

The normal closure of one specified generator commutator is all of U,
so U is perfect. A retained48-letter commutator-conjugate word equals
-I. Every one of the1440 actual automorphisms of A6 lifts to U:
all four central changes of the two generator images are tested against
all Cayley edges. The complete1440² composition check uses their two
generator values. The lift is unique. Indeed an automorphism inducing
identity on U/Z(U) has the form g↦g c(g), with c:U→Z(U) a homomorphism;
perfectness makes c trivial. The enumeration therefore identifies the
specified Aut(U)→Aut(A6) map as an isomorphism. Every lift fixes -I.

The cover program executed in44.570seconds. The arithmetic agent read
the entire program and independently reran it in an isolated directory
in42.895seconds. Every mathematical JSON field and every NPZ array
agreed, with all six original protected files unchanged. Root has read
that replay wrapper and its final result.

## Every free epikernel and the exact free image

Retain the53 old epikernel representatives (gbar_j,hbar_j) and choose
their saved q-lifts (g_j,h_j). Let L be the free group on xi1,xi2 and
let J be the image of its displayed map to U^53. The old complete
A6 epikernel and simplicity calculation proves q(J)=A6^53.
Thus J Z(U)^53=U^53. The equality

    U^53=[U^53,U^53]=[J Z(U)^53,J Z(U)^53]=[J,J] ≤ J

proves that this actual image is all of U^53. Adjoin the ordinary
two exponent characters L→F2². The common quotient of the perfect
U^53 and the abelian F2² is trivial, so the actual joint image is
U^53×F2².

Every one of the four central changes of each pair generates U by the
same perfectness argument. Two changes over a fixed A6 representative
have the same epikernel only when an automorphism of U identifies them.
Its induced A6 automorphism fixes a generating pair and is identity;
uniqueness of the lift then makes the U automorphism identity. Hence
all four kernels are distinct. A generating pair of U projects to a
generating pair of A6, so this accounts for every epikernel,212 in total.
The map recording all their word values is expressed exactly by

    w(z^a g_j,z^b h_j)=z^(a ab_x(w)+b ab_y(w)) w(g_j,h_j), z=-I.

## The complete Ferrari holomorph

Write an automorphism of the recorded free image as (p,alpha,E,M),
acting by

    (k,v) ↦ ((z^(E_j v) alpha_j(k_(p(j))))_j, Mv).

Here p permutes53 factors, alpha_j is one of the1440 actual lifted
automorphisms, E is53×2 overF2, and M is inGL2(F2). A translated
holomorph element also has k∈U^53 and t∈F2². For two elements
(p,alpha,E,M,k,t) and (q,beta,D,N,l,u) the exact product is

    (q∘p, alpha beta[p], E N+D[p], MN,
     k z^(E u) alpha(l[p]), t+M u).

This is the law implemented in `e_a6_double_model_root.py`; it is
derived by composing the displayed automorphisms and translations.
The Nielsen a,b values implement (g,h)↦(g,hg),(gh^-1,h), including
their actual central differences from the chosen representative lifts.
The free generators are (g_j,e1),(h_j,e2), and c=xi1 a. All braid
relations and literal Ferrari recoveries are checked.

The exact projections are

    (p,alpha,E,M,k,t) ↦ (p,Inn(q(k)) alpha,alpha)
    (p,alpha,E,M,k,t) ↦ (M,t).

The common ambient kernel is F2^159, comprising53 central k
coordinates and106 E coordinates. The program checks every pair
of159 kernel basis elements, all generator conjugation laws, all
212 lift pairs,1000 successive braid-word projections and100
ambient associativity/inverse controls. It executed in1.387seconds.
An independent isolated replay completed in1.355seconds, with every
mathematical JSON field and NPZ array equal. Root read the wrapper
and result; both agents' complete algebraic reads passed.

## Exact source restriction and its current calculation

The six specified pure evaluation pairs have affine-two image identity.
The preparation program checks all twelve generator values explicitly.
The entire image of each free evaluation therefore lies in M=I,t=0.
All36 induced blocks inherit that restriction. Substitution into the
proved full product law gives exactly

    (p,alpha,E,k)(q,beta,D,l)
       =(q∘p,alpha beta[p],E+D[p],k alpha(l[p])).

Packing E_j into a two-bit integer is a bijection F2²→{0,1,2,3};
its addition is XOR. The new C++ collector uses this exact restriction.
The preparation program compares192 operation-DAG values with the
full271-coordinate Python law and577 ambient-kernel/conjugation values.
All source projections reproduce the unchanged9462-point A6 action,
including its saved orbit-compression and point-order maps. The full
source calculation uses the unchanged complete A6 certificate, with
865049 final Schreier relations. The only inherited collector changes
are coefficient type names and labels; the separately saved binary
model contains the exact multiplication and inverse formulas above.

At the time of this entry the full relation enumeration is still running.
It has found128 independent kernel words, with the remaining relations
still being checked. This is not recorded here as a completed kernel
dimension. The independent word-replay program and central-coinvariant
presentation programs have been written for the subsequent checks.

## Completed source kernel and central presentation

The preceding running status is retained as its original historical entry.
The complete source enumeration subsequently finished in482.069seconds:
all865049 lifted relations and the normal closure give exactlyF2^128.
The separate full271-coordinate Python replay verified all128 literal
basis words in both the actual source and the unchanged A6 base, all256
normality conjugations, and all ten C lifts. It completed in23.566seconds.
The exact C,H,B commutator ranks on the kernel are98,98,118.
Both x and y have order dividing120, and the old ordinary quotient already
has abelianization(C120)^2. Thus the new whole kernel lies in the actual
F-prime image, with that ordinary quotient unchanged through its map.

For the full preimage E of C, the C coinvariant kernel has dimension30.
The ten original C lifts and those thirty central generators give40
abelian columns. All ten original-to-normal-form relations and all720615
complete C Schreier relations were evaluated in355.696seconds. Their
rank is37, with rank ten in the original-generator exponent columns.
The independent replay of all37 retained relation words, their10849
required ancestors, both actual maps, and their exponent/central rows
completed in12.705seconds. Hence E_ab=F2^3 and ker(E-prime->C)=F2^125.
All300 elementary central changes of the ten lifts were retained.

The actual s,r action on E_ab is given by

    S=[[0,0,1],[0,1,0],[1,0,0]],
    R=[[0,1,0],[0,0,1],[1,0,0]].

The exact x,y source words act identically; this was checked again by
literal matrix-word substitution in the commutator replay. For the
abelian-kernel/perfect-quotient extension E, E-prime is perfect by the
proved commutator lemma used in E60. This is a claim about the displayed
actual preimage, not a factor chosen only from its order.

## Complete binary module pairing and level-twelve correction

The six saved binary module words are obtained by the exact two-stage
word-DAG substitution through the nine original F-prime words. Their
old solvable coordinates are precisely the six specified W basis vectors.
All six squares and fifteen pair commutators lie over C. Their actual
Q12 values are identity; no such assertion was imposed on the original
six words, whose Q12 identity flags are(true,false,false,false,true,false).

The exact C normal-form evaluator checked all21 queries in92.5597seconds.
An independent full-model and actual-base replay checked all9004 required
C normal-form ancestors, every residue and all ten ordinary exponents
in9.208seconds. Both the square-image rank and commutator-image rank are3.
The pairs(0,1),(0,2),(3,4) have columns

    [[0,0,1],[1,0,0],[0,1,0]],

whose determinant is1. Thus the actual W pairing reaches all three
coordinates of E_ab. The signed-source comparison still needs its own
exact map; it is not inferred from this pairing.

For the full128-dimensional kernel, exactly122 original basis words had
Q12 value identity. The remaining six indices were112,113,114,115,116,124.
The program e_a6_double_modular_basis_root.py formed277 actual relations
among the kernel basis and its B action. Selected such relations, all
independently replayed to have double-source value identity, map onto the
entire literal Q8 kernel in Q12. Dividing each original basis word by the
corresponding retained Q8 word gives128 actual Q12-identity words with
exactly the original independent binary coordinates. Every resulting
word was replayed in the full source, A6 base, and Q12 action;5177 word
ancestors suffice and the run completed in4.122seconds.

The previously proved128-dimensional upper bound and these128 corrected
words prove that the actual common source is

    G_double x_(G_A6) B0,   B0=im(B -> G_A6 x Q12),

with its full128-dimensional relative kernel. This result retains the
actual level-twelve map. The further common source with the signed G_L
model, including its two-primary solvable coordinates, remains under
calculation. The separate forty-three-column perfect-bridge calculation
has been assigned to the profinite agent; no result from it is used here
before its recorded exact replay.

## Completed signed bridge and exact common source

The preceding pending statements are preserved as historical entries.
The complete forty-three-column pullback presentation has now evaluated
all720615 C relations and all ten original-generator links. Its rank is37,
so the full pullback abelianization is F2^6. The three independent Schur
signs inject into this abelianization. Its derived group is therefore
the graph of an actual surjection D2→SL2(F5)^3 lifting the specified
C→A5^3 map. The kernel over C has dimension125 and its sign-killing
subspace has dimension122. The independent full-model replay checked
all37 relation words,10849 ancestors and330 elementary lift changes.

The actual joint X2/G_L source has binary kernel rank167 in the specified
product F2^128×F2^42, after all1154659 complete base relations and the
normal closure. Its maximum common quotient has order9331200000.
Both actual maps to the explicit900-point signed quotient have now
been proved: the G_L gate evaluates all25965 relations and has unchanged
rank44; the X2 gate evaluates all865049 relations and has unchanged
rank128. The first interrupted candidate run is preserved separately.
The completed restart and independent word replay supply the accepted
result. The quotient's actual pure image is SL2(F5)^3×(Z/30)^2.
All six induced signs, the three actual matrix transporters and their
central free-character twists are retained in these comparisons.

The full common source is consequently X2×_(tilde Q30)G_L, equivalently
X2×_(Bstar)J with Bstar=G×_(Q30)tilde Q30. Its full relative kernel
over J is F2^125. The perfect common residual maps onto the old perfect
residual with kernel F2^122. The proof uses the universal central cover
SL2(F5)^3→A5^3 to prove perfection of the new pullback, including the
commutator equality for its entire kernel.

The six actual module words have been corrected to Q12 identity without
changing their full X2 values. Their fifteen commutator values retain
the rank-three matrix recorded above. The complete proof uses these
values together with the old exact lower-central image to establish
the entire preimage in every gamma_j(Nhat), j≥2, and in
I=gamma5(Nhat) intersect R_nil(H). The actual extension of the uniform
image by the triple-cover three-group has no C2 quotient. Goursat then
retains all125 binary correction values while killing the signed,
triple-cover, uniform and nilpotent boundary coordinates.

The full E63 proof is in sections/E_a6_double_agent.tex, with both root
target fragments included. Arithmetic and root have read the complete
proof and passed it. The final authoritative manifest and independent
isolated replay are the remaining integration checks at this entry.

## Joint double- and triple-cover target

The exact target is T2×_(T0)T3 over the specified old signed-A6 target.
Its order is2^557·3^271·5^117·7^8·11^3·13^2. The relative double
kernel is F2^151. The relative triple kernel maps onto ASL2(F3) with
kernel3^105; ASL2(F3) has abelianization C3. Thus its every two-group
quotient is trivial, proving the displayed actual fibre product by
Goursat. The kernel over Sigma=S_L×ASL2(F3) is perfect: its abelianization
is a quotient of both a two-group kernel and a three-group kernel.
The actual T23 and uniform/Hurwitz target comparisons are retained
through their specified maps. The proof is in
sections/E_a6_double_triple_target_root.tex, with its exact order
certificate e_a6_double_triple_target_root.json; peer proof read passes.

## Literal comparison with the E62 source

This new comparison retains the full old11010-point A6/A5 common base
and appends the literal4764-point E62 source. Every old strong-generator
word is evaluated in both sources before seeding the complete chain.
The resulting15774-point complete base has407 strong generators and
13526 word-DAG nodes. It evaluates all1279851 final Schreier relations
and finishes in593.222seconds. The full signed/binary170-column kernel
collector is now running over this exact enlarged base.

Two earlier probes remain available with their full outputs. The six
stable ternary actions on the old binary W are all identity; the new
central pairing has rank three. The125 old-J-identity representative
words are actual N words, but only eleven have E62 values in its N-prime
image. None of the six module representatives has value there. All
fifteen pair commutators do, with their exact central E62 coordinates
retained. These probes give literal word values only. The complete
enlarged source and its required deep-domain comparison are being
computed before any simultaneous E62 correction conclusion is drawn.
