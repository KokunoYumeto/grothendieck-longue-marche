# Research memo: fuseaux and the generisation cube, scans 153–154

Recorded: 2026-11-15 02:04:51 UTC

## Scope and conclusion

This memo evaluates the supplied extract of **Hua, findings register, 154-generisation-cube**, against the frozen transcription of cote 154, scans 153–154. The comparison object is precisely the truncated extract in context/notes/RESULTS_STATE.md, line 122; no verdict about unprovided portions of the external register is made. The root reported transcription freeze at 2026-11-15 01:44:43 UTC and context opening at 01:44:50 UTC. The context README and the entire RESULTS_STATE were read before writing these research records. No manuscript image was accessed, and no page or combined transcription was edited.

**Finding:** scan 154 explicitly asserts a cube correspondence, but its scope, the meaning of its parameter \(\nu\), and several identifications in Hua's extract require qualifications. A precise standard local model does give \(2^\nu\) generic resolutions and \(\nu 2^{\nu-1}\) states retaining one marked contact. For nearby straight lines in a **fixed realization** of the background arrangement, the corresponding count is \(2\nu\). These are conditional local calculations, not a proof of the manuscript's full classification, its claimed canonicity, or a global theorem about all relative positions.

Every candidate below has a prior, timestamped search in research_cube_searches.md. “No hit” means absence under the recorded searches of the four supplied context files, not novelty or absence from the wider archive or literature. No existing results-register status is changed.

## Ten short candidate notes

Ledger aliases: CUBE-01→C01, CUBE-02→C02, CUBE-03→C03, CUBE-04→C04, CUBE-05→C05, CUBE-06→C06, CUBE-07→C07, CUBE-08→C08, CUBE-09→C09, CUBE-10→C10. The original search IDs and timestamps remain authoritative in research_cube_searches.md.

### C01 — What the frozen page actually supports

**Kind:** manuscript assertion / qualification of another project’s claim.

**Source:** cote 154, scan 154, lines 31–44 and 75–78.

**Short quote:** “position relative non principale”.

**Context matches/status and relation:** CUBE-01→C01: Hua, findings register, `154-generisation-cube`, supplied in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched); Lean statement without verdict] is the relevant register hit. The other cube-word hits in `context/Esquisse_cote119_copy1_API_transcription.tex:921,1369` [API transcription not checked by eye] do not establish this particular assertion; relation: qualifies the extract without changing its status.

Scan 154 begins with a nonprincipal relative position and explicitly associates its stable generisations with cube vertices and its semistable generisations with edges, with specialization giving incidence. The readings of canonical and of the edge word, as well as the recorded vertex exponent, retain uncertainty marks, while \(\nu2^{\nu-1}\) is a clear edge-count display in the frozen text. Thus the core cube assertion is supported, but the supplied Hua extract is more definite about the parameter, the one-vertex interpretation, and the straight-line contrast than these two pages alone justify. Confidence: high for locating the asserted correspondence, but limited for a stronger reading because the frozen uncertainty marks and missing definitions remain.

### C02 — A conditional local construction of the cube vertices

**Kind:** own idea / conditional mathematical verification; no novelty claim.

**Source:** cote 154, scan 154, line 44.

**Short quote:** “sommets d'un cube”.

**Context matches/status and relation:** CUBE-02→C02: Hua, `154-generisation-cube`, in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched)] and the supplied Esquisse, marker 119/50, manuscript page 48, `context/Esquisse_cote119_copy1_API_transcription.tex:2212–2223` [API transcription not checked by eye; corresponding published §8 passage checked] are relevant hits. README rank 18 [planning lead] supplies subject context; relation: adds a conditional local proof, not a proof of the full register claim.

Assume a finite tame projective pseudoline arrangement, an additional pseudoline meeting every old pseudoline once transversely, and small pairwise disjoint conical disks around its \(\nu\) marked projective vertex contacts, each meeting only the background branches incident there. With the curve fixed outside those disks, fixed opposite endpoint sectors, and each incident old branch crossed exactly once, there are two local detours at each contact, including multiple concurrences. Independent disk surgeries therefore give exactly \(2^\nu\) local generic classes under isotopy through generic curves retaining those conditions and avoiding all marked contacts throughout. Confidence: high under the listed local hypotheses, because the two-route sector argument and disjoint-support construction are proved in `records/research_cube_memo.md`, §2.

### C03 — Why the straight-line comparison is \(2\nu\)

**Kind:** own idea / conditional fixed-realization calculation.

**Source:** cote 154, scan 154, lines 75–78; supplied Hua extract.

**Short quote:** “2ν”.

**Context matches/status and relation:** CUBE-03→C03: the sole relevant hit is Hua, `154-generisation-cube`, in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched); no proof supplied]. Relation: verifies a sharply delimited numerical comparison while leaving its attribution to the uncertain manuscript phrase unresolved.

For a fixed straight-line arrangement, put the original added line at \(y=0\) and its distinct marked vertices at \((x_i,0)\). Nearby lines \(y=ax+b\) meet those vertices on the \(\nu\) distinct parameter-space walls \(b=-ax_i\), which divide a sufficiently small punctured neighborhood into \(2\nu\) chambers. This equals \(2^\nu\) for \(\nu=2\) and is smaller for \(\nu\ge3\); it does not count global realizations after moving the background lines. Confidence: high for the local fixed-realization count, because the distinct incidence walls and their \(2\nu\) sectors are computed in `records/research_cube_memo.md`, §3.

### C04 — A cube of indices is not automatically a surface neighborhood

**Kind:** own idea / conditional compatibility test, not a contradiction.

**Source:** cote 154, scan 154, line 44; scan 151, lines 2–6 and 76–82.

**Short quote:** “surface cellulaire des positions relatives”.

**Context matches/status and relation:** CUBE-04→C04: Hua, `154-generisation-cube`, in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched)] and the supplied Esquisse, marker 119/50, manuscript page 48, `context/Esquisse_cote119_copy1_API_transcription.tex:2212–2223` [API transcription not checked by eye; corresponding published §8 passage checked] are relevant. Relation: separates a state-indexing assertion from a modular-surface programme; neither hit supplies the extra identifications used in the test.

The local construction indexes resolution states by faces of an abstract cube; its generic parameter chambers correspond to cube vertices, so the indexing dimension must not be confused with stratum dimension. The Esquisse's modular-surface discussion supplies a direct historical context for classifying an added pseudoline, but does not establish this identification with a surface neighborhood (Grothendieck, 1997, §8, p. 41). Only with additional same-position, distinct-incidence, and regular-surface assumptions would a \(Q_\nu\) face-adjacency graph conflict with the cyclic adjacency required at an interior surface vertex, or path adjacency at a boundary vertex, for \(\nu\ge3\). Confidence: high for the conditional degree comparison, but its application to the manuscript is unresolved because the same-position and local-incidence assumptions are not supplied.

### C05 — Count projective contacts or antipodal orbits, not an unspecified raw set

**Kind:** notation question / own conditional counting caution.

**Source:** cote 154, scan 153, lines 157–158; scan 154, lines 31–32 and 44.

**Short quote:** `\unsure{\{s,\bar s\}}=D\cap D'`.

**Context matches/status and relation:** CUBE-05→C05: Hua, `154-generisation-cube`, in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched)] is the only hit; no supplied antipodal-orbit definition was found. Relation: qualifies the parameter identification without changing the frozen notation.

The frozen text on 153 uses an intersection pair \(\{s,\bar s\}\), while 154 defines \(S_D=D\cap S\) without explicitly writing \(\nu=|S_D|\). In an antipodal double-cover model, the independent surgeries are paired and the cube dimension counts projective contacts, or antipodal orbits, rather than automatically all points of \(S_D\). The abstract product of two-element local choice sets needs no preferred signs, but an identification with standard \(\{-,+\}^{\nu}\) coordinates requires choices and may change under additional quotients. Confidence: high for paired surgery in an antipodal model, but low for identifying the manuscript’s \(\nu\) because the required convention is not stated here.

### C06 — The edge count and specialization direction have an exact model

**Kind:** own idea / conditional incidence verification.

**Source:** cote 154, scan 154, lines 44 and 78.

**Short quote:** “ν2^(ν−1) arêtes”.

**Context matches/status and relation:** CUBE-06→C06: Hua, `154-generisation-cube`, in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched)] is the relevant hit. Relation: explains its edge count under an explicit model while retaining the missing semistable/one-contact dictionary.

In the support-controlled model, a sign vector with exactly one zero retains one marked vertex and has two generic refinements, giving \(\nu2^{\nu-1}\) such states. Replacing nonzero signs by zeros records specialization, and identifies these incidences with vertex-edge incidences of a cube. Equating those one-contact states with every manuscript semistable position remains an additional dictionary assumption, because 153 instead presents semistable positions through its qualified fuseau correspondence. Confidence: high for the product count and incidence rule, because every one-zero vector has exactly two generic refinements; the manuscript dictionary remains conditional.

### C07 — The fuseau assertion is about isotopy classes with stated qualifications

**Kind:** manuscript claim / qualification of an isotopy correspondence.

**Source:** cote 154, scan 153, lines 153–168.

**Short quote:** “classes d'isotopie de”.

**Context matches/status and relation:** CUBE-07→C07: no matching supplied-context line or results-register ID was found for fuseau/couloir/supracritique/rive-libre terms. Relation: records an unmatched source assertion with its stated qualifications, without making a novelty claim.

Scan 153 gives conditions involving a connected component, a corridor, critical boundary pseudolines, and their intersections, then states a canonical correspondence between isotopy classes of fuseaux and semistable relative positions. It separately says that the boundary isotopy classes determine a fuseau except in trivial cases. These statements should not be replaced by the unrestricted assertion that any lens between two curves gives a unique semistable position, particularly while some ambient notation and criticality terms remain undefined in these pages. Confidence: high for the stated textual qualifications, but the correspondence is not independently proved here because its corridor and criticality definitions are not supplied.

### C08 — One-element extensions supply a compatibility language

**Kind:** bounded literature comparison / own explanatory identification.

**Source:** cote 154, scan 154, line 44; Backman, Santos, and Yuen (2026), Definition 2.1 and Lemma 2.4.

**Short quote:** “générisations stbles”.

**Context matches/status and relation:** CUBE-08→C08: no supplied-context hit or results-register ID was found for the oriented-matroid objects searched. Relation: introduces a modern compatibility language as a conditional comparison, not as an archive definition or register theorem.

An added pseudoline is naturally compared with a rank-preserving one-element extension of an oriented matroid; arbitrary cocircuit signs need not define an extension. The Las Vergnas criterion quoted by Backman, Santos, and Yuen (2026, Lemma 2.4) says that a cocircuit signature defines an extension if and only if its induced signature defines an extension on every uniform rank-two minor with three elements. Our local surgeries realize actual admissible curves, rather than assuming that arbitrary global signs are compatible. Confidence: high for the cited compatibility condition, because the precise primary-paper statement was read; identification with the archive’s equivalence relation is not claimed.

### C09 — Allowable sequences distinguish combinatorial encoding from linear realization

**Kind:** bounded primary-literature comparison.

**Source:** cote 154, scan 154, lines 75–78; Goodman and Pollack (1980), abstract and introduction.

**Short quote:** “2ν”.

**Context matches/status and relation:** CUBE-09→C09: no supplied-context hit or results-register ID was found for allowable sequences, Goodman/Pollack, or stretchability. Relation: compares realizability questions without claiming a new nonstretchability result.

Goodman and Pollack (1980) encode planar configurations by permutation sequences and distinguish formal allowable data from geometric realization. That is a useful comparison for the difference between flexible pseudoline resolutions and the restricted two-parameter straight-line family. Failure of a local state to occur with the fixed background realization does not by itself show that the entire resulting arrangement is intrinsically nonstretchable. Confidence: high for this limited distinction, because the primary abstract/introduction was read and no unread numbered theorem is invoked.

### C10 — The preceding specialization question remains separate

**Kind:** explicit manuscript question / limitation of the local deduction.

**Source:** cote 154, scan 154, lines 34–37.

**Short quote:** “est-elle une spécialisation”.

**Context matches/status and relation:** CUBE-10→C10: Hua, `154-generisation-cube`, in `context/notes/RESULTS_STATE.md:122` [conjecture (unsearched)] and general specialization-word hits in `context/Esquisse_cote119_copy1_API_transcription.tex:1010,1099,1107,1163,1206` [API transcription not checked by eye; no register IDs] occur. Relation: leaves the principal-position question unanswered; no matching supplied theorem settles it.

The page asks whether every principal position through \(S_D\) specializes the given \(D\), then discusses those positions that do specialize it. Constructing nearby resolutions of an existing \(D\) does not answer that existence/classification question. Neither “principale” nor “critique” is identified here with a principal matroid extension, membership in \(\Sigma\), or the elementary generic/contact terminology used in the local model. Confidence: high that the question is left separate here, because the text asks it explicitly and the following discussion is restricted to specializations that already exist.

## 1. Exact evidential comparison with the supplied Hua extract

The source locators below are lines in the frozen page fragments. Scan 153 carries manuscript-page marker 152; scan 154 carries marker 153. The context explicitly maps Hua's page 153 to our scan 154.

| Item in the supplied extract | Frozen-text evidence | Bounded assessment |
|---|---|---|
| A position of an added pseudoline through \(\nu\ge2\) vertices | 154:31 says nonprincipal; 154:32 defines \(S_D\) and states \(\operatorname{card}S_D\ge2\) | The extract suppresses the opening restriction and assigns a meaning to \(\nu\) not explicitly defined on this page. |
| Stable generisations correspond to cube vertices | 154:44 | Directly supported as a manuscript assertion; no proof is written there. |
| A canonical cube | 154:44 has `\unsure{canon.}` | The transcription deliberately retains reading uncertainty. A mathematical canonicity statement also requires the equivalence relation and coordinates to be specified. |
| Exactly \(2^\nu\) vertices | 154:78 is `2^{\nu\unsure{+}}` | \(2^\nu\) is the elementary vertex count of a \(\nu\)-cube, but must be supplied as an inference, not as a correction of the frozen exponent. |
| \(\nu2^{\nu-1}\) edges | 154:78 | This displayed count is clear and agrees with the cube assertion. |
| The edges are generisations through exactly one vertex | 154:44 says semistable generisations; 153:165 relates semistable positions to fuseaux | The one-contact interpretation is valid in the model proved below, but its equivalence with the manuscript term is not established in these pages. |
| Incidence is specialization | 154:44 | Explicitly supported, although a convention for the order direction should be stated when translating into a poset. |
| Straight lines give only \(2\nu\) stable generisations | 154:75–76 contains an uncertain polygon/diagonal phrase and \(2\nu\), not an unambiguous prose assertion of that comparison | The local calculation below verifies a precise statement. It does not establish that every part of Hua's interpretation was read securely from the manuscript. |

**Verdict on the supplied object:** the central cube/edge-incidence assertion is corroborated. The numerical formulas have a rigorous local explanation under additional hypotheses. The extract's scope, parameter identification, one-contact terminology, and straight-line reading are not fully justified by the two frozen pages alone. The supplied “conjecture (unsearched)” status remains a report of the other project's status; it is neither upgraded to a theorem nor refuted wholesale here.

The first question at 154:34 is syntactically a question. The subsequent discussion at 154:36–37 is restricted to specializations that exist, and its orientation data do not constitute a proof that all proposed principal positions occur.

## 2. A precise conditional local proposition

### 2.1 Hypotheses

Work in \(\mathbb{RP}^{2}\), or equivalently with an antipodally symmetric lift and count each antipodal pair once.

1. \(A\) is a finite labelled, tame pseudoline arrangement, not a pencil: distinct members intersect exactly once projectively, transversely, with multiple concurrence allowed.
2. \(D\) is an additional pseudoline, distinct from the members of \(A\), and \(A\cup\{D\}\) is again such an arrangement. This is an assumption of the model, not an interpretation of “nonprincipale.”
3. The vertices of \(A\) on \(D\) are the distinct projective points \(p_1,\ldots,p_\nu\). At \(p_i\), there are \(m_i\ge2\) incident background branches.
4. Choose disjoint closed disks \(U_i\), containing no other old vertex and meeting no nonincident old pseudoline, with a conical local chart in which all incident branches and \(D\) are diameters. This is an explicit sufficient tameness condition.
5. Allowed changes fix \(D\) near every \(\partial U_i\) and outside \(\bigcup_i U_i\). In each disk they connect the original, opposite endpoint sectors, remain embedded, and cross every incident background branch exactly once, with no other old-vertex contact.
6. Classify generic states up to isotopy through generic curves satisfying the same conditions and avoiding every marked \(p_i\) at every time; for partially resolved states, keep the retained-contact (zero) set fixed throughout the isotopy. The background curves remain fixed as a configuration; an ambient formulation may preserve each old branch setwise, allowing intersection points to slide. Requiring an ambient isotopy to fix every point of the old curves would be a different, unnecessarily rigid equivalence relation.

The terms “generic” and “one-contact” below are defined by avoidance or retention of these marked old vertices. Their identification with the manuscript's stable and semistable positions is an additional hypothesis, not part of this proposition.

### 2.2 Why there are two choices even at a multiple concurrence

Remove the common vertex from \(U_i\). The \(m_i\) background diameters divide the punctured disk into \(2m_i\) cyclically ordered sectors. Crossing one background branch moves to an adjacent sector, so the sector adjacency graph is the cycle \(C_{2m_i}\).

The endpoints of the original \(D\)-diameter lie in opposite sectors. An allowed replacement crosses all \(m_i\) incident background branches exactly once, so its sector walk has length \(m_i\). Between opposite vertices of \(C_{2m_i}\), there are exactly two walks of that minimum length: one in each direction around the cycle. Extra winding or backtracking would require extra crossings and is excluded.

Both walks have embedded representatives. Within each sector, ordinary disk-arc isotopy, together with sliding the crossing points along the background branches, identifies representatives with the same sector walk. The two walks cannot be interchanged by an admissible isotopy avoiding the central vertex. Thus the local generic choice set \(B_i\) has exactly two elements.

A contact state passing through the central vertex supplies the intermediate zero state. A concrete family is obtained by translating the \(D\)-diameter slightly in the conical chart and interpolating back to the fixed original arc in an outer collar. The collar can be chosen away from all background branches met by the original arc there, so a sufficiently small interpolation creates no extra intersection. The signs of the translation select the two detours.

This argument depends on fixed opposite endpoint sectors and one crossing of each incident branch. The phrase “two sides of a vertex” alone would not establish the count without those restrictions.

### 2.3 Independence and preservation of the pseudoline condition

The disks are disjoint, so the replacements can be performed independently. No old pseudoline can contain two different marked \(p_i\): it would then intersect \(D\) twice projectively, contrary to hypothesis 2. Each replacement preserves its one intersection with every incident old pseudoline; all other intersections remain unchanged outside the support.

The resulting curve is embedded because the inserted arcs are embedded in disjoint disks and agree with the old curve near their boundaries. The modification is an isotopy of the added curve if crossings of old vertices are allowed at the transition parameter, so it retains the noncontractible projective pseudoline class. This larger isotopy class is used only to preserve the projective class; it is not the equivalence relation between generic states, which forbids marked contacts throughout. Consequently every chosen combination produces a valid arrangement \(A\cup\{D_{\epsilon}\}\).

The local classification is therefore
\[
\prod_{i=1}^{\nu} B_i,
\qquad \left|\prod_i B_i\right|=2^\nu.
\]
This proves the support-controlled count. It does not identify these classes with all possible global generisations under an unspecified equivalence relation.

The construction concerns one added curve at a time. Different representatives may coincide outside the disks, so the entire family is not asserted to form an arrangement simultaneously. In particular, this construction alone does not produce the pairwise-compatible boundary curves or the corridor data required by the fuseau assertion on scan 153.

### 2.4 Partial resolutions and the face-indexing convention

After choosing names \(+\) and \(-\) for the two elements of each \(B_i\), include the contact label \(0\). A local state is indexed by
\[
s=(s_1,\ldots,s_\nu)\in\{-,0,+\}^{\nu}.
\]
There are \(\binom{\nu}{k}2^{\nu-k}\) states retaining exactly \(k\) contacts. In particular, \(k=0\) gives \(2^\nu\), while \(k=1\) gives \(\nu2^{\nu-1}\).

Associate to \(s\) the face
\[
F_s=\{x\in[-1,1]^\nu:
 x_i=1\text{ if }s_i=+,\quad
 x_i=-1\text{ if }s_i=-\}.
\]
Coordinates labelled zero are free. Thus \(F_s\) has dimension equal to the number of zero coordinates. Replacing a nonzero sign by zero records a limiting specialization and enlarges the indexed cube face. A one-zero state has precisely two generic refinements, matching the two endpoints of its indexed edge.

This is a face-indexing or dual-incidence statement. In an actual \(\nu\)-parameter surgery box, the all-nonzero sign regions have dimension \(\nu\), while the all-zero state is its origin. They are indexed respectively by cube vertices and the full cube. An identification of indices is therefore not an assertion that the parameter stratification is the cube's ordinary face stratification, or that an embedded \(\nu\)-cell occurs in a two-dimensional moduli surface.

### 2.5 Antipodal and canonicity qualifications

If the source's \(S_D\) is a set of lifted points on a sphere, a projective contact is represented twice. The surgery at one lift must be accompanied by its antipodal surgery; they are not two independent binary decisions. The correct parameter for this construction is the number of projective contacts or antipodal orbits.

Scan 153's pair notation makes this issue real, but does not settle the source's convention for \(\nu\). Neither the raw cardinality nor an orbit cardinality should be inserted into the frozen formula without a further supplied definition.

The product of the local two-element sets is intrinsic to the specified local problem. Numbering coordinates and naming their signs are not intrinsic. Additional unlabelled equivalences, symmetries, global isotopies, or reorientation quotients may identify states; no count after those quotients is asserted.

## 3. The straight-line calculation

Assume now that the background arrangement has a fixed straight-line realization and that \(D_0\) is a straight line distinct from its members. Let its marked background vertices be \(\nu\) distinct projective points. Choose an affine chart in which these finitely many relevant intersections are finite, and coordinates
\[
D_0:\ y=0,\qquad p_i=(x_i,0),\qquad x_1<\cdots<x_\nu.
\]

Every sufficiently nearby projective line has a unique normalized equation
\[
D_{a,b}:\ y=ax+b.
\]
Passing through \(p_i\) is exactly the parameter-space condition \(ax_i+b=0\). Because the \(x_i\) are distinct, these are \(\nu\) distinct lines through \((0,0)\). They meet a small circle around the origin in \(2\nu\) distinct points and hence cut a small punctured neighborhood into exactly \(2\nu\) chambers.

All other background vertices are off \(D_0\). Their incidence walls miss the parameter origin, so a sufficiently small neighborhood avoids them. It can also avoid coincidence with any old line. Each chamber therefore gives a stable local relative state, and connectedness of the chamber supplies a continuous deformation through such straight lines.

An equivalent direct check uses the signs of \(ax_i+b\). As \(i\) increases, a nonconstant affine function changes sign at most once. There are two constant sign sequences and \(2(\nu-1)\) sequences with one change, for a total of \(2\nu\).

On a nonzero parameter wall there is exactly one marked contact. A nearby line through two distinct \(p_i\) would be \(D_0\) itself and hence pass through all marked points. Thus the straight-line family has only \(2\nu\) one-contact rays and, for \(\nu\ge3\), does not realize the intermediate multi-contact states of the full independent-surgery model.

For \(\nu=3\), take \(x_1=-1,x_2=0,x_3=1\). The patterns \(+-+\) and \(-+-\) cannot be values of an affine function at these three points, because its middle value is the average of its endpoint values. Small independently supported curved detours can produce both patterns under the hypotheses of section 2. This gives an explicit \(8\)-versus-\(6\) comparison.

**Limits of this calculation.** It uses a full two-parameter neighborhood of the added line, a fixed background realization, distinct incidence walls, and no quotient identifying chambers. Restricting to parallel translations gives only two local choices; repeated constraints count fewer distinct walls. Allowing the old lines to move changes the realization problem. In particular, the two excluded patterns in the three-contact example are not thereby proved intrinsically nonstretchable as abstract arrangements.

## 4. What this does not settle about the manuscript

- “Principale” is not identified with a principal extension in matroid theory, nor with being an element of \(\Sigma\). “Nonprincipale” does not by itself decide criticality.
- “Stable” and “semistable” are not supplied with complete definitions on 153–154. The local generic/one-contact dictionary is conditional.
- The unspecified corridor notation and critical-boundary conditions in 153:153–164 are not reconstructed from later literature. The fuseau/isotopy correspondence at 153:165 is recorded as a manuscript claim.
- The local construction neither answers 154:34 nor proves uniqueness or existence of the subsequent principal specializations.
- A canonical labelled sign cube, a canonical unlabelled incidence cube, a topological neighborhood, and a moduli-space quotient are different claims.
- No novelty, historical influence, global contractibility, global extension-space theorem, or complete reconstruction of \(X^*\) is asserted.

For the bounded comparison with scan 151, its line 2 calls \(X^*=\operatorname{Rel}(\underline\Sigma)\) a cellular surface; lines 4–6 discuss vertices corresponding to critical positions and outgoing data. Lines 76–82 explicitly retain difficulty in reconstructing edge endpoints. If a position in 154 were the same regular surface vertex, and if its listed stable and semistable generisations were exactly all distinct local faces and separating edges there, their dual adjacency would be cyclic of degree two at an interior vertex, or a path with degrees at most two at a boundary vertex. The graph \(Q_\nu\) has degree \(\nu\), so these extra identifications cannot all hold for \(\nu\ge3\). The passage begins with a nonprincipal position and does not supply the missing dictionary: this is a conditional compatibility test, not a contradiction attributed to the text.

## 5. Literature verification and precise use

### P1. Allowable sequences

Goodman and Pollack's original paper distinguishes an encoding by rotating projections from the question whether formal permutation data are realizable. Its abstract supplies a counterexample to universal geometric realizability of the specified permutation data; this is not asserted here to be a five-pseudoline nonstretchability result. This supports the limited distinction used in C09; no theorem identifying the present manuscript's relative-position space is imported. 

**Actually read:** publisher-indexed abstract and the indexed introductory passage of the primary PDF, printed pp. 220–221. The introduction points to Remark 2.3, but that numbered remark was not independently read in a reliable text layer, so no assertion is cited to it. The primary PDF URL is https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/PollackRichard/Pollack5.pdf . 

**APA:** Goodman, J. E., & Pollack, R. (1980). On the combinatorial classification of nondegenerate configurations in the plane. *Journal of Combinatorial Theory, Series A, 29*(2), 220–235. https://doi.org/10.1016/0097-3165(80)90011-4

### P2. One-element extension signatures

The modern primary paper defines a rank-preserving extension by deletion of the added element. Its Lemma 2.4 characterizes compatible cocircuit signatures using induced extension data on uniform rank-two minors with three elements; it attributes the criterion to Las Vergnas. This is a compatibility warning, not a theorem that arbitrary local or global sign choices form a cube. 

**Actually read:** §2.1, Definition 2.1 and Lemma 2.4; publisher HTML lines 174–209. The verified publication date is 18 March 2026. 

**APA:** Backman, S., Santos, F., & Yuen, C. H. (2026). Extension-lifting bijections for oriented matroids. *Discrete & Computational Geometry, 75*, 969–994. https://doi.org/10.1007/s00454-026-00834-w

The older originating reference is recorded as a **bibliographical lead, not a source personally checked in full**: Las Vergnas, M. (1978). Extensions ponctuelles d'une géométrie combinatoire orientée. In *Problèmes combinatoires et théorie des graphes* (Colloques internationaux du CNRS, Vol. 260, pp. 265–270). CNRS. Metadata appear in the modern paper's reference 22; no original theorem number or DOI is invented.

### P3. Direct contextual link in the Esquisse

The published §8 describes a combinatorial modular-surface construction classifying stable and unstable positions of an additional pseudoline, equivalently choices of an affine chart by a pseudoline at infinity. It motivates the comparison but does not provide the local proof or the extra identifications required above. 

**Actually read:** supplied API transcription at lines 2212–2223, and the published primary PDF's §8, printed p. 41, PDF index 36, text lines 1340–1348. The API copy's unchecked status is preserved.

**APA:** Grothendieck, A. (1997). Esquisse d'un programme. In L. Schneps & P. Lochak (Eds.), *Geometric Galois actions* (Vol. 1, pp. 7–48). Cambridge University Press. (Original text dated January 1984.) https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf

### Verification boundaries

Folkman–Lawrence and older extension references were located bibliographically, but inaccessible original passages are not presented as read proofs. Author-hosted survey material supplied leads only; the conditional calculation in sections 2–3 is proved explicitly here. The supplied Hua extract is the authorized comparison object, and attempts to obtain an external full entry were stopped; no content from an unseen full entry is inferred.

No external source is quoted at length. Mathematical propositions in sections 2–3 are explicitly conditional deductions made in this memo, with the scope of their relationship to the frozen text stated separately.

