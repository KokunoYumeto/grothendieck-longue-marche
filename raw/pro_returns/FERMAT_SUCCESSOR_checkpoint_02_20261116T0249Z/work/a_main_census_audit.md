# Certified CM coefficient and section census

## Runtime and proof inputs

PARI/GP2.19.1 was downloaded from the official archive, SHA256
419553b11ff8c3ecb8e9031b7d91d7cee003a5d721e685fcb499565c96fe2943,
and compiled locally. Python-flint0.9.0 supplies Arb. The official PARI manual was opened for ellglobalred, ellrootno, ellan, elltors and ellrank. It explicitly distinguishes exact root numbers and unconditional algebraic rank bounds from the tolerance-based ellanalyticrank. The latter is not used as a certificate. The initial wrapper wrongly treated the harmless stack-size warning as an error; the log is retained as a_main_cubic_census_attempt1.out. Passing stack size on the command line fixed this harness issue.

Johansson's original Arb paper was opened at https://fredrikj.net/math/arbpaper.pdf, together with the official python-flint documentation. Both confirm rigorous enclosure arithmetic and the incomplete gamma/exponential integral functions used below.

## Analytic certificates

Let N be the exact conductor, w the exact root number, c=2pi/sqrt(N), r=exp(-c), and f=sum a_n q^n. Hasse's bound and the Euler-factor recurrences imply

    |a_n| <= d(n)sqrt(n) <= 2n.

Splitting the Mellin transform at its central point gives, for w=+1,

    L(E,1) = 2 sum_(n>=1) a_n r^n/n.

The absolute tail beyond M is at most 4 r^(M+1)/(1-r). When w=-1 the central value is exactly zero, and

    L'(E,1) = 2 sum_(n>=1) (a_n/n) E1(cn).

Since E1(x)<=exp(-x)/x, the derivative tail is at most

    4 r^(M+1)/(c(M+1)(1-r)).

We evaluate these in160-bit Arb balls, initially with M=8(floor(sqrt(N))+1). A ball excluding zero proves nonvanishing directly. No decimal tolerance, rational denominator guess, or conjectural BSD value is used.

For positive-sign central intervals containing zero, exact rational points of infinite order are obtained. Good inert reductions at11 and17 bound rational torsion by6 for all our cubic/sextic curves; good inert reductions at11 and19 bound it by4 for the quartic coefficient curves. The script verifies the equation in rational arithmetic and verifies that6P or4P is not the origin. Rubin CorollaryC forces L(E,1)=0; even parity then gives order at least2.

For the exact order, put Lambda(s)=c^(-s)Gamma(s)L(E,s), h=2^-45. We evaluate

    Lambda(1+h)
      = sum a_n [Gamma(1+h,cn)/(cn)^(1+h)
                 + w Gamma(1-h,cn)/(cn)^(1-h)]

in256-bit Arb balls through M=20(floor(sqrt(N))+1). Its absolute tail is bounded by

    T = 4 r^(M+1)/(1-r) * (1/c+1/(c^2(M+1))).

For j>=1 and |x|<=h<=1,

    |Lambda^(j)(1+x)| <= B_j,
    B_j = 4 j^j r/(1-r)^2 * (1/c+2/c^2+2/c^3).

Indeed |f(it/sqrt(N))|<=2exp(-ct)/(1-exp(-ct))^2, t^h<=t, and (log t)^j<=j^j t for t>=1. Taylor's theorem, known lower-order vanishing and parity give the interval

    L^(k)(1) in c k! Lambda(1+h)/h^k
           +/- c B_(k+2) h^2/((k+1)(k+2))

for k=2, or for k=3 when order at least3 is known. The latter lower bound follows from an unconditional algebraic rank lower bound at least2, Rubin CorollaryC, and odd parity. Every raw exact coefficient vector, minimal model, change of variables, torsion group, point certificate and higher-derivative bound is retained in gzip JSON. The CSV balls include rounding and the proved infinite tail.

## Cubic completion

All81 coefficient classes are rigorously certified:34 analytic rank0,41 rank1,6 rank2. The rank2 classes are d=30,126,210,420,2100,2205. In particular d=9 has conductor243, minimal model y^2+y=x^3-1 and certified first derivative

    [1.29019059036986358169134 +/- 6.10e-24].

Global minimality among arbitrary cubic twists is now proved in A.43 by conductor lower bounds: every p|d, p!=3 has exponent at least2; f3>=2, and f3>=3 if3|d, because no tame extension can turn discriminant valuation13 or17 into0 modulo12. A conductor at most243 therefore restricts d to1,2,3,4,5,6,9,12,18,25,36, whose exact conductors and ranks are already certified. Only d9 has rank1 at conductor at most243.

For alpha X^3+beta Y^3=Z^3 with cube-free positive representatives supported at2,3,5,7, let d be the cube class of alpha beta. Its Jacobian is E_d:y^2=x^3-432d^2. Inert reductions at11 and17 give12 and18 points. The2-division equation x^3=432d^2 has a rational solution exactly for d=2. The3-division polynomial 3x(x^3-1728d^2) gives rational3-torsion exactly for d=1, since x=0 has negative right side. Thus torsion is C3 for d=1, C2 for d=2, and trivial otherwise. All81 cases were checked against exact PARI torsion output.

If rank is zero and d differs from1 and2, every rational point P satisfies3[P]-H=0 in the rational Jacobian, H the plane hyperplane class. Hence P is a flex. The exact Hessian is -216 alpha beta XYZ, so these points are precisely coordinate cusps. If d=1 but the pair is not(1,1), some prime gives coefficient valuations1,2,0 modulo3 and prevents a local point. If d=2, the same obstruction away from2 leaves only(1,2),(2,1),(4,4). Each has one cusp and one ordinary point, respectively[-1:1:1], [1:-1:1], [1:1:2]. Their tripod values are-1,2,1/2.

The complete6561-pair CSV is a_main_cubic_pairs.csv. The rank-zero criterion applies to2754pairs:2654 have no sections,97 have only cusp packets,3 have an ordinary point and a cusp packet. Each cusp packet contains all its completed Kummer parameters. At0 it occurs iff beta=1, with parameter t in cube class alpha; at1 iff alpha=1, with parameter1-t in class beta; at infinity iff alpha=beta, with parameter1/t in class alpha^(-1).

## Quartic completion

All512 quartic coefficient curves y^2=x^3+A x are rigorously certified:220 analytic rank0,256 rank1,36 rank2. The complete262144-pair compressed CSV is a_main_quartic_pairs.csv.gz. The three Jacobian target rules are-4alpha beta,4alpha/beta^2,4beta/alpha^2 modulo fourth powers. The parent agent owns the proof of the ordinary point classification.

The criterion applies to213496pairs:212200 have no sections,1293 cusp-only,3 ordinary-only and0 both. The ordinary tripod values are-1,2,1/2; each relevant even cover has the four sign choices for its affine rational coordinates. Exact class, point and rule dictionaries accompany the full compressed CSV; a_main_cm_pairs.py has a lossless decoder.

## Sextic completion

All2592 coefficient curves y^2=x^3+B are rigorously certified:1136 analytic rank0,1296 rank1,160 rank2, with no unresolved class. The full6718464-row a_main_sextic_pairs.csv.gz is complete. The criterion applies to6689532 pairs:6681792 empty section sets,7725 cusp-only,15 ordinary-only,0 mixed. The28932 remaining rows are explicitly unclassified by these criteria.

The fifteen ordinary tripod values are the S3 orbits of-1,-8,4. Each occurs in one normalized pair of sixth-power classes and has the four independent sign choices for its affine coordinates. The exact point dictionary, class dictionary, ten target rules, mask histogram and lossless decoder are preserved. The parent owns A.33–A.36, proving the torsion/target/point-list geometry.

A.37–A.43 are written in deliverable/sections/A_census.tex. Every coefficient rank is printed in the paper in the three full rank matrices under deliverable/tables; the target join formulas and dictionaries give a complete factored paper representation of all pair rows. Full CSV data are supplied separately as requested.

