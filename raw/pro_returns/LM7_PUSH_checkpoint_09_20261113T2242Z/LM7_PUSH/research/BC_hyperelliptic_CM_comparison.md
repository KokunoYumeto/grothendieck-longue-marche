# Exact low-genus braid descent and the two CM frames

This is new E.3 research after the E.61 freeze. It does not change the
accepted status of E.3. Every action below is an actual group
homomorphism or automorphism; the final comparison records the specific
map whose value is not determined here.

## 1. Sources and the two printed proof issues

The current Boggi source is *Automorphisms of profinite mapping class
groups*, arXiv:2011.15075v6, 22 April 2026, 53 pages. Its saved PDF is
`research/Boggi_v6_source/2011.15075v6.pdf`, SHA256
`bb7ffec85e6dd42407cf0a8f6b7cba398af912c453cdbf283810ea88b536c146`.
The complete primary-source audit of the annular-complement embedding,
outer comparison cocycle, Proposition 6.9 capping image and Lemma 6.16
twist ambiguity is preserved in `DE_Boggi_v6_morphisms.md`.

For precision, the capping map from a one-boundary hyperelliptic surface
retains its chosen Weierstrass point. Its image in the full closed
hyperelliptic group has index `2g+2`. In genus two, the displayed
`B5/<z5^2>` has abelianization `Z/40`, whereas the full hyperelliptic
presentation below has abelianization `Z/10`. The actual inclusion into
the full group is the branch-point stabilizer inclusion. This proves the
typing defect of that capping arrow, without asserting that the theorem
it is used to prove is false.

For Lemma 6.16, the identity and conjugation by `tau_gamma_i` agree on
the oriented multicurve stabilizer, where that twist is central, and
differ on a twist meeting `gamma_i` once in the larger group. On the
corresponding rank-two homology quotient the latter discrepancy is
already `U L U^-1 != L`. The primary cited Boggi--Funar Theorem 4.14
assumes an open subgroup of the whole group. The oriented curve
stabilizer is not open there. The concrete inner alternatives glue to
`Inn(product tau_gamma_i^a_i)`; no assertion that these exhaust all
alternatives is made here.

The replacement presentation used below is Endo--Kamada, *Counting
Dirac braid relators and hyperelliptic Lefschetz fibrations*,
[arXiv:1508.07687v2](https://arxiv.org/pdf/1508.07687), 5 October 2016,
Theorems 3.2--3.3, printed pages 6--7. The theorem gives the full
Birman--Hilden hyperelliptic presentation and identifies its central
involution. The paper composes mapping classes on the right. At the
presentation level the identity on its positive generators is the
isomorphism from its displayed Artin presentation to ours: the defining
braid, palindromic, central and power relations are exactly the displayed
relations below. No reversal of a partially specified geometric path is
being used.

The standard GT braid action is Nakamura--Schneps,
[author PDF](https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf),
formula (1.1), author pages 2--3. The complete NTY III primary PDF is
saved in `research/NTYIII_source/NTYIII.pdf`, SHA256
`a2b7ad812611ba4a1fad113191360552cb31b66671a743868eaa2378b215cbe7`.
The words used in Sections 4--6 below are Notation 3.9, Lemma 4.6,
formula (4.15), and Propositions 4.11--4.13 of that paper.

## 2. The full hyperelliptic presentation is preserved explicitly

Write `B_n=<sigma_1,...,sigma_(n-1)>`, with

```
delta_n = sigma_1 ... sigma_(n-1),
z_n = delta_n^n,
W_n = sigma_1 ... sigma_(n-2) sigma_(n-1)^2 sigma_(n-2) ... sigma_1,
z_first = (sigma_1 ... sigma_(n-2))^(n-1),
z_last  = (sigma_2 ... sigma_(n-1))^(n-1).
```

The exact discrete braid identities are

```
z_last = delta_n z_first delta_n^-1,
W_n = z_n z_last^-1.
```

For `g>=2` and `n=2g+2`, the full hyperelliptic group is the quotient of `B_n`
by `z_n=1`, `W_n^2=1`, and `[W_n,sigma_i]=1`. The source theorem
uses only the last relation for `i=1`; adding all its conjugate
consequences gives the same quotient. The kernel of the induced map
to the full sphere mapping class group is the order-two group generated
by `W_n`.

Let `Phi_n` be the actual standard GT automorphism for `(lambda,f)`.
It restricts literally to `Phi_(n-1)` on the first `n-1` strands and
sends `z_k` to `z_k^lambda`. Put

```
u_n = Phi_n(delta_n) delta_n^-1.
```

Then the two identities above give the exact equation

```
Phi_n(W_n) = u_n W_n^lambda u_n^-1.
```

Consequently all the hyperelliptic relators vanish after applying
`Phi_n` and projecting to the hyperelliptic quotient. Applying the
same argument to the inverse GT element proves equality of the closed
relator kernels. Thus `Phi_n` induces an actual automorphism of the
full profinite hyperelliptic group. It fixes its deck involution since
`lambda` is odd, and the further quotient is the standard full
genus-zero mapping-class action. These statements prove this descent
directly and do not use the incorrect capping identification.

The comparison of presentations with completion is exact: the
profinite completion of a finitely presented discrete quotient is the
quotient of the completion by the closed normal closure of the stated
relators. This follows by comparing their finite quotient functors.

## 3. The selected genus-two self-sewing map

For the two-boundary torus, the standard three-chain presentation is

```
Mod(S_1^2) = B4 x <d>,
delta_1 = d,       delta_2 = z4 d^-1.
```

Here the first three positive chain twists are the literal `B4`
generators and the three-chain relation is `z4=delta_1 delta_2`.
The Birman--Hilden comparison, also stated in Margalit--Winarski,
*The Birman--Hilden theory*, Section 6, gives this group and its
boundary-twist factor. Gluing the two boundary circles by an annulus
sends both boundary twists to the core twist `t`. Its kernel is
generated by `delta_1 delta_2^-1`. The resulting oriented nonseparating
curve stabilizer has the exact presentation

```
G_gamma = (Bhat4 x Zhat)/<(z4,-2)>,     t^2=z4.
```

It is the oriented stabilizer: exchanging the two sides of the cut is
not included in this specified map. The kernel statement is obtained
by cutting a homeomorphism that preserves the oriented core; the only
ambiguity is an integer twist on the gluing annulus. For the full
profinite comparison, use the actual stabilizer exact sequence in
Boggi v6 Theorem 2.3 and the genus-at-most-two congruence comparison in
Proposition 2.6(i). The displayed abstract completed group has quotient
`Bhat4/<z4>=P Gammahat_(1,2)` after killing `t`. Its central `t` is
an injected `Zhat`: the homomorphism `(b,a) -> exp(b)+6a` annihilates
`(z4,-2)` and sends `t` to six. The map to the actual oriented
stabilizer is the identity on this inertia and on the indicated
cut-surface quotient. The two exact sequences therefore identify the
completed groups. This supplies the required intrinsic-topology
comparison rather than presuming that every infinite-index subgroup
has its full profinite topology.

In the genus-two presentation of Section 2, take `t=T5` and the first
three chain twists `T1,T2,T3`. Their subsurface is the displayed
two-boundary torus. Thus the actual three-chain relation gives

```
(T1 T2 T3)^4 = T5^2.
```

The first-five-strand full twist `z5=(T1 T2 T3 T4)^5` is the
hyperelliptic involution: its image on the six-point sphere is the
twist about the disk containing five points, hence is trivial; its
homology action is `-I`, so it is the nontrivial element of the
specified order-two kernel. Therefore the standard GT formula at
`T5` has trivial conjugating evaluation `f(z5,T5^2)`, giving
`Phi_6(T5)=T5^lambda`. The restriction on `T1,T2,T3` is literally
`Phi_4`. This proves the commuting sewing square with the explicit
action `(b,d^a) -> (Phi_4(b),d^(lambda a))`; no outer comparison
element is inserted in this square.

The integral symplectic certificate checks the three-chain homology
identity, `z5=-I`, `z6=I`, and `W6=-I`. It does not substitute a
homology check for the preceding full-group cutting and chain maps.

## 4. The actual Mordell braid inclusion

Use `B3=<u,v>` as the source and `B4=<a,b,c>` as target. Define

```
theta(u)=ab,                  theta(v)=b^-1 c b a,
xi_+ = ab,
xi_+2 = b^-1 a^-1 b^-1 a^-1 b^-1 c^-1,
xi_+3 = cbab,
xi_1 = ca^-1,                xi_2 = aba c^-1 b^-1 a^-1.
```

The exact word identities are

```
theta(uv)=xi_+3,       theta(uvu)=xi_+2^-1,
theta((uv)^3)=z4,
xi_+ xi_+2 xi_+3=1,   xi_+2^2=z4^-1,   xi_+3^3=z4.
```

They prove the Artin relation, with all centre signs retained.
Let `q:B4 -> B3=<a,b>` be the Ferrari fold `a,c -> a`, `b -> b`,
and `j` its first-three-strand section. Its kernel is the free group
`K=<xi_1,xi_2>`, with the literal Nielsen actions

```
a: xi_1 -> xi_1,          xi_2 -> xi_2 xi_1,
b: xi_1 -> xi_1 xi_2^-1,  xi_2 -> xi_2.
```

Both `q theta(u)` and `q theta(v)` are `r=ab`. The derived subgroup
of the source `B3` is free on

```
k1=(uv)u^-2,
k2=u^4(uv)(uv)^-3.
```

Their images are exactly `xi_1,xi_2`, with no central factor. The
second source word differs from the triangle word `u^4(uv)` by the
specified source centre. It is necessary to keep that factor before
passing to the quotient by the centre.

It follows that

```
theta:B3 -> q^-1(<ab>)
```

is an isomorphism: it is an isomorphism on the displayed free kernels
and on the infinite cyclic quotients. In particular the Mordell
triangle subgroup is its quotient by the centre, whose image is
`z4`, exactly as in NTY III Lemma 4.6.

This comparison remains an isomorphism in the full profinite groups.
For a split extension `K rt B3` with finitely generated free kernel
`K`, characteristic finite-index subgroups of `K` and the finite
actions on their quotients construct finite quotient extensions.
They prove that the full profinite topology on `K` is induced by
`B4`. The section splits the quotient, so
`Bhat4=Khat rt Bhat3`. The closure of `<ab>` is `Zhat`, since its
exponent sum is two and multiplication by two on `Zhat` is injective.
Likewise `B3=B3' rt <u>` completes to `Bhat3=Khat rt Zhat`.
Consequently

```
theta_hat:Bhat3 ~= q_hat^-1(overline(<ab>))
```

is an actual topological isomorphism, not just a discrete inclusion.

## 5. The induced second B3 action, with unique full frames

Restrict now to multiplier one. Write `Phi_3,Phi_4` for the
standard actions of a full GT element `F`. In `B3/<z3>` use

```
s=aba,    r=ab,    tau=sr=a^-1,
x=a^2,    y=b^2.
```

The equality for `tau` is in the central quotient. In `B3` itself
`sr=z3 a^-1`; this centre factor must not be dropped in a lifted
equation. Let `A_F,beta_F` be the unique pure frames of E.1/E.58.
Evaluate them in the free complement `<a^2,b^2>` inside `Bhat3`.
Then

```
Phi_3(r)=A_F r A_F^-1,
Phi_3(s)=beta_F s beta_F^-1.
```

They first hold modulo the centre by the normalized gentle action.
Their full exponent sums are equal on the two sides; since `z3`
has exponent sum six, the possible central power is zero. Thus these
are equalities in `Bhat3` itself.

The Ferrari fold and its section are equivariant on generators:
`q Phi_4=Phi_3 q` and `Phi_4 j=j Phi_3`. Hence the following is a
fully specified actual automorphism:

```
Psi_F = theta_hat^-1 Inn(A_F^-1) Phi_4 theta_hat : Bhat3 -> Bhat3.
```

It fixes `u` and the source centre `(uv)^3` literally. The frame
identity

```
A_(FG)=Phi_3,F(A_G) A_F
```

follows from full pure-frame uniqueness, so `F -> Psi_F` is a group
action. Its difference from the original standard braid action is
the actual automorphism

```
Delta_F^br = Psi_F Phi_3,F^-1.
```

It fixes `u` and the source centre. This is the exact second-action
comparison requested for the low-genus route; no equality of the two
actions has been imposed.

There is a third specified action to retain. The quotient
`F2 -> Delta(infinity,2,3)` sends the original puncture loops to
`x=u`, `y=(uvu)^-1`, `z=uv`, modulo the source centre. It gives the
NTY action (4.2), which is an actual action for every full gentle
pair. Its lift to `Bhat3`, denoted `Omega_F`, is

```
Omega_F(u)=u^lambda,
Omega_F(y)=f(y,u) y^lambda f(u,y),
Omega_F(z)=u^((lambda-1)/2) f(z,u) z^lambda
             f(u,z) u^((1-lambda)/2).
```

The product is one modulo the centre by the gentle relation; its
exponent sum is zero, so it is exactly one in `Bhat3`. The two
central power relations have the same argument, and the inverse
gentle pair supplies the inverse automorphism. Its centre action is
`z3 -> z3^lambda`. These facts also prove the composition law of the
lifts: two possible compositions agree modulo the centre and on
the exponent sums of both generators, so agree exactly.

Thus the exact NTY comparison is

```
Delta_F^orb = Psi_F Omega_F^-1.
```

The original standard `Phi_3` and the orbifold `Omega_F` are separate
specified homomorphisms. Identifying them without their comparison
would discard the genus-zero finite-cover/basepoint issue. This note
does not make that identification.

## 6. Integral homology, both positive CM frames, and central carries

In the ordered Ferrari basis `(xi_1,xi_2)` put

```
U=[[1,1],[0,1]],   L=[[1,0],[-1,1]],
R=UL=[[0,1],[-1,1]],    S=ULU=[[0,1],[-1,0]].
```

Let `M_F` be the actual action of `Phi_4` on `Khat^ab`. Its first
column is `(1,0)^t`, since
`Phi_4(xi_1)=e^-1 xi_1 e`, where `e=f(z3,c^2)` belongs to `Khat`.
It commutes with `U`, since `Phi_4(a)=a`. Therefore

```
M_F=[[1,t_F],[0,1]]
```

for a uniquely defined integral `t_F in Zhat`. This derivation uses
the actual automorphism, not a Galois formula for `t_F`.

Write `Q` for the literal matrix action of the first `B3` on this
basis. The two normalized homology actions are

```
C3(F)=Q(A_F)^-1 M_F,     C2(F)=Q(beta_F)^-1 M_F.
```

They commute respectively with `R` and `S`. Each is a representation
of the multiplier-one GT group, by the frame cocycle and the actual
semidirect-product covariance. Their determinants are one. The two
centralizers have the exact integral descriptions

```
Cent(R)={a I+b R},    det(a I+b R)=a^2+ab+b^2,
Cent(S)={a I+b S},    det(a I+b S)=a^2+b^2.
```

These formulas hold over every `Z/m` and hence over `Zhat`: solve
the four entry equations, or use that `(e1,R e1)` and `(e1,S e1)`
are unimodular bases. Thus the two representations are actual
commutative norm-one characters with their specified bases.

E.61 and the covariance with `b` show
`t_F=8 rho_frame(F) mod 12`. Indeed
`Q(f) M_F` centralizes `L`; its upper-right entry is
`t_F-8 rho_frame`, since E.61 gives the upper-left entry one.
On the E.1 CM matrix fibre, `q Phi=q`; in particular `q(f)=1`,
so `rho_frame=0 mod3` and `M_F=I mod3`. Consequently the two
positive E.1 coordinates are exactly

```
T=C3(F) mod3=Q(A_F)^-1 mod3,
W=C2(F) mod3=Q(beta_F)^-1 mod3.
```

The first CM bit is the sign of `T` on the line generated by
`(1,-1)^t`; the second is zero for `W=+/-I` and one for
`W=+/-S`. This is exactly the saved E.1 convention, not a sign
assignment through an unspecified isomorphic field.

All centres in this comparison remain distinct and typed. The
source centre of `theta` maps to the total centre `z4`, which acts
trivially on `K`. The first-three-strand centre `z3` is not central
in `B4`; it acts on `K^ab` as `R^3=-I`, and the exact word identity is

```
[xi_1,xi_2] = z4 z3^-2.
```

In NTY III the harmonic accessory is `g_F=beta_F^-1`, while the
equianharmonic accessory is `h_F=A_F^-1`, in the common projective
normalization. For an actual Galois element of multiplier one, its
specified path in Proposition 4.11 is

```
u_sigma = h_sigma(a^2,b^2)^-1 (ab)^(3 rho_K(sigma))
        = A_sigma z3^(rho_K(sigma)).
```

The added factor changes the action on `K^ab` by
`(-I)^(rho_K(sigma))`. This is the centre sign retained in
Theorem 4.16; it does not disappear from the based Tate comparison.
If `B_F` denotes the original triangle Tate matrix of NTY
Proposition 4.4, the actual matrix of `Delta_F^orb` is

```
D_F = Q(A_F)^-1 M_F B_F^-1.
```

Both factors commute with `R` and have determinant one, so `D_F`
is a continuous character into the displayed Eisenstein norm-one
group. On the Galois subgroup of multiplier one, the opened NTY
comparison gives `D_sigma=(-I)^(rho_K(sigma))`. Its value on the
entire full GT source is not evaluated here. The precise based
equation, rather than an assertion of outer naturality, is the
remaining transfer for this route.

## 7. Certificate, search scope, and retained attempts

`code/bc_hyperelliptic_sewing.py` uses an independent, rank-variable
faithful Artin word evaluator. It verifies the exact full-twist
factorizations for `n=3,4,6`, the CM inclusion and its two free-kernel
basis words, and the Ferrari fold. Its separate integer-matrix part
checks all five genus-two transvections and the stated central signs.
The outputs are `.json` and `.out` with the same prefix. It writes no
accepted E.61 input or output.

The initial note and the initial passing certificate are retained as
`BC_hyperelliptic_CM_comparison_initial.md` and
`bc_hyperelliptic_sewing_initial.{py,json,out}` in this research
directory. The subsequent revision restricts the closed hyperelliptic
statement to genus at least two (the only closed case used here),
spells out the full profinite oriented-stabilizer comparison, and adds
the literal Ferrari Nielsen and central-boundary word checks.

The author-index route for NTY II and the attempted AMS chapter URL
were inaccessible through the search tool in this session; no theorem
from either inaccessible page is used. The current computations use
the opened NTY III source and the literal maps proved above. The
stronger but unproved equation equating the three actions has not been
substituted into any finite test or registered result.
