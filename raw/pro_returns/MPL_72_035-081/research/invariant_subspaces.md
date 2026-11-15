# Invariant subspaces: source audit and exact calculations

## Scope and context searched

This research was written after the transcription freeze. The inputs used were the frozen LaTeX fragments for cote 72, especially scans 058–059, 073–074 and 080–081, and the three supplied context files; no manuscript image was read by this research worker and no transcription, doubt, inventory or progress file was changed. Searches of `context/README.md`, `context/LM2_CONGRUENCE_ROWS.md` and `context/notes/RESULTS_STATE.md` covered `invariant`, `sous-espace`, `beta`, `β`, `pseudo`, `caract`, and the exact `72-` identifiers.

The directly matching context entry is **Hua, findings register, 72-invariant-subspaces-string**, supplied in `context/notes/RESULTS_STATE.md`, under “Findings of another project on these pages, to check,” with cote 72, their pages 79–82, and our scans 080–081. Its recorded status is “conjecture (unsearched) | Lean card: partly proved,” and the intake says “new to us”; the supplied statement stops at an ellipsis after its first exceptional-space family. The notes below assess that supplied excerpt and the present manuscript pages, with no claim to have checked the full external findings register or its Lean card. The neighbouring **Hua, findings register, 72-automorphisms-deform-gm-to-ga** bears on the centre and its finite-distance localization; both supplied Hua entries remain prior-run claims.

## Research items

### IS01 — The classification and its proof in the recorded frame

**72/080, theorem, TeX lines 7–16; kind: unproved claim.** The theorem lists “$\varnothing,X,\{c\},C$” and two further spaces for each vanishing $\beta_i$, and the rank-one calculation in Appendix A gives a complete proof for the explicit frame recorded on 059 and used on 073–074. This supports the supplied classification excerpt in **Hua, findings register, 72-invariant-subspaces-string**, while adding the actual evaluation map, propagation argument and duplicate count; the source definition on earlier, unsupplied scans still matters for transporting this calculation to every realization meant elsewhere in the archive.

### IS02 — The cancelled draft contains the propagation argument

**72/058, cancelled block, especially “Var'tés invariantes” and “$\beta_0=0$”; 72/080, theorem; kind: withdrawn in the same text.** The earlier cancelled discussion already uses the alternative of lying in a fixed hyperplane or containing its reflection centre, and its unfinished chain argument reappears as the two-family classification on 080. This adds a source-local precursor to **Hua, findings register, 72-invariant-subspaces-string**; the crossing-out records the state of that draft, while Appendix A supplies an independent complete argument in the stated matrix model.

### IS03 — The labels change within scan 080

**72/080, preliminary “On posera” and following flag diagram; kind: reading question.** The preliminary passage calls the common hyperplane intersection $Z_n$ and the empty set $Z_n'$, whereas the subsequent diagram assigns the intersection to $Z_n'$ and the empty set to $Z_n^{\sharp\mid!}$. The frozen alternatives and labels remain intact, and Appendix A uses explicitly defined $K_i$ and $A_i$ with a map to the diagram's labels, so that **Hua, findings register, 72-invariant-subspaces-string** is compared to the actual subspaces without concealing this change.

### IS04 — The vertical arrows need the vanishing parameter

**72/080, “sans hyp. sur aucun des $\beta_i$,” diagram and “Toutes les inclusions”; kind: reading question.** In the recorded pairing, $a_i'(a_{i+1})=\beta_i$, so the vertical containment $\operatorname{span}(a_{i+1},\ldots,a_n)\subset\bigcap_{j\leq i}\ker a_j'$ is equivalent to $\beta_i=0$, exactly as the nearby “NB” says. The concrete reflection matrices with $n=1$, $k=\mathbf F_3$, $\mu=(1,1)$ and $\beta=(2)$ give a nonzero evaluation and hence disprove the unrestricted vertical containment read literally; this qualifies the diagram supporting **Hua, findings register, 72-invariant-subspaces-string** without changing any arrow in the transcription.

### IS05 — The author's distinctness question has an explicit continuation

**72/080, “sont ils distincts ?”; 72/081, first display; kind: self-flagged.** The question is followed by the equal-dimension comparison and then the conditions $\mu_i=0$ and $\beta_{i-1}=\beta_i=0$, with the endpoint omissions written explicitly. Appendix A proves those coincidences directly, and Appendix B checks them against full subspace enumeration; this adds the equality conditions missing from the supplied excerpt of **Hua, findings register, 72-invariant-subspaces-string**.

### IS06 — The upper bound and its attainment

**72/081, Cor. (a)–(b), “au plus $2(n+2)$”; kind: unproved claim.** The exact count in the recorded model is $4+2z-c$, where $z$ counts zero $\beta_i$ and $c$ counts the coincidences specified in the first display of 081, so the upper bound is attained exactly by all $\beta_i=0$ and all $\mu_i\ne0$. This verifies the maximum criterion in the model and adds a reproducible count to **Hua, findings register, 72-invariant-subspaces-string**; the file `invariant_subspaces_cases.csv` records every parameter and count used in the finite check.

### IS07 — A characteristic-two counterexample to the literal four-space endpoint criterion

**72/081, Cor. (c), “les $\beta_i\ne0$ si $0<i<n-1$”; kind: reading question.** For $n=2$ over $\mathbf F_2$ with $\mu_0=\mu_1=\mu_2=\beta_0=\beta_1=0$, the three displayed matrices in Appendix B have exactly five invariant vector subspaces, whose projectivizations are $\varnothing$, $\{c\}$, an additional line, $C$ and $X$. The quoted strict-interior condition is empty at $n=2$, and the preceding two endpoint implications also hold, so the frozen criterion requires a reading or mathematical correction in these research notes; this is an additional qualification to the source underlying **Hua, findings register, 72-invariant-subspaces-string**, whose supplied excerpt does not include the disputed criterion.

### IS08 — The precise minimum obtained from the same classification

**72/081, Cor. (c), “Pour que ce soient les seuls”; kind: unpursued implication.** In the recorded model for $n\ge2$, every zero $\beta_i$ produces an extra invariant space after all coincidences are counted, and exactly four spaces occur precisely when every $\beta_i$ is nonzero; for $n=1$, the further tuple $\beta_0=\mu_0=\mu_1=0$ also gives four. The zero-block argument in Appendix A proves this statement and explains why the endpoint criterion on 081 needs attention, adding an exact count to **Hua, findings register, 72-invariant-subspaces-string** rather than promoting its prior-run status.

### IS09 — The finite-centre noncontainment is valid, including endpoints

**72/080, bottom “Si $c\notin C$ i.e. $\rho\ne0$”; kind: unproved claim.** Each intersection $K_i$ contains the common fixed line $kc$, and every tail $A_j$ lies in $V$, so $c\notin\mathbf P(V)$ proves every stated noncontainment $\mathbf P(K_i)\not\subset\mathbf P(A_j)$, including the empty-set and full-space endpoints under the diagram's conventions. This establishes the bottom-note argument in the explicit model and connects **Hua, findings register, 72-invariant-subspaces-string** to the finite-centre locus in **Hua, findings register, 72-automorphisms-deform-gm-to-ga** through the projection morphism in Appendix A.

### IS10 — The crossed-out irreducibility sentence and its replacement

**72/081, cancelled (d) and replacement (d), “sont en corr. $1-1$”; kind: withdrawn in the same text.** The manuscript crosses out the irreducibility formulation and replaces it, under the circled $\rho\ne0$ condition, by the correspondence between proper nonempty stable subspaces of $C$ and the zero $\beta_i$, ending with the unfinished “Les deux”. Appendix A verifies that correspondence by sending $i$ to $\mathbf P(A_{i+1})$; this adds the exact map to **Hua, findings register, 72-invariant-subspaces-string**, and the cancellation by itself supplies no mathematical refutation of the discarded sentence.

### IS11 — An attained smaller bound in characteristic two

**72/081, Cor. (b)–(c), “dans le cas des réflexions” and “car. $2$”; kind: unpursued implication.** In the characteristic-two reflection specialization, the proved count becomes $4+z+b-e$, where $b$ counts maximal blocks of zero $\beta_i$ and $e$ counts the two chain endpoints incident to such a block, yielding the attained bound $n+3$. Taking every $\beta_i=0$ gives one full invariant flag with exactly $n+3$ members, as the Appendix A proof and the cases $n=1,2,3$ in Appendix B show; this supplies a concrete refinement beyond the supplied **Hua, findings register, 72-invariant-subspaces-string** excerpt.

### IS12 — A concrete comparison task for the full source definition

**72/059, the pairing table; 72/074, “$\tau_i=\operatorname{id}+a_i'\otimes a_i$”; kind: own idea.** Compare the earlier definition of a nondegenerate realization against the explicit frame and basepoint orbit in Appendix A, recording the basis map and every required orbit condition before extending these results beyond the recorded model. Confidence is high that this is the decisive verification task, because the construction already gives the stated pairings, invertible generators, the nonadjacent commutations, and $n+2$ independent orbit vectors; it targets the remaining scope issue in **Hua, findings register, 72-invariant-subspaces-string** without asserting a new conjecture.

## Appendix A — Definitions, exact maps and proof

### A1. The coordinate model and its source map

Fix a field $k$, an integer $n\ge1$, coefficients $\beta_0,\ldots,\beta_{n-1}\in k$, and coefficients $\mu_0,\ldots,\mu_n$ with $\lambda_i=1+\mu_i\in k^\times$. Define

\[
 E=k a_{-1}\oplus k a_0\oplus\cdots\oplus k a_n,
 \qquad V=\operatorname{span}(a_0,\ldots,a_n),
 \qquad \pi(a_{-1})=1,\quad \pi(V)=0.
\]

Define the linear functional $\phi_i$ by the following complete list:

\[
 \phi_i(a_{i-1})=1,\qquad
 \phi_i(a_i)=\mu_i,\qquad
 \phi_i(a_{i+1})=\beta_i\quad(i<n),
 \qquad \phi_i(a_j)=0\text{ at all other positions}.
\]

The map to the manuscript notation is $a_j\mapsto a_j$ and $\phi_i\mapsto a_i'$ in the pairing table on 059: its rows say $\langle a_i,a'_j\rangle=1$ for $j=i+1$, $\mu_i$ for $j=i$, and $\beta_j$ for $j=i-1$. Evaluation therefore agrees entry by entry, including the unit joining $a_{-1}$ to $a_0'$ in the diagram. The operator

\[
 T_i(x)=x+\phi_i(x)a_i
\]

is the evaluation of $a_i'\otimes a_i$ in scan 074; in column-matrix notation its added matrix is $a_i\phi_i$. The equality $N_i^2=\mu_iN_i$ for $N_i=a_i\phi_i$ gives the explicit inverse

\[
 T_i^{-1}=I-\lambda_i^{-1}N_i.
\]

For $|i-j|\ge2$, both $N_iN_j$ and $N_jN_i$ vanish by the displayed pairing, so $T_iT_j=T_jT_i$. In the reflection specialization $\mu_i=-2$, the equality $T_i^2=I+(2+\mu_i)N_i=I$ verifies the involution relations directly, including characteristic two. Thus $s_i\mapsto T_i$ defines an actual representation of the group with generators $s_0,\ldots,s_n$, relations $s_i^2=1$, and $s_is_j=s_js_i$ for $|i-j|\ge2$ in that specialization.

The orbit contains

\[
 v_0=a_{-1},\qquad v_j=T_{j-1}\cdots T_0a_{-1}
      =a_{-1}+a_0+\cdots+a_{j-1}\quad(1\le j\le n+1),
\]

because $\phi_j(v_j)=1$. These $n+2$ vectors are independent: $v_0=a_{-1}$ and $v_{j+1}-v_j=a_j$ give an explicit triangular inverse between their coordinates and the $a$-basis. This is the precise nondegeneracy verified here; comparison with all clauses of the archive's earlier definition remains the task recorded in IS12.

Put $X=\mathbf P(E)$, $h_i=\mathbf P(ka_i)$, $H_i=\mathbf P(\ker\phi_i)$ and $C=\mathbf P(V)$. The first $n+1$ columns of the matrix $(\phi_i)$ form an upper-triangular matrix with diagonal $1$, so the functionals are independent and their common kernel is one-dimensional. Its projectivization is the manuscript centre $\{c\}$.

### A2. The two flags and all invariant spaces

Use the following names for actual vector subspaces:

\[
 A_i=\operatorname{span}(a_i,\ldots,a_n)\quad(0\le i\le n),
 \qquad A_{n+1}=0,
\]
\[
 K_i=\bigcap_{0\le j\le i}\ker\phi_j\quad(0\le i\le n),
 \qquad K_{-1}=E.
\]

Their dimensions are $\dim A_i=n+1-i$ and $\dim K_i=n+1-i$ for $0\le i\le n$, with $A_0=V$ and $K_n=kc$. Under the notation in the large diagram on 080,

| Actual subspace | Diagram label | Projective dimension |
|---|---|---:|
| $\mathbf P(K_i)$, $-1\le i\le n$ | $Z_i'$ | $n-i$ |
| $\mathbf P(A_{i+1})$, $-1\le i\le n$ | $Z_i^{\sharp\mid!}$ | $n-i-1$ |

Here $\mathbf P(0)=\varnothing$ has dimension $-1$. This explicit table follows the diagram, and does not replace the different preliminary labels in the frozen text.

For a vector subspace $W$, the formula $T_i(w)-w=\phi_i(w)a_i$ proves the exact criterion

\[
 T_iW=W\quad\Longleftrightarrow\quad
 W\subset\ker\phi_i\ \text{ or }\ a_i\in W.
\]

Indeed, a nonzero value of $\phi_i$ on $W$ gives $a_i\in W$ by division in $k$, and either alternative makes every added term belong to $W$; invertibility of $T_i$ upgrades the resulting containment to equality. This is an equality of actual invariant-subspace conditions, not a dimension-only comparison.

An invariant $W$ containing none of the $a_i$ lies in $K_n$, giving $0$ or $K_n$. For every other invariant $W$, let $r$ be the least index with $a_r\in W$; the equality $T_{j+1}(a_j)-a_j=a_{j+1}$ propagates membership to all $a_r,\ldots,a_n$, while the criterion puts $W$ in $K_{r-1}$. Thus

\[
 A_r\subset W\subset K_{r-1}.
\]

The two bounding spaces have dimensions differing by one. Their only intervening vector subspaces are the two bounds, and, for $r\ge1$, their containment is equivalent to $\beta_{r-1}=0$: the only possibly nonzero evaluation on the tail is $\phi_{r-1}(a_r)=\beta_{r-1}$. For $r=0$ the bounds are $V$ and $E$.

Conversely, the four spaces $0,K_n,V,E$ are invariant. At $\beta_i=0$, every generator preserves $A_{i+1}$ and $K_i$: generators on the appropriate side add their own vector inside the space, and the other generators vanish there by the pairing table. This proves the complete list

\[
 \{0,E,K_n,V\}\ \cup\
 \{A_{i+1},K_i:0\le i<n,\ \beta_i=0\}.
\]

The map $W\mapsto\mathbf P(W)$ and its inverse, the linear cone over a projective linear subspace together with $0$ for the empty set, identify this list with the projective subspaces in the manuscript theorem.

### A3. Coincidences and the exact total

Both $A$ and $K$ are strict flags. Across the two flags, equal dimensions force the pair $A_i,K_i$ for a unique $0\le i\le n$, and equal dimensions turn equality into the containment $A_i\subset K_i$. Evaluating $\phi_j$ on the displayed basis of $A_i$ gives

\[
 A_i=K_i
 \quad\Longleftrightarrow\quad
 \mu_i=0,\qquad
 \beta_{i-1}=0\ (i>0),\qquad
 \beta_i=0\ (i<n).
\]

These are exactly the three local vanishings, with endpoint omissions, at the top of scan 081. Each such equality identifies two members of the invariant list, and every duplicate has this form. Define

\[
 z=\#\{i:0\le i<n,\ \beta_i=0\},
\]
\[
 c_{\mathrm{eq}}=
 \#\{i:0\le i\le n,\ \mu_i=0,
       \ (i=0\text{ or }\beta_{i-1}=0),
       \ (i=n\text{ or }\beta_i=0)\}.
\]

The notation $c_{\mathrm{eq}}$ denotes a count and keeps it separate from the centre point $c$. The resulting count is

\[
 \boxed{N=4+2z-c_{\mathrm{eq}}.}
\]

The four base spaces are distinct for $n\ge1$, as their vector dimensions are $0,1,n+1,n+2$. The maximum $2n+4$ requires $z=n$ and $c_{\mathrm{eq}}=0$; at $z=n$ the second condition is exactly $\mu_i\ne0$ for all $i$. This proves the manuscript's maximum criterion within the model.

For the minimum, a block of $\ell$ consecutive zero $\beta$ edges contributes at most $\ell-1$ interior coincidences plus one at each chain endpoint it meets. A proper block therefore contributes at most $\ell$ coincidences; the block comprising the entire chain contributes at most $n+1$. With at least one zero edge and $n\ge2$, these bounds give $c_{\mathrm{eq}}<2z$, hence $N>4$. For $n=1$ and $\beta_0=0$, the formula becomes $N=6-[\mu_0=0]-[\mu_1=0]$, giving the extra four-space case stated in IS08.

In the characteristic-two reflection specialization, all $\mu_i=0$. Writing $b$ for the number of nonempty maximal zero-edge blocks and $e\in\{0,1,2\}$ for the number of chain endpoints incident to a zero edge gives $c_{\mathrm{eq}}=z-b+e$ and

\[
 N=4+z+b-e.
\]

For $b>0$, at least $b+1-e$ nonzero edges separate the blocks and occupy their unfilled endpoints, so $n-z\ge b+1-e$ and $N\le n+3$. For $b=0$, $N=4\le n+3$ directly. At $\beta_0=\cdots=\beta_{n-1}=0$, the equalities $A_i=K_i$ hold for every $i$, and the list is the full flag with exactly $n+3$ members, attaining this bound.

### A4. The finite-centre localization and the replacement (d)

Normalize a common-kernel vector $q$ by $q_n=1$ and use the recurrence

\[
 q_{n+1}=0,\qquad
 q_{i-1}=-\mu_iq_i-\beta_iq_{i+1}\quad(0\le i\le n),
\]

with the final $\beta_nq_{n+1}$ term omitted. This constructs $q$ explicitly and proves $\phi_i(q)=0$. For the restricted pairing matrix $B=(\phi_i(a_j))_{0\le i,j\le n}$, determinant expansion gives

\[
 d:=q_{-1}=(-1)^{n+1}\det B.
\]

In the reflection specialization $\mu_i=-2$, this is the positive-diagonal continuant $\rho$ used in the earlier calculations. More generally, the zero locus of $d$ is exactly the locus where the centre lies in $C$, without a choice of sign convention for the symbol $\rho$.

The formulas also work over the polynomial coefficient ring with the $\lambda_i$ inverted. Over its localization at $d$, put $c_0=q/d$ and define

\[
 E\longrightarrow Rc_0\oplus V,
 \qquad x\longmapsto
 \bigl(\pi(x)c_0,\ x-\pi(x)c_0\bigr).
\]

Addition is the inverse. The equalities $T_i(c_0)=c_0$ and $\pi T_i=\pi$ show directly that this map intertwines every generator. The restriction of $\phi_i$ to $V$ is exactly the $a_i^\vee$ expression on 073; this supplies the explicit morphism from the full coordinates on 059 to the centred coordinates on 073–074.

On the locus $d\ne0$, each $K_i$ contains $q$ outside $V$, whereas every $A_j$ lies in $V$, so there is no cross-flag equality or containment $K_i\subset A_j$. Every proper nonzero invariant subspace inside $V$ is consequently one of the distinct $A_{i+1}$ with $\beta_i=0$. The replacement (d)'s exact bijection is

\[
 \{i:0\le i<n,\ \beta_i=0\}
 \longrightarrow
 \{\text{proper nonempty invariant projective subspaces of }C\},
 \qquad i\longmapsto\mathbf P(A_{i+1}).
\]

Its inverse sends a subspace to the least index of a basis vector it contains, minus one, as proved in A2. At $d=0$, the common fixed line is contained in $V$ and is proper for $n\ge1$; together with the finite-centre list, this also verifies the crossed-out irreducibility criterion in this model, while retaining its cancelled documentary status.

## Appendix B — Exhaustive finite checks and explicit counterexamples

### B1. Reproduction

Run, from the package root:

```sh
python3 research/invariant_subspaces.py
```

The script uses only the Python standard library. It generates every subspace of $\mathbf F_p^{n+2}$ once through its canonical reduced-row-echelon basis, applies every actual generator matrix to each basis vector, and tests membership in that subspace; the candidate list and count formula are checked against these independent exhaustive tests. Admissible parameters are all $\mu_i\in\{0,\ldots,p-2\}$, so $1+\mu_i\ne0$, and every $\beta_i\in\mathbf F_p$.

The generated files are `research/invariant_subspaces_cases.csv` (every parameter tuple, count and comparison) and `research/invariant_subspaces_results.json` (grid totals, exact matrices and complete invariant-space lists for four examples). The following totals are generated by that command, not inferred from a sample:

| $p$ | $n$ | Parameter tuples | Subspaces per tuple | Subspace tests | Invariant-count distribution | Literal 081 endpoint-criterion failures |
|---:|---:|---:|---:|---:|---|---:|
| 2 | 1 | 2 | 16 | 32 | 4: 2 | 0 |
| 2 | 2 | 4 | 67 | 268 | 4: 1; 5: 3 | 3 |
| 2 | 3 | 8 | 374 | 2,992 | 4: 1; 5: 2; 6: 5 | 3 |
| 3 | 1 | 12 | 28 | 336 | 4: 9; 5: 2; 6: 1 | 0 |
| 3 | 2 | 72 | 212 | 15,264 | 4: 32; 5: 17; 6: 19; 7: 3; 8: 1 | 18 |
| 5 | 1 | 80 | 64 | 5,120 | 4: 65; 5: 6; 6: 9 | 0 |
| **Total** | | **178** | | **24,012** | **All candidate sets and formula counts matched** | **24** |

The last column tests the literal strict-interior reading together with both endpoint implications on 081; the weaker/stronger uncertainty at its first inequality remains in the transcription. The unambiguous characteristic-two display separately gives the same failed prediction for the $n=2$ example below. Of the 24 failing tuples, six are reflection tuples in characteristic two; the other 18 are general pseudo-reflection tuples over $\mathbf F_3$.

### B2. The five invariant spaces in the characteristic-two example

Take $p=2$, $n=2$, $\mu=(0,0,0)$ and $\beta=(0,0)$, with coordinate order $(a_{-1},a_0,a_1,a_2)$. The actual matrices are

\[
 T_0=\begin{pmatrix}1&0&0&0\\1&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\quad
 T_1=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&1&1&0\\0&0&0&1\end{pmatrix},\quad
 T_2=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&1&1\end{pmatrix}.
\]

Each is invertible, has rank-one difference from the identity, and squares to the identity. The nonadjacent pair $T_0,T_2$ commutes. The orbit vectors $a_{-1}$, $a_{-1}+a_0$, $a_{-1}+a_0+a_1$, and $a_{-1}+a_0+a_1+a_2$ are independent, so no loss of the recorded basis or unit adjacency is responsible for the example.

The complete invariant list, checked among all 67 subspaces, is:

| Vector subspace | Projectivization | Vector dimension |
|---|---|---:|
| $0$ | $\varnothing$ | 0 |
| $\langle a_2\rangle$ | $\{c\}$ | 1 |
| $\langle a_1,a_2\rangle$ | an additional projective line | 2 |
| $\langle a_0,a_1,a_2\rangle$ | $C$ | 3 |
| $E$ | $X$ | 4 |

Here $z=2$ and all three coincidences occur, so $N=4+4-3=5$. Every endpoint condition on 081 is satisfied, and the strict interior interval $0<i<n-1$ is empty. The mismatch therefore lies in the stated minimum criterion as read, not in a missed duplicate in this enumeration.

### B3. An unrestricted vertical arrow fails even at a finite centre

Take $p=3$, $n=1$, $\mu=(1,1)$ and $\beta=(2)$; this is the reflection specialization $\mu=-2$ in $\mathbf F_3$. Then

\[
 \phi_0=(1,1,2),\qquad \phi_1=(0,1,1),
\]
\[
 T_0=\begin{pmatrix}1&0&0\\1&2&2\\0&0&1\end{pmatrix},\qquad
 T_1=\begin{pmatrix}1&0&0\\0&1&0\\0&1&2\end{pmatrix}.
\]

The scalar $\phi_0(a_1)=2$ proves $A_1\not\subset K_0$. The common kernel is spanned by $(2,2,1)$, whose first coordinate is nonzero, so the example also has $c\notin C$ and $\rho=2$. This isolates the vertical-arrow issue from the valid finite-centre noncontainment note.

### B4. Enumeration entries for the manuscript catalogue

| Scan | What is enumerated | Parameters | Total and reproduction |
|---|---|---|---|
| 058 | Cancelled draft's incidence cases and tail/intersection candidates | $h_i,H_i,\beta_i$; local low-dimensional sketches | A draft with incomplete final argument; the complete model is enumerated by `invariant_subspaces.py`. |
| 080 | Two full flags of candidate projective spaces | $n\ge1$, $-1\le i\le n$; all $\mu_i,\beta_i$ | $2(n+2)$ named entries before cross-flag identifications; distinct total $2(n+2)-c_{\mathrm{eq}}$. |
| 080–081 | All invariant projective subspaces | $n$, the zero set of the $\beta_i$, and local $\mu_i$ at adjacent zeros | Exactly $4+2z-c_{\mathrm{eq}}$ in the recorded model; script enumerates every parameter in the six grids above. |
| 081 (b) | Parameters attaining the maximum | All $\beta_i=0$ and every $\mu_i\ne0$, with $1+\mu_i\ne0$ | $2(n+2)$ spaces; the example $(p,n,\mu,\beta)=(3,2,(1,1,1),(0,0))$ has 8 and its full list is in JSON. |
| 081 (c) | Four-space minimum and endpoint qualifications | Same parameters, with the strict-interior bound as frozen | The written endpoint criterion has the explicit five-space exception in B2; all tested cases are in the CSV. |
| 081 (d) | Proper nonempty invariant subspaces of $C$ on the finite-centre locus | $\det B\ne0$, indices $i$ with $\beta_i=0$ | $z$ such subspaces; the bijection $i\mapsto\mathbf P(A_{i+1})$ is proved in A4 and checked in every finite-centre tuple. |

## Limits of this audit

The algebraic proof establishes the stated results for the explicit chain model and supplies the maps connecting its coordinates to the recorded pairings and centred restriction. The independent finite calculation covers exactly the six prime-field grids listed in B1; its numerical totals do not certify untested parameters by themselves, and the all-field statements above rest on their written proofs. The frozen transcription keeps the uncertain $Z$ exponent, the changed labels, the disputed endpoint condition, and every cancellation; questions raised by these calculations belong in the research notes only.
