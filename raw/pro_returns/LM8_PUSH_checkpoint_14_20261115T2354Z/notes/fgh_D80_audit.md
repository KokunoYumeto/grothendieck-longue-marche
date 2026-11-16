# Independent FGH audit of D.80

Status: full proof, primary-source and executed-certificate PASS. Notes-only during checkpoint12 freeze; no registration or canonical edits.

I read the complete236-line candidate, the entire exact certificate, and canonical D43's statement and proof. I also rechecked the D78/D79 actual-image, local-line, coinduction and finite-coefficient arguments during the preceding audits.

## Actual images with infinite ramification

The pro-five completion of the free valuation sum is exactly the c0 lattice: modulo every power of five there is finite support. Independence of the two residual global classes, with both five-coordinates zero, forces two non-five inertia columns with unit determinant. Untwisted inertia there is trivial, so these are actual pure translations. Their closed Z5-span is the full rank-two lattice, giving the actual semidirect operator image. Infinite support introduces no closure defect. The local logarithm ratios are integral, so c0 coefficients make the series unconditionally convergent; local primitiveness gives the same exact line image used in D79. Its restriction-kernel calculation therefore applies without a finite-support hypothesis.

## The new uniform finite-level step

Canonical D43 explicitly applies to ANY abelian cocycle with nonzero inertia, whether or not a metabelian lift exists, and proves compact H1=0. For each fixed non-five local field all finite H0 and H1 groups are finite. Their inverse systems are Mittag–Leffler; in particular lim1 H0=0 and compact H1 identifies with lim H1(Wr). Thus that inverse limit vanishes.

Finite local Tate duality is compatible with coefficient transitions. Pontryagin duality identifies the dual of the finite inverse limit with the discrete direct limit of the dual finite groups. Cohomology commutes with the discrete filtered union of coefficient modules, so H1(Gq,D)=0. Consequently a class at one finite coefficient level becomes a coboundary at some larger finite level. This is a local statement for one q; the proof correctly does not assume its bound is uniform over infinitely many q.

The residual-inertia exceptional set E is finite by the c0 condition. At every other non-five prime, even a nonzero inertia vector divisible by5 acts trivially on the fixed ten-dimensional order-five three-jet module: (1+u)^(5x)=(1+u^5)^x and degree5 vanishes. The untwisted action and the raw cubic cocycle are unramified there. Therefore the same explicit constant/linear/cubic Frobenius primitives in that ONE module trivialize every such local class. Only the finitely many primes in E need larger levels supplied by local discrete H1=0. Taking the maximum of their finitely many levels and4 gives a common finite global coefficient module. The old primitives remain primitives after coefficient inclusion even if the larger module has acquired ramification. This is the essential legitimate replacement for an invalid direct-limit/infinite-product interchange.

The class remains globally nonzero by the actual full-translation coinduction and primitive raw Soulé restriction, as in D78. Therefore the d=0 lower bound meets the D79 upper bound. At d>0 the upper bound is already zero. Global residual independence makes a,b,a−b all primitive, hence T=0; D77 yields exactly the asserted compact topological groups. The scope does not claim infinitely ramified first-cohomology ranks or section existence.

## Actual point examples

The CRT formula gives t≡22 modulo36, hence v2(t)=1, v3(1−t)=1 and the two opposite valuations zero. This proves actual global residual independence. The five-adic congruence is t≡−1+5^(d+1) modulo5^(d+2), so v5(t^4−1)=d+1 and 1−t≡2 modulo25. Dividing the logarithms by4log6 gives v5(α)=d and β≡2 modulo5. Thus the local depth is exactly d, not merely a lower bound. The point itself supplies the section; D74 is invoked only for this finite-support fibre.

## Fresh primary verification and exact rerun

Freshly opened Milne, *Arithmetic Duality Theorems*, second edition, I Corollary2.3, printed28 (PDF zero-based35): https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf . Exact primary refs `turn1048view1` and `turn1049view0` explicitly give the finite H1 pairing and finiteness. The author's book landing page was also opened at https://jmilne.org/math/Books/adt.html (`turn1048view0`). This is precisely the finite local theorem used, not a directly asserted infinite-module duality.

Copied and independently executed the complete certificate as `notes/fgh_D80_certificate.py/.json/.out`; all30 exact CRT/valuation examples pass and the entire JSON equals the author output. SHA-256: `ad8c6e70b79a004a23d51086afb2797d6d47113b73ea5a2dcb7334524a76febe`. The infinite-ramification conclusion comes from the written finite-exception proof above, not from these finite point tests. No correction needed.
