# Root audit of D.80 — PASS, notes only during checkpoint 12

Root read the full unrestricted-ramification candidate, its entire CRT
certificate, and the complete proof of the supporting local-cohomology
statement D.43. The CRT certificate was executed independently with
complete output in `notes/root_D80_certificate_rerun.out`. The frozen
paper and register were not changed.

Global mod-five independence, together with zero valuation at five,
forces two residual prime-valuation vectors away from five with unit
determinant. Their actual inertia images are pure translations because
the untwisted action is unramified there. They generate the entire
closed Z_5^2 translation group, even for infinitely ramified completed
Kummer classes. Local logarithm convergence is unconditional: its
integral coefficient factors are bounded and the prime coefficients
tend to zero five-adically. The actual local primitive-line image and
all D.79 upper-bound comparisons therefore apply as written.

The new lower-bound gate is valid at one common finite coefficient level.
For each nonzero ramified local inertia vector, D.43 proves compact
H^1(A)=0 for the actual twist, independently of section existence. The
finite H^0 coefficient tower is Mittag–Leffler, giving H^1(A)=lim H^1(W_r).
Finite local Tate pairings in degree one identify the latter finite
groups with the Pontryagin duals of H^1(W_r^D), naturally for all
transition maps. Duality and continuity on discrete filtered unions
then give H^1(D)=0. This assertion is derived locally prime by prime;
it alone does not supply a uniform level.

Uniformity is supplied by the fixed order-five cubic module. Away from
the finite residual inertia support, translations with both exponents
divisible by five act trivially modulo (5,(u,v)^4). Thus the already
proved constant/linear/cubic Frobenius primitives work there in the one
original module, including at primes where the full twist is ramified.
Only finitely many other places require enlargement. The maximum of
their finite coefficient levels is consequently a single common level.
Primitives in the smaller module remain primitives under its actual
equivariant inclusion, irrespective of new ramification in the larger
module. This avoids interchanging a colimit with an infinite product.

The exact CRT construction is explicitly restricted to positive finite
depth d>=1. Its two congruences give valuation-one detections at two and
three, and local depths (d,0,0). The examples are ordinary rational
points, hence have actual full sections. The d=0 finite-torsion case is
separately supplied by t=-2; no d=0 claim is made for the CRT family.
The executable checks all stated valuation identities for ranks1–30;
the displayed congruence and logarithm proof establishes every d>=1.

Primary local-duality text freshly opened by root: Milne, *Arithmetic
Duality Theorems*, second edition, I, Corollary 2.3, printed p.28,
https://www.jmilne.org/math/Books/ADTnot.pdf . The exact statement and
proof were read in browser reference turn1041view0, including finiteness
of both degree-one groups and the natural cup-product isomorphism.
Characteristic zero satisfies the stated characteristic restriction.

The general nonseparated kernel, arbitrary infinite-ramification first
cohomology ranks, and arbitrary section existence remain outside this
claim. Root's full proof and executed-certificate audit passes. PBC subsequently
completed an independent full proof, primary-source and exact-certificate
audit with PASS; its ledger is notes/pbc_D80_audit.md. The candidate remains
notes-only during this source freeze and is ready for later integration.

FGH also completed an independent full proof, primary-source and complete certificate audit with PASS before capture; see notes/fgh_D80_audit.md.
