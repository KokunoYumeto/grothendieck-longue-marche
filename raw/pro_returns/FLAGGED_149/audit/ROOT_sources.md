# Source audit for F8, F10, G and the opening of cote 142

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.

All sources below were opened in full at the indicated statement, rather than inferred from a search snippet. The bibliography gives the URLs and exact versions. Attached sources were read from the files supplied with this task. The mathematical paper states the inputs with their hypotheses and gives the comparison maps.

| Source / opened version | Exact input | Use and qualification |
|---|---|---|
| Constantin–Kolev, attached arXiv math/0303256v1 | Lemma 2.5; Theorem 3.1; Proposition 3.3(1) | Invariant disc and periodic local rotation. G1 proves the global identity-on-an-open-set implication and the isolated fixed-point assertion. |
| SGA 1, recomposed arXiv math/0206203 | XII, Theorem 5.1; X, Corollary 1.8; XIII, Corollaries 2.9 and 2.12 | Complex finite-cover comparison, proper base invariance, tame/prime-to-characteristic curve comparison. No full affine base invariance is asserted in positive characteristic. |
| Yagasaki, attached arXiv math/0010223v1 | Theorem 1.1(ii); Lemma 2.1(i); Theorem 2.1 | Contractibility of the identity component of the compact-open homeomorphism group in the hyperbolic cases. The listed elementary exceptions are checked against the surface type. |
| Earle–Eells, Bull. AMS 73 (1967), 557–559, attached announcement | Theorem 1 | A comparison statement for diffeomorphisms only. The homeomorphism conclusion uses Yagasaki. |
| Kerckhoff, Bull. AMS (N.S.) 2 (1980), 452–454, attached announcement | Theorem 1 | Nielsen realization allows fixed points. G5 gives a genus-two parity obstruction to a free realization. |
| Paris, arXiv math/0703703v1, PDF internally dated 14 October 2017 | Theorem 1.4 | Residual p property of the mod-p Torelli kernel of Out(P), for finitely generated free and surface groups. G8 writes the finite-index normal-core argument transferring residual finiteness. |
| Farb–Margalit, opened draft version 5.0 | Theorems 4.9, 4.11, 8.8, 10.6; section 10.6.3 | Finite generation in all relevant types, Dehn–Nielsen–Baer injection and contractible Teichmüller uniformization. Numbering is from the opened draft. |
| Stix, attached arXiv 0809.0017v1 | Proposition 8; Lemma 10; Proposition 11; Corollary 12; Theorem 14 | Cusp packet embeddings, disjointness and normalizer calculation, including type (0,3). Type (0,2) is calculated independently. |
| Attached CYCLOTOMIC_KERNEL return | B1 and its proof | The prompt expressly permits this citation. The auxiliary prime is also required to be unramified in the number field. This supplied derivation is not represented as an external primary source. |
| Noohi, arXiv math/0503247v1, 81-page PDF | Theorem 20.4 and proof, pp. 80–81 | Riemann existence for algebraic stacks locally of finite type over C; used on the pointed moduli/Hurwitz stacks, including their stabilizers. |
| Bertin–Romagny, arXiv math/0701680, 155-page PDF internally marked January 2007, version 2 | Definition 6.8; Theorem 6.9; Proposition 6.14; Theorem 6.20 | Hurwitz stack, branch morphism, stack/fibre distinction and nongalois variant. The target transport retains deck automorphisms; no coarse-space replacement is used. |
| Bresciani, Algebraic Geometry 8(2) (2021), 231–267 | Lemma A.22; Proposition A.23, pp. 263–264 | Characteristic-zero invariance of finite étale data for concentrated fibred categories and geometrically connected fundamental gerbes. Applied componentwise to Hurwitz stacks, and with finite classifying stacks to descend the covers. |

## Primary-source locations

- [Constantin–Kolev](https://arxiv.org/abs/math/0303256)
- [Yagasaki](https://arxiv.org/abs/math/0010223)
- [Paris](https://arxiv.org/abs/math/0703703)
- [Farb–Margalit draft](https://pagine.dm.unipi.it/~a019210/Farb%20Magalit_Primer%20on%20Teichmuller%20theory.pdf)
- [SGA 1](https://arxiv.org/abs/math/0206203)
- [Stix preprint](https://arxiv.org/abs/0809.0017)
- [Noohi](https://arxiv.org/abs/math/0503247)
- [Bertin–Romagny](https://arxiv.org/abs/math/0701680)
- [Bresciani published PDF](https://content.algebraicgeometry.nl/2021-2/2021-2-005.pdf)

## Manuscript checks

The complete opening transcription, cote 142 scans 1–22, was read. The attached scans 3–14 were inspected, with scans 4, 6, 5, 7 in their actual reading order. Cote 149 scans 45 and 54 were checked for the F8/F10 wording. The reading ledger preserves the nonfinal character of every doubtful reading. Scans 15–22 of cote 142 were available as transcription, not as supplied images.

## Independent arguments and finite computations

G2 gives the topological homology proof and proves its integral congruence lemma. G6–G10 construct the categorical completion and give explicit counterexample categories. Z142c computes the non-descending Artin–Schreier class. Z142e explicitly factors the degree-six family (z^3−3z+t)^2 into two finite étale covers and two puncture fillings; its twenty source punctures remain distinct while two branch values separate. Z142f supplies its actual restriction map. code/G_checks.py records the exact cubic discriminants, critical values, factorization identities and finite surface examples. These arguments are not attributed to an unverified source, and no novelty claim is made.

The group-rigidity contribution independently audited G6–G9. The Hurwitz comparison was checked with the additional instruction to apply connected-gerbe invariance separately to each geometrically connected component. The correction is present in Z142b.
