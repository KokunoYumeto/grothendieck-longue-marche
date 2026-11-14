# E.35: bounded search for the regulator at the ramified prime 3

Status: **Incomplete. No evaluation or nonvanishing proof for the exact class in E.35 was established by this search.**

The search was performed on 14 November 2026 after reading the full statement, the Kummer normalization, and the final comparison in `sections/E_ross_edge.tex`. Primary PDFs actually opened are distinguished below from search leads. “Verified” means opened and inspected at the specified locations; it does not certify an entire paper independently.

## Exact class being compared

Put (C:x^3+y^3=1), and retain the open curve, compact homology summand (H), arithmetic quotient \(\Gamma\), and tangent of E.35. The requested class is the compact Hochschild–Serre edge of

\[
\rho=\kappa_3(1-x)\smile\kappa_3(1-y).
\]

The exact map already proved in E.35 is

\[
\Phi_*[\eta]_{\rm ell}=-\iota_{w*}\operatorname{edge}_H(\rho)
\quad\text{in }H^1(\Gamma,H(1)).
\]

Thus a regulator result must concern this symbol, and must retain the map to this particular cohomology group. Equality after the real regulator alone does not perform this comparison: for two motivic elements (e_R,e_B), it asserts (e_R-e_B\in\ker r_\infty); to replace (r_3(e_R)) by (r_3(e_B)), one still has to prove that this particular difference belongs to \(\ker r_3\). No such inclusion or membership was proved here.

The elliptic-unit route has a concrete target map. On a torsion field (K_n) over (K=\mathbb Q(\zeta_3)), a unit (u_n) and rational torsion point (t_n\in C[3^n](K_n)) give

\[
\operatorname{cor}_{K_n/K}
\bigl(\kappa_{3^n}(u_n)\otimes t_n\bigr)
\in H^1(K,C[3^n](1)).
\]

Compatible systems give the corresponding class in (H^1(K,T_3C(1))). An application to E.35 needs an actual equality between its restricted compact edge and the specified Soulé class, together with a nonvanishing argument for that specialization. The sources below locate exactly which parts of this comparison are available.

## Primary results inspected

### Kings: both the main theorem and the regulator comparison exclude this prime

Primary PDF: [The Tamagawa number conjecture for CM elliptic curves](https://arxiv.org/pdf/math/0003113). Local PDF/text: `sources/B/ross_ramified/kings2000.*`.

**Verified:** §1.1.2–1.1.3, Theorem 1.1.5, §2.2 opening and Definition 2.2.1, Theorem 5.1.1 and its proof, §5.1.2, Corollary 5.2.2.

Theorem 1.1.5 assumes (p\ne2,3) and (p\nmid N_{K/\mathbb Q}\mathfrak f). The arithmetic comparison section additionally explicitly assumes (p\nmid\#\mathcal O_K^\times) and good reduction above (p). For (K=\mathbb Q(\zeta_3)), the unit order is six.

The decisive class comparison is Theorem 5.1.1, author page 51: it identifies the regulator of Deninger’s element with a sum of Kummer classes of theta values tensor torsion points. Its displayed hypothesis is again (p\nmid6N\mathfrak f). The next theorem fixes a prime of good reduction before using (\psi(\mathfrak p)) and the torsion decomposition. Consequently replacing Rubin’s old Iwasawa theorem with an all-prime theorem does not, by itself, remove the restriction from the regulator-comparison step. No extension of that step to this Ross symbol at three was proved.

### Johnson-Leung–Kings: an all-prime Iwasawa input is available

Primary PDF: [On the equivariant and the non-equivariant main conjecture for imaginary quadratic fields](https://arxiv.org/pdf/0804.2828). Local: `sources/B/ross_ramified/johnson_leung_kings2009.*`.

**Verified:** §5.1–5.3, Theorem 5.2, Corollary 5.3, Theorem 5.7 and Corollary 5.12; the source explicitly states that Theorem 5.2 covers all primes without exceptions.

Theorem 5.2 compares the determinant of the elliptic-unit lattice (J_\Lambda(\zeta(\chi))) with the Iwasawa cohomology complex, for every finite ray-class character \(\chi\). It applies at three. The class is defined in §5.2 by norm-compatible elliptic-unit Kummer classes and the normalization \((N\mathfrak a-\sigma_{\mathfrak a})^{-1}\).

This is a useful input for the concrete Soulé map above. In the inspected theorem there is no identification with \(\{1-x,1-y\}\), nor a computation of its prescribed specialization. Those two steps were not supplied by this audit. The stronger equivariant determinant conclusion in Theorem 5.7 adds its stated \(\mu\)-vanishing hypothesis; Corollary 5.12 establishes that hypothesis there for split primes (p\nmid6). Neither restriction should be silently transferred to Theorem 5.2, which is already unconditional for every prime.

### Nemoto: the new motivic equalities do not include the cubic case

Primary PDF: [L-function of CM elliptic curves and generalized hypergeometric functions](https://arxiv.org/pdf/2309.01059), v2; published in *International Journal of Number Theory* 21 (2025), 793–808. Local: `sources/B/ross_ramified/nemoto2024.*`.

**Verified:** introduction, author pages 1–3; Propositions 4.3 and 4.10 with their concluding divisor calculations.

For the quotient (X_3\to E_{27}), the introduction records Otsubo’s equality **after applying (r_D)**. Nemoto’s actual equalities in motivic cohomology are (e_{E_{36}}=2p_*e_6) and (e_{E_{64}}=2p_*e_4), obtained through Brunault’s injective divisor-symbol map. These statements provide a method for an explicit comparison calculation, but do not state the needed motivic equality for (E_{27}). I did not prove that missing calculation. I did not substitute the conjectured dimension of motivic cohomology for it.

### Asakura: the exact Ross formula has an excluded parameter

Primary PDF: [New p-adic hypergeometric functions and syntomic regulators](https://numdam.org/item/10.5802/jtnb.1250.pdf), *JTNB* 35 (2023), 393–451. Local: `sources/B/ross_ramified/asakura2023.*`.

**Verified:** Theorem 4.11 and its setup, condition (4.36), final paragraph of the proof and Conjecture 4.17.

The theorem computes the syntomic regulator of the exact Ross symbol on (z^N+w^M=1), but assumes (p>\max(N,M)). Our substitution is (p=N=M=3), which violates this inequality. Moreover the paper labels the associated general nonvanishing claim Conjecture 4.17. Its computational congruence criterion is not a computation at the excluded prime.

### Bley–Hofer: a genuine ramified-three result, with a different specified output map

Primary PDF actually downloaded: [Construction of elliptic p-units](https://arxiv.org/pdf/1806.02244). Local: `sources/B/ross_ramified/bley_hofer2018.*`.

**Verified:** §2.2, conditions (H1), (H2), case (c3), Theorem 2.7 and Remarks 2.9–2.10.

The downloaded PDF has arXiv v1 metadata and an internal date of 20 July 2021. It explicitly includes the ramified case (K_{\mathfrak p}=\mathbb Q_3(\zeta_3)), subject to complete splitting in the finite extension (L/K) and the class-number hypothesis. Its output is a formula equating coordinates of an elliptic unit’s local logarithm with valuations of constructed \(\mathfrak p\)-units. I did not establish an equality between that logarithm/valuation formula and the tensor-torsion Soulé class required above.

Version caution: the author-hosted PDF `https://www.math.lmu.de/~bley/ImagSolRank2.pdf`, dated 19 February 2018, has an earlier Theorem 2.7 without case (c3). The later downloaded text was used for the ramified-three scope. The earlier file must not be cited as excluding the case from the later result.

### Further close checks

**Oukhaba**, [Index Formulas for Ramified Elliptic Units](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/17BF075F84873E9D9BFBC46391DBEF6F/S0010437X03100346a.pdf/index_formulas_for_ramified_elliptic_units.pdf), *Compositio* 137 (2003), 1–22: opened introduction and Theorems A–B. Theorem A computes a unit index; Theorem B additionally requires its modulus prime to six. No comparison of the exact Kummer-cup edge with the unit lattice was established from these statements.

**Asakura–Chida, with Brunault’s appendix**, [A numerical approach toward the p-adic Beilinson conjecture for elliptic curves over Q](https://arxiv.org/pdf/2003.08888), v2: opened Theorems 1.1–1.2, the good-reduction setup in §3, Theorem 5.2, and Remark 5.1. The displayed proved regulator identity concerns its specified conductor-24 curve and symbol at a prime of good reduction. Its Beilinson–Kato comparison was not established for the present cubic at three.

The search also found a 2018 seminar title “On the p-adic regulator of Fermat cubic” on Nemoto’s institutional profile. The profile page timed out twice, and no theorem text or paper for that talk was obtained. The title is a lead, not evidence for an applicable theorem. The opened 2016 Keio workshop program confirms an earlier general Fermat-regulator talk but contains no theorem.

## Outcome and exact remaining work

No opened statement evaluates or proves nonvanishing of the specified three-adic class. The sharp remaining arithmetic comparison is between the Ross compact edge and an explicitly normalized specialization of elliptic-unit classes at the CM character. The all-prime Iwasawa theorem is available for use after that comparison and after checking the specialization; the proof in Kings that supplies the comparison has an explicit excluded-prime hypothesis. These are recorded as unfinished steps, not assumed statements.

The search does not assert that no such theorem exists anywhere. It records the bounded primary-source search and the exact conclusions inspected. No numerical experiment was presented as a regulator computation.

## Publication-status check

The bibliography now distinguishes the version inspected from publication status. Kings's paper is published in *Inventiones Mathematicae* 143 (2001), 571–627, as confirmed by the opened primary [arXiv journal reference](https://arxiv.org/abs/math/0003113). The mathematical text inspected was its March 2000 author preprint. Johnson-Leung–Kings's journal publication is likewise confirmed by the opened [primary arXiv record](https://arxiv.org/abs/0804.2828).

Bley–Hofer's work is published as a research article in *Advanced Studies in Pure Mathematics* 86 (2020), 79–111. The [publisher's contents](https://www.mathsoc.jp/assets/pdf/publications/aspm/CFM86.pdf) was opened; the mathematical version inspected remains the arXiv PDF specified above. Asakura–Chida–Brunault's paper is published in *Research in the Mathematical Sciences* 10 (2023), article 11; the [publisher's record](https://link.springer.com/article/10.1007/s40687-023-00374-2) and the university accepted-manuscript record were opened. Its mathematical statements were initially inspected in arXiv version 2.

Nemoto's publication metadata is reported by his institutional publication record, while the mathematical text read was author preprint version 2. Oukhaba was read in the publisher's PDF. No item was labelled unrefereed merely because an arXiv version was used; none of the version distinctions is silently erased.
