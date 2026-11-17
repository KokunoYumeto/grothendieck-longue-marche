# Research memo: cross-package questions and reused sources

Written after the transcription freeze. All page references below identify the frozen page files; references to earlier package notes remain first-pass leads. This memo never licenses an alteration of the transcription.

### R01 — The arithmetic ground field must be read from this packet

**Kind:** reading question  
**Witness:** 15/002:3–7; 15/003:2–30  
**Brief quotation:** “Cas d'un corps de base fini”; “Catégorie des motifs sur \(\mathbf F_p=k\)”  
**Search terms:** corps de base fini | Artin | Galois | exact sequence  
**Context comparison:** README.md, planning section, asks for an extension by \(\Gamma_{\mathbf Q}\); same_cote_15/MPL_15_195-228+18_002-017_notes.md, M06, distinguishes the separate local extension at 18/006 from that arithmetic question; these pages add a finite-field witness with its own Artin quotient.  
**Results ledger:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §2 [first-pass lead].

The cover and the first mathematical heading identify the present problem as motives over a finite field, and the intrinsic functor \(F^0\) is explicitly tied to \(\widehat{\mathbf Z}\)-representations. Accordingly, the Artin quotient suggested by these pages is the proconstant absolute Galois group of the finite field; none of the 45 supplied pages writes the requested exact sequence over \(\mathbf Q\). This is an evidence limit for this selection, and leaves the unprovided portions of cotes 12–15 available for a further search.

### R02 — A modern exact sequence supplies a comparison, not a missing manuscript line

**Kind:** unpursued implication  
**Witness:** 15/003:11–28; comparison with the question in README.md  
**Brief quotation:** “prolongeant \(F^0\)”  
**Search terms:** Nori | exact sequence | Galois descent | M06  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, M06 and S15, already gives the modern comparison for the local sequence at 18/006; the present pages add the explicit operation of fixing a fibre functor on an Artin-type subcategory.  
**Results ledger:** MPL_15_195-228+18_002-017 M07 and S15: [first-pass leads]; WG2 §2.4 #3 [unchecked plan].

For rational Nori motives with compatible Betti fibre functors, the modern statement is
\[
1\longrightarrow G_{\mathrm N}(\overline{\mathbf Q})
\longrightarrow G_{\mathrm N}(\mathbf Q)
\longrightarrow\underline{\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)}
\longrightarrow1,
\]
with exactness as affine group schemes and a proconstant final term (Kahn, 2025, Theorem 5.10 and §10). The restriction of the fibre functor to Artin motives explains the last arrow, while descent is needed to identify its kernel. Neither a canonical splitting nor identification of that kernel with the identity component follows from the displayed sequence alone, and the finite-field reduction on 15/003 does not provide either assertion over \(\mathbf Q\).

### R03 — The period witness is elsewhere, and an independent published witness exists

**Kind:** unpursued implication  
**Witness:** 12/152: realization paragraph; context witnesses reported at 18/011–013  
**Brief quotation:** “De Rham”; the earlier notes report “Conj. de transcendance forte”  
**Search terms:** period | transcendance | transcenden | De Rham  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, P15–P26, reports the live strong conjecture at 18/011, cancelled normalized draft at 18/012, and live elliptic questions at 18/013; context/MPL_16+47+54+44_transcription.tex, 16/021 and 16/035, has different uses of transcendental cohomology and periods.  
**Results ledger:** MPL_15_195-228+18_002-017 §2 [first-pass lead]; WG2 §2.4 #3 [unchecked plan; no dedicated period-result row].

No explicit period-transcendence conjecture occurs in the present 45 pages: the realization vocabulary on 12/152 supplies a setting rather than a transcendence assertion. The supplied earlier notes locate several explicit formulations on 18/011–013, but those locations are reported leads because their page images are not part of this packet. Independently, Grothendieck's own published de Rham paper discusses conjectural algebraic independence of elliptic periods and quasiperiods, so the README's suggestion that his period conjecture is known only through other people's reports is too restrictive (Grothendieck, 1966, p. 102, note 10).

### R04 — The several period formulations must keep their additional data

**Kind:** reading question  
**Witness:** context 18/011–013 as reported in the earlier notes; current 12/156–157 for duals and Tate twists  
**Brief quotation:** reported “\(g+u\)”; reported “\(\dim G\) (\(4\) ou \(2\)) ?”  
**Search terms:** g+u | normalized | normalis | P15 | P22 | Hodge splitting  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, P15–P26, already separates the additional Hodge-splitting data, the cancelled normalized period matrix, and the full elliptic period question; current 12/156–157 adds explicit twist and dual conventions but no transcendence proof.  
**Results ledger:** MPL_15_195-228+18_002-017 P14 [first-pass lead]; LM1 A.8 [Refuted, run claim]; WG2 §2.4 #3 [unchecked plan].

The earlier \(g+u\) formulation includes additional splitting parameters, whereas its elliptic \(4\)-or-\(2\) question concerns the full period tuple; identifying the two requires a comparison that the present pages do not supply. Removing a Tate determinant changes the normalization, so a cancelled \(\dim G-1\) draft must be compared with its own normalized matrix rather than substituted for the live full-period assertion. The existing LM1 A.8 warning about lost central data remains relevant without being rederived, and cancellation of a draft is not evidence that its author abandoned every associated conjecture.

### R05 — The Tate and anabelian Hom maps have different domains

**Kind:** unpursued implication  
**Witness:** 15/003:30; 15/013: endomorphism and Frobenius paragraphs  
**Brief quotation:** “conj. de Tate et de Tate-Honda”  
**Search terms:** Tate | anabelian | B01 | Hom  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, B01, compares 15/213, 215 and 227; context/MPL_16+47+54+44_transcription.tex, 16/021 and 16/049, supplies the Tate-sheaf and conditional-correspondence background; current 15/013 adds a concrete finite-field endomorphism calculation.  
**Results ledger:** MPL_15_195-228+18_002-017 B01 [first-pass lead]; FLAGGED_149 B9 [Open, run claim].

Tate's finite-field theorem identifies \(\operatorname{Hom}_k(A,B)\otimes\mathbf Z_\ell\) with \(\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)\) for abelian varieties and \(\ell\ne\operatorname{char}k\) (Tate, 1966, main theorem). For hyperbolic curves over a sub-\(p\)-adic field, the corresponding nonlinear reconstruction uses dominant morphisms and continuous open homomorphisms over \(G_k\), modulo geometric inner conjugacy (Mochizuki, 1999, Theorem A). The current reference to Tate–Honda therefore adds substantial linear evidence while supplying neither the prime-to-\(p\) point-recognition step in FLAGGED_149 B9 nor a general reconstruction theorem from cohomology.

### R06 — The packet itself prevents semisimplicity from being read as centrelessness

**Kind:** unpursued implication  
**Witness:** 12/151: semisimplicity paragraph; 12/159:4; 15/003:26  
**Brief quotation:** “algèbres de Riemann”; “un groupe commutatif”  
**Search terms:** semi-simple | semisimplicity | centre | center | B02  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, B02, already records the torus counterexample; context/MPL_16+47+54+44_transcription.tex, 16/049, gives the conditional semisimplicity programme; the current packet juxtaposes that programme with explicitly commutative finite-field bands.  
**Results ledger:** WG2 §2.3 #7 [unchecked plan]; LM1 A.8 [Refuted, run claim]; LM4_SUCCESSOR B.34/B.38 [Open headline claims].

The earlier B02 counterexample already blocks the implication from a semisimple representation category to a trivial group centre; the present commutative \(G\) makes that distinction visible within the manuscript selection itself. In characteristic zero the relevant connected Tannakian condition is pro-reductivity, while slimness of geometric hyperbolic fundamental groups is a separate group-theoretic fact (Deligne & Milne, 1982/2012, Proposition 2.23; Mochizuki, 2004, Lemma 1.3.1). None of this computes the special centralizer left open in LM4_SUCCESSOR B.34/B.38.

### R07 — Polarization does not supply a real fibre functor

**Kind:** unpursued implication  
**Witness:** 12/159–167; 15/011: NB on real fibre functors  
**Brief quotation:** “Formes définies positives sur les motifs”; “n'a pas de foncteur fibre sur \(R\)”  
**Search terms:** polarisation | polarization | real | réel | B03  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, B03, compares 15/203, 215 and 217 with context/MPL_16+47+54+44_transcription.tex, 44/002 and 44/008–009; current 15/011 adds an explicit obstruction to real neutrality.  
**Results ledger:** MPL_15_195-228+18_002-017 B03 [first-pass lead]; WG2 §2.3 #12 and WG H9 [unchecked plans/hunch].

For an algebraic Tannakian category over \(\mathbf R\), polarizability is characterized by a compact real form of the band, which does not itself give a neutralization of the gerbe (Deligne & Milne, 1982/2012, Theorem 4.17). Scan 15/011 is therefore an especially useful test of the proposed bridge: it discusses polarizability and failure of an \(\mathbf R\)-valued fibre functor on the same sheet. The nonlinear real-section comparison instead recovers \(\pi_0(X(\mathbf R))\) for a smooth projective hyperbolic curve from section classes, and does not distinguish all individual real points (Pál, 2011, Theorem 1.3).

### R08 — The normalizer comparison needs the character as well as the weight

**Kind:** unpursued implication  
**Witness:** 15/005 and 15/013: weight and augmentation maps  
**Brief quotation:** “\(\epsilon i=\lambda^2\)”  
**Search terms:** cyclotomic | normalizer | non-Tate | B04 | B05  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, B04–B05, already separates open arithmetic image from cyclotomic conjugation; context/MPL_16+47+54+44_transcription.tex, 16/021 and 16/052, gives Tate and Kummer data; current 15/013 adds the explicit square relation between two characters.  
**Results ledger:** LM6 A.22 [Open, run claim]; LM6 A.50 [Proved, run claim with truncated statement]; MPL_15_195-228+18_002-017 B04 [first-pass lead].

The manuscript's weight map and Tate augmentation must be retained as separately specified morphisms, even though their composite is constrained. In the nonlinear comparison, cyclotomic normalization includes both an open image in the arithmetic Galois group and the prescribed cyclotomic conjugation action; over number fields the non-Tate condition excludes a map \(\mathbf Z_\ell(1)\to T_\ell A\) (Stix, 2012, §5; checked also in the 2008 preprint, §5.2 and Theorem 20). Thus these scans provide a method and a character-normalization warning for LM6 A.22, while the truncated LM6 A.50 entry cannot supply an unstated missing hypothesis.

### R09 — A finite-field Frobenius description does not identify a global object from sparse traces

**Kind:** unpursued implication  
**Witness:** 15/013: centre of the simple endomorphism algebra  
**Brief quotation:** “engendré par \(f_M\)”  
**Search terms:** Frobenius | trace | SECTIONS_OVER_Q D.3 | density  
**Context comparison:** same_cote_15/MPL_15_087-138_notes.md, Frobenius notes FR01 and FR09, studies eigenvalues and realization; notes/RESULTS_STATE.md, SECTIONS_OVER_Q D.3, already records equal positive-density traces with different potential toric ranks; the current statement has the much stronger finite-field/simple-object setting.  
**Results ledger:** SECTIONS_OVER_Q D.3 [Proved, run claim]; MPL_15_087-138 §125 [first-pass lead].

The centre generated by Frobenius on a simple finite-field object concerns its complete endomorphism algebra and the appropriate realization theorem. It does not justify recognizing a number-field motive from equality of traces on only a positive-density set of primes. SECTIONS_OVER_Q D.3 already records the obstruction to that inference, and the present pages neither alter that status nor address the local degeneration data in the recorded example.

### R10 — Fixing a norm line is an additional rigidification

**Kind:** unpursued implication  
**Witness:** 15/022: canonical invertible object; 15/032: canonical section \(\tau\)  
**Brief quotation:** “objet inv. canonique”; “section canonique \(\tau\)”  
**Search terms:** norm-one | frame | split | LM7 C.5 | A.198  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, P32, isolates additional compatibility between splittings at 18/006; notes/RESULTS_STATE.md, LM7 C.5 and SECTIONS_OVER_Q A.198, records different extension and frame problems; the current pages add a determinant/norm-line rigidification, rather than solve either recorded problem.  
**Results ledger:** LM7 C.5 [Proved, run claim]; LM7 C.8 [Refuted, run claim]; SECTIONS_OVER_Q A.198 [Proved, run claim].

The canonical section on 15/032 is conditional on functorial norm trivializations and their transitivity, so its canonicity is part of the data to be justified. This is a useful comparison with the already registered distinction between an extension becoming split after pullback and a specified compatible splitting, and with the norm-one frame obstruction in SECTIONS_OVER_Q A.198. The Deuring construction does not remove those hypotheses or restore the generalized-Jacobian identification already refuted in LM7 C.8.

### R11 — The surface-singularity typescript is identifiable

**Kind:** unpursued implication  
**Witness:** 15/004, 006, 008, 010, 012; internal typed pages 163, 162, 161, 160, 159  
**Brief quotation:** “THEOREM 25.1”; “REMARK 25.3”  
**Search terms:** singular | factorial | Lipman | hypersurface | 25.1  
**Context comparison:** context/MPL_16+47+54+44_transcription.tex, 16/047, proposes a motivic programme for singular varieties; same_cote_15/MPL_15_195-228+18_002-017_notes.md, M05, reports a different smooth-projective construction at 15/223 and 227; these reused pages supply a third, source-identifiable surface-singularity text.  
**Results ledger:** WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 §107/§108 [truncated first-pass leads].

The theorem, proof and small-characteristic tables match §25 of Lipman's published paper on rational singularities, with the current typed pages 159–163 corresponding to material on published pages 269–271 (Lipman, 1969, Theorem 25.1 and Remarks 25.2–25.3). Differences in wording and configuration labels show that the supplied typescript should not be silently replaced by the published version. This identification gives no proof that cote 14 implements the distinct programme at 16/047, and publication in 1969 does not by itself date the typescript or the handwriting on these physical sheets.

### R12 — A source comparison suggests a reading without changing it

**Kind:** reading question  
**Witness:** 15/004:14; frozen array label  
**Brief quotation:** frozen \(\texttt{\backslash unsure\{1-3|l-3\}}\)  
**Search terms:** configuration | singular | Lipman | hypersurface  
**Context comparison:** context/MPL_16+47+54+44_transcription.tex, 16/047, supplies only the broader singular-variety programme; the supplied earlier notes contain no collation of this configuration label; the external publication adds a possible graphical interpretation.  
**Results ledger:** WG2 §2.4 #3 [unchecked plan; no dedicated reading entry].

The frozen first entry of the configuration column is \(\texttt{1-3|l-3}\), while Lipman's published Remark 25.3 labels a configuration \(G_2\) with vertices marked \(1\) and \(3\). This suggests treating the entry as an abbreviated configuration graph rather than an alphabetic word, but the source is a distinct version and cannot settle the ink on its own (Lipman, 1969, p. 271). The transcription and its doubt remain unchanged; this note records only the post-freeze comparison.

### R13 — The reused factoriality proof needs a height-one qualification

**Kind:** own idea  
**Witness:** 12/164:9–18, reused typed Lemma VII.15  
**Brief quotation:** “Let … be a prime ideal”; “a principal ideal”  
**Search terms:** factorial | prime ideal | Brauer | regular  
**Context comparison:** context/MPL_16+47+54+44_transcription.tex, 16/047, concerns singular varieties but supplies no proof of this commutative-algebra lemma; neither same-cote notes file identifies this typed source; current 15/018–020 uses related Brauer/order terminology in a separate handwritten argument.  
**Results ledger:** WG2 §2.4 #3 [unchecked plan, thematic only]; no matching settled commutative-algebra row.

The proof applies the UFD property to an arbitrary prime ideal, although that implication is valid for height-one primes, not all primes. For example, the maximal prime \((x,y)\) of \(k[x,y]_{(x,y)}\) is not principal, as its cotangent space has dimension two; this tests the inference, rather than refutes the lemma's stated conclusion. Restricting the proof to height-one primes and using noetherianity and the semilocal local-freeness argument gives the expected route, but this belongs to research commentary on an unidentified reused source. **Confidence: high**, because the two-generator regular-local example directly exhibits the missing qualification.

### R14 — “Unramified extension” depends on the missing source conventions

**Kind:** reading question  
**Witness:** 12/166:17–26, reused typed Lemma VII.14  
**Brief quotation:** “an unramified extension”; “any finite extension”  
**Search terms:** unramified | étale | Brauer | regular  
**Context comparison:** context/MPL_16+47+54+44_transcription.tex, 54/005–007, concerns different group extensions; no supplied context passage gives the definitions preceding typed Chapter VII; current 15/030 explicitly distinguishes admissible residue-preserving changes from arbitrary étale changes.  
**Results ledger:** WG2 §2.4 #3 [unchecked plan, thematic only]; no matching settled lemma row.

The lemma's conclusion uses finiteness in its displayed proof, and the missing earlier definition may include both finiteness and flatness in “unramified extension.” Under the modern unrestricted meaning of an unramified morphism, regularity does not automatically ascend, so the visible statement cannot be checked without those conventions. The institutional lines on 12/162 identify Radcliffe Institute for Independent Study and Wellesley College but do not identify an author; no authorship is inferred from them.

### R15 — These base-change constructions do not constitute six operations on motives

**Kind:** unpursued implication  
**Witness:** 12/150–154; 15/026–032  
**Brief quotation:** “foncteur … admissible”; “commute aux chgts de base”  
**Search terms:** six operations | six functors | base-change | projection | correspondance  
**Context comparison:** README.md places motives over a base among the planning questions; same_cote_15/MPL_15_195-228+18_002-017_notes.md, A20–A27 and introductory table, treats a broader relative programme; the current pages add pure motives over a field and an order-category base-change formalism with explicit restrictions.  
**Results ledger:** WG2 §3.2 #7 and WG2 §2.4 #3 [unchecked plans]; MPL_15_195-228+18_002-017 M01 [first-pass lead].

The operations actually defined here are correspondences, tensor products, Tate twists, internal-Hom candidates and admissible changes of the coefficient ring in Deuring categories. A six-operation theory would additionally require geometric direct and inverse images, their exceptional versions, and the specified adjunction, projection and base-change compatibilities. Those data are not supplied by these scans, so they contribute concrete pieces of the programme without establishing the broader claim in the planning register.

### R16 — The full period conjecture concerns the period locus itself

**Kind:** unpursued implication  
**Witness:** 12/152: faithful realization paragraph; comparison with reported 18/013  
**Brief quotation:** “fidèles en car. 0”; reported “A-t-on \(H=G\)”  
**Search terms:** period locus | torsor | P22 | P23 | pleinement fidèle  
**Context comparison:** same_cote_15/MPL_15_195-228+18_002-017_notes.md, P22–P23, distinguishes the full transcendence assertion from the group generated by a period locus at 18/013; the present realization paragraph supplies neither assertion and adds no proof of their equivalence.  
**Results ledger:** MPL_15_195-228+18_002-017 M08 and §2 [first-pass leads]; WG2 §2.4 #3 [unchecked plan].

For a smooth projective variety over \(\overline{\mathbf Q}\), the full formulation in Bost and Charles (2016, Conjecture 2.12) identifies the Zariski closure \(Z_X\) of the comparison point with the algebraically defined motivic period torsor \(\Omega_X^{\mathrm{mot}}\). In a corresponding Tannakian formulation this predicts that the field of periods has transcendence degree equal to the dimension of the relevant motivic group. Equality of the smallest torsor generated by the period point with \(\Omega_X^{\mathrm{mot}}\) is a weaker condition than this equality of the actual locus, and faithfulness of the realizations on 12/152 supplies no transcendence assertion.
