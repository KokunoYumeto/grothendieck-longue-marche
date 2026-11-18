## F. S20: Gauss–Manin, Cartier, uniformizing equations, and p-curvature

### F01 — The uniformizing-equation strand is now explicit

**File/location:** cote 93, scans 114–115 and 126–131. **Kind:** unpursued implication.

Scan 114 poses an “équation alg. différentielle,” scan 115 identifies its solutions with uniformizing functions, and scans 126–131 construct the canonical projective object from universal covers. This materially strengthens earlier P01–P04, where scan 036 supplied an isolated Schwarzian calculation without identifying the global object. The pages support the projective/uniformization part of S20 directly, while F09 supplies an external Gauss–Manin comparison for one of the classical examples.

**Context:** Adds explicit global structure to MPL_93_002-046 P01, P03, P04, and P09; supports H-VIIIb and H-Xa/H-Xb rather than deriving the connection from the catalogue title.
**Context query:** uniformis|équation.*diff|projective|P01|P04|S20
**Check:** used and rechecked in this run || Compared the explicit uniformization passages with the earlier package and the supplied planning hypothesis.

### F02 — Frobenius rigidity is present, a p-curvature computation is not

**File/location:** cote 93, scans 121–124, “Frobenius” on scan 121. **Kind:** unpursued implication.

The manuscript explicitly introduces Frobenius and changes the constant algebra and truncation level in small characteristic. These are substantive links between projective geometry, divided derivatives, and positive characteristic, but the pages do not calculate \(\nabla_D^p-\nabla_{D^{[p]}}\) for a specified linear connection. The local rigidity result checked in D01–D14 should therefore not be relabeled as zero or nilpotent p-curvature.

**Context:** Bears on H-FIND and on MPL_93_002-046 P06, E26, and P09; adds evidence for one strand of S20 while preserving their distinction between different characteristic-p constructions.
**Context query:** Frobenius|Cartier|courbure|p-curvature|E26|nilpot
**Check:** used and rechecked in this run || Compared the actual Hasse/Frobenius formulas with the definition of p-curvature; no such calculation appears in the frozen range.

### F03 — Cartier descent uses zero p-curvature

**File/location:** cote 93, scans 121–124, proposed comparison prompted by the Frobenius argument. **Kind:** own idea. **Confidence:** high for the theorem's distinction; no application to an unidentified connection.

For a smooth morphism in characteristic p, Cartier descent identifies sheaves on the relative Frobenius twist with integrable connections of zero p-curvature [B4, Theorem 5.1]. The Frobenius invariance of a projective expression alone does not verify that condition for a linear connection. This is the precise distinction to preserve when relating the manuscript to a Cartier operation on forms or to the earlier Hasse calculations.

**Context:** Rechecks the distinction in MPL_93_002-046 P06; E26 and RESULTS_STATE's MPL_5+6_001-037, cote 6 scan 007 item 10, remain first-pass leads rather than established comparison theorems.
**Context query:** Cartier|courbure|p-curvature|sans torsion|P06|E26
**Check:** used and rechecked in this run || Read Katz 1970 Theorem5.1 and compared its zero-p-curvature hypothesis with the manuscript's scalar/projective statements.

### F04 — Gauss–Manin nilpotence needs an actual geometric realization

**File/location:** cote 93, scans 114 and 121–124, proposed arithmetic bridge. **Kind:** own idea. **Confidence:** high for the source statement; no confidence claim for an absent realization.

Katz's global nilpotence theorem assumes a smooth connected base over a finitely generated integral \(\mathbb Z\)-algebra of characteristic-zero fraction field, a proper smooth family, and locally free Hodge and de Rham cohomology [B4, §§9.0–9.1 and Theorem 10.0]. Its conjugate-piece comparison separately uses the stated base-change or flat-Frobenius hypothesis [B4, Theorem 7.4]. These hypotheses cannot be invoked merely because an equation has algebraic coefficients; F09–F10 give a specific family for which the comparison can actually be made.

**Context:** Refines MPL_93_002-046 P06–P08, C25, and C33; Hua's later section XII discusses Gauss–Manin outside the supplied scan range.
**Context query:** Gauss|cohomolog|de Rham|C25|C33|nilpot
**Check:** used and rechecked in this run || Read the cited Katz statements and hypotheses; no independent proof of the paper or application to a specified manuscript family claimed.

### F05 — The earlier arithmetic proposals keep their first-pass status

**File/location:** cote 93, present scans 092–134 compared with prior scans 023, 036, and 044–046. **Kind:** unpursued implication.

P07's proposed Kodaira–Spencer comparison and P08/C25/C33's cohomology and universal-extension route are concrete leads, but this sequence supplies no comparison map realizing them. P07's pointer to Katz 1972, Theorem 3.2, was not independently source-checked here because the accessible retrieval exposed only its cover; it remains a prior pointer. P05's exponential p-curvature calculation was neither repeated nor promoted beyond the earlier return's own “checked” claim.

**Context:** Carries MPL_93_002-046 P05, P07, P08, C25, and C33 with their supplied status, as required by RESULTS_STATE; differs from treating their presence in the context as proof.
**Context query:** Kodaira|universelle|P05|P07|P08|C25|C33
**Check:** carried as background without fault found || Prior proposed bridges retained without re-proving their settled-looking claims; Katz1972 theorem text was not available in the source retrieval.

### F06 — The canonical uniformizing choice does not vary holomorphically in general

**File/location:** cote 93, scan 115, “Sont-elles algébriques ?” and analytic parameter dependence. **Kind:** self-flagged.

For compact curves of genus at least 2 over Teichmüller space, the Fuchsian uniformizing section is real analytic but not holomorphic [B5; B6]. Consequently a general claim that the fiberwise algebraic uniformizing connections form an algebraic section in varying moduli is false: algebraicity would imply holomorphicity. This confirms the substantive warning in Hua's reading, while leaving constant or specially restricted situations separate and leaving the manuscript's question unchanged.

**Context:** Rechecks H-VIIIb, p. 114/scan 115, against primary sources; bears on S20 and MPL_93_002-046 P04/P09, and goes beyond the generic fiberwise counterexample B16.
**Context query:** famille|holomorphe|Zograf|Takht|Weil|uniformisation
**Check:** used and rechecked in this run || Read McMullen's explicit statement and Loustau's maximal-totally-real explanation; general algebraic-moduli inference refuted, restricted statement F06.fixed_or_special.

### F07 — A concrete comparison test uses the second fundamental form

**File/location:** cote 93, scans 092, 109, and 114, linked to earlier cohomological material. **Kind:** own idea. **Confidence:** high for the conditional construction; medium as a direction for identifying what Grothendieck intended.

Given a geometric rank-two flat bundle \(E\) on a curve and a line \(L\subset E\), the map \(L\to(E/L)\otimes\omega\) induced by the connection is the exact transversality test for the associated projective section. If it is an isomorphism, the projectivized connection and section give the same kind of object described here; comparison with the canonical uniformizing object still requires matching the developing map and monodromy. Searching cotes 159 and 64 for that geometric bundle, its filtration, the second fundamental form, and the normalized equation would test S20 more decisively than shared terminology.

**Context:** Connects H-VIIa/H-VIIIb to MPL_93_002-046 P04, P07, P08, and C25/C33 without assuming the missing family; no such identification is established in the supplied context.
**Context query:** transversal|Kodaira|filtration|Gauss|C25|C33
**Check:** targeted proof check || Projectivizing a flat rank-two bundle identifies the section derivative with its second fundamental form; the additional uniformizing comparison is explicitly left open.

### F08 — S20 receives partial support, with a precise remaining gap

**File/location:** cote 93, package-wide, especially scans 114–115 and 121–134. **Kind:** own idea. **Confidence:** high about the evidence supplied in this run.

The frozen range contains explicit uniformization and Frobenius constructions, but no named Gauss–Manin, Cartier, or Picard–Fuchs construction and no p-curvature computation; this is a limit on the supplied evidence, not a proof that an implicit connection is impossible. Hua's whole-cote reading places the missing named topics in later sections XI–XXI, which cannot be imported as observations from these 42 images. F09–F10 supply one concrete mathematical bridge, but cotes 159 and 64 were not supplied, so a general or historical identification of all these constructions remains unconfirmed.

**Context:** Adds a qualified package verdict to README S20 and MPL_93_002-046 P09; agrees with RESULTS_STATE's statement that no directly matching settled result is available.
**Context query:** 159|64|S20|Gauss|Cartier|Picard|courbure
**Check:** used and rechecked in this run || Full-range textual/content comparison and full Hua-context map establish the evidence boundary; no absent cote or later scan is claimed to have been read as an image.

### F09 — The three-puncture example has a concrete Legendre realization

**File/location:** cote 93, scan 115, \(\mathbb P^1\) minus three points; comparison with scan 114's equation. **Kind:** own idea. **Confidence:** high, by an exact relative-differential certificate and coefficient identity; no novelty claim.

For the Legendre family \(y^2=x(x-1)(x-z)\), the periods of \(dx/y\) satisfy \(z(1-z)\Pi''+(1-2z)\Pi'-\Pi/4=0\), as verified by the exact differential identity in the accompanying report and confirmed by [B13]. Removing the first-derivative term gives the projective coefficient \(2P'+P^2-4Q=-(z^2-z+1)/(z^2(z-1)^2)\), exactly B18's uniformizing coefficient. This supplies an actual Gauss–Manin/Picard–Fuchs realization for that classical example, rather than an inference from a Schwarzian formula alone, but does not identify a family explicitly named on these manuscript pages.

**Context:** Adds a realized example to MPL_93_002-046 P04/P08/P09 and S20, beyond H-VIIIb's question on p. 114/scan 115; the same comparison also corrects H-Xb's later restricted-zero-connection wording.
**Context query:** Legendre|Picard|elliptique|trois points|P08|P09
**Check:** computation or formal certificate || legendre_certificate.txt checks L(dx/y)=d_x[y/(2(x-z)²)] and the exact normalized-coefficient identity; Harnad's period equation was independently opened and read.

### F10 — The geometric example permits a nilpotence conclusion, not a zero-curvature inference

**File/location:** cote 93, scan 115's example, linked to scans 121–124 only as a proposed arithmetic comparison. **Kind:** own idea. **Confidence:** high as an application to the specified smooth proper family, not as a manuscript attribution.

The projective Legendre family extends as a smooth proper elliptic curve over \(\mathbb Z[1/2,z,1/(z(1-z))]\), since its discriminant \(16z^2(1-z)^2\) is invertible there and its Hodge and de Rham bundles are locally free; Katz himself gives this model in [B4, (0.5.2)]. It therefore falls under the Gauss–Manin nilpotence theorem used in F04, giving nilpotent reductions for this identified geometric connection and its projectivization. This is a theorem-based arithmetic consequence for the example, not a computation of its p-curvature and not a claim that it vanishes; no such inference is made for every uniformizing connection.

**Context:** Strengthens the proposed elliptic route in MPL_93_002-046 P08 while respecting P06's zero/nilpotent distinction; does not turn H-FIND's scalar invariant into a p-curvature calculation.
**Context query:** Legendre|elliptique|Gauss|nilpot|P06|P08
**Check:** targeted proof check || Checked the proper elliptic model's discriminant and cohomology hypotheses before applying Katz10.0; no new p-curvature matrix or zero-curvature claim.
