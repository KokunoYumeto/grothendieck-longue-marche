# Review of the Pro return CYCLOTOMIC_KERNEL, 12 November 2026

Claude Opus 5.5 (effort max), 12 Nov 2026. No sub-agents.

**Reviewed.** The return of GPT-6 Astra (ChatGPT Pro mode, effort Pro) to
`pro_prompts_archive_20261112\CYCLOTOMIC_KERNEL\PROMPT.md`, unpacked in
`longue_marche_pro_pilot_20261104\answers\CYCLOTOMIC_KERNEL_unzipped\CYCLOTOMIC_KERNEL\`: `CYCLOTOMIC_KERNEL_paper.tex`
(2,653 lines; read in full for Parts A, B, C, D0–D9, AE, E1–E3 and the statements of D10–D15, E4; the PDF was not
opened), `CYCLOTOMIC_KERNEL_results.csv` (56 rows: 47 Proved, 5 Refuted, 4 Open), `_report.md`, `_readings.csv`,
`_references.bib`, the source audit (searched), the five mathematical programs and their outputs.

**Compared with.** The prompt; from its background zip: `R149_NOTES_20261112.md` and
`R149_WARGAME_EXCERPTS_20261112.md` (the reader R-149 and the war game, both Claude Fable 5.2, effort max), Stix's
arXiv:0809.0017 (§§3–5, 9.6, Appendix B), Nakamura 1994 (§§1.3, 2.1), the scan images of 149 scan 127. Opened and
saved in `papers\`: Katz–Lang with Ribet's appendix (e-periodica export), Haran–Jarden 1991 (Numdam), Jarden 2011
(author's PDF), Clark 2006 (arXiv:math/0604263v1), Minamide–Tsujimura, *Internal indecomposability of profinite
groups* (author's PDF dated 19 May 2022), Chou 2019 (arXiv:1711.00412).

**Grothendieck's text.** The checked transcriptions in `grothendieck_archive_transcription_20261110\returns\`
(MPL_149_001-090: scans 32, 45, 53–56, 61, 62, 66; MPL_149_091-136: scans 126–128, 130) and the image of scan 127.

**Computations.** The five mathematical programs were copied to `rerun\pro_code\` and run with `python -I` (Python
3.13.9, SymPy 1.13.1; the return used 3.12.14 and 1.14.0): all exit 0 with empty stderr, outputs identical apart from
version strings. The ledger and paper scripts were rerun in a full copy (`rerun\bundle_copy\`). My own code,
written from the paper without the return's code, is `rerun\indep\d4_d5_indep.py`. Details in §5 and
`rerun\out\COMPARISON.txt`.

## 1. Verdict table

| Verdict on the 56 statements | Number | Statements |
|---|---|---|
| correct | 43 | all others |
| correct with a gap | 0 | — |
| known | 9 | A1 (Ribet; Stix Lemma 19, Lemma 32), A2 (Stix Prop. 11, Cor. 12–13), A3 (Nakamura (2.1.4)), A6 (Stix Cor. 22 + Thm. 14 over K(μ∞); in substance), B2 (Minamide–Tsujimura Thm. 2.12), C2 (Stix Thm. 14(2); Esnault–Hai), C5 (homotopy sequence; Hoshi 2014 Prop. 2.4 as quoted), D2 (Tsujimura 2023 Prop. 4.2; Stix Thm. 45), D5 (content: Clark 2006 + cd(G_{Q^ab}) ≤ 1) |
| open as stated | 4 | D13, E3, D15, E4 |
| wrong | 0 | — |

No statement is wrong. The decisive results hold: R2 (A1–A7, AE1, with A5's repair of step (4)), R3 (B1) and its
Hilbertian form (B2), the scan-127 correction (B7–B9), the packets (C2) and the (0,2) failure (C3), the degree-81
separating cover (D4), the failure of Conjecture A over Q(μ∞) (D5), the primewise H1 (AE2, AE4) and the class-two CM
computation (E1, E2).

Checked: V = proof followed in full; C = recomputed by my own code; R = program rerun, identical; M = manuscript
(transcription or scan) read; S = spot check (statement, key step, sources named); O = read in outline only.

| Id | Claim (short) | Return | Verdict | Checked |
|---|---|---|---|---|
| A1 | over F′ finite over K(μ∞): torsion finite, T(A)^Γ = 0, Hom(TS,TA) = 0, no divisible points, divisible units = μ∞ | Proved | known | V; Ribet Thm. 1, 3 opened; descent F′ = k₁(μ∞) checked |
| A2 | inertia: trivial intersections, N_π(I_c) = I_c, C_π(z) = I_c, N_E(J) = D_c, sequence (A.1) | Proved | known | V; Stix Prop. 11, Cor. 12–13 opened |
| A3 | all-N boundary-image criterion for inertia elements | Proved | known | V; Nakamura Lemma (2.1.4) opened; Stix 2012 comparison not checked |
| A4 | R2 steps (1)–(3); proper case C = 1 | Proved | correct | V |
| A5 | a closed subgroup of inertia elements lies in one I_c (repair of step (4)) | Proved | correct | V, R |
| A6 | C(s) ≠ 1 iff s cuspidal; then C(s) = I_c, c unique | Proved | known (in substance) | V; Stix Cor. 22, Thm. 14, Rem. 15(2) |
| A7 | germs, open Ω ⊂ Γ°, Δ ⊃ Ω: C = ∏_{χ_ℓ\|Δ=1} Z_ℓ(1) | Proved | correct | V |
| A8 | exceptional types; real base: C(s) = π | Proved | correct | S |
| A9 | U_{0,3}: C = ⟨x⟩, y and [x,y] not fixed (Fermat cubic functional) | Proved | correct | V (n = 3 functional by hand), R |
| B1 | C_{G_Q}(G_{k(μ∞)}) = 1 (R3) | Proved | correct | V (special case of B2) |
| B2 | Hilbertian k: every nontrivial closed normal subgroup of G_k has trivial centralizer | Proved | known | V; Jarden Prop. 2.5, Haran–Jarden Cor. 2.5, Minamide–Tsujimura Thm. 2.12 opened |
| B3 | six named fields | Proved | correct | S, R |
| B4 | E_K, K finitely generated: C(E′°) = 1 | Proved | correct | S |
| B5 | slimness under extensions and limits; rank-one correction | Proved | correct | S |
| B6 | C_E(s(Ω)) = C_P(s(Ω)) | Proved | correct | V |
| B12 | Theorem 1 over fields finitely generated over K(μ∞) | Proved | correct | S |
| C1 | Z(L_i) is the normalizer D_c; torsor under K̂* | Proved | correct | S, M (scan 54) |
| C2 | packets embedded, disjoint, apart from points; (0,3) included | Proved | known | V; Stix Thm. 14(2) opened |
| C3 | first assertion of scan 54 false for (0,2) (G_m) | Refuted | correct | V, M (scans 53–55) |
| C4 | précisions for sections and germs | Proved | correct | S |
| C5 | homotopy exact sequence for elementary fibrations | Proved | known | S (Hoshi 2014 not opened) |
| C6 | point sections of elementary towers: C = 1; necessity of b) of scan 48 | Proved | correct | V |
| C7 | b) for V a point = noncuspidal; same defect as Conjecture A | Proved | correct | S |
| C8 | boundary diagonal nonzero; injectivity fails after a blow-up | Proved | correct | V (arc and chart), M (scan 130) |
| C9 | admissible germs = noncuspidal germs; scan 66 | Proved | correct | S, M (scan 66) |
| C10 | inertia = nonzero C(s); maximal cyclotomic procyclic; scan 483 false | Proved | correct | S |
| B7 | function field of a curve: C(s) ≠ 1 iff s in D_v of a rational place; then C = I_v | Proved | correct | V |
| B8 | (32)–(33) false with L (value I_v); true for the model U | Refuted | correct | V, M (scan 127 image) |
| B9 | statement 2 in tr. deg. 1 ⟺ birational section conjecture | Proved | correct | V |
| B10 | packets are the fibres of s ↦ [C(s)] | Proved | correct | S |
| B11 | packets recover X(K̄) and the open models | Proved | correct | O |
| D0a | topology; fixed pro-points = points and cusps | Proved | correct | S |
| D0b | at most one fixed pro-point; Γ°- and Γ-fixed sets equal | Proved | correct | V |
| D1 | exact abelianized coincidences over F; U_{0,3} parametrization | Proved | correct | V |
| D2 | point-section injectivity over finite and f.g. extensions of K(μ∞) | Proved | known | V; Stix Thm. 45 opened; Tsujimura not opened |
| D3 | w^n = z, u^m = 1 − ζw do not separate ζ₆, ζ₆⁻¹ | Proved | correct | V, R |
| D4 | degree-81 cover separates ζ₆, ζ₆⁻¹ over Q(μ∞) | Proved | correct | V, C, R |
| D5 | Conjecture A false over Q(μ∞): t⁶ + 2y³ + 4 = 0 | Refuted | known (content) | V, C, R; Clark opened |
| D6 | Théorème 2 (faithfulness) over F | Proved | correct | V |
| D7 | Théorème 3 fails over F (G_m: 1, ζ₆); semiabelian criterion | Refuted | correct | V, M (scan 32) |
| D8 | Théorème 1 over F | Proved | correct | S |
| D9 | Proposition and précisions over F; (0,2) persists | Proved | correct | S |
| D10 | Poincaré coverings ⟺ common finite étale cover | Proved | correct | O |
| D11 | continuous actions descend; B′ with continuity ⟺ B for Γ° | Proved | correct | O |
| D12 | Aut of the pro-curve, proper case: completion of Comm(Λ) | Proved | correct | O (Džambić–González-Diez not opened) |
| D13 | unrestricted D(e) | Open | open as stated | O |
| AE1 | finitely generated K: torsion finite over K′(μ∞); A1–A7 transfer | Proved | correct | V |
| AE2 | primewise H1: C_Δ = ∏_{ℓ∈P_Δ} Z_ℓ(1); normal Δ ⇒ s cuspidal | Proved | correct | V |
| AE3 | instances of (E.1); K^ab iff no CM subfield | Proved | correct | O (Murotani–Ozeki not opened) |
| AE4 | H1 as written false: Δ = G_{Q(μ_{3^∞})}, C = Z₃(1) | Refuted | correct | V |
| E1 | y² = x³ − x over Q(i): N₂^{s(Δ)} = N₂, N₂^{s(Γ°)} = centre | Proved | correct | V |
| E2 | LM3b D.5 in class two | Proved | correct | V, R |
| E3 | last layers fixed, non-inertia for r ≥ 3; full group open | Open | open as stated | S, R |
| D14 | p-adic good marked reduction, prime-to-p quotient | Proved | correct | S |
| D15 | full group, bad reduction | Open | open as stated | O |
| E4 | H2(a) (= Stix Thm. 20); H2(b) open | Open | open as stated | S |

Checked fully (V): A1–A7, A9, AE1, AE2, AE4, B1, B2, B6, B7–B9, C2, C3, C6, C8, D0b, D1–D7, E1, E2. By spot check (S):
A8, B3–B5, B12, C1, C4, C5, C7, C9, C10, B10, D0a, D8, D9, D14, E3, E4. In outline only (O): B11, D10–D13, D15, AE3.
None unread.

## 2. Decisive results

**A1 and Ribet (Part A(a)).** Ribet's appendix ("Torsion points of abelian varieties in cyclotomic extensions",
L'Enseignement Math. 27 (1981), 315–319) has: k a number field, K the field obtained by adjoining to k all roots of
unity, A/k an abelian variety; *Theorem 1: the torsion subgroup of A(K) is finite*, equivalent to Theorems 2–3
(A[p]^H = 0 for almost all p; V_p^H = 0 for every p, H = Gal(k̄/K)). The paper quotes it correctly. The descent is
right: a finite F′/K(μ∞) is k₁(μ∞) for the number field k₁ generated over K by generators of F′/F and the
coefficients of A (k₁ ⊂ F′ and μ∞ ⊂ F′ give one inclusion, F ⊂ k₁(μ∞) the other), and A = A₁ ⊗ F′. Theorem 3 gives
T(A)^{Γ_{F′}} = 0 directly; the paper derives it from finiteness, also correctly. The divisible-point argument
(finite non-empty sets of n!-division points, the Kummer cocycle killed on the normal subgroup Γ_{F′}, hence
divisibility over k₁, then reduction at a good place) and the unit argument (t ∈ Q with t − 1 = d·u, giving
d[f] = 0 in H¹(Q, Ẑ(1)), then finiteness of algebraic integers with bounded conjugates) are complete. Parts (iii) and
(v) are Stix's Lemma 19 and Lemma 32 / Corollary 33 (arXiv numbering), which are worded for "a number field k with
kQ^ab/Q^ab finite" and make sense only for algebraic k, as the reader said.

**A2–A7: R2.** A2 is Stix's Proposition 11 and Corollaries 12–13 with (3.1); the local argument (three cusps, the
diagonal) is right. A3 is Nakamura's Lemma (2.1.4) for the full class in another form; the proof (ℓ-Sylow of a
cyclic group generated by subgroups; compactness over levels; commuting ℓ-parts lie in one I_c) is complete. A4 is
R2's steps (1)–(3); I checked the open stabilizer of H, the covering H·s(Γ_{K′}) over K′, the vanishing in T(J_{X_H})
by A1, and the proper and affine conclusions. **A5 is a complete repair of step (4).** Step (4) as written in the war
game needs an open H ⊇ C separating two cusps x, y, which does not exist when y ∈ C·x. A5: if B (every nontrivial
element inertia) is not in one I_c, the set 𝒯 of cusps with B ∩ I_c ≠ 1 is not one B-orbit (else B = ⋃ conjugates of
the proper closed J_c, impossible in a finite quotient by Jordan's lemma); two cusps in distinct B-orbits stay
distinct at a level N; H = BN; if H has two cusps, X_H has genus ≥ 1 and a degree-2 étale cover (B dies in π₁(X_H))
gives four; with z, z′ and the classes a e_c, b e_{c′} in (A.1), zz′ and z²z′ must each lie in one line modulo the
diagonal, which forces a = b and 2a = b, so a = 0. I checked each case (three and four cusps; no zero-divisor
issue in Ẑ). A6 follows from A4 and A5 by normality of Γ°. Its second proof is the reader's route (I): over F, Stix's
Theorem 14 with Remark 15(2) (hypothesis: no divisible points, A1) gives the unique lifted cusp. **A6 is known in
substance**: Stix's Corollary 22 over a field distinguishing tori from abelian varieties (here F′, by A1(iii)) says
that s|Γ_F is cuspidal iff s(Γ_F) cyclotomically normalizes, here centralizes, a procyclic subgroup; Theorem 14 and the
last lines of its proof make the lifted cusp unique, hence C(s) = I_c. The formula C(s) = I_c itself is not stated in
Stix; no source I searched states it (§3). A7's formula (A.2) follows: in the cuspidal case C(s(Δ)) ⊂ I_c, where the
action is χ and Z_ℓ is a domain. AE1 (specialization of torsion points through the finite étale 𝒜[n] over a normal
model, evaluation at a closed point, Ribet for the residue field) and its divisible-point form are correct.

**B1–B2: R3 and the Hilbertian criterion.** B1 checked line by line: F(x) = F(σx) from equal stabilizers; split
primes from values of polynomials (no Chebotarev); p split in k′ and unramified in k, so the value group of F at
𝔭 is (1/(p−1))Z[1/p]; ℓ ∤ p(p−1); σα = cα^j by the τ-eigenspaces; 0 = ℓv(c) + j contradicts ℓv(F*) ∩ Z = ℓZ; then
every k″(μ∞). Complete. B2 checked against the opened texts: Jarden, *Almost locally free fields* (J. Algebra 335
(2011)), Proposition 2.5: K Hilbertian, N/K Galois and not separably closed ⇒ Gal(N) almost locally free (almost all
e-tuples generate a free profinite group of rank e); Haran–Jarden, Ann. Sci. ENS 24 (1991), Corollary 2.5: the
separable closure of a Hilbertian K is not the compositum of two Galois extensions neither equal to it (from Theorem
2.4). The derivation (no abelian normal closed subgroup; C ∩ H = Z(H) = 1; two proper Galois fields with compositum
K_s) is right. **B2 is known**: Minamide–Tsujimura, Theorem 2.12 (K Hilbertian ⇒ G_K strongly internally
indecomposable) with Proposition 1.2 (internally indecomposable ⟺ every nontrivial normal closed subgroup has
trivial centralizer); their proof uses Fried–Jarden Prop. 16.11.6 and Weissauer. The return's source audit records
finding this preprint in its search; the paper does not cite it.

**B7–B9 and scan 127.** The transcription and the image agree: "(32) (𝓔_L^{L̄})^{Γ⁰} = (1)" and "(33)
(π_{L/K}^{L̄})^{Γ⁰} = (1)", both with L, for "la section définie par x", x ∈ U rational over K (I read the crops of
the image myself). B7 is correct: compatible unique cusps c_V (A6 at each hyperbolic V ⊂ U₀, Stix Prop. 11 for
compatibility), the valuation ring as a directed union, I_v ⊂ C by Stix Lemma 10 and the cyclotomic action, the
reverse inclusion by the inverse limit. B8: for a section in D_v both groups equal I_v ≠ 1, so (32) and (33) are
false with L; through q_U: E_L → E_U, which kills I_v when x ∈ U, the section becomes the point section s_x and both
groups are 1 (A6, Stix Thm. 14(2); C6 in higher dimension). The example is right: K = Q, L = Q(t), place t = 0, the
tangential splitting by t^{1/n}, U = P¹ ∖ {1, 2, ∞} ∋ 0. B6 gives the equivalence (32) ⟺ (33). His own margin on the
same page, "𝓔_L^{(𝓔_K^0)} ≃ I_V" for a section through N_V, contradicts (32) with L; with "par dévissage … de la
conjecture analogue déjà faite pour la dim relative 1" this supports U as the letter meant. The return keeps L in
the transcription and corrects only the mathematics; that is right. B9 is formal from B7.

**C2–C3.** C2: injectivity (C(s′) = hC(s)h⁻¹ = I_c ⇒ h ∈ N_π(I_c) = I_c), different cusps (I_{c′} = I_{hc}), points
(C(s_x) = 1 needs that point sections are not cuspidal: Stix Thm. 14(2) over number fields, hypothesis by
Mordell–Weil, Remark 46; or the positive-genus neighbourhood, which the return builds: Fermat quartic in genus 0, a
double cover branched at two cusps in genus 1). Type (0,3) is included. This is known (Stix Thm. 14(2); Esnault–Hai)
and the centralizer route is a second proof. C3: on G_m the decomposition groups at 0 and ∞ are all of E_U =
Ẑ(1) ⋊ Γ_K, so each packet is the whole H¹(K, Ẑ(1)) and contains every point section; C(s) = Ẑ(1) for every s.
Correct. The scan supports it in a way the return does not note: on scan 55 he proves the first assertion "en
bouchant le trou i", that is, by injectivity for U ∪ {i}; for type (0,2), U ∪ {i} is of type (0,1), simply connected,
which is the obstruction he himself names for (0,3) in the second assertion.

**D4 (the degree-81 cover).** Rerun identical; recomputed by my own code (my own arithmetic in Q[a]/(a⁶ − a³ + 1),
my own group law on Y² = X³ − 432): P = (ζ₁₈, ζ₁₈⁻¹) has order 9 and 3P = (0, 12√−3); the nine Q_ij − P over ζ₆⁻¹ all
have order 9 with 3(Q_ij − P) = 3P; over ζ₆ the orders are 1, 3, …, 3. The arithmetic bound is right: the Frobenius at
7 acts on the free rank-one Z₃[ω]-module T₃E by α = 1 + 3ω (or ᾱ; #E(F₇) = 9, a₇ = −1), complex conjugation is
semilinear, so the commutator lies in G_{Q^ab} and acts by ᾱ/α; hence (α − ᾱ)R = 0 for R ∈ E(Q^ab)[3^∞]. The paper
concludes 9R = 0. Sharper and exact: α − ᾱ = 3√−3 is (1 − ω)³ times a unit, so E(Q^ab)[3^∞] ⊂ E[(1 − ω)³], of order
27; my code shows that ⟨P⟩ + E[3] has 27 points, all over Q(ζ₁₈), with (1 − ω)³-level 3; so **E(Q(μ∞))[3^∞] =
E[(1 − ω)³] ≅ Z/9 × Z/3**. This is known: Chou, Pacific J. Math. 302 (2019), Table 2, lists E(Q^ab)_tors = Z/3 × Z/9
for the curves 27a1 and 27a3 (j = 0); Y² = X³ − 432 is the Fermat cubic, conductor 27, j = 0. (The return's own
program prints the kernel size 27.) Then a point R of the degree-81 cover over ζ₆⁻¹ would satisfy 3R = Q_ij − P of
order 9, whereas 3·E[(1 − ω)³] = E[1 − ω] has exponent 3. The fibre over ζ₆ contains O. So the G_F-sets differ and
the two point sections over Q(μ∞) are not conjugate. Correct. The abstract statement (point-section injectivity
over Q(μ∞)) is D2, known (Tsujimura 2023, Prop. 4.2; Q(μ∞) is AVKF by Ribet); D4 is an explicit witness, and D3
shows that the two-step covers the prompt asked for cannot be one (the bijection w′ = ζ⁻²w⁻¹, u′ = λ_w u; rerun of
7,800 cases identical).

**D5 (Conjecture A over Q(μ∞)).** No point: at a place over 2 of Q(μ_N) the ramification index is 2^{r−1} (2^r ∥ N),
prime to 3, so the valuations of X³, 2Y³, 4Z³ are ≡ 0, e, 2e (mod 3), pairwise distinct; the minimum is attained
once; X³ + 2Y³ + 4Z³ ≠ 0. This is Clark 2006, Theorem 1 (p ≡ −1 mod 3, p ∤ abc; here p = 2, a = b = c = 1), opened.
The map (t, y) ↦ (t² : y : 1) carries C to this cubic, so C(Q^ab) = ∅. Genus: y³ = −(t⁶ + 4)/2 with t⁶ + 4 squarefree
of degree 6, three unramified points at infinity; 2g − 2 = 3(−2) + 6·2, g = 4 (my code also by the superelliptic
formula). Section: **yes, its existence follows from cd(G_{Q^ab}) ≤ 1 alone.** G_F (F = Q(μ∞) = Q^ab) has
cohomological dimension 1, so it is projective, and every continuous epimorphism of profinite groups onto it splits;
π₁(C) → G_F is one. The return's argument (Brauer vanishing over every finite L/F, H² vanishing for finite modules,
Frattini and finite embedding problems, recursive lifting along characteristic subgroups) is a correct proof of
exactly that fact. **The content of D5 is a curve of genus ≥ 2 over Q^ab without points.** Such curves are in Clark
2006 (Theorem 4: for every g ≥ 4 a curve over Q of genus g without Q^ab-points; Frey 1973 first gave a variety without
abelian points); Clark's footnote 6 cites Serre, Galois Cohomology II.3.3, Prop. 9, for Br(Q^ab) = 0 (not opened).
The deduction "Conjecture A fails over Q^ab" I did not find stated (§3). Over scan 62 it answers his question as
written: an action of Γ° that does not come from Γ need not have a fixed point.

**AE2/AE4 and E1–E2.** AE2 is right: the A4 construction under (E.1) puts every nontrivial z ∈ C_Δ in inertia, A5
puts C_Δ in one I_c, s(Δ) fixes c, and C_Δ = I_c^{χ(Δ)} = ∏_{ℓ: χ_ℓ|Δ=1} Z_ℓ(1); for normal Δ the no-divisible-points
property over every finite extension of K̄^Δ (cocycle on the normal subgroup) and Stix Thm. 14 over K̄^Δ give a unique
fixed cusp even when P_Δ = ∅. AE4: Δ = G_{Q(μ_{3^∞})} satisfies (E.1) (it contains G_{Q(μ∞)}), χ_q|Δ = Z_q* ≠ 1 for
q ≠ 3, χ₃|Δ = 1; for the tangential section at 0, C = Z₃(1) ≠ 1; H1 ("C = I_x exactly when χ is trivial on Δ")
is false. This is the correction the reader proposed in the R149 notes, now proved. E1: Δ = G_{Q(i)^ab} acts
trivially on V = T₅E (the two CM eigenlines carry characters of Γ_K^ab; 5 splits in Z[i]) and on Z = Λ²V; the
possible shear V → Z is excluded by the Galois-equivariant involution α = (local path t_n ↦ −t_n, valid because 5 is
odd) ∘ [−1], which is −1 on V and +1 on Z: an equivariant shear f would satisfy f = −f. So N₂^{s(Δ)} = N₂ and
N₂^{s(Γ°)} = Z ≅ Z₅(1); the image of the full C(s) = I_O is 0 in T(E) and the centre in N₂. E2 (LM3b D.5) is right:
y^r x^a c^d y^{−r} = x^a c^{d−ar} removes the central factor, primitivity gives maximality, all inertia lies in Z. The
"13,020 checks" verify that one-line Heisenberg identity modulo 5, 25, 125; they compute no Galois action.

## 3. New mathematics, with the literature searched

The return claims no priority. What I found new, in the sense that the searches below did not locate it:
- **A5**, a direct proof that a closed subgroup of π consisting of inertia elements lies in one inertia group (route
  proposed by the reader R-149; the degree-2 cover for the two-cusp case is the return's). The consequence A6 is
  known in substance (Stix over K(μ∞)).
- **A7 / AE2**, the primewise formula C(s(Δ)) = ∏_{ℓ: χ_ℓ|Δ=1} Z_ℓ(1), with AE4 refuting the war game's H1.
- **B7–B9**, the birational criterion in relative dimension one: a section of G_{K(X)} → G_K has C(s) ≠ 1 iff it
  lies in D_v of a rational place, and then C(s) = I_v; so his "conséquence" of scan 45 is, section by section, the
  birational section conjecture. A two-step limit of A6, as the reader predicted.
- **C8**, nonvanishing of the diagonal boundary inertia for every normal-crossings compactification of an
  elementary hyperbolic polycurve, by an explicit arc and Hoshi's valuative criterion.
- **D1**, the exact pairs of points with equal abelianized sections over finite extensions of Q(μ∞) (genus 0: S split
  and all h(a)/h(b) roots of unity). The equation of the U_{0,3} case is Stix's (9.2) in §9.6 (double ratios of
  divisible elements), used there for isomorphisms of fundamental groups, not for point sections.
- **D3, D4**: the requested two-step covers cannot separate ζ₆, ζ₆⁻¹, and an explicit degree-81 cover does. The
  torsion input is known (Chou 2019).
- **D6**, faithfulness of Théorème 2 over K(μ∞) through complex absolute values of f(a), f(a)+1, f(a)+i.
- **E1, E3**, the no-shear argument by the tangential involution in class two, and the fixed last layers with
  non-inertia elements for every class r ≥ 3 (the full group stays open).
Not new: A1–A3, A6, B2, C2, C5, D2, D5 (see the table), the 3-primary torsion of D4 (Chou), C10's counterexample
(FINDINGS F17; LM3 D.2), E4's proved part (Stix Thm. 20).

Searches (web, 12 Nov): "section conjecture fails over Q^ab cohomological dimension one curve without abelian points
sections exist" (found Clark 2006; no statement of the conclusion); "Hilbertian field absolute Galois group
nontrivial closed normal subgroup trivial centralizer" (found Minamide–Tsujimura; opened: Thm. 2.12, Prop. 1.2);
"centralizer of the image of the kernel of the cyclotomic character section hyperbolic curve cuspidal inertia group
anabelian" (only Stix's Cor. 22 and surveys; the formula C(s) = I_c not found); "Chou torsion of rational elliptic
curves over the maximal abelian extension of Q" (opened: Thm. 1.2, Table 2).

## 4. Credits the return omits

- **The reader R-149 (Claude Fable 5.2, effort max; `R149_NOTES_20261112.md`).** The A5 route (not one C-orbit by
  Jordan's lemma; two orbits separated; three cusps; zz′ and z²z′), which the prompt also prescribed in Part A(d)(II);
  the supplement to R3 that p must be unramified in k (B1's "two additions" do not name their origin); the primewise
  correction of H1 (AE2, AE4); the criterion of B7 (notes, item 7) and the L/U correction of (32)–(33) (item 8);
  the identification of R2 with Stix's Theorem 20, Corollary 22 and Theorem 14 over K(μ∞).
- **The transcriber's notes (GPT-6 Astra, ChatGPT Pro mode, effort Pro, first pass).** C054.4 (the (0,2) failure,
  = C3), C062.2 (ζ₆ and ζ₆⁻¹ coincide in the abelianized extension, the instance of D1), C061.2 (a unique Γ°-fixed
  point is Γ-fixed, the last step of D0b).
- **FINDINGS F17 and LM3 D.2** (scan 483 false as written: π itself) for C10's counterexample; FINDINGS F15
  (injectivity rests on the absence of divisible elements) for D1–D2.
- **Literature.** Stix's Corollary 22 (A6); Stix's Lemma 32 / Corollary 33 (A1(v)); Stix §9.6, (9.2) (D1);
  Minamide–Tsujimura, Thm. 2.12 (B2, found by the return and not cited); Chou 2019 (D4's torsion); Clark's Theorem 4,
  Frey 1973 and the cohomological dimension of Q^ab (D5; the return cites only Clark's Theorem 1).
- **Grothendieck.** C8's blow-up counterexample is his own margin of scan 130 ("visiblement faux « en général » pour
  card I(x) ≠ 1 … en y faisant éclater un pt de D"); the return says it confirms the withdrawal, which is fair.

## 5. Programs

| Program | Rerun (`python -I`) | Output vs shipped |
|---|---|---|
| A_boundary_checks.py | exit 0 | identical |
| B_field_certificates.py | exit 0 | identical except the version line |
| D_coverings.py | exit 0 | identical |
| D_cyclotomic_counterexample.py | exit 0 | identical |
| root_math_checks.py | exit 0 | JSON equal apart from the runtime entry |
| assemble_ledgers.py, prepare_paper.py (full copy) | exit 0 with `-X utf8` | CSVs, report, coverage, paper .tex, .bib, source audit identical |
| validate_bundle.py | exit 1 at its PDF first-page text check (local Poppler) | ledger assertions before it passed |

Without `-X utf8` the two ledger scripts fail on Windows (cp1252 cannot write Γ): an encoding default, not a defect of
the mathematics. Not run: fetch_root_sources.py (network), package_bundle.py (rewrites SHA256SUMS and the zip),
build_pdf.sh (LuaLaTeX), run_checks.py (wrapper of the five, which runs them without `-I`; run directly instead).

What the programs certify: D_coverings.py carries the only substantial computation (point orders in E(Q(ζ₁₈)),
#E(F₇), the Smith form (3, 9) of α − ᾱ, the 7,800 radicand cases). The others check finite identities that the proofs
already settle by hand (derangement counts, linear algebra modulo m, the Heisenberg identity, Lyndon-word ranks,
discriminants, S₅ derived series). None simulates a Galois action, as the return says.

My code (`rerun\indep\d4_d5_indep.py`, output `rerun\indep\out\d4_d5_indep.out`): the D4 orders by my own field and
group arithmetic; (1 − ω)³P = O; E[3] over Q(ω); |⟨P⟩ + E[3]| = 27 with exponent 9; Frobenius data for the 37 primes
p < 400, p ≡ 1 mod 3 (every β_p ≡ 1 mod 3 in Z[ω], v_{1−ω}(β_p − β̄_p) ≥ 3 with equality at 7); the D5 genus and the
2-adic residues. All pass.

## 6. Readings of the manuscript

| Place | Return's reading | Finding |
|---|---|---|
| 149 scan 45 | starred fact, "* à vérifier !"; E°_{K′} defined through a composite starting at E°_{K′} | confirmed in the checked transcription; the composite must start at E_{K′}; B1 proves the fact |
| scan 32 | Théorème 3 for X embedding in an extension of an abelian variety by a torus | confirmed; G_m is covered, so D7's counterexample applies over Q(μ∞) |
| scan 53–54 | Proposition with (g,ν) ≠ (0,0),(0,1); "centralisateur Z(L_i)"; (3) H¹(Γ,T) ≃ K̂* | confirmed; Z(L_i) must be the normalizer (C1) |
| scan 55 | (3) π^{Γ°} = L_i "hautement plausible"; "(donc π^Γ = (1))" | confirmed; A6, and A7 with Δ = Γ_K gives π^Γ = 1 |
| scan 55 (not in the return) | his proof of the first assertion "en bouchant le trou i" | uses injectivity on U ∪ {i}, of type (0,1) when U is of type (0,2): his proof breaks exactly where C3 refutes |
| scan 56 | Conjecture A; margin "précisions π^{Γ°} = (1) … = L_i (deux. cas)" | confirmed; "deux." = deuxième (doubts file) |
| scan 61 | Γ° has a unique fixed point, then fixed by Γ; π^{Γ°} ⊂ Norm_π(L_i) = L_i | confirmed; D0b, A2 |
| scans 61–62 | "tous nos beaux énoncés … dès que K est ext. de type fini d'un corps cyclotomique" | confirmed; existence fails (D5), uniqueness and centralizer statements survive |
| scan 62 | Poincaré curves isomorphic iff common finite étale cover | confirmed; D10 |
| scan 66 | "à ⟨deux⟩ cas. près" | the doubts file rates "deux" medium (first word faint, abbreviated). The mathematics gives no exceptional pair: the map from points to germs is injective with no exception (C2 over number fields; D2 over Q(μ∞)). So it offers no support for a reading naming two exceptional points; the return's "does not identify the omitted words" stands |
| scan 127 | (32), (33) with L; margin 𝓔_L^{(𝓔_K^0)} ≃ I_V | confirmed on the image; the margin contradicts (32) with L; U is supported mathematically, not as a reading |
| scan 130 | 1°) injectivity of I_x ≃ T^{I(x)} → π, withdrawn in the margin | confirmed: "visiblement faux « en général » pour card I(x) ≠ 1", by blowing up a point of D; C8 is that example |

Not checked by me: scans 13–15, 22, 48–49, 59, 131; Longue Marche scans 433, 483; the PS of the letter to Faltings.

## 7. Prompt changes

The texts below are for whoever edits the prompts; I changed no prompt file. The paragraph "New since this prompt
was drafted: the return CYCLOTOMIC_KERNEL" is the same in both prompts. **Is it accurate?** Yes, with five
differences: (1) "not yet reviewed" is now out of date; (2) "the Proposition fails for type (0,2)": only its first
assertion fails (the second excludes (0,2) itself); (3) it does not say which results are known (R2 = Stix over K(μ∞);
C2 = Stix Thm. 14(2); D2 = Tsujimura; B2 = Minamide–Tsujimura; D5's curve = Clark); (4) D4's torsion bound is exact
and known: E(Q(μ∞))[3^∞] = Z/9 × Z/3 (Chou 2019); (5) it omits results that settle rows of each prompt (FLAGGED F2, F3,
F6, F25; in LM6 the uniqueness at finite distance, F(b)(1), (3), (4), F(d) for B′, A(e)). The remark on D5 ("the
content of D5 is the curve without points") is right.

### FLAGGED_149 (`grothendieck_archive_montpellier\pro_prompts_archive_20261112\FLAGGED_149\PROMPT.md`)

Replace lines 59–88 (from "**New since this prompt was drafted" to "say so with the proof.") by:

> **New since this prompt was drafted: the return CYCLOTOMIC_KERNEL** (attached as `FLAGGED_149_new_results.zip`,
> folder `CYCLOTOMIC_KERNEL_return/`: 52-page paper, results and readings ledgers, report, source audit, programs with
> outputs; GPT-6 Astra, ChatGPT Pro mode, 12 November 2026), reviewed statement by statement by Claude Opus 5.5 at
> effort max (`CYCLOTOMIC_REVIEW.md`, 12 November 2026: no statement wrong; 9 of 56 known in the literature; D13, E3,
> D15, E4 open). The review is not authority either: check what you use, and cite the return's statements by number.
> Where it bears here:
> - **F8 (scan 45): proved.** B1 (elementary; the auxiliary prime must be unramified in `k` as well as split in
>   `k′`) and B2: over a Hilbertian field every nontrivial closed normal subgroup of `G_k` has trivial centralizer.
>   B2 is known: Minamide–Tsujimura, *Internal indecomposability of profinite groups* (2022), Theorem 2.12 with
>   Proposition 1.2; the return derives it from Jarden 2011, Proposition 2.5, and Haran–Jarden 1991, Corollary 2.5.
>   Cite them; do not redo.
> - **F2 (scan 14), first claim:** an open normal subgroup of `Γ_Q` has trivial centralizer in `Γ_Q` (B2), hence
>   trivial centre. The claims on elements of finite order and on the centralizer of τ remain for you.
> - **F3 (scans 14–15):** B5 proves that "every open subgroup has trivial centralizer" passes to extensions and to
>   projective limits with surjective transition maps, holds for free profinite groups of rank ≥ 2 (centre: Nakamura
>   1994, Corollary (1.3.4); torsion-freeness proved there), and fails in rank one; B4 and B12 give the field
>   statements. What remains of F3 is the surface-group case of scan 28.
> - **F6 (scan 34):** D7 proves, over any field of characteristic 0, that the Kummer classes of two points of a
>   semiabelian variety agree iff their difference is divisible in the group of rational points; with FINDINGS F15
>   this gives Théorème 3 over fields finitely generated over `Q`. Over `Q(μ_∞)` it fails (D7: the points 1 and `ζ_6`
>   of `G_m`); D1 gives the exact pairs for hyperbolic curves in the abelianized extension.
> - **F10 (scan 54):** the first assertion of the Proposition fails for type `(0,2)` (C3, on `G_m`; transcriber's note
>   C054.4); his own proof on scan 55 ("en bouchant le trou i") needs injectivity on `U ∪ {i}`, of type `(0,1)` there.
>   The second assertion holds for every hyperbolic type, `(0,3)` included (C2; known: Stix 2008, Theorem 14 (2), and
>   Esnault–Hai). `Z(L_i)` is the normalizer (C1).
> - **F24 (scan 127):** (32) and (33) are equivalent (B6) and false with `L` for every section through the
>   decomposition group of a rational place, where both equal `I_v` (B7, B8; example `L = Q(t)`, place `t = 0`, model
>   `U = P¹ ∖ {1, 2, ∞}`); with `U` in place of `L` both are trivial (B8 for curves, C6 for elementary `U`). The scan
>   has `L` in both (checked on the image by the reader and again in the review); his margin on the same page,
>   `𝓔_L^{(𝓔_K^0)} ≃ I_V`, contradicts (32) with `L`.
> - **F25 (scans 130–131), 1°):** C8 proves that the diagonal of `T^{I(x)}` has nonzero image in `π_1` for every
>   normal-crossings compactification of an elementary hyperbolic polycurve, and that injectivity fails after
>   blowing up a point of `D` on `(P¹ ∖ {0,1,∞})²` (the map is `(m, n) ↦ m + n`): his own example of the margin. The
>   minimal-model question and 2°) remain for you.
> - Also proved there, for citation: R2 (A1–A7, AE1: `C(s) = I_c` for `s` cuspidal at the unique lifted cusp `c`,
>   trivial otherwise and for proper curves; in substance Stix 2008, Corollary 22 and Theorem 14 over `K(μ_∞)`, with
>   Ribet's Theorem 1); the primewise form of H1 (AE2; AE4: `Δ = G_{Q(μ_{3^∞})}` gives `Z_3(1)`); at most one fixed
>   pro-point for `Γ°` (D0b) and point-section injectivity over finite extensions of `K(μ_∞)` (D2; known: Tsujimura
>   2023, Proposition 4.2); D4, a connected cover of degree 81 on the Fermat cubic separating `ζ_6` and `ζ_6^{-1}` on
>   `U_{0,3}` over `Q(μ_∞)` (its torsion input is exact and known: `E(Q^ab)_tors = Z/3 × Z/9` for this curve, Chou
>   2019); Conjecture A extended to `Q(μ_∞)` is false (D5). `Q(μ_∞) = Q^ab` has cohomological dimension 1, so every
>   variety over it has sections; the content of D5 is a curve without points, which Clark 2006 supplies (Theorem 1:
>   `X³ + 2Y³ + 4Z³ = 0`; Theorem 4: curves over `Q` of every genus ≥ 4 without `Q^ab`-points).
> - Left open there: A(b) (collation with the publisher's version of Stix), D(e) (an unrestricted number-field action
>   normalizing no deck group; the affine automorphism group), E(d) (full-group and bad-reduction cases), H2(b) (E4),
>   the surjectivity of points onto zero-centralizer sections for `U_{0,3}/Q` and for an arbitrary section of
>   `Q(t)/Q`, and the lift obstruction of E3.
> Where a row of this prompt is settled by one of these, cite the statement and give the work to what remains; where
> you find one wrong, say so with the proof.

### LM6_POINTS_AS_SECTIONS (`longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM6_POINTS_AS_SECTIONS\PROMPT.md`)

Replace lines 47–76 (the same paragraph) by:

> **New since this prompt was drafted: the return CYCLOTOMIC_KERNEL** (attached as
> `LM6_POINTS_AS_SECTIONS_new_results.zip`, folder `CYCLOTOMIC_KERNEL_return/`: 52-page paper, results and readings
> ledgers, report, source audit, programs with outputs; GPT-6 Astra, ChatGPT Pro mode, 12 November 2026), reviewed
> statement by statement by Claude Opus 5.5 at effort max (`CYCLOTOMIC_REVIEW.md`, 12 November 2026: no statement
> wrong; 9 of 56 known in the literature; D13, E3, D15, E4 open). The review is not authority either: check what you
> use, and cite the return's statements by number. Where it bears here:
> - **R2, R3 (Part F (b), (c)).** R2 is proved (A1–A7; A5 repairs step (4); AE1 for fields finitely generated over
>   `Q`); in substance it is Stix 2008, Corollary 22 and Theorem 14 over `K(μ_∞)`, with Ribet's Theorem 1. The
>   "précisions" hold for sections and germs (C4, A7). R3 is B1; B2 (known: Minamide–Tsujimura 2022, Theorem 2.12):
>   over a Hilbertian field every nontrivial closed normal subgroup of `G_k` has trivial centralizer; B6 makes the two
>   readings of "centralisateur" equivalent.
> - **F (b) (1), (3), (4).** a) ⇒ b) of the Conjecture fondamentale: C6 (U elementary over a number field, V any
>   connected scheme of finite type over `Q`; regularity not needed; both readings). For `V` a point and `U` a curve,
>   b) holds exactly for the noncuspidal sections (C7), so (F1) is (F2) over all finite extensions. Sections through a
>   cusp have `C(s) = I_c ≠ 1` (A6, C4); in higher dimension, sections through a boundary point have nonzero `C(s)`
>   (C8).
> - **F (d).** Uniqueness of the fixed points of `Γ°` is proved: at most one fixed pro-point in all, for sections over
>   finite extensions of `K(μ_∞)`, and the `Γ°`- and `Γ`-fixed sets coincide (D0b); point-section injectivity over
>   `K(μ_∞)` (D2; known: Tsujimura 2023, Proposition 4.2, `K(μ_∞)` being AVKF by Ribet). So the last item of the list
>   in "How this prompt stands on them" (uniqueness at finite distance on affine curves) is settled. In the
>   abelianized extension it fails, with the exact pairs in D1; the two-step covers `w^n = z`, `u^m = 1 − ζw` do not
>   separate `ζ_6`, `ζ_6^{-1}` (D3); a cover of degree 81 does (D4). For B′: D10 (common finite étale covers), D11
>   (with the continuity of scan 59, B′ is B for `Γ°` over all finite extensions), D12 (proper curves: the
>   automorphism group of the pro-curve is the completion of the commensurator); without continuity it is open (D13).
> - **F (e) (1).** B7–B9: in transcendence degree 1 a section lies in the decomposition group of a rational place iff
>   its `C(s)` is nontrivial, and then `C(s) = I_v`; (32), (33) are false with `L` and true with `U` (the scan has `L`;
>   his margin on the same page contradicts it); B10–B11 for the packets of scan 57.
> - **Part A (e) and F (f).** E1: for `y² = x³ − x` over `Q(i)` and `Δ = G_{Q(i)^ab}`, `Δ` fixes all of the class-two
>   pro-5 quotient (no shear, by a Galois-equivariant tangential involution), `Γ°` fixes its centre; E2 confirms LM3b
>   D.5 in class two; E3: every last layer `γ_r/γ_{r+1}` is fixed by `Δ` and contains non-inertia fixed elements for
>   `r ≥ 3`; the full group, and LM3b D.4, stay open. E4 proves H2 (a) (Stix's Theorem 20) and leaves H2 (b) open, with
>   the genus-2 CM test of F (f) (6) not done.
> - **Over cyclotomic bases.** Conjecture A extended to `Q(μ_∞)` is false (D5). `Q(μ_∞) = Q^ab` has cohomological
>   dimension 1, so every variety over it has sections; the content of D5 is a curve without points, which Clark 2006
>   supplies (Theorem 1: `X³ + 2Y³ + 4Z³ = 0`; Theorem 4: curves over `Q` of every genus ≥ 4 without `Q^ab`-points).
>   The primewise form of H1: AE2, AE4.
> - Left open there: A(b) (collation with the publisher's version of Stix), D(e) (an unrestricted number-field action
>   normalizing no deck group; the affine automorphism group), E(d) (full-group and bad-reduction cases), H2(b), the
>   surjectivity of points onto zero-centralizer sections for `U_{0,3}/Q` and for an arbitrary section of `Q(t)/Q`,
>   and the lift obstruction of E3.
> Where a row or part of this prompt is settled by one of these, cite the statement and give the work to what
> remains; where you find one wrong, say so with the proof.

And in line 45 ("How this prompt stands on them"), replace ", and the uniqueness of the fixed points of `Γ°` at finite
distance on affine curves." by ". The uniqueness of the fixed points of `Γ°` at finite distance on affine curves, also
listed here when this prompt was drafted, is now a theorem (CYCLOTOMIC_KERNEL D0b, D2)."

### Outside the prompts

CYCLOTOMIC_KERNEL's A(b) (the published version of Stix's paper) is still to be collated; nothing in this review
depends on it. The open items D13, E3, D15 and E4 are already listed in both replacement texts.

## 8. Limits of this review

Not opened by me: Stix 2012 (both versions), Esnault–Hai (published), Tsujimura 2023, Hoshi–Mochizuki–Tsujimura,
Murotani–Ozeki, Hoshi 2014, Bresciani, Carlson–Corwin, Džambić–González-Diez, Kodani and Ihara, Mochizuki 2004,
Tamagawa 1997, Milne, Serre's Galois Cohomology, Fried–Jarden; their statements were taken as the return and the
sources above quote them. D10–D13, D15, B11 and AE3 were read in outline. The PDF was not compiled or inspected. The
transcription was used as is; scan 127 was also read on the image.

## 9. Findings

**F1. No statement is wrong.** 43 correct, 9 known, 4 open as stated, 0 with a gap, 0 wrong. The return's 5
refutations (C3, B8, D5, D7, AE4) are all correct.

**F2. R2 holds, and A5's repair is complete.** A1–A7 and AE1 are correct; A5 closes the gap of step (4) (two cusps in
one C-orbit) by Jordan's lemma, separation of orbits, a degree-2 cover when only two cusps remain, and the products
zz′, z²z′ with three cusps. In substance R2 is Stix 2008, Corollary 22 and Theorem 14 applied over K(μ∞), with
Ribet; the exact formula C(s) = I_c was not found stated.

**F3. Ribet's Theorem 1 is quoted correctly and the descent is right.** Opened: k a number field, K = k(μ∞),
A(K)_tors finite (and Theorem 3: V_p^H = 0). Every finite F′/K(μ∞) is k₁(μ∞) for a number field k₁ ⊂ F′; A1's five
assertions follow as written.

**F4. B2 is known.** Every nontrivial closed normal subgroup of the absolute Galois group of a Hilbertian field has
trivial centralizer: Minamide–Tsujimura (2022), Theorem 2.12 with Proposition 1.2. The return's derivation from Jarden
2011 Prop. 2.5 and Haran–Jarden 1991 Cor. 2.5 is correct (both opened); its source audit found Minamide–Tsujimura but
the paper does not cite it. B1 is a special case, with a correct elementary proof.

**F5. Scan 127: (32) and (33) are false with L and true through E_L → E_U.** Both letters are L on the image. For a
section through D_v of a rational place both groups equal I_v (B7, B8); through q_U, which kills I_v when the point
lies in U, both are trivial. The example L = Q(t), v = (t = 0), U = P¹ ∖ {1, 2, ∞} is right. His own margin on the
page gives I_V and so contradicts (32) with L.

**F6. C2 (known) and C3 (correct).** Cusp packets are injective, pairwise disjoint and disjoint from point sections
for every hyperbolic type, (0,3) included (Stix Thm. 14(2); Esnault–Hai). On G_m both packets are everything. His own
proof of the first assertion (scan 55, "en bouchant le trou") fails at (0,2) for the reason he gives at (0,3).

**F7. D4 is correct, and its torsion bound is exact and known.** E(Q(μ∞))[3^∞] = E[(1 − ω)³] ≅ Z/9 × Z/3, defined
over Q(ζ₁₈) (my code; Chou 2019, Table 2, for 27a1 and 27a3). The return proves "killed by 9", which suffices.

**F8. D5: sections over Q^ab come from cd(G_{Q^ab}) ≤ 1 alone.** The content of D5 is a curve of genus ≥ 2 without
Q^ab-points; its cubic is Clark 2006, Theorem 1 (p = 2), and Clark's Theorem 4 gives such curves in every genus ≥ 4.
The return's section-existence proof is a correct derivation of the projectivity of G_{Q^ab}. The curve has genus 4
and no point over any Q(μ_N) (checked).

**F9. H1 as written is false; the primewise form is proved.** AE2: C_Δ = ∏_{ℓ: χ_ℓ|Δ=1} Z_ℓ(1) inside the inertia of a
unique cusp; for normal Δ a fixed cusp makes s cuspidal even when the product is empty. AE4: Δ = G_{Q(μ_{3^∞})}, the
tangent at 0 on U_{0,3}, C = Z₃(1). This is the reader's correction, proved.

**F10. E1–E2 are correct; the 13,020 checks verify one identity.** The class-two result rests on the tangential
involution (−1 on V, +1 on the centre), which excludes a shear; the program checks y^r x^a c^d y^{−r} = x^a c^{d−ar}
modulo 5, 25, 125.

**F11. Every program reruns.** The five mathematical programs give identical outputs under `python -I`; the ledger and
paper scripts regenerate the shipped CSVs, report and .tex byte for byte (with `-X utf8` on Windows).

**F12. Credits omitted.** The reader R-149 (A5's route, R3's supplement, H1's correction, B7, the L/U correction, the
identification with Stix), the transcriber's notes C054.4, C062.2, C061.2, FINDINGS F17/F15 and LM3 D.2, and the
sources Stix Cor. 22, Lemma 32, §9.6, Minamide–Tsujimura, Chou, Clark's Theorem 4 (§4).

**F13. Scan 66.** The mathematics gives no exceptional pair in the map from points to germs (C2, D2), so it offers no
support for reading "à deux cas près" as two exceptional points; the reading stays doubtful.

**F14. The prompt paragraphs are accurate but out of date.** Both say "not yet reviewed", say the scan-54 Proposition
fails for (0,2) where only its first assertion does, name no known statuses, and omit results that settle rows:
FLAGGED F2, F3, F6, F25; LM6's uniqueness at finite distance, F(b)(1), (3), (4), F(d) for B′, A(e). Replacement texts
in §7.
