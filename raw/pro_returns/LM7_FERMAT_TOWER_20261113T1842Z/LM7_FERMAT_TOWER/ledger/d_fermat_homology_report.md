# D39: the complete mixed Fermat homology tower

## Proved result and scope

D39 constructs an actual continuous peripheral automorphism, with multiplier exactly one, on

\[
\mathcal T=\widehat B/
\bigl(\overline{[L,L]}\cap\overline{D_9K}\bigr).
\]

Here $L$ is the rank-1153 mixed congruence/Fermat-twelve subgroup of D37 and $K$ is the marked rank-four subgroup of D34. The automorphism gives a single compatible generating family of finite GT0 shadows at all finite homology levels, jointly with the recorded degree-eight quotient $T_3=B/D_9K$.

The normalized $G_6$ and $T_3$ actions agree exactly with D38. Every normalized odd-primary homology component is the identity. Thus the new action explicitly replaces D38's $J_3$ and $J_{12}$ actions, while retaining the fixed-fibre pair $T_4=I,W_3=[i]$. Its actual marked compact matrices are cubic Tate16 $\left(\begin{smallmatrix}3&8\\8&11\end{smallmatrix}\right)$ and quartic Tate3 $I$. The two-cover arithmetic graph and the independently marked fixed-fibre CM obstruction both remain violated.

The full profinite GT0 realization problem is still unresolved. D39 proves an automorphism of this explicitly defined quotient and all of its indicated finite homology refinements. The exact remaining source kernel is the displayed intersection. It contains the already checked nonzero word $[a_1^{12},a_2^{12}]^2$, with a nonzero degree-sixteen mod-two Magnus term. This kernel is part of the next lifting problem, and its nontriviality alone is not a nonlifting theorem.

## Exact common quotient

The maximal common marked quotient of the full homology group and $T_3$ is

\[
C_8=B/([L_4,L_4]D_9K).
\]

It has order $2304\cdot2^{410}=18\cdot2^{417}$, with coefficient kernel $C_8^7\oplus C_4^{62}\oplus C_2^{265}$ over $H_4$. Its canonical map to D38's common quotient has kernel $C_2^7$.

The complete exponent-eight calculation includes the two power terms that vanish at coefficient exponent four:

\[
\operatorname{im}D_9K
=G^{16}+(\gamma_2G)^8+4\gamma_3G+2\gamma_5G+\gamma_9G.
\]

Every one of the 128 base cosets is included in the sixteenth-power calculation, with the norm map on its entire coefficient module. The full derived subgroup is generated and its coefficient intersection is computed before taking eighth powers. The two power spans are $C_2^{327}$ and $C_2^{189}$. The resulting complete image is $C_8^{51}\oplus C_4^{265}\oplus C_2^{62}$. Exact elimination checks all marked generator actions, full $s,r$ stability, and reduction to the preceding exponent-four image.

The common quotient stabilizes at exponent eight because $L_4\subset D_2K$ and $L_4^8\subset D_{16}K\subset D_9K$. The proof gives the maximal-common-quotient maps in both directions through the universal relative pro-two quotient; it does not infer an intersection merely from a comparison of images.

## Integral two-adic and all odd-prime lifts

The actual conjugator constraints and cusp equation form a signed integer matrix of size $2117\times3270$. Its invariant factors over \(\mathbb Z_2\) are

\[
1^{1588},\quad2^{457},\quad4^{64},\quad8^7,\quad16.
\]

All rows have a pivot at precision 256. The proof lifts the elementary operations to \(\mathbb Z_2\), where the resulting square leading block is a unit perturbation of this diagonal. This determines the exact integral invariant factors and proves that the cokernel is killed by 16. Consequently the recorded generating solution modulo 256 lifts to an exact solution retaining its coefficients modulo 16. A constructive lookahead recursion is specified, and two steps are checked against the original signed matrix at moduli 4096 and 65536. The multiplier remains one throughout.

At every odd prime, the selected base action is exactly conjugation by $x^6$. The program verifies this on all 6912 base elements. A canonical lift $c$ of $x^{-6}\beta_H$ is corrected by the actual cycle $-\tfrac12(P_c-sP_c)$. The resulting lift centralizes $s$, so $A=x^6,\beta=x^6c$ gives the exact inner action. This is one formula over \(\mathbb Z[1/2]\), valid simultaneously for every odd prime and every finite coefficient level.

The full homology group is explicitly identified with the product of these prime components over the common finite base $H$. Both conjugators assemble there. Their two-adic common images are exactly the recorded D33 images in $C_8$, giving the joint automorphism with $T_3$. A single global gauge $k=\beta_y^{\rm ab}-\beta_x^{\rm ab}$ puts the common $f$ in the image of \(\widehat F'\). Its odd components are $-6$, and its prime-to-odd order condition is verified, proving that the normalized odd homology actions are the identity.

## Retained finite seed and exact comparisons

The integral lift preserves a literal seed on $J_{48}\times_{C_8}T_3$. Its order is $2^{15771}3^{1156}$. The projection kernels have orders $2^{11151}$ and $2^{4202}3^{1154}$, respectively. Its cusp order is 1152 and $N_{\rm ord}=576$.

The actual checks include:

- The complete 2,676,134-letter cusp word, in all 6912 coefficient coordinates.
- Every one of the 1153 free-kernel basis images, computed independently by substitution.
- Full rank 1153 modulo two, and an explicit inverse for the odd kernel action.
- Both $m=0$ hexagons and the common conjugator equations.
- The exact finite abelianization $(1482,1044)$ and gauge $-438$.
- The normalized $G_6$ comparison with D38, and 4544 changed $J_3$ edge coordinates for each generator.
- The normalized $T_3$ equality: the gauge difference is $336=7\cdot48$, where $48$ is the exact order of $x$ in $T_3$.
- The 390,284-letter normalized $F$ word on all three marked compact covers and both projection maps.
- Nonvanishing of $x^{144}$ in the new seed, witnessing the strict projection to D38's underlying joint group.

All finite refinements retaining this seed have the stated nonarithmetical data. Smaller quotients can have arithmetic identity actions; D39 makes no nonarithmetical assertion about such quotients.

## Portable program order

The five programs use Python 3 and NumPy. Their older input certificates are read from the same code directory, or from the enclosing `LM7_FERMAT_TOWER/code` directory during scratch audits. Run them in this order:

1. `d_cm_fermat_homology_module.py`
2. `d_cm_fermat_homology_image.py`
3. `d_cm_fermat_homology_lift.py`
4. `d_cm_fermat_homology_seed.py`
5. `d_cm_fermat_homology_covers.py`

Each has a nonempty actual `.out` file and an exact `.json` certificate. The expensive first program reconstructs the complete common module. The other programs load it and reconstruct the precise retained D33 words, solve the integral system, check the actual finite words, and evaluate the compact covers. Imports rerun the required predecessor checks; certificate comparisons should omit only `elapsed_seconds` fields recursively.

## Sources and audit status

The mathematical construction is proved directly in `sections/D_fermat_homology.tex`, using the exact marked maps and previously audited calculations of D25 and D33--D38. The finite-shadow terminology uses the already opened primary source `dBDHP2026`, Definitions 2.1 and 2.3. No additional external theorem is used to pass from the finite computation to the integral lift. The Smith perturbation argument, odd averaging, all-prime product map and global gauge are proved explicitly.

The author's five final-name reruns are recorded in the accompanying outputs and execution manifest. Agent A has independently audited the complete mathematical proof and reports PASS. This includes the stabilized common quotient, exact integral Smith-to-limit argument, all-prime gauge, retained/replaced actions and both kernel claims. A does not claim a fresh execution of these five programs. The parent audit is pending. D13 and D19 remain open for the genuine full profinite metabelian-image comparison and the full CM-pair realization problem.

## Root independent audit

The complete proof and all five programs were read. Fresh copied executions of every program passed. The five complete JSON certificates agree recursively after excluding only elapsed_seconds; every mathematical field is identical. The independent A proof audit also passed. The exact audit hashes, fresh standard outputs and the original execution manifest are retained.

## Subsequent exact lifting test

D.45 proves that the entire recorded normalized D39 action and all D40-D44 extensions retaining it have no genuine full profinite GT0 lift. The full retained loop homology forces multiplier1; all112 central and38 complete lower-centralizer columns are annihilated by a four-term degree9 functional that takes value1 on the actual sphere target. The elliptic projection has a literal corrected finite lift. The prescribed CM pair remains open for a replacement action.
