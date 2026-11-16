#!/usr/bin/env python3
"""Root-authored research entries; frozen TeX is never modified."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
notes = []
NONE = "No directly corresponding mathematical result entry in R."
PLACE = "WG2 §1.1 #3 (unchecked placement question): additional elliptic/Picard material."
HUA = "Hua, findings register, 62-triples-rigidified-moduli (candidate claim, not an established novelty result)."

def add(i, section, title, scans, position, kind, quote, body, context,
        register=NONE, queries=(), confidence=""):
    notes.append(dict(id=i,section=section,title=title,scans=scans,position=position,
                      kind=kind,quote=quote,body=body,context=context,
                      register=register,queries=list(queries),confidence=confidence))

A = "1. The zero divisor, pole filtration, and Weierstrass coordinates"

add("A01",A,"The divisor convention and the Lie line","004","opening definition and first displays",
    "reading question",
    "“multiples” de D; “faisceau de Lie”.",
    r"""The prose about “multiples” of the zero divisor sits beside a section \(1:\mathcal O_C\to\underline L\), positive pole spaces, and \(s^*\underline L\simeq\operatorname{Lie}(C/S)\), so the working convention behaves as \(\mathcal O_C(D)\), not as the ideal \(\mathcal O_C(-D)\). The normal-bundle identity explains that convention: \(s^*\mathcal O_C(D)=N_{D/C}\simeq s^*T_{C/S}\), whereas invariant differentials give its dual. This is an interpretative consistency question, not a proposed replacement of “multiples” in the frozen text.""",
    "T, cote 54, scan 3, distinguishes the tangent line from invariant differentials; N, D01–D02, already flags variance in universal extensions; cote 62 adds an explicit divisor realization, with a possible sign-convention ambiguity.",
    PLACE, [r"t_A",r"t_B",r"différenti",r"D01",r"Lie"])

add("A02",A,"The cancelled first proposition is restated","004–005","cancelled Proposition 1 and next-page Proposition 1",
    "withdrawn in the same text",
    "“les L^n … sont … plats”; “Les faisceaux … sont coh. plats”.",
    r"""The cancellation on scan 004 is followed on scan 005 by a fuller live proposition giving cohomological flatness, ranks, ampleness, and very ampleness. It therefore records a change of presentation rather than evidence that the author abandoned cohomological flatness itself.""",
    "T, cote 54, scans 4 and 6, and N, D06, concern separate generic-freeness/flattening typescripts; they do not restate this elliptic proposition.",
    NONE, [r"plat",r"faisceau",r"D06"])

add("A03",A,"Riemann–Roch needs the relative base-change step","005","Proposition 1 and proof",
    "unproved claim",
    "“on est ramené au cas”; “pour n=0 elle est connue par ailleurs”.",
    r"""For a degree-\(n\) line bundle on a genus-one fibre, Riemann–Roch and duality give \(h^0=n,h^1=0\) when \(n>0\), \(h^0=0,h^1=-n\) when \(n<0\), and the trivial bundle has \(h^0=h^1=1\). The passage from these fibre calculations to locally free direct images and arbitrary base change uses the relative theorem, with the degree-zero trivial-bundle case separately justified, as the manuscript itself indicates. A modern framework is the perfect complex computing proper flat cohomology and its base changes (Stacks Project, n.d., Tag 0A1G); fibre dimensions alone should not be substituted for that argument over a nonreduced base.""",
    "T, cote 47, scans 7–8, also uses cohomological base change, but for the particular Fourier comparison map; N, F7–F8, leaves its unit-fibre compatibility open; this simpler positive-degree calculation supplies no missing kernel computation.",
    "WG2 §2.4 #4: a related method, not a completed Fourier witness.",
    [r"changement de base",r"compatibilité",r"F7",r"F8",r"Riemann"])

add("A04",A,"The omitted length-two separation argument","005","last paragraph",
    "unproved claim",
    "“un raisonnement connu n'utilisant que RR donne le résultat”.",
    r"""The missing very-ampleness argument is to test every length-two subscheme \(Z\) of a geometric fibre: for \(n\geq3\), the line bundle \(\mathcal O_C(nD)(-Z)\) has positive degree and hence vanishing \(H^1\), making restriction to \(Z\) surjective. This separates distinct points and tangent directions, and relative base change then supplies the relative embedding; the general degree-\(2g+1\) criterion is recorded in Stacks Project (n.d., Tag 0H2V). The uncertain inequality in the proposition remains a reading question even though this argument identifies the mathematical threshold.""",
    "No matching pole-divisor very-ampleness proof occurs in T/N/D; T, cote 44, scan 4, has hyperplane-section statements of a different kind.",
    NONE,[r"très ample",r"RR",r"hyperplan",r"Riemann"])

add("A05",A,"Universal injectivity and the exceptional degree one","006","Proposition 2",
    "unproved claim",
    "“universellement injective”; “n,m … ≠1”.",
    r"""The universal-injectivity assertion requires the cokernels of the inclusions \(\mathcal E_i\subset\mathcal E_j\) to be locally free, obtainable successively from the divisor exact sequences and the degree-positive \(H^1\)-vanishing. Degree one is exceptional because \(\mathcal E_1=\mathcal E_0\), so its associated graded piece is zero rather than a line. The displayed exclusion is mathematically material and should be retained when comparing the multiplication maps with the later intrinsic description.""",
    "T, cote 44, scan 3, also uses associated graded objects but in an adic-completion problem; N, D07, does not supply the elliptic filtration statement.",
    NONE,[r"gradu",r"filtration",r"D07"])

add("A06",A,"What does generation by E₃ mean?","006–007","filtered-algebra paragraph and second corollary",
    "reading question",
    "“E₃ engendre Γ_*(f,L)”.",
    r"""Taken as a statement about the filtered affine algebra of \(C-D\), generators with poles of orders two and three give the intended conclusion by their leading terms and induction on pole order. Taken literally as generation of the homogeneous section ring by its degree-three piece alone, it cannot generate degrees one and two; that ring instead uses a degree-one section together with weighted degree-two and degree-three generators. The surrounding shift between the filtered colimit and the direct sum of its filtered pieces is therefore a substantive notation question, not a license to rewrite the corollary.""",
    "T, cote 44, scan 3, distinguishes a graded direct sum from a product completion; N, D07, makes category restrictions consequential; the present ambiguity is between filtered and homogeneous generation, not that completion issue.",
    NONE,[r"coprod",r"gradu",r"produit",r"D07"])

add("A07",A,"The derivation action is explicitly left to define","007","paragraph before Proposition 3",
    "self-flagged",
    "“[reste à définir]”.",
    r"""The author has not yet defined invariant derivations acting on relative rational functions. A local construction must explain the relevant sheaf of relative meromorphic functions, its localization along the Cartier divisor, and compatibility with base change before passing to the pole filtration. This gap is smaller than, and different from, constructing a restricted Lie algebra or a Dieudonné module.""",
    "T, cote 54, scan 7, explicitly discusses p-Lie algebras; N, D04–D05, requires additional p-operations; cote 62 supplies only the beginning of the ordinary derivation action.",
    PLACE,[r"Lie",r"D04",r"D05",r"radic"])

add("A08",A,"The leading-pole calculation and characteristic p","007–008","Proposition 3 and live corollary",
    "unpursued implication",
    "“ssi p est premier à n”; “est nul”.",
    r"""For a local parameter \(z\), an invariant vector field with \(D(z)\) a unit gives \(D(z^{-n})=-nD(z)z^{-n-1}\), which explains exactly the invertibility and vanishing of the induced leading-term map. The vanishing when \(p\mid n\) concerns this associated graded map, not the whole derivative of every function with pole order \(n\), whose lower-order terms can survive. It consequently does not compute a Hasse invariant, a pth-power operator on the Lie line, or the full \(F,V\)-structure.""",
    "T, cote 54, scan 7, and N, D03–D05, concern Frobenius, Verschiebung, and restricted Lie data; the present calculation adds a concrete characteristic-p example without settling those comparisons.",
    PLACE,[r"Frobenius",r"Verschiebung",r"Lie",r"D03",r"D04"])

add("A09",A,"The two cancelled characteristic-dependent corollaries","008","upper half, before the live characteristic-p corollary",
    "withdrawn in the same text",
    "“Corollaire 1”; “Corollaire 2”.",
    r"""Both upper corollaries are cancelled, including the attempts to recover the graded lines by iterating differentiation in characteristic zero or away from two. The lower divisor-sequence argument gives an intrinsic identification without those characteristic restrictions, so cancellation plausibly reflects replacement by a stronger method; it does not make every formula in the deleted drafts a live assertion. In particular, the doubtful terminal exponent in the cancelled second corollary should not be rehabilitated from the later proof.""",
    "No equivalent cancelled corollaries occur in T/N/D; T, cote 54, scans 3 and 7, instead supplies the Lie/de Rham comparison setting.",
    NONE,[r"caract",r"Lie",r"Corollaire",r"différenti"])

add("A10",A,"The intrinsic graded-line identification and reordering instruction","008","lower exact sequences and margin",
    "self-flagged",
    "“intervertir avec la prop. 2” [first word uncertain].",
    r"""The exact sequence attached to successive powers of the zero divisor identifies the nonzero graded pieces with powers of the normal/Lie line once the relevant \(R^1\) vanishes. This also identifies multiplication intrinsically, which explains the marginal instruction to move the argument before Proposition 2. The boxed subscript and range remain diplomatic uncertainties; the argument is recorded separately rather than being used to resolve their ink after freezing.""",
    "T, cote 54, scan 3, identifies tangent and cotangent terms of a different exact sequence; N, D01–D02, supplies the variance caution; cote 62 adds the pole-filtration realization.",
    PLACE,[r"t_A",r"t_B",r"extension",r"D01",r"D02"])

add("A11",A,"The flex and tangent flag in the cubic embedding","009","opening paragraph and drawing",
    "unproved claim",
    "“tangente d'inflexion”.",
    r"""The section associated to \(\mathcal E_3/\mathcal E_2\) and the line associated to \(\mathcal E_3/\mathcal E_1\) are asserted to be the origin and its flex tangent in the \(|3D|\)-embedding. A direct justification uses the section cutting out \(3D\), so the tangent-line intersection divisor is three times the origin, with the projective-bundle convention tracked consistently. The cancelled seven-coefficient coordinate attempt on the same scan is a separate draft layer.""",
    "No matching flex-flag construction was found in T/N/D; the closest context is T, cote 54, scan 3, for the tangent line, not a cubic embedding.",
    NONE,[r"inflex",r"tangent",r"cubiq",r"projectiv"])

add("A12",A,"A term disappears in homogenization","010","affine φ and homogeneous Φ displays",
    "reading question",
    "“ey” in φ; Φ ends with “dxz²+fz³”.",
    r"""The affine expression includes \(ey\), while the displayed homogeneous cubic lacks the corresponding \(eyz^2\). Setting \(z=1\) in the written \(\Phi\) therefore does not recover the written \(\varphi\) unless an additional condition removes \(e\), which is not stated here. This is a frozen-text consistency issue, not an editorial insertion into the formula.""",
    "Searches of T/N/D found no second version of these coordinate formulas; the standard five-coefficient equation is a literature comparison only (Stacks Project, n.d., Tag 072S).",
    NONE,[r"homog",r"cubiq",r"Weier",r"discriminant"])

add("A13",A,"The dimension of the ambient projective bundle","010–011","end of scan 010 and opening of scan 011",
    "reading question",
    "“P(E₃)≃P³_S”; “P²_S”.",
    r"""The recorded superscript three on scan 010 conflicts with the rank-three bundle \(\mathcal E_3\), the ternary cubic, and the explicit projective plane on scan 011. The mathematical ambient dimension is thus constrained internally, but the transcription retains the glyph read during the visual pass. No contextual formula is being retrofitted into the source.""",
    "No parallel coordinate statement in T/N/D resolves the glyph; T, cote 47, uses projective/abelian geometry for a different purpose.",
    NONE,[r"projectiv",r"rang",r"cubiq"])

add("A14",A,"Why the displayed cubic generates the ideal","010","last paragraph and margin",
    "self-flagged",
    "“préciser ce pt cf. intersections complètes”.",
    r"""The author explicitly asks for the step showing that a cubic relation with a primitive coefficient is the defining equation. Locally one needs the genus-one image to be an effective Cartier cubic, compare the two sections of its invertible ideal in degree three, and show the scalar is a unit by testing every fibre; mere nonzero status in the coefficient ring is insufficient. This supplies a proof obligation, not a proof from the unfinished marginal instruction.""",
    "T, cote 16, scan 52, discusses relative complete intersections in the transitivity of the different; that is a shared tool, not the same ideal-generation statement.",
    NONE,[r"intersection complète",r"diviseur",r"unité"])

add("A15",A,"The discriminant is announced but not written","011","smoothness criterion and dash after the colon",
    "unproved claim",
    "“Ici le discriminant s'explicite : —”.",
    r"""No explicit discriminant follows the announcement, and the later proposition's \(\delta\ne0\) notation must be read against the preceding requirement that \(\delta\) be a unit everywhere. Over a general base a nonzero nonunit can still have a singular fibre; for example a discriminant divisible by a closed-point parameter does not define a smooth family at that point. The coefficient of \(y^3\) must also be a unit for this special flex model: if it vanished in a fibre, the homogeneous equation would acquire the line \(z=0\) as a component.""",
    "T, cote 16, scans 23 and 54, mentions respectively an intersection-lattice discriminant and an algebraic discriminant reference; neither supplies this omitted Weierstrass polynomial.",
    NONE,[r"discriminant",r"unité",r"simple"])

add("A16",A,"The written coordinate-action polynomial changes monomials","012","first polynomial display",
    "reading question",
    "“BXY²”; “CY^{3|2}” [exponent uncertain].",
    r"""The literal \(BXY^2\) differs from the preceding \(bxy\), and the following exponent is already marked uncertain. Such changes affect pole weights and the claimed stability under upper-triangular substitutions, so they cannot be dismissed as harmless relabellings. A future comparison should check the ink again from an independent source image or witness, leaving this frozen return unchanged.""",
    "No matching polynomial or second witness was found in T/N/D; the modern coordinate-change group in Stacks Project (n.d., Tag 072S) is a consistency benchmark, not evidence for a different reading.",
    NONE,[r"polyn",r"triang",r"forme",r"Weier"])

add("A17",A,"Representability with a special basis","011–013","M, the marginal Proposition, and orbit criterion",
    "unproved claim",
    "“courbes elliptiques ‘structurées’”; “représentable par M”.",
    r"""The proposed representing scheme records a cubic together with a special global basis, and its claim requires mutually inverse constructions between that coefficient data and the structured curve. Any isomorphism criterion must preserve the origin, the pole flag, and the normalization of the coefficient of the square term, not just the underlying abstract plane cubic. The later reduction to five coefficients agrees in shape with the modern Weierstrass atlas, but does not by itself verify every displayed action formula on scan 012.""",
    "T, cote 54, scan 3, has an intrinsic universal-extension construction rather than a coordinate atlas; N, D01, cannot certify this representability statement.",
    PLACE,[r"représent",r"universelle",r"base",r"D01"])

add("A18",A,"Descent requires torsors, not only pointwise orbits","013","principal bundle and D-representability paragraph",
    "unpursued implication",
    "“fibré principal”; “simples surjectifs”.",
    r"""The principal bundle of admissible frames explains how an arbitrary elliptic curve acquires coefficient data locally and why global coefficient orbits alone do not classify all curves over every base. A modern object-level formulation keeps the torsor and its equivariant coefficient map, yielding a quotient stack; the familiar Weierstrass version is \([W/H]\) (Stacks Project, n.d., Tag 072S). The historical \(\mathcal D\)-representability assertion should not be silently equated with a fine moduli scheme for unstructured curves.""",
    "T, cote 16, scan 56, records faithfully flat trivialization of finite étale covers; N, 16:56 entries, concerns a simpler descent setting; cote 62 supplies a smooth frame-torsor presentation.",
    PLACE,[r"fidèlement",r"fid.",r"descente",r"représent",r"16:56"])

add("A19",A,"The promised general-genus argument is only a sketch","013","last sentence",
    "unproved claim",
    "“un raisonnement général … pour les courbes de genre g”.",
    r"""The author says that a general argument gives the analogous presentation, but neither the projective parameter space nor the stabilizer and descent conditions are developed here. The final wording is partly uncertain, and a Hilbert-scheme/coordinate-group construction would require its own bounded embedding and flat-family arguments. This is a lead toward a general moduli presentation, not a theorem proved by the elliptic calculation.""",
    "T, cote 44, scan 2, proposes abelian varieties attached to cycle quotients; that is not a presentation of the moduli of curves, and no equivalent general-genus proof occurs in T/N/D.",
    PLACE,[r"genre",r"quotient",r"représent",r"programme"])

add("A20",A,"Weights two and three require no extraction of a root","014","two matrix groups and boxed relation",
    "unpursued implication",
    "“μ²−λ³=0”.",
    r"""For units satisfying \(\mu^2=\lambda^3\), the parameter \(u=\mu/\lambda\) satisfies \(u^2=\lambda\) and \(u^3=\mu\), exactly as the manuscript displays. Thus the diagonal subgroup is already a copy of \(\mathbf G_m\) over the base, without adjoining a square or cube root. This is the intrinsic source of weights two and three in the normalized coordinates.""",
    "T, cote 54, scan 3, supplies the tangent line but not these coordinate weights; T, cote 16, scan 52, concerns genuine Kummer root extraction, a different operation.",
    NONE,[r"Kummer",r"t_A",r"puissance",r"racine"])

add("A21",A,"‘Splitting’ versus a filtered object","014","auxiliary-structure paragraph",
    "reading question",
    "“muni d'un splitting”; upper-triangular matrix.",
    r"""An automorphism preserving a specified direct-sum splitting and its ordered summands would be diagonal on those summands, whereas the displayed group allows three upper-triangular translation entries. The group instead fits a filtration with identified associated graded lines, or a description in which the splitting is allowed to vary. The word is retained literally; the ambiguity concerns the precise moduli problem represented by the group.""",
    "T, cote 54, scan 3, has an extension rather than a canonical splitting; N, D02, already warns against promoting exterior-power duality to a splitting; the present point is a coordinate-structure version of that distinction.",
    NONE,[r"splitt",r"extension",r"D02",r"filtration"])

add("A22",A,"The expectation about the number of parameters","015","opening sentence",
    "conjecture",
    "“Il ne semble pas … moins de paramètres”.",
    r"""The expectation concerns normalizations valid without characteristic restrictions and compatible with the indicated topology of base changes. It is not a claim that the moduli space of elliptic curves has dimension five, nor does the existence of a five-parameter atlas prove minimality among all possible presentations. A precise minimality question would have to fix the allowed rigidifications, cover topology, and class of coordinate transformations.""",
    "No matching minimal-parameter claim was found in T/N/D; the modern five-coefficient atlas (Stacks Project, n.d., Tag 072S) corroborates the construction's form, not its optimality.",
    PLACE,[r"paramètre",r"normalis",r"représent"])

add("A23",A,"Normalizing the discriminant by a finite flat cover","015","middle paragraph",
    "unproved claim",
    "“δ(b,c,d,e,f)=1”; “12.ième (…24.ième)”.",
    r"""Locally, adjoining a twelfth root of an invertible discriminant gives a finite free faithfully flat algebra, so a weight-twelve normalization can be achieved in that topology. Such a cover need not be étale in residue characteristics two or three, and the Lie line versus its cotangent dual determines whether the invariant section is written as a discriminant or its inverse. The parenthetical twenty-fourth power remains an unresolved textual/mathematical qualification rather than an inferred alternative normalization.""",
    "T, cote 16, scan 56, distinguishes flatness and unramifiedness; T, cote 54, scan 3, fixes tangent/cotangent variance; neither supplies the twenty-fourth-power parenthesis.",
    NONE,[r"non ramifi",r"plat",r"t_A",r"puissance"])

add("A24",A,"Successive characteristic restrictions in normal forms","015–016","promise and normalized equation",
    "unproved claim",
    "“en car ≠2, puis en car. ≠3, puis on verra”.",
    r"""Completing the square removes the terms linear in the pole-three coordinate when two is invertible, while translating the pole-two coordinate removes the quadratic term of the cubic when three is invertible. These are distinct restrictions and must not be imposed retroactively on the characteristic-free five-coefficient model. The promised further normalization is only partly carried out within this selection.""",
    "T, cote 54, scans 3 and 7, separates characteristic-zero and characteristic-p constructions; no second normal-form derivation occurs in T/N/D.",
    NONE,[r"car.",r"normalis",r"caractéristique"])

add("A25",A,"A proper quotient is not an affine-line torsor","016","geometric interpretation of C/Z₂",
    "own idea",
    "“espace principal homogène sous … fibré vectoriel … inversible”.",
    r"""As written, the proper Brauer–Severi quotient cannot itself be a torsor under an additive line bundle: its geometric fibres are projective lines, whereas such torsor fibres are affine lines. The likely mathematical object for that assertion is the complement of the marked section at infinity, which does carry affine-line transition functions with the indicated linear part. This is an explicit proposed qualification of the claim, not a change to the noun phrase in the transcription.""",
    "T, cote 16, scans 21–23, uses Brauer groups for a different purpose; no same quotient/torsor identification was found; compare internally scan 034 for the analogous missing complement in a multiplicative torsor assertion.",
    NONE,[r"Brauer",r"homogène",r"fibré",r"tors"])
notes[-1]['confidence']=r"High: properness is preserved by field extension, and \(\mathbf P^1\) and \(\mathbf A^1\) differ in properness."

add("A26",A,"Inversion on E₂ without excluding characteristic two","017","live paragraph after the cancelled opening",
    "self-flagged",
    "“c'est ainsi … sans … la condition … on le verra” [wording uncertain].",
    r"""The forward claim is that inversion acts trivially on the functions with poles of order at most two even without inverting two. In a general Weierstrass equation the pole-two coordinate is fixed by inversion, while the pole-three coordinate transforms by its negative plus lower terms, which supplies the expected characteristic-free verification. The parenthetical reading uncertainty is retained, and the promised verification is not written out on this page.""",
    r"T, cote 47, scans 4–6, also requires inversion in the Fourier composite; N, F7–F8, does not prove that kernel identity from an action on \(\mathcal E_2\).",
    "WG2 §2.4 #4: a sign/involution comparison setting only.",
    [r"inversion",r"symétrie",r"F7",r"F8",r"(-1)"])

add("A27",A,"The anti-invariant complement and the factor two","017","unique complement L₃",
    "unpursued implication",
    "“un supplémentaire unique … où s opère par symétrie”.",
    r"""When two is invertible, the idempotents \((1+s)/2\) and \((1-s)/2\) give the invariant and anti-invariant summands, explaining the uniqueness of the specified complement. Identifying that complement with \(\mathcal L\cdot\mathcal E_2\) also uses the leading-pole coefficient two in the derivation calculation. Neither argument produces the same direct-sum decomposition in characteristic two.""",
    "T, cote 54, scan 3, and N, D02, concern an unsplit Hodge extension; this eigenspace splitting after inverting two is an additional, different structure.",
    NONE,[r"splitt",r"extension",r"D02",r"symétrie"])

add("A28",A,"The characteristic-free differential map need not be a complement","017","N.B. margin",
    "own idea",
    "“sans restriction de car”; “L^{⊗3}→E₃”.",
    r"""The margin can plausibly define a morphism in every characteristic while the image ceases to provide the anti-invariant basis in characteristic two. Indeed its leading term is governed by the same coefficient two as differentiation of a double pole, so the associated graded map vanishes there. The existence of a map and its use as a splitting or local generator should therefore be kept separate.""",
    "T, cote 54, scan 7, and N, D04–D05, already distinguish vector-space data from restricted Lie data; cote 62 supplies this concrete failure of a characteristic-zero splitting mechanism.",
    PLACE,[r"Lie",r"D04",r"D05",r"car."],
    "High for the leading-term obstruction, by A08; medium for identifying the marginal construction exactly, because its wording is partly uncertain.")

add("A29",A,"The cancelled L₆ complement","017","deleted sentence before the final matrices",
    "withdrawn in the same text",
    "“L₃^{⊗2} est un supplémentaire de E₅ dans E₆”.",
    r"""This complement assertion is explicitly struck through, and its unfinished “A condition” is retained as part of the cancellation. The later coordinate relation may explain the pole-six leading term, but does not restore the cancelled statement as a canonical choice of subbundle. It belongs to the record of attempts to normalize the equation.""",
    "No identical complement statement occurs in T/N/D; N, D02, is a related warning about inferring canonical splittings.",
    NONE,[r"supplément",r"splitt",r"D02",r"canonique"])

add("A30",A,"The normalization question is locally answered in the supplied order","016–017","last question of scan 017 and equation on scan 016",
    "self-flagged",
    "“Quelle est la normalisation correspondante de l'équation de C ?”.",
    r"""The preceding supplied scan already gives the equation with the inversion-odd cross terms removed, which is the natural answer to this question under the stated characteristic restriction. This suggests revision or arrangement across the sheets rather than a reason to reorder the diplomatic transcription. It gives no secure chronological date or evidence that one of the neighbouring dossiers was written earlier.""",
    "T, cote 44, scans 8–9, contains the separately dated letter to Serre, but neither T nor README dates this normalization sequence securely.",
    "WG2 §2.4 #4: local order is not evidence of an earlier Jacobians witness.",
    [r"Bures",r"1964",r"vieille",r"chronolog",r"normalis"])

add("A31",A,"The displayed group retains a central double cover of the affine group","017","last matrices and identification",
    "own idea",
    "“Ce n'est autre que le groupe affine à 1 variable”.",
    r"""The displayed matrices with diagonal \((1,\lambda^2,\lambda^3)\) project to the affine transformations of the pole-two coordinate, but the projection has kernel \(\{\operatorname{diag}(1,1,\pm1)\}\simeq\mu_2\). Thus, when two is invertible, the written group is a central double cover of the usual affine group, with torus weight two up to inversion, rather than that affine group itself; its nontrivial center distinguishes them. Passing to the quotient action on the genus-zero curve removes this kernel, exactly the deck involution whose information is lost in C16.""",
    "T, cote 47, scans 4–6, retains inversion as a genuine abelian automorphism; T, cote 54, scan 3, retains the full group object; no same matrix-group identification occurs in T/N/D.",
    PLACE+" Hua 62-triples-rigidified-moduli: clarification of the passage to branch-data rigidification.",
    [r"inversion",r"symétrie",r"groupe affine",r"62-triples"],
    "High: the central element diag(1,1,−1) is explicit, whereas the usual affine group has trivial center.")

B = "2. Cubic discriminants, cross-ratios, and the S₃ quotient"

add("B01",B,"The reducedness qualification in the Kummer scratch work","019","two Kummer correspondences",
    "self-flagged",
    "“à vérifier … géométriquement”; “ss élémts nilpotts” [wording uncertain].",
    r"""The notes explicitly restrict the passage from \(b^3=0\) or \(c^2=0\) to the vanishing of \(b\) or \(c\) by mentioning the absence of nilpotents. That qualification matters for the later special-invariant classification, where it is no longer written: equality of a ramified invariant to a branch value does not force the section into the reduced fixed locus over a nonreduced base. The Kummer exponent in the first unit quotient is itself uncertain and is not settled by this observation.""",
    "T, cote 16, scan 52, n°5, proposes a Kummer description of totally tamely ramified complete extensions; N, 16:52 and the tame-ramification discussion, supplies only a prior lead with its own hypotheses; cote 62 adds explicit nilpotent sensitivity.",
    HUA,[r"Kummer",r"Kumm",r"nilpot",r"16:52",r"modérément"])

add("B02",B,"Kummer classes and constant cyclic groups are not interchangeable","019","Kummer group labels",
    "own idea",
    "“Ext. Kummérienne de gr Z/3”.",
    r"""Over a base where three is invertible, adjoining a cube root of a unit naturally defines a \(\mu_3\)-torsor, and identifying this with a torsor under the constant group \(\mathbf Z/3\) requires a primitive cube root of unity. Over general schemes even \(H^1(S,\mu_n)\) need not be only units modulo nth powers, because the Kummer sequence also sees n-torsion line bundles; for an affine local base the line-bundle term vanishes (Stacks Project, n.d., Tag 03PK). These are necessary qualifications for interpreting the scratch correspondences and the later scan 048 assertion.""",
    "T, cote 16, scan 52, n°5, includes a complex-root generator in its Riemann-surface example; N's discussion of that scan already warns about residue and roots-of-unity hypotheses; this note applies that distinction to the actual cyclic-group labels in cote 62.",
    HUA+" CYCLOTOMIC_KERNEL C1 concerns a different completed torsor and is not reproved here.",
    [r"Kummer",r"racine",r"CYCLOTOMIC_KERNEL",r"16:52"],
    r"High: the group action on an nth-root equation is multiplication by \(\mu_n\); the distinction follows directly from descent.")

add("B03",B,"Two incompatible ratio formulas remain on the scratch sheet","019","lower calculations",
    "reading question",
    "“b³/c²=j”; “b³/c²=27(j−1)/j”.",
    r"""Both formulas are present, but they cannot be the same definition of \(j\) with unchanged coefficients on a general parameter space. The intervening equation \(27c^2(j-1)=b^3j\) supports the second ratio, while the final cubic uses that same rational expression. A normalization change or abandoned calculation is possible, but the sheet does not explicitly identify one, so the competing formulas remain a research question.""",
    "T/N/D contains no parallel version of this ratio; T, cote 16, scan 54, refers to algebraic discriminants without these elliptic parameters.",
    NONE,[r"discriminant",r"elliptiq",r"27",r"normalis"])

add("B04",B,"The queried cubic discriminant has a sign and coefficient problem","021","product-of-derivatives calculation and boxed question",
    "self-flagged",
    "“Δ=…b³−27c² ?”.",
    r"""For the monic depressed cubic \(f(x)=x^3+bx+c\), direct expansion gives \(\prod_i f'(x_i)=4b^3+27c^2\), while \(\prod_{i<j}(x_i-x_j)^2=-4b^3-27c^2\). Thus the derivative-product convention and the squared-difference convention differ by a sign, and the queried live boxed expression, as transcribed, is neither of these with unchanged \(b,c\). This calculation explains why the written question mark matters, without replacing its uncertain cancelled coefficient.""",
    "T, cote 16, scan 54, explicitly refers the reader to Alg. IX, §2 for a discriminant definition; T, cote 16, scan 23, uses a lattice discriminant, a different object; neither resolves the present scratch calculation.",
    NONE,[r"discriminant",r"trace",r"Alg. IX"],
    "High for the editorial calculation: the resultant and Vandermonde identities are verified symbolically in records/research/algebra_checks.json.")

add("B05",B,"The root expression reconciles the later invariant","023","two boxed formulas",
    "unpursued implication",
    "“j=(27c+2a³−9ab)²/(−27Δ)”.",
    r"""For \(f(x)=x^3+ax^2+bx+c\), the product \(\prod_i(3x_i+a)=-2a^3+9ab-27c\), so its square gives the stated numerator with the squared-difference discriminant. The intermediate line containing \(9b\) instead of \(9ab\) is a separate inconsistency that the final line does not erase. After depressing the cubic, this invariant is \(1-J/1728\) for the conventional elliptic invariant \(J\), consistent with the explicit cross-ratio formula on scan 040.""",
    "No same cubic-root formula occurs in T/N/D; the discriminant references in T, cote 16, scans 23 and 54, concern other constructions.",
    NONE,[r"discriminant",r"elliptiq",r"cubiq"],
    "High for the normalization calculation, by the direct polynomial identities recorded with B04.")

add("B06",B,"The family on scan 025 uses the classical invariant","025","top line",
    "reading question",
    "“y²=4x³−h(x+1)”; “h=27j(j−2⁶3³)⁻¹”.",
    r"""With \(g_2=g_3=h\) in \(y^2=4x^3-g_2x-g_3\), the conventional invariant is \(J=1728g_2^3/(g_2^3-27g_3^2)=1728h/(h-27)\), hence \(h=27J/(J-1728)\). The displayed formula therefore uses \(j\) in the classical normalization, whereas scans 023 and 040 use \(1-J/1728\). Its discriminant is \(h^2(h-27)\), so this smooth family is restricted to the open where \(J(J-1728)\) is invertible and does not extend as a smooth model by merely substituting \(J=0\). This is a local change of normalization to track, not a reason to standardize the symbol throughout the transcription.""",
    "No alternate copy of this family was found in T/N/D; N's general abelian-variety discussions do not fix an elliptic j normalization.",
    NONE,[r"elliptiq",r"invariant",r"1728",r"normalis"],
    "High: solving the displayed rational identity gives the claimed change exactly; see the explicit calculation record.")

add("B07",B,"The cross-ratio convention controls all six transforms","025, 028","four-point calculations and S₃ table",
    "unpursued implication",
    "“t=(x₃−x₁)/(x₃−x₂)”; “renommer” [uncertain].",
    r"""The cross-ratio convention gives the six anharmonic transforms \(t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t\), and changing the initial ordering permutes these rather than creating a new moduli invariant. The revised labels and marginal uncertainty on scan 028 concern which named group element represents each transformation, so one should check compositions from the displayed maps instead of relying on the letters alone. In particular, the written product \(\lambda\mu=\varphi\) uses left-to-right application, whereas ordinary \(\lambda\circ\mu\) is the displayed \(\psi\). The Legendre family is a standard realization of this parameter (Stacks Project, n.d., Tag 03VA).""",
    "T/N/D contains no same six-transform table; R, LM7 E.30, refers to the quotient orbifold of the same punctured line, giving a conceptual link rather than a second notation witness.",
    "LM7 E.30 (return's claim): explicit geometric model, not its relative-completion theorem.",
    [r"LM7 E.30",r"orbifold",r"crois",r"permut"])

add("B08",B,"The extra involution is explicit and requires 3 invertible","028","formula for σ and uniqueness comment",
    "unproved claim",
    "“σ=(t−2)/(2t−1)”; “c'est d'ailleurs le seul”.",
    r"""The matrix \(\begin{pmatrix}1&-2\\2&-1\end{pmatrix}\) has determinant three and square \(-3I\), so it defines a projective transformation whose square is the identity when three is invertible; it is nontrivial when two is also invertible. Direct substitution shows that it centralizes the two generating anharmonic involutions and sends \(\{0,1,\infty\}\) to \(\{2,1/2,-1\}\) when also two is invertible. Any uniqueness assertion must specify the required commuting or point-mapping conditions; there are of course many unrelated involutions of the projective line.""",
    "No matching matrix occurs in T/N/D; the normalizer questions in R, LM4 E.20 and LM6 A.22, have different ambient profinite groups.",
    "LM4 E.20 and LM6 A.22: an elementary finite-geometric comparison only.",
    [r"normalis",r"centralis",r"LM4 E.20",r"LM6 A.22"],
    "High for the direct identities; their verification is recorded in algebra_checks.json.")

add("B09",B,"The normalizer problem has a short tame-geometric solution","030","opening ‘Prouver’",
    "self-flagged",
    "“Prouver : le normalisateur … est S₃×(Z/2)”.",
    r"""Over a base with six invertible, split the two fixed points of the order-three subgroup by the cyclotomic étale cover; its centralizer in \(\mathrm{PGL}_2\) is then the diagonal torus, and commuting also with a transposition restricts that torus to \(\mu_2\), generated by the displayed \(\sigma\). Since every automorphism of the constant group \(S_3\) is inner, an element of its normalizer differs from an element of \(S_3\) by such a centralizer element, giving \(N=S_3\times\langle\sigma\rangle\), with descent back to the original base. This completes the stated elementary calculation under the explicit tame hypothesis; it does not establish a normalizer theorem in a profinite mapping-class or outer-automorphism group.""",
    r"R, LM4 E.20, claims a proved centralizer identification in a profinite outer group, without an explicit referee marker on that row; R, LM4 D.32, is explicitly reviewed and supplies a different finite/profinite recognition test; the present proof adds only the concrete \(\mathrm{PGL}_2\) calculation.",
    "LM4 E.20; LM4 D.32 (reviewed): distinct ambient groups and no register-status change.",
    [r"LM4 E.20",r"LM4 D.32",r"normalis",r"centralis"],
    "High under 6 invertible: the split-torus centralizer calculation and innerness of Aut(S₃) give the proof.")

add("B10",B,"The cyclotomic fixed bisection and bad characteristics","030","Φ₆ and fixed-locus calculations",
    "unpursued implication",
    "“Φ₆(t)=t²−t+1”; “non ramifié … ≠2,3”.",
    r"""The two order-three fixed points satisfy \(t^2-t+1=0\), whose discriminant is \(-3\); after inverting two this is the quadratic cover obtained by adjoining \(\sqrt{-3}\), and it is étale after also inverting three. In characteristic three the two roots merge, while in characteristic two several harmonic formulas and the involution comparisons change. The later restriction to \(\mathbf Z[1/6]\) is therefore substantive, and the uncertain bottom marginal warning cannot be converted into a more precise theorem than the ink supplies.""",
    "T, cote 16, scan 52, distinguishes tame ramification from the different; its ramification discussion is compatible with this explicit discriminant test, not a duplicate calculation.",
    HUA,[r"différente",r"modér",r"ramifi",r"racine"])

add("B11",B,"The stabilizer of the bisection is a twisted torus extension","030–034","group G and quadratic form",
    "unpursued implication",
    "“produit tordu de G_m”; “√−3”.",
    r"""After the two points split, their pointwise stabilizer is \(\mathbf G_m\), and interchanging them acts on that torus by inversion. Descending through the cyclotomic involution gives the norm-one torus associated to the quadratic étale algebra, together with the component interchanging the points. This explains the arithmetic twist in the manuscript and prevents replacing every cyclic stabilizer by a constant group before checking its descent.""",
    "T, cote 16, scan 52, and N's Kummer qualification provide a related root-of-unity issue; R, LM7_PUSH E.3, concerns a much larger arithmetic CM image and is not decided by this torus.",
    HUA+" LM7_PUSH E.3: finite geometric model only.",
    [r"Kummer",r"racine",r"LM7_PUSH E.3",r"CM"],
    "High for the split-and-descend description; it is the explicit action of the quadratic involution on the two fixed points.")

add("B12",B,"A fibrewise rational quotient needs a relative argument","032","full S₃ quotient and three sections",
    "self-flagged",
    "“à expliciter…”; “th. de Lüroth”.",
    r"""Lüroth's theorem identifies the rational function field of a geometric quotient, but by itself does not identify a relative quotient over an arbitrary base with the trivial projective-line bundle. For the full \(S_3\) quotient, the additional three pairwise disjoint sections provide the needed trivialization once existence and smoothness of the relative quotient are established. The author explicitly leaves those sections to be made explicit, whereas the following quotient by \(C_3\) initially has two distinguished sections and requires the separate cyclotomic normalization on scan 034.""",
    "No same relative quotient construction occurs in T/N/D; T, cote 16, scan 56, supplies relevant étale descent language only.",
    HUA,[r"Lüroth",r"section",r"descente",r"étale"])

add("B13",B,"The multiplicative torsor also requires deleting two sections","034","opening quotient description",
    "own idea",
    "“P¹_S/(Z/3) est can. isomorphe à un fibré principal”.",
    r"""The entire proper quotient cannot be a \(\mathbf G_m\)-torsor, since its geometric fibre is \(\mathbf P^1\), whereas such a torsor fibre is \(\mathbf G_m\). Deleting the two already defined zero and infinity sections gives the appropriate \(\mathbf G_m\)-torsor. Adjoining \(\sqrt{-3}\) splits the ramification bisection and permits a choice of unit section; it does not split the already defined zero and infinity sections. This is the multiplicative analogue of the missing-complement issue on scan 016.""",
    "No corresponding quotient/torsor assertion occurs in T/N/D; the direct comparison is internal, with scan 016, while T, cote 16, scan 52, supplies only the Kummer background.",
    HUA,[r"homogène",r"tors",r"Kummer",r"fibré"],
    "High: geometric fibres and properness distinguish the whole quotient from the stated torsor.")

add("B14",B,"Extending r=s² to the whole projective line","036","display (9) and bracket",
    "self-flagged",
    "“lui donner un sens, et justifier cette assertion…”.",
    r"""The global extension is the homogeneous morphism \([s_0:s_1]\mapsto[s_0^2:s_1^2]\), whose two coordinates have no common zero. Over \(\mathbf Z[1/6]\) its ramification is at zero and infinity with index two, agreeing with the quotient diagram after the chosen trivializations. This answers the local algebraic extension request, while the descent of the chosen coordinate must still be tracked as on the surrounding pages.""",
    "T, cote 16, scan 52, treats the different and tame Kummer maps; cote 62 adds an explicit degree-two projective model.",
    HUA,[r"Kummer",r"ramifi",r"différente",r"racine"],
    "High: the homogeneous formula gives a morphism on both standard affine charts.")

add("B15",B,"The degree-three quotient map and its uniqueness qualification","038","formula for f and prescribed values",
    "unproved claim",
    "“f(t)=…/(3√−3)”.",
    r"""The formula \(f(t)=F(t)/(3\sqrt{-3}\,t(t-1))\), where \(F=(t+1)(2t-1)(t-2)\), has simple poles at \(0,1,\infty\) and zeros at the harmonic triple, and direct differentiation gives ramification at the two cyclotomic points. A uniqueness assertion needs these full divisor/value normalizations; ramification locations alone allow postcomposition by target automorphisms. The quadratic Galois involution changes the sign of \(f\), explaining why its square descends.""",
    "No parallel rational function is present in T/N/D; T, cote 16, scan 52, is the relevant general ramification comparison.",
    HUA,[r"ramifi",r"racine",r"Kummer",r"normalis"],
    "High for the divisor and derivative calculation, recorded in algebra_checks.json.")

add("B16",B,"The normalized quotient invariant and its branch fibres","040","formulas (10)–(11)",
    "unpursued implication",
    "“définie sur S lui-même”.",
    r"""Writing \(i=-F(t)^2/(27t^2(t-1)^2)\), direct expansion gives \(1-i=4(t^2-t+1)^3/(27t^2(t-1)^2)\), hence \(i=1-J/1728\) for \(J=256(t^2-t+1)^3/[t^2(t-1)^2]\). Thus the fibre over zero is twice the harmonic triple, the fibre over one is three times the cyclotomic pair, and the fibre over infinity is twice \(\{0,1,\infty\}\). The multiplicities explain both the tame branch indices and why special invariant values lose infinitesimal information.""",
    "No matching formula occurs in T/N/D; R, LM7 E.30, names the quotient orbifold to which this map gives a concrete coordinate description.",
    "LM7 E.30: explicit orbifold/branch model; "+HUA,
    [r"LM7 E.30",r"orbifold",r"invariant",r"ramifi"],
    "High: the identity is a verified polynomial identity, and the three disjoint branch orbits are explicit over 6 invertible.")

add("B17",B,"The induced involution is reciprocal, not an isogeny calculation","040","question and last display",
    "self-flagged",
    "“Comment opère σ dans les quotients ?”; “1/t”.",
    r"""Substitution into the normalized invariant gives \(i(\sigma(t))=1/i(t)\), so in the conventional normalization it acts by \(J\mapsto1728J/(J-1728)\). This checks the stated quotient action and exchanges the two branch values zero and infinity while fixing one. No elliptic isogeny or action on a Poincaré bundle is constructed by that fractional-linear identity.""",
    "T, cote 47, scans 3–8, concerns a derived Fourier transform on abelian schemes, not this projective-line involution; R's CM image questions likewise require additional arithmetic data.",
    "WG2 §2.4 #4 and LM7_PUSH E.3: the reciprocal action does not close either problem.",
    [r"compatibilité",r"Fourier",r"LM7_PUSH E.3",r"inversion"],
    "High for the reciprocal identity, verified symbolically; no claim of an isogeny is inferred.")

add("B18",B,"The two quotient stages have different ramification sections","032–034","last sentence of 032 and its continuation on 034",
    "reading question",
    "“sections de ramification de P¹_S sur P¹_S/(Z/3)” [‘ramification’ uncertain].",
    r"""The two three-point orbits \(\{0,1,\infty\}\) and \(\{2,-1,1/2\}\) have trivial stabilizers under \(C_3\), so their images are not branch sections of the degree-three quotient. They instead become the two branch sections of the subsequent degree-two quotient by \(S_3/C_3\), while the cyclotomic pair supplies the degree-three ramification. The uncertain written word therefore gives a specific stage-of-quotient reading question, with the original ink left unchanged.""",
    "T, cote 16, scan 52, treats tame ramification and the different; the present distinction is an explicit two-stage example, not another witness to that text; R's Hua lead concerns the resulting triples.",
    HUA,[r"ramifi",r"différente",r"quotient",r"62-triples"],
    "High for the stabilizer calculation over 6 invertible; the glyph itself retains its diplomatic uncertainty.")

C = "3. Trisections, descent, and the limits of the invariant"

add("C01",C,"The trisection definition repeats the wrong apparent base","042","opening sentence",
    "reading question",
    "“non ramifié sur X, d'ordre 3 sur X”.",
    r"""The written definition places both unramifiedness and degree three over \(X\), although the subsequent construction treats \(X'\) as a finite étale degree-three object over \(S\) embedded in the relative genus-zero curve \(X\). A closed subscheme of \(X\) can be unramified over \(X\), but that does not express the asserted three-point family over the base. The expected \(S\)-relative formulation is a mathematical reading question only, and the repeated \(X\) remains in the transcription.""",
    "T, cote 16, scan 56, distinguishes étale, flat, and unramified morphisms; no second copy of the trisection definition occurs in T/N/D.",
    HUA,[r"non ramifi",r"étale",r"trisection",r"degré"])

add("C02",C,"Why a trisection gives an S₃ torsor","042","classification paragraph",
    "unproved claim",
    "“classification dans un H¹(S,S₃)”.",
    r"""For the intended finite étale trisection, the scheme of its orderings is an \(S_3\)-torsor; over that cover, the unique projective transformation taking the ordered three points to \(0,1,\infty\) trivializes the genus-zero curve. Conversely an \(S_3\)-torsor twists that standard marked projective line, giving inverse descent constructions. This explains the classification of pairs and their automorphisms; a torsor need not be connected even if it is called a Galois covering.""",
    "T, cote 16, scan 56, explicitly records finite étale trivialization after faithfully flat base change; the present pair-classification adds its concrete descent datum; the general torsor-plus-equivariant-map formalism is Stacks Project (n.d., Tag 04UV).",
    HUA,[r"trisection",r"fid.",r"étale",r"descente"])

add("C03",C,"The associated trisection is an involutive construction","042","X′ to X″ paragraph",
    "self-flagged",
    "“on restitue X′ [à préciser…]”.",
    r"""Because \(\sigma\) centralizes the standard \(S_3\)-action, it descends through every ordering torsor and takes the original triple to the associated harmonic triple. The identity \(\sigma^2=1\) then returns the original trisection, so the construction is intrinsic under the tame hypotheses used in the explicit formulas. This supplies the requested clarification once the pair-descent construction has been made precise.""",
    "No same associated-trisection construction occurs in T/N/D; R's Hua lead identifies the subject but does not supply a checked proof; the handwritten margin on scan 047 gives an additional local witness of the two triples.",
    HUA,[r"trisection",r"62-triples",r"descente",r"invol"],
    "High: equivariance and the explicit square of σ prove the descent and involutivity.")

add("C04",C,"The bisection is descended from the cyclotomic fixed locus","042","bracketed descent sentence",
    "self-flagged",
    "“[par descente…] une bisection”.",
    r"""The two roots of \(t^2-t+1\) form an \(S_3\)-stable degree-two subscheme, so the same ordering torsor descends them to the claimed bisection. Its étaleness requires the indicated tame restriction, and its arithmetic form includes the cyclotomic action rather than a chosen ordering of the two points. This is the geometric source of the twist that becomes decisive at invariant one.""",
    "T, cote 16, scans 52 and 56, supplies Kummer and étale-descent background; N's previous notes do not contain this explicit bisection.",
    HUA,[r"racine",r"descente",r"Kummer",r"non ramifi"])

add("C05",C,"The invariant is complete on the free-action locus","044–046","last bracket of scan 044 and first sentence of scan 046",
    "self-flagged",
    "“À déduire … des formalismes catégoriques généraux”; “l'invariant suffit”.",
    r"""Where \(i\) and \(i-1\) are units, the pullback of \(U\to\mathbf A^1_i\), with \(U=\mathbf P^1-\{0,1,\infty\}\), is an \(S_3\)-torsor because the action is free there. An equivariant map from the ordering torsor of a triple to that pullback is an isomorphism of torsors, which recovers the triple from \(i\). This is an object-level equivalence on the free locus, and it does not extend unchanged across the ramified fibres.""",
    "T, cote 16, scan 56, gives the relevant finite étale descent mechanism; Stacks Project (n.d., Tag 04UV) supplies the general quotient-stack formalism; no identical invariant reconstruction appears in T/N/D.",
    HUA,[r"descente",r"étale",r"catégori",r"invariant"],
    "High for this completion of the bracketed step: an equivariant morphism between two torsors is locally a translation and therefore an isomorphism.")

add("C06",C,"The normality paragraph changes X and S","046","first long paragraph",
    "reading question",
    "“X est normal, intègre”; “[S_{i(i−1)}]”.",
    r"""The paragraph speaks of the function field of \(X\), a covering of \(X\), and normality of \(X\), while the displayed open is explicitly an open of \(S\) and the preceding torsor lives over \(S\). The intended reconstruction is naturally a statement about a normal integral base, but that correction is not written into the frozen text. Any proof should first fix the base of normalization and the rational section being extended.""",
    "T, cote 16, scans 52, 54, and 56, distinguishes base rings from their étale extensions; no second version of this paragraph occurs in T/N/D.",
    HUA,[r"normal",r"corps des",r"intégr",r"revêt"])

add("C07",C,"Finiteness of normalization and the degree-three algebra","046","two numbered conditions",
    "unproved claim",
    "“une certaine extension de corps — de degré 3”.",
    r"""After making the base interpretation explicit, the generic object may be a product of separable fields, so a degree-three étale algebra is more general than a degree-three field extension. Over a locally Noetherian normal integral base, its integral closure is finite by the separable trace-pairing argument, applied componentwise (Stacks Project, n.d., Tag 032L). The remaining substantive requirement is that this finite normalization be étale everywhere; finiteness does not itself provide that condition.""",
    "T, cote 16, scan 54, treats integral extensions and discriminants; scans 52 and 56 distinguish ramification and étaleness; cote 62 asks for these tests in a specific moduli reconstruction.",
    HUA,[r"intégr",r"discriminant",r"non ramifi",r"corps"])

add("C08",C,"When the rational-section condition becomes automatic","046","condition (ii)",
    "own idea",
    "“Qu'une certaine application rationnelle … est partout définie”.",
    r"""Suppose \(S\) is normal integral, \(i\) is regular, and the full generic \(S_3\)-torsor extends to a finite étale torsor \(T\to S\). Since \(U\to\mathbf A^1_i\) is finite and \(T\) is normal, the generic equivariant map \(T\dashrightarrow U\) extends uniquely by integrality of its coordinate functions, and equivariance extends by uniqueness. Under these hypotheses the extra section-extension condition follows from the étale-torsor extension, although mere unramifiedness at codimension-one points would not justify this argument.""",
    "T, cote 16, scans 52 and 56, provides ramification/descent notions but not this finite-map extension argument; it sharpens the two separate conditions written here.",
    HUA,[r"non ramifi",r"normal",r"intégr",r"descente"],
    "High under the stated full-extension hypotheses: a function integral over a normal domain and lying in its fraction field lies in that domain.")

add("C09",C,"The branch indices give local divisibility tests","019, 046","normal local scratch work and ‘quels i’ question",
    "own idea",
    "“quels i conviennent ??”",
    r"""Over a discrete valuation ring with six invertible and \(i\) generically different from zero and one, the tame local models give \(2\mid v(i)\) when the closed point maps to zero and \(3\mid v(i-1)\) when it maps to one. These conditions make the relevant extracted-root extension unramified: after removing the divisible uniformizer power, the remaining equation extracts a prime-to-residue-characteristic root of a unit. They explain the exponents suggested on scan 019, but are local tests and do not automatically extend to every normal higher-dimensional base.""",
    "T, cote 16, scan 52, n°5, explicitly requests the complete tame Kummer description; N's corresponding discussion already flags the roots-of-unity/residue hypotheses; this note adds the concrete exponents two and three.",
    HUA,[r"Kummer",r"uniformis",r"modér",r"16:52"],
    "High in the stated DVR/tame setting, by the branch orders in B16 and the elementary root-of-unit étale criterion.")

add("C10",C,"Codimension-one unramifiedness is insufficient on a singular normal base","046","normalization criterion",
    "own idea",
    "“est non ramifié sur X”.",
    r"""Take \(R=k[[x,y,z]]/(xy-z^2)\), with \(k\) algebraically closed of characteristic zero, and \(i=x\): its divisor is twice the prime \((x,z)\), so the order-two divisibility test passes in codimension one. The normalization obtained by adjoining \(\sqrt{x}\) is \(k[[u,v]]\), with \(x=u^2,y=v^2,z=uv\), the quotient cover by simultaneous sign change; it is étale away from the closed singular point but ramified there. Since \(R\) is strictly henselian, a realizing triple would have trivial ordering torsor and a local harmonic parameter with \(i\) a unit times a square, forcing \(\sqrt{x}\in R\), a contradiction. This is a counterexample to replacing the manuscript's everywhere-unramified requirement by only divisorial tests.""",
    "T, cote 16, scans 52 and 56, keeps ramification and étaleness as scheme-level conditions; no matching singular-base example was found in T/N/D.",
    HUA,[r"non ramifi",r"normal",r"régulier",r"étale"],
    "High: the explicit invariant-ring cover is finite, free away from the origin, and has a fixed point at the origin; the contradiction uses only Henselian square roots of units.")

add("C11",C,"Invariant zero and the harmonic stabilizer","048","first live assertion",
    "unproved claim",
    "“H¹(S,Z/2)”.",
    r"""On a reduced base with six invertible, a section with \(i=0\) factors through the reduced harmonic orbit \(\{-1,1/2,2\}\), whose stabilizer is a constant order-two subgroup. Reduction of the ordering torsor to that stabilizer gives the claimed \(H^1(S,\mathbf Z/2)\) description, retaining the usual groupoid automorphisms. Over a nonreduced base the factorization into that reduced orbit need not follow from \(i=0\), as C13 makes explicit.""",
    "T, cote 16, scan 56, supplies finite étale descent only; R's Hua entry proposes a broad equivalence, for which this reducedness qualification is a material refinement.",
    HUA,[r"62-triples",r"nilpot",r"étale",r"réduction"])

add("C12",C,"Invariant one has a cyclotomic twist","048","second special-value assertion",
    "own idea",
    "“H¹(S,Z/3)”.",
    r"""On a reduced base with six invertible, the order-three stabilizer is naturally the cyclotomic form \(\mu_3\), so the special fibre is described, after choosing its evident neutral object, by \(H^1(S,\mu_3)\), becoming the written constant-group description after splitting the cyclotomic cover. Over \(\mathbf Q\), the triple \((\mathbf P^1,\{x^3=1\},\infty)\) has \(i=1\), but its ordering torsor has nontrivial sign character from \(\mathbf Q(\sqrt{-3})\), so it cannot reduce to the constant alternating subgroup \(C_3\subset S_3\). The automorphisms fixing infinity and preserving those three roots are multiplication by \(\mu_3\), which gives a direct check of the missing twist.""",
    "T, cote 16, scan 52, n°5, and N's Kummer qualification distinguish root extraction from a split constant cyclic action; this provides a specific counterexample to an unrestricted reading of scan 048.",
    HUA,[r"Kummer",r"racine",r"62-triples",r"cyclotom"],
    r"High: the discriminant of \(x^3-1\) has square class \(-3\), and the affine automorphism group of its root set fixing infinity is exactly \(\mu_3\).")

add("C13",C,"Infinitesimal special fibres are not just stabilizer torsors","048","both special-invariant classifications",
    "own idea",
    "“En tous cas, si i=0”; “Et si i=1”.",
    r"""Let \(S=\operatorname{Spec}k[\epsilon]/(\epsilon^2)\), with \(k\) algebraically closed of characteristic zero, and take the trivial ordering torsor with \(t=-1+\epsilon\): the squared factor in B16 makes \(i(t)=0\), yet no constant anharmonic transform takes this nonconstant section to \(t=-1\). All finite étale torsors under \(C_2\) over \(S\) are trivial, so the two resulting triples cannot both be classified by the stated \(H^1(S,C_2)\); similarly \(t=\zeta_6+\epsilon\) has \(i=1\) by the cubic factor but is not equivalent to the constant cyclotomic section. Thus the scheme-theoretic branch fibres contain infinitesimal directions omitted by the reduced stabilizer description. The earlier nilpotent warning on scan 019 is relevant evidence that this issue was already visible in the scratch work.""",
    "T, cote 16, scan 56, has étale descent but no infinitesimal branch example; R's Hua entry needs this qualification if its equivalence is taken to include classification by the scalar invariant at special values.",
    HUA,[r"nilpot",r"étale",r"62-triples",r"invariant"],
    r"High: the double- and triple-zero formulas make the calculation exact modulo \(\epsilon^2\), and every Möbius transform has nonzero derivative at these allowed points.")

add("C14",C,"The intermediate double quotient and its quadratic cover","048","diagram and last line",
    "unproved claim",
    "“trois sections”; “it²”; “√i”.",
    r"""After quotienting by the normal order-three subgroup and choosing the three indicated disjoint sections as infinity, zero, and one, the remaining degree-two map is normalized as \(u\mapsto iu^2\). Its preimage of one is \(u^2=i^{-1}\), which is isomorphic to the quadratic cover defined by \(\sqrt{i}\) because \(i\) is a unit. This explains the last phrase while keeping the intermediate coordinate and its normalization distinct from the original anharmonic parameter.""",
    "T, cote 16, scan 52, supplies the Kummer background; no same two-stage quotient diagram occurs in T/N/D.",
    HUA,[r"Kummer",r"racine",r"quotient",r"invariant"],
    "High for the elementary coordinate comparison once the three-section trivialization is justified.")

add("C15",C,"The last page gives a precise quotient-stack description","050","equivariant t and margin marked ‘fonctoriel’",
    "unpursued implication",
    "“t … disjoint de 0,1,∞”; “λt=1/t”, “μt=1−t”.",
    r"""The data are exactly an \(S_3\)-torsor \(T\to S\) together with an equivariant map \(T\to U=\mathbf P^1-\{0,1,\infty\}\), hence an object of \([U/S_3]\). The descended pointed trisection and its inverse construction preserve morphisms as well as isomorphism classes, giving a precise functorial version of the manuscript's description (Stacks Project, n.d., Tag 04UV). This formulation remains valid across the special fibres and retains the infinitesimal data that the scalar invariant forgets.""",
    "R, Hua 62-triples-rigidified-moduli, anticipates this subject; T, cote 16, scan 56, supplies the underlying descent idea; no equivalent full triple construction is already in T/N/D.",
    HUA,[r"62-triples",r"descente",r"fonctor",r"étale"])

add("C16",C,"These triples forget the quadratic twist of an elliptic curve","016, 042–050","double-cover interpretation and final classification",
    "own idea",
    "“courbes … de genre 0”; “section et … trisection”.",
    r"""Passing from an elliptic curve to its quotient by inversion remembers the branch trisection and marked fourth branch point, but generically forgets the deck involution and the quadratic twist of the double cover. Over a field of characteristic different from two, the curves \(y^2=f(x)\) and \(dy^2=f(x)\) have the same branch data, while they need not be isomorphic as elliptic curves when \(d\) is nonsquare and the generic automorphism group is \(\{\pm1\}\). Consequently \([U/S_3]\) is the rigidified branch-data moduli problem, and should not be identified with the entire elliptic moduli stack without the extra double-cover datum.""",
    "T, cote 54, scan 3, studies abelian schemes with their full group structure; R's Hua entry says ‘triples’, which is compatible with this narrower object; cote 62 adds the explicit reason the two moduli problems differ.",
    HUA+" WG2 §1.1 #3: elliptic/Picard placement with a precise object distinction.",
    [r"62-triples",r"V.A.",r"duale",r"courbe",r"involution"],
    "High: quadratic twisting changes the double cover while leaving its branch divisor and quotient unchanged.")

add("C17",C,"The complete local example is an orbit description after a choice","050","last paragraph, ‘non fonctoriel’ margin",
    "unproved claim",
    "“π₁(S)=0”; “Donn. non canonique” [reading uncertain].",
    r"""A complete local ring in the usual adic sense is Henselian, and with algebraically closed residue field every finite étale cover is a disjoint union of copies of the base; this validates the torsor trivialization used here (Stacks Project, n.d., Tags 03QD and 04GK). Choosing a trivialization leaves the six anharmonic transforms acting on \(t\in O^\times\) with \(t-1\in O^\times\), exactly the orbit relation written on the page. The choice is noncanonical, and automorphisms at special or infinitesimal parameters remain part of the groupoid even when a set of orbits describes isomorphism classes.""",
    "T, cote 16, scan 56, already discusses finite étale splitting after base change; this is a concrete strictly Henselian specialization, not a general global trivialization.",
    HUA,[r"hens",r"étale",r"revêt",r"non canoni"])

add("C18",C,"What the Hua lead is and is not supported by","042–050, especially 047 margin","trisection discussion and interleaved reused faces",
    "reading question",
    "“Ceci ne nous a pas donné de façon très explicite de classifier”.",
    r"""The supplied excerpt of Hua's findings register correctly identifies the trisection-plus-section problem, and scans 042, 044, 046, 048, 050 provide the main text, with scan 047 adding a handwritten diagram of the two triples over a reused algebra typescript. Its consecutive page range interleaves distinct textual layers, and its continuation through manuscript page 53 extends beyond the present selection, so that continuation has not been checked here. The torsor/equivariant-map description is supported, but an unrestricted equivalence with scalar-invariant or constant-stabilizer classifications needs the qualifications in C05 and C11–C13. No novelty conclusion follows from the excerpt's statement that a previous search found no reference.""",
    "R, section ‘Findings of another project’, sole entry 62-triples-rigidified-moduli; README labels earlier materials as claims; the present scan-by-scan checks refine the claim without treating its intake status as a theorem.",
    HUA,[r"62-triples",r"Hua",r"new to us",r"claims",r"not yet"])

add("C19",C,"The orbifold model is useful evidence but not a completion theorem","028–050","S₃ action and final descent",
    "own idea",
    "“σ.t=…σ̄(t)”; the two generating formulas on scan 050.",
    r"""The explicit action and the quotient-stack description give a concrete model for the orbifold \([(\mathbf P^1-\{0,1,\infty\})/S_3]\) occurring in the results register. Its order-two and order-three stabilizers, branch coordinate, and cyclotomic form can be supplied to any later study of its fundamental group or relative completion. Nothing here constructs that completion or verifies its claimed kernel or universal property.""",
    "R, LM7 E.30, is the directly matching return claim; T/N/D has no relative-completion proof for this quotient; the manuscript adds explicit geometric input only.",
    "LM7 E.30 (return's claim, not newly certified).",
    [r"LM7 E.30",r"orbifold",r"relative completion",r"complétion"],
    "High as an identification of the displayed moduli object; no inference is made about the registered completion result.")

add("C20",C,"Finite geometric normalizers do not decide the profinite questions","030, 040","normalizer and reciprocal action",
    "own idea",
    "“normalisateur … Aut P¹_S”; “σ′=σ″=1/t”.",
    r"""The normalizer calculation lives in algebraic automorphisms of a projective line and is a controlled finite geometric example. It neither evaluates the character governing the extra full-GT CM coset nor rules out procyclic subgroups in an arithmetic common kernel; those are different groups and representations. The reviewed reduction in the register should therefore be retained as given, with this packet adding no new evaluation of its remaining obstruction.""",
    r"R, LM7_PUSH E.3 and E.65, separates the open CM image from the reviewed character reduction; LM6 A.22 and LM8 G.20 concern arithmetic normalizers; LM4 D.32 is a reviewed finite/profinite test, not the present \(\mathrm{PGL}_2\) theorem.",
    "LM7_PUSH E.3; LM7_PUSH E.65 (reviewed); LM6 A.22; LM8 G.20; LM4 D.32 (reviewed).",
    [r"LM7_PUSH E.3",r"LM7_PUSH E.65",r"LM6 A.22",r"LM8 G.20",r"LM4 D.32"],
    "High for the scope distinction: the manuscript specifies its ambient group and contains none of the arithmetic character data.")

add("C21",C,"A section of a conic bundle is not an arithmetic section classification","044–050","section s and complete local example",
    "own idea",
    "“une section s de X … sur S”.",
    r"""The section here is a geometric morphism \(S\to X\) disjoint from a finite divisor, described through an \(S_3\)-torsor and an equivariant coordinate. It does not classify continuous splittings of arithmetic fundamental-group extensions, and the strictly Henselian example does not test the open arithmetic lifting fibres in the register. Its useful contribution is a finite descent model in which one can see exactly which scalar invariants discard data.""",
    "R, LM6 E.21, LM7 E.23, and LM6 F.15, records unresolved section/lifting problems; T/N/D has no bridge identifying those sections with the conic sections in cote 62.",
    "LM6 E.21; LM7 E.23; LM6 F.15: no status change.",
    [r"LM6 E.21",r"LM7 E.23",r"LM6 F.15",r"section"],
    "High: the two meanings of section have different definitions and targets.")

add("C22",C,"The trisection kills the Brauer obstruction without choosing coordinates","042, 050","Brauer–Severi curve with étale trisection",
    "own idea",
    "“schéma de Br. Severi … muni d'une trisection”.",
    r"""If \(D=X'\) is the trisection divisor on the smooth genus-zero curve, the line bundle \(\mathcal O_X(D)\otimes\omega_{X/S}\) has relative degree one, so its rank-two direct image identifies \(X\) with a projective bundle. Thus the trisection already kills the Brauer obstruction to being \(\mathbf P(E)\), although the rank-two bundle need not be globally trivial and no preferred coordinate is supplied. Over a field this recovers the familiar fact that the conic is split; it does not choose an ordering of the cubic étale divisor or remove the torsor data.""",
    "T, cote 16, scans 21–23, studies Brauer groups and Kummer sequences; this is a concrete genus-zero consequence not stated in that context; it refines the object classified by R's Hua lead.",
    HUA,[r"Brauer",r"Kummer",r"62-triples",r"diviseur"],
    "High: degree 3 plus relative canonical degree −2 gives a degree-one line bundle, and relative genus-zero cohomology supplies the projective-bundle identification.")

add("C23",C,"The involution-fixed bisection and sign cover are cyclotomic twists","040, 042, 048","normalized invariant, descended bisection, and √i",
    "own idea",
    "“bi-section”; “√i”.",
    r"""On the locus where \(i\) is invertible, the involution-fixed bisection of C14 has quadratic class \(i\), whereas the sign quotient of the ordering torsor has class \(-3i\). Indeed, \(r=F(t)/[t(t-1)]\) changes sign under both anharmonic transpositions and satisfies \(r^2=-27i\), giving that second quadratic cover on this locus. The two covers differ by the cyclotomic class \(-3\), explaining why the constant-alternating-subgroup interpretation can fail at \(i=1\). They become identified after splitting the cyclotomic cover, but should not be conflated over the original base.""",
    "T, cote 16, scan 52, n°5, and N, 16:52:8, distinguish tame root extraction from its root-of-unity qualifications; R's Hua lead requires this distinction in the special-invariant classification.",
    HUA,[r"Kummer",r"16:52:8",r"racine",r"62-triples"],
    "High: the two sign substitutions and square identity are checked exactly in algebra_checks.json, while C14 identifies the separate fixed bisection.")

add("C24",C,"Lifting a triple to an elliptic curve has a square-root obstruction","014, 016, 042–050","weights, inversion quotient, and trisection classification",
    "own idea",
    "“μ²−λ³=0”; “section et … trisection”.",
    r"""Centering the cubic of a pointed trisection over a base with 6 invertible yields a line \(L\) with coefficients \(a\in L^{\otimes2}\), \(b\in L^{\otimes3}\), and invertible discriminant. An elliptic lift requires a line \(M\) and an identification \(M^{\otimes2}\simeq L\), so the same coefficients have weights four and six, consistently with the Weierstrass presentation (Stacks Project, n.d., Tag 072S). Thus the map from elliptic curves to these triples is a \(\mu_2\)-gerbe with the square-root obstruction in \(H^2(S,\mu_2)\); after fixing one lift and its identification with the triple, isomorphism classes of lifts form an \(H^1(S,\mu_2)\)-torsor. This specifies the global obstruction and twisting choices behind the field-level example in C16.""",
    "T, cote 16, scan 21, §8.2, supplies Kummer/Brauer language, while T, cote 54, scan 3, retains full abelian-scheme structure; neither identifies this particular square-root gerbe; R's Hua entry describes the rigidified triple problem.",
    HUA,[r"Brauer",r"Kummer",r"62-triples",r"duale"],
    "High: centering removes translation, the two scaling actions have weights (2,3) and (4,6), and their squaring map has kernel μ₂; the Kummer obstruction is the obstruction to a square root of L.")

D = "4. The reused algebra typescripts and their annotations"

add("D01",D,"Artin–Rees is a genuine completion link","020","§2, Theorem 1 and lemma",
    "unpursued implication",
    "“La topologie m-adique … est induite”.",
    r"""The stated Noetherian and finite-module hypotheses are exactly those used by the Rees-module proof of Artin–Rees, which makes the intrinsic and induced adic filtrations cofinal (Stacks Project, n.d., Tag 00IN). The proof on this supplied face stops while constructing the graded module, so its missing continuation is not transcribed from a printed edition. This tool is relevant to exactness of completion in the separate cancelled context sheet, without identifying that sheet with the Jacobians programme.""",
    "T, cote 44, scan 3, has the cancelled graded-completion assertion; N, D07, distinguishes exactness from faithfulness; cote 62 contributes a relevant proof tool, not an earlier Th. 1–7.",
    "WG2 §2.4 #4: completion overlap only.",
    [r"complét",r"Artin",r"exact et fidèle",r"D07"])

add("D02",D,"The series criterion uses a non-Archimedean filtration","022","Proposition 4",
    "unpursued implication",
    "“toute série … dont le terme général tend vers 0”.",
    r"""The criterion is valid because the filtration gives the strong triangle inequality, so a sequence is Cauchy precisely when its successive differences tend to zero. It must not be generalized to arbitrary metric vector spaces, where terms tending to zero do not make a series converge. The handwritten remark about metrizable topology concerns the completeness/quotient discussion and does not remove the ultrametric hypothesis from the series criterion.""",
    "T, cote 44, scan 3, uses degree/adic filtrations; N, D07, does not discuss this series criterion; the connection is the convergence mechanism used to lift graded generators.",
    NONE,[r"filtration",r"complét",r"topolog",r"D07"])

add("D03",D,"Complete need not mean separated in this typescript","022–024","Corollary 1 and coefficientwise sums",
    "reading question",
    "“Tout module quotient … est complet”; “on ne suppose pas A séparé”.",
    r"""The explicit disclaimer on scan 024 fixes the convention: completeness permits a non-Hausdorff topology and therefore nonunique sums. An arbitrary quotient can be complete in this sense, while a separated complete quotient requires the submodule to be closed. Reading “complete” as automatically separated would create a false contradiction in the printed corollary.""",
    "T, cote 44, scan 3, and N, D07, involve an exactness/faithfulness question rather than this convention; cote 62 supplies an explicit separation distinction that should be retained in any comparison.",
    NONE,[r"sépar",r"complét",r"quotient",r"D07"])

add("D04",D,"The product-filtration inequality is reversed as written","024","first displayed inclusions",
    "own idea",
    "“A_pE×A_qF⊂A_n(E×F) … (p,q≤n)”.",
    r"""For a decreasing filtration the first inclusion generally needs sufficiently large \(p,q\), not the written \(p,q\leq n\). For example \(A=k[[u]]\), \(E=F=A\), \(A_n=u^nA\), and \(p=q=0,n=1\) would assert \(A^2\subset uA^2\), which is false. The intended product-topology conclusion remains valid, but the displayed index condition cannot justify it as it stands.""",
    "T, cote 44, scan 3, likewise uses an adic filtration; no parallel inequality or correction was found in T/N/D.",
    NONE,[r"filtration",r"adique",r"complét"],
    "High: the explicit power-series counterexample refutes the written inclusion.")

add("D05",D,"The marginal coefficient-topology request can be made precise","024–026","Proposition 5 and pencil margin",
    "self-flagged",
    "“Dire que … conv. simple des coefficients” [several words uncertain].",
    r"""For \(\mathfrak n=(\mathfrak m,X)\), membership in \(\mathfrak n^p\) means \(a_j\in\mathfrak m^{p-j}\) for \(j<p\), with no restriction on the higher coefficients. These finite coefficient conditions generate exactly the product of the \(\mathfrak m\)-adic topologies on the coefficient copies of \(A\), explaining the marginal request for a coefficientwise description. The summation proof uses completeness of each coefficient and then those finite simultaneous conditions, without requiring separatedness.""",
    "T, cote 44, scan 3, also compares products of homogeneous pieces with completion, but for a graded ring/module; N, D07, warns that its finite-type category still matters.",
    NONE,[r"prod",r"complét",r"homogène",r"D07"],
    r"High for the coefficient criterion: it follows by expanding the finite power \((\mathfrak m,X)^p\).")

add("D06",D,"The filtered-surjectivity proof is not on the supplied continuation","026","Proposition 6, hypotheses a–c",
    "unproved claim",
    "“E … complet”; “F … séparé”; “G(u) … surjectif”.",
    r"""The supplied face ends after the hypotheses, so its conclusion and proof are physically absent from this selection. The standard intended mechanism successively lifts a target element modulo deeper filtration pieces, sums the corrections in the complete source, and uses separatedness of the target to identify the limit; it yields strict surjectivity under the usual exhaustive filtration conventions. This is an editorial reconstruction of a proof method, not a completion of the transcription.""",
    "T, cote 44, scan 3, gives a different completion statement; N, D07, has no missing continuation of this proposition; cote 62 scans 049 and 047 show subsequent uses of the same graded-lifting method.",
    NONE,[r"filtration",r"surject",r"complét",r"D07"])

add("D07",D,"Completion preserves the filtration quotients","041","quotient comparison and associated graded ring",
    "unpursued implication",
    "“E/E_n→Ê/Ê_n … bijectifs”; “G(A) et G(Â) … isomorphes”.",
    r"""The filtration quotients are discrete and already complete, so the completion leaves them unchanged and consequently preserves the associated graded object; they need not be finite sets or finite modules. This does not identify the underlying ring with its completion or prove that completion is faithful on every module category. The reference to the topology of unhatted \(A\) in the paragraph defining the filtered completion is a local wording question, since the surrounding construction concerns \(\widehat A\).""",
    "T, cote 44, scan 3, and N, D07, explicitly raise exactness and faithfulness; cote 62 supplies the graded-quotient comparison but not all of that cancelled sheet's categorical hypotheses.",
    "WG2 §2.4 #4: tool connection, not Jacobians programme evidence.",
    [r"exact et fidèle",r"complét",r"gradu",r"D07"])

add("D08",D,"The completion lemma needs strict topological homomorphisms","043","Lemma 1 and marginal ‘topologt’",
    "reading question",
    "“homomorphismes topologiques”; marginal “topologt|topol.?”",
    r"""In the older terminology, a topological homomorphism may mean that the quotient topology agrees with the topology induced on the image, a condition now often called strictness. Mere continuity does not suffice: the identity \(\mathbf Q_{\mathrm{discrete}}\to\mathbf Q_{\mathrm{usual}}\), followed by the zero map to zero, is exact, whereas completion gives \(\mathbf Q\to\mathbf R\to0\), which is not exact in the middle. The lemma is therefore to be compared with strict exact sequences, not arbitrary algebraically exact sequences of continuous maps.""",
    "T, cote 44, scan 3, asserts exactness under unresolved qualifications; N, D07, already separates its graded category from unrestricted modules; this typescript supplies an explicit topological hypothesis that cannot be dropped.",
    "WG2 §2.4 #4: the completion overlap does not close the separate programme.",
    [r"topolog",r"exact",r"D07",r"complét"],
    "High for the continuity-only counterexample; medium for the historical terminology until its unprovided definitions are consulted.")

add("D09",D,"Strict maps are not closed under arbitrary composition","043","last sentence of the lemma's proof",
    "own idea",
    "“le composé de deux homomorphismes est un homomorphisme”.",
    r"""If this last sentence intends strict topological homomorphisms, it is too broad: for irrational \(\alpha\), the maps \(\mathbf Z\to\mathbf R,\ n\mapsto n\alpha\), and \(\mathbf R\to\mathbf R/\mathbf Z\) are strict, but their composite has dense image carrying a nondiscrete induced topology and is not strict. The particular exact-sequence argument can instead use the factorization into quotient maps and closed embeddings, with closure verified in the exact situation. This diagnoses a proof shortcut without refuting the strict completion lemma itself.""",
    "T, cote 44, scan 3, and N, D07, do not contain this topological composition claim; the present example refines the completion-tool connection.",
    NONE,[r"homomorph",r"topolog",r"complét",r"D07"],
    r"High: \(\alpha\mathbf Z\) is closed discrete in \(\mathbf R\), but its image modulo \(\mathbf Z\) is dense and nondiscrete.")

add("D10",D,"The target of the extended quotient map appears unhatted","045","paragraph defining H=E/F",
    "reading question",
    "“Ê→H”; next display “Ê/F̂→widehat(E/F)”.",
    r"""The canonical extension of a map from \(E\) to \(H\) generally lands in \(\widehat H\), while the recorded first extension here still has target \(H\). The immediately following displayed map has the completed quotient as target and the next page develops its comparison with \(\widehat E/\widehat F\). This is a local missing-hat question, not a reason to assume \(H\) was already complete without a stated hypothesis.""",
    "T, cote 44, scan 3, also distinguishes completed modules from original modules; N, D07, gives no second version of this line.",
    NONE,[r"complét",r"quotient",r"D07"])

add("D11",D,"The noetherian enveloping-algebra claim needs finite generation","047, 045","Corollary 5 and its printed next-page proof",
    "own idea",
    "“Soit g une algèbre de Lie … K … noethérien”.",
    r"""As written on the supplied face, no finiteness hypothesis on \(\mathfrak g\) accompanies the assertion that \(U(\mathfrak g)\) is left and right Noetherian. For the infinite-dimensional abelian Lie algebra \(\bigoplus_{n\geq1}ke_n\), its enveloping algebra is \(k[x_1,x_2,\ldots]\), and the ideals \((x_1)\subset(x_1,x_2)\subset\cdots\) do not stabilize. Finite generation of \(\mathfrak g\) as a \(K\)-module repairs the indicated filtered proof, since its associated graded algebra is a quotient of a polynomial algebra in finitely many variables; full PBW injectivity is not needed for that argument. An unprovided standing convention might have supplied the hypothesis, but it is not visible in this selection.""",
    "T, cote 54, scan 7, treats restricted Lie algebras of finite group schemes, a different setting; no matching universal-enveloping statement occurs in T/N/D.",
    NONE,[r"Lie",r"envelopp",r"noeth",r"type fini"],
    "High: the infinite abelian example is explicit and the ascending ideal chain is immediate.")

add("D12",D,"The marginal question beside formal power series","047","Corollaries 2–3 and pencil circles",
    "self-flagged",
    "“?” beside “un anneau commutatif noethérien”; “un corps” circled.",
    r"""The visible question mark and circles flag the stated hypotheses, but do not specify whether the writer doubts the theorem, wants a stronger version, or questions the exposition. The displayed proof of Noetherianity for \(A[[X]]\) uses completeness and the Noetherian associated graded ring \(A[X]\); the many-variable field corollary could equally be stated over a commutative Noetherian ring. The annotation's intention remains open rather than being assigned the nearby enveloping-algebra counterexample.""",
    "T, cote 44, scan 3, mentions Noetherian graded rings in its completion hypothesis; N, D07, does not explain these circles.",
    NONE,[r"noeth",r"complét",r"D07"])

add("D13",D,"Lifting noetherianity from the associated graded object","047–049","Corollary 4 and graded-module corollaries",
    "unpursued implication",
    "“G(E) … de type fini (resp. noethérien)”.",
    r"""The mechanism is to lift finitely many homogeneous generators and correct successive filtration errors, then apply the same argument to every submodule with its induced filtration. Completeness belongs to the coefficient ring and separatedness to the target module in the written formulation; these hypotheses are doing real work and should accompany any reuse of the criterion. The first congruence on scan 049 lacks a summation sign even though the immediately following graded equation has one, a local textual inconsistency retained in the transcription.""",
    "T, cote 44, scan 3, and N, D07, are a relevant but different finite-generation/completion problem; the current text gives a lifting tool without proving faithfulness on arbitrary modules.",
    NONE,[r"type fini",r"gradu",r"complét",r"D07"])

add("D14",D,"The complete-ring Nakayama statement does not assume E finite","049","Corollary 3",
    "unpursued implication",
    "“A complet et E séparé”; “ils engendrent E”.",
    r"""The statement is stronger in form than the elementary finite-module Nakayama lemma because finite generation of \(E\) is a conclusion. Starting with generators modulo \(\mathfrak mE\), one corrects coefficients in successive powers of \(\mathfrak m\); completeness supplies their limits and separatedness of \(E\) makes the error vanish. Without separatedness, \(A=k[[t]]\), \(\mathfrak m=(t)\), and \(E=k((t))\) give \(E/\mathfrak mE=0\) but \(E\ne0\), defeating the empty-generator conclusion.""",
    "T, cote 44, scan 3, and N, D07, already expose the danger of unrestricted faithfulness assertions; this is a related complete-ring generation criterion, not a proof of the cancelled claim.",
    NONE,[r"sépar",r"type fini",r"exact et fidèle",r"D07"])

add("D15",D,"Residue separation and full valuation approximation are distinct","029, 031","Corollary 2 and extension-count proof",
    "reading question",
    "“v_i(x_i)=0 … v_j(x_i)>0”; “deux à deux indépendantes”.",
    r"""Scan 031 invokes the weaker residue-separation corollary for incomparable extension valuation rings, not the full approximation theorem stated under pairwise independence on scan 029. In higher rank, different prolongations can share a nontrivial coarsening and therefore need not be independent. Keeping those two hypotheses separate preserves the proof's actual logical structure; the distinction is also explicit in modern work on valuation approximation (Anscombe et al., 2020, Theorem 1.2 and §5.2).""",
    "T, cote 16, scans 52 and 54, discusses valuation extensions and ramification but does not contain this proof; cote 62 provides a tool relevant to the normal-base reconstruction, not its automatic solution.",
    NONE,[r"valuation",r"ramifi",r"extension",r"indépend"])

add("D16",D,"The extension-count proof ends mid-argument","031","last paragraph",
    "unproved claim",
    "“Montrons … le nombre … ≤n”.",
    r"""The displayed linear-independence argument normalizes a coefficient of minimal base valuation and then should reduce at the corresponding valuation ring, leaving exactly one residue-unit term. This gives the bound on the number of distinct extensions, but the supplied face stops before that final reduction. It is distinct from the separate ramification-index/residue-degree inequality on scan 039.""",
    "T, cote 16, scan 52, asks for a ramification analysis; no exact continuation of this typescript was found in T/N/D.",
    NONE,[r"valuation",r"ramifi",r"degré",r"trace"])

add("D17",D,"Places into an algebraically closed field are not field homomorphisms","035, 033","Propositions 3–4 and maximal-pair argument",
    "unpursued implication",
    "“f→f(0)”; “une place … l'identité sur k”.",
    r"""The Zorn argument extends a place, so evaluation at zero on \(F(X)\) is understood as a place with its valuation-ring domain and possible value infinity, not a homomorphism defined on every rational function. Algebraic closedness then forces the finite/algebraic residue extension at the maximal stage back into \(k\). This explains why the statement can hold for a transcendental extension without requiring an impossible embedding into its base field.""",
    "T, cote 16, scans 52 and 54, uses valuation-ring and residue constructions; no same maximal-place argument occurs in T/N/D.",
    NONE,[r"place",r"valuation",r"résidu",r"algébriquement"])

add("D18",D,"The Samuel remark is an editorial question about retention","033","long square-bracketed paragraph",
    "self-flagged",
    "“Est-ce que cela en vaut la peine ?”; “sur les instances de Samuel”.",
    r"""The bracket asks whether to move the result earlier and whether to retain a proposition inherited from earlier drafts, while explicitly leaving the decision to another reader. It is evidence of an editorial exchange, not a conjecture about elliptic curves or proof that the typed voice is Grothendieck's. Identifying the contributor or a published version would require provenance evidence beyond the name Samuel and the typescript number.""",
    "T, cote 54, scans 4, 6, 8, and cote 44, scan 3, also preserve reused or separate algebra material; N, D06–D07 and D15, does not establish a common author or edition.",
    "WG2 §1.1 #3: mixed textual layers matter to dossier placement.",
    [r"Samuel",r"rédact",r"D06",r"D07",r"D15"])

add("D19",D,"The ordered-group lemma can be stated independently","037","Corollary 1 and bracketed question",
    "self-flagged",
    "“Est-il nécessaire de dégager … les lemmes sur les groupes ordonnés”.",
    r"""The proof uses that a torsion extension of ordered value groups induces a bijection on convex (isolated) subgroups, hence preserves rank. For injectivity, if \(H'_1\cap G=H'_2\cap G\), every \(x\in H'_2\) has a positive multiple in \(G\), hence in \(H'_1\), and convexity forces \(x\in H'_1\); this avoids relying on the unelaborated claim that the quotient embeds in \(G'/G\). The printed question is about extracting and presenting that lemma, not an indication that the final rank statement is false.""",
    "T, cote 16, scan 52, uses discrete valuation rings, a narrower rank-one setting; no same convex-subgroup lemma occurs in T/N/D.",
    NONE,[r"valuation",r"ordonn",r"rang",r"groupe"])

add("D20",D,"Discreteness requires the finite-extension hypothesis","037, 035","Corollary 3 and its continuation",
    "unpursued implication",
    "“Supposons que L soit une extension finie de K”.",
    r"""Finite index in the value group makes a finite extension of a discrete rank-one valuation discrete, as the typescript proves. This should not be extrapolated to arbitrary algebraic extensions: adjoining all compatible roots of a uniformizer can make the value group nondiscrete, such as \(\mathbf Q\), while retaining rank one. The explicit finite-extension hypothesis therefore distinguishes discreteness from the preceding rank-invariance statement.""",
    "T, cote 16, scan 52, n°5, discusses finite tame root extraction; cote 62 makes the finite-versus-infinite distinction explicit through the value-group argument.",
    NONE,[r"uniformis",r"valuation",r"finie",r"rang"])

add("D21",D,"The ef inequality is a complete local proof on the retained face","039","minimal-valuation argument",
    "unpursued implication",
    "“les éléments x_i y_α sont linéairement indépendants”.",
    r"""Choosing representatives of distinct value-group cosets and independent residue classes gives linearly independent products by isolating the terms of minimum valuation and reducing their normalized sum. This proves \(ef\leq[L:K]\) for one extension valuation, matching the modern formulation in Stacks Project (n.d., Tag 0ASH). It does not prove equality, exclude defect, or alone control all extension valuations simultaneously.""",
    "T, cote 16, scan 52, n°4–5, concerns trace/different and ramification; the present proof is a concrete algebraic input, while scan 046 still asks for global étaleness.",
    NONE,[r"valuation",r"trace",r"ramifi",r"degré"])

add("D22",D,"Completion exactness and faithfulness remain separate","020, 041, 043, 045, 049","collective completion tools",
    "own idea",
    "“la suite … est exacte” (scan 043).",
    r"""The retained typescripts supply exactness tools under finite-generation or strict-topological hypotheses, but they do not recover the unresolved category qualification in cote 44's cancelled statement that completion is exact and faithful. The earlier return's example \(k[x]/(x-1)\) killed by \((x)\)-adic completion is an ungraded example and should not be advertised as refuting an assertion restricted to appropriately graded modules. The packet adds a precise comparison of proof tools, while preserving that category-dependent limit.""",
    "T, cote 44, scan 3; N, D07 and 44:3:1–5, already identifies the exactness/faithfulness distinction and the ungraded example; the current return adds only the matching typescript hypotheses.",
    "WG2 §2.4 #4: no earlier form of Th. 1–7 is obtained.",
    [r"exact et fidèle",r"D07",r"44:3:",r"complét"],
    "High for the comparison and its limit: the categories and hypotheses are explicitly different.")

add("D23",D,"The completeness proof cites a different proposition number","022","proof of Corollary 1, final sentence",
    "reading question",
    "“E/F est complet d'après la proposition 1”.",
    r"""The proof uses convergence of every series whose terms tend to zero, which is the immediately preceding Proposition 4. Its terminal reference instead says Proposition 1, and the missing preceding typescript pages prevent checking whether that number also supplies an applicable criterion. The local mismatch should therefore be recorded without replacing the number from mathematical expectation.""",
    "No matching numbered completeness criterion occurs in T/N/D; T, cote 44, scan 3, and N, D07, concern completion but cannot settle this typescript cross-reference.",
    NONE,[r"proposition 1",r"complet",r"D07"])

add("D24",D,"The integral-closure and localization assertions lack their continuation","031","opening parts b), c) and truncated proof",
    "unproved claim",
    "“B … est la clôture intégrale”; “A_i=B_{p_i}”.",
    r"""Besides the extension-count bound, the opening asserts that the intersection of all prolongation valuation rings is the integral closure and that its localizations at the listed maximal ideals are precisely those rings. The retained proof only establishes incomparability and begins the counting argument, leaving these integral-closure and localization steps without a proof in this selection. Their use in reconstructing a normalization therefore requires a separate valuation-ring integrality and localization argument, not merely the numerical inequality.""",
    "T, cote 16, scans 52 and 54, raises ramification and algebraic-integrality questions; no continuation of parts b), c) appears in T/N/D; internally this bears on cote 62, scan 046, without supplying its everywhere-étale criterion.",
    NONE,[r"clôture",r"intégral",r"valuation",r"ramifi"])

E = "5. The direct Oda comparison and the two planning questions"

add("E01",E,"Oda verifies a filtered degree-one comparison under specific hypotheses","004, 007–008, 017","Lie line and invariant derivations",
    "unpursued implication",
    "“faisceau de Lie”; “opérations de … T”.",
    r"""Oda's Corollary 5.11 gives, for an abelian scheme over a perfect field of characteristic \(p\), a canonical isomorphism between the Dieudonné module of its p-torsion and \(H^1_{\mathrm{dR}}\), carrying the indicated \(V\)-submodule to \(H^0(\Omega^1)\) and matching the Hodge exact sequence (Oda, 1969, p. 131; supplied PDF page 70). That printed statement was checked directly here, so the corresponding literature claim in the earlier notes is supported within those hypotheses. Cote 62's pole filtration and Lie line give a dimension-one setting for comparison, but do not by themselves construct all operators or identify the particular restricted-Lie extension in cote 54.""",
    "T, cote 54, scans 3, 5, 7; N, D03–D05, already cites this Oda comparison; O, p. 131/PDF 70, independently checked; the present addition is a precise scope check, not a new reconstruction theorem.",
    "WG2 §1.1 #3: concrete connection to the abelian/Picard dossier; no directly corresponding open result is resolved.",
    [r"D03",r"D04",r"D05",r"Oda",r"Lie"])

add("E02",E,"The tangent line is the dual of the Hodge line","004, 014–017","Lie normalization and inversion",
    "own idea",
    "“L … [dérivation invariante]”; “chgt de signe”.",
    r"""For an elliptic scheme, the line called Lie here is dual to the invariant-differential line, and in relative dimension one it is also its own determinant line as a rank-one bundle. This makes these pages a useful test case for the line factor and inversion sign in the Fourier formula, provided tangent/cotangent variance and the choice of dual abelian scheme are kept explicit. Such a convention check is logically prior to, and insufficient for, proving compatibility of the actual derived comparison map.""",
    "T, cote 54, scan 3, and N, D01–D02, already distinguish the universal-extension variance; T, cote 47, scans 5–8, introduces the determinant/Lie twist; cote 62 adds concrete coordinates and inversion.",
    "WG2 §2.4 #4: a possible testing method, not a second witness.",
    [r"t_A",r"t_B",r"tau",r"D01",r"D02",r"compatibilité"],
    "High for the line-bundle comparison; no claim is made that checking the line alone establishes the Fourier theorem.")

add("Q01",E,"Planning question: no completed second Fourier witness in this selection","002, 004–017, 019–026, 028–050","all retained pages, compared with cote 47",
    "reading question",
    "Context, cote 47, scan 8: “à faire une vérification de compatibilité.....”.",
    r"""No second witness completing that check is identified in these 46 scans: the exact outstanding step in T, cote 47, scans 7–8, is whether the particular canonical map \(Rp_*W\to e_*\tau[-n]\), constructed from top-degree base change and the identity on the determinant line, is an isomorphism after derived restriction at the unit. N, F7, gives a cone/perfect-complex proof plan and N, F8, a Tor/exterior-power comparison, but both retain the compatibility of that actual map as unfinished. The Lie and inversion calculations here do not construct the universal kernel or evaluate that fibre map. This is a negative finding for the supplied selection, leaving the archive-wide planning question open.""",
    "T, cote 47, scans 6–8, especially the admitted Lemma 2 on scan 7 and the unit-fibre sentence on scan 8; N, 47:8:1–2 and F6–F8; README's two planning questions; R, WG2 §2.4 #4.",
    "WG2 §2.4 #4 (unchecked planning question): bounded negative answer; no status upgrade for prior Fourier notes.",
    [r"compatibilité",r"47:8:",r"F6",r"F7",r"F8",r"Fourier",r"Weil"])

add("Q02",E,"Planning question: no earlier forms of cote 44's Theorems 1–7","002, 004–017, 019–026, 028–050","all retained pages, compared with cote 44",
    "reading question",
    "Context, cote 44, scan 2: “Programme de travail”.",
    r"""No earlier formulation of those seven theorems is identified in this selection: their exact context locations are scan 2 for Th. 1–4, scan 4 for Th. 5–6, and scan 6 for Th. 7, concerning abelian-variety structures on cycle quotients, complementary duality, polarization, height/intersection, Lefschetz behavior, and numerical versus tau equivalence. The concrete overlap is with the separate cancelled completion sheet at cote 44, scan 3, not those theorems. The already supplied Serre letter, dated “Bures le 12.8.1964” on cote 44, scan 8 and continued on scan 9, is a companion to the programme, but neither the undated programme nor this cote 62 selection establishes an earlier/later order. The archive-wide search remains open, and WG H9's proposed height/positivity interpretation receives no new proof here.""",
    "T, cote 44, scans 2–4, 6, 8–9; N, 44:2, 44:4, 44:6, D08–D14; R, WG2 §2.4 #4, WG2 §2.3 #12, WG H9; the exact target-statement concordance is also in records/research/context_questions.md.",
    "WG2 §2.4 #4; WG2 §2.3 #12; WG H9 (all unchecked planning/hunch entries): bounded negative answer.",
    [r"Programme de travail",r"Th. 1",r"Th. 7",r"Bures",r"WG H9",r"WG2 §2.4"])

front_matter = r"""
# MPL_62_002-050 — Research notes

## Scope and evidential status

These notes concern the 46 retained scans of cote 62: 002, 004–017, 019–026, and 028–050. The transcription, including all reused typescripts, drawings, cancellations, insertions, and margins, was visually read and audited by the primary transcriber; the research comparisons below began only after the 47 TeX files were frozen. The freeze and context-opening events were recorded sequentially at 18:57:54 UTC on 16 November 2026; the combined transcription's SHA-256 is 9d5b838824b3bf4663823f19a80d2c98330181407538c2af34143a0b6f2c6869.

The distinction between evidence and inference is maintained throughout. A manuscript assertion is not certified merely by being transcribed; an earlier working note is a claim unless checked; a result-register entry retains exactly its supplied review status. No source reading was changed after the context opened, and every proposed correction or qualification below belongs only to these notes. The primary transcriber wrote and checked the final notes; research assistants compared frozen text and literature only, without reading or auditing the manuscript images.

The most consequential mathematical checks concern the changing j normalization, the arithmetic and infinitesimal qualifications to the special-invariant classifications, the full étaleness condition in reconstruction over a normal base, and missing or ambiguous hypotheses in the reused algebra text. The two requested witness questions receive bounded negative answers in Q01–Q02. These findings do not assert an exhaustive archive search or historical priority.

## Source key and method of comparison

| Key | Exact supplied or delivered file | How locations are cited |
|---|---|---|
| C62 | MPL_62_002-050_transcription.tex and pages/MPL_62_002-050_62_scanNNN.tex | Cote 62, three-digit scan, paragraph/display |
| T | MPL_16+47+54+44_transcription.tex, from the context ZIP | Cote plus its scan number; not a second visual audit of the earlier return |
| N | MPL_16+47+54+44_notes.md, from the context ZIP | Exact prior note ID or section, with cote/scan from T |
| D | MPL_16+47+54+44_doubts.md, from the context ZIP | Earlier reading uncertainties, never a correction source for C62 |
| R | notes/RESULTS_STATE.md, from the context ZIP | Exact register ID and the supplied status |
| README | README.md, from the context ZIP | Placement and the two planning questions |
| O | Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf | Printed page and PDF page; p. 131 is PDF page 70 |

For every numbered item, the supplied textual context was searched for the same objects, words, and notation; queries, hit counts, source lines, cote/scan or heading, and selected short excerpts are preserved in records/research/context_searches.json. The context comparison beneath each note states whether the manuscript adds to, restates, differs from, or fails to match the prior material. Lexical absence alone is not treated as proof of mathematical absence: the closest substantive passages and the earlier dossier's overall subject were also compared. Search hits for a different kind of discriminant, a TikZ path called “cycle”, or a repeated theorem number were not treated as subject matches.

The note paragraphs are deliberately limited to one to four sentences per item. “Own idea” means an editorial deduction, example, or proposed qualification, never a claim of novelty; confidence measures the stated argument, not historical attribution. Confidence statements accompanying a different kind identify an editorial calculation inside that note. The symbols \(i\) and \(J\) in the analysis distinguish the late normalized invariant from the conventional elliptic j-invariant; this convention applies only to these notes. Unless a note specifies otherwise, the explicit anharmonic/cyclotomic calculations are made over bases with 6 invertible, as the manuscript eventually requires.
"""

back_matter = r"""
## 6. Standing question: steps the text itself flags as unfinished or uncertain

This index records the author's own marks and unfinished instructions, including questions answered later and editorial questions in the reused typescripts. It does not equate the transcriber's uncertainty macros with the author's doubt. The detailed note IDs carry the corresponding context searches and register comparisons.

| Cote / scan | Brief words or mark | What is flagged; status within this selection | Note |
|---|---|---|---|
| 62 / 005 | “connue par ailleurs”; “un raisonnement connu … RR” | Degree-zero cohomology and the final very-ampleness argument are invoked rather than supplied | A03–A04 |
| 62 / 005 margin | “prop. préliminaire sur un faisceau inversible …” | Expository instruction to state a preliminary result | A03–A04 |
| 62 / 006 | “Il faut prouver que” | Multiplication/generation proof request, followed by the direct argument on 007 | A05–A06 |
| 62 / 007 | “[reste à définir]” | Action on relative rational functions | A07 |
| 62 / 007 | “vérification locale” | Leading-pole calculation, supplied at the opening of 008 | A08 |
| 62 / 008 margin | “intervertir avec la prop. 2” [uncertain first word] | Reorder the intrinsic graded-line proof; not a doubt about every preceding formula | A10 |
| 62 / 010 margin | “préciser ce pt cf. intersections complètes” | Why the relation is the defining cubic | A14 |
| 62 / 011 | “Ici le discriminant s'explicite : —” | Explicit formula announced but left blank | A15 |
| 62 / 011 | “Il reste à écrire…” | Smoothness condition, immediately answered by requiring the discriminant to be a unit; distinct from the absent explicit polynomial | A15 |
| 62 / 012 | “[on peut aussi dire … ce sera plus clair” | Unfinished/revised reformulation of the group action; no closing completed alternate proof is supplied on that face | A16–A17 |
| 62 / 013 | “un raisonnement général … genre g” | General presentation asserted without development | A19 |
| 62 / 015 | “Il ne semble pas … moins de paramètres” | Explicit tentative expectation about characteristic-free normalization | A22 |
| 62 / 015 | “12.ième (…24.ième)” | Unresolved power qualification in a partly uncertain parenthesis | A23 |
| 62 / 015 | “puis … puis on verra” | Further normal forms announced | A24 |
| 62 / 017 | “on le verra” | Characteristic-free trivial action on E₂ promised | A26 |
| 62 / 017 | “Quelle est la normalisation correspondante … ?” | Locally answered by the preceding supplied scan 016, without establishing writing order | A30 |
| 62 / 019 margin | “à vérifier … géométriquement” | Kummer correspondences and special-invariant scratch work | B01–B02 |
| 62 / 021 | “Δ=…b³−27c² ?” | Discriminant calculation explicitly questioned; several other displays are left incomplete | B04 |
| 62 / 022 margin | “fait général pour les top. métrisables” [wording uncertain]; “!” | Generality of the completeness criterion; the mark need not indicate doubt | D02–D03 |
| 62 / 024 margin | “Dire que … conv. simple des coefficients” [uncertain wording] | Request to state the topology coefficientwise | D05 |
| 62 / 026 | Proposition 6 stops after a), b), c) | Physically unfinished in this selection; no authorial question mark is inferred | D06 |
| 62 / 028 margin | “renommer” [uncertain], “??”, revised labels | Naming and conjugation/table calculations are provisional | B07–B08 |
| 62 / 030 | “Prouver : le normalisateur …” | The normalizer theorem is a proof request | B09 |
| 62 / 030 bottom margin | Characteristic-exception wording is low-confidence in C62 | Possible bad-characteristic query; no more precise authorial assertion is reconstructed | B10 |
| 62 / 032 | “à expliciter…” | The three quotient sections | B12 |
| 62 / 033 | “Est-ce que cela en vaut la peine ?” | Editorial placement/retention of the place proposition | D18 |
| 62 / 035 | “On pourrait aussi déduire … mais … plus naturel” | Alternative organization of a proof; preference stated, not a mathematical conjecture | D20 |
| 62 / 036 | “[lui donner un sens, et justifier cette assertion…]” | Extending the square-map formula over the whole projective line | B14 |
| 62 / 037 | “Est-il nécessaire de dégager … les lemmes … ?” | Whether to isolate ordered-group lemmas | D19 |
| 62 / 040 | “Comment opère σ dans les quotients ?” | Answered on the page by the reciprocal formula, with verification only sketched | B17 |
| 62 / 040 | “il serait facile de … prouver” [partly uncertain] | Explicit reciprocal identities left as an easy verification | B17 |
| 62 / 042 | “[à préciser…]” | Recovering X′ from its associated X″ | C03 |
| 62 / 042 | “[par descente…]” | Construction of the bisection | C04 |
| 62 / 043 margin | “topologt|topol.?” [transcription alternatives] | Topological qualification near completion exactness; the uncertain question mark is not treated as secure authorial doubt | D08 |
| 62 / 044–046 | “[À déduire … des formalismes catégoriques généraux …]” [opening uncertain] | Identifying the invariant pullback with the ordering torsor | C05 |
| 62 / 046 | “quels i conviennent ??” | Admissible invariant values over a normal integral base | C06–C10 |
| 62 / 046 | “Il faut exprimer (i) … (ii) …” | Everywhere-unramified extension and rational-map extension conditions | C07–C10 |
| 62 / 047 | “ne semble pas présenter d'avantage très décisif” | Editorial assessment of the preceding proof, whose start is not retained | D12 |
| 62 / 047 margin | “?” and circled hypotheses of Corollaries 2–3 | Exact intention uncertain; distinguish it from the separate missing Lie-algebra hypothesis | D11–D12 |
| 62 / 050 | “Ceci ne nous a pas donné de façon très explicite de classifier” | The writer acknowledges the limited explicitness of the preceding classification | C15, C18 |
| 62 / 050 margins | “fonctoriel”; “non fonctoriel”; “Donn. non canonique” [partly uncertain] | Functorial torsor formulation versus a chosen local trivialization | C15, C17 |

The conspicuous cancellations with mathematical content are separately retained: Proposition 1 on scan 004 is restated on 005 (A02); the characteristic-dependent corollaries on 008 are replaced by the intrinsic divisor argument on that same scan (A09–A10); the seven-coefficient coordinate trial on 009 is cancelled before the six-coefficient construction (A11–A12); the proposed E₂ complement and L₆ complement on 017 are struck through (A27, A29). These are withdrawn draft layers, not automatically claims of falsehood.

## 7. Standing question: title sheets, headings, and page-count evidence

### Titles and explicit headings

| Cote / scan | Wording carried by the sheet | Kind and count evidence |
|---|---|---|
| 62 / 002 | “Courbes elliptiques” | Cover/title sheet; handwritten numeral 1; no stated total page count |
| 62 / 004 | “Modules des courbes elliptiques” | Subject heading; manuscript page 3 |
| 62 / 020 | “§2. — Anneaux m-adiques noethériens”; “1. — Restriction de la topologie m-adique à un sous-module” | Reused typescript n°276, printed page 20; handwritten page 19 |
| 62 / 022 | “4. — Modules filtrés complets” | Reused typescript n°276, printed page 9; handwritten page 21 |
| 62 / 026 | “5. — Modules de type fini sur un anneau filtré complet” | Reused typescript n°276, printed page 11; handwritten page 25 |
| 62 / 029 | “2. Valuations indépendantes” | Reused typescript n°272, printed page 39; handwritten page 28 |
| 62 / 033 | “3°. — Prolongements d'une valuation à une extension algébrique” [3° reading uncertain] | Reused typescript n°272, printed page 46; handwritten page 32 |
| 62 / 035 | “2. — Application : prolongement d'une place à valeurs dans un corps algébriquement clos” | Reused typescript n°272, printed page 45; handwritten page 34 |
| 62 / 045 | “7. — Complété d'un module filtré” | Reused typescript n°276, printed page 16; handwritten page 44 |

No retained cover or heading declares “19 pages”, “Pages 1–67”, or another total page count. Numerals carried by individual sheets are pagination, not automatically counts. The catalogue's “53” is supplied task metadata, not a page-count inscription found on one of these retained images. The “59/60”, “59”, and “60” embedded in the drawing on scan 026 are drawing labels and cannot alone date the elliptic manuscript.

### The two printed pagination systems

| Typescript number | Scan → printed page, in scan order | Scope caution |
|---|---|---|
| n°276 | 020→20; 022→9; 024→10; 026→11; 041→18; 043→17; 045→16; 047→15; 049→13 | Nine retained faces; printed pages 12, 14, and 19 are absent within this partial run; no total length is inferred |
| n°272 | 029→39; 031→47; 033→46; 035→45; 037→44; 039→43 | Six retained faces; printed pages 40–42 are absent between the retained extremes; no total length is inferred |

Every retained scan carries the handwritten page number one less than its scan number, from scan 002/page 1 through scan 050/page 49, with the supplied omitted blank scans 003, 018, and 027 not present. Thus three numbering systems coexist: archive scan number, handwritten page number, and the independent printed pagination on reused sheets. The inventory classifies 30 faces as subject text, 15 as reused typescript, and one as cover; a reused face may still carry subject-related handwriting, notably the trisection diagram on scan 047. The reversed printed sequence in part of the selection is not a secure chronology of composition.

## 8. Register consequences and limits

| Register entry | Supplied status used here | Contribution of this packet |
|---|---|---|
| WG2 §2.4 #4 | Unchecked planning question | Q01–Q02 give bounded negative witness findings and exact target locations |
| WG2 §2.3 #12; WG H9 | Unchecked programme description / hunch | No new proof of cycle representability, complementary duality, the height/intersection formula, or positivity |
| WG2 §1.1 #3 | Unchecked placement question | Concrete elliptic/Lie/moduli connections, plus identification of independent reused algebra strata |
| Hua, 62-triples-rigidified-moduli | Candidate claim; “new to us” intake | Subject confirmed; torsor description clarified; constant-group, reducedness, and moduli-object qualifications recorded |
| LM7 E.30 | Proved (the return's claim); no explicit referee marker | Explicit quotient-orbifold geometry; no new proof of relative completion |
| LM4 E.20 | Proved as the earlier return's claim; no explicit referee marker | Finite PGL₂ centralizer/normalizer example only |
| LM4 D.32 | Explicitly reviewed | Its prior test is not rederived or transferred to a different ambient group |
| LM7_PUSH E.3; E.65 | Open image problem / explicitly reviewed reduction | No evaluation of the remaining character; the reduction retains its supplied status |
| LM6 A.22; LM8 G.20 | Open in the supplied returns | No decision of the arithmetic procyclic-normalizer problem |
| LM6 E.21; LM7 E.23; LM6 F.15 | Open in the supplied returns | The conic-bundle section problem is distinguished from arithmetic section lifting |
| CYCLOTOMIC_KERNEL C1 | Prior claim with the register's review/intake qualifications | Finite Kummer distinctions only; no reproof or extension of a completed-torsor assertion |

No result-register status has been changed. Entries about other profinite kernels, arbitrary finite-action realization, or the vanishing-cycle/centralizer hunches receive no new evidence from these finite genus-zero computations. The source files named inside R were not included as full research returns in the context ZIP and are not represented here as independently opened or reviewed.

## 9. References and verification scope

Manuscript citations use cote and archive scan as the stable locator; the diplomatic uncertainties remain part of that evidence. The supplied context return is cited as a working transcription and working notes, not as an established scholarly edition. The original scans and context files are deliberately not duplicated in the deliverable ZIP.

Anscombe, S., Dittmann, P., & Fehm, A. (2020). Approximation theorems for spaces of localities. *Mathematische Zeitschrift, 296*, 1471–1499. https://doi.org/10.1007/s00209-020-02516-6. [Theorem 1.2 and §5.2; publication details and accessible primary text are recorded in the literature verification record.]

Grothendieck, A. (n.d.). *Courbes elliptiques (généralités — vieille rédaction)* [Unpublished manuscript, Montpellier archive, cote 62, selected scans 002–050]. Diplomatic transcription in this deliverable.

Grothendieck, A. (n.d.). *Selected manuscripts in cotes 16, 47, 54, and 44* [Unpublished archival material, as represented in the supplied working transcription MPL_16+47+54+44_transcription.tex]. The cote 44 letter is dated August 12, 1964; this does not date every other sheet.

Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l'École Normale Supérieure, 4e série, 2*(1), 63–135. https://doi.org/10.24033/asens.1175. [Corollary 5.11, printed p. 131; supplied PDF p. 70 directly inspected.]

Stacks Project. (n.d.). *The Stacks Project*. Retrieved November 16, 2026, from the following stable tags:

| Tag | Exact result used | URL |
|---|---|---|
| 00IN | Lemma 10.51.2, Artin–Rees | https://stacks.math.columbia.edu/tag/00IN |
| 032L | Lemma 10.161.8, finiteness of integral closure in a finite separable extension of a Noetherian normal domain | https://stacks.math.columbia.edu/tag/032L |
| 03PK | §59.28, Kummer exact sequences and torsors | https://stacks.math.columbia.edu/tag/03PK |
| 03QD | §59.32, especially Theorem 59.32.3, complete local rings are Henselian | https://stacks.math.columbia.edu/tag/03QD |
| 03VA | §64.24, the Legendre family | https://stacks.math.columbia.edu/tag/03VA |
| 04GK | Lemma 10.153.7, finite étale algebras over a Henselian local ring and its residue field | https://stacks.math.columbia.edu/tag/04GK |
| 04UV | §95.15, quotient stacks via torsors and equivariant maps | https://stacks.math.columbia.edu/tag/04UV |
| 072S | §105.6, the Weierstrass smooth cover and quotient-stack presentation | https://stacks.math.columbia.edu/tag/072S |
| 0A1G | §36.30, proper flat cohomology, perfect complexes, and base change | https://stacks.math.columbia.edu/tag/0A1G |
| 0ASH | Lemma 15.125.2, the valuation-theoretic fundamental inequality | https://stacks.math.columbia.edu/tag/0ASH |
| 0H2V | Lemma 53.22.5, degree at least 2g+1 implies very ampleness | https://stacks.math.columbia.edu/tag/0H2V |

The explicit polynomial, Möbius, and infinitesimal calculations in B04–B17 and C09–C13 are editorial calculations, with reproducible checks in records/research/algebra_checks.json and its generating script. They are not attributed to a publication and are not claims of novelty. Literature cited only inside the prior notes, including their broader Fourier, Jacobian, height, and algebraic-representative comparisons, remains prior-context leads unless explicitly rechecked above.
"""

if __name__ == '__main__':
    data = dict(front_matter=front_matter, notes=notes, back_matter=back_matter)
    out = ROOT / 'records/research/notes_entries.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(notes)} research notes written to {out}')

