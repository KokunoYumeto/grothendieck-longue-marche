# Source-ordered research register

Each item records a manuscript statement, its documentary state, or a specific research comparison. “Verified here” refers to the explicit proofs and computations included in this package; it does not change the status of an earlier research run. Context searches are recorded in `context_search_audit.csv`; the supplied context contains no earlier transcription of these 47 pages and no dedicated continuant-results row, so the README calculation brief is the relevant comparison for many entries.

## Scans 035–043: automorphisms, quadrics, and antipodism

### N035.1 — The initial conic uniqueness assertion is doubted immediately

**72/035, opening; kind: self-flagged.** The claim “$\exists!$ … conique $Q\subset X$” has a marginal question mark and is followed by “Peut-être faux,” with several words of that bracketed sentence uncertain. The later invariant-form calculation on 073 and the $n\ge2$ caveat on 077 supply concrete comparison passages, but the isolated capital $N$ on 035 has no definition within this page. **Context:** `README.md`, quadrics/definition questions — adds an explicit authorial doubt; no supplied results ID settles it.
<!-- context-query: conic;quadric;regular -->

### N036.1 — Reconstruction from adjacent products has precise local prerequisites

**72/036, “$\tau_i$ se reconstruit”; kind: unproved claim.** The proposed reconstruction takes the orthogonal complement of a sum of neighboring fixed spaces and identifies it with the intersection of two adjacent spans, after the displayed invertibility conditions. A proof must verify those fixed-space equalities, the double-perpendicular identifications, and the rank-one intersection over the stated base, rather than merely compare the names of the spaces. **Context:** `README.md`, regular-polyhedron definition brief — adds a local reconstruction mechanism; no supplied result ID proves this step.
<!-- context-query: orthogonal;reflection;polyhed -->

### N036.2 — The final trigonometric equality fails a direct exact substitution

**72/036, final two displays; kind: reading question.** The frozen line reads both “$\beta_i=\alpha_i+2$” and “$4\cos2\theta_i$,” with $\alpha_i=4\cos^2\theta_i$. At $\theta_i=\pi/3$ these give $3$ and $-2$, respectively, as recorded in calculation A15 and `group_quadric_checks_results.json`. **Context:** `README.md`, recomputable calculations — adds a numerical discrepancy while preserving the visible signs.
<!-- context-query: calcul;enumerat;quadric -->

### N037.1 — The isolated automorphism identification anticipates the next calculation

**72/037, the sole formula; kind: unproved claim.** The page identifies a doubtful script $\mathcal U_\rho$ with an automorphism group of an uncertain script object and the marked operators. Scans 038–039 then give a concrete group law and named morphisms, and calculations A03–A05 prove the centralizer identification in the recorded chain frame. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — supplies the immediately preceding isolated assertion, with its alphabet uncertainty retained.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;automorphism;rho -->

### N038.1 — The parameter law is a complete group-scheme construction

**72/038, “$\lambda *_\rho\lambda'$”; kind: unpursued implication.** The written multiplication, together with the open condition $1+\rho\lambda$ invertible, gives the Hopf algebra, inverse and two specialization maps in A01–A02. The actual maps are $t\mapsto1+\rho t$ and, over $R[1/\rho]$, $u\mapsto(u-1)/\rho$, while reduction modulo $\rho$ gives addition. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — verifies the supplied deformation description by explicit morphisms, without treating its register status as a proof.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;continuant;group scheme -->

### N038.2 — The group identity needs a reading note

**72/038, inserted “él. unit. $\unsure{1}$”; kind: reading question.** Direct substitution in the written law gives $t*0=t$ and $0*1=1$, so the parameter identity is $0$, whose character value is $1$. The doubtful numeral remains as transcribed; A01 records the exact coordinate map that relates the two identity values. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds a local reading qualification to the displayed formula.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;law;group -->

### N038.3 — The ring-valued realization data are explicit but introduced mid-calculation

**72/038, “hyperpolyèdre régulier … épinglé sur $S$”; kind: unpursued implication.** The page uses $n+1$ parameters $\mu_i$, $n$ parameters $\beta_i$, unit conditions on $1+\mu_i$, and a scalar expressed as both a continuant and $\langle\Pi,\Pi'\rangle$. Scans 059 and 073–077 supply the frame, pinning and projective/orthogonal reformulation used in the definition section below. **Context:** `README.md`, regular-polyhedron-over-a-ring question and bridge B5 — adds the actual geometric data; the symbol $n$ here is attached to the displayed dimension, and no level kernel is specified on this page.
<!-- context-query: regular polyhedron;ring;B5;72-automorphisms -->

### N039.1 — The automorphism theorem can be proved in the recorded frame

**72/039, “$\alpha$ et $(\alpha\alpha)$ sont des iso.”; kind: unproved claim.** Calculations A03–A05 give an explicit ring-level proof: every commuting endomorphism is $cI+t\,w\pi$, its units give $\mathbf G_m\times U_\rho$, and the unit-minor argument plus fppf descent gives the projective centralizer $U_\rho$. This proof centralizes the labelled operators and records the exact scalar quotient. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — supports its supplied statement with a proof for the actual coordinate model, while the full earlier definition remains a separate comparison task.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;automorphism -->

### N039.2 — The cancelled dual-action terminology has a precise algebraic comparison

**72/039, “contragrédientes” replaced by “transposées”; kind: withdrawn in the same text.** The transpose of $x\mapsto\pi(x)w$ is $\ell\mapsto\ell(w)\pi$, while the contragredient group operation uses the inverse transpose; these are the exact maps compared in A06. Both printed tensor strings in the frozen fragment remain identical, so their target typing is a reading question even though the wording replacement is clear. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — refines the representation underlying the automorphism assertion.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;linear;projective -->

### N040.1 — The torsor statement has an explicit two-section model

**72/039–040, “$D_0^{**}$ est un torseur”; kind: unproved claim.** A07 constructs the open line $\mathbf P^1\setminus\{[1:0],[1:-\rho]\}$, identifies its affine coordinate ring with that of $U_\rho$, and writes the translation matrices preserving the two sections. The marked point $[0:1]$ gives the stated trivialization after a compatible frame choice, and the two removed sections meet on $\rho=0$. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds the action on the pinned line, beyond the abstract group-law description.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;centre;torus -->

### N040.2 — The preservation equation gives a subgroup over the entire base

**72/040, “$\lambda(\sigma+\lambda\widetilde\sigma\widetilde\rho)=0$”; kind: unpursued implication.** Expanding the quadratic form under $I+t\,w\pi$ gives the exact coefficient polynomial in A09, and hence a closed subgroup of $U_\rho$ with no division by $2$. Evaluation at the fixed normalized vector $a_0$ also identifies preservation of the form with preservation of its projective quadric in this frame. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds the orthogonal stabilizer inside the full automorphism group.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;quadric;quadratic -->

### N041.1 — The even case retains a nonidentity specialization in characteristic two

**72/041, “antipodisme”; kind: unpursued implication.** The source equation becomes $t\sigma'(1+\rho't)=0$, and its stated nonidentity root is $-1/\rho'$ when the written unit conditions hold. The concrete $\mathbf F_2$ specialization in A11 gives the two-root algebra $\mathbf F_2[t]/(t^2+t)$, exhibiting the section directly in the additive fibre of the same family. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds a characteristic-two stabilizer calculation.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;characteristic;additive -->

### N042.1 — The request for a common parity statement is explicit

**72/042, “Donner un énoncé commun aux cas $1^\circ)$ et $2^\circ)$”; kind: self-flagged.** The margin asks for a common statement after observing that $-2/\rho$ can vanish in characteristic two. A09–A11 give the common preserving algebra and its integral parity substitutions, while the proposition on 043 records the author's own subsequent unified formulation. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds both the request and its local continuation, without suppressing the degeneration of the section.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;characteristic;group -->

### N042.2 — Whole-group invariance is controlled by two coefficients

**72/042–043, “$\sigma=0$ et $\widetilde\sigma\widetilde\rho=0$”; kind: unproved claim.** The coefficient argument in A09 proves this exact criterion in the displayed model, including coefficient rings with zero divisors. The parity substitutions in A10 identify the even and odd lists by explicit polynomial maps. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — verifies the invariance condition missing from the supplied summary of the group family.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;quadratic;ring -->

### N043.1 — The $n=1$ example loses a needed qualification

**72/043, example “$\rho$ inv.” after the cancellation of $2$; kind: reading question.** A11–A12 give $n=1$, $k=\mathbf F_2$, $\beta_0=1$, where $\rho=1$ but the preserving subgroup has equation $t^2=0$ and only the identity geometric point. This directly tests the literal everywhere-nonidentity assertion, while the later proposition's stronger unit condition excludes that example. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds a concrete qualification rather than silently restoring the deleted factor.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;characteristic;torus -->

### N043.2 — The marginal question on the local-section criterion remains visible

**72/043, proposition (d), marginal “?”; kind: self-flagged.** Under its displayed vanishing coefficient the existence of a section with parameter invertible forces the remaining coefficient to vanish, and the open parameter scheme $D(t(1+\rho t))$ gives a concrete fppf cover carrying such a section. The local topology intended by the isolated “loc.” is not named on this page, so the notes retain that distinction of specified constructions rather than infer a Zariski-local assertion. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — identifies the exact local-cover issue in the question-marked clause.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;local;group scheme -->

## Scans 045–055: discriminants, matchings, centres, and characteristic two

### N045.1 — The quadratic form is specified by a complete chain of pairings

**72/045, “$f$ caractérisée par les conditions”; kind: unproved claim.** The three normalizations and the displayed diagonal, adjacent and nonadjacent pairings give the polynomial form written in A09. The script records the full vertex/edge pairing matrix for $n=1$ through $5$, with $(n+2)(n+1)$ entries and the exact structural-zero count, and A08 proves the invariant-form line on the centred determinant localization. **Context:** `README.md`, calculations and quadrics brief; **Hua, findings register, 72-automorphisms-deform-gm-to-ga** and **Hua, findings register, 72-invariant-subspaces-string** — supplies the coefficient data supporting their common matrix model.
<!-- context-query: quadratic;quadric;72-automorphisms;72-invariant -->

### N046.1 — The determinant recurrence is a directly recomputable calculation

**72/046, the $F_n$ determinant and recurrence; kind: unpursued implication.** The tridiagonal determinant has contributions only from fixed points and disjoint adjacent transpositions, giving the recurrence and the finite examples catalogued in `enumerations.md`. The recomputation preserves the source's chosen diagonal and off-diagonal entries, and records any change of sign or argument count explicitly. **Context:** `README.md`, “Returns: enumerations that a script can recompute” — supplies exactly that requested calculation; the supplied results register has no continuant proof row.
<!-- context-query: continuant;calcul;enumerat -->

### N046.2 — The small question under a diagonal entry flags a coefficient check

**72/046, determinant with “?” beneath the final $2$; kind: self-flagged.** The transcription retains the uncertain question mark beneath the diagonal coefficient, independently of the readable matrix entry. The determinant script tests the literal displayed matrix and does not use the question mark as permission to replace that entry. **Context:** `README.md`, calculation brief — adds a locally flagged coefficient check.
<!-- context-query: calcul;enumerat;quadratic -->

### N047.1 — The admissible permutations are path matchings

**72/047, “$\sigma$ admissible”; kind: self-flagged.** The question-marked determinant expansion constrains every image to $i-1,i,i+1$, and the proof in `enumerations.md` identifies these permutations with disjoint adjacent transpositions by an explicit map from an edge set to its product of swaps. For $p$ swaps on $n$ positions the count is $\binom{n-p}{p}$, and the supplied script lists every matching through $n=12$. **Context:** `README.md`, enumeration brief — supplies the parameterization and totals requested there.
<!-- context-query: enumerat;calcul;graph -->

### N047.2 — Two written restrictions omit valid determinant terms

**72/047 and 049, “$p\ge1$” and “Attention $p=0$!”; kind: reading question.** The lower bound on 047 excludes the identity matching, whose product is the diagonal term, whereas 049 explicitly includes and warns about $p=0$. The gap-variable equality on 047 also loses the final slack gap: $n=3,p=1$ has two adjacent swaps, and the literal restricted gap list gives only one, as the explicit enumeration shows. **Context:** `README.md`, enumeration brief — records two source-local indexing issues and the later treatment of the first.
<!-- context-query: enumerat;calcul;continuant -->

### N048.1 — The centre coordinates are determined by a unit-ended recurrence

**72/048, “$\zeta_n=1,\ \zeta_{n-1}=2$”; kind: unpursued implication.** The common-kernel recurrence determines each preceding coordinate from the displayed endpoint values and gives the centre vector in A03. Its final coordinate is $1$, so this constructs a primitive line even at a zero of $\rho$, while division by $\rho$ is exactly the additional map to the affine centre. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds the actual centre vector behind the parameter $\rho$.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;centre;continuant -->

### N048.2 — A question-marked pairing is completed on the same sheet

**72/048, “$2f(c')=\langle c',\Psi(c')\rangle\overset?=$”; kind: self-flagged.** The subsequent lines evaluate the pairings against every $a_i$ and end with $\Psi(c')=-\zeta_0a_{-1}^*$ and $2f(c')=-\zeta_0\zeta_{-1}$. A09 and the symbolic checks verify those exact polynomial identities in the recorded reflection frame. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds both the question and its written local resolution.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;continuant;quadratic -->

### N049.1 — The determinant normalization and the “no cancellation” claim have a finite model

**72/049, “Il n'y a pas de cancellation de termes”; kind: unproved claim.** Each admissible edge set gives a square-free matching monomial in the independent edge parameters, with its explicitly determined diagonal factor and sign, so distinct edge sets have distinct supports before any parameter specialization. The script records the determinant, matching expansion and the $B$-monomial factorization separately, allowing the source's normalizations to be compared by an actual polynomial equality. **Context:** `README.md`, enumeration brief — verifies the generic-polynomial mechanism, without extending the no-cancellation phrase to arbitrary specialized values.
<!-- context-query: continuant;enumerat;calcul -->

### N049.2 — The index warning concerns the number of arguments

**72/049, bottom “Attention, $n-1$ et non $n$!”; kind: reading question.** The continuant $L_n$ has $n-1$ edge arguments, and the warning is retained verbatim in the frozen transcription and inventory. The later indices and argument lists are compared to that parameter count in the reproducible catalogue, with doubtful or extra arguments identified as reading issues. **Context:** `README.md`, calculation brief — adds an explicit source warning relevant to the enumeration parameters.
<!-- context-query: continuant;calcul;enumerat -->

### N050.1 — Low-degree values and reversal provide independent checks

**72/050, “$L_1$” through “$L_4$” and the reversal NB; kinds: unpursued implication and reading question.** For the reversal matrix $J$, the entrywise identity $JA_n(B_1,\ldots,B_{n-1})J=A_n(B_{n-1},\ldots,B_1)^T$ proves the determinant's parameter reversal, while the catalogue retains the source NB's argument-count question. The standard low-degree polynomials and the final $L_4$ alpha expression agree, but the earlier surviving $B$ expression has residual $B_1^2+B_2^2+B_3^2-B_3B_4$, and $B_i=B_i'+4$ sends the shifted product to $(-1)^n\prod_iB_i'/2^n$, exposing the written scalar-only right side; E04 and the E-Q050 entries in `enumeration_reading_questions.csv` record these precise discrepancies. **Context:** `README.md`, calculation brief — supplies exact low-degree comparisons and the basis-reversal map without certifying every surviving equality.
<!-- context-query: continuant;calcul;enumerat -->

### N051.1 — The mod-two formulas select maximal matchings

**72/051, “mod $2$”; kind: unpursued implication.** In even size the unique perfect matching survives the matching expansion modulo $2$, while in odd size the integral half-continuant retains the maximal matchings indexed by the unmatched vertex. The script enumerates those edge sets and checks the written parity-normalized recurrence; these are polynomial reductions over $\mathbf Z$ followed by the map to $\mathbf F_2$, rather than division inside that field. **Context:** `README.md`, enumeration and ring-calculation brief — supplies the exact reduction map and term counts.
<!-- context-query: continuant;ring;enumerat -->

### N051.2 — The raised delta mark and a visible last exponent remain reading questions

**72/051, even determinant-square display; kind: reading question.** The prime/star alternative and the unfinished continuation strokes are preserved, and the catalogue records the precise polynomial obtained from the surrounding determinant definition before comparing this line. Any exponent or normalization discrepancy is reported against that definition, without upgrading the doubtful raised stroke to a confident prime. **Context:** `README.md`, recomputable calculations — adds the scope of the symbolic comparison.
<!-- context-query: calcul;continuant;quadratic -->

### N052.1 — The boxed recurrence reconstructs the centre coordinates

**72/052, “$L_n=2L_{n-1}-B_1L_{n-2}$”; kind: unpursued implication.** Expanding the tridiagonal determinant at the first row gives the boxed recurrence, and reversing the parameter order identifies the solutions with the recorded $\zeta_{n-i}$. The first recurrence above it has an uncertain subscript and the rearranged coordinate line has a division/minus alternative, both left in place and compared to the boxed identity only in the notes. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** and `README.md` calculation brief — supplies the explicit continuant expression for its centre parameter.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;continuant -->

### N052.2 — The two sigma definitions have an explicit equation between them

**72/048 and 052, “$f(c')=\sigma$” and “$\sigma=\zeta_0$”; kind: reading question.** A14 assigns temporary scan-indexed names in the research notes and records the exact relation $2\sigma_{[048]}=-\rho\sigma_{[052]}$. This retains both written definitions and supplies the comparison needed to use later form values and determinants. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — qualifies the notation supporting the centralizer and quadric calculations.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;continuant;rho -->

### N053.1 — Smoothness and biregularity use the parity-normalized discriminants

**72/053, “$(\mathcal E,V,f)$ birégulier”; kind: unproved claim.** The page gives four discriminant expressions and two smoothness criteria, then identifies their joint unit condition with invertibility of $f(\widetilde o)=-\sigma'\rho'$. The recomputation identifies the determinant polynomials and their parity-normalized versions; a full relative smoothness statement uses the fibrewise quadratic-form criterion, including the odd-rank characteristic-two radical value, rather than only the determinant of the polar matrix. **Context:** `README.md`, quadrics and ring calculations — adds a concrete proof obligation and the polynomial data for it; no supplied results ID settles this smoothness assertion.
<!-- context-query: quadric;quadratic;ring -->

### N053.2 — The prime notation changes again in the dual calculations

**72/053 and 061, “$\sigma'$”; kind: reading question.** On 053 the prime denotes the parity-normalized $L'_n$, whereas 061 defines a left-end cofactor $\rho_{0,n-2}$ with that symbol. A14 gives the actual maps: parity normalization in the integer polynomial ring and reversal $\beta_i\mapsto\beta_{n-1-i}$ between the two endpoint cofactors. **Context:** `README.md`, calculation brief — records the comparison required before importing either primed symbol into a later formula.
<!-- context-query: continuant;calcul;ring -->

### N053.3 — The full polar determinant has a recorded sign discrepancy

**72/053, “$\delta_{\mathcal E}=B\sigma$”; 72/046, determinant; kind: reading question.** For the displayed polar Gram matrix on $E$, expansion at its first row gives $\det G_E=-M_n\sigma_{\mathrm{tail}}$, where $M_n=\prod_{i=0}^{n-1}\beta_i^{\,n-i}$ and $\sigma_{\mathrm{tail}}=L_n(\beta_1,\ldots,\beta_{n-1})$, whereas the restricted matrix gives $\det G_V=M_n\rho$. Thus the literal positive full-space expression on 053 differs by a sign from the determinant convention on 046; E10 and `computation_conventions.md` give the exact comparison, leaving both frozen displays intact. **Context:** `README.md`, calculation brief and **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — records the determinant convention needed for its invariant quadratic form.
<!-- context-query: continuant;calcul;quadratic;72-automorphisms-deform-gm-to-ga -->

### N054.1 — The antipodal operator is controlled by the normalized centre vector

**72/054, “$\underline a=-\mathrm{id}+\Pi\otimes o'$”; kind: unpursued implication.** The identity $\langle o',\Pi\rangle=2$ computes the square of this operator directly and explains the recorded involution, while the right margin preserves the possibility that $o'$ exists when the unscaled affine centre does not. The characteristic-two exceptional value $o'=0$ must be carried along into every fixed-locus statement, as A12 shows concretely. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds the normalized-vector extension and its explicit degeneracy.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;centre;characteristic -->

### N054.2 — The fixed-locus sentence has an internal exception

**72/054, “se réduit à $P(V)$ en car. $2$”; kind: reading question.** The same page's margin gives $o'=0$ and $\underline a=\mathrm{id}$, and A12 exhibits the resulting entire fixed projective space over $\mathbf F_2$. The seven fixed points versus three on $P(V)$ are computed directly, so the blanket sentence cannot be used without its preceding qualification. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds a verified internal consistency check.
<!-- context-query: 72-automorphisms-deform-gm-to-ga;centre;characteristic -->

### N054.3 — The two intersection sections remain separated by a unit determinant

**72/054, “rev. étale de longueur $2$”; kind: unproved claim.** On the stated locus where $\sigma'=\sigma$ is invertible, the even binary restriction has factors $\mu$ and $\lambda+\rho'\mu$, giving the two sections $[1:0]$ and $[-\rho':1]$, whose determinant is $1$. A13 verifies that particular two-section construction and relates the second section to $-\rho's_0+\widetilde o$. **Context:** `README.md`, quadrics brief — supplies the explicit root map for the stated line/quadric intersection.
<!-- context-query: quadric;quadratic;calcul -->

### N055.1 — The odd characteristic-two restriction is a double point

**72/055, “$D_0$ est tangente à $Q_X$”; kind: unproved claim.** The displayed binary polynomial specializes to a unit times $\mu^2$ under the page's nonvanishing condition, giving a length-two subscheme with one support point. A13 and the script compute that multiplicity, while the margin's $\underline a x=x$ records the accompanying collapse of the antipodal geometric section. **Context:** `README.md`, quadrics brief and **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds the exact tangency algebra.
<!-- context-query: quadric;72-automorphisms-deform-gm-to-ga;characteristic -->

### N055.2 — A geometric reconstruction is abandoned and later reformulated

**72/055, cancelled “Supposons $n$ pair”; 72/076–077, reconstruction and equivalence; kind: withdrawn in the same text.** The whole final attempt to pass from $(X,Q_X,\tau_*)$ to the doubtful “antidual|multidual” data is struck through. The later projective quadratic triple and its lift conditions give a concrete comparison passage, but their rewritten scope and $n\ge2$ qualification must be retained. **Context:** `README.md`, definition and B12 questions — adds a cancelled precursor to the later reformulation.
<!-- context-query: B12;quadric;regular polyhedron -->

## Scans 057–071: duality and centred calculations

### N057.1 — The displayed negative-diagonal determinant carries a dimension sign

**72/057, the determinant identified with $\rho$; kind: reading question.** For the displayed matrix $Q$ with diagonal $-2$, upper entries $1$ and lower entries $\beta_i$, the entrywise identity $Q^T=-A_{n+1}$ with the continuant matrix gives $\det Q=(-1)^{n+1}L_{n+1}(\beta_0,\ldots,\beta_{n-1})$. The exact script records the sign, so the literal equality to $\rho$ needs attention at even $n$, with no invertibility requirement on the $\beta_i$ in this matrix identity. **Context:** `README.md`, calculation brief and **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — qualifies the determinant used as its centre parameter.
<!-- context-query: continuant;72-automorphisms-deform-gm-to-ga;calcul -->

### N058.1 — The cancelled invariant-space draft has a later continuation

**72/058 and 080; kind: withdrawn in the same text.** The draft's “Var'tés invariantes,” incidence picture and boxed $\beta_0=0$ anticipate the eventual theorem, but the entire argument is cancelled. Items IS01–IS04 give the exact matrix comparison and preserve the distinction between the draft's documentary state and the proof supplied in these notes. **Context:** **Hua, findings register, 72-invariant-subspaces-string** — adds the earlier cancelled source passage.
<!-- context-query: 72-invariant-subspaces-string;invariant -->

### N059.1 — The general pairing table gives a universal coordinate construction

**72/059, “$\mu_i=\lambda_i-1$”; kind: unpursued implication.** The pairing entries define $T_i=I+a_i\phi_i$ over $\mathbf Z[\mu_i,\beta_j,(1+\mu_i)^{-1}]$, with inverse $I-(1+\mu_i)^{-1}a_i\phi_i$. The specialization homomorphism $\mu_i\mapsto-2$ gives the involutory reflection chart used in the quadratic calculations, and the basis-to-orbit map is written explicitly in invariant-subspace Appendix A1. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** and **Hua, findings register, 72-invariant-subspaces-string** — supplies their common coordinate model and the base-change map relating the general parameters to reflections.
<!-- context-query: 72-invariant-subspaces-string;72-automorphisms-deform-gm-to-ga;pseudo -->

### N061.1 — Four interval continuants organize the dual formulae

**72/061, “$\rho,\sigma,\sigma',\gamma$”; kind: unpursued implication.** These are respectively the full continuant, its two endpoint deletions, and the interior deletion, with the displayed empty-interval values $2$ and $1$. The table on this page reconstructs dual coordinates by a unit-triangular matrix, and the script prints that matrix and its inverse; the uncertain reversed-index $j-i+1$ remains a reading question against the explicit argument count. **Context:** `README.md`, enumeration brief and **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds the cofactor data used in the dual centralizer computations.
<!-- context-query: continuant;72-automorphisms-deform-gm-to-ga;calcul -->

### N061.2 — The parity rule is corrected within the page

**72/061, deleted “$\widetilde\rho_{ij}=\frac12\rho_{ij}$” and oval case table; kind: withdrawn in the same text.** The global halving rule is crossed out and replaced by the parity-dependent rule, with further crossed and inserted parity words inside the table. The integral matching expansion explains the halving exactly in the odd-size continuants, retaining the manuscript's local indexing rather than applying a universal factor $1/2$. **Context:** `README.md`, ring calculations — adds an explicit internal correction crucial in characteristic two.
<!-- context-query: continuant;ring;characteristic -->

### N063.1 — The boxed determinant identity is the organizing scalar relation

**72/063, “$\sigma\sigma'=\beta+\gamma\rho$”; kind: unproved claim.** The continuant proof in `enumerations.md` verifies this identity with the endpoint-cofactor meanings of $\sigma,\sigma'$ and $\beta=\prod\beta_i$. It gives the exact scalar relation used by the two composition formulas and the later centred coefficient calculations. **Context:** `README.md`, calculation brief — supplies the missing cofactor identity; no supplied result ID establishes it.
<!-- context-query: continuant;calcul;enumerat -->

### N063.2 — The rank-one defect gives an integral inverse numerator

**72/063, “Dén. de $\Psi^{-1}$”; kind: unpursued implication.** The recorded compositions differ from scalar multiplication by the explicit rank-one term $\gamma\Pi'\otimes\Pi$, and the numerator $\sigma\Psi'+\gamma\Pi\otimes\Pi$ satisfies the stated scalar-composition identity in the script's typed bases. This constructs a polynomial map before localizing at $\beta\sigma$, which is the precise relation between the inverse notation and the later $\Theta$ calculations. **Context:** `README.md`, calculation brief and **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — adds an explicit map relating the duality and centralizer tensors.
<!-- context-query: continuant;72-automorphisms-deform-gm-to-ga;linear -->

### N063.3 — A failed orthogonality attempt is cancelled, then repaired by a new vector

**72/063, cancelled “$t_0$ orth.” with “?”; 72/065, $t_{n+1}$; kind: withdrawn in the same text.** The cancelled block itself computes the pairings as $\gamma$ and $\beta+\gamma$, and then introduces a combination cancelling the common $\gamma$ term. Scan 065 gives the surviving $\Theta(s'_{n+1})$ vector and its zero pairings with the first vertices, all recomputed in the supporting script. **Context:** `README.md`, calculation brief — records both the author's question and the explicit later replacement.
<!-- context-query: calcul;quadratic;continuant -->

### N065.1 — The dual vertex pairing has a triangular enumeration

**72/065, “$\langle s_i,s'_j\rangle$”; kind: unpursued implication.** The two cumulative vertex lists define a pairing matrix with the displayed zero region and diagonal ones, and the catalogue records the uncertain endpoint $n-1|n+1$ separately from the complete computed matrix. The construction is reproduced for $n=1$ through $5$ with every entry retained. **Context:** `README.md`, enumeration brief — supplies the finite table and its explicit parameters.
<!-- context-query: enumerat;calcul;linear -->

### N065.2 — The polynomial numerator survives beyond the inverse locus

**72/065, “mais sans que néc. $\sigma$ inv.”; kind: unpursued implication.** The explicit $t_i=\Theta(s'_i)$ still exists as a polynomial vector before $\Psi^{-1}$ exists, and its pairing with the affine-coordinate functional is $-\beta$. Thus division by the stated unit $\beta$ gives the written normalized affine point through the actual map $t_i\mapsto-t_i/\beta$, without requiring a second localization at $\sigma$. **Context:** `README.md`, ring calculations — adds the precise extension map highlighted by the author.
<!-- context-query: ring;calcul;continuant -->

### N065.3 — The vanishing and norm assertions are finite symbolic tests

**72/065, “$t_i=0$ … sss $\sigma=\gamma=0$”; kind: unproved claim.** The $a_n$ and $a_{n-1}$ coefficients of $t_{n+1}$ are $\gamma$ and $2\gamma-\sigma$, and the invertible maps in $t_i=\tau_i t_{i+1}$ transport the resulting simultaneous-vanishing test to every $t_i$; the displayed formula $t_{n+1}=-\sigma a_n'^*+\gamma\Pi$ proves the converse, and $\sigma\sigma'=\beta+\gamma\rho$ then gives $\beta=0$. The script verifies the vector's orthogonality and its norm $\beta\widetilde\sigma\widetilde\gamma$ in its explicit dimensions, while these coefficient identities record the general mechanism. **Context:** `README.md`, calculation brief — adds a direct check of the numerator's degeneracy.
<!-- context-query: calcul;continuant;quadratic -->

### N067.1 — Two question marks occur inside a cancelled cofactor calculation

**72/067, cancelled “$\sigma\sigma'-\beta$” and “$\Psi'\Psi$”; kind: self-flagged.** The page questions both the interior-continuant factor and its rank-one composition interpretation, although the same scalar identity is already boxed on 063. The determinant calculation verifies the scalar identity and the typed matrix computation verifies the composition in the chosen frame, while preserving the cancellation and the incomplete opening $\Theta$ formula as documentary facts. **Context:** `README.md`, calculation brief — adds the self-checking stage rather than treating the crossed block as a settled lemma.
<!-- context-query: calcul;continuant;linear -->

### N067.2 — Midpoint and dual-edge sums have explicit quadratic values

**72/067, “pour mémoire”; kind: unpursued implication.** The source lists $u_0=s_0+s_1$ and $v=t_n+t_{n+1}$ with values $f(u)=-1$ and $f(v)=\beta\sigma(2\gamma-\sigma)$. The script recomputes the four-row memory table from the same form and vector matrices, keeping the distinction between a sum and the later divided midpoint through the map $u\mapsto u/2$. **Context:** `README.md`, enumeration brief — adds a small exact norm table.
<!-- context-query: calcul;enumerat;quadratic -->

### N069.1 — The two low-dimensional examples test the whole dual construction

**72/069, “Ex $n=1$” and “$n=2$”; kind: unpursued implication.** The listed scalars, inverse numerator, vector and norm agree with the coherent continuant calculation except for the separately marked coefficient discussed next. The catalogue gives each expression and its residual, so the examples test the actual parameter substitutions $\beta_i=\alpha_i+2$. **Context:** `README.md`, recomputable calculations — supplies two complete low-dimensional examples.
<!-- context-query: calcul;continuant;enumerat -->

### N069.2 — The first exponent reading has a measurable residual

**72/069, “$2+\unsure{\alpha_1^2|\alpha_1}$”; kind: reading question.** The first reading differs from the neighbouring underbrace $\beta_1$ by $\alpha_1^2-\alpha_1$, and the computed norm differs from the displayed norm by $(\alpha_0+2)(\alpha_1^2-\alpha_1)^2$. At $(\alpha_0,\alpha_1)=(0,2)$ the first-reading vector has norm $8$ while the written norm is $0$, as the script reports. **Context:** `README.md`, calculation brief — gives exact evidence for the already marked alternative without changing their order in the transcription.
<!-- context-query: calcul;quadratic;enumerat -->

### N071.1 — The centred coordinate map is an equivariant isomorphism

**72/071, “$p_\lambda$”; kind: unpursued implication.** On the stated localization at $\rho$, the map $x\mapsto(\pi(x)w/\rho,\ x-\pi(x)w/\rho)$ has addition as inverse and intertwines every recorded generator. Restriction to the affine hyperplane $\pi(x)=\lambda$ followed by division by its unit $\lambda$ gives the page's projection formula. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** and **Hua, findings register, 72-invariant-subspaces-string** — supplies the exact morphism relating the centre geometry, automorphisms and the later invariant-space data.
<!-- context-query: 72-invariant-subspaces-string;72-automorphisms-deform-gm-to-ga;centre -->

### N071.2 — The translated-vertex line has a later explicit comparison

**72/071 and 078, “$\widetilde s_i$”; kind: reading question.** The frozen 071 line subtracts $\rho^{-1}(a_0+\cdots+a_{i-1})$, whereas the definitions $\widetilde s_i=s_i-c$ and $s_i-s_0=a_0+\cdots+a_{i-1}$ give a plus sign with coefficient $1$, which is written on 078. The script prints the exact vector residual and the two source formulas remain unchanged. **Context:** `README.md`, calculation brief — supplies an explicit map between the earlier and later coordinate expressions.
<!-- context-query: calcul;centre;continuant -->

### N071.3 — The dual centred coefficients require sign and scaling checks

**72/071, coefficient of $a_{n-1}$ and the final $\widetilde t_i$ display; kind: reading question.** The script expands the recorded definition $\widetilde t_i=-t_i/\beta-\Pi/\rho$ before comparing the subsequent signs and the final factor multiplying the tail sum. This provides exact residuals for the questionable equalities without repairing the frozen algebra in place. **Context:** `README.md`, calculation brief — adds source-specific coefficient checks tied to the cofactor identity.
<!-- context-query: calcul;continuant;linear -->

## Scans 073–081: definition, projective recovery, and invariant spaces

### N073.1 — The change of notation is explicitly announced

**72/073, “il n'y a plus de $a_{-1},a_{-1}^*$”; kind: reading question.** The old affine vertex is replaced by its translated representative in $V$, and the page explicitly identifies the new $s_0$ with the previous $\widetilde s_0$. The projection in N071.1 gives the exact map between these coordinate systems; the $n+i|n-i$ index and the final $\beta_n$ argument remain marked for comparison with that map and the continuant recurrence. **Context:** **Hua, findings register, 72-automorphisms-deform-gm-to-ga** and **Hua, findings register, 72-invariant-subspaces-string** — identifies the coordinate change needed for later formula comparisons.
<!-- context-query: 72-invariant-subspaces-string;72-automorphisms-deform-gm-to-ga;centre -->

### N073.2 — The invariant-form statement includes zero and has a canonical coefficient map

**72/073, deleted “torseur” and surviving “Module … rg $1$”; kind: withdrawn in the same text.** A08 proves that evaluation at $a_0$ identifies the invariant-form module with the coefficient ring on the finite-centre chart, with inverse $r\mapsto r f_V$. The bases of this module are exactly the images of units under that same map, giving the explicit scaling action relevant to the crossed-out torsor language. **Context:** `README.md`, ring/quadric definition brief and **Hua, findings register, 72-automorphisms-deform-gm-to-ga** — verifies the surviving module assertion in its stated chart.
<!-- context-query: ring;quadratic;72-automorphisms-deform-gm-to-ga -->

### N074.1 — Condition 3 conflicts with the later unit pairing

**72/074, “$L_i\subset H_{i+1}$”; 72/076, “$h_i\notin H_{i+1}$”; kind: reading question.** The later normalization on 074 is $\langle a_i,a'_{i+1}\rangle=1$, which evaluates the proposed contained generator to $1$ rather than $0$. The explicit evaluation map $a'_{i+1}(a_i)=1$ therefore supplies a direct contradiction to the literal inclusion, and 076 states the corresponding non-incidence. **Context:** `README.md`, regular-polyhedron definition brief — identifies a specific condition that must be resolved before quoting the reformulation as a complete definition.
<!-- context-query: regular polyhedron;ring;pseudo -->

### N074.2 — Pinning is a sequence of specified duality maps

**72/074, “qui épingle la situation”; kind: unproved claim.** A base of $D_0$, its dual element in $L'_0$, and the rank-one operator determine $a_0$, after which the unit pairings propagate the choices along the chain. The definition section writes these actual evaluation and tensor maps, and the invariant-subspace construction supplies an explicit coordinate realization of them. **Context:** `README.md`, definition brief and **Hua, findings register, 72-invariant-subspaces-string** — adds the framing data absent from the truncated contextual statement.
<!-- context-query: regular polyhedron;72-invariant-subspaces-string;ring -->

### N075.1 — The discriminant and translated radius are computed separately

**72/075, “$B\rho\omega_V^{\otimes-2}$”; kind: unpursued implication.** The weighted product $B=\prod\beta_i^{n-i}$ and the continuant give the determinant in the displayed basis, while translation by the centre gives the positive radius value $\sigma'\rho'/\rho^2$ using the parity-normalized primes. The later calculation on 078 recomputes the same value, and the script records both the determinant and the translated norm. **Context:** `README.md`, quadrics calculation brief — verifies the concrete coefficient data supporting the circumscribed quadric.
<!-- context-query: quadric;continuant;calcul -->

### N075.2 — The smoothness adjective is deliberately changed

**72/075, “affine” deleted and “projectivement” inserted; kind: withdrawn in the same text.** The surviving condition concerns the projective closure of $f_V-\lambda=0$ and includes invertibility of $\sigma'$ in addition to the $\beta_i$. A proof must apply the homogeneous equation $f_V(v)-\lambda t^2$ and test its singular points, preserving the extra radius condition that the correction records. **Context:** `README.md`, quadrics brief — adds the precise formulation that survives the deletion.
<!-- context-query: quadric;quadratic;ring -->

### N075.3 — The implication question is explicit and unresolved on the sheet

**72/075, marginal “Cette condition entraîne celles des autres ?”; kind: self-flagged.** The wording remains doubtful, but its question mark is attached to the comparison of strict orthogonality and the preceding conditions. The page changes a proposed extra condition into “Ceci implique” and replaces $f|D_0$ by $f|L_0$, so a proof needs to state exactly which implication is intended. **Context:** `README.md`, definition/quadric brief — adds the author's own unresolved dependency question.
<!-- context-query: quadric;regular polyhedron;ring -->

### N075.4 — The final normalization on $D_0$ has a concrete obstruction

**72/075–076, “section $a_0$ de $D_0$ telle que $f_V(a_0)=1$” and “Rien n'empêche … $f_V(s_0)=0$”; kind: reading question.** In the explicit $n=2$, $\beta=(1,4)$ realization in the bridge section, $D_0$ is generated by $s_0=-E_{12}$ and $f_V=-\det$ vanishes on that whole line, so it has no section of value $1$. The earlier insertion $f|L_0$ on 075 and the following warning on 076 provide source-local comparison passages for this literal final sentence. **Context:** `README.md`, definition and B5/B12 questions — adds an explicit matrix obstruction and retains the written line name.
<!-- context-query: B5;B12;regular polyhedron;quadric -->

### N076.1 — The low-dimensional lift caveat is exhibited by two matrices

**72/076, “ne remonte pas de façon unique”; kind: unproved claim.** The matrices $\operatorname{diag}(1,-1)$ and $\operatorname{diag}(-1,1)$ give the same projective transformation in dimension two and are both reflection lifts over $\mathbf Q$. Calculation A16 explains the higher-dimensional unit-minor argument and its exact first-generator check on the finite-centre chart. **Context:** `README.md`, definition brief — supplies the explicit comparison behind the $n=1$ margin.
<!-- context-query: regular polyhedron;projective;linear -->

### N076.2 — The two recorded ambiguities have different explicit actions

**72/076, “groupe $\mu_2$” and “mod $\otimes L$”; kind: unpursued implication.** Scaling a normalized vector by $u$ changes its quadratic value by $u^2$, so the value-one choices carry the stated $\mu_2$ action, while tensoring the entire module by an invertible sheaf changes the linear lift of the projective bundle. The notes keep these actual operations and their descent data when stating the geometric definition. **Context:** `README.md`, definition and B12 brief — adds the two explicit transformations required in the reconstruction.
<!-- context-query: B12;ring;projective -->

### N077.1 — The categorical equivalence is stated without its descent proof

**72/077, “La catégorie … est équivalente”; kind: unproved claim.** The asserted equivalence includes $n\ge2$, a centre at finite distance and the three cited incidence conditions, with the original realization symbol still $\Pi_1|\Pi_n$. The supplied proofs establish the frame-to-centred morphism, scalar descent and invariant-form calculation, but the literal condition 3 on 074 and the earlier source definition still require explicit comparison before this exact categorical statement is promoted. **Context:** `README.md`, regular-polyhedron definition brief — supplies the manuscript's formulation and its remaining proof obligations; no supplied results ID settles the equivalence.
<!-- context-query: regular polyhedron;projective;ring -->

### N077.2 — The unique invariant hyperquadric is a further assertion

**72/077, “unique hyperquadrique fixe”; kind: unproved claim.** The note says that the hyperquadric is recoverable even without including it in the initial triple. A08 proves the invariant quadratic-module line in the finite-centre reflection frame and provides the map to its scalar classes, while the initial conic doubt on 035 and the explicit rank bound remain relevant when comparing its scope. **Context:** `README.md`, quadrics brief — adds a later uniqueness assertion rather than erasing the earlier doubt.
<!-- context-query: conic;quadric;quadratic -->

### N078.1 — The centred norm calculation checks the earlier radius

**72/078, “$f_V(s'_0)=\rho'\sigma'$”; kind: unpursued implication.** The source expands $f(s_0-o)$, uses the two parity identities, and rescales by $s'_0=-\rho\widetilde s_0$; the script reproduces each step. This gives an explicit comparison between the affine radius, the rescaled vector norm and the earlier value $f(\widetilde o)$, with the source's raised $\sigma$ mark still uncertain. **Context:** `README.md`, calculation brief — adds a later verification of the centred formula.
<!-- context-query: calcul;quadratic;continuant -->

### N078.2 — The edge-sum homothety requires a stated square-root extension

**72/078, “$\lambda=2\sqrt{\cdots}$”; kind: unproved claim.** The preceding norm equation is polynomial and the script verifies the edge-sum value, whereas the final radical notation presupposes a chosen solution of its quadratic equation and uses the displayed denominators. A concrete algebraic version is the base change adjoining a root of that equation after the required denominator localizations, together with the scaling map $v\mapsto\lambda v$; this records the actual operation without asserting a root in every starting ring. **Context:** `README.md`, regular-polyhedra-over-rings brief — identifies the extra base-change data in the final formula.
<!-- context-query: ring;regular polyhedron;quadratic -->

### N080–081 — The invariant-space theorem, counts, exceptions and replacement paragraph

**72/080–081, “sont ils distincts ?” and “au plus $2(n+2)$”; kinds: unproved claim, self-flagged, reading question and withdrawn in the same text.** Items IS01–IS12 give the separate one-item notes, exact two-flag proof, full finite enumeration and the characteristic-two counterexample to the literal minimum criterion. They also record the changed labels, the vertical-arrow condition, the valid finite-centre noncontainment and the cancelled irreducibility formulation replaced by a correspondence ending “Les deux”. **Context:** **Hua, findings register, 72-invariant-subspaces-string** — supports the classification in the explicit frame and adds its exact count and source-local qualifications.
<!-- context-query: 72-invariant-subspaces-string;invariant;characteristic -->
