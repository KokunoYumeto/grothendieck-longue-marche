# Structural similarities across the frontier resolutions (blind run)

Run on 13 Nov 2026 by Claude Fable 5.2 at effort medium (the user's choice), with a cap of 250k tokens (it used 211k).
The brief said nothing of the user's hunch: it asked only for structural similarities in how the results were resolved
that no single one shows, for the features only some of them have, and for carry-overs. Saved verbatim by the main session.

---

## Findings: structural similarities across the seven results

The proofs behind our own returns were not read, and several external results rest on overviews or summaries, so every similarity below is a reading of statements, not a check of proofs.

### What I read

| Item | Source read | Limits |
|---|---|---|
| 1. ETH | OpenAI paper (`openai/math`, preprint of 25 Oct 2026): abstract, Theorem 1.1, corollaries, §1.1, §2.1–2.4 | Rest of the 64 pages and the Lean files not read |
| 2. Yang–Mills | The KITP PDF, in full | It is a two-page statement by the shepherding committee (Gross, Douglas, Jaffe, Klebanov, Nekrasov). It is not a validation: the 1147-page proof is unreleased and the committee says it must first be convinced it is correct. No mathematics is in it beyond "Wilson lattice + Balaban's renormalization group, continuum limit, fermions included; mass gap and confinement open" |
| 3. Local smoothing | OpenAI paper "Local smoothing for the Euclidean wave equation" (25 Oct 2026): abstract, Theorems 1.1–1.2, §1.3–1.4 | Proof sections not read |
| 4. Navier–Stokes | News summaries only | See below |
| 5. Andrews–Connes–La Gatta | TeX: abstract, introduction, Theorem `thm:condpos` with proof and remark | Middle sections not read |
| 6. S^6 | README, S6_02 `FINDINGS.md` (F1–F19), survey `FINDINGS.md` F1–F10, first half of `ROUTES.md` | `REVIEW.md`, `IMPLICATIONS.md`, `NOTES.md` not read |
| 7. Returns | Every row of each results CSV: LM7 (103), EXIT_ONE_TYPE (63), CYCLOTOMIC_KERNEL (56), FLAGGED_149 (107), TOTEX2 (32) plus its report head | FLAGGED statements cut at 300 characters. LM7 rows D.1–D.6, D.8, D.9, D.14, D.17, D.20–D.23 carry only a title in the CSV. The coordinator's added request to read the proofs of statements I use was not met: no `sections/` TeX was opened |

**Navier–Stokes, what the latest result is (summary only).** On 8 Sept 2026 OpenAI claimed, with a Lean formalization, finite-time blow-up for 3D Navier–Stokes from smooth data at rest under a smooth finite-energy force. The same day Buckmaster and Alpöge posted Lean-formalized forced blow-up for porous medium, 2D Boussinesq and 3D Euler; their Navier–Stokes extension is unreleased. The claim is unverified, and it is disputed whether a forced statement answers the problem as intended. The most recent result for the unforced equation is Hou–Wang–Yang's computer-assisted non-uniqueness of Leray–Hopf solutions (arXiv revision March 2026).

### Similarities

**S1. Each result has a scale parameter with one tractable end, and the difficulty is the transport back.** Confidence: high that the pattern is there; medium that it is the right common description.
- **ETH §2.3:** a polynomial H(T) with H(0) = #F. At T = 1..Q the variable groups decouple. deg H ≤ 3nR lets interpolation return to T = 0.
- **Local smoothing §1.4:** two auxiliary time coordinates σ from an imaginary translation. A scalar differential inequality carries a bound between circles |σ| = 2a, 1, 4a; each passage costs one inverse logarithm, giving the [log N]^{2/p} of Theorem 1.2.
- **Yang–Mills (committee's description only):** renormalization-group flow in lattice scale, followed "all the way to infinite distances".
- **Connes:** the window λ. QW_λ sees only primes ≤ λ². The transport (ground state → θ, then Hurwitz) is not done: the lower bound is Hypothesis LA.
- **S^6:** the period parameter w. Interior is settled (moduli = disc 0 < |w| < 216, F2); all three open items are its ends (F13 boundary |w| = 216, F14–F15 limit w → 0).
- **LM7:** level n and the profinite limit. Finite modules are non-free (B.7) but the limit is free cyclic (B.8). The 24 automorphisms extend through every abelian-exponent refinement, yet the system is not cofinal (D.26). The full profinite image is open (D.13, D.19).
- **TOTEX2:** stages of the AKR completion. A finite stage passes (C.10); persistence through the union is open (C.9).

The three that claim completion each have a bound uniform in the parameter (degree bound; logarithmic loss; Balaban's bounds, by report). Every open item in 5–7 is a missing uniform bound of this kind.

**S2. A small explicit interface carries all the interaction; the bulk is handled by a robust argument.** Confidence: medium.
- **ETH Definition 2.1:** groups interact only through at most δn bounded linear measurements.
- **Connes:** QW_λ is a finite-dimensional near-radical part (≈ 2λ² prolate vectors plus the pole functional) plus a strictly positive part. `thm:condpos` gives QW_λ ≥ (log σ / 2)‖f‖² on a subspace of codimension ≤ 2 + 2(n₀+1)|M|.
- **LM7:** sections are classified fibrewise over the toric minimum (E.16), then abelian (E.24), then class two (E.29, E.32, E.36), each fibre a torsor or empty.
- **S^6:** everything is computed as direct images along f = |−2K| over P¹, with all content at three fibres.

**S3. The decisive invariant is quadratic in two linear classes, and linear data provably miss it.** Confidence: high within item 7; medium as a cross-item claim.
- **LM7:** obstruction {2}∪{3} (E.20); κ₂(−1)∪κ₂(−1) (E.25); central corrections c_q = −9(A_q b_q − B_q a_q)/(q−1) (E.32); liftability varies inside one abelian fibre (E.31); the S₃ splitting fails first at integral class two (E.26).
- **FLAGGED:** class-two monodromy detects what homology does not (F17.2–F17.4, ZCF3).
- **CYCLOTOMIC:** abelianized sections coincide where full sections are injective (D7 against D2).
- **Local smoothing §1.4:** "summing the squares would discard the interference"; the square is taken after summing.
- **S^6 routes:** the Kodaira–Spencer determinant is a perfect square (I6); the fibration obstruction is κ ∪ α (Route 1.1). These are unverified by the routes note's own statement.
- **Connes:** the object is a quadratic form whose radical is the image of a linear map E.

**S4. The difficulty sits at a few exceptional loci, and progress came from exact local analysis there.** Confidence: high for 6 and 7.
- **S^6:** the multiplicity-four fibre (the bound M is attained only there, F3); the cusp fibre W (the CDP20 p. 692 step fails there, survey F6); the order-three point.
- **LM7:** the primes 2 and 3 (A.3, B.13; E.26 has two, zero and one section classes at p = 2, 3, ≥ 5) and the cusps (B.3, C.4).
- **CYCLOTOMIC / FLAGGED:** type (0,2) breaks statements true for hyperbolic types (C3, F10c, D7); bad reduction (F17).
- **EXIT:** the unmarked and one-punctured sphere factors (P1e5); non-stratal blow-up centres (P2a).
- **Local smoothing:** the focusing wave fixes the exponent and the lower logarithmic power (Prop. 8.1).
- **Connes:** the constraint ∫f = 0 removes exactly one rung per sector.

**S5. A stronger or neighbouring statement was attacked because it carries an exact identity.** Confidence: medium.
- **ETH:** counts instead of deciding; the count is an exact polynomial sum.
- **Local smoothing:** the wave estimate instead of Kakeya directly; waves have a conserved current. Kakeya and restriction follow as corollaries.
- **Navier–Stokes** (forced) and **Yang–Mills** (existence without mass gap): a variant of the famous statement.
- **Connes:** a finite-window form with a finite-dimensional truncation instead of the global form.
- **CYCLOTOMIC B11:** recorded as stronger than requested.
- **TOTEX2:** the direct implication stays open (A.2), while a stronger hypothesis with an identity, finite-family Ramsey, is proved sufficient (C.12–C.13).

**S6. The key tool is imported from a neighbouring field.** Confidence: medium.
- **Local smoothing:** Monge–Ampère potentials, Aubin–Mabuchi energy, Serre's compensated integrability.
- **Connes:** Slepian–Pollak–Landau prolate functions from signal theory.
- **S^6:** Néron heights and Eichler–Zagier (F8, I1–I2).
- **LM7:** K₂ tame symbols (E.29), Bass–Serre graphs (A.2, D.25).
- **ETH:** polynomial interpolation and tensor contraction.

**S7. Four returns stop at the same statement.** Confidence: high. LM7 E.23, CYCLOTOMIC C7 and C9, FLAGGED ZCF6, ZD10 and ZD11 all reduce their residue to section surjectivity for P¹ minus three points over Q. One fact also appears independently in three returns: a non-stratal blow-up breaks injectivity of local inertia, with map (m,n) → m+n (EXIT P2a, FLAGGED E2, CYCLOTOMIC C8).

### Features only some have

| Feature | Has it | Lacks it |
|---|---|---|
| Lean formalization | 1, 3, 4; 2 promised | 5, 6, 7 |
| Human author or committee taking responsibility | 5; 2 (custody only, no verdict yet) | 1, 3, 4, 6, 7 |
| Certified numerics or exhaustive finite checks | 5 (ball-arithmetic zero count), 6 (19,701 interval boxes, F3), 7 (LM7 B.13, D.25, E.12), Hou–Wang–Yang | 1, 3 as far as read |
| Result is a refutation | 1, 4, parts of 6 and 7, TOTEX2 D.2 | 2, 3, 5 |
| Positivity or monotonicity as the engine | 3, 5; 2 presumably | 1 (purely algebraic), 7 |
| Recognition by normalizers and centralizers | 7 (CYCLOTOMIC A6, C10; FLAGGED D5, D10; LM7 E.15), 6 (Aut = C*, F7) | 1–5 |
| Conditional main statement | 5 (Hypothesis LA; the paper says the positivity it assumes cannot be used unconditionally) | the others |
| Open items recorded inside the result | 6, 7, 5 | 1, 3 |

The refutations in item 7 are numerous: FLAGGED has 31 Refuted of 107; LM7 has A.6, A.9, A.13, B.3, C.2, C.8; CYCLOTOMIC has D5 (Conjecture A false over Q(μ_∞)); S^6 corrects [AC26] Remarks 1.3 and 9.21 and Engel's Remark 8.1.

### Carry-overs

1. **EXIT → the S^6 Leech question (strong).** EXIT P4d2: the genus-zero boundary dual complex for n ≥ 4 is a wedge of (n−2)! spheres of dimension n−4, with f-vector (25,105,105) and unimodular Smith form at n = 6. That is the Z²⁴ = H₂ of the complex in `LEECH_Z24_QUESTION`. It is an independent computation to set against the unchecked `delta06_lattice_20261113.py`.
2. **EXIT → S^6 open limits F14–F15.** Those items need the link and nearby fibre of a degeneration with multiplicities 3 and 4 after w = s⁶. EXIT computes this local model: the resolved cusp with multiplicities 1, 2, 3, 6 and its degree-six stack quotient (P1e-cusp, P1e-cusp-proper, P1e-cusp-stack), and the depth rule r ≥ k+2 (P5a2).
3. **LM7 E.28/E.31 → FLAGGED F17 and CYCLOTOMIC D15.** The tame-relation argument (Frobenius and inertia lifts in a Heisenberg quotient cannot commute) is a finite test of the kind F17.3 uses for bad reduction. D15 states its open obstruction as an H¹ class of the same shape.
4. **CYCLOTOMIC D5 ↔ LM7 E.34.** Both produce sections by solving all finite embedding problems after H² vanishes. E.34 lifts every unramified class. D5 shows the same mechanism gives a section with no point. The two together bound what "all finite stages lift" can prove in D.13 and D.19.
5. **Local smoothing → Connes (speculative).** Connes's missing step is a lower bound uniform in λ with only logarithmic slack; his upper bounds already carry (log λ)³. Local smoothing obtains this kind of bound from a positive divergence-free tensor built by Gaussian time–frequency filtering, with only logarithmic loss. Both are localization-in-phase-space positivity problems.
6. **Potential theory → S^6 F3 (speculative).** The routes note recasts N ≤ √2 as "a logarithmic potential is largest at t = 1" (I4, unproved). A maximum-principle proof in the style of local smoothing's scalar supersolution would replace the interval certificate.
7. **S5 → TOTEX2.** C.14 (totality ⇒ Ramsey) is the stronger statement with an identity; the report head gives no approach tried for it, while A.2 and C.9 were attacked directly.

Sources (as given by the agent):
- OpenAI math repository: https://github.com/openai/math
- ETH paper: https://raw.githubusercontent.com/openai/math/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf
- Local smoothing paper: https://raw.githubusercontent.com/openai/math/main/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf
- Yang–Mills committee statement: https://www.kitp.ucsb.edu/sites/default/files/YM_working_group.pdf
- NYU Shanghai RITS on the Navier–Stokes claim: https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/
- IAS, Hou–Wang–Yang talk: https://www.ias.edu/node/323971
- aicybr on the Lean statement: https://aicybr.com/blog/openai-exponential-time-hypothesis-eth-lean-proof-verification
