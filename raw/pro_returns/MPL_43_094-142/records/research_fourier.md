# Research review: cote 47, cote 44, and the Oda comparison

Research-only review after the 46-page transcription was frozen. No manuscript image was read by this reviewer and no transcription file was edited. The entire frozen transcription was read; the contextual transcription of cotes 47, 54, and 44 was read in full. The context README and RESULTS_STATE register were read before this report.

## Source and status key

- **T43** = `MPL_43_094-142_transcription.tex`; individual-page line numbers below refer to `pages/MPL_43_094-142_43_scanNNN.tex`.
- **CT** = supplied `MPL_16+47+54+44_transcription.tex`, with cote and scan specified; this remains a first-pass contextual transcription, not a newly audited reading.
- **CN** = supplied `MPL_16+47+54+44_notes.md`; its F7–F8 and D01–D14 items are earlier-run claims or proposals, not independently reviewed results.
- **RS** = supplied `notes/RESULTS_STATE.md`; the planning entries **WG2 §1.1 #3**, **WG2 §2.3 #12**, and **WG H9** remain questions/hunches with the register's stated unchecked status.
- **Oda** = the supplied `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`: Tadao Oda, *The first de Rham cohomology group and Dieudonné modules*, Annales scientifiques de l'École Normale Supérieure, 4e série, 2 (1969), 63–135, DOI `10.24033/asens.1175`. Relevant statements were read in its existing text layer and visually checked on printed pp. 67, 69–70, 76–77, 89, 119, and 131 (PDF pp. 6, 8–9, 15–16, 28, 58, and 70); the PDF skill was used for this printed witness.
- **Search records** = `research_fourier_searches.jsonl`, one record per F01–F23, with literal search patterns, source files, line/scan locators, and hit counts. Long result lists are explicitly marked as truncated.

This report identifies documentary evidence and explicit comparison maps; it makes no changes to register statuses. A source's assertion and a proof of the asserted comparison are reported separately. In particular, none of the finite-group or cohomological calculations below is announced as resolving the open arithmetic rows of RS.

## Requested questions

| Question | Finding within the supplied range | Items |
|---|---|---|
| A second cote 47 witness, with the compatibility check completed? | No second occurrence of its Poincaré-kernel transform or of the specific zero-section comparison proof was identified in T43/94–142. The trace/Ext construction on T43/130–133 supplies a concrete related comparison to study. | F01–F03 |
| Earlier forms of cote 44 Theorems 1–7? | T43/133 explicitly invokes Jacobian self-duality and gives curve cohomology/torsion formulas, providing a comparison at the curve endpoint of the programme. The seven statements in their stated ranges, and any chronology between the mathematical leaves, are not established by this packet. | F04–F11 |
| Does the Oda witness add a checked bridge? | Yes: its printed statements supply the isogeny-kernel Cartier pairing, the Dieudonné duality isomorphism, the filtered de Rham comparison, and actual functoriality/biduality diagrams. Identifying those maps with the particular rough margins of T43/133 remains an explicit comparison task. | F12–F22 |

## Notes

### F01 — The requested second Fourier witness

**File/scan:** cote 43, scans 94–142, especially 130 and 132–133. **Kind:** reading question. **Context:** CT, cote 47, scans 3–8; CN F7–F8; README, carry-question for cote 47. **Register:** bears on **WG2 §1.1 #3** (unchecked planning item).

T43/130 constructs a map out of \(E_f(G,S\sigma)\), while CT/47/3 explicitly defines \(\Phi_{\mathcal L}(F)=R\operatorname{pr}_{2*}(L\operatorname{pr}_1^*F\otimes\mathcal L)\) and CT/47/7–8 constructs \(\theta:Rp_*W\to e_*(\det t_{B^\vee})[-n]\), ending “à faire une vérification de compatibilité.....”. Reading the whole frozen range and searching the contextual vocabulary found no second occurrence in T43 of that transform together with a calculation of \(Li_{e(s)}^*\theta\). This is a scope-limited answer about these 46 supplied pages; the unprovided earlier scans of cote 43 remain outside the finding.

### F02 — Two explicit comparison-map constructions

**File/scan:** cote 43, scan 130, fragment lines 15–39; scan 132, final displays. **Kind:** unproved claim. **Context:** CT, cote 47, scans 6–8; CN F6–F8. **Register:** bears on **WG2 §1.1 #3**; no settled RS row specifically proves the map on scan 130.

The words “en composant, on trouve l'hom voulu” accompany \(E_f(G,S\sigma)\to E_f(Rf_*G,Rf_*S\sigma)\to E_f(Rf_*G,\sigma)\), whose second arrow uses the proposed \(\gamma\in\operatorname{Hom}^0(Rf_*S\sigma,\sigma)\). CT/47/7 instead specifies its comparison through \(R^nq_*\mathcal O_B\simeq\bigwedge^n t_{B^\vee}\), choosing “l'hom identique”, so both records make the chosen morphism—not only its source and target—part of the proof. T43 adds an explicit finite-coefficient trace/Ext programme to this comparison, but its “préciser” and changing finiteness clauses leave the asserted isomorphism's exact range to be checked.

### F03 — Preserve the exact unfinished Fourier test

**File/scan:** cote 43, scans 130–133, compared with cote 47, scans 7–8. **Kind:** own idea. **Context:** CT/47/7–8; CN F7–F8. **Register:** bears on **WG2 §1.1 #3**.

For a future comparison of the two constructions, retain the actual arrow \(\theta\), its determinant line and shift, and evaluate \(Li_{e(s)}^*\theta\) in every cohomological degree. CN F7–F8 already propose the perfect-cone test and a Koszul cohomology computation; those are prior-run leads, and this packet supplies no replacement calculation of the specific arrow at the unit. **Confidence: high** as a verification task, because CT/47/8 expressly places the unfinished work at that fiber and T43/130 expressly builds its own comparison by composition.

### F04 — The chronology required by “earlier forms”

**File/scan:** cote 43, scans 118, 131, 134, and 133. **Kind:** reading question. **Context:** CT, cote 44, scans 2, 4, 6, and dated letter at scan 8. **Register:** bears on **WG2 §1.1 #3** and **WG2 §2.3 #12** (both unchecked).

The cancelled administrative list on T43/118 contains “James September 1963” and “Bott September 1963 ?”, whereas CT/44/8 explicitly dates its letter “Bures le 12.8.1964”. The dates on the cancelled list do not date the separate mathematical text of T43/133, and the title leaves 131 and 134 supply no date. The packet therefore supports comparisons of statements and methods without establishing that any matched assertion precedes the cote 44 programme.

### F05 — Cote 44 Theorem 1: the kernel of the cycle map

**File/scan:** cote 43, scans 132–133. **Kind:** reading question. **Context:** CT, cote 44, scan 2, Theorem 1; scan 9, \(A\to A^\vee\) and \(J=A/N\); CN D08. **Register:** bears on **WG2 §2.3 #12** and **WG2 §1.1 #3**.

CT/44/2 identifies \(N(\xi)\subset\operatorname{Alb}(S)\) with the kernel of the natural map \(\varphi_\xi:\operatorname{Alb}(S)\to Z^i(X)/Z^i_{\mathrm{alb}}(X)\), qualified “en substance”. T43/132–133 instead gives the Kummer/Picard sequence and the curve expression \(H^1(C,\mathbb Q/\mathbb Z)\simeq\operatorname{Ext}^1(J^{0|\bullet},\mathbb Q/\mathbb Z)\), with “autodualité de la Jacobienne” in the margin. No occurrence of \(\varphi_\xi\), its family of cycles, or this kernel characterization was identified in the supplied T43 range; the Picard-to-cohomology maps just cited are the specific available comparison.

### F06 — Cote 44 Theorem 2: the dimension bound

**File/scan:** cote 43, scans 117 and 133. **Kind:** reading question. **Context:** CT, cote 44, scans 2 and 8; CN D09–D10. **Register:** bears on **WG2 §2.3 #12**.

CT/44/2 proposes the uniform bound \(\dim(\operatorname{Alb}(S)/N(\xi))\leq\frac12 b^{2i-1}(X)\), and CT/44/8 names a Tate-module subquotient of \(H^{2i-1}(X,\mathbb Z_\ell(i))\). T43/117 writes \(\mu(A)=2\alpha(A^0)+\mu(A^0)\), with abelian and multiplicative component labels, and T43/133 writes \(\operatorname{Hom}(T(J),\mathbb Q/\mathbb Z)\); these are the displayed component-count and cohomology expressions. The symbol \(T(J)\) remains undefined on scan 133 and is not identified here with a Tate module, particularly because scan 106 explicitly names a Greenberg–Néron–Grothendieck functor \(T\). The packet gives no map from the general cycle-family quotient in Theorem 2 to that odd cohomology, so its contribution is the explicit curve/local-group material rather than a proof of the uniform bound; CN's later codimension-two claim remains a cited lead here.

### F07 — Cote 44 Theorem 3: the curve self-duality endpoint

**File/scan:** cote 43, scan 133, fragment lines 7–23 and 38–43. **Kind:** unpursued implication. **Context:** CT, cote 44, scans 2 and 8; CT, cote 54, scans 5 and 7; CN D03, D05, D08. **Register:** bears on **WG2 §2.3 #12** and **WG2 §1.1 #3**.

T43/133 repeatedly invokes “autodualité de la Jacobienne” while writing its finite-torsion and \(H^1(C,-)\) comparisons; CT/44/8 records the endpoints \(J^1=\operatorname{Pic}^0\) and \(J^n=\operatorname{Alb}^0\) of the claimed complementary dualities. Thus the concrete common object is the ordinary curve Jacobian and its dual, with the finite-level comparison made explicit in F12. The passage supplies that endpoint and its cohomological uses, but no construction here of \(Z^i_{\mathrm{alg}}(X)/Z^i_{\mathrm{alb}}(X)\) for every codimension.

### F08 — Cote 44 Theorem 4: self-duality and polarization

**File/scan:** cote 43, scan 133, right margin. **Kind:** unproved claim. **Context:** CT, cote 44, scan 2, Theorem 4, and scans 8–9; CN D13. **Register:** bears on **WG2 §2.3 #12** and **WG H9** (unchecked hunch).

The margin's “autodual. d'ordre infinitésimal de la Jacobienne” is used to explain a pairing of Frobenius kernel/cokernel data. CT/44/8–9 specifies the separate construction \(D=r_*(p^*z\cdot q^*z)\), its descent along \(A\to A/N\), and the request “A prouver que cette dernière est positive !”. To connect the written finite-level pairing to that programme, the verification must identify the descended divisor correspondence and its ampleness; neither that divisor nor an ampleness argument appears in T43/133.

### F09 — Cote 44 Theorem 5: the Néron–Tate/intersection formula

**File/scan:** cote 43, scans 107, 117, and 142. **Kind:** reading question. **Context:** CT, cote 44, scan 4, Theorem 5 and its fibration margin; CN D12. **Register:** bears on **WG H9** and **WG2 §2.3 #12**.

T43/107 boxes \(H^i(A)\times H^{2-i}(B)\mathrel{-}H^2(K,G_m)\), T43/117 compares \(H^1(K,A)\) with Ext of the dual-group data, and T43/142 is the title “Dualité de Tate-Cassels”. CT/44/4 takes a smooth projective \(X\) of dimension \(n\), cycles \(Z,Z'\) of codimensions \(i,j\) with \(i+j=n\), and algebraically trivial restrictions \(\zeta,\zeta'\) to the generic member \(Y\) of a pencil with geometrically integral fibres, then writes \(\langle\zeta,\zeta'\rangle=(-1)^mZ\cdot Z'\). That written \(m\) remains beside the cancelled \(\dim Y=2m-1\) and the surviving margin \(2i=2j=n\), so its source convention remains part of the sign comparison. No calculation transporting the displayed local cohomology pairing through that pencil to the intersection number was found in this range, so the packet adds candidate local duality inputs without establishing the height formula or its sign.

### F10 — Cote 44 Theorem 6: restriction to a hyperplane section

**File/scan:** cote 43, scan 118, cancelled outline item 12, and scan 133. **Kind:** reading question. **Context:** CT, cote 44, scan 4, Theorem 6; CN 44:4:4–44:4:6. **Register:** bears on **WG2 §2.3 #12** and **WG H9**.

T43/118 lists “Sections hyperplanes, multisections” in a cancelled chapter plan. Under Theorem 5's hypotheses, CT/44/4 writes \(P^i(X)\to P^i(Y)\) as an isomorphism for \(2i\leq n-1\), records its surjectivity for \(2i\geq n+1\) in brackets, and identifies its image with the fixed part for \(2i=n\). The available T43 text supplies neither that restriction map nor a fixed-part calculation, and the isolated outline entry gives no earlier formulation of those three assertions.

### F11 — Cote 44 Theorem 7: numerical and \(\tau\)-equivalence

**File/scan:** cote 43, scans 132–133. **Kind:** reading question. **Context:** CT, cote 44, scan 6, Theorem 7; CN D14. **Register:** bears on **WG2 §2.3 #12**.

CT/44/6 writes “L'équivalence numérique = \(\tau\)-équivalence”, with a “Matsusaka” margin, while T43/132 defines the locally uncertain \(\sigma|\tau\) as a finite coefficient group, with “étale” itself marked uncertain, and forms \(S\sigma=(D\Delta\sigma)(2)\), leaving the meaning of the parenthesized \((2)\) open. This explicit local definition governs the coefficient in the Ext formulas; no definition of cycle \(\tau\)-equivalence or equality of the two cycle relations occurs in the supplied range. CN D14 contains a later interpretation and counterexample discussion, whose claims were not independently audited in this comparison and supply no license to read the coefficient letter as that cycle relation.

### F12 — The finite-level morphism behind Jacobian self-duality

**File/scan:** cote 43, scan 133, fragment lines 7–23. **Kind:** unpursued implication. **Context:** CT, cote 54, scans 5 and 7; CN D03; Oda, Theorem 1.1 and Corollary 1.3(ii), printed pp. 67–70. **Register:** bears on **WG2 §1.1 #3** and **WG2 §2.3 #12**; no matching reviewed Oda-comparison row is listed in RS.

Write \(\lambda_J:J\to J^\vee\) for the Jacobian self-duality invoked by the margin “autodualité”; the finite-level map to check is \(J[p]\xrightarrow{\lambda_J[p]}J^\vee[p]\xrightarrow{\nu_{[p]}}D(J[p])\). For an isogeny \(\lambda\) of abelian schemes over a prescheme \(S\), with the dual abelian schemes defined, Oda's \(\nu_\lambda:\ker(\lambda^t)\xrightarrow{\sim}D_S(\ker\lambda)\) is constructed by translating a trivialization of the pullback of a line bundle, and its functoriality square is printed and proved. This supplies a precise primary-source comparison for the \({}_pJ\), Frobenius and \(\alpha_p\) entries, while identifying the manuscript's particular pairing with that composite remains to be done.

### F13 — Frobenius, Verschiebung, and the annihilator map

**File/scan:** cote 43, scan 133, margin mentioning \(V,F\mid p\) (the frozen alternatives). **Kind:** unpursued implication. **Context:** CT, cote 54, scans 5 and 7; CN D03; Oda, Theorem 1.1 and Corollary 1.3(ii), printed pp. 67–70. **Register:** bears on **WG2 §1.1 #3**; no specific RS result establishes this manuscript identification.

CT/54/7 draws the Frobenius and Verschiebung maps for \(A\) and \(B\), with its upper terminal object still \(V\mid A\)-uncertain, following the statement that the Frobenius kernels are orthogonal. For abelian schemes \(A\) and \(B=A^\vee\) over a characteristic-\(p\) base, with \(\iota:\ker F_A\hookrightarrow A[p]\), Oda's isomorphism \(\nu_{F_A}:\ker(V_B:B^{(p)}\to B)\to D(\ker F_A)\) satisfies the functoriality identity \(D(\iota)\circ\nu_{[p]}=\nu_{F_A}\circ(F_B|_{B[p]})\). This composite has kernel \(\ker F_B\) by \([p]=V_BF_B\), providing the explicit annihilator comparison while retaining the Frobenius twists and the frozen \(V,F|p\) reading.

### F14 — Cartier duality carried through the Dieudonné functor

**File/scan:** cote 43, scan 133, infinitesimal-duality margin. **Kind:** unpursued implication. **Context:** CT/54/5,7; CN D03–D05; Oda, Definition 3.5 and Theorem 3.19, printed pp. 82 and 89. **Register:** bears on **WG2 §1.1 #3**; the RS excerpt contains no reviewed statement of this comparison.

For finite commutative group schemes \(G\) of \(p\)-primary rank over a perfect field \(k\) of characteristic \(p\), Oda's contravariant functor \(M\) comes with \(d(G):M(DG)\xrightarrow{\sim}D(MG)\), where \(D(M)=\operatorname{Hom}_{W(k)}(M,\operatorname{Frac}(W(k))/W(k))\), \((Fa)(x)=\sigma(a(Vx))\), and \((Va)(x)=\sigma^{-1}(a(Fx))\), with \(\sigma\) induced by Witt-vector Frobenius. The theorem includes the biduality square \(M(G)\leftarrow MDD(G)\to DMD(G)\leftarrow DDM(G)\), with canonical identifications specified. This adds the exact realization morphism to T43's phrase “dualité des algèbres de Lie correspondantes”; the equality of the manuscript's pairing with the transported pairing is a further verification, not an alteration of the source.

### F15 — The filtered de Rham statement actually available in Oda

**File/scan:** cote 43, scan 133, Frobenius and Lie-algebra margin. **Kind:** unpursued implication. **Context:** CT, cote 54, scans 3, 5, 7; CN D05; Oda, Corollary 5.11, printed p. 131. **Register:** bears on **WG2 §1.1 #3**; no specific settled RS row replaces this primary comparison.

For Oda's stated setting, an abelian scheme \(J\) over a perfect field of characteristic \(p\), the printed map is \(\psi:M(J[p])\xrightarrow{\sim}H^1_{\mathrm{dR}}(J)\), and it sends \(VM(J[p])=\ker F\) onto \(H^0(J,\Omega^1_{J/k})\). The displayed exact sequence is carried to \(0\to H^0(J,\Omega^1)\to H^1_{\mathrm{dR}}(J)\to H^1(J,\mathcal O_J)\to0\), which directly addresses the extension question “peut-elle se déduire de la connaissance de \(p^A\) ??” in CT/54/7. T43/133 adds curve-level Frobenius kernel/cokernel data to compare with this filtration; the identification of its particular restricted-Lie pairing still requires the maps of F12–F14.

### F16 — Direct comparison with curve cohomology

**File/scan:** cote 43, scan 128, curve setup; scan 133, \(H^1(C,\mathcal O_C)\) entries. **Kind:** unpursued implication. **Context:** CT/54/3,5,7; CN D05; Oda, Corollaries 5.2 and 5.12, printed pp. 119 and 131. **Register:** bears on **WG2 §1.1 #3** and the curve endpoint of **WG2 §2.3 #12**.

After reducing to an algebraically closed field, Oda's proof of Corollary 5.2 uses \(i:C\to J\) and the pullback isomorphism \(i^*:H^1(J,\mathcal O_J)\to H^1(C,\mathcal O_C)\) in its commutative square with \(d:H^1(\mathcal O)\to H^1(\Omega^1)\). Corollary 5.12 supplies, for a smooth proper scheme \(C\) with \(C(k)\ne\varnothing\) over a perfect field of characteristic \(p\), the canonical injection \(\xi:D M({}_p\operatorname{Pic}_{C/k})\to H^1_{\mathrm{dR}}(C)\), with image \(\bigcap_n\ker(d\circ V^n)\). These are explicit comparison maps for the curve cohomology written on T43/133; applying the latter statement retains its rational-point and perfect-field conditions rather than silently adding them to T43/128.

### F17 — Specify which semilinear operator is being paired

**File/scan:** cote 43, scan 133, fragment lines 10–23. **Kind:** own idea. **Context:** CT/54/7; CN D04–D05; Oda, Definitions 3.1, 3.5, 5.5, 5.8 and Corollary 5.11, printed pp. 80–82, 121–124, 131. **Register:** bears on **WG2 §1.1 #3**.

A reproducible verification of “Dualité … de \(H^1(C,\mathcal O_C)_F\) et \({}_FH^1(C,\mathcal O_C)\)” should write the induced maps through \(i^*\), \(\psi\), and \(d(J[p])\), retaining \(F\)'s \(\sigma\)-linearity and \(V\)'s \(\sigma^{-1}\)-linearity. Oda defines the dual operators through \(F\leftrightarrow V\) and defines the de Rham action of \(V\) via the Cartier operator (Definition 5.8), while the page uses a single \(F\) on both a kernel and a cokernel, so the missing calculation is precisely the transpose identification under those comparison maps. **Confidence: high** as a proof-checking task, because the source itself invokes Lie duality and Oda states the required operator formulas.

### F18 — The largest \(\alpha_p\) subgroup and quotient

**File/scan:** cote 43, scan 133, fragment line 23. **Kind:** unproved claim. **Context:** CT, cote 54, scans 5 and 7; CN D04; Oda, Theorem 3.14, Corollary 3.16, and Theorem 3.19, printed pp. 87–89. **Register:** bears on **WG2 §1.1 #3**; no matching settled RS assertion is listed.

The difficult margin claims duality between the largest subgroup of \(A\) or \({}_pA\) of the form \(\alpha_p^n\) and the largest quotient of \({}_pA\) with the same property, attributing it to the corresponding Lie algebras. Over a perfect field of characteristic \(p\), Oda's anti-equivalence \(M\) for finite commutative group schemes of \(p\)-primary rank, together with \(d(G):M(DG)\to D(MG)\), supplies a concrete way to track the subgroup inclusion and quotient map with their reversed arrows. The manuscript's maximality assertions, the \(A\) versus \({}_pA\) scope, and the exact restriction of its self-duality still need to be checked; the low-confidence wording in the frozen margin remains material.

### F19 — The three characteristic-\(p\) rows need separate map checks

**File/scan:** cote 43, scan 133, fragment lines 9–22. **Kind:** own idea. **Context:** CT/54/5,7; CN D03–D05; Oda, §5 and Corollary 5.2, printed pp. 117–124. **Register:** bears on **WG2 §1.1 #3**, and provides comparison data for the open **FLAGGED_149 B9** without settling it.

Build a page-local check of the \(\mu_p\), \(\mathbb Z/p\mathbb Z\), and \(\alpha_p\) rows using exactly the multiplication-by-\(p\), \(1-F\), and \(F\) maps indicated by the table and its “complexe adélique … Frobenius” annotation. The comparison should keep the end groups, the fixed subgroup, and the cokernel zero in their written positions, then identify the map induced on \(H^1(C,\mathcal O_C)\) through Oda's curve/Jacobian pullback square. **Confidence: medium** as a research task, because the operators are explicit but the exponents and some margin words remain uncertain; no prime-to-\(p\) point-section conclusion is derived here.

### F20 — A common finite-level pairing for all the torsion rows

**File/scan:** cote 43, scan 132, Kummer sequence; scan 133, first table row and characteristic-\(p\) rows. **Kind:** unpursued implication. **Context:** CT/54/5,7; CN D03; Oda, Theorem 1.1 and Corollary 1.3(ii), printed pp. 67–70. **Register:** bears on **WG2 §1.1 #3**; the range issue also bears on open **FLAGGED_149 B9**.

The first row writes \((n,p)=1\), and the following rows explicitly treat \(\mu_p\) and \(\alpha_p\). For a positive integer \(n\) and the multiplication isogeny \([n]:J\to J\), Oda gives \(\nu_{[n]}:J^\vee[n]\to D(J[n])\), so \(\lambda_J[n]\) supplies one specified route from the invoked Jacobian self-duality to all the finite-level pairings. Passing that route through each cohomology construction remains to be checked, with the prime restrictions and the group-scheme coefficients retained as written.

### F21 — Oda does contain a completed compatibility, with its map named

**File/scan:** cote 43, scan 133, self-duality margins; cote 47, scan 8, comparison question. **Kind:** unpursued implication. **Context:** CT/47/7–8, CT/54/5,7; CN F7 and D03; Oda, Proposition 1.8 and Definition 1.9, printed pp. 74–75; Definitions 1.13–1.14 and Proposition 1.15, printed pp. 76–78. **Register:** bears on **WG2 §1.1 #3**.

For an invertible sheaf \(L\) on an abelian scheme \(J/S\) with \(J^\vee\) defined, Oda proves \(\rho(L)=\nu_J\circ\Lambda(L)(p)=e(L)\), where \(\nu_J:J^\vee(p)\to J(p)^t\) is the isomorphism to the Serre dual formed from the compatible finite Cartier pairings, and \(e(L)\) is defined by the compatible commutator pairings attached to \(L^{\otimes p^n}\). This is a completed primary-source compatibility for an explicitly named pairing, useful for T43/133's finite self-duality. The outstanding cote 47 arrow is instead the specified \(\theta:Rp_*W\to e_*(\det t_{B^\vee})[-n]\) at its unit fiber, and no transport of Oda's equality to that arrow is supplied in the current packet.

### F22 — The sign in Cartier biduality is part of the comparison

**File/scan:** cote 43, scan 133, “autodualité” margins. **Kind:** own idea. **Context:** CT/54/5,7 and CT/44/8–9; CN D03, D13; Oda, Corollary 1.3(ii), printed p. 70, and Proposition 1.12, printed p. 76. **Register:** bears on **WG2 §2.3 #12** and **WG H9**, without upgrading either.

Retain Oda's printed biduality square \(\nu_{\lambda^t}\circ k_X=-D(\nu_\lambda)\circ\mathrm{can}\) when comparing the self-duality on the finite Jacobian subgroup with a correspondence \(J\to J^\vee\). This is a concrete sign datum, and Oda's Proposition 1.12 carries a symmetric correspondence to a skew-symmetric homomorphism of \(p\)-divisible groups. **Confidence: high** as a comparison check, because the minus sign is present in the primary printed square; matching that sign supplies no ampleness proof for the divisor correspondence of CT/44/9.

### F23 — The reused \(J\)-notation and its actual maps

**File/scan:** cote 43, reused typescript scans 101 and 103. **Kind:** reading question. **Context:** CT, cote 44, scans 2 and 8; CT, cote 47, scans 3–5; RS returned-package provenance leads. **Register:** bears on **MPL_136_095-141 1.5**, **MPL_136_189-234 R008**, and **MPL_136_235-281 N16** as first-pass provenance cautions, plus **WG2 §1.1 #3**.

T43/103 specifies that \(J(\xi)\in J(P_k)\) has finite order \(q_k\), and T43/101 compares \(Df:X^{\gamma+\delta}\to X^\gamma\wedge X^\delta\) with the map induced by the diagonal \(X\to X\times X\), saying “It would seem reasonable to suppose” they have the same stable homotopy type. The contextual \(J^i(X)\) is introduced through cycle classes and the maps \(\operatorname{Alb}(S)\to Z^i(X)/Z^i_{\mathrm{alb}}(X)\), while the contextual Fourier functor is specified by its line-bundle kernel. A concordance must record these actual constructions and sheet provenance; no morphism identifying the displayed \(J(P_k)\) with that cycle quotient is given on the supplied reused pages.

## Verification limits

The prior-run context transcriptions were searched and read as supplied; their original manuscript images were not available for this review and their doubt marks were retained in all comparisons. Oda's cited statements and displayed maps were checked from the supplied printed witness, but this review does not claim a new complete proof of every theorem in that paper. The claim that no second Fourier witness or seven-theorem sequence was identified is restricted to the 46 frozen pages and the supplied context, and carries no assertion about unseen archive material or the existence of mathematical relations beyond the explicit comparisons recorded here.

## Final source audit

2026-11-16 23:19:30 UTC — The 23 note IDs match the 23 JSONL search records; all recorded `rg` calls completed with exit 0 or the legitimate no-match exit 1. Broad searches with truncated result lists were supplemented by the following fixed-string searches in CT; each was re-run with `rg -n -F`, and the locators below derive from the surrounding `cotefile` and `scanpage` markers. This table supplements the existing search log without changing it.

| Item | Fixed-string query | Verified CT locator(s) |
|---|---|---|
| F01 | `compatibilité.....` | cote 47, scan 8, line 2393 |
| F02 | `l'hom identique` | cote 47, scan 7, line 2377 |
| F03 | `mapping-cylindres` | cote 47, scan 8, line 2388 |
| F04 | `Bures le 12.8.1964` | cote 44, scan 8, line 2970 |
| F05 | `noyau de l'application naturelle` | cote 44, scan 2, line 2787 |
| F06 | `majorée par un nb` | cote 44, scan 2, line 2793 |
| F07 | `en dualité canonique` | cote 44, scan 2, line 2799 |
| F08 | `A prouver que cette dernière` | cote 44, scan 9, line 2995 |
| F09 | `\langle\zeta,\zeta` | cote 44, scan 4, line 2862; cote 44, scan 4, line 2864 |
| F10 | `facteur fixe` | cote 44, scan 4, line 2879 |
| F11 | `L'équivalence numérique` | cote 44, scan 6, line 2944 |
| F12 | `dualité de Cartier` | cote 54, scan 5, line 2696 |
| F13 | `B^{(p)}` | cote 54, scan 7, line 2719 |
| F14 | `de la connaissance` | cote 54, scan 7, line 2730 |
| F15 | `Cette extension peut-elle` | cote 54, scan 7, line 2730 |
| F16 | `t_B=H^1(A` | cote 54, scan 3, line 2617 |
| F17 | `p$-alg. de Lie` | cote 54, scan 7, line 2727 |
| F18 | `extension de groupes radiciels` | cote 54, scan 7, line 2730 |
| F19 | `p^A` | cote 54, scan 5, line 2696; cote 54, scan 5, line 2698; cote 54, scan 7, line 2723; cote 54, scan 7, line 2730 |
| F20 | `p^B` | cote 54, scan 5, line 2696; cote 54, scan 5, line 2699 |
| F21 | `compatibilité.....` | cote 47, scan 8, line 2393 |
| F22 | `correspondance symétrique` | cote 44, scan 9, line 2995 |
| F23 | `jacobienne intermédiaire` | cote 44, scan 8, line 2974 |

Oda source-location check: Definition 3.1 is on p. 80; Definition 3.5 on p. 82; Definition 3.12 on p. 85; Theorem 3.14 on p. 87; Corollary 3.16 on p. 88; Theorem 3.19 on p. 89; Corollary 5.2 on p. 119; Definition 5.5 on p. 121; Definition 5.8 on p. 124; Corollaries 5.11–5.12 on p. 131. The proof of Proposition 1.15 continues from p. 77 to p. 78; F21 now cites pp. 76–78. No chronological priority of the independent mathematical leaves is inferred.

Numbering and hypotheses recheck: Theorem 1.1 states the Cartier-pairing functoriality on p. 67 and proves it through p. 69; Corollary 1.3(ii), p. 70, explicitly restates the kernel isomorphism and its functoriality square before giving the signed biduality square. F12, F13, and F20 now cite both statements. F16 retains the smoothness, properness, perfect-field characteristic-\(p\), and \(C(k)\ne\varnothing\) assumptions of Corollary 5.12; F14 defines \(\sigma\) as Witt-vector Frobenius, and F17 records that the de Rham \(V\)-action is via the Cartier operator.

Main-assembly audit: the retained main items F01 and F03–F22 matched this record before the additional tightening above. F09 now gives the stated cycle/pencil hypotheses, F10 the written numerical ranges, F13 the exact identity with the Cartier-dual restriction map, F16 the algebraically closed reduction used in Corollary 5.2, and F21 the actual p-divisible composite and its source locators; the main Oda bibliography should consequently include Proposition 1.8, Definition 1.9, and Corollary 3.16 as well as the previously listed statements. The main Fourier and chronology overview answers remain within the evidence of these notes.

Additional context checks for the expanded theorem hypotheses and ranges (exact `rg -n -F` queries):

| Item | Query | Hit |
|---|---|---|
| F09 | `de codim $i,j$` | CT, cote 44, scan 4, line(s) 2852 |
| F09 | `fibres sont géom. intègres` | CT, cote 44, scan 4, line(s) 2859 |
| F10 | `Si $2i\leq n-1$` | CT, cote 44, scan 4, line(s) 2878 |
| F10 | `$2i\geq n+1$` | CT, cote 44, scan 4, line(s) 2884 |
