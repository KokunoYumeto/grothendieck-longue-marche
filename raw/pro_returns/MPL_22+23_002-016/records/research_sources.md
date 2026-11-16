## Comparison-source checks and limits

### S01. Supplied context and original-print checks

**Kind: reading question / source control. Locations: A27, A29; O05, O07–O10; E01–E02.** The supplied `ega_fr` files are a textual comparison edition, with English prose in most chapter-0 files despite the README's description of a French edition. The notes identify their filenames and numbered passages, and the original-print checks below cover specific discrepancies rather than certify every line of that edition. The original EGA IV-1 leaves at printed pp. 131, 147–148 and 204 were retrieved and visually inspected after freeze; A27 and A29 record their results.

### S02. The proof text at EGA 0.20.7.2–3

**Kind: reading question in the supplied context. Location: 22/024's coefficient-differential map; context `EGA_chap0_ega0-20.tex`, 0.20.7.2–3.** The printed p. 147 gives the precomposition map \(h\mapsto h\circ v\) from \(\operatorname{Hom}_{C,\mathrm{cont}}(\Omega_{C/A},L)\) to \(\operatorname{Hom}_{C,\mathrm{cont}}(\Omega_{B/A}\otimes_BC,L)\), agreeing with restriction of derivations, whereas the supplied context reverses that display. The printed topology comparison says “moins fines”; the supplied English text says “finer,” so the identity from the induced module topology to the stated differential topology is the comparison to retain. At 0.20.7.3 the original p. 148 uses induced topologies and cites 20.7.2 and 19.1.7, while the supplied context inserts a substantially different paragraph asserting surjectivity, injectivity and density. These verified textual differences are recorded for the comparison edition only, with primary reference [B6] and no change to the frozen page files.

### S03. Scope of the literature comparison

**Kind: reading question / research limit. Locations: 22/003, 015, 024, 027–029; 23/007, 013.** The original Lang 1952 argument, the full MacLane 1940 paper, the continuation and attribution of the English integrability typescript, and the other archive cotes named in the README were not supplied or independently reconstructed here. The Hua statuses describe that register's claims, including its own search and Lean-card reports; the concrete verifications in A20–A28 do not establish priority or the state of all subsequent literature. The source-by-source checks below and the logged searches delimit the evidence actually used.

## Checked primary references

All online checks below were made on **16 November 2026 UTC**, after the transcription freeze. The supplied chapter-0 files and plan witnesses are cited at their use sites; they remain part of the user's context and are not duplicated in this ZIP.

| Reference | Bibliographic identification and checked passage | Used in |
|---|---|---|
| **B1** | Busé, L., & Jouanolou, J.-P. (2012). *A computational approach to the discriminant of homogeneous polynomials*. arXiv:1210.4697v1. [Version record](https://arxiv.org/abs/1210.4697v1); [full text](https://arxiv.org/html/1210.4697v1), Definition 4.6 and Proposition 4.7(i). The cited numbering is that of this preprint version. | E04–E05: resultant normalization and coefficient-scaling degree. |
| **B2** | The Stacks Project Authors. *The Stacks Project*, [Tag 047N](https://stacks.math.columbia.edu/tag/047N), Lemma 39.8.2; terminology checked in [Section 39.8, Tag 0BF6](https://stacks.math.columbia.edu/tag/0BF6). | E16: the locally finite type scope of the characteristic-zero group-scheme smoothness comparison. |
| **B3** | Cartier, P. (1956). *Hyperalgèbres et groupes formels*. Séminaire « Sophus Lie », vol. 2 (1955–1956), exposé 2, dated 27 January 1956, pp. 2-01–2-06. [Numdam record](https://www.numdam.org/item/SSL_1955-1956__2__A4_0/). The original printed pp. 2-01–2-02 were inspected visually, especially Definition 1, axiom HA3, and Lemma 2. | E14, E23: the filtration axiom used to assess the literal marginal checklist. |
| **B4** | The Stacks Project Authors. *The Stacks Project*, [Tag 0593](https://stacks.math.columbia.edu/tag/0593), Theorem 10.85.4. | A22, A24 and the detailed review: freeness of projective modules over a local ring. |
| **B5** | The Stacks Project Authors. *The Stacks Project*, [Section 10.138, Tag 00TH](https://stacks.math.columbia.edu/tag/00TH), especially Lemma 10.138.7 and Proposition 10.138.8(6). | A20–A24 and the detailed review: split conormal presentation and the projective-differential requirement for formal smoothness. |
| **B6** | Grothendieck, A., with J. Dieudonné. (1964). *Éléments de géométrie algébrique, IV: Étude locale des schémas et des morphismes de schémas, Première partie*. Publications Mathématiques de l'IHÉS, 20, 5–259. [Numdam record](https://www.numdam.org/item/PMIHES_1964__20__5_0/), DOI 10.1007/BF02684747. Printed pp. 131, 147–148 and 204 were inspected visually. | A27, A29, S02: literal generator list, differential-arrow labels and the proof-text comparison. |
