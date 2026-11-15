# Enumerations and tables: cote 72, scans 035–081

These post-freeze notes use the saved TeX and context text. The complete catalogue is [enumeration_catalogue.csv](enumeration_catalogue.csv), its coverage map has [47 scan rows](enumeration_scan_coverage.csv), and the coordinate maps and proofs are in [computation_conventions.md](computation_conventions.md). Root separately owns the prose condition/case lists, B5, and invariant-subspace scans 080–081.

**Context status:** the exact ID **72-automorphisms-deform-gm-to-ga** in the supplied Hua register is labelled **“conjecture (unsearched) | Lean card: partly proved.”** Each mathematical note below computes the continuant/center parameter connected with that ID; the recorded group-scheme claim is not used as a proved premise.

Every table is reproduced by:

    python3 research/recompute_enumerations.py --max-n 12 --matrix-max-n 5

## E01 — Scans 046–049: determinant permutations

**Kind: proof and exact enumeration.** The source condition “$\sigma(i)\in\{i-1,i,i+1\}$” admits a proved bijection with disjoint adjacent transpositions, giving $\binom{n-p}{p}$ permutations with p pairs; [matching_terms.csv](matching_terms.csv) lists all 609 matchings for orders 0–12, and [matching_counts.csv](matching_counts.csv) gives 49 order/pair-size counts. The totals are 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, with coefficient $(-1)^p2^{n-2p}$ on each distinct squarefree edge monomial. **Context relation:** this supplies the enumerated coefficients of the continuant named in **72-automorphisms-deform-gm-to-ga**.

## E02 — Scans 047 and 049: matching endpoints and gaps

**Kind: computed comparison and reading/math question.** The lower bound “$1\leq p$” on 047 omits the identity term, producing residual -4 at n=2, while 049 starts at0 and says “Attention p=0!”. The exact gap bijection has p+1 nonnegative gaps with sum n-2p, or p gaps with sum at most n-2p; at n=3,p=1, the literal equality with one gap counts one of the two matchings. **Context relation:** questions E-Q047-identity and E-Q047-gap refine the parameter calculation connected with **72-automorphisms-deform-gm-to-ga**, with both frozen source lines retained.

## E03 — Scans 046, 049, 052: determinant recurrences

**Kind: proof and polynomial calculation.** The displayed recurrence “$\Delta_n=2C_0\Delta_{n-1}-C_1^2\Delta_{n-2}$” follows by expansion, and the ring map $C_i\mapsto\prod_{k=0}^{i}B_k$ gives the entrywise identity $\phi(T_n)=D A_n$, hence $\delta_n=(\prod B_k^{n-k})L_n$. [continuant_determinants.csv](continuant_determinants.csv) verifies determinants through order 7 and includes the three low-order source examples and their integral quotients; the unsure recurrence subscript, off-band sketch entry, and quotient-label arity remain questions. **Context relation:** these exact polynomial maps compute the rho parameter connected with **72-automorphisms-deform-gm-to-ga**.

## E04 — Scans 048 and 050: low-degree examples

**Kind: computation with explicit coordinate maps.** “$L_1=2$” begins the verified sequence $L_2=4-B_1$, $L_3=8-2(B_1+B_2)$, $L_4=16-4(B_1+B_2+B_3)+B_1B_3$; the isolated L2 alpha line uses $B_1\mapsto\alpha_0+2$, while L3/L4 use $B_i\mapsto\alpha_i+2$. The final alpha expression for L4 verifies, but its earlier live B-expression has residual $B_1^2+B_2^2+B_3^2-B_3B_4$; the shifted product maps exactly to $(-1)^n\prod B'_i/2^n$, exposing the scalar-only right side at n=1,$B'_1=0$. **Context relation:** [continuant_polynomials.csv](continuant_polynomials.csv) and E-Q050-* add these source comparisons to the continuant connection in **72-automorphisms-deform-gm-to-ga**.

## E05 — Scans 049 and 051: cancellation and parity

**Kind: proof and enumeration.** “Il n'y a pas de cancellation de termes” follows by recovering the edge set from its monomial and recovering C exponents from cumulative B exponents through $a_k=e_k-e_{k+1}$. After the proved integer coefficient operation and reduction to $\mathbb F_2[B]$, the even L polynomial has one surviving monomial and odd order 2m+1 has m+1; [continuant_parity.csv](continuant_parity.csv) and [continuant_delta_parity.csv](continuant_delta_parity.csv) include the four determinant families and their even-order square roots. **Context relation:** these are coefficient/parity results for the continuant in **72-automorphisms-deform-gm-to-ga**; the last-pair exponent and comma on 051 stay named questions.

## E06 — Scans 048, 052, 061, 073: center coordinates

**Kind: proved recurrence and table.** “$\zeta_n=1,\ \zeta_{n-1}=2$” and $\zeta_{i-1}=2\zeta_i-\beta_i\zeta_{i+1}$ give $\zeta_i=L_{n-i}(\beta_{i+1},\ldots,\beta_{n-1})$, including $L_0=1$. [continuant_zeta.csv](continuant_zeta.csv) gives every coordinate for dimensions 1–5, verifies the five completed endpoint expressions on 048 under $\beta_i\mapsto\alpha_i+2$, and catalogues its unfinished zeta-(n-5) line without supplying a manuscript reading. **Context relation:** the center parameter $\rho=\zeta_{-1}$ is the explicit connection to **72-automorphisms-deform-gm-to-ga**.

## E07 — Scans 045–046, 048, 059: pairings and polar matrices

**Kind: exact matrices and specialization.** The four source cases headed “$\mu_i=\lambda_i-1$” give a lower unitriangular N-by-N pairing with N=n+2, occupied-band counts N,N-1,N-2, and $N^2-(3N-3)$ zeros; the reflection map sends $\mu_i$ to -2 and $\beta_i$ to $\alpha_i+2$. [enumeration_matrix_entries.csv](enumeration_matrix_entries.csv), [enumeration_pairing_cases.csv](enumeration_pairing_cases.csv), and [enumeration_matrix_counts.csv](enumeration_matrix_counts.csv) give complete pairing/polar tables for dimensions 1–5. **Context relation:** these matrices supply explicit coordinates for the parameter family named by **72-automorphisms-deform-gm-to-ga**.

## E08 — Scans 057 and 059: determinant sign

**Kind: proved identity and evaluated source question.** The final displayed tridiagonal determinant “$=L_{n+1}=\rho$” has the exact matrix relation $Q^T=-A_{n+1}$, giving $\det Q=(-1)^{n+1}\rho$. At n=2,$\beta_0=\beta_1=1$, the determinant and rho are -4 and 4, so E-Q057-sign records residual -8 and asks for verification of the intended sign convention; the two earlier schematic arrays retain their blanks and indices. **Context relation:** this checks the matrix representative of the continuant connected with **72-automorphisms-deform-gm-to-ga**.

## E09 — Scan 061: dual-basis tables

**Kind: proof and complete coefficient table.** “$a_i^*=a'_{i+1}+2a'_{i+2}+\cdots$” gives $(P^{-1})_{r,c}=L_{r-c}(\beta_c,\ldots,\beta_{r-2})$ for r≥c, with $L_0=1,L_1=2$; multiplication by P proves the formula. [enumeration_dual_basis.csv](enumeration_dual_basis.csv) records both inverse and inverse-transpose tables, 270 entries across dimensions 1–5, while the reversed interval subscript and alternating right-hand stars remain source questions. **Context relation:** these interval coordinates refine the continuant parameter in **72-automorphisms-deform-gm-to-ga**.

## E10 — Scans 048, 053, 061, 075–078: sigma and discriminant maps

**Kind: explicit convention maps and verification questions.** “$f(c')=\sigma$” on 048 equals $-\rho\sigma_{\mathrm{tail}}/2$; the primed sigma on 053/075–078 is the parity-normalized tail, while the primed sigma on 061 is the reverse continuant, related by $d_n\sigma_{\mathrm{normalized}}\sigma_{\mathrm{reverse}}=\beta+\gamma\rho$. The actual Gram determinants are $\det G_E=-M_n\sigma_{\mathrm{tail}}$ and $\det G_V=M_n\rho$, so053's written “$\delta_{\mathcal E}=B\sigma$” is the negative of 046's determinant, an exact sign-convention question. **Context relation:** [computation_conventions.md](computation_conventions.md) proves these coordinate maps for the parameter family of **72-automorphisms-deform-gm-to-ga**.

## E11 — Scans 063, 065, 067: four continuants and inverse numerator

**Kind: proof of polynomial identities.** “$\sigma\sigma'=\beta+\gamma\rho$” is the determinant identity of the explicit product of matrices $\bigl(\begin{smallmatrix}2&-\beta_i\\1&0\end{smallmatrix}\bigr)$ followed by $\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$. The same model proves $\Theta\Psi=\Psi\Theta=\beta\sigma I$ over the integral polynomial ring, and gives the inverse in its stated localization; [enumeration_checks.json](enumeration_checks.json) also checks every entry for dimensions 1–5. **Context relation:** these are new exact identities among the continuants connected with **72-automorphisms-deform-gm-to-ga**, without adopting its verdict or the cancelled draft on 063.

## E12 — Scans 065 and 067: vertex and norm tables

**Kind: proof and complete tables.** “$s_{i+1}=\tau_i s_i$” and the dual sequence give the complete pairing: zero above the diagonal, one on the diagonal, and $\sum_{k=j}^{i-2}(\beta_k-1)$ below it, with the first lower diagonal zero. [enumeration_vectors.csv](enumeration_vectors.csv) and [enumeration_norms.csv](enumeration_norms.csv) reproduce the t coefficients and prove $f(t_{n+1})=\beta\sigma\gamma/2$, $f(s_0+s_1)=-1$, and $f(t_n+t_{n+1})=\beta\sigma(2\gamma-\sigma)$ by exact matrix multiplication and telescoping. **Context relation:** these are coordinate consequences of the parameter associated with **72-automorphisms-deform-gm-to-ga**.

## E13 — Scan 069: dimensions 1 and 2

**Kind: exact examples and evaluated reading question.** The headings “n=1” and “n=2” produce the 19 scalar/coefficient rows in [enumeration_n1_n2.csv](enumeration_n1_n2.csv), with script alpha-zero identified with the source's unindexed alpha in dimension 1 and $\beta_i=\alpha_i+2$. The first frozen coefficient reading $2+\alpha_1^2$ has residual $\alpha_1^2-\alpha_1$ and norm residual $(\alpha_0+2)(\alpha_1^2-\alpha_1)^2$; at alpha=(0, 2), the coefficients are 6/4 and norms 8/0. **Context relation:** E-Q069-first-exponent adds this exact comparison to the continuant connection in **72-automorphisms-deform-gm-to-ga** and retains both frozen readings.

## E14 — Scans 071 and 073: centered coordinates

**Kind: exact maps and literal questions.** “$p_\lambda(x)=x/\lambda-\Pi/\rho$” gives the integral scaled coordinates $S_i=\Pi-\rho s_i$ and increment $-\rho a_{i-1}$, while the dual-image increment follows by substituting the proved t formula. The literal 071 increments/numerators have cleared residuals $-(\rho+1)$, $4\beta$, $-2\sigma\rho$, and $\rho(\beta+1)$ per indicated basis/tail factor; the full quotes and derivations are listed in §6 of [computation_conventions.md](computation_conventions.md), and 073's marked subscripts are checked by argument counts. **Context relation:** E-Q071-* and E-Q073-* refine the center coordinates connected with **72-automorphisms-deform-gm-to-ga**.

## E15 — Scans 075 and 078: centered radii

**Kind: proved identities and parity table.** “$f_V(s'_0)=\rho'\sigma'$” holds with $s'_i=\Pi-\rho s_i$ and parity-normalized primes: all vertex norms are $\rho\sigma/2$, the adjacent sum norm is $2\rho\sigma-\rho^2$, and the difference norm is $\rho^2$. [enumeration_centered_tables.csv](enumeration_centered_tables.csv) reproduces the two parity rows and squared homothety ratio in its explicit localization; the first minus alternative on the later 078 line differs from the displayed sum table by $2\rho(\rho-\sigma)$. **Context relation:** these centered-coordinate formulas connect to **72-automorphisms-deform-gm-to-ga** and make no claim to prove 077's category-equivalence prose.

## E16 — Scans 060, 062, 064, 068: notices and juries

**Kind: literal documentary counts.** “Composition du jury” / “Membres du jury” gives 4, 5, 4, 3 entries, totaling 16 name occurrences; the three thesis forms each have eight labelled fields, and 064 names three ecological indices. [documentary_items.csv](documentary_items.csv), [documentary_totals.csv](documentary_totals.csv), and [documentary_metadata.csv](documentary_metadata.csv) retain notice numbers, dates, times, durations, labels, and spellings without cross-list identity resolution. **Context relation:** the unnumbered “Planning brief” in [context/README.md](../../context/README.md) requests these tables; the supplied LM2 rows and RESULTS_STATE have no matching numbered documentary-list ID.

## E17 — Scan 066: council sessions

**Kind: literal documentary table count.** “Décisions prises au cours des séances” lists six dates, sessions 116–121, with two lettered descriptions for 118 and six personnel categories within 119, giving six session rows and seven description units. [documentary_sessions.csv](documentary_sessions.csv) retains those nested counts, while addressee label 5, Recueil 16, postcode 34060, and manuscript 65 keep their source roles. **Context relation:** the unnumbered README planning brief requests the table inventory; no matching numbered documentary-list result occurs in the supplied context.

## E18 — Scan 070: attendance and line break

**Kind: literal counts and explicit extraction question.** The upper “Etaient représentés” list has eight pairs, the upper absence list ten tokens, and the director list four; the lower “120ème séance” has three agenda items, twelve present tokens, four representation pairs, and nine comma-delimited absence atoms. Replacing the single ROUZAUD–line-break–BERTRAND atom by two tokens gives ten, and [documentary_lists.json](documentary_lists.json) preserves both totals without assigning the upper meeting the lower heading's identity. **Context relation:** the unnumbered README planning brief requests the enumerations; no numbered documentary-list result is present in the supplied context.

## E19 — Scans 035–081: page and printed numbering

**Kind: literal marker inventory.** [enumeration_page_metadata.csv](enumeration_page_metadata.csv) records all 47 scan markers and every manuscript-page occurrence, including manuscript 60 twice on 061. Documentary metadata preserves 070's printed 5|3 alongside manuscript 69 and keeps 066's addressee/recueil/session numbering in its stated roles. **Context relation:** the unnumbered README planning brief requests scan-referenced tables; this metadata count promotes no prior context claim.

## Output limits

[enumeration_checks.json](enumeration_checks.json) states exact bounds and every check, while [enumeration_source_hashes.json](enumeration_source_hashes.json) records the 48 source digests. The separate [reading-question CSV](enumeration_reading_questions.csv) changes no frozen TeX, inventory, doubts, or page records. The early matrix sketches on 057 and the cancelled063 draft are catalogued without filling omitted entries or assigning them the later live formulas.

