# D.30: the Legendre finite-ramification reduction

## Proved result

The new section proves absolute irreducibility of every Legendre representation attached to a continuous noncuspidal section of the rational tripod. It then proves the exact equivalence between finite ramification for one coefficient prime at least five, cofinite ordinary integral local sections, and one common finite ramification set for the whole system. Under those conditions the rational system comes from an elliptic curve over Q.

The decisive character argument handles invariant lines defined only over a finite coefficient extension E. Kronecker-Weber and the dense direct sum of the non-coefficient local unit factors remove those factors after taking a power. Tate's local algebraicity theorem then forces a single integral exponent on the Q_ell-defined cocharacter of Res_E G_m. A reducible representation would have trace 1+v on a positive-density set splitting its finite characters, contradicting the density-one elliptic Weil bound from D.25.

The local cuspidal case uses the exact Kummer extension theorem: every extension of Q_ell by Q_ell(1) is semistable. A quadratic twist is retained, especially at the infinity cusp. Pan's theorem is invoked only after assuming finite ramification. At a good ordinary place, NOS and the Legendre j-function force an integral parameter. At an unramified cuspidal place, unramifiedness of the full representation first forces its quadratic diagonal twist to be unramified; the trace is then plus or minus v+1 and violates modular purity. A split cuspidal extension is included in this argument.

For the elliptic realization, Chebotarev compares the newform with every coefficient conjugate using density-one rational traces, and away-from-level newform multiplicity one gives a rational Hecke field. Eichler-Shimura gives the elliptic curve; another Chebotarev/Brauer-Nesbitt comparison gives its rational Tate representation at every coefficient prime.

## Exact limitations

Finite ramification itself is not proved for an arbitrary noncuspidal section. The theorem is a reduction to that hypothesis, not a solution of D1–D4.

Cofinite integrality leaves the possibility of finitely many cuspidal local sections. D.5 and Stix Corollary6 require ordinary points at every finite place; they cannot be applied at this stage. Even equality with a global elliptic rational representation system does not recover the full nonabelian section and does not identify all local Legendre parameters.

The accompanying genuine cuspidal section, obtained by twisting the tangent-one section at zero by e5*Kummer(13), shows that matching semisimple Frobenius polynomials alone does not force strict Weil-Deligne compatibility. Its monodromy at13 has rank1 at coefficient5 and rank0 at coefficient7. This is explicitly cuspidal and is not a noncuspidal counterexample.

The KLR source audit is version-qualified. The opened arXiv2003 full proof permits weight1 by its explicit increasing-prime bound. The stale “weight chosen large” phrase in its sketch is not a hypothesis of that full proof. The final2005 publisher text could not be retrieved, so no exact numbering or weight range is silently attributed to that unopened version. KLR is used only to delimit a general representation-theoretic shortcut; no realization of its examples by sections is asserted.

## Review and validation

Root read the full candidate and independently opened the relevant primary passages. Degeneration's independent complete review is audit/D_legendre_modularity_degeneration_review.md; it approves the mathematical proof and cuspidal example while excluding the KLR version comparison from its own sign-off.

The exact standard-library certificate code/D_legendre_modularity_checks.py was executed and returned PASS. It checks the leading order2 and coefficient1/256 of the reciprocal Legendre j-function, the residue square root of minus one modulo13, six compatible CRT idempotent levels, the tame Frobenius/inertia relation, the two monodromy ranks, and the shared polynomial T^2−14T+13. It does not test modularity, finite ramification, or the section conjecture.

Files added: sections/D_legendre_modularity_extension.tex; audit/D_legendre_modularity_results.json; this report; sources/D_legendre_modularity_refs.bib; sources/D_legendre_modularity_sources.md; code/D_legendre_modularity_checks.py and .json. The reviewable candidate is retained with the integrated proofs. The root owns the D.tex input, assembler registration and combined build.
