## Continuation to 250 audited statements

This continuation adds C.83 and F.21. Both have complete proofs, independent mathematical reviews and independently rerun exact certificates. The register now has 250 numbered statements: 219 Proved, 3 Known, 25 Refuted and 3 Open. The two additions refine the remaining C.12 and F.7 comparisons. D.12 retains its previously stated equations and partial results. None of these three open rows is closed by the new work.

### C.83: a continuous infinite evaluation loop with no original-disk lift

The example specifies the actual compactification, operator group, transitive commuting group, vertex labels and both topologies. Its plane coordinate is the homeomorphism

\[
j(z)=\frac{z}{1+\lVert z\rVert},\qquad
j^{-1}(w)=\frac{w}{1-\lVert w\rVert}
\]

from the plane to the interior of the original closed unit disk. The operator group is the conjugate through this map of integer horizontal translations. It is closed, discrete, free and proper on the interior. All plane translations extend through this same compactification by the identity on the original circle, and provide the actual transitive commuting subgroup required by C.81. The quantitative extension estimate is

\[
\lVert j(z+v)-j(z)\rVert\le
\frac{2\lVert v\rVert}{1+\lVert z\rVert}.
\]

It controls the maps and their inverses, jointly over compact translation-parameter sets.

The invariant grid has labelled vertices \((k/4,l)\), indexed by a fixed enumeration of \(\mathbb Z^2\). The generator of the operator group acts by the literal label change \((k,l)\mapsto(k+4,l)\). Dividing each rectangle by the same diagonal gives a quotient triangulation. Each closed lifted vertex star has horizontal width \(1/2<1\), so it projects injectively under the unit deck translation. The stars have a common diameter bound in the plane. The displayed radial estimate makes their original-disk diameters tend to zero as the vertices escape, proving the finite-large-star property of C.82 for this exact carrier.

The target is the actual simultaneous evaluation image, with the subspace topology of ordered-coordinate convergence and vague convergence of its counting measures. The evaluation map from the original disk group is continuous: coordinate convergence follows from uniform convergence of maps; for any compactly supported test function, uniform convergence of inverse maps confines all relevant original vertices to one compact interior neighborhood. Thus the test-function sum eventually involves a fixed finite set of labels. This proves continuity of the actual map in both components of the specified target topology.

Put \(b(u)=\max(0,1-4|u|)\). The explicit shear family

\[
F_{n,s}(x,y)=(x+sn\,b(y-n),y),\qquad 0\le s\le1
\]

has inverse with the minus sign and commutes with every integer horizontal translation. For each fixed \(n\), its displacement is bounded by \(n\); the radial estimate therefore gives an actual continuous family of boundary-fixed disk homeomorphisms, including its inverses. Only the grid row \(l=n\) moves.

On the interval \([2^{-n-1},2^{-n}]\), the amplitude rises linearly from zero to one and returns to zero. Concatenate these evaluated paths as the intervals accumulate at zero. Every fixed finite set of labels is eventually fixed. Every compact planar test support eventually misses the moving row and all its images, since the shear preserves the second coordinate. These two exact facts prove continuity of the concatenated loop in the stated evaluation-image topology. Multiplying all amplitudes by \(1-r\), for \(0\le r\le1\), gives an explicit based null-homotopy in that same image; the continuity estimates are uniform in \(r\).

At the peak time \(t_n=3\,2^{-n-2}\), every putative lift must send the vertex \(j(0,n)\) to \(j(n,n)\). Its uniform original-disk displacement is consequently at least

\[
\lVert j(n,n)-j(0,n)\rVert
\ge\frac{n}{1+\sqrt2\,n}>\frac13.
\]

Since \(t_n\to0\), no lift starting at the identity is continuous. The bound applies to every homeomorphism with the required labelled evaluation, regardless of its behavior between vertices. It proves failure of path lifting and hence of the Serre and Hurewicz fibration properties for this exact evaluation map. The target loop is explicitly null-homotopic. No nonzero homotopy class in the original centralizer is claimed.

The certificate `code/part_b/c83_evaluation_path_certificate.py` passes 143 exact symbolic and rational checks. Root and the independent reviewer both read the proof and producer and reran it. The checks verify the radial inverse, shear identities, literal labels, time intervals, row values and displacement formulas. The written proof establishes the infinite continuity and universal nonlifting statements. The original Teh definition on printed pages 5–6 of arXiv:2602.07362v1 was reopened; only its topology definitions are used in C.83.

### F.21: transitivity on the full divisor cosets and normal generation in the joint kernel

F.20 had proved transitivity on its specified finite quotient families. F.21 proves the actual source action transitive on each entire discrete cross-divisor coset space, and then on the corresponding full profinite coset space. It retains all four old labels, both new-point signs and the original chosen source meridians and whiskers.

For each old label \(u\in\mu_5\setminus\{\zeta\}\), the coordinates are

\[
A(s)=\frac{\zeta-s}{\zeta+s},\quad
C_u(s)=\frac{u-s}{u+s},\quad
B=A^2,\quad U=C_u^2,\quad V=\epsilon A.
\]

The argument is based first at the actual selected collision point \(d\) in the filled source \(Y\). At that point \(U=V\), giving a literal common diagonal basepoint. The original source whisker and its image in the configuration space transport every group and forgetting map back to the original basepoint. The selected meridian is retained through these specified transports.

The fourfold square-root cover of \(\mathcal M_{0,5}\) is

\[
W=\{(A,C):A,C\notin\{0,\infty,1,-1\},\ C\ne\pm A\}.
\]

It maps through the intermediate double cover \(W_A\) by \((A,C)\mapsto(A,C^2)\). The actual pencil

\[
\kappa(A,C)=\frac{C-A}{1-AC}
\]

takes values in \(\mathscr B=\mathbb P^1\setminus\{0,1,-1\}\). Removing \(E=\{AC=1\}\) gives a locally trivial bundle over \(\mathscr B\setminus\{\infty\}\). Its fiber is the sphere with the eight specified punctures \(0,\infty,1,-1,-k,-1/k\) and the two roots of \(kA^2+2A+k=0\). Their distinctness, local root choices and disjoint puncture isotopies provide explicit bundle charts.

The old source lies on the fiber \(k_u=(u-\zeta)/(u+\zeta)\). In its original \(s\)-coordinate that entire fiber removes exactly \(0,\infty,\pm\zeta,\pm u,\pm t_u\), where \(t_u^2=\zeta u\). The map from \(Y\) fills the remaining four punctures, so its fundamental-group map onto the fiber image is onto. The divisor \(E\) is connected and smooth, and the derivative of \(1/\kappa\) transverse to it is nonzero. Filling it kills exactly the normal closure of its meridian, whose base image is one meridian of infinity. The resulting actual quotient maps prove

\[
N=\operatorname{im}\bigl(\pi_1(Y,d)\to J=\pi_1(W)\bigr)
 =\ker\bigl(\kappa_*:J\to\pi_1(\mathscr B,k_u)\bigr).
\]

This is a discrete equality; the subsequent proof does not require exactness after completing this pencil-kernel sequence.

The new section of \(W_A\) is \(A\mapsto(A,\epsilon A)\). Its pullback to \(W\) is the connected double cover \(r\mapsto\epsilon r^2\) on the sphere minus \(0,\infty,\pm1,\pm i\), with the literal map \(r\mapsto(\epsilon r^2,r)\). The pencil on this pullback is

\[
f_\epsilon(r)=\frac{r}{r^2+\epsilon r+1}.
\]

Deleting the extra target branch value \(\epsilon/3\) makes it an unramified degree-two cover. The meridian of that value has odd covering monodromy and is killed by the actual target filling. Multiplying a base element by that meridian to the negative of its parity proves that the cover subgroup maps onto the filled-base fundamental group.

Writing \(T=\pi_1(W_A)\) and \(M\) for the new-section subgroup, the precise factorizations are

\[
J=N(M\cap J),\qquad T=NM.
\]

The diagonal right-coset coordinate is \((b_o,b_n)\operatorname{diag}\mapsto b_nb_o^{-1}\), with inverse \(v\mapsto(1,v)\operatorname{diag}\). In this coordinate the actual source acts by \(v\mapsto m(a(n))vn^{-1}\). Factor \(v^{-1}=nm\) in \(T=NM\) and project to the \(A\)-coordinate. This forces \(m=m(a(n))^{-1}\), so \(v\) is the image of the identity under the source action. It proves discrete transitivity. The full completion comparison already proved in F.19–F.20 identifies the full divisor coset with \(\widehat F_3\). The compact source orbit contains the dense discrete orbit and is therefore the whole coset space.

A small oriented normal circle bundle over the regular part of each cross divisor gives actual lifts of its loops that centralize the selected meridian. Its base projection is onto on fundamental groups, its fiber generator is central, and the simple holomorphic source collision identifies that generator with the original positive primitive meridian. Completing this homomorphism gives a compact centralizing image whose projection contains the full divisor subgroup; injectivity of the circle-bundle completion is not required.

Let \(N_D\) be the closed normal closure of \(K^+\) inside \(D^+\). Source transitivity and the centralizer lift factor every ambient element as \(g=dhc\), where \(d\in D^+\), \(h\) lies in the actual drilled source image and \(c\) centralizes the chosen meridian \(\nu\). Hence

\[
g\nu g^{-1}=d(h\nu h^{-1})d^{-1}\in N_D.
\]

The middle conjugate lies in \(K^+\) by its normality in that source image. F.19's eight ambient normal generators therefore all have their conjugates in \(N_D\), proving

\[
\overline{\langle\!\langle K^+\rangle\!\rangle}_{D^+}=D^+.
\]

Passing to the abelianization proves that the actual image of \(K^+\) is the entire \(D^+_{\mathrm{ab}}\). The image is also full in every finite nilpotent quotient: a proper image would lie in a maximal subgroup, and the explicit upper-central-series argument proves that every such maximal subgroup is normal, contradicting normal generation. Compactness then gives the actual surjection onto the maximal pronilpotent quotient of \(D^+\).

The symbolic producer `code/part_a/cross_divisor_geometry_f21.py` passes 95 exact rational and cyclotomic checks, independently rerun by root and the peer reviewer. It checks all four source fibers, the puncture indexing, both collision factorizations, the pencil inverse and reduced divisor derivative, and both degree-two section maps. The bundle, group quotient, orbit, full completion and centralizer arguments are proved in the text. Equality \(K^+=D^+\) remains unresolved.

### Source audit of the two infinite-configuration preprints

Both exact versioned PDFs were opened: arXiv:2512.21498v1 and arXiv:2602.07362v1. The attached source-audit notes give explicit counterexamples to specified statements, together with a rational certificate passing 202 checks. None of these refutations is used to infer failure of configuration-space asphericity.

For the collar assertions, take \(F(t)=\{1-t\}\cup\{10,11,\ldots\}\) on \([0,1/8]\). Every compactly supported test sum is a single continuous term plus a fixed finite sum. The source's one-sided collar supremum is \(3/4\) at zero and \(1-t\) for positive \(t\). This directly contradicts its asserted upper semicontinuity; a continuous strict separator below one is also impossible. The data satisfy the exact hypotheses of the 2025 Lemma 5.10 and the 2026 Lemma 6.7.

For the 2026 Lemma 6.8, move only strand four along the supplied rational lasso around strand one, with winding zero around strand two. Its first three strands stay fixed, so the class lies in the required finite-truncation kernel. The asserted representative would keep the fourth strand outside the radius-two disk while fixing the first two at one and two. Interpolating between these two fixed points gives a nonzero homotopy of pair differences and forces their winding numbers equal, contradicting the retained values one and zero.

An infinite sequence of these finite lassos also refutes the precise Cauchy-realization assertion in Theorem 6.14 and the completeness assertion for the displayed metric in Theorem 6.18. The required compatible finite data demand unequal windings around the first two strands for every later strand. For any actual continuous configuration loop, coordinate and vague continuity force uniform escape of all sufficiently late labels from each compact set. Those late strands then avoid a disk containing both first-strand tracks; their pair windings must agree by the same interpolation. Thus the compatible finite data have no actual realization. This does not decide the existence of another complete metric for the quotient topology.

The complete notes retain each theorem number, printed page, version, exact formula and failed step. C.83 uses only the 2026 topology definitions. No asphericity, infinite normalization, inverse-limit realization or completeness theorem from these preprints is imported.

### Remaining obligations and current validation

C.12 still requires the general admissible-surface level-zero comparison and the controlled deformation of arbitrary original families into the lifted-skeleton stabilizer, together with the stated frontier comparisons. C.83 proves that the specified coordinate-and-vague infinite evaluation map cannot provide an unrestricted path-lifting argument. The existing finite-orbit and fixed-support results retain their exact proved scope.

D.12 retains the distinguished pants equation D.74.40, the torus conjugacy equation D.75.5, the scalar cubic decision and the remaining fixed-group recognition. The accompanying source recheck records the exact Haran and Zalesskii maps inspected and supplies no further recognition theorem.

F.7 retains the original residual source-membership equation. F.21 gives full divisor transitivity, the exact centralizer-image containment, normal generation inside the kernel and all finite nilpotent quotient images. It does not identify \(K^+\) with \(D^+\).

The assembly, final build, overflow counts, actual rendered-page inspection, archive manifest and packaged catalogue rerun are recorded below and in the included verification files after the final build. Mathematical status comes from the written proofs and audits; successful execution alone does not assign that status.

### Exact 250-claim checkpoint verification

The final four-stage LuaLaTeX/BibTeX build produced a 534-page PDF, 3,622,355 bytes, SHA-256 `f3527a4e2e15ba7bfd5c07d5df9a4cc57da97147a3a31168267b8e651ef3432b`. The final log contains zero overfull boxes, missing-glyph warnings, undefined references or citations, and fatal errors. One inherited BibTeX warning records a series number without a volume for Tukia’s 1972 source; its actual Series A I, number 504 metadata was retained.

An initial 7.59178pt overflow on page 521 came from F.21’s four exponent pairs. The same pairs were moved to an unnumbered display. Both the overflowing original and the repaired page were actually viewed. The independent review also found missing spaces in an older bibliography verification note on page 525; that note was repaired without changing its factual content.

The final review covers 64 exact page images. Twenty-six images were proved byte-identical to already inspected images from the preceding checkpoint; root opened 18 additional images, and the independent reviewer opened 20. After the last typography repair, 63 of these images remained byte-identical; root opened and inspected the one changed image, page 525. Every page of C.83 and F.21, all eleven historical overflow passages, the updated C.12 and F.7 overviews and a spread through the six parts are covered. Exact image hashes and the distinction between rendering and inspection are retained in the review records.

The assembled register has 250 numbered claims: 219 Proved, 3 Known, 25 Refuted and 3 Open, with 36 doubtful-reading rows and 77 verified bibliography records (76 cited in the paper, plus the report’s independently checked 2025 source-audit entry). The 39-obligation table remains immediately after INCOMPLETE. Archive manifest validation and the packaged catalogue rerun are recorded in the package verification files.
