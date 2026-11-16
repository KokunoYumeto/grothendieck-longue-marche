# Item-level context search log

**Search hits are candidate retrieval locations, not proof, source validation, or a change in evidentiary status.** Earlier CT/CN/CD contents remain supplied, unreviewed claims/readings. No source image was opened and no OCR or external lookup was performed by this script.

Coverage: **117 / 117 items** — 61 heading items with Search fields and 56 table items (S01–S40, T01–T08, G01–G08). Missing, duplicate, unexpected, or empty entries: **none**.

Search specification: 457 item-term searches, 273 distinct normalized terms. Matching is case-insensitive NFC-normalized **literal substring matching per source line**. No regex, stemming, accent removal, TeX normalization, OCR correction, or joining across line breaks is performed. Counts are matching lines, not word occurrences; source totals are unions of lines and are not the sum of query counts. Single-letter and short terms can be very broad. Zero hits do not establish conceptual absence.

Corpus keys: CR = context/README.md; RS = context/notes/RESULTS_STATE.md; CT = earlier transcription TEX; CN = earlier notes; CD = earlier doubts; Oda = the 74 supplied printed-source page_*.txt extracts. Oda printed page = PDF/extract index + 61 for indices 2–74; index 1 is the NUMDAM cover. Extraction errors and mathematical formatting can cause missed literal matches.

Per item, query counts are followed by union counts for CR/RS/CT/CN/CD/Oda. Candidate locators are ranked within each corpus by number of distinct matched terms, then summed inverse global hit frequency, then source order. At most CR 2, RS 3, CT 4, CN 4, CD 2, and Oda 3 locations are shown. These are compact samples, not an exhaustive concordance or necessarily the strongest mathematical comparators. The JSON records corpus-specific query counts, source hashes, and the number of candidate units before truncation; it contains no source-text dumps.

Reproduce with `python MPL_57_271-315/scripts/build_context_search_log.py` in the supplied workspace. The script rereads the latest main notes and fails if the expected 117-ID coverage or a Search entry is missing. Paths can be set with `--workspace`, `--notes`, `--oda-dir`, and `--output-dir`. It requires the existing context texts and existing printed Oda extracts and does not regenerate them. It writes only this log and its companion JSON.

Generated UTC: 2026-11-16T19:47:35+00:00. Main-notes SHA-256: `01b51fcd55a2b0daeb65e22fb5fa885949b5e4c74df4cf1f3e04600efab693a0`. ID/query signature: `c3e6f17c8577fcc46b4fabc9bda00766e54fe71bc99f2e0d3820f713e1ee0720`. Rerun after final prose edits if an exact whole-file hash is required; the ID/query signature isolates search coverage from prose-only changes.

## F items

### F01 — The compatibility gap remains a particular map

- **Queries → matching lines:** `Fourier` → 15; `Pontryagin` → 1; `convolution` → 24; `compatibilité` → 3; `F7` → 7; `F8` → 3.
- **Union by corpus:** CR 2; RS 4; CT 5; CN 29; CD 7; Oda 4.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L18); § What is in this zip (L28) · **RS:** FLAGGED_149 F8a (L64); LM2 B.f7 (L31); LM7 D.42 (L74) [3/4 units] · **CT:** 47:2 (L2078); 47:3 (L2101); 47:8 (L2393); 47:5 (L2249) · **CN:** F7 (L3279); 47:2:1 (L1781); 47:8:1 (L2031); F8 (L3285) [4/20 units] · **CD:** § Observed recurring forms (L49); 47:2 (Doubts) (L480) [2/7 units] · **Oda:** printed p.95 / PDF 34 (L24); printed p.115 / PDF 54 (L30); printed p.122 / PDF 61 (L44).

### F02 — An admitted lemma is a separate issue

- **Queries → matching lines:** `admettre` → 2; `lemme 2` → 6; `algébriquement trivial` → 0; `faisceau de Weil` → 2.
- **Union by corpus:** CR 0; RS 0; CT 7; CN 1; CD 0; Oda 0.
- **Candidate locators:** **CT:** 47:7 (L2335); 47:3 (L2147); 47:6 (L2297); 47:8 (L2390) · **CN:** F6 (L3275).
- **Literal zero-hit terms:** `algébriquement trivial`.

### F03 — Product line bundles and dual equivariance are real bridges

- **Queries → matching lines:** `pointé` → 0; `transport de structure` → 2; `contragrédient` → 1; `Hom` → 428; `faisceau de Weil` → 2.
- **Union by corpus:** CR 1; RS 6; CT 63; CN 116; CD 12; Oda 235.
- **Candidate locators:** **CR:** § What is in this zip (L29) · **RS:** LM7_PUSH E.67 (L50); LM6 B.22 (L69); LM7 D.37 (L71) [3/6 units] · **CT:** 47:11 (L2546); 47:3 (L2089); 47:6 (L2297); 16:3 (L40) [4/32 units] · **CN:** 47:11:5 (L2213); 16:3:1 (L11); 16:4:1 (L35); 16:5:4 (L91) [4/90 units] · **CD:** § Shared notation table (L15); 16:3 (Doubts) (L65) [2/10 units] · **Oda:** NUMDAM cover / PDF 1 (L7); printed p.63 / PDF 2 (L7); printed p.65 / PDF 4 (L1) [3/67 units].
- **Literal zero-hit terms:** `pointé`.

## J items

### J01 — Theorem 1: the kernel construction is absent

- **Queries → matching lines:** `N(\xi)` → 1; `Albanese` → 13; `noyau` → 19; `système linéaire` → 0.
- **Union by corpus:** CR 0; RS 0; CT 15; CN 12; CD 4; Oda 1.
- **Candidate locators:** **CT:** 44:2 (L2787); 44:8 (L2974); 16:6 (L195); 16:19 (L756) [4/12 units] · **CN:** 44:2:1 (L2463); 44:9:3 (L2781); 16:46:3 (L1391); 44:2:2 (L2473) [4/10 units] · **CD:** § Abbreviations encountered (L696); 16:38 (Doubts) (L345) [2/3 units] · **Oda:** printed p.112 / PDF 51 (L47).
- **Literal zero-hit terms:** `système linéaire`.

### J02 — Theorem 2: tangent dimension is not the Betti bound

- **Queries → matching lines:** `Betti` → 7; `b^{2i` → 1; `Tate` → 226; `dimension` → 99; `Alb` → 32.
- **Union by corpus:** CR 2; RS 16; CT 71; CN 193; CD 31; Oda 25.
- **Candidate locators:** **CR:** § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L33) · **RS:** WG H9 (L106); WG2 §2.3 #12 (L108); LM6 F.6 (L22) [3/16 units] · **CT:** 44:2 (L2787); 44:8 (L2974); 16:44 (L1723); 44:9 (L2991) [4/16 units] · **CN:** 44:8:3 (L2725); 44:2:5 (L2495); 44:8:7 (L2759); 16:44:2 (L1293) [4/162 units] · **CD:** § Abbreviations encountered (L696); 44:4 (Doubts) (L649) [2/26 units] · **Oda:** printed p.112 / PDF 51 (L47); printed p.113 / PDF 52 (L3); printed p.133 / PDF 72 (L19) [3/13 units].

### J03 — Theorem 3: ordinary endpoints do not construct all higher representatives

- **Queries → matching lines:** `Z^i` → 4; `P^i` → 50; `J^1` → 1; `Pic` → 295; `dual` → 191; `correspondances` → 5.
- **Union by corpus:** CR 2; RS 9; CT 229; CN 112; CD 43; Oda 135.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § This package in our plan (L9) · **RS:** WG2 §2.3 #12 (L108); LM7 D.19 (L38); LM8 G.20 (L39) [3/9 units] · **CT:** 44:2 (L2787); 44:8 (L2974); 44:4 (L2851); 16:18 (L694) [4/62 units] · **CN:** 44:8:3 (L2725); § References (L3419); 16:18:1 (L537); S19 (L3213) [4/87 units] · **CD:** 16:36 (Doubts) (L332); 44:2 (Doubts) (L628) [2/30 units] · **Oda:** printed p.102 / PDF 41 (L22); printed p.110 / PDF 49 (L12); printed p.63 / PDF 2 (L17) [3/30 units].

### J04 — Theorem 4: a cone does not prove positivity of a correspondence

- **Queries → matching lines:** `Hodge` → 43; `positive` → 41; `polarisation` → 4; `cône` → 0; `symétrique` → 11.
- **Union by corpus:** CR 0; RS 8; CT 18; CN 45; CD 7; Oda 16.
- **Candidate locators:** **RS:** LM6 B.27 (L17); FLAGGED_149 Z142g (L28); LM6 A.45 (L35) [3/8 units] · **CT:** 44:9 (L2989); 44:2 (L2802); 44:8 (L2974); 16:19 (L760) [4/13 units] · **CN:** 44:9:1 (L2767); 44:2:4 (L2487); D20 (L3606); 16:30:1 (L951) [4/34 units] · **CD:** 16:19 (Doubts) (L231); § Abbreviations encountered (L749) [2/5 units] · **Oda:** printed p.71 / PDF 10 (L4); printed p.74 / PDF 13 (L4); printed p.80 / PDF 19 (L11) [3/11 units].
- **Literal zero-hit terms:** `cône`.

### J05 — Theorem 5: the name Néron is not a height formula

- **Queries → matching lines:** `Néron` → 17; `hauteur` → 0; `intersection` → 36; `pinceau` → 2; `verticale` → 1.
- **Union by corpus:** CR 0; RS 1; CT 16; CN 30; CD 5; Oda 2.
- **Candidate locators:** **RS:** WG2 §2.3 #12 (L108) · **CT:** 44:4 (L2849); 16:26 (L1072); 16:21 (L886); 44:9 (L2989) [4/11 units] · **CN:** 44:4:2 (L2551); 47:9:5 (L2115); 44:4:1 (L2545); R4 (L2867) [4/25 units] · **CD:** 44:4 (Doubts) (L650); § Abbreviations encountered (L734) [2/4 units] · **Oda:** printed p.119 / PDF 58 (L20); printed p.130 / PDF 69 (L5).
- **Literal zero-hit terms:** `hauteur`.

### J06 — Theorem 6: a close hyperplane question remains a question

- **Queries → matching lines:** `hyperplan` → 31; `bijectif` → 2; `fixe` → 23; `surjectif` → 2; `2i` → 32.
- **Union by corpus:** CR 0; RS 2; CT 38; CN 40; CD 7; Oda 2.
- **Candidate locators:** **RS:** LM8 G.20 (L39); WG2 §2.3 #12 (L108) · **CT:** 44:4 (L2847); 16:43 (L1710); 16:54 (L1958); 16:3 (L31) [4/19 units] · **CN:** 16:4:4 (L59); 16:15:7 (L441); 16:17:5 (L521); 16:22:1 (L723) [4/36 units] · **CD:** 16:5 (Doubts) (L88); 16:3 (Doubts) (L72) [2/5 units] · **Oda:** printed p.126 / PDF 65 (L13); printed p.129 / PDF 68 (L44).

### J07 — Theorem 7: the divisor-level comparison is explicit

- **Queries → matching lines:** `numérique` → 4; `tau` → 31; `équivalence` → 20; `déformer` → 0; `D14` → 2.
- **Union by corpus:** CR 0; RS 2; CT 22; CN 21; CD 4; Oda 0.
- **Candidate locators:** **RS:** LM6 E.21 (L21); LM4 F.12 (L67) · **CT:** 44:6 (L2944); 16:46 (L1781); 47:5 (L2233); 16:10 (L347) [4/12 units] · **CN:** D14 (L3540); 44:6:1 (L2639); 47:9:3 (L2097); 44:8:2 (L2719) [4/14 units] · **CD:** § Abbreviations encountered (L763); 16:15 (Legibility and limits) (L923) [2/3 units].
- **Literal zero-hit terms:** `déformer`.

## P items

### P01 — Reused divisor pages supply vocabulary, not the analytic criterion

- **Queries → matching lines:** `diviseur` → 3; `linéairement équivalent` → 0; `valuation` → 6; `Pic(U)` → 4.
- **Union by corpus:** CR 0; RS 1; CT 3; CN 5; CD 2; Oda 2.
- **Candidate locators:** **RS:** 57-ns-p-divisibility-generization (L115) · **CT:** 16:23 (L958); 44:9 (L2995); 16:52 (L1912) · **CN:** 16:19:4 (L609); R11 (L2948); 16:52:6 (L1639); R6 (L2901) [4/5 units] · **CD:** 16:19 (Doubts) (L233); 16:19 (Legibility and limits) (L927) · **Oda:** printed p.121 / PDF 60 (L47); printed p.80 / PDF 19 (L34).
- **Literal zero-hit terms:** `linéairement équivalent`.

### P02 — Algebraization, projectivity and punctured Picard groups are separate questions

- **Queries → matching lines:** `hensélien` → 0; `complétion` → 0; `projectif` → 2; `Mumford` → 33; `longueur finie` → 0.
- **Union by corpus:** CR 0; RS 0; CT 4; CN 11; CD 2; Oda 18.
- **Candidate locators:** **CT:** 16:22 (L924); 16:19 (L753); 47:7 (L2335); 47:9 (L2439) · **CN:** 16:22:3 (L745); 16:19:2 (L591); 47:7:1 (L1989); 47:9:3 (L2099) [4/8 units] · **CD:** 47:9 (Doubts) (L543); 47:9 (Legibility and limits) (L972) · **Oda:** printed p.64 / PDF 3 (L6); printed p.66 / PDF 5 (L10); printed p.71 / PDF 10 (L25) [3/10 units].
- **Literal zero-hit terms:** `hensélien`; `complétion`; `longueur finie`.

### P03 — The analytic Hua claim is only partly witnessed here

- **Queries → matching lines:** `analytic` → 3; `analytique` → 0; `completion` → 21; `finite length` → 12; `supp` → 185.
- **Union by corpus:** CR 0; RS 14; CT 35; CN 101; CD 37; Oda 28.
- **Candidate locators:** **RS:** 57-analytic-pic-completion-criterion (L116); LM4 F.7 (L19); CYCLOTOMIC_KERNEL E4 (L26) [3/14 units] · **CT:** 16:3 (L33); 16:4 (L120); 16:5 (L133); 16:7 (L216) [4/25 units] · **CN:** 16:7:2 (L137); 16:37:1 (L1063); 44:3:3 (L2521); § Abstract Lefschetz algebra and standard conjectures (L3072) [4/94 units] · **CD:** 44:8 (Legibility and limits) (L990); 16:4 (Doubts) (L82) [2/32 units] · **Oda:** printed p.108 / PDF 47 (L20); printed p.134 / PDF 73 (L19); printed p.64 / PDF 3 (L37) [3/18 units].
- **Literal zero-hit terms:** `analytique`.

### P04 — Keep the two Picard quotient definitions distinct

- **Queries → matching lines:** `Pic(U)^0` → 0; `NS(U)` → 1; `Pic` → 295; `torsion` → 46; `numériquement` → 0.
- **Union by corpus:** CR 2; RS 6; CT 173; CN 47; CD 7; Oda 105.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** LM4 D.12 (L14); LM4 C.17 (L51); FLAGGED_149 A3 (L61) [3/6 units] · **CT:** 16:21 (L872); 16:23 (L947); 47:9 (L2426); 16:1 (L3) [4/50 units] · **CN:** 16:21:3 (L691); 16:19:2 (L595); 16:15:2 (L403); 16:21:1 (L675) [4/32 units] · **CD:** § Abbreviations encountered (L739); § Shared notation table (L29) [2/5 units] · **Oda:** printed p.66 / PDF 5 (L8); printed p.69 / PDF 8 (L36); printed p.103 / PDF 42 (L4) [3/23 units].
- **Literal zero-hit terms:** `Pic(U)^0`; `numériquement`.

### P05 — Sheafification and torsor representability are explicit hypotheses

- **Queries → matching lines:** `fid plat` → 0; `quotient` → 52; `principal homogène` → 0; `représentable` → 0.
- **Union by corpus:** CR 0; RS 13; CT 3; CN 31; CD 3; Oda 2.
- **Candidate locators:** **RS:** LM7 E.23 (L15); LM7_PUSH E.3 (L16); LM6 A.45 (L35) [3/13 units] · **CT:** 16:19 (L747); 16:35 (L1376); 44:8 (L2974) · **CN:** 16:20:4 (L651); 16:21:1 (L675); 16:21:6 (L713); 16:23:4 (L811) [4/26 units] · **CD:** 54:4 (Doubts) (L591); 44:2 (Doubts) (L627) · **Oda:** printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).
- **Literal zero-hit terms:** `fid plat`; `principal homogène`; `représentable`.

### P06 — The weaker quotient-existence expectation stays open on the page

- **Queries → matching lines:** `non ramifié` → 9; `séparé` → 2; `quotient` → 52; `semble` → 28; `existence` → 39.
- **Union by corpus:** CR 0; RS 16; CT 29; CN 61; CD 19; Oda 2.
- **Candidate locators:** **RS:** LM6 A.22 (L13); FLAGGED_149 ZCF6 (L18); LM2 B.g11 (L32) [3/16 units] · **CT:** 16:43 (L1708); 54:4 (L2664); 16:35 (L1376); 16:56 (L2008) [4/14 units] · **CN:** 16:43:2 (L1253); R16 (L2997); 54:4:4 (L2303); 16:51:3 (L1591) [4/55 units] · **CD:** 16:9 (Doubts) (L124); 16:16 (Doubts) (L197) [2/18 units] · **Oda:** printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).

### P07 — A terminology revision changes what is being parameterized

- **Queries → matching lines:** `Pol` → 97; `Nér` → 62; `prépolarisation` → 0; `équivalent` → 20; `ample` → 52.
- **Union by corpus:** CR 1; RS 7; CT 57; CN 98; CD 30; Oda 25.
- **Candidate locators:** **CR:** § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L5) · **RS:** WG2 §2.3 #12 (L108); § Our results so far on these folders (package 231: cotes 57) (L5); LM8 A.12 (L23) [3/7 units] · **CT:** 16:54 (L1958); 44:9 (L2989); 47:3 (L2092); 16:45 (L1729) [4/32 units] · **CN:** 44:9:1 (L2767); D19 (L3584); 16:25:4 (L853); 47:9:6 (L2123) [4/81 units] · **CD:** § Abbreviations encountered (L734); 16:22 (Legibility and limits) (L930) [2/17 units] · **Oda:** printed p.64 / PDF 3 (L4); printed p.120 / PDF 59 (L32); printed p.123 / PDF 62 (L9) [3/18 units].
- **Literal zero-hit terms:** `prépolarisation`.

### P08 — The rational cone deliberately forgets integral scale

- **Queries → matching lines:** `cône` → 0; `polarisation` → 4; `discriminant` → 16; `rationnel` → 0; `intersection` → 36.
- **Union by corpus:** CR 0; RS 0; CT 13; CN 35; CD 3; Oda 2.
- **Candidate locators:** **CT:** 16:23 (L956); 44:2 (L2803); 44:9 (L2989); 16:54 (L1970) [4/10 units] · **CN:** 16:19:3 (L603); R4 (L2863); R5 (L2883); R13 (L2964) [4/28 units] · **CD:** 54:4 (Doubts) (L590); 54:8 (Doubts) (L620) · **Oda:** printed p.119 / PDF 58 (L20); printed p.130 / PDF 69 (L5).
- **Literal zero-hit terms:** `cône`; `rationnel`.

### P09 — The product formula depends on universal hypotheses

- **Queries → matching lines:** `section` → 174; `universelle` → 3; `produit` → 16; `pointé` → 0; `Weil` → 15.
- **Union by corpus:** CR 3; RS 35; CT 39; CN 73; CD 13; Oda 41.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L17) · **RS:** WG H9 (L106); § Our results so far on these folders (package 231: cotes 57) (L5); LM6 A.22 (L13) [3/35 units] · **CT:** 47:3 (L2101); 47:6 (L2289); 16:23 (L956); 16:33 (L1249) [4/25 units] · **CN:** 47:3:4 (L1815); 47:6:1 (L1941); 54:3:2 (L2239); 16:50:1 (L1533) [4/64 units] · **CD:** 16:3 (Doubts) (L63); 47:5 (Doubts) (L508) [2/12 units] · **Oda:** printed p.135 / PDF 74 (L30); printed p.63 / PDF 2 (L17); printed p.64 / PDF 3 (L39) [3/29 units].
- **Literal zero-hit terms:** `pointé`.

### P10 — Fixed parts require care with the action and with scheme structure

- **Queries → matching lines:** `invariant` → 13; `Gamma` → 18; `transport de structure` → 2; `non ramifié` → 9; `Hom` → 428.
- **Union by corpus:** CR 1; RS 14; CT 76; CN 119; CD 15; Oda 242.
- **Candidate locators:** **CR:** § What is in this zip (L29) · **RS:** WG H1 (L105); LM4 F.7 (L19); LM4 C.12 (L34) [3/14 units] · **CT:** 47:11 (L2546); 16:43 (L1708); 16:56 (L2008); 54:6 (L2708) [4/35 units] · **CN:** 47:2:1 (L1783); 47:11:5 (L2213); 44:5:6 (L2631); R17 (L3005) [4/93 units] · **CD:** 44:5 (Doubts) (L664); § Shared notation table (L15) [2/11 units] · **Oda:** printed p.85 / PDF 24 (L1); printed p.88 / PDF 27 (L23); printed p.110 / PDF 49 (L4) [3/67 units].

### P11 — The final openness proposition has missing local dependencies

- **Queries → matching lines:** `viii` → 3; `ouvert` → 7; `rétrocompact` → 0; `platitude` → 4; `Proposition A` → 12.
- **Union by corpus:** CR 2; RS 0; CT 8; CN 11; CD 2; Oda 1.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **CT:** 54:6 (L2707); 16:52 (L1920); 16:56 (L2038); 54:4 (L2666) [4/6 units] · **CN:** 16:56:3 (L1759); 54:6:2 (L2375); 16:15:6 (L431); 16:17:1 (L491) [4/10 units] · **CD:** 16:43 (Doubts) (L391); 47:3 (Legibility and limits) (L966) · **Oda:** printed p.75 / PDF 14 (L24).
- **Literal zero-hit terms:** `rétrocompact`.

## E items

### E01 — The Igusa example is flat but has extra infinitesimal structure

- **Queries → matching lines:** `Igusa` → 3; `Picard variety` → 1; `non-reduced` → 0; `tangent` → 21; `characteristic` → 82.
- **Union by corpus:** CR 0; RS 5; CT 7; CN 46; CD 9; Oda 39.
- **Candidate locators:** **RS:** LM6 E.39 (L52); INTAKE 20261114 §14.1 (L83); FLAGGED_149 Z142g (L28) [3/5 units] · **CT:** 47:6 (L2303); 47:7 (L2376); 54:3 (L2637); 16:45 (L1731) [4/6 units] · **CN:** 47:6:1 (L1941); 47:6:4 (L1965); 47:6:5 (L1969); 47:7:4 (L2015) [4/41 units] · **CD:** § Observed recurring forms (L40); 54:3 (Doubts) (L570) [2/5 units] · **Oda:** printed p.64 / PDF 3 (L11); printed p.134 / PDF 73 (L19); printed p.63 / PDF 2 (L18) [3/23 units].
- **Literal zero-hit terms:** `non-reduced`.

### E02 — Two different Hodge terms drive the proposed asymmetry

- **Queries → matching lines:** `t_A` → 29; `t_B` → 16; `Hodge` → 43; `H^1` → 21; `Omega` → 45; `invariant` → 13.
- **Union by corpus:** CR 0; RS 4; CT 61; CN 61; CD 9; Oda 8.
- **Candidate locators:** **RS:** WG H1 (L105); WG H9 (L106); WG2 §2.3 #12 (L108) [3/4 units] · **CT:** 54:3 (L2613); 47:5 (L2234); 54:5 (L2687); 16:25 (L979) [4/21 units] · **CN:** F17 (L3366); F4 (L3255); D01 (L3433); 47:5:3 (L1899) [4/39 units] · **CD:** § Observed recurring forms (L40); 47:5 (Doubts) (L500) [2/8 units] · **Oda:** printed p.85 / PDF 24 (L43); printed p.88 / PDF 27 (L33); printed p.110 / PDF 49 (L8) [3/6 units].

### E03 — The four pathologies are announced outcomes, not four completed examples

- **Queries → matching lines:** `spécialisation` → 1; `continuité` → 0; `plat` → 23; `sous-schéma abélien` → 0; `vanishing` → 21.
- **Union by corpus:** CR 0; RS 1; CT 19; CN 23; CD 2; Oda 0.
- **Candidate locators:** **RS:** WG H2 (L107) · **CT:** 16:26 (L1081); 16:56 (L2014); 47:3 (L2116); 47:6 (L2320) [4/7 units] · **CN:** 16:56:2 (L1749); 16:12:1 (L283); 16:18:3 (L555); 16:18:4 (L563) [4/22 units] · **CD:** 16:18 (Legibility and limits) (L926); 44:3 (Doubts) (L635).
- **Literal zero-hit terms:** `continuité`; `sous-schéma abélien`.

### E04 — The specialization construction distinguishes integral divisibility from rational identification

- **Queries → matching lines:** `divisibility` → 6; `divisible` → 33; `Hom` → 428; `spécial` → 3; `p-torsion` → 4.
- **Union by corpus:** CR 2; RS 8; CT 66; CN 120; CD 13; Oda 258.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L22); § What is in this zip (L29) · **RS:** 57-ns-p-divisibility-generization (L115); INTAKE 20261114 §4.4 (L85); LM7_PUSH E.67 (L50) [3/8 units] · **CT:** 16:19 (L756); 16:21 (L886); 16:23 (L963); 16:26 (L1081) [4/36 units] · **CN:** 16:19:4 (L609); 47:9:5 (L2115); 16:21:1 (L675); 16:23:4 (L811) [4/93 units] · **CD:** 47:9 (Doubts) (L540); § Shared notation table (L15) [2/11 units] · **Oda:** printed p.113 / PDF 52 (L1); printed p.103 / PDF 42 (L1); printed p.65 / PDF 4 (L1) [3/68 units].

### E05 — The Néron–Severi conclusion and the Hua comparison

- **Queries → matching lines:** `57-ns-p-divisibility` → 1; `Maulik` → 1; `Poonen` → 1; `NS` → 1802; `mixed-characteristic` → 1.
- **Union by corpus:** CR 12; RS 92; CT 780; CN 553; CD 283; Oda 82.
- **Candidate locators:** **CR:** § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L3); § This package in our plan (L9) [2/5 units] · **RS:** 57-ns-p-divisibility-generization (L115); § Our results so far on these folders (package 231: cotes 57) (L5); § Open items: the rows our runs left open, and what we are pushing next (2… (L11) [3/77 units] · **CT:** 16:1 (L5); 16:3 (L29); 16:4 (L75); 16:5 (L125) [4/79 units] · **CN:** § Research notes (L3); 16:3:1 (L11); 16:3:2 (L17); 16:3:3 (L23) [4/365 units] · **CD:** § Shared notation table (L3); § Observed recurring forms (L33) [2/136 units] · **Oda:** NUMDAM cover / PDF 1 (L9); printed p.63 / PDF 2 (L43); printed p.64 / PDF 3 (L6) [3/37 units].

### E06 — Pointwise divisibility does not answer the flatness question

- **Queries → matching lines:** `plat` → 23; `divisible` → 33; `first order` → 0; `Frobenius` → 12; `deformation` → 0.
- **Union by corpus:** CR 1; RS 2; CT 23; CN 15; CD 1; Oda 26.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L22) · **RS:** INTAKE 20261114 §4.4 (L85); 57-ns-p-divisibility-generization (L115) · **CT:** 16:56 (L2014); 47:3 (L2116); 47:6 (L2320); 54:4 (L2658) [4/10 units] · **CN:** 54:5:5 (L2353); 54:7:1 (L2401); 54:7:5 (L2431); S17 (L3203) [4/13 units] · **CD:** 44:3 (Doubts) (L635) · **Oda:** printed p.65 / PDF 4 (L27); printed p.64 / PDF 3 (L29); printed p.80 / PDF 19 (L34) [3/14 units].
- **Literal zero-hit terms:** `first order`; `deformation`.

### E07 — The first-order diagrams need map-level interpretation

- **Queries → matching lines:** `cup` → 13; `tangent` → 21; `extension` → 94; `de Rham` → 50; `compatibilité` → 3.
- **Union by corpus:** CR 1; RS 12; CT 26; CN 67; CD 8; Oda 61.
- **Candidate locators:** **CR:** § What is in this zip (L29) · **RS:** LM6 E.39 (L52); INTAKE 20261114 §14.1 (L83); LM6 B.27 (L17) [3/12 units] · **CT:** 47:6 (L2303); 16:21 (L886); 54:3 (L2627); 47:8 (L2393) [4/17 units] · **CN:** 54:3:3 (L2245); D01 (L3429); 54:3:1 (L2231); 54:5:4 (L2343) [4/48 units] · **CD:** § Observed recurring forms (L40); 54:3 (Doubts) (L570) [2/6 units] · **Oda:** printed p.67 / PDF 6 (L1); printed p.75 / PDF 14 (L1); printed p.77 / PDF 16 (L1) [3/43 units].

### E08 — Continuity of Néron–Severi torsion is distinct from rank continuity

- **Queries → matching lines:** `torsion` → 46; `rang` → 46; `Kummer` → 12; `T_\ell` → 5; `continuité` → 0.
- **Union by corpus:** CR 0; RS 8; CT 26; CN 53; CD 10; Oda 8.
- **Candidate locators:** **RS:** CYCLOTOMIC_KERNEL C1 (L60); LM6 B.22 (L69); INTAKE 20261114 §4.4 (L85) [3/8 units] · **CT:** 16:21 (L866); 16:23 (L948); 16:52 (L1922); 16:14 (L507) [4/10 units] · **CN:** D10 (L3509); 16:21:3 (L691); 16:23:4 (L811); 16:23:2 (L791) [4/40 units] · **CD:** § Abbreviations encountered (L756); 16:21 (Doubts) (L255) [2/7 units] · **Oda:** printed p.66 / PDF 5 (L8); printed p.69 / PDF 8 (L48); printed p.103 / PDF 42 (L7) [3/7 units].
- **Literal zero-hit terms:** `continuité`.

### E09 — Variation and correspondence representability remain differently qualified

- **Queries → matching lines:** `Corr` → 167; `correspondances` → 5; `alpha` → 132; `lambda` → 164; `mu` → 550; `Picard` → 27.
- **Union by corpus:** CR 2; RS 24; CT 291; CN 316; CD 146; Oda 166.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** LM7_PUSH E.19 (L56); § Our results so far on these folders (package 231: cotes 57) (L3); WG2 §2.4 #4 (L109) [3/24 units] · **CT:** 16:18 (L694); 16:47 (L1787); 16:42 (L1619); 16:12 (L397) [4/59 units] · **CN:** 16:18:1 (L537); § References (L3223); S3 (L3098); S9 (L3147) [4/244 units] · **CD:** § Abbreviations encountered (L739); § Observed recurring forms (L37) [2/96 units] · **Oda:** printed p.64 / PDF 3 (L6); printed p.66 / PDF 5 (L9); printed p.79 / PDF 18 (L6) [3/57 units].

### E10 — Extension of an algebraically trivial bundle has two obligations

- **Queries → matching lines:** `trait` → 1; `se prolonge` → 2; `propre` → 2; `représentable` → 0; `Raynaud` → 1.
- **Union by corpus:** CR 0; RS 1; CT 4; CN 1; CD 0; Oda 0.
- **Candidate locators:** **RS:** MPL_142_001-093 §316 (L91) · **CT:** 16:14 (L502); 16:21 (L894); 16:26 (L1091); 47:3 (L2121) · **CN:** 16:26:1 (L861).
- **Literal zero-hit terms:** `représentable`.

## D items

### D01 — Preserve the manuscript's variance conventions

- **Queries → matching lines:** `contravariant` → 13; `covariant` → 2; `Tate` → 226; `Hom` → 428; `Q_p` → 2.
- **Union by corpus:** CR 3; RS 20; CT 114; CN 222; CD 32; Oda 257.
- **Candidate locators:** **CR:** § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L33); § What is in this zip (L29) · **RS:** LM7_PUSH E.67 (L50); LM6 B.22 (L69); LM6 B.27 (L17) [3/20 units] · **CT:** 16:19 (L756); 16:21 (L864); 16:28 (L1157); 16:30 (L1219) [4/38 units] · **CN:** D05 (L3463); R10 (L2933); 16:10:2 (L219); 16:15:6 (L435) [4/179 units] · **CD:** 44:8 (Doubts) (L677); 16:21 (Legibility and limits) (L929) [2/29 units] · **Oda:** printed p.135 / PDF 74 (L1); printed p.114 / PDF 53 (L4); printed p.78 / PDF 17 (L4) [3/69 units].

### D02 — “Modulo finite groups” requires localization on the target side too

- **Queries → matching lines:** `groupes finis` → 2; `modulo` → 13; `Q_p` → 2; `isog` → 15; `Tate` → 226.
- **Union by corpus:** CR 2; RS 17; CT 59; CN 136; CD 23; Oda 20.
- **Candidate locators:** **CR:** § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L33) · **RS:** LM6 B.27 (L17); INTAKE LM6_FINAL_20261114 §1 (L80); LM4 E.20 (L66) [3/17 units] · **CT:** 47:6 (L2330); 44:8 (L2979); 16:18 (L699); 16:19 (L769) [4/14 units] · **CN:** 16:21:1 (L673); R8 (L2915); D03 (L3449); 16:19:5 (L617) [4/124 units] · **CD:** 47:6 (Doubts) (L517); § Abbreviations encountered (L846) [2/23 units] · **Oda:** printed p.65 / PDF 4 (L37); printed p.66 / PDF 5 (L5); printed p.67 / PDF 6 (L29) [3/12 units].

### D03 — The finite test group must not be zero

- **Queries → matching lines:** `p-groupe fini` → 0; `injectif` → 4; `conoyau libre` → 0; `tensor` → 29; `Proposition 3.9` → 2.
- **Union by corpus:** CR 0; RS 0; CT 6; CN 17; CD 9; Oda 3.
- **Candidate locators:** **CT:** 16:36 (L1402); 16:38 (L1480); 16:43 (L1712); 16:23 (L960) [4/6 units] · **CN:** 16:23:2 (L791); 16:29:3 (L933); 16:29:4 (L939); 47:3:3 (L1807) [4/15 units] · **CD:** 16:43 (Doubts) (L390); 47:3 (Doubts) (L487) [2/8 units] · **Oda:** printed p.83 / PDF 22 (L35); printed p.99 / PDF 38 (L40); printed p.100 / PDF 39 (L41).
- **Literal zero-hit terms:** `p-groupe fini`; `conoyau libre`.

### D04 — Oda supplies a precise finite-group-scheme comparison for abelian varieties

- **Queries → matching lines:** `p^A` → 10; `extension` → 94; `Dieudonné` → 5; `Corollary 5.11` → 2; `de Rham` → 50.
- **Union by corpus:** CR 1; RS 10; CT 19; CN 51; CD 8; Oda 61.
- **Candidate locators:** **CR:** § What is in this zip (L29) · **RS:** LM6 B.27 (L17); FLAGGED_149 Z142g (L28); LM4 D.74 (L48) [3/10 units] · **CT:** 54:5 (L2696); 54:7 (L2723); 16:19 (L735); 16:21 (L886) [4/11 units] · **CN:** D05 (L3463); 54:7:4 (L2423); § References (L3623); 54:3:1 (L2231) [4/32 units] · **CD:** § Observed recurring forms (L41); 54:7 (Doubts) (L616) [2/6 units] · **Oda:** printed p.65 / PDF 4 (L1); NUMDAM cover / PDF 1 (L7); printed p.67 / PDF 6 (L1) [3/42 units].

### D05 — General smooth proper varieties receive only a canonical subspace

- **Queries → matching lines:** `Corollary 5.12` → 3; `Pic` → 295; `subspace` → 7; `Hodge` → 43; `tangent` → 21.
- **Union by corpus:** CR 2; RS 7; CT 180; CN 57; CD 13; Oda 103.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** LM6 E.39 (L52); INTAKE 20261114 §14.1 (L83); WG H9 (L106) [3/7 units] · **CT:** 54:3 (L2614); 47:6 (L2303); 16:25 (L979); 44:2 (L2787) [4/55 units] · **CN:** 54:7:3 (L2417); 54:3:3 (L2245); 44:8:5 (L2741); § References (L3223) [4/42 units] · **CD:** 54:3 (Doubts) (L569); 44:8 (Doubts) (L679) [2/9 units] · **Oda:** printed p.64 / PDF 3 (L11); printed p.131 / PDF 70 (L14); printed p.132 / PDF 71 (L4) [3/22 units].

### D06 — The Albanese/divisible part does not exhaust finite torsion

- **Queries → matching lines:** `Albanese` → 13; `divisible` → 33; `torsion` → 46; `Proposition 4.9` → 1; `Picard` → 27.
- **Union by corpus:** CR 3; RS 8; CT 11; CN 46; CD 4; Oda 44.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § This package in our plan (L9) · **RS:** § Our results so far on these folders (package 231: cotes 57) (L3); WG2 §2.4 #4 (L109); 57-analytic-pic-completion-criterion (L116) [3/8 units] · **CT:** 16:21 (L872); 16:23 (L948); 44:8 (L2974); 16:19 (L771) [4/6 units] · **CN:** 16:46:3 (L1391); 44:8:3 (L2729); 16:21:1 (L675); 16:23:4 (L811) [4/33 units] · **CD:** § Abbreviations encountered (L696) · **Oda:** printed p.113 / PDF 52 (L15); printed p.134 / PDF 73 (L4); printed p.135 / PDF 74 (L20) [3/21 units].

### D07 — Duality of extensions is weaker than a canonical splitting

- **Queries → matching lines:** `t_A` → 29; `t_B` → 16; `extension` → 94; `dualité` → 26; `Lambda` → 164; `Cartier` → 48.
- **Union by corpus:** CR 0; RS 12; CT 174; CN 89; CD 23; Oda 55.
- **Candidate locators:** **RS:** LM6 B.27 (L17); FLAGGED_149 Z142g (L28); LM4 D.74 (L48) [3/12 units] · **CT:** 54:5 (L2694); 54:3 (L2617); 47:5 (L2234); 47:11 (L2540) [4/43 units] · **CN:** F4 (L3255); 54:5:4 (L2341); 54:7:2 (L2405); 47:5:3 (L1899) [4/59 units] · **CD:** § Observed recurring forms (L40); 47:5 (Doubts) (L500) [2/14 units] · **Oda:** printed p.66 / PDF 5 (L8); printed p.67 / PDF 6 (L23); printed p.87 / PDF 26 (L3) [3/26 units].

### D08 — Absolute Dieudonné comparison cannot establish relative flatness

- **Queries → matching lines:** `Proposition 2.1` → 1; `flat` → 48; `representable` → 4; `Frobenius` → 12; `platitude` → 4.
- **Union by corpus:** CR 0; RS 0; CT 3; CN 41; CD 3; Oda 20.
- **Candidate locators:** **CT:** 16:56 (L2038); 54:4 (L2666); 54:6 (L2710) · **CN:** 16:56:3 (L1759); 54:5:5 (L2353); 54:7:1 (L2401); 54:7:5 (L2431) [4/34 units] · **CD:** 16:18 (Doubts) (L227); 16:18 (Legibility and limits) (L926) [2/3 units] · **Oda:** printed p.79 / PDF 18 (L3); printed p.65 / PDF 4 (L12); printed p.80 / PDF 19 (L7) [3/13 units].

### D09 — Torsion-free fibres may still have a nonsaturated specialization image

- **Queries → matching lines:** `no torsion` → 2; `Corollary 1.3` → 7; `NS` → 1802; `divisible` → 33; `Cartier` → 48.
- **Union by corpus:** CR 13; RS 92; CT 780; CN 557; CD 284; Oda 144.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L3) [2/5 units] · **RS:** INTAKE 20261114 §4.4 (L85); 57-ns-p-divisibility-generization (L115); § Our results so far on these folders (package 231: cotes 57) (L5) [3/77 units] · **CT:** 16:19 (L728); 16:21 (L864); 16:23 (L948); 44:5 (L2891) [4/79 units] · **CN:** D03 (L3449); 16:19:4 (L609); 16:21:1 (L671); 16:23:4 (L811) [4/365 units] · **CD:** 54:5 (Doubts) (L600); § Shared notation table (L3) [2/136 units] · **Oda:** printed p.65 / PDF 4 (L11); printed p.69 / PDF 8 (L45); printed p.66 / PDF 5 (L5) [3/51 units].

## C items

### C01 — The first gluing example has an explicit function obstruction

- **Queries → matching lines:** `recollement` → 0; `quasi-affine` → 0; `fonctions` → 0; `principal` → 9; `Pic` → 295.
- **Union by corpus:** CR 2; RS 3; CT 169; CN 23; CD 7; Oda 100.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** § Our results so far on these folders (package 231: cotes 57) (L3); WG2 §2.4 #4 (L109); 57-analytic-pic-completion-criterion (L116) · **CT:** 16:1 (L3); 16:3 (L60); 16:4 (L115); 16:5 (L126) [4/50 units] · **CN:** 16:6:1 (L99); 44:9:4 (L2793); R7 (L2909); F4 (L3261) [4/19 units] · **CD:** 16:7 (Legibility and limits) (L915); § Shared notation table (L29) [2/6 units] · **Oda:** printed p.65 / PDF 4 (L4); printed p.113 / PDF 52 (L29); printed p.63 / PDF 2 (L20) [3/21 units].
- **Literal zero-hit terms:** `recollement`; `quasi-affine`; `fonctions`.

### C02 — The involution quotient has its own outstanding verification

- **Queries → matching lines:** `quotient` → 52; `ouvert affine` → 2; `vérifier` → 2; `Gamma` → 18.
- **Union by corpus:** CR 0; RS 18; CT 12; CN 32; CD 6; Oda 2.
- **Candidate locators:** **RS:** LM7_PUSH E.46 (L59); FLAGGED_149 A9 (L62); LM4 F.7 (L19) [3/18 units] · **CT:** 54:6 (L2708); 16:36 (L1438); 44:5 (L2908); 16:19 (L747) [4/6 units] · **CN:** 54:6:2 (L2377); 16:20:4 (L651); 16:21:1 (L675); 16:21:6 (L713) [4/27 units] · **CD:** 44:5 (Doubts) (L664); 54:4 (Doubts) (L591) [2/3 units] · **Oda:** printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).

### C03 — Independent restrictions obstruct projectivity of the second pushout

- **Queries → matching lines:** `indépendantes` → 0; `projectif` → 2; `faisceau inversible` → 2; `polarisation` → 4.
- **Union by corpus:** CR 0; RS 0; CT 5; CN 3; CD 0; Oda 0.
- **Candidate locators:** **CT:** 16:22 (L924); 47:3 (L2088); 47:9 (L2429); 44:2 (L2803) [4/5 units] · **CN:** 16:22:3 (L745); 44:2:4 (L2487); 44:9:1 (L2767).
- **Literal zero-hit terms:** `indépendantes`.

### C04 — Pinching makes the unit contribution visible

- **Queries → matching lines:** `unités` → 0; `O_S` → 8; `généralisé` → 1; `Jacobian` → 13; `toric` → 9; `B11` → 1.
- **Union by corpus:** CR 7; RS 1; CT 6; CN 14; CD 2; Oda 1.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § This package in our plan (L9) [2/3 units] · **RS:** WG2 §2.4 #4 (L109) · **CT:** 47:6 (L2301); 47:7 (L2352); 47:8 (L2383) · **CN:** § References (L3415); 16:44:6 (L1327); 16:47:1 (L1415); 16:47:2 (L1423) [4/13 units] · **CD:** 47:6 (Doubts) (L510); 47:7 (Doubts) (L522) · **Oda:** printed p.119 / PDF 58 (L34).
- **Literal zero-hit terms:** `unités`.

### C05 — A bounded linear system is asserted without its construction

- **Queries → matching lines:** `non complètes` → 0; `Chevalley` → 7; `système linéaire` → 0; `diviseur` → 3; `irrégularité` → 0.
- **Union by corpus:** CR 0; RS 0; CT 3; CN 2; CD 0; Oda 5.
- **Candidate locators:** **CT:** 16:23 (L958); 44:9 (L2995); 44:7 (L2960) · **CN:** 44:7:5 (L2695) · **Oda:** printed p.121 / PDF 60 (L47); printed p.105 / PDF 44 (L50); printed p.112 / PDF 51 (L48) [3/5 units].
- **Literal zero-hit terms:** `non complètes`; `système linéaire`; `irrégularité`.

### C06 — The diangle typescript is not a new Picard or CM computation

- **Queries → matching lines:** `diangle` → 0; `rotation` → 2; `N(X)` → 1; `G_0` → 0; `CM` → 86.
- **Union by corpus:** CR 0; RS 9; CT 75; CN 0; CD 2; Oda 3.
- **Candidate locators:** **RS:** LM6 A.22 (L13); LM7_PUSH E.3 (L16); LM7_PUSH E.64 (L44) [3/9 units] · **CT:** 16:1 (L3); 16:3 (L60); 16:4 (L115); 16:5 (L126) [4/36 units] · **CD:** 16:43 (Legibility and limits) (L950); 54:8 (Legibility and limits) (L982) · **Oda:** printed p.133 / PDF 72 (L17); printed p.117 / PDF 56 (L33); printed p.122 / PDF 61 (L37).
- **Literal zero-hit terms:** `diangle`; `G_0`.

### C07 — A group-scheme immersion proof retains its characteristic restriction

- **Queries → matching lines:** `monomorphisme` → 0; `immersion` → 4; `Cartier` → 48; `réduit` → 7; `caractéristique nulle` → 0.
- **Union by corpus:** CR 0; RS 0; CT 8; CN 8; CD 5; Oda 38.
- **Candidate locators:** **CT:** 16:33 (L1249); 16:43 (L1712); 16:6 (L195); 16:54 (L1966) [4/8 units] · **CN:** F7 (L3283); 54:5:4 (L2341); 54:5:6 (L2359); 54:7:1 (L2401) [4/6 units] · **CD:** 16:43 (Doubts) (L391); 54:6 (Doubts) (L607) [2/4 units] · **Oda:** printed p.63 / PDF 2 (L17); printed p.64 / PDF 3 (L17); printed p.65 / PDF 4 (L37) [3/19 units].
- **Literal zero-hit terms:** `monomorphisme`; `caractéristique nulle`.

### C08 — The bilinear-form Phi is a different object

- **Queries → matching lines:** `Phi` → 629; `bilinéaire` → 8; `sesquilinéaire` → 0; `extension des scalaires` → 0.
- **Union by corpus:** CR 0; RS 10; CT 215; CN 105; CD 58; Oda 247.
- **Candidate locators:** **RS:** LM8 B.28 (L24); LM7_PUSH E.64 (L44); LM7_PUSH A.36 (L55) [3/10 units] · **CT:** 16:21 (L876); 16:27 (L1119); 16:35 (L1376); 16:23 (L956) [4/49 units] · **CN:** 16:3:1 (L11); 16:3:3 (L27); 16:6:4 (L123); 16:7:3 (L147) [4/87 units] · **CD:** § Abbreviations encountered (L704); § Shared notation table (L20) [2/31 units] · **Oda:** printed p.63 / PDF 2 (L31); printed p.64 / PDF 3 (L22); printed p.65 / PDF 4 (L26) [3/70 units].
- **Literal zero-hit terms:** `sesquilinéaire`; `extension des scalaires`.

### C09 — The derived-limit leaf keeps filteredness and finiteness visible

- **Queries → matching lines:** `limite` → 4; `varprojlim` → 1; `filtrant` → 0; `Ext` → 486; `complétion` → 0.
- **Union by corpus:** CR 2; RS 23; CT 219; CN 159; CD 43; Oda 44.
- **Candidate locators:** **CR:** § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L1) · **RS:** § Open items: the rows our runs left open, and what we are pushing next (2… (L11); LM7_PUSH E.3 (L16); LM6 B.27 (L17) [3/23 units] · **CT:** 16:21 (L864); 16:23 (L972); 16:3 (L35); 16:4 (L81) [4/59 units] · **CN:** 16:23:5 (L821); § Research notes (L3); 16:3:2 (L19); 16:4:1 (L35) [4/123 units] · **CD:** 47:7 (Doubts) (L522); § Shared notation table (L22) [2/39 units] · **Oda:** printed p.64 / PDF 3 (L35); printed p.66 / PDF 5 (L36); printed p.67 / PDF 6 (L53) [3/22 units].
- **Literal zero-hit terms:** `filtrant`; `complétion`.

### C10 — The Tribu leaves carry separate algebraic proof tasks

- **Queries → matching lines:** `Tribu` → 30; `p-base` → 3; `dérivations` → 0; `différentielles` → 2; `régulier` → 4.
- **Union by corpus:** CR 0; RS 1; CT 11; CN 20; CD 4; Oda 3.
- **Candidate locators:** **RS:** MPL_145 9 (L98) · **CT:** 16:52 (L1885); 47:11 (L2543); 16:19 (L753); 16:54 (L1956) [4/6 units] · **CN:** 16:35:1 (L1015); 16:39:1 (L1127); 16:44:2 (L1295); 47:6:5 (L1973) [4/17 units] · **CD:** 47:11 (Doubts) (L559); 16:19 (Legibility and limits) (L927) [2/4 units] · **Oda:** printed p.121 / PDF 60 (L35); printed p.122 / PDF 61 (L8).
- **Literal zero-hit terms:** `dérivations`.

## I items

### I01 — Track the integral divisibility locus, not only the rank

- **Queries → matching lines:** `torsion` → 46; `spécialisation` → 1; `NS` → 1802; `Hom` → 428; `rang` → 46.
- **Union by corpus:** CR 13; RS 94; CT 812; CN 612; CD 299; Oda 322.
- **Candidate locators:** **CR:** § What is in this zip (L28); § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L3) [2/5 units] · **RS:** LM4 D.12 (L14); FLAGGED_149 B9 (L27); LM4 C.17 (L51) [3/79 units] · **CT:** 16:21 (L864); 16:23 (L948); 47:8 (L2381); 47:9 (L2421) [4/79 units] · **CN:** 16:7:3 (L147); 16:20:3 (L643); 16:21:1 (L671); 16:21:3 (L689) [4/379 units] · **CD:** § Abbreviations encountered (L687); 44:8 (Doubts) (L675) [2/137 units] · **Oda:** printed p.66 / PDF 5 (L5); printed p.113 / PDF 52 (L1); printed p.134 / PDF 73 (L4) [3/70 units].

### I02 — Use the basic involution example as a control case

- **Queries → matching lines:** `Igusa` → 3; `invariant` → 13; `symmetry` → 18; `tangent` → 21; `Hodge` → 43.
- **Union by corpus:** CR 0; RS 5; CT 13; CN 54; CD 8; Oda 13.
- **Candidate locators:** **RS:** WG H1 (L105); LM6 E.39 (L52); INTAKE 20261114 §14.1 (L83) [3/5 units] · **CT:** 54:3 (L2614); 47:6 (L2303); 47:7 (L2376); 16:25 (L979) [4/10 units] · **CN:** 44:5:6 (L2631); D01 (L3429); 47:6:4 (L1965); 54:5:2 (L2329) [4/42 units] · **CD:** 54:3 (Doubts) (L569); 44:8 (Doubts) (L679) [2/5 units] · **Oda:** printed p.64 / PDF 3 (L13); printed p.134 / PDF 73 (L47); printed p.85 / PDF 24 (L43) [3/10 units].

### I03 — Specialize the pinching sequence to two disjoint points

- **Queries → matching lines:** `généralisé` → 1; `unités` → 0; `toric` → 9; `Chevalley` → 7; `B11` → 1.
- **Union by corpus:** CR 2; RS 0; CT 1; CN 10; CD 0; Oda 4.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L21) · **CT:** 44:7 (L2960) · **CN:** 44:7:5 (L2695); § References (L3415); 16:44:6 (L1327); 16:47:1 (L1415) [4/9 units] · **Oda:** printed p.105 / PDF 44 (L50); printed p.112 / PDF 51 (L48); printed p.134 / PDF 73 (L28) [3/4 units].
- **Literal zero-hit terms:** `unités`.

### I04 — Test equivariant kernels only after fixing the quotient category

- **Queries → matching lines:** `transport de structure` → 2; `contragrédient` → 1; `quotient` → 52; `Fourier` → 15; `Weil` → 15.
- **Union by corpus:** CR 2; RS 15; CT 10; CN 50; CD 4; Oda 3.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L18); § What is in this zip (L28) · **RS:** WG H9 (L106); WG2 §2.4 #4 (L109); LM7 E.23 (L15) [3/15 units] · **CT:** 47:11 (L2564); 44:8 (L2974); 16:50 (L1835); 47:2 (L2081) [4/8 units] · **CN:** § References (L3219); 47:11:5 (L2213); 16:50:1 (L1533); 47:2:1 (L1781) [4/35 units] · **CD:** § Observed recurring forms (L49); 54:4 (Doubts) (L591) [2/3 units] · **Oda:** printed p.135 / PDF 74 (L30); printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).

### I05 — Reconstruct the missing numerical criteria before strengthening closedness

- **Queries → matching lines:** `viii` → 3; `générisation` → 0; `spécialisation` → 1; `numérique` → 4; `projectif` → 2.
- **Union by corpus:** CR 2; RS 0; CT 4; CN 3; CD 1; Oda 0.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **CT:** 16:26 (L1081); 16:22 (L924); 16:52 (L1920); 44:6 (L2944) · **CN:** 16:22:3 (L745); 44:6:1 (L2639); D14 (L3542) · **CD:** § Abbreviations encountered (L852).
- **Literal zero-hit terms:** `générisation`.

## R items

### R01 — Completion target

- **Queries → matching lines:** `widehat` → 13; `Pic` → 295; `completion` → 21; `analytique` → 0.
- **Union by corpus:** CR 2; RS 18; CT 172; CN 30; CD 7; Oda 98.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** LM4 F.7 (L19); 57-analytic-pic-completion-criterion (L116); LM7_PUSH E.3 (L16) [3/18 units] · **CT:** 16:26 (L1073); 16:43 (L1711); 16:1 (L3); 16:3 (L60) [4/51 units] · **CN:** § References (L3419); F18 (L3383); 16:7:2 (L137); 16:37:1 (L1063) [4/23 units] · **CD:** 44:8 (Legibility and limits) (L990); § Shared notation table (L29) [2/6 units] · **Oda:** printed p.105 / PDF 44 (L30); printed p.63 / PDF 2 (L20); printed p.64 / PDF 3 (L11) [3/21 units].
- **Literal zero-hit terms:** `analytique`.

### R02 — Product Picard component and an inserted dual-scheme formula

- **Queries → matching lines:** `pointé` → 0; `A'` → 57; `Pic` → 295; `Weil` → 15; `dual` → 191.
- **Union by corpus:** CR 3; RS 11; CT 239; CN 115; CD 32; Oda 141.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L35) [2/3 units] · **RS:** WG H9 (L106); FLAGGED_149 F8a (L64); LM7 D.19 (L38) [3/11 units] · **CT:** 47:3 (L2110); 44:8 (L2974); 44:5 (L2901); 16:50 (L1835) [4/60 units] · **CN:** § References (L3219); 47:3:4 (L1815); 47:6:1 (L1941); 44:8:3 (L2725) [4/86 units] · **CD:** § Observed recurring forms (L39); 16:3 (Doubts) (L69) [2/25 units] · **Oda:** printed p.135 / PDF 74 (L3); printed p.69 / PDF 8 (L30); printed p.112 / PDF 51 (L12) [3/35 units].
- **Literal zero-hit terms:** `pointé`.

### R03 — Subgroup conditions and the dual factor in the specialization example

- **Queries → matching lines:** `F_1` → 1; `G_1` → 0; `B'` → 5; `Hom` → 428; `NS` → 1802.
- **Union by corpus:** CR 13; RS 94; CT 807; CN 594; CD 291; Oda 314.
- **Candidate locators:** **CR:** § What is in this zip (L28); § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L3) [2/5 units] · **RS:** LM7_PUSH E.67 (L50); LM6 B.22 (L69); LM7 D.37 (L71) [3/79 units] · **CT:** 16:20 (L782); 16:54 (L1958); 16:56 (L2010); 44:5 (L2891) [4/79 units] · **CN:** R1 (L2834); 16:3:1 (L11); 16:4:1 (L33); 16:5:4 (L91) [4/377 units] · **CD:** § Shared notation table (L3); 16:3 (Doubts) (L63) [2/137 units] · **Oda:** NUMDAM cover / PDF 1 (L7); printed p.63 / PDF 2 (L7); printed p.65 / PDF 4 (L1) [3/69 units].
- **Literal zero-hit terms:** `G_1`.

### R04 — The first-order labels are not fixed by a familiar deformation template

- **Queries → matching lines:** `deformation` → 0; `H^2` → 14; `tangent` → 21; `Pic` → 295; `de Rham` → 50.
- **Union by corpus:** CR 3; RS 5; CT 183; CN 36; CD 10; Oda 140.
- **Candidate locators:** **CR:** § What is in this zip (L29); § This package in our plan (L9) [2/3 units] · **RS:** LM6 E.39 (L52); INTAKE 20261114 §14.1 (L83); § Our results so far on these folders (package 231: cotes 57) (L3) [3/5 units] · **CT:** 16:20 (L783); 16:21 (L884); 16:23 (L947); 16:25 (L981) [4/52 units] · **CN:** 54:3:3 (L2245); § References (L3419); R8 (L2917); 47:6:1 (L1941) [4/28 units] · **CD:** § Observed recurring forms (L40); 54:3 (Doubts) (L570) [2/8 units] · **Oda:** printed p.63 / PDF 2 (L7); printed p.65 / PDF 4 (L1); printed p.67 / PDF 6 (L1) [3/47 units].
- **Literal zero-hit terms:** `deformation`.

### R05 — Uncertain conditions in the final question lists

- **Queries → matching lines:** `primaire` → 2; `prénormal` → 0; `constructible` → 0; `invariants` → 5; `platitude` → 4.
- **Union by corpus:** CR 0; RS 1; CT 4; CN 2; CD 0; Oda 4.
- **Candidate locators:** **RS:** WG H1 (L105) · **CT:** 16:21 (L887); 16:56 (L2038); 54:4 (L2666); 54:6 (L2710) · **CN:** 16:21:4 (L697); 16:56:3 (L1759) · **Oda:** printed p.85 / PDF 24 (L43); printed p.88 / PDF 27 (L33); printed p.114 / PDF 53 (L52) [3/4 units].
- **Literal zero-hit terms:** `prénormal`; `constructible`.

### R06 — The finite subgroup wording in the Igusa construction

- **Queries → matching lines:** `Gamma_S` → 0; `translation` → 9; `section` → 174; `dual isogeny` → 0; `Igusa` → 3.
- **Union by corpus:** CR 3; RS 34; CT 23; CN 66; CD 11; Oda 48.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L17) · **RS:** § Our results so far on these folders (package 231: cotes 57) (L5); LM6 A.22 (L13); LM7 E.23 (L15) [3/34 units] · **CT:** 16:6 (L195); 16:19 (L747); 16:23 (L956); 16:33 (L1249) [4/16 units] · **CN:** 47:8:6 (L2073); 47:8:3 (L2049); F10 (L3307); 16:6:2 (L103) [4/59 units] · **CD:** 16:7 (Doubts) (L113); 16:38 (Doubts) (L343) [2/10 units] · **Oda:** printed p.134 / PDF 73 (L47); printed p.64 / PDF 3 (L13); printed p.67 / PDF 6 (L7) [3/31 units].
- **Literal zero-hit terms:** `Gamma_S`; `dual isogeny`.

## S items

### S01 — S01 — 272(i)

- **Queries → matching lines:** `hensélien` → 0; `projectif` → 2; `complétion` → 0.
- **Union by corpus:** CR 0; RS 0; CT 1; CN 1; CD 0; Oda 0.
- **Candidate locators:** **CT:** 16:22 (L924) · **CN:** 16:22:3 (L745).
- **Literal zero-hit terms:** `hensélien`; `complétion`.

### S02 — S02 — 272(ii)

- **Queries → matching lines:** `supp` → 185; `Pic` → 295; `analytic` → 3.
- **Union by corpus:** CR 2; RS 9; CT 200; CN 111; CD 43; Oda 113.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** 57-analytic-pic-completion-criterion (L116); LM6 F.6 (L22); LM8 B.28 (L24) [3/9 units] · **CT:** 16:3 (L33); 16:4 (L115); 16:5 (L126); 16:7 (L216) [4/58 units] · **CN:** 16:19:4 (L609); R11 (L2948); D13 (L3535); 16:52:8 (L1655) [4/100 units] · **CD:** 16:45 (Doubts) (L411); § Abbreviations encountered (L737) [2/35 units] · **Oda:** printed p.134 / PDF 73 (L19); printed p.63 / PDF 2 (L20); printed p.71 / PDF 10 (L40) [3/31 units].

### S03 — S03 — 272(iii), margin

- **Queries → matching lines:** `singulier` → 1; `Mumford` → 33; `Pic` → 295.
- **Union by corpus:** CR 2; RS 3; CT 172; CN 28; CD 8; Oda 115.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** § Our results so far on these folders (package 231: cotes 57) (L3); WG2 §2.4 #4 (L109); 57-analytic-pic-completion-criterion (L116) · **CT:** 16:42 (L1641); 16:19 (L727); 47:9 (L2426); 47:7 (L2335) [4/51 units] · **CN:** § References (L3419); 16:19:2 (L591); 47:7:1 (L1989); 47:9:3 (L2099) [4/20 units] · **CD:** 47:9 (Doubts) (L543); 47:9 (Legibility and limits) (L972) [2/7 units] · **Oda:** printed p.64 / PDF 3 (L6); printed p.66 / PDF 5 (L9); printed p.106 / PDF 45 (L4) [3/27 units].

### S04 — S04 — 276 margin

- **Queries → matching lines:** `type fini` → 9; `quotient` → 52.
- **Union by corpus:** CR 0; RS 13; CT 11; CN 32; CD 3; Oda 2.
- **Candidate locators:** **RS:** LM7 E.23 (L15); LM7_PUSH E.3 (L16); LM6 A.45 (L35) [3/13 units] · **CT:** 16:19 (L730); 16:21 (L872); 16:22 (L924); 54:4 (L2660) [4/7 units] · **CN:** 16:22:3 (L745); 16:20:4 (L651); 16:21:1 (L675); 16:21:6 (L713) [4/27 units] · **CD:** 54:4 (Doubts) (L591); 44:2 (Doubts) (L627) · **Oda:** printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).

### S05 — S05 — 277 end

- **Queries → matching lines:** `semble` → 28; `représentable` → 0; `non ramifié` → 9.
- **Union by corpus:** CR 0; RS 0; CT 18; CN 3; CD 16; Oda 0.
- **Candidate locators:** **CT:** 16:43 (L1708); 16:56 (L2008); 16:9 (L279); 16:35 (L1380) [4/7 units] · **CN:** 16:43:2 (L1253); 16:51:3 (L1591); 54:5:1 (L2321) · **CD:** 16:9 (Doubts) (L124); 16:16 (Doubts) (L197) [2/16 units].
- **Literal zero-hit terms:** `représentable`.

### S06 — S06 — 279 margin

- **Queries → matching lines:** `Matsusaka` → 10; `polarisation` → 4.
- **Union by corpus:** CR 0; RS 0; CT 5; CN 8; CD 1; Oda 0.
- **Candidate locators:** **CT:** 44:9 (L2989); 44:2 (L2803); 16:23 (L960); 44:6 (L2942) · **CN:** 44:2:4 (L2487); 44:9:1 (L2767); 16:23:1 (L781); 44:6:2 (L2647) [4/6 units] · **CD:** 44:6 (Doubts) (L674).

### S07 — S07 — 287–288

- **Queries → matching lines:** `exemples` → 2; `symétrie` → 11; `spécialisation` → 1.
- **Union by corpus:** CR 0; RS 0; CT 8; CN 5; CD 0; Oda 1.
- **Candidate locators:** **CT:** 16:26 (L1081); 16:18 (L697); 47:4 (L2223); 47:6 (L2329) [4/7 units] · **CN:** § References for R9–R22 (L3062); 47:6:4 (L1963); 47:11:6 (L2221); 44:5:1 (L2591) · **Oda:** printed p.114 / PDF 53 (L54).

### S08 — S08 — 294 end

- **Queries → matching lines:** `douteux` → 0; `divisible` → 33; `flat` → 48.
- **Union by corpus:** CR 1; RS 2; CT 5; CN 35; CD 3; Oda 35.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L22) · **RS:** INTAKE 20261114 §4.4 (L85); 57-ns-p-divisibility-generization (L115) · **CT:** 16:19 (L771); 16:21 (L886); 16:23 (L963); 44:5 (L2915) · **CN:** 16:19:4 (L609); 16:21:1 (L675); 16:23:4 (L811); 16:54:3 (L1703) [4/30 units] · **CD:** 16:18 (Doubts) (L227); 16:18 (Legibility and limits) (L926) [2/3 units] · **Oda:** printed p.65 / PDF 4 (L12); printed p.74 / PDF 13 (L9); printed p.76 / PDF 15 (L10) [3/19 units].
- **Literal zero-hit terms:** `douteux`.

### S09 — S09 — 296

- **Queries → matching lines:** `filtrant` → 0; `limite` → 4; `Ext` → 486.
- **Union by corpus:** CR 2; RS 23; CT 218; CN 159; CD 43; Oda 44.
- **Candidate locators:** **CR:** § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L1) · **RS:** § Open items: the rows our runs left open, and what we are pushing next (2… (L11); LM7_PUSH E.3 (L16); LM6 B.27 (L17) [3/23 units] · **CT:** 16:21 (L882); 16:23 (L972); 16:3 (L35); 16:4 (L81) [4/59 units] · **CN:** 16:23:5 (L821); § Research notes (L3); 16:3:2 (L19); 16:4:1 (L35) [4/123 units] · **CD:** 47:7 (Doubts) (L522); § Shared notation table (L22) [2/39 units] · **Oda:** printed p.64 / PDF 3 (L35); printed p.66 / PDF 5 (L36); printed p.67 / PDF 6 (L53) [3/22 units].
- **Literal zero-hit terms:** `filtrant`.

### S10 — S10 — 299 middle

- **Queries → matching lines:** `extension` → 94; `caract` → 14; `régulières` → 0.
- **Union by corpus:** CR 0; RS 10; CT 24; CN 47; CD 8; Oda 19.
- **Candidate locators:** **RS:** LM6 B.27 (L17); FLAGGED_149 Z142g (L28); LM4 D.74 (L48) [3/10 units] · **CT:** 16:28 (L1163); 16:13 (L458); 16:16 (L641); 16:17 (L670) [4/17 units] · **CN:** 16:18:3 (L553); 16:4:1 (L35); 16:9:2 (L187); 16:15:5 (L427) [4/32 units] · **CD:** § Abbreviations encountered (L737); § Observed recurring forms (L41) [2/4 units] · **Oda:** printed p.135 / PDF 74 (L16); printed p.66 / PDF 5 (L36); printed p.67 / PDF 6 (L53) [3/12 units].
- **Literal zero-hit terms:** `régulières`.

### S11 — S11 — 299 end

- **Queries → matching lines:** `diviseur de 0` → 0; `tensoriel` → 0.
- **Union by corpus:** CR 0; RS 0; CT 0; CN 0; CD 0; Oda 0.
- **Candidate locators:** none.
- **Literal zero-hit terms:** `diviseur de 0`; `tensoriel`.

### S12 — S12 — 300

- **Queries → matching lines:** `vérifier` → 2; `affine` → 26; `quotient` → 52.
- **Union by corpus:** CR 0; RS 14; CT 8; CN 39; CD 3; Oda 15.
- **Candidate locators:** **RS:** LM6 A.50 (L68); LM7 E.23 (L15); LM7_PUSH E.3 (L16) [3/14 units] · **CT:** 54:6 (L2708); 16:36 (L1438); 54:8 (L2744); 16:19 (L747) [4/6 units] · **CN:** 54:6:2 (L2373); 54:6:3 (L2385); 54:6:4 (L2393); 54:8:3 (L2457) [4/32 units] · **CD:** 54:4 (Doubts) (L591); 44:2 (Doubts) (L627) · **Oda:** printed p.84 / PDF 23 (L21); printed p.115 / PDF 54 (L45); printed p.117 / PDF 56 (L31) [3/13 units].

### S13 — S13 — 302 end

- **Queries → matching lines:** `quotient` → 52; `projectif` → 2.
- **Union by corpus:** CR 0; RS 13; CT 4; CN 32; CD 3; Oda 2.
- **Candidate locators:** **RS:** LM7 E.23 (L15); LM7_PUSH E.3 (L16); LM6 A.45 (L35) [3/13 units] · **CT:** 16:22 (L924); 16:19 (L747); 16:35 (L1376); 44:8 (L2974) · **CN:** 16:22:3 (L745); 16:20:4 (L651); 16:21:1 (L675); 16:21:6 (L713) [4/27 units] · **CD:** 54:4 (Doubts) (L591); 44:2 (Doubts) (L627) · **Oda:** printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).

### S14 — S14 — 301, 303

- **Queries → matching lines:** `dérivations` → 0; `base` → 112; `différentielle` → 2.
- **Union by corpus:** CR 0; RS 3; CT 28; CN 51; CD 12; Oda 20.
- **Candidate locators:** **RS:** FLAGGED_149 Z142g (L28); LM7 D.45 (L54); LM7 E.30 (L75) · **CT:** 47:11 (L2543); 16:6 (L181); 16:15 (L560); 16:17 (L672) [4/12 units] · **CN:** 16:5:3 (L79); 16:18:1 (L539); 16:22:1 (L721); 16:22:2 (L731) [4/47 units] · **CD:** 47:11 (Doubts) (L559); § Observed recurring forms (L44) [2/11 units] · **Oda:** printed p.66 / PDF 5 (L36); printed p.67 / PDF 6 (L53); printed p.71 / PDF 10 (L38) [3/14 units].
- **Literal zero-hit terms:** `dérivations`.

### S15 — S15 — 303

- **Queries → matching lines:** `Kähler` → 9; `différentielles` → 2.
- **Union by corpus:** CR 0; RS 0; CT 4; CN 6; CD 1; Oda 0.
- **Candidate locators:** **CT:** 47:11 (L2543); 16:52 (L1893) · **CN:** 16:52:6 (L1637); R14 (L2974); R15 (L2987); R16 (L2997) [4/5 units] · **CD:** 47:11 (Doubts) (L559).

### S16 — S16 — 309(a)

- **Queries → matching lines:** `type fini` → 9; `géométriquement` → 1.
- **Union by corpus:** CR 0; RS 0; CT 8; CN 1; CD 1; Oda 0.
- **Candidate locators:** **CT:** 16:19 (L730); 16:21 (L872); 16:22 (L924); 54:4 (L2660) [4/5 units] · **CN:** 16:22:3 (L745) · **CD:** § Abbreviations encountered (L830).

### S17 — S17 — 309(a′)

- **Queries → matching lines:** `quasi-compact` → 0; `fermé` → 6.
- **Union by corpus:** CR 0; RS 0; CT 3; CN 1; CD 2; Oda 0.
- **Candidate locators:** **CT:** 16:43 (L1712); 54:6 (L2707); 54:8 (L2742) · **CN:** 54:6:1 (L2367) · **CD:** 16:43 (Doubts) (L391); 54:6 (Doubts) (L608).
- **Literal zero-hit terms:** `quasi-compact`.

### S18 — S18 — 309(a″), 310(1)

- **Queries → matching lines:** `normal` → 94; `fermé` → 6; `Pic` → 295.
- **Union by corpus:** CR 2; RS 16; CT 173; CN 59; CD 29; Oda 116.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** LM6 A.22 (L13); LM4 F.7 (L19); LM8 B.28 (L24) [3/16 units] · **CT:** 16:43 (L1712); 54:6 (L2707); 54:8 (L2742); 16:54 (L1960) [4/54 units] · **CN:** 47:8:6 (L2071); R11 (L2948); § References (L3419); 54:6:1 (L2367) [4/48 units] · **CD:** § Shared notation table (L3); 16:43 (Doubts) (L391) [2/27 units] · **Oda:** printed p.105 / PDF 44 (L30); printed p.71 / PDF 10 (L10); printed p.72 / PDF 11 (L30) [3/30 units].

### S19 — S19 — 309(b), 310(9)

- **Queries → matching lines:** `quotient` → 52; `existence` → 39.
- **Union by corpus:** CR 0; RS 16; CT 12; CN 57; CD 3; Oda 2.
- **Candidate locators:** **RS:** LM6 A.22 (L13); FLAGGED_149 ZCF6 (L18); LM2 B.g11 (L32) [3/16 units] · **CT:** 16:4 (L120); 16:8 (L239); 16:17 (L666); 16:43 (L1710) [4/9 units] · **CN:** R16 (L2997); 16:4:4 (L57); 16:8:3 (L169); 16:9:1 (L179) [4/52 units] · **CD:** 54:4 (Doubts) (L591); 44:2 (Doubts) (L627) · **Oda:** printed p.82 / PDF 21 (L34); printed p.91 / PDF 30 (L46).

### S20 — S20 — 309(c), 310(3), 311

- **Queries → matching lines:** `ouvert` → 7; `car` → 176; `torsion` → 46.
- **Union by corpus:** CR 3; RS 8; CT 45; CN 83; CD 23; Oda 64.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L15) · **RS:** LM4 D.12 (L14); LM4 C.17 (L51); FLAGGED_149 A3 (L61) [3/8 units] · **CT:** 47:9 (L2461); 16:43 (L1712); 54:6 (L2707); 16:21 (L872) [4/34 units] · **CN:** 54:7:4 (L2425); F15 (L3347); 54:6:2 (L2375); 16:15:2 (L403) [4/65 units] · **CD:** § Abbreviations encountered (L739); 16:43 (Doubts) (L391) [2/14 units] · **Oda:** printed p.66 / PDF 5 (L8); printed p.69 / PDF 8 (L45); printed p.134 / PDF 73 (L4) [3/28 units].

### S21 — S21 — 309(d)

- **Queries → matching lines:** `type fini` → 9; `Weil` → 15; `formelle` → 1.
- **Union by corpus:** CR 0; RS 1; CT 14; CN 9; CD 0; Oda 1.
- **Candidate locators:** **RS:** WG H9 (L106) · **CT:** 54:7 (L2716); 16:19 (L730); 16:21 (L872); 16:22 (L924) [4/10 units] · **CN:** 16:22:3 (L745); 16:50:1 (L1533); 47:3:4 (L1815); 47:6:1 (L1941) [4/6 units] · **Oda:** printed p.135 / PDF 74 (L30).

### S22 — S22 — 309(e)

- **Queries → matching lines:** `séparé` → 2; `représentable` → 0.
- **Union by corpus:** CR 0; RS 0; CT 1; CN 1; CD 0; Oda 0.
- **Candidate locators:** **CT:** 54:4 (L2674) · **CN:** 54:4:4 (L2303).
- **Literal zero-hit terms:** `représentable`.

### S23 — S23 — 309(b′), (f)

- **Queries → matching lines:** `continuité` → 0; `rang` → 46; `fondamental` → 1.
- **Union by corpus:** CR 0; RS 2; CT 16; CN 21; CD 8; Oda 0.
- **Candidate locators:** **RS:** FLAGGED_149 B9 (L27); LM7_PUSH E.62 (L46) · **CT:** 44:5 (L2893); 16:14 (L507); 16:25 (L1015); 16:56 (L2042) [4/6 units] · **CN:** 16:7:3 (L147); 16:15:1 (L391); 16:15:3 (L411); 16:15:7 (L441) [4/19 units] · **CD:** 16:15 (Doubts) (L180); 16:33 (Doubts) (L307) [2/6 units].
- **Literal zero-hit terms:** `continuité`.

### S24 — S24 — 309(g)

- **Queries → matching lines:** `produit` → 16; `géom` → 12; `vérifier` → 2.
- **Union by corpus:** CR 0; RS 0; CT 16; CN 5; CD 9; Oda 0.
- **Candidate locators:** **CT:** 47:3 (L2088); 16:36 (L1438); 54:6 (L2710); 44:4 (L2859) [4/11 units] · **CN:** § References for R9–R22 (L3060); § References (L3627); 16:3:3 (L25); 16:56:4 (L1765) [4/5 units] · **CD:** 47:3 (Doubts) (L481); 44:4 (Doubts) (L648) [2/5 units].

### S25 — S25 — 309(h)

- **Queries → matching lines:** `hyperplane` → 26; `bijectif` → 2.
- **Union by corpus:** CR 0; RS 0; CT 8; CN 20; CD 0; Oda 0.
- **Candidate locators:** **CT:** 16:43 (L1710); 16:54 (L1958); 16:33 (L1249); 16:45 (L1731) [4/7 units] · **CN:** 16:33:2 (L975); 16:42:3 (L1223); 16:44:3 (L1303); 16:45:5 (L1365) [4/17 units].

### S26 — S26 — 310(2)

- **Queries → matching lines:** `Mumford` → 33; `plat` → 23.
- **Union by corpus:** CR 0; RS 0; CT 21; CN 14; CD 3; Oda 18.
- **Candidate locators:** **CT:** 16:56 (L2014); 47:3 (L2116); 47:6 (L2320); 54:4 (L2658) [4/9 units] · **CN:** 16:56:2 (L1749); 16:56:3 (L1759); 47:3:2 (L1797); 44:3:1 (L2503) [4/11 units] · **CD:** 44:3 (Doubts) (L635); 47:9 (Doubts) (L543) [2/3 units] · **Oda:** printed p.64 / PDF 3 (L6); printed p.66 / PDF 5 (L10); printed p.71 / PDF 10 (L25) [3/10 units].

### S27 — S27 — 310(4), N.B.

- **Queries → matching lines:** `multiplication` → 45; `étale` → 35; `n` → 6298.
- **Union by corpus:** CR 22; RS 126; CT 1778; CN 1826; CD 899; Oda 1647.
- **Candidate locators:** **CR:** § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L1); § This package in our plan (L7) [2/5 units] · **RS:** LM1 B.18 (L29); LM7_PUSH E.19 (L56); § Our results so far on these folders (package 231: cotes 57) (L1) [3/99 units] · **CT:** 16:52 (L1883); 16:54 (L1954); 16:56 (L2004); 16:15 (L528) [4/82 units] · **CN:** R22 (L3046); 16:54:1 (L1681); 16:54:3 (L1697); 16:54:5 (L1713) [4/436 units] · **CD:** 16:25 (Doubts) (L275); 16:15 (Legibility and limits) (L923) [2/161 units] · **Oda:** printed p.70 / PDF 9 (L3); printed p.72 / PDF 11 (L4); printed p.74 / PDF 13 (L3) [3/74 units].

### S28 — S28 — 310(5)

- **Queries → matching lines:** `projectif` → 2; `normal` → 94; `lisse` → 4.
- **Union by corpus:** CR 0; RS 13; CT 5; CN 41; CD 22; Oda 19.
- **Candidate locators:** **RS:** LM6 A.22 (L13); LM4 F.7 (L19); LM8 B.28 (L24) [3/13 units] · **CT:** 16:22 (L924); 16:19 (L728); 16:21 (L894); 16:33 (L1249) [4/5 units] · **CN:** 16:22:3 (L745); 16:10:1 (L211); 16:10:4 (L235); 16:10:5 (L241) [4/37 units] · **CD:** 16:19 (Legibility and limits) (L927); § Shared notation table (L3) [2/22 units] · **Oda:** printed p.71 / PDF 10 (L10); printed p.72 / PDF 11 (L30); printed p.77 / PDF 16 (L42) [3/10 units].

### S29 — S29 — 310(5′), nearby margins

- **Queries → matching lines:** `multiplication` → 45; `composantes` → 6.
- **Union by corpus:** CR 0; RS 2; CT 7; CN 27; CD 3; Oda 12.
- **Candidate locators:** **RS:** LM1 B.18 (L29); LM7_PUSH E.19 (L56) · **CT:** 16:15 (L546); 16:19 (L751); 16:51 (L1863); 47:5 (L2275) [4/5 units] · **CN:** 47:5:7 (L1929); F3 (L3249); 16:3:1 (L11); 16:4:1 (L35) [4/26 units] · **CD:** 16:25 (Doubts) (L279); 16:15 (Legibility and limits) (L923) · **Oda:** printed p.70 / PDF 9 (L33); printed p.72 / PDF 11 (L58); printed p.74 / PDF 13 (L12) [3/10 units].

### S30 — S30 — 310(6)

- **Queries → matching lines:** `ordre` → 6; `composantes` → 6; `torsion` → 46.
- **Union by corpus:** CR 0; RS 3; CT 12; CN 31; CD 4; Oda 8.
- **Candidate locators:** **RS:** LM4 D.12 (L14); LM4 C.17 (L51); FLAGGED_149 A3 (L61) · **CT:** 16:19 (L751); 16:21 (L872); 16:15 (L546); 16:25 (L979) [4/8 units] · **CN:** 47:5:7 (L1929); F3 (L3249); 16:15:2 (L403); 16:21:1 (L675) [4/20 units] · **CD:** 16:19 (Doubts) (L234); 16:21 (Doubts) (L254) [2/4 units] · **Oda:** printed p.66 / PDF 5 (L8); printed p.69 / PDF 8 (L48); printed p.103 / PDF 42 (L7) [3/7 units].

### S31 — S31 — 310(7)

- **Queries → matching lines:** `rang` → 46; `NS` → 1802.
- **Union by corpus:** CR 12; RS 93; CT 783; CN 561; CD 290; Oda 82.
- **Candidate locators:** **CR:** § Context for the research notes: package 231 (cotes 57), 12 Nov 2026 (L3); § This package in our plan (L9) [2/5 units] · **RS:** FLAGGED_149 B9 (L27); LM7_PUSH E.62 (L46); § Our results so far on these folders (package 231: cotes 57) (L5) [3/78 units] · **CT:** 16:14 (L490); 16:25 (L996); 16:56 (L2010); 47:8 (L2386) [4/79 units] · **CN:** 16:7:3 (L147); 16:15:1 (L391); 16:15:3 (L411); 16:15:7 (L441) [4/367 units] · **CD:** 16:15 (Doubts) (L180); 16:33 (Doubts) (L307) [2/136 units] · **Oda:** NUMDAM cover / PDF 1 (L9); printed p.63 / PDF 2 (L43); printed p.64 / PDF 3 (L6) [3/37 units].

### S32 — S32 — 310(8)

- **Queries → matching lines:** `composantes connexes` → 0; `disjointe` → 0.
- **Union by corpus:** CR 0; RS 0; CT 0; CN 0; CD 0; Oda 0.
- **Candidate locators:** none.
- **Literal zero-hit terms:** `composantes connexes`; `disjointe`.

### S33 — S33 — 310 footer

- **Queries → matching lines:** `compatibilité` → 3; `spécialisation` → 1; `descente` → 3.
- **Union by corpus:** CR 0; RS 0; CT 3; CN 4; CD 0; Oda 0.
- **Candidate locators:** **CT:** 16:26 (L1081); 16:56 (L2032); 47:8 (L2393) · **CN:** 16:56:2 (L1749); 47:8:1 (L2031); § References (L3627); F7 (L3281).

### S34 — S34 — 311

- **Queries → matching lines:** `Artinien` → 1; `réduit` → 7; `plat` → 23.
- **Union by corpus:** CR 0; RS 0; CT 21; CN 4; CD 3; Oda 0.
- **Candidate locators:** **CT:** 54:4 (L2658); 16:56 (L2014); 54:6 (L2707); 16:6 (L195) [4/8 units] · **CN:** 16:56:2 (L1749); 16:56:3 (L1759); 47:3:2 (L1797); 44:3:1 (L2503) · **CD:** 54:6 (Doubts) (L607); § Abbreviations encountered (L883) [2/3 units].

### S35 — S35 — 311

- **Queries → matching lines:** `torsion` → 46; `Igusa` → 3.
- **Union by corpus:** CR 0; RS 3; CT 5; CN 29; CD 1; Oda 11.
- **Candidate locators:** **RS:** LM4 D.12 (L14); LM4 C.17 (L51); FLAGGED_149 A3 (L61) · **CT:** 16:21 (L872); 16:23 (L948); 47:9 (L2461) · **CN:** 16:15:2 (L403); 16:21:1 (L675); 16:21:3 (L691); 16:21:4 (L695) [4/18 units] · **CD:** § Abbreviations encountered (L756) · **Oda:** printed p.134 / PDF 73 (L4); printed p.64 / PDF 3 (L13); printed p.66 / PDF 5 (L8) [3/8 units].

### S36 — S36 — 313 separation

- **Queries → matching lines:** `séparé` → 2; `séparables` → 0; `Mumford` → 33.
- **Union by corpus:** CR 0; RS 0; CT 4; CN 11; CD 2; Oda 18.
- **Candidate locators:** **CT:** 54:4 (L2674); 16:19 (L753); 47:7 (L2335); 47:9 (L2439) · **CN:** 54:4:4 (L2303); 16:19:2 (L591); 47:7:1 (L1989); 47:9:3 (L2099) [4/8 units] · **CD:** 47:9 (Doubts) (L543); 47:9 (Legibility and limits) (L972) · **Oda:** printed p.64 / PDF 3 (L6); printed p.66 / PDF 5 (L10); printed p.71 / PDF 10 (L25) [3/10 units].
- **Literal zero-hit terms:** `séparables`.

### S37 — S37 — 313 variation

- **Queries → matching lines:** `alpha` → 132; `lambda` → 164; `mu` → 550; `dimension` → 99.
- **Union by corpus:** CR 0; RS 21; CT 284; CN 308; CD 125; Oda 144.
- **Candidate locators:** **RS:** WG H9 (L106); LM6 F.6 (L22); LM7_PUSH E.64 (L44) [3/21 units] · **CT:** 16:46 (L1765); 16:12 (L397); 16:13 (L444); 16:15 (L535) [4/57 units] · **CN:** S4 (L3117); D17 (L3569); S5 (L3121); D13 (L3536) [4/236 units] · **CD:** 44:4 (Doubts) (L646); § Observed recurring forms (L37) [2/83 units] · **Oda:** printed p.106 / PDF 45 (L14); printed p.130 / PDF 69 (L14); printed p.64 / PDF 3 (L6) [3/54 units].

### S38 — S38 — 313 correspondences

- **Queries → matching lines:** `Corr` → 167; `Raynaud` → 1; `correspondances` → 5.
- **Union by corpus:** CR 0; RS 3; CT 26; CN 89; CD 37; Oda 13.
- **Candidate locators:** **RS:** MPL_142_001-093 §316 (L91); LM7_PUSH E.19 (L56); MPL_14_002-044 §108 (L93) · **CT:** 16:18 (L694); 16:47 (L1787); 16:8 (L239); 16:26 (L1064) [4/22 units] · **CN:** 16:18:1 (L537); S19 (L3213); 16:3:3 (L27); 16:7:2 (L137) [4/79 units] · **CD:** 16:4 (Doubts) (L75); 16:5 (Doubts) (L94) [2/35 units] · **Oda:** printed p.71 / PDF 10 (L41); printed p.86 / PDF 25 (L40); printed p.87 / PDF 26 (L37) [3/10 units].

### S39 — S39 — 314

- **Queries → matching lines:** `projectif` → 2; `propre` → 2; `normal` → 94.
- **Union by corpus:** CR 0; RS 13; CT 4; CN 41; CD 21; Oda 19.
- **Candidate locators:** **RS:** LM6 A.22 (L13); LM4 F.7 (L19); LM8 B.28 (L24) [3/13 units] · **CT:** 16:21 (L894); 16:22 (L924); 47:3 (L2121); 16:54 (L1960) · **CN:** 16:22:3 (L745); 16:10:1 (L211); 16:10:4 (L235); 16:10:5 (L241) [4/37 units] · **CD:** § Shared notation table (L3); § Observed recurring forms (L45) [2/21 units] · **Oda:** printed p.71 / PDF 10 (L10); printed p.72 / PDF 11 (L30); printed p.77 / PDF 16 (L42) [3/10 units].

### S40 — S40 — 315

- **Queries → matching lines:** `prolonge` → 2; `représentable` → 0; `Raynaud` → 1.
- **Union by corpus:** CR 0; RS 1; CT 1; CN 1; CD 0; Oda 0.
- **Candidate locators:** **RS:** MPL_142_001-093 §316 (L91) · **CT:** 16:26 (L1091) · **CN:** 16:26:1 (L861).
- **Literal zero-hit terms:** `représentable`.

## T items

### T01 — T01 — 274

- **Queries → matching lines:** `Polarisation` → 4; `Néron` → 17.
- **Union by corpus:** CR 0; RS 1; CT 5; CN 12; CD 2; Oda 0.
- **Candidate locators:** **RS:** WG2 §2.3 #12 (L108) · **CT:** 44:9 (L2989); 44:2 (L2803); 16:21 (L886); 44:4 (L2849) · **CN:** 44:9:1 (L2767); 44:2:4 (L2487); 16:19:1 (L587); 16:21:4 (L699) [4/11 units] · **CD:** 44:4 (Doubts) (L650); § Abbreviations encountered (L734).

### T02 — T02 — 282

- **Queries → matching lines:** `Exemples` → 2; `Igusa` → 3.
- **Union by corpus:** CR 0; RS 0; CT 0; CN 1; CD 0; Oda 4.
- **Candidate locators:** **CN:** § References for R9–R22 (L3062) · **Oda:** printed p.114 / PDF 53 (L54); printed p.64 / PDF 3 (L13); printed p.134 / PDF 73 (L47).

### T03 — T03 — 305

- **Queries → matching lines:** `Chevalley` → 7; `non complètes` → 0; `Albanese` → 13.
- **Union by corpus:** CR 0; RS 0; CT 2; CN 11; CD 2; Oda 5.
- **Candidate locators:** **CT:** 44:7 (L2960); 44:8 (L2974) · **CN:** 44:7:5 (L2695); 16:46:3 (L1391); 44:2:1 (L2465); 44:2:2 (L2473) [4/9 units] · **CD:** § Abbreviations encountered (L696) · **Oda:** printed p.112 / PDF 51 (L47); printed p.105 / PDF 44 (L50); printed p.134 / PDF 73 (L28) [3/4 units].
- **Literal zero-hit terms:** `non complètes`.

### T04 — T04 — 308

- **Queries → matching lines:** `Questions` → 10; `Pic` → 295.
- **Union by corpus:** CR 4; RS 5; CT 169; CN 23; CD 6; Oda 98.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L35) [2/3 units] · **RS:** LM7 D.19 (L38); § Questions of our planning document (the war game) for these folders (6 o… (L102); § Our results so far on these folders (package 231: cotes 57) (L3) [3/5 units] · **CT:** 16:1 (L3); 16:3 (L60); 16:4 (L115); 16:5 (L126) [4/50 units] · **CN:** 16:51:1 (L1575); 16:52:2 (L1607); § Post-freeze research and literature comparisons (L2822); R14 (L2974) [4/19 units] · **CD:** § Shared notation table (L29); 16:19 (Doubts) (L230) [2/5 units] · **Oda:** printed p.121 / PDF 60 (L47); printed p.63 / PDF 2 (L20); printed p.64 / PDF 3 (L11) [3/22 units].

### T05 — T05 — 272, 291, 309, 313, 314

- **Queries → matching lines:** `Questions` → 10; `groupes divisibles` → 0; `Séparation` → 0; `Variation` → 0.
- **Union by corpus:** CR 2; RS 2; CT 0; CN 5; CD 0; Oda 1.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L24); § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L35) · **RS:** LM7 D.19 (L38); § Questions of our planning document (the war game) for these folders (6 o… (L102) · **CN:** 16:51:1 (L1575); 16:52:2 (L1607); § Post-freeze research and literature comparisons (L2822); R14 (L2974) [4/5 units] · **Oda:** printed p.121 / PDF 60 (L47).
- **Literal zero-hit terms:** `groupes divisibles`; `Séparation`; `Variation`.

### T06 — T06 — 271, 273, 295, 296, 299, 301, 312

- **Queries → matching lines:** `Tribu` → 30; `page` → 359; `n°` → 34.
- **Union by corpus:** CR 2; RS 6; CT 220; CN 127; CD 53; Oda 1.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L24); § `notes/RESULTS_STATE.md` (added 15 Nov 2026 16:00 UTC) (L35) · **RS:** MPL_145 9 (L98); § Our results so far on these folders (package 231: cotes 57) (L5); LM8 B.28 (L24) [3/5 units] · **CT:** 16:52 (L1883); 16:54 (L1954); 16:56 (L2004); 44:7 (L2948) [4/82 units] · **CN:** 44:7:1 (L2663); 16:39:1 (L1127); 47:6:5 (L1973); 47:11:2 (L2191) [4/118 units] · **CD:** 44:6 (Legibility and limits) (L988); § Abbreviations encountered (L719) [2/46 units] · **Oda:** printed p.63 / PDF 2 (L15).

### T07 — T07 — 299, 301, 303

- **Queries → matching lines:** `Tribu` → 30; `Octobre` → 0; `THEORIE DES CORPS` → 0.
- **Union by corpus:** CR 0; RS 1; CT 7; CN 20; CD 2; Oda 0.
- **Candidate locators:** **RS:** MPL_145 9 (L98) · **CT:** 16:52 (L1885); 16:54 (L1956); 16:56 (L2006); 44:7 (L2954) · **CN:** 16:35:1 (L1015); 16:39:1 (L1127); 16:44:2 (L1295); 47:6:5 (L1973) [4/17 units] · **CD:** 44:6 (Doubts) (L674); 44:6 (Legibility and limits) (L988).
- **Literal zero-hit terms:** `Octobre`; `THEORIE DES CORPS`.

### T08 — T08 — all 43 scans

- **Queries → matching lines:** `pages` → 25; `scans` → 52; `271` → 3.
- **Union by corpus:** CR 4; RS 35; CT 0; CN 32; CD 3; Oda 1.
- **Candidate locators:** **CR:** § This package in our plan (L9); § What our planning document asks of these folders (L16) [2/3 units] · **RS:** 57-analytic-pic-completion-criterion (L116); LM8 B.28 (L24); § Our results so far on these folders (package 231: cotes 57) (L5) [3/34 units] · **CN:** 16:41:3 (L1199); R2 (L2842); 16:20:2 (L635); 16:21:1 (L675) [4/29 units] · **CD:** § Legibility and limits (L908); § Shared notation table (L3) [2/3 units] · **Oda:** printed p.76 / PDF 15 (L26).

## G items

### G01 — G01 — 275–288, 314–315

- **Queries → matching lines:** `WG2` → 3; `Picard` → 27; `43` → 73.
- **Union by corpus:** CR 4; RS 10; CT 27; CN 23; CD 20; Oda 17.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L15); § This package in our plan (L9) · **RS:** WG2 §2.4 #4 (L109); WG2 §1.1 #3 (L104); WG2 §2.3 #12 (L108) [3/10 units] · **CT:** 16:1 (L7); 16:19 (L763); 16:23 (L946); 16:26 (L1072) [4/9 units] · **CN:** § References (L3411); 16:19:1 (L587); 16:46:3 (L1391); 47:8:5 (L2065) [4/15 units] · **CD:** § Abbreviations encountered (L739); § Observed recurring forms (L44) [2/5 units] · **Oda:** printed p.63 / PDF 2 (L20); printed p.134 / PDF 73 (L28); printed p.135 / PDF 74 (L23) [3/9 units].

### G02 — G02 — 271–315

- **Queries → matching lines:** `Fourier` → 15; `Th. 1` → 7; `compatibilité` → 3.
- **Union by corpus:** CR 3; RS 1; CT 5; CN 12; CD 1; Oda 2.
- **Candidate locators:** **CR:** § What our planning document asks of these folders (L18); § What is in this zip (L28) · **RS:** WG2 §2.4 #4 (L109) · **CT:** 47:8 (L2393); 16:30 (L1215); 16:54 (L1972); 44:2 (L2787) [4/5 units] · **CN:** 47:8:1 (L2031); F7 (L3281); 47:2:1 (L1781); § References (L3409) [4/6 units] · **CD:** § Observed recurring forms (L49) · **Oda:** printed p.102 / PDF 41 (L11); printed p.118 / PDF 57 (L38).

### G03 — G03 — 275, 280–281, 309, 314–315

- **Queries → matching lines:** `H9` → 1; `Hodge` → 43; `hauteur` → 0; `hyperplan` → 31.
- **Union by corpus:** CR 0; RS 2; CT 21; CN 47; CD 3; Oda 0.
- **Candidate locators:** **RS:** WG H9 (L106); WG2 §2.3 #12 (L108) · **CT:** 16:47 (L1787); 16:33 (L1249); 16:42 (L1658); 16:45 (L1731) [4/14 units] · **CN:** 16:49:3 (L1511); 16:33:2 (L975); 16:42:3 (L1223); 16:44:3 (L1303) [4/36 units] · **CD:** 54:3 (Doubts) (L569); 44:8 (Doubts) (L681) [2/3 units].
- **Literal zero-hit terms:** `hauteur`.

### G04 — G04 — 285, 289–292, 311

- **Queries → matching lines:** `57-ns-p-divisibility` → 1; `divisibility` → 6.
- **Union by corpus:** CR 0; RS 1; CT 0; CN 4; CD 1; Oda 0.
- **Candidate locators:** **RS:** 57-ns-p-divisibility-generization (L115) · **CN:** 16:19:4 (L611); 47:9:5 (L2115); 44:5:3 (L2609); R8 (L2917) · **CD:** 47:9 (Doubts) (L540).

### G05 — G05 — 271–272

- **Queries → matching lines:** `57-analytic-pic` → 1; `finite length` → 12.
- **Union by corpus:** CR 0; RS 1; CT 0; CN 0; CD 0; Oda 11.
- **Candidate locators:** **RS:** 57-analytic-pic-completion-criterion (L116) · **Oda:** printed p.64 / PDF 3 (L37); printed p.83 / PDF 22 (L44); printed p.87 / PDF 26 (L8) [3/6 units].

### G06 — G06 — 289–292, 309(f), 311

- **Queries → matching lines:** `H1` → 12; `B9` → 2; `p-primary` → 2; `centralizer` → 13.
- **Union by corpus:** CR 0; RS 15; CT 0; CN 0; CD 1; Oda 11.
- **Candidate locators:** **RS:** CYCLOTOMIC_KERNEL C1 (L60); WG H1 (L105); FLAGGED_149 B9 (L27) [3/15 units] · **CD:** 16:20 (Doubts) (L243) · **Oda:** printed p.64 / PDF 3 (L33); printed p.106 / PDF 45 (L24); printed p.63 / PDF 2 (L35) [3/10 units].

### G07 — G07 — 288, 298–304

- **Queries → matching lines:** `H2` → 3; `B.22` → 1; `vanishing` → 21; `Kummer` → 12.
- **Union by corpus:** CR 0; RS 5; CT 3; CN 25; CD 2; Oda 0.
- **Candidate locators:** **RS:** LM6 B.22 (L69); WG H2 (L107); CYCLOTOMIC_KERNEL E4 (L26) [3/5 units] · **CT:** 16:21 (L882); 16:23 (L963); 16:52 (L1922) · **CN:** 16:20:3 (L641); 16:21:3 (L691); 16:23:2 (L791); 16:23:4 (L811) [4/25 units] · **CD:** 16:21 (Doubts) (L255); 16:18 (Legibility and limits) (L926).

### G08 — G08 — 291–292, 295

- **Queries → matching lines:** `G.20` → 3; `A.22` → 1; `E.3` → 15; `E.65` → 6.
- **Union by corpus:** CR 0; RS 18; CT 0; CN 1; CD 0; Oda 0.
- **Candidate locators:** **RS:** LM6 A.22 (L13); § Our results so far on these folders (package 231: cotes 57) (L8); LM7_PUSH E.62 (L46) [3/18 units] · **CN:** § References (L3417).

## Coverage and source inventory

| Prefix | Expected | Recorded |
|---|---:|---:|
| F | 3 | 3 |
| J | 7 | 7 |
| P | 11 | 11 |
| E | 10 | 10 |
| D | 9 | 9 |
| C | 10 | 10 |
| I | 5 | 5 |
| R | 6 | 6 |
| S | 40 | 40 |
| T | 8 | 8 |
| G | 8 | 8 |

All-zero-hit items: S11, S32. Zero-hit item-term entries: 80. These are search outcomes, not missing search records.

- CR: 1 file(s), 35 lines. Supplied package scope and research instructions.
- RS: 1 file(s), 151 lines. Mixed-status register; a lexical hit does not change an entry's stated status.
- CT: 1 file(s), 3001 lines. Supplied earlier transcription; not second-passed, a provisional witness.
- CN: 1 file(s), 3637 lines. Supplied earlier research notes; unreviewed claims and bibliographic leads.
- CD: 1 file(s), 991 lines. Supplied earlier doubts; reported reading uncertainties, not newly inspected images.
- Oda: 74 file(s), 3610 lines. Supplied extraction of the printed primary paper; keyword hits alone are not verification.

The companion JSON retains every parsed ID exactly once, exact terms, notes-line provenance, per-term/per-corpus counts, limited candidate locators, and hashes of the allowlisted source files.
