# Checks of the principal algebraic tests in the research notes

These are checks of this return’s explicitly labelled calculations, not additional manuscript text or claims of originality. The hypotheses in each numbered note remain part of the conclusion. No frozen transcription file was changed during this review.

## N35: the finite torsion presentation

Work in an abelian category of sheaves where the displayed section calculations may be made locally. A pair satisfies \(u(m)=ng\), and replacing it by \((m+nm',g+u(m'))\) preserves that relation. The map to \(M/nM\) is locally surjective because multiplication by \(n\) on \(G\) is an epimorphism. A pair above zero can be reduced to \((0,g_0)\) with \(ng_0=0\); two such representatives differ by an element \(m'\) with \(nm'=0\), so the assumption \({}_nM=0\) makes the map from \({}_nG\) injective. This proves the exact sequence claimed in the note, independently of an identification with a particular derived Ext convention.

## N52 and N63: restricted hypothesis tests

For the real-field example, the norm of a nonzero complex number is its positive squared modulus, and every positive real number is a norm. The quotient of \(\mathbb R^*\) by this image has two elements; the field Brauer/cohomology comparison is cited separately as P6. This tests only the absolute étale, degree-at-least-two reading.

For the Artin–Schreier example over \(\mathbb F_p\), a geometrically connected proper abelian variety has global functions \(\mathbb F_p\), and Frobenius minus identity is zero there. The first cokernel in the cohomology sequence is therefore \(\mathbb F_p\). Pullback of the base cohomology class is injective because the origin is a section. The test concerns arithmetic cohomology, not the geometric version over an algebraic closure.

## N69: the tensor vanishing

The surjection \({}_nP\twoheadrightarrow P''\) implies \(nP''=0\). For every local pure tensor \(p''\otimes q\), lift \(q\) locally as \(nq'\) using the epimorphism on \(Q\). Then \(p''\otimes q=np''\otimes q'=0\). Local generation proves the sheaf tensor product vanishes; it does not prove the rest of the cancelled categorical argument.

## N74: a nonzero finite-level system with zero limit pairing

Let \(P=\mathbb Z/\ell\) and \(Q=G=\mathbb Q_\ell/\mathbb Z_\ell\). The two-term free resolution of \(P\), tensored with \(Q\), is \([Q\xrightarrow{\ell}Q]\) in degrees \(-1,0\); multiplication by \(\ell\) is onto and has kernel \(\mathbb Z/\ell\). Hence \(P\otimes^LQ\) is quasi-isomorphic to \((\mathbb Z/\ell)[1]\), and its degree-one Ext into \(G\) is \(\operatorname{Hom}(\mathbb Z/\ell,G)\), which is nonzero.

For \(r\geq1\), the map \(\phi_r(x,y/\ell^r)=xy/\ell\bmod\mathbb Z\) is well defined: changing \(x\) by \(\ell\) changes the fraction by an integer, and changing \(y\) by \(\ell^r\) changes it by \(x\ell^{r-1}\). It is bilinear and takes the pair \((1,1/\ell^r)\) to a nonzero element of order \(\ell\). Under the transition from \(r+1\) to \(r\), multiplication by \(\ell\) sends the first argument to zero, while multiplying the value of \(\phi_{r+1}\) by \(\ell\) also gives zero. Thus the simultaneous compatibility holds. The asymmetric identities can also be checked using inclusion on the bounded factor or inclusion \(Q[\ell^r]\hookrightarrow Q[\ell^{r+1}]\), which multiplies the numerator by \(\ell\).

Every inverse-limit element of the \(P\)-system is zero, because its transition maps are zero. The induced pairing of inverse-limit groups is consequently zero. This example concerns information retained in a strict finite-level system; its interpretation in a pro-category requires the separate distinction made in N43 and N73. The calculation by itself is not a proof of the manuscript’s equivalence of biextension categories.

## N76–N79: conditional edge maps and coherence

For N76, the two outer terms in the low-degree local-to-global sequence are the first and second cohomology of the internal Hom sheaf; vanishing of that sheaf forces the edge map to be an isomorphism once the applicable spectral sequence exists. For N77, the zero section splits pullback in degree two, so the image of the Leray transgression is zero; the degree-one sequence then splits by the same section. Neither argument replaces the necessary internal or slice hypotheses by a condition only on global group homomorphisms.

For N79, universal pointed-function rigidity implies the corresponding rigidity on every finite power by holding the other coordinates fixed after base change. A primitive torsor isomorphism normalized at the origin has the required unit normalizations by that rigidity. Its associativity and commutativity defects are normalized maps from the third and second powers into the coefficient group and therefore vanish. Inverses are obtained locally by the torsor law and descend by uniqueness. This checks the stated conditional route; it does not prove the universal rigidity assumption for an arbitrary source group.
