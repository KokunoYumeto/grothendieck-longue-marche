# Signed conjugators at the first Fermat stage

The unrestricted minimal-stage integral comparison is **refuted**. The corrected first-stage lift functor is computed. B.31–B.34 now construct the actual §49 source and its local/profinite relative actions, identify the entire abelian Fermat quotient, compute the first modular image, and refute a compatible rational-base action. The retained conjugator images and higher realization remain **Open**, as the revised B.24d states. This report does not mark Part B complete.

## Source and distinction

The new argument rereads the §51.1–2 construction, folios 664–669, C4 scans 33–44, especially equations (15), (18), (21), (28), (30), (31), and (38). The supplied original scan 41 was directly inspected; the checked transcriptions of the surrounding pages were read. The direct public-PDF browser request did not succeed, so original-image inspection is not asserted for the other pages. LM1 E.24–E.25 and its integral cocycle code were reopened as prior calculations, then the needed rank-five extension was independently constructed.

The full profinite signed automorphism source of §49, its minimal §51 specialization, and a finite-dimensional matrix scheme called M in still earlier sections are distinct inputs. The counterexample concerns the explicit minimal fine data, with a required compatible action on the next integral modular/Fermat stage. It does not refute functoriality for an actual automorphism of the original group preserving its Fermat kernel.

## Exact obstruction

Let C=SL2(Z), F=Π0=<x,y> of index12, and K=ker(F→(C2)^2)=Γ(4), of index48 and rank5. The canonical integral cocycle models C2→C0 have vector kernels Ga5→Ga2, with matrix

```
2 0 0 2 0
0 0 2 0 2
```

This is constructed over Z before reduction. Modulo2 its linear part is zero. Its scheme-theoretic image is exactly the constant group SL2(Z/4), embedded as the four points defined by X²−X=Y²−Y=0 on each of twelve minimal components.

Over A=F2[epsilon]/epsilon², the valid positive-sign fine datum alpha=beta=epsilon*x, nu=nu_prime=nu2=nu3=0, mu=1 gives the inner automorphism Int(epsilon*x). It preserves the prescribed loop and sends rho to (epsilon,epsilon)rho, outside that scheme-theoretic image. Therefore it has no compatible lift, even after a faithfully flat extension. This is an actual incompatibility, not merely nonuniqueness of reconstruction from the two generator images.

The rewritten **B.24 Refuted** and **B.24a Proved** give the complete proof and canonical projection.

## Replacement and computed kernel

**B.24b Proved** computes the entire characteristic-two image of the linear fine action. It factors through U=Ga×constant C2, with coordinates t=a+nu2+nu3 and e=nu2. The fine-parameter fibres are Ga²×constant C2, retaining nu3. A compatible lift exists exactly when t²=t. Thus its liftable image is the constant group C2².

Each nonempty lift fibre is a torsor under the automorphisms of the rank-five extension inducing the identity on its finite quotient. The full unmarked kernel is given explicitly by

```
(v,h) -> (T(v)+b_h,h)
T A_h = A_h T
b_h + A_h b_k - b_hk = T(c(h,k)) - c(h,k).
```

With six labelled boundary vector subgroups, these equations simplify completely. The six primitive boundary directions have the single unimodular relation that their sum is zero. A line-preserving additive polynomial T must therefore be coordinatewise one scalar additive polynomial f. A norm-annihilating functional forces f(1)=1; the translations are exactly Z1(H48,W). The latter is Ga6, proved by a four-row reduced matrix on the ten values at rho,sigma. The marked kernel is consequently Ga6 semidirect Aut_add(Ga;f(1)=1). It is represented as an ind-affine functor by bounding the polynomial degrees of the map and its inverse; finite-type representability is not claimed.

On A there are256 fine parameter points,8 minimal automorphisms and4 liftable minimal automorphisms. Every fine-parameter fibre has32 points, so128 of256 fine data lift. All points over the reduced field F2 lift; the obstruction first appears on its dual numbers.

The degree-at-most-two identity tangent lift kernel has dimension7: six translation cocycles and one invisible Frobenius direction. That last direction is the genuine nonidentity scheme automorphism

```
(v,h) -> (v+epsilon*(v^[2]-v),h),
```

which fixes every discrete word. Polynomial additivity, inverses, and the nonzero epsilon*T² coefficient are checked symbolically. Its values on A-points alone would not detect this nonidentity scheme map. Allowing arbitrary finite additive-polynomial degree gives an invisible tangent space with one basis vector v^[2^r]−v for each r≥1.

The extra nu3 sign is constant C2, not mu2. On A both constant labels map to1 under nu3↦(−1)^nu3, whereas mu2(A) also contains1+epsilon. Substituting mu2 would change the source functor and does not remove the incompatibility.

## Rational comparison and residual

**B.24c Proved** gives the explicit inner lift t↦Int((t/2)k1) over Z[1/2]. Rational inner lifts supplied by the identity vector subgroup form a Ga3 torsor; this does not classify inner lifts arising from other components. Finite-group cocycle averaging proves that every minimal fine datum over a Q-algebra has a compatible automorphism lift to this first abelian relative stage after rational choices. No Q-to-F2 base change is used or possible, and this rational existence does not imply integral lifting at2.

**B.24d Open** now retains the exact remaining task of determining the retained normalizer/conjugator images on q2 and higher relative stages and classifying the full kernels beyond word-congruence criteria. B.31–B.34 have removed the former source, preservation, local/profinite action-existence and first-modular-image residuals; the proposed compatible action of the entire profinite source over Q is refuted. In particular, arbitrary additive-polynomial first-stage lifts have not been shown compatible with every higher nonabelian stage. The present result removes the old vague missing-infinitesimal-parameter diagnosis and replaces it with a proved obstruction plus an explicit corrected first-stage input.

## Files and reproduction

The source is `sections/g_signed_fermat2.tex`, included directly after the rewritten B.24 in `sections/B.tex`. Dedicated ledgers are `B_signed2_results.json` (B.24a–d only; the root-generated B.24 row must be refreshed), `B_signed2_coverage.json`, `B_signed2_readings.json`, and `B_signed2_refs.bib`.

Run, from the deliverable directory:

```
python code/g_signed_fermat2.py > code/g_signed_fermat2.out
python code/g_signed2_registers.py > code/g_signed2_registers.out
```

Only Python's standard library is required. The first program writes `g_signed_fermat2.json` and the complete exact `g_signed_fermat2_model.json`; it checks all110592 integral cocycle triples, all2304 projection identities, all finite quotient actions, the six unimodular peripheral minors, the module equations over F2, every dual-number fine datum, and the Frobenius polynomial identities. The second program writes only the dedicated ledgers. No root assembler or checkpoint writer was run.

The B.14d uniform all-prime proof and its metadata were not modified during this task.
