# E.124 — ordinary classes and the coherent three-valuation

The complete next ordinary three-class transition is now evaluated. A nine-prime cubic residue matrix proves that the eight literal ordinary units from E.122, together with \(\zeta_3\), are a basis of the completed ordinary units of \(L_2\). Both inverse matrix products are retained. All these units have zero positive tame character at the unique place over \(53\); reciprocity and the Hasse norm theorem prove that every ordinary \(L_2\) unit is a field norm from \(L_3\).

| Object | Evaluated result |
|---|---|
| \(\operatorname{Cl}(L_2)\{3\}\) | \(C_9^2\oplus C_3\) |
| \(\operatorname{Cl}(L_3)\{3\}\) | \(C_{27}\oplus C_9\oplus C_3\) |
| Lower three-prime | \((6,3,1)\), order \(3\) |
| Upper three-prime | \((21,0,1)\), order \(9\) |
| Ordinary unit norm quotient | \(C_3^2\) |
| Completed ordinary unit norm kernel | \(\mu_3\oplus\mathbb Z_3^{18}\) |

The certificate retains the complete actual norm, extension, prime and S-quotient maps. It checks all 729 upper and 243 lower classes, every norm-lift rule, both trace identities and all finite kernels. Exact ambient rational Smith coordinates, including thirds in the trivial Smith row, are encoded and decoded without truncation. The third ideal is factored into its three actual prime factors; the earlier failed assumption that it was prime is retained.

## All-level result

For the actual order \(3^{a_d}\) of the prime over three, the proof gives \(a_2=1\), \(a_3=2\) and \(a_d\leq a_{d+1}\leq a_d+1\). The norm kernel lies in this fixed prime subgroup, so \((\sigma-1)^2=3(\sigma-1)=0\). The actual trace is exactly multiplication by three.

Kato's theorem is applied to \(L_2(\mu_{3^\infty},53^{1/3^\infty})\), and the coherent system is restricted to the literal \(L_d\) chain. Relative residue degree one preserves the three-valuation. It follows that \(h=\sup a_d\) is finite and at least two. Actual compatible basis choices and inverses give
\[
D_d\simeq C_{3^{a_d+1}}\oplus C_9\oplus C_3,\qquad
\varprojlim_N D_d\simeq C_{3^{h+1}}\oplus C_9\oplus C_3.
\]
The prime is \((3,0,1)\); norms reduce the first coordinate and preserve the other two. Extension is three times any actual norm lift, and the exponent-three kernel proves independence.

The strongly ambiguous subgroup is \(3D_{d+1}+\langle q_{d+1}\rangle\), with index nine. Lemmermeyer Theorem1(2), with **ordinary units**, gives the complete quotient type \(C_3^{\,3-a_{d+1}+a_d}\). Its embedded norm subgroup and Hilbert–90 maps are retained without assigning uncomputed rows on a higher unit basis.

Compact valuation fibres prove both inclusions in the coherent image \(3^h\mathbb Z_3\). A chosen coherent unit of this valuation and the literal tuple \((\beta_d)\) give the continuous product and its displayed inverse. The rational norm is exactly \(3^{3^hk}53^{2t}\). Composing E.123's actual divisor splitting gives the complete positional coordinates stated in the theorem.

The numerical \(h\) and a literal minimal coherent three-unit remain to be evaluated. The next calculation is the ordinary-unit character on the actual \(L_3\) lattice for \(L_4/L_3\). Neither a stationary step nor continued growth is inferred from boundedness.

## Verification

All nine mathematical stages were rebuilt from copied sources and four immutable inputs in a separate tree. Complete stdout, stderr and JSON match byte for byte, with no excluded fields. Both complete PARI objects agree after actual decoding. Their differing raw serialization bytes and the exact comparison are retained. No upper BNF or regulator assumption is used.

All seven rendered pages were viewed as images and are clean; the layout checker reports no overfull boxes. Source evidence distinguishes newly opened complete proofs from prior retained reads. The ordinary-unit Herbrand argument is Milne VII Proposition3.1, read through its final lattice calculation.

The histories retain four real failed approaches: the wrong lower binary structure, Vecsmall JSON serialization, treating a composite ideal as prime, and vector-modulus syntax. Their source, stdout and stderr remain with their exact scope.

## Replay

From this directory, run:

~~~text
python code/e53_ordinary_replay.py --gp /absolute/path/to/gp --label independent_replay
~~~

Use Python with SymPy and PARI/GP 2.19.0, and a fresh label. The replay reconstructs all nine stages and compares every complete output and decoded binary component.

The original E.23 remains open beyond these evaluated maps. This theorem proves no new intrinsic lifting surjectivity from the H quotient.
