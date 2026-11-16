## A. Determinants, tensor operations, and coefficient hypotheses

### F01 — Characteristic polynomials and exterior traces

**Witness:** 60/003, opening display; **kind:** unproved claim; **quote:** “on pose”. **Context query:** `characteristic polynomial|car. pol.|endomorphisme`; **comparison:** CT 16/048 uses rational characteristic coefficients to recover an inverse, whereas this page supplies the underlying linear determinant identity. **RS:** bears on WG2 §2.4 #3 and WG2 §6. #9 only at the linear-algebraic level.

The equality \(\det(1-ft)=\sum_i(-1)^i\operatorname{Tr}(\Lambda^if)t^i\) requires no semisimplicity: after extension to an algebraic closure, triangularize f and compare elementary symmetric functions of its diagonal entries. Zero eigenvalues explain why the roots are inverses only of nonzero eigenvalues, a restriction the manuscript states explicitly. This identity does not supply the rationality of characteristic coefficients for algebraic correspondences over a rational coefficient field in CT 16/048.

### F02 — Symmetric powers and exact-sequence multiplicativity

**Witness:** 60/003, middle displays; **kind:** unproved claim; **quote:** “suite exacte … produit des polynômes”. **Context query:** `groupe de Grothendieck|suite exacte|rang virtuel`; **comparison:** CT 16/035 defines a split Grothendieck group in a reused Karoubi typescript, while CT 47/008 uses a virtual rank in a different derived setting. **RS:** MPL_15_195-228+18_002-017 R01 is a relevant first-pass warning about treating reused text as motivic evidence; no exact RS theorem settles this item.

For an f-stable short exact sequence, an adapted basis makes f block triangular, so characteristic polynomials multiply and their reciprocals do as well. The symmetric-power trace identity follows by expanding the product of geometric series, including in positive characteristic; it does not require division by factorials. The word “additif” therefore concerns addition in a Grothendieck group mapping to ordinary multiplication of series, not addition of rational functions.

### F03 — The written product is the rational Witt construction

**Witness:** 60/003 and 005; **kind:** unpursued implication; **quote:** “(1−at)*(1−bt)=1−abt”. **Context query:** `Grothendieck|produit tensoriel|lambda|sigma`; **comparison:** CT 16/035 gives a separate K-group construction and CT 47/009 uses Chern operations, but neither supplied passage identifies this rational-function multiplication. **RS:** WG2 §2.4 #3, with no construction of motives inferred.

The elementary-factor rule identifies the polynomial/quotient part with the rational Witt ring, with ordinary series multiplication serving as addition and tensor product supplying the second multiplication. Blumberg et al. (2013, introduction and §6; published 2016) use precisely this rule and describe the rational subring; that is a later mathematical comparison, not a dating or priority claim about the present undated pages. The finite-polynomial restriction on scan 007 is consequently structural, not merely a convergence warning.

### F04 — Reciprocal L-functions change the additive sign convention

**Witness:** 60/005, first and last displays; **kind:** reading question; **quote:** “L … = 1/(L*L)”. **Context query:** `sigma|lambda|produit|K^`; **comparison:** CT 47/009 has formal Chern powers but no matching tensor-L convention. **RS:** no exact matching entry; related only to WG2 §2.4 #3.

Replacing P by \(L=P^{-1}\) is additive negation in the Witt convention, which explains why tensor and exterior/symmetric formulas acquire inversions. The next multi-factor expression is written with a product sign, so it should be checked as a Witt product before being used as ordinary multiplication: for two one-dimensional endomorphisms a,b, \(L_{a\otimes b}=1/(1-abt)\), whereas the ordinary reciprocal of \(L_aL_b\) is \((1-at)(1-bt)\). This is a notes-only interpretation question; no star has been inserted into the frozen display.

### F05 — The same-page cancelled λ identity is not a second theorem

**Witness:** 60/005, crossed-out product and final brace; **kind:** withdrawn in the same text; **quote:** the deleted product ending “−1”. **Context query:** `lambda|sigma|classes de Chern`; **comparison:** CT 47/009 also experiments with formal operations, but has no identical cancellation. **RS:** no exact matching entry.

The cancelled two-series product is superseded on this same scan by the σ-series and the final exchange of λ and σ. The usable proof obligation is to reconstruct those final formulas with the manuscript's additive and multiplicative conventions fixed; the crossed-out expression cannot be cited as a live claim. This also explains why a conventional λ-ring identity should not be used to repair the cancelled ink.

### F06 — Contragrédient reciprocity has a rational-function domain

**Witness:** 60/007, final paragraph; **kind:** unpursued implication; **quote:** “produits … finis de polynômes”. **Context query:** `ration|polynôme|automorphisme`; **comparison:** CT 16/048 uses Cayley–Hamilton for inverses, a related finite algebraic calculation but not a formal-series substitution theorem. **RS:** WG2 §6. #9 is background only.

The warning is justified because an arbitrary series in \(k[[t]]\) cannot generally be evaluated at \(t^{-1}\) inside that ring. For an automorphism of rank r, the elementary identity is \(P_{(f^{-1})^\vee}(t)=(-t)^r\det(f)^{-1}P_f(t^{-1})\), and quotients of finite polynomials with invertible relevant coefficients allow the same rational manipulation. The uncertain minus sign in one intermediate argument remains a reading question, not a correction licensed by the boxed identity.

### F07 — Epsilon changes meaning within the packet

**Witness:** 60/007, boxed exponent; 021/027, virtual ranks; **kind:** reading question; **quote:** “ε(Rf_!(E))”. **Context query:** `rang virtuel|varepsilon|epsilon`; **comparison:** CT 47/008 explicitly glosses ε as virtual rank, while cote 60 also uses ε(E) for a normalized determinant. **RS:** MPL_15_195-228+18_002-017 M03 is a first-pass reminder that similarly named gradings and characters require definitions.

The exponent ε(f) on scan 007 is not defined there, but its position and the later rank notation support a rank/Euler-index interpretation. This must remain distinct from the determinant sign ε(E) introduced on scan 009 and from the multiplicity letters on scan 017. The context provides a lexical parallel, not proof that every epsilon in the archive denotes one invariant.

### F08 — Purity alone does not force determinant sign ±1

**Witness:** 60/009, determinant paragraph; **kind:** unproved claim; **quote:** “s'il s'agit d'un motif”. **Context query:** `ration|Weil|characteristic polynomial`; **comparison:** CT 16/048 explicitly adds rational characteristic coefficients and CT 16/050 proposes deriving Weil from its conjectural inputs. **RS:** WG2 §2.3 #7; MPL_14_002-044 M29 and MPL_14_087-132 M09 remain first-pass distinctions, not proofs of realization claims.

Absolute values alone give an absolute value for the determinant, not a real sign: a rank-one finite-order character with Frobenius a primitive cube root of unity is pure of weight zero but has determinant different from ±1 over a coefficient field containing that root. Rationality or a suitable selfduality/polarization is therefore a substantive extra input in the motivic clause. The opening replacement of “motif” by “Q_l-faisceau” does not erase the later explicit restriction back to a motive.

### F09 — Why the odd-weight dimension must be even under rationality

**Witness:** 60/009 and 023; **kind:** unproved claim; **quote:** “tjrs entier”. **Context query:** `ration|poids|Weil`; **comparison:** adds a numerical consequence to CT 16/048–050, where rationality and the Weil programme are separate inputs. **RS:** WG2 §2.4 #3 and WG2 §2.3 #7.

If the determinant is rational and equals \(\pm p^{n\rho/2}\) with p prime, then odd nρ would make its square-root factor irrational, proving nρ even. Without that rationality input, a one-dimensional \(\mathbf Q_\ell\)-representation with Frobenius \(\sqrt p\), when \(\sqrt p\in\mathbf Q_\ell\), is a pure odd-weight counterexample to the unrestricted statement. This argument uses p prime as written and should not be transferred unchanged to a square prime-power base field.

### F10 — Selfduality is a hypothesis on the coefficient object

**Witness:** 60/009, “par Lefschetz”; 013 and 017; **kind:** unproved claim; **quote:** “check E ≃ E(ρ)”. **Context query:** `motive-theoretically|dual|Lefschetz`; **comparison:** CT 16/048 discusses motive-theoretic identification with a dual while explicitly dropping a twist; CT 16/049 needs additional inputs for algebraic splittings. **RS:** WG2 §2.4 #3; MPL_14_087-132 M01 and M09, both first-pass leads.

A nondegenerate pairing of the appropriate weight yields this isomorphism, but an arbitrary pure lisse sheaf need not possess one. The manuscript's later “si on admet que” and its favorable-case restriction are therefore material, not redundant qualifications. These pages use a motivic duality package; they do not construct it from the Lefschetz correspondence rings of cote 16.

### F11 — A Tate twist supplies the variable change

**Witness:** 60/009, final equality; **kind:** unpursued implication; **quote:** “L_checkE(t)=L_E(t/p^ρ)”. **Context query:** `twist|Tate|dual`; **comparison:** CT 16/048 explicitly suppresses a twist, while CT 47/004–005 tracks shifts in another functorial calculation. **RS:** MPL_15_195-228+18_002-017 P09 is an earlier first-pass twist-convention question.

Under the convention stated above, tensoring by \(\mathbf Q_\ell(\rho)\) scales every Frobenius eigenvalue by \(p^{-\rho}\), hence gives the displayed substitution directly. The positive \(\mathbf Q_\ell(n)\) written later in scan 015's pairing should be kept as a separate convention/reading question rather than used to reverse this explicit calculation. Twists and cohomological shifts have different effects on an L-function and must be tracked separately.

### F12 — Properness is a visible correction, later revisited

**Witness:** 60/011, amended hypothesis; 019–021; **kind:** withdrawn in the same text; **quote:** deleted “compactifiable”, inserted “propre”. **Context query:** `propre|compact|dualit`; **comparison:** CT 47/004–005 and CN F20 concern proper derived operations, not the present nonproper boundary correction. **RS:** no exact matching entry; WG2 §2.4 #3 is thematic.

The page narrows its first global-duality calculation to proper X, then scans 019–021 restore a compactifiable nonproper setting by keeping \(Rf_!\) and \(Rf_*\) distinct. The boundary L-factor is the added content that makes this later return substantive. Quoting the first formula with the struck-out broader hypothesis would suppress the manuscript's own correction.


## B. Proper duality, parity, and normalization

### F13 — Derived determinant reciprocity follows degree by degree

**Witness:** 60/011, equation (1); **kind:** unproved claim; **quote:** “par le th. de dualité globale”. **Context query:** `dualit|complexe|rang virtuel`; **comparison:** CT 47/004–005 explicitly distinguishes derived shifts from the class-level formula, but contains no corresponding L-function equation. **RS:** MPL_15_195-228+18_002-017 M03/P09 are first-pass convention leads; no exact settled entry applies.

For a finite-dimensional Frobenius complex V, apply the inverse-eigenvalue identity of F06 in each degree and take alternating products to obtain \(L_{DV}(t)=(-t)^{-\chi(V)}\delta(V)L_V(t^{-1})\). Proper duality identifies \(D Rf_*E\) with \(Rf_*DE\), giving the manuscript's formula without a purity or semisimplicity assumption. Deligne (1973, §§10.3.4–10.5) supplies a later primary formulation of this determinant-and-duality calculation.

### F14 — The cohomological weight substitution is an additional input

**Witness:** 60/011, determinant exponent and insertion; **kind:** self-flagged; **quote:** “avec les conjectures …”. **Context query:** `Weil|standard|standart|poids`; **comparison:** CT 16/050 proposes a deduction of Weil from other conjectures; cote 60 uses the needed cohomological weights directly. **RS:** WG2 §2.4 #3 and WG2 §2.2 #4 remain plans.

The exponent \(\tfrac12\sum_i(-1)^i(i+\rho)b_i\) presupposes that the relevant proper smooth cohomology has weight \(i+\rho\), together with the arithmetic/pairing inputs that make each normalized determinant a sign. A modern purity theorem for suitable pure lisse coefficients supplies the weight assertion, but does not by itself establish all the motivic rationality or polarization assumptions used here (Deligne, 1980, §3.3). The inserted qualification must therefore be retained when extracting a historical claim, even where parts of the required cohomological theory are now available.

### F15 — Betti symmetry needs the selfdual coefficient comparison

**Witness:** 60/013, opening calculation; **kind:** unproved claim; **quote:** “comme b_i=b_{2n-i}”. **Context query:** `dual|Betti|Lefschetz`; **comparison:** CT 16/014–018 supplies alternating/Lefschetz structures and CT 16/048 explicitly asks for motivic duality; the present page computes a determinant consequence. **RS:** WG2 §6. #9; MPL_14_087-132 M05 is a first-pass grading warning.

Poincaré duality initially compares coefficients E with \(E^\vee\), so equality of the two Betti numbers with the same E needs the stated selfduality up to twist, or another justification. Given that equality, replacing i by \(2n-i\) in the alternating sum proves \(\sum_i(-1)^i i b_i=n\chi(E)\), hence the exponent \((n+\rho)\chi(E)/2\). The algebraic simplification is sound once that coefficient-level hypothesis is supplied.

### F16 — A generic isomorphism extends only under the lisse hypotheses

**Witness:** 60/013, small insertion; **kind:** self-flagged / reading question; **quote:** “si on admet que”; “il suffit … sur le corps des fonctions”. **Context query:** `corps des fonctions|générique|normal|isomorph`; **comparison:** CT 16/049 discusses algebraicity of inverses and splittings, not extension of lisse-sheaf morphisms from a generic point. **RS:** no exact matching entry; the category-construction question WG2 §2.4 #3 remains separate.

For an integral normal X and two lisse sheaves on X, a generic Galois-equivariant isomorphism extends because the generic fundamental group surjects onto \(\pi_1(X)\), so restriction is fully faithful (The Stacks Project Authors, n.d.-h). This establishes the conditional “il suffit” in that setting; it does not establish existence of the generic selfduality, nor apply unchanged to arbitrary constructible extensions with extra punctual summands. The uncertain conclusion “donc … tjrs vrai” must therefore remain a reading and hypothesis question.

### F17 — Even shifts are invisible to L but visible to duality

**Witness:** 60/013 and 019, explicit [2n]; 025 and 033, omitted even shifts; **kind:** unpursued implication; **quote:** “shift”. **Context query:** `shift|degré|decal|décal|[-n]`; **comparison:** CT 47/005 retains a derived shift while CT 47/008 computes its parity effect; cote 60 supplies another instance of the same distinction. **RS:** MPL_15_195-228+18_002-017 M03/P09/P14, all first-pass leads.

For lisse E on a smooth n-dimensional X, the full formula is \(D_XE=E^\vee(n)[2n]\), so the selfdual specialization gives \(E(n+\rho)[2n]\). An even shift leaves \(\chi,\delta,L\) unchanged, whereas an odd shift changes the virtual sign and inverts \(\delta,L\). Consequently the missing [2n] on 025 and [2] on 033 can be harmless in the subsequent L-function calculation without being correct as literal derived-object identities.

### F18 — The normalized function may require a square-root coordinate

**Witness:** 60/015, 029, 031, 035; **kind:** own idea; **quote:** “Posant … t^{χ(E)/2}L_E(t)”. **Confidence:** high; the issue follows from odd integral χ and the displayed exponent. **Context query:** `demi|racine|chi|normalis`; **comparison:** no matching half-power normalization was found in CT; CT 47/008 only supplies an Euler-characteristic comparison. **RS:** no exact matching entry.

When χ is odd, \(\xi(t)=t^{\chi/2}L(t)\) is naturally a function on the square-root coordinate \(u^2=t\), rather than necessarily a rational function of t. After choosing \(q^{1/2}\), the involution lifts as \(u\mapsto q^{-1/2}u^{-1}\), and the manuscript's algebra gives \(\xi(1/(qt))=(-1)^\chi\varepsilon A(t)\xi(t)\). This is a domain qualification for the normalization, not a reason to alter its ink.

### F19 — The written Tate target has the opposite sign to the adopted convention

**Witness:** 60/015, lower paragraph; **kind:** reading question; **quote:** “duaux à valeurs dans Q_l(n)”. **Context query:** `twist|Tate|duaux|dualité`; **comparison:** CT 16/048 explicitly suppresses a twist, while the present page writes one; the two passages do not resolve each other's convention. **RS:** MPL_15_195-228+18_002-017 P09 is a first-pass twist question.

With geometric Frobenius acting on \(\mathbf Q_\ell(1)\) as \(p^{-1}\), the unshifted Poincaré target is \(\mathbf Q_\ell(-n)\), or \(\mathbf Q_\ell\) after twisting the second factor by (n) (Deligne, 1974, §2.3 and Theorem 2.8). The positive (n) written here conflicts with that convention and with the variable change elsewhere in this packet. Its use merely to assert a positive real Frobenius factor still permits the following sign cancellation.

### F20 — The total sign reduces to the middle degree

**Witness:** 60/015, final three displays; **kind:** unproved claim; **quote:** “Pour la raison analogue” (uncertain reading). **Context query:** `altern|dual|signe|discrimin`; **comparison:** CT 16/014 and 025 concern nondegenerate pairings; this page adds a Frobenius-determinant application. **RS:** MPL_14_002-044 A36 is a first-pass autoduality lead, not a checked proof of this formula.

Under the pairing assumptions, complementary degrees have determinant signs equal, so their product contributes +1 and only degree n survives. The same degree pairing gives \(\chi(E)\equiv b_n\pmod2\), yielding \(\varepsilon'=(-1)^{b_n}\operatorname{sgn}\det(F\mid H^n)\). Negative exponents in the alternating determinant do not change a ±1 sign, which explains the ordinary product of signs on this page.

### F21 — Odd-weight positivity uses an alternating polarization

**Witness:** 60/017, opening paragraph; 023, odd-index sign; **kind:** unproved claim; **quote:** “une forme alternée non dégénérée”. **Context query:** `forme alternée|symplect|polar|Lefschetz`; **comparison:** CT 16/014 begins with precisely an alternating nondegenerate form, while 16/048–050 treats additional motivic inputs as conjectural. **RS:** WG2 §2.4 #3 and WG2 §6. #9.

If a 2m-dimensional space carries a nondegenerate alternating form and F multiplies that form by a positive scalar c, then \(\det F=c^m\); after normalization its determinant is +1. Thus the stated alternating-form hypothesis proves the sign conclusion and the even-dimension assertion, including without semisimplicity of F. Pure weight or selfduality without the required symmetry type does not suffice, as F22 tests.

### F22 — A symmetric odd-weight selfduality is a scope counterexample

**Witness:** 60/017 and 023; **kind:** own idea; **quote:** “+1 si i est impair”. **Confidence:** high; both the pairing and determinant are verified by 2×2 matrix multiplication. **Context query:** `semi-simple|polar|symétrique|alternée`; **comparison:** CT 16/048–050 separates duality, positivity and semisimplicity; this example makes that separation concrete. **RS:** bears on first-pass MPL_14_002-044 M29a and MPL_14_087-132 M09 only as a separate local-system scope test.

On \(\operatorname{Spec}\mathbf F_p\), let \(F=\begin{pmatrix}0&p\\1&0\end{pmatrix}\) and \(B=\operatorname{diag}(1,p)\), with \(\ell\ne p\). Then \(F^tBF=pB\), so \(E^\vee\simeq E(1)\), and the rational characteristic polynomial \(x^2-p\) gives pure weight 1, but \(\det F=-p\) and \(\varepsilon'=\varepsilon=-1\). This symmetric pairing therefore disproves extending the odd-weight positive-sign assertion to all rational, pure, selfdual sheaves; it does not contradict a polarized motivic assertion with alternating symmetry.

### F23 — Eigenvalues ±1 require normalized Frobenius

**Witness:** 60/017, even-weight paragraph; **kind:** reading question; **quote:** deleted “dimension”, inserted “multiplicité”; “valeur propre 1 (−1)”. **Context query:** `Frobenius|valeur propre|multiplicité|Weil`; **comparison:** CT 16/020 has an unfinished weighted expression but no identification of these normalized eigenvalues. **RS:** MPL_14_087-132 M05 is a first-pass warning about distinct gradings.

For \(F_0=p^{-(n+\rho)/2}F\) in the orthogonal case, reciprocal eigenvalues away from ±1 pair, so \(b_n\equiv e_1+e_{-1}\pmod2\), \(\det F_0=(-1)^{e_{-1}}\), and \(\varepsilon'=(-1)^{e_1}\). These are algebraic multiplicities, not merely dimensions of ordinary eigenspaces; the insertion “multiplicité” is mathematically significant. Deligne (1974, §2.6) states the corresponding sign using the unnormalized central eigenvalue \(p^{n/2}\) over \(\mathbf F_p\), making the normalization issue explicit in the constant-coefficient case.

### F24 — Projective space detects both the normalization and central-pole issue

**Witness:** 60/015–017; **kind:** own idea; **quote:** “ε′(E)=(−1)^{e_1}”. **Confidence:** high; the cohomology of \(\mathbf P^2\) gives three explicit Frobenius eigenvalues. **Context query:** `projectif|projective|espace|Lefschetz`; **comparison:** CT 16/014–018 develops Lefschetz linear algebra, but no matching central-sign test was found. **RS:** WG2 §6. #9 is thematic only.

For \(X=\mathbf P^2\) with constant coefficients, \(\chi=3\), \(\delta=p^3\), \(q=p^2\), hence \(\varepsilon=1\), \(\varepsilon'=-1\), while raw Frobenius on \(H^2\) has eigenvalue p, not 1. Normalizing by p gives multiplicity one and the correct sign, whereas the literal raw-eigenvalue interpretation fails. Moreover \(L(t)=[(1-t)(1-pt)(1-p^2t)]^{-1}\) has a simple pole at the central point \(t=1/p\), so a negative normalized sign constrains the parity of the order of a zero **or pole**, and implies a central zero only with an additional holomorphy hypothesis.

### F25 — The two-object functional equation is the general statement

**Witness:** 60/017, final paragraph; **kind:** unpursued implication; **quote:** “elle relie deux fonctions”. **Context query:** `dualité|dual|isomorphe`; **comparison:** CT 16/048's duality requirement is an extra conjectural input, in accord with this explicit restriction. **RS:** WG2 §2.4 #3; MPL_14_087-132 M01 remains a first-pass distinction between rings and a constructed category.

When the required selfduality does not exist, the equation relating \(L_E\) and \(L_{DE}\) remains the appropriate result, and there is no canonical reason to turn it into an involutive equation for \(L_E\) alone. The manuscript says this expressly, so its earlier favorable-case sign formulas should not be exported to all constructible sheaves. The non-selfdual finite-order character of F08 is already a minimal test.

## C. The nonproper boundary and its determinants

### F26 — The boundary term has an intrinsic cone interpretation

**Witness:** 60/019–021; **kind:** unpursued implication; **quote:** “cl R_∞f(E)”. **Context query:** `compactif|frontière|infin|R_∞|R_\\infty`; **comparison:** no matching compact/ordinary boundary formula was found in CT/CN; CT 47/004–005 concerns a different derived transform. **RS:** no exact settled entry applies.

Define \(C_\infty(E)=\operatorname{Cone}(Rf_!E\to Rf_*E)\), whose class is exactly the difference written on 019. For a compactification \(j:X\hookrightarrow\bar X\), closed complement \(i:Z\hookrightarrow\bar X\), and proper \(\bar f\), localization realizes this cone as \(R\bar f_*i_*i^*Rj_*E\). This proves independence of the chosen compactification at the level of the intrinsic cone, subject to the usual constructibility/finiteness framework and a compatible derived isomorphism, and gives the boundary object whose L-function is used below.

### F27 — The formal nonproper equation separates from the weight assertions

**Witness:** 60/019–021; **kind:** unproved claim; **quote:** “Dualité”; “A(t)=L_E^∞(1/(p^{n+ρ}t))^{−1}”. **Context query:** `résolution|Weil|dualité|compact`; **comparison:** CT 16/050 is a conditional Weil programme; it supplies no boundary calculation. **RS:** WG2 §2.2 #4 and WG2 §2.4 #3 remain unchanged.

Under the smooth lisse selfdual hypotheses, duality and the triangle in F26 give the displayed functional equation with \(A(t)=L_\infty(1/(qt))^{-1}\), \(q=p^{n+\rho}\), and compact-support \(\chi,\delta\). This formal deduction does not itself need resolution of singularities or Weil bounds; those assumptions belong to the further weight/type interpretation and the motivic hypotheses on coefficients. This logical distinction sharpens the boxed historical qualification without deleting or relocating it in the transcription.

### F28 — The type and weight bounds need a separate definition and proof

**Witness:** 60/021, NB margin; **kind:** self-flagged / unproved claim; **quote:** “type ≤τ+(n−1)”; “poids ≤ρ+2n”. **Context query:** `type|poids|niveau|résolution|weight`; **comparison:** CT has unrelated root-system weights and motivic grading discussions, but no definition settling this boundary type bound; CN supplies no matching proof. **RS:** WG2 §2.4 #3 and the first-pass MPL_14_087-132 M05 distinguish structures whose gradings cannot be identified automatically.

A proof must specify what “type” means, how boundary strata and local monodromy affect it, and how the stated weight bound applies to the particular complex or virtual motive. Modern mixed-sheaf weight estimates are relevant comparison tools, but the page's undefined type must not be silently renamed as a modern weight, niveau or coniveau invariant. No complete proof or counterexample to this exact two-part assertion was obtained from the supplied materials, and its explicit resolution/Weil qualification remains material.

### F29 — The Euler characteristics agree under the stated selfduality

**Witness:** 60/021 and 027; **kind:** unproved claim; **quote:** “les deux ε sont égaux”. **Context query:** `rang virtuel|Euler|chi|epsilon`; **comparison:** CT 47/008 identifies ε as virtual rank but gives no compact/ordinary comparison. **RS:** no exact matching entry.

The isomorphism \(D Rf_!E\simeq Rf_*E(n+\rho)[2n]\) preserves total Euler characteristic, giving \(\chi_c(E)=\chi_*(E)\) in this setting. Consequently the boundary virtual rank is zero. This is a consequence of the coefficient selfduality used on these pages, not a proof supplied here for every possible constructible coefficient object under every convention.

### F30 — Virtual weight pieces must not be mistaken for cohomological degrees

**Witness:** 60/023; **kind:** unproved claim; **quote:** “composantes virtuelles”; “nbs de Betti virtuels”. **Context query:** `virtuel|Betti|poids|grading`; **comparison:** CT 16/020 has an unfinished weighted Betti sum; cote 60 supplies a concrete weighted determinant but does not determine that earlier completion. **RS:** MPL_14_087-132 M05 and MPL_15_195-228+18_002-017 M03/P09/P14 are first-pass grading leads.

The formula follows if the virtual class is decomposed into pure weight-i pieces with the stated ranks and determinant signs. In nonproper cohomology, weight and cohomological degree need not coincide, so the symbols \(h_!^i,\beta_i\) require the virtual decomposition intended here, not automatic identification with ordinary \(H_c^i\) and nonnegative Betti numbers. The alternating correction in the final exponent is essential; the odd-i positive sign still requires the polarization issue isolated in F21–F22.

### F31 — The author's ±1 shift question has a definite answer after choosing the cone

**Witness:** 60/025, boxed shift; **kind:** self-flagged / own verification; **quote:** “à vérifier si c'est 1 ou −1 !”. **Confidence:** high; the dual triangle determines the cohomological shift. **Context query:** `dualité locale|shift|décal|dualit`; **comparison:** CT 47/005 explicitly tracks a different derived shift, but does not determine this one. **RS:** MPL_15_195-228+18_002-017 M03/P09 are pertinent convention leads, not a settled boundary result.

Dualizing \(A\to B\to C_\infty(E)\to A[1]\), with \(A=Rf_!E\) and \(B=Rf_*E\), gives \(DC_\infty(E)\to Rf_!DE\to Rf_*DE\to DC_\infty(E)[1]\), hence \(DC_\infty(E)\simeq C_\infty(DE)[-1]\). Under the selfdual smooth hypothesis this is \(C_\infty(E)(n+\rho)[2n-1]\). The alternative shifts +1 and −1 have the same class and L-function effect, so the later determinant equations cannot decide the author's question; the cone convention and degree calculation can (The Stacks Project Authors, n.d.-b).

### F32 — The deleted boundary square is replaced by a dual-object relation

**Witness:** 60/025, cancelled box and insertion; **kind:** withdrawn in the same text; **quote:** deleted “L_E^∞(t)L_E^∞(t)=1”, inserted “L_DE^∞”. **Context query:** `dual|inversion|fonctionnelle`; **comparison:** CT 47/004 also visibly corrects a functorial formula, but no same boundary identity occurs there. **RS:** no exact matching entry.

The deleted square should not be quoted as an assertion that the boundary L-function is ±1. Odd-shift duality instead relates the dual boundary object to the inverse L-function, and determinant reciprocity introduces the reciprocal variable and determinant factor in the live final formula. Scans 027 and 029 then specialize and cross-check that formula.

### F33 — Compact and ordinary normalized determinants are reciprocal

**Witness:** 60/027, two adjacent boxed identities; **kind:** own idea / inconsistency check; **quote:** “δ(E)δ′(E)=q^{χ(E)}”. **Confidence:** high; the conclusion is an algebraic consequence of the first box and has the explicit test F34. **Context query:** `déterminant|determinant|epsilon|infin`; **comparison:** CT 16/020 concerns a different determinant-style calculation and no context formula repairs this equality. **RS:** no exact matching entry.

Writing \(\delta_c=\delta(Rf_!E)\), \(\delta_*=\delta(Rf_*E)\), the first box gives \(\delta_*q^{-\chi/2}=(\delta_cq^{-\chi/2})^{-1}\). Therefore the next box's equality of both expressions with ε is false generally; equality holds when \(\varepsilon^2=1\), in particular in the proper case. The accompanying formula \(\delta_\infty=q^\chi\delta_c^{-2}=\varepsilon^{-2}\) is compatible with the reciprocal relation.

### F34 — The affine line verifies the boundary equation and separates its normalizations

**Witness:** 60/021, 025, 027 and 029; **kind:** own idea; **quote:** “=±1 si X … propre”. **Confidence:** high; only \(H_c^2(\mathbf A^1)=\mathbf Q_\ell(-1)\) and \(H^0(\mathbf A^1)=\mathbf Q_\ell\) enter. **Context query:** `affine|compact|Frobenius|fonctionnelle`; **comparison:** no matching boundary test was found in CT/CN. **RS:** no exact matching entry.

For constant coefficients on \(\mathbf A^1/\mathbf F_p\), \(q=p,\chi=1,\delta_c=p,\delta_*=1\), so the two normalized determinants are \(\sqrt p\) and \(1/\sqrt p\). Here \(L_c=(1-pt)^{-1}\), \(L_\infty=(1-pt)/(1-t)\), \(\delta_\infty=p^{-1}\), and \(A(t)=(1-pt)/(p(1-t))\). Substitution verifies both \(L_c(1/(pt))=A(t)p(-t)L_c(t)\) and \(L_\infty(t)L_\infty(1/(pt))\delta_\infty=1\), isolating the error to the normalized-determinant equality rather than the boundary functional equation.

### F35 — A two-boundary-point example makes the nonsign epsilon explicit

**Witness:** 60/027 and 031; **kind:** own idea; **quote:** “ε′(E)=±1” only for complete X. **Confidence:** high; the four cohomology groups listed in the research record give the stated products directly. **Context query:** `multiplicatif|G_m|infin|ramification`; **comparison:** CT 44's reused root-system material supplies no relevant boundary comparison. **RS:** no exact matching entry.

For constant coefficients on \(\mathbf G_m\), \(\chi=0\), \(\delta_c=p\), \(\delta_*=p^{-1}\), \(\varepsilon=p\), and \(\delta_\infty=p^{-2}\). Its compact-support L-function is \((1-t)/(1-pt)\), while \(L_\infty=((1-pt)/(1-t))^2\), reflecting the two missing points of the projective line. Thus ε need not be a sign outside the proper case, fully consistent with the manuscript's explicit qualification.

### F36 — Applying the involution twice is a consistency test, not an independent existence proof

**Witness:** 60/029; **kind:** unpursued implication; **quote:** “C'est précisément l'équation fonctionnelle explicitée plus haut”. **Context query:** `involution|fonctionnelle|inversion`; **comparison:** CT 47/004–005 computes a different square of a transform; this is an analogy of method, not the same theorem. **RS:** no exact matching entry.

If \(L(1/(qt))=B(t)L(t)\) as nonzero rational functions, then necessarily \(B(t)B(1/(qt))=1\). With \(B=A\delta_c(-t)^\chi\), this recovers \(L_\infty(t)L_\infty(1/(qt))=\delta_c^2q^{-\chi}\), agreeing with F33. Because the argument starts from the functional equation, it checks compatibility but does not independently prove the original duality or its existence.

### F37 — Variation under finite-field extension gives a simple next test

**Witness:** 60/027, marginal research direction; **kind:** own idea; **quote:** uncertain “Varions … avec E, X !!”. **Confidence:** high for base-field extension; no general family-variation theorem is claimed. **Context query:** `variation|extension|Frobenius|famille`; **comparison:** CT 16/048–050 varies coefficient assumptions but gives no variation formula for these epsilon invariants. **RS:** no exact matching entry.

Under \(\mathbf F_p\subset\mathbf F_{p^r}\), geometric Frobenius becomes \(F^r\), so χ is unchanged while \(\delta_c,\delta_*\), and \(\delta_\infty\) become their rth powers. Using the compatible positive square-root normalization gives \(\varepsilon_r=\varepsilon^r\), a direct test any proposed variation theory should pass. The L-function itself is not generally obtained by the naive substitution \(t\mapsto t^r\), because its eigenvalues, rather than its variable, are raised to the rth power.

### F38 — The extra mark on A in the normalized box remains a reading question

**Witness:** 60/031, top box; **kind:** reading question; **quote:** “A” with uncertain superscript “ξ”. **Context query:** `normalis|xi|zeta|fonctionnelle`; **comparison:** no matching boundary notation was found in CT/CD. **RS:** no exact matching entry.

The derivation on 029 and the definition immediately below the box on 031 use A(t), with the change of normalization absorbed by \(\varepsilon'=(-1)^\chi\varepsilon\). They therefore suggest that the tiny mark need not introduce a different independently defined function, but neither that algebra nor the context settles its ink. The frozen uncertainty is retained, and no new exponent or definition is supplied.

## D. The generic curve L-function and the failure of exactness

### F39 — The function field determines the smooth proper curve, with a finiteness qualification on coefficients

**Witness:** 60/033, opening; **kind:** unproved claim; **quote:** “K détermine X”. **Context query:** `corps de fonctions|courbe|générique`; **comparison:** CT 44/004 uses a fibration in a height question, but no matching generic L-function construction appears. **RS:** WG H9 and WG2 §2.3 #12 are not advanced by this separate curve construction.

A one-variable function field over a perfect field has its smooth proper model determined up to unique isomorphism after fixing its function-field identification, explaining the geometric claim (The Stacks Project Authors, n.d.-c). For the coefficient construction, one should also specify that the generic representation extends to a lisse sheaf on a nonempty open, so that the underived extension is constructible and the finitely many correction points used on 035 exist. This is a finiteness hypothesis to verify for the intended category of generic ℓ-adic objects, not a conclusion supplied merely by writing “constr.” on the generic point.

### F40 — Underived extension on a curve has selfdual middle-extension behavior

**Witness:** 60/033, duality display; **kind:** unproved claim; **quote:** “On sait alors que”. **Context query:** `image directe|dualité|courbe`; **comparison:** CT 47/004–005 uses derived direct images in another theory, while the current choice of underived image is essential. **RS:** no exact matching entry; first-pass MPL_14_002-044 A36 is only a duality lead.

For \(j:U\hookrightarrow X\) on a smooth projective curve and lisse L on U, the full derived formula is \(D_X(j_*L)\simeq j_*L^\vee(1)[2]\), equivalently the duality of the perverse middle extension \(j_*L[1]\). Deligne (1974, §§2.11–2.12) states the resulting perfect cohomological pairing explicitly. The missing [2] in the manuscript affects the derived identity but leaves its subsequent L-function computation unchanged.

### F41 — The positive Euler exponent in the curve equation is correct

**Witness:** 60/033, first functional equation; **kind:** own verification; **quote:** “(−t)^{χ*(check E_y)}”. **Confidence:** high; substitution in F13 gives the sign without any new geometric assumption. **Context query:** `chi|Euler|fonctionnelle`; **comparison:** no matching curve equation was found in CT; CT 47/008 uses χ in a different transform identity. **RS:** no exact matching entry.

Writing \(M=j_*L\), F13 gives \(L_{DM}(t)=(-t)^{-\chi(M)}\delta(M)L_M(t^{-1})\). Since \(L_{DM}(t)=L_{j_*L^\vee}(t/p)\), substitution \(t\mapsto t^{-1}\) gives exactly the positive exponent \((-t)^{\chi(M)}\), and duality identifies the dual coefficient Euler characteristic with χ(M). Thus this apparent sign reversal is explained by the substitution and should not be listed as an error.

### F42 — The underived correction formula has the right multiplicative direction

**Witness:** 60/035, exact sequences and final display; **kind:** unproved claim; **quote:** “ce n'est pas additif”. **Context query:** `suite exacte|Grothendieck|image directe|additif`; **comparison:** CT 16/035 imposes split direct-sum K-group relations; this example shows why exact-sequence relations require additional care. **RS:** MPL_15_195-228+18_002-017 R01 is a first-pass reused-text caution only.

The stalk of \(j_*L\) at a missing point is the inertia-invariant space, and invariants are left exact rather than exact. For \(Q=\operatorname{coker}(j_*L\to j_*L'')\), the displayed sequence gives \([j_*L]=[j_*L']+[j_*L'']-[Q]\), hence \(L^*(L)=L^*(L')L^*(L'')L(Q)^{-1}\). Thus the correction direction is correct and records an obstruction to descending this underived construction through all exact Grothendieck relations.

### F43 — The correction can occur where the quotient is unramified

**Witness:** 60/035, support assertion; **kind:** own idea / counterexample; **quote:** “pts de ‘ramification’ de E''_y”. **Confidence:** high; the local tame relation and invariant spaces are explicit. **Context query:** `ramification|invariant|unipotent|extension`; **comparison:** CT has no matching inertia-invariants claim, and its reused algebra ramification exercises concern a different setting. **RS:** MPL_14_002-044 M29a is a first-pass mixed-extension lead; this is an independent test, not a reproof of that result.

Take \(Ne_2=e_1,Ne_1=0\), inertia \(T(u)=1+uN\), and geometric Frobenius \(F=\operatorname{diag}(1,p)\), so \(FT(u)F^{-1}=T(u/p)\). In \(0\to\mathbf Q_\ell\to V\to\mathbf Q_\ell(-1)\to0\), both end terms are unramified but \(V^I=\mathbf Q_\ell e_1\) maps to zero in the quotient invariants, giving \(Q=\mathbf Q_\ell(-1)\ne0\). Therefore the support need not be a ramification point of the quotient; it is the failure-of-surjectivity locus for invariants, contained in the ramification locus of the middle representation.

### F44 — The local obstruction globalizes on the multiplicative group

**Witness:** 60/035; **kind:** own idea; **quote:** “produit … P_{Q_x}(t)”. **Confidence:** high; the tame Kummer extension has the same nonzero monodromy at 0 and infinity. **Context query:** `Kummer|G_m|extension|ramification`; **comparison:** no matching construction was found in CT/CN. **RS:** no exact matching entry; the mixed/pure distinction remains related to first-pass MPL_14_002-044 M29a.

The representation of F43 is the suitable Tate twist of the Kummer extension on \(\mathbf G_m\), compactified in \(\mathbf P^1\), and has \(Q_x=\mathbf Q_\ell(-1)\) at both boundary points. Its L-functions satisfy \(L(j_*V)=[(1-t)(1-p^2t)]^{-1}\), \(L(j_*V')=[(1-t)(1-pt)]^{-1}\), and \(L(j_*V'')=[(1-pt)(1-p^2t)]^{-1}\). The missing correction is exactly \((1-pt)^2\), giving a complete global test of the formula and its erroneous quotient-support restriction.

### F45 — Purity excludes that mixed counterexample through geometric semisimplicity

**Witness:** 60/035, additivity complaint; **kind:** unpursued implication; **quote:** “ce n'est pas additif”. **Context query:** `semi-simple|pure|extension|Weil`; **comparison:** CT 16/049 proposes a conditional semisimple motivic category, whereas this uses a later theorem for geometric local systems. **RS:** MPL_14_087-132 M09 and MPL_14_002-044 M29a are first-pass category/scope distinctions.

The example F43–F44 is mixed, with weights 0 and 2, and should not be presented as a counterexample within a pure geometrically semisimple category. If the sequence splits on the geometric fundamental group, inertia invariants are exact; finite inertia image of the middle representation also gives exactness by averaging in characteristic zero. Deligne's geometric semisimplicity theorem for pure lisse sheaves supplies this restriction in its own setting (1980, Theorem 3.4.1(iii)/3.4.9), without asserting arithmetic semisimplicity of every pure sheaf.

### F46 — The crossed-out kernel remains the useful connecting-homomorphism description

**Witness:** 60/035, cancelled formula for Q; **kind:** withdrawn in the same text / unpursued implication; **quote:** “Ker(R¹i_*E'_y − R¹i_*E_y)” in the deletion. **Context query:** `noyau|Ker|suite exacte|image directe`; **comparison:** CT 47/004–005's derived formalism is methodologically relevant but has no matching inertia sequence. **RS:** no exact matching entry.

The long exact sequence in the ambient étale category identifies the cokernel Q with \(\ker(R^1i_*E'_y\to R^1i_*E_y)\), without asserting that each higher generic direct image is constructible. Thus the kernel expression's cancellation does not make the underlying mathematical description false, and it provides a practical way to compute the correction. For a fixed finite-type open \(j:U\hookrightarrow X\), the derived functor \(Rj_*\) preserves triangle relations and restores exact additivity at the appropriate class level; the generic-point functor needs the separate finiteness caution F55.

### F47 — Closed-point factors require their residue degrees

**Witness:** 60/035, product over x; **kind:** reading question; **quote:** “P_{Q_x}(t)”. **Context query:** `point fermé|degré|Frobenius|polynôme`; **comparison:** no corresponding local Euler-factor notation was found in CT/CD. **RS:** no exact matching entry.

If \(P_{Q_x}\) denotes the characteristic polynomial of local Frobenius over \(\kappa(x)\), its contribution is \(\det(1-F_xt^{\deg x}\mid Q_x)\). The written \(P_{Q_x}(t)\) is consistent if induction to the base field or the residue-degree substitution is already built into the notation, but the selected pages do not state that convention. The degree-one examples above avoid deciding this notational question.

### F48 — The final H² note is duality data, not a new height construction

**Witness:** 60/035, overwritten lower margin; **kind:** reading question / unpursued implication; **quote:** “H² … dual de H⁰ … (ρ+1)”. **Context query:** `H^2|H^0|hauteur|dualité`; **comparison:** CT 44/002–004 studies different duality/polarization and height expectations, whereas this margin concerns the two endpoint cohomology groups of the curve. **RS:** WG H9 and WG2 §2.3 #12 remain unchanged.

Under the selfdual coefficient assumption, the curve pairing gives \(H^2(X,j_*L)\simeq H^0(X,j_*L(\rho+1))^\vee\), with the twist and dual placed as written in this explanatory formula. This supplies a check on χ and δ using global invariant sections, but the heavy overwriting leaves the precise placement in the manuscript uncertain. It offers no height-pairing or local-symbol construction in the selected packet.


## E. Further distinctions exposed by the complete packet

### F49 — The Euler-product bridge is a trace-formula input

**Witness:** 60/011, passage from E on X to \(Rf_*E\); **kind:** unproved claim / convention; **quote:** “L_E”. **Context query:** `trace|Frobenius|fonction L|Lefschetz`; **comparison:** CT 16/048–050 treats trace/characteristic-polynomial rationality in a motivic programme but gives no global Euler-product formula here. **RS:** WG2 §2.4 #3 and WG2 §6. #9 are related background only.

If \(L_E\) is initially defined by local Euler factors, identifying it with the alternating determinant on \(H_c^i(\bar X,\bar E)\) requires the Grothendieck trace formula, not merely linear-algebraic duality. If it is defined cohomologically, that same theorem is the bridge back to arithmetic local factors. Deligne (1973, Theorem 10.4 and (10.4.2)) explicitly separates this input from the following duality equation, a useful comparison for the manuscript's compressed transition.

### F50 — The deleted χ formula uses a virtual object rather than the later integer

**Witness:** 60/011, cancelled cohomological and χ displays; **kind:** withdrawn in the same text / reading question; **quote:** deleted “χ(DE)=Σ(−1)^iH^i”. **Context query:** `virtuel|Grothendieck|chi|rang`; **comparison:** CT 47/008 distinguishes virtual rank from Euler characteristic, and CT 16/035 uses a different split K-group. **RS:** MPL_15_195-228+18_002-017 M03 is a first-pass notation/structure lead.

The cancelled expression treats χ as a virtual cohomology object, whereas the live definition below takes χ to be the integer alternating sum of ranks. The surviving derived identity organizes the former object-level duality without identifying that virtual class with its numerical rank. Both uses should be distinguished when citing the page; the deletion is evidence of revision, not an additional live definition.

### F51 — The packet has two determinant epsilons as well as rank epsilon

**Witness:** 60/023 versus 027; **kind:** reading question / own verification; **quote:** “ε(E)=∏ε_i(E)”; “ε(E)=δ(E)q^{−χ(E)/2}”. **Confidence:** high; the affine-line calculation distinguishes the definitions. **Context query:** `epsilon|varepsilon|rang virtuel|poids`; **comparison:** CT 47/008 explains the rank usage only; no earlier supplied context identifies the two determinant normalizations. **RS:** MPL_15_195-228+18_002-017 M03/P09 remain first-pass convention leads.

On 023, \(\varepsilon_{\mathrm{weight}}\) is the sign after extracting the full weighted determinant exponent, whereas 027 defines \(\varepsilon_{\mathrm{center}}=\delta_cq^{-\chi/2}\), which need not be a sign for nonproper X. For \(\mathbf A^1\), the weight-2 contribution gives \(\varepsilon_{\mathrm{weight}}=1\), but F34 gives \(\varepsilon_{\mathrm{center}}=\sqrt p\). These are two different invariants written with the same letter, in addition to the virtual-rank epsilon identified in F07.

### F52 — The correction A has a specified norm under the involution

**Witness:** 60/029–031; **kind:** unpursued implication; **quote:** “B(t)B(1/(qt))=1”. **Context query:** `involution|inversion|epsilon|fonctionnelle`; **comparison:** no matching norm identity was found in CT/CN. **RS:** no exact matching entry.

Since \(A(t)=L_\infty(1/(qt))^{-1}\), the boundary equation implies \(A(t)A(1/(qt))=\delta_\infty=\varepsilon_{\mathrm{center}}^{-2}\). Thus the full normalized multiplier \(A(t)\varepsilon'\) has norm one, even when ε′ alone is not ±1. This explains why the same A remains in the normalized equation and why discarding it outside the proper case would break involutivity.

### F53 — The curve defect also changes χ and δ

**Witness:** 60/035, Q correction; **kind:** unpursued implication; **quote:** “Q_x=Coker”. **Context query:** `coker|rang|déterminant|suite exacte`; **comparison:** CT 16/035's direct-sum K-group does not account for this underived exactness defect. **RS:** no exact matching entry.

The class identity in F42 gives \(\chi^*(E)=\chi^*(E')+\chi^*(E'')-\chi(Q)\) and \(\delta^*(E)=\delta^*(E')\delta^*(E'')/\delta(Q)\), where the punctual sheaf is pushed to the base field before taking rank and determinant. Hence the normalized scalar acquires the corresponding quotient factor when a common central q is fixed; the defect affects more than the rational function alone. This provides two further consistency tests for any proposed additive replacement of \(L^*\).

### F54 — “Constant tordu” supplies a contextual expansion, not a new ink reading

**Witness:** 60/011, 017, 019, uncertain c^t/ct abbreviations; **kind:** reading question; **quote:** “c^t tordu” (uncertain). **Context query:** `constant tordu|localement constant|lisse`; **comparison:** CT contains local-constancy language but does not settle the strokes on these scans; the strongest terminology parallel is Deligne (1980, introduction, p. 138). **RS:** no exact matching entry.

Deligne explicitly identifies “lisse” with the older term “constant tordu,” supporting that interpretation of the coefficient hypothesis. This is evidence about terminology, not a visual adjudication of the superscript or abbreviation in the current manuscript. The uncertain spelling and placement in every frozen occurrence remain unchanged.


### F55 — The higher generic direct image is not automatically constructible

**Witness:** 60/033–035, generic i and deleted R¹i_*; **kind:** own idea / scope check; **quote:** “i:y−X” and “R¹i_*”. **Confidence:** high; the constant sheaf already exhibits the obstruction at every closed point. **Context query:** `constructible|image directe|générique|invariant`; **comparison:** CT 47/004–005 uses finite-type derived operations and supplies no finiteness result for this generic-point map. **RS:** no exact matching entry.

For the generic inclusion \(i:\operatorname{Spec}K\to X\) of a smooth curve, \(R^1i_*\mathbf Q_\ell\) has nonzero tame-inertia \(H^1\) at every closed point, even though the underived constant extension is lisse. Thus replacing i_* by Ri_* does not automatically produce a bounded constructible object to which the same L-function formalism applies. A fixed nonempty finite-type open carrying the lisse representation provides the appropriate constructible derived setting; the generic kernel description of Q can still be used in the ambient category.
