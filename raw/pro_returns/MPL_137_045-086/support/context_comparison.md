# Context comparison support memorandum

## Scope, source status, and locator convention

This is research support for the root editor, not the final notes and not a
revision of the diplomatic transcription. It compares supplied text after the
freeze recorded at **2026-11-17 21:38:33 UTC**. The 42 fragments and combined
transcription still match all **43 SHA-256 hashes** in
`support/frozen_hashes.json`. No scan image was opened by this checker, and no
page fragment or combined transcription was edited.

The checker read the complete `context/README.md`,
`context/notes/RESULTS_STATE.md`, `context/hua_project/README.md`, and
`context/hua_project/137.modern.tex`, and the complete frozen text of scans
045–086. The supplied PS VI/VII texts were searched throughout; the passages
specified below were read in context. They were not read in their entirety.
No external literature search, Lean execution, or verification of the proofs
claimed by Hua was performed for this memorandum.

`Snnn:Lx–y` below means lines x–y of
`pages/MPL_137_045-086_137_scannnn.tex`. `H:Lx–y` means the supplied
`context/hua_project/137.modern.tex`. `RS` means
`context/notes/RESULTS_STATE.md`; `PS6` and `PS7` mean the supplied
`context/ps_chapters_VI_VII/ps6.tex` and `ps7.tex`. Original PS page numbers
are taken from their `\pspage` markers. Hua's manuscript page numbers are
one less than the scan identifiers in this packet; they agree here with the
archive foliation recorded in the frozen comments, not with a newly inferred
author pagination.

The supplied context explicitly treats its planning suggestions as unverified
leads. Hua's README identifies the modern reading as AI-produced interpretation,
not a transcription or an established result of this project. Hua itself
distinguishes normalized notation, mathematical repairs, and source statements
(H:L3–85). These distinctions matter throughout this memorandum.

## Principal findings

1. **The universal construction is substantial but its exactness hypotheses
   remain part of the source's work.** Scans049–057 contain a proposed theorem,
   two proof routes, and an important restriction of the exact-functor statement
   to an abelian target with all short exact sequences (S056:L28–33). Hua's
   headline part (b) omits that restriction (H:L1344–1345).
2. **The source does not require the multiplicative unit map to be an
   isomorphism at its displayed definition.** S066:L9–13 gives a map
   `1_B → F(1_B')`; Hua changes it to an isomorphism and says the page requires
   one (H:L1586–1593). This is a real difference in the supplied texts.
3. **Two modern repairs should remain conditional proposals.** The comparison
   on S073 fits good upper truncation ending in cycles under the left-exactness
   interpretation; Hua's word “naïve” is too strong without an additional
   argument. The factorization questioned on S071 can follow from preservation
   of a suitable source Σ-kernel without flatness of the target tensor product.
   Neither observation completes the author's full multiplicative construction.
4. **The polynomial/pd equivalence is asserted after strengthened
   representability and unit axioms, with one uniqueness claim already
   withdrawn.** The source itself inserts “n'est pas unique” on S076. Hua's
   claimed Lean result covers a homogeneous composition core, expressly not the
   full strict polynomial category structure (H:L1899–1919).
5. **The strongest integral-homotopy connection is in later PS VI, where it is
   a corrected programme and an explicit question.** PS VI §119, pp.501–503,
   distinguishes integral-coefficient polynomial cochains from binomial
   cochains and asks a comparison with all set-theoretic cochains. Cote137
   scans045–086 do not themselves supply that comparison theorem.

## 1. Scan-to-Hua map

| Frozen scans | Hua manuscript pages / section | Main comparison |
|---|---|---|
| 045 | p.44; “Le complexe universel,” proposition3 proof, H:L1197–1226 | Evaluation/Hom reconstruction; packet begins inside the argument. |
| 046–047 | pp.45–46; “Exemple3 et proposition5,” H:L1228–1271 | Dold–Puppe; direct factors/karoubian target for equivalence; fully faithful version without that assumption. Proposition4 begins on046 and its displayed formula continues on047. |
| 048 | p.47 | Only a marginal uncertain mark is transcribed. It does not provide a page count. |
| 049–057 | pp.48–56; “Classes de suites exactes et propriété universelle,” H:L1273–1422 | Σ axioms, proposed theorem, reconstruction and proof qualifications. |
| 058–064 | pp.57–63; “Caractérisation intrinsèque” and “Algèbre homologique relative,” H:L1424–1544 | Intrinsic category, added exactness axioms, essential image, Q, relative Ext and derived evaluation. |
| 065–072 | pp.64–71; “Structures multiplicatives,” H:L1546–1691 | Transported tensor, multiplicative functors, extension beyond K, cup products up to homotopy. |
| 073–074 | pp.72–73; “De Rham à puissances divisées,” H:L1693–1715 | Weight-n resolution/comparison, undeveloped pd structure on F; characteristic-zero Sullivan remark. |
| 075–084 | pp.74–83; “Catégories polynomiales,” H:L1717–1938 | Multigrading, withdrawn uniqueness, strengthened representation, Γ/α and asserted converse equivalence. |
| 085–086 | pp.84–85; “Questions ouvertes,” H:L1940–1966 | When Γ*(M) has pd structure; polynomial-law enrichment of composition and Γ on Hom. |

The source heading on S075:L3 is **“Catégories hypopolynomiales.”** The following
definition uses “polynomiale” (L5). Hua's modern section title should not replace
the source heading. S074:L3 is one sentence about De Rham/Sullivan in
characteristic zero, not a title for the whole packet.

## 2. Universal Σ-exactness: what the frozen text supports

### 2.1 Definitions and proposed theorem

S049:L5–20 fixes finite complexes with finite free components and degreewise
exact Σ sequences. Over the stated free objects those short sequences split in
each degree, but not necessarily as complexes. The initial abstract Sex1/Sex2
axioms, S049:L23–54, are weaker than a completed Quillen exact-category axiom
system. S050:L23–24 explicitly asks whether closure of Σ-monomorphisms and
Σ-epimorphisms under composition should be imposed. S060:L38–46 later adds
base-change/cobase-change conditions. Hua acknowledges the initial weakness
(H:L1288–1314); it should not be silently upgraded from the start.

The theorem on S051 is introduced by “Il faudrait prouver le” (L3), with a
marginal question whether B must be abelian (L5–8). Part (a) concerns **left
Σ-exact** functors, evaluation on the universal complex, full faithfulness, and
the relevant kernel condition on differentials (L14–28). The universal-triple
morphisms are also left Σ-exact (L30–34). The word “equivalence” appears in
cancelled text before the live fully faithful version. Part (b) concerns exact
functors and Σ-resolutions (L36–43).

The proof work is not a single uninterrupted polished proof. S052 is a cancelled
draft. S053:L16–23 assumes all morphisms of B have Σ-kernels and retains the
flatness doubt in the margin. The reconstruction and adjunction run through
S053:L29–56, S054, and the length/pullback induction S055. S056:L3–9 concludes
under the stronger all-kernels assumption, then L11–26 explains the weaker
fully faithful conclusion by a presheaf-valued reconstruction.

### 2.2 The qualification lost from Hua's part (b)

S056:L28–33 says the equivalence between exactness of F and its evaluated
complex being a Σ-resolution is established **“du moins si B cat. abélienne”**
with Σ all exact sequences. H:L1344–1345 states the part-(b) equivalence without
carrying that qualification into its headline. H:L1348–1357 presents the
preceding proof more decisively than this last source paragraph.

This does not prove that the broader theorem is false. It establishes a precise
editorial distinction: the frozen source supplies a restricted verification,
whereas the unrestricted modern statement needs its own argument. The marginal
flatness doubt on S053 likewise is an authorial question, not a demonstrated
counterexample and not a theorem that all targets must be flat.

### 2.3 What Hua says was formalized

H:L1326–1343 claims a Lean proof of a bounded finite-free model over an arbitrary
commutative base, with left exactness formulated by preservation of specified
kernel diagrams. It claims full faithfulness without a flatness assumption and
an equivalence after adding finite biproducts and kernels. It expressly excludes
the general relative-Σ/karoubian setting, part (b), later propositions, and the
cosimplicial extension. No Lean source or executable proof was checked here.
Accordingly, cite this as **Hua's reported formalization of a specified model**,
not as independent validation of all the manuscript's universal claims.

### 2.4 The intrinsic-category change is a repair, not a quotation

S060:L24–29 and S061:L18–29 develop an intrinsic category and its tentative
essential image. S061 describes finite free L, Z, B, H, while using provisional
language. H:L1478–1484 explicitly substitutes **all bounded finite-free
complexes** for that free-homology image because extension constructions also
produce torsion homology. This is a material mathematical change, explicitly
acknowledged by Hua.

H:L1490–1499 adds a PID hypothesis to its argument about kernels and admissible
monomorphisms. This is another added hypothesis, not a verbatim source result.
At the following universal characterization, S062:L34 emphasizes **“à g”**
with double underlining. H:L1500–1504 says Σ-exact without that left qualifier.
That omission is worth keeping visible alongside the earlier part-(b)
qualification.

S063:L3 introduces Q using finite free L, Z, B, H. S064:L9 still says “on doit
pouvoir montrer” and “sauf erreur” for the derived evaluation/Hom calculation.
H:L1506–1544 gives a more settled account. The source provides a proposed
relative-homological mechanism; it does not erase its own provisional language.

**Relevant state records:** RS:L467–469,
`137-perfect-complexes-universal-sigma-exact`, is explicitly a candidate with no
reference found, not a result already established by this project. RS:L10–19
also says there is no established own result directly on this packet. Earlier
cote137 scans002–044 are not supplied here; conclusions relying on those pages
must remain outside this comparison's source scope.

## 3. Multiplicative structure: precise agreements and differences

### 3.1 Which tensor and which commutativity?

S065:L7–30 constructs tensoring from the simplicial side and transports it to
complexes. This transported `*` should not be identified without explanation
with the usual total tensor product of complexes. Hua makes that distinction
explicit (H:L1546–1578). The data on S066–069 are coherent multiplicative
structure maps on a functor, including associativity, commutativity, and unit
diagrams. S072:L5–20 then states the resulting cup-product properties **up to
homotopy**, with the sign caveat, and obtains the graded cohomological product.

These are concrete connections to multiplicative (co)simplicial methods. They
do not by themselves identify all chain-level structures with a strictly
commutative differential graded algebra. Hua's E-infinity comparison is marked
as a modern analogy (H:L1597–1632), not a proved reconstruction theorem. This
agrees with RS `MPL_133 B06` (L290–291), which warns against equating strict
cosimplicial commutativity with strict DGA commutativity.

### 3.2 Unit: a source/interpretation discrepancy

S066:L9–13 displays μ and a unit **map** `1_B → F(1_B')`, with no isomorphism
mark. H:L1587 makes this a unit isomorphism; H:L1589–1593 calls the functor lax
monoidal with strong unit and says the page demands the isomorphism. The supplied
frozen text does not support that last attribution. The later unit discussion on
S071:L19–23 does not retrospectively change the displayed definition on066 into
an isomorphism. The final notes can describe the definition as lax unital unless
they separately identify a later stronger assumption.

### 3.3 Conditional factorization argument for the question on071

S070:L15–22 supplies presentations by objects I,J in K. S071:L8–15 marks the
desired factorization with a question. H:L1651–1658 diagnoses a need for target
tensor products to preserve kernels, suggesting flatness. The following is a
**bounded independent argument**, not a transcription correction or a completed
proof of the author's extension theorem.

Suppose presentations `0→X→I0→I1` and `0→Y→J0→J1` have been chosen, and suppose
the source diagram

```text
X*Y → I0*J0 → (I1*J0) ⊕ (I0*J1)
```

is a Σ-kernel diagram preserved by F. Form the map

`F(X)⊗F(Y) → F(I0)⊗F(J0) → F(I0*J0)`.

Its composite with each next component is zero: use naturality of the existing
μ on K, the zero composites in the two presentations, and biadditivity of the
target tensor. The kernel universal property therefore gives the desired unique
factor through `F(X*Y)`. This argument does **not** require the target tensor to
preserve kernels.

The remaining work is consequential: prove that the displayed source diagram
is the required admissible Σ-kernel, establish that F preserves it, and check
independence of presentations and coherence. Target flatness may supply a
different sufficient route, but its necessity does not follow from the question
mark alone. This is the bounded sense in which Hua's diagnosis may be stronger
than needed.

### 3.4 Conditional good-truncation reading of073

S073:L3 says the weight-n de Rham complex ends in Ψ^n and has the cohomology of
C through degree n **inclusive**; it calls the target a “complexe tronqué
supérieur.” It also says the pd structure on F is still to be defined. Hua
H:L1700–1707 calls the target a **naïve truncation**.

Under the left-exact evaluation interpretation `F(Ψ^n)=Z^n(C)`, the terminal
term naturally gives the good upper truncation `τ≤n C`, ending in `Z^n(C)`.
That preserves `H^n(C)`. Brutal/naïve truncation ending in `C^n` instead has
top cohomology `C^n / im(d^{n−1})`, generally larger. For example, the complex
`Z --id→ Z` in degrees0,1 has H0=0, whereas its brutal truncation at0 has H0=Z.

Thus good truncation is a plausible precise modern formulation **conditional
on the stated kernel interpretation**. This is not a claim that the present
packet supplies an unambiguous definition of the author's truncation terminology;
it is a reason to avoid importing Hua's “naïve” unqualified. The canonical
comparison and its homotopy uniqueness still depend on the source's resolution
and multiplicative hypotheses.

## 4. Polynomial/pd categories: strengthened assumptions and open steps

### 4.1 Composition is linear only in the outer variable

S075:L8–26 starts with finite products and a wide additive category of linear
arrows. Its composition-additivity condition is in the outer argument. Hua
H:L1722–1743 explicitly preserves that asymmetry and repairs the source's
`id_Y`/`id_X` variable in the dilation formula. That correction belongs in
commentary, not in the frozen page.

S076:L3–17 adds multigrading. The subsequent attempted uniqueness argument is
not a surviving theorem: the page already contains the live insertion
**“n'est pas unique”** (L21), a marginal characteristic-p counterexample
(L19), and cancelled proof text continuing into S077:L3–7. S077:L9 then takes
the decomposition as additional structure after mentioning a base-change
alternative. Hua H:L1757–1785 explains the failure, but the source's own
withdrawal should receive credit.

### 4.2 Ordinary representability is deliberately strengthened

S078:L5–23 introduces representability for tensor products and divided powers;
L25–31 asks about the unit. S079:L3 explicitly says the universal property must
be strengthened. L11–20 requires representation in the presence of all other
variables; L23 invokes the karoubian condition for homogeneous summands, with a
presheaf alternative on L24. S080:L3–20 adds the exponential/multigraded Γ
compatibility and explains how the unit follows under the stronger hypotheses.

H:L1788–1820 accurately emphasizes these spectator-variable and multigraded
conditions. Without them, the later equivalence statement is not the same
claim. A bare category with representing objects for just the unary functors
does not automatically supply all the strict product compatibilities used in
the converse.

### 4.3 The direction of α and the forgotten unit condition

S081:L11–23 introduces `α:Γ^{pq}→Γ^pΓ^q` with coherence. Hua H:L1827–1845
corrects an exponent in its modern version of the diagram; it should not be
reported as an exact source formula. S082:L3–23 lists the converse exponential,
associativity, degree0/degree1, and unit data. S083:L5–15 defines homogeneous
arrows using `Hom(Γ^n X,Y)` and their substitution. S083:L24 explicitly says
that the preliminary axioms had apparently omitted a condition on the unit
`1→Γ^q(1)`.

S084:L4 says the remaining axioms are checked, and L6 asserts equivalence of the
two notions. There is no full expanded verification on these pages. Hua
H:L1886–1899 acknowledges the forgotten unit and the asserted nature of the
equivalence. It also changes the source's reference to axioms c)–g) into its own
renumbered range; such labels must be mapped to the modern numbering rather
than quoted as source labels.

### 4.4 Hua's formalized core leaves the full equivalence open

H:L1899–1919 claims a Lean treatment of the graded co-Kleisli composition core,
including associativity and units. Its express exclusions include products,
additivity, multidegrees and homogeneity, the `1≅Γ^q1` condition, strict tensor
representation, the exponential formula, and the module example. Hence it does
not validate the whole source assertion on084.

There is a concrete reason for this limit: composing pure degrees p and q only
uses the degree-pq substitution formula. A category whose Hom is a direct sum
over degrees must also handle an inhomogeneous inner arrow and its mixed-degree
expansion. Linearity only in the outer argument does not make that extension
automatic. The extra exponential and multigraded compatibility data are exactly
where more work remains.

H:L1925–1934 and L1940–1966 draw connections to Roby and later strict polynomial
functors. This memorandum has not verified the bibliographical identification
or equated the different uses of “strict polynomial category.” Treat that as a
literature lead requiring a precise comparison of Hom objects and base-change
conditions.

### 4.5 The final questions are not the converse theorem again

S085:L12–14 asks when Γ*(M) itself has a pd structure. Its desired maps
`Γ^pΓ^q(M)→Γ^{pq}(M)` run **opposite** to the α used in the converse construction.
The presence of α therefore does not answer this question. S086:L4–10 asks for
composition and the induced Γ-map on Hom to be polynomial laws, not merely
maps of sets. Hua H:L1940–1966 marks these as open/enrichment questions. The
source does not finish a general proof for arbitrary tensor-pd categories.

**Relevant state record:** RS:L470–472,
`137-polynomial-categories-pd-tensor-categories`, records the construction as a
candidate rather than an established project theorem. It maps to the present
scans075–084, with the further open questions on085–086.

## 5. Explicit PS VI/VII links and their limits

| Supplied locator | What it explicitly says | Relation to this packet and limitation |
|---|---|---|
| PS VI §112, pp.461–462; PS6:L925–945 | Asks whether discrete group/monoid cohomology can be computed with polynomial cochains; proposes dévissage. | An early hope subsequently corrected in §119. Do not quote it without that later correction. |
| PS VI §117, pp.492–496; PS6:L2471–2688 | Contrasts module-valued and affine/vector constructions, polynomial maps and divided-power coalgebras, completed versus discrete Γ; flags nonflatness and failed comparisons. | A direct later setting for polynomial/divided-power ideas, but not an identification of all Γ constructions in137 with homotopy types. |
| PS VI §119, pp.500–502; PS6:L2895–2989 | Reports the failure of the proposed derived-Γ comparison; the Ga/W2 extension exposes the difference between integer-valued binomial polynomials and polynomials with integral coefficients. | Provides a specific obstruction to treating ordinary integral polynomial cochains as all cochains. This supports a careful binomial bridge, not a theorem already proved in137. |
| PS VI §119, p.503; PS6:L3000–3036 | Asks whether `Symbin_Z(L_*^∨) → Maps(L_*,Z)` is a weak equivalence for degreewise finite free simplicial Z-modules, with H0=0 and perhaps H1=0; suggests reduction to K(Z,n). | The sharpest supplied cochain/binomial/schematization question. The connectivity uncertainty belongs in any quotation of its scope. |
| PS VI §120, pp.506–507; PS6:L3139–3197 | Suggests analyzers encompassing pd, λ, binomial and Adams operations, with composition and coaddition/comultiplication compatibility. | A later conceptual link to compositional algebraic operations. The axioms are explicitly not fully written here; it is not a demonstrated equivalence with the Γ/α axioms of137. |
| PS VI §124, p.521; PS6:L3938–3980 | Distinguishes semisimplicial-scheme, pd de Rham, and category-with-diagonal approaches; questions the desired adjoint in the pd de Rham approach. | Strong evidence against conflating the programmes. The proposed pd construction forgets the original k-module structure except possibly over Z. |
| PS VI §128, p.540; PS6:L4981–4996 | Describes semisimplicial affine schemes through co-semisimplicial commutative algebras and linearization by forgetting multiplication. | An explicit later (co)simplicial-commutative-algebra link. It does not identify a strict commutative DGA replacement over every base. |
| PS VI §131, pp.547–549; PS6:L5280–5442 | Uses co-semisimplicial algebras with A0=k, components Sym(Mn), and flat Mn; proposes a square-zero model for a hypothetical spherical functor. | Records additional connectivity, flatness, and model-category restrictions; the derived adjunction remains a hope. |
| PS VI §132, pp.553–554; PS6:L5637–5693 | Discusses André–Quillen complexes, possible truncation, nonflat replacements, and the wrong-quadrant problem. | The source itself preserves unresolved reconstruction obstacles; these cannot be supplied by the finite-free calculations in137 alone. |
| PS VII §134, p.557; PS7:L116–135 | Explicitly relates schematization and ordinary linearization, contrasting Δ/Dold–Puppe models with integrators on more general categories. | A genuine programme-level connection, not an assertion that the two models are equivalent. |
| PS VII §139, pp.590–591; PS7:L1716–1744 | Says k-additive envelopes with diagonal triggered the schematization reflections and asks how far the operations formalism extends. | Relevant to multiplicative enhancements of categorical models; its questions remain questions. |

In §119's example, the splitting equation needs the binomial expression
`t(t−1)/2` (PS6:L2917–2949). It is integer-valued on integers but is not a
polynomial with integral coefficients. The next page introduces binomial rings,
and p.503 formulates the actual comparison question. This sequence is more
precise than a general resemblance between divided powers and binomial rings.

Whole-file literal searches in PS VII found no occurrence of the stems
`binom`, `cochain`, `cosimplic`, or `co-semisimplic`; the explicit links located
there are the linearization/schematization passages above. That is a bounded
search result, not proof that every synonymous formulation is absent. No
standalone word “Witt” was found in PS VI/VII; the W2 construction in §119 is
identified by its displayed extension rather than by that name in the supplied
text.

## 6. Relation to RESULTS_STATE and the planning guesses

| Record / exact supplied location | Supported use here | What this packet does not establish |
|---|---|---|
| `137-perfect-complexes-universal-sigma-exact`, RS:L467–469 | Track the universal Σ-exact candidate and its qualifications, especially051,053,056,061–064. | A theorem for all abstract relative exactness classes or a complete reconstruction of homotopy types. |
| `137-polynomial-categories-pd-tensor-categories`, RS:L470–472 | Track the Γ/α construction and asserted equivalence on075–084. | A verified full equivalence under only the initial axioms, or solutions to085–086. |
| `MPL_133 B01`, RS:L285–286 | Keep the binomial adjective attached to the correct object in any comparison. | A binomial statement in the present packet merely because Γ occurs. |
| `MPL_133 B05`, RS:L288–289 | Use PS VI §119's correction and new question as the strong later bridge. | The earlier polynomial-cochain hope as an established theorem. |
| `MPL_133 B06`, RS:L290–291 | Preserve the strict cosimplicial / strict DGA distinction. | Interchangeability of those algebraic models over Z. |
| `MPL_133 §2`, RS:L447; `MPL_133 §88`, RS:L454 | The register's digest points to finite-G-set/Burnside/Witt material elsewhere. | Independent verification of cote133, whose text and scans are not supplied here. |
| `MPL_136_047-094 §2`, RS:L455; `MPL_136_189-234 §2`, RS:L456 | Leads for comparing functorial cochains and truncated additive comparisons. | A checked use of those packets: only the register summaries were available. |
| `WG2 §2.4 #5`, RS:L461 | An outstanding abelian-variety/Fourier/Chern question. | A solution or direct example from045–086. |
| `WG H6`, RS:L463 | A schematization/local-systems hunch to compare in future. | A characteristic-zero localizer theorem derived from these finite-complex constructions. |
| `WG2 §Week #3`, RS:L465 | The declared137/133/153/PS research programme. | Evidence that its planned comparisons have already been made. |
| `GALOIS G.6`, RS:L352; `RESIDUE I.7`, RS:L363; `GALOIS E.11`, RS:L372 | Possible thematic motivation for keeping monoidal/coefficient data beyond a bare derivator. | Resolution of any of these open project entries by the present manuscript. |

The broad finite-G-set/Witt guess concerns another cote. The supplied digest is
enough to locate that follow-up, not to verify it. Searches of the frozen137 text
found no literal `binom`, `Witt`, `Chern`, `Fourier`, `schémati/schemati`, or
“variété abélienne” expression. Sullivan occurs only on074. These negative
findings concern this supplied text and these search terms; they do not replace
an image audit or rule out an indirect mathematical application.

Likewise, the general exact-colimit/total-asphericity questions elsewhere in RS
are not settled by the finite universal Σ-exact category. There is no supplied
argument connecting their hypotheses to these constructions. Avoid attaching
those IDs solely because “exact” or “complex” occurs in both records.

## 7. Additional hypothesis checks for the root editor

The following are independent mathematical checks suggested by the comparison.
They are not authorial statements and should not be entered as manuscript
readings or declared settled objections without further work.

**P0 and the meaning of left exactness.** In the nonnegative finite-complex model,
P0 consists of sums of discs and Ψ0 (S058:L53–59). These are projective for the
ambient degreewise-split exact structure, so short exact sequences entirely in
P0 split. Preservation of only those internal short sequences therefore imposes
no extra condition on an additive functor. The kernel relation determining Ψ0
from discs uses a next sphere outside P0. For the extension through P0 mentioned
on S069–070/H:L1636–1643, specify whether “left exact” means preservation of
ambient kernel diagrams; alternatively work in Q or the ambient category. This
is a clarification of the exactness data needed, not a refutation of an
unspecified convention.

**Q and a Quillen exact structure.** Over Z, free-homology complexes are not
extension closed in all finite-free complexes: extensions of Z in degree1 by Z
in degree0 can have middle complex `[Z --n→ Z]`, whose homology is not free for
nonunit n≠0. The two extensions with n=1 have free-homology middle terms, while
their ambient Baer sum n=2 does not. Consequently, restricting the ambient Σ
short sequences to Q does not automatically supply every exact-category closure
property needed for a standard Ext formalism. S063–064's relative-homological
claims need their precise axioms stated. Hua's acknowledgment that the initial
Σ structure is weak is relevant here.

## 8. Mechanical state and limitations

The frozen checks pass:42 fragments,794 inventory rows,43 unchanged hashes,
64 balanced environments,41 tikzcd diagrams,179 arrow commands. No structural
warning was emitted by the current static checker. This does not certify
diagram destinations, PGF grammar, mathematical meaning, or image fidelity.

The temporary `support/compile_wrapper.tex` now expands `\unsure` to a braced
group, supporting its use immediately after a math-script marker on086. This
support-only change did not affect frozen hashes. The wrapper has **not been
compiled**: engine binaries are present, but the installed environment cannot
locate the necessary LaTeX format/classes/packages. No package installation or
network workaround was attempted. The mechanical report records the full scope.

The root editor remains responsible for the image-based transcription and final
interpretive judgments. This memorandum makes no manuscript-reading claims from
images, does not resolve doubtful glyphs by context, and does not authorize any
change to the frozen transcription.
