# Conjecture lettering: research evidence after the freeze

Prepared only after the cote 11 transcription was frozen at 2026-11-15 19:37:25 UTC and the context was opened. No manuscript image was opened by this research worker, and no transcription fragment was changed. `README.md` and `notes/RESULTS_STATE.md` were read before this comparison.

## Result and scope

The frozen cote 11 text supplies a correspondence construction and Poincaré/bivariant algebra formalism, but it supplies no labeled list of the standard conjectures A–D. Its only occurrence of `conject` is the Tits conjecture in the reused typescript on scan 016, and its isolated underlined A on scan 027 heads the subsequent definitions of a Poincaré-algebra category and a functor. The lettering evidence consequently comes from the supplied first-pass transcription of cote 16, chiefly scans 044–050; its status remains a context transcription claim, with its recorded doubts retained.

**A complete verified four-letter permutation cannot be extracted from these witnesses.** The strongest comparison is draft C with printed B, through the actual complementary-degree inverse maps; draft A matches the algebraic-class portion of printed A. The draft's B and D are used in implications and bundled criteria, but their standalone definitions are not supplied in the searched context: their operational comparisons below are evidence to locate the missing definitions, not substituted definitions.

## Statement-to-statement table

Here CT means `MPL_16+47+54+44_transcription.tex`; the original subscript is uncertain between ℓ and χ in CT16/044–049, as its doubts file explicitly records. All varieties, coefficient fields, polarizations and degree ranges belong to the cited source's setting; the table does not transport a conjecture to an unstated setting.

| Draft witness and actual content | Printed comparison | Evidential limit |
|---|---|---|
| CT16/044 discusses dimensions of algebraic-class spaces `C^i` and `C^{n-i}`; CT16/045 identifies the critical maps on the self-product and adjacent hyperplane product; CT16/046 quantifies `A(k)=C(k)` over varieties. | G69, p. 196, A(a) asserts the cohomological Lefschetz isomorphisms; A(b) requires their restrictions to rational algebraic classes to be isomorphisms. | The draft evidence identifies the A(b) operation. Its use of the Lefschetz isomorphisms must remain visible; the full printed A(a)+(b) is not recovered by a bare relabeling of a critical-degree sentence. |
| CT16/048–049, draft C: the proof constructs the inverse of `v=L_X^{n-i}:H^i(X)→H^{2n-i}(X)` from an algebraic map in the opposite direction and rational characteristic-polynomial coefficients. | G69, p. 196, B requires algebraic Λ; K68, Proposition 2.3, p. 370, gives its complementary-degree inverse-map characterization. | This comparison identifies the same maps, with the same degrees and polarization, rather than identifying letters by their names. |
| CT16/044–045, draft B: `A+index` implies B, and the index qualification accompanies the displayed comparison of A with B. | K68, Corollary 3.9, p. 380, connects A with printed D in the presence of the strong Lefschetz and index conditions; printed D is equality of homological and numerical equivalence. | These parallel relations do not supply the missing standalone definition of draft B; do not print an unqualified B↔D dictionary entry. |
| CT16/048, draft D: D accompanies algebraic complementary-degree isomorphisms, and the proof invokes rationality of characteristic-polynomial coefficients. | K68, Theorem 2.9, p. 371, uses printed C with the same isomorphism requirement, or rationality with that requirement; printed C concerns algebraic Künneth projectors. | The comparison is of the bundled statements. CT16/040 also uses D(Y) with primitive-projector notation, increasing the need to locate a definition before asserting an isolated D↔C identity. |
| CT16/044 and 049 refer to the index condition, with 049 specifying `I(X×X)`. | K68, pp. 360, 380, writes I for positivity of the signed primitive algebraic pairing. | Keep the variety versus self-product, polarization and sign explicit. |

G69's C on p. 195 also carries a parenthetical requirement of representatives independent of ℓ. That extra clause must be recorded whenever G69's printed statement is used in a comparison with a fixed-theory draft condition.

## The actual inverse-map comparison

CT16/048 names `u:H^{2n-i}(X)→H^i(X)` and `v=L_X^{n-i}` and puts `w=uv`; CT16/049 concludes `w^{-1}u=v^{-1}`. This is an explicit identity: `(w^{-1}u)v=w^{-1}(uv)=1`, and `v` is the isomorphism named in the source, so its two-sided inverse is the displayed map. The inverse `e_i` in K68, Proposition 2.3, has precisely this source, target and defining inverse identity. Two such inverse maps S and T agree by `T=T(vS)=(Tv)S=S`; thus the comparison has an actual map-level verification and does not depend on a convention about letters.

The context's abstract operator algebra, CT16/015–017, also explicitly tracks the images of the degree projectors under its map from Φ and marks that condition “essentielle !”. This prevents dropping the grading data while making the comparison. K68, Proposition 2.3 and its proof through Lemma 2.4, is the printed location for recovering the complete operator from the inverse-map data; no new theorem or replacement proof is offered here.

## Four proposed notes for the main research register

### CL01 — Cote 11, scans 003 and 027 — reading question

The frozen phrases “`A: X→A(X)`” on scan 003 and “Catégorie … des Alg. de Poincaré” under the underlined A on scan 027 identify the roles of those occurrences; a full-text search found no standard-conjecture list in this packet. Context searches `conject|A(X)|B(X)|C(X)|D(X)` lead to CT16/044–050 and the earlier notes' S1, so cote 11 **adds** the correspondence formalism used for comparison while the labeling evidence remains in that context. This bears on **WG2 §2.4 #3**, status **question or plan item of the war game (round 2; unchecked)**; the supplied earlier S1 remains a first-pass research lead, not an established dictionary.

### CL02 — Cote 11, scan 003, Hom definition; context cote 16, scans 048–049 — unpursued implication

“`Hom_{V^A}(X,Y)=A(X×Y)`” gives the formal location for the context's algebraic correspondence inducing `u:H^{2n-i}(X)→H^i(X)`, and the context's identity `w^{-1}u=v^{-1}` identifies the inverse of the very map `v=L_X^{n-i}`. Search `inverse|correspondance|C_` finds CT16/048–049; cote 11 **adds** the general composition framework to that map-level calculation, whose operator content matches printed B via K68, Proposition 2.3, p. 370. The inverse identity is verified above without changing either degree or polarization, and the lemma/proposition location records the printed reconstruction of Λ. This bears on **WG2 §2.4 #3** and **WG2 §2.3 #2**, both **question or plan item of the war game (round 2; unchecked)**.

### CL03 — Cote 11, scans 003 and 034; context cote 16, scans 040 and 044–049 — reading question

The added formalism on scans 003 and 034 supplies objects, pairs `(f_*,f^*)` and projection formulas, while the context search `B_|D_|index|characteristic polynomial` finds draft B through “`A+index` implies `B`” on CT16/044 and draft D through a bundled duality/rationality criterion on CT16/048. These relations **restate** the evidence recorded as incomplete in the earlier context notes S1; neither the current pages nor the searched context supplies a standalone definition from which an unqualified draft B→printed D or draft D→printed C identification follows. The literal match of CT16/048's bundled criterion with K68, Theorem 2.9, p. 371, is a useful location lead, and CT16/040's primitive-projector use of D must be checked with it. This bears on **WG2 §2.4 #3**, status **question or plan item of the war game (round 2; unchecked)**.

### CL04 — Cote 11, scans 021–023; context cote 16, scans 045–046 — unpursued implication

Scan 023's “pour tous les `f:Y-X`” makes the range of objects and maps part of the stable-subfunctor construction, and the context likewise writes `A(k)=C(k)` together with “for every T” on CT16/046. Search `pour tous|produit|A(k)|every T` locates CT16/045–046's products and hyperplane flags; cote 11 **adds** a general language for closure under these operations rather than supplying an identification on a single fixed variety. G69, p. 196, explicitly records both `B(X)⇒A(X)` and `A(X×X)⇒B(X)`, so the self-product and universal quantifiers must survive any dictionary. This bears on **WG2 §2.2 #4** and **WG2 §2.4 #3**, both **question or plan item of the war game (round 2; unchecked)**.

## Search and source audit

| Search | Result used |
|---|---|
| Frozen cote 11: case-insensitive `conject`, `Lefschetz`, `lefschet`, `standard`, `motif` | Counts 1, 0, 0, 0, 0; the `conject` occurrence is Tits on 016. |
| Frozen cote 11: underlined A/B/C/D headings | The isolated A on 027 is followed by the Poincaré-algebra category and functor definitions. |
| Context transcription: labeled A/B/C/D uses, tracked by the current `cotefile` and `scanpage` | CT16/033, 040, 042, 044–050; main comparison witnesses 044–049. |
| Context notes: `letter|printed|standard|A(X)|B(X)|C(X)|D(X)` | S1 explicitly leaves draft B and D without secure standalone definitions; S9 and following sections discuss hyperplane flags and the inverse criterion. |
| Context doubts: cote 16 scans 044, 045, 048 | ℓ/χ ambiguities, a local A/Q ambiguity on 045, and the overwritten Cayley–Hamilton display remain recorded. |
| Results ledger: conjecture lettering, Lefschetz, inverse/correspondence content | WG2 §2.4 #3, WG2 §2.3 #2, WG2 §2.2 #4 are unchecked planning items; no reviewed ledger result supplies the missing labeling definitions. |

The ledger's reviewed LM7_PUSH D.44 concerns modular descent and its cited parts; it is not used to settle the lettering question. Unopened originals behind the abbreviated ledger rows are not cited as read sources.

### Verified primary references

- **G69:** Alexander Grothendieck, “Standard conjectures on algebraic cycles,” in *Algebraic Geometry, Bombay Colloquium 1968* (Oxford University Press, 1969), pp. 193–199, especially pp. 194–196, §§2–3. [Primary PDF](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf). The PDF was downloaded to scratch and pp. 195–196 were visually checked; p. 194's cycle-class definition was checked in retrieved primary-source text.
- **K68:** Steven L. Kleiman, “Algebraic cycles and the Weil conjectures,” in *Dix exposés sur la cohomologie des schémas* (1968), pp. 359–386: Proposition 2.3 and Lemma 2.4, p. 370; Theorem 2.9, p. 371; Proposition 3.6, p. 379; Corollary 3.9, p. 380. [Primary paper scan](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf). Checked through the primary paper's retrieved text; the host filename's 1966 is not substituted for the publication year.

The source comparisons use the cited primary texts. No unverified tertiary source is used for a mathematical claim.

## Addendum: exact coefficients of the two lowering operators

**Normalization check; current scan 11/003; context search `Lambda|6.5|6.14`: CT16/010, 013; relation: adds an exact operator comparison to CL02.** K68, p. 367, equations 1.4.2.1–1.4.2.2, visually checked in the primary PDF, gives the following formulas in the primitive decomposition used there: for \(a\in P^i\), put \(m=n-i\); both operators kill \(a\), and for \(1\leq j\leq m\),

\[
\Lambda(L^j a)=L^{j-1}a,
\qquad
{}^c\Lambda(L^j a)=j(m-j+1)L^{j-1}a.
\]

The exact conversion is the invertible degree-zero operator \(D\) defined by \(D|_{P^i}=1\) and \(D|_{L^jP^i}=j(m-j+1)\,1\) for \(j\geq1\): direct evaluation on each displayed summand gives \({}^c\Lambda=\Lambda D\) and \(\Lambda={}^c\Lambda D^{-1}\), while iteration gives \(\Lambda^mL^ma=a\) and \(({}^c\Lambda)^mL^ma=(m!)^2a\). The context's literal identity “\((\Lambda^{n-i}L^{n-i}-1)\pi_i=0\)” in CT16/013, (6.14), supplies the inverse-power comparison; CT16/010's dotted definition (6.5) remains unfilled, and the uncertain bounds and exponents in adjacent context formulas remain uncertain. Accordingly the table's verified draft-C/printed-B comparison is anchored to K68, Proposition 2.3, p. 370, which explicitly includes the inverse-map criterion and both lowering operators' algebraicity, rather than to equality of the two operator symbols suggested by G69's phrase “Λ-operation … of Hodge theory”; **WG2 §2.4 #3** remains **question or plan item of the war game (round 2; unchecked)**, and confidence in the coefficient calculation is high because it is a direct substitution in the visually verified formulas.

Primary locations for this addendum: [K68, pp. 367–370](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf), §§1.4.2–1.4.4 and Proposition 2.3; [G69, p. 196](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf). K68's introductory scalar-modification remark is on p. 359; the displayed formulas above spell out that remark without silently changing the operators.
