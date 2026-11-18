# Research notes: MPL_93_092–134

## Scope, evidence, and separation from the transcription

These notes concern **cote 93, scans 092–134, excluding the omitted blank scan 125: 42 sheets**. The diplomatic transcription was completed in one stream by the primary reader, followed by a second visual reading of every sheet and a reconciliation of recurring notation. No OCR was used. The transcription was frozen at **2026-11-18 01:07:16 UTC**, before the context ZIP was opened at **01:07:29 UTC**; its combined SHA-256 is **79288e81270a4e71be4892a79a77abb437d41510064a8f5699572b07496b9dc9**. Mathematical repairs and alternative readings below belong to these notes alone.

The principal result of the comparison is a more precise account of what this sequence establishes and what it leaves open. It develops projective connections, their Riccati and Schwarzian descriptions, an integral divided-derivative invariant, and the connection associated with analytic uniformization. It does **not**, on these 42 sheets, identify a particular uniformizing equation as a Gauss–Manin connection or calculate its p-curvature. The small-characteristic argument is substantial, but its determinant normalization and the transition from a local calculation to arbitrary base rings require separate attention. The post-freeze research adds one concrete external bridge in F09–F10: the Legendre period equation realizes the three-puncture coefficient, with a theorem-based nilpotence consequence for that identified family.

All scan references below are the supplied PDF scan numbers. References to Hua's pages use the convention **Hua page n = supplied scan n+1**. Thus Hua's pages 120–123 are scans 121–124. Archive foliation is not treated as Grothendieck's own pagination.

### Context and credit

The supplied **README.md**, **notes/RESULTS_STATE.md**, **same_cote_93/MPL_93_002-046_notes.md**, and **hua_project/93.modern.tex** were consulted only after the freeze. The README's early “Only this README” statement is superseded by its additions of 17 November; the earlier package and Hua material were in fact present. The results register explicitly says that no settled result of the user's runs directly covers this folder; its relevant leads are **MPL_93_002-046 P01–P09**, related earlier Cartier/crystalline notes where specified, and **Hua, findings register, 93-integral-schwarzian-level-p2**. Unrelated headline results about GT, the section conjecture, and finite homotopy models are not assigned a connection merely because a crossed-out moduli-space diagram occurs on scan 101.

**Hua, modernised reading of cote 93**, is Michel Hua's project's AI-produced interpretation, not a diplomatic transcription and not a result of this run. Its full file was read within the research team; the primary reader also compared its relevant sections VII–X directly with the frozen text. When we use, refine, or disagree with that reading, the note says so. Its references to computations or Lean verification are reports by that project: no external proof artifact was supplied here, and none is described below as independently executed.

For compactness, the following source labels have fixed meanings:

| Label | Exact supplied source and location |
|---|---|
| H-VIIa | Hua, modernised reading of cote 93, VII, “1.4. Connexions, et la condition de transversalité,” pp. 88–94; scans 089–095 |
| H-VIIb | Same, VII, “1.5 et 1.6. Sections horizontales,” pp. 95–100; scans 096–101 |
| H-VIIIa | Same, VIII, “La formule de transformation,” pp. 101–107; scans 102–108 |
| H-VIIIb | Same, VIII, “Le dictionnaire,” pp. 107–114; scans 108–115 |
| H-IX | Same, IX, “Mise au net : le cocycle schwarzien,” pp. 115–123; scans 116–124 |
| H-IXp | Same, IX, “L'injectivité en caractéristique p,” pp. 121–123; scans 122–124 |
| H-Xa | Same, X, “Domaines homogènes et revêtement universel,” pp. 125–129; scans 126–130 |
| H-Xb | Same, X, “Le torseur des connexions projectives, et les singularités régulières,” pp. 130–137; scans 131–138, of which only 131–134 are supplied scans |
| Pnn | same_cote_93/MPL_93_002-046_notes.md, item Pnn, generally its scan 036 unless otherwise specified; first-pass, unreviewed leads |
| S20 | README.md, planning guess about Gauss–Manin, Cartier, projective connections, uniformization, p-curvature, and cotes 159 and 64 |
| H-FIND | notes/RESULTS_STATE.md, “Findings of another project,” id 93-integral-schwarzian-level-p2; candidate finding, not an established priority claim |

Each numbered note has a context query. These were actually run against all supplied textual context files; **documentation/context_searches.tsv** records the patterns, matching files, line numbers, and hit counts. A query match is evidence of topical overlap, not evidence that a claim is true. **CHECK_EVENTS.tsv** records the kind of check actually performed, including background carried without a new proof, textual comparisons, computations, and counterexamples. The model was GPT-6 Astra Pro; the runtime did not expose the numerical effort setting, so the log says so rather than inventing it.

### Conventions used only in the notes

On a characteristic-zero coordinate chart with \(s'\ne0\), write
\[
G_t(s)=-2\,\frac{s'''}{s'}+3\left(\frac{s''}{s'}\right)^2=-2S_t(s).
\]
This is the manuscript's later normalization, not a correction inserted into its earlier calculations. Write \(\omega=\Omega^1_{X/S}\), and use \(D_t(f\,dt)=f'\,dt^2\) for the coordinate connection on \(\omega\). In characteristic p, divided derivatives \(D^{(i)}\) must be specified separately; \(G_0=G/12\) is an equality after inverting 12, not an instruction to divide by 12 in characteristics 2 or 3.

## Typed sheets, titles, and page counts

**There are no typescript sheets or printed offprints among the 42 supplied sheets.** Every inventory sheet_kind is **text**: handwritten notes on the subject of this sequence. There are no reused_typed or typed sheets, no cover, and no wholly cancelled draft sheet; local deletions are recorded individually. This conclusion concerns these scans, not all of cote 93, whose catalogue title and earlier package do describe other kinds of material.

There is **no title sheet and no explicit total page count** such as “19 pages” or “Pages 1–67” in this set. The following own-page numbers and internal headings are visible; they are not rearranged into a reconstructed authorial order.

| Scan | Own numbering or internal heading | Qualification |
|---|---|---|
| 096 | “1.5. Sections horizontales de P” | Internal subsection, not a title sheet |
| 097 | “1.6.” | Begins the intrinsic differential-operator description |
| 101 | 1 | Own sheet number |
| 102 | 5 | Own sheet number; kept in scan order |
| 103 | 2 | Own sheet number |
| 104 | 2 bis | Very short continuation, fully included |
| 105 | 3 | Own sheet number |
| 106 | 9 \| 4 | Frozen reading remains doubtful; the sequence and Hua favor 4, but do not change the ink-based record |
| 119 | “Extension à la géom. alg.” | Internal heading, not a title sheet |
| 124 | “Cas car. 2 ou 3” | Internal heading, not a title sheet |
| 126 | “Th. (classique)” followed by 1 | Internal theorem enumeration |
| 128 | “Théorème 2” | Internal theorem enumeration |

Archive foliation, where recorded, appears only in TeX comments. Scan 125 is absent because the supplied task identifies it as blank; it is not a missing transcribed page.

## Steps the manuscript itself marks as unverified

This register separates genuine open questions, checks completed later in the sequence, and doubtful marginal wording. A question mark is retained even where the present notes supply a calculation.

| Scan(s) | Brief words or sign on the page | What is at issue; later disposition |
|---|---|---|
| 093 | \(\gamma_0=?\); “On va déterminer” | Principal symbol; the following calculation gives the identity, A02 |
| 095 | “Faire le lien” | Connection and infinitesimal/formal neighborhood descriptions; revisited 109 and 133–134, A04 |
| 095 | Doubtful margin beginning “cela a l'air…” | Exact wording remains low confidence; no mathematical objection is inferred from it, A03 |
| 096 | “Pour quelles connexions… ?” | Horizontal sections; a local/split criterion follows, A05 |
| 097 | “Quelles connexions…”; “Sauf erreur”; “sauf erreur de calcul”; “facteur 2 !” | Riccati normalization; corrected in 105–107 and 114, A06 |
| 099 | “doit être déterminée !”; “élts de contact can. d'ordre 1 à trouver” | Polar principal part and intrinsic contact element; A10 and A15 |
| 101 | “Quels sont les autom… ??”; “de la forme… ?”; question marks beside components | Automorphisms and the horizontal-section equation; distinct questions, A11–A12 and B12 |
| 103 | Margin read doubtfully as “facteur 2 qui manque avant ce calcul ?” | Same normalization issue, A06 |
| 105 | “Et vérifions” followed by “OK” | Compatibility of successive shifts; final identity checked, B03 |
| 110 | Deleted, very doubtful “Quid…” | Wording remains uncertain; no specific conjecture inferred, B19 |
| 111 | “Quelle est l'interprétation…”; “Quelles sont les sections…” | The quotient-torsor dictionary; continued 112–114, B08–B10 |
| 112 | “Condition d'horizontalité ?”; “quel est le faisceau…” | Horizontal trivializations and developing coordinates; answered locally on the page, B10 |
| 113 | Isolated marginal “?” | Near the description by nonvanishing horizontal one-forms; exact attachment remains uncertain, B10 |
| 114–115 | “Pb”; “Est-elle algébrique ?” | Uniformizing projective connection, especially on nonproper curves; B15 and B17–B18, with E12's section qualification |
| 115 | “Sont-elles algébriques ?”; question about independence of the topology of \(\mathbb C\) | Families and a purely algebraic interpretation, B16 and F06 |
| 116–117 | “se vérifie facilement”; “on prouve aisément une réciproque” | Invariance and the local ODE converse; claims rather than explicit doubt, C01–C02 |
| 119 | “on vérifie bien sûr…” | Extension of the Schwarzian identities to algebraic coordinates; C04–C05 |
| 120 | “que le lecteur (bis) énoncera” | Relative formulation left to the reader; C06 |
| 121 | “lisse/S ??”; “à vérifier !” | Relative/global constants and the kernel statement, C07 |
| 121 | “Cf plus bas !” beside the doubtful \(p>3\) qualification | Small-characteristic Frobenius refinement, D04–D05 |
| 122 | “On peut espérer”; deleted words read as “Non vérifiée” | The characteristic-p injectivity proposition, D04–D09 |
| 123 | “À prouver…” and the reduction to \(\alpha=0\) | Local coefficient argument and base change; D06–D10 |
| 124 | Deleted branch, then “On gagne encore !” | Revised characteristic-3 proof; D07–D08 |
| 128 | “cf. explication plus bas” | Some hypotheses/germ details are postponed; E06 |
| 130 | “prouver (ou l'infirmer !)” and “oui elle est algébrique cf plus bas” | Affine-connection algebraicity checked in E09–E10; distinction from the covering map in E11 |
| 131 | Programme to establish uniqueness and “préciser” the problem | What algebraization is actually sought, E12 |
| 132 | “comment reconstituer… ?” | Recovering the analytic open and covering from the algebraic marked data, E14 |
| 132 | “description purement algébrique” of \(\sigma'\), and of \(p_X\) when \(X\simeq\mathbb A^1\) | The horizontal omitted section \(\sigma'\) is distinct from the transverse \(\sigma\); E19–E20 |

No conjecture is inferred merely from every question-like stroke in a difficult diagram. Low-confidence readings and deleted words remain marked in the transcription and doubts table; the register is not a replacement for those records.

## A. Transverse connections, principal parts, and horizontal sections
