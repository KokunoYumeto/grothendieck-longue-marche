# Research record: conjecture lettering, correspondences, and tautological products

Research-only record, 16 November 2026. The transcription freeze preceded this work. No page transcription, combined transcription, or source image was changed or reinterpreted here. The comparisons below use the frozen page files and the supplied context transcription. The latter remains a first-pass witness, exactly as `context/README.md` specifies. Claims in `context/notes/RESULTS_STATE.md` are leads unless the present record identifies independently checked evidence.

## 1. Evidence and scope

`11/044`, for example, means `work/MPL_11_043-058+56/pages/MPL_11_043-058+56_11_scan044.tex`, scan 044 of cote 11. `C16/016` means `context/MPL_16+47+54+44_transcription.tex`, cote 16, scan 016. Current 11/044, 046, 048, 051, 053, 055, 057 were reread in full. Context 16/009, 015–018, 033, 040, 042, 044–051, 053, 055 were read or reread for the comparisons. Context notes and doubts were used as leads and checked against that supplied transcription. No new scan-level verification of the context was undertaken.

Searches of the fifty current frozen page files for `Lefschetzien`, `motif`, `motives`, `Künneth`, `idempoten`, `twist`, `Tate`, `tautolog`, `simplicial`, `jaug`, and `associativ` locate the correspondence and tautological material identified below. Substring hits in `rotatebox` have no subject significance. Broader `Phi`, `Lambda`, `conj`, and `semi-simple` searches also hit vanishing cycles, quadratic forms, and reused texts; the matching letters alone do not identify the algebra `Phi` of C16/014–018 or a motivic construction. These are search boundaries within the supplied fifty pages, not claims about an entire cote or the archive.

**Principal findings.** Cote 11 supplies explicit correspondence actions, composition, the diagonal acting as identity, and a proposed system of tautological subalgebras on powers of one variety. Its author still marks signs, a Cartesian axiom, associativity, units, and one excess-intersection coefficient for verification. C16 supplies a homomorphism from a specified operator algebra into a graded endomorphism ring. The exact bridge is the cycle-action map, together with the explicit idempotent and twist construction in section 3. No homomorphism from C16's `Phi` is written on the seven current correspondence/tautological sheets. This limited textual observation does not obstruct the mathematical relationships displayed below.

## 2. Standard-conjecture lettering: statements and evidence grades

### 2.1 The printed comparison

Use the algebraic class space

\[
C^j_H(X)=\operatorname{im}\bigl(\operatorname{CH}^j(X)_{\mathbb Q}\xrightarrow{\mathrm{cl}}H^{2j}(X)\bigr),\quad
L(x)=\xi\cup x,\quad d=\dim X.
\]

The following is a compact paraphrase of the printed definitions, not a transcription of the manuscript's lettering.

| Printed label | Specific content | Checked printed location |
|---|---|---|
| A | The map \(L^{d-2j}:C^j_H(X)\to C^{d-j}_H(X)\) is an isomorphism. Grothendieck's 1969 formulation additionally lists the cohomological isomorphism \(L^{d-i}:H^i\to H^{2d-i}\) as part (a). | G69 §3, p.196; K68 introduction, p.360 |
| B | The lowering operator \(\Lambda\) is induced by a rational algebraic correspondence. K68 specifies the operator that is zero on primitive vectors and reverses \(L\) along each primitive string. | G69 §3, p.196; K68 p.359 |
| C | The Künneth components of the diagonal are algebraic; their actions are the degree projectors on cohomology. G69 also records an independence-of-\(\ell\) strengthening in parentheses. | G69 §2, p.195; K68 pp.360,366 |
| D | Homological equivalence and numerical equivalence of cycles agree. | K68 introduction, p.360, and §3.6, p.379 |
| I / Hdg | Positivity of \((-1)^j\operatorname{Tr}(xy\xi^{d-2j})\) on primitive algebraic classes. | K68 p.360; G69 §4, p.197 |

Sources G69 and K68 are identified with URLs and retrieval citations in section 6. The table uses approximately 180 source-derived words across the two articles.

### 2.2 What the supplied manuscript transcription actually identifies

| Manuscript label | Concrete evidence in the supplied context | Comparison justified by those statements |
|---|---|---|
| A | C16/044 expresses A using equality of dimensions of \(C^i\) and \(C^{d-i}\); C16/045 specifies the critical-degree Lefschetz map on algebraic classes; C16/050 gives weak variants through a hyperplane section. | The algebraic-class Lefschetz content agrees with printed A. The manuscript's complete standalone definition is not reproduced on these letter sheets; do not infer that every convention of G69 part (a) was included verbatim. |
| B | C16/044 says A together with the index statement gives B; C16/045 writes the equality of the A and B conditions in its discussion of the index theorem. | The printed D comparison has the corresponding role in K68 p.360. The supplied manuscript passage does not state a standalone definition of B as equality of two equivalence relations. Record the shared role and leave that last identification unverified. |
| C | C16/040 obtains \(\Lambda_Y=\varphi^*\Lambda_X^2\varphi_*\) and then records passage from C(X) to C(Y). C16/042 describes algebraicity of \(\Lambda_X\varphi_*\). C16/048–049 characterize C using algebraic inverse maps between complementary degrees. | These are the operator/inverse-correspondence statements of printed B. This is the secure relabeling in the supplied evidence. |
| D | C16/040 invokes D(Y) while discussing algebraicity of primitive/Lefschetz projectors, with an uncertain inserted L or Λ in the preceding formula and a marginal L question. C16/048 invokes D(X) for rational coefficients of characteristic polynomials of algebraic endomorphisms. | Printed C has the Künneth-projector and characteristic-polynomial role in K68 pp.360,366. The manuscript's standalone D definition is not supplied here, and the primitive-projector formula on 040 requires its own reading check. A complete D-to-C identification therefore remains a documentary question. |

Thus the supplied text gives A's algebraic Lefschetz content and the C-to-printed-B identification directly. It gives meaningful B/D comparison evidence, but a four-entry permutation would exceed the standalone definitions actually recovered. The uncertainty is specific: the missing manuscript definitions of B and D, and the flagged projector formula on C16/040. This agrees with the evidential caution in `context/MPL_16+47+54+44_notes.md`, §S1, after checking the relevant context transcription rather than relying on that note alone.

C16/044 also uses `C(X)` for a **space of algebraic classes** in the sentence about finite dimension. Its mathematical referent there is the image of the cycle-class map displayed above. The surrounding letter uses the same characters for a conjectural condition. The exact maps and grammatical positions identify these uses; one cannot replace every occurrence mechanically by a conjecture name. Likewise `A` on C16/051 is expressly a ring of endomorphisms.

**Register connections.** WG2 §2.4 #3 asks for this lettering comparison. WG2 §2.2 #4 concerns the actual hyperplane reduction on C16/042,045–046. The current fifty pages add the correspondence machinery in section 3, but supply no further standalone A–D definitions. The source's reduction uses the concrete arrows

\[
\varphi^*:H^i(X)\to H^i(Y),\qquad
\Lambda_X\varphi_*:H^i(Y)\to H^i(X),
\]

and the critical Lefschetz operator on \(X\times Y\). These connect its letter C to inverse correspondences without an argument based merely on labels. This record does not repropose the source's reduction as a new conditional theorem.

## 3. Correspondence ring to category: the exact maps

### 3.1 Current 11/044: action and coefficient scope

The page explicitly allows Chow rings, cycle quotients, rationalization, and K-theory with the Euler-characteristic gauge. Its preceding topological/Poincaré variant retains uncertainty in the coefficient and cohomology wording. For the inclusion of indexing sets into their disjoint union, the correspondence action is

\[
\rho_{I',I}(u)(x)=\alpha'_*\bigl(u\,\alpha^*x\bigr),
\qquad u\in A(I\amalg I'),\quad x\in A(I).
\]

The margin explicitly asks which product order to use, `Cy` or `yC`. That choice must remain visible in graded comparisons.

**Context search and addition.** `correspondance`, `composition`, `endomorphisme`, and `Lefschetzien` lead to C16/009,015–018,049,051–055. The new sheet supplies the pull–multiply–push action in the indexed-power formalism. C16's discussion already uses rings of operators on a graded module; this page makes the cycle-to-operator arrow explicit.

### 3.2 Current 11/046: composition and its precise orientation

The literal notation is

\[
A(I';I):=A(I\amalg I'),\qquad
v\circ u=p_{31*}\bigl(p_{21}^*u\,p_{32}^*v\bigr).
\]

The target-first notation before the semicolon does **not** itself reverse the factors of the geometric product: the displayed defining equality fixes them. Write \(X_I=X^I\), and use the canonical coordinate map

\[
c_{I,J}:X^{I\amalg J}\longrightarrow X^I\times X^J,
\qquad (x_t)_{t\in I\amalg J}\longmapsto
((x_i)_{i\in I},(x_j)_{j\in J}).
\]

For its three-factor counterpart \(c_{I,J,K}\), the actual maps satisfy

\[
c_{I,J}p_{21}=\operatorname{pr}_{12}c_{I,J,K},\quad
c_{J,K}p_{32}=\operatorname{pr}_{23}c_{I,J,K},\quad
c_{I,K}p_{31}=\operatorname{pr}_{13}c_{I,J,K}.
\]

Transport of pullback and pushforward along these coordinate isomorphisms gives exactly

\[
v\circ u=\operatorname{pr}_{13*}
(\operatorname{pr}_{12}^*u\,\operatorname{pr}_{23}^*v).
\]

This proves the relationship with the printed correspondence composition used in J92 p.447, with every source and target fixed. It leaves the manuscript's notation unchanged.

The source calculation compares \(\rho(v\circ u)\) and \(\rho(v)\rho(u)\). It flags the base-change identity

\[
\alpha'^*\gamma'_*=p_{32*}p_{21}^*
\]

for the Cartesian projection square and writes `axiome cartésien oublié !`. Its two terminal expressions have the factors u and v in opposite orders. The margin says `OK mod signes` and calls for attention. One intermediate displayed line also drops the outer \(\beta''_*\) before the subsequent transitivity line; the frozen file retains that line.

In the concrete rational Chow-correspondence model, cycles have even cohomological degree. Projection formula and the displayed Cartesian square give the common value

\[
\rho(v)\rho(u)(x)=p_{3*}(p_{12}^*u\,p_{23}^*v\,p_1^*x)
=\rho(v\circ u)(x).
\]

This calculation verifies the action comparison in that specified model. The broader graded version of the page retains its authorial sign question.

### 3.3 Current 11/048: diagonal and the exact limit of the written proof

The construction is \(\Delta_I=\delta_*(1)\), where \(\delta:X^I\to X^I\times X^I\) is the diagonal. The page proves

\[
\rho(\Delta_I)(x)
=p_{2*}(\delta_*1\,p_1^*x)
=p_{2*}\delta_*(\delta^*p_1^*x)
=x.
\]

Its last sentence expressly leaves associativity of the correspondence operation and the diagonal's unit identities to `définir|vérifier`, then ends after the words about the stated conditions. The result written out is the **identity action on A(I)**. The source does not insert a faithfulness argument identifying correspondence classes from their actions in every example of 044.

For the rational Chow model, the unit identities themselves follow from the diagonal embeddings in the middle two factors, and associativity has the single four-factor expression

\[
w\circ(v\circ u)
=p_{14*}(p_{12}^*u\,p_{23}^*v\,p_{34}^*w)
=(w\circ v)\circ u.
\]

Here \(u:X\rightsquigarrow Y\), \(v:Y\rightsquigarrow Z\), \(w:Z\rightsquigarrow W\), and all \(p_{ab}\) are the displayed product projections. This is a verification of a standard concrete realization, not a completion of every bivariant axiom left unwritten in the manuscript.

### 3.4 Explicit projectors and twists in the printed category construction

J92 pp.447–448 uses cycle groups \(A^j_\sim\) modulo an adequate equivalence. Its objects and arrows are

\[
(X,p,m),\quad p\circ p=p,\quad m\in\mathbb Z,
\]
\[
\operatorname{Hom}((X,p,m),(Y,q,n))
=q\circ A^{\dim X-m+n}_\sim(X\times Y)\circ p.
\]

Composition is the preceding push–pull formula; the identity of \((X,p,m)\) is p. Numerically equivalent cycles give the semisimple abelian category in J92 Theorem 1, pp.448–449. J92 Corollary 1, pp.449–450, states its Künneth-algebraicity premise explicitly when identifying the homological-to-numerical kernel with a nilpotent Jacobson radical. This verifies the exact printed reference underlying WG2 §2.3 #7; it does not establish that premise from current 11/044–048.

The splitting maps are particularly concrete. For \(h(X)=(X,\Delta_X,0)\) and \(M=(X,p,0)\), the arrow \(h(X)\to M\) and the arrow \(M\to h(X)\) are both represented by p. Their composites are p on \(h(X)\) and \(\operatorname{id}_M=p\) on M. For the sum \(h(X)\oplus h(Y)\), with the two summand projectors \(e_X,e_Y\),

\[
e_Y\operatorname{End}(h(X)\oplus h(Y))e_X
=\operatorname{Hom}(h(X),h(Y)).
\]

Thus the relevant cross-correspondences are exact matrix blocks of an endomorphism ring. This is the explicit algebra-to-category relationship needed for MPL_14_087-132 M01 and MPL_14_002-044 M01, rather than an assertion that the subjects are unrelated.

The twist shift \((X,p,m)\mapsto(X,p,m+1)\) leaves a correspondence representative unchanged and preserves the codimension formula because \(-(m+1)+(n+1)=-m+n\). A degree-r correspondence has the precise form \(h(X)\to h(Y)(r)\). In particular,

\[
\Delta_{X*}\xi\in A^{\dim X+1}(X\times X),\qquad
L:h(X)\to h(X)(1),
\]

and its realization is

\[
\rho(\Delta_{X*}\xi)(x)
=p_{2*}\Delta_{X*}(\xi\,\Delta_X^*p_1^*x)=\xi x.
\]

The lowering correspondence occupies codimension \(\dim X-1\), hence the arrow \(h(X)\to h(X)(-1)\). This fixes the twist convention rather than suppressing it as C16/048 expressly does for its discussion.

### 3.5 The particular link to C16's Lefschetzien rings

C16/015–016 specifies a graded ring homomorphism

\[
\varphi:\Phi_0\to\mathcal E,
\quad \varphi(\mathbf L_0)=L,
\quad \varphi(\boldsymbol\pi_i)=\pi_i,
\quad \varphi(\boldsymbol\Lambda_0)=\Lambda.
\]

The projector condition is marked `condition essentielle !`. C16/017 gives the corresponding \(u:\Phi\to\mathcal E\) and records the failed attempt to determine it from L without the projectors. C16/018 names the resulting ring structure `anneau de correspondances Lefschetzien`. Its operator degree is cohomological: L has degree 2.

For a fixed smooth projective X and its homological correspondence groups, the cycle-action map is

\[
\rho_X:\bigoplus_r A^{\dim X+r}_{\mathrm{hom}}(X\times X)
\longrightarrow\operatorname{End}(H^*(X)),
\quad u\longmapsto[x\mapsto p_{2*}(\mathrm{cl}(u)p_1^*x)].
\]

It sends correspondence degree r to operator degree 2r. Künneth and Poincaré duality identify the relevant cohomological correspondence space with its operator space, so this action is injective after passage to homological equivalence. Its image is a concrete \(\mathcal E\) of the sort discussed in C16. The explicit correspondence \(\Delta_{X*}\xi\) just computed gives the specified L. This is the precise common structure between C16 and current 11/044–048.

The source data still have to be kept at their written level: the current seven sheets contain no displayed \(\Phi_0\to\mathcal E\), no chosen Künneth projectors, and no triple \((X,p,m)\). The comparison above supplies exact mathematical maps connecting their constructions. It does not attribute the full printed category construction to the incomplete last line of 11/048.

C16/049 supplies the direct historical link: its phrase `category of motives which is semi-simple !` accompanies the author's proposed semisimplicity argument using his C(X) and index statement. The preceding inverse calculation uses an algebraic transpose \(u'\) and the composite \((u'u)^{-1}u'\). That source programme is being reported with its stated premises, not advanced here as a new theorem. Current 11/044–048 add explicit composition and action for the indexed powers \(X^I\); the splitting maps of 3.4 explain exactly how the endomorphism calculations enter objects with projectors.

WG2 §2.3 #2 and WG2 §6. #9 also ask for an integral/rational analysis of \(\Phi\). C16/015 records matrix-unit-type multiplication, but its upper bounds and C16/014's integral model carry first-pass reading issues. Current 11/044's permission to tensor with \(\mathbb Q\) is not a proof of those universal-property or integral-order claims. Those register tasks remain uncompleted by these seven sheets.

### 3.6 Numerical quotient and the group-action lead

The exact quotient relevant to MPL_14_087-132 M09 and MPL_14_002-044 M29 is

\[
q_{XY}:A^r_{\mathrm{hom}}(X\times Y)\twoheadrightarrow
A^r_{\mathrm{num}}(X\times Y).
\]

Well-definedness follows directly from
\(\deg(z\cdot w)=\operatorname{Tr}(\mathrm{cl}(z)\mathrm{cl}(w))\): a homologically zero z has all these numbers zero. The maps preserve products, pushforward and pullback, and therefore the correspondence composition. On the displayed triples they give

\[
(X,p,m)\mapsto(X,q_{XX}(p),m),\qquad f\mapsto q_{XY}(f).
\]

Its kernel on a Hom group consists exactly of the projected homological correspondence classes whose numerical class vanishes. The question whether a particular cohomological realization descends through this quotient is expressed by its action on that explicit kernel. J92's nilpotence statement has the scope recorded in 3.4. For the exact algebraic meaning of nilpotence, the quotient \(\mathbb Q[\epsilon]/(\epsilon^2)\to\mathbb Q\), \(\epsilon\mapsto0\), has kernel \(\mathbb Q\epsilon\), with nonzero \(\epsilon\) and square-zero kernel. This explicit quotient prevents replacing a nilpotence conclusion by vanishing of the kernel.

For MPL_14_002-044 M27, the twist arrows above also specify the naturality calculation. A tensor automorphism g of a realization, acting on the one-dimensional Tate object by \(\chi(g)\), has the square

\[
(g_X\otimes\chi(g))\,\omega(L)=\omega(L)\,g_X.
\]

After a basis of the Tate line is fixed, this reads
\(g_X Lg_X^{-1}=\chi(g)^{-1}L\); the lowering arrow reads
\(g_X\Lambda g_X^{-1}=\chi(g)\Lambda\).
These equalities give the precise relationship relevant to the register's motivic-group question. The current sheets provide neither a fibre functor nor a group map realizing the entire \(\mathfrak{sl}_2\) discussion; their contribution here is the correspondence action and the exhibited twist degrees.

## 4. Tautological products and the Hua register claim

**Claim checked:** `Hua, findings register, 11-tautological-diagonal-product-rule`, as excerpted in `context/notes/RESULTS_STATE.md`. The supplied status is conjecture (unsearched), Lean card partly proved; the intake says the package was waiting. The excerpt ends after the beginning of its `(R,…)` description. No unseen continuation or Lean development was inspected. Their page range 50–56 is mapped in the supplied register to our scans 051–057.

| Current witness | What it actually supplies | Audit result for the supplied claim |
|---|---|---|
| 11/051 | Relations for one, two and three factors; an Euler-characteristic annotation; lists headed base. | The excerpt's two-factor square and three-factor small-diagonal identities are explicitly written. |
| 11/053 | Permuted copies of y and partial diagonal generators, with binomial counts and degrees; final relations heading has no formulas beneath it. | General generators are present. A completed general presentation is not written on this sheet. |
| 11/055 | Pairs (R,J), marked blocks, set-theoretic intersections, a reduction to unmarked partitions whose generated equivalence relation is coarse. | The partition indexing and product reduction are visible, with uncertain overwritten indices. |
| 11/057 | Three degree/excess cases; stability under external products and projection pullbacks, discussion of pushforwards, then stability under composition. | The transverse case has `! vérifier` followed by `OK`; the coefficient χ in the next case has a question mark and another `! vérifier`. This is an explicit authorial verification boundary. |
| 11/052,054,056 | Reused typescript about configuration quotients and invariant theory. | These scans belong to the supplied range, but the tautological handwritten formulas used here occur on 051,053,055,057. No mathematical nonrelationship with the reused text is asserted. |

### 4.1 Exact supported identities

Using y as the research symbol for the frozen `y|eta` uncertainty, the two-factor identities on 051 include

\[
y_1^2=y_2^2=0,\qquad y_1y_2=y_1\delta=y_2\delta,
\qquad \delta^2=\chi y_1y_2.
\]

On three factors the page writes

\[
\delta_{12}^2=\chi y_1y_2,\quad
\delta_{23}^2=\chi y_2y_3,\quad
\delta_{31}^2=\chi y_3y_1,
\]
\[
\delta_{12}\delta_{23}=\delta_{12}\delta_{31}
=\delta_{23}\delta_{31}=\delta,
\quad \delta y_i=y_1y_2y_3,
\]
\[
\delta^2=0,\qquad
\delta_{12}\delta=\delta_{23}\delta=\delta_{31}\delta
=\chi y_1y_2y_3.
\]

The manuscript uses δ both for the two-factor diagonal and for the three-factor small diagonal in their respective blocks. The maps are \(\Delta_2:X\to X^2\) and \(\Delta_3:X\to X^3\), so the exact classes are \(\Delta_{2*}1\) and \(\Delta_{3*}1\). Pullback by a coordinate projection \(p_{ij}:X^3\to X^2\) gives the partial diagonal \(p_{ij}^*\Delta_{2*}1\). These maps fix the relationship between the repeated notation and its geometric meaning.

Other frozen details must remain visible: the two-factor δ is written in `H^{n|m}(X)`; the two-factor top-degree base entry contains \(y_1y_2y_3\); one partial-diagonal/point relation contains `delta_1|y_1`; the degree symbol is `n|m`. These readings have not been repaired in this research record.

### 4.2 The general reduction and two indexing questions

On 055, R explicitly includes the empty block, and J is a selected block. For J empty, the exact coordinate isomorphism is

\[
X^{R\setminus\{\varnothing\}}\longrightarrow Z_R,
\qquad (x_B)_B\longmapsto(x_{B(i)})_{i\in I}.
\]

Its inverse takes the common coordinate on each nonempty block. Thus the number of geometric factors is \(b=\#(R\setminus\{\varnothing\})\). The next sheet writes \(s=\operatorname{card}R\) and \(\dim Z_R=sn\). The explicit forget-empty map
\(R\mapsto R\setminus\{\varnothing\}\) changes cardinality by one relative to 055. The two readings therefore require a convention change or an indexing correction; silently using one count for both loses this issue.

With its own s and s′ notation, 057 writes the three cases

\[
s+s'=k+1:\ \varepsilon_R\varepsilon_{R'}=\delta_k;
\quad k>s+s':\ \varepsilon_R\varepsilon_{R'}=0;
\quad k=s+s':\ \varepsilon_R\varepsilon_{R'}=\underset{?}{\chi}\,y_{X^k}.
\]

The last coefficient remains questioned. The source labels the equality case as checked by its `OK`; the source's general excess calculation is not completed there.

A second index shift is visible: 053 calls the diagonal on k factors \(\delta_{k-1}\), following \(\delta_r\) on r+1 factors, while 057 calls its diagonal on k factors \(\delta_k\). The common geometric map is \(\Delta_k:X\to X^k\); the written subscripts differ by one. Both readings are retained.

### 4.3 An independent concrete check, with the realization map explicit

Take \(X=\mathbb P^1\) over \(\mathbb Q\) and use Chow degree. Repeated projective-bundle decomposition gives

\[
R_k=\operatorname{CH}^*((\mathbb P^1)^k)_{\mathbb Q}
=\mathbb Q[h_1,\ldots,h_k]/(h_1^2,\ldots,h_k^2).
\]

The cycle-class map sends degree r here to cohomological degree 2r. The projective-bundle formula is the only external input in this calculation (Stacks, tag 02TX). The diagonal and point classes are

\[
y_i\longmapsto h_i,\qquad
\delta_{ij}\longmapsto h_i+h_j,\qquad
\delta\text{ on three factors}\longmapsto h_1h_2+h_1h_3+h_2h_3,
\quad \chi(\mathbb P^1)=2.
\]

Direct multiplication in \(R_3\) yields

\[
(h_1+h_2)^2=2h_1h_2,\quad
(h_1+h_2)(h_2+h_3)=h_1h_2+h_1h_3+h_2h_3,
\]
\[
(h_1h_2+h_1h_3+h_2h_3)^2=0,
\]
\[
(h_1+h_2)(h_1h_2+h_1h_3+h_2h_3)=2h_1h_2h_3.
\]

This verifies the quoted Hua formulas in a concrete realization. It also tests the scope of the lists headed base. The algebra presented by the two-factor displayed generators and quadratic relations at χ=2 has a surjective graded homomorphism to \(R_2\). The element \(\delta-y_1-y_2\) is nonzero in its degree-one space (all stated relations are quadratic), and its image in \(R_2\) is zero. Consequently those three listed classes have a dependency in this actual realization. A universal presentation and its realization are related by this explicit quotient map; the source's use of base needs its intended algebra and geometric scope specified.

The three-case rule of 057 also has a direct calculation in this same realization. Discard the empty bookkeeping block by the map above and write b,b′ for the nonempty block counts. Choose a tree on every block. Its diagonal polynomial is the product of \(h_i+h_j\) over the tree edges: expansion gives one monomial omitting each possible root, since a tree has exactly one orientation away from each chosen root. The union of the two block-tree systems has \(2k-b-b'\) edges. For the coarse generated equivalence relation it is connected. A tree gives the small diagonal polynomial; a connected graph with k edges has a single cycle and contributes \(2h_1\cdots h_k\), from its two cycle orientations; degree above k gives zero in \(R_k\). This proves the three values in the \(\mathbb P^1\) realization and fixes the block-count conversion explicitly. Its scope is this calculated Chow ring; it leaves the manuscript's general χ coefficient and the exact ambient hypotheses at their recorded status.

**Hua verdict.** The supplied excerpt accurately reports the displayed k=2,3 diagonal identities and the presence of partition data. It should retain the authorial question mark and verification flags for the general rule, the incomplete relations heading, and the notation/basis scope issues just identified. The intake can be updated from package waiting to checked against the frozen transcription for precisely these claims. The reported Lean status has not been independently checked.

## 5. Changes supported for the results register

| Register ID | Concrete addition from this packet/research | Remaining boundary |
|---|---|---|
| WG2 §2.4 #3 | 11/044 gives the action, 046 composition, 048 diagonal; C16 lettering comparison in section 2. | Full B/D manuscript definitions and a written \(\Phi\)-to-category construction are not recovered in the supplied witnesses. |
| WG2 §2.2 #4 | C16/042,045–046 use \(\Lambda_X\varphi_*\) and the product Lefschetz operator; present correspondence action fixes their geometric interpretation. | Current fifty pages supply no completion of that hyperplane induction. |
| WG2 §2.3 #2; WG2 §6. #9 | C16/015–018 provide the exact \(\Phi\)-homomorphism and mandatory projectors; 11/044 realizes the action arrow and explicit doubling of degrees. | The integral order/universal-property computations remain outside the present verification. |
| WG2 §2.3 #7 | J92 Theorem 1 and Corollary 1 independently checked at pp.448–450; exact homological-to-numerical quotient displayed. | The corollary's Künneth-algebraicity input is not supplied by 11/044–048. |
| MPL_14_087-132 M01; MPL_14_002-044 M01; MPL_15_195-228+18_002-017 M01 | The action, off-diagonal endomorphism blocks, projector splitting maps, and twist codimensions make the ring/category relationship explicit. | Those other package transcriptions were not supplied; their ledger excerpts remain leads. |
| MPL_14_087-132 M09; MPL_14_002-044 M29 | Explicit quotient functor and Hom kernel, together with exact J92 location. | No assertion that the kernel vanishes follows from the current sheets. |
| MPL_14_002-044 M27; MPL_14_087-132 M04/M05 | Exact naturality equation for L and Λ with Tate twists, section 3.6. | No subgroup inclusion or entire \(\mathfrak{sl}_2\) realization is asserted from these seven sheets. |
| Hua, findings register, 11-tautological-diagonal-product-rule | Literal formula audit, authorial flags, two indexing questions, and explicit \(\mathbb P^1\) ring calculation. | The excerpt is truncated; the unseen record and Lean development were not checked. |

LM7 and LM7_PUSH entries in the supplied register have no new result established by this narrow research record. The current packet's other subjects and Oda comparisons belong to the other research tasks.

## 6. Primary references and retrieval record

Only primary sources were used for the technical printed comparisons. No external prose quotation is used beyond source titles and labels; no source contributes a quotation of 25 words. The detailed manuscript analysis and the explicit calculations above are not paraphrases of the external sources.

- **G69.** Grothendieck, A. (1969), *Standard conjectures on algebraic cycles*, in *Algebraic Geometry, Bombay Colloquium 1968*, pp.193–199. Checked the available seven-page rekeyed witness, especially printed pp.195–198, §§2–4. [PDF](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf). The latest direct URL opening returned no readable lines; reopening the previously retrieved text witness returned the full article. Thus this is a checked rekeyed witness, not a claim of collation against the original printing. 
- **K68.** Kleiman, S. L. (1968), *Algebraic cycles and the Weil conjectures*, in *Dix exposés sur la cohomologie des schémas*, pp.359–386. Checked introduction pp.359–360; correspondence formalism §§1.3.1–1.3.7, pp.364–366; reduction §§2.13–2.14, pp.372–373; D at §3.6, p.379; related index discussion §3.9, p.380. [PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf). The filename's 1966 string is not the publication date used here. 
- **J92.** Jannsen, U. (1992), *Motives, numerical equivalence, and semi-simplicity*, *Inventiones mathematicae* 107, 447–452, DOI 10.1007/BF01231898. Construction pp.447–448; Theorem 1 pp.448–449; Corollary 1 pp.449–450. [Author-repository PDF](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf). 
- **Stacks 02TX.** *The Stacks Project*, Lemma 42.36.2, projective-space bundle formula. Used only to compute the explicit Chow ring of powers of \(\mathbb P^1\). [Tag 02TX](https://stacks.math.columbia.edu/tag/02TX). 

Parent review: open the cited URLs or retrieval references independently before reusing their web citation IDs in a final response. Preserve the frozen-page uncertainty marks and the first-pass status of the context when integrating this record.
