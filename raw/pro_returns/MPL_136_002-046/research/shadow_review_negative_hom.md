# Independent research check of negative_hom_appendix.md, section D

**Scope:** mathematical review after the transcription freeze; no image inspection, OCR, transcription changes, or uploads. Sources read: the appendix sections A–E, frozen scans043 and045 (with the intervening supplied page files), and the already read no-carry argument in frozen scans020–034. This review concerns the literal intersection target, not a new assertion that it is the maximal divisible submodule.

## Verdict

The argument in section D is valid under its stated hypotheses: $k$ commutative unital, $S=\Gamma_k(T)$, $d>0$, $\alpha\geq d$, and an actual degree-$-d$ $S$-linear map from $\tau_\alpha(M\otimes_kS)$ into $N\otimes_kS$. No additional finite-generation or flatness hypothesis on $M$ or $N$ is needed.

## Steps checked

1. **Restriction and localization:** fixing an actual $m\in M$ gives the $S$-linear map $a\mapsto m\otimes a$ on $\tau_\alpha S$; this map need not be injective. Localization of this actual composite is legitimate and does not claim that localization commutes with an infinite Hom group.

2. **Necessary recurrence:** for $p^r\geq\alpha$ and $p^r>d$, the relation $T_s^{p-1}T_s=p\nu'_sT_{s+1}$ holds for every actual map, regardless of whether the relation list presents the ideal. If $B_s$ is the digit monomial basis vector of degree $p^s-d$, then $B_{s+1}=B_sT_s^{p-1}$; thus the coefficient recurrence is exactly $\xi_s=p\nu'_s\xi_{s+1}$. Each $B_s$ differs from the divided-power basis vector by a unit of $\mathbb Z_{(p)}$, so passage between the two coefficient descriptions preserves membership in a $p$-divisible submodule.

3. **Coherent roots:** the normalization in section B is correct: $a_{s+1}=a_s\nu'_s$ makes $y_s=a_s\xi_s$ satisfy $y_s=py_{s+1}$. Their $k_{(p)}$-span is $p$-divisible, and multiplication or division by any $p$-local unit preserves that property.

4. **High-tail generation:** a digit monomial of weight at least $p^r$ has a nonzero exponent at some index $s\geq r$, so it is divisible by $T_s$ in the digit-monomial basis. This uses generation only, avoiding the missing cross-generator relations identified in section C. Since the maximal $p$-divisible submodule is a $k_{(p)}$-submodule, arbitrary coefficient factors and finite sums preserve it.

5. **Lowering to every remaining degree:** for fixed $j\geq\alpha$, one can choose $t$ so large that $\ell=p^t-1-(j-d)\geq0$ and $j+\ell=p^t-1+d\geq p^r$. The $S$-linearity relation is correctly oriented as $c_{\ell,j-d}b_j=c_{\ell,j}b_{j+\ell}$; its left coefficient is a unit by the no-carry criterion. The right coefficient need not be a unit, because it only multiplies an element already in the divisible submodule.

6. **Global intersection:** for each positive integer $n$, the coefficient class in $N/nN$ vanishes after localization at every integer prime; localization is exact and detects zero elements of abelian groups. Hence $b_j\in nN$ for every $n$, giving the stated coefficientwise inclusion in $N_\infty=\bigcap_n nN$. Finally $S$ is free over $k$, so $N_\infty\otimes_kS\hookrightarrow N\otimes_kS$ is injective and the image condition yields a unique $S$-linear factorization.

## Limits retained

The proof does not identify $\bigcap_n nN$ with the largest divisible submodule. Its final caution about that possible strengthening is therefore appropriate. The section E torsion-ring consequence is also valid: a unital torsion ring has a single positive integer killing its unit and therefore all of its modules, forcing the literal intersection to vanish.
