# Exact quartic CM inclusion and the two norm characters

This note supplements the frozen, independently audited
`BC_hyperelliptic_CM_comparison.md`. It supplies the order-four inclusion,
the unique full accessory frame, and the exact rigidity comparison requested
for E.64. It does not evaluate the remaining full-GT orbifold discrepancy.

## 1. Literal quartic subgroup

In `B4=<a,b,c>`, put

```
d=abc,       y=b^-1 d^2 b,       x=(yd)^-1,       z4=d^4.
```

The Ferrari fold is `q(a)=q(c)=a`, `q(b)=b`; write `s=aba` in its
target. Its kernel is the already specified free group
`K=<xi1,xi2>`, with `xi1=ca^-1` and
`xi2=aba c^-1 b^-1 a^-1`. The exact words are

```
y^2=d^4,             q(d)=s,       q(y)=s^2,       q(x)=s^-3,
k0=yd^-2=xi2^-1,     k1=dyd^-3=xi1^-1,
d xi1 d^-1=xi2^-1,   d xi2 d^-1=xi1.
```

They identify the whole subgroup, not just its homology. Indeed, let
`G4=<D,Y | Y^2=D^4>`. The maps

```
G4 -> Free(k0,k1) semidirect Z:
       D -> (1,1),    Y -> (k0,2),
alpha(k0)=k1,         alpha(k1)=k0^-1
```

and

```
k0 -> YD^-2,         k1 -> DYD^-3,        1 in Z -> D
```

are mutually inverse homomorphisms. The single relation is equivalent
to `alpha^2(k0)=k0^-1`; its conjugate gives the second generator relation,
and `alpha^4=1`. Sending `D` to `d` and `Y` to `y` is an isomorphism on
the displayed free kernels and on the infinite cyclic quotient. Therefore

```
G4 ~= q^-1(<s>).
```

The cyclic subgroup `<s>` has its full profinite topology because the
exponent sum sends `s` to three. The characteristic finite quotients of
the finitely generated free kernels give the exact completed map

```
G4hat ~= qhat^-1(overline(<s>)) inside B4hat.
```

Its centre is `<D^4>`, and its quotient by this centre is the literal
free profinite product `C4 * C2`. The kernel of
`C4 * C2 -> C4`, `D -> 1`, `Y -> 2`, is the same `Khat`. It is a
once-punctured torus group with the explicit cusp word

```
x=xi1 d^-3,
x^4 z4^3=[xi1,xi2^-1]=xi2^-1 [xi1,xi2]^-1 xi2.
```

The algebraic fourfold cover with these ramification orders is
`Y^2=X^3-X -> P1`, `t=1/X^2`, with deck generator
`(X,Y)->(-X,iY)`. The deleted origin maps to `t=0`; the other two
ramification orders are two at `t=1` and four at `t=infinity`.
Choosing the oriented orbifold generators `(x,y,d)` with product one
and deck values `(1,2,1)` identifies its group with the displayed
triangle quotient. The literal braid inclusion above fixes the ensuing
Ferrari basis; no unnamed equality with a differently framed NTY II
map is asserted.

## 2. The unique full order-four frame

Let `F` be a full GT element of multiplier one, and use the standard
braid automorphisms `Phi3_F,Phi4_F`. The E.1 positive harmonic frame
`beta_F` satisfies the exact lifted equation

```
Phi3_F(s)=beta_F s beta_F^-1.
```

The full periodic-braid conjugacy theorem E.39 supplies a conjugator
`H` with `Phi4_F(d)=H d H^-1`. Apply `q`. Since the centralizer of `s`
in `B3hat` is `overline(<s>)`, there is a unique `a in Zhat` such that
`q(H)=beta_F s^a`. Replacing `H` by `H d^-a` retains its conjugacy
equation and gives the exact projection `q(H)=beta_F`. Thus

```
H_F=j(beta_F) k_F,       k_F in Khat,
Phi4_F(d)=H_F d H_F^-1.
```

This frame is unique. For completeness, `B3hat/<z3>=C2 * C3`, and the
factor-centralizer theorem of Herfort--Ribes gives the centralizer of
the image of `s` as `C2`. Its preimage is precisely `<s>` because
`z3=s^2`. In the quartic subgroup, a member of `Khat` centralizing `d`
maps to the intersection of the `C4` factor with the kernel of
`C4*C2 -> C4`, which is trivial. It then belongs to `<d^4>` and to
`Khat`; their intersection is trivial because `q(d^4)=s^4` has infinite
profinite order. Hence `C_Khat(d)=1`, proving uniqueness.

All choices are continuous. For example, the conjugation map from
the compact set of frames with prescribed projection to its orbit is
a continuous bijection and therefore a homeomorphism. Uniqueness also
gives

```
H_(FG)=Phi4_F(H_G) H_F.
```

Consequently `Inn(H_F^-1) Phi4_F` restricts to an actual group action
on `G4hat`, fixing `d` and `z4` literally. On `Khat^ab` its matrix is
`Q(beta_F)^-1 M_F`: the factor `k_F` is an inner automorphism of `Khat`
and has zero homology action. This constructs the harmonic CM action
from full braid automorphisms with a unique full frame.

## 3. Exact integral rigidity and the positive signs

In the ordered Ferrari basis `(xi1,xi2)`, write

```
U=[[1,1],[0,1]],    L=[[1,0],[-1,1]],
Rplus=UL=[[0,1],[-1,1]],
S=ULU=[[0,1],[-1,0]].
```

The standard modular positive order-three matrix in E.1 is
`Rminus=-Rplus`; its centralizer is identical to that of `Rplus`.
The first-three-strand centre acts by `Rplus^3=-I`, while the total
four-strand centre acts trivially on `K`.

Let `M_F` be the actual Ferrari homology matrix of `Phi4_F`. It has
first column `e1` and commutes with `U`, so

```
M_F=[[1,t_F],[0,1]] with t_F in Zhat.
```

Here `Phi4_F(xi1)=e^-1 xi1 e`, where `e=f(z3,c^2)`. Both arguments
commute with `a`, so `e` does also, and `q(e)=f(z3,a^2)=1`. This
justifies the first column before passing to homology. Covariance
with `b` is the exact integral equation

```
M_F L M_F^-1 = Q(f)^-1 L Q(f).
```

There is a unique matrix `V` over any commutative coefficient ring
with these covariance equations, commuting with `U` and fixing
`e1`. Indeed, two such matrices have quotient commuting with `U`
and `L`. For `A=[[a,b],[c,d]]`, the two differences are

```
AU-UA=[[-c,a-d],[0,c]],
AL-LA=[[-b,0],[a-d,b]].
```

Thus the joint centralizer is the scalar matrices over that ring;
fixing `e1` makes the scalar one. In particular the signed
congruence-rigidity shear with this same covariance is exactly
`V_F=M_F` over every `Z_l` and over `Zhat`. This is an actual
integral comparison, rather than an identification only modulo 12.

For the E.61 convention, put `t=8 rho`. Its literal matrix is

```
F_rho=[[1,-t],[-t,1+t^2]],       V=U^t.
```

Then, as integer matrix identities,

```
V L V^-1=F_rho^-1 L F_rho,
V S V^-1=S F_rho,
V Rminus V^-1=F_rho^-1 Rminus.
```

E.61 reduces these identities modulo 12 for every normalized gentle
pair. For full GT the actual integral shear above reduces to this
one, with this precise orientation.

The two actual multiplier-one characters are

```
C3(F)=Q(A_F)^-1 M_F in Cent(Rplus),
C2(F)=Q(beta_F)^-1 M_F in Cent(S).
```

The first is the normalized Mordell action of the frozen note; the
second is the uniquely framed quartic action in Section 2. Their
cocycle equations and semidirect covariance prove multiplicativity.
Their determinants are one. Over every commutative ring,

```
Cent(Rplus)={aI+bRplus},  det=a^2+ab+b^2,
Cent(S)={aI+bS},         det=a^2+b^2.
```

They are therefore characters into the specified commutative norm-one
groups. On the E.1 CM matrix fibre, `q12(f)=I` and the preceding
rigidity calculation gives `M_F=I mod3`. The positive matrices are
exactly `T=C3(F) mod3` and `W=C2(F) mod3`. The first bit is the sign
of `T` on `(1,-1)`; the second is zero for `W=+/-I` and one for
`W=+/-S`. The program prints all six Eisenstein and all four Gaussian
values with these bits.

## 4. The original orbifold actions and the unevaluated comparison

For either triangle quotient, the original two-generator GT action
is the quotient of the specified action on the three puncture loops.
For the quartic triangle `(x,y,d)` it has the literal lift to `G4hat`

```
Omega4_F(x)=x^lambda,
Omega4_F(y)=f(y,x) y^lambda f(x,y),
Omega4_F(d)=x^m f(d,x) d^lambda f(x,d) x^-m,
 m=(lambda-1)/2.
```

The quotient product relation holds by the gentle equation. Any
product discrepancy upstairs is a power of `z4`; the homomorphism
`G4hat -> Zhat`, with `(d,y,x)->(1,2,-3)`, makes that power zero.
The relation `y^2=d^4=z4` is preserved because both sides map to
`z4^lambda`. The inverse pair and the same uniqueness argument prove
an actual action, including its composition law. This records all
central carries and does not replace an orbifold action by a braid
action.

At multiplier one its matrix `B4_F` on `Khat^ab` commutes with `S`.
Its determinant is one: the exact cusp word of Section 1 is fixed,
and its image in the second lower-central quotient is a primitive
commutator. Thus

```
D4(F)=C2(F) B4_F^-1
```

is a continuous character into the same Gaussian norm-one group.
The frozen note analogously defines
`D3(F)=C3(F) B3_F^-1`, where `B3_F` is the NTY Proposition 4.4
triangle Tate matrix. These are specified homomorphisms whose values
on all of full GT have not been evaluated here.

One strengthening of the already opened Galois comparison is exact
at group level. On a Galois element of multiplier one, NTY III
Propositions 4.11--4.13 give `u_sigma=A_sigma z3^rho_K`. Since
`z3=(ab)^3=theta(u^3)`, the Mordell discrepancy is

```
Psi_sigma Omega_sigma^-1=Inn(u^(3 rho_K(sigma))).
```

Its homology is therefore `D3(sigma)=(-I)^rho_K(sigma)`. No
extension of this evaluated formula to an arbitrary full-GT element
is used. The new quartic construction has not silently adopted the
basepoint path of the inaccessible NTY II source.

## 5. Certificate and scope

The authoritative new program is `code/bc_cm_norm_characters.py`,
with `.json` and `.out` outputs. It imports only the frozen faithful
Artin and integer-matrix helpers in `bc_hyperelliptic_sewing.py`.
It verifies 14 literal braid equations, the independent free-by-cyclic
presentation, all centralizer equations over `Z/m` for `2<=m<=12`,
the two positive CM tables, and the signed covariance identities.
The proof over general coefficient rings is the displayed coefficient
calculation, not an extrapolation from the finite checks.

The Herfort--Ribes input is their *Torsion elements and centralizers in
free products of profinite groups*, J. reine angew. Math. 358 (1985),
155--161, Theorem B in the introduction and Theorem B' in Section 4,
printed page 159. Root and two peers independently opened the primary
full text during the E.58 audit. The periodic-braid input is the
already accepted E.39 with its exact based full profinite conclusion.
No new all-GT sewing equality is imported from an outer naturality
statement.
