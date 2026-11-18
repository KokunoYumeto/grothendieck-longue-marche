# S20 and Michel Hua comparison: research-only contribution

**Boundary.** This contribution began after the transcription freeze at 2026-11-17 23:29:03 UTC and context opening at 23:29:08 UTC. No manuscript image was viewed and no transcription or doubt was changed; manuscript quotations below come from the frozen pages/MPL_64_116-157_64_scanNNN.tex. Michel Hua's project's whole hua_project/64.modern.tex was read, not merely the excerpt in notes/RESULTS_STATE.md; it describes itself as an interpretation with modernized notation and mathematical repairs, not a diplomatic transcription.

**Locators and status.** Context paths below are relative to MPL_64_116-157_context/. In the supplied selection, Hua's page number is the current scan number minus one: his pages 117, 138, 150, 154 correspond respectively to scans 118, 139, 151, 155; this convention is not asserted for other cotes. The prior-results register states that returned-package notes are first-pass leads, and its MPL_93_002-046 P09/E14/E16/C29 entries are not listed among the independently refereed claims. No full cote-93 or cote-159 transcription or notes file is present in the supplied context: the catalogue descriptions in SECTIONS_STATE.md and summaries in notes/RESULTS_STATE.md cannot substitute for those texts.

## S. The S20 connection hypothesis

### S01 — Scans 143–145, “un système local H” and “τ = z₂/z₁” — own idea

These pages supply a rank-two integral local system and a holomorphic period ratio, but the frozen selection contains no occurrence of Gauss–Manin, Cartier, Picard–Fuchs, Hasse–Witt, connection/connexion, Schwarzian, p-curvature, or \nabla, and its displayed constructions do not identify any such operator. **Comparison: adds analytic input** to the future-comparison programme **MPL_93_002-046 P09** in notes/RESULTS_STATE.md, “Orientation for this package” and the P09 register row, while README.md S20 and SECTIONS_STATE.md, entries for cotes 93 and 159, remain research leads. **Verdict on S20: not addressed as an explicit authorial connection in these scans; neither historically confirmed nor refuted**, since the required cote-93 and cote-159 texts are absent. **Our confidence: high** for this bounded textual finding, because it rests on the frozen text and an exact-term search, but insufficient evidence for an assertion about Grothendieck's wider unpublished programme.

### S02 — Scan 151, “une base φ de t_E” — unpursued implication

The stated “rigidification différentielle” is a nonzero tangent vector, hence dually a normalization of an invariant one-form; it is not the specification of a connection on a vector bundle (Hain, 2014, Proposition 5.16). **Comparison: restates the object identified by Hua, modernised reading of cote 64**, “Approche transcendante — seconde mouture,” subheading “La rigidification différentielle (pages 150 et 151),” and **adds a necessary distinction** to **MPL_93_002-046 P09**. A connection obtained from the local system on scan 143 acts on a rank-two bundle, whereas the frame on scan 151 concerns a line, so the adjective “différentielle” alone supplies no Cartier or p-curvature evidence. The tangent/Hodge duality is used as published background with its hypotheses checked, not as a new result of this run.

### S03 — Scans 118 and 143–144, “épinglage de Legendre” and “τ = z₂/z₁” — own idea

A concrete modern comparison is to introduce a separate Legendre parameter \(u\), take \(y^2=x(x-1)(x-u)\), and compare the manuscript's period ratio with the ratio of independent period solutions of \(u(1-u)f''+(1-2u)f'-f/4=0\) (Katz, 1968, pp. 71–74). On a one-dimensional base where the period map is locally univalent, this gives the projective datum \(\{\tau,u\}=(u^2-u+1)/(2u^2(u-1)^2)\), with \(\{\tau,u\}=\tau'''/\tau'-3(\tau''/\tau')^2/2\). **Comparison: adds an explicit candidate calculation** to **MPL_93_002-046 P09**, and makes README.md S20 testable against cote 159; it does not identify the absent cote-159 connection or attribute this equation to the present pages. **Our confidence: high** for the mathematical calculation, because the exact-differential identity and Schwarzian simplification are checked in Certificate C1 in research/connections_hua.md; the historical identification remains untested.

### S04 — Scan 143, “loc libres de rang 2” — own idea

For a smooth proper elliptic family over a scheme S smooth over a field of characteristic \(p\), the relevant Gauss–Manin p-curvature is \(\psi(D)=\nabla_D^p-\nabla_{D^{[p]}}\); nilpotence of exponent at most two is the applicable general phenomenon, whereas Cartier descent requires **zero** p-curvature (Katz, 1970, Theorem 5.1 and §§7.4–7.5). A Hasse–Witt map, a Cartier operator on forms, and this p-curvature endomorphism therefore require separate definitions and comparison maps. **Comparison: adds a mathematical constraint** to **MPL_93_002-046 P09** and the thematic description of cote 93 in SECTIONS_STATE.md, rather than treating “Cartier” and “p-curvature” as interchangeable names. **Our confidence: high** in this distinction from the cited results, but it supplies no evidence that Grothendieck makes the proposed comparison in these scans.

### S05 — Scans 143–144, “τ = z₂/z₁” — own idea

For the Legendre Picard–Fuchs equation introduced in S03, take the **period/solution companion** connection \(\nabla_\partial=\partial-A\), where \(A=\begin{pmatrix}0&1\\1/(4u(1-u))&-(1-2u)/(u(1-u))\end{pmatrix}\), and reduce over \(\mathbb F_3[u,1/(u(u-1))]\). Direct calculation gives

\[
\psi(\partial)=\frac{1}{u^2(u-1)^2}
\begin{pmatrix}-(u+1)&(u+1)^2\\-1&u+1\end{pmatrix}\ne0,
\qquad \psi(\partial)^2=0,
\]

and at \(u=-1\), where the normalized Hasse polynomial \(1+u\) vanishes, the value of this p-curvature tensor on the parameter base is still nonzero (Katz, 1968, p. 74); the dual de Rham coefficient-column connection in the basis \((\omega,\nabla_\partial\omega)\) is \(\partial+A^T\), with p-curvature \(-\psi(\partial)^T\), so the nonzero square-zero conclusions are unchanged. **Comparison: adds a discriminating example** to **MPL_93_002-046 P09**: a future cote-93/159 comparison must distinguish supersingularity, zero p-curvature, and nilpotent p-curvature, rather than infer one from a shared vocabulary. **Our confidence: high** because Certificate C2 computes the connection and its square explicitly; this is our example, and neither this matrix nor a characteristic-three calculation occurs in the frozen pages.

### S06 — Scan 149, “revêtement universel de M₁,₁” — own idea

The stated target here is the elliptic **moduli problem**, whereas a projective connection might instead live on an individual elliptic curve, on a different curve, or on the parameter base of a family. The Schwarzian in S03 lives on the Legendre parameter base; it must not be identified solely by the word “uniformization” with the affine projective charts of an individual quotient \(\mathbb C/H\). **Comparison: adds a domain-of-definition test** to **MPL_93_002-046 P09**, README.md S20, and the catalogue-only description of cote 159 in SECTIONS_STATE.md: a future comparison must specify the curve/base, bundle, rank, and integral model before comparing its reduction and p-curvature. **Our confidence: high** in this necessary distinction, because scan 149 explicitly names the moduli target, but the absent cote 159 text prevents determining which object its connections concern.

### Q3 — Summary of the S20 assessment

The selected pages establish the analytic period and lattice side needed for a possible connection, but do not themselves state the Gauss–Manin/Cartier/projective-connection/p-curvature identification. S03–S06 provide a precise modern comparison to try, distinguishing a tangent frame, a rank-two connection, its projectivization, Hasse–Witt data, p-curvature, and the curve or moduli base on which each construction lives. S20 remains a historical conjecture pending the actual cote-93 and cote-159 texts; the available P09 summary is a programme, not an established result.

## H. Comparison with Michel Hua's whole modernised reading

### H01 — Scans 121 and 126, “Dieu sait comment — il faudra … y revenir” and “t correspond donc à” — self-flagged

The frozen pages **support and restate** Hua, modernised reading of cote 64, “Vers l'épinglage de Legendre (pages 117 à 125),” in leaving condition c unfinished while computing the line represented by the cyclic differences in scan 126. Hua explicitly credits the attachment of the loose calculations to condition b as his project's inference, which should remain credited to that project rather than presented as a manuscript cross-reference. notes/RESULTS_STATE.md, “Cote 64: the opening of transcripts/64/64.modern.tex,” supplies only the broad pinning summary and no dedicated result ID; **MPL_93_002-046 P09** is a further comparison programme and does not fill this gap. The precise scalar/square relation in c is therefore not established merely by the later line calculation.

### H02 — Scans 141 and 151, “fibré principal associé” and “un réseau H ⊂ C” — own idea

**Hua's project adds**, in “Approche transcendante — seconde mouture,” footnote to “La rigidification différentielle,” the identification of lattice moduli with the complement of \(g_2^3=27g_3^2\) and hence with fundamental group \(B_3\), expressly marking this as its own remark; the frozen pages construct the frame space but do not state that conclusion. **Comparison: supplies an elliptic frame interpretation of the earlier claim** in LM_140-2_notes.md, items **467-5 and 467-7**, and LM_140-2_text.tex, scan 467, “une extension centrale … de SL(2,Z) par Z”; notes/RESULTS_STATE.md has no separate B3 result ID, and none of the open arithmetic-image IDs is settled by it. Hain (2014, Proposition 8.2, Corollary 8.3, Remark 8.4) independently supports the identification and specifies that the kernel of \(B_3\to\mathrm{SL}_2(\mathbb Z)\) is generated by the **square of the central full twist**, not by the full twist itself. **Our confidence: high** for this credited modern identification, from the published construction and the matrix check in Certificate C3; it is an unpursued implication here, not a newly found assertion in Grothendieck's text.

### H03 — Scans 139–140, “E_z = C/(Z·1 + Z·(−bar z))” and “de rang 1” — reading question

**Hua's project differs deliberately** from the frozen wording in “V. Approche transcendante — première mouture (pages 126 à 140)”: it replaces the first-draft family by the holomorphic model \(\mathbb C/(\mathbb Z+\mathbb Zz)\), and changes the stated abelianization rank from one to two while reporting both changes in footnotes. These are mathematical modernizations, not independent evidence that the frozen readings should be altered; the second draft on scans 143–145 supplies the manuscript's own later holomorphic period formulation. notes/RESULTS_STATE.md, “Orientation for this package,” names **EXIT_TOWER E.24** and **LM4_SUCCESSOR B.38** as open comparison targets, but neither their arithmetic-image question nor their congruence-kernel question is answered by these corrections. T04 and T08 supply the analytic-family and rank checks, respectively, without reopening the frozen transcription.

### H04 — Scan 155, “On suppose d'abord A …” — reading question

**Hua's project differs** in “VI. Appendice,” subheading “Normalité de B = A[S]/(S²−a) (page 154)”: it reads the hypothesis as “régulier” local and inserts dimension one, whereas the frozen transcription leaves the word unresolved as `\unsure{anneau jauge}`. Consequently its footnote's criticism of an omitted dimension hypothesis is not a verified criticism of the manuscript in this run: the intended local-ring term is itself a post-freeze reading question. The exact-term context search found this hypothesized reading only in Hua's text, and notes/RESULTS_STATE.md, “Orientation for this package,” explicitly names no prior result to use for these scans; there is no matching normality result ID to cite. This difference is recorded for a later independent image audit, with the frozen text unchanged.

### H05 — Scans 152–153, the deleted “M₁,₂!” and “normalité des ext. quadratiques” — reading question

**Hua's project differs** in its footnote to “La rigidification différentielle (pages 150 et 151),” which reports a boxed “M₁,₁!” at the end and calls its page 152 blank, while current frozen scan 152 ends with deleted \(M_{1,2}^{!}\) and scan 153 is a titled quadratic-extension cover. These differences concern the identification and extent of the source text, so neither Hua's modernized moduli interpretation nor its page inventory resolves the present reading. notes/RESULTS_STATE.md, “Cote 64: the opening of transcripts/64/64.modern.tex,” contains no detailed assertion about these leaves and no corresponding result ID. The differing subscript and treatment of the cover belong in the post-freeze reading questions, not in a silent correction.

### H06 — Scan 156, “λ = 2^α3^β l'invariant modulaire exceptionnel” — own idea

**Hua's project adds an interpretation**, in “VI. Appendice,” subheading “Exemple”: it identifies this value with 1728 and interprets the example as a double cover of the j-line, while expressly acknowledging that the page does not name j. This is compatible with the earlier model's suggestions in LM_140-2_notes.md, **A14** at scan 535 and **B9** at scan 560, but those contextual claims do not determine the unnamed coordinate or exponents in the present frozen page. **Comparison: restates that earlier interpretive lead**, while **MPL_93_002-046 E14** and **P09** in notes/RESULTS_STATE.md still distinguish deformation/moduli questions from an established coarse-coordinate identification. **Our confidence: medium** for Hua's interpretation because the exceptional-value description and factorization fit it, but the scan leaves the exponents and coordinate implicit; it must not be imported as a resolved reading.

### H07 — Scan 118, “associer … canoniquement … un épinglage de Legendre” — own idea; optional upstream caveat

**Outside the current scan range**, Hua's modernised reading of cote 64, “II. Structures octaédrales dans P¹ — 1. Actions du groupe de Klein, configuration octaédrale (pages 43 à 52),” adds a characteristic-five exception for an **unpaired** six-point set, which must be credited to his project. In characteristic five, \(\{0,\infty,\pm1,\pm i\}=\mathbb P^1(\mathbb F_5)\) has 120 projective symmetries, whereas the subgroup preserving the three opposite pairs has 24, as independently checked in Certificate C4; the current scan's canonicity programme does not justify forgetting that extra structure. **Comparison: adds a distinction** to LM_140-2_notes.md, **C02**, scan 363, whose octahedral statement concerns the normalizer of the Klein group, and to the octahedron paragraph in notes/RESULTS_STATE.md, “Cote 64: the opening …,” which has no dedicated result ID. **Our confidence: high** in this finite-group distinction, but it is not an audit or correction of the unseen earlier manuscript pages and establishes no error in current scans 116–157.

## Reproducible mathematical certificates

These certificates check the labelled modern constructions above. They do not resolve handwriting, prove full earlier-run statements, or establish historical attribution.

### C1. Legendre exact differential and Schwarzian

Put \(q=x(x-1)(x-u)\), \(\omega=dx/y\) with \(y^2=q\), and \(R=x(x-1)/(2(x-u))\). Differentiating in u while holding x fixed gives

\[
\partial_u\omega=\frac{1}{2(x-u)}\omega,\qquad
\partial_u^2\omega=\frac{3}{4(x-u)^2}\omega,
\]
\[
\left(u(1-u)\partial_u^2+(1-2u)\partial_u-\tfrac14\right)\omega
=d_x(R/y).
\]

The last equality is the rational identity

\[
\frac{3u(1-u)}{4(x-u)^2}+\frac{1-2u}{2(x-u)}-\frac14
=R_x-\frac{R q_x}{2q}.
\]

Integrating over a locally transported closed cycle annihilates the right side and gives the stated Picard–Fuchs equation. For \(f''+Pf'+Qf=0\), putting \(f=e^{-\frac12\int Pdu}v\) gives \(v''+(Q-P'/2-P^2/4)v=0\); the ratio of independent solutions has Schwarzian \(2Q-P'-P^2/2\). Substituting \(P=(1-2u)/(u(1-u))\), \(Q=-1/(4u(1-u))\) gives S03. These statements are local away from \(u=0,1,\infty\); an arbitrary period map need not be unramified.

Actual symbolic check (Python/SymPy, 2026-11-17):

~~~python
import sympy as s
x, u = s.symbols('x u')
q = x*(x-1)*(x-u)
R = x*(x-1)/(2*(x-u))
lhs = u*(1-u)*s.Rational(3,4)/(x-u)**2 + (1-2*u)/(2*(x-u)) - s.Rational(1,4)
assert s.factor(lhs-(s.diff(R,x)-R*s.diff(q,x)/(2*q))) == 0
P = (1-2*u)/(u*(1-u))
Q = -1/(4*u*(1-u))
assert s.factor(2*Q-s.diff(P,u)-P**2/2) == (u**2-u+1)/(2*u**2*(u-1)**2)
~~~

Observed exploratory output: exact-differential residual 0; Schwarzian \((u^2-u+1)/(2u^2(u-1)^2)\). The live run used variable name l, renamed u in this display; the displayed certificate was subsequently rerun.

### C2. Nonzero nilpotent p-curvature at p = 3

The connection in S05 is the period/solution companion \(\partial-A\), with horizontal equation \(v'=Av\). In the de Rham row basis \(e=(\omega,\nabla_\partial\omega)\), one has \(\nabla_\partial e=eA^T\), so the coefficient-column connection on a section \(ec\) is \(c'+A^Tc\); the two connections are dual and \(\psi_{\mathrm{dR}}=-\psi_{\mathrm{sol}}^T\). The displayed matrix is \(\psi_{\mathrm{sol}}\), and its nonzero square-zero properties are invariant under this duality. On \(\mathbb F_3(u)\), \(\partial^3=0\), since the third power of a derivation in characteristic three is a derivation and annihilates u. Set \(B_0=I\), \(B_{n+1}=B_n'-AB_n\); then \(\psi_{\mathrm{sol}}(\partial)=B_3\). This recurrence gives S05's matrix. For \(h=u+1\), its numerator is the outer product \((-h,-1)^T(1,-h)\), whose middle scalar product vanishes, proving square-zero; the lower-left entry is nonzero throughout the smooth base. The coefficient of \(x^{p-1}=x^2\) in \(q^{(p-1)/2}=q\) is \(-(1+u)\), so the normalized Hasse polynomial is \(1+u\), and at \(u=-1\) the lower-left p-curvature entry remains nonzero.

~~~python
red = lambda f: s.cancel(f, modulus=3)
A = s.Matrix([[0,1],[1/(4*u*(1-u)),-P]]).applyfunc(red)
B = s.eye(2)
for _ in range(3):
    B = (B.diff(u)-A*B).applyfunc(red)
assert (B*B).applyfunc(red) == s.zeros(2)
expected = s.Matrix([[-u-1,(u+1)**2],[-1,u+1]])/(u**2*(u-1)**2)
assert (B-expected).applyfunc(red) == s.zeros(2)
assert B[1,0] != 0
# Review-response check: de Rham coefficient columns use the dual connection.
BdR = s.eye(2)
for _ in range(3):
    BdR = (BdR.diff(u)+A.T*BdR).applyfunc(red)
assert (BdR+B.T).applyfunc(red) == s.zeros(2)
assert (BdR*BdR).applyfunc(red) == s.zeros(2)
~~~

The live output had denominator \(u^4+u^3+u^2=u^2(u-1)^2\) modulo three and zero square, trace, and determinant. This checks the chosen companion model, not every connection that could be called uniformizing.

### C3. Central generator in the B3 map

The standard braid generators map to \(a=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\), \(b=\left(\begin{smallmatrix}1&0\\-1&1\end{smallmatrix}\right)\). Direct multiplication gives \(aba=bab\), \((ab)^3=-I\), \((ab)^6=I\): the full twist \((\sigma_1\sigma_2)^3\) survives as \(-I\) and cannot generate the kernel. The full kernel identification is taken from Hain (2014, Remark 8.4), rather than claimed from these three equalities alone.

~~~python
a = s.Matrix([[1,1],[0,1]])
b = s.Matrix([[1,0],[-1,1]])
assert a*b*a == b*a*b
assert (a*b)**3 == -s.eye(2)
assert (a*b)**6 == s.eye(2)
~~~

### C4. Hua's characteristic-five distinction

Over \(\mathbb F_5\), take \(i=2\); the six-point set is all of \(\mathbb P^1(\mathbb F_5)\). Every projective transformation preserving it is defined over \(\mathbb F_5\): its values on \(0,1,\infty\) determine it uniquely, and are three distinct rational points. Hence its full stabilizer is \(\mathrm{PGL}_2(\mathbb F_5)\), of order \((25-1)(25-5)/(5-1)=120\). Exhaustive invertible-matrix enumeration and deduplication of their six-point permutations produced 120 transformations, of which 24 preserved the opposite pairs.

~~~python
from itertools import product
p = 5
points = [None,0,1,2,3,4]  # None denotes infinity
pairs = {frozenset([None,0]),frozenset([1,4]),frozenset([2,3])}
perms, paired = set(), set()
for a,b,c,d in product(range(p), repeat=4):
    if (a*d-b*c) % p == 0:
        continue
    def act(x):
        num,den = (a,c) if x is None else ((a*x+b)%p,(c*x+d)%p)
        return None if den == 0 else num*pow(den,-1,p)%p
    perm = tuple(act(x) for x in points)
    perms.add(perm)
    if {frozenset(act(x) for x in pair) for pair in pairs} == pairs:
        paired.add(perm)
assert len(perms) == 120
assert len(paired) == 24
~~~

## References and proof boundary

Hain, R. (2014). *Lectures on moduli spaces of elliptic curves* (Version 3) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.0812.1803. Inspected PDF: https://arxiv.org/pdf/0812.1803; Proposition 5.16 and Proposition 8.2/Corollary 8.3/Remark 8.4, printed pp. 52 and 66–68. The relevant argument, including the discriminant-complement construction and braid-group proof sketch, was read; this is published-background verification. Duke's author record dates the book chapter 2010, in L. Ji and S. T. Yau (Eds.), *Transformation groups and moduli spaces of curves* (Advanced Lectures in Mathematics, Vol. 16, pp. 95–166), Higher Education Press: https://scholars.duke.edu/publication/1025733. Cite the inspected version consistently.

Katz, N. M. (1968). On the differential equations satisfied by period matrices. *Publications Mathématiques de l'IHÉS, 35*, 71–106. https://doi.org/10.1007/BF02698924. Inspected PDF: https://www.numdam.org/article/PMIHES_1968__35__71_0.pdf, Introduction, pp. 71–74: differentiation of periods and the Legendre/Hasse/hypergeometric example. C1 and C2 independently calculate the formulas used; the rest of the paper was not proof-audited.

Katz, N. M. (1970). Nilpotent connections and the monodromy theorem: Applications of a result of Turrittin. *Publications Mathématiques de l'IHÉS, 39*, 175–232. https://doi.org/10.1007/BF02684688. Inspected PDF: https://www.numdam.org/item/PMIHES_1970__39__175_0.pdf, Theorem 5.1, §§7.4–7.5, and Theorem 10.0. Theorem 7.4 applies through (7.4.1): absolute Frobenius is flat for S smooth over a field, as explicitly stated in (7.3.3); only the two bidegrees (0,1) and (1,0) contribute to H¹, so Corollary 7.5 gives exponent at most two. General proofs are carried as published background, not independently established by this run.

Michel Hua's project. (2026). *Modules courbes elliptiques en caractéristiques ≠2: Lecture modernisée du dossier entier* [AI-produced modernised reading of cote 64; context snapshot downloaded November 14, 2026]. hua_project/64.modern.tex, from https://github.com/Commutator-IO/grothendieck-project. This provided artifact, not a web-fetched transcription, is the comparison source throughout H01–H07; subsection locators refer to that exact snapshot.
