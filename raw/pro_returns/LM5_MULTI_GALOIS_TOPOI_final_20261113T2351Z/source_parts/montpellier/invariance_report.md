# F(h-added)(2): completion and link invariance

Completed in `F_invariance.tex`, statements F.40–F.42. All requested alternatives and both examples decided. No custom LaTeX macros; uses standard amsmath/amssymb and proof environment.

## Main correction

The reviewer's proposed contrast is false. Proper-compactification invariance holds nonarchimedeanly as an actual analytic isomorphism, and archimedeanly already as the exact pro-system of open subsets U minus compact subsets. In SNC complex compactifications, that pro-system has a constant homotopy model given by the boundary of the real oriented blow-up. Failure of the map from the link into U is a separate property, false in both requested examples.

“No hypothesis” can mean no smoothness, SNC, or characteristic-zero assumption in the precise trivially valued nonarchimedean statement. It cannot remove properness: Gm in A1 yields one interval and in P1 yields two. The notation formal completion minus D is not literally an open formal subscheme: its underlying open complement would be empty.

## Explicit computations

The curve has archimedean link three circles, U a wedge of two circles, and underlying nonarchimedean tube three intervals.

For M0,5 the integral Betti numbers through degree three are U=(1,5,6,0), archimedean link=(1,11,11,1), and underlying nonarchimedean tube=(1,6,0,0). The Petersen graph has 10 vertices and 15 edges; its H1 has rank 6. The plumbing intersection matrix is adjacency minus identity and has Smith diagonal (1,1,1,1,1,0,0,0,0,0). The proof uses the unimodular blow-up lattice to explain, not merely compute, the Smith cokernel. The finite exact computation is in `code/invariance_checks.py` with checked output.

## Reading

Read transcription and directly viewed the complete image `background/scans/149/MPL_149_091-136_scan133.jpg`. Folio is 66, marginal printed page 132. Relevant sentence is independent of the uncertain local-tubulure exact sequence below it. Two reading rows supplied separately for merging.

## Verified primary sources

All four entries in `invariance_refs.bib` are marked verified with opened passage. Sources:

- Ben-Bassat–Temkin, full preprint: https://math.huji.ac.il/~temkin/papers/Tubular_Descent.pdf ; section 3.3.2 and Proposition 4.5.1. Open/find refs turn55view0–turn55view2.
- Thuillier, full 2006 preprint: https://epub.uni-regensburg.de/561/1/10-2006.pdf ; Theorem 3.25, Proposition 4.5, Theorem 4.6. Open/find refs turn66view1, turn83view0, turn84view3. Theorem numbering is explicitly that of this preprint.
- Weber, published full primary text in volume: https://www.journalofsing.org/volume4/volume4.pdf ; article pages171–179, section2 p172 and section4 p173. Refs turn66view2–3. Only supports the familiar cohomology invariant; the full pro-object proof is supplied independently.
- Dolgachev–Farb–Looijenga, primary full author-hosted article: https://math.uchicago.edu/~farb/papers/wiman.pdf ; sections2.1–2.2, Petersen graph and blow-up descriptions. Refs turn83view2, turn84view1–2. Publisher metadata opened https://link.springer.com/article/10.1007/s40879-018-0231-3 , ref turn84view0.

Failed retrieval of old Michigan author PDF (redirect404) is not used; the Chicago author copy was successfully opened.
