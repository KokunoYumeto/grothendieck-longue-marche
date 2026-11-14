# D.51 — exact class-two residual and a further compatible lift

## Actual result

The complete chosen D.50 action and its conjugators extend through a strict additional class-two quotient. No D.50 homology coordinate is replaced.

Write \(q=|A|\), \(m=|G_3|/(6q)\), \(\rho=1+mq\), and \(w=m(q-1)\), using the same actual arithmetic subgroup \(A\) as D.49. The image of the D.50 full-source kernel in the free class-two exponent-four quotient is exactly
\[
 Z=W\wedge V.
\]
The proof upgrades the earlier inclusion to equality before defining any further common quotient.

The canonical odd-\(A\) averaging idempotent splits \(Z=Z_0\oplus Z_-\), with
\[
 \dim Z_0=m^2(q-1)/2,\qquad \dim Z_-=w\rho/2.
\]
Both dimensions are positive. The new finite target is the actual class-two quotient modulo only \(Z_0\). Its exact common quotient with D.50 is \(\mathcal T_2/Z\). The central cusp correction is onto on \(Z_-\), giving the new joint source
\[
 \mathcal Y_h=\mathcal Z_h\times_{\mathcal T_2/Z}(\mathcal T_2/Z_0).
\]
Its projection to the complete D.50 source has kernel \(Z_-\). The action, both full conjugators, normalized parameter, CM pair, full metabelian action and global-sign congruence action are retained through this literal projection.

## Exact residual proof

For the image \(H\) of the fixed-parameter kernel in the full class-two quotient, choose its odd complement \(\widetilde A\). The subgroup \(E=[D,\widetilde A]\) has the moving abelian image. Normality therefore places \(W\wedge V\) in \(E\cap D'\).

For the reverse inclusion, the invariant abelian projection lifts to homomorphisms from the free class-two exponent-four group into the corresponding group on the invariant generators. Their central ambiguity is an affine vector space over \(\mathbb F_2\). Averaging over the odd complement gives an actual invariant surjection. On commutators it is the exterior projection, with kernel exactly \(W\wedge V\).

The proof then establishes \([E,\widetilde A]=E\) inside this group: the moving abelian image supplies \(\bigwedge^2W\), and the remaining \(W\wedge V^A\) summand has no odd invariants. This proves that \(E\) is the exact pronilpotent residual of \(H\). An actual fourth-power adjustment in the original source removes any residual abelian coordinate divisible by four. It gives the exact image of the intersection with the complete homology kernel.

## Descent, generation and compatibility

The D.50 action descends to the common class-two quotient by a characteristic quotient of the image of \(K_3\). Its specified conjugators descend as actual elements.

Lifting those two elements and correcting in \(Z_-\) solves the exact cusp equation. The action on \(V\) is the unchanged \(G_3\)-linear D.50 map, so its exterior action preserves the subgroup \(Z_0\). This proves factorization through the target quotient; it is not omitted in passing from a map of the original source to an endomorphism. The unchanged invertible Frattini map proves generation of the finite two-kernel, and hence an automorphism of the full finite quotient.

The component conjugators agree on the actual common quotient. Their fibre-product pair therefore retains the full D.50 action and parameter. The exact remaining source-kernel image back in the unquotiented class-two target is \(Z_0\), not merely a lower bound.

## Exact finite moving-lift verification

The program code/d_cm_class2_moving.py uses only the Python standard library. Its sole input is the byte-identical frozen D.50 JSON. It rebuilds the actual marked order-1080 group and all 181 free graph-generator words.

The recorded D.50 modulo-sixteen conjugators are retained modulo four. Their moving coordinates lift to commutators with an actual order-three element. The program computes the complete central cusp error, splits its invariant and moving components, and obtains actual central corrections by telescoping the literal odd-deck word into the two cusp columns.

The corrected conjugators have lengths 1,039,508 and 1,040,212 in the \(B\) alphabet. Their 4,159,444-letter cusp word is directly collected in the faithful class-two exponent-four graph model. Its result is exactly the invariant error, hence identity in the specified quotient. Both torsion relations pass. Every old homology matrix column is unchanged, and its rank remains 181. The added central dimension is 10,860 and the exact invariant residual dimension is 3,600.

This calculation is a separate finite verification. The actual enormous \(G_3\) application is established symbolically and does not rely on an unevaluated arithmetic coefficient guess.

## Separate exact nonlifting diagnostic

The program code/d_class2_diagnostic.py also uses only the Python standard library and reads the same input without modifying it. It independently rebuilds the integral ribbon-graph pairing. The order-1080 cover has 36 cusps, genus 73, and compact homology rank 146.

The fixed D.50 finite matrix has pairing-defect rank 72; the first nonzero entry is \((0,6)\). A multiplier-one peripheral action preserves the compact symplectic tensor already in the class-two boundary relation. Hence no choice of conjugators with that same finite homology action can lift it to the unquotiented class-two source. This conclusion applies to the finite verification case only. It does not exclude the actual arithmetic D.50 action.

The diagnostic explains why the invariant residual must remain explicit while the moving part is lifted. The actual arithmetic obstruction in that invariant residual is still unresolved.

## Validation and provenance

Both final programs passed fresh copied-source/input executions. Their complete JSON certificates match the originals after excluding only /summary/elapsed_seconds. The D.50 input remains byte-identical to its frozen source. Control-character, display and environment lint passed.

The initial exploratory pairing calculation and its executed copied D.50 helper remain under raw_trials/initial_pairing with their actual programs, outputs and JSON files. The final diagnostic no longer executes a helper or rewrites any input. Root and the independent peer completed their full-proof audits: PASS. Root also read both final programs, reran copied sources and input, and compared every JSON/stdout field. Only elapsed time differs. The historical author path raw_trials/initial_pairing is archived at code/d51_historical/initial_pairing; its input and actual output are kept separate from the immutable current D50 input.
