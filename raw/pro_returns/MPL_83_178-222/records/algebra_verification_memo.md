# Algebraic verification of the frozen transcription

## Status and scope

These are independent calculations made after the transcription freeze and after reading `context/README.md` and `context/notes/RESULTS_STATE.md`. They do not change any page file or the combined TeX. `verify_algebra.py`, in this directory, reproduces the polynomial identities, determinant calculations, ranks, and Smith normal forms; `algebra_verification.json` records the results and source hashes. The mathematical arguments about generic fields below are separate from the computer checks.

The inputs are the formulas in the frozen transcription, not new readings of the images. In particular, the scan219 matrix calculation uses the first reading **−1** for its uncertain upper-left entry; the scan211 calculation uses its displayed matrix, without silently reconciling preceding prose or diagrams. Distinct occurrences of the manuscript's `Δ`, and the `Δ` character in the research register, are not identified.

No status in `RESULTS_STATE.md` is changed. The supplied register has no result row settling these particular trace-polynomial, cube-lattice, or λ-extension calculations. **WG H5** is a thematic connection through trace coordinates for `PSL₂(F_q)`, not a deduction about the GT action. **LM4 F.7**, **LM4_SUCCESSOR B.39/B.41**, and **EXIT_TOWER E.49** concern substantially different profinite questions; nothing here proves, refutes, or re-reviews them.

## 1. The product of the two triple traces

Use the manuscript's scan184 notation:

\[
b=\operatorname{Tr}X,\quad b'=\operatorname{Tr}Y,\quad b''=\operatorname{Tr}Z,
\qquad c=\det X,\quad c'=\det Y,\quad c''=\det Z,
\]
\[
t=\operatorname{Tr}YZ,\quad t'=\operatorname{Tr}ZX,\quad t''=\operatorname{Tr}XY,
\quad \tau=\operatorname{Tr}XYZ,\quad \tau'=\operatorname{Tr}YXZ.
\]

Let `Π₀` denote exactly the displayed polynomial on scan189, without adding anything to the transcription. Direct expansion in the twelve independent entries of three generic matrices gives

\[
\tau+\tau'=bt+b't'+b''t''-bb'b''=\Sigma,
\qquad \boxed{\tau\tau'=\Pi_0-4cc'c''.}
\]

Thus the corrected polynomial, used only in these notes, is

\[
\Pi_* = tt't''+ct^2+c't'^2+c''t''^2
+b^2c'c''+b'^2c''c+b''^2cc'
-b'b''ct-b''bc't'-bb'c''t''-4cc'c''.
\]

For `X=Y=Z=I₂`, the six trace quantities all equal2, the three determinants equal1, `τ=τ′=2`, `Σ=4`, and `Π₀=8`, whereas `ττ′=Π*=4`. This is a counterexample over the integers or rationals, with no uncertain subscript involved. With the formal scan188 Gram matrix `G₄`, independent of a matrix substitution, the script also verifies

\[
\Sigma^2-\det G_4-4\Pi_0=-16cc'c''.
\]

These are integer polynomial identities, so the corrected identities hold for matrices over **every commutative ring**, including rings with2-torsion. They also descend to rank4 Azumaya algebras using reduced trace and norm, because those algebras are faithfully flat locally matrix algebras. This reasoning does not divide by4 in the coefficient ring.

The exact error is `4cc′c″`, not simply the condition `cc′c″≠0`. Hua's modernised reading of cote83, XII, “Trois variables (pages182 à191),” explicitly supplies the same missing term, but its footnote's unrestricted phrase about failure whenever `cc′c″≠0` needs qualification over2-torsion bases: over `F₂`, the identity-matrix example has determinant product1 and the error nevertheless vanishes. Scan205 repeats the missing-constant problem in its vertex polynomial, although several of that page's other subscripts remain uncertain; the uniform identity-matrix specialization makes all those determinant subscripts1 and still detects the same error in characteristic0.

The unspecified `π_a` on scan207 can be supplied **as a research construction** by substituting `X_i,X_j,X_kX_l` into `Π*`: its norm variables are `c_i,c_j,c_kc_l`, its trace variables are `b_i,b_j,t_kl`, and its pair traces are `T_jkl,T_kli,t_ij`. In particular, its constant norm term is `−4c_ic_jc_kc_l`. This supplies a testable candidate for the unfinished expression, not text for insertion into the manuscript.

## 2. Normalization, reversal, and characteristic2

Fix the matrix basis

\[
e_0=E_{11}\wedge E_{22}\wedge E_{21}\wedge E_{12}.
\]

The script proves the integral identity

\[
\frac{1\wedge X\wedge Y\wedge Z}{e_0}
=\operatorname{Tr}([X,Y]Z)=\tau-\tau'.
\]

For the determinant polar form `φ(U,V)=Tr(U)Tr(V)−Tr(UV)`, the Gram determinant in this basis is1; consequently the square of this volume is exactly the determinant of the scan188 Gram matrix. Taking `X=E₂₁`, `Y=E₁₂`, and `Z=[X,Y]=diag(−1,1)` gives `τ=1`, `τ′=−1`, volume2, and `Tr([X,Y]Z)=2`. Thus the first-reading factor `1/2` on scan185 is incompatible with this normalization, while scan188's `4ττ′=Σ²−Δ²` and scan189's `τ−τ′=ε₀Δ` have the correct magnitude. The opening `τ′−τ=Tr([X,Y]Z)` on scan186 reverses the already fixed names: it compares−2 with+2 on the same example.

The chosen scan186 example has volume2, so it is a basis test only when2 is invertible; in characteristic2 it becomes dependent. A unit-volume test is instead `E₂₁,E₁₂,E₁₁`, for which both the volume and the commutator trace are−1. The latter is an independent calculation, not a replacement for his example.

There is also a genuine boundary to reconstruction from `det,1,e` when `e` means only ordinary top exterior volume. The adjugate map

\[
\iota(X)=\operatorname{Tr}(X)I-X
\]

fixes1, preserves determinant, and has linear determinant−1 on `M₂`. In characteristic2 it therefore preserves `e₀`, but it is not multiplicative:

\[
\iota(E_{12})\iota(E_{21})=E_{11},\qquad
\iota(E_{12}E_{21})=E_{22}.
\]

Hence the data `det,1,e₀` alone cannot recover the product uniquely over `F₂`: an automorphism of those data need not preserve multiplication. This statement concerns ordinary volume orientation, and makes no claim about additional component or quadratic-refinement data.

Finally, the pairing `Tr(UV)` itself is not degenerate on `M₂(F₂)`: its Gram matrix in the above basis is

\[
\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},
\qquad\det=-1.
\]

This corrects the contrary sentence in Hua, IX, “Le critère (pages92 à99),” footnote at lines1285–1298 of the supplied file. Scan183's use of the nondegenerate trace pairing is compatible with this calculation; one must distinguish this pairing from the restriction to the traceless subspace, which does behave differently at2.

## 3. Three matrices: identity versus a presentation theorem

The computations prove `τ²−Στ+Π*=0` universally, but a polynomial identity alone does not prove that it generates the entire relation ideal or that invariants commute with arbitrary base change. No arbitrary-base invariant-ring theorem has been verified here.

For an algebraically closed field, a supplied generator theorem saying that the three-matrix invariant ring is generated by the nine scalar/pair invariants and `τ` would complete a short argument: its quotient has dimension9, `τ` is algebraic over the nine-generator subring, so those nine generators are algebraically independent; simultaneous transpose fixes them and exchanges `τ` with `τ′`, generically nontrivially. Thus the quadratic has degree2 in the generic field, and the monic quadratic presentation follows from the generator theorem. Here invariants mean invariants of the algebraic group acting by simultaneous conjugation, not merely invariants under the possibly finite group of rational points.

A separate primary-source lead used in the main notes is Kaygorodov–Lopatin–Popov, `https://arxiv.org/pdf/1711.06889`, §1.2 and §3 Lemma3.1; generator assertions from that paper are not conclusions of this script. Hua XII also recognizes the characteristic-zero presentation while explicitly leaving the arbitrary-base assertion unchecked. A claim over an arbitrary commutative base still needs its own invariant-formation/base-change argument.

Conditional on `B=A⊕Aτ` with the corrected quadratic relation, the scan192 obstruction is exact:

\[
A[\tau-\tau']=A[2\tau-\Sigma]=A+2A\tau,
\qquad B/A[\tau-\tau']\simeq A/2A.
\]

The displayed quotient is a quotient of `A`-modules, not a quotient ring. Indeed `(τ−τ′)²=Σ²−4Π*` lies in `A`, so every polynomial in that difference reduces to degree at most1. This proves the proposed change of generator requires2 to be invertible in this presentation; it does not assume the presentation has already been proved over all bases.

## 4. Four matrices: the Gram relation and generic degree2

Work first over an algebraically closed field of characteristic different from2. Write

\[
X_i=\frac{b_i}{2}I+Y_i,\qquad \operatorname{Tr}Y_i=0,
\quad g_{ij}=\operatorname{Tr}(Y_iY_j).
\]

The traceless space has dimension3 and a nondegenerate trace pairing. Its four-vector Gram matrix gives the relation anticipated on scan193:

\[
\boxed{\det H=0},\qquad
H_{ii}=b_i^2-4c_i,\quad H_{ij}=2t_{ij}-b_ib_j\quad(i\ne j),
\qquad H=2(g_{ij}).
\]

As a polynomial in fourteen **independent formal** variables, `detH` has **108 monomials** and integer coefficient content **16**. Its primitive polynomial `P=detH/16` has a nonzero reduction modulo2 with **60 monomials**. The script checks both the raw determinant identity and the primitive identity after substituting generic integer matrices; the latter also follows because that substitution ring is torsion-free. Thus the primitive identity remains meaningful at2, whereas the raw determinant matrix reduces to a rank1 matrix and its determinant says nothing there. This establishes a universal relation, not the entire integral kernel or an integral presentation.

For the generic-degree assertion, let `K₀` be the field generated by the `b_i,c_i,t_ij`. On the open set where `Y₁,Y₂,Y₃` form a basis, put `G=(g_ij)_{1≤i,j≤3}`, `h=(g₁₄,g₂₄,g₃₄)^t`, and `(r₁,r₂,r₃)^t=G⁻¹h`. Then

\[
Y_4=r_1Y_1+r_2Y_2+r_3Y_3,
\]

with every `r_i` in `K₀`. If `Ω_ijk=Tr([Y_i,Y_j]Y_k)`, multilinearity gives

\[
\Omega_{124}=r_3\Omega_{123},\quad
\Omega_{134}=-r_2\Omega_{123},\quad
\Omega_{234}=r_1\Omega_{123},
\qquad \Omega_{123}^2=-2\det G.
\]

All four triple-volume choices are therefore controlled by one quadratic parameter. Equivalently, the Gram data classify a spanning configuration up to the orthogonal group of the traceless3-space; simultaneous `PGL₂` conjugation gives the special orthogonal subgroup, leaving two orientations. Simultaneous transpose fixes `K₀` and negates the nonzero generic `Ω₁₂₃`, so those orientations do not coincide. The generic invariant field is consequently `K₀(Ω₁₂₃)` of degree **2**, under these field/open-set hypotheses.

This contradicts the scan194 presumption of a finite free **rank16** actual invariant ring over the scalar/pair subring: such a free ring would have generic degree16. It does not contradict that the *formal algebra obtained by adjoining four independent roots of four monic quadratics* is free of rank16; that larger algebra omits compatibility between the four orientations. No global freeness assertion for the actual ring is needed for this refutation.

For completeness, writing `α_i=b_i/2`, exact expansion verifies

\[
\operatorname{Tr}(X_1X_2X_3X_4)
=2\alpha_1\alpha_2\alpha_3\alpha_4
+\sum_{i<j}\!\Bigl(\prod_{\ell\notin\{i,j\}}\alpha_\ell\Bigr)g_{ij}
+\frac12\sum_{\ell=1}^4\alpha_\ell\Omega_{[4]\setminus\{\ell\}}
+\frac12(g_{12}g_{34}-g_{13}g_{24}+g_{14}g_{23}),
\]

where the remaining triple is in increasing order. Thus the degree-at-most8 construction around scans199–205 is a coarse upper bound in this characteristic range; it is not the generic minimal degree over `K₀`. This argument does not extend the same generator statement to characteristic2: the primitive Gram relation's survival there is not a substitute for the additional invariant-theoretic work.

## 5. Cube relations and integral lattices

The script uses the twelve equations exactly displayed on scan203, with variables ordered

`a,b,c,a′,b′,c′,AB′,BC′,CA′,AC′,CB′,BA′`.

| Map or matrix | Rank over Q | Smith diagonal over Z | Rank modulo2 |
|---|---:|---|---:|
| All twelve scan203 equations | 6 | `1,1,1,1,1,1,0,0,0,0,0,0` | 6 |
| First six equations | 6 | `1,1,1,1,1,2` | 5 |
| Last six equations | 5 | `1,1,1,1,1,0` | 5 |
| Six face values → twelve adjacent-face sums | 6 | `1,1,1,1,1,2` | 5 |
| Displayed scan211 matrix | 6 | `1,1,2,4,8,16` | 2 |
| Displayed scan219 block matrix, first reading−1 | 6 | `1,1,1,8,8,8` | 3 |
| Scan215 map `(δ,δ′,δ″)→(ε₁,ε₂,ε₃)` | 3 | `1,1,2` | 2 |

The last six scan203 equations have exactly one rational dependency, their sum, so the manuscript's observation that each follows from the other five is correct. All twelve have only six independent rational constraints. The first six alone have a row-lattice defect at2: their integer solution kernel agrees with the full kernel, but the implication to the remaining relations cannot be transported unchanged to arbitrary2-torsion rings.

The face-to-edge map is the **unoriented incidence map of the octahedral adjacency graph**, not the incidence map of the cube's own vertices. Its kernel over a commutative ring consists of constant face values killed by2; over `F₂` this is one-dimensional, while over `Z` the map is injective with a `Z/2` torsion summand in its cokernel. Thus Hua XIII's unqualified injectivity claim is valid in characteristic0 or over a2-torsion-free coefficient module, but not over every base.

There is a useful distinction between the written linear relations and actual integer face sums. Setting all twelve edge values equal1 satisfies all twelve written equations, but cannot arise from integer face values: the three edges of any adjacency triangle would sum to twice an integer and instead sum to3. In the six selected coordinates, the linear-relation lattice requires `a+b+c+a′+b′+c′` even, whereas actual integer face sums require both `a+b+c` and `a′+b′+c′` even. The extra obstruction is a single parity class.

The scan207 counts themselves are correct: `4+4+6+8+6=28` quantities, and `4×2+12×2=32` displayed vertex/edge relations. They are counts of equations, not of independent equations or a proof of a complete presentation. Already their linear face-sum part has the dependencies above; the uncorrected vertex products also retain the scan189 error.

The scan201 claim that each `Σ_a` depends only on edge direction fails for general matrix inputs. Define `Σ_(ij|kl)=Tr(X_iX_jX_kX_l)+Tr(X_jX_iX_kX_l)` by the two adjacent cyclic words specified in scans205–207. For `X₁=I`, `X₂=E₂₁`, `X₃=E₁₂`, `X₄=diag(−1,1)`, one gets `Σ_(12|34)=Tr1234+Tr2134=1+1=2`, whereas `Σ_(34|12)=Tr3412+Tr4312=1−1=0`. The complementary endpoint-label pairs12 and34 give parallel cube edges of the same direction, labelled by the unordered partition `12|34`; this specifies the mapping as well as the numerical values. The later twelve-variable treatment on scan203 does not retain the earlier three-value simplification, as Hua XII also observes.

## 6. The two displayed determinants and the sign/denominator questions

For the literal6×6 matrix on scan211, the four signed first-row cofactors are all256, giving

\[
\det N_{211}=1024=2^{10}.
\]

Its Smith form gives cokernel `Z/2⊕Z/4⊕Z/8⊕Z/16`. This verifies Hua XIII's determinant computation and adds the full integral obstruction. It does not reconcile the earlier edge-label formulas with the matrix: for example, scan209's `v=u−(d−b)` and the scan211 expansion involving `u+(d−b)` must not be silently treated as the same convention.

For scan219, with the first reading−1, set

\[
M=\begin{pmatrix}-1&2&2\\2&-1&2\\2&2&-1\end{pmatrix},
\qquad N_{219}=\begin{pmatrix}M&I\\I&M\end{pmatrix}.
\]

Here `detM=27` is correct, but `M²=9I`, so

\[
\det N_{219}=\det(M^2-I)=8^3=512,
\qquad N_{219}^{-1}=\frac18\begin{pmatrix}M&-I\\-I&M\end{pmatrix}.
\]

Replacing a matrix block by its determinant before taking the2×2 determinant is the invalid step producing728. The conclusions “nonzero” and “prime to3” survive, but7 and13 are not bad primes for this map; its cokernel is `(Z/8)^3` and it becomes invertible after inverting2. If the uncertain upper-left entry alone were `+1` instead, the determinant would be384; the reported512 is explicitly conditional on the frozen first reading.

Scan215's final system has matrix

\[
\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix},
\]

of determinant2. Its half-sum formulas are correct over `Z[1/2]`; over `Z` they have solutions exactly when `ε₁+ε₂+ε₃` is even, and those solutions are unique; over `F₂` consistency requires that sum to be0 and a one-dimensional family of solutions remains. Over a general ring, the exact obstruction is the corresponding class in `k/2k`, with ambiguity in `k[2]` when a solution exists.

The solved formulas on213 and the final system on215 consistently make the earlier scan213 chain equal **−δ″**, although the chain's right endpoint is written `=δ″`. This is a whole-chain sign discrepancy, not grounds to change only the displayed formula for `γ`. Likewise the scan217 expressions are conditional on its marked signs/subscripts: the integral linear system predicts `b+b′` and `c′−c` in the corresponding slots, while the frozen first readings contain their marked alternatives; this is a research reading question, not a correction of the transcription.

On scan221, changing from each pair `(a,a′)` to its sum and difference uses matrix `[[1,1],[-1,1]]` of determinant2. Thus the three-pair change has an index8 image lattice over the integers and loses three dimensions in characteristic2. The summed identity `φ_a+φ_a′=2(μ+ν)` is valid for the scan219 first-reading system, but it is not an invertible recovery formula at2.

## 7. The λ-split extension unit question

This is conditional on the usual morphisms of extensions preserving the injection, quotient, and λ-retraction; a chosen splitting is not treated as part of the structure. Define

\[
E_\beta=(k\oplus k,\ i(a)=(a,0),\ q(a,b)=b,\ u_\beta(a,b)=\lambda a+\beta b).
\]

The shear `φ_c(a,b)=(a+cb,b)` is an isomorphism

\[
\phi_c:E_{\beta+\lambda c}\longrightarrow E_\beta,
\qquad u_\beta\phi_c=u_{\beta+\lambda c}.
\]

The split-product formula recorded on scan180 gives `E_β *_λ E_γ ≅ E_{βγ}`. A direct compatible coupling is

\[
((a,b),(d,e))\longmapsto
(\lambda ad+\gamma ae+\beta bd,\ be),
\]

whose target λ-retraction is the product of the two source retractions. Consequently the isomorphism classes of these framed split extensions form the multiplicative monoid of `k/(λ)`, and their invertible classes are `(k/(λ))^×`: the unit condition is `(β,λ)=k`. This is the criterion already suggested by scan181's intrinsic surjectivity condition.

The simplest counterexample to “iff β is a unit in k” is `λ=1,β=0`: `φ₁:E₁→E₀` is an isomorphism. An equally concrete example over `Z` at the involution-relevant value `λ=2` is `φ₁:E₃→E₁`;3 is not a unit of `Z`, but the two objects are isomorphic. These arguments use the product/unit structure posited by the manuscript and do not finish its separate coherence checks. If a splitting were rigidly included in the category, the shear would be forbidden, so the precise category remains the relevant clarification; Hua XI repeats both statements without resolving this issue.

## 8. Context concordance

| Current material | Exact supplied context | Relationship and limits |
|---|---|---|
| Scans183–192, triple traces and corrected product | Hua, modernised reading of cote83, XII, “Trois variables (pages182 à191),” lines1765–1834 | Hua already supplies `−4cc′c″`, the normalization/reversal observations, and a characteristic-zero scope qualification. Independent identities and counterexamples here confirm these, while adding the2-torsion qualification and ordinary-volume obstruction. |
| Scans193–207, four variables | Hua XII, “Quatre variables, et le cube (pages191 à200),” lines1837–1867; XIII, “Variables et relations (pages202 à206),” lines1877–1905 | Hua describes the freeness presumption and cube bookkeeping without proving the rank16 claim. The generic degree2 argument and primitive integral Gram relation are additions here. |
| Scans203,211–221, cube linear algebra | Hua XIII, “Les relations linéaires entre les Σ_a (pages202,208 à220),” lines1908–1944 | Determinants512 and1024 are already Hua's calculations. Smith forms, parity lattices, and the characteristic2 correction to the incidence injectivity claim are additional checks. |
| Scans180–181, λ-retractions | Hua XI, “Extensions λ-scindées (pages171 à180),” lines1719–1756 | Confirms the intended λ-retraction model, but repeats rather than resolves the two unit criteria. The shear counterexamples are an additional conditional objection. |
| Rank4 Azumaya setup and matrix descent | `LM_140-3_text.tex`, scan258, formula(9), continuing259; scan267–268, equations(32)–(35); scan290, “Un épinglage canonique” | The LM source identifies rank4 Azumaya algebras as fppf forms of `M₂`, relates them to forms of `GL₂,SL₂,GP(1)`, and uses trace/norm equations. It supplies a structural comparison, not the local three-/four-matrix presentation proved here. |
| Why characteristic2 qualifications matter | `LM_140-2_text.tex`, scan245, exact sequence `1→μ₂→SL₂→GP(1)→1` and its lifting gerbe; scan250, unfinished fixed-degree Azumaya2-category remarks | A related quadratic/descent setting, without identifying its gerbe with the present cube parity classes. No result on GT parity or the profinite centralizer follows. |
| Trace coordinates over finite fields | `notes/RESULTS_STATE.md`, **WG H5**, under “Questions of our planning document” | A planning hunch, unchecked: the corrected trace identity is relevant background for determinant1 matrix coordinates. It supplies neither the hunch's GT/Galois comparison nor a centralizer calculation. |

## 9. Candidate short notes for the main research file

Each item below is deliberately separate, with one to four sentences of note text; the longer arguments above supply the details. Registry comments are not proposed changes of status.

### V01 — 83/183; own idea; “det,1 ... e”

Over `F₂`, adjugation fixes1, determinant, and ordinary top exterior volume, but `adj(E₁₂)adj(E₂₁)=E₁₁≠E₂₂=adj(E₁₂E₂₁)`, so those data do not determine multiplication without additional structure. Confidence is high because the matrix-unit witness is exact. This qualifies Hua XII's reconstruction discussion; no supplied registry row settles this local characteristic2 question.

### V02 — 83/185–186,188–189; withdrawn or revised normalization; “2(τ−τ′)=ε₀Δ”

The displayed matrix-unit triple gives volume2 and `τ−τ′=2`, confirming the later coefficient1 and refuting the first-reading coefficient1/2 in the scan188 polar-form normalization. Scan186 also interchanges the names in its opening `τ′−τ` equality. Hua XII records both issues; this verification confirms them without changing the frozen readings.

### V03 — 83/185,187–188; withdrawn in the same text; “ce qui est fâcheux !”

The attempt to use only traces and pair traces is explicitly abandoned when the determinant variables are reinstated. The Gram determinant on188 supplies an exact replacement, but the original scan186 test is not a basis test at2. Hua XII already identifies the withdrawal; this adds its base-ring limitation.

### V04 — 83/189,205; own verification of an unproved formula; “ττ′=Π”

The identity-matrix specialization gives the written polynomial8 but the product of traces4; the missing term is `−4cc′c″`, independently verified as an integer polynomial identity. Hua XII and XIII already supply this correction, so it is credited to that reading rather than claimed as new. Over a general ring the error vanishes exactly when `4cc′c″=0`, which is weaker than requiring a singular factor; **WG H5** is only a thematic trace-coordinate connection.

### V05 — 83/190–192; self-flagged; “À vérifier”

The corrected quadratic identity is universal, while the asserted invariant-ring presentation over arbitrary bases requires a separate generation and base-change theorem. Under the field generator theorem and a nontrivial transpose involution, the quadratic presentation follows, but this memo does not promote that argument to every commutative base. Hua XII makes the same characteristic-zero versus arbitrary-base distinction.

### V06 — 83/192; unpursued implication; “cas seulement”

Conditional on the stated quadratic free presentation, `A[τ−τ′]=A+2Aτ` and its quotient in `B` is `A/2A`, giving an exact explanation for the obstruction at2. Confidence is high under that explicit hypothesis. This sharpens Hua XII's observation without proving the unverified arbitrary-base presentation itself.

### V07 — 83/193–194; own idea; “il doit y avoir ... une relation”

The relation is supplied in characteristic different from2 by the four-vector Gram determinant with diagonal `b_i²−4c_i` and off-diagonal `2t_ij−b_ib_j`. Its determinant has content16; the primitive polynomial has108 terms and a nonzero60-term reduction modulo2. Confidence is high from exact expansion, but neither the whole integral kernel nor an invariant-base-change theorem is claimed; Hua XII leaves the relation unstated.

### V08 — 83/194; conjecture refuted generically; “je présume ... rang 2⁴”

On the nondegenerate three-vector Gram open set over an algebraically closed field of characteristic different from2, every triple volume is a Gram-rational multiple of one volume. Transpose exchanges the two orientations, so the generic invariant-field degree over the scalar/pair field is2, contradicting rank16 for the actual invariant ring. This adds a generic refutation to Hua XII's report of the presumption, without asserting global freeness or characteristic2 generation.

### V09 — 83/199–205; unpursued implication; degree8 sketches

After inverting2, direct expansion expresses each four-letter trace through scalar/pair data and the common triple-volume parameter. Thus degree at most8 is a valid coarse bound but not the generic minimal field degree in that setting. Confidence is high from the exact expansion and the Gram argument; fixed rings under the separate permutation group are not being conflated with the conjugation-invariant base.

### V10 — 83/201,203; withdrawn in the same text; “trois valeurs”

For `I,E₂₁,E₁₂,diag(−1,1)`, the adjacent-word sums `Σ_(12|34)=Tr1234+Tr2134=2` and `Σ_(34|12)=Tr3412+Tr4312=0` belong to the same cube direction, the partition `12|34`. Thus the claimed dependence only on direction is not a universal matrix identity, and scan203's twelve quantities no longer use that simplification. Hua XII already flags the abandonment; the explicitly labelled witness adds an exact check.

### V11 — 83/203; unpursued implication; “six dernières relations”

The last six relations have rank5 and sum to zero, while the full twelve-equation system has rank6, confirming the stated dependency. The first six alone have Smith invariant2, so their implications need care on2-torsion bases. This refines the rational relation count in Hua XIII; no profinite parity conclusion follows.

### V12 — 83/203,207; own idea; adjacent-face sums

The octahedral face-to-edge sum map has Smith form `(1,1,1,1,1,2)`, and its kernel over a ring is the constant vector valued in the ring's2-torsion. Consequently Hua XIII's unqualified injectivity fails in characteristic2. The all-one integer edge vector satisfies the written linear relations but is not an integer face-sum vector, exposing the additional parity obstruction; confidence is high from the exact incidence matrix.

### V13 — 83/205,207; unproved presentation; “28 variables ... 32 relations”

The counts are arithmetically correct, but the listed equations have substantial dependencies and do not alone establish a presentation. The unfinished edge-product expression can be tested by substituting `X_i,X_j,X_kX_l` into the corrected triple polynomial. Hua XIII records the same bookkeeping without a completeness proof.

### V14 — 83/211; own verification; displayed determinant

The literal displayed matrix has determinant1024 and Smith form `(1,1,2,4,8,16)`, so its integral cokernel is `Z/2⊕Z/4⊕Z/8⊕Z/16`. Hua XIII already computes1024; the Smith form adds the precise obstruction. This calculation does not silently reconcile the sign conventions of209 with the preceding formulas on211.

### V15 — 83/213,215,217; reading question; common difference `δ″`

The solved formulas and the final system make every term of the preceding scan213 difference chain equal `−δ″`, whereas its endpoint is written `δ″`. Changing only `γ` would therefore break the later consistent system. This is a post-freeze sign-normalization question, with the uncertain scan217 entries still retained as uncertain.

### V16 — 83/215,217; unpursued implication; half-sum formulas

The final three-difference system has determinant2: over the integers its exact solvability condition is `ε₁+ε₂+ε₃` even, and in characteristic2 a one-dimensional ambiguity remains. Confidence is high for that final written system, independently of scan213's preceding sign discrepancy. Hua XIII notes the need to invert2, and the present Smith calculation supplies the sharper lattice statement.

### V17 — 83/219; own verification; “728 ... premier à3”

With the frozen first reading−1, the block matrix has `M²=9I`, determinant512, and Smith form `(1,1,1,8,8,8)`. Hua XIII already corrects728 to512; this independently verifies the correction and shows that only2, not7 or13, obstructs invertibility. The conclusions nonzero and prime to3 survive, while the uncertain entry remains explicitly a condition of the calculation.

### V18 — 83/221; unpursued implication; “λ,μ,ν”

Replacing each opposite pair by its sum and difference has determinant2 per pair, so the three-pair coordinate change has index8 over the integers and loses information in characteristic2. The final identity `φ_a+φ_a′=2(μ+ν)` is compatible with the first-reading scan219 system but cannot be inverted at2. This extends Hua XIII's closing observation without identifying these parity classes with **LM7_PUSH E.65** or any other GT character.

### V19 — 83/180–181; own conditional counterexample; “ssi β est inversible”

Under ordinary λ-extension morphisms, the shear `φ_c(a,b)=(a+cb,b)` identifies `E_{β+λc}` with `E_β`, so invertibility depends on `β modλ`, equivalently `(β,λ)=k`, as the later intrinsic criterion suggests. For `λ=2` over `Z`, `E₃≅E₁` although3 is not a unit. Confidence is high for this category model; Hua XI repeats the conflicting criteria, and a category with a rigidly chosen splitting would require a separate statement.

### V20 — 83/183; context correction; nondegenerate trace pairing

The pairing `Tr(UV)` has determinant−1 on the matrix-unit basis over every field, including `F₂`. Thus Hua IX's sentence claiming this full trace pairing is degenerate in characteristic2 is false as stated. This supports the use of nondegeneracy on scan183, while leaving the separate characteristic2 orientation obstruction in V01 intact.
