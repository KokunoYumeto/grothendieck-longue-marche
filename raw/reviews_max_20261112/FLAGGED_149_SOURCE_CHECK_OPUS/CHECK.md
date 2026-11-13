# FLAGGED_149, F17.6–F17.7: check of the cited sources

Checker: Claude Opus 5.5, effort max, no sub-agents. 13 November 2026.
Return checked: GPT-6 Astra (ChatGPT Pro mode), FLAGGED_149, `sections\F_agent.tex` lines 597–1011 (F17.6, F17.7),
with the bibliography `FLAGGED_149_references.bib` and the return's own source audit `audit\CF_sources.md`.
Intake this check completes: `..\FLAGGED_149_REVIEW_FABLE\REVIEW.md` (Claude Fable 5.2), which followed every step
and opened no source.

## Result

Every cited place says what the return uses it for. In each case the hypotheses hold in the return's setting:

- a henselian DVR (completed by the return before Hoshi is applied);
- a residue field finitely generated over ℚ, so characteristic 0 and the set of all primes;
- marked stable curves;
- any continuous splitting.

| # | Place | Exact work | Verdict |
|---|---|---|---|
| 1 | Illusie, Thm 7.6 | Astérisque 279 (2002) 271–322, pp. 305–306 | matches |
| 2 | Hoshi, Cor. 3.9 | RIMS-1558, July 2006 (published Hiroshima Math. J. 39 (2009) 61–121), p. 31 | matches; needs a complete base, which the return arranges |
| 3 | Mochizuki, Example 2.5 | combinatorial Grothendieck conjecture, April 2007 author version (Tohoku 59 (2007)), pp. 21–22 | matches, after one routine identification (B2 below) |
| 4 | Mochizuki, Prop. 1.2 (i)–(ii) | same, pp. 8–9 | matches |
| 5 | Hoshi–Mochizuki, Def. 2.10(iv), Lemma 2.11(ii)–(iii), Rem. 2.14.1 | nodally nondegenerate outer representations, December 2011 author version, pp. 30–36 | matches for the minimal log structure over an algebraically closed field; the transfer to the return's case is a routine base change (B3) |
| 6 | Stix, Thm 20 | arXiv:0809.0017v1 (the only arXiv version), p. 7 | matches, with the added hypothesis "k distinguishes tori from abelian varieties": the setting meets it, but the return proves it from its own earlier AI return (A1 below) |
| 7 | Stix, Cor. 21 | same, p. 8 | matches in substance (same added hypothesis); the count the return draws comes from Thm 20 together with Stix Cor. 13 |
| 8 | Tamagawa, Thm (5.3) | Compositio 109 (1997) 135–194, p. 177; also Rem. (5.2), Thm (0.8) | matches |
| 9 | Knudsen, Thm 2.7 | Math. Scand. 52 (1983) 161–199, p. 179 | matches; the return uses standard consequences of properness and separatedness, which the theorem does not state itself |

**F17.6–F17.7 stand as a theorem on these sources.** Taken with the return's own arguments, the sources prove:

- F17.6: with stable bad reduction, no residue outer action is that of a smooth hyperbolic curve over k, for any
  splitting and after any finite extension of k;
- F17.7: condition e) for one splitting, condition e) for every splitting, and potentially good marked reduction are
  equivalent.

What a fully cited version still needs is listed below under "What is missing". None of it is a mathematical gap.

## Sources opened

Local copies, read as text with page images where the text was garbled:

- Mochizuki, *A combinatorial version of the Grothendieck conjecture*, April 2007:
  `Free or receipted\free\lm-expert-20261112\mochizuki-combgc\combgc.pdf`.
- Hoshi–Mochizuki, *On the combinatorial anabelian geometry of nodally nondegenerate outer representations*,
  December 2011: `...\hoshi-mochizuki-nodnon\nodnon.pdf`.
- Stix, *On cuspidal sections of algebraic fundamental groups*, arXiv:0809.0017v1, 29 August 2008:
  `...\stix-cuspidal\stix_cuspidal_sections_arxiv_0809.0017.pdf`. Page 7 was rendered to check the overlines:
  `work\stix_p-07.png`.
- Tamagawa, *The Grothendieck conjecture for affine curves*, publisher PDF:
  `...\tamagawa-1997-affine\tamagawa_affine_curves.pdf`.

Fetched for this check, each in its own folder under `sources\`, read as untrusted data:

| Folder | Work | URL | SHA-256 |
|---|---|---|---|
| `illusie2002_numdam` | Illusie, *An overview of the work of K. Fujiwara, K. Kato, and C. Nakayama on logarithmic étale cohomology* | numdam.org/item/AST_2002__279__271_0.pdf | 9d708353a45f30e7db0e41605f827e36065d3e7a1ee2a0c2490694a4d15661d0 |
| `hoshi2009_rims1558` | Hoshi, *The exactness of the log homotopy sequence*, RIMS-1558, July 2006 | kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf | 2dc433bbe1bc08a34e66213ac31ee00778a4cc2504e1e9702a2fa19ef8d210fe |
| `knudsen1983_mscand` | Knudsen, *The projectivity of the moduli space of stable curves, II*, journal scan; p. 179 viewed as an image (`p-19.png`) | journals.msp.org/mscand/article/download/1622/1621 | 18e04bbf5c24a460ff10e965ebf665ea0229378c6a9521bd279909476012e230 |
| `mochizuki1999_extending` | Mochizuki, *Extending families of curves over log regular schemes*, J. reine angew. Math. 511 (1999), author PDF; opened for the published proof of log purity | kurims.kyoto-u.ac.jp/~motizuki/Extending Families of Curves over Log Regular Schemes.pdf | 4e9d0fe36ee7e3a496e26eaa7155b0a244ec67d9b555ddd40ae99f25297e994d |

Not opened:

- The published Hiroshima version of Hoshi: Project Euclid refused automated access.
- Fujiwara–Kato's preprint: unpublished.
- Ribet's appendix to Katz–Lang.

Also read: Statement AE1 of the CYCLOTOMIC_KERNEL return (`answers\CYCLOTOMIC_KERNEL_unzipped\...\CYCLOTOMIC_KERNEL_paper.tex`,
lines 2212–2234), because F17.6 uses it.

## Per source

### 1. Illusie, Theorem 7.6 (`\cite{CF_Illusie2002}`)

**Source.** Let X be a log regular fs log scheme and U its open subset of triviality. Restriction Y ↦ Y ×_X U is an
equivalence from finite Kummer étale covers of X onto the finite étale covers of U that are tamely ramified along
X − U. Tameness is tested at the points x ∈ X − U with dim O_{X,x} = 1, on the normalization of X in the cover.
Log regularity is defined in 7.3.1. Illusie credits the theorem to [F-K] 3.1 and gives no proof.

**Use in the return.** F17.6 (F.9) applies it twice:

- to the stable marked model 𝒞, with its log structure from 𝒞_k ∪ 𝒟, giving π₁(𝒞^log) ≅ π₁(U);
- to the trait, giving π₁(R^log) ≅ G_K.

**Setting.**

- 𝒞^log is fs and log regular. At a node of thickness m the monoid is ⟨X, Y, T | X + Y = mT⟩. In the basis (X, T) its
  cone is {c ≥ 0, ma + c ≥ 0}, and every lattice point of that cone is a combination of (1,0), (0,1) and (−1, m).
  So the monoid is saturated, and dim O = 2 = rank. Shorter: 𝒞^log is log smooth over the log regular trait, so it is
  log regular by Illusie 7.3(c).
- The codimension-one boundary points are the generic points of 𝒞_k and of 𝒟. Their residue fields have
  characteristic 0, so every cover is tame.

**Verdict.** Matches. For a citable text, add a published proof next to the survey:

- Mochizuki 1999, Theorem 3.3 = Theorem B, "Log Purity Theorem" (opened). For a regular log scheme and a finite étale
  cover of the interior, tamely ramified over the generic points of the boundary, it shows that the normalization is
  toric and that the cover extends uniquely to a log étale cover.
- Hoshi RIMS-1558, Remark 1.10 (opened) records that this extension is Kummer, by Mochizuki's proof.
- Full faithfulness is the normality of Kummer étale covers of a log regular scheme.

### 2. Hoshi, Corollary 3.9 (`\cite{CF_Hoshi2009}`)

**Source.** Let S^log be fs, with S the spectrum of a complete local ring with residue field k. Let X^log be log
regular fs, and let X^log → S^log be proper. Then the strict closed immersion X_0^log = X^log ×_{S^log} s^log → X^log
gives an equivalence of the categories of ket coverings. If X^log is connected, so is X_0^log, and
π₁(X_0^log) ≅ π₁(X^log). Hoshi defines a ket covering as a finite Kummer log étale morphism, which is Illusie's Kcov.

**Use in the return.** F17.6 (F.9) gives π₁(𝒞_k^log) ≅ π₁(𝒞^log), and the same for the base:
π₁(k^log) ≅ π₁(R^log).

**Setting.** The return first passes from the henselian R to its completion. That step uses SGA 1 XIII 4.3, 4.4,
§4.5.3 and 5.1–5.2, which are outside this check; the argument given is sound in residue characteristic 0. After it,
𝒞 is proper over a complete DVR and log regular, as in item 1.

**Verdict.** Matches.

- The numbering is that of RIMS-1558, July 2006. The bibliography entry names the journal but records that version;
  the journal numbering is unchecked.
- The return's audit says printed p. 31; the statement is on p. 31.

### 3. Mochizuki, Example 2.5 (`\cite{CF_MochizukiComb2007}`)

**Source.** Let S^log = Spec k with the chart N → k, 1 ↦ 0. The field k is arbitrary; the definition of "stable log
curve" in §0 is the pull-back of the tautological log curve over M̄_{g,r}^log along a classifying morphism. Then:

- G_k^log = Aut(T^log/S^log) sits in 1 → I_k^log → G_k^log → G_k → 1.
- Admissible coverings, tame at the cusps, give 1 → Δ_{X^log} → Π_{X^log} → G_k^log → 1.
- For Σ not containing the characteristic of k, the maximal pro-Σ quotient of Δ_{X^log} is naturally the
  PSC-fundamental group Π_𝒢 of the semi-graph of anabelioids of the pointed stable curve over k̄.
- The resulting outer action of G_k^log on Π_𝒢 is graphic: it lands in Aut(𝒢) ⊂ Out(Π_𝒢).

This is an Example. The identification rests on the theory of admissible coverings: [Mzk1] §3, [Mzk2] §2, and
§2 and the Appendix of [Mzk4] (*Absolute anabelian geometry*).

**Use in the return.** (F.10): with all primes, Π_𝒢 = ker[π₁(𝒞_k^log) → π₁(k^log)] ≅ Π, with graphic arithmetic action.

**Setting.**

- char k = 0, so Σ = all primes and the pro-Σ quotient is the whole group.
- k^log is the standard log point.
- 𝒞_k^log is a stable log curve in Mochizuki's sense. The classifying morphism of the trait is a log morphism. The fs
  pull-back of the tautological log curve has underlying scheme 𝒞 and is log regular, so its log structure is the
  divisorial one (Illusie 7.3(d)). That is the return's log structure; restricted to the closed fibre it gives 𝒞_k^log.
  The return does not write this out.

**Verdict.** Matches. One identification is unwritten (B2): the Example's admissible fundamental group is the Kummer
étale log fundamental group the return uses. In characteristic 0 these agree ([Mzk1] §3), and Hoshi–Mochizuki
Def. 2.10(iv) states the exact sequence directly for log fundamental groups.

### 4. Mochizuki, Proposition 1.2 (i)–(ii) (`\cite{CF_MochizukiComb2007}`)

**Source.** Let 𝒢 be of PSC-type, that is, coming from a pointed stable curve over an algebraically closed field of
characteristic not in Σ (Def. 1.1(i)). Let A_1, A_2 be verticial or edge-like subgroups of Π_𝒢 attached to v_i or e_i.

- (i) If A_1 ∩ A_2 is open in A_1, then v_1 = v_2, respectively e_1 = e_2. Edges include cusps (open edges) and
  nodes (closed edges).
- (ii) The A_i are commensurably terminal in Π_𝒢.

Also used:

- Def. 1.1(ii): the graph-theoretic quotient Π_𝒢^grph and the filtration M^cusp ⊂ M^edge ⊂ M^vert ⊂ M.
- Rem. 1.1.3: edge-like subgroups and their open subgroups are ≅ Ẑ^Σ; Π_𝒢 is centre-free; Π_𝒢^grph is free pro-Σ of
  rank n − i + 1.
- Rem. 1.1.4: the subquotients of the filtration are free.

**Use in the return.**

- Edge groups are maximal procyclic: an abelian overgroup normalizes the edge group, so it lies in the commensurator,
  which is the edge group itself.
- Distinct nodes and cusps give distinct Π-conjugacy classes (part (i) applied to a conjugate).
- In the case b > 0: Π ↠ (π₁ of the dual graph)^ ≅ Ẑ^b.

**Setting.** Σ = all primes and characteristic 0, so the hypotheses are met.

**Verdict.** Matches. One addition: the return asserts that an open subgroup of G_k acts trivially on M/M^vert, the
H₁ of the dual graph, for every splitting, and argues it from the graph. Mochizuki Prop. 2.4(i) (opened) states it for
any profinite J acting through Aut(𝒢): (M_𝒢/M_𝒢^vert) ⊗ ℤ_ℓ is quasi-trivial. That is the citation to add.

### 5. Hoshi–Mochizuki, Def. 2.10(iv), Lemma 2.11(ii)–(iii), Remark 2.14.1 (`\cite{CF_HoshiMochizukiNodes}`)

**Source.** Let k be algebraically closed of characteristic not in Σ, s ∈ M̄_{g,r}(k), and s^log the strict log point
(minimal log structure, Q_s ≅ ⊕_{nodes} ℕ_e, I_s = Hom(Q_s^gp, Λ) ≅ ⊕ Λ_e).

- Def. 2.10(iv): 1 → Π_{𝒢_s} → π₁^Σ(X_s^log) → I_s → 1, with the action through Aut(𝒢_s).
- Lemma 2.11(ii): for the point s′ ∈ M̄_{g,r+1}(k) at a node e, the map I_{s′} → π₁^Σ(X_s^log) is injective. Its
  image is an inertia subgroup I_e, the centralizer of the edge-like subgroup Π_e (Def. 2.2(iii)). So I_e ∩ Π_𝒢 = Π_e
  by commensurable terminality (Lemma 2.5(iv)).
- Lemma 2.11(iii): composed to I_s, the map is (a, b, m) ↦ (a + b, m).
- Rem. 2.14.1, stated as "not difficult to show": ι : Ẑ → I_s is of IPSC-type exactly when it comes from a monoid map
  Q_s → ℕ that is positive on every ℕ_f. These are the smoothing exponents.

**Use in the return.** At a node of thickness m:

- D_e = T_P ⋊ G_k, with T_P = {(a, b, c) : a + b = mc};
- the map (F.11) to T ⋊ G_k = G_K, with kernel the antidiagonal;
- "the map from this kernel into (F.10) is the injected edge group of Lemma 2.11".

**Setting.** Lemma 2.11 covers only the minimal log structure over an algebraically closed field. The return's
setting has thickness m, the standard log point and a non-closed k. The transfer (B3) is a routine fs base change
along ⊕ℕ_e → ℕ, e ↦ m_e:

- T_P = Hom(P^gp, Ẑ(1)) = I_{s′} ×_{I_s} Ẑ(1).
- π₁(𝒞_{k̄}^log) = π₁(X_s^log) ×_{I_s} Ẑ(1), since both are extensions with the same kernel Π_𝒢 by Example 2.5.
- Injectivity therefore passes to T_P, and the antidiagonal goes onto Π_e.

The Galois action, cyclotomic on all three coordinates, is the return's own computation of π₁ of a log point.

**Verdict.** Matches, with the transfer step B3 to be written out.

### 6. Stix, Theorem 20 (cited in the text without a `\cite` key; bibliography `CF_Stix2008` = arXiv:0809.0017)

**Source.** Theorem 20, credited to Nakamura. Let k distinguish tori from abelian varieties (§5.3: Hom_{Gal_k}(TS, TA)
is trivial for every torus S and abelian variety A over k), and let U/k be a hyperbolic curve. For a nontrivial closed
subgroup I of the geometric group π̄₁(U) (overline checked on the page image), the following are equivalent:

- (a) I lies in an inertia subgroup;
- (b) I is procyclic and cyclotomically normalized;
- (c) I is procyclic and essentially cyclotomically normalized.

Def. 5.2: essentially cyclotomically normalized means that some subgroup N of the normalizer of I in the arithmetic
π₁(U) projects onto an open subgroup of Gal_k and acts on I through the cyclotomic character.

Stix's U is X − Y with Y reduced and possibly empty, and χ(U) < 0 (§3.1, §3.3). So proper curves of genus at least 2
are included, and for them (a) never holds.

**Use in the return.**

- n = 0: E_s is the arithmetic group of the special fibre, which has exactly r classes.
- Tree, proper: the realizing curve must be proper, and then a node group would be a nontrivial procyclic essentially
  cyclotomically normalized subgroup, which Thm 20 excludes.
- Tree, affine: a realizing curve with r_V = r cusps has exactly r classes, against at least r + n.

**Setting.** The return's "essentially cyclotomically normalized" is Def. 5.2 with E_s in place of π₁(U), so it is
intrinsic to the extension. The added hypothesis needs k finitely generated over ℚ to distinguish tori from abelian
varieties.

- Stix gives this only for number fields: Lemma 19, a reformulation of Theorem 1 of Ribet's appendix to Katz–Lang.
  Every number field k has kℚ^ab/ℚ^ab finite.
- The return takes the finitely generated case from AE1 of its earlier return CYCLOTOMIC_KERNEL, which is AI-produced.
- AE1's proof (read) reduces to Ribet by specialization: torsion over K(μ_∞) injects into torsion of a fibre over
  k_x(μ_∞). It is correct.
- The direct form of the argument: a nonzero G_k-map ℤ_ℓ(1) → T_ℓA, after splitting the torus, is π₁(S)-equivariant on
  a smooth model S over a number field where A has good reduction. Restricted to a closed point, it gives a nonzero
  G_{κ(x)}-map ℤ_ℓ(1) → T_ℓA_x, which contradicts Lemma 19.

**Verdict.** Matches, with that added hypothesis. The setting meets it, but its support is an AI return, not
literature (A1).

### 7. Stix, Corollary 21

**Source.** For k and U as in Thm 20, the inertia subgroups of π̄₁(U) are exactly the maximal elements among the
closed subgroups that are procyclic and cyclotomically normalized, with the full normalizer.

**Use in the return.** It counts maximal procyclic subgroups that are essentially cyclotomically normalized. That
count follows from:

- Thm 20, (c) ⇒ (a): such a subgroup lies in an inertia group, so it equals it;
- Stix Cor. 13 (opened): an abelian subgroup meeting an inertia group nontrivially lies in it, so inertia groups are
  maximal procyclic;
- Prop. 11: distinct cusps give distinct inertia groups, so there are r classes.

**Verdict.** Matches in substance, with the same added hypothesis as item 6. The precise citation is "Thm 20 and
Cor. 13", or Cor. 21 read through its proof.

### 8. Tamagawa, Theorem (5.3), with Remark (5.2) and Theorem (0.8) (`\cite{CF_Tamagawa1997}`)

**Source.** §5 takes any DVR R, with G = Gal(K^sep/K) and I the inertia at s. X is proper, smooth and geometrically
connected over K; D is a relatively étale effective divisor; n = deg D_{K^sep}; and 2 − 2g − n < 0. Then the following
are equivalent:

- (a) (X, D) has good reduction: a proper smooth model with a relatively étale divisor;
- (b) I has trivial image in Out(π₁(U_{K^sep})^{(p′)});
- (c) the same in Out of the pro-ℓ quotient, for every ℓ ≠ p;
- (d) the same for one ℓ ≠ p.

Rem. (5.2): the smooth model is unique if 2 − 2g − n < 0, which follows from uniqueness of the stable model [DM],
[Knudsen].

**Use in the return.** F17.1, and in F17.7 the step "good reduction over K₁ makes I_{K₁} act trivially in Out(Π)"
((a) ⇒ (b) with p = 0, so the full Π), together with uniqueness of the smooth model.

**Verdict.** Matches. No semistability or completeness hypothesis is involved.

### 9. Knudsen, Theorem 2.7 (`\cite{CF_Knudsen1983}`)

**Source** (page image, p. 179). For all relevant g and n, M̄_{g,n} is an algebraic stack, proper and smooth over
Spec ℤ, and the substack of singular curves is a divisor with normal crossings relative to Spec ℤ. The proof starts
from (g, n) = (0, 3), (1, 1), and g ≥ 2 with n = 0, which is the range 2g − 2 + n > 0.

**Use in the return.** F17.7, after splitting and ordering the cusps:

- existence of the stable marked model over a finite extension, from properness;
- uniqueness and compatibility with base change, from separatedness;
- the descent in (1) ⇒ (2): every generic isomorphism σ*(Ū, D) ≅ (Ū, D) extends uniquely.

**Setting.** These are the standard consequences for a proper DM stack, and the theorem does not state them:

- universally closed: a K-point extends over the normalization of R in a finite extension of K;
- separated: Isom is finite over the DVR, so a generic isomorphism extends uniquely.

The unordered case is the quotient by S_n, which is still separated. The normalization of a henselian R in a finite
extension is a DVR.

**Verdict.** Matches.

## What is missing

**A1. The arithmetic hypothesis needs a literature citation.** "k finitely generated over ℚ distinguishes tori from
abelian varieties" (Stix §5.3) is used:

- for Stix Thm 20;
- in (F.13), Hom_{G_k}(V_ℓA, ℚ_ℓ) = 0;
- in (F.15).

The return cites its own AE1. To fix it, cite Stix Lemma 19 (Ribet) and add the five-line specialization argument of
item 6, or cite AE1's argument as a proof.

**B. Routine bridging steps, unwritten or partly written in the return.**

- B1. For Illusie 7.6, add the published proof: Mochizuki 1999, Thm 3.3, and Hoshi, Rem. 1.10.
- B2. Example 2.5 uses admissible coverings, and the return uses Kummer étale log π₁. The two agree in characteristic 0
  ([Mzk1] §3; Hoshi–Mochizuki Def. 2.10(iv)). Also, 𝒞_k^log is a stable log curve in Mochizuki's sense (item 3).
- B3. Lemma 2.11 is stated for the minimal log structure over k̄. Transfer it to thickness m by the fs base change in
  item 5.
- B4. Quasi-triviality on the graph quotient: cite Mochizuki Prop. 2.4(i).
- B5. Cite Stix Cor. 13 alongside Thm 20 and Cor. 21 for maximality.

**C. Citation edits.**

- Give Stix a `\cite{CF_Stix2008}` in F17.6, which names "Theorem 20 and Corollary 21" with no key; arXiv:0809.0017
  has only v1.
- Mark the Hoshi numbering as that of RIMS-1558.
- The return's I_e for the edge group is Π_e in Hoshi–Mochizuki, whose I_e is the rank-two inertia group. Rename it
  to avoid the clash.

**D. Outside this check, not opened:**

- the SGA 1 XIII citations in the completion step;
- C4 (for a centre-free Π the outer action determines the extension; this is elementary);
- the H²(Π, ℤ/ℓ) dichotomy between proper and affine curves;
- the Kummer computation of π₁ of a log point.

With A1 and B1–B5 written in, F17.6–F17.7 are a complete, fully cited proof.

## Context

About 150k tokens of context used when this file was written. Every source place listed above was read in the source
itself, not in a summary.
