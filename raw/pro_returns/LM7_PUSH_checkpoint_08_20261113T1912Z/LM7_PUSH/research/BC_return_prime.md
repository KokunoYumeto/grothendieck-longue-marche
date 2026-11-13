# D44 infinite application audit and D46 return-prime comparison

## Audited starting point

The independently read D44.26–32 fragment had SHA-256
`7e437b360908026f758206604051b65cc1b0348f9e44b0bfd51f009c9035033d`.
The centreless extension pullback, literal tau-root equation, normalized
commutator gauge, uniqueness, converse source factorization, and maximal
pro-ell quotient comparison all passed the independent proof audit.

The integral R8 construction also passed. After an integral inner
adjustment fixing x, two group conjugators realize the prescribed leading
derivation at y and z. At each subsequent degree the error changes by
`(u,v) -> [u,y]+[v,-x-y]`, whose image is the full integral free Lie lattice.
The actual correcting factors converge in the free pro-ell topology,
because every finite ell-group kills sufficiently deep ordinary lower
central terms. The resulting special endomorphism is an automorphism by
its identity Frattini action. The closed IA outer filtration is pro-ell;
the leading map is onto and equivariant. Coprime complement conjugacy in
its kernel lifts an S3-fixed leading element to an S3-fixed outer element.
The averaging factor 1/6 is a unit for ell at least 5.

One clarification was sent to the author and root: the special outer
group has an actual peripheral-permutation map to the permutations of the
three distinct conjugacy classes x,y,z. The geometric S3 maps onto the
natural faithful S3. A centralizing outer element has trivial peripheral
permutation, because the centre of S3 is trivial. This supplies the exact
justification for choosing a representative fixing x. The arithmetic
agent owns and preserves the integrated D44 source; no D44 edit was made
by this agent.

## Preserved initial reduction, superseded by the finite result below

The first audit established the exact adjacent identity
`O^p(O^p K)=O^p K`: the quotient by the left-hand residual is an extension
of two pro-p groups. It also identified that a nonadjacent return can be
strict, and that the old D44 coprime existence argument does not establish
the return, since that new base has quotients divisible by the returning
prime. This was an unproved existence question, not a nonexistence claim.

The construction below proves a complete finite return-prime lift while
retaining the entire old infinite quotient. It does not assert a lift to
the whole return-prime completion, and does not replace the full profinite
D1/D2 problems by this family.

## Exact finite groups and maps

Take distinct primes ell,p at least 5, a=ord_p(ell), k=F_(ell^a), and an
element zeta of order p. Let N=(F_p)^ell, let c cyclically permute its
coordinates, and put P=N semidirect C_ell. On V=k^ell, N acts diagonally
with entries zeta^(n_i), and c acts by the same cyclic shift. Set
H=V semidirect P, and define the actual epimorphism from the rank-two
pure source by x -> X=(e0,c), y -> Y=(0,n0).

The ell-th power of X is the nonzero constant vector. Its P-orbit spans V.
The exact residual maps give O^ell H=V semidirect N,
O^p(O^ell H)=V, and O^ell V=1. In P the first two residuals instead give
N and 1. The cusp orders in H are ell^2,p,ell*p, and in P they are
ell,p,ell*p. The fixed-space dimensions on V are a,(ell-1)*a,0.

The source B=C2*C3 is induced through the actual six B/F cosets using
the Schreier cocycle t_i b t_j^(-1). Its actual H and P images are E and D.
The kernel E -> D is the full W=V^6: each cusp power of exponent ell*p
lies in this kernel and has a nonzero projection into the relevant
simple component. The six components have the six distinct fixed-space
profiles, so they are pairwise nonisomorphic F-modules. Their sum is
simple as a D-module because S3 permutes them transitively.

With K=O^p(O^ell F), the source map to D kills K and q_E(K)=W. The latter
is proved by the identity-coordinate residual epimorphism onto V and
the simplicity of W. Consequently the actual joint source is
J=Gamma x_D E, Gamma=B/K, and it is a quotient of B/O^ell K. Its kernel
over the entire old Gamma is the nontrivial elementary abelian W.

## Complete fibre, including ordinary centralizer freedom

The induced W fixed dimensions at s,r,tau are d/2,d/3,d/6, d=6*ell*a.
The full peripheral product map has rank d because W_D=0. For prescribed
base conjugators the set of distinct literal peripheral maps has |W|
elements. They all generate: the tau order grows from 2*ell*p to
2*ell^2*p, which excludes a complement to W. The generating stabilizer
in W is zero, so this is one free W orbit.

All three upper-to-base centralizer maps are onto. The s and r cases are
the explicit coprime cyclic calculation. For tau, the local X-centralizer
maps exactly onto <c>, while the Y and Z centralizers map onto their full
base centralizers. The identity-coordinate sum and its s-conjugate retain
both ordinary abelian mod-p characters. A pure element commuting with
tau has zero y character; hence its component in C_P(c) has zero
constant-N coordinate and belongs to <c>. The two-cycle induced
centralizer equations now lift independently in V^6. This verifies the
entire ordinary centralizer union, not only chosen conjugators.

Fixing tau leaves exactly ell^(ell*a) literal normalized maps, acted on
freely and transitively by W^tau. Prescribed whole old conjugators in
Gamma are retained by pairing them with E-conjugators having the same
D-images.

## Actual kernel preservation and retention of the whole old pair

Any normalized gentle map on Gamma induces the identity on the specified
P quotient: f has image in P' inside N, which centralizes n0. It preserves
the six-coset core and therefore induces an actual automorphism of D.

The pure peripheral source fibre F -> H over id_P is one inner orbit.
A conjugate of X over c has translation sum zeta^b, a conjugate of Y has
translation in k e0, and every lift of z is conjugate to Z. Kernel
conjugation, a constant-N scalar, and the remaining V^c conjugation send
every such pair to (X,Y). This proves preservation of ker q_H.

For a normalized generating source B -> E, the identity coordinate
F -> H has just this form. For a word in the normal core of ker q_H,
conjugate it through each of the six cosets. The changed coset
representative differs from the original one by an element of E_F;
each coordinate is therefore an inner conjugate of a zero image. This
proves preservation of the actual induced source kernel, so the map is
an automorphism of the same E.

The component automorphisms on Gamma and E agree on D and give a genuine
automorphism of Gamma x_D E. Conversely every normalized peripheral
source map above the specified old automorphism gives one of these E
maps, and so has this component factorization. The count therefore is
the full normalized fibre above the entire old map. Since [J_F,W]=W,
the new normalized f lies in J_F', and its old image is literal.
The maximal pro-ell pure quotient stays P_ell by its universal map from F.
For each conjugator image the actual profinite word fibre is the coset
of ker(F' -> J_F') recorded in D46.17.

## Authoritative new files and replay

The theorem is in `sections/D_return_prime_agent.tex`.
The model and centralizer programs are independent of the frozen E51
programs and outputs.

1. Run `bc_return_prime_model.py --ell 5 --prime 7`, redirecting stdout to
   `bc_return_prime_l5_p7.out`. It writes the matching JSON and NPZ.
2. Run `bc_return_prime_centralizers.py --ell 5 --prime 7`, redirecting to
   `bc_return_prime_l5_p7_centralizers.out`.
3. Repeat the two commands with `--ell 7 --prime 5`, using the analogous
   `bc_return_prime_l7_p5` prefix.

The only external code dependency is `de_ferrari_a6_source_data.py`, whose
read-only `load_data()` supplies the already audited literal B/F source
rewriting and its JSON dependency `de_ferrari_sl2_5_N.json`.

The model retains every new-kernel basis word and replays its image.
The centralizer program enumerates the entire quotient over the
p-translation kernel, uses every Schreier edge to obtain that kernel,
solves every top-coset centralizer equation, and lifts a complete set of
base centralizer generators. Each final ell-correction has coefficients
in the saved literal new-kernel word basis. No inaccessible abstract
quotient automorphism is substituted for a source map.

The first case has kernel dimension 180, invariant dimensions 90/60/30,
and tau orders 70/350. The actual top quotient has order 150 and its
p-translation kernel has rank 14. The complete centralizer projection
indices are all 1. Model and centralizer runtimes were 9.851s and 1.687s.

## Separate E52 independent audit

`bc_symplectic_integral_audit.py/.out/.json` is a read-only independent
audit of the root's integral symplectic probe. It reconstructs all eight
literal integral pairs, checks all 4,656 N matrices and all 240 K2
matrices, the actual theta block quotient, the standard group maps, and
all radical products. It additionally checks radical commutation with
both elementary SL2 generators. It reproduced rank 5, Smith
[1,6,6,6,6], and minor determinant 73728=2^13*3^2 in 18.933s. The root
certificate remained byte-identical throughout. Root owns E52 and its
global closure theorem.
