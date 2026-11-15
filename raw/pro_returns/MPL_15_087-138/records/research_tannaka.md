# Research branch: real fibre functors, gerbes, exact sequences, and S15

Prepared after the transcription freeze, 15 November 2026. This branch read the frozen LaTeX and the supplied context, not the scans, and made no change to the transcription. Locations use frozen page-file lines. Earlier context returns and register entries retain their supplied, mostly unreviewed status.

## Context search record

Searches covered context/MPL_16+47+54+44_transcription.tex, its notes file, and context/notes/RESULTS_STATE.md after reading the README and the complete register. The terms gerbe, foncteur fibre, Giraud, Nori, and Ayoub find no corresponding construction in the earlier transcript; the closest category passage is cote 16, scan 049, “the category of motives which is semi-simple !”. Polarization searches lead to cote 44/002, Theorem 4, and 44/008–009, and the Lefschetz discussion in 16/044–050. Period, Betti, transcendence, algebraic-independence, comparison, and de Rham searches locate no explicit period-conjecture assertion in the current batch: the earlier context has Bott periodicity on 16/035 and Betti comparison on 16/044, and includes Oda's de Rham/Dieudonné paper. The modern Nori/Ayoub leads are supplied as register excerpts rather than full research returns.

## Candidate notes

### T01 — The actual real-fibre criterion and its compatibility clause

**File/scan/lines:** cote 15, pages/MPL_15_087-138_15_scan117.tex, lines 2–33. **Kind:** unproved claim, with a proof sketch. **Quote:** “non modifié”; “forme alternée fondamentale”. **Context relation:** adds explicit criteria to context 16/049 and its notes 16:49:3–4; bears on **MPL_7_061-072+8_001-078 Scan 061 (§66)** and **Hua, findings register, 15-real-fibre-functor-criterion**.

The sheet asserts equivalence of a torus kernel, primitivity of the Tate character, and existence of the specified real fibre functor, together with the complementary square-character/\(\mu_2\)-kernel obstruction. Its outline uses compact-torus cohomology and even rank of odd-degree objects, so the phrase “situation motivique” includes structural input beyond the displayed character and cocharacter. The marginal compatibility with effective weight-zero motives and canonical conjugation on the displayed \(H^0_{\mathbb C}\) must accompany any restatement; the page also gives the even-degree subcategory as a corollary.

### T02 — Check on the abbreviated Hua entry

**File/scan/lines:** cote 15, scans 117–119; 117 lines 13–18, 33; 119 lines 2–16. **Kind:** reading question / unpursued implication. **Quote:** “non modifié”; “Dans le cas de la prop 2”. **Context relation:** directly checks **Hua, findings register, 15-real-fibre-functor-criterion**; closest earlier category witness: context 16/049.

The supplied Hua excerpt correctly points to the two propositions, the \(U^\circ\times\mu_2\) alternative, and the even-degree corollary, but its abbreviated statement omits the handwritten fibre-functor compatibility and the proof's alternating-form input. Its inclusive scan range also contains scan 118, a reused errata sheet, so the mathematical continuation is 117→119. This confirms a manuscript claim with these qualifications; it does not validate every implication of Hua's full finding, which was not supplied.

### T03 — A concrete test of the necessary structural input

**File/scan/lines:** cote 15, scan 117, lines 23–31. **Kind:** own idea. **Confidence:** high, from the explicit representation and character. **Context relation:** tests **Hua, findings register, 15-real-fibre-functor-criterion** and **MPL_7_061-072+8_001-078 Scan 061 (§66)**; no matching example found in context, whose nearest category passage is 16/049.

In \(\operatorname{Rep}_{\mathbb R}(\mathbb G_m)\), take \(\varepsilon(t)=t^2\) and \(j(t)=t\): then \(\varepsilon j(t)=t^2\), \(U=\mu_2\), and the ordinary forgetful functor is a real fibre functor. The character \(t\mapsto t\) gives a one-dimensional object of degree one, whose exterior square is zero, so it cannot carry the nondegenerate alternating form invoked on scan 117. This example identifies exactly why the displayed group data alone cannot replace the manuscript's additional motivic and polarizing structure.

### T04 — Direct check of compact-torus cohomology

**File/scan/lines:** cote 15, scan 117, line 31; scan 119, lines 6, 8. **Kind:** own idea. **Confidence:** high, by the displayed cyclic-group cohomology computation. **Quote:** “\(H^2(\mathbb R,T)=0\) !”. **Context relation:** verifies one proof ingredient of **Hua, findings register, 15-real-fibre-functor-criterion**; no corresponding calculation occurs in context, whose nearest motive-category witness is 16/049.

For \(S=\operatorname{Res}^1_{\mathbb C/\mathbb R}\mathbb G_m\), write \(S(\mathbb C)=\mathbb C^\times\) with \(\sigma(z)=1/\bar z\); its cyclic norm \(z\sigma(z)=z/\bar z\) has image \(S^1=S(\mathbb C)^\sigma\). Thus \(H^2(\mathbb R,S)=S^1/\{z/\bar z\}=0\), whereas \(H^1(\mathbb R,S)=\mathbb R^\times/\mathbb R_{>0}=\{\pm1\}\), and products give the compact-torus calculation used on the sheet. For \(S^d\times\mu_2\), the second cohomology reduces to \(H^2(\mathbb R,\mu_2)=\mu_2\); the particular motivic gerbe's identification with its nonzero class is the further assertion on scan 119.

### T05 — The square character and the displayed projection have different kernels

**File/scan/lines:** cote 15, scan 117, lines 23–25; scan 119, lines 2–5. **Kind:** reading question. **Quote:** “Dans le cas de la prop 2”; “\(\varepsilon=\operatorname{pr}_2\)”. **Context relation:** qualifies **Hua, findings register, 15-real-fibre-functor-criterion**; no matching formula found in context (nearest category witness: 16/049).

The frozen corollary gives \(G^\circ\simeq U^\circ\times\mathbb G_m\) and \(\varepsilon=\operatorname{pr}_2\), whose kernel is explicitly \(\{(u,1)\}\simeq U^\circ\), while Proposition 2 has kernel \(U^\circ\times\mu_2\). On that same product the character \((u,t)\mapsto t^2\) has kernel \(U^\circ\times\mu_2\), so the displayed projection and the preceding square-character assertion require reconciliation. This remains a research question; the frozen reading, including the uncertain injection index in \(j\), stays unchanged.

### T06 — The rank-two odd object is a further construction claim

**File/scan/lines:** cote 15, scan 119, line 6. **Kind:** unproved claim. **Quote:** “de degré 1, rang 2”; “\(\mathbb R\)-tordue”. **Context relation:** adds an object-level assertion to **Hua, findings register, 15-real-fibre-functor-criterion**; compare context 16/049 and note 16:49:4.

The sheet claims an odd object of rank two, with trivial \(U^\circ\)-action, already generating a twisted real subcategory. A model for its descent sign is \(J(z_1,z_2)=(-\bar z_2,\bar z_1)\), with \(J^2=-1\); more generally, \(J=A\circ\text{conjugation}\) and \(J^2=-I_r\) give \(|\det A|^2=(-1)^r\), forcing even \(r\). This checks the parity mechanism but leaves the promised object's construction inside the specified motivic category to be supplied.

### T07 — The torsor-to-polarization map

**File/scan/lines:** cote 15, scan 119, lines 8–16; scan 121, line 2. **Kind:** unproved claim. **Quote:** “donc bijective”; “se déterminent mutuellement”. **Context relation:** adds \(H^0(\mathscr G_{\mathbb R})\to\operatorname{Pol}(\mathscr G_{\mathbb R})\) to context 44/002 Th.4 and 44/008–009; bears on **WG2 §2.3 #12**, **MPL_14_002-044 A36**, and **Hua, findings register, 15-real-fibre-functor-criterion**.

The source identifies both sets as torsors under \({}_2U(\mathbb R)\), and its equivariance makes bijectivity formal: after choosing one source point, every point is its translate by a unique group element, and the image translates by that same element. The substantive obligations are the construction of a polarization from a fibre functor and the two torsor identifications, compatible with fixed Tate and weight-zero data. Deligne–Milne, *Tannakian Categories*, §4, especially Theorems 4.16–4.17, provides a later framework relating polarized real Tannakian categories, compact real forms, and descent data, for comparison with these particular gerbe reductions.

### T08 — Domains of the polarizing homomorphisms

**File/scan/lines:** cote 15, scan 119, lines 9–12; scan 121, lines 7–12; scan 123, lines 2–3. **Kind:** reading question. **Quote:** “\(i_1\bar i_1=j_{\mathbb R}\)”; “\(i|\mu_2\)”. **Context relation:** compare **MPL_14_002-044 M24a**, which reports \(i_1\bar i_1=j\) at 14/009; its full source was not supplied.

The frozen scan 119 starts \(i_1\) on \(\mu_{2\mathbb C}\), while the following equalities carry real subscripts and an unqualified \(j\); scan 121 starts \(i\) on \(\mathbb G_{m\mathbb C}\), and 123 explicitly restricts \(i\) to \(\mu_2\). The restriction map \(\operatorname{Hom}(\mathbb G_m,G_{\mathbb C})\to\operatorname{Hom}(\mu_2,G_{\mathbb C})\) gives the exact comparison: restricting \(\bar i i=j\) gives \(\overline{i|\mu_2}(i|\mu_2)=j|\mu_2\). This records the domain issue without supplying omitted restrictions in the transcription.

### T09 — Transitivity and preferred polarizations

**File/scan/lines:** cote 15, scan 121, line 4; scan 123, lines 3, 16. **Kind:** self-flagged. **Quote:** “À voir”; “opère-t-il transitivement”; “un paquet de polarisations préférentielles”. **Context relation:** adds an orbit-selection question to context 44/002 and 44/008–009 and **MPL_14_002-044 M24a**; bears on **WG2 §2.4 #3**.

The author asks about transitivity under three automorphism groups, successively retaining real, rational, and full group data. Scan 123 supplies privileged classes in the finite-field setting by restricting its distinguished cocharacters to \(\mu_2\), but leaves the ambiguity of those restrictions open. That construction gives a method for selecting a packet without a proof of all three transitivity assertions.

### T10 — The valuation construction has its own integrality warning

**File/scan/lines:** cote 15, scan 121, lines 6–30. **Kind:** self-flagged. **Quote:** “caveat”; “n'est pas tjrs ! à valeurs entières”. **Context relation:** adds a warning to **MPL_14_002-044 M24a** and **MPL_14_002-044 M01**; the earlier transcript has the Tate sheaf at 16/021 but no matching valuation-cocharacter construction.

The proposed cocharacter is described by \(\lambda\mapsto n^{-1}v_{\mathfrak p}(\lambda)\), but the page warns that this functional need not be integer-valued. A cocharacter of a complex diagonalizable group evaluates its character group in \(\mathbb Z\), so this denominator issue arises before its restrictions to \(\mu_2\) can be formed. The uncertain weight-zero example and the displayed valuation product on line 28 deserve scrutiny as written: an additive valuation sends a product to a sum, and that sum must not be inserted into the frozen text.

### T11 — A small calculation locating a denominator

**File/scan/lines:** cote 15, scan 121, lines 18–28. **Kind:** own idea. **Confidence:** high, by squaring the indicated number. **Context relation:** tests T10 and **MPL_14_002-044 M24a**; closest earlier Tate witness: 16/021, without this valuation example.

For \(L=\mathbb Q(\sqrt{-3})\), \(q=3\), and the extended normalized valuation \(v_3(3)=1\), the equation \((\sqrt{-3})^2=-3\) gives \(v_3(\sqrt{-3})=1/2\). On \(M=\langle\sqrt{-3},-1\rangle\subset L^\times\), this rational-valued character functional therefore cannot itself be the integer-valued functional of a cocharacter of \(D(M)\). This checks an integrality issue of the stated kind without asserting the manuscript's uncertain stronger “\(j=0\)” example.

### T12 — The finite-index claim has a target-lattice obstruction

**File/scan/lines:** cote 15, scan 121, lines 12, 30; scan 123, line 8. **Kind:** own idea. **Confidence:** high, by the exact character-pairing map. **Quote:** “d'indice fini”. **Context relation:** adds a check to **MPL_14_002-044 M24a**; no matching lattice assertion occurs in the supplied transcript (nearest category witness: 16/049).

Put \(X_*=\operatorname{Hom}(\mathbb G_{m\mathbb C},G^\circ_{\mathbb C})\), with \(L\subset X_*\) generated by the written \(i-i'\); the equations \(\varepsilon i=\varepsilon i'=1\) give \(\varepsilon_*(L)=0\). Meanwhile \(\varepsilon_*(j)=2\), so \(X_*/L\) maps onto a nonzero subgroup of \(\mathbb Z\), proving infinite index in the displayed target \(X_*\). The nonzero quotient persists after tensoring with \(\mathbb Q\); \(\ker\varepsilon_*\) is a candidate target to investigate, not a transcriptional correction.

### T13 — Reduction modulo two needs parity data

**File/scan/lines:** cote 15, scan 123, line 8. **Kind:** own idea. **Confidence:** high, by the two reduction maps. **Quote:** “aucune indication”; “Question semble secondaire”. **Context relation:** supplies a test for the present question and **Hua, findings register, 15-real-fibre-functor-criterion**, alongside **MPL_14_002-044 M24a**; no matching modulo-two discussion occurs in context (nearest category witness: 16/049).

Both \(2\mathbb Z\) and \(3\mathbb Z\) have finite index in \(\mathbb Z\), but their images under \(\mathbb Z\to\mathbb Z/2\mathbb Z\) are zero and the whole group, respectively. Thus even a repaired finite-index assertion would not by itself determine the differences of restrictions to \(\mu_2\). This explains why the residual question needs parity information.

### T14 — Effectivity from a distinguished cocharacter

**File/scan/lines:** cote 15, scan 121, lines 14, 30; scan 123, line 2. **Kind:** unproved claim. **Quote:** “sur \(Q\) !”; “La structure d'effectivité ... est déterminée grâce à \(i\)”. **Context relation:** adds arithmetic cocharacters to **MPL_14_002-044 M01** and **MPL_14_002-044 §107**; their full return is absent, while context 16/015–018 gives graded correspondence-ring constructions.

The page says that \(i\) and its conjugates determine effectivity, and that an automorphism preserving \(i\) is the identity, while the marginal generation/count statement is a low-confidence reading. The exact lattice test is that an automorphism fixing every conjugate cocharacter acts identically on their generated span. The manuscript still requires the integral lattice, the scope of “preserves \(i\)” over \(\mathbb Q\), and an effectivity rule compatible with its denominator caveat.

### T15 — The group involution and its gerbe lift

**File/scan/lines:** cote 15, scan 123, lines 20–24; scan 125, line 2. **Kind:** self-flagged / unproved claim. **Quote:** “involution canonique”; “Il [ne|me] semble pas”; “élément fondamental ... conjectural”. **Context relation:** adds a gerbe-obstruction question absent from the earlier transcript; compare context 16/049 and **MPL_7_061-072+8_001-078 Scan 061 (§66)**.

The character-group conjugation is asserted to give an involution on \(G\), followed by a tentative comment about an involution of the associated gerbe. The reading “ne|me” materially affects the author's stance and must remain marked. The mathematical questions are the band automorphism's action on the specified cohomology class and the coherence of a square-one lift.

### T16 — Direct check of the displayed two-torsion class

**File/scan/lines:** cote 15, scan 121, line 28; scan 123, lines 20–24; scan 125, line 2. **Kind:** own idea. **Confidence:** high for the displayed character/cohomology computation; no constructed gerbe involution is claimed. **Context relation:** adds a check to T15 and **MPL_7_061-072+8_001-078 Scan 061 (§66)**; no matching formula in context (nearest category passage: 16/049).

Write characters additively with \(q=\varepsilon^*(1)\): the relation \(\lambda\bar\lambda=q^{j^*(\lambda)}\) gives \(c(m)=j^*(m)q-m\), hence \(c([m])=-[m]\) on \(X^*(U)=X^*(G^\circ)/\mathbb Zq\). Thus the induced automorphism of \(U\) is inversion, acting on abelian \(H^2\) by \(h\mapsto-h\), and the page's “order dividing two” gives \(-h=h\). This calculation supplies no non-invariance obstruction from that class, while a chosen lift's square-one coherence still requires analysis.

### T17 — Order two is weakened on the sheet

**File/scan/lines:** cote 15, scan 125, line 2, both deleted and live readings. **Kind:** withdrawn in the same text. **Quote:** deleted “d'ordre \(2\)”, followed by “d'ordre ... divisant \(2\)”. **Context relation:** adds an explicit weakening to T15 and **MPL_7_061-072+8_001-078 Scan 061 (§66)**; no matching class in context 16/049.

The revision admits the zero class as well as a nonzero class of order two. A neutralization or involution comparison must preserve that revision, since the zero class and the nonzero \(\mu_2\)-class on scan 119 play different roles. Both textual states remain in the frozen transcription.

### T18 — Tate reduction and cancelled canonicity

**File/scan/lines:** cote 15, scan 135, lines 15–29. **Kind:** withdrawn in the same text / unpursued implication. **Quote:** “can.” cancelled; “munis d'un isom.”; “Giraud?”. **Context relation:** gives an explicit reduction beyond context 16/049; bears on **WG2 §2.4 #3** and **MPL_7_061-072+8_001-078 Scan 061 (§66)**; no earlier Giraud/gerbe passage found.

Restriction to the category generated by \(\mathbb Q(1)\) gives \(\varepsilon:G\to\mathbb G_m\), and fixing its fibre functor produces the gerbe of pairs \((\omega,\omega|_{M_0}\simeq\varphi)\), with automorphisms \(\ker\varepsilon\). The cancelled “can.” matters: tensor automorphisms of the Tate fibre functor act by \(t^i\) on \(\mathbb Q(i)\), for \(t\in\mathbb Q^\times\), so an isomorphism class does not choose an isomorphism. “Giraud?” marks a reference to verify and belongs in the standing register of self-marked steps.

### T18b — A later precise reference for “Giraud?”

**File/scan/lines:** cote 15, scan 135, lines 24–29. **Kind:** unpursued implication / primary-source comparison. **Quote:** “Giraud?”. **Context relation:** adds a later reference to T18 and standing item U16; searches for Giraud, Tate, restriction and gerbe in the supplied context locate the Tate sheaf at 16/021 and the category programme at 16/049, with no earlier matching reduced-gerbe construction; bears on **WG2 §2.4 #3** and **MPL_7_061-072+8_001-078 Scan 061 (§66)**.

Deligne–Milne, Proposition 5.8, constructs the gerbe of liftings of the canonical section along \(\operatorname{FIB}(\mathcal C)\to\operatorname{TORS}(\mathbb G_m)\), describing its objects as a fibre functor together with an isomorphism trivializing its Tate restriction. Its proof cites Giraud (1971), IV, 3.2.1, giving a precise later reference for comparison with the handwritten query. The Deligne–Milne passage was checked directly; Giraud's cited section was not independently inspected, and its 1971 publication does not date this manuscript sheet.

### T19 — The supplied arithmetic quotient

**File/scan/lines:** cote 15, scan 135, lines 32–43; scan 137, lines 2–4. **Kind:** unproved claim. **Quote:** “un nb fini d'objets simples”; “ss-catégorie ... pleinement fidèle”. **Context relation:** adds an arithmetic quotient to **WG2 §2.4 #3** and the README's extension-by-\(\Gamma_{\mathbb Q}\) question; earlier category witness: 16/049, with the Tate sheaf at 16/021 giving only a realization-level relation.

The manuscript characterizes \(M'\) by finiteness of simple constituents in tensor powers, identifies \(\ker(G\to G')\) with \(G^\circ\), and asserts a fully faithful embedding into étale rational vector spaces over \(k\). Evaluation at \(\bar k\) gives the quotient \(\Gamma_k\to G'\) acting on those representations, with kernel equal to the intersection of their kernels. The text supplies a subcategory, so identification of \(G'\) with the full \(\Gamma_k\), and specifically \(\Gamma_{\mathbb Q}\), requires documenting that all Artin representations occur.

### T20 — Two kernels called \(U\)

**File/scan/lines:** cote 15, scan 135, line 28; scan 137, lines 26–32. **Kind:** reading question. **Quote:** “\(\operatorname{Ker}\varepsilon=U\)”; “\(G^{(0)}=G_m\times G'\)”. **Context relation:** sharpens the sequence question in **WG2 §2.4 #3** and the README; no matching notation occurs in context (nearest category witness: 16/049).

The first reduction on 135 uses \(\ker(\varepsilon:G\to\mathbb G_m)\), while 137's final sequence uses \(\ker(\varepsilon,r)=\ker\varepsilon\cap\ker r=\ker\varepsilon\cap G^\circ\), with \(r:G\to G'\). The inclusion \(\ker(\varepsilon,r)\hookrightarrow\ker\varepsilon\) is their explicit relation, and silently identifying them would discard the action on \(M'\). The latter kernel agrees with the restricted-kernel notation beginning scan 117.

### T21 — The Artin–Tate quotient's representation formula

**File/scan/lines:** cote 15, scan 137, lines 6–32. **Kind:** unpursued implication. **Quote:** “\(\sum_{i\in Z}V_i(i)\)”; “\(G^{(0)}\simeq G'\times G_m\)”. **Context relation:** supplies the requested product quotient for **WG2 §2.4 #3** and the README; compare context 16/021's Tate sheaf and 16/049's category programme.

Relative to the chosen Tate functor and \(\bar k\)-evaluation, \((\gamma,t)\in G'\times\mathbb G_m\) acts on \(\bigoplus_iV_i(i)\) by \(v_i\mapsto t^i\rho_i(\gamma)v_i\), and the written convolution tensor formula makes this action tensor-compatible. This gives the map \(G\to G'\times\mathbb G_m\) and reduction by its kernel at the foot of the sheet. The displayed functor's \(k|i\) remains a reading question, and this construction supplies no chosen section of the full group map.

### T22 — The arithmetic trivialization is chosen

**File/scan/lines:** cote 15, scan 137, lines 2–4. **Kind:** unpursued implication. **Quote:** “un choix très particulier”. **Context relation:** adds a choice warning to **MPL_7_061-072+8_001-078 Scan 061 (§66)** and the README; no matching arithmetic-gerbe passage occurs in context (nearest motive category: 16/049).

The source chooses \(\psi_{\bar k}\) on \(M'\) and explicitly invokes nontrivial \(H^1(\mathbb Q,\Gamma)\). Already for the constant group \(\Gamma=\mathbb Z/2\mathbb Z\), the quotient homomorphism \(\Gamma_{\mathbb Q}\to\Gamma\) associated with \(\mathbb Q(\sqrt2)\) gives a nontrivial torsor class, exhibiting the kind of arithmetic choice involved. The selected structure on the page is a section of the gerbe restricted to the Artin subcategory.

### T23 — S15: the Nori–Ayoub comparison

**File/scan/lines:** cote 15, scan 135, lines 7–11, 32–43; scan 137, lines 26–32. **Kind:** unpursued implication. **Quote:** “lien de \(M\)”. **Context relation:** verifies part of README **S15**, building on **MPL_14_087-132 M23** and **MPL_14_002-044 M28a** as leads; earlier source context: 16/049.

For a fixed embedding \(k\hookrightarrow\mathbb C\), Choudhury–Gallauer (2017, Theorem 9.1) construct inverse Hopf-algebra maps \(\varphi_A:\mathcal H_N\to\mathcal H_A\), \(\varphi_N:\mathcal H_A\to\mathcal H_N\), yielding \(G_A(k)\simeq G_N(k)\); rational coefficients are included in their principal-ideal-domain result. This is a proved comparison of these constructions with a specified Betti embedding. It does not identify the manuscript's unspecified correspondence category with them, or give a specialization to the finite-field gerbes of scans 100–125.

### T24 — S15: pure Nori motives and the cycle comparison

**File/scan/lines:** cote 15, scan 135, line 7; scan 117, line 31. **Kind:** unpursued implication. **Quote:** “\(\frac12\) simples”. **Context relation:** checks **MPL_14_087-132 M23**, **MPL_14_002-044 M28a**, and **WG2 §2.3 #7** against a primary source; compare context 16/049 and notes 16:49:3–4.

For a fixed embedding \(k\hookrightarrow\mathbb C\), Arapura's Theorem 6.3.3, Corollary 6.3.4, and Theorem 6.4.1 prove semisimplicity and pro-reductivity for the pure rational Nori category and identify it with André's category through \(h_A^i(X)\mapsto h_N^i(X)\), compatible with realization. The additional cycle question is surjectivity of \(A_{\mathrm{hom}}^r(X)_{\mathbb Q}\hookrightarrow A_{\mathrm{mot}}^r(X)_{\mathbb Q}\subset H^{2r}(X,\mathbb Q(r))\), whose source is algebraic cycle classes and whose target is motivated classes. The cited theorem proves the Nori/motivated equivalence, without proving that inclusion surjective for every smooth projective \(X\); this identifies the remaining algebraicity requirement.

### T25 — S15: arithmetic exactness for Nori motives

**File/scan/lines:** cote 15, scan 135, lines 35–43; scan 137, lines 2–4, 30. **Kind:** unpursued implication. **Quote:** “composante neutre”. **Context relation:** adds a verified modern sequence to README **S15** and **WG2 §2.4 #3**; earlier source context: 16/049, with only register leads for Nori.

Kahn (2025, Theorem 5.10 and §10, especially Proposition 10.1, Theorem 10.2, and Remark 10.3) proves for rational Nori motives over \(k\subset\mathbb C\) the exact sequence \(1\to G_N(\bar k)\to G_N(k)\to\Gamma_k\to1\), with maps induced by base change and Artin inclusion. Its proof uses effective Galois descent and does not invoke standard conjectures. This supplies a modern arithmetic sequence, while the manuscript's \(G^\circ\) and initially unspecified \(M'\) still require comparison with the geometric group and the full Artin category.

### T26 — The period-conjecture evidence limit

**File/scan/lines:** cote 15, the kept scans 087–138, especially 125 line 2 and 135–137. **Kind:** reading question. **Quote:** “gerbe des ... foncteurs fibres”; “élément fondamental ... conjectural”. **Context relation:** answers the README's period-witness question; context searches locate Betti comparison at 16/044, Bott periodicity at 16/035, and Oda's paper, but no requested assertion on the current sheets; the missing cote 12 “Motifs” and excluded cote 15/136 lie outside this search.

The present batch contains a fibre-functor gerbe and a conjectural \(H^2\)-class, but its complete text search locates no period-pairing, transcendence-degree, or algebraic-independence assertion. For a later precise comparison, Huber's *Galois theory of periods*, §§3–5, describes the formal-period algebra, its torsor interpretation, and conjectural injectivity of evaluation \(\widetilde{\mathcal P}\to\mathbb C\); these assertions add to the restrictions and trivializations actually written on 135–137. The finding is limited to the 48 supplied pages.

### T27 — Descent formulas for the polarization/real-structure bridge

**File/scan/lines:** cote 15, scan 119, lines 8–16; scan 121, lines 2–4. **Kind:** own idea. **Confidence:** high for the group identities and representation comparison; no equivalence of reconstruction problems is claimed. **Context relation:** adds formulas to the README's requested table and **MPL_14_002-044 §3**, **MPL_14_087-132 §81**; earlier pairing witnesses: context 44/002 Th.4 and 44/008–009.

For an extension \(1\to\Pi\to E\to\operatorname{Gal}(\mathbb C/\mathbb R)\to1\), a lift \(s\) of conjugation gives \(\tau=\operatorname{Ad}_s\), \(c=s^2\in\Pi\), \(\tau^2=\operatorname{Ad}_c\), and \(\tau(c)=c\); replacing \(s\) by \(as\) sends \((\tau,c)\) to \((\operatorname{Ad}_a\tau,a\tau(a)c)\). For a homomorphism \(\widetilde\rho:E\to\operatorname{GL}_{\mathbb C}(V)\rtimes\operatorname{Gal}(\mathbb C/\mathbb R)\), with coefficient conjugation in a fixed complex basis of \(V\), and commuting with the projections to \(\operatorname{Gal}(\mathbb C/\mathbb R)\), write \(\rho=\widetilde\rho|_\Pi\) and let \(J\) be the semilinear operator assigned to \(s\); the identities become \(J\rho(g)J^{-1}=\rho(\tau(g))\) and \(J^2=\rho(c)\), with the same change-of-lift formula. The real fibre functors on 119 thus have an explicit descent-language comparison with real arithmetic extensions, including the equation to solve for a square-one lift.

## Suggested S15 summary

| Manuscript feature | Verified result / exact comparison | Remaining manuscript-specific issue |
|---|---|---|
| Group or band of a motivic category | Inverse Nori–Ayoub Hopf-algebra maps, T23 | Specify the manuscript's correspondence equivalence and comparison functor |
| Semisimplicity | Pure rational Nori = André category, T24 | Surjectivity of the displayed algebraic-to-motivated cycle-class inclusion |
| Arithmetic quotient | Nori exact sequence from Artin inclusion and base change, T25 | The kept manuscript supplies a subcategory \(M'\), a \(G'\), and its gerbe |
| Tate/Artin reduction | Restriction \(G\to G'\times\mathbb G_m\), T18–T21 | Preserve both scopes of \(U\) and the chosen trivializations |
| Compact real obstruction | Direct cohomology calculation T04 and framework T07 | Compatibility clause and scan119 projection formula |
| Period assertion | Formal evaluation map and torsor, T26 | No such written assertion identified in this batch |

## Primary references inspected

Source-derived summaries are kept below approximately 200 words per external source across this report; there are no substantial external quotations. Root should open a source itself before citing its retrieval reference in the final chat.

1. **CG2017:** Utsav Choudhury and Martin Gallauer Alves de Souza, *An isomorphism of motivic Galois groups*, Advances in Mathematics 313 (2017), 470–536; [DOI](https://doi.org/10.1016/j.aim.2017.04.006). Checked [arXiv:1410.6104v3](https://arxiv.org/pdf/1410.6104), printed p.5 conventions, p.41 Theorem 9.1. Retrieval references: turn4view0, turn5view0, turn5view1.
2. **Ara2013:** Donu Arapura, *An abelian category of motivic sheaves*, Advances in Mathematics 233 (2013), 135–195. Checked [arXiv:0801.0261v4](https://arxiv.org/pdf/0801.0261), printed pp.57–61, Theorems 6.3.3, 6.4.1 and Corollary 6.3.4, including the comparison functor's proof. Retrieval references: turn4view1, turn5view2, turn5view3, turn8view3.
3. **DM1982/2012:** Pierre Deligne and James S. Milne, *Tannakian Categories*, Lecture Notes in Mathematics 900 (1982), pp.101–228. Checked [corrected 15 August 2012 text](https://www.jmilne.org/math/xnotes/tc.pdf), §4, printed pp.36–44, especially Theorems 4.16–4.17, and Proposition 5.8, p.50; the Artin addendum also checks Proposition 6.17 and Remark 6.19, p.61. The corrected §6.22–6.23 records a qualification; T25 uses Kahn's later exactness proof. Retrieval references: turn4view2, turn5view4, turn8view1, turn8view2.
4. **Kahn2025:** Bruno Kahn, *Galois descent for motivic theories*, Theory and Applications of Categories 44 (2025), No.20. Checked [arXiv:2312.01825v4](https://arxiv.org/pdf/2312.01825), printed p.19 Theorem 5.10 and pp.24–25 §10. Publisher PDF timed out; the checked text is the dated author preprint. Retrieval references: turn11view1, turn12view0, turn12view1.
5. **Huber2018:** Annette Huber, *Galois theory of periods*, 29 November 2018 version, [author PDF](https://home.mathematik.uni-freiburg.de/arithgeom/preprints/huber-galois.pdf), §§3–5. Retrieval reference: turn23view0. Used for the precise formal-evaluation/torsor formulation, with no assertion that a broad period conjecture has been proved.

## Source for root's separate bridge research

Joseph Ayoub, *Anabelian presentation of the motivic Galois group in characteristic zero*, [current author PDF](https://user.math.uzh.ch/ayoub/PDF-Files/Anabel.pdf) and [Cambridge publication](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/anabelian-presentation-of-the-motivic-galois-group-in-characteristic-zero/060D618ED5F59A2FAFAB845999BD963A). Root owns inspection of this paper; this branch uses no theorem from it above.
