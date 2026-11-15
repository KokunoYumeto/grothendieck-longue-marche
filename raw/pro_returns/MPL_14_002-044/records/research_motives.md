# Research evidence and proposed notes: effectivity and motivic groups

Research agent: /root/research_motives. Written after the transcription freeze of 2026-11-15 00:41:55 UTC. Frozen page files and the combined transcription were not edited. No manuscript images or manuscript OCR were used. Published primary-source PDFs were read; Künnemann's scanned printed article was read visually on the relevant printed pages.

The files context/notes/RESULTS_STATE.md and context/README.md were fully read before drafting. Earlier AI notes and register statuses retain their stated review limitations; they are comparison leads, not automatically established results.

## Conventions and search ledger

The complete 31-query context ledger is records/research_motives_context_search.md. Searches M01–M31 used rg -n -i on the four supplied context text files, recording full hit counts and up to ten excerpts per file. Supplementary searches are listed at the end of this record.

**CT** = context/MPL_16+47+54+44_transcription.tex; **CN** = context/MPL_16+47+54+44_notes.md; **RS** = context/notes/RESULTS_STATE.md. Every frozen filename below lies in MPL_14_002-044_work/pages/. “No matching row” means no directly matching row in the supplied, fully read RS.

Each paragraph headed **Proposed note** contains at most four prose sentences; evidence and search/status metadata are separate. Own examples test their explicitly displayed data, not the unseen four-structure package. No conditional theorem is proposed.

## Proposed notes

### M01 — The fragment starts with an existing category and a fourth structure

**Frozen evidence:** MPL_14_002-044_14_scan002.tex, lines3–5; MPL_14_002-044_14_scan003.tex, line4; cote14, scans002–003. Quotes: “Structure d'effectivité”; “4°) La donnée d'une sous-catégorie … de M”.
**Kind:** reading question. **Context M01:** terms Structure d.effectiv, structures motiviques, category of motives; CT cote16 scan49 line1829; CN S15. **Delta:** adds effectivity on an existing category, without supplying its construction. **RS:** WG2 §2.4 #3 [question or plan item, round2; unchecked]; no row settles the construction in cotes12–13.

**Proposed note.** The cancelled general title on scan002 and the surviving fourth item on scan003 place these sheets inside a larger account of motivic structures, but the supplied fragment begins with \(M\) already in use. The references to \(3^\circ\) on scans009 and011 therefore cannot be expanded into an unseen definition of \(I(G)\), its polarization conditions, or a construction from Lefschetz correspondence rings. Cote16 scan49 supplies a related semisimplicity question; the actual category-building passages of cotes12–13 are absent from the supplied context.

### M02 — Proposed axioms and the character cone

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, lines4–16; cote14 scan003. Quotes: “stable … pr sommes … pr sous-objets”; “et réciproqt”; “Il y a lieu de poser d'autres axiomes”.
**Kind:** unproved claim and proposed axioms. **Context M02:** effectivité, effectivity, K(G), semi.simple; CT cote16 scan49; CN 16:49:4 and S15. **Delta:** adds effectivity and descent claims beyond the earlier semisimplicity request. **RS:** no direct matching row; WG2 §2.4 #3 is the broader unchecked question.

**Proposed note.** The live requirements are a strictly full subcategory \(M^+\), closure under tensor products, sums and subobjects, inclusion of \(\Lambda(-1)\), eventual effectivity after an integral Tate twist, positive grading, and the proposed origin in a structure on \(G^0\) invariant under the whole group; “quotients” is cancelled. The asserted equivalence between rational and complex descriptions and the cone \(K^+(G)\subset K(G)\) is not proved here, while the margin names the basis of rational irreducible characters that the rational description must retain. The cone is required to contain \(0,\varepsilon\) and be closed under multiplication and the uncertain \(\lambda|\Lambda\) operation; the deleted \(1\) and uncertain operation must not be completed from a standard definition.

### M03 — Finitely many “types” needs a precise quantifier

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, lines12,18–19; cote14 scan003. Quotes: “nb fini de types … de poids i … ???”; “G^0 opère trivialt”.
**Kind:** self-flagged axiom; own calculation. **Context M03:** poids, weight, types de motifs, Artin; CT cote44 scan7 is root-weight terminology, not this finiteness question; no answer in CN. **Delta:** adds an expressly queried axiom. **RS:** no matching finiteness row; WG2 §2.4 #3 [unchecked] is broader. **Confidence:** high for the direct-sum calculation; no claim about the intended meaning of “types”.

**Proposed note.** The question marks belong to the proposed axiom and “types” is not defined here. For every nonzero effective object \(E\) of fixed weight, \(E^{\oplus r}\), \(r\geq1\), remains effective of that weight and has distinct realization dimension, so finiteness cannot mean all such isomorphism classes. The nearby irreducible-character margin suggests a quantity to investigate without deciding the reading, and the stated trivial action of \(G^0\) in effective weight zero gives the exact factorization \(\rho_E:G\to G/G^0\to\operatorname{GL}(\omega E)\).

### M04 — Preserve the two written signs of the twist

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, line4; MPL_14_002-044_14_scan005.tex, lines4–6; cote14 scans003,005. Quotes: \(E(-n)=E\otimes\Lambda(-1)^{\otimes n}\); \(E(n)\in P(i)\).
**Kind:** reading question; own calculation. **Context M04:** Tate, twist, Lambda(-, effectif; CT cote16 scan48 expressly drops twists for simplicity; CN S14 concerns twist-sensitive inverses. **Delta:** adds an explicit sign issue. **RS:** no direct matching row. **Confidence:** high for the integer reindexing and weight shift.

**Proposed note.** Scan003 writes \(E(-n)\), whereas scan005 writes \(E(n)\), and both readings must remain. Over all integers the substitution \(n\mapsto-n\) gives an exact equivalence of the existence assertions; the sign matters for a nonnegative bound or the direction of a displayed construction. With \(\varepsilon\) the character of \(\Lambda(-1)\), the \(i\)-weights of \(E\otimes\Lambda(-1)^{\otimes N}\) are \(a+N\varepsilon(i)\), so \(\varepsilon(i)>0\) specifies the twist that moves the finitely many weights upward.

### M05 — Conjugation transports the weight spaces

**Frozen evidence:** MPL_14_002-044_14_scan005.tex, line2; cote14 scan005. Quote: “ses conjugués … en particulier de \bar i”.
**Kind:** unproved claim with verification of inner conjugation. **Context M05:** conjugu, polarisation, foncteur, graduation; CT cote16 scans16–17 requires images of grading projectors; CN R3 studies conjugation fixing L. **Delta:** adds the exact representation map. **RS:** no matching row. **Confidence:** high; the displayed intertwiner proves transport.

**Proposed note.** For \(i'=gig^{-1}\), the map \(\rho_E(g)\) sends \(E_a(i)\) isomorphically onto \(E_a(i')\), since \(\rho_E(i'(t))\rho_E(g)=\rho_E(g)\rho_E(i(t))\). Hence the nonnegative-weight test defining \(P(i)\) is invariant under inner conjugation. The further assertion about automorphisms of \(\mathbb C\) uses the rational descent data invoked on scan003 and is not proved by this inner-conjugation calculation alone.

### M06 — An infinite intersection can lose eventual Tate effectivity

**Frozen evidence:** MPL_14_002-044_14_scan005.tex, lines9–10; cote14 scan005. Quote: “sauf peut être au dernier sur la graduation”.
**Kind:** self-flagged claim; own idea. **Context M06:** intersection, saturation, cône, cone, P(i); no matching construction in CT cote16 scans3–18 or their CN notes, incidental hits in the ledger. **Delta:** adds an explicit test of the caveat. **RS:** no matching row. **Confidence:** high; every character and cocharacter is specified.

**Proposed note.** In \(G=\mathbb G_m^2\), set \(\varepsilon(x,y)=x\) and \(i_m(t)=(t,t^m)\) for \(m\in\mathbb Z\), so every \(\varepsilon\circ i_m\) is the identity. The character \(y\varepsilon^N\) has \(i_m\)-weight \(m+N\), and no integer \(N\) makes these weights nonnegative for all \(m\). Thus each \(P(i_m)\) has eventual Tate effectivity, whereas their intersection has only characters \(x^a\), \(a\geq0\), and no twist of \(y\); this gives a precise failure relevant to the unfinished intersection discussion without deciding the uncertain “dernier”.

### M07 — A torus test for \(W\) versus \(W'\)

**Frozen evidence:** MPL_14_002-044_14_scan007.tex, lines6–15; cote14 scan007. Quote: “invariant pr W (mais peut-être pas pr W'!]”.
**Kind:** self-flagged claim; own idea. **Context M07:** Aut.*ext, Norm.*T, W', conjug; CT cote16 scans16–17 and CN R3 concern inner changes, without imposing all outer automorphisms. **Delta:** adds a direct test of the larger action. **RS:** no matching row. **Confidence:** high for the lattice computation; it tests the displayed cone data, not unseen polarization axioms.

**Proposed note.** For \(G=\mathbb G_m^2\), \(W=1\), while \(\alpha(x,y)=(x,y^{-1})\) defines an element of \(W'\) preserving \(\varepsilon(x,y)=x\) and \(j(t)=(t^2,1)\). The cone generated by \((2,0),(1,1)\) is \(W\)-invariant, contains \(j\), and lies in \(\varepsilon\geq0\), but \(\alpha(1,1)=(1,-1)\) lies outside it. This realizes the source's “peut-être pas” for those displayed requirements, with trivial rational Galois action, without claiming a counterexample to the additional structure referenced as \(3^\circ\).

### M08 — Orbit notation and finite Galois action

**Frozen evidence:** MPL_14_002-044_14_scan007.tex, lines16–21; MPL_14_002-044_14_scan013.tex, line6; MPL_14_002-044_14_scan015.tex, lines5–7; cote14 scans007,013,015. Quotes: \(\Gamma'=\Gamma/W\); “\(\Gamma=S(\mathbb C)\)”; “via un quotient fini”.
**Kind:** reading question; own scope example. **Context M08:** pi_1, galois, quotient fini, finite quotient; CT cote16 scan28 is reused group-scheme typescript; README lines16–18 asks the motivic exact-sequence question. **Delta:** adds the prime-sensitive notation issue and finite-type boundary. **RS:** WG2 §2.4 #3 [unchecked]; no direct result. **Confidence:** high for the product-torus calculation.

**Proposed note.** Scan007 assigns the orbit set to \(\Gamma'\), then writes \(\Gamma=S(\mathbb C)=S(\overline{\mathbb Q})\), leaving a missing or omitted prime to record. The later torus discussion explicitly specifies a finite-rank character lattice and a faithful finite quotient. For the protorus \(T=\prod_n\operatorname{Res}_{K_n/\mathbb Q}\mathbb G_m\), with independent quadratic extensions \(K_n\), the character lattice \(\bigoplus_n\mathbb Z[\operatorname{Gal}(K_n/\mathbb Q)]\) has infinite Galois image, although every finite subproduct has a finite quotient action, displaying the additional limit issue for a full proalgebraic motivic group.

### M09 — Saturation remains an unanswered definition

**Frozen evidence:** MPL_14_002-044_14_scan009.tex, lines4–6; cote14 scan009. Quotes: “saturation que nous ne précisons pas ici”; “est-elle automatiquement satisfaite ?”.
**Kind:** explicit question; unproved equivalence. **Context M09:** satur, polaire, polar cone, cône; no matching definition in CT or CN; CT cote16 scans15–18 does not define this cone operation. **Delta:** adds a missing datum to the claimed parameterization. **RS:** no matching row.

**Proposed note.** The asserted equivalence between intersections of \(P(i)\)'s and Galois-invariant cones includes an unnamed saturation condition and immediately asks whether it is automatic. The margin that \(\varepsilon\) lies in the interior of the polar cone also leaves the real ambient space, topology, and meaning of a cone in \(\Gamma/W\) unstated. Neither the equivalence nor the automatic-saturation answer is supplied by the earlier correspondence-ring construction.

### M10 — Positivity tests forget primitive-generator information

**Frozen evidence:** MPL_14_002-044_14_scan009.tex, lines4,8–10; cote14 scan009. Quotes: “saturation”; \(\varepsilon i_1=\mathrm{id}\).
**Kind:** own idea. **Context M10:** saturation, primitive, cocharacter, copoid; CT cote44 scan7 concerns root/coroot terminology, not a saturation theorem here. **Delta:** adds a rank-one calculation. **RS:** no matching row. **Confidence:** high; the two inequalities are equivalent.

**Proposed note.** In \(X_*(\mathbb G_m)=\mathbb Z\), the monoids \(2\mathbb Z_{\geq0}\) and \(\mathbb Z_{\geq0}\) impose the same character inequalities, since \(2a\geq0\) is equivalent to \(a\geq0\). Thus the map from raw cocharacter sets to their nonnegative-weight subcategories forgets this primitive-generator information. The calculation motivates saturation but does not settle \(I(G)\to\mathrm{Eff}(G)\), because \(\varepsilon i_1=\mathrm{id}\) explicitly excludes replacing a normalized \(i_1\) by its double.

### M11 — The normalization gives weight \(+2\)

**Frozen evidence:** MPL_14_002-044_14_scan009.tex, lines8–10; MPL_14_002-044_14_scan013.tex, line8; cote14 scans009,013. Quotes: \(i_1\bar i_1=j\); \(\langle i,\varepsilon\rangle=2\).
**Kind:** unpursued implication; own calculation. **Context M11:** graduation, poids, weight cocharacter, j; CT cote16 scans3,16–17 retains degree projectors; CN S3 gives an operator model. **Delta:** adds the exact weight convention. **RS:** WG2 §2.4 #3 [unchecked]. **Confidence:** high; apply the rational character to the displayed product.

**Proposed note.** Applying \(\varepsilon\) to \(i_1\bar i_1=j\), with \(\varepsilon i_1=\mathrm{id}\), gives \(\varepsilon(j(t))=t^2\). This matches weight \(+2\) for \(\mathbb L=\mathbb Q(-1)\); the character of \(\mathbb Q(1)\) is \(\varepsilon^{-1}\) and has composition \(t^{-2}\) with the same cocharacter. This supplies an exact comparison of conventions, while the missing \(3^\circ\) prevents assigning a full definition of \(j\) to these sheets alone.

### M12 — Retain the two possible injectivity maps

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, lines3–9; cote14 scan011. Quotes: \(I^{a|\alpha}(G)\to\mathrm{Pol}(G)\times\mathrm{Eff}(G)\); “I(G)-Eff(G), injective ?”.
**Kind:** explicit question. **Context M12:** injectiv, I(G), Eff, polarisation; CT cote16 scans16–17 and CN R3 discuss forgetting grading data in the universal-ring map. **Delta:** adds a cocharacter injectivity problem with specified quotient group. **RS:** WG2 §2.4 #3 [unchecked]; no row resolves it.

**Proposed note.** The displayed map retains polarization and effectivity, while the insertion names the map retaining effectivity alone, leaving two possible targets of the injectivity question. The sentence “modulo action de \(G(\mathbb R)\)” gives part of the intended equivalence relation, but \(I^{a|\alpha}(G)\) still depends on the absent \(3^\circ\). M10's scaling computation cannot decide either normalized question, and the earlier negative example for a Lefschetz-ring homomorphism has its own expressly given domain and target.

### M13 — Is one cocharacter sufficient for motivic effectivity?

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, line11; cote14 scan011. Quote: “sont elles dans Im I(G) ?”.
**Kind:** explicit question. **Context M13:** Im I(G), effectiv, foncteur fibre, single cocharacter; no answer in CT cote16 scans3–18,49 or CN S15–S16. **Delta:** adds a surjectivity question beyond intersections. **RS:** WG2 §2.4 #3 [unchecked]; no resolved row.

**Proposed note.** The question is specifically whether effectivity structures coming from motives admit \(M^+=P(i_1)\) for one admissible cocharacter. The preceding construction permits intersections of many \(P(i)\)'s, and M06 displays the extra eventual-twist issue in an infinite intersection. The supplied context and the verified comparison theorems below do not answer this normalized surjectivity question for \(I(G)\).

### M14 — Fibre-functor change has an exact torsor transport

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, lines13–15; cote14 scan011. Quotes: “propriété intrinsèque … indép. du foncteur”; “en tordant pr un torseur”.
**Kind:** unproved intrinsicness claim; verified formal comparison. **Context M14:** torseur, fibre, fiber, De.Rham; CT cote54 scan3; CN D01–D02; README lines22–26. **Delta:** adds the actual transport underlying the suggestion. **RS:** MPL_7_061-072+8_001-078 Scan061 (§66) [observation, first-pass research lead] concerns fibre-functor requirements; no row proves this intrinsicness claim. **Primary:** Deligne–Milne Theorem3.2.

**Proposed note.** Deligne–Milne's Theorem3.2 identifies \(P=\operatorname{Isom}^{\otimes}(\omega,\omega')\) as a torsor under \(G=\operatorname{Aut}^{\otimes}(\omega)\). The transport is \(\omega'(E)=P\times^G\omega(E)\) and \(G'=\operatorname{Aut}^{\otimes}(\omega')=P\times^G G\), with conjugation in the second contracted product; a trivialization \(p\) transports \(i\) as \(p i p^{-1}\). Changing \(p\) changes this expression by inner conjugation, so M05 verifies independence of the weight inequalities, while descent of the further \(I(G)\)-conditions is the part of the author's intrinsicness claim not defined in this fragment.

### M15 — The relative de Rham proposal remains unfinished

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, line15; MPL_14_002-044_14_scan013.tex, line2; cote14 scans011,013. Quote: “motif sur schéma connexe S … foncteur de De-Rham … ?”.
**Kind:** research suggestion; related opening sentence cancelled on013. **Context M15:** De.Rham, universelle, H^1, foncteur fibre; CT cote54 scan3 lines2620–2636; CN D01–D02. **Delta:** adds a proposed relative setting to the earlier degree-one construction. **RS:** no directly matching row; WG2 §2.4 #3 [unchecked] is broader.

**Proposed note.** Scan011 asks about the four structures over a connected base with a rational point, and the opening Hodge/de Rham fibre-functor sentence on scan013 is cancelled. The concrete context witness is cote54 scan3, with \(0\to t_A^\vee\to H^1_{\mathrm{dR}}(A)\to t_B\to0\) and the universal-vector-extension tangent sequence, providing a degree-one realization to compare. Those sequences do not themselves define the relative category, descent of all four structures, or a six-operations formalism, and none is constructed in this fragment.

### M16 — The uncertain \(\mathrm{SL}_2|\mathrm{GL}_2\) example and its character

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, line17; cote14 scan011. Quote: \(G=\mathrm{Sl}(2,\mathbb Q)|\mathrm{Gl}(2,\mathbb Q)\).
**Kind:** reading question; added calculation attached to an existing register row. **Context M16:** Sl(2, Gl(2, SL_2, GL_2, theta, det; CT cote16 scans14–17; RS group-scheme comparison. **Delta:** adds the determinant character without reproving or promoting the row. **RS:** LM1 A.8 [Refuted, the return's claim], unrestricted uniqueness of GL2 group-scheme isomorphisms. **Confidence:** high for the determinant calculation.

**Proposed note.** The proposed example remains \(\mathrm{Sl}(2,\mathbb Q)|\mathrm{Gl}(2,\mathbb Q)\) in the frozen reading. RS LM1 A.8 already records \(\theta(g)=\det(g)^{-1}g\) fixing \(\mathrm{SL}_2\); the additional datum here is \(\det(\theta(g))=\det(g)^{-1}\). Thus the comparison must track the distinguished character \(\varepsilon\): for \(\varepsilon=\det\), one has exactly \(\varepsilon\circ\theta=\varepsilon^{-1}\), so agreement on \(\mathrm{SL}_2\) does not preserve that character.

### M17 — Frobenius is an announced arithmetic extension

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, line19; cote14 scan011. Quote: “peuvent être sans doute formulées … éléments de Frobenius”.
**Kind:** expectation. **Context M17:** Frobenius, Weil, arithm; CT cote16 scans46,50; CN S17. **Delta:** adds the expectation of reinterpreting structures3°–4°, without a criterion. **RS:** WG2 §2.4 #3 [unchecked]; no row settles it.

**Proposed note.** The sentence proposes introducing Frobenius elements to formulate deeper arithmetic properties and reinterpret the third and fourth structures. It gives no realization, specialization, Frobenius conjugacy class, or equation determining effectivity or polarization. Later cohomological uses of Frobenius in cotes14 and16 cannot be substituted for the unwritten criterion proposed here.

### M18 — Rational torus characters have an explicit descent map

**Frozen evidence:** MPL_14_002-044_14_scan013.tex, lines6–10; MPL_14_002-044_14_scan015.tex, lines5–14; cote14 scans013,015. Quotes: \(\mathbb Z(M)^+\); \(K(T)=\mathbb Z(M)^\pi\).
**Kind:** unproved claim with direct descent calculation. **Context M18:** caract, torus, tore, Z(M); CT cote44 scan7 supplies a different weight-lattice discussion; no descent proof in CN. **Delta:** adds the representation-semiring descent. **RS:** no matching row. **Confidence:** high for the orbit representation.

**Proposed note.** Over a finite Galois splitting field \(L/\mathbb Q\), a finite orbit \(O\subset M\) gives \(\bigoplus_{m\in O}Le_m\), with \(te_m=m(t)e_m\) and \(\sigma(ae_m)=\sigma(a)e_{\sigma m}\). Descent yields a rational representation with complex character \(\sum_{m\in O}e^m\), directly explaining the positive invariant combinations on scan013 and their group completion on015. The finite-generation assertion for \(K(T)\) and quotient \(D_{\mathbb Z}(M)/\pi\) are written claims; neither specifies the further effectivity subcone without the additional \(i_1\)-inequalities.

### M19 — Compactness is asserted; its displayed proof is cancelled

**Frozen evidence:** MPL_14_002-044_14_scan013.tex, lines14–20; cote14 scan013. Quotes: “J'affirme … dim S=1”; “Ker ε est compact”.
**Kind:** unproved assertion; attempted proof withdrawn on the same page. **Context M19:** compact, polarisation, real form, forme réelle; CN's discussions for cote16 scans44,49 do not prove the torus assertion. **Delta:** adds its later formal mechanism. **RS:** no matching row. **Primary:** Deligne–Milne Lemma4.24, Proposition5.18.

**Proposed note.** The assertion that the split quotient has dimension one survives, but the two-dimensional argument beneath it is entirely cancelled. Deligne–Milne's Lemma4.24 and Proposition5.18 relate a polarization to a compact inner real form of the Tate-character kernel. For a torus the inner action is trivial, so \(\sigma_C(g)=C^{-1}\sigma(g)C=\sigma(g)\), giving the exact later compactness mechanism; identifying the missing manuscript \(3^\circ\) with those polarization axioms remains an evidence gap.

### M20 — The target of “Fausse” remains uncertain

**Frozen evidence:** MPL_14_002-044_14_scan015.tex, line24; compare MPL_14_002-044_14_scan013.tex, lines14–20; cote14 scans015,013. Quotes: “ne peut pas … Q pr R”; “partie compacte … Fausse”.
**Kind:** self-correction with uncertain scope. **Context M20:** Fausse, compact, remplacer, simplifier; whole-file CT/CN search across cotes16,47,54,44 found no directly matching scan or missing sentence resolving the correction. **Delta:** records the self-correction with bounded scope. **RS:** no matching row.

**Proposed note.** The final paragraph attempts fixed-weight finiteness and expressly denies replacing \(\mathbb Q\) by \(\mathbb R\). Its uncertain “notion|condition de partie compacte” and final “Fausse” do not unambiguously cancel the earlier assertion that \(\ker\varepsilon\) is compact. Both the surviving assertion on013 and this later correction should be recorded with their actual textual scopes, without assigning “Fausse” a target supplied by expectation.

### M21 — Real-value positivity loses two distinct pieces of data

**Frozen evidence:** MPL_14_002-044_14_scan015.tex, line14; cote14 scan015. Quote: “valeurs ≥0 … S(R)° ??”.
**Kind:** explicit question; own idea. **Context M21:** valeurs, positiv, effectiv, character; CT cote16 scan44 and CN S13 concern a trace-pairing positivity test, not these evaluation maps. **Delta:** adds the exact map and two counterexamples to the proposed test. **RS:** no matching row. **Confidence:** high; explicit Laurent polynomials.

**Proposed note.** For \(T=S=\mathbb G_m\), evaluation \(\mathbb Z[x,x^{-1}]\to\operatorname{Fun}(\mathbb R_{>0},\mathbb R)\) sends \(x^{-1}\) to a positive function although its weight under the identity cocharacter is \(-1\). It sends \(x^2-x+1=(x-\tfrac12)^2+\tfrac34\) to a positive function although its coefficient of \(x\) is negative, so it is not an actual representation character. These calculations exhibit exactly why the proposed test recovers neither the coefficient-positive character semiring nor the chosen nonnegative cocharacter degrees.

### M22 — The one-variable polynomial test is valid

**Frozen evidence:** MPL_14_002-044_14_scan015.tex, lines14–22; cote14 scan015. Quote: “fonction polynômiale i.e. restant finie … t→0”.
**Kind:** unproved claim with own verification. **Context M22:** polyn, anneau affine, t.*0, alpha; CT cote16 scans48–49 concerns characteristic polynomials and supplies no intrinsic-effectivity criterion; CN polynomial hits are recorded in the ledger. **Delta:** verifies the chosen-cocharacter test. **RS:** no matching row. **Confidence:** high; the least Laurent exponent determines the limit.

**Proposed note.** The map \(i_1^*:M\to\mathbb Z\) induces \(\alpha^*:\mathbb Z[M]\to\mathbb Z[t,t^{-1}]\), \(e^m\mapsto t^{\langle i_1,m\rangle}\). A nonzero finite Laurent polynomial with least exponent \(a\) is bounded as \(t\to0\) exactly for \(a\geq0\), since it is \(t^a\) times a polynomial nonzero at zero, and the zero polynomial satisfies both tests. Actual representation characters have nonnegative coefficients, so cancellation cannot hide a negative weight, verifying the test once \(i_1\) is chosen without answering the intrinsic-choice question.

### M23 — A dimension-three real model displays the finiteness hazard

**Frozen evidence:** MPL_14_002-044_14_scan015.tex, line24; MPL_14_002-044_14_scan003.tex, lines18–19; cote14 scans015,003. Quotes: “T … dim ≥3”; “poids 0 … G^0 … trivialt”.
**Kind:** own idea. **Context M23:** compact, poids, fini, real; CT cote16 scans3–18 and CN's operator models give no torus fixed-weight calculation. **Delta:** adds a real model and identifies the extra axiom it violates. **RS:** no matching row. **Confidence:** high for the lattice calculation, low for identifying it as the author's intended example.

**Proposed note.** Take \(T_{\mathbb R}=\mathbb G_m\times U(1)^2\), with character basis \(a,b,c\), conjugation \((a,b,c)\mapsto(a,-b,-c)\), and \(\varepsilon=a\), \(j=(2,0,0)\), \(i_1=(1,1,0)\). Then \(i_1+\bar i_1=j\), \(\langle i_1,\varepsilon\rangle=1\), and \(\ker\varepsilon=U(1)^2\) is compact, while the distinct real irreducibles with characters \(e^{rc}+e^{-rc}\), \(r\geq1\), all have weight zero and nonnegative \(i_1\)-degrees. Thus these real compact-kernel/cocharacter conditions permit infinitely many fixed-weight types; the model violates scan003's additional trivial-\(G^0\)-action requirement in effective weight zero, so it tests the proposed real simplification rather than refuting the full intended axioms.

### M24 — Correspondence-to-motive maps locate the construction question

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, line4; MPL_14_002-044_14_scan011.tex, lines13–15; cote14 scans003,011. Quote: “sous-catégorie … de M”.
**Kind:** unpursued implication requested by the context. **Context M24:** lefschetzien, correspondance, motives, semi.simple; CT cote16 scans3–18, especially18, and49; CN S3,S14–S16. **Delta:** adds explicit maps without inventing absent cotes12–13. **RS:** WG2 §2.4 #3 and WG2 §6. #9 [unchecked]. **Primary:** Jannsen1992 opening definitions p447.

**Proposed note.** The standard correspondence construction has objects \((X,p,m)\), morphisms \(qA^{\dim X-m+n}(X\times Y)p\), and composition \(g\circ f=p_{13*}(p_{12}^*f\cdot p_{23}^*g)\), giving the concrete passage from correspondence rings and their idempotents to motives and maps. Cote16's graded correspondences, degree projectors and Lefschetz operators can be compared through \(\bigoplus_r\operatorname{Hom}(h(X),h(X)(r))\), retaining Tate twists. Cote14 already names \(M\), so these maps explain the mathematical relation without proving that absent cotes12–13 use that construction.

### M24a — The abelian-scheme bridge has a rational Chow-motive realization

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, line4; MPL_14_002-044_14_scan009.tex, line10; cote14 scans003,009. Quotes: “M”; \(i_1\bar i_1=j\).
**Kind:** unpursued implication with verified later theorem. **Context M24 plus Fourier, Lefschetz, Künnemann:** CT cote47 scans3–5 gives Fourier, convolution and corrected inversion; cote16 scans15–18 gives the ring construction. **Delta:** adds a published Chow-motive bridge. **RS:** WG2 B16 (§1.2) [unchecked]; the primary result is checked without promoting the whole row. **Primary:** Künnemann1993 pp94–97, Proposition4.3, equation(15), Theorems5.1–5.2.

**Proposed note.** Künnemann constructs the Lefschetz decomposition in relative Chow motives with rational coefficients for an abelian scheme \(A/S\) of relative dimension \(g\), with \(S\) smooth and quasi-projective over a field and a chosen symmetric relatively ample class defining \(L\). Theorem5.2 gives, for \(0\leq i\leq g\), the correspondence isomorphism \(L^{g-i}:R^i(A/S)\xrightarrow{\sim}R^{2g-i}(A/S)(g-i)\) and inverse \(\Lambda^{g-i}\), with Fourier comparison on pp96–97. This proves a positive bridge from rational Chow correspondences to the Lefschetz decomposition in that setting, retaining equation(15)'s normalization rather than assigning it to cote16's integral exterior model without calculation.

### M25 — Exact conversion from unit-step lowering to \(\mathfrak{sl}_2\)

**Frozen evidence:** MPL_14_002-044_14_scan009.tex, line10; MPL_14_002-044_14_scan013.tex, line8; cote14 scans009,013. Quote: \(i_1\bar i_1=j\).
**Kind:** own calculation resolving a prerequisite of the requested bridge. **Context M25:** sl_2, sl₂, Lambda, contraction, normalis; CT cote16 scans10,13–17, unfinished definition and exterior model; CN R2,S2–S3. **Delta:** supplies exact normalization, without reusing the conditional integral statement in CN. **RS:** WG2 §2.3 #2, WG2 §2.3 #3, WG2 S28 (§1.7) [unchecked]. **Confidence:** high; the brackets are calculated on the given basis. **Primary comparison:** Künnemann1993 p95 equation(15).

**Proposed note.** On the primitive string \(v_a=L^av\), \(0\leq a\leq r=d-p\), with \(v\) of degree \(p\), unit-step lowering is \(\Lambda_{\rm step}v_a=v_{a-1}\), while the \(\mathfrak{sl}_2\) operators are \(ev_a=v_{a+1}\), \(fv_a=a(r-a+1)v_{a-1}\), and \(hv_a=(2a-r)v_a\), with zero at the appropriate endpoints. Direct subtraction gives \([h,e]=2e\), \([h,f]=-2f\), \([e,f]=h\), hence a homomorphism \(U(\mathfrak{sl}_2)\to\operatorname{End}_{\mathbb Q}(\bigoplus_a\mathbb Qv_a)\). For the projector \(P_a\) onto \(\mathbb Qv_a\), the exact conversion is \(f=\sum_{a=1}^r a(r-a+1)\Lambda_{\rm step}P_a\) and \(\Lambda_{\rm step}=\sum_{a=1}^r[a(r-a+1)]^{-1}fP_a\), exposing the rational denominators to track before identifying the integral algebras. On \(V_n=\bigoplus_{r=0}^n\operatorname{Sym}^r\mathbb Q^2\), the Casimir \(C=h^2+2h+4fe\) has scalar \(r(r+2)\); polynomial interpolation in \(C,h\) isolates every string and weight, and the operators \(e^aP_0f^b\) give nonzero scalar multiples of all matrix units, proving \(\operatorname{im}U(\mathfrak{sl}_2)=\prod_{r=0}^n\operatorname{Mat}_{r+1}(\mathbb Q)\) in this explicit rational model.

### M26 — The grading and Cartan operator differ by a displayed scalar

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, line14; MPL_14_002-044_14_scan009.tex, line10; MPL_14_002-044_14_scan013.tex, line8; cote14 scans003,009,013. Quotes: “graduations positives”; \(\langle i,\varepsilon\rangle=2\).
**Kind:** own calculation answering the weight-cocharacter question. **Context M26:** grading, graduation, weight cocharacter, sl₂; CT cote16 scans3,16–17; CN S3,R3. **Delta:** supplies the exact relation between the actions. **RS:** WG2 §2.4 #3 [unchecked]. **Confidence:** high; degreewise calculation. **Primary convention:** Deligne–Milne §5.1 uses the Tate object \(\mathbb Q(1)\), whereas M11 uses \(\mathbb L=\mathbb Q(-1)\).

**Proposed note.** With \(w(t)|H^r=t^r\mathrm{id}\) on the total realization of a smooth projective variety of dimension \(d\), one has \(d\rho(w)|H^r=r\mathrm{id}\), \(h|H^r=(r-d)\mathrm{id}\), and therefore \(d\rho(w)=h+d\,\mathrm{id}\). On this chosen realization, the group-level formula is \(\rho(w(t))=t^d\lambda_{\mathfrak{sl}_2}(t)\), where \(\lambda_{\mathfrak{sl}_2}(t)|H^r=t^{r-d}\mathrm{id}\). For \(\mathbb P^1\), the degree-\(0,2\) matrices give exactly \(\operatorname{diag}(0,2)=\operatorname{diag}(-1,1)+I\), with \(\varepsilon\circ w=t^2\) as in scan009.

### M27 — Naturality gives the precise motivic-group action on Lefschetz operators

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, lines4,14; MPL_14_002-044_14_scan011.tex, lines13,17; cote14 scans003,011. Quotes: “Λ(-1)”; “indép. du foncteur”.
**Kind:** own calculation answering the requested \(\mathfrak{sl}_2\)-group comparison. **Context M27:** sl₂, motivic Galois, grading, projecteur; CT cote16 scans16–17 requires preserving \(\pi_r\); CN R3 displays their role. **Delta:** supplies commutation and Tate-character equations plus a completely specified example. **RS:** WG2 §2.4 #3 [unchecked]. **Confidence:** high; naturality and explicit matrices.

**Proposed note.** In the pure Nori category of M28a, a tensor automorphism \(g\) respects \(\pi_r\) and \(L:h^r(X)\otimes\mathbb L\to h^{r+2}(X)\), so \(g\pi_r=\pi_rg\) and \(g_{r+2}L=L(g_r\otimes\chi_{\mathbb L}(g))\), hence after choosing a basis of \(\omega(\mathbb L)\), \(gLg^{-1}=\chi_{\mathbb L}(g)L\), \(gfg^{-1}=\chi_{\mathbb L}(g)^{-1}f\), and \(ghg^{-1}=h\). Thus \(\ker\chi_{\mathbb L}\) commutes with the Lefschetz \(\mathfrak{sl}_2\), and the full group normalizes its image by the displayed character action, realized on \(\mathbb P^1\) by \(\rho(z)=\operatorname{diag}(1,z)\). The category generated by \(h(\mathbb P^1)=\mathbb Q(0)\oplus\mathbb Q(-1)\) has group \(\mathbb G_m\), whereas \(e=E_{21}\), \(f=E_{12}\), \(h=\operatorname{diag}(-1,1)\) give a nonzero \(\mathfrak{sl}_2\)-action, and every Lie homomorphism \(\mathfrak{sl}_2\to\operatorname{Lie}\mathbb G_m\) is zero because \([\mathfrak{sl}_2,\mathfrak{sl}_2]=\mathfrak{sl}_2\) and the target is abelian. This explicit example rules out a universal inclusion inducing the given Lefschetz action on each realization, while retaining the positive relation through grading, naturality and the Tate-character normalizer action.

### M28 — Nori–Ayoub comparison is an actual group isomorphism

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, line4; MPL_14_002-044_14_scan011.tex, lines13–15; cote14 scans003,011. Quotes: “M”; “foncteur qui la réalise”.
**Kind:** verified later comparison answering the S15 request. **Context M28:** Nori, Ayoub, S15, Tannak; README lines25–26; CT cote16 scan49; CN S15. **Delta:** adds the precise unconditional comparison. **RS:** WG2 §2.3 #7 and WG2 §2.4 #3 [unchecked]. **Primary:** Choudhury–Gallauer Alves de Souza2017 §2.2 and Theorem9.1, pp6–7,41; field \(k\) of characteristic0 with fixed embedding in \(\mathbb C\), coefficient PID \(\Lambda\).

**Proposed note.** In that setting, Choudhury–Gallauer construct inverse Hopf-algebra maps \(\varphi_A:H_A\to H_N\) and \(\varphi_N:H_N\to H_A\), hence the canonical isomorphism \(G_N\xrightarrow{\sim}G_A\) in the opposite direction. Here \(H_A\) is the degree-zero Hopf algebra from Ayoub's Betti construction, and the passage from effective Nori diagrams to the group inverts the Tate element. This supplies the actual group comparison relevant to scan011, without identifying the unspecified manuscript \(M\), settling \(I(G)\)-injectivity or effectivity-surjectivity, or proving that every Lefschetz inverse is represented by an algebraic cycle.

### M28a — Pure Nori motives are related by a proved equivalence to motivated cycles

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, lines4,14,18–19; cote14 scan003. Quotes: “graduations”; “poids”.
**Kind:** verified later comparison. **Context M28 plus André, pure, motivated, semi.simple:** CT cote16 scan49; CN S15–S16, no proof of this equivalence there. **Delta:** adds the actual functor between correspondence and pure Nori constructions. **RS:** WG2 §2.3 #7 [unchecked]. **Primary:** Arapura2013 Theorems6.3.3,6.3.5,6.4.1, proof steps1–7, arXivpp57–61; HMS2025 Theorem10.2.8. Rational coefficients and the fixed Betti embedding are retained.

**Proposed note.** Arapura's Theorem6.4.1 gives an equivalence \(\iota:\mathcal M_A\to\mathcal M_{\rm pure}\), sending \(h_A^i(X)\) to \(h_N^i(X)\) and commuting with Betti realization, with inverse supplied by the weight-graded construction. Its proof sends motivated correspondences to Nori morphisms through \(\ast,\cup,p_*\), then identifies simple objects and their Hom spaces; it does not replace the motivated-cycle space by the algebraic-cycle space. Inclusion of pure objects and weight grading give the group sequence \(1\to U\to G_N\to G_{\rm pure}\to1\), with \(U\) pro-unipotent and \(G_{\rm pure}\) pro-reductive (HMS Theorem10.2.8), specifying where semisimplicity is realized.

### M29 — The numerical quotient and cycle-class factorization

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, line4; MPL_14_002-044_14_scan011.tex, line13; cote14 scans003,011. Quote: “catégorie de motifs M”.
**Kind:** unpursued implication with verified theorem and exact map. **Context M29:** Jannsen, numéri, numerical, semi.simple, S16; CT cote16 scan49 requests algebraic left inverses and semisimplicity; CN S15–S16. **Delta:** restates the verified numerical theorem and adds a factorization test. **RS:** WG2 §2.3 #7 [unchecked], no promotion of the whole row. **Primary:** Jannsen1992 Theorem1, Corollaries1–2, pp448–451. **Confidence:** high for the quotient and dual-number calculation.

**Proposed note.** Jannsen's Theorem1 proves semisimplicity of numerical motives with characteristic-zero coefficients, and the relevant map is \(q:\mathcal M_{\rm hom}\to\mathcal M_{\rm num}\), induced by quotienting cycle correspondences and sending \((X,p,m)\) to \((X,q(p),m)\). A cycle action \(c:A_{\rm hom}\to\operatorname{End}H\) factors through \(q\) exactly when \(\ker q\subseteq\ker c\), so the numerical theorem alone supplies neither that factorization nor the algebraic inverse acting on the given \(H\) demanded in cote16 scan49. The quotient \(\mathbb Q[u]/(u^2)\to\mathbb Q\), with its faithful regular representation, has semisimple target but a nonzero kernel acting nontrivially, proving the algebraic gap in the inference without claiming a geometric counterexample. Jannsen's Corollary1 gives its nilpotent-radical conclusion under the stated Künneth-projector hypothesis, and Corollary2 has its own grading and commutativity hypotheses for the Tannakian conclusion.

### M29a — A concrete mixed extension tests the scope of semisimplicity

**Frozen evidence:** MPL_14_002-044_14_scan003.tex, lines4,14; MPL_14_002-044_14_scan011.tex, line15; cote14 scans003,011. Quotes: “motifs effectifs”; “De-Rham”.
**Kind:** own calculation using a published motivic example. **Context M29 plus Kummer, extension, mixed, semisimple:** CT cote54 scan3 has a different degree-one extension; cote16 scan49 asks semisimplicity; CN S15. **Delta:** adds a mixed Nori test linked by realization. **RS:** WG2 §2.3 #7 [unchecked]; no row asserts full mixed semisimplicity. **Primary:** Huber2018 §7.2; HMS §14.1. **Confidence:** high for the period/Hodge calculation.

**Proposed note.** The relative motive \(H^1(\mathbb G_m,\{1,2\})\) gives \(0\to\mathbb Q(0)\to M\to\mathbb Q(-1)\to0\), with periods \(1,\log2,2\pi i\). Twisting by \(\mathbb Q(1)\) identifies its Hodge extension class with \(\log2\) in \(\mathbb C/(2\pi i)\mathbb Q\), which is nonzero because \(\log2\) is nonzero real and every nonzero rational multiple of \(2\pi i\) is imaginary. Realization would send a motivic splitting to a Hodge splitting, so this Nori extension is nonsplit, locating concretely why the semisimple pure quotient of \(G_N\) does not make all its mixed motives semisimple.

### M30 — The exact sequence over \(\mathbb Q\): later theorem and bounded absence

**Frozen evidence:** MPL_14_002-044_14_scan007.tex, line21; MPL_14_002-044_14_scan013.tex, line6; MPL_14_002-044_14_scan015.tex, lines5–7; cote14 scans007,013,015. Quote: “\(\pi_1(\mathbb Q,\mathbb C)\) opère”.
**Kind:** reading question with bounded absence and later theorem. **Context M30:** Galois, Gal(, exact, Γ_Q, extension; README lines16–18 assigns the proposed sequence to cotes13/15, neither supplied. **Delta:** actual cote14 gives an action without the requested sequence. **RS:** WG2 §2.4 #3 [unchecked]; no matching proved row. **Primary:** HMS2025 Theorem9.1.16 and corrected §9.5; Kahn2025 Theorem5.10, Proposition10.1, Theorem10.2, Remark10.3. All 40 frozen pages were searched as recorded below.

**Proposed note.** The supplied cote14 pages state a \(\Gamma_{\mathbb Q}\)-action on torus/cocharacter data, but contain no exact sequence of motivic Galois groups. Writing \(G_N(k)\) for the affine \(\mathbb Q\)-group scheme of rational Nori motives over \(k\), HMS Theorem9.1.16 gives \(1\to G_N(\overline{\mathbb Q})\to G_N(\mathbb Q)\to\Gamma_{\mathbb Q}\to1\), with the left arrow induced contravariantly by base change and the right by inclusion of Artin motives, interpreting \(\Gamma_{\mathbb Q}\) as a proconstant group scheme. Its corrected proof addresses middle exactness and Artin subquotients; Kahn Theorem5.10 and §10 supply a separate descent proof, with \(G_N(\overline{\mathbb Q})=\varprojlim_K\operatorname{Aut}^{\otimes}(\omega_K)\) over finite Galois extensions. HMS Remark9.5.7 in the July2025 annotated edition still lists connectedness of \(G_N(\overline{\mathbb Q})\) as open, so the proved kernel sequence does not identify this kernel with the identity component.

### M31 — The period torsor and evaluation map

**Frozen evidence:** MPL_14_002-044_14_scan011.tex, line15; MPL_14_002-044_14_scan013.tex, line2; cote14 scans011,013. Quote: “tordant pr un torseur … De-Rham”.
**Kind:** bounded reading conclusion; later comparison. **Context M31:** period, périod, torseur, de.Rham; README lines17–18 presents the conjecture's location as a planning guess; no cotes12–13 witness supplied. **Delta:** adds exact torsor/evaluation maps without assigning the later conjecture to this fragment. **RS:** WG2 §2.4 #3 [unchecked]; no period-conjecture row. **Primary:** HMS2025 Theorem13.1.4, Definition13.1.9, Conjectures13.2.1,13.2.5. All-page period-word search returned no hit.

**Proposed note.** The torsor/de Rham suggestion on scan011 concerns changing realizations, and these supplied pages contain no written period-conjecture statement. HMS Theorem13.1.4 identifies the formal-period spectrum with \(\operatorname{Isom}^{\otimes}(\omega_{\rm dR},\omega_B\otimes k)\), while the comparison point \(\mathrm{per}\) gives \(\mathrm{ev}:\mathcal O(\operatorname{Isom}^{\otimes})\to\mathbb C\). For algebraic \(k/\mathbb Q\), Conjecture13.2.1 asks for zero kernel of this evaluation, and Conjecture13.2.5 gives the corresponding formulation for the tensor category generated by one motive. These maps relate the manuscript suggestion to the later formulation without making torsor existence a proof of injectivity or inventing an absent assertion in cotes12–13.

## Primary-source evidence ledger

Only primary author texts, published articles, or corrected author versions are used below. Retrieval references are provided for the root editor to reopen before citing. The note bodies keep the source paraphrases short; their explicitly displayed elementary calculations are independent computations.

| Primary source | Passages actually read | URL / retrieval references |
|---|---|---|
| Deligne, P., & Milne, J. S. (1982; corrected author version2012). Tannakian Categories. | Theorem2.11; Proposition2.23; Theorem3.2; §5.1; Proposition5.5; Proposition4.23/Lemma4.24; Propositions5.18–5.19; Proposition6.23. Weight-sign convention checked in the local text. | https://www.jmilne.org/math/xnotes/tc2012.pdf ; turn16view0, turn18view0–turn18view5. Author-version page https://www.jmilne.org/math/xnotes/tc.html (turn14search1). Root has used additional short paraphrases from this work. |
| Jannsen, U. (1992). Motives, numerical equivalence, and semi-simplicity. Inventiones Mathematicae107,447–452. | All six pages; initial Hom/composition definition; Theorem1; Corollaries1–2; Remark3. | https://epub.uni-regensburg.de/26642/1/jannsen10.pdf (turn27view2); repository record turn25search2. |
| Künnemann, K. (1993). A Lefschetz decomposition for Chow motives of abelian schemes. Inventiones Mathematicae113,85–102. | Printed pp85,94–99 visually read; Proposition4.3; equation(15); Theorems5.1–5.2; Fourier comparison on pp96–97. | https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0011.pdf . turn16view3 is metadata only; actual evidence is the printed primary PDF, rendered locally. |
| Choudhury, U., & Gallauer Alves de Souza, M. (2017). An isomorphism of motivic Galois groups. | arXiv1410.6104v3,18May2017; introduction pp1–4; §2.2 pp6–7; Theorem2.3; Theorem9.1 p41. | https://arxiv.org/pdf/1410.6104 (turn16view1, turn14academia7, turn25search3); https://doi.org/10.1016/j.aim.2017.04.006 . |
| Arapura, D. (2013). An abelian category of motivic sheaves. Advances in Mathematics233,135–195. | arXiv0801.0261v4; Theorems6.3.3,6.3.5,6.4.1; proof steps1–7, arXivpp57–61. | https://arxiv.org/pdf/0801.0261 (turn58view0); https://doi.org/10.1016/j.aim.2012.10.004 . |
| Huber, A., & Müller-Stach, S. (2017; annotated1July2025). Periods and Nori Motives. | Theorem9.1.16 p213; corrected §9.5 pp236–239, including corrections dated2024-02-10 and2025-06-26; Remark9.5.7; Theorems10.2.7–10.2.8; Theorem13.1.4 pp284–285; Definition13.1.9 p286; Conjectures13.2.1,13.2.5 pp288–289; §14.1. Pagination is that of the annotated PDF. | https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-errata/buch-errata.pdf (turn56view0); author errata page https://home.mathematik.uni-freiburg.de/arithgeom/preprints/buch-errata/buch.html (turn55view0). The2016 draft first consulted was superseded for numbering and proof checks. |
| Huber, A. (2018). Galois theory of periods. | Introduction; Conjecture3.3; §4.4 and Proposition4.11; §4.5; §7.2. | https://home.mathematik.uni-freiburg.de/arithgeom/preprints/huber-galois.pdf (turn48view0). |
| Kahn, B. (2025). Galois descent for motivic theories. Theory and Applications of Categories44(20),588–616. | §5.1–5.10, especially pp605–606; Proposition10.1, Theorem10.2, Remark10.3 pp611–612; adjunction and base-change proof read. | https://webusers.imj-prg.fr/~bruno.kahn/preprints/stacks-TAC.pdf (turn68view0); journal record https://tac.mta.ca/tac/volumes/44/20/44-20abs.html (turn67search0, revised7July2025); https://arxiv.org/abs/2312.01825 (turn67academia7). |

### Source-sensitive checks for the editor

- The connectedness statement in M30 is expressly qualified by the July2025 annotated HMS source. No literature-wide absence claim for every later date is made.
- The Nori exact sequence was checked in the corrected HMS proof and separately in Kahn's proof, rather than only in an old theorem statement.
- Deligne–Milne uses \(\mathbb Q(1)\); M11 and the manuscript use the effective \(\mathbb Q(-1)\) character. Their inversion is explicitly displayed.
- Künnemann's equation(15) was read in the actual printed page image; no normalization was imported into cote16's frozen text.
- Arapura's proof was read through step7; its later Hodge conjecture is not used as a theorem.
- Period-torsor orientation: M31 follows the HMS proof, \(\operatorname{Isom}^{\otimes}(\omega_{\rm dR},\omega_B\otimes k)\). Huber2018 §4.4 prints the opposite direction; the exact comparison is \(u\mapsto u^{-1}\), exchanging the left/right actions, so its convention must not be silently substituted.
- The Nori–Ayoub comparison is the actual Hopf-algebra theorem. No unrestricted equivalence of triangulated motives with a derived Nori category, motivic t-structure, or proof of every standard conjecture is inferred from it.

## Supplementary searches and bounded negative findings

1. The all-page frozen search was:
   rg -n -i 'périod|period|torseur|galois|suite exacte|exact sequence|groupe fondamental|pi_1|gal\(' MPL_14_002-044_work/pages

   Hits: Galois-action passages on007,009,013,015; the torsor suggestion on011; and an unrelated finite-presentation typescript “exact sequence” on010 line11. There were no period-word hits and no motivic Galois exact sequence. This is a bounded result about these 40 frozen files, supported by reading the complete effectivity fragment, not an assertion about absent cotes12–13.

2. The supplementary context search for Kunnemann, Künnemann, S15, S16, S3, R2 in CN found R2,S3,S15–S16 and later height-pairing references. The2001 height-pairing paper is not substituted for the1993 Lefschetz article.

3. CT cote47 scans3–5 was read around the Fourier/convolution calculation and corrected inversion statement, alongside cote16 scans15–18. These support M24a's context link; no new proof of every derived-functor assertion in47 is claimed.

4. Primary web queries included:
   - Deligne Milne Tannakian Categories 5.18 6.23
   - Jannsen motives numerical equivalence semisimplicity1992
   - Choudhury Gallauer isomorphism motivic Galois groups9.1
   - Kunnemann Lefschetz decomposition Chow motives abelian schemes1993
   - Huber Muller Stach Nori exact sequence9.1.16 errata
   - Arapura abelian category motivic sheaves6.4.1
   - Galois descent for motivic theories Kahn2025 arxiv

5. The Kahn journal PDF returned503/502; the author-hosted published PDF was obtained and its proof read. A Jossen download failed, and no theorem from that failed download is used.

## Handoff

There are 34 proposed notes: M01–M31, with additional M24a,M28a,M29a. The new mathematical bridges are the explicit normalization, scalar-shift and naturality maps in M25–M27; the actual comparison functors in M28–M29a; and the bounded manuscript absence plus verified group/torsor maps in M30–M31. The torus examples isolate particular displayed data and do not refute the unseen four-structure package. No existing RS status has been promoted, no absent cote12–13 passage has been invented, and no frozen source reading has been repaired.
