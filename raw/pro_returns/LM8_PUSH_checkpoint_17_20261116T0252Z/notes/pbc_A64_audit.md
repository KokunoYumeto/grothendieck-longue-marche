# Independent full audit of A64

2026-11-15, around21:19UTC. **PASS**, with a minor bibliography page correction sent to the author. This is a proof and exact-certificate audit, not a claim that the general TaskA.5 frontier has been closed.

## Actual tame source model

I read the complete candidate. Integral j gives a potentially good elliptic model also at residue2. The relevant specialization is the prime-to-residue comparison for the actual smooth pointed pair, applied to the actual geometric Galois closure. After a finite extension kills its arithmetic twist, the cover and its prescribed generic identification extend tamely. Local normalization at the origin has the tame parameter relation t=u^e with e invertible, while the complement is finite etale. Hence the proper source itself is smooth, and subgroup quotients are covered by the same local argument. This is stronger than a claim about good Jacobian reduction and uses the actual map required by the task.

## All torsion clusters, including ordinary reduction

Finite-flat idempotent decomposition over the strict henselian base separates the geometric special torsion points. Each factor has positive rank and a nonempty generic fibre. A generic torsion point extends after finite base extension by properness, and its translation identifies the factors. Thus every r-primary specialization fibre has the same size r^(a(2-f)); the prime-to-r factor specializes bijectively. Distinct prime-to-r factors cannot merge with an r-primary difference, so the resulting count applies to every m-torsion cluster, not only the one at the origin.

Over a non-origin cluster, each source formal disc is etale and receives one point over each target point. Over the origin, a ramification indexe gives one old cusp and e points over each of the other c-1 target marks. The respective source-cluster sizes c and1+e(c-1) are at least2. After marked separation all joining paths inside each such cluster are rational, so the exact pointed hypotheses of the previously audited A41/A42 apply at every coefficient prime. The count m^2d-2g+2 follows directly from Riemann--Hurwitz and unramifiedness away fromO. The actual open immersion and unchanged proper homology are precisely the normalizer-transfer scope; no finite-refinement or fixed-element-lifting assertion is being used.

## Inert Heisenberg prime and pure powers

The only case outside the prime-to-closure criterion and A63 has p=3mod4 and m=p^a. The target is supersingular, so every new target mark specializes toO. In the actual A61 model the main component is radicial over the good elliptic target and has exactly one geometric point overO. Every other positive-genus component is constant at a finite critical centre distinct fromO. A rational component mapping to an elliptic curve is constant, even in positive characteristic. Therefore a connecting path in the O-fibre cannot cross one of those positive-genus components. Nodalness gives at most one attachment branch at the unique main point, so the remaining fibre is one rational subtree. If it is absent before marking, separating the colliding sections creates it; if the attachment is already a node, resolving marked sections through that node inserts only rational components. All enlarged marks thus have rational joining paths, and the original p^2>=9 marks ensure a distinct companion for every mark.

The Heisenberg degree, genus and cusp formulas are consistent with the actual degree-p^3 base cover. This covers every m through the stated elementary case partition. The universal assertion for arbitrary TaskA.5 covers is explicitly left Open.

## Executed independent certificate

I executed the entire computational body of `notes/fgh_A64_certificate.py` without writing its owner outputs. The result is retained in `notes/pbc_A64_independent_rerun.json`; all full JSON data agree with the author's output. It checks200 abstract tame-index count rows,52 actual Heisenberg count rows,16 inert-power rows and600 exhaustive sample case partitions, together with both symbolic identities. Exact hashes and comparison details are in `notes/pbc_A64_independent_rerun.out`. The initial direct Python-object comparison distinguished tuples from their serialized JSON lists; comparison of both complete JSON values passes. No mathematical assertion failed. The finite count certificate does not substitute for the actual-model proof audited above.

## Primary sources independently reopened

- **verified:** SGA1, ExposeXIII, Corollary2.9, Section2.10, Lemma2.11 and the proof of Corollary2.12, https://arxiv.org/pdf/math/0206203 . Exact opened references: `turn1009view0/2`, `turn1010view0/1`, `turn1012view0/1/2`. The final proof explicitly distinguishes the prime-to-p bijective comparison and inertia preservation.
- **verified:** Silverman, *The Arithmetic of Elliptic Curves*, second edition, TheoremV.3.1, PropositionVII.5.5 and AppendixA Corollary1.4(b), https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . Exact opened references: `turn1009view1/3`, `turn1010view2/3`, `turn1012view3/4`. The VII5.5 statement appears on printedp197, notp196; this small citation correction was sent to FGH and root. V3.1 covers the two geometric p-power torsion possibilities, and A1.4(b) explicitly covers the potential-good criterion.
