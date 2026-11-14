# Independent D.62 proof, source, and exact-map audit

## Outcome and scope

**PASS.** I read the complete frozen D.62 theorem and proof and all four complete owned program sources. I independently reconstructed the marked finite correction maps from the four frozen arithmetic inputs and verified the two word identities over the integers in a degree-two Magnus algebra. No mathematical or presentation correction is requested.

The frozen proof is D62_EXPERIMENTS/sections/D_self_wedge_actual_corrections.tex, SHA256 e5c0cc61fe2094b339b8fd844bdf0d87593fc4f36cafc4870631b3c8d8afaa8d. The frozen author manifest has SHA256 66a05d0534733dc7f6002488f20b45644fefe10c6adae1ad4168497d0ad3c68c. My program validates every owned-file and immutable-input hash in that manifest.

This audit includes a complete proof/source review and an independently written, actually executed finite-map certificate. It does not claim a second execution of the author's four programs. Root owns that complete copied replay. The author's universal exponent-eight word check proves precisely the displayed word identities in that coefficient model; D.62's arithmetic automorphism is constructed on its displayed exponent-four class-two quotient.

## Actual source preimages and retained comparisons

I reread the exact D.58 source-image proof used in D62.12–13. For an integral vector in \(\mathcal L\), the proof first chooses a preimage in \(\mathfrak R_h\). Its small class-two image is then removed by an actual element of \(R_{50}\), using the proved surjection \(R_{50}\to Z_*\). The resulting element lies in the literal intersection \(S_{57}\), retains the prescribed full homology vector, and is trivial in \(X_*\) and \(\mathcal W_h\). Thus the correction words start with genuine source elements.

I also checked the left-projector identity against D.61. The needed statement is \(eT_{61}=e\). The proof retains the actual complementary term in \(T_{61}e\); it never substitutes a stronger right-projector identity. The left identity gives the exact preservation of the kernels of the selected exterior projectors. The selected projectors annihilate the cusp homology lattice, and compactification is injective on their images.

The source map defined by the two lifted torsion conjugators respects their actual orders and hence is a homomorphism from the original profinite free product. Its cusp error lies in \(\mathcal K\). The D.54 source-kernel identification makes the commutators used in the proof faithful elements of the actual central module \(Z\): their \(\mathcal W_h\) image and full homology image vanish. This supplies the exact passage from the source words to the exterior coordinates.

## The two source words

For the source-involution route, \(b_s=u\widetilde s u\widetilde s^{-1}\) is formed using an actual lift of the conjugating element. The normality of \(S_{57}\) keeps the entire word in that source kernel. Since \(\widetilde s^2=1\),

\[
b_s\widetilde s b_s^{-1}\widetilde s^{-1}
 =[u,\widetilde s u\widetilde s^{-1}]
\]

is an exact group identity. The homology value of \(b_s\) is \(v+sv\), which centralizes the actual involution in \(Y\). The source-\(s\) correction therefore leaves the complete \(Y\)-action and the literal retained conjugators unchanged.

For the cusp route, I derived the identity with the actual wrap \(u_{36}=cuc^{-1}\), \(c=t^{36}\):

\[
[b_t,t]=[u,u_1\cdots u_{35}]\,[c,u]^{-1},
\qquad b_t=u_0u_1\cdots u_{35}.
\]

The retained \(c\)-term has the displayed inverse sign. It vanishes on the selected projector only after applying the proved annihilation of cusp homology. The preceding source identity keeps that term. Its other exterior coordinate is \(v\wedge N_{36}(t)v\).

The actual \(Y\)-image of \(b_t\) is \(N_{36}(t)v\), and the integral action of \(t\) has period dividing 36. This proves that \(b_{t,Y}\) centralizes \(t\). Its image is trivial in \(X_*\) and \(\mathcal W_h\), while its effect on \(Y\) is exactly

\[
\operatorname{Int}(b_{t,Y})\alpha_{61,Y}.
\]

This explicit comparison preserves the claimed original source maps. The final central corrections vanish on \(Y\), so they do not introduce an unrecorded additional change there.

Products of the source corrections add their central error columns. For source-\(s\) corrections, the changed involution differs from the previous one by an element centralizing the kernel. For cusp corrections, the commutator with \(t\) is central in that kernel. These facts justify the finite product construction from the computed binary coefficients.

## Independent finite-map implementation

My check.py imports none of the author's program code. It reads the four frozen marked input certificates and uses dense \(\mathbb F_2\) matrices and polynomial arithmetic in \(\mathbb F_4\). The invariant exterior pair is computed by the direct Hermitian formula

\[
x\wedge y\longmapsto x\overline y^{\,T}+y\overline x^{\,T}.
\]

The complete dual fixed space is obtained by row reduction. Its values on the author's literal quotient representatives give the change to the recorded coinvariant basis. This independently recovers all coinvariant projections and norm columns.

The implementation reconstructs the induced affine matrices from the actual output-coset character. It proves the complete \(s,r,t,N_{36}(t)\) column arrays agree with the retained arrays and verifies \(s^2=r^3=1\), \(t=sr\), the full 36 powers, and the literal affine value

\[
t^{18}=((0,2,1,0),q_{314}).
\]

It also computes the conjugacy-class sizes 36 and 3 for the source-\(s\) and state-314 involutions and proves those classes are disjoint. The profinite source-torsion input is the previously independently opened Herfort–Ribes Theorem A′, with its full proof recorded in the main independent-audit ledger. Consequently the diagnostic state-314 map is not used as an additional source torsion generator.

Every correction column, every retained coordinate block, every diagnostic involution map, and every stated independent-image vector is reproduced. The checker verifies 415,488 full polar identities. It checks both actual factorizations through \(\ker(1+s)\) and \(\ker N_{36}(t)\), as well as containment in the ordinary norm kernel. These factorization checks use the complete dense nullspaces.

The resulting dimensions are:

| Self type | Multiplicity | Coinvariant dimension | Norm rank | Source-\(s\) rank | Cusp rank | Joint rank |
|---|---:|---:|---:|---:|---:|---:|
| Old \((0,0,0,1)\) | 1 | 4 | 2 | 0 | 2 | 2 |
| New \((0,0,1,1)\) | 4 | 3 | 0 | 2 | 1 | 3 |
| New \((0,0,1,2)\) | 4 | 3 | 0 | 2 | 1 | 3 |

The full small coinvariant inverse tables are exhausted. In the old block, the coordinates \(4a+8b\) correspond exactly to correction coefficients \((a+b,b)\). Each new block has the complete eight-entry inverse table. Thus the joint correction image is the entire 26-dimensional norm kernel. The selected module and its coinvariants have dimensions 6656 and 28.

The two word identities are checked separately in the integral rank-37 truncated Magnus algebra, with all signed quadratic tensor coordinates retained. This verifies their universal class-two form before any finite coefficient reduction. Reducing the resulting upper-triangular central coordinates matches every coordinate in the author's exponent-four and exponent-eight word outputs.

## Arithmetic boundary and quotient maps

The exact D.55 compact-orientation identity applies to the actual initial source map. Because \(eT_{61}=e\) and compactification is injective on each selected self block, its projected norm is zero. The computed correction basis therefore removes the actual projected coinvariant error, regardless of its initial coordinates.

The new commutator vectors lie in their single selected self factors. The extra cusp factor is annihilated by every already retained projector. Hence the earlier retained central components keep their zero coinvariant error. The moving component has zero coinvariants by odd averaging. In each retained component the remaining representative is in the actual augmentation image

\[
(1-s)M+s(1-r)M=I_GM,
\]

so central conjugator corrections remove it while preserving the stated lower sources and their conjugators.

The defining class-two laws and the left-projector identities give the quotient map to \(\mathcal T_2/\mathcal J_{62}\). Its invertible Frattini action and identity finite-base action prove it is an automorphism. The simultaneous full-homology and \(\mathcal W_h\) comparison uses the original source-kernel intersection and the same marked common quotient as D.58/D.61. This proves the exact \(X/\mathcal J_{62}\) map, rather than inferring a joint source from separate quotient images.

Finally the orthogonal projectors give the displayed exact kernels. I independently checked

\[
512+8\cdot768=6656,\quad 4+8\cdot3=28,\quad
331776-6656=325120,\quad 562-28=534.
\]

The proved onto map \(R_{50}\to Z\) supplies a genuine source preimage of a nonzero vector in the remaining module. The theorem retains that nonzero source kernel and its unresolved arithmetic boundary explicitly.

## Retained evidence

The independent executable, complete stdout, and complete JSON are a_d62_audit/check.py, check.out, and check.json. The first successful run is preserved under history/initial_dense_check; the final run adds the exhaustive inverse tables and the source-conjugacy-class calculation. Both actual runs exited zero. Exact hashes and audit scope are recorded in audit.json.

No author source or main manuscript file was edited during this audit.
