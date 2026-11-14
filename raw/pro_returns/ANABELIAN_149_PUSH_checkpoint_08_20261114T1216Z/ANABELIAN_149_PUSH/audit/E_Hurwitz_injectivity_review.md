# E.13: genus-zero faithfulness, exact scope and source audit

## Status and deliverables

The complete proof is integrated as `sections/E_Hurwitz_injectivity_extension.tex`, after root read and approved every step. It is included by `sections/E.tex` before the separately owned arithmetic-image argument. The independent restricted-cancellation and chosen-sheet review by `/root/topos` is in `audit/E_chosen_sheet_topos_review.md`. The two new bibliographic entries in `audit/E_Hurwitz_sources.bib` have been appended, with permission, to `sources/root_refs.bib`.

The statement concerns the explicit labelled/coloured presentation in E.8: continuous, type-preserving category autoequivalences preserving covering and filling generators, the finite labelling/colour groupoids, their label-forgetting maps, and all specified puncture deletions. The finite permutation quotients are part of this structure. They are not inferred from a weaker unspecified compatibility condition on abstract unlabelled groups.

**Conclusion:** identity of the COMPLETE genus-zero outer-action system forces identity of every outer mapping-class action. This proves faithfulness of restriction for systems induced by the specified autoequivalences. It does not classify autoequivalences with a fixed system, identify an arbitrary genus-zero system with an element of GT, or prove that arbitrary genus-zero conjugators lift.

Manuscript question locus: **142; manuscript pp. 7–10; scans 15–21; especially the programme on scan 17 and the puncture-forgetting structure in Z142f/R26.** The proof is a derivation for the present question, with no assertion that it appears in the historical manuscript and no priority claim.

## Proof obligations checked

1. The compact outer-homomorphism category supplies an auxiliary continuous profinite surface-group functor. Its existence uses neither congruence injectivity nor a profinite Dehn–Nielsen–Baer theorem.
2. A balanced degree-d cover/filling square gives an inclusion between two index-d subgroups. Equality proves that its completed image is the genuine puncture-pullback right orbit, with exactly d new degree-one cusps.
3. Restricted cancellation is first proved DISCRETELY: the ordinary pi1 functor turns equality `(fu)a=fu` into a normalizer relation for the covering subgroup. The corresponding deck map and the forgotten mapping class have the same outer ordinary-pi1 action; ordinary homotopy-to-isotopy identifies them. The full profinite conclusion then follows from E.6's stabilizer-closure formula and the closed kernel of the surjective forgetting homomorphism.
4. The finite deck group survives completion. Its free action on an affine hyperbolic surface gives the rational graph-homology module `Q ⊕ Q[D]^(r−1)` with r≥2, so one finite homology quotient detects every deck element.
5. The full profinite Birman kernel is established by the centre-free free-profinite action, not by assuming the mapping-class congruence subgroup property. The double-deletion square recovers each cusp's closed normal closure.
6. The chosen-sheet construction includes the condition that the filled source marking is the identity. This removes a possible deck adjustment. Restricted cancellation makes that condition an open kernel of a finite deck quotient, which justifies the density and completion step for arbitrary F-image completed squares.
7. The genus-zero pure completion is centre-free by Birman induction. For every colour partition the finite permutation quotient acts faithfully on pure rational first homology. The explicit pair-meridian presentation proves this also when an individual colour has only two elements.
8. Source cusp target-incidence and exact positive integral ramification index are recovered from normal-closure preservation and the distinct cusp lines in genus-zero abelianization. No profinite Magnus property is asserted.
9. For `d ≥ 2g+2n+5`, the marked Hurwitz source map is smooth and surjective with geometrically connected fibres. The fixed-curve parameter space is a vector bundle of functions with varying reduced pole divisor, cut by n independent derivative conditions. All bad loci are controlled by jet lengths at most `2n+4`; their incidence dimensions are explicitly smaller. Remaining branch points are unordered, which avoids an artificial disconnected ordering fibre.
10. The branch map is finite étale, its connected monodromy is S_d, and its degree-d centralizer is trivial. The source-fundamental-group surjection then forces the normalized higher-genus action to be the identity. The proof includes the proper genus≥2 and once-punctured genus-one cases.

## Opened exact primary sources

### Ordinary homotopy-to-isotopy

Cantwell, J., & Conlon, L. (2014). *Hyperbolic geometry and homotopic homeomorphisms of surfaces* (arXiv:1305.1379v3, 6 March 2014). <https://arxiv.org/pdf/1305.1379>.

Opened the complete 17-page primary PDF and the full statement/proof of Theorem 5.6(1), printed p. 13, together with Corollary 5.7, printed p. 14. Definition 1.2 is on printed p. 2; Proposition 6.4 on printed p. 15 supplies the standard complete metric for a finite-type negative-Euler-characteristic surface with annular ends. The finite-area punctured surfaces in E.13 have no simply connected ends. Tool openings: `turn560view0`, `turn561view0`, `turn561view1`; earlier `turn544view0–1` also opened the same exact clauses. This source is used only before profinite completion.

Parent independently opened an additional direct source: Farb–Margalit, *A primer on mapping class groups*, Version 5.0, <https://pagine.dm.unipi.it/~a019210/Farb%20Magalit_Primer%20on%20Teichmuller%20theory.pdf>. The punctured Dehn–Nielsen–Baer theorem is Theorem 8.8, printed pp. 245–246 (PDF pp. 254–255); Birman is Theorem 4.6, printed p. 102, proof pp. 104–105 (PDF pp. 111, 113–114). Parent tool references: `turn546view1`, `turn547view0`, `turn547view2–3`. These are draft-version page numbers, not asserted to be the published book's pagination. The integrated proof cites Cantwell–Conlon for the exact ordinary cancellation input and proves the needed full profinite Birman step directly.

### Hurwitz branch cover

Romagny, M., & Wewers, S. (2006). Hurwitz spaces. *Séminaires et Congrès, 13*, 313–341. <https://imag.umontpellier.fr/~romagny/articles/hurwitz_spaces.pdf>.

Opened the complete 29-page author PDF, particularly Section 1.1, printed pp. 313–314 (PDF pp. 1–2). It supplies the finite unramified classical branch cover, connectedness, and the unmarked source-surjectivity statement. Tool references: `turn560view1`, earlier `turn536view0`. E.13 does not misattribute its stronger marked connected-fibre theorem to this source; that theorem is proved by the explicit vector-bundle and jet argument. The existing E.8 stack comparison uses the already opened Bertin–Romagny source, Proposition 6.14 and Theorem 6.20.

## Arithmetic-image scope

The complete genus-zero system is the restriction target. A GT-based arithmetic test must either supply the exact comparison for this structured system or explicitly require equality with the standard GT tower action of an element of the chosen subgroup. If such an element is already known to be arithmetic, its arithmetic all-types lift exists; E.13 then proves uniqueness of the resulting outer system. Selecting the actual G_Q subgroup from Hoshi–Mochizuki–Tsujimura's conjugacy class is a separate group-theoretic/source question being handled by the parent. Nothing in E.13 silently proves `GT=G_Q` or a lifting theorem for arbitrary GT conjugators.

## Independent reviews and corrections

The first actual-Hurwitz-transport argument did not explicitly control arbitrary completed F-image squares. It has been replaced by the discrete ordinary-pi1 restricted-cancellation proof followed by E.6 closure. Topos independently checked both that proof and a longer boundary-profile proof, and recorded a final pass after the revision. Jet terminology was made precise as length `2n+4`; a misleading `two-jets` phrase was removed. Genus-zero centrelessness is proved for every colour partition, rather than inferred from a possibly nontrivial centre of a small permutation factor. These corrections are incorporated in the integrated proof.
