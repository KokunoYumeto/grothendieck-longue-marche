# Final research-note review: N48–N68

Reviewed `records/research_note_manifest.json` against the frozen per-page LaTeX and the supplied context. No scan image was inspected and no transcription or final-note file was changed. The following are concrete wording/locator corrections and verified findings only.

## Corrections and precision fixes

1. **N66 title:** replace “An elementary example separates the two induced filtrations” with **“An elementary example separates the two filtrations on R.”** The source expressly calls $R'_k=R\cap N'_k$ induced, whereas $R''_k$ is constructed by the displayed sum; they are not both induced from $N'$.
2. **N66 example:** the calculation is correct. For maximum specificity, include $M=k$ in the exact-sequence data and write the quotient as **$R'_1/R''_1\cong k$**, rather than the less explicit “with quotient $k$.”
3. **N63 example:** the counterexample is correct as stated. Making the coefficient category **$k$-vector spaces, with $k$ a field and $F'=F$**, explicit removes any possible ambiguity about the target object or categorical setting without changing the proof.
4. **Composite register references:** in N48, N59 and N68, the shorthand `MPL_33_098-146 §1/§65` denotes two entries; for exact identifiers write **MPL_33_098-146 §1** and **MPL_33_098-146 §65** separately. Likewise N61's `MPL_33_098-146 N08/N25` should be expanded to **MPL_33_098-146 N08** and **MPL_33_098-146 N25** if the final notes promise exact register IDs.
5. **N61 contextual scan precision:** the exact prior locations are **N43: scans 111, 109, 107, 105, 103, 101** and **N45: scans 107, 115, 113**, rather than the broad combined range “101–115.” N08 is **108,112**; N25 is **126–132** as the prior note itself labels it.
6. **N65 title precision:** “without a separation hypothesis” is the literal scope of the source. A title such as **“The cancelled sheet leaves the arbitrary-n implication without separation open”** avoids letting “nonseparated” suggest a claim about schemes; the undefined b)/c) conditions are not recovered from this leaf. The body already preserves this limitation correctly.

## Verified mathematical and contextual points

- **N49, rank one:** the source's $(\ell\geq1)$ and $\|\alpha_1\|^2=2$ make the $ell=1$ substitution decisive. The internal inconsistency is correctly recorded without a transcription emendation.
- **N50, partial continuation:** scan 013 expressly concludes irreducibility for type A, scan 027 concludes reducedness/rank 6 and irreducibility for $E_6$, and scan 031 does so for $E_7$. It is correct to report partial completion of scan 019's deferred verification rather than claiming either no verification or all cases verified.
- **N52, immediate completion:** scan 023's order-three quotient computation follows “qu'il reste à calculer” in the same paragraph. The comparison with prior **N27, scans 132,134**, is accurate as a reporting analogy; it does not identify the mathematics.
- **N53, E6:** the literal factor 13 conflicts with $51840\bmod13=9$. No outside root table is used.
- **N54, B2:** $u=(1,-1)$, $v=(0,1)$ give $n(u,v)=-1$, squared length ratio $1/2$, and $s_us_v=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ of order 4. This is an irreducible example, so adding irreducibility alone would not resolve the ordered-pair sentence.
- **N55, reducible scope:** the independently scaled two-component example is valid. The important caveat about scan 033 is also correct: once the source's global weight function exists, it records relative component scales, and a single rescaling factor is not itself a counterexample.
- **N56–N57, E8:** scan 049 has both literal $\mathrm R^8$ and $V=\mathrm R^4$. Separately, scan 037 gives $2\omega_8-\omega_7=\alpha_8=\varepsilon_7-\varepsilon_6$; with the source's orthonormal convention on 019 and highest root $\varepsilon_7+\varepsilon_8$, the pairing is $+1$. The manuscript's $-1$ remains frozen.
- **N58, prior locator:** prior **N33** indeed lists scans **138–142**, with individual source locators on 138,140,142. Its uncertainty concerns interval letters and an ordinary tensor, so the stated difference from the E7 readings is accurate.
- **N60:** the final formal-group arrow is dashed and qualified by finite dimension of $G$ **or** openness of $J$; the note preserves both alternatives.
- **N62:** for $x\in U\setminus V$, the stated $\widetilde p_{xV}$ is not one of the projections supplied by the product over $V$. This is distinct from the Hom problem.
- **N63, Sierpiński calculation:** the constant sheaf has stalks $F_a=F_b=k$. The restriction square commutes because the second coordinate of $(t,0)$ is zero; the extraction at $a$ applies the map to the diagonal $(x,x)$ and obtains $x$, while the extraction at $b$ is zero. Reconstruction is therefore $(s,t)\mapsto(s,0)$, different from the original map, exactly as stated. The caveat about unseen restrictions on $X$ is appropriate.
- **N64:** the source's “complete,” “enough small objects,” and “right perfect” hypotheses are preserved; the note does not overextend the $P_X$ counterexample into a refutation of every reflector consequence.
- **N65–N66:** the explicit arbitrary-$n$ unknown and the failure of c)$\Rightarrow$b) even at $n=1$ belong to the cancelled typescript. The filtration example gives $R'_1=tA$, $R''_1=t^2A$, quotient $k$, without addressing those absent b)/c) definitions.
- **N68:** scan 021's classification theorem explicitly says **“réduit irréductible.”** The preceding deferred ambiguity statement should retain the note's warning to recover its intended scope; for reducible products, a blanket at-most-two assertion would require separate examination.
- Prior **N46** has scans **105,109,111,131,135,139,143**; **N50–N51** have scan **135**; **N54/N55/S14** have scan **145**; **N18** has scan **120**; **N31** has scans **138,140**; **N06** has scan **106**. These comparisons are correctly identified as different objects or methodological parallels, not prior proofs of the new examples.
- All directly relevant same-cote register entries are first-pass research leads, not reviewed results. No cited local-algebra example changes the statuses of LM4/LM7 items.

## Reused-sheet headings and pagination extracted from the frozen text

This table extracts exact words and numbers from the frozen transcription; it is not an independent image-reading pass. “Upper source number” keeps source pagination separate from the package's small foliation. In the frozen files, the upper numbers on 041/043/045 and IV-1007 on 047 use `\mspage`; their printed/handwritten physical status was not independently reassessed here. No authorship is inferred from the common `n° 391` label or from subject familiarity.

| Scan | Upper source number | Other source identifier | Small package folio | Exact observed title/heading, or continuation status |
|---|---|---|---|---|
| 005 | `- 180 -` | `n° 391` | 4 | No section title; `COROLLAIRE 4.-` and `LEMME 2.-` are statement labels. |
| 007 | `- 179 -` | `n° 391` | 6 | No section title; `LEMME 1.-`, `COROLLAIRE 1.-`, `COROLLAIRE 2.-`, `COROLLAIRE 3.-`. |
| 009 | `- 22 -` | `Tribu n° 62` | 8 | **`Variétés de groupe`**. |
| 011 | `- 137 -` | `n° 391` | 10 | No section title; `COROLLAIRE.-`, beginning `Si les conditions de la prop. 1 sont vérifiées`. |
| 013 | `- 194 -` | `n° 391` | 12 | **`5. Systèmes de type` $A_\ell$, $(\ell\geq1)$.** |
| 015 | `- 193 -` | `n° 391` | 14 | No section title; enumerated data `(I)`–`(XI)` and the definition of `schéma de Dynkin complété`. |
| 017 | `- 192 -` | `n° 391` | 16 | No section title; lattice items `2)`, `3)`, `4)`; item 4 explicitly assumes $n$ `multiple de` 4. |
| 019 | `- 191 -` | `n° 391` | 18 | No section title; lattice-shell argument and item `1) Le réseau` $L_{o\mid0}$. |
| 021 | `- 189 -` | `n° 391` | 20 | No subject title; **`THEOREME 2.- Si` $R$ `est un système de racines réduit irréductible`**; drawings labelled $A_\ell$, $B_\ell$, $C_\ell$, $D_\ell$, $E_6$. |
| 023 | `- 218 -` | `n° 391` | 22 | No type heading on this leaf; `(VII)`, `(VIII)`, `(IX) et (X).` |
| 025 | `- 217 -` | `n° 391` | 24 | No type heading on this leaf; continuation `(IV)`–`(VI)`. |
| 027 | `- 216 -` | `n° 391` | 26 | **`12. Système de type` $E_6$.** It follows the preceding type's `(X)`–`(XI)`. |
| 029 | `- 214 -` | `n° 391` | 28 | No type heading on this leaf; continuation of highest-root calculation, then `(V)`–`(VI)`. |
| 031 | `- 213 -` | `n° 391` | 30 | **`11. Système de type` $E_7$.** |
| 033 | `- 188 -` | `n° 391` | 32 | No section title; `PROPOSITION 2.-` and `COROLLAIRE.-`; Proposition 2 says `un système réduit de racines`, without adding “irréductible” on this leaf. |
| 035 | `- 187 -` | `n° 391` | 34 | No section title; definition of `schéma de Dynkin`; the initial full paragraph says `un système de racines réduit de rang` $\ell$, without “irréductible” there. |
| 037 | `- 212 -` | `n° 391` | 36 | No $E_8$ section heading on this leaf; weight continuation, then `(VII)`–`(XI)`. |
| 039 | `40` | None stated | 38 | No section title; `Proof:`. |
| 041 | `34` | None stated | 40 | No section title; `a)` and `b)` define stalks and $P_X$. |
| 043 | `38` | None stated | 42 | No section title; continuation and `ii)`, `iii)`, `iv)`. |
| 045 | `39` | None stated | 44 | **`1.4 Theorem:`**; later **`Remarks:`**. |
| 047 | `- IV-1007 -` | None stated | 46 | **`19.6. Suites régulières relativement à un module`** with deleted **`quotient`**, inserted **`filtré`**; the whole typed sheet is inside an outer deletion. Also `(19.6.1)`, `(19.6.1.1)`, `(19.6.2)`. |
| 049 | `- 211 -` | `n° 391` | 48 | No $E_8$ section heading on this leaf; `(III)`–`(VI)`. |

### Counts and hypotheses that should not become page totals

- Scan 015 says **“Pour chacun des 9 types de schémas de Dynkin”** and **“planches II à X.”** Nine types and a plate range are not a stated length of this manuscript.
- Scan 017 says **“dans chacun des 8 n\textsuperscript{os} suivants”** and **“8 types … autres que $G_2$.”** These are numbered subdivisions/types, not eight pages.
- Scan 021's displayed restrictions are **$A_\ell$: $(\ell\geq1\ \mathrm{sommets})$; $B_\ell$: $(\ell\geq2\ \mathrm{sommets})$; $C_\ell$: $(\ell\geq3\ \mathrm{sommets})$; $D_\ell$: $(\ell\geq4\ \mathrm{sommets})$**. These are rank/vertex restrictions, not sheet counts.
- Scan 009's `P. 3-13`, `P. 3-14`, and `P. 3-15 à 3-19` are editorial references to other pages; the number 22 is the surviving source page's own pagination.
- None of these reused sheets states a total such as “19 pages” or “Pages 1–67.” Their visible page numbers must not be reported as total lengths.
