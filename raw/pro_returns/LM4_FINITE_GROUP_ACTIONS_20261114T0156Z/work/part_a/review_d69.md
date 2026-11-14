# Independent audit of D.69

**Result: PASS.** I read the full written proof, metadata, its D.53 affine-label input, and the complete exact producer. The independent rerun passed all **134,418** checks. No mathematical correction is required.

## The original quotient and cover

The action on the actual D.68 quotient is identity at the specified negative coordinate. This supplies the literal product quotient \(E/N=D_{2q}\times C_4\), with both inverse coordinate maps, rather than just a quotient up to an unspecified automorphism. The two peripheral cycles have length \(q\), so the index-\(2q\) cover has genus \(q\), two punctures, and free rank \(2q+1\).

For the intermediate type-\((1,2)\) cover, the quotient sends \(u,B,C\) to \(1,r,r^{-1}\). Its graph boundary is the displayed \((0,r-1,r^{-1}-1)\). The two cycle-module maps are actual inverses: the boundary equation is
\[
(r-1)(b-r^{-1}d)=0,
\]
and cyclic coefficient comparison gives the unique multiple \(k\nu\). Hence the two regular modules and one trivial module, and every subsequent rank and deck multiplicity, are integral.

Restriction and transfer identify the deck-invariant summand with the specified intermediate cover. The odd index makes the averaging projector integral over \(\mathbb Z_2\), and the maps are equivariant for the actual quartic representative.

## Integral and residual operators

The cohomology action is explicitly pullback by \(\alpha^{-1}\). Its square is pullback by \(\beta\), since \(\beta^2=1\). This is the correct convention for the mod-four cochain later in the proof.

The unramified splitting ring exists because \(q\) is odd. Every nontrivial deck-character lattice has rank two. Modulo two, \(S^4=1\) makes its operator unipotent, so its square is identity. On the rank-three deck-trivial summand the already proved relation \(S^2=-J\) gives one nonzero rank in \(B-I\); its reduction is a single Jordan block of size three for \(S\), and blocks of sizes two and one for \(B\). Thus the asserted total rank one for \(B-I\) is exact.

## Section classes and normalizers

D.53 supplies three distinct affine section labels. The chosen \(\sigma=s^2\) has zero label and is fixed by \(s\), so the affine translation vanishes. A nonidentity transvection has one fixed line; the two interchanged labels lie outside that line and have nonzero value under the unique fixed dual character. Those two global classes cannot meet either of the indicated kernels.

All conjugates of the remaining section do lie in the smaller extensions because its image in \(D_{2q}\times C_4\) is central. The exact \(N\)-conjugacy relation is the right-coset relation in \(Q/\rho(C)\), since the full \(F\)-normalizer of an order-two section is its fixed subgroup \(C\). The quotient character and the vanishing of \(H^1(C,\mathbb F_2)\) put \(\rho(C)\) in the rotation group, which has prime order.

Conjugation by \(s\) acts trivially on the coset parameter because \(\rho\alpha=\rho\). Thus no additional fusion occurs in the quartic extension. The displayed direct-product and semidirect-product normalizers are the actual intersections with those extensions, with the specified section labels and coordinate inverses. In particular the trivial-image case really has \(2q\) factors in both Brown comparisons.

## Brown restriction and the localized injection

I independently reopened the original primary source:

https://mat.unb.br/~pz/arquivos/Claus3.pdf

Kochloukova--Zalesskii, Theorem 2 and §1.1, printed pp.3–4 of that preprint, state the full profinite dense restriction embedding for a group with an open subgroup of finite \(p\)-cohomological dimension and no \(C_p^2\). The source is not restricted to pro-\(p\) groups in this theorem. The subsequent paragraph explicitly upgrades the dense embedding when the cohomology groups are finite.

Both actual extensions here have the open finitely generated free group \(N\), and every finite subgroup injects into its stated cyclic quotient. The two-row spectral sequences give finite cohomology in every degree. Thus the dense embeddings used here are onto; their maps are restrictions and consequently preserve products. This gives precisely the high-degree product-ring comparison.

Under \(\rho(C)=1\), each fixed group is \(C\). Its positive-degree mod-two cohomology vanishes because it is a closed subgroup of a free profinite group, hence has \(2\)-cohomological dimension at most one, and its first cohomology vanishes by D.46. Localizing at the actual quotient character therefore gives the stated product \(\mathbb F_2^{2q}\).

For \(\theta\in W\), extension with \(\theta(\sigma)=0\) is an actual character. The section makes bottom-row inflation injective in all degrees. All possible differentials of the two-row spectral sequence target that bottom row, and hence vanish. The \(W\)-summand is a direct trivial \(C_2\)-module, so the associated graded class of \(u^m\theta\) is nonzero for every \(m\) whenever \(\theta\ne0\). This proves the injection after localization, rather than merely an injection before possible \(u\)-torsion is killed.

## The mod-four identity and contradiction

Every character in \(W\) lifts from the specified integral lattice. The exact coboundary of \(\varphi(n)\) on \(N\rtimes\langle\sigma\rangle\) is
\[
2\epsilon(D\theta)(m).
\]
The convention \(B=\beta^*\) gives the stated sign \((I-B)/2\). Changing the lift by twice a character changes nothing modulo two because \(B\) is identity there. The Bockstein is the cup square, so \(\theta^2=uD\theta\) is the literal ring identity for those extensions.

Every element of the localized product algebra is idempotent. The already proved \(W\)-injection then forces \(D=I\) modulo two, or \(B=-I\) modulo four on the integral lattice. On each rank-two unramified character block, an identity reduction for \(S\) would force \(S^2=I\) modulo four. Thus each block is a nonidentity unipotent block of size two.

For \(C_4\), the two periodic maps are \(S-I\) and \((S-I)^3\). A size-two block and a size-three block each contribute one dimension in every positive cohomology degree. There are \(q-1\) former blocks and one latter block. The total spectral-sequence bound is therefore \(q+1\), while the actual normalizers and Brown restriction give \(2q\). This is the required contradiction.

## The surviving image and its cohomology

Once \(\rho(C)=C_q\), the coset parameter has two classes, represented by \(1,x\). Intersecting with the square extension gives exactly the two displayed \(C_0\times C_2\) normalizers. The rank-one operator \(B-I\) on the \((2q+1)\)-dimensional first-cohomology module gives positive \(C_2\)-cohomology dimension \(2q-1\); the split two-row sequence consequently gives total dimension \(2q\).

Brown then forces finite \(H^1(C_0,\mathbb F_2)\) and the exact equality
\[
2q=2\bigl(1+\dim H^1(C_0,\mathbb F_2)\bigr).
\]
No identification of \(C_0\) with a full free profinite group is used. The statement concerns \(C_F(s^2)\), and no image assertion for \(C_F(s)\) is inferred.

## Executed certificate

The producer was independently rerun to work/part_a/d69_audit_stdout.txt.

It passed all 134,418 exact checks. I read its dihedral multiplication, peripheral-cycle traversal, integral module inverse, affine label enumeration, Jordan-resolution calculation, and explicit mod-four cochain/cup-square comparison. Its finite models verify the displayed identities and dimension calculations; the full Brown and subgroup arguments supply the theorem.

One optional exposition improvement was sent to C: explicitly insert the finite-cohomology sentence immediately before upgrading the first dense Brown embedding to an isomorphism. The hypotheses and proof already establish it.

## Final written continuation, D.69y–z

**PASS on the final integral continuation as written.** I reread the added subsection in the current source. It uses the already proved full rotation image to choose an actual \(h\in C\) over \(r\). This choice fixes \(\sigma\), and \(h^q\in C_0\) makes the induced cohomology action the finite deck action. Hence the extension of \(W\) by the value zero on \(\sigma\), and its quotient by \(u\), are genuinely equivariant.

The two Brown factors have square-zero augmentation ideals of total dimension \(2(q-1)\). The rotation group fixes both section classes, so it acts identically on the residue algebra \(\mathbb F_2^2\). Averaging kills the composite from the nontrivial deck summand \(W\) to that residue algebra. The previously established injective map \(W/u\) therefore lands in the nilradical, and the equal dimensions make it the entire nilradical.

Its square is zero. The same exact cochain then forces \(D=0\) modulo two and \(B=I\) modulo four. Finally the displayed cancellation in \((I+4L)^2=I\), followed by invertibility of \(I+2L\), proves \(B=I\) on the full integral lattice. The inverse-transpose convention agrees because \(\beta^{-1}=\beta\). No new finite computation is needed for this integral deduction.
