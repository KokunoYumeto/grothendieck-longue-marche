# Main audit and certified CM census

These files support statements A.1–A.16 and A.37–A.43. The mathematical proof
of each analytic certificate is A.37 in `sections/A_census.tex`. The programs
do not use a floating-point zero tolerance to certify an analytic rank.

## Principal outputs

| Family | Coefficient curves | Ranks 0, 1, 2 | Full ordered-pair table |
|---|---:|---|---|
| Cubic `y²=x³−432d²` | 81 | 34, 41, 6 | `a_main_cubic_pairs.csv`: 6,561 rows |
| Quartic `y²=x³+A x` | 512 | 220, 256, 36 | `a_main_quartic_pairs.csv.gz`: 262,144 rows |
| Sextic `y²=x³+B` | 2,592 | 1,136, 1,296, 160 | `a_main_sextic_pairs.csv.gz`: 6,718,464 rows |

The coefficient tables are `a_main_cubic_census.csv`,
`a_main_quartic_census.csv`, and `a_main_sextic_census.csv`. They contain the
exact conductor, root number, minimal Weierstrass model, analytic rank,
certified derivative order, enclosure, precision and truncation length.
Even-sign central zeros have a rational point of infinite order. Its
coordinates and its exact non-torsion verification are retained.

All raw exact Fourier coefficients are in the gzip JSON files under
`a_main_cubic_data/` and `a_main_cm_data/`. Each higher-derivative case also
retains its longer coefficient vector and its Taylor and infinite-tail
bounds. These are part of the proof record and should be kept with the CSVs.

## Runtime and reproduction

The run used Python, SymPy, NumPy, python-flint **0.9.0**, and PARI/GP
**2.19.1**. The official PARI source archive is
<https://pari.math.u-bordeaux.fr/pub/pari/unix/pari-2.19.1.tar.gz>.
Its SHA256 is

```text
419553b11ff8c3ecb8e9031b7d91d7cee003a5d721e685fcb499565c96fe2943
```

`a_main_fetch_pari.py` downloads and verifies that exact archive.
`a_main_pari_configure.out` and `a_main_pari_build.out` retain the build logs.
In the source directory, the configuration was `./Configure
--prefix=ABSOLUTE_PROJECT_ROOT/work/pari --without-readline --graphic=none`,
followed by `make -j4 gp`. The scripts default to
`PROJECT_ROOT/work/pari-2.19.1/gp`; the environment variable `A_MAIN_GP` may
instead identify an existing GP executable. Here `PROJECT_ROOT` is the
directory containing the `deliverable/` directory.

Run from that project root:

```bash
python deliverable/code/a_main_exact.py
python deliverable/code/a_main_quartic.py
python deliverable/code/a_main_cubic_census.py
python deliverable/code/a_main_cubic_rank2.py
python deliverable/code/a_main_cubic_pairs.py
python deliverable/code/a_main_cm_census.py quartic
python deliverable/code/a_main_cm_census.py sextic
python deliverable/code/a_main_cm_pairs.py quartic
python deliverable/code/a_main_cm_pairs.py sextic
python deliverable/code/a_main_make_rank_tables.py
python deliverable/code/a_main_verify_census.py
```

The first two commands verify the exact local counterexample, modular genus
calculations, explicit cubic and quartic maps, torsion calculations, and
quartic descent identities. The remaining commands generate the census.
The CM census resumes from an existing coefficient CSV. To recompute those
enclosures, move the corresponding completed CSV aside before running it;
the exact raw coefficient cache remains usable. The cubic first pass
rebuilds its CSV, and the following rank-two pass completes all six remaining
analytic-rank certificates. No network request is needed once GP and the
Python dependencies are installed.

The initial cubic attempt rejected a harmless GP stack-size warning. Its
log is preserved as `a_main_cubic_census_attempt1.out`; the successful
wrapper passes the stack size on the command line. This failed harness
attempt does not enter any final certificate.

## Certificate logic

For conductor `N`, put `c=2π/√N`, `r=exp(−c)`. Exact coefficients satisfy
`|a_n|≤2n`. A positive functional-equation sign gives

```text
L(1) = 2 Σ a_n r^n/n,
tail after M ≤ 4r^(M+1)/(1−r).
```

A negative sign gives an exact central zero and

```text
L′(1) = 2 Σ (a_n/n) E1(cn),
tail after M ≤ 4r^(M+1)/(c(M+1)(1−r)).
```

These are evaluated in outward-rounded 160-bit Arb balls. An interval
excluding zero proves nonvanishing directly. If the positive-sign value
is zero, an exact infinite-order rational point supplies the zero proof
through the CM rank-zero theorem. The second derivative is then enclosed
at 256 bits using the completed L-function at `1+2^−45`, an explicit
infinite tail, and a proved fourth-derivative Taylor bound. All enclosures
exclude zero at their claimed order; no rank is left undecided.

The integrity program independently counts points over the finite fields
with 11, 13, 17 and 19 elements for every coefficient curve and compares
the resulting traces with the saved Fourier coefficients. It also checks
every printed interval, every rank-two point witness, the full row order,
the exact row counts, cusp flags, point dictionaries, and mask histograms.

## Lossless CSV decompression and exact row decoding

The two `.csv.gz` files are ordinary UTF-8 CSV compressed with gzip.
They contain every pair row, not only a matrix bitmap. Decompress with a
standard gzip reader, for example:

```bash
python -c 'import gzip,shutil; shutil.copyfileobj(gzip.open("deliverable/code/a_main_sextic_pairs.csv.gz","rb"),open("deliverable/code/a_main_sextic_pairs.csv","wb"))'
```

Columns are `alpha_id,beta_id,criterion_mask,point_ids,cusp_flags`.
For exponent `m=4` or `m=6`, the representative of class identifier `i` is
`ε·2^e2·3^e3·5^e5·7^e7`, where

```text
i = ((1−ε)/2) m^4 + e2 m^3 + e3 m^2 + e5 m + e7,
0 ≤ ep < m,  ε = ±1.
```

The `*_classes.csv` dictionaries give these representatives and their
coefficient-curve ranks. The `*_join_rules.csv` dictionaries define each
criterion-mask bit. A bit is set exactly when that elliptic target has
analytic rank zero. The paper prints all coefficient ranks and the complete
join formulas, which together specify every row of the pair tables.

For a nonzero criterion mask, `point_ids` indexes the
`*_point_dictionary.csv` file. Each entry supplies its tripod value and all
four sign choices of the affine coordinates on the even cover.
The three bits of `cusp_flags` correspond to tripod cusps `0,1,∞`. Their
conditions are respectively `β=1`, `α=1`, and `β=−α` in normalized classes.
Each flag specifies two individual rational cusps. Each individual cusp
contributes its **whole** completed Kummer packet
`H¹(Q,Zhat(1))`, after choosing a tangent origin. Thus packet flags specify
infinite families of sections exactly; they are not a finite sample.

The image-packet congruences on the tripod are `[t]_m=[α]_m` at zero,
`[1−t]_m=[β]_m` at one, and `[1/t]_m=[α^−1]_m` at infinity.
The cubic CSV records its corresponding cube congruences directly.

For a readable exact expansion, run, for example:

```bash
python deliverable/code/a_main_cm_pairs.py quartic --decode 256 64
python deliverable/code/a_main_cm_pairs.py sextic --decode 1944 72
```

These expand the quartic pair `(-1,2)` and sextic pair `(-8,9)`.
The output includes every applicable target, exact ordinary coordinates,
and cusp centres. A **zero mask means unclassified by these criteria**.
An empty ordinary-point field in such a row does not assert that the curve
has no ordinary point or no Selmer section. Cusp flags remain valid known
cusps there, without an exhaustion claim.

## Scope

The complete section lists are proved for full profinite **Selmer**
sections when at least one criterion applies. They do not assert the
absence of non-geometric sections in positive-rank classes. The separate
least-conductor proof A.43 identifies `d=9`, conductor 243, as the curve
for task A.12, but does not solve the lifting questions for its profinite
Mordell–Weil parameters.

## Combined census sizes

The three coefficient dictionaries contain 81 + 512 + 2592 = **3,185** classes. The full pair tables contain 6,561 + 262,144 + 6,718,464 = **6,987,169** rows. The two compressed even-degree tables alone contain **6,980,608** rows; the cubic table contributes the other 6,561 rows.

## Quintic finite-descent target

`a_main_quintic.py` is the executed certificate for the genus-two Jacobian
`J=Jac(y²+y=x⁵)` used in A.50–A.52 to settle the maximal-prosolvable
Selmer-section question for the plus quintic. It requires the same PARI/GP
and python-flint installations as the elliptic census. Run it from any
directory with:

```bash
python deliverable/code/a_main_quintic.py
```

Set `A_MAIN_GP` to the GP executable when it is installed elsewhere. The
script reconstructs all 4,096 exact Dirichlet coefficients from direct
finite-field Euler polynomials and checks them against `lfunan`. It uses
the CM functional equation, conductor 3,125, and a Bessel inverse Mellin
transform to prove the root number is +1 from a positive certified value
of `Theta(1)`. The central value is then enclosed in

```text
L(J/Q,1) = [0.71831362842056477051660347805 +/- 2.72e-30].
```

The entire omitted tail is bounded analytically; the program does not
use a numerical analytic rank or an uncertified `lfun` value. Preserve
`a_main_quintic_gp.out` (raw exact output),
`a_main_quintic_data.json.gz` (all coefficients and Euler factors),
`a_main_quintic_certificate.json`, and `a_main_quintic.out` together.
The compressed JSON is ordinary gzip-compressed UTF-8 JSON and can be
decoded losslessly by `gzip.open(path,"rt")` and `json.load`.

The arithmetic implication uses Darmon's explicit Hilbert modular
identification and Zhang's published Theorem 4.3.2. A.50 records all
hypotheses and transparently identifies the theorem's printed reference
to Tian–Zhang as “in preparation.” This source qualification is separate
from the unconditional exact numerical certificate. The proof then
descends finite rank and finite Tate–Shafarevich group from `Q(sqrt5)` to
`Q`, determines the three rational points of the genus-two target, and
uses their cusp fibres in B.1. It concerns maximal-prosolvable **Selmer**
sections and does not assert a full-profinite lifting theorem.

`a_main_quintic_maps.py` and its executed `.out` file give the additional
exact symbolic certificate for A.53. The three cyclic quotient maps from
the plus Fermat quintic to `y²+y=x⁵` pull back the two target differentials
to all six regular plane-quintic monomials. The program checks every
curve and differential identity in the rational function field and
computes determinant 1 for the coefficient matrix. This proves a
`Q`-isogeny `Jac(X5) -> J³`; it does not assert that the isogeny degree is
one. Its rank and finite-Sha consequences supply the compact Jacobian
input for the separate first-derived-quotient argument B.26.

`a_main_quintic_inertia.py` and `.out` record the exact polynomial and
character checks for A.54. The CM conductor gives a wild-inertia
generator with primitive fifth-root eigenvalues. The integral Bezout
identity with `Phi5(1)=5` makes its difference from the identity invertible
on every prime-to-five Tate lattice. It proves that both local Jacobian
point groups over `Q5` are pro-five and that their five-adic Kummer maps
are injective. The same script checks the three geometric trace
projectors, which give `Phi Psi = Psi Phi = [5]` for the explicit isogeny
and its transpose. This arithmetic inertia input is proved in the paper;
the program certifies the exact algebra used after that input.

## Bad-prime local section

`a_main_bad_prime.py` and `.out` verify the exact local example A.55.
The point `[2:y:1]` on the plus septic over `Q7`, where `y⁷=−129`,
exists by a simple-root Hensel calculation. Its tripod Kummer pair
modulo cubes is `(2,1)` in `F3²`, outside all three cusp lines. The
program checks six successive Hensel lifts and the entire finite test.
Its section is nevertheless intrinsically ramified because inertia
permutes the geometric cusps at seven. This refutes the extension of
the good-prime cusp criterion as a purely local bad-prime principle.
It is an actual full **local** point section and does not assert a
global full-section lift.

## All exceptional primes in the natural residual quotient (A.56–A.57)

`a_main_exceptional_groups.py` enumerates SL(2,F_ell) for ell=5,7,11,13 and checks that the normal closure of a suitable q-power-order element equals the full group for every q dividing ell(ell²−1). Its output is `a_main_exceptional_groups.out`. The uniform proof is elementary and does not extrapolate from these examples.

`a_main_exceptional_twists.gp` runs the exact PARI Tate algorithm on all eight Q2 quadratic-twist classes of y²=x³−x. `a_main_exceptional_twists.out` records invariants, minimal discriminant valuation, local conductor exponent, Kodaira code, Tamagawa number and global conductor. Codes3 and−6 are III and I2*, respectively. Every local conductor exponent is5 or6. The manuscript proves why reduction modulo each coefficient prime ell≥5 preserves both tame and Swan conductor terms.

These are witnesses in an explicitly identified natural joint arithmetic quotient, with a genuine global section of that quotient. No lift to the full fundamental group is asserted.


## Rank-one tangent units and the abelian Selmer obstruction (A.59–A.60)

Run `python deliverable/code/a_main_rankone_units.py`. Its saved output is
`a_main_rankone_units.out`. It checks the conductor243 cubic
`y²+y=x³−1`, the Hessian and three-division polynomial, all flex
residue fields, and the normalized tangent units with divisor `3(d−O)`.
It also executes857 finite cyclic instances of the primary-component
step in the proof. The infinite obstruction is proved in
`sections/A_rankone_progress.tex`; no finite search is substituted for
Faltings's genus-two finiteness theorem.

A.59 proves every proper exponent lifts to the all-coefficient
cuspidally central quotient, using the opened published
Borne–Emsalem–Stix theorem. A.60 proves that the explicit exponents
`n(1−e_P)` for nonempty finite coefficient-prime sets P and nonzero
integers n have no geometrically abelian Selmer lift. The obstruction
already uses a finite toric coefficient layer above the full compact
Tate module. The distinction between an abstract lift and a locally
geometric lift is essential. No determination of all profinite
exponents or all congruence-cover lifts is claimed.


## Rank-one exponents beyond finite alterations (A.61–A.65)

The proofs in `sections/A_finiteprime.tex` exclude every noninteger exponent
which equals an integer outside a finite set of coefficient primes, for CM
elliptic curves punctured at full torsion. They give a direct CM Kummer
openness proof, exact finite entanglement control, and the product
Manin–Mumford argument. `sections/A_abelian_fibres.tex` gives the exact
abelian Selmer fibre over every rational compact point.

`sections/A_unit_exponents.tex` strengthens the result for arbitrary E/Q:
if an exponent is a unit at almost all coefficient primes, its abelian
Selmer lift exists exactly at nonzero integers, with unique point-section
fibre. This includes infinitely many changed components and uses no CM,
rank-one, primitive-generator or finite-Sha hypothesis. Finite nonempty
zero-component sets are excluded even after multiplication by an arbitrary
profinite unit, over every number field. The proof uses full proper
section-neighbourhoods, rational multiplicative completion, all boundary
unit characters, and Faltings, not a finite search.

Run `python deliverable/code/a_main_unit_covers.py` for the supplementary
exact genus-two-cover computations. The executed output is saved as
`a_main_unit_covers.out`. It checks the eight K-squareclasses, explicit
birational maps, two elliptic quotients and differential independence,
a rational norm comparison, nontorsion Prym points by exact reduction
orders, and existing rigorously certified rank data. These positive-rank
cover calculations are a diagnostic and do not supply the theorem by a
rank-zero shortcut. The direct proof settles unit exponents without
asserting finite-descent excellence for that genus-two curve. General
exponents with infinitely many nonunit components and full metabelian
fibres remain outside these results.


A.66, in `sections/A_infinite_valuations.tex`, adds a proved infinite-nonunit-support
family. With finitely many zero components, if one prime lambda divides almost
all finite coefficient valuations, Selmer lifting is possible exactly at nonzero
integers. The proof uses translated Miller units of divisor
`(P)+(Q)-(P+Q)-(O)`, ordinary lambda-th-power divisors n_j of the exponent,
formal logarithms, and finitely many genus `2*lambda-1` covers. It applies also
when lambda divides N. No new numerical computation is needed for this proof.
In particular it excludes a_p=p^r for every p and every fixed r>=2; it leaves
the valuation-one profile and infinitely many zero components outside its scope.


## Actual modular j-line comparison and finite congruence obstructions (A.67)

Run `python deliverable/code/a_main_jline_covers.py` and
`python deliverable/code/a_main_jline_at3.py`; the saved outputs have the same
stem with `.out`. The first program verifies the Hesse Weierstrass
transformation, constant nine flexes, exact genus-zero X3 map, genus4 cubic
pullback, all four projective modular groups and Fermat subgroup/cusp images,
and fibre-product genera4,46,118,343 for levels3,4,5,7. It also checks the exact
translated-unit identity used in the uniform erased-three proof. The second
program finds and exactly verifies the q61 nonsquare witness (plus five
independent additional examples).

Run `work/pari-2.19.1/gp -fq deliverable/code/a_main_jline_local3.gp` to replay
the local number-field samples. Its `.out` records the exact degree6 field,
ramification, unit valuations and local-square tests. The manuscript proves
the uniform odd-valuation identity for every n; it does not extrapolate from
the twelve displayed samples.

The convention is the modular j-tripod J=j/1728, with ramification(3,2,m).
It is not the Legendre lambda-tripod, whose projective mod3 cover is X6.
A.67 proves every singleton erasure n(1-e_p) on the least-conductor rankone
cubic fails Selmer lifting in the actual finite joint X3 quotient. All finite
erasures fail at X4 uniformly for cubic twists with a rational infinity flex;
that obstruction already factors through the degree-two sign cover1-J.
The modular levels are not nested unless joined. Abstract finite-kernel lifts
still exist; full metabelian/punctured-cover lifting sets remain separate.


A.68 (`sections/A_finite_congruence.tex`) strengthens the actual finite X3
comparison to every finite alteration of a nonzero integer on the least
curve. Its uniform norm/ramification proof includes coefficient2 and joint
finite alterations; it does not assume quadratic disjointness inside a
pro2 tower. Pure coefficient3 changes are also excluded around baseline0
using the order9/nonsquare q73 row already in `a_main_jline_at3.out`.
The proof gives the exact prescribed-primary Frobenius construction and
fixed-S isogeny-norm argument. General finite support around0 at other
primes and infinite alterations remain outside this theorem.


## Complete finite-alteration classification at actual X3 (A.69)

A.69 (`sections/A_finite_support.tex`) completes the finite-support
baseline-zero case left by A.68. Thus every exponent differing at only
finitely many coefficient primes from any integer has a Selmer lift in
the actual joint compact/X3 quotient exactly when it is that integer.
Arbitrary infinite alterations and the quotient's fibres remain outside
this classification.

Run `python deliverable/code/a_main_finite_support.py`. Its saved raw
output is `a_main_finite_support.out`. The exact certificate checks the
dyadic half-numerator, denominator `(x+y)^8`, exact pole order23, cubic
conjugate norm identities and the nonsquare2-torsion value at31. The
proof works uniformly for every coefficient prime p>=5: a full Cartan
orbit has at least24 points, whereas the nonzero dyadic polynomial has
at most23 zeros. This is a uniform proof, not extrapolation from a finite
prime search. A quadratic-character argument in the joint proper
division tower and prescribed-primary Chebotarev then exclude every
nonzero finite support. The coefficient2 case uses its separate exact
torsion value, and the support{3} case is already A.68.
