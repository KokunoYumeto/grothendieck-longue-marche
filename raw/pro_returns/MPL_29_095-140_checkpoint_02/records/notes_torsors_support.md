# Torsor and infinitesimal fundamental-group support

Research support by `/root/notes_torsors`, 2026-11-18, after the transcription freeze at 06:04:22 UTC. This file is ancillary evidence only: no source image or crop was opened, and no transcription, final note, or CHECK_EVENTS row was changed. The parent will assign final note IDs and integrate any selected text.

## Scope, pagination, and status rules

- Frozen source witnesses read: scans 124, 126, 129, 130, 137, 138, 139, 140, from their page-level `.tex` files.
- Context read: `context/README.md`, `context/hua_project/README.md`, relevant entries and status guidance in `context/notes/RESULTS_STATE.md`, and the passages of `context/hua_project/29.modern.tex` listed below.
- **Pagination:** our scan N corresponds to Hua page N−1. Thus Hua p.124 is scan125; Hua pp.136–139 are scans137–140. Hua pp.140–142 correspond to scans141–143 and are context-only continuations outside this package's supplied-image evidence.
- Credit all contextual interpretations as **Hua, modernised reading of cote 29**, followed by the actual subsection title. Credit the findings entry as **Hua, findings register, `29-fundamental-group-scheme-via-torsors`**.
- `RESULTS_STATE.md` expressly treats register statuses as the return's claims unless a stated intake/referee check says otherwise; package notes are first-pass leads. The Hua entry's intake is **new to us**, not a proof review. No general priority, dependence, or unpublished-novelty claim is warranted by this check.
- The support labels T01–T20 below are not final note IDs. Each note body is limited to one to four sentences; its metadata gives source words, actual search terms, contextual relation, and relevant state IDs.

## Actual searches and read evidence

### S1 — broad topic and pagination search

Command executed against `context/hua_project/29.modern.tex`:

```sh
rg -n 'tors|minimal|admiss|1959|Nori|Witt|Cartier|abelien|abélien|homotopie|124|125|126|127|128|129|136|137|138|139|140|141|142' context/hua_project/29.modern.tex
```

This located the letter section at lines3178ff, the conjectures/computation section at3322ff, admissibility/minimality at3524ff, and the context-only continuation at3655ff. It also located the notation convention at33–34, the editorial correction list around40, and the comparison with the prime-to-characteristic product assertion at1725–1735.

### S2 — precise subsection, obstruction, and alternate-terminology search

Command executed:

```sh
rg -n 'Vrai|feuilles anciennes|Le dispositif|Le foncteur|pro-représentabilité|suite exacte d.homotopie|variété abélienne|Witt|Le calendrier|groupes admissibles|Minimalité|proposition 4|condition minimale|frobenius|Frobenius|platitude|non.*normal|cusp|cuspid|alpha_p|alpha\_p' context/hua_project/29.modern.tex
```

Relevant hits: `Le dispositif`3194, `Le foncteur, et ce qu'il vérifie`3247, `La pro-représentabilité`3267, `La suite exacte d'homotopie, à trouver`3325, `Le calcul sur une variété abélienne`3357, Witt3381, `Le calendrier`3424, cover quotation3443–3444, `Les groupes admissibles`3527, `Minimalité`3573, `La proposition 4, démontrée deux fois`3600, `La fin de la proposition 4`3658, and condition minimale3685–3687. No cusp/cuspid/alpha_p obstruction was returned by this search; that negative result is a search result, not a novelty claim.

### S3 — RESULTS_STATE status and cross-project identifiers

Command executed:

```sh
rg -n '29-fundamental|N063|N100|E\.11|E\.2|Hua|unreviewed|status|referee|1976|1983|1959' context/notes/RESULTS_STATE.md
```

Read the guidance and orientation at1–24 and the relevant registers at338–376. The relevant references are **LM1 E.11** (open, return's claim), **LM1 E.2** (proved, return's claim), **MPL_11_043-058+56 N063** and **N100** (first-pass leads), and **Hua `29-fundamental-group-scheme-via-torsors`** (claim to check, statement-level intake new to us). Their mathematical scopes are distinguished below rather than forcibly connected.

### Context passages actually read

| Context passage | Hua pagination | Corresponding scans | Use |
|---|---:|---:|---|
| “Lettre à Serre, 18 août 1959 : le groupe fondamental infinitésimal”; “Le dispositif”, “Le foncteur, et ce qu'il vérifie”, “La pro-représentabilité”, “Le dévissage sur un corps parfait” |124–126|125–127| Axioms, provisional hypotheses, rigidity, pointed-torsor functor, context-only pro-object |
| “Ce que la lettre conjecture, et ce qu'elle calcule”; “La suite exacte d'homotopie, à trouver” |127–129, especially128|128–130, especially129| Conjectural status and product consequence |
| “Le calcul sur une variété abélienne” |128–129|129–130| Torsion limit, Cartier duality, Witt speculation and family variation |
| “Ce que c'est, aujourd'hui”; “Le calendrier” |127–129, calendar129|128–130, calendar130| Contextual literature assertions and undated closing continuation |
| “Les « feuilles anciennes » : représentabilité et recollement”; all three subsections |130–134, cover quotation referring backward|131–135; assigned source cover124| Relative pointed-torsor functor, representability criterion, gluing; cover comparison, no date inference |
| “Groupes admissibles, couples minimaux, et la proposition 4”; “Les groupes admissibles” |136–137|137–138| Admissibility, uniqueness question, base-change correction, rigidity |
| “Minimalité” |137–138|138–139| Repaired contracted product and notation normalization |
| “La proposition 4, démontrée deux fois” |138–140|139–141| Supplied unfinished proof versus later categorical restart |
| “Le pro-objet π₁^C(S,ξ)”; “La fin de la proposition 4”, “Le pro-objet” |141–142|142–143| Context-only claimed completion; not independently re-proved here |

## Candidate notes

### T01 — Faint cover subtitle remains a reading question

**Witness:** scan124, cover. **Source words:** “Vrai groupe fondamental”; frozen uncertain subtitle “ensembles|schémas”. **Search:** S1 `124`, S2 `Vrai|feuilles anciennes`. **Context:** Hua, modernised reading of cote29, opening of “Les « feuilles anciennes » : représentabilité et recollement” (Hua pp.130–134), quoting the cover as “[feuilles anciennes]”. **Relation:** differs; unresolved reading question. **State ID:** Hua `29-fundamental-group-scheme-via-torsors` (orientation only).

The cover supplies the label “Vrai groupe fondamental,” but the frozen subtitle remains uncertain. Hua's contextual “[feuilles anciennes]” differs from the audited alternatives and should be recorded as a question, not used to replace the frozen reading or to date the manuscript sheets.

### T02 — The two awkward hypotheses are expressly provisional

**Witness:** scan126, typescript p.2. **Source words:** “ont une sale gueule”; “essentiellement provisoires”. **Search:** S1 `admiss|1959|126`, S2 `Le dispositif`. **Context:** Hua, modernised reading of cote29, “Le dispositif” (Hua pp.124–126, witness p.125). **Relation:** restates and adds drafting status. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The source explicitly marks (v), the infinitesimal/separable decomposition, and (vi), reducedness of S, as provisional assumptions serving the rigidity lemma. This supports Hua's account of a construction with restricted hypotheses and prevents the source from being cited here as an unconditional existence theorem over every base; assumptions (i)–(iv) enter this selected witness only by reference and are supplied in Hua's context from the preceding letter page.

### T03 — The perfect-field splitting is a semidirect product

**Witness:** scan126, opening paragraph. **Source words:** “va opérer”; “seulement un produit semi-direct”. **Search:** S1 `tors|126|124`, read through the opening of `Le dévissage sur un corps parfait`. **Context:** Hua, modernised reading of cote29, “Le dispositif” / “Le dévissage sur un corps parfait” (Hua pp.124–126, source p.125). **Relation:** restates. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The perfect-field remark identifies the reduced subgroup with the separable quotient but immediately retains its action on the infinitesimal part. Any summary as a direct product would lose the source's explicit qualification; the result recorded here is a semidirect decomposition under the stated perfect-field hypothesis.

### T04 — Rigidity is used to pass to an exact functor of isomorphism classes

**Witness:** scan126, lemma and final diagrams. **Source words:** “alors u=v”; “exactitude de F, et du lemme”. **Search:** S1 `tors|124|126`, S2 `Le foncteur|pro-représentabilité`. **Context:** Hua, modernised reading of cote29, “Le foncteur, et ce qu'il vérifie” and “La pro-représentabilité” (Hua pp.124–126, source p.125). **Relation:** restates, with scope qualification. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The page defines Z(G) as the set of isomorphism classes of pointed F(G)-torsors and asserts compatibility with products and equalizers by exactness of F and the rigidity lemma. It supports the torsor-based route in Hua's finding, while the categorical closure and exactness assumptions must remain attached; the later unrestricted category of all admissible S-groups is not automatically interchangeable with this setting. Isomorphism classes can still form a set when objects have automorphisms, so rigidity supports the exactness/descent argument rather than the mere existence of that set; Hua's stronger set-versus-groupoid wording should not be repeated.

### T05 — The homotopy sequence is a conjecture, including its local-group formulation

**Witness:** scan129, first paragraph, typescript p.5. **Source words:** deleted “hypothèse”, inserted “conjecture”; “reliés par une suite exacte”. **Search:** S1 `homotopie|129`, S2 `suite exacte d.homotopie`. **Context:** Hua, modernised reading of cote29, “La suite exacte d'homotopie, à trouver” (Hua pp.127–129, source p.128). **Relation:** restates and adds visible revision. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The revision from “hypothèse” to “conjecture” fixes the status of the proposed sequence relating the relative group object, the local system of fundamental groups on X, and the inverse image of the analogous object on Y. The absence of a base field is explicitly said to make the formulation unclear, and the cancelled continuation about sections and a complete local base should not be promoted into a surviving theorem.

### T06 — The product formula is conditional and concerns the total group scheme

**Witness:** scan129, second paragraph. **Source words:** “Elle impliquerait”; “schémas complets”; “corps alg clos”. **Search:** S1 `homotopie|129`; contextual cross-read lines1725–1735; S2 `suite exacte d.homotopie`. **Context:** Hua, modernised reading of cote29, “La suite exacte d'homotopie, à trouver” (Hua p.128 within pp.127–129), and its comparison with Hua p.62. **Relation:** restates conditional status; differs from any conflation with the other product statement. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The product identity for complete X,Y over an algebraically closed k is introduced as a consequence the conjecture would imply. Hua rightly distinguishes its total group scheme, including infinitesimal structure, from the prime-to-characteristic assertion elsewhere in his reading; this leaf does not provide a proof of the product identity or evidence for the chronology of that comparison.

### T07 — The abelian-variety formula is written explicitly, but the local derivation is conditional

**Witness:** scan129, middle. **Source words:** “Utilisant tes raisonnements”; “On en déduit”; “avec sa partie infinitésimale aussi”. **Search:** S1 `Cartier|abélien|129`, S2 `variété abélienne`. **Context:** Hua, modernised reading of cote29, “Le calcul sur une variété abélienne” (Hua p.128 within pp.127–129). **Relation:** restates formula; adds proof-status qualification. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The source writes Π₁(X/k)=lim←ₙ X[n], gives transition X[mn]→X[n] as multiplication by m, and identifies its Cartier dual with lim→ₙ X*[n]. It connects this to commutativity and minimal torsors being isogenous abelian varieties, but the visible chain follows the conjectural product formula and invokes the correspondent's arguments, so this page supplies an explicit announced computation rather than a self-contained independent proof.

### T08 — The Witt-module paragraph records an expectation, not a specified equivalence

**Witness:** scan129 end and scan130 opening. **Source words:** “Il est hors de doute”; “Cartier doit l'avoir fait”; “devrait ... fournir”. **Search:** S1 `Witt|Cartier|129|130`, S2 `Witt|variété abélienne`. **Context:** Hua, modernised reading of cote29, “Le calcul sur une variété abélienne” (Hua pp.128–129). **Relation:** restates and qualifies. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The proposed functor from infinitesimal commutative proalgebraic groups to Witt modules and its three-part decomposition are expressed as expectations, without a category equivalence, operators, or proof here. Scan130 continues with the anticipated uniform treatment of ℓ≠p and ℓ=p and variation in an abelian scheme, using the finite flat torsion kernels; those are programmatic benefits, not a completed construction on these pages.

### T09 — The timetable does not independently date this continuation

**Witness:** scan130, second paragraph and closing. **Source words:** “Dans trois ans”; “Sauf difficultés imprévues”; “Bien à toi”. **Search:** S1 `1959|Nori|129|130`, S2 `Le calendrier`; S3 `1976|1983|1959`. **Context:** Hua, modernised reading of cote29, “Le calendrier” and the enclosing section “Lettre à Serre, 18 août 1959” (Hua pp.124–129, calendar p.129). **Relation:** restates programme; contextual attribution distinguished. **State IDs:** RESULTS_STATE orientation questions; Hua `29-fundamental-group-scheme-via-torsors`.

The closing continuation gives a relative schedule for the fundamental group, categories, duality/intersection theory, Weil cohomology, and homotopy, but no date or signature on the selected witness. “18 août 1959” and Serre are contextual attributions from Hua's enclosing section, not independently read from scans126/129/130. The parent separately verified publisher metadata for Nori's 1976, 1982, and 1983 publications; that bibliographic verification does not independently date this letter continuation or establish a priority claim.

### T10 — Uniqueness of the infinitesimal kernel need not use reducedness under an explicit étale-quotient hypothesis

**Witness:** scan137, definition and bracketed question. **Source words:** “déterminé de façon unique”; “S réduit ... nécessaire?” **Search:** S1 `admiss|136|137`, S2 `groupes admissibles`. **Context:** Hua, modernised reading of cote29, “Les groupes admissibles” (Hua p.136). **Relation:** restates the question; adds a scoped answer by an independent check. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`; no resolution of LM1 E.11. **CHECK_EVENTS recommendation:** independent re-proof, final ID to be supplied by parent; proof A below.

With two exact sequences having geometrically injective kernels Uᵢ and finite étale quotients Γᵢ over an arbitrary S, each composite U₁→G→Γ₂ lands in the identity section because its inverse image is clopen and contains every geometric point. Thus U₁⊂U₂ and conversely, so uniqueness does not require S reduced under these precise hypotheses; this answers the margin question about uniqueness and does not remove reducedness from the separate rigidity assertion.

### T11 — The base-change direction has already been visibly corrected in the source

**Witness:** scan137, Proposition and margin. **Source words:** “Si G ... est admissible”; “la réciproque ... fidèlement plat”; margin “S′ et S réduits”. **Search:** S1 `admiss|137`, S2 `groupes admissibles|platitude`. **Context:** Hua, modernised reading of cote29, “Les groupes admissibles”, Proposition1 and its footnote (Hua p.136). **Relation:** restates final assertion; differs in description of the revision. **State IDs:** Hua `29-fundamental-group-scheme-via-torsors`; MPL_11_043-058+56 N063 only as a distinct first-pass descent lead.

The frozen reading preserves a cancelled descending statement and an inserted forward base-change statement, followed by faithfully flat descent as the converse. Hua's final mathematical ordering agrees, but his footnote describes the reversed draft as what the page says; the visible insertion and the reduced-base margin are additional source evidence that the note should retain.

### T12 — The torsor hypothesis in rigidity must not disappear

**Witness:** scan138, Proposition3. **Source words:** inserted “princ. sous G|principal sous G”; “admissible sur S ... réduit connexe”. **Search:** S1 `tors|admiss|138`, S2 `groupes admissibles`. **Context:** Hua, modernised reading of cote29, “Les groupes admissibles”, Proposition3 (Hua p.137). **Relation:** contradicts the unqualified contextual generalization, not the source's qualified claim. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`. **CHECK_EVENTS recommendation:** targeted proof check / refuted for the strengthened contextual assertion, final refined ID to be assigned; proof B below.

The source qualifies P as a principal torsor under an admissible group over reduced connected S. Hua's sentence about two sections of an arbitrary reduced connected P drops that hypothesis and is false: for S=Spec k[t], P=𝔸¹_S, the sections 0 and t agree at t=0 but differ globally; the corrected torsor-rigidity statement is separately justified under the finite-étale-quotient hypotheses in proof C.

### T13 — Minimality requires a declared mathematical repair, not a transcription repair

**Witness:** scan138, final definition. **Source words:** “relatif à G”; “×_G G′”. **Search:** S1 `minimal|138`, S2 `Minimalité`. **Context:** Hua, modernised reading of cote29, “Minimalité” and its editorial footnote (Hua p.137). **Relation:** differs literally; supports an explicitly labelled interpretation. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

The frozen definition writes P′ as relative to G and uses P′×_G G′; Hua replaces this by a G′-torsor extended through P′×_{G′}G. That is the mathematically intended reading used in the checks below, together with **proper** admissible subgroup, but these repairs must remain explicit because the source's literal formula and absence of an explicit strictness word are preserved in the transcription.

### T14 — Gothic Z is contextual evidence, not a resolved glyph

**Witness:** scan139, definition and Proposition4. **Source words:** audited alternatives Z⁰|Z¹ in the definition; Z¹ in the proposition source; bare Z in its target. **Search:** S1 `tors|139`; S2 `Le foncteur|Minimalité`; notation convention at lines33–34. **Context:** Hua, modernised reading of cote29, “Minimalité” (Hua pp.137–138) and its global notation convention. **Relation:** differs as notation normalization; reading question only. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

Hua normalizes the old leaves to a gothic Z and identifies their functor with the letter's Z(S,a;G). This is useful as a contextual comparison, but it does not resolve the audited source alternatives or justify changing the source and target superscripts in the frozen transcription.

### T15 — The minimality argument needs an admissible flat reduction

**Witness:** scans139–140, Proposition4 and fibre-product opening. **Source words:** “est injective”; “le produit fibré”. **Search:** S1 `minimal|admiss|139|140`, S2 `proposition 4|platitude`. **Context:** Hua, modernised reading of cote29, “La proposition 4, démontrée deux fois” (Hua pp.138–140, supplied evidence only pp.138–139). **Relation:** adds a precise gap assessment. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`. **CHECK_EVENTS recommendation:** targeted proof check; conditional implication only, with counterexample D below.

To infer u=v from minimality one must show that H=Eq(u,v) is an admissible finite flat subgroup and that R=P×_Q P′ is a pointed H-torsor yielding P by extension of structure group. The supplied face stops before either assertion, and neither follows merely from the existence of a scheme-theoretic fibre product; the counterexample below makes both flatness failures explicit.

### T16 — The supplied attempted proof stops; the contextual restart adds hypotheses

**Witness:** scan140, its sole sentence. **Source words:** “Soit (R,λ) le produit fibré”; terminal comma. **Search:** S1 `139|140|141|142`, S2 `proposition 4|condition minimale`. **Context:** Hua, modernised reading of cote29, “La proposition 4, démontrée deux fois” and “La fin de la proposition 4” (Hua pp.139–142). **Relation:** differs from any assertion of a completed proof on supplied pages; adds boundary and hypothesis distinction. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

Our scan140 is Hua p.139 and ends at the introduction of R; Hua's restart at p.140 and completion at pp.141–142 are context-only scans141–143. His footnote says the restart introduces a category C closed under products, equalizers, and images, so the contextual completion cannot be silently imported into the earlier unrestricted admissible-group formulation or described as a proof visible on this supplied face.

### T17 — Reduced connectedness alone does not make all admissible-group equalizers flat

**Witness:** scans137 and139–140. **Source words:** “réduit connexe”; “S-groupes admissibles”; “le produit fibré”. **Search:** S1 `admiss|minimal|140`, S2 `platitude|non.*normal|cusp|cuspid|alpha_p|alpha\_p`. **Context:** Hua, modernised reading of cote29, “Les groupes admissibles” and “La proposition 4, démontrée deux fois” (Hua pp.136–140). **Relation:** adds a targeted obstruction to the unrestricted reading. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`. **CHECK_EVENTS recommendation:** targeted proof check / refuted for the closure assertion; proof D1 below.

Over S=Spec k[t] in characteristic p, G=G′=α_p,S is admissible, while the equalizer of 0 and multiplication by t has coordinate algebra k[t,T]/(T^p,tT). Its generic fibre has length1 and its fibre at t=0 has length p, so it is not flat; closure under equalizers is a substantive extra condition even over a reduced connected regular base.

### T18 — A cusp gives a minimal pointed torsor for which the broad injectivity claim fails

**Witness:** scans138–140. **Source words:** “minimal”; “est injective”; “le produit fibré”. **Search:** S1 `minimal|admiss|139|140`, S2 `platitude|non.*normal|cusp|cuspid|alpha_p|alpha\_p`. **Context:** Hua, modernised reading of cote29, “Minimalité” and “La proposition 4, démontrée deux fois” (Hua pp.137–140). **Relation:** contradicts the broad all-admissible-S-group formulation under the explicit intended minimality repair; no contradiction to the restricted letter category is claimed. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`. **CHECK_EVENTS recommendation:** independent re-proof / refuted for a refined broad claim ID; proof D2 below.

Let A=k[x,y]/(y^p−x^(p+1)) for an algebraically closed field k of characteristic p, take the cusp point a:Spec k→Spec A, and point the α_p-torsor z^p=x by z=0. It is nontrivial and minimal among finite flat subgroup reductions, but the distinct endomorphisms 0 and [x] both push it to a pointed-trivial torsor because x^p·x=y^p; the resulting R is the nonflat normalization Spec k[z]→Spec A. This refutes the unrestricted intended assertion, while [x] is a variable S-group morphism and therefore is not a morphism of constant k-groups in the letter's example; the proposed equalizer-closed categorical restart also excludes the nonflat equalizer used here.

### T19 — The contextual literature identification is not a new priority result

**Witness:** scans126 and129–130. **Source words:** “Z(S,a;G)”; “On en déduit”; “Bien à toi”. **Search:** S1 `Nori|1959|Cartier`, S3 `29-fundamental|1976|1983|1959`. **Context:** Hua, modernised reading of cote29, “Ce que c'est, aujourd'hui” (Hua pp.127–129), and Hua findings register `29-fundamental-group-scheme-via-torsors`. **Relation:** restates contextual identification; limits unsupported chronology. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

These witnesses support the pointed-torsor method, explicit infinitesimal part, and stated abelian-variety formula recorded in Hua's finding. His literature identification and date attribution remain credited context, while the source-dependent hypotheses, conjectural step, and unfinished unrestricted proof prevent an unqualified priority or full-generality claim from this package.

### T20 — Relation to the registered group-scheme work is limited and precise

**Witness:** scans126,137–140. **Source words:** “finis et plats”; “S réduit”; “S-groupes admissibles”. **Search:** S3 `E\.11|E\.2|N063|N100`, S1 `admiss|tors`. **Context:** Hua, modernised reading of cote29, “Le dispositif” (Hua pp.124–126) and “Les groupes admissibles” (Hua pp.136–137). **Relation:** adds a scope distinction, no claimed settlement. **State IDs:** LM1 E.11; LM1 E.2; MPL_11_043-058+56 N063 and N100; Hua `29-fundamental-group-scheme-via-torsors`.

The finite admissible-group and pointed-torsor arguments do not settle LM1 E.11's general separated locally finitely presented group-scheme question or re-prove LM1 E.2's characteristic-zero linear exponential assertion. The positive-characteristic cusp check addresses the local minimality claim alone; N063's cancelled descent/rank discussion and N100's Weyl-subquotient test remain separate first-pass leads, with no direct mathematical implication established by these leaves.

## Independent mathematical checks and exact hypotheses

These are new checks performed in this run, distinct from reading or repeating Hua. The parent independently rechecked the cusp construction in a message and requested the proof below; that is a separate review event if the parent chooses to log it. No final statement IDs or CHECK_EVENTS rows are assigned in this support file.

### A. Uniqueness of the infinitesimal kernel without reducedness

**Statement checked.** Let S be any scheme and let G be an S-group scheme with exact sequences of fppf sheaves

`1 → U_i → G → Γ_i → 1`, for i=1,2,

where Γ_i is a finite étale S-group scheme and U_i→S is geometrically injective. The unit section is present because U_i is an S-group scheme. Then the subgroup schemes U_1 and U_2 are equal. Reducedness or connectedness of S is not required for this uniqueness statement.

**Proof.** The identity section e_2:S→Γ_2 is open and closed: it is an open immersion as a section of an étale morphism and is closed because Γ_2→S is separated. Pull it back under U_1→G→Γ_2. The result V⊂U_1 is an open-and-closed subscheme. Every geometric fibre of U_1→S has precisely one geometric point, because geometric injectivity gives at most one and the unit gives at least one; its image in Γ_2 is therefore the identity point. Thus V contains every topological point of U_1. An open subscheme containing every point equals the whole scheme, including its nilpotent structure, so the composite factors through e_2 and U_1⊂ker(G→Γ_2)=U_2. Reverse the indices to get equality.

**Scope limit.** “Finite, flat, separable” in the historical definition must be interpreted as finite étale for this check. This proof does not remove reducedness from the rigidity theorem and does not establish that every closed subgroup or equalizer is flat.

**Proposed log.** Type `independent re-proof`; outcome `proved under finite étale quotient and geometrically injective kernel hypotheses; reducedness unused`. Use a refined statement ID tied to T10.

### B. Counterexample to the context's unqualified two-sections assertion

**Strengthened assertion checked.** Two sections of a reduced connected S-scheme P agreeing over one point must coincide, without a torsor/admissibility hypothesis.

**Counterexample.** Take any field k, S=Spec k[t], and P=Spec k[t,z]=𝔸¹_S. Both schemes are reduced and connected. The sections z=0 and z=t agree over the point t=0 but differ since t is nonzero in k[t]. Therefore the strengthened statement is false. The source's inserted principal-torsor and admissibility qualifications are essential; this counterexample does not refute them.

**Proposed log.** Type `targeted proof check`, outcome `refuted for the unqualified contextual statement; source torsor hypothesis restores the intended scope`. Use a refined statement ID tied to T12.

### C. A precise version of the source's pointed-torsor rigidity

**Statement checked.** Let S be reduced and connected. Let G be a finite locally free S-group scheme in an exact fppf sequence `1→U→G→Γ→1` with U geometrically injective and Γ finite étale. For a G-torsor P, two global sections s_1,s_2 that agree over one geometric point a of S coincide. Consequently a pointed G-torsor has no nonidentity G-equivariant automorphism, provided inner twisting preserves this admissibility class, as it does by fpqc descent for these hypotheses.

**Proof for sections.** Use s_1 to trivialize P; s_2 then corresponds to g∈G(S), equal to the identity at a. Its image γ∈Γ(S) equals the identity on an open-and-closed subset of S, namely the equalizer of the two sections of the finite étale scheme Γ. This subset is nonempty, hence all of connected S, so g is a section of U. For every geometric point of S, the section g and the identity of U coincide because U has one geometric point per fibre. Their equalizer is a closed subscheme of S, since U→S is separated; its defining ideal vanishes at every point and is therefore zero because S is reduced. Hence g=e.

**Automorphisms.** The group scheme Ad(P) of G-equivariant automorphisms of P is an inner form of G and locally is G on a faithfully flat trivializing cover. Admissibility descends because its infinitesimal kernel is unique by A, and finiteness, local freeness, geometric injectivity, and finite étaleness descend. An automorphism fixing the chosen geometric point gives a section of Ad(P) equal to the identity there, to which the preceding argument applies.

**Scope limit.** This check deliberately uses finite locally free groups and a finite étale quotient; it is not a proof for an arbitrary reduced connected P, nor for nonreduced S. No claim about the equalizer of two group morphisms is included.

**Proposed log.** Type `independent re-proof`, outcome `proved with reduced connected S and finite locally free admissible torsor hypotheses`. Use a refined statement ID associated with T04/T12.

### D1. Flatness fails for an equalizer even over a regular base

Let k be any field of characteristic p>0, S=Spec k[t], and G=G′=α_p,S=Spec k[t,T]/(T^p). Both are admissible: U=G is finite locally free of rank p and geometrically injective, and Γ=1 is finite étale. Multiplication by t defines an S-group endomorphism since T↦tT respects the additive comultiplication and T^p=0. The equalizer of zero and [t] is

`H = Spec k[t,T]/(T^p,tT)`.

After inverting t its coordinate algebra is k(t), so the generic fibre has length1. At t=0 it is k[T]/(T^p), length p. Equivalently the nonzero element T is killed by the nonzerodivisor t. Thus H is finite but not flat over S, so the class of all admissible finite flat S-groups is not closed under such equalizers.

This example diagnoses the missing categorical property; it alone does not refute injectivity for minimal torsors because no such torsor was specified.

**Proposed log.** Type `targeted proof check`, outcome `refuted: admissibility plus reduced connected base does not imply equalizer flatness`. Use the refined T17 ID.

### D2. Full counterexample to the broad minimality-injectivity statement

#### Exact claim and interpretation tested

Test the following precise broad statement: for every reduced connected S, every admissible finite locally free S-group G, every geometrically pointed G-torsor (P,ξ) minimal with respect to **proper admissible finite flat closed subgroup reductions**, and every admissible G′, the map

`Hom_S-gp(G,G′) → {pointed G′-torsor isomorphism classes}, u ↦ u_*[P,ξ]`

is injective.

This uses the intended mathematical repair of scan138: a reduction is a pointed G₀-torsor P₀ for a proper admissible subgroup G₀⊊G with P≅P₀×^{G₀}G. It does **not** pretend that the source's literal exchanged contracted-product indices already express this definition.

#### Base, point, group, and torsor

Let k be any algebraically closed field of characteristic p>0. Set

`A = k[t^p,t^(p+1)] ≅ k[x,y]/(y^p−x^(p+1))`,

where x=t^p and y=t^(p+1), and A is a subring of its normalization k[t]. The subring description shows A is an integral domain, so S=Spec A is reduced and connected. Let a:Spec k→S be the cusp point defined by x↦0,y↦0. It is a geometric basepoint because k is algebraically closed. The algebraic example also works over an arbitrary characteristic-p field after choosing a geometric point above its rational cusp, but that extension is unnecessary for this check.

Take `G=G′=α_p,S=Spec A[T]/(T^p)`. It is finite free of rank p over A, every geometric fibre has one point, and it is admissible with U=G and Γ=1. Define

`P = Spec B`, `B=A[z]/(z^p−x)`,

with α_p action z↦z+T and chosen ξ:Spec k→P given by x=y=z=0 above a. B is free over A on 1,z,…,z^(p−1). On P×_S P, T=z_2−z_1 satisfies T^p=0, giving the usual isomorphism P×G≅P×_S P; hence P is an fppf G-torsor.

#### Nontriviality

A trivial G-torsor has a global section. A section of P would be b∈A with b^p=x=t^p in the fraction field k(t). Frobenius is injective in this field, so b=t. But t∉k[t^p,t^(p+1)]: the monomials in A have exponents in the semigroup generated by p and p+1, which does not contain1. Hence P is nontrivial.

#### Minimality for the intended finite-flat subgroup definition

Let H⊂G be an admissible finite flat closed subgroup. Since A is noetherian, H is finite locally free, with constant rank on the connected scheme S. Over K=Frac A=k(t), the only closed subgroup schemes of α_p,K have ranks1 or p: their defining ideals in K[T]/(T^p) are (T^d), and the Hopf-ideal condition forces all intermediate binomial coefficients of d to vanish modulo p, which for 1≤d≤p gives d=1 or d=p. Thus H has rank1 or p over S.

If rank p, the coordinate surjection A[T]/(T^p)→O(H) is a surjection between locally free A-modules of equal rank, hence an isomorphism locally and therefore globally; H=G. If rank1, the unit section makes H the trivial group. A reduction of P to the trivial group would trivialize P, which is impossible. Consequently (P,ξ) is minimal for the repaired definition.

#### Two distinct endomorphisms with the same pointed pushforward

Let u=0 and v=[x] be multiplication by x on α_p,S. These are distinct: on coordinates their pullbacks send T to0 and xT respectively, and xT≠0 in the free A-module A[T]/(T^p).

Pushforward of the additive torsor z^p=f through [c] has equation w^p=c^p f, with equivariant map w=c z. Here u_*P is the trivial α_p-torsor, and

`v_*P : w^p = x^p·x = x^(p+1) = y^p`.

The coordinate w−y satisfies (w−y)^p=0, so translation by −y gives a G′-equivariant trivialization. At a, x=y=z=0, so the pushforward point has w=0 and this translation takes it to the identity. Both pushforwards are therefore **pointedly** isomorphic to the same trivial G′-torsor, although u≠v.

#### The two missing flatness assertions fail exactly in the proposed diagram

Under the pointed trivializations just chosen, Q=u_*P×v_*P is the trivial G′×G′-torsor, the map P→Q is `z ↦ (0,xz−y)`, and P′=G′ maps diagonally into Q. The fibre product is therefore

`R = Spec A[z]/(z^p−x,xz−y)`.

Substituting x=z^p and y=z^(p+1) identifies this ring with k[z]. Thus R→S is precisely the finite normalization of the cusp. Its generic fibre has length1; its fibre at a is k[z]/(z^p,z^(p+1))=k[z]/(z^p), length p. It is not flat. The equalizer subgroup is

`H = ker[x] = Spec A[T]/(T^p,xT)`,

whose generic fibre has length1 and fibre at a length p, so H is not flat or admissible. R contains the distinguished point z=0 and surjects on underlying points; neither fact makes it a faithfully flat torsor. Flatness is exactly what fails and is exactly what minimality needs.

#### Scope of the refutation

This counterexample refutes the broad all-admissible-S-group version of Proposition4 with the intended minimality definition. It does not refute the earlier letter's example in which objects and morphisms come from finite k-group schemes via an exact base-change functor F: [x] is an S-dependent morphism and does not come from a k-group morphism. Nor does it show that Hua's later, context-only proof in an equalizer-closed category is wrong; that closure condition excludes this nonflat kernel, and the later proof itself has not been independently verified here.

The example is an independently checked construction in this run, not a claim that the literature has never recorded it. S2 found no cusp/alpha_p discussion in the supplied modern context; no broader literature search was performed.

**Proposed log.** Type `independent re-proof` or `targeted proof check`; outcome `refuted: broad minimality-injectivity statement for all admissible finite locally free S-groups over reduced connected S; cusp example, variable S-group endomorphisms`. The parent may separately log `used and rechecked in this run` for its independent review. Use the refined T18 statement ID and keep it distinct from any entry for the letter's exact-category claim.

## What has not been checked

- No image, handwriting, diagram placement, or glyph was re-audited; all source words above come from frozen transcription.
- No independently verified date or correspondent has been recovered from the selected letter continuations.
- This support agent did not perform a literature or priority check; the parent separately verified Nori's publisher metadata and read a primary-source discussion of the finite-field-group versus relative-group-scheme flatness distinction. No general priority claim follows, and the Cartier, Witt, and Gasbarri references remain unchecked by this support agent.
- The full categorical pro-representability assertion and the context-only proof on Hua pp.140–142 were read but not independently re-proved.
- The abelian-variety formula, Cartier-dual formula, and proposed Witt-module decomposition were not independently established in this run.
- LM1 E.11 and LM1 E.2 retain their recorded scopes and statuses; none of the above changes their register status.

## Additional modern-context coverage requested by parent

After writing the core support, read all of lines3706–4102 and4295–4386 of `context/hua_project/29.modern.tex` in four contiguous chunks:3706–3835,3836–3970,3971–4102,4295–4386. The parent reported it had separately read4103–4294; that middle range is **not** claimed as my own reading here. Together these readings cover the requested3706–4386 interval. No source image or additional frozen page was opened during this extension.

Also completed the previously partial contexts at3300–3321 (“Le dévissage sur un corps parfait”) and3441–3523 (all of “Les « feuilles anciennes » : représentabilité et recollement”). My own context reading is therefore continuous from3178 through4102, plus4295–4386, with the earlier isolated notation/product-comparison passages listed above. The latter representability section concerns proper flat X/S with a section, universal f_*O_X=O_S, and finite étale G, followed by a local-noetherian representability criterion and an unfinished gluing argument; these add relative moduli context but are not used as a proof of unrestricted admissible-group minimality.

### S4 — actual additional-context search

```sh
rg -n 'Données de descente|Compléments aux notes IHES|topos des|morphisme fini étale de rang|Catégorie galoisienne|Groupe fondamental dans les catégories|cinq classes|Notre intérêt|Un plan en sept|groupe abstrait fini|condition de cocycle' context/hua_project/29.modern.tex
```

Relevant hit positions: cocycles3707, relative product3742, π-sets3807, finite étale quotient3839, Galois-category axioms3956, abstract descent categories4064, constant structural groups4087, five classes4296, infinite-group interest4334, plan4358. These are coverage and source-link observations only, not independent checks of their theorems, and require no mathematical CHECK_EVENTS entry.

| Context actually read | Hua pages → corresponding scans | Link to the assigned frozen source | Relation and safe use |
|---|---|---|---|
| “Données de descente : la relation de cocycle” |144–146 →145–147| Scan137 “théorème de la descente et unicité” | Adds a later contextual formulation of descent data by a cocycle rectangle and a cancelled path version. It supplies a formal parallel, not a proof that the U or torsor descent invoked on scan137 is effective. |
| “« Compléments aux notes IHES » : le π₁ d'un produit fibré”; “L'énoncé”, “La démonstration” |148–150 →149–151| Scan129 “Elle impliquerait” and its total-group product conjecture | Adds a separate relative fibre-product comparison for ordinary fundamental groups, with proper/separable hypotheses and an additional étale-base-change/section condition for bijectivity as stated by Hua. It must not be substituted for the total infinitesimal group-scheme conjecture on scan129. |
| “Le topos des π-ensembles” |151 →152| Scan126 “catégorie des ensembles”; pointed-torsor functor | Adds a distinct contextual classifying-topos/group-cohomology discussion. It is not the same representability problem as the finite group-scheme pointed-torsor functor, and no new source note is needed solely from this parallel. |
| “Un morphisme fini étale de rang n est un P/H”; “La proposition3.2”, “La démonstration de Serre”, “La proposition3.1 : l'existence de X/G” |152–156 →153–157| Scans126/138 sections and components; scan129 “revêtement principal minimal” | Adds a finite étale quotient construction using the symmetric-group torsor of ordered fibres. Its finite étale scope is narrower than the admissible finite-flat infinitesimal torsor setting, so it does not fill the missing flatness of H or R in scans139–140. |
| “« Catégorie galoisienne » : Gal1 à Gal6”; all four subsections |157–158 →158–159| Scan126 products/equalizers and scan138 section-component rigidity | Adds a formal analogy: the contextual Gal3 singles out sections as components, and quotient/exactness properties are axioms of a selected category. No assertion of the relative dating of the two draft axiom systems is independently established here. |
| “« Groupe fondamental dans les catégories »” |159–160 →160–161| Scan126 exact F and its selected structural groups; scan137 descent | Adds explicit restrictions on a class D of descent morphisms and uses structural groups X×G with G an abstract finite group. This reinforces the need to name the allowed structural groups and morphisms; it does not identify this category with all admissible S-group schemes. |
| “Les cinq classes de recouvrements”; “Pourquoi cela n'a d'intérêt que pour G infini”, “Les comparaisons” |170–171 →171–172| Scan126 “finis et plats”, scan129 “partie infinitésimale” | Adds a sharp type distinction: here G is a discrete abstract group and finite G gives étale principal coverings; it is not the category of arbitrary finite group schemes that includes α_p. Thus the contextual coincidence of the five classes for finite discrete G supplies no shortcut for the infinitesimal equalizer issue. |
| “Un plan en sept sections” |173 →174| Scan129 homotopy expectations; scan130 schedule | Adds another contextual programme of base-change statements and connectivity notions. Its asserted unexecuted status supplies no dating or completion evidence for the selected letter's timetable. |

### Optional short note from the additional coverage

**Witness:** scans126 and129. **Source words:** “finis et plats”; “avec sa partie infinitésimale aussi”. **Search:** S4 `cinq classes|Notre intérêt|groupe abstrait fini`. **Context:** Hua, modernised reading of cote29, “Les cinq classes de recouvrements” / “Pourquoi cela n'a d'intérêt que pour G infini” (Hua pp.170–171), and “Groupe fondamental dans les catégories” (Hua pp.159–160). **Relation:** adds a distinction between categories; not an independent theorem. **State ID:** Hua `29-fundamental-group-scheme-via-torsors`.

In the later contextual five-class comparison, “finite G” means a finite discrete abstract group, whose torsors are finite étale, while scans126/129 deliberately retain finite flat group schemes with infinitesimal structure. The statements therefore address different allowed structural groups, and neither that comparison nor the constant-group descent framework can be used to erase the flatness issue in the all-admissible-S-group version of Proposition4.
