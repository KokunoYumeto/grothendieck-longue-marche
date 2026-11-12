# La Longue Marche expert line: reading base

What this line has read, where it is, what statements are relied on (with hypotheses), and what could not be obtained
yet. Section 1 by Claude Fable 5.2, effort max, 12 Nov 2026. A source is "read" only if its text was in the
expert's context; "from memory" items are listed separately and must be read before they carry a verdict.

## 1. Read in full

| Source | Location | What was read | Date |
|---|---|---|---|
| Grothendieck, *La Longue Marche à travers la théorie de Galois*, Part I (§§1–37, ms. pp. 1–292) | cote 140-2, 575 scans; current texts `second_pass\LM_P01..P058` (P04, P05 first pass in `answers\unzipped\`); reading copies `LM_EXPERT\work\reading2\001..058` | everything; notes in `GROTHENDIECK_NOTES.md` | 12 Nov 2026 |
| Tables of contents of Part II (§§38–49) and of §§50–53 | cote 140-3 scans 3–5; cote 140-4 scans 3–4 | titles only | 12 Nov 2026 |
| Board card `braindump_board\cards\reading-list.md` | as named | in full | 12 Nov 2026 |

## 2. Read in part (introductions and main statements only; the proofs are NOT read)

| Source | Location | Statements noted (verbatim content, hypotheses) | Not read |
|---|---|---|---|
| OpenAI, *The Deligne–Drinfeld conjecture*, 23 Sep 2026 (family 008), 41 pp. Claimed, unrefereed; Lean said to cover the main statement | `recent_results_20261110\papers\008_...pdf`; text `LM_EXPERT\work\papers\008_...txt` | L = Lie_Q⟨x,y⟩ graded by weight; W ⊂ L the solutions ψ of (1.2) ψ(x,y)+ψ(y,x) = 0, (1.3) ψ(x,y)+ψ(y,−x−y)+ψ(−x−y,x) = 0, (1.4) the pentagon in t_4: ψ(t12,t23+t24)+ψ(t13+t23,t34) = ψ(t23,t34)+ψ(t12+t13,t24+t34)+ψ(t12,t23); Ihara bracket {ψ,φ} = D_ψ(φ) − D_φ(ψ) + [ψ,φ], D_ψ(x) = 0, D_ψ(y) = [y,ψ]. **Theorem 1.1**: there are homogeneous σ_{2k+1} ∈ W_{2k+1} (k ≥ 1) with Lie_Q⟨e_3,e_5,...⟩ → (W,{,}) an isomorphism of graded Lie algebras; also after weight completion. Main estimate (Cor. 5.4): dim W_n ≤ dim Lie(e_3,e_5,...)_n for all n, by a filtered degeneration of the pentagon in characteristic 2 (A = x^2, C = [x,y], B = y) and integral deletion operators; lower bound from Brown (MT(Z)) or internally (Sections 6–8). Lemma 2.1: W_1 = W_2 = 0. Consequence stated: H^0(GC_2) = completed free Lie algebra (via Willwacher). It is a statement about the graded rational Lie algebra grt_1 only: nothing on the profinite group GT or on G_Q → GT | Sections 2 (after Lemma 2.4)–8 |
| OpenAI, *The p-adic section conjecture*, 6 Oct 2026 (family 019), 24 pp. Claimed, unrefereed, no formal proof | `papers\019_The-p-adic-section-conjecture-...pdf`; text in `work\papers\` | **Theorem 1.1**: p prime, k/Q_p finite, X/k smooth proper geometrically connected of genus ≥ 2: X(k) → {continuous sections of π_1(X) → G_k}/conjugation by π_1(X_k̄) is bijective. **Theorem 1.2** (completion statement on the universal étale function field) is the geometric core; then Pop–Stix localization at valuations, Koenigsmann's birational p-adic result, the two-valuation principle. Global consequence (Section 8): the section conjecture over number fields for proper curves of genus ≥ 2 whose finite-cover descent locus equals the rational points, including X_0(N), X_1(N) of genus ≥ 2 over Q. Proper curves only; nothing on cuspidal sections of affine curves | Sections 2–8 |
| `recent_results_20261110\RECENT_RESULTS.md`, Part 2 table (links L1–L14), and the SCOREBOARD rows for 008, 019, 031 | as named | used as pointers only (written at effort medium): L1/L1q (008 and the loop equation of Part II), L2/L2q (019 and LM Part I sections), L3 (031 Uchida Hom-form; 009 Bogomolov–Pop) | BRIEF_FOR_PROMPTS.md, OPENAI_MATH_INVENTORY.md, the rest of both files |

Extracted but not yet read (text files in `LM_EXPERT\work\papers\`): 019 *Étale covers with a prescribed exterior
sheet* (24 Sep 2026, 7 pp.); 009 *The Bogomolov–Pop reconstruction theorem* (23 Sep 2026, 26 pp.); 031 *Open
homomorphisms of global solvably closed Galois groups* (5 Oct 2026, 23 pp.). The two 009 Milnor K-theory papers are
not extracted.

## 3. Not yet obtained or read in this line (the successor's literature step)

Primary sources the reviews and prompts need, with the statements this line expects to rely on (all "from memory"
until read; see `FINDINGS.md` for where each is used):

- Drinfeld, *On quasitriangular quasi-Hopf algebras and on a group closely connected with Gal(Q̄/Q)* (1990): the
  definitions of GT, GT_0, grt_1; Prop. 5.7, Prop. 6.3. Ihara, *Braids, Galois groups, and some arithmetic functions*
  (ICM 1990) and *On the embedding of Gal(Q̄/Q) into GT* (1994).
- Deligne, *Le groupe fondamental de la droite projective moins trois points* (1989): tangential base points (§15).
- Belyi 1979 (three-point theorem). Nakamura, *Galois rigidity of the étale fundamental groups of punctured
  projective lines* (1990) and *Galois rigidity of pure sphere braid groups and profinite calculus* (1994).
- Harbater–Schneps, *Fundamental groups of moduli and the Grothendieck–Teichmüller group* (2000): Out^♯_n = GT for
  n ≥ 5, GT_0 at n = 4. Lochak–Schneps; Hatcher–Lochak–Schneps, *On the Teichmüller tower of mapping class groups*
  (2000); Schneps's survey of GT.
- Pop (Ihara/Oda–Matsumoto question: G_Q = Out of the tower of π_1 of varieties); Matsumoto 1996; Hoshi–Mochizuki
  (combinatorial anabelian geometry: injectivity and bijectivity of Out^FC(Π_{n+1}) → Out^FC(Π_n));
  Hoshi–Minamide–Mochizuki (Out of configuration space groups and GT); Asada 2001, Boggi, Hoshi–Iijima (congruence
  subgroup property).
- Tamagawa 1997, Mochizuki 1999 (Isom- and Hom-forms for hyperbolic curves); Koenigsmann, Pop–Stix, Stix's book
  (section conjecture).
- Kerckhoff 1983 (Nielsen realization); Birman–Hilden 1973, MacLachlan–Harvey 1975; Earle–Eells, Earle–Schatz,
  Hamstrom; Zieschang–Vogt–Coldewey; Bridson–Conder–Reid 2016; Birman–Lubotzky–McCarthy 1983.
- Collas, *Anabelian perspectives in Galois–Teichmüller theory*, arXiv:2603.02848 (named on the reading-list card);
  arXiv:2601.07112 (m-step solvable anabelian statement for affine hyperbolic curves; status unknown).
- A search of arXiv and of the announcements for 2026 results on GT, the section conjecture, mapping class groups
  and anabelian geometry has NOT been made in this section.
