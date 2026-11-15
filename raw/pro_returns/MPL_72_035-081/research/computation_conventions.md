# Exact conventions and proofs for the enumeration tables

This file supplies the coordinate maps and proofs used by [recompute_enumerations.py](recompute_enumerations.py). The inputs are the frozen TeX pages, read as text after the freeze; the calculations do not select between paleographic alternatives or alter the source. [enumeration_reading_questions.csv](enumeration_reading_questions.csv) records literal comparisons separately, and [enumeration_catalogue.csv](enumeration_catalogue.csv) gives scans, parameters, totals, source anchors, and the complete rerun command.

## Reproduction and scope

Run from the extracted package root:

    python3 research/recompute_enumerations.py --max-n 12 --matrix-max-n 5

Python 3 and SymPy are the only dependencies. The command recomputes individual matchings for orders 0–12, direct symbolic determinants for orders 0–7, complete matrices and vectors for dimensions 1–5, low-dimensional examples, reductions modulo 2, documentary counts, and the catalogue. [enumeration_checks.json](enumeration_checks.json) records the actual versions, parameters, and every exact residual. The script hashes the 47 page fragments and combined transcription before and after the run and asserts that all 48 inputs are unchanged; the separate final freeze verifier compares these inputs with the authoritative freeze manifest.

The proofs below establish the stated polynomial identities for every indicated order. The finite tables provide additional reproducible expansions within the stated bounds. The source's categorical, smoothness, group-scheme, and invariant-subspace claims are addressed in the companion research sections.

**Context status used throughout:** the exact ID **72-automorphisms-deform-gm-to-ga**, in the Hua findings register summarized by [RESULTS_STATE.md](../../context/notes/RESULTS_STATE.md), is labelled **“conjecture (unsearched) | Lean card: partly proved.”** Its mention of the continuant measuring the center supplies the contextual connection; this file proves the displayed polynomial identities and does not adopt the recorded group-scheme verdict. The supplied LM2 rows were read and are retained as claims; none is used as a proof of the continuant identities.

## 1. Polynomial and index maps

Work first in polynomial rings over $\mathbb Z$. Define $L_0=1$, $L_1=2$, and, for $r\geq2$,

$$
L_r(B_1,\ldots,B_{r-1})=
2L_{r-1}(B_2,\ldots,B_{r-1})-
B_1L_{r-2}(B_3,\ldots,B_{r-1}).
$$

Thus $L_r$ has exactly $r-1$ arguments for $r\geq1$. This defines the order and arity used by the script; conflicting written subscripts and endpoints on scans 049, 050, 053, 061, and 073 remain reading questions.

Let $T_r(C)$ have diagonal $2C_i$, adjacent entries $-C_{i+1}$, and zero elsewhere, with $0\leq i<r$. Put $\Delta_r=\det T_r$ and $\Delta_0=1$. The exact ring homomorphism

$$
\phi:\mathbb Z[C_0,\ldots,C_{r-1}]
\longrightarrow\mathbb Z[B_0,\ldots,B_{r-1}],
\qquad C_i\longmapsto\prod_{k=0}^{i}B_k
$$

defines $\delta_r=\phi(\Delta_r)$. On monomial exponents the map and its inverse are

$$
e_k=\sum_{i=k}^{r-1}a_i,\qquad
a_k=e_k-e_{k+1},\qquad e_r=0.
$$

The inverse formula proves that distinct C-monomials retain distinct images.

For the general pairing on scans 048/059, the map to the source's $\lambda,\alpha$ coordinates is

$$
\mu_i\longmapsto\lambda_i-1,\qquad
\beta_i\longmapsto1-\lambda_i+\alpha_i.
$$

The reflection specialization sends every $\lambda_i$ to $-1$, giving $\mu_i=-2$ and $\beta_i=\alpha_i+2$. The isolated $L_2$ alpha line on scan 050 uses $B_1\mapsto\alpha_0+2$, while the $L_3,L_4$ alpha lines use $B_i\mapsto\alpha_i+2$; the script checks these maps separately.

### Primed and tilde quantities

The matching formula in §2 proves that every coefficient of $L_r$ is even for odd $r$. For odd $r$, define the integral polynomial $L'_r$ by halving its integer coefficients; for even $r$, define $L'_r=L_r$. For $R=\mathbb Z[B]$, the exact operation is the **R-module isomorphism**

$$
2R\longrightarrow R,\qquad
\sum_m 2a_mB^m\longmapsto\sum_m a_mB^m,
$$

whose inverse is multiplication by 2; it is performed before the reduction homomorphism $R\to\mathbb F_2[B]$. The same coefficient operation defines $\Delta'_r$ and $\delta'_r$.

For $r\geq1$, every matching term of $\Delta_r$ contains $C_{r-1}$, so $\Delta'_r=C_{r-1}Q_r$ for an integral polynomial $Q_r$. The CSV gives $Q_r$ with its full arguments; the source's varying tilde subscripts and argument lists on scan 049 remain a question. The B substitution gives the exact factor $B_{r-1}$ in $\delta'_r$.

For dimension $n\geq1$, use these names:

| Output name | Exact polynomial | Source usage |
|---|---|---|
| rho | $L_{n+1}(\beta_0,\ldots,\beta_{n-1})$ | $\rho$, scans 048, 052 onward |
| sigma_tail | $L_n(\beta_1,\ldots,\beta_{n-1})$ | $\zeta_0$, scans 052, 061 onward |
| sigma_reverse | $L_n(\beta_0,\ldots,\beta_{n-2})$ | $\sigma'$, scans 061–071 |
| gamma | $L_{n-1}(\beta_1,\ldots,\beta_{n-2})$ | $\gamma$; $n=1$ gives $L_0=1$ |
| rho_normalized | $L'_{n+1}(\beta_0,\ldots,\beta_{n-1})$ | $\rho'$ or $\widetilde\rho$, scans 053, 075, 078 |
| sigma_normalized | $L'_n(\beta_1,\ldots,\beta_{n-1})$ | $\sigma'$ or $\widetilde\sigma$, scans 053, 075, 078 |
| norm on scan 048 | $-\rho_{\mathrm{normalized}}\sigma_{\mathrm{normalized}}$ | the quantity called $\sigma=f(c')$ on 048 |

Put $d_r=1$ for even $r$ and $d_r=2$ for odd $r$. The exact relations are

$$
\rho=d_{n+1}\rho_{\mathrm{normalized}},\qquad
\sigma_{\mathrm{tail}}=d_n\sigma_{\mathrm{normalized}},\qquad
d_nd_{n+1}=2,
$$

$$
2\sigma_{048}=-\rho\sigma_{\mathrm{tail}},\qquad
d_n\sigma_{\mathrm{normalized}}\sigma_{\mathrm{reverse}}
=\beta+\gamma\rho,\qquad
\beta=\prod_{i=0}^{n-1}\beta_i.
$$

Section 4 proves the last identity, directly relating the two uses of the primed sigma glyph.

## 2. Determinants, permutations and matching counts

Let $A_r$ have diagonal 2, upper diagonal $-B_1,\ldots,-B_{r-1}$, and lower diagonal $-1$. Expansion at its first row gives $\det A_r=L_r$, with initial determinants 1 and 2.

Take the smallest moved label $i$ in a contributing tridiagonal permutation. All earlier labels are fixed, forcing $i\mapsto i+1$; the only remaining row able to map to $i$ is $i+1$, forcing the adjacent transposition. Removing those two labels proves inductively that every contributing permutation is a product of disjoint adjacent transpositions.

Write $J\subseteq\{1,\ldots,r-1\}$ for the left edge labels, with no consecutive labels, and $p=|J|$. Each transposition contributes $-B_j$ and each unmatched vertex contributes 2, giving

$$
L_r=
\sum_{p=0}^{\lfloor r/2\rfloor}
(-1)^p2^{r-2p}
\sum_{\substack{J\subseteq[1,r-1],\ |J|=p\\
J\text{ has no consecutive labels}}}
\prod_{j\in J}B_j.
$$

The map $j_k\mapsto j_k-(k-1)$ is a bijection to increasing p-tuples in $[1,r-p]$, with inverse $y_k\mapsto y_k+(k-1)$. Therefore the exact count is $\binom{r-p}{p}$. The monomial recovers J, proving the source's noncancellation statement in the formal polynomial ring.

The complete gap coordinates are

$$
a_1=j_1-1,\quad
a_k=j_k-j_{k-1}-2\ (2\leq k\leq p),\quad
a_{p+1}=r-1-j_p,\qquad
\sum_{k=1}^{p+1}a_k=r-2p.
$$

Their inverse is $j_k=2k-1+\sum_{h=1}^{k}a_h$. The empty matching has the single gap $a_1=r$. Thus the equality version uses p+1 gaps; retaining only the first p gaps gives $\sum_{1}^{p}a_k\leq r-2p$. For r=3,p=1, the tuples (0, 1),(1, 0) give edges 1 and 2, whereas the source's equality in one gap selects only edge 2.

For $T_r(C)$, unmatched vertex i contributes $2C_i$ and edge j contributes $-C_j^2$, so

$$
\Delta_r=\sum_J(-1)^p2^{r-2p}
\prod_{i\text{ unmatched}}C_i\prod_{j\in J}C_j^2.
$$

Set $D=\operatorname{diag}(\phi(C_0),\ldots,\phi(C_{r-1}))$. Comparison of every diagonal and adjacent entry proves

$$
\phi(T_r)=D A_r(B_1,\ldots,B_{r-1}),\qquad
\delta_r=M_rL_r,\qquad
M_r=\prod_{k=0}^{r-1}B_k^{r-k}.
$$

This is an entrywise polynomial matrix identity. Reversal sends edge j to r-j; this involutive bijection preserves matching size and sends each monomial to its reversed-variable monomial, proving the reversal identity.

### Parity tables

In order 2m, only the perfect matching $\{1, 3,\ldots, 2m-1\}$ survives modulo 2. In order 2m+1, after integer coefficient halving, surviving matchings have size m and unmatched vertex in $\{0, 2,\ldots, 2m\}$. Explicitly,

$$
L_{2m}\equiv B_1B_3\cdots B_{2m-1},
$$

$$
L'_{2m+1}\equiv
\sum_{k=0}^{m}
(B_1B_3\cdots B_{2k-1})
(B_{2k+2}B_{2k+4}\cdots B_{2m})
\pmod2.
$$

There are m+1 terms in the second line, including both empty-end products. Multiplication by $M_r$ proves all four determinant parity families on scan 051; the two even-order families have the explicit polynomial square roots in [continuant_delta_parity.csv](continuant_delta_parity.csv). In particular, each variable in the last pair of the unshifted even formula has exponent 2.

## 3. Full pairing, dual bases and polar matrices

Use $N=n+2$, the E basis $(a_{-1},a_0,\ldots,a_n)$, and the E-prime basis $(a'_0,\ldots,a'_{n+1})$. The general pairing matrix has

$$
P_{r,r}=1,\qquad P_{r,r-1}=\mu_{r-1},\qquad
P_{r,r-2}=\beta_{r-2},
$$

with all other entries zero. Lower unitriangularity gives determinant 1 and the case counts $N,N-1,N-2,N^2-(3N-3)$.

Under $\mu_i\mapsto-2$, its inverse is

$$
(P^{-1})_{r,c}=
\begin{cases}
L_{r-c}(\beta_c,\ldots,\beta_{r-2})&r\geq c,\\
0&r<c.
\end{cases}
$$

The diagonal and first lower diagonal use $L_0=1,L_1=2$. Multiplication by P produces $Q_{r,c}-2Q_{r-1,c}+\beta_{r-2}Q_{r-2,c}$, which vanishes by the right-end continuant recurrence; diagonal multiplication gives 1. This proves both dual-basis tables.

The restricted pairing Q, with E rows 1 through N-1 and E-prime columns 0 through N-2, satisfies

$$
Q^T=-A_{n+1}(\beta_0,\ldots,\beta_{n-1}),\qquad
\det Q=(-1)^{n+1}\rho.
$$

For $n=2,\beta_0=\beta_1=1$, the determinant and rho are -4 and 4. This exact matrix map supplies the scan 057 sign comparison.

Let $q_i=\prod_{k=0}^{i-1}\beta_k$, $q'_i=\prod_{k=i}^{n-1}\beta_k$ for $0\leq i\leq n$. The source quadratic polynomial is

$$
f(x)=\sum_{i=0}^{n}q_ix_i^2-x_{-1}x_0-
\sum_{i=0}^{n-1}q_{i+1}x_ix_{i+1}.
$$

Its polar matrix G has diagonal $0, 2q_0,\ldots, 2q_n$ and adjacent entries $-q_0,\ldots,-q_n$. The reverse polar matrix G-prime has diagonal $2q'_0,\ldots, 2q'_n, 0$ and adjacent entries $-q'_0,\ldots,-q'_n$. Direct entry comparison and determinant expansion give

$$
\Psi=P^{-1}G,\qquad
\Psi'=P^{-T}G',\qquad
\det G=-M_n\sigma_{\mathrm{tail}},\qquad
\det G_V=M_n\rho.
$$

Thus scan 053's written $\delta_E=M_n\sigma_{\mathrm{tail}}$ is related to scan 046's $\delta(f)=\det G$ by multiplication by -1. The verification task concerns that change of discriminant sign convention; the script retains both expressions.

## 4. Four continuants, center and dual-image vectors

Define

$$
R_i=\begin{pmatrix}2&-\beta_i\\1&0\end{pmatrix},
\qquad H=\begin{pmatrix}2&1\\1&0\end{pmatrix}.
$$

Successive multiplication using the recurrence gives

$$
R_0\cdots R_{n-1}H=
\begin{pmatrix}
\rho&\sigma_{\mathrm{reverse}}\\
\sigma_{\mathrm{tail}}&\gamma
\end{pmatrix}.
$$

Taking determinants proves
$\sigma_{\mathrm{tail}}\sigma_{\mathrm{reverse}}=\beta+\gamma\rho$.
The cases n=1 and n=2 have gamma equal to 1 and 2, respectively.

In column coordinates put $u=P^{-T}e_{N-1}$ and $u'=P^{-1}e_0$. Then
$u=(\rho,\sigma_{\mathrm{tail}},\zeta_1,\ldots, 1)^T$, and

$$
\Psi u=-\sigma_{\mathrm{tail}}u',\qquad
\Psi'u'=-\sigma_{\mathrm{reverse}}u,\qquad
\Psi'\Psi=\beta I+\gamma u e_0^T,\qquad
\Psi\Psi'=\beta I+\gamma u'e_{N-1}^T.
$$

For the first composition $\Psi'\Psi$, each column $a_i$ gives $\beta a_i$ because $q_iq'_i=\beta$. Applying the composition to u and using the four-continuant identity leaves the remaining column equation $\rho(V-\beta e_0-\gamma u)=0$. In the universal integral polynomial ring, rho is nonzero, with constant term $2^{n+1}$, so cancellation proves that column identity; the substitution homomorphism $\mathbb Z[\beta_i]\to A,\ \beta_i\mapsto b_i$ then carries the polynomial matrix identity to every commutative coefficient ring A.

The parameter involution $\beta_i\mapsto\beta_{n-1-i}$, together with reversal of the two ordered bases, sends the first composition to the second: with reversal matrix J, $\Psi'(\beta)=J\Psi(\beta_{\mathrm{rev}})J$ and $u'(\beta)=Ju(\beta_{\mathrm{rev}})$. This gives the stated dual composition by the same exact matrix map.

Define

$$
\Theta=\sigma_{\mathrm{tail}}\Psi'+\gamma u e_{N-1}^T.
$$

The row identity $e_{N-1}^T\Psi=-\sigma_{\mathrm{tail}}e_0^T$ and the two composition identities give

$$
\Theta\Psi=\Psi\Theta=\beta\sigma_{\mathrm{tail}}I,\qquad
\Theta u'=-\beta u.
$$

These are integral polynomial identities. In the explicit localization
$R\to R[(\beta\sigma_{\mathrm{tail}})^{-1}]$, the fraction
$\Theta/(\beta\sigma_{\mathrm{tail}})$ is the inverse matrix.

Let $s_i=\sum_{r=0}^{i}e_r$, $s'_j=\sum_{c=j}^{N-1}e'_c$, and $t_i=\Theta s'_i$. Summing P's three bands proves the complete table

$$
\langle s_i,s'_j\rangle=
\begin{cases}
0&i<j,\\
1&i=j,\\
\displaystyle\sum_{k=j}^{i-2}(\beta_k-1)&i>j.
\end{cases}
$$

The first lower diagonal uses the empty sum, hence zero. The other exact formulas are

$$
\langle s_i,u'\rangle=\langle u,s'_j\rangle=1,\qquad
t_{n+1}=-\sigma_{\mathrm{tail}}P^{-T}e_n+\gamma u,
$$

$$
t_i=t_{n+1}-\sigma_{\mathrm{tail}}\sum_{j=i}^{n}q'_ja_j.
$$

The final vector has coefficients -beta on $a_{-1}$, zero on $a_0$, and gamma on $a_n$, and
$Gt_{n+1}=\beta\sigma_{\mathrm{tail}}e_{N-1}$. Consequently,

$$
f(u)=-\rho\sigma_{\mathrm{tail}}/2,\qquad
f(t_{n+1})=\beta\sigma_{\mathrm{tail}}\gamma/2,
$$

$$
f(s_0+s_1)=-1,\qquad
f(t_n+t_{n+1})=\beta\sigma_{\mathrm{tail}}(2\gamma-\sigma_{\mathrm{tail}}).
$$

The half-products are integral by the continuant parities. For
$w_i=\sum_{j=i}^{n}q'_ja_j$, adjacent terms in $f(w_i)$ cancel all square terms except the last, giving $f(w_i)=\beta$; also
$\varphi(t_{n+1},w_i)=\beta\sigma_{\mathrm{tail}}$.
Expanding $f(t_{n+1}-\sigma_{\mathrm{tail}}w_i)$ proves the equal norms of all t-vectors.

## 5. Low-dimensional and centered tables

The exact map is $\beta_i\mapsto\alpha_i+2$; the script's $\alpha_0$ in dimension 1 is the source's unindexed alpha.

| Dimension | rho, sigma-tail, sigma-reverse, gamma | Final t-vector | Norm |
|---|---|---|---|
| 1 | $2-\alpha_0,\ 2,\ 2,\ 1$ | $a_1-(\alpha_0+2)a_{-1}$ | $\alpha_0+2$ |
| 2 | $-2(\alpha_0+\alpha_1),\ 2-\alpha_1,\ 2-\alpha_0,\ 2$ | $2a_2+(\alpha_1+2)a_1-(\alpha_0+2)(\alpha_1+2)a_{-1}$ | $(\alpha_0+2)(4-\alpha_1^2)$ |

Replacing the dimension-2 coefficient on $a_1$ by the first frozen reading $2+\alpha_1^2$ changes that coefficient by $\alpha_1^2-\alpha_1$ and its norm by
$(\alpha_0+2)(\alpha_1^2-\alpha_1)^2$. At $(\alpha_0,\alpha_1)=(0, 2)$, the coefficients are 6 and 4, and the norms are 8 and 0. The alternate linear reading and the beta-one underbrace are retained beside this comparison.

In $R[\rho^{-1}]$, put $c=u/\rho$ and $\widetilde s_i=s_i-c$. The integral scaled coordinates are

$$
S_i=-\rho\widetilde s_i=u-\rho s_i,\qquad
S_i-S_{i-1}=-\rho a_{i-1}.
$$

Telescoping in f gives $f(s_i)=0$ and $\varphi(s_i,u)=-\sigma_{\mathrm{tail}}$. Expansion proves

$$
f(S_i)=\rho\sigma_{\mathrm{tail}}/2
=\rho_{\mathrm{normalized}}\sigma_{\mathrm{normalized}},
$$

$$
f(S_0+S_1)=2\rho\sigma_{\mathrm{tail}}-\rho^2,\qquad
f(S_0-S_1)=\rho^2.
$$

The two parity substitutions give scan 078's displayed table for the sum:

| Parity of n | Norm of adjacent sum |
|---|---|
| even | $4\rho_{\mathrm{normalized}}(\sigma_{\mathrm{normalized}}-\rho_{\mathrm{normalized}})$ |
| odd | $\rho_{\mathrm{normalized}}(4\sigma_{\mathrm{normalized}}-\rho_{\mathrm{normalized}})$ |

In the further localization at
$\rho_{\mathrm{normalized}}\sigma_{\mathrm{normalized}}$, the squared homothety ratio is
$4-\rho^2/(\rho_{\mathrm{normalized}}\sigma_{\mathrm{normalized}})$.
This is the algebraic equation verified by the source's two radical displays; the computation makes no square-root branch choice. The first frozen minus alternative on the later norm line differs from the displayed sum table by $2\rho(\rho-\sigma_{\mathrm{tail}})$.

## 6. Required literal comparisons, source quotes and context status

Each row below has **kind: proved/computed identity plus reading/math verification question**. In every row the exact contextual ID is **72-automorphisms-deform-gm-to-ga**, with the recorded status **conjecture (unsearched); Lean card partly proved**; the relation is the explicit continuant/center calculation, and the prior group-scheme claim remains a claim.

| Scan | Short source quote | Exact comparison and verification task |
|---|---|---|
| 047 | “$1\leq p\leq n/2$”; “$\sum\alpha_i=n-2p$” | The first bound omits the identity term; at n=2 the residual is -4. The equality requires p+1 gaps; at n=3,p=1, p gaps with equality give one of the two matchings. Compare the written bounds with scan 049's “Attention p=0!”. |
| 053 | “$\delta_{\mathcal E}=B\sigma$” | The 045/046 polar matrix gives $\det G_E=-M_n\sigma_{\mathrm{tail}}$, so the written value is its negative. Check the change of sign convention from scan 046; no source sign is silently replaced. |
| 057 | “$=L_{n+1}(\beta_0,\ldots,\beta_{n-1})=\rho$” | $Q^T=-A_{n+1}$ gives $\det Q=(-1)^{n+1}\rho$. At n=2 and both beta parameters 1, the literal difference is -8. Check the intended determinant sign. |
| 069 | first reading “$2+\alpha_1^2$”, with underbrace “$\beta_1$” | The coefficient residual is $\alpha_1^2-\alpha_1$; the norm residual is $(\alpha_0+2)(\alpha_1^2-\alpha_1)^2$. At alpha=(0, 2), the two norms are 8 and 0. Verify the exponent-shaped mark while preserving both frozen readings. |
| 071 | “$\widetilde s_i=\widetilde s_0-\rho^{-1}[a_0+\cdots+a_{i-1}]$” | The defining map gives increment $+\sum a_j$. Multiplying the literal residual by rho gives $-(\rho+1)\sum a_j$. Compare scan 078's explicit plus increment. |
| 071 | “$-(2\gamma\rho-\sigma\rho-2\beta)/(\beta\rho)$” | Combining the preceding expression gives numerator $-(2\gamma-\sigma)\rho-2\beta$; the printed numerator has residual $4\beta$. Verify the sign on the beta term. |
| 071 | “$-\sigma[2\sigma'+\rho]/(\beta\rho)$” | The four-continuant identity gives the numerator $\sigma(\rho-2\sigma_{\mathrm{reverse}})$, so the printed final numerator has residual $-2\sigma\rho$. Verify the rho sign separately. |
| 071 | “$+\rho\beta(a_n+\beta_{n-1}a_{n-1}+\cdots)$” | For the displayed scaled t-vector, the exact increment is $-\rho$ times that tail; the printed residual is $\rho(\beta+1)$ times the tail. Verify both sign and factor. |

The complete [question CSV](enumeration_reading_questions.csv) also locates arity issues, the scan 050 product and L4 expression, scan 051 exponent/comma issues, dual-basis stars, and the scan 078 sign alternatives.

## 7. Documentary extraction and totals

The documentary CSV records source-list entries without resolving people across lists. Representation-pair fields retain the displayed name tokens after separating their leading honorific; the explicit lists in the script determine the row counts. This operation changes no source text.

The juries on scans 060, 062, 064, 068 have 4, 5, 4, 3 entries, totaling 16 occurrences. The three thesis forms have eight labelled fields each. Scan 066 has six dated sessions, 116–121; session 118 has two lettered descriptions, giving seven description units, and session 119 lists six personnel categories. Scan 064 names three ecological indices.

On scan 070 the upper lists have eight representation pairs, ten absent/excused tokens, and four directors. The lower session has three agenda items, twelve present tokens, four representation pairs, and nine literal comma-delimited absence atoms. Replacing the single atom ROUZAUD followed by a TeX line break and BERTRAND by two tokens gives ten; that precise candidate split is recorded without a source edit or person-identity claim.

The 47-row page metadata preserves every manuscript-page marker, including two occurrences of 60 on 061. Documentary metadata preserves the printed 5|3 on 070 alongside manuscript 69, and keeps 066's addressee label 5, Recueil 16, postcode 34060, and session numbers in their printed roles.

**Documentary context:** [README.md](../../context/README.md), “Planning brief” (unnumbered), explicitly requests the enumeration/table catalogue. No numbered documentary-list result matching these items occurs in the supplied LM2 rows or RESULTS_STATE; none has been invented to fill that absence.

