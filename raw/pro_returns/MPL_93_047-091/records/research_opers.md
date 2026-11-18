## Projective bundles, Lie algebras, and transverse connections: scans086–091

The note IDs in this section are prefixed **OP**. Algebraic checks are given in `records/projective_proof_checks.md` (A–E), with an executable exact-arithmetic certificate; they are post-freeze work, not readings inferred from the context. In references to `hua_project/93.modern.tex`, §VII's labels “pages85–90” correspond to supplied scans086–091; its continuation uses pages whose original images are outside this package.

### OP01 — Local projectivizations are not a global rank-two bundle

**Short quote (frozen TeX, scan 086):** `Données équivalentes`.

**File/location:** cote93, scan086, 1.1(a–c) and “L défini loc. fppf … ou loc ét.” **Kind:** unproved claim. **Context queries:** Brauer; Azumaya; module inversible; fppf.

The list “Données équivalentes” needs the local qualification which the paragraph about L itself supplies: a general Brauer–Severi curve need not be the projectivization of one global rank-two vector bundle. For instance, the real conic `x²+y²+z²=0` becomes a projective line over C but has no real point, whereas the projectivization of a real two-dimensional vector space does; the Azumaya/line-twist framework is consistent with [OP-S2]. Context comparison: `hua_project/93.modern.tex`, §VII, pages85–86, restates the list more globally than its displayed local construction warrants; `notes/RESULTS_STATE.md` has no matching settled entry, and **MPL_93_002-046 P01** (scan036 in `same_cote_93/MPL_93_002-046_notes.md`) supplies only the earlier projective-calculus strand.

### OP02 — Why tensoring by a line disappears from End(E)

**Short quote (frozen TeX, scan 086):** `M=\check E\otimes E\simeq\underline{\operatorname{End}}(E)`.

**File/location:** cote93, scan086, `M=E-check tensor E` display. **Kind:** unpursued implication. **Context queries:** End; tensorisation; Azumaya.

The formula `M=End(E)` is insensitive to replacing E by `E tensor lambda`, and the rank-two wedge pairing gives `E-dual=E tensor(det E)^(-1)` without requiring 2 to be invertible. This elementary tensor identity explains which parts of 1.1 descend before introducing Lie-algebra equivalences; [OP-S2, Lemma59.62.1] also identifies the line-twist ambiguity between two global presentations of the same endomorphism algebra. Context comparison: Hua §VII, pages85–86, restates the construction but does not distinguish this characteristic-free identity from the later characteristic restriction; no exact result-state ID settles it.

### OP03 — The two exact sequences retain different quadratic functors

**Short quote (frozen TeX, scan 086):** `\Gamma^2E\otimes(\Lambda^2E)^{-1}`.

**File/location:** cote93, scan086, the two “ext. de … par …” displays. **Kind:** unproved claim. **Context queries:** Gamma; Sym; trace; Dieudonné.

The appearances of `Gamma²E` and `Sym²E` encode different sequences: after twisting by `(det E)^(-1)`, the kernel of trace is the divided-square submodule of `E tensor E`, whereas the quotient by the alternating scalar line is the symmetric square. In a basis, the first is spanned by `x tensor x`, `x tensor y+y tensor x`, `y tensor y`, and the second imposes `x tensor y-y tensor x=0`; this checks exactness and explains why identifying the two requires care at 2. Context comparison: Hua §VII compresses these displays into `g=M/O` and `g′=trace-zero`, while **MPL_93_002-046 C19** (scan043) warns in another setting that local freeness is extra work; the present free-basis check does not settle that crystalline claim.

### OP04 — The determinant inverse in the tangent formula

**Short quote (frozen TeX, scan 086):** `\unsure{f^*\Lambda^2E|f^*(\Lambda^2E)^{-1}}`.

**File/location:** cote93, scan086, inserted display identifying `t_{P/X}`. **Kind:** reading question. **Context queries:** tangent; det; projective; t_{P/X}.

The frozen alternative is `L² tensor f*(Lambda²E)` versus `L² tensor f*(Lambda²E)^(-1)`. With the quotient convention explicitly used on087, the rank-two Euler sequence gives the inverse-determinant expression, but that mathematical check cannot choose the ink after the freeze. Context comparison: Hua §VII, pages85–86, uses `Sym²(E) tensor(det E)^(-1)` and [OP-S1] specifies the quotient convention; neither is new manuscript evidence, and no matching result-state entry resolves this reading.

### OP05 — “Expliciter!”: a bracket calculation is available

**Short quote (frozen TeX, scan 086):** `\unsure{expliciter|expliquer} !`.

**File/location:** cote93, scan086, left margin beside the quadratic-functor diagrams; scan088, multiplication table. **Kind:** self-flagged. **Context queries:** expliciter; crochet; Killing; Sym.

The margin's “expliciter !” asks for actual bilinear maps, and scan088 later supplies a local bracket table. In the frame `e=E12`, `h=diag(1,0) mod scalars`, `f=E21`, direct matrix commutators give `[e,h]=-e`, `[f,h]=f`, `[e,f]=2h`, providing the missing local calculation and its normalization [proof checksA]. Context comparison: Hua §VII, pages85–88, restates the structures without this explicit certificate; this adds a check, not a new result under any settled `RESULTS_STATE` ID.

### OP06 — The Killing forms do not remove the bad-characteristic issue

**Short quote (frozen TeX, scan 087):** `2 inv.!`.

**File/location:** cote93, scan086, “formes de Killing” and scan087, “2 inv.!” **Kind:** self-flagged. **Context queries:** Killing; orthogonal; Car.2.

The same basis gives Killing matrix `[[0,0,4],[0,2,0],[4,0,0]]`, of determinant `-32`; it is perfect when 2 is invertible and degenerates in characteristic two [proof checksA]. Thus the inserted “2 inv.!” is a necessary structural condition for recovering the dual flag from this pairing. Context comparison: Hua §VII, page86, repeats orthogonality, while **MPL_93_002-046 P01** concerns the earlier Schwarzian and contains no Killing-form result; the matrix check adds the precise restriction absent from any settled result-state row.

### OP07 — The question M versus first jets of the vertical tangent

**Short quote (frozen TeX, scan 086):** `M\overset{?}{\simeq}f_*\bigl(P^1_{P/X}(\underline t_{P/X})\bigr)`.

**File/location:** cote93, scan086, `M ?= f_*P¹(t_{P/X})` and doubtful “additivement ?”. **Kind:** self-flagged. **Context queries:** principal; P^1; additivement; tangent.

The pushed-forward relative first-jet sequence is canonically split as `O_X direct-sum g`, because the universal relative jet is linear over functions from X; if 2 is invertible, reduced trace divided by2 also splits `M -> g`, giving a compatible module identification [proof checksC]. In characteristic two there is no conjugation-equivariant trace retraction of M onto its scalar line, so this argument cannot give a canonical identification with those subquotients, although a bare vector-space isomorphism is a different question. Context comparison: Hua §VII omits this question, and the principal-parts material later in §XI, pages141–147, is related constructional evidence only; `RESULTS_STATE` has no matching entry.

### OP08 — The centre and the vertical-vector-field quotient

**Short quote (frozen TeX, scan 086):** `en est le centre`.

**File/location:** cote93, scan086, “O_X en est le centre” and `g = f_*t_{P/X}`. **Kind:** unproved claim. **Context queries:** centre; vector; Aut; projectif.

For a local matrix algebra, commutation with the matrix units forces an element of its associative centre to be scalar, and the infinitesimal projective action identifies its quotient with the three relative vector fields on the projective line. This proves the local identification on the sheet and lets it descend with the projective bundle; it does not identify every automorphism of the resulting Lie algebra with a projective automorphism in bad characteristic. Context comparison: Hua §VII, page85, repeats the quotient, adding a coordinate-free continuation to **MPL_93_002-046 P01** at scan036 without supplying a settled result-state proof.

### OP09 — Trace-zero and quotient-by-scalars differ at2

**Short quote (frozen TeX, scan 086):** `can, iso si 2 inv. sur $X$`.

**File/location:** cote93, scan086, `g′ -> g can, iso si 2 inv.` **Kind:** unpursued implication. **Context queries:** trace; sl; characteristic; Car.

The canonical map becomes an isomorphism by subtracting `(trace A)/2` from A when 2 is invertible. In characteristic two the identity matrix belongs to the trace-zero algebra and gives a nonzero centre, whereas `pgl2` has zero centre; hence the qualification cannot be removed [proof checksA]. Context comparison: Hua §VII expressly retains this distinction, so these pages add a concrete reason to the projective lead **MPL_93_002-046 P01**, not a contradiction of it.

### OP10 — The warning beside automorphism groups is substantive

**Short quote (frozen TeX, scan 086):** `attention à la Car. (notamment Car. 2!)`.

**File/location:** cote93, scan086, right-margin automorphism chain and “attention à la Car. (notamment Car.2!)”. **Kind:** self-flagged. **Context queries:** automorphism; Car.; PGL; Lie.

In characteristic two write `pgl2=W semidirect kh`, with `W=span(e,f)` abelian and `[h,w]=w`; every invertible linear map of W, together with `h -> h+v` for v in W, is a Lie automorphism. This gives a six-dimensional automorphism group, whereas the projective group has dimension three, so the unqualified Lie-automorphism identification fails; the refined version **OP10-R** retains the characteristic restriction or the projective-group structure [proof checksA]. Context comparison: Hua §VII repeats the author's caution, and no `RESULTS_STATE` entry has already settled this chain.

### OP11 — Special ideals and Borel data need their precise structure

**Short quote (frozen TeX, scan 086):** `schéma des Idéaux à gauche`.

**File/location:** cote93, scan086, final “Idéaux à gauche … spéciaux” and Borel list. **Kind:** unproved claim. **Context queries:** idéal; Borel; special; Brauer.

The “spéciaux” condition is locally a rank-two direct-summand left ideal in `End(E)`, equivalently the maps annihilating a rank-one kernel of a quotient E; this checks the projective-line parametrization in the split model. Passing from group Borels to arbitrary Lie subalgebras in characteristic two is a separate issue, already signalled by OP10, and is not established merely by this ideal computation. Context comparison: Hua §VII, page85, repeats the Borel correspondence; no matching settled `RESULTS_STATE` entry supplies its unrestricted Lie version.

### OP12 — The standard rank-two representation does not descend to PGL2

**Short quote (frozen TeX, scan 087):** `rep. \unsure{vraie|naïve}`.

**File/location:** cote93, scan087, top list “E=module d'une ‘rep. vraie|naïve’”. **Kind:** reading question. **Context queries:** representation; vraie; naïve; GL.

The frozen word remains `vraie|naïve`, but the list itself cannot mean that the standard rank-two representation of GL2 descends unchanged to PGL2: the central scalar matrices act nontrivially on E. E is a module for its endomorphism algebra and for SL(E); a projective action, a local lift, and an actual representation of the quotient group are distinct data. Context comparison: Hua §VII omits this list, and neither **MPL_93_002-046 P01** nor any settled result-state entry determines the intended reading or a descent assertion.

### OP13 — A marked section supplies the global normalized extension

**Short quote (frozen TeX, scan 087):** `avec section marquée $\sigma$`.

**File/location:** cote93, scan087, 1.2(a–b) and the rigidification of L. **Kind:** unproved claim. **Context queries:** section; rigidifié; extension; Omega.

Unlike OP01's unmarked situation, a section sigma gives a relative degree-one divisor and hence a degree-one line bundle, which can be twisted from X so that its restriction to sigma is trivial. Pushing forward then gives the displayed extension `0 -> Omega -> mathcal L -> O_X -> 0`; its quotient defines the marked section using [OP-S1]. Context comparison: Hua §VII, page86, restates this construction, while `RESULTS_STATE` has no corresponding marked-bundle result, so the present pages add to the earlier coordinate calculation **MPL_93_002-046 P01**.

### OP14 — The deleted sixth description remains a reading problem

**Short quote (frozen TeX, scan 087):** `f) Une \unsure{$O_X$ Algèbre|Ext($O_X$)}`.

**File/location:** cote93, scan087, cancelled 1.2(f). **Kind:** reading question. **Context queries:** algèbre; rigidifiée; nilpotente; extension.

The frozen alternatives include `O_X Algèbre|Ext(O_X)`, `P_2|Omega_2`, and “rigidité|rigidifiée”, all inside a deletion. Hua §VII, page86, interprets the cancelled text as an augmented nilpotent algebra of level2, but labels its own reading uncertain; this is a comparison to test against a better image, not a replacement of the preserved text. No exact entry of `notes/RESULTS_STATE.md` settles the cancelled proposal or its equivalence.

### OP15 — The first-jet recovery distinguishes I² from I

**Short quote (frozen TeX, scan 087):** `\unsure{\mathcal I^2L|\mathcal IL}`.

**File/location:** cote93, scan087, `f_*L = f_*(L/I²L) = sigma*P¹(L)`. **Kind:** reading question. **Context queries:** I^2; principal; jet; rigidifié.

The frozen alternative `I²L|IL` has different ranks: the first infinitesimal neighborhood has length2 on each projective-line fibre, while restriction to the section alone has length1. For I² the kernel on a fibre is `O(1)(-2)=O(-1)`, with H0 and H1 zero, proving the asserted pushforward isomorphism in the projective-bundle setting and identifying why the square matters. Context comparison: Hua §VII does not reproduce this display, while its later §XI uses principal parts; no result-state entry selects the ink, which remains unchanged.

### OP16 — Compactifying the extension torsor

**Short quote (frozen TeX, scan 087):** `clôture projective du torseur sous $W(\Omega)$ défini par l'extension.`.

**File/location:** cote93, scan087, “clôture projective du torseur sous W(Omega)”. **Kind:** unproved claim. **Context queries:** torseur; W; compactification; projective.

Locally splitting the extension identifies the complement of the marked section in `P(mathcal L)` with the affine line modeled on Omega, and two splittings differ by a translation in Omega. These translation changes glue the claimed torsor and its projective compactification, with the ordering of section and complement fixed by the quotient convention on the page. Context comparison: Hua §VII, pages86–87, restates this geometric interpretation; no matching settled result-state entry replaces the local gluing check.

### OP17 — The annihilator ideal is a left ideal

**Short quote (frozen TeX, scan 087):** `avec idéal annulateur de $\Omega$`.

**File/location:** cote93, scan087, “M=End mathcal L, avec idéal annulateur de Omega”. **Kind:** unpursued implication. **Context queries:** annulateur; idéal; End; Omega.

Maps `mathcal L -> mathcal L` which vanish on Omega form `Hom(mathcal L/Omega,mathcal L)` and are preserved by multiplication on the left, making the rank-two special ideal of OP11 explicit. The statement uses the kernel Omega of the marked quotient; substituting the image of that quotient would change the convention. Context comparison: Hua §VII compresses this part of1.2, and no exact `RESULTS_STATE` ID addresses the left/right ideal convention.

### OP18 — The three-step flag and the second use of mathcal L

**Short quote (frozen TeX, scan 087):** `et $\mathcal L$ est une ss.-Alg. de Borel`.

**File/location:** cote93, scan087, `Fil1=Omega`, `Fil2=mathcal L`, graded pieces. **Kind:** unproved claim. **Context queries:** filtration; Sym; Borel; mathfrak.

Multiplication gives `ker(Sym² mathcal L -> O_X)=Omega tensor mathcal L`, so after twisting by `Omega^(-1)` the middle filtered piece is indeed isomorphic to mathcal L. A local upper-triangular matrix identifies it with the Borel Lie submodule and gives graded pieces `(Omega,O_X,Omega^(-1))`; this checks the reuse of the same letter for an extension and a subalgebra. Context comparison: Hua §VII, page86, explicitly explains the reused notation, which is new structural evidence relative to **MPL_93_002-046 P01**, not an already settled entry.

### OP19 — The request to express the pair from the extension

**Short quote (frozen TeX, scan 087):** `\unsure{exprimer|expliquer} aussi`.

**File/location:** cote93, scan087, left margin “exprimer|expliquer aussi … (g,mathcal L)”. **Kind:** self-flagged. **Context queries:** exprimer; Borel; extension; unipotente.

The margin asks for an intrinsic reconstruction from `0 -> Omega -> mathcal L -> O_X -> 0`, and the symmetric-square construction plus its multiplication submodule supplies one locally and functorially. The phrase identifying Omega with the unipotent part must still distinguish the unipotent radical of a group Borel from the behavior of arbitrary Lie subalgebras in characteristic two. Context comparison: Hua §VII, page86, restates the construction without preserving this request as a separate task; no matching settled result-state ID is available.

### OP20 — “Vérifier!” on the dual quotient has a conditional answer

**Short quote (frozen TeX, scan 087):** `vérifier!`.

**File/location:** cote93, scan087, right margin `g/Omega = mathcal L-dual`, “vérifier!”. **Kind:** self-flagged. **Context queries:** vérifier; dual; Killing; filtration.

For 2 invertible, the perfect Killing pairing and `Omega-perp=mathcal L` give the displayed isomorphism, with the opposite filtration [proof checksA–B]. It fails without that restriction: on a characteristic-two genus-one curve take a nonsplit extension of O by O, for which the upper-triangular transition calculation makes `g/Omega` split but `mathcal L-dual` nonsplit; **OP20-R** is the version with2 invertible. Context comparison: Hua §VII, page86, repeats the question without resolving its characteristic scope, and no `RESULTS_STATE` entry settles it.

### OP21 — Quotient by mu2 is a group-scheme statement

**Short quote (frozen TeX, scan 087):** `déduits par passage au quot. par Centre $\mu_2$`.

**File/location:** cote93, scan087, `G′=SL_Omega mathcal L`, `G,B` obtained modulo centre mu2. **Kind:** unproved claim. **Context queries:** mu_2; SL; quotient; centre.

The map from SL2 to PGL2 has kernel mu2 and is a surjection as an fppf sheaf: locally an invertible determinant acquires a square root, allowing a matrix representative of determinant1. This explains why the quotient statement can remain meaningful in characteristic two even though the Lie-algebra isomorphism fails; mu2 is then not étale. Context comparison: Hua §VII, pages85–86, uses “revêtement universel”, but the sheaf quotient must not be replaced by an étale or topological covering; no exact settled result-state ID covers this distinction.

### OP22 — The “faux” margin has an uncertain target

**Short quote (frozen TeX, scan 087):** `\margin{\uline{faux}}`.

**File/location:** cote93, scan087, lower-right1.4 paragraph and isolated “faux”. **Kind:** self-flagged. **Context queries:** faux; section; plat; connexion.

The page explicitly says that sigma is not assumed horizontal and also carries a marginal “faux”, whose precise target is not securely identified by the frozen reading. Later scans090–091 distinguish horizontal and transverse sections, so the margin cannot safely be treated as a retraction of the entire `(P,sigma,C)` programme or as permission to remove a condition. Context comparison: Hua §VII, pages88–94, supplies a smooth-base exposition and omits this “faux”; no result-state entry resolves its attachment.

### OP23 — The proposed extension-language description is carried out locally

**Short quote (frozen TeX, scan 087):** `\unsure{Il nous sera peut-être commode d'expliciter|Il me sera peut-être commode d'expliciter}`.

**File/location:** cote93, scan087, “Il nous sera peut-être commode d'expliciter …” and scans089–090. **Kind:** self-flagged. **Context queries:** expliciter; connexion; extension; commode.

The proposed expression in terms of `(mathcal L,Omega)` becomes the split-basis connection calculation on089–090, so it is a research intention pursued within the supplied pages. Its validity for all bracket-compatible Lie connections still requires the characteristic restriction stated on090, whereas the projective-bundle version retains its group origin. Context comparison: Hua §VII, pages88–94, reorganizes this into a finished discussion; **MPL_93_002-046 P01** supplies earlier differential formulas but no proof of this equivalence.

### OP24 — Two ordered disjoint sections split the extension

**Short quote (frozen TeX, scan 088):** `\uline{deux} sections \uline{disjointes}`.

**File/location:** cote93, scan088, 1.3 and the infinity/zero margin. **Kind:** unproved claim. **Context queries:** disjointes; splittage; W; section.

The two sections are ordered, and a second section disjoint from the first is a splitting of the normalized extension, giving `P=P(Omega direct-sum O_X)` with the indicated infinity and zero. Reversing the order dualizes the line datum, so forgetting the ordering would change the classification. Context comparison: Hua §VII, pages86–87, restates the split description; no matching settled result-state entry supplies the order convention.

### OP25 — The two special ideals give a direct sum

**Short quote (frozen TeX, scan 088):** `somme directe de deux Idéaux spéciaux`.

**File/location:** cote93, scan088, bracketed “M somme directe de deux Idéaux spéciaux”. **Kind:** unproved claim. **Context queries:** idéaux; somme directe; splitting; Azumaya.

For `E=Omega direct-sum O`, the two annihilator left ideals consist respectively of matrices with one prescribed column zero, and their sum is the whole endomorphism algebra with zero intersection. This checks the bracketed assertion and shows that it is a decomposition into left modules, not a decomposition of algebras into two-sided ideals. Context comparison: Hua §VII compresses this datum into the split bundle; neither **MPL_93_002-046 P01** nor another result-state entry treats it.

### OP26 — The trace-zero bracket has a different normalization

**Short quote (frozen TeX, scan 088):** `Mais dans la table de multiplication`.

**File/location:** cote93, scan088, parenthetical replacement table for g′. **Kind:** unproved claim. **Context queries:** sl; multiplication; -2; crochet.

Using `H=diag(1,-1)` in the trace-zero algebra gives `[e,H]=-2e`, `[f,H]=2f`, `[e,f]=H`, exactly the replacement coefficients `-2,+2,1`. The quotient map sends H to2h, so these tables explain both the good-characteristic identification and its failure at2 [proof checksA]. Context comparison: Hua §VII, pages85–87, restates the equivalence with a restriction but suppresses this comparison of coefficients; the check adds to **MPL_93_002-046 P01** without settling any separate crystalline entry.

### OP27 — “One of the two” root lines is not intrinsic to the bad-characteristic Lie algebra

**Short quote (frozen TeX, scan 088):** `le choix d'une des deux sous-Algèbres`.

**File/location:** cote93, scan088, Cartan subalgebra and “une des deux sous-Algèbres … normalisées”. **Kind:** own idea. **Confidence:** high for the counterexample; the intended additional group structure remains a reading issue. **Context queries:** Cartan; unipotent; normalisées; Car.

In characteristic two, `ad(h)` acts by the same scalar on `span(e,f)`, so every line in that plane is normalized by h, not just the two displayed root lines. The refined claim **OP27-R** uses the group torus and its root subgroups, or restricts to the characteristic setting where the two Lie weights are distinct. Context comparison: Hua §VII, page87, repeats the two-line formulation, while the manuscript's own characteristic warning on086 and doubtful margin on088 require this qualification; no result-state entry already resolves it.

### OP28 — The terminal “couple de Killing” is not silently regularized

**Short quote (frozen TeX, scan 088):** `avec couple de \unsure{Killing}`.

**File/location:** cote93, scan088, last two equivalences for G and G′. **Kind:** reading question. **Context queries:** Killing; couple; Cartan; Borel.

The frozen word is doubt-marked as “Killing”, whereas the surrounding mathematics suggests data involving a torus and opposite Borel or root subgroups. Hua §VII stops at a Cartan and a chosen unipotent subgroup and therefore does not supply a reliable reading of those two terminal lines. There is no matching result-state entry, and the possible mathematical reformulation remains outside the transcription.

### OP29 — The reference connection is locally flat

**Short quote (frozen TeX, scan 089):** `Une connexion (sans courbure)`.

**File/location:** cote93, scan089, “Une connexion (sans courbure) c0 est obtenue par …”. **Kind:** unproved claim. **Context queries:** courbure; c_0; splittage; delta.

After the stated local splitting and choice of delta, the bracket structure constants are constant and c0 differentiates only the three coefficients, so it preserves the bracket and has square zero. This verifies the local reference connection; it does not assert a global splitting or the existence of a global flat connection on every bundle. Context comparison: Hua §VII, page88, repeats this construction and explicitly distinguishes a general connection from a flat one; no result-state entry settles global existence.

### OP30 — “Every derivation is inner” is restricted on the following page

**Short quote (frozen TeX, scan 089):** `toute dérivation de $\mathfrak g$ est intérieure!`.

**File/location:** cote93, scan089, “toute dérivation de g est intérieure!”, and scan090, lower “si2 inv. — sinon … sur P, ou G”. **Kind:** withdrawn in the same text. **Context queries:** dérivation; intérieure; si 2; connexion.

The unqualified claim on089 is false in characteristic two: `D(e)=f`, `D(f)=D(h)=0` is a derivation and cannot be inner, as the exact matrix calculation shows [proof checksA]. Scan090 supplies the appropriate restriction, **OP30-R**: with2 invertible all derivations are inner, while in the general case one must retain connections originating on P or G. Context comparison: Hua §VII, page88, repeats the inner-derivation assertion without the nearby correction's force; the present two-scan comparison adds a qualification absent from every settled result-state entry.

### OP31 — The unfinished formula is pursued on090

**Short quote (frozen TeX, scan 089):** `\overset{?}{=}`.

**File/location:** cote93, scan089, final question-mark equality, deletion, and isolated plus sign; scan090, opening calculation. **Kind:** self-flagged. **Context queries:** connexion; varpi; formule; calcul.

The sheet ends with a question mark and an unfinished addition, so its formula is a live calculation rather than a completed proof. Scan090 resumes it, and the local expression `C=d+ad(ae+bh+cf)` gives the missing three-by-three matrix [proof checksA], subject to OP30's scope. Context comparison: Hua §VII, pages88–89, replaces the interrupted calculation by a finished proposition; no result-state entry provides the missing handwritten line.

### OP32 — The coefficient calculation is checked without rewriting its annotations

**Short quote (frozen TeX, scan 090):** `\text{poids }2`.

**File/location:** cote93, scan090, first display and three weight-annotated equations. **Kind:** reading question. **Context queries:** poids; lambda; coefficient; -2.

The frozen first line retains an uncertain external lambda and a lambda inside an underbrace, and the small margin preserves a deleted sign. The independently calculated matrix has columns `(b,-2c,0)`, `(-a,0,c)`, `(0,2a,-b)`, fixing the algebraic comparison but not authorizing a cleaner transcription of those annotations [proof checksA]. Context comparison: Hua §VII, page89, reports the graded conclusion rather than these crowded expressions; no result-state entry selects their doubtful glyphs.

### OP33 — Filtration transversality requires the corrected connection category

**Short quote (frozen TeX, scan 090):** `\unsure{tte|toute} connexion $c$ satisfait`.

**File/location:** cote93, scan090, “tte connexion c satisfait …”. **Kind:** own idea. **Confidence:** high; a concrete flat counterexample and the inner-matrix calculation. **Context queries:** filtration; connexion; Lie; caractéristique.

For a projective-bundle connection the displayed matrix indeed raises the flag by at most one, but over characteristic-two `A¹` the bracket-compatible flat connection `d+D dt` from OP30 sends e directly to fdt and violates that property. The refined claim **OP33-R** uses projective-group connections, or bracket-compatible Lie connections with2 invertible, exactly as the lower paragraph of090 requires [proof checksD]. Context comparison: Hua §VII calls the property a proposition for every such Lie connection; these scans qualify that formulation rather than supplying an unrestricted theorem under any result-state ID.

### OP34 — Why the induced maps on the graded pieces are linear

**Short quote (frozen TeX, scan 090):** `qui est \uline{linéaire}`.

**File/location:** cote93, scan090, underlined “linéaire” after `c_{i,i+1}`. **Kind:** unproved claim. **Context queries:** gradué; linéaire; Leibniz; filtration.

For a section x in Fili, the Leibniz term `x tensor df` remains in Fili and therefore vanishes in the next graded quotient. This checks the asserted O-linear graded maps once the filtration property is available; it is not a statement that the connection itself is O-linear. Context comparison: Hua §VII, page89, restates the maps, with no corresponding settled item in `RESULTS_STATE`.

### OP35 — The boxed factor −2 is correct in the chosen normalization

**Short quote (frozen TeX, scan 090):** `\boxed{c_{1,2}=-2c_{2,3}}`.

**File/location:** cote93, scan090, boxed `c_{1,2}=-2c_{2,3}`. **Kind:** unproved claim. **Context queries:** -2; normalisation; crochet; gradué.

The matrix for `ad(ae+bh+cf)` gives `c12=-2c` and `c23=c`, verifying the box and its dependence on scan088's bracket normalization [proof checksA,D]. In characteristic two the first map can vanish while the second is nonzero, which explains why the page consistently uses c23 to test preservation of the flag. Context comparison: Hua §VII, page89, repeats this relation; it extends the normalization issue in **MPL_93_002-046 P01** (scan036) to a different, explicitly checked Lie-theoretic normalization.

### OP36 — Horizontal section, preserved Borel, and preserved flag

**Short quote (frozen TeX, scan 090):** `On trouve que la connexion respecte la filtration ssi`.

**File/location:** cote93, scan090, first “NB” paragraph. **Kind:** unproved claim. **Context queries:** horizontale; Borel; filtration; section.

The vanishing of c23 means the local connection form is Borel-valued, which preserves the Borel reduction and hence the marked projective section; the same matrix then preserves both steps of the flag. Thus the three descriptions agree for connections on the projective bundle, while “a section of mathcal L tensor omega” describes their difference from a chosen local reference connection [proof checksD]. Context comparison: Hua §VII, page89, restates the equivalence, and no result-state entry establishes a global preferred reference connection.

### OP37 — The connection torsor is a sheaf-level object

**Short quote (frozen TeX, scan 090):** `forment un torseur sous $\mathfrak g\otimes\uline\omega$`.

**File/location:** cote93, scan090, lower “les connexions … forment un torseur”. **Kind:** unproved claim. **Context queries:** torseur; Conn; g; local.

Differences of projective-bundle connections are sections of `g tensor omega`, so the local connections form the claimed torsor, and OP30 explains the explicit condition for replacing them by all bracket-compatible Lie connections. A torsor is locally nonempty; this assertion alone does not furnish a global connection or a global origin. Context comparison: Hua §VII, pages88–94, restates this affine description and later gives global results only with additional geometric hypotheses; no exact result-state ID settles global existence here.

### OP38 — The normal-component quotient does have a canonical zero

**Short quote (frozen TeX, scan 090):** `\uline{Ce dernier} est splitté canoniquement`.

**File/location:** cote93, scan090, “Ce dernier est splitté canoniquement”. **Kind:** unproved claim. **Context queries:** canoniquement; splitté; Conn; normal.

Changing a local frame which preserves the section contributes a Borel-valued derivative term, so the normal component of the connection is intrinsic and zero precisely for section-preserving connections. This proves that the quotient torsor is canonically identified with `Omega^(-1) tensor omega`, even though the full connection torsor need not have a global origin [proof checksD]. Context comparison: Hua §VII, page89, presents the transverse map but does not separately prove this canonical-zero assertion; no settled result-state entry supplies it.

### OP39 — Fixing i leaves the Borel-valued torsor

**Short quote (frozen TeX, scan 090):** `d'où torseur $\mathrm{Conn}_i$ sous $\mathcal L\otimes\uline\omega$`.

**File/location:** cote93, scan090, “Conn_i sous mathcal L tensor omega”. **Kind:** unproved claim. **Context queries:** Conn_i; restriction; i; torseur.

The kernel of `g tensor omega -> Omega^(-1) tensor omega` is `mathcal L tensor omega`, so fixing the normal component i leaves precisely that torsor. This is a local affine-linear argument and preserves the distinction between a prescribed section i and an actual global connection above it. Context comparison: Hua §VII, pages89–90, restates this reduction, while **MPL_93_002-046 P01** contains no torsor statement and no other matching result-state entry settles it.

### OP40 — Restriction to Omega is a first-order operator with prescribed symbol

**Short quote (frozen TeX, scan 090):** `C_\Omega(f\omega)-fC_\Omega(\omega)\simeq\omega\otimes df.`.

**File/location:** cote93, scan090, final displayed Leibniz condition. **Kind:** unproved claim. **Context queries:** op. diff.; ordre; symbol; principal.

The displayed difference `C_Omega(f eta)-f C_Omega(eta)=eta tensor df` says that the first-order symbol is the inclusion `Omega tensor omega -> mathcal L tensor omega`. Its quotient is the linear map `-2i`, and changing the full connection by `Omega tensor omega` leaves this restriction fixed [proof checksD]. Context comparison: Hua §VII, pages90–93, develops the same statement through principal parts, consistent with [OP-S3]; no settled result-state entry already identifies the restricted triple.

### OP41 — The quotient operator really is more informative in characteristic two

**Short quote (frozen TeX, scan 090):** `(p.e. en Car. $2$?) c'est \unsure{peut-être|encore} plus précis`.

**File/location:** cote93, scan090, right margin “p.e. en Car.2? … plus précis”. **Kind:** self-flagged. **Context queries:** plus précis; Car.; quotient; C_Omega.

For connections from P, the operator from `g/Omega` to `(g/mathcal L) tensor omega` is well-defined and detects c through the image of h, while `C_Omega(e)=b e-2c h` loses c in characteristic two. This verifies the proposed greater precision, without using the questionable bad-characteristic identification `g/Omega=mathcal L-dual`; when2 is invertible the two restricted data recover each other [proof checksD]. Context comparison: Hua §VII omits this margin, and no `RESULTS_STATE` item resolves it, so this is an added answer to the author's own question.

### OP42 — A prescribed restricted operator reduces the structure group again

**Short quote (frozen TeX, scan 091):** `une restriction du Groupe structural`.

**File/location:** cote93, scan091, first paragraph, “restriction|réduction du Groupe structural”. **Kind:** unproved claim. **Context queries:** réduction; Conn; groupe structural; Omega.

Within the torsor at fixed i, two connections have the same `C_Omega` exactly when their difference lies in `Omega tensor omega`, as the matrix calculation shows. Thus the reduction assertion is correct in OP30's connection category; it fixes the restriction, not all coefficients of a connection. Context comparison: Hua §VII, pages90–94, restates this reduction, with no exact settled result-state entry for it.

### OP43 — The transversal isomorphism forces2 to be a unit

**Short quote (frozen TeX, scan 091):** `ce qui implique $2$ inv.`.

**File/location:** cote93, scan091, inserted “ce qui implique2 inv.” **Kind:** unpursued implication. **Context queries:** 2 inv.; iso; transverse; i.

The composite `-2i:Omega -> omega` is an isomorphism of line bundles, so in local trivializations the product of2 with a scalar is a unit, forcing both factors to be units. This proves the insertion and shows why the specific restricted-data normal form excludes characteristic two, even though projective-bundle connections themselves remain meaningful there. Context comparison: Hua §VII, pages90–93, assumes2 invertible from the outset; **MPL_93_002-046 P01** and the integral Schwarzian candidate in the result register do not remove this distinct factor2 restriction.

### OP44 — The principal-parts normal form follows from its universal property

**Short quote (frozen TeX, scan 091):** `est défini à isom unique près par $X/S$`.

**File/location:** cote93, scan091, `mathcal L=P¹(omega) tensor omega^(-1)` and “défini à isom unique près”. **Kind:** unproved claim. **Context queries:** P^1; isom unique; universel; principal.

Universality gives a map `P¹(Omega) -> mathcal L tensor omega` which is the identity on the kernel `Omega tensor omega` and the isomorphism `j=-2i` on the quotient. It is therefore an isomorphism, and identifying Omega with omega by j yields exactly the stated first-jet bundle and universal operator [proof checksE; OP-S3]. Context comparison: Hua §VII, pages90–93, restates this argument using an i-based normalization and later diagrams; the proof here needs only the frozen091 statement and does not claim to have inspected those later pages, nor to re-prove a settled result-state entry.

### OP45 — “Exists iff omega is invertible” has an inherited scope

**Short quote (frozen TeX, scan 091):** `et existe ssi $\uline\omega=\underline\Omega^1_{X/S}$ est inversible`.

**File/location:** cote93, scan091, parenthetical “existe ssi omega … est inversible”. **Kind:** unproved claim. **Context queries:** existe; inversible; lisse; principal.

With2 already invertible, the first-jet construction supplies the restricted triple when `omega=Omega¹_{X/S}` is a line bundle, and an isomorphism `Omega -> omega` conversely forces that line-bundle property. The assertion concerns the restricted data; it neither proves that X/S is smooth merely from the rank of its differential sheaf nor asserts a global full connection extending the restriction. Context comparison: Hua §VII adds smoothness for its oper discussion, so its setting is stronger than the literal start of086–091; no result-state item eliminates this distinction.

### OP46 — The remaining full connections vary by quadratic differentials

**Short quote (frozen TeX, scan 091):** `à $\Omega\otimes\uline\omega$`.

**File/location:** cote93, scans090–091, successive reductions of Conn. **Kind:** own idea. **Confidence:** high for the local torsor calculation; no claim of global nonemptiness over every base. **Context queries:** quadratique; Omega^2; torseur; oper.

Combining OP42 with `Omega=omega` shows that full connections extending the canonical restricted data form a sheaf torsor under `Omega tensor omega=omega²`, so uniqueness of the restricted triple is not uniqueness of the full connection. Hua §VII's later sentence instead prints `Omega² tensor omega=omega²`, whose left-hand side would have tensor degree3 under that identification; the manuscript091 supports the degree2 expression [proof checksE]. This is a contextual correction outside the transcription, related to **MPL_93_002-046 P01/P03** but not already settled by them.

### OP47 — The oper comparison identifies a precise projective object

**Short quote (frozen TeX, scan 087):** `(P,\sigma,C)`.

**File/location:** cote93, scans087 and090–091, `(P,sigma,C)` and the nonzero transverse map. **Kind:** unpursued implication. **Context queries:** oper; projective; transverse; uniformisation.

For a smooth complex curve this is the projective-bundle description of a PGL2-oper: a connection with a section whose covariant derivative is nowhere zero; [OP-S4, §§1.2,2.7,3.1–3.3] gives the comparison and the quadratic-differential parameter. This identifies a concrete bridge from the coordinate Schwarzian on072–074 to the geometric data on086–091, but does not identify the connection as Gauss–Manin for a specified family. Context comparison: Hua §VII calls these opers, strengthening the projective interpretation **MPL_93_002-046 P01/P03** while leaving **P05–P08** and README.md's S20 arithmetic question open.

### OP48 — The sl index is a contextual reading question

**Short quote (frozen TeX, scan 086):** `\mathfrak{sl}(\unsure{1|2})_X`.

**File/location:** cote93, scan086, 1.1(d′). **Kind:** reading question. **Context queries:** sl(1); sl(2); index; Lie.

The frozen reading preserves `sl(1|2)` rather than selecting a mathematically expected index. Hua §VII explicitly says that it reads the source's `sl(1)` as `sl(2)`, and the rank-two constructions make2 the natural mathematical interpretation; neither consideration revises the ink-based alternative. No exact `RESULTS_STATE` entry independently resolves the index.

### OP49 — The final universal-operator subscript stays doubtful

**Short quote (frozen TeX, scan 091):** `d^1_{X/S,\underset{\uline\omega}{\unsure{\omega|\infty}}}`.

**File/location:** cote93, scan091, final `d¹` subscript. **Kind:** reading question. **Context queries:** d^1; omega; infini; universel.

The frozen subscript is marked `omega|infty`, with the nearby underlined omega preserved. Hua §VII, page90 and its continuation, interprets the operator as the universal first derivative on omega, consistent with OP44's mathematics, but this remains a post-freeze comparison rather than evidence selecting the small handwritten sign. There is no matching result-state entry which resolves that glyph.

### OP primary-source register

| ID | Primary source and exact locus | Use and limits |
| --- | --- | --- |
| **OP-S1** | Stacks Project, [§27.21, tag01OA](https://stacks.math.columbia.edu/tag/01OA), definition and quotient functor. | Fixes the convention for P(E); it does not classify every Brauer–Severi curve by a global E. |
| **OP-S2** | Stacks Project, [§59.62, tag0A2J](https://stacks.math.columbia.edu/tag/0A2J), definition and Lemma59.62.1. | Étale-local matrix algebras and the line-twist ambiguity of endomorphism-algebra presentations. |
| **OP-S3** | Stacks Project, [Lemma10.133.6, tag09CN](https://stacks.math.columbia.edu/tag/09CN), first principal-parts sequence and symbol. | Compared with the short exact-sequence argument above; the manuscript reading is independent of this source. |
| **OP-S4** | A. Beilinson and V. Drinfeld, [Opers](https://arxiv.org/pdf/math/0501398), §§1.2,2.7,3.1–3.3. | Modern comparison over smooth complex curves; no blanket positive-characteristic or Gauss–Manin identification is imported. |
