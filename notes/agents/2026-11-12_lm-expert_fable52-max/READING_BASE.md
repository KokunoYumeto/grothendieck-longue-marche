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

## 4. Read by the successor line (12 Nov 2026)

Compiled 12 Nov 2026, 14:08 UTC (clock read) by fork D of the successor from the download logs `work\lit\downloads_*.jsonl`, the three notes `work\lit\LIT_*.md` and the main agent's reading before 13:55 UTC. All readers: Claude Fable 5.2, effort max. Folders are under `C:\Users\user\Documents\Free or receipted\free\lm-expert-20261112\`; all 68 downloaded files are entered in `free\CLAUDE_FREE_SHELF.json`. The statements relied on, with hypotheses, are in the LIT notes and in FINDINGS section E.

| Source | Location | What was read | By |
|---|---|---|---|
| OpenAI, The Deligne–Drinfeld conjecture, 23 Sep 2026 (family 008) | recent_results_20261110/papers/008_...pdf; UTF-8 text LM_EXPERT/work/papers/008_utf8.txt | in full, proofs included (sections 1–8); no error found in one reading; not certified | main agent |
| OpenAI, The p-adic section conjecture, 6 Oct 2026, and Étale covers with a prescribed exterior sheet, 24 Sep 2026 (family 019) | recent_results_20261110/papers/019_*.pdf; LM_EXPERT/work/papers2/ | in full, every lemma followed; nine citations compared with the cited texts | fork B1 |
| OpenAI, The Bogomolov–Pop reconstruction theorem, 23 Sep 2026 (family 009) | recent_results_20261110/papers/009_*.pdf; work/lit/sq_009.txt | in full; the two Milnor K-theory companions: statements only | fork B2 |
| OpenAI, Open homomorphisms of global solvably closed Galois groups, 5 Oct 2026 (family 031) | recent_results_20261110/papers/031_*.pdf; work/lit/sq_031.txt | in full | fork B2 |
| Hirose, Confluence relations, Hoffman basis over Z_(2), and the Deligne–Drinfeld conjecture, arXiv:2610.23719 (16 Oct 2026) | arXiv API ; https://arxiv.org/abs/2610.23719 | abstract only | main agent |
| Bonatto–Robertson, Galois actions on surfaces and a higher genus Grothendieck–Teichmüller group, arXiv:2606.01466 | arXiv API ; https://arxiv.org/abs/2606.01466 | abstract only | main agent |
| Constantin, Kolev: The theorem of Kerekjarto on periodic homeomorphisms of the disc and the sphere (arXiv:math/0303256; Enseign. Math. 40 (1994)) | `constantin-kolev-kerekjarto` ; https://arxiv.org/pdf/math/0303256 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Kerckhoff: The Nielsen realization problem (research announcement), Bull. AMS (N.S.) 2 (1980) 452-454 | `kerckhoff-1980-announcement` ; https://www.ams.org/journals/bull/1980-02-03/S0273-0979-1980-14764-3/S0273-0979-1980-14764-3.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Margalit, Winarski: Braids groups and mapping class groups: The Birman-Hilden theory (arXiv:1703.03448) | `margalit-winarski-birman-hilden` ; https://arxiv.org/pdf/1703.03448 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Bridson, Conder, Reid: Determining Fuchsian groups by their finite quotients (arXiv:1401.3645; Israel J. Math. 214 (2016)) | `bridson-conder-reid` ; https://arxiv.org/pdf/1401.3645 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Gross, Harris: Real algebraic curves, Ann. Sci. ENS (4) 14 (1981) 157-182 (Numdam) | `gross-harris-real-curves` ; http://www.numdam.org/item/ASENS_1981_4_14_2_157_0.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Kolev: Sous-groupes compacts d homeomorphismes de la sphere (arXiv:math/0304106; Enseign. Math. 52 (2006)) | `kolev-compact-subgroups-sphere` ; https://arxiv.org/pdf/math/0304106 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Yagasaki: Homotopy types of homeomorphism groups of noncompact 2-manifolds (arXiv:math/0010223; Topology Appl. 108 (2000)) | `yagasaki-homeo-noncompact-surfaces` ; https://arxiv.org/pdf/math/0010223 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Earle, Eells: The diffeomorphism group of a compact Riemann surface, Bull. AMS 73 (1967) 557-559 | `earle-eells-1967-announcement` ; https://www.ams.org/journals/bull/1967-73-04/S0002-9904-1967-11746-4/S0002-9904-1967-11746-4.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Zieschang: On extensions of fundamental groups of surfaces and related groups, Bull. AMS 77 (1971) 1116-1119 | `zieschang-1971-extensions` ; https://www.ams.org/journals/bull/1971-77-06/S0002-9904-1971-12887-2/S0002-9904-1971-12887-2.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Gabai: Convergence groups are Fuchsian groups (research announcement), Bull. AMS (N.S.) 25 (1991) 395-402 | `gabai-1991-announcement` ; https://www.ams.org/journals/bull/1991-25-02/S0273-0979-1991-16082-9/S0273-0979-1991-16082-9.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Bers: Finite dimensional Teichmuller spaces and generalizations, Bull. AMS (N.S.) 5 (1981) 131-172 | `bers-1981-finite-dim-teichmuller` ; https://www.ams.org/journals/bull/1981-05-02/S0273-0979-1981-14933-8/S0273-0979-1981-14933-8.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Eckmann, Mueller: Poincare duality groups of dimension two, Comment. Math. Helv. 55 (1980) 510-520 (GDZ) | `eckmann-mueller-1980-pd2` ; https://gdz.sub.uni-goettingen.de/download/pdf/PPN358147735_0055/LOG_0036.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Eckmann, Linnell: Poincare duality groups of dimension two, II, Comment. Math. Helv. 58 (1983) 111-114 (GDZ) | `eckmann-linnell-1983-pd2-ii` ; https://gdz.sub.uni-goettingen.de/download/pdf/PPN358147735_0058/LOG_0011.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Eckmann, Mueller: Plane motion groups and virtual Poincare duality of dimension two, Invent. Math. 69 (1982) 293-310 (GDZ) | `eckmann-mueller-1982-plane-motion` ; https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0069/LOG_0037.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Birman, Hilden: Isotopies of homeomorphisms of Riemann surfaces and a theorem about Artin s braid group, Bull. AMS 78 (1972) 1002-1004 | `birman-hilden-1972-announcement` ; https://www.ams.org/journals/bull/1972-78-06/S0002-9904-1972-13082-9/S0002-9904-1972-13082-9.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Harvey: On branch loci in Teichmuller space, Trans. AMS 153 (1971) 387-399 | `harvey-1971-branch-loci` ; https://www.ams.org/journals/tran/1971-153-00/S0002-9947-1971-0297994-0/S0002-9947-1971-0297994-0.pdf | statements quoted in LIT_LM4_surfaces.md | fork A |
| Minasyan, Zalesskii: Virtually compact special hyperbolic groups are conjugacy separable (arXiv:1504.00613; Comment. Math. Helv. 91 (2016)) | `minasyan-zalesskii-vcsh-conjugacy` ; https://arxiv.org/pdf/1504.00613 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Minasyan: Hereditary conjugacy separability of right angled Artin groups and its applications (arXiv:0905.1282; Groups Geom. Dyn. 6 (2012)) | `minasyan-hcs-raag` ; https://arxiv.org/pdf/0905.1282 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Power quotients of surface groups and mapping class groups (arXiv:2507.13701) | `power-quotients-2507.13701` ; https://arxiv.org/pdf/2507.13701 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Behrstock, Minsky: Dimension and rank for mapping class groups (arXiv:math/0512352; Ann. of Math. 167 (2008)) | `behrstock-minsky-rank` ; https://arxiv.org/pdf/math/0512352 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Mann, Tshishiku: Realization problems for diffeomorphism groups (arXiv:1802.00490) | `mann-tshishiku-realization` ; https://arxiv.org/pdf/1802.00490 | statements quoted in LIT_LM4_surfaces.md | fork A |
| Koenigsmann, On the section conjecture in anabelian geometry (arXiv:math/0305226v1) | `koenigsmann-2005` ; https://arxiv.org/pdf/math/0305226v1 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Pop-Stix, Arithmetic in the fundamental group of a p-adic curve (arXiv:1111.1354v1) | `pop-stix-2011` ; https://arxiv.org/pdf/1111.1354v1 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Stix, On cuspidal sections of algebraic fundamental groups (arXiv:0809.0017) | `stix-cuspidal` ; https://arxiv.org/pdf/0809.0017 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Esnault-Hai, Packets in Grothendieck's section conjecture (arXiv:math/0703877) | `esnault-hai` ; https://arxiv.org/pdf/math/0703877 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Stix, On the period-index problem in light of the section conjecture (arXiv:0802.4125) | `stix-period-index` ; https://arxiv.org/pdf/0802.4125 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Stix, On the birational section conjecture with local conditions (arXiv:1203.3236v3) | `stix-local-conditions` ; https://arxiv.org/pdf/1203.3236v3 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Bresciani-Vistoli, An elementary approach to Stix's proof of the real section conjecture (arXiv:2012.06278v2) | `bresciani-vistoli` ; https://arxiv.org/pdf/2012.06278v2 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Mochizuki-Tsujimura, Resolution of nonsingularities, point-theoreticity, and metric-admissibility for p-adic hyperbolic curves (author's page) | `mochizuki-tsujimura-rns` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/Resolution%20of%20Nonsingularities%20for%20Arbitrary%20Hyperbolic%20Curves.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Mochizuki, Topics surrounding the anabelian geometry of hyperbolic curves (author's page) | `mochizuki-topics` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/Topics%20Surrounding%20the%20Anabelian%20Geometry%20of%20Hyperbolic%20Curves.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Mochizuki, Galois sections in absolute anabelian geometry (author's page) | `mochizuki-galois-sections` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/Galois%20Sections.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Amini-Baker-Brugalle-Rabinoff, Lifting harmonic morphisms I (arXiv:1303.4812v3) | `abbr-lifting` ; https://arxiv.org/pdf/1303.4812v3 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Baker-Rabinoff, The skeleton of the Jacobian (arXiv:1308.3864v1) | `baker-rabinoff` ; https://arxiv.org/pdf/1308.3864v1 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Harari-Stix, Descent obstruction and fundamental exact sequence (author preprint, 11 Feb 2011) | `harari-stix` ; https://www.imo.universite-paris-saclay.fr/~david.harari/articles/finidesc.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Stoll, Finite descent obstructions and rational points on curves (author's revised preprint) | `stoll-finite-descent` ; https://mathe2.uni-bayreuth.de/stoll/papers/covers-revised.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Grothendieck, Brief an G. Faltings, 27.6.1983 (German; Grothendieck Circle, page of L. Schneps, editor of Geometric Galois Actions 1) | `grothendieck-faltings-1983` ; https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/GanF.pdf | in full | fork B1 |
| Pop, On the birational p-adic section conjecture (MPIM preprint 2007-102) | `pop-birational-2007` ; https://archive.mpim-bonn.mpg.de/2312/1/preprint_2007_102.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Deligne, Le groupe fondamental de la droite projective moins trois points (1989), IAS scan | `deligne-1989` ; https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Steklov, Fermat's Last Theorem for Selmer sections (arXiv:2602.17746v2) | `steklov-2026` ; https://arxiv.org/pdf/2602.17746v2 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Porowski, Families of curves separating points (arXiv:2607.27746v1) | `porowski-2026` ; https://arxiv.org/pdf/2607.27746v1 | statements quoted in LIT_LM6_sections.md | fork B1 |
| Hoshi-Tsujimura, Construction of abundant explicit nongeometric pro-p Galois sections of punctured projective lines (RIMS-1950, author's page) | `hoshi-tsujimura-rims1950` ; https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1950.pdf | statements quoted in LIT_LM6_sections.md | fork B1 |
| Mochizuki-Tamagawa, The algebraic and anabelian geometry of configuration spaces, Hokkaido Math. J. 37 (2008) | `mochizuki-tamagawa-config` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Algebraic%20and%20Anabelian%20Geometry%20of%20Configuration%20Spaces.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Mochizuki, The local pro-p anabelian geometry of curves, Invent. Math. 138 (1999) | `mochizuki-local-pro-p` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Mochizuki, The profinite Grothendieck conjecture for closed hyperbolic curves over number fields, J. Math. Sci. Univ. Tokyo 3 (1996) | `mochizuki-1996-closed` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Profinite%20Grothendieck%20Conjecture%20for%20Closed%20Hyperbolic%20Curves%20over%20Number%20Fields.pdf | downloaded, not re-read | fork B2 |
| Mochizuki, The absolute anabelian geometry of hyperbolic curves (Galois Theory and Modular Forms, Kluwer 2004, 77-122) | `mochizuki-absolute-anabelian` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Hoshi-Mochizuki, On the combinatorial anabelian geometry of nodally nondegenerate outer representations, Hiroshima Math. J. 41 (2011) 275-342 | `hoshi-mochizuki-nodnon` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/Nodally%20Nondegenerate%20Outer%20Representations.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Mochizuki, A combinatorial version of the Grothendieck conjecture, Tohoku Math. J. 59 (2007) 455-479 | `mochizuki-combgc` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/Combinatorial%20Grothendieck%20Conjecture.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Nakamura, Galois rigidity of pure sphere braid groups and profinite calculus, J. Math. Sci. Univ. Tokyo 1 (1994) 71-136 | `nakamura-1994-profinite-calculus` ; https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Belyi, O rasshireniyakh Galua maksimalnogo krugovogo polya, Izv. Akad. Nauk SSSR Ser. Mat. 43:2 (1979) 267-276 | `belyi-1979` ; https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=1682&what=fullt&option_lang=rus | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Tamagawa, The Grothendieck conjecture for affine curves, Compositio Math. 109 (1997) 135-194 | `tamagawa-1997-affine` ; https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0010437X97000614 | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Nakamura-Tamagawa-Mochizuki, The Grothendieck conjecture on the fundamental groups of algebraic curves, Sugaku Expositions 14 (2001) 31-53 | `ntm-survey` ; https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Grothendieck%20Conjecture%20on%20the%20Fundamental%20Groups%20of%20Algebraic%20Curves.pdf | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Collas, Anabelian perspectives in Galois-Teichmuller theory, arXiv:2603.02848 (3 Mar 2026) | `collas-2603.02848` ; https://arxiv.org/pdf/2603.02848 | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Yamaguchi, Center-freeness of finite-step solvable groups arising from anabelian geometry, arXiv:2601.07112v4 (24 May 2026) | `yamaguchi-2601.07112` ; https://arxiv.org/pdf/2601.07112 | statements quoted in LIT_LM6_anabelian.md | fork B2 |
| Luo-Watanabe, The section conjecture for generic pointed curves, arXiv:2610.24986 | `luo-watanabe-2610.24986` ; https://arxiv.org/pdf/2610.24986 | abstract and main theorem statements | fork D |
| Holzschuh-Schmidt-Stix, Anabelian Geometry in Families, arXiv:2608.21232 | `holzschuh-schmidt-stix-2608.21232` ; https://arxiv.org/pdf/2608.21232 | abstract and main theorem statements | fork D |
| Carlson-Corwin, Cuspidal sections for varieties of arbitrary dimension, arXiv:2611.09080 | `carlson-corwin-2611.09080` ; https://arxiv.org/pdf/2611.09080 | abstract and main theorem statements | fork D |
| Collas-Philip-Yamaguchi, Anabelian geometry for Deligne-Mumford curves, arXiv:2605.02577 | `collas-philip-yamaguchi-2605.02577` ; https://arxiv.org/pdf/2605.02577 | abstract and main theorem statements | fork D |
| Pop, Generalizations and minimalistic refinements of the t-birational Section Conjecture, arXiv:2604.26131 | `pop-2604.26131` ; https://arxiv.org/pdf/2604.26131 | abstract and main theorem statements | fork D |
| Holzschuh, On the real Section Conjecture in etale homotopy theory, arXiv:2510.13325 | `holzschuh-2510.13325` ; https://arxiv.org/pdf/2510.13325 | abstract and main theorem statements | fork D |
| Drinfeld, O kvazitreugolnykh kvazikhopfovykh algebrakh i odnoi gruppe, tesno svyazannoi s Gal(Qbar/Q), Algebra i Analiz 2:4 (1990) 149-181 | `drinfeld-1990-gt` ; https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&paperid=199&what=fullt&option_lang=rus | section 4, pp. 164-167 (OCR text layer of the Russian original): equations (4.3), (4.4), (4.10), the definitions of GT, the passages on the tower and on Belyi | main agent |
| Harbater-Schneps, Fundamental groups of moduli and the Grothendieck-Teichmuller group, Trans. AMS 352 (2000) 3117-3148 | `harbater-schneps-2000` ; https://www.ams.org/journals/tran/2000-352-07/S0002-9947-00-02347-3/S0002-9947-00-02347-3.pdf | abstract, introduction (0.1-0.3), Main Theorem, Theorem A | main agent |
| Hoshi-Minamide-Mochizuki, Group-theoreticity of numerical invariants and distinguished subgroups of configuration space groups, RIMS-1870 (2017) | `hoshi-minamide-mochizuki-rims1870` ; https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1870.pdf | Corollaries B and C, Definition 2.7, Corollary 2.8 | main agent |
| Minamide-Nakamura, The automorphism groups of the profinite braid groups, arXiv:1904.06749 | `minamide-nakamura-1904.06749` ; https://arxiv.org/pdf/1904.06749 | introduction: Theorems A, B, 1.1, Corollary C | main agent |
| Boggi, A congruence subgroup property for symmetric mapping class groups, arXiv:2408.12486 | `boggi-2408.12486` ; https://arxiv.org/pdf/2408.12486 | sections 1.1, 1.2: Theorems A-C and the state of the congruence subgroup problem | main agent |
| Bux-Ershov-Rapinchuk, The congruence subgroup property for Aut F_2: a group-theoretic proof of Asada's theorem, arXiv:0909.0304 | `ber-0909.0304` ; https://arxiv.org/pdf/0909.0304 | downloaded, not read | main agent |
| Schneps, The Grothendieck-Teichmuller group GT: a survey | `schneps-gt-survey` ; https://webusers.imj-prg.fr/~leila.schneps/SchnepsGT.pdf | extracts found by search (definition of GT_0 and GT, theorem statements) | main agent |
| Lochak-Nakamura-Schneps, The Grothendieck-Teichmuller group GT acts on the genus g mapping class group with 0 or 1 marked point, arXiv:2602.12462 | `lochak-nakamura-schneps-2602.12462` ; https://arxiv.org/pdf/2602.12462 | abstract, section 1, Theorem 1.1 | main agent |
| Boggi, Automorphisms of profinite mapping class groups, arXiv:2011.15075v6 (22 Apr 2026) | `boggi-2011.15075` ; https://arxiv.org/pdf/2011.15075v6 | abstract, introduction (Theorems A-C), sections 2.1-2.6 | main agent |

### Not obtained (paywalled, or the host refused automated access; nothing was bypassed)

- Surfaces (fork A): Kerckhoff, Ann. of Math. 117 (1983); Birman–Hilden, Ann. of Math. 97 (1973); MacLachlan–Harvey, Proc. LMS 30 (1975); Hamstrom, Illinois J. Math. 10 (1966); Earle–Eells, J. Diff. Geom. 3 (1969); Earle–Schatz, J. Diff. Geom. 4 (1970); Scott, Topology 9 (1970); Wolpert 1987; Birman–Lubotzky–McCarthy, Duke 50 (1983); Stallings, Ann. of Math. 88 (1968); Bieri–Eckmann, JPAA 13 (1978); Zieschang, LNM 875; Zieschang–Vogt–Coldewey, LNM 835; Macbeath, Canad. J. Math. 19 (1967); Farb–Margalit, A Primer on Mapping Class Groups; Birman, Comm. Pure Appl. Math. 22 (1969); Herfort–Ribes, Crelle 358 (1985).
- Sections (fork B1): Hoshi, Publ. RIMS 46 (2010); Pál 2011; Wickelgren 2014; Esnault–Wittenberg 2009; Betts–Stix (Annals 2025); Pop, note of 28 Sep 2025 on the t-birational section conjecture (403); Stix, LNM 2054; the OpenAI paper "The Selmer converse for elliptic curves at every prime".
- Anabelian (fork B2): Anderson, Topology 13 (1974); Lubotzky–van den Dries, Israel J. Math. 39 (1981); Matsumoto, Crelle 474 (1996); Matsumoto–Tamagawa, Amer. J. Math. 122 (2000); Nakamura, Crelle 411 (1990); Pop, Invent. Math. 216 (2019) (I/OM; no verbatim statement in this line).
- GT (main agent, up to 13:55 UTC): Hatcher–Lochak–Schneps, Crelle 521 (2000) (the guessed URL on Hatcher's page gave 404); Ihara, ICM 1990 and the 1994 paper; Lochak–Schneps on braid groups; Nakamura–Schneps, Invent. Math. 141 (2000); Asada, JPAA 159 (2001); Hoshi–Iijima; Boggi–Zalesskii, Bull. LMS 57 (2025): not yet fetched.

### Found by search, 2026 (claims, unchecked unless said above)

- GT and the tower: arXiv:2602.12462 (Lochak–Nakamura–Schneps: the full GT acts on the profinite mapping class groups of genus g with 0 or 1 marked point); arXiv:2011.15075v6 (Boggi, 22 Apr 2026: the automorphisms of procongruence mapping class groups preserving one inertia class form GT; GT is the automorphism group of the procongruence tower); arXiv:2606.01466 (Bonatto–Robertson: a modular operad for the higher-genus tower); arXiv:2610.23719 (Hirose: a second proof of the Deligne–Drinfeld conjecture); arXiv:2603.02848v2 (Collas, survey; statements listed in LIT_LM6_anabelian.md 2.6); Mochizuki–Tsujimura RIMS-1974, Theorem G (the p-adic versions of GT coincide).
- Sections: arXiv:2610.24986 (Luo–Watanabe: universal curve over M_{g,n}, g ≥ 3); arXiv:2611.09080 (Carlson–Corwin: cuspidal sections in any dimension); arXiv:2602.17746 (Steklov: Selmer sections of Fermat curves; DM-curves); arXiv:2509.15660, arXiv:2607.27746 (Porowski: reductions of Selmer sections); arXiv:2604.26131 (Pop: t-birational section conjecture); arXiv:2510.13325 (Holzschuh: real section conjecture in étale homotopy theory); arXiv:2409.07923v5 (Bresciani: toric fundamental group); arXiv:2604.23485 (Sun).
- Anabelian: arXiv:2608.21232 (Holzschuh–Schmidt–Stix: families); arXiv:2605.02577 (Collas–Philip–Yamaguchi: Deligne–Mumford curves); arXiv:2604.24898 (Carlson: elementary anabelian varieties); arXiv:2608.01417 (Minamide–Sawada–Tsujimura); arXiv:2511.06725 (Shimizu–Yamaguchi); Tsujimura, pro-p anabelian geometry in genus 0 (RIMS, Feb 2026); Hoshi–Mochizuki–Tsujimura, J. Math. Sci. Univ. Tokyo 32 (2025).
- Congruence subgroup problem: no 2026 claim for genus ≥ 3 found (arXiv API searches of 12 Nov 2026); arXiv:2408.12486v2 (Boggi, Jan 2026) states that it is known for genus ≤ 2.

Correction to section 3 above and to the reading-list card: arXiv:2601.07112 is N. Yamaguchi, "Center-freeness of finite-step solvable groups arising from anabelian geometry" (v4 of 24 May 2026): the maximal m-step solvable quotients (m ≥ 2) of the étale and tame fundamental groups of a hyperbolic curve over a separably closed field are torsion-free and center-free. It is not an "m-step solvable anabelian statement for affine hyperbolic curves".
