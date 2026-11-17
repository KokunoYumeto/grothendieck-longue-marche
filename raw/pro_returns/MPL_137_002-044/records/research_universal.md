# Internal research memo: the universal cochain category and reconstruction

## Scope and evidence

The complete supplied `context/hua_project/137.modern.tex` (1,968 lines) has been read, together with the relevant entry in `context/notes/RESULTS_STATE.md` and the frozen transcription of scans 028–037 and 040–044. No scan image was consulted and no transcription was changed. Below, “scan N, lines …” means `pages/MPL_137_002-044_137_scanNNN.tex`; the line references identify the frozen text, including its uncertainty and deletion markers, and do not resolve the underlying ink.

**Register reconciliation.** **Hua, findings register, `137-perfect-complexes-universal-sigma-exact`** has the supplied status **“conjecture (candidate: their search found no reference) | L…”**, with intake **“new to us: our package for this cote is waiting”** (`RESULTS_STATE.md`, lines 475–479). The excerpt is truncated: the missing text after `L…` must not be supplied from conjecture. The local pages support the additive universal property below; they do not contain the later definition of Σ or the full Σ-exact theorem. The modernised account of those later pages is a contextual lead, not additional manuscript evidence for this package, and neither its claimed Lean verification nor the register’s priority claim has been independently verified here.

## U1. The local universal property is precise and elementary

**Sources:** scans 040, lines 3–19 and 122–154; 041, lines 42–48. **Comparison:** Hua, modernised reading of cote137, **“Le complexe universel / La catégorie engendrée par un complexe”** supports the following interpretation.

For a commutative ground ring \(k\), let \(A\) have objects \(c_i\), \(i\geq0\), with \(A(c_i,c_i)=k1_i\), \(A(c_i,c_{i+1})=kd_i\), all other Hom modules zero, and \(d_{i+1}d_i=0\). Its additive envelope \(K=\operatorname{Add}(A)\), consisting of finite formal sums and matrices of these maps, satisfies

\[
\operatorname{Fun}_{k}(K,B)\simeq\operatorname{Fun}_{k}(A,B)
\simeq\operatorname{Ch}^{\geq0}(B)
\]

for every \(k\)-additive category \(B\). The proof is direct: choose the images of \(c_i,d_i\), extend to finite biproducts and matrices, and extend natural transformations by direct sums. This needs finite biproducts in \(B\), already included in “additive”; it needs neither general kernels nor an abelian or Karoubian target. The resulting uniqueness is categorical, up to the appropriate natural isomorphism. The Hom modules **with their compositions** matter: scan 028, lines 10–12 explicitly notes the omitted composition calculation. Kelly’s general enriched free-completion theorem provides an established framework for this finite-biproduct construction (Kelly, 1982/2005, Theorem 5.35); it is not a reference for the later specific Σ-exact theorem.

## U2. Free modules, projective modules, and “perfect complexes” must stay distinct

**Sources:** scan 040, lines 134–138; scan 041, lines 3–39, an entirely deleted passage containing the ring qualification and “karoubienne”; scan 042, lines 34–41. **Comparison:** Hua, modernised reading of cote137, **“La catégorie engendrée par un complexe”** and **“Les réalisations de \(\mathbb K\)”** adds explanatory completions of the models.

The concrete local \(K\) consists of bounded nonnegative **acyclic** finite-free chain complexes whose cycle modules are also finite free; splitting \(0\to Z_n\to L_n\to Z_{n-1}\to0\) decomposes them into discs. Merely replacing “free cycles” by “projective cycles” can enlarge this category over a general ring. Likewise, an arbitrary finite projective is a summand of a finite free module, not necessarily free (Stacks Project, Lemma 10.78.2, tag 00NX).

The Karoubian qualification needs a ring hypothesis or completion: for \(k=k_1\times k_2\), with \(k_1,k_2\) nonzero fields, multiplication by \(e=(1,0)\) on a disc is an idempotent whose image is the disc on \(ke\), and \(ke\) is not free over \(k\); this idempotent cannot split inside the finite sums of free discs. The cancelled text and margin already record relevant qualifications, so this is a hypothesis check, not a proposed correction. Finally, these are categories of actual complexes and chain maps: passing the acyclic local \(K\) into the derived category sends every object to zero. Thus the register title “perfect complexes” must not be read as asserting this same universal property of the derived category of perfect complexes.

## U3. Ordinary density is stronger than generation by finite sums

**Sources:** scan 029, lines 10–26; scan 030, lines 21–30. **Comparison:** Hua, modernised reading of cote137, **“Reconstruire une catégorie à partir d’une sous-catégorie pleine / Densité”** explicitly repairs the arbitrary-colimit/canonical-colimit conflation, but its next finite-sum sentence must be read as an assertion about the **Ab-enriched** nerve only.

The ordinary restricted Yoneda \(X\mapsto C(-,X)|_A\) is fully faithful when \(A\) is dense, equivalently when the **canonical** diagram \(A/X\to C\) has colimit \(X\). Scan 029 identifies this condition with the existence of some presentation by objects of \(A\); that implication fails. The root-supplied counterexample is already finite: take \(C=\operatorname{Vect}^{\mathrm{fd}}_k\), \(A=\{k\}\), and

\[
h:k^2\to k,\qquad h(x,y)=\begin{cases}x&y=0,\\0&y\ne0.\end{cases}
\]

For every scalar \(\lambda\), \(h(\lambda x,\lambda y)=\lambda h(x,y)\), so \(h\) gives a natural transformation of the **Set-valued** restricted representables, while \(h(1,0)+h(0,1)=1\ne h(1,1)\). Hence that nerve is not full although every object is a finite sum of copies of \(k\). Requiring components to be group homomorphisms, and naturality for the \(k\)-action, removes the counterexample and gives the correct enriched result separately stated on scan 030. Isbell’s original definition uses full faithfulness of precisely the ordinary restricted nerve (Isbell, 1960, p. 541); Kelly treats the enriched criterion explicitly (1982/2005, Theorem 5.1).

## U4. The duality requires codensity as well as density

**Sources:** scans 031–033; scan 034, lines 3–5. **Comparison:** Hua, modernised reading of cote137, **“Reconstruire… / Le cas dual, et une équivalence remarquable”** adds the missing density and codensity hypotheses to its reconstructed proposition.

For \(X\mapsto C(X,-)|_A\), the relevant hypothesis is **codensity**. A colimit indexed by \(\tau\) in \(C\) becomes a limit indexed by \(\tau^{\mathrm{op}}\) in the covariant functor category; the resulting anti-equivalence is between the specified images or closures of representables, not between unrestricted presheaf and copresheaf categories. Finite free left/right module duality is valid without replacing free modules by all modules. A transcription comparison matters here: frozen scan 032, line 27 already prints `\varprojlim`; the modernised reading’s footnote describing a manuscript `\varinjlim` is therefore not corroborated by this frozen representation. This is a difference between supplied readings, with no decision about the ink. The Isbell comparison is mathematically useful but establishes no historical dependence.

## U5. Restriction, tensor pairings, and the abelian margin

**Sources:** scan 034, lines 7–29, especially the “à vérifier” margin; scans 035–036; scan 037, lines 10–14. **Comparison:** Hua, modernised reading of cote137, **“Reconstruire… / Foncteurs sur \(\mathcal C\)”** supports the additive-envelope case and adds the modern end/coend terminology.

Restriction from \(k\)-linear additive functors on \(\operatorname{Add}(A)\) to \(k\)-linear functors on \(A\) is an equivalence for every \(k\)-additive target. The more general claim about selected colimit-preserving functors needs presentations that exhibit density and the relevant preservation conditions; arbitrary objectwise presentations are insufficient. For a finite sum of representables, the pairing written \(F\otimes G\) on scan 035 can be constructed using finite biproducts alone; interpreting the same expression for arbitrary presheaves as a coend introduces additional existence assumptions on the target. Finally, the scan 037 margin “\(C\) abélienne” cannot be imported into the local free-complex argument: if \(C\) is interpreted as bounded finite-free complexes over \(\mathbb Z\), multiplication by 2 on \(\mathbb Z[0]\) is a bimorphism without being an isomorphism, so that category is not abelian. This last observation is conditional on that category identification, not an interpretation of the uncertain surrounding notation.

## U6. Variance and the degree-zero boundary are substantive

**Sources:** scan 041, lines 52–61; scan 042; scan 043, lines 3–23 and 71–98. **Comparison:** Hua, modernised reading of cote137, **“Les réalisations de \(\mathbb K\)”** supplies a corrected chain realisation and a shifted perfect-pairing formula.

The functor \(\alpha^\bullet(x)=(\operatorname{Hom}(x,c_i))_{i\geq0}\) is contravariant in \(x\); its image of \(c_i\) is a cochain disc in degrees \(i,i+1\). The unshifted covariant nerve \(\beta_n(x)=\operatorname{Hom}(c_n,x)\) instead sends \(c_0\) to \(k[0]\), exactly the boundary phenomenon represented on scan 043. A perfect composition pairing compatible with the displayed Hom table is

\[
\operatorname{Hom}(c_n,x)\times\operatorname{Hom}(x,c_{n+1})
\longrightarrow kd_n\simeq k.
\]

Indeed for \(x=c_j\) both factors are \(k\) when \(j=n,n+1\) and zero otherwise; finite sums preserve perfectness. Pairing through the same \(c_n\) in both positions would fail at \(x=c_{n+1}\), where the first factor is \(k\) and the second zero. This explains the mathematical role of the modernised shift, but it does not select a reading of the uncertain indices in frozen Proposition 2 or justify replacing them.

## U7. Proposition 3 represents chain maps, with two different existence arguments

**Source:** scan 044, lines 13–44. **Comparison:** Hua, modernised reading of cote137, **“Les réalisations de \(\mathbb K\)”**, Proposition 3, extends through its following page, outside this package.

The displayed \(\operatorname{Hom}^\bullet_k(K^\bullet,C^\bullet)\) is an **object of \(B\)** representing degree-zero cochain maps, not by this definition a whole differential graded Hom complex or a derived Hom. For bounded finite-free \(K^\bullet\), its candidate is

\[
\ker\left(\prod_i\operatorname{Hom}_k(K^i,C^i)
\xrightarrow{\delta}\prod_i\operatorname{Hom}_k(K^i,C^{i+1})\right),
\quad (\delta u)^i=d_Cu^i-u^{i+1}d_K.
\]

The products are finite, the component cotensors exist by finite biproducts, and the indicated kernel suffices. For finitely presented \(K^i\), cotensors can instead be constructed as kernels from finite presentations; this alone does not supply arbitrary tensor objects \(b\otimes_kK^i\). Unbounded \(K\) introduces potentially infinite products: the final frozen line ends “et les deux”, so the missing continuation cannot be asserted to be absent from the original argument.

For the special \(K^\bullet=\alpha^\bullet(x)\), no general kernel hypothesis on \(B\) is necessary: \(x\) is a finite sum of discs, a map from the cochain disc tensored with \(b\) into \(C^\bullet\) is determined by one map \(b\to C^i\), and finite sums give the representing object \(F_C(x)\). Thus the local universal property proves this special representability even when arbitrary kernels fail to exist.

## U8. The later Σ-left-exact theorem has a different domain and hypotheses

**Context only:** Hua, modernised reading of cote137, **“Classes de suites exactes et propriété universelle / Les définitions”** and **“Le théorème”**; register `137-perfect-complexes-universal-sigma-exact`, status as quoted above.

The later \(P\) includes bounded **nonnegative** finite-free complexes, including spheres and nonacyclic complexes, and Σ consists of degreewise-split short exact sequences. For a \(k\)-additive target with kernels, the same finite-product/kernel formula constructs an extension, and restriction identifies Σ-left-exact functors with nonnegative cochain complexes; full faithfulness can be checked using the functorial sequences \(0\to L\to\operatorname{Cone}(1_L)\to L[1]\to0\), followed by the analogous sequence for \(L[1]\), whose cone terms are sums of discs. The nonnegative restriction is essential: on complexes in arbitrary integer degrees, \(L\mapsto L_{-1}\) is a nonzero degreewise-exact additive functor vanishing on every disc \(c_i\), \(i\geq0\). Thus the register’s abbreviated “bounded” cannot be expanded silently to all integer degrees. The modernised footnotes claim Lean checks of a specified nonnegative, ordinary-kernel version and explicitly exclude the general target-Σ formulation and part (b); no Lean source or proof was inspected in this assignment.

## U9. A conditional counterexample to the weak target-Σ formulation

**Context only; independent mathematical check.** Hua, modernised reading of cote137, **“Classes de suites exactes et propriété universelle / Les définitions”** lists only Sex1–Sex2, then **“Le théorème”**, part (b), identifies Σ-preserving functors with Σ-resolutions. Taken with **only** those weak target axioms, that conclusion fails; this is not a claim about the unseen manuscript or a theorem with stronger exact-category axioms.

Let \(B\) be bounded nonnegative finite-free \(\mathbb Z\)-complexes, and let \(E\) consist of sequences isomorphic to finite direct sums of split sequences and the elementary sequences \(0\to S_i\to D_i\to S_{i+1}\to0\), where \(S_i=\mathbb Z[i]\). This \(B\) is Karoubian, and \(E\) satisfies Sex1–Sex2; the universal disc complex is an \(E\)-resolution of \(S_0\). Yet

\[
0\longrightarrow S_0\longrightarrow
[\mathbb Z\xrightarrow{2}\mathbb Z]
\longrightarrow S_1\longrightarrow0
\]

is degreewise split and is not in \(E\): with these two rank-one endpoints, a sequence in \(E\) has middle term either \(D_0\) or \(S_0\oplus S_1\), whose homology distinguishes it from the displayed middle term. Consequently the identity functor does not preserve Σ into \(E\). Nor can another Σ-preserving extension have the same disc cochain complex, including its differentials: such an extension is ordinarily Σ-left-exact, and the two-step cone-kernel reconstruction in U8 forces it to be naturally isomorphic to the identity. Additional closure or admissibility assumptions on the target exact structure are therefore material to any proposed version of (b). In particular this example does not satisfy the stronger condition that every morphism have an E-admissible kernel: the projection of the displayed middle complex onto S₁ has the forbidden kernel inclusion. The counterexample therefore concerns part (b) under the weak prefatory axioms alone, not a version incorporating that extra condition from the equivalence clause of (a).

## U10. The earlier augmentation convention admits a consistent boundary case

**Additional parent-requested check:** frozen scan 023, its acyclicity axiom, Hom table, \(\Psi^0\simeq\Phi^0\), and the explicit \(i=j=0\) exception in \(\operatorname{Hom}(\Psi^i,\Phi^j)\); compare scan 037, lines 31–32. **Comparison:** Hua, modernised reading of cote137, **“L’axiomatisation (pages 22 à 27)”** rejects \(\Psi^0\simeq\Phi^0\) as contradicting acyclicity after applying a uniform reindexing. That rejection is not forced.

The parent’s alternative model is internally consistent: put \(\Phi^0=S_0=k[0]\), \(\Phi^i=D_{i-1}\) for \(i\geq1\), and use the exact cochain sequence \(0\to S_0\to D_0\to D_1\to\cdots\) in the abelian category of chain complexes. It has the displayed identity/adjacent-arrow Hom table, and \(\Psi^i=\ker(\Phi^{i+1}\to\Phi^{i+2})=\ker(D_i\to D_{i+1})=S_i\), so \(\Psi^0=\Phi^0\). Moreover, \(\operatorname{Hom}(S_i,\Phi^j)\) is \(k\) for \(j=i+1\) and also for \(i=j=0\), exactly the exceptional case explicitly retained in the frozen table. Thus this is a high-confidence consistency check and a counterexample to the alleged necessary contradiction; it remains an alternative mathematical interpretation, not a resolution of ink or proof of all other axioms.

## Primary reference checks

These are background identifications, not a priority search for the later theorem. No claim that Grothendieck knew a particular reference is made.

- Isbell, J. R. (1960). Adequate subcategories. *Illinois Journal of Mathematics, 4*, 541–552. https://doi.org/10.1215/ijm/1255456274 . The original paper’s definition on p. 541 was checked in the [available reproduction](https://conceptualmathematics.wordpress.com/wp-content/uploads/2013/05/adequatesubcategories.pdf).
- Kelly, G. M. (2005). *Basic concepts of enriched category theory*. *Reprints in Theory and Applications of Categories, 10*, 1–136. (Original work published 1982.) https://tac.mta.ca/tac/reprints/articles/10/tr10.pdf . Theorems 5.1 and 5.35 were checked; they distinguish enriched density and free completion from arbitrary generation.
- The Stacks Project Authors. (2026). Finite projective modules, Lemma 10.78.2, tag 00NX. *The Stacks Project*. https://stacks.math.columbia.edu/tag/00NX . The finite-projective/direct-summand equivalence was checked.

The parent should open any external source itself before citing its web reference identifier in a user-facing answer. All original counterexamples and deductions above are supplied with their short proofs and are separate from the supplied modernised reading.
